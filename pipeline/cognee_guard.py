"""Light guards so intake memory promotion does not pile onto heavy Cognee work."""

from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from typing import Any

from filelock import FileLock, Timeout

from pipeline.cognee_lock import LOCK_FILE, file_lock_enabled

DEFAULT_MAX_CHARS = 2500
DEFAULT_MAX_PROPOSES_PER_HOUR = 6
LOCK_PROBE_SECONDS = 0.05


def _parse_iso(value: str) -> datetime | None:
    text = (value or "").strip()
    if not text:
        return None
    try:
        if text.endswith("Z"):
            text = text[:-1] + "+00:00"
        return datetime.fromisoformat(text)
    except ValueError:
        return None


def _recent_propose_count(within_hours: float = 1.0) -> int:
    from pipeline.eve_staging import _load_ledger  # noqa: SLF001

    ledger = _load_ledger()
    cutoff = datetime.now(timezone.utc) - timedelta(hours=within_hours)
    count = 0
    for entry in ledger.get("entries") or []:
        if not isinstance(entry, dict):
            continue
        if str(entry.get("status") or "") not in {"proposed", "confirmed"}:
            continue
        when = _parse_iso(str(entry.get("proposed_at") or ""))
        if when and when >= cutoff:
            count += 1
    return count


def cognee_busy() -> bool:
    if not file_lock_enabled():
        return False
    lock = FileLock(str(LOCK_FILE), timeout=LOCK_PROBE_SECONDS, thread_local=False)
    try:
        lock.acquire(timeout=LOCK_PROBE_SECONDS)
        lock.release()
        return False
    except Timeout:
        return True
    except OSError:
        return False


def memory_promote_allowed(*, chars: int) -> tuple[bool, str]:
    max_chars = int(os.environ.get("EMPIRE_INTAKE_MEMORY_MAX_CHARS", DEFAULT_MAX_CHARS))
    max_hour = int(os.environ.get("EMPIRE_INTAKE_MEMORY_MAX_HOUR", DEFAULT_MAX_PROPOSES_PER_HOUR))
    if chars > max_chars:
        return (
            False,
            f"intake memory capped at {max_chars} chars (got {chars}) — shorten summary or promote manually",
        )
    if _recent_propose_count(1.0) >= max_hour:
        return (
            False,
            f"staging propose limit {max_hour}/hour — wait or confirm/drop pending entries in Memory tab",
        )
    if cognee_busy():
        return (
            False,
            "Cognee is busy (lock held) — skipped auto remember; card is local, retry memory later",
        )
    return True, ""


def guard_memory_promotion(content: str) -> dict[str, Any] | None:
    """Return error dict to embed in intake result, or None if OK."""
    text = (content or "").strip()
    ok, reason = memory_promote_allowed(chars=len(text))
    if ok:
        return None
    return {"ok": False, "skipped": True, "reason": reason}
