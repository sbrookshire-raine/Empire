"""FastMCP: Docling local document → markdown."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import docling_convert

mcp = FastMCP("empire-docling")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def docling_check_install() -> str:
    """Check whether docling is installed in the EMPIRE venv."""
    return _json(docling_convert.check_install())


@mcp.tool()
async def docling_convert(
    input_path: str,
    output_path: str = "",
) -> str:
    """Convert a local PDF/Office file to Markdown under Resource Queue (or output_path).

    Does not write Cognee — stage then cognee_remember / Workbench upload.
    """
    return _json(
        docling_convert.convert_file(
            input_path,
            output_path=output_path or None,
        )
    )


if __name__ == "__main__":
    mcp.run()
