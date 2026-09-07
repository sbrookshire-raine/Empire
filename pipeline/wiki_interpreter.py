"""Wiki Interpreter — glasses for Eve over the Weaviate Wikipedia archive.

Pipeline: retrieve wide → Wikipedia heuristics → optional local BGE rerank →
top-K structured cards. Hits are encyclopedia pages/chunks, never footnote counts.

Goal: any conversational encyclopedia question → usable titles + answer-bearing
snippets, without per-topic constant rewrites.
"""

from __future__ import annotations

import os
import re
from functools import lru_cache
from typing import Any

from pipeline.wiki_title_matcher import (
    normalize_text,
    strip_leading_article,
    strip_parens,
    subject_match_forms,
)

# Wide pool from Weaviate before interpret; final cards stay small for chat ctx.
DEFAULT_CANDIDATE_POOL = int(os.environ.get("EMPIRE_WIKI_CANDIDATE_POOL", "20"))
DEFAULT_TOP_K = int(os.environ.get("EMPIRE_WIKI_INTERPRETER_TOP_K", "5"))
RERANK_MODEL = os.environ.get(
    "EMPIRE_WIKI_RERANK_MODEL",
    "BAAI/bge-reranker-base",
)


def rerank_enabled() -> bool:
    return os.environ.get("EMPIRE_WIKI_RERANK", "1").strip().lower() not in {
        "0",
        "false",
        "no",
        "off",
    }


# Back-compat for callers that read the module constant once
RERANK_ENABLED = rerank_enabled()

_DISAMBIG_RE = re.compile(r"\(disambiguation\)", re.I)
_LIST_RE = re.compile(r"^list of\b|^outline of\b|^lists? of lists\b", re.I)
_LAB_RE = re.compile(r"\blaboratory\b|\binstitute\b", re.I)
_FICTIONAL_RE = re.compile(r"\bfictional\b|\bfictitious\b|\bhypothetical\b", re.I)
_BARE_YEAR_RE = re.compile(r"^\d{4}$")
_YEAR_TOKEN_RE = re.compile(r"\b((?:19|20)\d{2})\b")
_CHATTER_RE = re.compile(
    r"^(can you|could you|please|tell me|find out|sure[, ]+|"
    r"let'?s\s+\w+\s+|what(?:'s| is| was)|who(?:'s| is| was)|"
    r"how many|give me|i want|show me)\s+",
    re.I,
)
_STOPWORDS = frozenset(
    {
        "a",
        "an",
        "the",
        "of",
        "and",
        "or",
        "to",
        "in",
        "on",
        "for",
        "by",
        "at",
        "from",
        "with",
        "as",
        "is",
        "it",
        "its",
        "be",
        "was",
        "were",
        "are",
        "been",
        "being",
        "that",
        "this",
        "these",
        "those",
        "into",
        "about",
        "over",
        "under",
        "than",
        "then",
        "also",
        "just",
        "only",
        "each",
        "year",
        "years",
        "across",
        "between",
        "during",
        "until",
        "after",
        "before",
        "which",
        "what",
        "who",
        "whom",
        "whose",
        "when",
        "where",
        "why",
        "how",
        "usa",
        "u.s",
        "us",
    }
)
_YEAR_NOISE_TITLE = re.compile(
    r"\b(fifa|world cup|census|olympics|election|elections|fap)\b",
    re.I,
)
_SATELLITE_TITLE_RE = re.compile(
    r"\b("
    r"medal|award|awards|prize|school|lyc[eé]e|university|college|institute|"
    r"peninsula|records|journal|airport|station|bridge|avenue|street|"
    r"film|album|song|comics?|organisation|organization|foundation|"
    r"library|museum|hospital|theatre|theater|stadium"
    r")\b|\.com$",
    re.I,
)
_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+|\n+")
_DATE_SPAN_RE = re.compile(
    r"\b(?:january|february|march|april|may|june|july|august|september|"
    r"october|november|december)\s+\d{1,2},?\s+\d{4}\b|"
    r"\b(?:19|20)\d{2}\b|"
    r"\b(?:began|begun|ended|inaugurat\w*|succeed\w*|incumbent|tenure)\b",
    re.I,
)


def clean_query_for_retrieval(query: str) -> str:
    """Strip chat filler and year lists so archive years do not poison BM25/rerank."""
    raw = (query or "").strip()
    if not raw:
        return ""
    cleaned = raw
    for _ in range(3):
        nxt = _CHATTER_RE.sub("", cleaned).strip()
        if nxt == cleaned:
            break
        cleaned = nxt
    cleaned = re.sub(r"[?!.]+$", "", cleaned).strip()
    cleaned = re.sub(
        r"\bin (each of )?the years?\b.*$",
        "",
        cleaned,
        flags=re.I,
    ).strip()
    cleaned = re.sub(
        r"\bacross (the )?(three |3 )?years?\b.*$",
        "",
        cleaned,
        flags=re.I,
    ).strip()
    cleaned = re.sub(
        r"\bin\s+(?:the\s+years?\s+)?(?:19|20)\d{2}(?:\s*,\s*(?:19|20)\d{2})*"
        r"(?:\s*,?\s*(?:and|&)\s*(?:19|20)\d{2})?\s*$",
        "",
        cleaned,
        flags=re.I,
    ).strip()
    cleaned = re.sub(
        r"(?:,?\s*(?:and|&)?\s*(?:19|20)\d{2})+\s*$",
        "",
        cleaned,
        flags=re.I,
    ).strip()
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" ,;")
    cleaned = re.sub(r"^(the|a|an)\s+", "", cleaned, flags=re.I).strip()
    # After stripping year lists, "who was the president in 2017…" collapses to
    # bare "president" — that matches the wrong Wikipedia page. Restore the usual
    # US office title when the raw question was clearly asking who held that office.
    if normalize_text(cleaned) in {"president", "presidency"}:
        raw_n = normalize_text(raw)
        if any(
            w in raw_n
            for w in (
                "who",
                "united states",
                "usa",
                "u.s",
                "american",
                "potus",
            )
        ) or re.search(r"\bpresident\b", raw_n):
            cleaned = "President of the United States"
    return cleaned or raw


