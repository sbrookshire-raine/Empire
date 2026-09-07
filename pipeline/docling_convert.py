"""Docling local convert → Markdown for Resource Queue / Cognee staging."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT_DIR = Path(
    os.environ.get(
        "EMPIRE_DOCLING_OUT_DIR",
        r"C:\Empire_Workbench\00_Resource_Queue",
    )
)
_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")


def check_install() -> dict[str, Any]:
    try:
        from docling.document_converter import DocumentConverter  # noqa: F401

        return {"ok": True, "hint": "docling available"}
    except ImportError:
        return {
            "ok": False,
            "hint": "pip install docling — https://github.com/docling-project/docling",
        }


def convert_file(
    input_path: str | Path,
    *,
    output_path: str | Path | None = None,
    out_dir: Path | None = None,
) -> dict[str, Any]:
    src = Path(input_path)
    if not src.is_file():
        return {"ok": False, "error": f"not a file: {src}"}

    install = check_install()
    if not install.get("ok"):
        return {"ok": False, "error": install.get("hint"), **install}

    try:
        from docling.document_converter import DocumentConverter

        converter = DocumentConverter()
        result = converter.convert(str(src))
        doc = result.document
        if not hasattr(doc, "export_to_markdown"):
            return {"ok": False, "error": "Docling Document missing export_to_markdown()"}
        md = doc.export_to_markdown()
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "input": str(src)}

    from pipeline.provenance import provenance_fields, provenance_markdown_footer

    if output_path:
        out = Path(output_path)
    else:
        dest_dir = Path(out_dir) if out_dir else DEFAULT_OUT_DIR
        dest_dir.mkdir(parents=True, exist_ok=True)
        stem = _SAFE.sub("_", src.stem).strip("_") or "document"
        out = dest_dir / f"{stem}.md"

    header = "\n".join(
        [
            "---",
            *provenance_fields(
                source="docling",
                kind="document_convert",
                tool="docling_convert",
                limb="core",
                extra={"input": str(src), "output": str(out)},
            ),
            "---",
            f"# {src.name}",
            "",
        ]
    )
    body = header + md + provenance_markdown_footer(
        source="docling", tool="docling_convert", limb="core"
    )
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body, encoding="utf-8")
    except OSError as exc:
        return {"ok": False, "error": str(exc), "input": str(src)}

    return {
        "ok": True,
        "input": str(src),
        "output": str(out),
        "chars": len(body),
        "note": "Markdown staged — use cognee_remember or Workbench upload to store in memory.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Docling → Markdown for EMPIRE")
    parser.add_argument("input", nargs="?", help="Local PDF/Office path")
    parser.add_argument("-o", "--output", help="Output .md path")
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    parser.add_argument("--check-install", action="store_true")
    args = parser.parse_args(argv)

    if args.check_install or not args.input:
        info = check_install()
        print(json.dumps(info, indent=2))
        return 0 if info.get("ok") else 1

    result = convert_file(args.input, output_path=args.output, out_dir=Path(args.out_dir))
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
