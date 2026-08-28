"""Isolated Cognee worker — run as subprocess to avoid Kuzu DB lock conflicts."""

from __future__ import annotations

import argparse
import asyncio
import inspect
import json
import sys
from pathlib import Path

from pipeline.cognee_client import (
    forget,
    improve,
    load_cognee_env,
    recall,
    remember,
)
from pipeline.ingest_files import ingest_files_async

load_cognee_env()

import cognee
import cognee.shared.utils as cognee_utils
from cognee.infrastructure.databases.cache.get_cache_engine import close_cache_engine
from litellm.llms.custom_httpx.async_client_cleanup import close_litellm_async_clients


async def _close_cognee_resources() -> None:
    """Release Cognee/litellm aiohttp sessions so short-lived workers exit cleanly."""
    try:
        await close_cache_engine()
    except Exception:  # noqa: BLE001
        pass

    try:
        session = cognee_utils._telemetry_session
        if session is not None and not session.closed:
            await session.close()
        cognee_utils._telemetry_session = None
        cognee_utils._telemetry_session_loop = None
    except Exception:  # noqa: BLE001
        pass

    try:
        await close_litellm_async_clients()
    except Exception:  # noqa: BLE001
        pass

    try:
        close = getattr(cognee, "close", None)
        if callable(close):
            result = close()
            if inspect.isawaitable(result):
                await result
    except Exception:  # noqa: BLE001
        pass


async def _dispatch(args: argparse.Namespace) -> int:
    if args.command == "ingest-files":
        result = await ingest_files_async(
            [Path(path) for path in args.path],
            args.dataset,
            args.job_id,
            args.full_graph,
        )
        print(json.dumps(result, default=str))
        return 0

    if args.command == "remember":
        await remember(args.content, dataset=args.dataset)
        print(json.dumps({"status": "stored", "dataset": args.dataset}))
        return 0

    if args.command == "recall":
        dataset = args.dataset or None
        results = await recall(args.query, dataset=dataset)
        print(json.dumps({"query": args.query, "dataset": dataset, "results": results}, default=str))
        return 0

    if args.command == "improve":
        await improve(dataset=args.dataset)
        print(json.dumps({"status": "improved", "dataset": args.dataset}))
        return 0

    if args.command == "forget":
        removed = await forget(dataset=args.dataset)
        print(
            json.dumps(
                {
                    "status": "forgotten" if removed else "absent",
                    "dataset": args.dataset,
                    "removed": removed,
                }
            )
        )
        return 0

    raise ValueError(f"Unknown command: {args.command}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Cognee subprocess worker")
    sub = parser.add_subparsers(dest="command", required=True)

    remember_parser = sub.add_parser("remember")
    remember_parser.add_argument("--content", required=True)
    remember_parser.add_argument("--dataset", default="mock")

    recall_parser = sub.add_parser("recall")
    recall_parser.add_argument("--query", required=True)
    recall_parser.add_argument("--dataset", default="")

    improve_parser = sub.add_parser("improve")
    improve_parser.add_argument("--dataset", default="mock")

    forget_parser = sub.add_parser("forget")
    forget_parser.add_argument("--dataset", default="mock")

    ingest_parser = sub.add_parser("ingest-files")
    ingest_parser.add_argument("--path", action="append", required=True)
    ingest_parser.add_argument("--dataset", required=True)
    ingest_parser.add_argument("--job-id", required=True)
    ingest_parser.add_argument("--full-graph", action="store_true")

    args = parser.parse_args()

    async def _run() -> int:
        try:
            return await _dispatch(args)
        finally:
            await _close_cognee_resources()

    try:
        return asyncio.run(_run())
    except Exception as exc:  # noqa: BLE001
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
