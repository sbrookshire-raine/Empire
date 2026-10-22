"""Bounded server-side Wikipedia prefetch for common Architect phrasings.

Injects archive evidence next to the user ask so Eve can answer in one pass without
multi-minute tool loops. Does NOT set wiki_lookup_lock — tools remain available.
"""

from __future__ import annotations

import os
import re

from frontend.eve_toolbelt import load_active_tools
from frontend.wiki_drift_api import (
    WIKI_EXTRACT_MARKER,
    WIKI_LOOKUP_MARKER,
    _call_with_timeout,
    _lookup_from_title_dns,
    discography_title_from_album_question,
    extract_search_query,
    is_wiki_lookup_query,
)

WIKI_GREEN_MARKER = "[[EMPIRE_WIKI_GREEN]]"
_DEFAULT_TIMEOUT = 28.0


def _green_path_enabled() -> bool:
    raw = os.environ.get("EMPIRE_WIKI_GREEN_PATH", "1").strip().casefold()
    return raw not in {"0", "false", "no", "off"}


def _discography_title(user_question: str, extracted: str) -> str | None:
    title = discography_title_from_album_question(user_question)
    if title:
        return title
    cleaned = (extracted or "").strip()
    if cleaned and "discography" in cleaned.casefold():
        return cleaned[:160]
    return None


def build_green_path_block(user_question: str) -> str:
    """Return an evidence block for fast wiki list/fact asks, or empty string."""

    text = (user_question or "").strip()
    if not text or not _green_path_enabled():
        return ""
    # The shared classifier decides; `is_wiki_lookup_query` adds the stateful
    # rules (the page we are currently discussing) on top. Both must agree
    # that this is a wiki ask before any evidence is prefetched.
    try:
        from pipeline import route_classifier

        if route_classifier.classify(text) != route_classifier.WIKI:
            return ""
    except Exception:  # noqa: BLE001
        pass
    if not is_wiki_lookup_query(text):
        return ""
    try:
        if "wiki_local" not in set(load_active_tools()):
            return ""
    except Exception:  # noqa: BLE001
        return ""

    extracted = extract_search_query(text)
    title = _discography_title(text, extracted) or extracted
    if not title:
        return ""

    from pipeline.wiki_scout import default_snapshot_year

    year = default_snapshot_year()
    timeout = float(os.environ.get("EMPIRE_WIKI_GREEN_TIMEOUT", str(_DEFAULT_TIMEOUT)))
    try:
        block, _evidence = _call_with_timeout(
            _lookup_from_title_dns,
            max(5.0, min(timeout, 45.0)),
            title,
            year=year,
            user_question=text,
            include_hops=False,
        )
    except Exception:  # noqa: BLE001
        return ""

    if not block or (
        WIKI_LOOKUP_MARKER not in block and WIKI_EXTRACT_MARKER not in block
    ):
        return ""
    green = block
    if WIKI_LOOKUP_MARKER in green:
        green = green.replace(WIKI_LOOKUP_MARKER, WIKI_GREEN_MARKER, 1)
    elif WIKI_EXTRACT_MARKER in green:
        green = green.replace(WIKI_EXTRACT_MARKER, WIKI_GREEN_MARKER, 1)
    return (
        f"\n\n{green}\n"
        "Answer from this archive evidence only. List the albums (or facts) in order, "
        "brief bullets or one short paragraph. Skip wiki tool calls when the list is "
        "already above. No long preamble, no repeating these markers, no asking the "
        "Architect to confirm unless Title DNS was ambiguous."
    )
