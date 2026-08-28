"""Stub-first local ingestion: mock_data_ingest -> Cognee graph memory."""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import httpx
from dotenv import load_dotenv

from pipeline.cognee_client import IngestMode, embed_dataset, improve, remember
from pipeline.config import MOCK_DATA_DIR, POCKETBASE_URL, ROOT
from pipeline.normalizer import normalize_file

load_dotenv(ROOT / ".env.local")
load_dotenv(ROOT / ".env")


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.000Z")


async def _pb_create_job(source_type: str, source_file: str) -> str:
    payload = {
        "source_type": source_type,
        "source_file": source_file,
        "status": "running",
        "started_at": _utc_now_iso(),
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            f"{POCKETBASE_URL}/api/collections/ingestion_jobs/records",
            json=payload,
        )
        response.raise_for_status()
        return response.json()["id"]


async def _pb_update_job(
    job_id: str,
    *,
    status: str,
    records_ingested: int = 0,
    error: str = "",
) -> None:
    payload: dict[str, str | int] = {
        "status": status,
        "records_ingested": records_ingested,
        "finished_at": _utc_now_iso(),
    }
    if error:
        payload["error"] = error[:5000]

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.patch(
            f"{POCKETBASE_URL}/api/collections/ingestion_jobs/records/{job_id}",
            json=payload,
        )
        response.raise_for_status()


async def ingest_file(path: Path, mode: IngestMode = "fast") -> dict[str, str | int]:
    """Hybrid Fast Mode (default): normalize + remember only.

    Fast path intentionally skips Cognee cognify / improve (llama3.1 graph extract).
    Deep LLM reasoning is deferred to runtime. PocketBase ingestion_jobs still
    track running → success/failed for resume visibility.
    """
    normalized = normalize_file(path)
    job_id = await _pb_create_job(
        str(normalized["source_type"]),
        str(normalized["source_file"]),
    )

    started = time.perf_counter()
    try:
        document = str(normalized["document"])
        dataset = str(normalized["dataset"])
        if mode == "fast":
            print(f"[ingest] {path.name}: fast store (remember only; no LLM graph)...", flush=True)
        else:
            print(f"[ingest] {path.name}: full graph extract via Ollama (~2 min)...", flush=True)

        # Fast Mode: remember (add) + nomic embed — never llama3.1 cognify/improve.
        # Full Mode: remember(..., mode="full") runs cognify inside cognee_client.
        await remember(document, dataset=dataset, mode=mode)

        if mode == "full":
            print(f"[ingest] {path.name}: running graph enrichment...", flush=True)
            await improve(dataset=dataset)
        else:
            # Base embeddings via nomic-embed-text (chunk + vector index only).
            # await cognify_dataset / improve intentionally skipped — deferred to runtime.
            print(f"[ingest] {path.name}: fast embed (nomic-embed-text)...", flush=True)
            await embed_dataset(dataset)

        elapsed = time.perf_counter() - started
        await _pb_update_job(job_id, status="success", records_ingested=1)
        print(f"[ingest] {path.name}: done in {elapsed:.1f}s", flush=True)
        return {
            "job_id": job_id,
            "external_id": str(normalized["external_id"]),
            "dataset": dataset,
            "status": "success",
            "mode": mode,
            "seconds": round(elapsed, 1),
        }
    except Exception as exc:  # noqa: BLE001
        await _pb_update_job(job_id, status="failed", error=str(exc))
        raise


async def ingest_directory(
    directory: Path,
    concurrency: int = 8,
    mode: IngestMode = "fast",
) -> list[dict[str, str | int]]:
    files = sorted(
        p for p in directory.iterdir() if p.is_file() and p.suffix.lower() in {".json", ".md"}
    )
    if not files:
        raise FileNotFoundError(f"No .json or .md files found in {directory}")

    # Postgres unlocks concurrent remember/add; cap with --concurrency / EMPIRE_REMEMBER_CONCURRENCY.
    env_conc = os.environ.get("EMPIRE_REMEMBER_CONCURRENCY", "").strip()
    if env_conc:
        try:
            concurrency = max(1, int(env_conc))
        except ValueError:
            pass
    concurrency = max(1, concurrency)
    sem = asyncio.Semaphore(concurrency)
    results: list[dict[str, str | int] | None] = [None] * len(files)

    async def _one(index: int, file_path: Path) -> None:
        async with sem:
            results[index] = await ingest_file(file_path, mode=mode)

    await asyncio.gather(*[_one(i, path) for i, path in enumerate(files)])
    return [r for r in results if r is not None]


def _resolve_path(raw: str) -> Path:
    path = Path(raw)
    if not path.is_absolute():
        path = ROOT / path
    return path.resolve()


async def _async_main(args: argparse.Namespace) -> int:
    mode: IngestMode = "full" if args.full_graph else "fast"

    if args.file:
        result = await ingest_file(_resolve_path(args.file), mode=mode)
        print(
            f"Ingested {result['external_id']} -> dataset={result['dataset']} "
            f"mode={result['mode']} job={result['job_id']} ({result['seconds']}s)"
        )
        return 0

    directory = _resolve_path(args.directory)
    results = await ingest_directory(directory, concurrency=args.concurrency, mode=mode)
    for result in results:
        print(
            f"Ingested {result['external_id']} -> dataset={result['dataset']} "
            f"mode={result['mode']} job={result['job_id']} ({result['seconds']}s)"
        )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest local mock files into Cognee")
    parser.add_argument("--file", help="Path to a single .json or .md mock file")
    parser.add_argument(
        "--directory",
        default=str(MOCK_DATA_DIR),
        help="Directory of mock files (default: mock_data_ingest/)",
    )
    parser.add_argument(
        "--full-graph",
        action="store_true",
        help="Run slow Ollama graph extraction (~2 min/file). Default is fast store.",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=8,
        help="Parallel ingest cap for directory mode (Postgres default 8; was 1 under SQLite)",
    )
    args = parser.parse_args()

    try:
        return asyncio.run(_async_main(args))
    except Exception as exc:  # noqa: BLE001
        message = str(exc)
        if "Could not set lock" in message:
            print(
                "ERROR: Cognee database lock conflict.\n"
                "  Another ingest or MCP tool is using the graph — wait and retry.\n"
                f"  Detail: {message}",
                file=sys.stderr,
            )
        else:
            print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
