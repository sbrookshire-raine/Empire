"""Check dataset eve_core against the Foundation registry (config/foundation.json).

Purpose: turn the memory governance policy (docs/MEMORY_GOVERNANCE.md sections 1-3) into a
measurement instead of an intention. ``eve_core`` is the dataset chat recall prefers, and it was
filled by keyword scoring (scripts/optimize_eve_memory.py) that - provably - ranked NotebookLM
exports above project knowledge and admitted duplicate and 'unmatched-*' residue. This script says
how far the dataset is from the deliberate set, so the rebuild has a target.

Read-only: it inspects the manifest and the referenced files, and writes nothing to Cognee.

Exit codes:
  0 = registry satisfied (or the manifest is absent - instrument unavailable is not a violation)
  1 = a forbidden entry is present, or --strict was given and unregistered entries exist
  2 = the registry itself is broken (a registered path does not exist, or the JSON is unreadable)

Usage::

    .\\venv\\Scripts\\python.exe scripts\\check-foundation.py
    .\\venv\\Scripts\\python.exe scripts\\check-foundation.py --strict --json out.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "config" / "foundation.json"


def _read_body(path: Path) -> str:
    """Tolerant decode, mirroring the ingest decoder (utf-8 -> cp1252 -> latin-1)."""
    raw = path.read_bytes()
    for encoding in ("utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return ""


def _load_registry() -> dict:
    try:
        return json.loads(REGISTRY.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"REGISTRY UNREADABLE: {REGISTRY}: {type(exc).__name__}: {exc}")
        raise SystemExit(2) from exc


def _compile(patterns: list[str]) -> list[re.Pattern[str]]:
    """Compile registry patterns. A bad pattern is a broken registry, never a crash.

    Earned 2026-09-26: the first registry shipped `\\TASK_QUEUE` (JSON `"\\TASK_QUEUE"`), which is
    a bad regex escape, and `\\n8n` (which silently means newline + '8n'). A checker that dies with
    a traceback on its own config cannot be trusted in a gate.
    """
    compiled: list[re.Pattern[str]] = []
    bad: list[tuple[str, str]] = []
    for pattern in patterns:
        try:
            compiled.append(re.compile(pattern, re.IGNORECASE))
        except re.error as exc:
            bad.append((pattern, str(exc)))
    if bad:
        print(f"REGISTRY BROKEN - invalid regex pattern(s) in {REGISTRY}:")
        for pattern, error in bad:
            print(f"  ! {pattern!r}: {error}")
        raise SystemExit(2)
    return compiled


def main() -> int:
    parser = argparse.ArgumentParser(description="Check eve_core against the Foundation registry.")
    parser.add_argument("--strict", action="store_true", help="unregistered entries fail the check")
    parser.add_argument("--json", dest="json_path", help="write the full report here")
    parser.add_argument(
        "--advisory",
        action="store_true",
        help="report violations but always exit 0 (gate wiring before the curated rebuild)",
    )
    args = parser.parse_args()

    registry = _load_registry()
    registered = {str(item["path"]).casefold(): item for item in registry.get("registered", [])}
    reference_re = _compile(list((registry.get("reference_only") or {}).get("path_patterns", [])))
    forbidden_path_re = _compile(list((registry.get("forbidden") or {}).get("path_patterns", [])))
    forbidden_body_re = _compile(list((registry.get("forbidden") or {}).get("content_markers", [])))

    # The registry must be truthful about itself: a wrong path is worse than a missing one.
    broken = [item["path"] for item in registry.get("registered", []) if not Path(item["path"]).exists()]
    if broken:
        print(f"REGISTRY BROKEN - registered path(s) do not exist ({len(broken)}):")
        for path in broken:
            print(f"  ! {path}")
        return 2

    manifest_path = Path((registry.get("wiring") or {}).get("manifest", ""))
    if not manifest_path.exists():
        print(f"SKIP: manifest not present ({manifest_path}) - nothing to measure.")
        print(
            f"Registry loads clean: {len(registered)} registered source(s), "
            f"{len(reference_re)} reference pattern(s), "
            f"{len(forbidden_path_re) + len(forbidden_body_re)} forbidden pattern(s)."
        )
        return 0

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    files = manifest.get("files", [])

    ok: list[str] = []
    reference: list[str] = []
    unregistered: list[str] = []
    forbidden: list[tuple[str, str]] = []

    for entry in files:
        raw_path = str(entry.get("path", ""))
        key = raw_path.casefold()
        body_marker = ""
        if raw_path and Path(raw_path).exists():
            body = _read_body(Path(raw_path))
            for pattern in forbidden_body_re:
                if pattern.search(body):
                    body_marker = pattern.pattern
                    break

        if body_marker:
            forbidden.append((raw_path, f"content matches /{body_marker}/"))
        elif key in registered:
            ok.append(raw_path)
        elif any(p.search(raw_path) for p in forbidden_path_re):
            forbidden.append((raw_path, "path pattern"))
        elif any(p.search(raw_path) for p in reference_re):
            reference.append(raw_path)
        else:
            unregistered.append(raw_path)

    print(f"Foundation check - dataset {registry.get('dataset')} (registry v{registry.get('version')})")
    print(f"manifest: {manifest_path}  ({len(files)} entries)")
    print(f"  registered   {len(ok)}")
    print(f"  reference    {len(reference)}   (belongs in a Library access point, not embedded)")
    print(f"  unregistered {len(unregistered)}")
    print(f"  forbidden    {len(forbidden)}")

    if forbidden:
        print("\nFORBIDDEN in eve_core:")
        for path, why in forbidden[:25]:
            print(f"  ! {path}  [{why}]")
    if unregistered:
        print("\nUNREGISTERED (no registry entry, no known reference pattern):")
        for path in unregistered[:25]:
            print(f"  ? {path}")

    if args.json_path:
        out = Path(args.json_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(
                {
                    "dataset": registry.get("dataset"),
                    "manifest": str(manifest_path),
                    "counts": {
                        "registered": len(ok),
                        "reference": len(reference),
                        "unregistered": len(unregistered),
                        "forbidden": len(forbidden),
                    },
                    "registered": ok,
                    "reference": reference,
                    "unregistered": unregistered,
                    "forbidden": [{"path": p, "why": w} for p, w in forbidden],
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"\nwrote {out}")

    if forbidden or (args.strict and unregistered):
        if args.advisory:
            print(
                "\nADVISORY: violations reported, exit 0 until the curated rebuild lands "
                "(docs/MEMORY_GOVERNANCE.md section 7 step 5)."
            )
            return 0
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

