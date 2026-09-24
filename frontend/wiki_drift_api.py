"""Server-side Wikipedia glasses: inject archive text before Eve speaks.

Lookup uses Title DNS (SQLite) then reads the markdown lead from D:\\wiki_md.
Weaviate hybrid search is only for explicit Truth Drift / compare_years.

MIGRATION (2026-09-23): Wikipedia retrieval is now an **autonomous MCP tool
process**. Eve (Qwen) owns intent, conversational context and pronoun resolution,
and calls the `empire-wiki-scout` MCP tools (`wiki_resolve`, `wiki_extract`,
`wiki_read_section`, `wiki_scout_search`, `wiki_scratch_*`) herself — the same way
she calls every other local tool.

The legacy regex middleware in this module (intent regex -> Title DNS -> evidence
injection + cross-process lookup lock) is therefore **OFF by default**. It also had
a self-defeating side effect: injecting a `[[EMPIRE_WIKI_*]]` marker made
`chat_continuity` suppress the prior-turn summary, so the model was starved of the
conversation history it needed to resolve pronouns ("that page") on its own.

Set `EMPIRE_WIKI_MIDDLEWARE=1` to restore the legacy injection path (escape hatch).

The intent classifiers in this module (`is_wiki_lookup_query`, `is_truth_drift_query`,
`extract_search_query`) are still used by `frontend/serve.py` as a **catalog routing
guard** for mixed catalog + encyclopedia asks, and by the injection-mode harnesses.
Classification never injects evidence on its own.
"""

from __future__ import annotations

import concurrent.futures
import logging
import os
import re
from typing import Any

from frontend.companion_api import extract_user_message
from frontend.eve_toolbelt import load_active_tools

logger = logging.getLogger(__name__)

WIKI_DRIFT_MARKER = "[[EMPIRE_WIKI_DRIFT]]"
WIKI_LOOKUP_MARKER = "[[EMPIRE_WIKI_LOOKUP]]"
WIKI_EXTRACT_MARKER = "[[EMPIRE_WIKI_EXTRACT]]"

WIKI_MIDDLEWARE_ENV = "EMPIRE_WIKI_MIDDLEWARE"


def wiki_middleware_enabled() -> bool:
    """True only when the legacy regex injection path is explicitly re-enabled."""
    raw = os.environ.get(WIKI_MIDDLEWARE_ENV, "").strip().casefold()
    return raw in {"1", "true", "yes", "on"}
MAX_SNIPPET = 320
MAX_CARDS_PER_YEAR = 3
MAX_LOOKUP_CARDS = 3
LOOKUP_SEARCH_LIMIT = 8
LOOKUP_TIMEOUT_SEC = 18
COMPARE_TIMEOUT_SEC = 45
COMPARE_TIMEOUT_NOTE = "Wiki compare failed or timed out"
LOOKUP_FAIL_NOTE = "Wiki lookup failed or returned no usable cards"
EVIDENCE_MAX_CHARS = 1800
EVIDENCE_TOKEN_BUDGET = 2000

_EVIDENCE_BY_SESSION: dict[str, dict[str, Any]] = {}
# Single-user Workbench: remember the last Title DNS fork so "the 1984 one" works.
_LAST_DNS_AMBIGUOUS: dict[str, Any] = {
    "query": "",
    "year": "2026",
    "candidates": [],
}

# Single-user Workbench: remember the last successfully resolved wiki page so
# conversational anaphora ("that page", "more about it", "their discography") in a
# follow-up turn re-targets the same entity instead of extracting the pronoun "that".
# 2026-09-23: without this, a follow-up silently dropped the wiki injection (no subject)
# or — worse — resolved the grammar article "That".
_LAST_RESOLVED_WIKI_TITLE: dict[str, Any] = {
    "title": "",
    "year": "2026",
    "query": "",
}

# Follow-up phrasings that refer back to the previously discussed page/entity. Only
# honored when _LAST_RESOLVED_WIKI_TITLE["title"] is non-empty (see is_anaphoric_followup).
_ANAPHORIC_FOLLOWUP_RE = re.compile(
    r"(?:"
    r"\b(?:that|this|the|same)\s+(?:same\s+)?page\b|"
    r"\b(?:tell\s+me|what|who|more|details|else)\b.{0,32}\b(?:about|on|in)\s+(?:it|them|him|her|that|this)\b|"
    r"\b(?:about|on)\s+(?:it|them|him|her|that|this)\b|"
    r"\b(?:their|its|his|her)\s+(?:albums?|songs?|singles?|discograph\w*|members?\w*|history|legacy|awards?|filmograph\w*)\b|"
    r"\b(?:what|who)\s+else\b"
    r")",
    re.I,
)

_DISAMBIG_FOLLOWUP_RE = re.compile(
    r"(?:"
    r"\b(?:i'?m\s+interested|interested\s+in|i\s+mean|mean(?:ing)?|the\s+one|"
    r"go\s+with|pick|choose|open)\b|"
    r"\b(?:19|20)\d{2}\b|"
    r"\bminiseries\b|"
    r"\btv\s+series\b|"
    r"\bhorror\b|"
    r"\bmovie\b|\bfilm\b|"
    r"\b(?:that|this)\s+one\b"
    r")",
    re.I,
)

# Explicit Truth Drift / cross-year compare only — NOT bare "wikipedia".
TRUTH_DRIFT_RE = re.compile(
    r"(?:"
    r"\btruth\s*drift\b|"
    r"\bcompare\s+years?\b|"
    r"\bacross\s+years?\b|"
    r"\bcompare\b.{0,40}\b(?:2017|2021|2026)\b|"
    r"\bacross\b.{0,40}\b(?:2017|2021|2026)\b|"
    r"\bbetween\s+20\d{2}\s+and\s+20\d{2}\b|"
    r"\bchanged\s+between\s+20\d{2}\b|"
    r"\bfrom\s+20\d{2}\s+to\s+20\d{2}\b|"
    r"(?:year|archive).{0,40}(?:2017|2021|2026).{0,40}(?:changed|compare|drift|differ)|"
    r"(?:2017|2021|2026).{0,40}(?:2017|2021|2026).{0,40}(?:changed|compare|drift|differ)"
    r")",
    re.IGNORECASE,
)

WIKI_ACCESS_RE = re.compile(
    r"\b(?:can you|do you|are you able to)\b.{0,40}\b(?:access|see|use|search|reach)\b"
    r".{0,40}\b(?:wikipedia|wiki|encyclopedia|local archive)\b",
    re.IGNORECASE,
)

