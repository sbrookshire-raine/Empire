"""Session research scratchpad + Error Book for Wikipedia workbench hops.

Scratchpad: retain bridging facts; drop raw markdown from the chat path.
Error Book: persistent dead-ends so Eve does not re-hallucinate misses.
Neither writes Cognee.
"""

from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path
from typing import Any


def _local_empire_dir() -> Path:
    local_app = os.environ.get("LOCALAPPDATA", "").strip()
    if local_app:
        path = Path(local_app) / "EMPIRE"
        try:
            path.mkdir(parents=True, exist_ok=True)
            return path
        except OSError:
            pass
    root = Path(__file__).resolve().parents[1]
    path = root / "config"
    path.mkdir(parents=True, exist_ok=True)
    return path


def scratchpad_path(session_id: str = "") -> Path:
    override = os.environ.get("EMPIRE_WIKI_SCRATCHPAD", "").strip()
    if override:
        return Path(override)
    sid = re.sub(r"[^a-zA-Z0-9_-]+", "_", (session_id or "default").strip()) or "default"
    workbench = Path(os.environ.get("EMPIRE_WORKBENCH", r"C:\Empire_Workbench"))
    folder = workbench / "04_Thought_Experiments" / "wiki_scratch"
    try:
        folder.mkdir(parents=True, exist_ok=True)
        return folder / f"{sid}.json"
    except OSError:
        return _local_empire_dir() / f"wiki-scratch-{sid}.json"


def error_book_path() -> Path:
    override = os.environ.get("EMPIRE_WIKI_ERROR_BOOK", "").strip()
    if override:
        return Path(override)
    return _local_empire_dir() / "wiki-error-book.jsonl"


# The book is append-only and now written automatically on every miss, so it needs a ceiling:
# distinct misses still accumulate over months of use.
_MAX_ERROR_BOOK_ENTRIES = int(os.environ.get("EMPIRE_WIKI_ERROR_BOOK_MAX", "500"))


def _trim_error_book(path: Path) -> None:
    """Keep at most `_MAX_ERROR_BOOK_ENTRIES` lines, newest last. Never raises."""

    if _MAX_ERROR_BOOK_ENTRIES <= 0:
        return
    try:
        lines = [
            line
            for line in path.read_text(encoding="utf-8", errors="replace").splitlines()
            if line.strip()
        ]
        if len(lines) <= _MAX_ERROR_BOOK_ENTRIES:
            return
        temp = path.with_suffix(path.suffix + ".tmp")
        temp.write_text(
            "\n".join(lines[-_MAX_ERROR_BOOK_ENTRIES:]) + "\n",
            encoding="utf-8",
        )
        os.replace(temp, path)
    except OSError:
        return


def _read_json(path: Path) -> dict[str, Any]:
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, TypeError):
        return {}
    return parsed if isinstance(parsed, dict) else {}


def scratch_read(session_id: str = "") -> dict[str, Any]:
    path = scratchpad_path(session_id)
    data = _read_json(path)
    facts = data.get("facts") if isinstance(data.get("facts"), list) else []
    return {
        "ok": True,
        "session_id": session_id or "default",
        "path": str(path),
        "facts": facts,
        "updated_at": data.get("updated_at"),
        "summary": _facts_summary(facts),
    }


def _facts_summary(facts: list[Any], *, limit: int = 12) -> str:
    lines: list[str] = []
    for item in facts[-limit:]:
        if isinstance(item, dict):
            text = str(item.get("text") or "").strip()
            title = str(item.get("title") or "").strip()
            if title and text:
                lines.append(f"- [{title}] {text}")
            elif text:
                lines.append(f"- {text}")
        else:
            text = str(item).strip()
            if text:
                lines.append(f"- {text}")
    return "\n".join(lines)


def scratch_upsert(
    text: str,
    *,
    session_id: str = "",
    title: str = "",
    source: str = "wiki",
) -> dict[str, Any]:
    note = (text or "").strip()
    if not note:
        return {"ok": False, "error": "text is required"}
    path = scratchpad_path(session_id)
    data = _read_json(path)
    facts = data.get("facts") if isinstance(data.get("facts"), list) else []
    facts.append(
        {
            "text": note[:1200],
            "title": (title or "").strip()[:200],
            "source": (source or "wiki").strip()[:64],
            "at": time.time(),
        }
    )
    # Cap memory: keep last 40 bridging facts
    facts = facts[-40:]
    payload = {
        "session_id": session_id or "default",
        "updated_at": time.time(),
        "facts": facts,
    }
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    except OSError as exc:
        return {"ok": False, "error": str(exc)}
    return {
        "ok": True,
        "path": str(path),
        "count": len(facts),
        "summary": _facts_summary(facts),
    }


def scratch_clear(session_id: str = "") -> dict[str, Any]:
    path = scratchpad_path(session_id)
    try:
        if path.is_file():
            path.unlink()
    except OSError as exc:
        return {"ok": False, "error": str(exc)}
    return {"ok": True, "cleared": True, "path": str(path)}


def error_book_append(
    *,
    query: str,
    reason: str,
    title: str = "",
    year: str = "2026",
) -> dict[str, Any]:
    path = error_book_path()
    row = {
        "at": time.time(),
        "query": (query or "").strip()[:400],
        "title": (title or "").strip()[:200],
        "year": (year or "2026").strip(),
        "reason": (reason or "miss").strip()[:400],
    }
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        _trim_error_book(path)
    except OSError as exc:
        return {"ok": False, "error": str(exc)}
    return {"ok": True, "path": str(path), "entry": row}


def error_book_recent(limit: int = 20) -> dict[str, Any]:
    path = error_book_path()
    rows: list[dict[str, Any]] = []
    try:
        if path.is_file():
            for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(row, dict):
                    rows.append(row)
    except OSError as exc:
        return {"ok": False, "error": str(exc), "entries": []}
    return {"ok": True, "path": str(path), "entries": rows[-max(1, min(limit, 100)) :]}


def error_book_mentions_miss(query: str) -> bool:
    q = normalize_loose(query)
    if not q:
        return False
    recent = error_book_recent(limit=50)
    for row in recent.get("entries") or []:
        if not isinstance(row, dict):
            continue
        blob = f"{row.get('query') or ''} {row.get('title') or ''}".casefold()
        if q in normalize_loose(blob):
            return True
    return False


def normalize_loose(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (text or "").casefold()).strip()


def format_scratchpad_block(session_id: str = "") -> str:
    data = scratch_read(session_id)
    summary = str(data.get("summary") or "").strip()
    if not summary:
        return ""
    return (
        "[[EMPIRE_WIKI_SCRATCHPAD]]\n"
        "Active research notes (use these bridging facts; do not re-fetch unless needed):\n"
        f"{summary}\n"
    )


def format_error_book_hint(query: str) -> str:
    if not error_book_mentions_miss(query):
        return ""
    return (
        "[[EMPIRE_WIKI_ERROR_BOOK]]\n"
        "This exact query has missed before — never invent a page for it. Try the bare subject/title "
        'once (`Drum kit`, not `how to play the drums`); if that misses too, say plainly that it is '
        "not in the local Wikipedia archive.\n"
    )
