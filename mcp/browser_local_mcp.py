"""FastMCP: allowlisted localhost Playwright fetch."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import browser_local

mcp = FastMCP("empire-browser-local")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def browser_local_fetch(url: str, note: str = "") -> str:
    """Fetch title/text from an allowlisted localhost EMPIRE URL only. No Cognee. No form submit."""
    return _json(browser_local.fetch_page(url, note=note))


if __name__ == "__main__":
    mcp.run()