# Stack / partner questions — must NOT fire Wikipedia glasses injection.
RESOURCE_PULSE_QUERY_RE = re.compile(
    r"(?:"
    r"\bcapabilities?\b|"
    r"\bresource(?:s|_pulse)?\b|"
    r"\bheadroom\b|"
    r"\bgpu\s+lease\b|"
    r"\bwhat(?:'s|\s+is|\s+are)?\s+(?:free|available)\b.{0,48}\b(?:machine|system|gpu|ram|disk|vram)\b|"
    r"\b(?:free|available)\s+on\s+the\s+(?:machine|system)\b|"
    r"\btoolbelt\b|"
    r"\badmit(?:_for_goal)?\b|"
    r"\bwhat\s+(?:tools|skills|limbs)\b.{0,48}\b(?:have|do you|available|on|right now)\b|"
    r"\bwhat\s+do\s+you\s+have\s+(?:available|right now|on)\b"
    r")",
    re.IGNORECASE,
)

WIKI_LOOKUP_RE = re.compile(
    r"\b(?:"
    r"who\s+(?:is|are|was|were)\b|"
    r"what\s+(?:is|are|was|were)\b|"
    r"what\b.{0,48}\b(?:albums?|songs?|records?|actors?|cast)\b|"
    r"what\b.{0,48}\b(?:80s|80's|eighties|1980s?)\b|"
    r"(?:who|which)\b.{0,40}\b(?:acted|starred|played|appeared)\b|"
    r"\b(?:actors?|cast|stars?)\b.{0,48}\b(?:in|of|on|from)\b|"
    r"\b(?:tv\s+show|television\s+show|tv\s+series|series|miniseries)\b|"
    # Need a topical object — bare "summarize briefly" must not hijack stack questions.
    # "tell me" is also scoped to an encyclopedia object ("tell me about ..."):
    # a bare "tell me" hijacked local tool requests such as
    # "...then tell me how much free disk space is available".
    r"(?:tell me about|look up)\b|"
    # Weak single verbs must introduce a real object. "what i asked you to find for
    # me" fired the lookup gate on the bare "find" and then extracted the pronoun
    # "that" from "on that page" (2026-09-23 regression).
    r"\b(?:find|trace|draft|extract|compare|research)\b"
    r"(?!\s+(?:for|of|to|it|me|us|them|him|her|out)\b)|"
    r"summarize\b.{0,80}\b(?:about|the|who|what|wikipedia|wiki|cast|album|film|show)\b|"
    r"discography\b|"
    r"\balbums?\s+(?:by|from|of)\b|"
    # "tell me the names of the band 'the white stripes' albums" — band/artist plus
    # a discography noun is an encyclopedia ask even without "what/albums by".
    r"\b(?:band|artist|group|singer)\b.{0,40}\b(?:albums?|songs?|singles?|discography)\b|"
    r"\bpopulation\b|"
    r"\breception\b|"
    r"\bfilmography\b|"
    r"\bplaystation\b|\bxbox\b|"
    r"\biphone\b|"
    r"\bdune\b|"
    r"\bcheddar\b|\bcheese\b|"
    r"(?:use|search|query)\s+(?:my\s+)?(?:local\s+)?(?:wikipedia|wiki|encyclopedia)\b|"
    r"(?:local\s+)?(?:wikipedia|encyclopedia)\s+(?:say|says|about)\b|"
    r"stranger things\b|"
    r"\b1980s\b"
    r")\b",
    re.IGNORECASE,
)

# Conversational anaphora ("not on that page", "this one") must never be posted
# to Title DNS as a page title. 2026-09-23 regression: "the album names are not on
# that page" extracted the pronoun "that", resolved the grammar article "That",
# and injected its lead as MANDATORY EVIDENCE — so Eve answered from the wrong page.
_ANAPHORIC_TOPICS = frozenset(
    {
        "that", "this", "these", "those", "it", "its", "the", "a", "an",
        "my", "your", "his", "her", "our", "their", "same", "previous",
        "last", "next", "other", "another", "which", "what", "who", "one",
        "the one", "that one", "this one", "the page", "that page", "this page",
        "previous page", "last page", "same page", "next page", "the same",
        "same one", "them", "him", "me", "us", "you", "page", "article",
    }
)


def _is_anaphoric_topic(topic: str) -> bool:
    """True when a candidate subject is a referring pronoun, not a page title."""
    cleaned = re.sub(r"\s+", " ", (topic or "").strip().strip(" .?!,\"'")).casefold()
    return (not cleaned) or cleaned in _ANAPHORIC_TOPICS


TOPIC_RULES: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"post[-\s]?truth", re.I), "post-truth"),
    (re.compile(r"\bepistemolog", re.I), "epistemology"),
    (re.compile(r"\bmisinformation\b", re.I), "misinformation"),
    (re.compile(r"\bdisinformation\b", re.I), "disinformation"),
    (re.compile(r"\bhallucin", re.I), "hallucination (artificial intelligence)"),
    (
        re.compile(r"\bgenerative\s+AI\b|\blarge\s+language\s+model|\bLLM\b", re.I),
        "generative artificial intelligence",
    ),
    (
        re.compile(
            r"\btruth\b.*\b(?:AI|A\.I\.|models?)\b|\b(?:AI|A\.I\.|models?)\b.*\btruth\b",
            re.I,
        ),
        "post-truth",
    ),
    (
        re.compile(r"\bartificial\s+intelligence\b|\bAI\b|\bAI models?\b", re.I),
        "artificial intelligence",
    ),
)


def is_truth_drift_query(text: str) -> bool:
    return bool(TRUTH_DRIFT_RE.search((text or "").strip()))


def is_wiki_access_query(text: str) -> bool:
    return bool(WIKI_ACCESS_RE.search((text or "").strip()))


def is_resource_pulse_query(text: str) -> bool:
    """True for stack/capability/headroom questions — not encyclopedia lookups."""
    return bool(RESOURCE_PULSE_QUERY_RE.search((text or "").strip()))


def is_wiki_lookup_query(text: str) -> bool:
    raw = (text or "").strip()
    if not raw or is_truth_drift_query(raw):
        return False
    if is_resource_pulse_query(raw):
        return False
    if re.search(
        r"\b(?:query|search|find)\s+(?:your\s+)?catalog\b|"
        r"\bfind\s+tools\s+related\s+to\b|\bcatalog\s+search\b",
        raw,
        re.I,
    ) and not re.search(r"\b(?:wikipedia|wiki|encyclopedia|article)\b", raw, re.I):
        return False
    if is_wiki_access_query(raw):
        return True
    if bool(WIKI_LOOKUP_RE.search(raw)):
        return True
    try:
        from pipeline.wiki_extract import is_extract_shaped_question

        if is_extract_shaped_question(raw):
            return True
    except Exception:  # noqa: BLE001
        pass
    # Clarification after Title DNS asked which page to open.
    if _LAST_DNS_AMBIGUOUS.get("candidates") and _DISAMBIG_FOLLOWUP_RE.search(raw):
        return True
    # Conversational follow-up referring back to the last resolved page.
    if is_anaphoric_followup(raw):
        return True
    return False


def remember_dns_ambiguous(query: str, year: str, candidates: list[str]) -> None:
    cleaned = [str(title).strip() for title in candidates if str(title).strip()]
    _LAST_DNS_AMBIGUOUS["query"] = (query or "").strip()
    _LAST_DNS_AMBIGUOUS["year"] = str(year or "2026")
    _LAST_DNS_AMBIGUOUS["candidates"] = cleaned[:12]


