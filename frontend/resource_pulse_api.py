"""Inject resource_pulse snapshot for capability/headroom questions (like wiki glasses)."""

from __future__ import annotations

from typing import Any

from frontend.companion_api import extract_user_message
from frontend.wiki_drift_api import is_resource_pulse_query

RESOURCE_PULSE_MARKER = "[[EMPIRE_RESOURCE_PULSE]]"


def enrich_eve_message_payload(payload: dict[str, object]) -> dict[str, object]:
    """Attach a live pulse so Eve cannot invent headroom/inventory."""
    message = payload.get("message")
    if not isinstance(message, str) or not message.strip():
        return payload
    if RESOURCE_PULSE_MARKER in message:
        return payload

    raw = extract_user_message(message)
    if not is_resource_pulse_query(raw):
        # Also catch explicit tool-name asks
        low = raw.casefold()
        if "resource_pulse" not in low and "admit_for_goal" not in low:
            return payload
        if "resource_pulse" not in low:
            return payload

    try:
        from pipeline import resource_pulse

        snap = resource_pulse.pulse()
    except Exception as exc:  # noqa: BLE001
        block = (
            f"{RESOURCE_PULSE_MARKER}\n"
            f"resource_pulse failed ({exc}). Say diagnostics are unavailable; "
            "do not invent GPU/RAM/tool inventory."
        )
        return {**payload, "message": f"{message.rstrip()}\n\n{block}"}

    summary = str(snap.get("summary") or "").strip()
    effective = snap.get("inventory", {}).get("effective_tools") if isinstance(snap.get("inventory"), dict) else []
    can_admit = snap.get("can_admit_now") or []
    lease = snap.get("gpu_lease") if isinstance(snap.get("gpu_lease"), dict) else {}
    block = (
        f"{RESOURCE_PULSE_MARKER}\n"
        f"Live pulse (authoritative — answer from this, do not invent):\n"
        f"- summary: {summary}\n"
        f"- effective_tools: {effective}\n"
        f"- gpu_lease.tenant: {lease.get('tenant')}\n"
        f"- headroom_ok: {snap.get('headroom_ok')}\n"
        f"- can_admit_now: {can_admit}\n"
        "If they ask you to search GitHub/Web/Docker, call the matching scout tool "
        "(it auto-admits). Never claim you lack internet or GitHub."
    )
    return {**payload, "message": f"{message.rstrip()}\n\n{block}"}
