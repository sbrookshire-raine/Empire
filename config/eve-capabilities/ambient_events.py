"""Shared parsing and trigger rules for EMPIRE ambient workers."""

from __future__ import annotations

import json
import re
from typing import Any

MEMORY_PHRASES = (
    "that worked",
    "perfect",
    "finally",
    "this is exactly it",
    "keep this",
    "looks good",
    "resolved",
    "nailed it",
)
MEMORY_PATTERN = re.compile(
    r"(?<!\w)(?:" + "|".join(re.escape(phrase) for phrase in MEMORY_PHRASES) + r")(?!\w)",
    re.IGNORECASE,
)


def parse_event(line: str) -> dict[str, Any] | None:
    try:
        event = json.loads(line)
    except (TypeError, json.JSONDecodeError):
        return None
    if not isinstance(event, dict):
        return None
    return event


def event_text(event: dict[str, Any]) -> str:
    value = event.get("text")
    return value.strip() if isinstance(value, str) else ""


def is_completed_user_event(event: dict[str, Any]) -> bool:
    return event.get("role") == "user" and event.get("status", "completed") == "completed"


def memory_triggered(event: dict[str, Any]) -> bool:
    return is_completed_user_event(event) and bool(MEMORY_PATTERN.search(event_text(event)))


def research_triggered(event: dict[str, Any], minimum_chars: int = 16) -> bool:
    if not is_completed_user_event(event):
        return False
    text = event_text(event)
    if len(text) < minimum_chars:
        return False
    return bool(re.search(r"\b(?:research|papers?|simulation|causal|forecast|algorithm|theory|architecture)\b", text, re.I))