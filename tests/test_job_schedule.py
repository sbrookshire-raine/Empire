"""Tests for pipeline.job_schedule — the durable retry policy (P3).

The policy is pure, so these need no PocketBase and no server. What they pin: the delay actually grows and is
capped, jitter actually varies (a "jittered" constant is a common way to ship a lie), a permanent failure never
retries, an exhausted row is quarantined rather than lost, and the emitted timestamp format matches the one the
runner already writes.
"""

from __future__ import annotations

import random
import re
from datetime import datetime, timedelta, timezone

import pytest

from pipeline.job_schedule import (
    BASE_DELAY_SECONDS,
    DEFAULT_MAX_RETRIES,
    MAX_DELAY_SECONDS,
    PERMANENT,
    STATUS_DEAD_LETTER,
    STATUS_PENDING,
    TRANSIENT,
    classify_failure,
    plan_after_failure,
    retry_delay_seconds,
    to_pb_date,
)

PB_DATE = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.000Z$")


def test_delay_grows_exponentially_within_the_jitter_band() -> None:
    rng = random.Random(7)
    delays = [retry_delay_seconds(n, rng=rng) for n in range(4)]
    nominal = [BASE_DELAY_SECONDS * (2**n) for n in range(4)]

    for delay, expected in zip(delays, nominal):
        assert expected * 0.75 <= delay <= expected * 1.25
    assert delays[0] < delays[1] < delays[2] < delays[3]


def test_delay_never_exceeds_the_cap() -> None:
    rng = random.Random(3)
    for n in range(12):
        assert retry_delay_seconds(n, rng=rng) <= MAX_DELAY_SECONDS


def test_jitter_actually_varies() -> None:
    """Two draws at the same attempt count must differ — otherwise the jitter is decorative."""
    draws = {round(retry_delay_seconds(3, rng=random.Random(seed)), 3) for seed in range(8)}
    assert len(draws) > 1


def test_negative_retry_count_is_rejected() -> None:
    with pytest.raises(ValueError):
        retry_delay_seconds(-1)


@pytest.mark.parametrize(
    ("message", "expected"),
    [
        ("Could not set lock on the graph database", TRANSIENT),
        ("httpx.ConnectError: connection refused", TRANSIENT),
        ("Read timed out after 30s", TRANSIENT),
        ("503 Service Unavailable", TRANSIENT),
        ("Mock file not found: C:/x.md", PERMANENT),
        ("Only .json and .md mock files are supported", PERMANENT),
        ("[Errno 13] Permission denied", PERMANENT),
        ("unknown collection: ingestion_jobs", PERMANENT),
        ("something nobody anticipated", TRANSIENT),
    ],
)
def test_classify_failure(message: str, expected: str) -> None:
    assert classify_failure(message) == expected


def test_first_failure_is_rescheduled_not_quarantined() -> None:
    now = datetime(2026, 9, 27, 10, 0, 0, tzinfo=timezone.utc)
    patch = plan_after_failure(reason=TRANSIENT, now=now, rng=random.Random(1))

    assert patch["status"] == STATUS_PENDING
    assert patch["retry_count"] == 1
    assert patch["failure_reason"] == TRANSIENT
    assert PB_DATE.match(patch["next_run_at"])

    scheduled = datetime.strptime(patch["next_run_at"], "%Y-%m-%d %H:%M:%S.000Z").replace(tzinfo=timezone.utc)
    assert now < scheduled <= now + timedelta(seconds=BASE_DELAY_SECONDS * 1.25)


def test_a_permanent_failure_goes_straight_to_quarantine() -> None:
    patch = plan_after_failure(reason=PERMANENT, error="Mock file not found")
    assert patch["status"] == STATUS_DEAD_LETTER
    assert patch["next_run_at"] is None
    assert patch["retry_count"] == 1


def test_an_exhausted_row_is_quarantined_not_lost() -> None:
    patch = plan_after_failure(retry_count=DEFAULT_MAX_RETRIES - 1, reason=TRANSIENT)
    assert patch["status"] == STATUS_DEAD_LETTER
    assert patch["next_run_at"] is None
    assert patch["retry_count"] == DEFAULT_MAX_RETRIES


def test_one_retry_remains_while_attempts_are_below_the_ceiling() -> None:
    patch = plan_after_failure(retry_count=DEFAULT_MAX_RETRIES - 2, reason=TRANSIENT)
    assert patch["status"] == STATUS_PENDING
    assert patch["next_run_at"] is not None


def test_error_text_is_recorded_and_bounded() -> None:
    patch = plan_after_failure(reason=TRANSIENT, error="x" * 9000)
    assert len(patch["error"]) == 5000


def test_error_field_is_omitted_when_there_is_nothing_to_say() -> None:
    patch = plan_after_failure(reason=TRANSIENT, error="")
    assert "error" not in patch


def test_unknown_reason_is_rejected() -> None:
    with pytest.raises(ValueError):
        plan_after_failure(reason="mystery")


def test_timestamp_format_matches_the_runner() -> None:
    assert PB_DATE.match(to_pb_date(datetime(2026, 9, 27, 10, 4, 5, tzinfo=timezone.utc)))
