"""FastMCP: Heptabase CLI + Disassembly catalog (host desktop app required)."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import disassembly_card, disassembly_publish, heptabase_cli
from pipeline.heptabase_config import catalog_whiteboard_id

mcp = FastMCP("empire-heptabase")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def heptabase_health() -> str:
    """Check Heptabase CLI and desktop app reachability."""
    return _json(heptabase_cli.health_check())


@mcp.tool()
async def heptabase_search(query: str = "", limit: int = 20) -> str:
    """Search Heptabase cards by keyword (read-only)."""
    return _json(heptabase_cli.search_cards(query, limit=limit))


@mcp.tool()
async def heptabase_read_note(card_id: str) -> str:
    """Read one Heptabase note card by id."""
    return _json(heptabase_cli.read_note(card_id))


@mcp.tool()
async def heptabase_whiteboard_structure(whiteboard_id: str = "") -> str:
    """Read catalog whiteboard structure (default: configured disassembly board)."""
    wid = (whiteboard_id or catalog_whiteboard_id() or "").strip()
    if not wid:
        return _json({"ok": False, "error": "whiteboard_id required or set HEPTABASE_DISASSEMBLY_WHITEBOARD_ID"})
    structure = heptabase_cli.whiteboard_read_structure(wid)
    layout = heptabase_cli.whiteboard_read_layout(wid)
    return _json({"ok": True, "whiteboard_id": wid, "structure": structure, "layout": layout})


@mcp.tool()
async def disassembly_card_write(payload_json: str) -> str:
    """Write a local Disassembly Card (JSON string matching DisassemblyCard.v1)."""
    try:
        data = json.loads(payload_json)
    except json.JSONDecodeError as exc:
        return _json({"ok": False, "error": f"invalid JSON: {exc}"})
    if not isinstance(data, dict):
        return _json({"ok": False, "error": "payload must be a JSON object"})
    try:
        return _json(disassembly_card.write_card(data))
    except ValueError as exc:
        return _json({"ok": False, "error": str(exc)})


@mcp.tool()
async def disassembly_card_list(limit: int = 30) -> str:
    """List recent local Disassembly Cards."""
    return _json({"ok": True, "cards": disassembly_card.list_cards(limit=limit)})


@mcp.tool()
async def disassembly_publish_heptabase(
    card_id: str,
    architect_confirm: bool = False,
) -> str:
    """Publish a local card to the Heptabase catalog board (requires architect_confirm=true)."""
    return _json(
        disassembly_publish.publish_to_heptabase(
            card_id,
            architect_confirm=architect_confirm,
        )
    )


@mcp.tool()
async def disassembly_mark_mature(
    card_id: str,
    architect_confirm: bool = False,
) -> str:
    """Recolor a published card green on Heptabase (requires architect_confirm=true)."""
    return _json(
        disassembly_publish.mark_mature(
            card_id,
            architect_confirm=architect_confirm,
        )
    )


if __name__ == "__main__":
    mcp.run()
