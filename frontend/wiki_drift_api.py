"""Server-side Wikipedia glasses: inject archive cards before Eve speaks.

Fast models often skip tools. This module pre-fetches local Weaviate hits so Eve
answers from real archive snippets — not invented essays.

Two modes:
- **Lookup** (default): one-year search for who/what/albums-style questions.
- **Truth Drift** (opt-in): compare_years only when the user explicitly asks.
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
    r"what\b.{0,48}\b(?:albums?|songs?|records?)\b|"
    r"what\b.{0,48}\b(?:80s|80's|eighties|1980s?)\b|"
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
    (re.compile(r"\bartificial\s+intelligence\b|\bAI models?\b", re.I), "artificial intelligence"),
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
    return bool(WIKI_LOOKUP_RE.search(raw))


def is_wiki_enriched_query(text: str) -> bool:
    """Any server-side wiki injection (lookup or Truth Drift)."""
    raw = (text or "").strip()
    return is_truth_drift_query(raw) or is_wiki_lookup_query(raw)


def pick_compare_topic(text: str) -> str:
    cleaned = (text or "").strip()
    for pattern, topic in TOPIC_RULES:
        if pattern.search(cleaned):
            return topic
    extracted = extract_search_query(cleaned)
    return extracted or "truth"


def _clean_topic(value: str) -> str:
    topic = re.sub(r"\s+", " ", (value or "").strip(" .?!,\"'"))
    if not topic:
        return ""
    topic = re.split(r"\s+(?:and|or|using|from|with|that|who|which)\s+", topic, maxsplit=1)[0]
    return topic[:120].strip()


def extract_search_query(text: str) -> str:
    """Pull an encyclopedia title/subject from a conversational question."""
    from pipeline.wiki_interpreter import resolve_lookup_topic

    raw = (text or "").strip()
    if not raw or is_wiki_access_query(raw):
        return ""

    topic = resolve_lookup_topic(raw)
    if topic:
        return topic

    quoted = re.search(r'"([^"]{2,120})"|\'([^\']{2,120})\'', raw)
    if quoted:
        return _clean_topic(quoted.group(1) or quoted.group(2) or "")

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
    lines = [
        WIKI_LOOKUP_MARKER,
        f"EVIDENCE (mandatory — snapshot {evidence.get('snapshot', '')}):",
        f"Title: {evidence.get('title', '')}",
        f"Lead: {evidence.get('lead', '')}",
        f"Allowed names: {allowed_text}",
        "",
        "CONTRACT: Answer only from EVIDENCE above.",
        "If the user asked for a song/person not named in EVIDENCE, say it is not in this archive.",
        "Never use training-memory song titles (e.g. do not answer \"Wow\" for Kate Bush revival questions).",
        "",
        f"User question: {user_question.strip()}",
    ]
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
                result = run_lookup(query, year=requested_year, user_question=raw)
                cards = result.get("cards") if isinstance(result.get("cards"), list) else []
                year = str(result.get("snapshot_year") or requested_year or default_snapshot_year())
                if not result.get("ok") or not cards:
                    err = str(result.get("error") or LOOKUP_FAIL_NOTE)
                    block = (
                        f"{WIKI_LOOKUP_MARKER}\n"
                        f"{LOOKUP_FAIL_NOTE} for '{query}' ({err}). "
                        "Say local Wikipedia did not return a hit — suggest a simpler title or "
                        "check Weaviate (`scripts/start-weaviate.ps1`). Do NOT invent facts."
                    )
                else:
                    lookup_cards = cards
                    hit_meta = (
                        result.get("hit_meta")
                        if isinstance(result.get("hit_meta"), list)
                        else []
                    )
                    lead_evidence = _build_lead_evidence(
                        user_question=raw,
                        year=year,
                        hit_meta=hit_meta,
                    )
                    if lead_evidence:
                        block = _format_evidence_block(lead_evidence, user_question=raw)
                        enriched_evidence = lead_evidence
                    else:
                        enriched_evidence = None
                        block = _format_lookup_block(
                            cards,
                            query=query,
                            year=year,
                            user_question=raw,
                        )
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
