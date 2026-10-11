"""Inject resource_pulse snapshot on every Eve turn (authoritative inventory + verified hands)."""

from __future__ import annotations

import re
from typing import Any

RESOURCE_PULSE_MARKER = "[[EMPIRE_RESOURCE_PULSE]]"
_USER_MESSAGE_ANCHOR = "\n\nUser message:\n"

RESOURCE_FARM_QUERY_RE = re.compile(
    r"(?:\bresource[_\s-]?farm\b|\bprocessed\s+materials\b|\bfarm(?:ed)?\s+repos\b|\bscout\s+catalog\b|"
    r"\bresource_farm_run\b|\bdisassembly\s+catalog\b)",
    re.IGNORECASE,
)


def is_resource_farm_query(text: str) -> bool:
    return bool(RESOURCE_FARM_QUERY_RE.search((text or "").strip()))


def _format_pulse_block(snap: dict[str, Any], *, farm_query: bool) -> str:
    summary = str(snap.get("summary") or "").strip()
    effective = snap.get("inventory", {}).get("effective_tools") if isinstance(snap.get("inventory"), dict) else []
    can_admit = snap.get("can_admit_now") or []
    lease = snap.get("gpu_lease") if isinstance(snap.get("gpu_lease"), dict) else {}
    verified_line = str(snap.get("verified_hands_snippet") or "").strip()
    meter = snap.get("capacity_meter") if isinstance(snap.get("capacity_meter"), dict) else {}
    activation = snap.get("activation") if isinstance(snap.get("activation"), dict) else {}
    dormant = [
        str(x.get("id") or "")
        for x in (activation.get("limbs") or [])
        if isinstance(x, dict) and x.get("state") == "DORMANT"
    ]
    farm_hint = ""
    if farm_query:
        farm_hint = (
            "\nResource farm: call resource_farm_run (no query = catalog status; with query = GitHub scout cards). "
            "Never Cognee unless Architect asks. Heptabase only with architect_confirm in the same turn."
        )
    return (
        f"{RESOURCE_PULSE_MARKER}\n"
        f"Live pulse (authoritative every turn — use this; do not invent inventory):\n"
        f"- note: DORMANT / can_admit_now limbs are OFF until ACTIVATE (no extra RAM/VRAM for those names).\n"
        f"- summary: {summary}\n"
        f"- effective_tools: {effective}\n"
        f"- gpu_lease.tenant: {lease.get('tenant')}\n"
        f"- headroom_ok: {snap.get('headroom_ok')}\n"
        f"- can_admit_now (ACTIVATE now): {can_admit}\n"
        f"- capacity_meter: {meter.get('room_label')} status={meter.get('status')}\n"
        f"  RAM {meter.get('ram_bar')} | Disk {meter.get('disk_bar')} | VRAM {meter.get('vram_bar')} | "
        f"GPU tenant {meter.get('gpu_tenant')}\n"
        f"- activation: {activation.get('session_slots')} | ACTIVE {activation.get('active')} | "
        f"DORMANT (ready) {dormant}\n"
        f"- eve_contract: {activation.get('eve_contract')}\n"
        + (f"- verified_hands: {verified_line}\n" if verified_line else "")
        + "ACTIVATE light limbs via admit_for_goal or scout tool call; DEACTIVATE via release_capabilities. "
        "When headroom_ok and github_scout is in can_admit_now, call github_scout_search — VRAM bar does NOT block scouts. "
        "Web/GitHub analyze+catalog+board: intake_to_lego_run (skill-intake-to-lego; playbook intake-and-legos). "
        "playbook(area) + tool_docs(name) for how."
        + farm_hint
    )


def _attach_pulse_block(message: str, block: str) -> str:
    """Keep pulse in the preamble — never append after the Architect's ask."""

    text = message.rstrip()
    pulse = block.strip()
    if not pulse:
        return text
    if _USER_MESSAGE_ANCHOR in text:
        head, _, user_part = text.rpartition(_USER_MESSAGE_ANCHOR)
        return f"{head.rstrip()}\n\n{pulse}\n\nUser message:\n{user_part.strip()}"
    return f"{text}\n\n{pulse}"


def enrich_eve_message_payload(payload: dict[str, object]) -> dict[str, object]:
    """Attach live pulse so Eve always knows current tools and headroom."""
    message = payload.get("message")
    if not isinstance(message, str) or not message.strip():
        return payload
    if RESOURCE_PULSE_MARKER in message:
        return payload

    try:
        from frontend.companion_api import extract_user_message
        from frontend.wiki_drift_api import is_wiki_lookup_query

        user_line = extract_user_message(message) or message
        if is_wiki_lookup_query(user_line):
            return payload
    except Exception:  # noqa: BLE001
        pass

    farm_source = message
    if _USER_MESSAGE_ANCHOR in message:
        farm_source = message.rsplit(_USER_MESSAGE_ANCHOR, 1)[-1].strip()
    farm_query = is_resource_farm_query(farm_source)

    try:
        from pipeline import resource_pulse

        snap = resource_pulse.pulse()
    except Exception as exc:  # noqa: BLE001
        block = (
            f"{RESOURCE_PULSE_MARKER}\n"
            f"resource_pulse failed ({exc}). Say diagnostics are unavailable; "
            "do not invent GPU/RAM/tool inventory."
        )
        return {**payload, "message": _attach_pulse_block(message, block)}

    block = _format_pulse_block(snap, farm_query=farm_query)
    return {**payload, "message": _attach_pulse_block(message, block)}
