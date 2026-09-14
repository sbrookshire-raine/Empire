"""Server-side Wikipedia glasses: inject archive text before Eve speaks.

Lookup uses Title DNS (SQLite) then reads the markdown lead from D:\\wiki_md.
Weaviate hybrid search is only for explicit Truth Drift / compare_years.
"""

from __future__ import annotations

import concurrent.futures
import logging
import re
from typing import Any

from frontend.companion_api import extract_user_message
from frontend.eve_toolbelt import load_active_tools

logger = logging.getLogger(__name__)

WIKI_DRIFT_MARKER = "[[EMPIRE_WIKI_DRIFT]]"
WIKI_LOOKUP_MARKER = "[[EMPIRE_WIKI_LOOKUP]]"
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

_DISAMBIG_FOLLOWUP_RE = re.compile(
    r"(?:"
    r"\b(?:i'?m\s+interested|interested\s+in|i\s+mean|mean(?:ing)?|the\s+one|"
    r"go\s+with|pick|choose|open)\b|"
    r"\b(?:19|20)\d{2}\b|"
    r"\bminiseries\b|"
    r"\btv\s+series\b|"
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

WIKI_LOOKUP_RE = re.compile(
    r"\b(?:"
    r"who\s+(?:is|are|was|were)\b|"
    r"what\s+(?:is|are|was|were)\b|"
    r"what\b.{0,48}\b(?:albums?|songs?|records?|actors?|cast)\b|"
    r"what\b.{0,48}\b(?:80s|80's|eighties|1980s?)\b|"
    r"(?:who|which)\b.{0,40}\b(?:acted|starred|played|appeared)\b|"
    r"\b(?:actors?|cast|stars?)\b.{0,48}\b(?:in|of|on|from)\b|"
    r"\b(?:tv\s+show|television\s+show|tv\s+series|series)\b|"
    r"(?:tell me|look up|find)\s+(?:about\s+)?|"
    r"discography\b|"
    r"\balbums?\s+(?:by|from|of)\b|"
    r"(?:use|search|query)\s+(?:my\s+)?(?:local\s+)?(?:wikipedia|wiki|encyclopedia)\b|"
    r"(?:local\s+)?(?:wikipedia|encyclopedia)\s+(?:say|says|about)\b|"
    r"stranger things\b"
    r")\b",
    re.IGNORECASE,
)

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


def is_wiki_lookup_query(text: str) -> bool:
    raw = (text or "").strip()
    if not raw or is_truth_drift_query(raw):
        return False
    if is_wiki_access_query(raw):
        return True
    if bool(WIKI_LOOKUP_RE.search(raw)):
        return True
    # Clarification after Title DNS asked which page to open.
    if _LAST_DNS_AMBIGUOUS.get("candidates") and _DISAMBIG_FOLLOWUP_RE.search(raw):
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
        if len(year_hits) == 1:
            return year_hits[0]
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
    topic = re.split(r"\s+(?:and|or|using|from|with|that|who|which)\s+", topic, maxsplit=1)[0]
    return topic[:120].strip()


def extract_search_query(text: str) -> str:
    """Pull an encyclopedia title/subject from a conversational question."""
    from pipeline.wiki_interpreter import extract_quoted_title, resolve_lookup_topic

    raw = (text or "").strip()
    if not raw or is_wiki_access_query(raw):
        return ""

    # Quoted titles first — contractions like I'm must not become the subject.
    quoted = extract_quoted_title(raw)
    if quoted:
        return _clean_topic(quoted)

    topic = resolve_lookup_topic(raw)
    if topic:
        return topic

    for pattern in (
        re.compile(r"\bwho\s+(?:is|are|was|were)\s+(.+?)[\?.!]*$", re.I),
        re.compile(r"\bwhat\s+(?:is|are|was|were)\s+(.+?)[\?.!]*$", re.I),
        re.compile(r"\bdiscography\s+(?:of|for)\s+(.+?)[\?.!]*$", re.I),
        re.compile(r"\balbums?\s+(?:by|from|of)\s+(.+?)[\?.!]*$", re.I),
        re.compile(
            r"\bwhat\s+(?:albums?|records?)\s+(?:did|has|have)\s+(.+?)\s+(?:release|make|record|done)[\?.!]*$",
            re.I,
        ),
        re.compile(r"\b(?:tell me about|look up|search for?|find)\s+(.+?)[\?.!]*$", re.I),
    ):
        match = pattern.search(raw)
        if match:
            topic = _clean_topic(match.group(1))
            if topic and topic.casefold() not in {"wikipedia", "wiki", "encyclopedia", "it"}:
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
        "Do NOT suggest Weaviate, Docker port 8091, wiki_scout_compare_years, or Truth Drift "
        "unless they asked to compare years. Do NOT claim the page exists in another snapshot "
        "unless cards for that year were provided above. Offer a simpler title or confirm the "
        "Title DNS index and `D:\\wiki_md` are available (`scripts/build-wiki-title-index.ps1`)."
    )


