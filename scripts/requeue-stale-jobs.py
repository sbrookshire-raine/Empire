"""Reap stale ingestion_jobs: requeue what can still succeed, quarantine what cannot (P3).

Replaces "close every stale running job as failed". That was wrong in both directions: an interrupted job (Ctrl-C,
reboot, Ollama restart, a killed worker) is not a failure, and closing it terminally discarded work a retry would
have finished. It is also why 14 of 544 rows sat in `running` with nothing able to act on them.

    python scripts/requeue-stale-jobs.py                      # review: stale + quarantined, no writes
    python scripts/requeue-stale-jobs.py --apply              # requeue / quarantine
    python scripts/requeue-stale-jobs.py --apply -m 60        # only rows running > 60 min

Deliberately a script, not a Toolbelt tool: it is an operator/mechanic path, it runs on CPU, and adding a limb
would spend Eve's prompt budget (Lens B) for something she can already do through the generic `pb_update_record`.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timedelta
from typing import Any

import httpx

from pipeline.config import (  # noqa: F401  (ROOT keeps cwd-independent imports working)
    POCKETBASE_URL,
    ROOT,
)
from pipeline.job_schedule import (
    DEFAULT_MAX_RETRIES,
    INTERRUPTED,
    STATUS_DEAD_LETTER,
    STATUS_PENDING,
    plan_after_failure,
    to_pb_date,
    utc_now,
)

RECORDS = f"{POCKETBASE_URL}/api/collections/ingestion_jobs/records"


def _list(client: httpx.Client, filter_expr: str, per_page: int) -> list[dict[str, Any]]:
    response = client.get(RECORDS, params={"filter": filter_expr, "perPage": per_page})
    response.raise_for_status()
    return response.json().get("items", [])


def _name(job: dict[str, Any]) -> str:
    return str(job.get("source_file") or "").rsplit("/", 1)[-1].rsplit("\\", 1)[-1] or "(no file)"


def _plan(job: dict[str, Any], now: datetime) -> dict[str, Any]:
    """An interrupted row resumes where its counter left off, rather than restarting the count."""
    return plan_after_failure(
        retry_count=int(job.get("retry_count") or 0),
        max_retries=int(job.get("max_retries") or DEFAULT_MAX_RETRIES),
        reason=INTERRUPTED,
        error="Auto-closed: process interrupted while running (retry scheduled).",
        now=now,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Requeue or quarantine stale ingestion_jobs")
    parser.add_argument("--apply", action="store_true", help="Write changes (default is a dry run)")
    parser.add_argument(
        "-m",
        "--older-than-minutes",
        type=int,
        default=10,
        help="How long a job must have been running to count as stale (default 10)",
    )
    parser.add_argument("--limit", type=int, default=200, help="Max rows per pass (default 200)")
    args = parser.parse_args(argv)

    now = utc_now()
    cutoff = to_pb_date(now - timedelta(minutes=args.older_than_minutes))

    try:
        with httpx.Client(timeout=30.0) as client:
            stale = _list(client, f"status='running' && started_at<'{cutoff}'", args.limit)
            quarantined = _list(client, f"status='{STATUS_DEAD_LETTER}'", args.limit)

            print(f"stale running rows (started before {cutoff}): {len(stale)}")
            print(f"quarantined rows ({STATUS_DEAD_LETTER}): {len(quarantined)}")
            print()

            if stale:
                print("STALE -> DECISION")
                for job in stale:
                    patch = _plan(job, now)
                    verdict = (
                        f"{patch['status']} (attempt {patch['retry_count']}"
                        + (f", retry at {patch['next_run_at']}" if patch["next_run_at"] else ", no retry")
                        + ")"
                    )
                    print(f"  {_name(job)[:56]:<56} {verdict}")
                    if args.apply:
                        response = client.patch(f"{RECORDS}/{job['id']}", json=patch)
                        response.raise_for_status()

            if quarantined:
                print()
                print("QUARANTINED - needs a human, or a deliberate requeue:")
                for job in quarantined:
                    reason = job.get("failure_reason") or "?"
                    error = str(job.get("error") or "")[:80]
                    print(f"  {_name(job)[:56]:<56} {reason}: {error}")

    except httpx.HTTPError as exc:
        print(f"PocketBase unreachable at {POCKETBASE_URL}: {exc}", file=sys.stderr)
        return 2

    print()
    if args.apply:
        print(f"Applied. Requeued rows are 'pending' with a next_run_at; exhausted rows are '{STATUS_DEAD_LETTER}'.")
        print("'pending' is the state a runner picks up - see docs/WORK_PLAN.md P3.")
    else:
        print("Dry run - nothing written. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