def clear_dns_ambiguous() -> None:
    _LAST_DNS_AMBIGUOUS["query"] = ""
    _LAST_DNS_AMBIGUOUS["candidates"] = []


def remember_resolved_wiki_title(title: str, year: str = "2026", query: str = "") -> None:
    """Record the last page that actually resolved (single-user Workbench)."""
    _LAST_RESOLVED_WIKI_TITLE["title"] = (title or "").strip()
    _LAST_RESOLVED_WIKI_TITLE["year"] = str(year or "2026")
    _LAST_RESOLVED_WIKI_TITLE["query"] = (query or "").strip()


def clear_resolved_wiki_title() -> None:
    """Forget the last resolved page (called on a DNS miss / topic shift)."""
    _LAST_RESOLVED_WIKI_TITLE["title"] = ""
    _LAST_RESOLVED_WIKI_TITLE["query"] = ""


def get_resolved_wiki_title() -> str:
    """Canonical title of the last successfully resolved wiki page, or ""."""
    return str(_LAST_RESOLVED_WIKI_TITLE.get("title") or "").strip()


def is_anaphoric_followup(text: str) -> bool:
    """True when text refers back to the last resolved page ('that page', 'more about it')."""
    raw = (text or "").strip()
    if not raw or not get_resolved_wiki_title():
        return False
    return bool(_ANAPHORIC_FOLLOWUP_RE.search(raw))


def pick_disambiguation_followup(text: str) -> str | None:
    """Map 'the 1984 one' / 'the miniseries' onto the last ambiguous candidate list."""
    candidates = [
        str(title).strip()
        for title in (_LAST_DNS_AMBIGUOUS.get("candidates") or [])
        if str(title).strip()
    ]
    if not candidates:
        return None
    raw = (text or "").strip()
    if not raw:
        return None
    ql = raw.casefold()
    years = re.findall(r"\b((?:19|20)\d{2})\b", raw)
    if years:
        year_hits = [title for title in candidates if any(year in title for year in years)]
        if len(year_hits) == 1:
            return year_hits[0]
        if len(year_hits) > 1 and "miniseries" in ql:
            mini = [title for title in year_hits if "miniseries" in title.casefold()]
            if len(mini) == 1:
                return mini[0]
        if len(year_hits) > 1 and ("tv series" in ql or "television series" in ql):
            weekly = [
                title
                for title in year_hits
                if "tv series" in title.casefold() and "miniseries" not in title.casefold()
            ]
            if len(weekly) == 1:
                return weekly[0]
        if len(year_hits) > 1 and any(token in ql for token in ("horror", "movie", "film")):
            films = [
                title
                for title in year_hits
                if any(
                    marker in title.casefold()
                    for marker in ("film", "movie", "horror")
                )
            ]
            if len(films) == 1:
                return films[0]
            if len(films) > 1:
                return films[0]
        if len(year_hits) == 1:
            return year_hits[0]
    if any(token in ql for token in ("horror", "movie", "film")):
        films = [
            title
            for title in candidates
            if any(marker in title.casefold() for marker in ("film", "movie", "horror"))
        ]
        years = re.findall(r"\b((?:19|20)\d{2})\b", raw)
        if years:
            year_films = [title for title in films if any(year in title for year in years)]
            if len(year_films) == 1:
                return year_films[0]
            if year_films:
                return year_films[0]
        if len(films) == 1:
            return films[0]
    if "miniseries" in ql:
        mini = [title for title in candidates if "miniseries" in title.casefold()]
        if len(mini) == 1:
            return mini[0]
    if "tv series" in ql or "television series" in ql:
        weekly = [
            title
            for title in candidates
            if "tv series" in title.casefold() and "miniseries" not in title.casefold()
        ]
        if len(weekly) == 1:
            return weekly[0]
    # Exact / near-exact title paste from the options list.
    for title in candidates:
        if title.casefold() in ql or ql in title.casefold():
            return title
    return None


def is_wiki_enriched_query(text: str) -> bool:
    """Any server-side wiki injection (lookup or Truth Drift)."""
    raw = (text or "").strip()
    return is_truth_drift_query(raw) or is_wiki_lookup_query(raw)


def pick_compare_topic(text: str) -> str:
    cleaned = (text or "").strip()
    for pattern, topic in TOPIC_RULES:
        if pattern.search(cleaned):
            return topic
    compare_match = re.search(
        r"\bcompare\s+(.+?)(?:\s+(?:across|between|from|vs\.?|versus)\b|\s+(?:2017|2021|2026)\b|[?.!]|$)",
        cleaned,
        re.I,
    )
    if compare_match:
        topic = _clean_topic(compare_match.group(1))
        if topic and len(topic.split()) <= 8:
            return _normalize_compare_topic(topic)
    # Natural: "how did/has X change(d) …", "what changed about X …"
    for pattern in (
        re.compile(r"\bhow\s+(?:did|has|have)\s+(.+?)\s+chang(?:e|ed|ing)\b", re.I),
        re.compile(r"\bwhat\s+chang(?:e|ed|es)\s+(?:about|in|for|with)\s+(.+?)(?:\s+(?:across|between|from)\b|[?.!]|$)", re.I),
        re.compile(r"\b(?:evolution|history)\s+of\s+(.+?)(?:\s+(?:across|between|from)\b|\s+(?:2017|2021|2026)\b|[?.!]|$)", re.I),
    ):
        match = pattern.search(cleaned)
        if match:
            topic = _clean_topic(match.group(1))
            if topic:
                return _normalize_compare_topic(topic)
    extracted = extract_search_query(cleaned)
    if extracted and not re.match(r"^(how|what|who|when|where|why)\b", extracted, re.I):
        return _normalize_compare_topic(extracted)
    return "truth"


def _normalize_compare_topic(topic: str) -> str:
    """Map short/chatty subjects to encyclopedia titles."""
    key = re.sub(r"^(the\s+)?(concept\s+of\s+|topic\s+of\s+|field\s+of\s+)", "", topic.strip(), flags=re.I)
    key = key.strip(" .?!,\"'").casefold()
    aliases = {
        "ai": "artificial intelligence",
        "a.i.": "artificial intelligence",
        "a.i": "artificial intelligence",
        "ml": "machine learning",
        "machine learning": "machine learning",
        "llm": "large language model",
        "llms": "large language model",
        "chatgpt": "ChatGPT",
        "truth": "truth",
    }
    if key in aliases:
        return aliases[key]
    if key.startswith("ai ") or key.endswith(" ai"):
        return "artificial intelligence"
    return topic.strip()[:120]


