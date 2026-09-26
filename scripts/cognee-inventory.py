"""Read-only Cognee dataset inventory — the curation instrument.

Why this exists: curating memory means measuring it first, and Cognee 1.4.0 already
ships the instrument (``cognee.datasets.list_datasets`` / ``get_status`` / ``list_data``).
This script wraps it read-only; it never deletes, prunes, or writes.

**Env discipline (important).** Importing ``cognee`` before applying
``config/cognee.env`` inspects a *different system*: the default posture is
``authentication=required, multi_tenant=enabled`` and ``SYSTEM_ROOT_DIRECTORY`` falls
back to ``site-packages\\cognee\\.cognee_system``. That mistake was made once on
2026-09-26 and produced a phantom "auth is wrong" finding. So: ``load_cognee_env()``
FIRST, ``import cognee`` SECOND — always.

Usage::

    .\\venv\\Scripts\\python.exe scripts\\cognee-inventory.py            # table
    .\\venv\\Scripts\\python.exe scripts\\cognee-inventory.py --json out.json
    .\\venv\\Scripts\\python.exe scripts\\cognee-inventory.py --with-data
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# ``dataset:sha256`` keys written by pipeline/ingest_files.py — a cheap cross-check of
# what the ingester *believes* it stored, independent of what Cognee reports.
CONTENT_INDEX = Path(os.environ.get("LOCALAPPDATA", "")) / "EMPIRE" / "memory-jobs" / "content-index.json"


def _apply_env() -> None:
    """Canonical env FIRST (see module docstring)."""
    from pipeline.cognee_client import load_cognee_env

    load_cognee_env()


def _content_index_summary() -> dict:
    if not CONTENT_INDEX.exists():
        return {}
    try:
        payload = json.loads(CONTENT_INDEX.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 — the instrument must never fail on this
        return {"error": f"{type(exc).__name__}: {exc}"}

    counts: dict[str, int] = {}
    for key in payload:
        dataset = str(key).rsplit(":", 1)[0] if ":" in str(key) else "(unkeyed)"
        counts[dataset] = counts.get(dataset, 0) + 1
    return {
        "path": str(CONTENT_INDEX),
        "total_keys": len(payload),
        "per_dataset": dict(sorted(counts.items(), key=lambda kv: -kv[1])),
    }


async def _collect(with_data: bool) -> dict:
    import cognee

    datasets = await cognee.datasets.list_datasets()
    rows: list[dict] = []
    for ds in datasets:
        ds_id = str(getattr(ds, "id", "") or "")
        row: dict = {
            "id": ds_id,
            "name": getattr(ds, "name", "") or "",
            "created_at": str(getattr(ds, "created_at", "") or ""),
        }
        try:
            row["status"] = await cognee.datasets.get_status([uuid.UUID(ds_id)])
        except Exception as exc:  # noqa: BLE001
            row["status_error"] = f"{type(exc).__name__}: {exc}"
        if with_data:
            try:
                data = await cognee.datasets.list_data(uuid.UUID(ds_id))
                row["data_items"] = len(data)
            except Exception as exc:  # noqa: BLE001
                row["data_error"] = f"{type(exc).__name__}: {exc}"
        rows.append(row)

    return {
        "cognee_version": getattr(cognee, "__version__", "unknown"),
        "system_root": os.environ.get("SYSTEM_ROOT_DIRECTORY", ""),
        "access_control": os.environ.get("ENABLE_BACKEND_ACCESS_CONTROL", "(unset)"),
        "db_provider": os.environ.get("DB_PROVIDER", ""),
        "vector_provider": os.environ.get("VECTOR_DB_PROVIDER", ""),
        "graph_provider": os.environ.get("GRAPH_DATABASE_PROVIDER", ""),
        "dataset_count": len(rows),
        "datasets": rows,
        "content_index": _content_index_summary(),
    }


def _render(report: dict) -> None:
    print(f"cognee {report['cognee_version']}  |  root={report['system_root']}")
    print(
        f"access_control={report['access_control']}  db={report['db_provider']}  "
        f"vector={report['vector_provider']}  graph={report['graph_provider']}"
    )
    print(f"\n{report['dataset_count']} dataset(s):")
    for row in report["datasets"]:
        status = row.get("status") or row.get("status_error", "")
        if isinstance(status, dict):
            status = json.dumps(status, default=str)[:150]
        extra = f" data={row['data_items']}" if "data_items" in row else ""
        print(f"  - {row['name']:<24} {row['id'][:8]}  created={row['created_at'][:19]}{extra}")
        print(f"      status={status}")

    ci = report.get("content_index") or {}
    if ci:
        print(f"\ncontent-index ({ci.get('total_keys', 0)} keys) at {ci.get('path')}:")
        for name, count in list((ci.get("per_dataset") or {}).items())[:40]:
            print(f"  - {name:<24} {count}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Cognee dataset inventory.")
    parser.add_argument("--json", dest="json_path", help="write the full report here")
    parser.add_argument("--with-data", action="store_true", help="also count data items per dataset")
    args = parser.parse_args()

    _apply_env()
    report = asyncio.run(_collect(args.with_data))
    _render(report)

    if args.json_path:
        out = Path(args.json_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
        print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
