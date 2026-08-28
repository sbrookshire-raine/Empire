"""Smoke test for Cognee MCP tools."""
import asyncio
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("cognee_mcp", Path("mcp/cognee_mcp.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


async def main() -> None:
    recall = await mod.cognee_recall("What is Issue 42?", dataset="mock")
    print("cognee_recall:", recall[:500])


asyncio.run(main())