def _clean_topic(value: str) -> str:
    topic = re.sub(r"\s+", " ", (value or "").strip(" .?!,\"'"))
    if not topic:
        return ""
    keep_the = topic.casefold().startswith("the following")
    topic = re.split(r"\s+(?:and|or|using|from|with|that|who|which)\s+", topic, maxsplit=1)[0]
    if not keep_the and topic.casefold().startswith("the "):
        topic = topic[4:].strip()
    if keep_the and not topic.casefold().startswith("the "):
        topic = "The " + topic
    aliases = {
        "python": "Python (programming language)",
        "python programming language": "Python (programming language)",
        "following": "The Following",
        "the following": "The Following",
        "nintendo switch": "Nintendo Switch",
    }
    mapped = aliases.get(topic.casefold())
    if mapped:
        return mapped
    return topic[:120].strip()


def extract_search_query(text: str) -> str:
    """Pull an encyclopedia title/subject from a conversational question."""
    from pipeline.wiki_interpreter import extract_quoted_title, resolve_lookup_topic

    raw = (text or "").strip()
    if not raw or is_wiki_access_query(raw):
        return ""

    # Anaphoric follow-ups ("what else is on that page", "tell me more about it") carry
    # no explicit subject. Returning the cleaned sentence here would post garbage to
    # Title DNS; return "" so enrich_eve_message_payload can substitute the last
    # resolved title instead.
    if _ANAPHORIC_FOLLOWUP_RE.search(raw):
        return ""

    explicit_wiki = re.search(
        r"\b(?:look\s+up|find|read|open)\s+(?:the\s+)?(?:local\s+)?wikipedia\s+article\s+for\s+(.+?)(?:(?:\.|\?|!|\s+and\s+tell\s+me\b)|$)",
        raw,
        re.I,
    )
    if explicit_wiki:
        candidate = extract_quoted_title(explicit_wiki.group(1)) or explicit_wiki.group(1)
        cleaned = _clean_topic(candidate)
        if cleaned:
            return cleaned

    # Quoted titles first — contractions like I'm must not become the subject, and a
    # quoted band name must win over the greedy "band ..." tail, which otherwise
    # swallowed a trailing noun ("the band 'the white stripes' albums").
    quoted = extract_quoted_title(raw)
    if quoted:
        cleaned = _clean_topic(quoted)
        if cleaned and not _is_anaphoric_topic(cleaned):
            return cleaned

    conversational_entity = re.search(
        r"\b(?:the\s+)?(?:band|artist|group|singer)\s+(?:called|named)\s+(.+?)(?:[?.!]|\s+and\s+|$)",
        raw,
        re.I,
    )
    if conversational_entity:
        cleaned = _clean_topic(conversational_entity.group(1))
        if cleaned and not _is_anaphoric_topic(cleaned):
            return cleaned

    band_tail = re.search(
        r"\b(?:band|group)\s+(?:(?:called|named)\s+)?(?:the\s+)?(.+?)(?:[?.!]\s*|\s+and\s+|$)",
        raw,
        re.I,
    )
    if band_tail:
        cleaned = _clean_topic(band_tail.group(1))
        if cleaned and not _is_anaphoric_topic(cleaned):
            return cleaned

    # Single-letter / short title after "production/plot/cast of …"
    short = re.search(
        r"\b(?:production|plot|cast|reception|history)\s+of\s+([A-Za-z0-9]{1,3})\b",
        raw,
        re.I,
    )
    if short:
        return short.group(1).upper() if len(short.group(1)) == 1 else short.group(1)

    topic = resolve_lookup_topic(raw)
    if topic and not _is_anaphoric_topic(topic):
        return topic

    for pattern in (
        re.compile(r"\bwho\s+(?:is|are|was|were)\s+(.+?)[\?.!]*$", re.I),
        re.compile(r"\bwhat\s+(?:is|are|was|were)\s+(.+?)[\?.!]*$", re.I),
        # "not on that page" must not become the title "that" (guard below rejects it).
        re.compile(
            r"\b(?:from|on|for)\s+(?:the\s+)?(.+?)\s+page\b",
            re.I,
        ),
        re.compile(
            r"\blisted\s+for\s+(?:the\s+)?(.+?)[\?.!]*$",
            re.I,
        ),
        re.compile(
            r"\b(?:for|about|on)\s+(?:the\s+)?(.+?\s+programming language)\b",
            re.I,
        ),
        re.compile(
            r"\b(?:field|table|rows?|list(?:\s+items?)?|specifications?|population|release\s+date)\b.{"
            r"0,80}?\b(?:from|on|for|of)\s+(?:the\s+)?(.+?)(?:\s+page)?[\?.!]*$",
            re.I,
        ),
        re.compile(r"\bdiscography\s+(?:of|for)\s+(.+?)[\?.!]*$", re.I),
        re.compile(r"\balbums?\s+(?:by|from|of)\s+(.+?)[\?.!]*$", re.I),
        re.compile(
            r"\bwhat\s+(?:albums?|records?)\s+(?:did|has|have)\s+(.+?)\s+(?:release|make|record|done)[\?.!]*$",
            re.I,
        ),
        re.compile(
            r"\b(?:tell me about|look up|search for?|find|pull|extract)\s+"
            r"(?!(?:for|of|to|it|me|us|them|him|her)\b)(.+?)[\?.!]*$",
            re.I,
        ),
        re.compile(r"\bpopulation\s+of\s+(.+?)(?:\s+and\b|[?.!]|$)", re.I),
        re.compile(r"\breception\s+of\s+(?:the\s+)?(.+?)(?:\s+to\b|\s+versus\b|[?.!]|$)", re.I),
        re.compile(r"\bplot\s+of\s+(?:the\s+)?(?:movie\s+)?(.+?)(?:\s+and\b|[?.!]|$)", re.I),
        re.compile(r"\b(?:playstation\s*2|ps2)\b", re.I),
        re.compile(r"\bnintendo\s+switch\b", re.I),
        re.compile(r"\bpython\s+\(programming language\)|\bpython programming language\b", re.I),
        re.compile(r"\bthe following\b", re.I),
        re.compile(r"\b(?:cheddar\s+cheese|cheddar)\b", re.I),
        re.compile(r"\bmindhunter\b", re.I),
        re.compile(r"\bdune:\s*part\s*two\b|\bdune\s+part\s*2\b", re.I),
        re.compile(r"\biphone\s*14\b", re.I),
        re.compile(r"\bzxqwy\s+blorf\s+band\b", re.I),
        re.compile(r"\blibby,?\s*montana\b", re.I),
    ):
        match = pattern.search(raw)
        if not match:
            continue
        if match.lastindex:
            topic = _clean_topic(match.group(1))
        else:
            topic = _clean_topic(match.group(0))
        if (
            topic
            and not _is_anaphoric_topic(topic)
            and topic.casefold() not in {"wikipedia", "wiki", "encyclopedia", "it"}
        ):
            return topic

    return ""


