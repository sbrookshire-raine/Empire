#!/usr/bin/env python3
"""Ingest DAZE canonical profile + flattened codebase chunks into Cognee."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import uuid
from pathlib import Path

EMPIRE_ROOT = Path(__file__).resolve().parent.parent
WORKBENCH_ROOT = Path(r"C:\Empire_Workbench")
PROFILE = WORKBENCH_ROOT / "00_Core_Profile" / "DAZE_PRODUCT_PROFILE.md"
FLATTENED = WORKBENCH_ROOT / "03_Active_Tools" / "DAZE_flattened_3.txt"
LIVE_URL = "https://daze-murex.vercel.app/"
MAX_CHUNK_BYTES = 90_000
FILE_BOUNDARY = re.compile(r"\n={70,}\nFILE: ", re.MULTILINE)


def worker_env() -> dict[str, str]:
    env = dict(**{key: value for key, value in __import__("os").environ.items()})
    env["PYTHONPATH"] = str(EMPIRE_ROOT)
    env["PYTHONUNBUFFERED"] = "1"
    env["CACHING"] = "false"
    env["COGNEE_SKIP_CONNECTION_TEST"] = "true"
    return env


def run_remember(content: str, dataset: str) -> dict[str, object]:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pipeline.cognee_worker",
            "remember",
            "--content",
            content,
            "--dataset",
            dataset,
        ],
        cwd=EMPIRE_ROOT,
        env=worker_env(),
        capture_output=True,
        text=True,
        timeout=600,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "remember failed")
    for line in reversed(result.stdout.splitlines()):
        line = line.strip()
        if line.startswith("{"):
            return json.loads(line)
    return {"status": "ok"}


def chunk_flattened(path: Path) -> list[str]:
    body = path.read_text(encoding="utf-8")
    parts = FILE_BOUNDARY.split(body)
    if len(parts) <= 1:
        return [
            (
                f"# DAZE flattened codebase (canonical product reference)\n"
                f"Live app: {LIVE_URL}\n"
                f"Source file: {path}\n\n{body}"
            )
        ]

    header = parts[0].strip()
    file_sections = parts[1:]
    chunks: list[str] = []
    current = (
        f"# DAZE flattened codebase (canonical product reference)\n"
        f"Live app: {LIVE_URL}\n"
        f"Source file: {path}\n\n{header}\n"
    )

    for section in file_sections:
        piece = f"\n{'=' * 72}\nFILE: {section}"
        if (
            len(current.encode("utf-8")) + len(piece.encode("utf-8")) > MAX_CHUNK_BYTES
            and current.strip()
        ):
            chunks.append(current.strip())
            current = (
                f"# DAZE flattened codebase (continued)\n"
                f"Live app: {LIVE_URL}\n"
                f"Source file: {path}\n"
            )
        current += piece

    if current.strip():
        chunks.append(current.strip())
    return chunks


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest DAZE product profile + flattened code into Cognee.")
    parser.add_argument("--dataset", default="eve_memory", help="Cognee dataset (default: eve_memory)")
    parser.add_argument("--dry-run", action="store_true", help="Print chunk plan only")
    parser.add_argument(
        "--skip-flattened",
        action="store_true",
        help="Ingest profile only (faster smoke test)",
    )
    args = parser.parse_args()

    if not PROFILE.is_file():
        print(f"Missing profile: {PROFILE}", file=sys.stderr)
        return 1
    if not args.skip_flattened and not FLATTENED.is_file():
        print(f"Missing flattened file: {FLATTENED}", file=sys.stderr)
        return 1

    profile_body = PROFILE.read_text(encoding="utf-8").strip()
    profile_doc = (
        f"# DAZE canonical product profile (Cognee ingest)\n"
        f"Live app: {LIVE_URL}\n\n{profile_body}"
    )
    chunks = [profile_doc]
    if not args.skip_flattened:
        chunks.extend(chunk_flattened(FLATTENED))

    print(f"Prepared {len(chunks)} document(s) for dataset {args.dataset}.")
    for index, chunk in enumerate(chunks, start=1):
        size = len(chunk.encode("utf-8"))
        print(f"  chunk {index}: {size:,} bytes")
    if args.dry_run:
        return 0

    ingested = 0
    for index, chunk in enumerate(chunks, start=1):
        result = run_remember(chunk, args.dataset)
        ingested += int(result.get("documents", 1))
        print(f"Ingested chunk {index}/{len(chunks)} -> {result.get('documents', 1)} doc(s)")

    embed_job = f"daze-embed-{uuid.uuid4().hex[:8]}"
    embed = subprocess.run(
        [
            sys.executable,
            "-m",
            "pipeline.cognee_worker",
            "embed",
            "--dataset",
            args.dataset,
            "--job-id",
            embed_job,
        ],
        cwd=EMPIRE_ROOT,
        env=worker_env(),
        capture_output=True,
        text=True,
        timeout=600,
        check=False,
    )
    if embed.returncode != 0:
        print(f"Embed warning: {embed.stderr.strip() or embed.stdout.strip()}", file=sys.stderr)
    else:
        print(f"Embedded dataset {args.dataset}.")

    print(f"Done — {ingested} remember pass(es) on {args.dataset}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