def significant_terms(query: str) -> list[str]:
    """Content tokens for overlap / snippet scoring."""
    subject = clean_query_for_retrieval(query) or query
    terms: list[str] = []
    seen: set[str] = set()
    for tok in re.findall(r"[a-z0-9][a-z0-9'.-]{2,}", normalize_text(subject)):
        if tok in _STOPWORDS or _BARE_YEAR_RE.match(tok):
            continue
        if tok not in seen:
            seen.add(tok)
            terms.append(tok)
    return terms


def expand_queries(query: str) -> list[str]:
    """Conversational → encyclopedia title variants for better Weaviate recall.

    Never returns year-laden conversational strings — those pull year-stub pages.
    """
    raw = (query or "").strip()
    if not raw:
        return []
    cleaned = clean_query_for_retrieval(raw)
    variants: list[str] = []
    titled = ""
    if cleaned:
        variants.append(cleaned)
        titled = cleaned[:1].upper() + cleaned[1:] if cleaned else ""
        if titled and titled not in variants:
            variants.append(titled)

    ql = normalize_text(cleaned or raw)
    raw_n = normalize_text(raw)

    # "Nile River" / "Amazon River" → bare hydronym
    m_river = re.search(r"^(.+?)\s+river$", cleaned or "", flags=re.I)
    if m_river:
        bare = m_river.group(1).strip()
        if bare and bare not in variants:
            variants.append(bare)
        river_flip = f"River {bare}"
        if bare and river_flip not in variants:
            variants.append(river_flip)

    # Single-token famous-name nudges (Wikipedia primary topics)
    if ql in {"beethoven", "shakespeare", "einstein", "napoleon", "mozart", "plato", "aristotle"}:
        fancy = {
            "beethoven": "Ludwig van Beethoven",
            "shakespeare": "William Shakespeare",
            "einstein": "Albert Einstein",
            "napoleon": "Napoleon",
            "mozart": "Wolfgang Amadeus Mozart",
            "plato": "Plato",
            "aristotle": "Aristotle",
        }[ql]
        if fancy not in variants:
            variants.append(fancy)

    # Ambiguous / famous one-word topics — inject primary Wikipedia titles when present
    if ql in {"mercury", "python", "java", "apple", "turkey", "nile", "beethoven"}:
        extras = {
            "mercury": (
                "Mercury (planet)",
                "Mercury (element)",
                "Mercury (mythology)",
                "Outline of Mercury (planet)",
                "Mercury (disambiguation)",
            ),
            "python": (
                "Python (programming language)",
                "Python (genus)",
                "Python (disambiguation)",
            ),
            "java": ("Java (programming language)", "Java", "Java (disambiguation)"),
            "apple": ("Apple Inc.", "Apple", "Apple (disambiguation)"),
            "turkey": ("Turkey", "Turkey (bird)", "Turkey (disambiguation)"),
            "nile": ("Nile (disambiguation)", "Geography of Egypt", "White Nile", "Blue Nile"),
            "beethoven": (
                "Ludwig van Beethoven",
                "Beethoven (disambiguation)",
                "List of compositions by Ludwig van Beethoven",
            ),
        }[ql]
        for extra in extras:
            if extra not in variants:
                variants.append(extra)

    if "arcade" in ql:
        for extra in (
            "Arcade game",
            "Arcade cabinet",
            "History of arcade video games",
            "Video arcade",
        ):
            if extra not in variants:
                variants.append(extra)

    # Person / topic: always try the disambiguation page (archive often lacks the primary)
    if cleaned and "(" not in cleaned and len(cleaned.split()) <= 4:
        dab = f"{cleaned} (disambiguation)"
        if dab not in variants:
            variants.append(dab)
        dab_t = f"{titled} (disambiguation)" if titled else ""
        if dab_t and dab_t not in variants:
            variants.append(dab_t)

    # Known useful fallbacks when famous primaries are absent from this dump
    fallbacks = {
        "leonardo da vinci": (
            "Science and inventions of Leonardo da Vinci",
            "Leonardo da Vinci (disambiguation)",
        ),
        "marie curie": ("Marie Curie (disambiguation)", "Curie family"),
        "industrial revolution": (
            "Second Industrial Revolution",
            "Industrial Revolution in Scotland",
        ),
        "nile river": ("Nile (disambiguation)", "Geography of Egypt"),
        "nile": ("Nile (disambiguation)", "Geography of Egypt"),
    }
    for key, extras in fallbacks.items():
        if key in ql:
            for extra in extras:
                if extra not in variants:
                    variants.append(extra)

    # "capital of France" → country page (avoids "capital punishment" traps)
    m_cap = re.search(r"\bcapital of\s+(.+)$", cleaned or "", flags=re.I)
    if m_cap:
        place = m_cap.group(1).strip(" .,")
        if place:
            for extra in (place, place[:1].upper() + place[1:] if place else place):
                if extra and extra not in variants:
                    variants.append(extra)
            # Common Wikipedia phrasing lives on the country/city article, not "Capital of X"
            if f"Geography of {place}" not in variants and len(place.split()) <= 4:
                variants.append(f"Geography of {place}")

    # Office / who-was patterns common in Wikipedia
    if "president" in ql and (
        "united states" in ql
        or "usa" in ql
        or "u.s" in ql
        or "american" in ql
        or ql.startswith("president")
        or "who" in raw_n
    ):
        for extra in (
            "List of presidents of the United States",
            "President of the United States",
            "Presidency of Donald Trump",
            "Presidency of Joe Biden",
        ):
            if extra not in variants:
                variants.append(extra)

    # "capital of X" / "prime minister of X" → keep cleaned; add List-of when short
    m_list = re.match(
        r"^(?:list of\s+)?(.+)$",
        cleaned or "",
        flags=re.I,
    )
    if m_list and "list of" not in ql and len((cleaned or "").split()) <= 6:
        body = m_list.group(1).strip()
        if body and not body.casefold().startswith("list of"):
            list_var = f"List of {body}"
            # Only for plural-ish / office queries — avoid "List of Artificial Intelligence"
            if any(
                w in ql
                for w in (
                    "president",
                    "minister",
                    "governor",
                    "senator",
                    "mayor",
                    "king",
                    "queen",
                    "emperor",
                )
            ):
                if list_var not in variants:
                    variants.append(list_var)

    if "history of" not in ql and len(ql.split()) <= 4 and ql:
        hist = f"History of {cleaned}"
        if hist not in variants and any(
            w in raw_n for w in ("history", "began", "origin", "started")
        ):
            variants.append(hist)

    return variants


