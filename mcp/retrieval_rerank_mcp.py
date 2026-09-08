"""FastMCP: retrieval rerank eval (scratch; nomic production unchanged)."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import retrieval_rerank

mcp = FastMCP("empire-retrieval-rerank")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def retrieval_rerank(query: str, candidates_json: str, top_k: int = 5) -> str:
    """Rerank candidate passages for a query. Eval/scratch only — does not change Cognee embeds."""
    try:
        cands = json.loads(candidates_json)
    except json.JSONDecodeError as exc:
        return _json({"ok": False, "error": str(exc)})
    return _json(
        retrieval_rerank.rerank(query, cands if isinstance(cands, list) else [], top_k=top_k)
    )


@mcp.tool()
async def retrieval_rerank_eval() -> str:
    """Run golden retrieval rerank cases; write acceptance YAML. Never touches production embeds."""
    return _json(retrieval_rerank.run_eval())


if __name__ == "__main__":
    mcp.run()
