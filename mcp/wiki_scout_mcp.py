"""FastMCP server: on-demand Weaviate Wikipedia scout → wiki_cache markdown.

Does not auto-promote to Cognee. Full overnight wiki ingest remains halted.
"""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import wiki_scout

mcp = FastMCP("empire-wiki-scout")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def wiki_scout_search(
    query: str,
    year: str = "2021",
    limit: int = 3,
) -> str:
    """Query local Wikipedia Weaviate (hybrid BM25+vector) and cache Truth Drift markdown.

    year: 2017, 2021, or 2026. Returns short summaries + cache file paths.
    Does NOT write to Cognee — promote later via cognee_remember after triage.
    Requires Weaviate on WEAVIATE_URL (default http://127.0.0.1:8091) and Ollama nomic-embed-text.
    """
    result = wiki_scout.search(query=query, year=year or "2021", limit=int(limit) or 3)
    return _json(result)


@mcp.tool()
async def wiki_scout_compare_years(
    query: str,
    years: str = "2017,2021,2026",
    limit_per_year: int = 2,
) -> str:
    """Truth Drift compare: same query across Wikipedia snapshot years; one compare .md.

    years: comma-separated list (default 2017,2021,2026). Never auto-promotes to Cognee.
    """
    year_list = tuple(y.strip() for y in str(years).split(",") if y.strip())
    result = wiki_scout.compare_years(
        query=query,
        years=year_list or ("2017", "2021", "2026"),
        limit_per_year=int(limit_per_year) or 2,
    )
    return _json(result)


if __name__ == "__main__":
    mcp.run()
