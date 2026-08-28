"""Cross-process Cognee access guard.

Historically serialized Kuzu/SQLite writers via ``%LOCALAPPDATA%\\EMPIRE\\cognee.lock``.
With Just-Postgres (``DB_PROVIDER=postgres``), concurrent writers are supported and the
file lock is skipped by default (``EMPIRE_COGNEE_SKIP_FILE_LOCK=1``).
"""

from __future__ import annotations

import asyncio
import os
from collections.abc import Awaitable, Callable
from pathlib import Path
from typing import TypeVar

from filelock import FileLock, Timeout

T = TypeVar("T")

LOCK_DIR = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "EMPIRE"
LOCK_FILE = LOCK_DIR / "cognee.lock"
LOCK_TIMEOUT_SECONDS = 600


def _env_flag(name: str, default: bool = False) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def file_lock_enabled() -> bool:
    """Return False when Postgres backend (or explicit skip) allows concurrent writers."""
    if _env_flag("EMPIRE_COGNEE_SKIP_FILE_LOCK", default=False):
        return False
    if os.environ.get("DB_PROVIDER", "").strip().lower() == "postgres":
        return False
    return True


def _lock() -> FileLock:
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    # thread_local=False: we acquire and release from different asyncio executor threads,
    # so lock ownership must be process-wide, otherwise release() silently no-ops and leaks
    # the OS lock (self-deadlocking the next acquire). is_singleton keeps one instance/path
    # so nested/back-to-back operations in the same process reuse the reentrancy counter.
    return FileLock(
        str(LOCK_FILE),
        timeout=LOCK_TIMEOUT_SECONDS,
        thread_local=False,
        is_singleton=True,
    )


async def run_with_cognee_lock(operation: Callable[[], Awaitable[T]]) -> T:
    """Optionally serialize Cognee DB access across MCP tools and CLI scripts."""
    if not file_lock_enabled():
        return await operation()

    lock = _lock()
    loop = asyncio.get_event_loop()
    try:
        await loop.run_in_executor(None, lock.acquire)
        return await operation()
    except Timeout as exc:
        raise RuntimeError(
            "Timed out waiting for the Cognee database lock after "
            f"{LOCK_TIMEOUT_SECONDS}s. Another ingest or MCP tool may still be running."
        ) from exc
    finally:
        if lock.is_locked:
            await loop.run_in_executor(None, lock.release)
