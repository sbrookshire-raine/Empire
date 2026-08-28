"""Title/alias-only subject matcher for Wiki Ops priority resolve."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import asdict, dataclass
from typing import Any, Literal

MatchTier = Literal["exact", "exact_stripped", "starts_with", "contains"]

PAREN_TRAIL_RE = re.compile(r"\s*\([^)]*\)\s*$")
LEADING_ARTICLE_RE = re.compile(r"^(the|an|a)\s+", re.IGNORECASE)

# Bare titles that are useless as priority matches (and as starts_with prefixes).
TITLE_STOPWORDS = frozenset(
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
        "t",
        "s",
    }
)
# Minimum significant title length for starts_with / contains prefix games.
MIN_SIGNIFICANT_TITLE_LEN = 5


def normalize_text(s: str) -> str:
    text = unicodedata.normalize("NFKC", str(s or ""))
    text = text.casefold()
    text = re.sub(r"\s+", " ", text).strip()
    return text


def strip_parens(s: str) -> str:
    return PAREN_TRAIL_RE.sub("", str(s or "")).strip()


def strip_leading_article(s: str) -> str:
    return LEADING_ARTICLE_RE.sub("", str(s or "")).strip()


def is_useless_title(title: str) -> bool:
    """True for stopwords / single letters / tiny stubs like 'The', 'T', 'A'."""
    norm = normalize_text(title)
    if not norm:
        return True
    if norm in TITLE_STOPWORDS:
        return True
    if len(norm) < MIN_SIGNIFICANT_TITLE_LEN and " " not in norm:
        return True
    return False


def _word_boundary_prefix(longer: str, shorter: str) -> bool:
    """True if shorter is a whole-word prefix of longer (not 'bala' of 'balancing')."""
    if not longer.startswith(shorter):
        return False
    if len(longer) == len(shorter):
        return True
    return longer[len(shorter)] in " \t-–—:/"


def subject_match_forms(subject: str) -> list[str]:
    """Normalized subject strings to score against (full + article-stripped)."""
    forms: list[str] = []
    full = normalize_text(subject)
    if full:
        forms.append(full)
    stripped = normalize_text(strip_leading_article(subject))
    if stripped and stripped not in forms:
        forms.append(stripped)
    no_parens = normalize_text(strip_parens(strip_leading_article(subject)))
    if no_parens and no_parens not in forms:
        forms.append(no_parens)
    return forms


@dataclass(frozen=True)
class Candidate:
    title: str
    path: str
    page_id: str
    score: float
    match_tier: MatchTier

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _aliases_of(entry: dict[str, Any]) -> list[str]:
    aliases: list[str] = []
    for key in ("aliases", "redirects"):
        raw = entry.get(key) or []
        if isinstance(raw, str):
            aliases.append(raw)
        elif isinstance(raw, list):
            aliases.extend(str(a) for a in raw if str(a).strip())
    return aliases


def _score_pair(subject_norm: str, title: str) -> tuple[float, MatchTier] | None:
    title_norm = normalize_text(title)
    if not subject_norm or not title_norm:
        return None
    # Never offer bare articles / letters as Wikipedia "matches".
    if is_useless_title(title_norm):
        return None
    if title_norm == subject_norm:
        return 1.00, "exact"
    subj_stripped = normalize_text(strip_parens(subject_norm))
    title_stripped = normalize_text(strip_parens(title))
    if title_stripped and is_useless_title(title_stripped):
        return None
    if subj_stripped and title_stripped and subj_stripped == title_stripped:
        return 0.95, "exact_stripped"
    # starts_with only on whole-word prefixes, never syllable stubs ("bala"/"emer").
    if title_norm.startswith(subject_norm) or subject_norm.startswith(title_norm):
        if len(title_norm) <= len(subject_norm):
            shorter_s, longer_s = title_norm, subject_norm
        else:
            shorter_s, longer_s = subject_norm, title_norm
        if is_useless_title(shorter_s) or len(shorter_s) < MIN_SIGNIFICANT_TITLE_LEN:
            return None
        if not _word_boundary_prefix(longer_s, shorter_s):
            return None
        shorter = len(shorter_s)
        longer = len(longer_s)
        ratio = shorter / longer if longer else 0.0
        score = 0.80 + 0.14 * ratio
        return round(min(0.94, score), 4), "starts_with"
    tokens = title_norm.split()
    if subject_norm in tokens and not is_useless_title(subject_norm):
        return 0.75, "contains"
    if subject_norm in title_norm and len(subject_norm) >= MIN_SIGNIFICANT_TITLE_LEN:
        # Prefer shorter titles within contains band.
        density = len(subject_norm) / max(len(title_norm), 1)
        score = 0.60 + 0.19 * density
        return round(min(0.79, score), 4), "contains"
    return None


def score_subject_against_titles(
    subject: str,
    catalog: list[dict[str, Any]],
    *,
    candidate_limit: int = 10,
) -> list[Candidate]:
    subject_forms = subject_match_forms(subject)
    if not subject_forms:
        return []
    scored: list[Candidate] = []
    seen_paths: set[str] = set()
    for entry in catalog:
        title = str(entry.get("title") or "").strip()
        path = str(entry.get("path") or "").strip()
        page_id = str(entry.get("page_id") or "").strip()
        if is_useless_title(title):
            continue
        names = [title, *_aliases_of(entry)]
        best: tuple[float, MatchTier] | None = None
        matched_title = title
        for name in names:
            if is_useless_title(name):
                continue
            for subject_norm in subject_forms:
                pair = _score_pair(subject_norm, name)
                if pair is None:
                    continue
                if best is None or pair[0] > best[0]:
                    best = pair
                    matched_title = title or name
        if best is None or best[0] < 0.60:
            continue
        key = path or f"{matched_title}|{page_id}"
        if key in seen_paths:
            continue
        seen_paths.add(key)
        scored.append(
            Candidate(
                title=matched_title,
                path=path,
                page_id=page_id,
                score=best[0],
                match_tier=best[1],
            )
        )
    scored.sort(key=lambda c: (-c.score, len(c.title), c.title.casefold()))
    return scored[: max(1, int(candidate_limit))]


def decide_match(
    candidates: list[Candidate],
    *,
    auto_min_score: float = 0.90,
    auto_margin: float = 0.05,
) -> dict[str, Any]:
    eligible = [c for c in candidates if c.score >= 0.60]
    if not eligible:
        return {
            "decision": "unmatched",
            "primary": None,
            "candidates": [],
            "suggestions": list(candidates[:5]),
        }
    best = eligible[0]
    second = eligible[1] if len(eligible) > 1 else None
    margin_ok = second is None or (best.score - second.score) >= auto_margin
    alone = len(eligible) == 1
    # Auto only for a clear single primary. Exact+competitors (e.g. "guitar")
    # stay needs_confirm so contains-hits are never batch-enqueued.
    auto = alone and (
        best.score >= 1.0 or (best.score >= auto_min_score and margin_ok)
    )
    if auto:
        return {
            "decision": "auto",
            "primary": best,
            "candidates": eligible,
            "suggestions": [],
        }
    return {
        "decision": "needs_confirm",
        "primary": None,
        "candidates": eligible,
        "suggestions": [],
    }
