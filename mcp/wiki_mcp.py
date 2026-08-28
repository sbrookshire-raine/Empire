"""FastMCP server exposing the Wikipedia -> Cognee ingestion pipeline as AI tools.

Lets the Cursor orchestrator trigger resumable Wikipedia batch ingestion, check progress,
run the one-time Weaviate export, and recall graph context - all mid-conversation. Each tool
delegates to an isolated subprocess (Kuzu-lock safe) matching the empire-cognee pattern.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline.cognee_subprocess import (
    run_cognee_worker,
    run_weaviate_export,
    run_wiki_ingest,
)
from pipeline.wiki_checkpoint import load_checkpoint

ROOT = Path(__file__).resolve().parents[1]

mcp = FastMCP("empire-wiki")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def wiki_ingest_batch(
    year: str,
    batch: str,
    mode: str = "fast",
    limit: int = 0,
    dataset: str = "",
) -> str:
    """Ingest one Wikipedia batch (D:\\wiki_md\\{year}\\batch_{batch}) into Cognee.

    mode: 'fast' (frontmatter edges + embeddings) or 'full' (adds Ollama summary + graph).
    limit: max files this run (0 = all remaining). Resumes from checkpoint automatically.
    """
    if mode not in {"fast", "full"}:
        raise ValueError("mode must be 'fast' or 'full'")
    args = ["--year", str(year), "--batch", str(batch), "--mode", mode, "--limit", str(limit)]
    if dataset:
        args.extend(["--dataset", dataset])
    result = await run_wiki_ingest(*args)
    return _json(result)


@mcp.tool()
async def wiki_ingest_export_dir(
    export_dir: str,
    mode: str = "fast",
    limit: int = 0,
    dataset: str = "wikipedia_weaviate",
) -> str:
    """Ingest a flat directory of exported .md chunks (Weaviate staging) into Cognee."""
    if mode not in {"fast", "full"}:
        raise ValueError("mode must be 'fast' or 'full'")
    args = ["--export-dir", export_dir, "--mode", mode, "--limit", str(limit), "--dataset", dataset]
    result = await run_wiki_ingest(*args)
    return _json(result)


@mcp.tool()
async def wiki_ingest_status() -> str:
    """Return the resumable ingestion checkpoint (per-batch progress)."""
    state = load_checkpoint()
    batches = state.get("batches", {})
    summary = {
        "tracked_batches": len(batches),
        "batches": batches,
    }
    return _json(summary)


@mcp.tool()
async def wiki_export_weaviate(collection: str, limit: int = 0, url: str = "http://localhost:8080") -> str:
    """One-time read-only export of a Weaviate collection (e.g. wikichunk) to Markdown staging.

    Requires a temporary Weaviate Docker container running against D:\\weaviate_v2_archive.
    """
    args = ["--collection", collection, "--limit", str(limit), "--url", url]
    result = await run_weaviate_export(*args)
    return _json(result)


@mcp.tool()
async def wiki_recall(query: str, dataset: str = "") -> str:
    """Query Cognee graph memory for Wikipedia context.

    dataset: a specific snapshot (e.g. 'wikipedia_2026'), or '' to search ALL datasets -
    use the empty default for cross-year Truth-Drift queries that must return every snapshot.
    """
    args = ["recall", "--query", query]
    if dataset:
        args.extend(["--dataset", dataset])
    result = await run_cognee_worker(*args)
    return _json(result)


if __name__ == "__main__":
    mcp.run()
