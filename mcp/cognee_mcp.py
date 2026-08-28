"""FastMCP server exposing Cognee graph memory as AI tools."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline.cognee_subprocess import run_cognee_worker, run_ingest_file
from pipeline.normalizer import normalize_file

ROOT = Path(__file__).resolve().parents[1]

mcp = FastMCP("empire-cognee")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def cognee_remember(content: str, dataset: str = "mock", session_id: str = "") -> str:
    """Store content in Cognee graph memory for the given dataset."""
    _ = session_id
    result = await run_cognee_worker("remember", "--content", content, "--dataset", dataset)
    return _json({**result, "chars": len(content)})


@mcp.tool()
async def cognee_recall(query: str, dataset: str = "", session_id: str = "") -> str:
    """Query Cognee graph memory. Returns retrieval context for the query."""
    _ = session_id
    args = ["recall", "--query", query]
    if dataset:
        args.extend(["--dataset", dataset])
    result = await run_cognee_worker(*args)
    return _json(result)


@mcp.tool()
async def cognee_improve(dataset: str = "mock") -> str:
    """Run Cognee enrichment/improvement pass on a dataset."""
    result = await run_cognee_worker("improve", "--dataset", dataset)
    return _json(result)


@mcp.tool()
async def cognee_forget(dataset: str = "mock") -> str:
    """Remove dataset memory from Cognee (best-effort on local install)."""
    result = await run_cognee_worker("forget", "--dataset", dataset)
    return _json(result)


@mcp.tool()
async def cognee_ingest_mock_file(path: str) -> str:
    """Ingest a local mock .json or .md file from mock_data_ingest into Cognee."""
    file_path = Path(path)
    if not file_path.is_absolute():
        file_path = ROOT / file_path
    file_path = file_path.resolve()

    if not file_path.exists():
        raise FileNotFoundError(f"Mock file not found: {file_path}")

    suffix = file_path.suffix.lower()
    if suffix not in {".json", ".md"}:
        raise ValueError("Only .json and .md mock files are supported")

    preview = normalize_file(file_path)
    result = await run_ingest_file(file_path)
    return _json({"preview_external_id": preview["external_id"], **result})


if __name__ == "__main__":
    mcp.run()
