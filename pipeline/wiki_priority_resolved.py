"""Resolved priority ingest queue (priority_resolved.jsonl on I:)."""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from pipeline.wiki_ops_paths import reports_dir, resolved_path, validate_year


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _new_id() -> str:
    return f"res_{uuid.uuid4().hex[:10]}"


def load_resolved_lines(year: str) -> list[dict[str, Any]]:
    path = resolved_path(year)
    if not path.exists():
        return []
    lines: list[dict[str, Any]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict):
            lines.append(obj)
    return lines


def save_resolved_lines(year: str, lines: list[dict[str, Any]]) -> None:
    validate_year(year)
    path = resolved_path(year)
    path.parent.mkdir(parents=True, exist_ok=True)
    body = "\n".join(json.dumps(line, ensure_ascii=False) for line in lines)
    if body:
        body += "\n"
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(body, encoding="utf-8")
    tmp.replace(path)


def cancel_awaiting_for_subject(year: str, subject_id: str) -> int:
    lines = load_resolved_lines(year)
    changed = 0
    for line in lines:
        if line.get("subject_id") == subject_id and line.get("ingest_status") == "awaiting":
            line["ingest_status"] = "cancelled"
            changed += 1
    if changed:
        save_resolved_lines(year, lines)
    return changed


def append_resolved(year: str, record: dict[str, Any]) -> None:
    lines = load_resolved_lines(year)
    row = dict(record)
    row.setdefault("schema_version", 1)
    row.setdefault("id", _new_id())
    row.setdefault("queued_at", _now_iso())
    row.setdefault("ingest_status", "awaiting")
    row["year"] = validate_year(year)
    lines.append(row)
    save_resolved_lines(year, lines)


def list_awaiting(year: str) -> list[dict[str, Any]]:
    awaiting = [
        line
        for line in load_resolved_lines(year)
        if line.get("ingest_status") == "awaiting"
    ]
    awaiting.sort(
        key=lambda r: (
            int(r.get("subject_rank") or 10_000),
            str(r.get("queued_at") or ""),
        )
    )
    return awaiting


def mark_status(year: str, resolved_id: str, status: str) -> bool:
    lines = load_resolved_lines(year)
    found = False
    for line in lines:
        if line.get("id") == resolved_id:
            line["ingest_status"] = status
            found = True
            break
    if found:
        save_resolved_lines(year, lines)
    return found


def drain_awaiting(
    year: str,
    ingest_one_path_cb: Callable[[dict[str, Any]], str],
) -> dict[str, Any]:
    """Drain awaiting rows via callback. Callback returns new ingest_status."""
    lines = load_resolved_lines(year)
    if not lines:
        return {"drained": 0, "failed": 0, "skipped": 0, "message": "no resolved file or empty"}
    awaiting = [
        (i, line)
        for i, line in enumerate(lines)
        if line.get("ingest_status") == "awaiting"
    ]
    awaiting.sort(
        key=lambda pair: (
            int(pair[1].get("subject_rank") or 10_000),
            str(pair[1].get("queued_at") or ""),
        )
    )
    drained = failed = skipped = 0
    seen: set[str] = set()
    for idx, line in awaiting:
        identity = (
            str(line.get("page_id") or "").strip()
            or str(line.get("path") or "").strip().casefold()
            or str(line.get("title") or "").strip().casefold()
        )
        if identity and identity in seen:
            lines[idx]["ingest_status"] = "skipped_already_done"
            skipped += 1
            continue
        if identity:
            seen.add(identity)
        try:
            status = ingest_one_path_cb(line)
        except Exception:  # noqa: BLE001
            status = "failed"
        lines[idx]["ingest_status"] = status
        if status == "ingested":
            drained += 1
        elif status == "skipped_already_done":
            skipped += 1
        else:
            failed += 1
    save_resolved_lines(year, lines)
    return {"drained": drained, "failed": failed, "skipped": skipped}


def resolution_summary_path(year: str) -> Path:
    return reports_dir(year) / "priority_resolution.json"
