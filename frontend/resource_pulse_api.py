"""Inject resource_pulse snapshot on every Eve turn (authoritative inventory + verified hands)."""

from __future__ import annotations

import re
from typing import Any

RESOURCE_PULSE_MARKER = "[[EMPIRE_RESOURCE_PULSE]]"

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
        "playbook(area) + tool_docs(name) for how. Never claim no GitHub/internet when DORMANT scouts can ACTIVATE."
        + farm_hint
    )


def enrich_eve_message_payload(payload: dict[str, object]) -> dict[str, object]:
    """Attach live pulse so Eve always knows current tools and headroom."""
    message = payload.get("message")
    if not isinstance(message, str) or not message.strip():
        return payload
    if RESOURCE_PULSE_MARKER in message:
        return payload

    farm_query = is_resource_farm_query(message)

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

    block = _format_pulse_block(snap, farm_query=farm_query)
    return {**payload, "message": f"{message.rstrip()}\n\n{block}"}
