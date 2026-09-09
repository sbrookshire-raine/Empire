"""FastMCP: Tool Forge — docs scrape, skill inventory, active tool listing."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import docs_guide_scraper, skill_compiler

mcp = FastMCP("empire-tool-forge")

ACTIVE_TOOLS_DIR = Path(
    os.environ.get("EMPIRE_ACTIVE_TOOLS_DIR", r"C:\Empire_Workbench\03_Active_Tools")
)
HARVEST_CACHE_DIR = Path(
    os.environ.get(
        "EMPIRE_HARVEST_CACHE_DIR",
        r"C:\Empire_Workbench\04_Thought_Experiments\harvest_cache",
    )
)


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def docs_guide_discover(root_url: str, max_pages: int = 80) -> str:
    """Discover documentation page URLs via llms.txt or sitemap (no full scrape)."""
    return _json(docs_guide_scraper.discover_pages(root_url, max_pages=max_pages))


@mcp.tool()
async def docs_guide_scrape(root_url: str, max_pages: int = 80, note: str = "") -> str:
    """Scrape a documentation site into one Markdown guide under harvest_cache."""
    return _json(
        docs_guide_scraper.scrape_site(
            root_url,
            max_pages=max_pages,
            cache_dir=HARVEST_CACHE_DIR,
            note=note,
        )
    )


@mcp.tool()
async def skill_inventory(paths: str = "", include_installed: bool = True) -> str:
    """Inventory SKILL.md files from comma-separated paths/zips and .cursor/skills."""
    path_list = [p.strip() for p in paths.split(",") if p.strip()] if paths else []
    return _json(
        skill_compiler.inventory_sources(
            path_list,
            include_default_skills=include_installed,
        )
    )


@mcp.tool()
async def skill_triage_manifest(paths: str = "", include_installed: bool = True) -> str:
    """Run Build1 3-Bin heuristic triage; write manifest JSON + markdown under harvest_cache."""
    path_list = [p.strip() for p in paths.split(",") if p.strip()] if paths else []
    return _json(
        skill_compiler.run_inventory_and_triage(
            path_list,
            out_dir=HARVEST_CACHE_DIR,
            include_default_skills=include_installed,
        )
    )


@mcp.tool()
async def list_harvest_outputs() -> str:
    """List Markdown guides and triage manifests in harvest_cache."""
    HARVEST_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(
        [
            {
                "name": p.name,
                "path": str(p),
                "bytes": p.stat().st_size,
            }
            for p in HARVEST_CACHE_DIR.iterdir()
            if p.is_file() and p.suffix.lower() in {".md", ".json"}
        ],
        key=lambda row: row["name"],
    )
    return _json({"ok": True, "dir": str(HARVEST_CACHE_DIR), "files": files, "count": len(files)})


@mcp.tool()
async def list_active_tools() -> str:
    """List flattened tool files in 03_Active_Tools (read-only index)."""
    if not ACTIVE_TOOLS_DIR.is_dir():
        return _json({"ok": False, "error": f"directory missing: {ACTIVE_TOOLS_DIR}"})
    files = sorted(
        p.name for p in ACTIVE_TOOLS_DIR.iterdir() if p.is_file() and not p.name.startswith(".")
    )
    return _json({"ok": True, "dir": str(ACTIVE_TOOLS_DIR), "files": files, "count": len(files)})


if __name__ == "__main__":
    mcp.run()
