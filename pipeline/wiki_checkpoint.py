"""Resumable checkpoint state for Wikipedia batch ingestion.

Compact, index-based resume: files within a batch are processed in sorted order, so we only
need to persist ``next_index`` per batch (not millions of doc ids). Stored outside OneDrive
at ``%LOCALAPPDATA%\\EMPIRE\\wiki-checkpoint.json``.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CHECKPOINT_DIR = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "EMPIRE"
CHECKPOINT_FILE = CHECKPOINT_DIR / "wiki-checkpoint.json"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_checkpoint() -> dict[str, Any]:
    if not CHECKPOINT_FILE.exists():
        return {"version": 1, "batches": {}}
    try:
        data = json.loads(CHECKPOINT_FILE.read_text(encoding="utf-8"))
        if "batches" not in data:
            data["batches"] = {}
        return data
    except Exception:  # noqa: BLE001 — corrupt checkpoint should not block ingest
        return {"version": 1, "batches": {}}


def save_checkpoint(state: dict[str, Any]) -> None:
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    tmp = CHECKPOINT_FILE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=2), encoding="utf-8")
    tmp.replace(CHECKPOINT_FILE)


def batch_key(year: str, batch_name: str) -> str:
    return f"{year}/{batch_name}"


def get_batch(state: dict[str, Any], key: str) -> dict[str, Any]:
    return state["batches"].get(key, {})


def get_next_index(state: dict[str, Any], key: str) -> int:
    return int(get_batch(state, key).get("next_index", 0))


def update_batch(
    state: dict[str, Any],
    key: str,
    *,
    next_index: int,
    processed: int,
    mode: str,
    dataset: str,
    status: str,
    total: int | None = None,
) -> dict[str, Any]:
    entry = state["batches"].get(key, {})
    entry.update(
        {
            "next_index": next_index,
            "processed": processed,
            "mode": mode,
            "dataset": dataset,
            "status": status,
            "updated": _now_iso(),
        }
    )
    if total is not None:
        entry["total"] = total
    state["batches"][key] = entry
    return state
