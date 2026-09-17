"""Read document — extract text/markdown from local files.

Evidence arm (read-only). Prefers MarkItDown when installed (fast, local, no
auth); falls back to Docling (already wired via pipeline/docling_convert.py).
Input is constrained to allowlisted roots; output is a provenance-stamped
markdown file under eve-output (never Cognee, never Resource Queue mutation).

Offline-convertible: markitdown/docling are local libs; no network at runtime.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any

from pipeline.provenance import provenance_fields, provenance_markdown_footer

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_ROOTS: tuple[Path, ...] = (
    Path(r"C:\Empire_Workbench"),
    ROOT / "docs",
    ROOT / "data",
)
DEFAULT_OUTPUT_DIR = Path(
    os.environ.get("EMPIRE_EVE_OUTPUT_DIR", r"C:\EMPIRE\eve-output")
)
DEFAULT_MAX_INPUT_BYTES = int(os.environ.get("EMPIRE_READ_DOC_MAX_BYTES", str(50 * 1024 * 1024)))
_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")

_SUPPORTED_EXTENSIONS: frozenset[str] = frozenset(
    {
        ".md", ".txt", ".csv", ".tsv", ".json", ".jsonl",
        ".pdf", ".docx", ".pptx", ".xlsx", ".html", ".htm",
    }
)


def _input_roots() -> list[Path]:
    override = os.environ.get("EMPIRE_READ_DOC_ROOTS", "").strip()
    if override:
        roots: list[Path] = []
        for part in override.split(os.pathsep):
            p = Path(part.strip()).expanduser()
            if p.is_dir():
                roots.append(p)
        if roots:
            return roots
    return [r for r in DEFAULT_INPUT_ROOTS if r.is_dir()]


def _resolve_input(candidate: str) -> tuple[Path | None, str | None]:
    raw = (candidate or "").strip().strip('"').strip("'")
    if not raw:
        return None, "input path is required"
    if raw.startswith("http://") or raw.startswith("https://"):
        return None, "network paths are forbidden"
    p = Path(raw)
    roots = _input_roots()
    if not roots:
        return None, "no allowlisted input roots configured"
    if p.is_absolute():
        candidate_path = p.resolve()
    else:
        candidate_path = None
        for root in roots:
            guess = (root / raw).resolve()
            if guess.exists():
                candidate_path = guess
                break
        if candidate_path is None:
            candidate_path = (roots[0] / raw).resolve()
    for root in roots:
        try:
            candidate_path.relative_to(root.resolve())
            if candidate_path.is_file():
                return candidate_path, None
            return None, f"file not found: {candidate_path}"
        except ValueError:
            continue
    return None, "path escapes allowlisted input roots"


def _try_markitdown(src: Path) -> str | None:
    try:
        from markitdown import MarkItDown  # type: ignore

        md = MarkItDown()
        result = md.convert(str(src))
        text = getattr(result, "text_content", None)
        if text is None:
            return None
        return str(text)
    except Exception:  # noqa: BLE001
        return None


def _try_docling(src: Path) -> str | None:
    try:
        import tempfile

        from pipeline import docling_convert

        with tempfile.TemporaryDirectory(prefix="empire-read-doc-") as tmp:
            converted = docling_convert.convert_file(
                str(src),
                output_path=None,
                out_dir=Path(tmp),  # write to temp, never Resource Queue
            )
            if not converted.get("ok"):
                return None
            out = Path(converted.get("output") or "")
            if out.is_file():
                return out.read_text(encoding="utf-8", errors="replace")
            return None
    except Exception:  # noqa: BLE001
        return None


def read_document(
    input_path: str,
    *,
    max_chars: int = 200_000,
) -> dict[str, Any]:
    src, err = _resolve_input(input_path)
    if err or src is None:
        return {"ok": False, "error": err or "invalid input"}

    ext = src.suffix.lower()
    if ext not in _SUPPORTED_EXTENSIONS:
        return {"ok": False, "error": f"unsupported extension: {ext}"}

    try:
        if src.stat().st_size > DEFAULT_MAX_INPUT_BYTES:
            return {"ok": False, "error": f"input too large (> {DEFAULT_MAX_INPUT_BYTES} bytes)"}
    except OSError as exc:
        return {"ok": False, "error": str(exc)}

    # Plain text/markdown: read directly (fast, no converter).
    if ext in {".md", ".txt", ".csv", ".tsv", ".json", ".jsonl"}:
        try:
            body = src.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            return {"ok": False, "error": str(exc)}
        engine = "direct"
    else:
        body = _try_markitdown(src)
        if body is not None:
            engine = "markitdown"
        else:
            body = _try_docling(src)
            engine = "docling" if body is not None else None
        if body is None:
            return {
                "ok": False,
                "error": "no converter available (markitdown/docling) for this format",
                "ext": ext,
            }

    truncated = len(body) > max_chars
    excerpt = body[:max_chars]

    header = "\n".join(
        [
            "---",
            *provenance_fields(
                source="read_document",
                kind="document_read",
                tool="read_document",
                limb="local_evidence",
                extra={"input": str(src), "engine": engine},
            ),
            "---",
            f"# {src.name}",
            "",
        ]
    )
    stamped = header + excerpt + provenance_markdown_footer(
        source="read_document", tool="read_document", limb="local_evidence"
    )

    return {
        "ok": True,
        "engine": engine,
        "input": str(src),
        "chars": len(excerpt),
        "truncated": truncated,
        "content": stamped,
    }


def main(argv: list[str] | None = None) -> int:
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Read a local document to text/markdown")
    parser.add_argument("input")
    parser.add_argument("--max-chars", type=int, default=200_000)
    args = parser.parse_args(argv)
    result = read_document(args.input, max_chars=args.max_chars)
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
