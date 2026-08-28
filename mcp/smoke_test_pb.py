"""Smoke test for PocketBase MCP tools (Phase 2 verification gate)."""
import asyncio
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "pocketbase_mcp", Path("mcp/pocketbase_mcp.py")
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


async def main() -> None:
    health = await mod.pb_health()
    print("pb_health:", health[:120])

    collections = await mod.pb_list_collections()
    print("pb_list_collections:", collections[:300])

    records = await mod.pb_list_records("tasks")
    print("pb_list_records(tasks):", records[:400])


asyncio.run(main())
