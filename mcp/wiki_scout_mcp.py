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

# Per-process record of landing searches already issued in this session. A repeated call
# with the same subject is the signature of premature completion: the model re-runs the
# landing search and answers the same lead instead of reading deeper. The tool response then
# tells the agent, deterministically, which tool to use instead (docs/WIKI_SCOUT.md).
# Bookkeeping lives in pipeline.wiki_scout so it is unit-testable.
from pipeline.wiki_scout import (
    HARD_STOP_REPEAT_HINT,
    REPEAT_CALL_HINT,
    search_strike,
    should_refuse_repeat,
)

mcp = FastMCP("empire-wiki-scout")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def wiki_scout_search(
    query: str,
    year: str = "",
    limit: int = 5,
) -> str:
    """Local Wikipedia lookup: Title DNS + markdown lead first.

    Who/what/cast questions resolve without Weaviate. Weaviate is a fallback only
    when EMPIRE_WIKI_WEAVIATE_FALLBACK=1. Does NOT write Cognee.
    """
    try:
        from pipeline.wiki_lookup_lock import locked_tool_response, wiki_lookup_lock_active

        if wiki_lookup_lock_active():
            return _json(locked_tool_response(tool="wiki_scout_search"))
    except Exception:  # noqa: BLE001
        pass
    year_value = year.strip()
    strike = search_strike(query, year_value)
    if should_refuse_repeat(strike):
        # Refuse: no cards means repeating cannot "unlock" anything, and the only remaining
        # useful move is to answer. Bounds a stuck turn instead of paying a model round-trip
        # per repeat (measured: 7 repeats / 66 s before this guard).
        return _json(
            {
                "ok": False,
                "usable": False,
                "refused": "repeat_call",
                "query": query,
                "cards": [],
                "titles": [],
                "chat_reply_rule": HARD_STOP_REPEAT_HINT,
                "coverage_note": (
                    "Identical search already answered in this turn — refused. "
                    "Answer from the cards already in the conversation."
                ),
            }
        )
    repeated = strike == 2
    result = wiki_scout.search(
        query=query,
        year=year_value or None,
        limit=int(limit) or 3,
        write_files=False,
        use_rerank=False,
    )
    if isinstance(result, dict) and result.get("ok"):
        rule = str(result.get("chat_reply_rule") or "").strip()
        slim = {
            "ok": True,
            "query": result.get("query"),
            "snapshot_year": result.get("snapshot_year"),
            "usable": result.get("usable"),
            "cards": result.get("cards") or [],
            "chat_reply_rule": f"{rule} {REPEAT_CALL_HINT}".strip() if repeated else rule,
            "repeat_call": repeated,
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
async def remember_wiki_lead(
    subject: str,
    year: str = "2026",
    dataset: str = "eve_memory",
) -> str:
    """Explicitly remember one Title DNS lead into Cognee. Never automatic. Lead only."""
    from pipeline.wiki_title_dns import remember_wiki_lead as _remember

    return _json(
        _remember(
            subject,
            year.strip() or "2026",
            dataset=(dataset.strip() or "eve_memory"),
        )
    )


@mcp.tool()
async def wiki_resolve(
    subject: str,
    year: str = "2026",
    question: str = "",
) -> str:
    """Exact Title DNS resolve (phone book). Does not read Cognee or Weaviate."""
    from pipeline.wiki_extract import wiki_resolve as _resolve

    return _json(_resolve(subject, year.strip() or "2026", user_question=question))


@mcp.tool()
async def wiki_extract(
    subject: str,
    year: str = "2026",
    need_hint: str = "",
    section: str = "",
    question: str = "",
) -> str:
    """Locate a local wiki page and return structured Evidence JSON (fields/tables/lists).

    Deterministic parse only. Empty extract fails closed — does not invent. Does NOT write Cognee.
    """
    from pipeline.wiki_extract import wiki_extract as _extract

    return _json(
        _extract(
            subject,
            year.strip() or "2026",
            need_hint=need_hint or question,
            section=section.strip(),
            user_question=question,
        )
    )


@mcp.tool()
async def wiki_remember(
    subject: str,
    year: str = "2026",
    dataset: str = "eve_memory",
    need_hint: str = "",
    extract_id: str = "",
) -> str:
    """Remember a successful structured wiki extract into Cognee. Never automatic. Rejects non-ok extracts."""
    from pipeline.wiki_extract import remember_wiki_extract

    return _json(
        remember_wiki_extract(
            subject,
            year.strip() or "2026",
            dataset=(dataset.strip() or "eve_memory"),
            need_hint=need_hint,
            extract_id=extract_id.strip(),
        )
    )


@mcp.tool()
async def wiki_read_section(
    title: str,
    year: str = "2026",
    section: str = "",
    question: str = "",
) -> str:
    """Read a Title DNS page lead and optional H2 section from local markdown."""
    from pipeline.wiki_read_lead import wiki_read

    return _json(
        wiki_read(
            title,
            year.strip() or "2026",
            section=section.strip(),
            user_question=question,
        )
    )


@mcp.tool()
async def wiki_scratch_upsert(text: str, title: str = "", session_id: str = "") -> str:
    """Save a bridging fact to the Wikipedia research scratchpad. Not Cognee."""
    from pipeline.wiki_scratchpad import scratch_upsert

    return _json(scratch_upsert(text, session_id=session_id, title=title))


@mcp.tool()
async def wiki_scratch_read(session_id: str = "", include_errors: bool = False) -> str:
    """Read Wikipedia research scratchpad and optional Error Book."""
    from pipeline.wiki_scratchpad import error_book_recent, scratch_read

    result = scratch_read(session_id)
    if include_errors:
        result["errors"] = error_book_recent(limit=20)
    return _json(result)


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
