"""FastMCP: DAZE day blocks for EMPIRE Phase 5 time reclaim."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from frontend import daze_api

mcp = FastMCP("empire-daze")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def daze_list_day(date: str = "", phase: str = "") -> str:
    """List day_blocks for a YYYY-MM-DD date (default today). Optional phase: planned|actual."""
    return _json(daze_api.list_day(day=date or None, phase=phase or None))


@mcp.tool()
async def daze_upsert_block(
    title: str,
    start_minute: int,
    end_minute: int,
    date: str = "",
    kind: str = "focus",
    phase: str = "planned",
    notes: str = "",
    color: str = "",
    record_id: str = "",
) -> str:
    """Create or update a day block (minutes 0–1440). Overlaps are allowed but flagged as conflicts on list."""
    payload = {
        "date": date,
        "title": title,
        "start_minute": start_minute,
        "end_minute": end_minute,
        "kind": kind,
        "phase": phase,
        "notes": notes,
        "color": color,
    }
    return _json(daze_api.upsert_block(payload, record_id=record_id))


@mcp.tool()
async def daze_free_windows(
    date: str = "",
    phase: str = "planned",
    min_minutes: int = 30,
) -> str:
    """Compute free arcs in the day for coaching (exercise/meditation slots)."""
    return _json(
        daze_api.free_windows(
            day=date or None,
            phase=phase or "planned",
            min_minutes=int(min_minutes) or 30,
        )
    )


@mcp.tool()
async def daze_delete_block(record_id: str) -> str:
    """Delete a day_blocks record by id."""
    return _json(daze_api.delete_block(record_id))


if __name__ == "__main__":
    mcp.run()
