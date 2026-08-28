"""Resumable, checkpointed Wikipedia -> Cognee ingestion.

Reads Markdown batches from D:\\wiki_md (or a Weaviate export staging dir), normalizes each
article (reusing frontmatter as ground-truth edges), and stores it in Cognee via the shared
lock-protected client. One aggregated PocketBase ``ingestion_jobs`` record is written per
batch. Resumes from the checkpoint so interrupted runs skip completed files.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import httpx
from dotenv import load_dotenv

from pipeline.cognee_client import (
    IngestMode,
    cognify_dataset,
    embed_dataset,
    improve,
    remember_many,
)
from pipeline.config import POCKETBASE_URL, ROOT
from pipeline.wiki_checkpoint import (
    batch_key,
    get_next_index,
    load_checkpoint,
    save_checkpoint,
    update_batch,
)
from pipeline.wiki_normalizer import normalize_wiki_file

load_dotenv(ROOT / ".env.local")
load_dotenv(ROOT / ".env")

DEFAULT_WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", r"D:\wiki_md"))
RESULT_SENTINEL = "__WIKI_RESULT__"


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.000Z")


def resolve_batch_dir(root: Path, year: str, batch: str) -> Path:
    """Accept ``0`` / ``00000`` / ``batch_00000`` and resolve to the batch directory."""
    name = batch
    if not name.startswith("batch_"):
        name = f"batch_{int(batch):05d}"
    return root / year / name


async def _pb_create_batch_job(source_file: str) -> str | None:
    payload = {
        "source_type": "wikipedia",
        "source_file": source_file[:500],
        "status": "running",
        "started_at": _utc_now_iso(),
    }
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{POCKETBASE_URL}/api/collections/ingestion_jobs/records",
                json=payload,
            )
            response.raise_for_status()
            return response.json()["id"]
    except Exception as exc:  # noqa: BLE001 — PB logging must never block ingest
        print(f"[wiki] WARN: PocketBase job create failed: {exc}", file=sys.stderr, flush=True)
        return None


async def _pb_finish_batch_job(
    job_id: str | None,
    *,
    status: str,
    records_ingested: int,
    error: str = "",
) -> None:
    if not job_id:
        return
    payload: dict[str, str | int] = {
        "status": status,
        "records_ingested": records_ingested,
        "finished_at": _utc_now_iso(),
    }
    if error:
        payload["error"] = error[:5000]
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.patch(
                f"{POCKETBASE_URL}/api/collections/ingestion_jobs/records/{job_id}",
                json=payload,
            )
            response.raise_for_status()
    except Exception as exc:  # noqa: BLE001
        print(f"[wiki] WARN: PocketBase job update failed: {exc}", file=sys.stderr, flush=True)


async def ingest_batch(
    *,
    year: str,
    batch: str,
    root: Path,
    mode: IngestMode,
    dataset: str,
    limit: int,
    resume: bool,
    flush_every: int,
) -> dict:
    batch_dir = resolve_batch_dir(root, year, batch)
    if not batch_dir.is_dir():
        raise FileNotFoundError(f"Batch directory not found: {batch_dir}")

    files = sorted(p for p in batch_dir.iterdir() if p.is_file() and p.suffix.lower() == ".md")
    total = len(files)
    if total == 0:
        raise FileNotFoundError(f"No .md files in {batch_dir}")

    key = batch_key(year, batch_dir.name)
    state = load_checkpoint()
    start_index = get_next_index(state, key) if resume else 0
    if start_index >= total:
        return {
            "batch": key,
            "dataset": dataset,
            "mode": mode,
            "status": "already_complete",
            "total": total,
            "processed": 0,
            "start_index": start_index,
        }

    end_index = total if limit <= 0 else min(total, start_index + limit)
    source_file = str(batch_dir)
    job_id = await _pb_create_batch_job(source_file)

    processed = 0
    started = time.perf_counter()
    current_index = start_index
    remember_complete = False
    remember_seconds = 0.0
    embed_seconds = 0.0
    cognify_seconds = 0.0
    pending_docs: list[str] = []
    pending_end_index = start_index
    try:
        def _remember_concurrency() -> int:
            raw = os.environ.get("EMPIRE_REMEMBER_CONCURRENCY", "8").strip()
            try:
                return max(1, int(raw))
            except ValueError:
                return 8

        async def _flush_pending() -> None:
            nonlocal processed, pending_docs, pending_end_index, state
            if not pending_docs:
                return
            count = len(pending_docs)
            # Concurrent cognee.add under Postgres (EMPIRE_REMEMBER_CONCURRENCY).
            await remember_many(pending_docs, dataset=dataset, mode="fast")
            processed += count
            update_batch(
                state,
                key,
                next_index=pending_end_index,
                processed=int(state["batches"].get(key, {}).get("processed", 0)) + count,
                mode=mode,
                dataset=dataset,
                status="in_progress",
                total=total,
            )
            save_checkpoint(state)
            elapsed = time.perf_counter() - started
            rate = (processed / elapsed) if elapsed > 0 else 0.0
            print(
                f"[wiki] {key}: {processed}/{end_index - start_index} "
                f"(idx {pending_end_index}, {rate:.2f} docs/s remember "
                f"conc={_remember_concurrency()})",
                flush=True,
            )
            pending_docs = []

        remember_t0 = time.perf_counter()
        # Normalize a flush window concurrently (CPU/disk), then concurrent remember.
        window = flush_every
        idx = start_index
        while idx < end_index:
            chunk_end = min(end_index, idx + window)
            chunk_paths = [(i, files[i]) for i in range(idx, chunk_end)]

            async def _normalize_one(item: tuple[int, Path]) -> tuple[int, str]:
                i, path = item
                normalized = await asyncio.to_thread(
                    normalize_wiki_file,
                    path,
                    dataset=dataset,
                    mode=mode,
                    fallback_year=year,
                )
                return i, str(normalized["document"])

            normalized_docs = await asyncio.gather(
                *[_normalize_one(item) for item in chunk_paths]
            )
            normalized_docs.sort(key=lambda pair: pair[0])
            pending_docs = [doc for _, doc in normalized_docs]
            pending_end_index = chunk_end
            current_index = chunk_end - 1
            await _flush_pending()
            idx = chunk_end

        remember_seconds = time.perf_counter() - remember_t0

        remember_complete = True
        # Fast Mode (Hybrid): remember + Truth-Drift edges + nomic embed only.
        # CRITICAL: do NOT run cognify_dataset / improve — that is llama3.1 graph extract.
        # Deep reasoning is deferred to runtime. PocketBase + checkpoint unchanged below.
        if mode == "full":
            print(f"[wiki] {key}: cognifying {processed} docs into '{dataset}'...", flush=True)
            cognify_t0 = time.perf_counter()
            await cognify_dataset(dataset)
            print(f"[wiki] {key}: running graph enrichment (memify)...", flush=True)
            await improve(dataset=dataset)
            cognify_seconds = time.perf_counter() - cognify_t0
        else:
            print(
                f"[wiki] {key}: fast mode — embedding {processed} docs "
                f"(nomic-embed-text; skip llama cognify/improve) into '{dataset}'...",
                flush=True,
            )
            embed_t0 = time.perf_counter()
            await embed_dataset(dataset)
            embed_seconds = time.perf_counter() - embed_t0
            # await cognify_dataset(dataset)  # intentionally bypassed in fast mode
            # await improve(dataset=dataset)  # intentionally bypassed in fast mode

        final_index = end_index
        completed = final_index >= total
        prior_processed = int(state["batches"].get(key, {}).get("processed", 0))
        # pending flushes already advanced processed; do not double-count on final write
        update_batch(
            state,
            key,
            next_index=final_index,
            processed=prior_processed,
            mode=mode,
            dataset=dataset,
            status="complete" if completed else "in_progress",
            total=total,
        )
        save_checkpoint(state)

        elapsed = time.perf_counter() - started
        rate = round(processed / elapsed, 2) if processed and elapsed > 0 else 0.0
        remember_rate = (
            round(processed / remember_seconds, 2) if processed and remember_seconds > 0 else 0.0
        )
        print(
            f"[wiki] {key}: done in {elapsed:.1f}s ({rate} docs/s, {elapsed / max(processed, 1):.1f}s/doc)",
            flush=True,
        )
        print(
            f"[wiki] DIAG remember={remember_seconds:.1f}s ({remember_rate} docs/s) "
            f"embed={embed_seconds:.1f}s cognify={cognify_seconds:.1f}s "
            f"docs={processed} flush_every={flush_every}",
            flush=True,
        )
        await _pb_finish_batch_job(job_id, status="success", records_ingested=processed)
        return {
            "batch": key,
            "dataset": dataset,
            "mode": mode,
            "status": "complete" if completed else "partial",
            "total": total,
            "processed": processed,
            "start_index": start_index,
            "next_index": final_index,
            "seconds": round(elapsed, 1),
            "docs_per_sec": rate,
            "remember_seconds": round(remember_seconds, 1),
            "embed_seconds": round(embed_seconds, 1),
            "cognify_seconds": round(cognify_seconds, 1),
            "remember_docs_per_sec": remember_rate,
            "pb_job": job_id,
        }
    except Exception as exc:  # noqa: BLE001
        # Full-mode cognify flake after remembers: retry the same slice.
        # Fast mode embed flake after remembers: also retry slice (vectors may be partial).
        if remember_complete:
            resume_at = start_index
        else:
            resume_at = pending_end_index if not pending_docs else pending_end_index - len(pending_docs)
            if resume_at < start_index:
                resume_at = current_index
        update_batch(
            state,
            key,
            next_index=resume_at,
            processed=int(state["batches"].get(key, {}).get("processed", 0))
            if remember_complete
            else int(state["batches"].get(key, {}).get("processed", 0)),
            mode=mode,
            dataset=dataset,
            status="error",
            total=total,
        )
        save_checkpoint(state)
        await _pb_finish_batch_job(
            job_id, status="failed", records_ingested=processed, error=str(exc)
        )
        raise


def _print_result(result: dict) -> None:
    print(
        f"[wiki] {result['batch']}: {result['status']} "
        f"processed={result['processed']}/{result['total']} dataset={result['dataset']}",
        flush=True,
    )
    print(RESULT_SENTINEL + json.dumps(result), flush=True)


async def ingest_flat_dir(
    *,
    directory: Path,
    mode: IngestMode,
    dataset: str,
    limit: int,
    resume: bool,
    flush_every: int,
) -> dict:
    """Ingest a flat directory of .md files (e.g. Weaviate export staging)."""
    if not directory.is_dir():
        raise FileNotFoundError(f"Export directory not found: {directory}")
    files = sorted(p for p in directory.iterdir() if p.is_file() and p.suffix.lower() == ".md")
    total = len(files)
    if total == 0:
        raise FileNotFoundError(f"No .md files in {directory}")

    key = f"export/{directory.name}"
    state = load_checkpoint()
    start_index = get_next_index(state, key) if resume else 0
    if start_index >= total:
        return {
            "batch": key,
            "dataset": dataset,
            "mode": mode,
            "status": "already_complete",
            "total": total,
            "processed": 0,
            "start_index": start_index,
        }

    end_index = total if limit <= 0 else min(total, start_index + limit)
    job_id = await _pb_create_batch_job(str(directory))
    processed = 0
    started = time.perf_counter()
    current_index = start_index
    remember_complete = False
    remember_seconds = 0.0
    embed_seconds = 0.0
    cognify_seconds = 0.0
    pending_docs: list[str] = []
    pending_end_index = start_index
    try:
        async def _flush_pending() -> None:
            nonlocal processed, pending_docs, pending_end_index, state
            if not pending_docs:
                return
            count = len(pending_docs)
            await remember_many(pending_docs, dataset=dataset, mode="fast")
            processed += count
            update_batch(
                state,
                key,
                next_index=pending_end_index,
                processed=int(state["batches"].get(key, {}).get("processed", 0)) + count,
                mode=mode,
                dataset=dataset,
                status="in_progress",
                total=total,
            )
            save_checkpoint(state)
            elapsed = time.perf_counter() - started
            rate = (processed / elapsed) if elapsed > 0 else 0.0
            print(
                f"[wiki] {key}: {processed}/{end_index - start_index} "
                f"(idx {pending_end_index}, {rate:.2f} docs/s remember)",
                flush=True,
            )
            pending_docs = []

        remember_t0 = time.perf_counter()
        window = flush_every
        idx = start_index
        while idx < end_index:
            chunk_end = min(end_index, idx + window)
            chunk_paths = [(i, files[i]) for i in range(idx, chunk_end)]

            async def _normalize_one(item: tuple[int, Path]) -> tuple[int, str]:
                i, path = item
                normalized = await asyncio.to_thread(
                    normalize_wiki_file,
                    path,
                    dataset=dataset,
                    mode=mode,
                )
                return i, str(normalized["document"])

            normalized_docs = await asyncio.gather(
                *[_normalize_one(item) for item in chunk_paths]
            )
            normalized_docs.sort(key=lambda pair: pair[0])
            pending_docs = [doc for _, doc in normalized_docs]
            pending_end_index = chunk_end
            current_index = chunk_end - 1
            await _flush_pending()
            idx = chunk_end

        remember_seconds = time.perf_counter() - remember_t0
        remember_complete = True
        if mode == "full":
            print(f"[wiki] {key}: cognifying {processed} docs into '{dataset}'...", flush=True)
            cognify_t0 = time.perf_counter()
            await cognify_dataset(dataset)
            await improve(dataset=dataset)
            cognify_seconds = time.perf_counter() - cognify_t0
        else:
            print(
                f"[wiki] {key}: fast mode — embedding {processed} docs "
                f"(nomic-embed-text; skip llama cognify/improve) into '{dataset}'...",
                flush=True,
            )
            embed_t0 = time.perf_counter()
            await embed_dataset(dataset)
            embed_seconds = time.perf_counter() - embed_t0
            # await cognify_dataset(dataset)  # intentionally bypassed in fast mode
            # await improve(dataset=dataset)  # intentionally bypassed in fast mode
        completed = end_index >= total
        prior = int(state["batches"].get(key, {}).get("processed", 0))
        update_batch(
            state,
            key,
            next_index=end_index,
            processed=prior,
            mode=mode,
            dataset=dataset,
            status="complete" if completed else "in_progress",
            total=total,
        )
        save_checkpoint(state)
        elapsed = time.perf_counter() - started
        remember_rate = (
            round(processed / remember_seconds, 2) if processed and remember_seconds > 0 else 0.0
        )
        print(
            f"[wiki] DIAG remember={remember_seconds:.1f}s ({remember_rate} docs/s) "
            f"embed={embed_seconds:.1f}s cognify={cognify_seconds:.1f}s "
            f"docs={processed} flush_every={flush_every}",
            flush=True,
        )
        await _pb_finish_batch_job(job_id, status="success", records_ingested=processed)
        return {
            "batch": key, "dataset": dataset, "mode": mode,
            "status": "complete" if completed else "partial",
            "total": total, "processed": processed, "start_index": start_index,
            "next_index": end_index, "seconds": round(elapsed, 1),
            "remember_seconds": round(remember_seconds, 1),
            "embed_seconds": round(embed_seconds, 1),
            "cognify_seconds": round(cognify_seconds, 1),
            "remember_docs_per_sec": remember_rate,
            "pb_job": job_id,
        }
    except Exception as exc:  # noqa: BLE001
        if remember_complete:
            resume_at = start_index
        else:
            resume_at = (
                pending_end_index - len(pending_docs) if pending_docs else pending_end_index
            )
            if resume_at < start_index:
                resume_at = current_index
        update_batch(
            state, key, next_index=resume_at,
            processed=int(state["batches"].get(key, {}).get("processed", 0)),
            mode=mode, dataset=dataset, status="error", total=total,
        )
        save_checkpoint(state)
        await _pb_finish_batch_job(job_id, status="failed", records_ingested=processed, error=str(exc))
        raise


async def drain_priority_resolved(
    *,
    year: str,
    mode: IngestMode,
    dataset: str,
    flush_every: int = 50,
) -> dict:
    """Ingest awaiting priority_resolved.jsonl paths before linear checkpoint work."""
    from pipeline.wiki_priority_resolved import (
        list_awaiting,
        load_resolved_lines,
        save_resolved_lines,
    )

    awaiting = list_awaiting(year)
    if not awaiting:
        print(f"[wiki] priority drain: no awaiting rows for year={year}", flush=True)
        return {"drained": 0, "failed": 0, "skipped": 0, "message": "empty_or_missing"}

    pending_docs: list[str] = []
    flush_every = max(1, flush_every)

    async def _flush() -> None:
        nonlocal pending_docs
        if not pending_docs:
            return
        await remember_many(pending_docs, dataset=dataset, mode="fast" if mode == "fast" else "full")
        pending_docs = []

    async def _ingest_one(row: dict) -> str:
        path = Path(str(row.get("path") or ""))
        if not path.is_file():
            print(f"[wiki] priority drain: missing path {path}", flush=True)
            return "failed"
        try:
            normalized = await asyncio.to_thread(
                normalize_wiki_file,
                path,
                dataset=dataset,
                mode=mode,
                fallback_year=year,
            )
            pending_docs.append(str(normalized["document"]))
            if len(pending_docs) >= flush_every:
                await _flush()
            return "ingested"
        except Exception as exc:  # noqa: BLE001
            print(f"[wiki] priority drain failed {path}: {exc}", file=sys.stderr, flush=True)
            return "failed"

    lines = load_resolved_lines(year)
    awaiting_idx = [
        (i, line)
        for i, line in enumerate(lines)
        if line.get("ingest_status") == "awaiting"
    ]
    awaiting_idx.sort(
        key=lambda pair: (
            int(pair[1].get("subject_rank") or 10_000),
            str(pair[1].get("queued_at") or ""),
        )
    )
    drained = failed = skipped = 0
    seen: set[str] = set()
    for idx, line in awaiting_idx:
        identity = (
            str(line.get("page_id") or "").strip()
            or str(line.get("path") or "").strip().casefold()
            or str(line.get("title") or "").strip().casefold()
        )
        if identity and identity in seen:
            lines[idx]["ingest_status"] = "skipped_already_done"
            skipped += 1
            continue
        if identity:
            seen.add(identity)
        status = await _ingest_one(line)
        lines[idx]["ingest_status"] = status
        if status == "ingested":
            drained += 1
        elif status == "skipped_already_done":
            skipped += 1
        else:
            failed += 1
    await _flush()
    if drained and mode == "fast":
        await embed_dataset(dataset)
    elif drained and mode == "full":
        await cognify_dataset(dataset)
        await improve(dataset=dataset)
    save_resolved_lines(year, lines)
    print(
        f"[wiki] priority drain done: drained={drained} failed={failed} skipped={skipped}",
        flush=True,
    )
    return {"drained": drained, "failed": failed, "skipped": skipped}


async def _async_main(args: argparse.Namespace) -> int:
    mode: IngestMode = "full" if args.mode == "full" else "fast"
    # Truth-Drift: default per-snapshot dataset to wikipedia_<year> so years never collide.
    if args.export_dir:
        dataset = args.dataset or "wikipedia_weaviate"
    else:
        dataset = args.dataset or (f"wikipedia_{args.year}" if args.year else "wikipedia")

    if getattr(args, "drain_priorities", False):
        if not args.year:
            raise ValueError("--year is required with --drain-priorities")
        from pipeline.wiki_priority_resolved import list_awaiting

        if not list_awaiting(str(args.year)):
            print(
                f"[wiki] priority drain: no awaiting rows for year={args.year}",
                flush=True,
            )
            if not args.batch and not args.export_dir:
                return 0
        else:
            result = await drain_priority_resolved(
                year=str(args.year),
                mode=mode,
                dataset=dataset,
                flush_every=max(1, args.flush_every),
            )
            _print_result(result)
            if not args.batch and not args.export_dir:
                return 0

    if args.export_dir:
        export_dir = Path(args.export_dir)
        if not export_dir.is_absolute():
            export_dir = ROOT / export_dir
        result = await ingest_flat_dir(
            directory=export_dir,
            mode=mode,
            dataset=dataset,
            limit=args.limit,
            resume=not args.no_resume,
            flush_every=max(1, args.flush_every),
        )
        _print_result(result)
        return 0

    if not args.year or not args.batch:
        raise ValueError("--year and --batch are required unless --export-dir is set")

    root = Path(args.root) if args.root else DEFAULT_WIKI_ROOT
    result = await ingest_batch(
        year=str(args.year),
        batch=str(args.batch),
        root=root,
        mode=mode,
        dataset=dataset,
        limit=args.limit,
        resume=not args.no_resume,
        flush_every=max(1, args.flush_every),
    )
    _print_result(result)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Resumable Wikipedia -> Cognee ingestion")
    parser.add_argument("--year", default="", help="Snapshot year folder, e.g. 2026")
    parser.add_argument("--batch", default="", help="Batch index/name, e.g. 0 or batch_00000")
    parser.add_argument("--root", default="", help=r"Wiki root (default D:\wiki_md or $WIKI_ROOT)")
    parser.add_argument("--export-dir", default="", help="Flat dir of exported .md (Weaviate staging)")
    parser.add_argument("--mode", choices=["fast", "full"], default="fast")
    parser.add_argument(
        "--dataset",
        default="",
        help="Cognee dataset (default: wikipedia_<year>, or wikipedia_weaviate for --export-dir)",
    )
    parser.add_argument("--limit", type=int, default=0, help="Max files this run (0 = all remaining)")
    parser.add_argument("--no-resume", action="store_true", help="Ignore checkpoint; start at 0")
    parser.add_argument("--flush-every", type=int, default=25, help="Checkpoint flush cadence")
    parser.add_argument(
        "--drain-priorities",
        action="store_true",
        help="Drain priority_resolved.jsonl awaiting rows (before linear batch if also set)",
    )
    args = parser.parse_args()

    try:
        return asyncio.run(_async_main(args))
    except Exception as exc:  # noqa: BLE001
        import traceback

        message = str(exc)
        if "Could not set lock" in message or "database lock" in message:
            print(
                "ERROR: Cognee database lock conflict. Another ingest or MCP tool is using "
                f"the graph - wait and retry.\n  Detail: {message}",
                file=sys.stderr,
            )
        else:
            print(f"ERROR: {exc}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
