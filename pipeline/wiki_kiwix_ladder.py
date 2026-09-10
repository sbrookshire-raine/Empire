"""Kiwix-MCP-style three-rung Wikipedia ladder — server-side only.

Mirrors scottyphillips/kiwix-mcp contracts without exposing MCP to Eve:
  search_with_snippets → get_content_summary → get_content

All calls hit local Weaviate + D:\\wiki_md; never live Wikipedia.
"""

from __future__ import annotations

from typing import Any

from pipeline.wiki_read_lead import wiki_read_lead
from pipeline.wiki_scout import DEFAULT_SEARCH_TOP_K, DEFAULT_SUMMARY_CHARS, search

SNIPPET_CHARS = 200
DEFAULT_CONTENT_CHARS = 6000


def search_with_snippets(
    query: str,
    *,
    year: str | int | None = None,
    limit: int = DEFAULT_SEARCH_TOP_K,
    snippet_chars: int = SNIPPET_CHARS,
    write_files: bool = False,
    **search_kwargs: Any,
) -> dict[str, Any]:
    """Rung 1: vector/BM25 search with ~200-char snippets per hit."""
    result = search(
        query,
        year=year,
        limit=limit,
        write_files=write_files,
        interpret=True,
        **search_kwargs,
    )
    if not result.get("ok"):
        return result
    snippets: list[dict[str, str]] = []
    for card in result.get("cards") or []:
        if not isinstance(card, dict):
            continue
        text = str(card.get("snippet") or card.get("text") or "")
        if len(text) > snippet_chars:
            text = text[: snippet_chars - 1].rstrip() + "…"
        snippets.append(
            {
                "title": str(card.get("title") or ""),
                "snippet": text,
                "corpus_rel_path": str(card.get("corpus_rel_path") or ""),
                "snapshot_year": str(card.get("snapshot_year") or result.get("snapshot_year") or ""),
            }
        )
    return {
        "ok": True,
        "query": query,
        "snapshot_year": result.get("snapshot_year"),
        "snippets": snippets,
        "hit_meta": result.get("hit_meta") or [],
        "titles": result.get("titles") or [],
        "ladder_rung": "search_with_snippets",
    }


def get_content_summary(
    entity: str,
    snapshot: str,
    *,
    corpus_rel_path: str | None = None,
    max_chars: int = 1800,
) -> dict[str, Any]:
    """Rung 2: article lead from D:\\wiki_md after title resolution."""
    lead = wiki_read_lead(
        entity,
        snapshot,
        corpus_rel_path=corpus_rel_path,
        max_chars=max_chars,
    )
    if lead.get("ok"):
        lead["ladder_rung"] = "get_content_summary"
    return lead


def get_content(
    entity: str,
    snapshot: str,
    *,
    corpus_rel_path: str | None = None,
    max_chars: int = DEFAULT_CONTENT_CHARS,
) -> dict[str, Any]:
    """Rung 3: longer article body (still capped) — use only when lead is insufficient."""
    from pipeline.wiki_normalizer import _parse_frontmatter
    from pipeline.wiki_read_lead import resolve_md_path

    title = (entity or "").strip()
    if not title:
        return {"ok": False, "error": "entity is required", "ladder_rung": "get_content"}
    path = resolve_md_path(title, snapshot, corpus_rel_path=corpus_rel_path)
    if path is None:
        return {
            "ok": False,
            "error": f"no markdown file for {title!r} ({snapshot})",
            "title": title,
            "snapshot": snapshot,
            "ladder_rung": "get_content",
        }
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return {
            "ok": False,
            "error": str(exc),
            "title": title,
            "snapshot": snapshot,
            "ladder_rung": "get_content",
        }
    meta, body = _parse_frontmatter(raw)
    resolved_title = str(meta.get("title") or title).strip() or title
    text = body.strip()
    if len(text) > max_chars:
        text = text[: max_chars - 1].rstrip() + "…"
    return {
        "ok": True,
        "title": resolved_title,
        "snapshot": snapshot,
        "content": text,
        "path": str(path),
        "chars": len(text),
        "ladder_rung": "get_content",
    }


def ladder_lookup(
    query: str,
    *,
    year: str | int | None = None,
    summary_max_chars: int = 1800,
    content_max_chars: int = DEFAULT_CONTENT_CHARS,
    need_full_content: bool = False,
) -> dict[str, Any]:
    """Convenience: run search → summary → optional full content for top hit."""
    search_result = search_with_snippets(query, year=year, limit=DEFAULT_SEARCH_TOP_K)
    if not search_result.get("ok"):
        return search_result
    snippets = search_result.get("snippets") or []
    if not snippets:
        return {"ok": False, "error": "no snippets", "ladder_rung": "ladder_lookup"}
    top = snippets[0]
    title = str(top.get("title") or "")
    snap = str(top.get("snapshot_year") or search_result.get("snapshot_year") or "2026")
    rel = str(top.get("corpus_rel_path") or "") or None
    summary = get_content_summary(title, snap, corpus_rel_path=rel, max_chars=summary_max_chars)
    out: dict[str, Any] = {
        "ok": bool(summary.get("ok")),
        "query": query,
        "search": search_result,
        "summary": summary,
        "ladder_rung": "ladder_lookup",
    }
    if need_full_content and summary.get("ok"):
        out["content"] = get_content(title, snap, corpus_rel_path=rel, max_chars=content_max_chars)
    return out