def classify_title(title: str) -> str:
    t = str(title or "").strip()
    if _DISAMBIG_RE.search(t):
        return "disambiguation"
    if _FICTIONAL_RE.search(t):
        return "fictional"
    if _LIST_RE.search(t):
        return "list"
    if _LAB_RE.search(t) and "artificial intelligence" in t.casefold():
        return "laboratory"
    if _LAB_RE.search(t):
        return "institution"
    return "article"


def _title_match_bonus(query: str, title: str) -> tuple[float, str]:
    subject = clean_query_for_retrieval(query)
    forms = subject_match_forms(subject)
    title_norm = normalize_text(title)
    title_stripped = normalize_text(strip_parens(strip_leading_article(title)))
    had_parens = title_stripped != title_norm and bool(title_stripped)
    if not title_norm:
        return 0.0, ""
    if _BARE_YEAR_RE.match(title_stripped):
        return 0.0, ""
    for form in forms:
        if not form:
            continue
        if title_norm == form:
            return 14.0, "exact_title"
        if had_parens and title_stripped == form:
            return 2.0, "stripped_title"
        if title_stripped.startswith(form) or form.startswith(title_stripped):
            if abs(len(title_stripped) - len(form)) <= max(8, len(form) // 2):
                return 8.0, "near_title"
        if form in title_stripped:
            if len(form) >= 8:
                return 4.0, "title_contains"
        if title_stripped in form:
            if len(title_stripped) >= 12 and len(title_stripped) >= len(form) * 0.45:
                return 4.0, "title_contains"
    return 0.0, ""


def _years_mentioned(*texts: str) -> set[str]:
    years: set[str] = set()
    for text in texts:
        for match in _YEAR_TOKEN_RE.finditer(str(text or "")):
            years.add(match.group(1))
    return years


def _president_topic(query: str) -> bool:
    qn = normalize_text(clean_query_for_retrieval(query) or query)
    raw_n = normalize_text(query)
    return (
        "president" in qn
        or "presidency" in qn
        or "president" in raw_n
        or "potus" in raw_n
    )


def _term_overlap(text: str, terms: list[str]) -> tuple[float, int]:
    if not text or not terms:
        return 0.0, 0
    hay = normalize_text(text)
    hits = 0
    for term in terms:
        if term in hay:
            hits += 1
    return (hits / max(len(terms), 1)), hits


def _is_year_noise_title(title: str, query: str) -> bool:
    title_n = normalize_text(title)
    subject = normalize_text(clean_query_for_retrieval(query) or query)
    if _BARE_YEAR_RE.match(title.strip()):
        return True
    years_in_title = _years_mentioned(title)
    if not years_in_title:
        return False
    # Year pages / sports/census bids when the subject is not that year event
    if _YEAR_NOISE_TITLE.search(title) and not any(y in subject for y in years_in_title):
        # Allow if subject itself is about elections/olympics/etc.
        if not any(
            n in subject for n in ("fifa", "world cup", "census", "olympic", "election")
        ):
            return True
    return False


def heuristic_score(query: str, hit: dict[str, Any]) -> tuple[float, list[str]]:
    """Score a hit for Wikipedia usefulness. Higher = better."""
    title = str(hit.get("title") or "")
    kind = classify_title(title)
    reasons: list[str] = [f"kind={kind}"]
    score = 0.0
    subject = clean_query_for_retrieval(query)
    qn = normalize_text(subject or query)
    title_n = normalize_text(title)
    text = str(hit.get("text") or "")
    terms = significant_terms(query)

    bonus, why = _title_match_bonus(query, title)
    if bonus:
        score += bonus
        reasons.append(why)

    # Prefer the canonical page over Medal/School/Peninsula satellites
    subject_n = qn
    title_stripped = normalize_text(strip_parens(strip_leading_article(title)))
    if subject_n and title_n == subject_n:
        score += 12.0
        reasons.append("canonical_exact")
    elif subject_n and (
        title_n.startswith(subject_n + " ")
        or title_n.startswith(subject_n + ",")
    ):
        if _SATELLITE_TITLE_RE.search(title) and not _SATELLITE_TITLE_RE.search(subject or ""):
            score -= 18.0
            reasons.append("penalize_satellite_page")
    # Parenthetical sense pages (planet/element/language) beat random satellites
    if subject_n and title_stripped == subject_n and "(" in title:
        if any(
            s in title_n
            for s in (
                "(planet)",
                "(element)",
                "(programming language)",
                "(disambiguation)",
                "(genus)",
                "(mythology)",
            )
        ):
            score += 8.0
            reasons.append("useful_paren_sense")
        elif _SATELLITE_TITLE_RE.search(title) or "charity" in title_n or "film" in title_n:
            score -= 16.0
            reasons.append("penalize_paren_satellite")
    # One-token queries: prefer Mercury / Python / Beethoven primaries over odd compounds
    if len(terms) == 1:
        term = terms[0]
        if title_stripped == term:
            score += 12.0
            reasons.append("single_token_exact")
        elif title_n.startswith(term + " (") or title_n.startswith(term + ","):
            score += 9.0
            reasons.append("single_token_paren")
        elif term in title_n and not (
            title_stripped == term
            or title_n.startswith(term + " ")
            or title_n.startswith(term + "(")
            or title_n.startswith(term + ",")
        ):
            # "Lil' Beethoven", "List of newspapers named Mercury"
            if title_n.startswith("list of") or _SATELLITE_TITLE_RE.search(title) or "'" in title:
                score -= 14.0
                reasons.append("penalize_nonprimary_token")

    # "Second Industrial Revolution" should not beat "Industrial Revolution" for that query
    if subject_n and title_n != subject_n and subject_n in title_n:
        if title_n.startswith("second ") or title_n.startswith("first "):
            if not subject_n.startswith("second ") and not subject_n.startswith("first "):
                score -= 10.0
                reasons.append("penalize_numbered_variant")

    if _is_year_noise_title(title, query):
        score -= 22.0
        reasons.append("penalize_year_noise")

    # "capital of X" must not rank "capital punishment"
    if "capital of" in qn and "capital punishment" in title_n:
        score -= 30.0
        reasons.append("penalize_capital_punishment")
    if "capital of" in qn:
        m_cap = re.search(r"capital of\s+(.+)$", qn)
        if m_cap:
            place = m_cap.group(1).strip()
            if place and (title_n == place or title_n.startswith(place + " ")):
                score += 16.0
                reasons.append("place_article_for_capital")
            if place and place in text[:800] and re.search(
                r"\bcapital\b", text[:800], re.I
            ):
                score += 10.0
                reasons.append("capital_in_place_lead")

    if kind == "disambiguation":
        if "disambiguation" not in qn:
            score -= 18.0
            reasons.append("penalize_disambiguation")
        else:
            score += 4.0
            reasons.append("disambiguation_requested")
    elif kind == "fictional":
        score -= 20.0
        reasons.append("penalize_fictional")
    elif kind == "list":
        # Lists help "who/what are the…" ; soft-prefer when title shares query terms
        overlap, n = _term_overlap(title, terms)
        if n >= 2 or (n >= 1 and len(terms) <= 3):
            score += 6.0 + (overlap * 4.0)
            reasons.append("useful_list")
        elif not qn.startswith("list ") and "list of" not in qn:
            score -= 2.0
            reasons.append("penalize_list")
    elif kind == "laboratory":
        score -= 2.0
        reasons.append("penalize_lab_unless_queried")
        if "laboratory" in qn or "lab" in qn.split():
            score += 4.0
            reasons.append("lab_query_boost")

    # Tenure / office article pattern (Wikipedia "Presidency of X", "Mayorality of…")
    if re.match(r"^(presidency|mayoralty|premiership|reign) of\b", title_n):
        if any(t in qn for t in ("president", "mayor", "premier", "prime", "king", "queen")):
            score += 14.0
            reasons.append("tenure_article")
            try:
                if int(hit.get("chunk_index")) == 0:
                    score += 8.0
                    reasons.append("tenure_lead")
            except (TypeError, ValueError):
                pass
            if re.search(r"\bmay refer to\b", text[:280], re.I):
                score -= 16.0
                reasons.append("penalize_tenure_disambiguation")

    # Bare Wikipedia "President" dab/office stub must not beat POTUS pages
    if "president of the united states" in qn or _president_topic(query):
        if title_n in {"president", "presidency"}:
            score -= 20.0
            reasons.append("penalize_bare_president_stub")

    # Query-term density in body (general answer-bearing signal)
    text_overlap, text_hits = _term_overlap(text[:2500], terms)
    if text_hits:
        score += min(12.0, text_hits * 2.5 + text_overlap * 4.0)
        reasons.append(f"term_overlap={text_hits}")

    # Snapshot / asked years in the chunk beat empty lead intros
    snapshot_year = str(hit.get("snapshot_year") or "").strip()
    focus_years = _years_mentioned(query, snapshot_year)
    if snapshot_year and snapshot_year in text:
        score += 12.0
        reasons.append("mentions_snapshot_year")
    elif focus_years and any(y in text for y in focus_years):
        score += 7.0
        reasons.append("mentions_focus_year")

    # Explicit date / tenure language helps officeholder and timeline questions
    date_hits = len(_DATE_SPAN_RE.findall(text[:2000]))
    if date_hits >= 2 and any(
        w in qn for w in ("who", "when", "president", "began", "ended", "year")
    ):
        # "who" may have been stripped from cleaned qn — also check raw
        score += min(6.0, date_hits * 1.5)
        reasons.append("date_bearing")
    elif date_hits >= 2 and any(
        w in normalize_text(query) for w in ("who", "when", "president", "began", "ended")
    ):
        score += min(6.0, date_hits * 1.5)
        reasons.append("date_bearing")

    chunk_index = hit.get("chunk_index")
    try:
        ci = int(chunk_index) if chunk_index is not None else 99
    except (TypeError, ValueError):
        ci = 99
    answered = any(
        tag.startswith("term_overlap")
        or tag
        in {
            "mentions_snapshot_year",
            "mentions_focus_year",
            "date_bearing",
            "tenure_lead",
        }
        for tag in reasons
    )
    if answered and (
        "mentions_snapshot_year" in reasons
        or "date_bearing" in reasons
        or "tenure_lead" in reasons
    ):
        score += 3.0
        reasons.append("answer_bearing_chunk")
    elif ci == 0:
        score += 5.0
        reasons.append("lead_chunk")
    elif ci <= 2:
        score += 2.0
        reasons.append("early_chunk")
    elif ci <= 5:
        score += 0.5
    else:
        # Soften late penalty when the late chunk is carrying dates/terms
        if answered:
            score -= 0.25
            reasons.append("late_answer_chunk")
        else:
            score -= 1.0
            reasons.append("late_chunk")

    raw = hit.get("score")
    if isinstance(raw, (int, float)):
        capped = min(float(raw), 2.5)
        score += capped * 1.5
        reasons.append(f"hybrid_score={raw:.3f}")
    dist = hit.get("distance")
    if isinstance(dist, (int, float)):
        score += max(0.0, 1.0 - float(dist)) * 1.5

    if hit.get("from_exact_title"):
        score += 20.0
        reasons.append("exact_title_fetch")
    if hit.get("from_title_bm25"):
        score += 3.0
        reasons.append("title_bm25")

    return score, reasons


def dedupe_by_page(hits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Keep the best-scoring chunk per page_id (or title if no page_id)."""
    best: dict[str, dict[str, Any]] = {}
    order: list[str] = []
    for hit in hits:
        key = str(hit.get("page_id") or "").strip() or normalize_text(
            str(hit.get("title") or "")
        )
        if not key:
            key = f"anon-{len(order)}"
        if key not in best:
            best[key] = hit
            order.append(key)
            continue
        prev = best[key]
        prev_score = float(prev.get("heuristic_score") or 0.0)
        new_score = float(hit.get("heuristic_score") or 0.0)
        try:
            prev_ci = int(prev.get("chunk_index") if prev.get("chunk_index") is not None else 99)
        except (TypeError, ValueError):
            prev_ci = 99
        try:
            new_ci = int(hit.get("chunk_index") if hit.get("chunk_index") is not None else 99)
        except (TypeError, ValueError):
            new_ci = 99
        if new_score > prev_score or (new_score == prev_score and new_ci < prev_ci):
            best[key] = hit
    return [best[k] for k in order]


def diversify_hits(hits: list[dict[str, Any]], top_k: int) -> list[dict[str, Any]]:
    """Prefer a mix of page kinds so Eve sees article + supporting list/tenure."""
    if len(hits) <= top_k:
        return hits
    selected: list[dict[str, Any]] = []
    seen_titles: set[str] = set()
    kinds_used: dict[str, int] = {}

    def _take(hit: dict[str, Any]) -> None:
        title_key = normalize_text(str(hit.get("title") or ""))
        if title_key in seen_titles:
            return
        kind = str(hit.get("kind_hint") or classify_title(str(hit.get("title") or "")))
        selected.append(hit)
        seen_titles.add(title_key)
        kinds_used[kind] = kinds_used.get(kind, 0) + 1

    # First pass: highest score, skip disambiguation until an article is taken
    for hit in hits:
        if len(selected) >= top_k:
            break
        kind = str(hit.get("kind_hint") or "")
        if kind == "disambiguation" and kinds_used.get("article", 0) == 0 and any(
            str(h.get("kind_hint") or "") == "article" for h in hits[:12]
        ):
            continue
        if kind in {"disambiguation", "fictional"} and kinds_used.get("article", 0) == 0:
            continue
        _take(hit)

    # Second pass: fill remaining
    for hit in hits:
        if len(selected) >= top_k:
            break
        _take(hit)

    return selected[:top_k]


def check_reranker() -> dict[str, Any]:
    if not rerank_enabled():
        return {"ok": False, "available": False, "reason": "EMPIRE_WIKI_RERANK disabled"}
    try:
        from sentence_transformers import CrossEncoder  # noqa: F401

        return {
            "ok": True,
            "available": True,
            "model": RERANK_MODEL,
            "hint": "sentence-transformers CrossEncoder ready",
        }
    except ImportError:
        return {
            "ok": False,
            "available": False,
            "reason": "sentence-transformers not installed",
            "hint": "pip install sentence-transformers  # optional BGE rerank",
            "model": RERANK_MODEL,
        }


@lru_cache(maxsize=1)
def _load_cross_encoder():  # type: ignore[no-untyped-def]
    from sentence_transformers import CrossEncoder

    device = os.environ.get("EMPIRE_WIKI_RERANK_DEVICE", "cpu")
    return CrossEncoder(RERANK_MODEL, device=device)


def rerank_hits(
    query: str,
    hits: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Optional BGE cross-encoder rerank. Returns (hits_with_rerank_score, meta)."""
    meta = check_reranker()
    if not meta.get("available") or not hits:
        return hits, {**meta, "applied": False}

    pairs: list[tuple[str, str]] = []
    for hit in hits:
        title = str(hit.get("title") or "")
        text = str(hit.get("text") or "")[:1500]
        doc = f"{title}\n{text}".strip() or title or "(empty)"
        pairs.append((query, doc))

    try:
        model = _load_cross_encoder()
        scores = model.predict(pairs)
    except Exception as exc:  # noqa: BLE001
        return hits, {
            "available": True,
            "applied": False,
            "error": str(exc),
            "model": RERANK_MODEL,
        }

    enriched: list[dict[str, Any]] = []
    for hit, rr in zip(hits, scores, strict=False):
        row = dict(hit)
        try:
            row["rerank_score"] = float(rr)
        except (TypeError, ValueError):
            row["rerank_score"] = 0.0
        enriched.append(row)
    enriched.sort(key=lambda h: float(h.get("rerank_score") or 0.0), reverse=True)
    return enriched, {
        "available": True,
        "applied": True,
        "model": RERANK_MODEL,
        "candidates": len(enriched),
    }


def assess_usability(query: str, cards: list[dict[str, Any]]) -> dict[str, Any]:
    """Gate junk retrieve sets so Eve can refuse to invent."""
    if not cards:
        return {
            "usable": False,
            "confidence": 0.0,
            "reason": "no_cards",
        }
    terms = significant_terms(query)
    subject = clean_query_for_retrieval(query)
    subject_n = normalize_text(subject or query)
    raw_n = normalize_text(query)
    best = 0.0
    best_why = "weak_overlap"
    for card in cards[:4]:
        title = str(card.get("title") or "")
        snippet = str(card.get("snippet") or "")
        title_n = normalize_text(title)
        blob = f"{title} {snippet}"
        overlap, n = _term_overlap(blob, terms)
        score = overlap
        why = f"overlap={n}/{len(terms)}"
        if subject_n and (
            title_n == subject_n
            or title_n.startswith(subject_n + " (")
            or subject_n.startswith(title_n)
        ):
            score = max(score, 0.85)
            why = "title_match"
        elif subject_n and subject_n in title_n and len(subject_n) >= 8:
            score = max(score, 0.7)
            why = "title_contains_subject"
        elif n >= 2:
            score = max(score, 0.55 + overlap * 0.2)
        elif n == 1 and len(terms) <= 4:
            score = max(score, 0.35)
        # Tenure / office pages for who-was
        if re.match(r"^(presidency|mayoralty|premiership) of\b", title_n) and (
            "president" in raw_n or "who" in raw_n
        ):
            score = max(score, 0.8)
            why = "tenure_page"
        if _DATE_SPAN_RE.search(snippet) and any(
            w in raw_n for w in ("who", "when", "last", "first", "president")
        ):
            score = max(score, score + 0.1)
        if score > best:
            best = score
            best_why = why

    # Factoid questions need stronger grounding than soft topical drift
    needs_fact = bool(
        re.search(
            r"\b(when|who|last|first|how many|what year|which year)\b",
            raw_n,
        )
    )
    threshold = 0.5 if needs_fact else 0.35
    usable = best >= threshold
    # "when / last …" needs a date-bearing snippet, not just a related topic page
    if usable and re.search(r"\b(when|last|first)\b", raw_n):
        has_date = any(_DATE_SPAN_RE.search(str(c.get("snippet") or "")) for c in cards[:3])
        if not has_date and best < 0.9:
            usable = False
            best_why = "no_date_in_snippets"
    return {
        "usable": usable,
        "confidence": round(min(1.0, best), 3),
        "reason": best_why if usable else f"below_threshold:{best_why}:{best:.2f}",
        "threshold": threshold,
    }


def best_snippet(
    text: str,
    query: str,
    max_chars: int = 360,
    *,
    focus_year: str | None = None,
) -> str:
    """Pick the sentence/window most useful for answering — not always chunk start."""
    cleaned = re.sub(r"\s+", " ", (text or "").strip())
    if not cleaned:
        return ""
    if len(cleaned) <= max_chars:
        return cleaned

    terms = significant_terms(query)
    focus_years = _years_mentioned(query, focus_year or "")
    sentences = [s.strip() for s in _SENTENCE_SPLIT_RE.split(cleaned) if s.strip()]
    if not sentences:
        return cleaned[: max_chars - 1] + "…"

    def _score_sentence(sent: str) -> float:
        s = 0.0
        overlap, n = _term_overlap(sent, terms)
        s += n * 3.0 + overlap * 2.0
        if any(y in sent for y in focus_years):
            s += 4.0
        if focus_year and focus_year in sent:
            s += 3.0
        if _DATE_SPAN_RE.search(sent):
            s += 3.0
        # Prefer declarative tenure lines — especially end dates for later archives
        if re.search(
            r"\b(began|ended|inaugurat\w*|succeed\w*|became|was elected|incumbent)\b",
            sent,
            re.I,
        ):
            s += 4.0
        if re.search(r"\bended\b", sent, re.I) and focus_year:
            s += 5.0
        if sent.count("|") >= 3:
            s -= 3.0
        return s

    ranked = sorted(sentences, key=_score_sentence, reverse=True)
    best = ranked[0]
    if len(best) < max_chars * 0.45 and len(sentences) > 1:
        idx = sentences.index(best)
        window = " ".join(sentences[max(0, idx - 1) : idx + 2])
        if _score_sentence(window) >= _score_sentence(best):
            best = window

    best = re.sub(r"\s+", " ", best).strip()
    if len(best) <= max_chars:
        return best
    hay = normalize_text(best)
    center = 0
    for term in terms:
        pos = hay.find(term)
        if pos >= 0:
            center = pos
            break
    start = max(0, center - max_chars // 3)
    chunk = best[start : start + max_chars]
    if start > 0:
        chunk = "…" + chunk
    if start + max_chars < len(best):
        chunk = chunk.rstrip() + "…"
    return chunk


def interpret_hits(
    query: str,
    hits: list[dict[str, Any]],
    *,
    top_k: int = DEFAULT_TOP_K,
    use_rerank: bool = True,
    focus_year: str | None = None,
) -> dict[str, Any]:
    """Rank and package hits into Eve-facing cards."""
    if not hits:
        return {
            "ok": True,
            "usable": False,
            "cards": [],
            "count": 0,
            "interpreter": {
                "heuristics": True,
                "rerank": {"applied": False},
                "usable": False,
            },
            "coverage_note": "No encyclopedia hits returned for this query/year.",
            "note": (
                "No encyclopedia hits. These would be page/chunk hits, "
                "not footnote/reference counts."
            ),
        }

    # Optional year focus for compare_years (helps end-date snippets)
    if focus_year:
        enriched_hits: list[dict[str, Any]] = []
        for hit in hits:
            row = dict(hit)
            if not row.get("snapshot_year"):
                row["snapshot_year"] = focus_year
            enriched_hits.append(row)
        hits = enriched_hits

    scored: list[dict[str, Any]] = []
    for hit in hits:
        h_score, reasons = heuristic_score(query, hit)
        # Extra tenure boost when this archive year is the focus
        title_n = normalize_text(str(hit.get("title") or ""))
        text = str(hit.get("text") or "")
        if focus_year and re.match(r"^presidency of\b", title_n):
            if re.search(r"\b(began|ended|inaugurat)", text[:1200], re.I):
                h_score += 8.0
                reasons = list(reasons) + ["focus_year_tenure"]
            if re.search(rf"\bended\b.*{re.escape(focus_year)}|{re.escape(focus_year)}", text[:1200], re.I) or (
                focus_year >= "2025"
                and re.search(r"\bended\b", text[:1200], re.I)
            ):
                h_score += 6.0
                reasons = list(reasons) + ["tenure_end_date"]
        row = dict(hit)
        row["heuristic_score"] = h_score
        row["rank_reasons"] = reasons
        row["kind_hint"] = classify_title(str(hit.get("title") or ""))
        scored.append(row)

    scored = dedupe_by_page(scored)

    # If the archive lacks the bare canonical title, prefer disambiguation /
    # useful paren senses / closest numbered history over Medal/School satellites.
    subject = clean_query_for_retrieval(query)
    subject_n = normalize_text(subject or query)
    has_canonical = any(
        normalize_text(str(h.get("title") or "")) == subject_n for h in scored
    )
    if subject_n and not has_canonical:
        for hit in scored:
            title = str(hit.get("title") or "")
            title_n = normalize_text(title)
            kind = str(hit.get("kind_hint") or "")
            boost = 0.0
            why = list(hit.get("rank_reasons") or [])
            if kind == "disambiguation" and subject_n in title_n:
                boost += 22.0
                why.append("fallback_disambiguation")
            if title_n.startswith(subject_n + " (") and any(
                s in title_n
                for s in (
                    "planet",
                    "element",
                    "programming language",
                    "genus",
                    "mythology",
                )
            ):
                boost += 16.0
                why.append("fallback_paren_sense")
            if subject_n == "industrial revolution" and title_n.startswith(
                "second industrial revolution"
            ):
                boost += 14.0
                why.append("fallback_numbered_history")
            if subject_n in {
                "leonardo da vinci",
                "nile",
                "nile river",
                "marie curie",
                "beethoven",
            }:
                if "science and inventions of leonardo" in title_n:
                    boost += 18.0
                    why.append("fallback_related_article")
                if title_n in {"geography of egypt", "curie family"}:
                    boost += 10.0
                    why.append("fallback_related_article")
                if title_n.startswith("list of compositions by ludwig van beethoven"):
                    boost += 12.0
                    why.append("fallback_related_article")
            if boost:
                hit["heuristic_score"] = float(hit.get("heuristic_score") or 0.0) + boost
                hit["rank_reasons"] = why
    else:
        # Canonical page present — keep disambiguation out of the top cards
        for hit in scored:
            if str(hit.get("kind_hint") or "") == "disambiguation":
                hit["heuristic_score"] = float(hit.get("heuristic_score") or 0.0) - 10.0
                why = list(hit.get("rank_reasons") or [])
                why.append("demote_dab_when_canonical")
                hit["rank_reasons"] = why

    scored.sort(key=lambda h: float(h.get("heuristic_score") or 0.0), reverse=True)

    rerank_query = clean_query_for_retrieval(query) or query
    rerank_meta: dict[str, Any] = {"applied": False}
    if use_rerank and rerank_enabled():
        scored, rerank_meta = rerank_hits(rerank_query, scored)
        if rerank_meta.get("applied"):
            for hit in scored:
                rr = float(hit.get("rerank_score") or 0.0)
                hs = float(hit.get("heuristic_score") or 0.0)
                kind = str(hit.get("kind_hint") or "")
                title = str(hit.get("title") or "")
                blend = hs + (rr * 8.0)
                if kind == "disambiguation" and "disambiguation" not in normalize_text(
                    rerank_query
                ):
                    blend -= 12.0
                if kind == "fictional":
                    blend -= 20.0
                if _BARE_YEAR_RE.match(title.strip()):
                    blend -= 30.0
                hit["blend_score"] = blend
            scored.sort(
                key=lambda h: float(h.get("blend_score") or 0.0),
                reverse=True,
            )

    k = max(1, min(int(top_k), 10))
    selected = diversify_hits(scored, k)
    cards: list[dict[str, Any]] = []
    fy = (focus_year or "").strip() or None
    for idx, hit in enumerate(selected, start=1):
        reasons = list(hit.get("rank_reasons") or [])
        if hit.get("rerank_score") is not None and rerank_meta.get("applied"):
            reasons.append(f"rerank={float(hit['rerank_score']):.3f}")
        snippet = best_snippet(
            str(hit.get("text") or ""),
            query,
            max_chars=360,
            focus_year=fy or str(hit.get("snapshot_year") or "") or None,
        )
        cards.append(
            {
                "rank": idx,
                "title": hit.get("title") or "",
                "year": hit.get("snapshot_year") or fy or "",
                "kind_hint": hit.get("kind_hint")
                or classify_title(str(hit.get("title") or "")),
                "rank_why": "; ".join(reasons[:8]),
                "snippet": snippet,
                "page_id": hit.get("page_id") or "",
                "chunk_id": hit.get("chunk_id") or "",
                "heuristic_score": hit.get("heuristic_score"),
                "rerank_score": hit.get("rerank_score"),
                "_hit": hit,
            }
        )

    usability = assess_usability(query, cards)
    coverage_note = ""
    if not has_canonical:
        coverage_note = (
            f"No page titled exactly {subject!r} in this year's retrieve pool. "
            "That can be a year-specific archive gap (seen on 2021 for some famous "
            "articles that exist in 2017/2026). Try compare_years or another year "
            "before concluding the encyclopedia lacks the topic."
        )
    if not usability.get("usable"):
        junk_note = (
            "USABLE=false: top cards do not look like a reliable answer to this "
            "question (weak title/snippet overlap). Do not invent facts — say the "
            "local encyclopedia did not return a usable page."
        )
        coverage_note = f"{coverage_note} {junk_note}".strip()

    return {
        "ok": True,
        "usable": bool(usability.get("usable")),
        "cards": cards,
        "count": len(cards),
        "candidates_in": len(hits),
        "interpreter": {
            "heuristics": True,
            "rerank": rerank_meta,
            "top_k": k,
            "diversified": True,
            "query_aware_snippets": True,
            "canonical_in_pool": bool(has_canonical),
            "subject": subject or query,
            "focus_year": fy,
            "usable": bool(usability.get("usable")),
            "confidence": usability.get("confidence"),
            "usability_reason": usability.get("reason"),
        },
        "coverage_note": coverage_note,
        "note": (
            "INTERPRETER: These are ranked Wikipedia page/chunk hits from the local "
            "archive — NOT the number of footnotes at the end of an article. "
            "Snapshot years (2017/2021/2026) are frozen encyclopedia dumps, not "
            "hypothetical futures. Quote titles and snippets; respect stated "
            "began/ended dates; do not invent citation counts or extend terms "
            "past dates written in the cards. If usable=false, refuse to invent."
        ),
        "selected_hits": [c["_hit"] for c in cards],
    }


def cards_public(cards: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Strip internal _hit before returning to Eve/MCP."""
    out: list[dict[str, Any]] = []
    for card in cards:
        public = {k: v for k, v in card.items() if k != "_hit"}
        out.append(public)
    return out


def _snippet(text: str, max_chars: int) -> str:
    """Backward-compatible plain trim (prefer best_snippet for cards)."""
    cleaned = re.sub(r"\s+", " ", (text or "").strip())
    if len(cleaned) <= max_chars:
        return cleaned
    return cleaned[: max_chars - 1] + "…"


def candidate_pool_size(final_top_k: int) -> int:
    pool = max(DEFAULT_CANDIDATE_POOL, int(final_top_k) * 4)
    return max(1, min(pool, 50))
