"""FastMCP: artifact arms — spreadsheet, code author, python verify."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import author_code, create_spreadsheet, python_verify

mcp = FastMCP("empire-artifact")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def create_spreadsheet(
    filename: str,
    headers: list[str],
    rows: list[list[Any]],
    sheet_name: str = "Sheet1",
    note: str = "",
) -> str:
    """Write an .xlsx into eve-output (formula injection blocked)."""
    return _json(
        create_spreadsheet.create_spreadsheet(
            filename=filename,
            headers=list(headers),
            rows=rows,
            sheet_name=sheet_name,
            note=note,
        )
    )


@mcp.tool()
async def author_code_create_worktree(note: str = "") -> str:
    """Create a disposable Git worktree for code authoring (never push/merge)."""
    return _json(author_code.create_worktree(note=note))


@mcp.tool()
async def author_code_apply_patch(worktree: str, relative_path: str, content: str) -> str:
    """Write a file inside a disposable worktree and return its reviewable diff."""
    return _json(author_code.apply_patch(worktree=worktree, relative_path=relative_path, content=content))


@mcp.tool()
async def author_code_remove_worktree(worktree: str) -> str:
    """Remove a disposable worktree."""
    return _json(author_code.remove_worktree(worktree))


@mcp.tool()
async def python_verify(worktree: str, run_tests: bool = True) -> str:
    """Syntax-check + (optional) lint/test a disposable worktree; never merges."""
    return _json(python_verify.verify(worktree=worktree, run_tests=run_tests))


if __name__ == "__main__":
    mcp.run()
