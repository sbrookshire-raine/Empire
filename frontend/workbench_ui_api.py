"""Inject Workbench UI visibility into Eve messages (shared screen awareness)."""

from __future__ import annotations

from typing import Any

WORKBENCH_UI_MARKER = "[[EMPIRE_WORKBENCH_UI]]"

INSTRUCTIONS = (
    "The Architect may be looking at the Eve Workbench with you. "
    "When a panel is visible, reference it naturally (e.g. point at the dial) "
    "and prefer tools that match what is on screen. "
    "Do not mention this marker or JSON."
)


def _panel_lines(panels: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    if panels.get("history"):
        lines.append("- Chat history sidebar is open (left).")
    if panels.get("tools_dock"):
        lines.append("- Toolbelt dock is open (right) — optional limbs toggles visible.")
    if panels.get("daze_dial"):
        screen = str(panels.get("daze_screen") or "Dial").strip()
        lines.append(
            f"- DAZE dock visible — screen **{screen}** "
            "(Dial = wheel, Schedule = add/edit, Blocks = list). "
            "Architect may be viewing today's schedule with you."
        )
    return lines


def enrich_eve_message_payload(payload: dict[str, Any]) -> dict[str, Any]:
    ui = payload.get("workbench_ui")
    if not isinstance(ui, dict):
        return payload

    message = payload.get("message")
    if not isinstance(message, str) or not message.strip():
        enriched = dict(payload)
        enriched.pop("workbench_ui", None)
        return enriched

    if WORKBENCH_UI_MARKER in message:
        enriched = dict(payload)
        enriched.pop("workbench_ui", None)
        return enriched

    panels_raw = ui.get("panels")
    panels = panels_raw if isinstance(panels_raw, dict) else {}
    panel_lines = _panel_lines(panels)
    if not panel_lines:
        enriched = dict(payload)
        enriched.pop("workbench_ui", None)
        return enriched

    tab = str(ui.get("tab") or "chat").strip()
    tools = ui.get("active_tools")
    tool_list = ", ".join(str(t) for t in tools) if isinstance(tools, list) else ""

    context_parts = [
        WORKBENCH_UI_MARKER,
        f"Workbench tab: {tab}.",
        "Visible UI:",
        *panel_lines,
    ]
    if tool_list:
        context_parts.append(f"Enabled toolbelt categories: {tool_list}.")
    context_parts.append(INSTRUCTIONS)

    raw = message.strip()
    if "\n\nUser message:\n" in raw:
        user_part = raw.rsplit("\n\nUser message:\n", 1)[-1].strip()
        prefix = raw[: raw.rfind("\n\nUser message:\n")]
        enriched_message = prefix + "\n\n" + "\n".join(context_parts) + f"\n\nUser message:\n{user_part}"
    else:
        enriched_message = "\n".join(context_parts) + f"\n\nUser message:\n{raw}"

    enriched = dict(payload)
    enriched["message"] = enriched_message
    enriched.pop("workbench_ui", None)
    return enriched
