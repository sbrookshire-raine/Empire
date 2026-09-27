"""FastMCP server exposing Cognee graph memory as AI tools."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline.cognee_subprocess import run_cognee_worker, run_ingest_file
from pipeline.normalizer import normalize_file
from pipeline.paths import PathOutsideRoot, resolve_within

ROOT = Path(__file__).resolve().parents[1]

mcp = FastMCP("empire-cognee")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def cognee_remember(content: str, dataset: str = "eve_memory", session_id: str = "") -> str:
    """Store content in Cognee graph memory for the given dataset."""
    _ = session_id
    result = await run_cognee_worker("remember", "--content", content, "--dataset", dataset)
    return _json({**result, "chars": len(content)})


@mcp.tool()
async def cognee_recall(
    query: str,
    dataset: str = "eve_core",
    session_id: str = "",
) -> str:
    """Query Cognee graph memory. Prefer eve_core for chat recall; eve_memory for archive."""
    _ = session_id
    args = ["recall", "--query", query]
    if dataset:
        args.extend(["--dataset", dataset])
    result = await run_cognee_worker(*args)
    return _json(result)


@mcp.tool()
async def cognee_improve(dataset: str = "eve_memory") -> str:
    """Run Cognee enrichment/improvement pass on a dataset."""
    result = await run_cognee_worker("improve", "--dataset", dataset)
    return _json(result)


@mcp.tool()
async def cognee_forget(dataset: str = "eve_memory") -> str:
    """Remove dataset memory from Cognee (best-effort on local install)."""
    result = await run_cognee_worker("forget", "--dataset", dataset)
    return _json(result)


@mcp.tool()
async def cognee_ingest_mock_file(path: str) -> str:
    """Ingest a local mock .json or .md file from mock_data_ingest into Cognee.

    The path is jailed to the repository root (P1, 2026-09-27). Before this, the tool resolved whatever it was
    handed and ingested it, so a traversal such as `..\\..\\Users\\<user>\\notes.json` — or any absolute path on
    the machine ending in .json/.md — was read and pushed into graph memory. Errors are returned, not raised, so
    the failure crosses the MCP boundary as data the caller can act on (OPERATING_CONTRACT §5).
    """
    try:
        file_path = resolve_within(path, ROOT, label="mock file")
    except PathOutsideRoot as exc:
        return _json({"ok": False, "error": str(exc), "path": path, "root": str(ROOT)})

    if not file_path.exists():
        return _json({"ok": False, "error": f"Mock file not found: {file_path}", "path": str(file_path)})

    suffix = file_path.suffix.lower()
    if suffix not in {".json", ".md"}:
        return _json(
            {
                "ok": False,
                "error": "Only .json and .md mock files are supported",
                "path": str(file_path),
            }
        )

    preview = normalize_file(file_path)
    result = await run_ingest_file(file_path)
    return _json({"preview_external_id": preview["external_id"], **result})


if __name__ == "__main__":
    mcp.run()
