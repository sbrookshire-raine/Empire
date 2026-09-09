"""FastMCP: GitHub Scout — search + README cache (no auto-Cognee)."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import github_scout

mcp = FastMCP("empire-github-scout")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def github_scout_search(query: str, limit: int = 10, note: str = "") -> str:
    """Search GitHub repositories by keyword. Caches markdown under github_cache."""
    return _json(github_scout.search_repos(query, limit=limit, note=note))


@mcp.tool()
async def github_scout_readme(repo: str, note: str = "") -> str:
    """Fetch README excerpt for owner/repo. Scratch cache only — no clone/install."""
    return _json(github_scout.repo_readme(repo, note=note))


if __name__ == "__main__":
    mcp.run()