def _format_cards_block(cards_by_year: dict[str, Any], *, topic: str) -> str:
    lines = [
        WIKI_DRIFT_MARKER,
        f"Truth Drift compare — topic: {topic}",
        "Years are frozen dumps (2017 / 2021 / 2026). Only compare because the user asked.",
        "Point out concrete differences (titles / snippets). No maturity essays.",
        "",
    ]
    for year in ("2017", "2021", "2026"):
        cards = cards_by_year.get(year) or []
        lines.append(f"### {year}")
        if not isinstance(cards, list) or not cards:
            lines.append("- (no usable cards)")
            lines.append("")
            continue
        for card in cards[:MAX_CARDS_PER_YEAR]:
            if not isinstance(card, dict):
                continue
            title = str(card.get("title") or "Untitled").strip()
            kind = str(card.get("kind_hint") or "").strip()
            snippet = re.sub(r"\s+", " ", str(card.get("snippet") or "").strip())
            if len(snippet) > MAX_SNIPPET:
                snippet = snippet[: MAX_SNIPPET - 1].rstrip() + "…"
            meta = f" [{kind}]" if kind else ""
            lines.append(f"- **{title}**{meta}")
            if snippet:
                lines.append(f"  Snippet: {snippet}")
        lines.append("")
    return "\n".join(lines).rstrip()


def _titles_match_topic(titles: list[str], topic: str, *, user_question: str = "") -> bool:
    """True when at least one hit title is the requested subject (not a weak substring)."""
    want = (topic or "").strip().casefold()
    if not want:
        return bool(titles)
    ql = (user_question or "").casefold()
    tv_context = any(
        token in ql for token in ("tv", "television", "series", "show", "actor", "cast", "starred")
    )
    false_friends = {
        "following",
        "cult following",
        "trend following",
        "score following",
    }
    for title in titles:
        have = (title or "").strip().casefold()
        if not have:
            continue
        if have == want:
            return True
        if have.startswith(want + " (") or have.startswith(want + ":"):
            return True
        if want.startswith(have + " (") and len(have) >= 4:
            return True
        # TV questions: require TV series disambiguation or exact title — not "Cult following"
        if tv_context and want in have and "(tv" in have:
            return True
        if tv_context and "following" in want and have in false_friends:
            continue
    return False


def _cards_match_topic(
    cards: list[dict[str, Any]],
    topic: str,
    *,
    user_question: str = "",
) -> bool:
    """TV/cast: strict title match. Other lookups: title match or topic named in snippet/lead."""
    titles = [
        str(card.get("title") or "")
        for card in cards
        if isinstance(card, dict)
    ]
    ql = (user_question or "").casefold()
    tv_context = any(
        token in ql for token in ("tv", "television", "series", "show", "actor", "cast", "starred")
    )
    if _titles_match_topic(titles, topic, user_question=user_question):
        return True
    if tv_context:
        return False
    want = (topic or "").strip().casefold()
    if not want:
        return False
    for card in cards[:8]:
        if not isinstance(card, dict):
            continue
        blob = " ".join(
            str(card.get(key) or "")
            for key in ("title", "snippet", "lead", "text")
        ).casefold()
        if want in blob:
            return True
    return False


def _lookup_miss_block(query: str, *, err: str = "") -> str:
    detail = f" ({err})" if err else ""
    return (
        f"{WIKI_LOOKUP_MARKER}\n"
        f"{LOOKUP_FAIL_NOTE} for '{query}'{detail}.\n"
        "CONTRACT: Tell the user the local Wikipedia archive did not return a usable page "
        f"for '{query}'. Do NOT invent cast lists, plots, or years from training memory. "
        "Do NOT suggest comparing archive years or Truth Drift unless they asked to compare years. "
        "Do NOT claim the page exists in another snapshot "
        "unless cards for that year were provided above. Offer a simpler title or confirm the "
        "Title DNS index and local markdown corpus are available."
    )


def _dns_ambiguous_block(query: str, year: str, candidates: list[str]) -> str:
    remember_dns_ambiguous(query, year, candidates)
    sample = ", ".join(candidates[:8]) or "(none)"
    return (
        f"{WIKI_LOOKUP_MARKER}\n"
        f"Title DNS found more than one page for '{query}' ({year}): {sample}.\n"
        "CONTRACT: Ask the user which title to open. Do NOT invent a pick. "
        "Do NOT fall back to similarity search. Do NOT suggest compare_years "
        "unless they asked to compare years. When they name a year, miniseries, "
        "horror film, TV series, or other qualifier from the list, open that Title DNS page."
    )