def _dns_ambiguous_block(query: str, year: str, candidates: list[str]) -> str:
    remember_dns_ambiguous(query, year, candidates)
    sample = ", ".join(candidates[:8]) or "(none)"
    return (
        f"{WIKI_LOOKUP_MARKER}\n"
        f"Title DNS found more than one page for '{query}' ({year}): {sample}.\n"
        "CONTRACT: Ask the user which title to open. Do NOT invent a pick. "
        "Do NOT fall back to Weaviate similarity. Do NOT suggest compare_years "
        "unless they asked to compare years. When they name a year, miniseries, "
        "or TV series from the list, open that Title DNS page — stay on Title DNS."
    )


def _lookup_from_title_dns(
    query: str,
    *,
    year: str,
    user_question: str,
) -> tuple[str, dict[str, Any] | None]:
    """Resolve via Title DNS, then read the markdown lead. No Weaviate."""
    from pipeline.wiki_title_dns import resolve as dns_resolve

    follow = pick_disambiguation_followup(user_question)
    resolve_query = follow or query
    result = dns_resolve(resolve_query, year, user_question=user_question)
    status = result.status
    if status == "ambiguous":
        titles = [c.title for c in result.candidates]
        return _dns_ambiguous_block(query, year, titles), None
    if status != "hit" or result.hit is None:
        return _lookup_miss_block(query, err=result.reason or "not in title registry"), None
    clear_dns_ambiguous()
    hit = result.hit
    from pipeline.wiki_read_lead import wiki_read_lead, wiki_read_lead_enabled

    if not wiki_read_lead_enabled():
        return _lookup_miss_block(query, err="lead read disabled"), None
    lead = wiki_read_lead(
        hit.title,
        year,
        corpus_rel_path=hit.rel_path or None,
        max_chars=EVIDENCE_MAX_CHARS,
    )
    if not lead.get("ok"):
        err = str(lead.get("error") or "lead missing")
        return _lookup_miss_block(query, err=f"page listed but {err}"), None
    lead["user_question"] = user_question
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
            hop_dns = dns_resolve(str(hop_title), year, user_question=user_question)
            if hop_dns.status != "hit" or hop_dns.hit is None:
                continue
            hop = wiki_read_lead(
                hop_dns.hit.title,
                year,
                corpus_rel_path=hop_dns.hit.rel_path or None,
                max_chars=max(400, EVIDENCE_MAX_CHARS // 2),
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
    if related_text:
        lines.append(f"Related titles (page links): {related_text}")
    hop_leads = evidence.get("hop_leads")
    if isinstance(hop_leads, list):
        for hop in hop_leads[:2]:
            if not isinstance(hop, dict):
                continue
            hop_title = str(hop.get("title") or "").strip()
            hop_lead = str(hop.get("lead") or "").strip()
            if hop_title:
                lines.append(f"Hop title: {hop_title}")
            if hop_lead:
                lines.append(f"Hop lead: {hop_lead}")
    lines.extend([
        "",
        "CONTRACT: Answer only from EVIDENCE above.",
        "If the user asked for a song/person not named in EVIDENCE, say it is not in this archive.",
        "Never use training-memory song titles (e.g. do not answer \"Wow\" for Kate Bush revival questions).",
        "",
        f"User question: {user_question.strip()}",
    ])
    block = "\n".join(lines)
    if _estimate_tokens(block) > EVIDENCE_TOKEN_BUDGET:
        lead = str(evidence.get("lead") or "")
        trimmed = lead[: max(400, EVIDENCE_MAX_CHARS // 2)].rstrip() + "…"
        evidence = dict(evidence)
        evidence["lead"] = trimmed
        return _format_evidence_block(evidence, user_question=user_question)
    return block


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
        "The Architect is asking whether you can use local Wikipedia (offline Weaviate: "
        "2017 / 2021 / 2026 snapshots).\n"
        "Answer in 2–3 sentences: yes — you can look up artists, albums, places, concepts "
        "from the local archive without the public web. Invite them to ask a concrete question "
        "(e.g. who is X, what albums did Y release). Do NOT run Truth Drift or compare years."
    )


def enrich_eve_message_payload(payload: dict[str, object]) -> dict[str, object]:
    """Inject Wikipedia cards so Fast mode cannot skip the archive."""

    message = payload.get("message")
    if not isinstance(message, str) or not message.strip():
        return payload
    if WIKI_DRIFT_MARKER in message or WIKI_LOOKUP_MARKER in message:
        return payload

    try:
        active = set(load_active_tools())
    except Exception:  # noqa: BLE001
        active = set()
    if "wiki_local" not in active:
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
                f"Local Wikipedia/Weaviate did not return usable cards ({err}). "
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
            if follow:
                query = follow
            elif not query and _LAST_DNS_AMBIGUOUS.get("candidates"):
                query = str(_LAST_DNS_AMBIGUOUS.get("query") or "").strip()
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
                year = str(requested_year or default_snapshot_year())
                block, lead_evidence = _lookup_from_title_dns(
                    query,
                    year=year,
                    user_question=raw,
                )
                lookup_cards = None
                enriched_evidence = lead_evidence
                label = "Answer from local Wikipedia snippets above"
    else:
        return payload

    enriched = dict(payload)
    if enriched_evidence:
        enriched["message"] = block
        enriched["_wiki_evidence"] = enriched_evidence
    elif lookup_cards and _lookup_answer_hint(lookup_cards, raw):
        enriched["message"] = block
    else:
        enriched["message"] = f"{block}\n\nUser message ({label}):\n{raw}"
    return enriched
