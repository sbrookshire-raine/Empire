#!/usr/bin/env python3
"""docling-local-ingest: convert local documents to Markdown for Cognee staging.

Install: pip install docling
Does not call cloud LLMs or Azure Document Intelligence.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from docling.document_converter import DocumentConverter
except ImportError:
    DocumentConverter = None  # type: ignore[misc, assignment]


def check_install() -> dict:
    ok = DocumentConverter is not None
    return {
        "ok": ok,
        "hint": "pip install docling — https://github.com/docling-project/docling",
    }


def convert_to_markdown(src: Path) -> str:
    if DocumentConverter is None:
        raise RuntimeError("docling not installed; run: pip install docling")

    converter = DocumentConverter()
    result = converter.convert(str(src))
    doc = result.document
    if hasattr(doc, "export_to_markdown"):
        return doc.export_to_markdown()
    raise RuntimeError("Docling Document missing export_to_markdown(); check docling version")


def main() -> int:
    parser = argparse.ArgumentParser(description="EMPIRE Docling → Markdown helper")
    parser.add_argument("input", nargs="?", type=Path, help="Local PDF/Office path")
    parser.add_argument("-o", "--output", type=Path, help="Output .md path")
    parser.add_argument("--check-install", action="store_true")
    args = parser.parse_args()

    if args.check_install or args.input is None:
        info = check_install()
        print(json.dumps(info, indent=2))
        if args.input is None:
            return 0 if info["ok"] else 1

    src: Path = args.input
    if not src.is_file():
        print(json.dumps({"ok": False, "error": f"not a file: {src}"}), file=sys.stderr)
        return 2

    try:
        md = convert_to_markdown(src)
    except Exception as exc:  # noqa: BLE001 — surface any convert failure as JSON
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 1

    out = args.output
    if out is None:
        out = src.with_suffix(".md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    print(json.dumps({"ok": True, "input": str(src), "output": str(out), "chars": len(md)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