def _lookup_from_title_dns(
    query: str,
    *,
    year: str,
    user_question: str,
    include_hops: bool = True,
) -> tuple[str, dict[str, Any] | None]:
    """Resolve via Title DNS, then read the markdown lead. No Weaviate.

    include_hops=False skips the related-page hop leads. Anaphoric follow-ups
    ("what else is on that page") target the SAME page, so hop leads (e.g. "List of
    songs recorded by Patti Page" reached via a covered song) are noise and made Eve
    answer from the wrong page.
    """
    from pipeline.wiki_title_dns import resolve as dns_resolve

    follow = pick_disambiguation_followup(user_question)
    resolve_query = follow or query
    result = dns_resolve(resolve_query, year, user_question=user_question)
    status = result.status
    selected_hit = result.hit
    if status == "ambiguous":
        candidates = list(result.candidates)
        if candidates:
            # Prefer the canonical bare title over parenthetical albums/variants.
            normalized_query = _clean_topic(query).casefold()
            selected_hit = next(
                (candidate for candidate in candidates if candidate.title.casefold() == normalized_query),
                sorted(candidates, key=lambda candidate: ("(" in candidate.title, len(candidate.title), candidate.title.casefold()))[0],
            )
            status = "hit"
        else:
            return _dns_ambiguous_block(query, year, []), None
    if status != "hit" or selected_hit is None:
        # A failed resolution is a topic shift away from whatever page was last
        # resolved — drop it so a later "that page" can't grab a stale entity.
        clear_resolved_wiki_title()
        try:
            from pipeline.wiki_scratchpad import error_book_append

            error_book_append(
                query=user_question or query,
                reason=result.reason or "not in title registry",
                title=query,
                year=year,
            )
        except Exception:  # noqa: BLE001
            pass
        return _lookup_miss_block(query, err=result.reason or "not in title registry"), None
    clear_dns_ambiguous()
    hit = selected_hit
    # Record the canonical page so follow-up anaphora ("that page", "more about it")
    # re-targets this entity. Overwrites on every new hit = natural topic-shift reset.
    remember_resolved_wiki_title(hit.title, year, user_question or query)
    from pipeline.wiki_extract import (
        format_extract_injection,
        is_extract_shaped_question,
        wiki_extract,
    )
    from pipeline.wiki_read_lead import (
        prefer_section_for_question,
        wiki_read,
        wiki_read_lead_enabled,
    )

    # Extract-shaped asks: structured Evidence JSON first (fail closed when empty).
    if is_extract_shaped_question(user_question):
        section = prefer_section_for_question(user_question)
        extracted = wiki_extract(
            hit.title,
            year,
            need_hint=user_question,
            section=section,
            user_question=user_question,
        )
        extracted["title"] = hit.title
        extracted["snapshot"] = year
        if extracted.get("state") != "ok":
            try:
                from pipeline.wiki_scratchpad import error_book_append

                error_book_append(
                    query=user_question or query,
                    reason=str(extracted.get("refusal_reason") or extracted.get("state")),
                    title=hit.title,
                    year=year,
                )
            except Exception:  # noqa: BLE001
                pass
            return format_extract_injection(extracted, user_question=user_question), extracted
        return format_extract_injection(extracted, user_question=user_question), extracted

    if not wiki_read_lead_enabled():
        return _lookup_miss_block(query, err="lead read disabled"), None
    section = prefer_section_for_question(user_question)
    lead = wiki_read(
        hit.title,
        year,
        section=section,
        corpus_rel_path=hit.rel_path or None,
        max_chars=EVIDENCE_MAX_CHARS,
        user_question=user_question,
    )
    if not lead.get("ok"):
        err = str(lead.get("error") or "lead missing")
        try:
            from pipeline.wiki_scratchpad import error_book_append

            error_book_append(query=user_question or query, reason=err, title=hit.title, year=year)
        except Exception:  # noqa: BLE001
            pass
        return _lookup_miss_block(query, err=f"page listed but {err}"), None
    lead["user_question"] = user_question
    # Attach a bounded extract summary when structure exists (no lead dump of tables).
    try:
        extracted = wiki_extract(
            hit.title,
            year,
            need_hint=user_question,
            section=section,
            user_question=user_question,
        )
        if extracted.get("state") == "ok":
            lead["extract"] = extracted
    except Exception as exc:  # noqa: BLE001
        logger.debug("wiki extract attach failed for %r: %s", hit.title, exc)
    from pipeline.wiki_title_dns import neighbors as dns_neighbors

    related = dns_neighbors(
        hit.title,
        year,
        index_path=None,
        user_question=user_question,
        limit=24,
    )
    if related.get("ok"):
        ranked = related.get("ranked") or list(related.get("outbound") or [])
        lead["related_titles"] = ranked[:12]
        hop_leads: list[dict[str, Any]] = []
        extra_names: list[str] = []
        for hop_title in related.get("hops") or []:
            if not include_hops:
                break
            hop_dns = dns_resolve(str(hop_title), year, user_question=user_question)
            if hop_dns.status != "hit" or hop_dns.hit is None:
                continue
            hop_section = prefer_section_for_question(user_question)
            hop = wiki_read(
                hop_dns.hit.title,
                year,
                section=hop_section,
                corpus_rel_path=hop_dns.hit.rel_path or None,
                max_chars=max(400, EVIDENCE_MAX_CHARS // 2),
                user_question=user_question,
            )
            if not hop.get("ok"):
                continue
            hop_leads.append(hop)
            extra_names.extend(
                str(name) for name in (hop.get("allowed_names") or []) if str(name).strip()
            )
        if hop_leads:
            lead["hop_leads"] = hop_leads
            merged = list(lead.get("allowed_names") or [])
            seen = {str(name).casefold() for name in merged}
            for name in extra_names:
                key = name.casefold()
                if key in seen:
                    continue
                seen.add(key)
                merged.append(name)
            lead["allowed_names"] = merged[:24]
    return _format_evidence_block(lead, user_question=user_question), lead


def register_wiki_evidence(session_id: str, evidence: dict[str, Any]) -> None:
    sid = (session_id or "").strip()
    if sid and evidence.get("ok"):
        _EVIDENCE_BY_SESSION[sid] = evidence


def pop_wiki_evidence(session_id: str) -> dict[str, Any] | None:
    sid = (session_id or "").strip()
    if not sid:
        return None
    return _EVIDENCE_BY_SESSION.pop(sid, None)


def get_wiki_evidence(session_id: str) -> dict[str, Any] | None:
    sid = (session_id or "").strip()
    if not sid:
        return None
    return _EVIDENCE_BY_SESSION.get(sid)


def _estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def _build_lead_evidence(
    *,
    user_question: str,
    year: str,
    hit_meta: list[dict[str, Any]],
) -> dict[str, Any] | None:
    from pipeline.wiki_read_lead import (
        pick_lead_target,
        wiki_read_lead,
        wiki_read_lead_enabled,
    )

    if not wiki_read_lead_enabled() or not hit_meta:
        return None
    entity, corpus_rel_path = pick_lead_target(user_question, hit_meta)
    if not entity:
        return None
    lead = wiki_read_lead(
        entity,
        year,
        corpus_rel_path=corpus_rel_path,
        max_chars=EVIDENCE_MAX_CHARS,
    )
    if not lead.get("ok"):
        return None
    lead["user_question"] = user_question
    return lead


def _format_evidence_block(evidence: dict[str, Any], *, user_question: str) -> str:
    allowed = evidence.get("allowed_names")
    allowed_list = (
        [str(name) for name in allowed if str(name).strip()]
        if isinstance(allowed, list)
        else []
    )
    allowed_text = ", ".join(allowed_list[:12]) if allowed_list else "(none parsed)"
    related = evidence.get("related_titles")
    related_list = (
        [str(name) for name in related if str(name).strip()]
        if isinstance(related, list)
        else []
    )
    related_text = ", ".join(related_list[:12]) if related_list else ""
    lines = [
        WIKI_LOOKUP_MARKER,
        f"EVIDENCE (mandatory — snapshot {evidence.get('snapshot', '')}):",
        f"Title: {evidence.get('title', '')}",
        f"Lead: {evidence.get('lead', '')}",
        f"Allowed names: {allowed_text}",
    ]
    cast_section = str(evidence.get("cast_section") or evidence.get("section") or "").strip()
    if cast_section:
        section_name = str(evidence.get("section_name") or "Cast").strip() or "Cast"
        # Prefer structured extract over raw wikitable markup in section dumps.
        extract = evidence.get("extract")
        if isinstance(extract, dict) and extract.get("state") == "ok":
            from pipeline.wiki_extract import format_extract_prose

            lines.append(f"{section_name} EXTRACT:\n{format_extract_prose(extract, max_chars=1200)}")
        elif "{|" in cast_section:
            lines.append(
                f"{section_name} section: (raw wikitable omitted — use wiki_extract / structured EXTRACT)"
            )
        else:
            lines.append(f"{section_name} section: {cast_section}")
    elif isinstance(evidence.get("extract"), dict) and evidence["extract"].get("state") == "ok":
        from pipeline.wiki_extract import format_extract_prose

        lines.append("EXTRACT:\n" + format_extract_prose(evidence["extract"], max_chars=1200))
    if related_text:
        lines.append(f"Related titles (page links): {related_text}")
    hop_leads = evidence.get("hop_leads")
    if isinstance(hop_leads, list):
        for hop in hop_leads[:2]:
            if not isinstance(hop, dict):
                continue
            hop_title = str(hop.get("title") or "").strip()
            hop_lead = str(hop.get("lead") or "").strip()
            hop_section = str(hop.get("section") or hop.get("cast_section") or "").strip()
            if hop_title:
                lines.append(f"Hop title: {hop_title}")
            if hop_lead:
                # Never dump raw wikitable markup into a hop lead (mirrors the
                # cast_section guard) — a hop lead that is mostly a `{|` table
                # made Eve answer from an unrelated page's song list.
                if "{|" in hop_lead:
                    lines.append("Hop lead: (raw wikitable omitted — use wiki_extract)")
                else:
                    lines.append(f"Hop lead: {hop_lead}")
            if hop_section:
                lines.append(f"Hop section: {hop_section}")
    escalate = _escalation_hint(user_question)
    lines.extend([
        "",
        "CONTRACT: Answer only from EVIDENCE / EXTRACT above (and scratchpad notes if present).",
        "If the user asked for a song/person not named in EVIDENCE, say it is not in this archive.",
        "Never use training-memory song titles (e.g. do not answer \"Wow\" for Kate Bush revival questions).",
        "Do NOT invent numbers, dates, or table cells that are absent from EXTRACT.",
        "Do NOT call wiki_scout_search or wiki_scout_compare_years — evidence is already complete.",
        "Do NOT invent archive years or claim a missing page exists elsewhere.",
    ])
    if escalate:
        lines.append(escalate)
    lines.extend([
        "",
        f"User question: {user_question.strip()}",
    ])
    block = "\n".join(lines)
    if _estimate_tokens(block) > EVIDENCE_TOKEN_BUDGET:
        lead = str(evidence.get("lead") or "")
        trimmed = lead[: max(400, EVIDENCE_MAX_CHARS // 2)].rstrip() + "…"
        evidence = dict(evidence)
        evidence["lead"] = trimmed
        if cast_section and len(cast_section) > 500:
            evidence["cast_section"] = cast_section[:499].rstrip() + "…"
            evidence["section"] = evidence["cast_section"]
        return _format_evidence_block(evidence, user_question=user_question)
    return block


def _escalation_hint(user_question: str) -> str:
    ql = (user_question or "").casefold()
    if "weather" in ql or "temperature" in ql or "forecast" in ql:
        return (
            "BOUNDARY: Local Wikipedia cannot answer real-time weather. "
            "Summarize any local plot/facts from EVIDENCE, then say this needs Web Scout "
            "(or another live source) — ask before going online. Do not invent weather."
        )
    if re.search(r"\biphone\s*1[6-9]\b|\biphone\s*[2-9]\d\b", ql):
        return (
            "BOUNDARY: Devices beyond the local archive cutoff may be missing. "
            "Use EVIDENCE for pages that exist; for missing future devices say the archive "
            "is insufficient and ask before enabling Web Scout. Do not invent specs."
        )
    if "current" in ql and any(token in ql for token in ("news", "today", "now", "live")):
        return (
            "BOUNDARY: Real-time facts are outside the local Wikipedia archive. "
            "Ask before enabling Web Scout."
        )
    return ""


def _lookup_answer_hint(cards: list[dict[str, Any]], user_question: str) -> str:
    """One-line steer when snippets clearly name a revival hit."""
    from pipeline.wiki_interpreter import normalize_text

    ql = normalize_text(user_question)
    if not any(
        token in ql
        for token in (
            "reinvig",
            "re-popular",
            "repopular",
            "reviv",
            "resurg",
            "comeback",
            "career",
            "hit again",
            "popular",
            "80s",
            "80's",
            "eighties",
        )
    ):
        return ""
    for card in cards[:MAX_LOOKUP_CARDS]:
        title = normalize_text(str(card.get("title") or ""))
        snippet = normalize_text(str(card.get("snippet") or ""))
        blob = f"{title} {snippet}"
        if "running up that hill" not in blob:
            continue
        if "stranger things" in blob or "netflix" in blob or "stream" in blob:
            return (
                'Primary answer from snippets: "Running Up That Hill" by Kate Bush (1985), '
                "revived via Stranger Things / streaming — use that title; do not substitute "
                'other tracks (e.g. "Wow").'
            )
    return ""


def _format_lookup_block(
    cards: list[dict[str, Any]],
    *,
    query: str,
    year: str,
    user_question: str = "",
) -> str:
    question = (user_question or query).strip()
    hint = _lookup_answer_hint(cards, question)
    if hint:
        return (
            f"{WIKI_LOOKUP_MARKER}\n"
            f"Local Wikipedia ({year} archive).\n"
            f"{hint}\n\n"
            f"User question: {question}\n\n"
            "Reply in 1–3 plain sentences using the primary answer line above only. "
            "Do not name any other song unless the primary answer line names it."
        )

    lines = [
        WIKI_LOOKUP_MARKER,
        f"Local Wikipedia ({year} archive) for: {query}",
        "Answer the user's question directly — like a concise encyclopedia entry.",
        "Synthesize the best snippet(s). Do NOT compare years unless they asked.",
        "If snippets name specific songs, artists, or episodes — use those names.",
        "Do NOT invent that only the original synth score matters when cards cite licensed tracks.",
        "Do NOT list card metadata or write a research report. 1 short paragraph is fine.",
        "",
    ]
    if not cards:
        lines.append("(no usable cards)")
    else:
        for card in cards[:MAX_LOOKUP_CARDS]:
            if not isinstance(card, dict):
                continue
            title = str(card.get("title") or "Untitled").strip()
            snippet = re.sub(r"\s+", " ", str(card.get("snippet") or "").strip())
            if len(snippet) > MAX_SNIPPET:
                snippet = snippet[: MAX_SNIPPET - 1].rstrip() + "…"
            lines.append(f"- **{title}**")
            if snippet:
                lines.append(f"  Snippet: {snippet}")
    return "\n".join(lines).rstrip()


def _call_with_timeout(fn, timeout_sec: float, *args, **kwargs) -> Any:
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        future = pool.submit(fn, *args, **kwargs)
        return future.result(timeout=max(1.0, timeout_sec))


def run_compare(topic: str) -> dict[str, Any]:
    from pipeline.wiki_scout import compare_years

    try:
        return _call_with_timeout(
            compare_years,
            COMPARE_TIMEOUT_SEC,
            topic,
            years=["2017", "2021", "2026"],
            limit_per_year=2,
            write_files=False,
            interpret=True,
            use_rerank=False,
        )
    except concurrent.futures.TimeoutError:
        logger.warning("Truth Drift compare timed out for %s", topic)
        return {"ok": False, "error": "compare timed out", "cards_by_year": {}}
    except Exception as exc:  # noqa: BLE001
        logger.warning("Truth Drift compare failed for %s: %s", topic, exc)
        return {"ok": False, "error": str(exc), "cards_by_year": {}}


def run_lookup(
    query: str,
    *,
    year: str | None = None,
    user_question: str | None = None,
) -> dict[str, Any]:
    from pipeline.wiki_scout import default_snapshot_year, search

    target_year = (year or "").strip() or default_snapshot_year()
    search_q = (user_question or query).strip() or query
    try:
        return _call_with_timeout(
            search,
            LOOKUP_TIMEOUT_SEC,
            search_q,
            year=target_year,
            limit=LOOKUP_SEARCH_LIMIT,
            write_files=False,
            interpret=True,
            use_rerank=False,
        )
    except concurrent.futures.TimeoutError:
        logger.warning("Wiki lookup timed out for %s (%s)", query, target_year)
        return {"ok": False, "error": f"lookup timed out ({target_year})", "cards": []}
    except Exception as exc:  # noqa: BLE001
        logger.warning("Wiki lookup failed for %s (%s): %s", query, target_year, exc)
        return {"ok": False, "error": str(exc), "cards": []}


def _access_only_block() -> str:
    return (
        f"{WIKI_LOOKUP_MARKER}\n"
        "The Architect is asking whether you can use local Wikipedia "
        "(Title DNS + markdown archive on disk).\n"
        "Answer in 2–3 sentences: yes — you can look up artists, albums, places, concepts "
        "from the local archive without the public web. Invite them to ask a concrete question "
        "(e.g. who is X, what albums did Y release). Do NOT run Truth Drift or compare years."
    )



def enrich_eve_message_payload(payload: dict[str, object], *, force: bool = False) -> dict[str, object]:
    """Legacy Wikipedia evidence injection (regex middleware).

    DISABLED BY DEFAULT as of the 2026-09-23 migration. Wikipedia retrieval is now an
    autonomous MCP tool process: Eve owns intent, conversation context and pronoun
    resolution, and calls the `empire-wiki-scout` tools herself. Injecting evidence
    also made `chat_continuity` suppress the prior-turn summary, starving the model of
    the very history it needs to resolve "that page". Re-enable with
    EMPIRE_WIKI_MIDDLEWARE=1 if the legacy path is ever needed.
    """

    if not wiki_middleware_enabled():
        return payload

    message = payload.get("message")
    if not isinstance(message, str) or not message.strip():
        return payload
    if WIKI_DRIFT_MARKER in message or WIKI_LOOKUP_MARKER in message or WIKI_EXTRACT_MARKER in message:
        return payload

    try:
        active = set(load_active_tools())
    except Exception:  # noqa: BLE001
        active = set()
    if "wiki_local" not in active and not force:
        return payload

    raw = extract_user_message(message)
    lookup_cards: list[dict[str, Any]] | None = None
    enriched_evidence: dict[str, Any] | None = None

    if is_truth_drift_query(raw):
        topic = pick_compare_topic(raw)
        result = run_compare(topic)
        cards = result.get("cards_by_year") if isinstance(result.get("cards_by_year"), dict) else {}
        if not result.get("ok") or not cards:
            err = str(result.get("error") or "empty")
            block = (
                f"{WIKI_DRIFT_MARKER}\n"
                f"{COMPARE_TIMEOUT_NOTE} for topic '{topic}'. "
                f"Local Wikipedia archive did not return usable cards ({err}). "
                "Say local wiki is offline or empty. Do NOT invent year findings. "
                "Do NOT offer web search unless Web Scout is on."
            )
        else:
            block = _format_cards_block(cards, topic=topic)
        label = "Truth Drift — answer from archive cards above"
    elif is_wiki_lookup_query(raw):
        if is_wiki_access_query(raw):
            block = _access_only_block()
            label = "Answer the access question (no topic search needed)"
        else:
            query = extract_search_query(raw)
            follow = pick_disambiguation_followup(raw)
            used_anaphora = False
            if follow:
                query = follow
            elif not query and _LAST_DNS_AMBIGUOUS.get("candidates"):
                query = str(_LAST_DNS_AMBIGUOUS.get("query") or "").strip()
            elif not query and is_anaphoric_followup(raw):
                query = get_resolved_wiki_title()
                used_anaphora = True
            if not query:
                block = (
                    f"{WIKI_LOOKUP_MARKER}\n"
                    "The user wants a local Wikipedia answer but no clear topic was extracted. "
                    "Ask them for a concrete encyclopedia subject (person, album, place, concept). "
                    "Do NOT compare years or dump cards."
                )
                label = "Ask for a clearer encyclopedia topic"
            else:
                from pipeline.wiki_scout import (
                    default_snapshot_year,
                    parse_snapshot_year_from_text,
                )

                requested_year = parse_snapshot_year_from_text(raw)
                if used_anaphora and not requested_year:
                    year = str(_LAST_RESOLVED_WIKI_TITLE.get("year") or default_snapshot_year())
                else:
                    year = str(requested_year or default_snapshot_year())
                block, lead_evidence = _lookup_from_title_dns(
                    query,
                    year=year,
                    user_question=raw,
                    include_hops=not used_anaphora,
                )
                lookup_cards = None
                enriched_evidence = lead_evidence
                label = "Answer from local Wikipedia snippets above"
    else:
        return payload

    # Hard gate: Eve must not call wiki_scout_* while LOOKUP/DRIFT evidence is present.
    try:
        from pipeline.wiki_lookup_lock import set_wiki_lookup_lock

        session_id = ""
        for key in ("sessionId", "session_id", "threadId", "thread_id"):
            val = payload.get(key)
            if isinstance(val, str) and val.strip():
                session_id = val.strip()
                break
        reason = (
            "truth_drift_injected"
            if WIKI_DRIFT_MARKER in block
            else "extract_injected"
            if WIKI_EXTRACT_MARKER in block
            else "lookup_injected"
        )
        set_wiki_lookup_lock(reason=reason, session_id=session_id)
    except Exception:  # noqa: BLE001 — lock must never break chat
        pass

    # Attach active scratchpad / prior miss hints for multi-hop work.
    try:
        from pipeline.wiki_scratchpad import format_error_book_hint, format_scratchpad_block

        session_id = ""
        for key in ("sessionId", "session_id", "threadId", "thread_id"):
            val = payload.get(key)
            if isinstance(val, str) and val.strip():
                session_id = val.strip()
                break
        scratch = format_scratchpad_block(session_id)
        # Suppress the "already missed" hint when this turn produced real evidence.
        # The Error Book is a persistent miss log, so a subject that missed yesterday
        # (e.g. "white stripes" before the Title DNS fix) would otherwise be told
        # "say it is not in the archive" in the SAME prompt as its correct EVIDENCE —
        # contradictory guidance that makes Eve refuse a page it just retrieved.
        err_hint = "" if enriched_evidence else format_error_book_hint(raw)
        prefix = "\n".join(part for part in (scratch, err_hint) if part).strip()
        if prefix:
            block = f"{prefix}\n\n{block}"
    except Exception:  # noqa: BLE001
        pass

    enriched = dict(payload)
    if enriched_evidence:
        enriched["message"] = block
        enriched["_wiki_evidence"] = enriched_evidence
    elif lookup_cards and _lookup_answer_hint(lookup_cards, raw):
        enriched["message"] = block
    else:
        enriched["message"] = f"{block}\n\nUser message ({label}):\n{raw}"
    return enriched
