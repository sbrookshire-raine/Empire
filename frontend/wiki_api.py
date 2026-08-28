"""Wiki Ops API helpers used by frontend/serve.py (file-only; no Cognee)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs

from pipeline.wiki_checkpoint import load_checkpoint
from pipeline.wiki_ops_paths import (
    overnight_pid_alive,
    reports_dir,
    status_path,
    subjects_path,
    validate_year,
)
from pipeline.wiki_priority_resolved import (
    append_resolved,
    cancel_awaiting_for_subject,
    list_awaiting,
    resolution_summary_path,
)
from pipeline.wiki_priority_subjects import (
    add_subjects,
    delete_subject,
    load_subjects,
    move_subject,
    patch_subject,
    put_full_list,
    save_subjects,
)
from pipeline.wiki_report_export import build_progress_block
from pipeline.wiki_titles_by_letter import list_letters, page_letter


def _page_jsonl(path: Path, *, offset: int, limit: int, q: str = "") -> dict[str, Any]:
    if not path.exists():
        return {
            "items": [],
            "total": 0,
            "offset": offset,
            "limit": limit,
            "message": f"Missing {path.name} — run maintenance export after overnight stops",
        }
    qn = q.strip().casefold()
    matched: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if qn and qn not in str(obj.get("t") or "").casefold():
            continue
        matched.append(obj)
    total = len(matched)
    slice_ = matched[offset : offset + limit]
    return {"items": slice_, "total": total, "offset": offset, "limit": limit}


def wiki_status(year: str) -> dict[str, Any]:
    y = validate_year(year)
    cp = load_checkpoint()
    progress = build_progress_block(cp, y)
    file_status: dict[str, Any] = {}
    sp = status_path(y)
    if sp.exists():
        try:
            file_status = json.loads(sp.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            file_status = {}
    alive = overnight_pid_alive(y)
    phase = str(file_status.get("phase") or "idle")
    if alive:
        phase = "ingest"
    return {
        "ok": True,
        "year": y,
        "phase": phase,
        "overnight_pid_alive": alive,
        "progress": progress,
        "ingest": file_status.get("ingest") or {},
        "maintenance": file_status.get("maintenance") or {},
        "priorities": file_status.get("priorities") or {},
        "titles": file_status.get("titles") or {},
        "updated_at": file_status.get("updated_at"),
        "status_path": str(sp),
    }


def wiki_titles(year: str, *, q: str, offset: int, limit: int) -> dict[str, Any]:
    y = validate_year(year)
    return _page_jsonl(reports_dir(y) / "titles.jsonl", offset=offset, limit=limit, q=q)


def wiki_new_titles(year: str, *, offset: int, limit: int) -> dict[str, Any]:
    y = validate_year(year)
    return _page_jsonl(reports_dir(y) / "new-titles.jsonl", offset=offset, limit=limit)


def wiki_letters(year: str) -> dict[str, Any]:
    return list_letters(year)


def wiki_titles_by_letter(
    year: str,
    letter: str,
    *,
    offset: int,
    limit: int,
    q: str = "",
    only_missing: bool = True,
) -> dict[str, Any]:
    return page_letter(
        year,
        letter,
        offset=offset,
        limit=limit,
        q=q,
        only_missing=only_missing,
    )


def wiki_queue_articles(payload: dict[str, Any]) -> dict[str, Any]:
    """Queue whole articles (from letter browser) onto priority_resolved awaiting."""
    year = validate_year(str(payload.get("year") or "2017"))
    articles = payload.get("articles") or []
    if not isinstance(articles, list) or not articles:
        raise ValueError("articles list required")
    queued = 0
    for art in articles:
        if not isinstance(art, dict):
            continue
        path = str(art.get("path") or art.get("p") or "").strip()
        title = str(art.get("title") or art.get("t") or "").strip()
        if not path or not title:
            continue
        page_id = str(art.get("page_id") or art.get("id") or "").strip()
        append_resolved(
            year,
            {
                "subject_id": "browse",
                "subject": title,
                "subject_rank": 0,
                "title": title,
                "page_id": page_id,
                "path": path,
                "match_score": 1.0,
                "match_reason": "letter_browse",
                "ingest_status": "awaiting",
            },
        )
        queued += 1
    return {
        "ok": True,
        "queued": queued,
        "awaiting": len(list_awaiting(year)),
    }


def wiki_priorities_get() -> dict[str, Any]:
    doc = load_subjects()
    year = str(doc.get("year_hint") or "2017")
    summary = {}
    sp = resolution_summary_path(year)
    if sp.exists():
        try:
            summary = json.loads(sp.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            summary = {}
    awaiting = list_awaiting(year)[:20]
    return {
        "ok": True,
        "subjects_path": str(subjects_path()),
        "queue": doc,
        "resolution": summary,
        "awaiting_head": awaiting,
    }


def wiki_priorities_put(payload: dict[str, Any]) -> dict[str, Any]:
    doc = put_full_list(payload)
    return {"ok": True, "queue": doc}


def wiki_priorities_post(payload: dict[str, Any]) -> dict[str, Any]:
    items = payload.get("subjects")
    if items is None and payload.get("subject"):
        items = [payload]
    if not isinstance(items, list):
        raise ValueError("subjects must be a list")
    for item in items:
        if isinstance(item, dict) and (item.get("path") or item.get("page_id")):
            raise ValueError("Reject path/page_id on subject create")
    doc = load_subjects()
    if payload.get("year_hint"):
        doc["year_hint"] = str(payload["year_hint"])
    if "notes" in payload:
        doc["notes"] = str(payload.get("notes") or "")
    doc = add_subjects(doc, items, updated_by="wiki.html")
    save_subjects(doc)
    return {"ok": True, "queue": load_subjects()}


def wiki_priorities_patch(subject_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    doc = load_subjects()
    direction = payload.get("direction")
    if direction in ("up", "down"):
        doc = move_subject(doc, subject_id, direction)
        # Cancel not needed for reorder
    else:
        intent = payload.get("intent")
        if intent is None and "notes" in payload:
            intent = payload.get("notes")
        subject_text = payload.get("subject")
        if subject_text is not None:
            cancel_awaiting_for_subject(str(doc.get("year_hint") or "2017"), subject_id)
        doc = patch_subject(
            doc,
            subject_id,
            subject=subject_text,
            intent=intent,
            rank=payload.get("rank"),
        )
    save_subjects(doc)
    return {"ok": True, "queue": load_subjects()}


def wiki_priorities_delete(subject_id: str) -> dict[str, Any]:
    doc = load_subjects()
    year = str(doc.get("year_hint") or "2017")
    cancel_awaiting_for_subject(year, subject_id)
    doc = delete_subject(doc, subject_id)
    save_subjects(doc)
    return {"ok": True, "queue": load_subjects()}


def wiki_priorities_confirm(payload: dict[str, Any]) -> dict[str, Any]:
    subject_id = str(payload.get("subject_id") or "")
    if not subject_id:
        raise ValueError("subject_id required")
    doc = load_subjects()
    year = str(doc.get("year_hint") or "2017")
    row = next((s for s in doc.get("subjects") or [] if s.get("id") == subject_id), None)
    if not row:
        raise KeyError(f"Subject not found: {subject_id}")
    skip = bool(payload.get("skip"))
    articles = payload.get("articles") or []
    if skip or not articles:
        row["status"] = "skipped"
        save_subjects(doc)
        return {"ok": True, "queue": load_subjects()}
    selected = list(row.get("selected_articles") or [])
    for art in articles:
        if not isinstance(art, dict):
            continue
        path = str(art.get("path") or "")
        title = str(art.get("title") or "")
        page_id = str(art.get("page_id") or "")
        append_resolved(
            year,
            {
                "subject_id": subject_id,
                "subject": row.get("subject"),
                "subject_rank": row.get("rank"),
                "title": title,
                "page_id": page_id,
                "path": path,
                "match_score": 1.0,
                "match_reason": "user_confirm",
                "ingest_status": "awaiting",
            },
        )
        selected.append(
            {"title": title, "path": path, "page_id": page_id, "score": 1.0, "match_tier": "user_confirm"}
        )
    row["selected_articles"] = selected
    row["status"] = "queued"
    save_subjects(doc)
    return {"ok": True, "queue": load_subjects()}


def parse_query(path_with_query: str) -> dict[str, list[str]]:
    if "?" not in path_with_query:
        return {}
    return parse_qs(path_with_query.split("?", 1)[1])
