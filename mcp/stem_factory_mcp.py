"""FastMCP: Shard of the Division stem splitter (Stem Factory) for Eve."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import stem_factory

mcp = FastMCP("empire-stem-factory")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def stem_status() -> str:
    """Check Stem Factory (Shard of the Division) path, venv, and inbox song count."""
    return _json(stem_factory.status())


@mcp.tool()
async def stem_list_inbox() -> str:
    """List audio files waiting in C:/Empire_Workbench/stem_factory/input."""
    return _json(stem_factory.list_inbox())


@mcp.tool()
async def stem_run(
    limit: int = 1,
    device: str = "cuda",
    overwrite: bool = False,
    input_dir: str = "",
    output_dir: str = "",
) -> str:
    """Run Demucs stem + practice-track generation on the inbox folder.

    Drop songs into C:/Empire_Workbench/stem_factory/input first.
    Default limit=1 (one song). GPU preferred; auto-falls back to CPU if needed.
    Takes ~1–several minutes per song. Returns output paths under stem_factory/output.
    """
    result = stem_factory.run_stems(
        input_dir=input_dir or None,
        output_dir=output_dir or None,
        device=device or "cuda",
        limit=int(limit) if limit else 1,
        overwrite=bool(overwrite),
    )
    return _json(result)


if __name__ == "__main__":
    mcp.run()
