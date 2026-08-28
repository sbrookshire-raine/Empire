"""Ranked priority subject queue IO (%LOCALAPPDATA%\\EMPIRE\\priority_subjects.json)."""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pipeline.wiki_ops_paths import subjects_path

MAX_SUBJECTS = 500
MAX_SUBJECT_LEN = 200
MAX_INTENT_LEN = 500
CONSUMED_STATUSES = frozenset({"resolved_done"})
SCHEMA_VERSION = 2


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _new_id() -> str:
    return f"subj_{uuid.uuid4().hex[:10]}"


def empty_queue(year_hint: str = "2017") -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "updated_at": _now_iso(),
        "updated_by": "system",
        "year_hint": str(year_hint),
        "notes": "",
        "subjects": [],
    }


def renumber(doc: dict[str, Any]) -> dict[str, Any]:
    subjects = list(doc.get("subjects") or [])
    for i, row in enumerate(subjects, start=1):
        row["rank"] = i
    doc["subjects"] = subjects
    return doc


def _normalize_row(raw: dict[str, Any]) -> dict[str, Any]:
    intent = str(raw.get("intent") or raw.get("notes") or "").strip()
    if len(intent) > MAX_INTENT_LEN:
        intent = intent[:MAX_INTENT_LEN]
    subject = str(raw.get("subject") or "").strip()
    status = str(raw.get("status") or "pending").strip() or "pending"
    return {
        "id": str(raw.get("id") or _new_id()),
        "rank": int(raw.get("rank") or 0),
        "subject": subject,
        "intent": intent,
        "added_at": str(raw.get("added_at") or _now_iso()),
        "status": status,
        "candidates": list(raw.get("candidates") or []),
        "selected_articles": list(raw.get("selected_articles") or []),
        "resolved": raw.get("resolved"),
        "suggestions": list(raw.get("suggestions") or []),
    }


