"""FastMCP: structured DocumentMetadata extract (scratch only, no Cognee)."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import structured_extract

mcp = FastMCP("empire-structured-extract")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def structured_extract_text(text: str, prefer: str = "llama", note: str = "") -> str:
    """Extract DocumentMetadata JSON from text via llama.cpp (preferred) or Ollama fallback. Scratch cache only."""
    prefer_norm = prefer if prefer in {"llama", "ollama"} else "llama"
    return _json(
        structured_extract.extract_text(text, prefer=prefer_norm, note=note)
    )


@mcp.tool()
async def structured_extract_file(path: str, prefer: str = "llama", note: str = "") -> str:
    """Extract DocumentMetadata from a local UTF-8 text file. Does not write Cognee."""
    prefer_norm = prefer if prefer in {"llama", "ollama"} else "llama"
    return _json(
        structured_extract.extract_file(path, prefer=prefer_norm, note=note)
    )


if __name__ == "__main__":
    mcp.run()
