"""FastMCP: Container Scout — Docker Hub + local empire-* status (no auto-Cognee)."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import container_scout

mcp = FastMCP("empire-container-scout")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def container_scout_search(query: str, limit: int = 10, note: str = "") -> str:
    """Search Docker Hub by keyword. Caches markdown under container_cache. Never pulls images or writes Cognee."""
    return _json(container_scout.search_hub(query, limit=limit, note=note))


@mcp.tool()
async def container_scout_detail(repo: str, tag_limit: int = 15, note: str = "") -> str:
    """Fetch Docker Hub repo metadata and recent tags. Scratch cache only — no pull/run."""
    return _json(container_scout.detail_hub(repo, tag_limit=tag_limit, note=note))


@mcp.tool()
async def container_scout_docker_status(name_filter: str = "empire-") -> str:
    """List local Docker containers matching EMPIRE names (default empire-*). Status only."""
    return _json(container_scout.docker_status(name_filter=name_filter))


if __name__ == "__main__":
    mcp.run()