def load_subjects(path: Path | None = None) -> dict[str, Any]:
    target = path or subjects_path()
    if not target.exists():
        return empty_queue()
    try:
        data = json.loads(target.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return empty_queue()
    if not isinstance(data, dict):
        return empty_queue()
    subjects_raw = data.get("subjects")
    if not isinstance(subjects_raw, list):
        subjects_raw = []
    # Legacy priority-sort migrate
    if subjects_raw and any("priority" in s for s in subjects_raw if isinstance(s, dict)):
        subjects_raw = sorted(
            subjects_raw,
            key=lambda s: int((s or {}).get("priority", 50)) if isinstance(s, dict) else 50,
        )
    subjects = [_normalize_row(s) for s in subjects_raw if isinstance(s, dict)]
    doc = {
        "schema_version": SCHEMA_VERSION,
        "updated_at": str(data.get("updated_at") or _now_iso()),
        "updated_by": str(data.get("updated_by") or "system"),
        "year_hint": str(data.get("year_hint") or "2017"),
        "notes": str(data.get("notes") or ""),
        "subjects": subjects,
    }
    return renumber(doc)


def save_subjects(doc: dict[str, Any], path: Path | None = None) -> None:
    target = path or subjects_path()
    doc = renumber(dict(doc))
    subjects = list(doc.get("subjects") or [])
    if len(subjects) > MAX_SUBJECTS:
        raise ValueError(f"Too many subjects ({len(subjects)} > {MAX_SUBJECTS})")
    for row in subjects:
        subject = str(row.get("subject") or "").strip()
        if not subject:
            raise ValueError("Empty subject text rejected")
        if len(subject) > MAX_SUBJECT_LEN:
            raise ValueError(f"Subject exceeds {MAX_SUBJECT_LEN} chars")
        intent = str(row.get("intent") or "")
        if len(intent) > MAX_INTENT_LEN:
            raise ValueError(f"Intent exceeds {MAX_INTENT_LEN} chars")
        row["subject"] = subject
        row["intent"] = intent
    doc["schema_version"] = SCHEMA_VERSION
    doc["updated_at"] = _now_iso()
    doc["subjects"] = subjects
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    tmp.write_text(json.dumps(doc, indent=2), encoding="utf-8")
    tmp.replace(target)


def add_subjects(
    doc: dict[str, Any],
    items: list[str | dict[str, Any]],
    *,
    updated_by: str = "api",
) -> dict[str, Any]:
    subjects = list(doc.get("subjects") or [])
    for item in items:
        if isinstance(item, str):
            subject = item.strip()
            intent = ""
            extra: dict[str, Any] = {}
        elif isinstance(item, dict):
            if item.get("path") or item.get("page_id"):
                raise ValueError("Reject path/page_id on subject create")
            subject = str(item.get("subject") or "").strip()
            intent = str(item.get("intent") or item.get("notes") or "").strip()
            extra = item
        else:
            raise ValueError("Invalid subject item")
        if not subject:
            raise ValueError("Empty subject text rejected")
        row = _normalize_row(
            {
                "id": extra.get("id") if isinstance(item, dict) else None,
                "subject": subject,
                "intent": intent,
                "status": "pending",
                "added_at": _now_iso(),
            }
        )
        subjects.append(row)
    doc["subjects"] = subjects
    doc["updated_by"] = updated_by
    return renumber(doc)


def _find_index(doc: dict[str, Any], subject_id: str) -> int:
    for i, row in enumerate(doc.get("subjects") or []):
        if row.get("id") == subject_id:
            return i
    raise KeyError(f"Subject not found: {subject_id}")


def _is_consumed(row: dict[str, Any]) -> bool:
    if row.get("status") in CONSUMED_STATUSES:
        selected = row.get("selected_articles") or []
        if not selected:
            return True
        # All selected done if status says so
        return True
    return False


def patch_subject(
    doc: dict[str, Any],
    subject_id: str,
    *,
    subject: str | None = None,
    intent: str | None = None,
    rank: int | None = None,
) -> dict[str, Any]:
    idx = _find_index(doc, subject_id)
    row = doc["subjects"][idx]
    if subject is not None:
        new_subject = subject.strip()
        if not new_subject:
            raise ValueError("Empty subject text rejected")
        if _is_consumed(row):
            raise ValueError("already ingested; add a new subject instead")
        if new_subject != row.get("subject"):
            row["subject"] = new_subject
            row["status"] = "pending"
            row["candidates"] = []
            row["selected_articles"] = []
            row["resolved"] = None
            row["suggestions"] = []
            try:
                from pipeline.wiki_priority_resolved import cancel_awaiting_for_subject

                year = str(doc.get("year_hint") or "2017")
                cancel_awaiting_for_subject(year, subject_id)
            except Exception:  # noqa: BLE001 — cancel best-effort
                pass
    if intent is not None:
        row["intent"] = intent.strip()[:MAX_INTENT_LEN]
    if rank is not None:
        subjects = list(doc["subjects"])
        row = subjects.pop(idx)
        new_idx = max(0, min(len(subjects), int(rank) - 1))
        subjects.insert(new_idx, row)
        doc["subjects"] = subjects
    return renumber(doc)


def delete_subject(doc: dict[str, Any], subject_id: str) -> dict[str, Any]:
    idx = _find_index(doc, subject_id)
    doc["subjects"].pop(idx)
    try:
        from pipeline.wiki_priority_resolved import cancel_awaiting_for_subject

        year = str(doc.get("year_hint") or "2017")
        cancel_awaiting_for_subject(year, subject_id)
    except Exception:  # noqa: BLE001
        pass
    return renumber(doc)


def move_subject(doc: dict[str, Any], subject_id: str, direction: str) -> dict[str, Any]:
    idx = _find_index(doc, subject_id)
    subjects = list(doc["subjects"])
    if direction == "up" and idx > 0:
        subjects[idx - 1], subjects[idx] = subjects[idx], subjects[idx - 1]
    elif direction == "down" and idx < len(subjects) - 1:
        subjects[idx + 1], subjects[idx] = subjects[idx], subjects[idx + 1]
    elif direction not in ("up", "down"):
        raise ValueError("direction must be up or down")
    doc["subjects"] = subjects
    return renumber(doc)


def put_full_list(payload: dict[str, Any], path: Path | None = None) -> dict[str, Any]:
    subjects_in = payload.get("subjects")
    if not isinstance(subjects_in, list):
        raise ValueError("subjects must be a list")
    for item in subjects_in:
        if isinstance(item, dict) and (item.get("path") or item.get("page_id")):
            raise ValueError("Reject path/page_id on subject create")
    doc = empty_queue(str(payload.get("year_hint") or "2017"))
    doc["notes"] = str(payload.get("notes") or "")
    doc["updated_by"] = str(payload.get("updated_by") or "api")
    normalized = []
    for item in subjects_in:
        if isinstance(item, str):
            normalized.append(_normalize_row({"subject": item, "status": "pending"}))
        elif isinstance(item, dict):
            normalized.append(_normalize_row(item))
        else:
            raise ValueError("Invalid subject entry")
    doc["subjects"] = normalized
    save_subjects(doc, path=path)
    return load_subjects(path)
