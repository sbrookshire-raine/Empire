"""FastMCP: workspace search, query data, read document (local evidence arms)."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import query_data, read_document, workspace_search

mcp = FastMCP("empire-evidence")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def workspace_search(query: str, max_results: int = 100, note: str = "") -> str:
    """Search allowlisted local roots (C:/Empire_Workbench, C:/EMPIRE/docs) for text."""
    return _json(workspace_search.search(query, max_results=max_results, note=note))


@mcp.tool()
async def query_data(sql: str, data_file: str = "", max_rows: int = 1000) -> str:
    """Run a read-only DuckDB query over a local CSV/JSON/Parquet/SQLite file (or inline)."""
    return _json(query_data.query(sql, data_file=data_file, max_rows=max_rows))


@mcp.tool()
async def read_document(input_path: str, max_chars: int = 200000) -> str:
    """Extract text/markdown from a local document (MarkItDown → Docling fallback)."""
    return _json(read_document.read_document(input_path, max_chars=max_chars))


if __name__ == "__main__":
    mcp.run()
