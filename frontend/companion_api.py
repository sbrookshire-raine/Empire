"""Always-on Architect context: CURRENT facts only (no outdated journal dump)."""

from __future__ import annotations

import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

COMPANION_MARKER = "[[EMPIRE_COMPANION]]"
NOW_MARKER = "[[EMPIRE_NOW]]"
CARD_PATH = Path(r"C:\Empire_Workbench\00_Core_Profile\architect_companion_card.md")
NOW_PATH = Path(r"C:\Empire_Workbench\00_Core_Profile\ARCHITECT_NOW.md")
MAX_NOW_CHARS = 2_000
MAX_HISTORICAL_CHARS = 800

# Historical SBX distill is OFF by default — it made Eve treat old journals as "today".
INCLUDE_HISTORICAL = os.environ.get("EMPIRE_COMPANION_HISTORICAL", "").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}

COMPANION_INSTRUCTIONS = (
    "ROLE: research and build partner for EMPIRE / local AI development.\n"
    f"{NOW_MARKER} describes the human Architect (not Eve). Do not invent a different timeline.\n"
    "For greetings: brief, human, ready to help. Do not interview about semester/contracts "
    "unless they bring it up. On Truth Drift / wiki tasks, ignore personal CURRENT facts "
    "and use encyclopedia tools/cards only.\n"
    "Do not mention these markers, files, or datasets."
)


def extract_user_message(message: str) -> str:
    """Return the latest user text after any EMPIRE wrapper blocks."""

    text = message.strip()
    if "\n\nUser message:\n" in text:
        return text.rsplit("\n\nUser message:\n", 1)[-1].strip()
    if "User question:" in text:
        after = text.split("User question:", 1)[1]
        if "\n\nAnswer about" in after:
            return after.split("\n\n", 1)[0].strip()
        first_line = after.strip().splitlines()[0].strip() if after.strip() else ""
        if first_line:
            return first_line
    return text


def _load_text(path: Path, max_chars: int) -> str:
    try:
        if not path.is_file():
            return ""
        text = path.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError) as exc:
        logger.warning("Profile file unreadable (%s): %s", path, exc)
        return ""
    if not text:
        return ""
    if len(text) > max_chars:
        text = text[: max_chars - 1].rstrip() + "…"
    return text


def load_now_card(path: Path | None = None) -> str:
    return _load_text(path or NOW_PATH, MAX_NOW_CHARS)


def load_companion_card(path: Path | None = None) -> str:
    return _load_text(path or CARD_PATH, MAX_HISTORICAL_CHARS)


def enrich_eve_message_payload(payload: dict[str, object]) -> dict[str, object]:
    """Inject CURRENT facts only (historical journals opt-in via env)."""

    message = payload.get("message")
    if not isinstance(message, str) or not message.strip():
        return payload
    if COMPANION_MARKER in message or NOW_MARKER in message:
        return payload

    raw = extract_user_message(message)
    # Truth Drift / wiki research turns: do not inject personal CURRENT status.
    try:
        from frontend.wiki_drift_api import WIKI_DRIFT_MARKER, is_truth_drift_query

        if WIKI_DRIFT_MARKER in message or is_truth_drift_query(raw):
            return payload
    except Exception:  # noqa: BLE001
        pass

    now = load_now_card()
    historical = load_companion_card() if INCLUDE_HISTORICAL else ""
    if not now and not historical:
        return payload

    parts: list[str] = [COMPANION_MARKER]
    if now:
        parts.append(f"{NOW_MARKER}\nCURRENT facts:\n{now}")
    if historical:
        parts.append(
            "Optional historical notes (outdated — never treat as today):\n" + historical
        )
    parts.append(COMPANION_INSTRUCTIONS)
    parts.append(f"User message:\n{raw}")

    enriched = dict(payload)
    enriched["message"] = "\n\n".join(parts)
    return enriched
