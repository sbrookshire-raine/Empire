"""FastMCP: web scout → web_cache markdown (explicit Cognee promote only)."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import web_scout

mcp = FastMCP("empire-web-scout")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def web_scout_url(url: str, note: str = "") -> str:
    """Fetch a public http(s) page and cache Truth Drift-style markdown under web_cache.

    Never auto-promotes to Cognee. Requires Web Scout Toolbelt when used via Eve.
    """
    return _json(web_scout.scout(url, note=note))


if __name__ == "__main__":
    mcp.run()
