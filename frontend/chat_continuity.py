"""Rolling chat continuity — short summary injected into Eve messages.

Keeps num_ctx 8192 safe: never dumps full transcripts into KV.
"""

from __future__ import annotations

import re
from typing import Any

from frontend import chat_history

SUMMARY_MARKER = "[[EMPIRE_CHAT_SUMMARY]]"
MAX_SUMMARY_CHARS = 1_200
MAX_TURNS_FOR_LOCAL_SUMMARY = 12


def _plain(messages: list[dict[str, Any]]) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for item in messages:
        role = chat_history.plain_role(item.get("role"))
        if role not in {"user", "assistant"}:
            continue
        text = str(item.get("text") or "").strip()
        if not text:
            continue
        # Strip prior summary wrappers from stored assistant/user text
        if SUMMARY_MARKER in text:
            text = text.split(SUMMARY_MARKER, 1)[-1].strip()
            # After marker the real user line may still be prefixed
            if "\n\nUser message:\n" in text:
                text = text.split("\n\nUser message:\n", 1)[-1].strip()
        out.append((role, text))
    return out


def build_rolling_summary(messages: list[dict[str, Any]] | None) -> str:
    """Deterministic short digest from recent user/assistant turns (no LLM)."""

    turns = _plain(messages or [])
    if len(turns) < 2:
        return ""
    recent = turns[-MAX_TURNS_FOR_LOCAL_SUMMARY :]
    lines: list[str] = []
    for role, text in recent:
        compact = re.sub(r"\s+", " ", text).strip()
        if len(compact) > 160:
            compact = compact[:159] + "…"
        label = "User" if role == "user" else "Eve"
        lines.append(f"- {label}: {compact}")
    summary = "Prior conversation (rolling):\n" + "\n".join(lines)
    if len(summary) > MAX_SUMMARY_CHARS:
        summary = summary[: MAX_SUMMARY_CHARS - 1] + "…"
    return summary


def update_chat_summary(chat_id: str | None, messages: list[dict[str, Any]] | None) -> str:
    """Persist rolling_summary on the chat JSON when possible."""

    if not chat_id or not isinstance(chat_id, str):
        return ""
    summary = build_rolling_summary(messages)
    if not summary:
        return ""
    try:
        cleaned = chat_history.validate_chat_id(chat_id.strip())
        existing = chat_history.get_chat(cleaned)
    except chat_history.ChatHistoryError:
        return summary
    try:
        payload = dict(existing)
        payload["rollingSummary"] = summary
        payload["messages"] = existing.get("messages") or []
        chat_history.upsert_chat(cleaned, payload)
    except chat_history.ChatHistoryError:
        pass
    return summary


def enrich_eve_message_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Prepend rolling summary for the active (or named) chat."""

    message = payload.get("message")
    if not isinstance(message, str) or not message.strip():
        return payload
    if SUMMARY_MARKER in message:
        return payload

    chat_id = payload.get("chat_id") or payload.get("chatId")
    summary = ""
    if isinstance(chat_id, str) and chat_id.strip():
        try:
            chat = chat_history.get_chat(chat_id.strip())
            summary = str(chat.get("rollingSummary") or "").strip()
            if not summary:
                summary = build_rolling_summary(chat.get("messages") or [])
        except chat_history.ChatHistoryError:
            summary = ""

    if not summary:
        # Fall back to active chat pointer
        active = chat_history.get_active_chat_id()
        if active:
            try:
                chat = chat_history.get_chat(active)
                summary = str(chat.get("rollingSummary") or "").strip()
                if not summary:
                    summary = build_rolling_summary(chat.get("messages") or [])
            except chat_history.ChatHistoryError:
                summary = ""

    if not summary:
        return payload

    enriched = dict(payload)
    enriched["message"] = (
        f"{SUMMARY_MARKER}\n{summary}\n\n"
        "Prior turns are BACKGROUND only. The User message below is the ONLY task "
        "for this turn — answer THAT question. If the topic changed, ignore the old "
        "topic completely. Call tools for the new question. Do not mention this digest.\n\n"
        f"User message:\n{message.strip()}"
    )
    # Strip chat_id so Eve upstream does not see unknown fields
    enriched.pop("chat_id", None)
    enriched.pop("chatId", None)
    return enriched
