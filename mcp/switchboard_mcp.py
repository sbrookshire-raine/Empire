"""FastMCP: Eve Switchboard — governed service control for Cursor."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import switchboard

mcp = FastMCP("empire-switchboard")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def switchboard_status() -> str:
    """Snapshot of EMPIRE services, headroom, and GPU lease (read-only)."""
    return _json(switchboard.status())


@mcp.tool()
async def switchboard_plan(services: list[str]) -> str:
    """Dry-run plan for which services a task needs (no mutation)."""
    return _json(switchboard.plan(list(services)))


@mcp.tool()
async def switchboard_ensure(services: list[str], dry_run: bool = True) -> str:
    """Start services a task needs (headroom-gated). dry_run defaults True."""
    return _json(switchboard.ensure(list(services), dry_run=dry_run))


@mcp.tool()
async def switchboard_release(services: list[str], dry_run: bool = True) -> str:
    """Stop managed services a task no longer needs. dry_run defaults True."""
    return _json(switchboard.release(list(services), dry_run=dry_run))


@mcp.tool()
async def switchboard_tenant(action: str, tenant: str = "", dry_run: bool = True) -> str:
    """GPU tenant lease: acquire/release/status. dry_run defaults True."""
    return _json(switchboard.tenant(action, tenant_name=tenant, dry_run=dry_run))


if __name__ == "__main__":
    mcp.run()
