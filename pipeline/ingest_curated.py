"""Curated primitives ingest: Fuel-only folder → Cognee dataset primitives_test."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from pipeline.cognee_client import (
    cognify_dataset,
    embed_dataset,
    improve,
    recall,
    remember_many,
)
from pipeline.config import ROOT
from pipeline.wiki_ops_paths import overnight_pid_alive

DATASET = "primitives_test"
CURATED_ROOT = ROOT / "data" / "curated_primitives"
RAW_DIR = CURATED_ROOT / "raw_materials"
DIRECTIVES_DIR = CURATED_ROOT / "directives"
STATUS_DIR = CURATED_ROOT / "status"
DEFAULT_LLM = "huihui_ai/qwen2.5-coder-abliterate:14b"


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_env() -> None:
    load_dotenv(ROOT / "config" / "cognee.env", override=False)
    load_dotenv(ROOT / "cognee" / ".env", override=False)
    load_dotenv(ROOT / ".env.local", override=False)
    # Curated graph LLM (do not permanently rewrite cognee.env).
    llm = os.environ.get("EMPIRE_PRIMITIVES_LLM_MODEL", DEFAULT_LLM).strip()
    if llm:
        os.environ["LLM_MODEL"] = llm
        os.environ["LLM_PROVIDER"] = os.environ.get("LLM_PROVIDER", "ollama")
        os.environ["LLM_ENDPOINT"] = os.environ.get(
            "LLM_ENDPOINT", "http://localhost:11434/v1"
        )
        os.environ["LLM_API_KEY"] = os.environ.get("LLM_API_KEY", "ollama")


def _collect_fuel_markdown(raw_dir: Path) -> list[tuple[Path, str]]:
    if not raw_dir.is_dir():
        raise FileNotFoundError(f"Missing Fuel folder: {raw_dir}")
    # Refuse directives mixed into fuel.
    forbidden = raw_dir / "directives"
    if forbidden.exists():
        raise ValueError("directives/ must not live under raw_materials/")
    files: list[tuple[Path, str]] = []
    for path in sorted(raw_dir.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".txt"}:
            continue
        name_l = path.name.lower()
        if "system.md" in name_l or name_l.startswith("lens_"):
            raise ValueError(
                f"Directive-looking file in Fuel (refuse): {path.name}. "
                "Keep prompts under data/curated_primitives/directives/"
            )
        text = path.read_text(encoding="utf-8", errors="replace").strip()
        if not text:
            continue
        header = (
            f"Title: {path.stem}\n"
            f"source_file: {path.name}\n"
            f"dataset: {DATASET}\n"
            f"fuel: curated_primitives\n\n"
        )
        files.append((path, header + text))
    if not files:
        raise FileNotFoundError(f"No .md/.txt Fuel files in {raw_dir}")
    return files


async def run_ingest(
    *,
    skip_cognify: bool = False,
    skip_remember: bool = False,
    smoke_query: str = "",
) -> dict:
    _load_env()
    if overnight_pid_alive("2017") or overnight_pid_alive("2021") or overnight_pid_alive("2026"):
        raise RuntimeError(
            "Wikipedia overnight still appears alive — stop it before 14b cognify "
            "(GPU contention)."
        )

    fuel = _collect_fuel_markdown(RAW_DIR)
    STATUS_DIR.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    contents = [c for _, c in fuel]
    if not skip_remember:
        print(f"[curated] remembering {len(contents)} docs -> dataset={DATASET}")
        print(f"[curated] LLM_MODEL={os.environ.get('LLM_MODEL')}")
        await remember_many(contents, dataset=DATASET, mode="fast")
        print("[curated] embed_dataset (nomic)...")
        await embed_dataset(DATASET)
    else:
        print(f"[curated] skip_remember; cognify existing dataset={DATASET}")
        print(f"[curated] LLM_MODEL={os.environ.get('LLM_MODEL')}")
    cognify_seconds = 0.0
    if not skip_cognify:
        t0 = time.perf_counter()
        print("[curated] cognify_dataset (graph extract)...")
        # Prefer stock cognify for small curated set (full graph tasks).
        os.environ["EMPIRE_COGNIFY_FULL"] = "1"
        os.environ["EMPIRE_COGNIFY_SKIP_SUMMARIZE"] = "0"
        await cognify_dataset(DATASET)
        try:
            await improve(DATASET)
        except Exception as exc:  # noqa: BLE001
            print(f"[curated] improve skipped: {exc}")
        cognify_seconds = time.perf_counter() - t0
    query = smoke_query.strip() or (
        "Identify hidden structural parallels: feedback loops, scaffolding, "
        "friction/flow, or learning transfer across these materials."
    )
    print(f"[curated] smoke recall: {query}")
    hits = await recall(query, dataset=DATASET)
    elapsed = time.perf_counter() - started
    result = {
        "ok": True,
        "dataset": DATASET,
        "files": [str(p.relative_to(ROOT)) for p, _ in fuel],
        "docs": len(fuel),
        "llm_model": os.environ.get("LLM_MODEL"),
        "embedding_model": os.environ.get("EMBEDDING_MODEL"),
        "cognify_seconds": round(cognify_seconds, 1),
        "elapsed_seconds": round(elapsed, 1),
        "smoke_query": query,
        "smoke_hits": hits if isinstance(hits, list) else [str(hits)],
        "directives_path": str(DIRECTIVES_DIR / "SYSTEM.md"),
        "finished_at": _utc_now(),
    }
    out = STATUS_DIR / "last_ingest.json"
    out.write_text(json.dumps(result, indent=2, default=str)[:200_000], encoding="utf-8")
    print(json.dumps({k: result[k] for k in result if k != "smoke_hits"}, indent=2))
    print("--- smoke hits (truncated) ---")
    for i, hit in enumerate(result["smoke_hits"][:5]):
        text = hit if isinstance(hit, str) else json.dumps(hit, default=str)
        print(f"[{i}] {text[:500]}")
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Ingest curated primitives Fuel")
    parser.add_argument("--skip-cognify", action="store_true")
    parser.add_argument(
        "--cognify-only",
        action="store_true",
        help="Skip remember/embed; re-run cognify + smoke recall on existing Fuel docs",
    )
    parser.add_argument("--smoke-query", default="")
    args = parser.parse_args(argv)
    try:
        asyncio.run(
            run_ingest(
                skip_cognify=bool(args.skip_cognify),
                skip_remember=bool(args.cognify_only),
                smoke_query=args.smoke_query,
            )
        )
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        err = {
            "ok": False,
            "error": str(exc),
            "finished_at": _utc_now(),
        }
        STATUS_DIR.mkdir(parents=True, exist_ok=True)
        (STATUS_DIR / "last_ingest.json").write_text(
            json.dumps(err, indent=2), encoding="utf-8"
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
