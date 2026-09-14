"""Rank Wikipedia title-to-title neighbors by the user's question.

The link table stores unordered roads. Chat only has room for a dozen names,
so we score those roads against the question (cast vs song vs cheddar) instead
of A–Z order. No embeddings.
"""

from __future__ import annotations

import re
from typing import Iterable, Literal

from pipeline.wiki_interpreter import conversational_lookup_queries
from pipeline.wiki_title_matcher import normalize_text

LookupKind = Literal["song", "cast", "bio", "generic"]

_QUESTION_STOP = frozenset(
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
        "what",
        "who",
        "whom",
        "which",
        "whose",
        "when",
        "where",
        "why",
        "how",
        "did",
        "does",
        "do",
        "got",
        "get",
        "tell",
        "me",
        "about",
        "during",
        "later",
        "seasons",
        "season",
        "series",
        "show",
        "tv",
        "television",
        "played",
        "actors",
        "actor",
        "cast",
        "her",
        "his",
        "their",
        "career",
        "that",
        "this",
        "was",
        "were",
        "is",
        "are",
        "became",
        "again",
        "popular",
        "reinvigorated",
        "listen",
        "track",
    }
)
_SONG_QUESTION_RE = re.compile(
    r"\b(?:songs?|albums?|singles?|tracks?|soundtrack|discography|"
    r"80s|80's|eighties|1980s?|hit\s+again|re-?popular|featured)\b",
    re.I,
)
_CAST_QUESTION_RE = re.compile(
    r"\b(?:actors?|actress(?:es)?|cast|starred|played|characters?)\b",
    re.I,
)
_BIO_QUESTION_RE = re.compile(r"^\s*who\s+(?:is|are|was|were)\b", re.I)
_SONG_TITLE_RE = re.compile(r"\([^)]*\bsong\b[^)]*\)\s*$", re.I)
_PERSON_TITLE_RE = re.compile(r"\([^)]*\b(?:actor|actress|singer|rapper|musician)\b[^)]*\)\s*$", re.I)
_NOISE_TITLE_RE = re.compile(
    r"^(?:list of\b|.*\bin music$|allmusic$|bbc news$|billboard \(magazine\)$)",
    re.I,
)
_WOW_SONG_RE = re.compile(r"^wow\b.*\bsong\b", re.I)


def classify_lookup_kind(question: str) -> LookupKind:
    raw = (question or "").strip()
    if _BIO_QUESTION_RE.search(raw):
        return "bio"
    if _CAST_QUESTION_RE.search(raw):
        return "cast"
    if _SONG_QUESTION_RE.search(raw):
        return "song"
    return "generic"


def _question_tokens(question: str) -> set[str]:
    parts = re.findall(r"[a-z0-9']+", (question or "").casefold())
    kept: set[str] = set()
    for part in parts:
        if part in _QUESTION_STOP or len(part) < 3:
            continue
        kept.add(part)
    return kept


def _variant_weights(question: str) -> dict[str, float]:
    weights: dict[str, float] = {}
    try:
        variants = conversational_lookup_queries(question)
    except Exception:  # noqa: BLE001 — ranking must not fail lookup
        variants = []
    for index, item in enumerate(variants):
        key = normalize_text(item)
        if not key or key in weights:
            continue
        weights[key] = 120.0 - (index * 12.0)
    return weights


def score_related_title(
    title: str,
    question: str,
    *,
    landing_title: str = "",
    kind: LookupKind | None = None,
    variant_norms: dict[str, float] | None = None,
) -> float:
    text = (title or "").strip()
    if not text:
        return -100.0
    intent = kind or classify_lookup_kind(question)
    hints = variant_norms if variant_norms is not None else _variant_weights(question)
    key = normalize_text(text)
    landing_key = normalize_text(landing_title)
    if key and key == landing_key:
        return -50.0
    score = 0.0
    if key in hints:
        score += float(hints[key])
    q_tokens = _question_tokens(question)
    title_tokens = set(re.findall(r"[a-z0-9']+", text.casefold()))
    landing_tokens = set(re.findall(r"[a-z0-9']+", (landing_title or "").casefold()))
    overlap = (q_tokens & title_tokens) - landing_tokens
    score += 28.0 * len(overlap)
    if intent == "song":
        if _SONG_TITLE_RE.search(text):
            score += 40.0
        if _WOW_SONG_RE.search(text) and "wow" not in (question or "").casefold():
            score -= 90.0
        if _NOISE_TITLE_RE.search(text):
            score -= 50.0
    elif intent == "cast":
        if _PERSON_TITLE_RE.search(text):
            score += 55.0
        elif re.fullmatch(r"[A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}", text):
            score += 35.0
        if _NOISE_TITLE_RE.search(text):
            score -= 40.0
    if _NOISE_TITLE_RE.search(text):
        score -= 15.0
    return score


def rank_related_titles(
    titles: Iterable[str],
    question: str,
    *,
    landing_title: str = "",
) -> list[str]:
    kind = classify_lookup_kind(question)
    hints = _variant_weights(question)
    seen: set[str] = set()
    unique: list[str] = []
    for raw in titles:
        text = str(raw or "").strip()
        if not text:
            continue
        key = normalize_text(text)
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(text)
    scored = [
        (
            score_related_title(
                title,
                question,
                landing_title=landing_title,
                kind=kind,
                variant_norms=hints,
            ),
            idx,
            title,
        )
        for idx, title in enumerate(unique)
    ]
    scored.sort(key=lambda row: (-row[0], row[1]))
    return [title for _score, _idx, title in scored]


def select_hop_titles(
    ranked: list[str],
    question: str,
    *,
    landing_title: str = "",
    limit: int = 1,
) -> list[str]:
    """Open at most one neighbor lead when the question is about that neighbor."""
    kind = classify_lookup_kind(question)
    if kind in {"bio", "cast"}:
        return []
    landing_key = normalize_text(landing_title)
    cap = max(1, min(int(limit), 2))
    hops: list[str] = []
    if kind == "song":
        for title in ranked:
            if normalize_text(title) == landing_key:
                continue
            hops.append(title)
            if len(hops) >= cap:
                break
        return hops
    q_tokens = _question_tokens(question)
    landing_tokens = set(re.findall(r"[a-z0-9']+", (landing_title or "").casefold()))
    extra = q_tokens - landing_tokens - {"cheese"}
    if not extra:
        return []
    for title in ranked:
        if normalize_text(title) == landing_key:
            continue
        title_tokens = set(re.findall(r"[a-z0-9']+", title.casefold()))
        if extra & title_tokens:
            hops.append(title)
            break
    return hops
