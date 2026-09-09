"""FastMCP: Loom intake — Knowledge Shell CSV → primitive ledger."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import loom_intake

mcp = FastMCP("empire-loom-intake")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def loom_status() -> str:
    """Paths and row counts for primitive ledger, shell buffer, and gap report."""
    return _json(loom_intake.loom_status())


@mcp.tool()
async def loom_process_shell_csv(
    csv_path: str,
    domain_bucket: str = "general",
    max_per_cycle: int = 7,
) -> str:
    """Process a 12-column Shell Packet CSV through Knowledge Shell intake."""
    return _json(
        loom_intake.process_shell_csv(
            csv_path,
            domain_bucket=domain_bucket,
            max_per_cycle=max_per_cycle,
        )
    )


if __name__ == "__main__":
    mcp.run()
