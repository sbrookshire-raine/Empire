"""Durable retry scheduling for PocketBase `ingestion_jobs` (P3).

Why this exists: retries were an in-process fixed sleep (`ingest_workbench.py` RETRY_DELAY_SECONDS = 15), and a job
whose process died simply stayed `running` forever. The cleanup script then closed it as **failed** — wrong twice
over: an interrupted job is not a failed one, and a terminal state throws away work a retry could have finished.
Measured 2026-09-27: **14 of 544** job rows were stuck in `running`, and the schema had nowhere to say "try again
at 10:04", so nothing could act on them.

The technique is the one already trusted for LLM calls (`pipeline/cognee_client.py` uses tenacity's
`wait_exponential_jitter(8, 128)`) — exponential growth with jitter — but expressed as an **absolute timestamp**,
because a durable schedule has to survive the death of the process that wrote it.

Pure functions, no I/O: the policy is testable without a database or a server. See `tests/test_job_schedule.py`.
"""

from __future__ import annotations

import random
from datetime import datetime, timedelta, timezone
from typing import Any

DEFAULT_MAX_RETRIES = 3
BASE_DELAY_SECONDS = 15.0  # matches the fixed sleep this replaces, so first-retry latency is unchanged
MAX_DELAY_SECONDS = 900.0  # 15 min ceiling
JITTER_FRACTION = 0.25

INTERRUPTED = "interrupted"
TRANSIENT = "transient"
PERMANENT = "permanent"
FAILURE_REASONS = (INTERRUPTED, TRANSIENT, PERMANENT)

STATUS_PENDING = "pending"
STATUS_RUNNING = "running"
STATUS_SUCCESS = "success"
STATUS_FAILED = "failed"
STATUS_DEAD_LETTER = "dead_letter"

# Substrings that mean "this will fail again the same way" — retrying only burns time and GPU.
_PERMANENT_MARKERS = (
    "not found",
    "no such file",
    "unsupported",
    "only .json and .md",
    "no .json or .md files",
    "permission denied",
    "access is denied",
    "not a file",
    "invalid",
    "schema",
    "unknown collection",
)

# Substrings that are worth another attempt: contention, timeouts, a service still coming up.
_TRANSIENT_MARKERS = (
    "lock",
    "timeout",
    "timed out",
    "connection",
    "refused",
    "reset by peer",
    "temporarily",
    "unavailable",
    "429",
    "502",
    "503",
    "504",
    "try again",
    "context length",
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def to_pb_date(value: datetime) -> str:
    """PocketBase date format, matching `ingest_local._utc_now_iso` so the two never disagree."""
    return value.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.000Z")


def retry_delay_seconds(
    retry_count: int,
    *,
    base: float = BASE_DELAY_SECONDS,
    cap: float = MAX_DELAY_SECONDS,
    jitter: float = JITTER_FRACTION,
    rng: Any = None,
) -> float:
    """Seconds to wait before attempt `retry_count + 1`.

    Exponential from `base`, capped at `cap`, with +/- `jitter` of the raw value so a batch of jobs that failed
    together does not retry in lockstep. `retry_count=0` gives roughly `base` — the first retry is as prompt as the
    fixed sleep it replaces.
    """
    if retry_count < 0:
        raise ValueError("retry_count cannot be negative")
    raw = min(base * (2**retry_count), cap)
    spread = raw * jitter
    draw = (rng or random).uniform(-spread, spread)
    return max(0.0, min(raw + draw, cap))


def classify_failure(failure: BaseException | str) -> str:
    """Decide whether another attempt is worth it: `permanent`, `transient`, or `interrupted`.

    Defaults to `transient` — an unrecognised error gets `max_retries` attempts and then quarantine, which is the
    cheap direction to be wrong in. `interrupted` is set explicitly by callers that know the process was killed
    (the stale-job reaper), because a process death leaves no exception at all.
    """
    message = str(failure).lower()
    if any(marker in message for marker in _PERMANENT_MARKERS):
        return PERMANENT
    if any(marker in message for marker in _TRANSIENT_MARKERS):
        return TRANSIENT
    return TRANSIENT


def plan_after_failure(
    *,
    retry_count: int = 0,
    max_retries: int = DEFAULT_MAX_RETRIES,
    reason: str = TRANSIENT,
    error: str = "",
    now: datetime | None = None,
    rng: Any = None,
) -> dict[str, Any]:
    """Build the PocketBase patch for a failed attempt.

    Returns `status=pending` with a `next_run_at` when another attempt is allowed, or `status=dead_letter` with no
    schedule when it is not. `dead_letter` (not `failed`) is the terminal state so a quarantine is visibly different
    from an ordinary failure, and so a review pass can find exactly the rows a human must look at.

    `max_retries` is the ceiling on **total attempts**, not just retries: 3 means the initial attempt plus two more.
    """
    if reason not in FAILURE_REASONS:
        raise ValueError(f"unknown failure reason {reason!r}; expected one of {FAILURE_REASONS}")

    attempts_made = retry_count + 1
    can_retry = reason != PERMANENT and attempts_made < max_retries

    patch: dict[str, Any] = {
        "retry_count": attempts_made,
        "max_retries": max_retries,
        "failure_reason": reason,
        "finished_at": to_pb_date(now or utc_now()),
    }
    if error:
        patch["error"] = error[:5000]

    if can_retry:
        delay = retry_delay_seconds(retry_count, rng=rng)
        patch["status"] = STATUS_PENDING
        patch["next_run_at"] = to_pb_date((now or utc_now()) + timedelta(seconds=delay))
        patch["retry_delay_seconds"] = round(delay, 1)
    else:
        patch["status"] = STATUS_DEAD_LETTER
        patch["next_run_at"] = None

    return patch
