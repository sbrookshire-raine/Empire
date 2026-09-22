"""Cross-process lock: Title DNS evidence was already injected this turn.

When Workbench injects [[EMPIRE_WIKI_LOOKUP]] or [[EMPIRE_WIKI_EXTRACT]], Eve must not register or call
wiki_scout_search / Weaviate. Prompt text alone is soft; this file is the hard gate.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any

DEFAULT_TTL_SEC = 90.0


def lock_path() -> Path:
    override = os.environ.get("EMPIRE_WIKI_LOOKUP_LOCK", "").strip()
    if override:
        return Path(override)
    local_app = os.environ.get("LOCALAPPDATA", "").strip()
    if local_app:
        return Path(local_app) / "EMPIRE" / "eve-wiki-lookup-lock.json"
    return Path(__file__).resolve().parents[1] / "config" / "eve-wiki-lookup-lock.json"


def _ttl_sec() -> float:
    raw = os.environ.get("EMPIRE_WIKI_LOOKUP_LOCK_TTL", "").strip()
    if not raw:
        return DEFAULT_TTL_SEC
    try:
        return max(5.0, float(raw))
    except ValueError:
        return DEFAULT_TTL_SEC


def set_wiki_lookup_lock(
    *,
    reason: str = "lookup_injected",
    session_id: str = "",
    ttl_sec: float | None = None,
) -> Path:
    path = lock_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    ttl = _ttl_sec() if ttl_sec is None else max(5.0, float(ttl_sec))
    now = time.time()
    payload = {
        "active": True,
        "reason": (reason or "lookup_injected").strip() or "lookup_injected",
        "session_id": (session_id or "").strip(),
        "set_at": now,
        "expires_at": now + ttl,
    }
    try:
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    except OSError:
        pass
    return path


def clear_wiki_lookup_lock() -> None:
    path = lock_path()
    try:
        if path.is_file():
            path.unlink()
    except OSError:
        pass


def read_wiki_lookup_lock() -> dict[str, Any] | None:
    path = lock_path()
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, TypeError):
        return None
    if not isinstance(parsed, dict):
        return None
    return parsed


def wiki_lookup_lock_active() -> bool:
    data = read_wiki_lookup_lock()
    if not data or not data.get("active"):
        return False
    try:
        expires = float(data.get("expires_at") or 0)
    except (TypeError, ValueError):
        clear_wiki_lookup_lock()
        return False
    if time.time() > expires:
        clear_wiki_lookup_lock()
        return False
    return True


def locked_tool_response(*, tool: str = "wiki_scout_search") -> dict[str, Any]:
    return {
        "ok": True,
        "usable": True,
        "source": "lookup_lock",
        "tool": tool,
        "cards": [],
        "paths": [],
        "titles": [],
        "chat_reply_rule": "Use the already-injected local Wiki evidence in the conversation context.",
        "coverage_note": "No additional Wiki lookup needed.",
    }
