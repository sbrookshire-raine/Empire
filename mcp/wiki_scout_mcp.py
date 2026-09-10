"""FastMCP server: on-demand Weaviate Wikipedia scout → wiki_cache markdown.

Uses Wiki Interpreter (wide retrieve + heuristics + optional BGE rerank).
Does not auto-promote to Cognee. Full overnight wiki ingest remains halted.
"""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import wiki_scout
from pipeline.wiki_interpreter import check_reranker

mcp = FastMCP("empire-wiki-scout")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def wiki_scout_search(
    query: str,
    year: str = "",
    limit: int = 5,
) -> str:
    """Wiki Interpreter search: wide hybrid retrieve, rank with Wikipedia heuristics
    (+ optional local BGE rerank), return structured cards + cache paths.

    Cards are encyclopedia page/chunk hits — NOT footnote counts.
    Snapshot years are frozen dumps, not hypothetical futures.
    Does NOT write to Cognee. Requires Weaviate on :8091.
    """
    result = wiki_scout.search(
        query=query,
        year=year.strip() or None,
        limit=int(limit) or 3,
        write_files=False,
        use_rerank=False,
    )
    if isinstance(result, dict) and result.get("ok"):
        slim = {
            "ok": True,
            "query": result.get("query"),
            "snapshot_year": result.get("snapshot_year"),
            "usable": result.get("usable"),
            "cards": result.get("cards") or [],
            "chat_reply_rule": result.get("chat_reply_rule"),
            "coverage_note": result.get("coverage_note"),
        }
        return _json(slim)
    return _json(result)


@mcp.tool()
async def wiki_scout_compare_years(
    query: str,
    years: str = "2017,2021,2026",
    limit_per_year: int = 4,
) -> str:
    """Truth Drift compare with Wiki Interpreter ranking per year.

    Returns cards_by_year (title, kind_hint, rank_why, snippet). Never auto-promotes.
    """
    year_list = tuple(y.strip() for y in str(years).split(",") if y.strip())
    result = wiki_scout.compare_years(
        query=query,
        years=year_list or ("2017", "2021", "2026"),
        limit_per_year=int(limit_per_year) or wiki_scout.DEFAULT_COMPARE_TOP_K,
        write_files=False,
        use_rerank=False,
    )
    return _json(result)


@mcp.tool()
async def promote_wiki_cache(path: str, dataset: str = "") -> str:
    """Explicitly promote a wiki_cache markdown file into Cognee. Never automatic."""
    override = dataset.strip() or None
    return _json(wiki_scout.promote_wiki_cache(path, dataset=override))


@mcp.tool()
async def wiki_interpreter_status() -> str:
    """Show whether local BGE rerank is available (heuristics always on)."""
    return _json(
        {
            "ok": True,
            "heuristics": True,
            "rerank": check_reranker(),
            "defaults": {
                "search_top_k": wiki_scout.DEFAULT_SEARCH_TOP_K,
                "compare_top_k": wiki_scout.DEFAULT_COMPARE_TOP_K,
            },
        }
    )


if __name__ == "__main__":
    mcp.run()
