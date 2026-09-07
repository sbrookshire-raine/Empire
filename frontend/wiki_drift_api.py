"""Server-side Truth Drift glasses: inject wiki cards before Eve speaks.

Fast models often skip tools and invent year essays. This runs compare_years
locally and puts compact cards in the message so Eve must answer from archives.
"""

from __future__ import annotations

import logging
import re
from typing import Any

from frontend.companion_api import extract_user_message
from frontend.eve_toolbelt import load_active_tools, write_active_tools

logger = logging.getLogger(__name__)

WIKI_DRIFT_MARKER = "[[EMPIRE_WIKI_DRIFT]]"
MAX_SNIPPET = 280
MAX_CARDS_PER_YEAR = 3
COMPARE_TIMEOUT_NOTE = "Wiki compare failed or timed out"

TRUTH_DRIFT_RE = re.compile(
    r"\b(?:"
    r"truth\s*drift|compare\s+years?|across\s+years?|"
    r"between\s+20\d{2}\s+and\s+20\d{2}|"
    r"changed\s+between\s+20\d{2}|from\s+20\d{2}\s+to\s+20\d{2}|"
    r"2017|2021|2026"
    r")\b",
    re.IGNORECASE,
)

TOPIC_RULES: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"post[-\s]?truth", re.I), "post-truth"),
    (re.compile(r"\bepistemolog", re.I), "epistemology"),
    (re.compile(r"\bmisinformation\b", re.I), "misinformation"),
    (re.compile(r"\bdisinformation\b", re.I), "disinformation"),
    (re.compile(r"\bhallucin", re.I), "hallucination (artificial intelligence)"),
    (re.compile(r"\bgenerative\s+AI\b|\blarge\s+language\s+model|\bLLM\b", re.I), "generative artificial intelligence"),
    # "truth" + AI/models → post-truth is the archive term that actually drifts
    (re.compile(r"\btruth\b.*\b(?:AI|A\.I\.|models?)\b|\b(?:AI|A\.I\.|models?)\b.*\btruth\b", re.I), "post-truth"),
    (re.compile(r"\bartificial\s+intelligence\b|\bAI models?\b", re.I), "artificial intelligence"),
    (re.compile(r"\btruth\b", re.I), "truth"),
)


def is_truth_drift_query(text: str) -> bool:
    return bool(TRUTH_DRIFT_RE.search((text or "").strip()))


def pick_compare_topic(text: str) -> str:
    cleaned = (text or "").strip()
    for pattern, topic in TOPIC_RULES:
        if pattern.search(cleaned):
            return topic
    return "post-truth"


def _format_cards_block(cards_by_year: dict[str, Any], *, topic: str) -> str:
    lines = [
        f"{WIKI_DRIFT_MARKER}",
        f"Local Wikipedia archive cards for topic: {topic}",
        "Years are frozen dumps (2017 / 2021 / 2026), not hypothetical futures.",
        "Answer ONLY from these cards. Point out concrete differences (titles / snippets).",
        "Do not invent maturity essays. Do not mention this marker or Cognee.",
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
            why = str(card.get("rank_why") or "").strip()
            snippet = re.sub(r"\s+", " ", str(card.get("snippet") or "").strip())
            if len(snippet) > MAX_SNIPPET:
                snippet = snippet[: MAX_SNIPPET - 1].rstrip() + "…"
            meta = f" [{kind}]" if kind else ""
            lines.append(f"- **{title}**{meta}" + (f" — {why}" if why else ""))
            if snippet:
                lines.append(f"  Snippet: {snippet}")
        lines.append("")
    return "\n".join(lines).rstrip()


def run_compare(topic: str) -> dict[str, Any]:
    from pipeline.wiki_scout import compare_years

    try:
        return compare_years(
            topic,
            years=["2017", "2021", "2026"],
            limit_per_year=MAX_CARDS_PER_YEAR,
            write_files=True,
            interpret=True,
        )
    except Exception as exc:  # noqa: BLE001
        logger.warning("Truth Drift compare failed for %s: %s", topic, exc)
        return {"ok": False, "error": str(exc), "cards_by_year": {}}


def enrich_eve_message_payload(payload: dict[str, object]) -> dict[str, object]:
    """Inject Truth Drift cards so Fast mode cannot skip the glasses."""

    message = payload.get("message")
    if not isinstance(message, str) or not message.strip():
        return payload
    if WIKI_DRIFT_MARKER in message:
        return payload

    raw = extract_user_message(message)
    if not is_truth_drift_query(raw):
        return payload

    # Ensure Wiki Local limb stays on for any follow-up tool use.
    try:
        from frontend.eve_toolbelt import load_active_tools

        merged = sorted(set(load_active_tools()) | {"wiki_local"})
        write_active_tools(merged)
    except Exception:  # noqa: BLE001
        try:
            write_active_tools(["wiki_local"])
        except Exception:  # noqa: BLE001
            pass

    topic = pick_compare_topic(raw)
    result = run_compare(topic)
    cards = result.get("cards_by_year") if isinstance(result.get("cards_by_year"), dict) else {}
    if not result.get("ok") or not cards:
        block = (
            f"{WIKI_DRIFT_MARKER}\n"
            f"{COMPARE_TIMEOUT_NOTE} for topic '{topic}'. "
            f"Tell the Architect the local wiki index did not return usable cards "
            f"({result.get('error') or 'empty'}). Do not invent year findings."
        )
    else:
        block = _format_cards_block(cards, topic=topic)

    # Drop prior companion wrappers — research turn should not carry life-status NOW.
    enriched = dict(payload)
    enriched["message"] = (
        f"{block}\n\n"
        "User message (Truth Drift — answer from archive cards above):\n"
        f"{raw}"
    )
    return enriched
