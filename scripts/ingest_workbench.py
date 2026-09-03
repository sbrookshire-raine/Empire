#!/usr/bin/env python3
"""Batch-ingest Empire Workbench notes and skills into Cognee eve_memory on V:\\Cognee."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
import uuid
from pathlib import Path

from pipeline.ingest_files import MAX_BATCH_FILES, _load_content_index

WORKBENCH_ROOT = Path(r"C:\Empire_Workbench")
EMPIRE_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FOLDERS = (
    WORKBENCH_ROOT / "01_Memory_Bank",
    WORKBENCH_ROOT / "02_Skills_and_Prompts",
)
# Cognee ingest pipeline supports .md and .txt only (not .csv despite harvester collecting them).
ALLOWED_SUFFIXES = {".md", ".txt"}
PROGRESS_FILE = WORKBENCH_ROOT / "ingest_progress.json"
SKIP_LOG = WORKBENCH_ROOT / "ingest_skipped_files.txt"
INGEST_TIMEOUT_SECONDS = 600
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 15


def content_index_path() -> Path:
    local_app_data = os.environ.get("LOCALAPPDATA")
    base = Path(local_app_data) if local_app_data else Path.home() / "AppData" / "Local"
    return base / "EMPIRE" / "memory-jobs" / "content-index.json"


def file_content_hash(path: Path) -> str:
    body = path.read_text(encoding="utf-8")
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def is_ingestible_text(path: Path) -> bool:
    """Skip empty, binary, or whitespace-only text files."""
    try:
        if path.stat().st_size == 0:
            return False
        body = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return False
    return bool(body.strip())


def log_skipped(path: Path, reason: str) -> None:
    SKIP_LOG.parent.mkdir(parents=True, exist_ok=True)
    with SKIP_LOG.open("a", encoding="utf-8") as handle:
        handle.write(f"{path}\t{reason}\n")


def collect_files(folders: list[Path]) -> list[Path]:
    files: list[Path] = []
    for folder in folders:
        if not folder.is_dir():
            print(f"SKIP missing folder: {folder}", file=sys.stderr)
            continue
        for path in sorted(folder.rglob("*")):
            if not path.is_file():
                continue
            suffix = path.suffix.lower()
            if suffix == ".csv":
                log_skipped(path, "csv_not_supported_by_cognee")
                continue
            if suffix not in ALLOWED_SUFFIXES:
                continue
            if not is_ingestible_text(path):
                log_skipped(path, "empty_or_non_utf8")
                continue
            files.append(path)
    return files


def filter_pending(files: list[Path], dataset: str) -> tuple[list[Path], int]:
    """Return files not yet embedded, using the same content-hash keys as ingest_files."""
    index = _load_content_index(content_index_path())
    pending: list[Path] = []
    already = 0
    for path in files:
        try:
            content_hash = file_content_hash(path)
        except (OSError, UnicodeError):
            log_skipped(path, "empty_or_non_utf8")
            continue
        if f"{dataset}:{content_hash}" in index:
            already += 1
            continue
        pending.append(path)
    return pending, already


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    return {"completed_batches": 0, "ingested_files": 0, "skipped_files": 0}


def save_progress(progress: dict) -> None:
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2), encoding="utf-8")


def ingest_batch_subprocess(
    batch: list[Path],
    dataset: str,
    job_id: str,
) -> dict[str, object]:
    """Run one batch in a fresh worker process (avoids asyncio loop reuse bugs)."""
    command = [
        sys.executable,
        "-m",
        "pipeline.cognee_worker",
        "ingest-files",
        "--dataset",
        dataset,
        "--job-id",
        job_id,
    ]
    for path in batch:
        command.extend(("--path", str(path)))

    result = subprocess.run(
        command,
        cwd=EMPIRE_ROOT,
        capture_output=True,
        text=True,
        timeout=INGEST_TIMEOUT_SECONDS,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "ingest worker failed")

    for line in reversed(result.stdout.splitlines()):
        line = line.strip()
        if line.startswith("{"):
            return json.loads(line)
    raise RuntimeError("ingest worker returned no JSON result")


def ingest_batch_resilient(
    batch: list[Path],
    dataset: str,
    job_id: str,
    progress: dict,
) -> dict[str, object]:
    """Ingest a batch; on failure, fall back to per-file ingest and skip bad files."""
    try:
        return ingest_batch_subprocess(batch, dataset, job_id)
    except Exception as batch_error:
        print(f"  batch failed ({batch_error}); trying files individually ...", file=sys.stderr)

    combined: dict[str, object] = {
        "documents": 0,
        "skipped": [],
        "files": [],
    }
    for path in batch:
        file_job = f"{job_id}-{path.stem[:20]}"
        try:
            result = ingest_batch_subprocess([path], dataset, file_job)
            combined["documents"] = int(combined["documents"]) + int(result.get("documents", 0))
            combined["skipped"] = list(combined["skipped"]) + list(result.get("skipped", []))
            combined["files"] = list(combined["files"]) + list(result.get("files", []))
        except Exception as exc:
            log_skipped(path, f"ingest_failed: {exc}")
            progress["skipped_files"] = progress.get("skipped_files", 0) + 1
            print(f"  SKIP {path.name}: {exc}", file=sys.stderr)
    return combined


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest Empire Workbench into eve_memory")
    parser.add_argument("--dataset", default="eve_memory")
    parser.add_argument("--limit", type=int, default=0, help="Max files to process (0 = all)")
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Skip files already embedded (content-index based)",
    )
    parser.add_argument(
        "--folders",
        nargs="*",
        default=[str(p) for p in DEFAULT_FOLDERS],
        help="Folders to ingest (default: Memory Bank + Skills)",
    )
    args = parser.parse_args()

    folders = [Path(f) for f in args.folders]
    all_files = collect_files(folders)
    progress = load_progress() if args.resume else {
        "completed_batches": 0,
        "ingested_files": 0,
        "skipped_files": 0,
    }

    if args.resume:
        pending, already_embedded = filter_pending(all_files, args.dataset)
        print(
            f"Found {len(all_files)} text files; "
            f"{already_embedded} already embedded; {len(pending)} pending."
        )
    else:
        pending = all_files
        print(f"Found {len(all_files)} ingestible files across {len(folders)} folder(s).")

    if args.limit:
        pending = pending[: args.limit]

    total = len(pending)
    print(f"Embeddings land on V:\\Cognee via dataset '{args.dataset}'.")

    batch_num = progress.get("completed_batches", 0)
    for i in range(0, total, MAX_BATCH_FILES):
        batch = pending[i : i + MAX_BATCH_FILES]
        batch_num += 1
        job_id = f"workbench-{uuid.uuid4().hex[:12]}"
        print(f"Batch {batch_num}: {len(batch)} files ({i + 1}-{i + len(batch)} of {total}) ...")
        last_error: Exception | None = None
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                result = ingest_batch_resilient(batch, args.dataset, job_id, progress)
                progress["completed_batches"] = batch_num
                progress["ingested_files"] += int(result.get("documents", 0))
                progress["skipped_files"] += len(result.get("skipped", []))
                progress["pending_remaining"] = max(0, total - (i + len(batch)))
                save_progress(progress)
                print(
                    f"  embedded={result.get('documents', 0)} "
                    f"skipped={len(result.get('skipped', []))}"
                )
                last_error = None
                break
            except Exception as exc:
                last_error = exc
                if attempt < MAX_RETRIES:
                    print(
                        f"  attempt {attempt} failed ({exc}); retrying in {RETRY_DELAY_SECONDS}s ...",
                        file=sys.stderr,
                    )
                    time.sleep(RETRY_DELAY_SECONDS)
                else:
                    print(f"  ERROR: {exc}", file=sys.stderr)
        if last_error is not None:
            save_progress(progress)
            return 1

    progress["pending_remaining"] = 0
    save_progress(progress)
    print(
        f"\nDone. embedded={progress['ingested_files']} "
        f"skipped={progress['skipped_files']} "
        f"batches={progress['completed_batches']}"
    )
    print(
        "\nNext: build fast chat recall with "
        ".\\scripts\\optimize-eve-memory.ps1"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
