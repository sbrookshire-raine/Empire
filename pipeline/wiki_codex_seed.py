"""Codex → pending priority subjects seed (planning only)."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

from pipeline.wiki_ops_paths import subjects_path
from pipeline.wiki_priority_subjects import add_subjects, load_subjects, save_subjects
from pipeline.wiki_title_matcher import normalize_text

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CODEX = ROOT / "docs" / "reference" / "THE MASTER CODEX! 50 UNIVERSAL PRIMITIVES.md"

SECTION_RE = re.compile(r"^##\s+(.+)$")
PRIMITIVE_RE = re.compile(r"^\d+\.\s+\*\*(.+?)\*\*:")  # **Name**:
PRIMITIVE_RE_COLON_IN = re.compile(r"^\d+\.\s+\*\*(.+?):\*\*")  # **Name:**
PRIMITIVE_RE_NO_COLON = re.compile(r"^\d+\.\s+\*\*(.+?)\*\*\s*$")


def parse_codex_primitives(text: str) -> list[dict[str, str]]:
    current_section = "codex_primitive"
    out: list[dict[str, str]] = []
    for line in text.splitlines():
        sec = SECTION_RE.match(line.strip())
        if sec:
            current_section = sec.group(1).strip()
            continue
        stripped = line.strip()
        m = (
            PRIMITIVE_RE.match(stripped)
            or PRIMITIVE_RE_COLON_IN.match(stripped)
            or PRIMITIVE_RE_NO_COLON.match(stripped)
        )
        if not m:
            continue
        name = m.group(1).strip().rstrip(":")
        if not name:
            continue
        out.append(
            {
                "subject": name,
                "intent": f"codex_primitive | {current_section}",
            }
        )
    return out


def seed_from_codex(
    *,
    codex_path: Path | None = None,
    subjects_file: Path | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    path = codex_path or DEFAULT_CODEX
    if not path.exists():
        msg = f"Codex seed skipped: file not found at {path}"
        print(msg)
        return {"ok": True, "skipped": True, "message": msg, "added": 0, "would_add": 0}
    primitives = parse_codex_primitives(path.read_text(encoding="utf-8"))
    doc = load_subjects(subjects_file)
    existing = {normalize_text(s.get("subject", "")) for s in doc.get("subjects") or []}
    to_add: list[dict[str, str]] = []
    for prim in primitives:
        if normalize_text(prim["subject"]) in existing:
            continue
        to_add.append(prim)
        existing.add(normalize_text(prim["subject"]))
    if dry_run:
        print(f"Codex dry-run: would-add={len(to_add)} already={len(primitives) - len(to_add)}")
        return {
            "ok": True,
            "dry_run": True,
            "would_add": len(to_add),
            "skipped_dupes": len(primitives) - len(to_add),
            "parsed": len(primitives),
        }
    if to_add:
        doc = add_subjects(doc, to_add, updated_by="codex_seed")
        save_subjects(doc, subjects_file)
    print(f"Codex seed: added={len(to_add)} skipped_dupes={len(primitives) - len(to_add)}")
    return {
        "ok": True,
        "added": len(to_add),
        "skipped_dupes": len(primitives) - len(to_add),
        "parsed": len(primitives),
        "path": str(subjects_file or subjects_path()),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Seed priority subjects from Master Codex")
    parser.add_argument("--codex-path", default="")
    parser.add_argument("--subjects-path", default="")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    result = seed_from_codex(
        codex_path=Path(args.codex_path) if args.codex_path else None,
        subjects_file=Path(args.subjects_path) if args.subjects_path else None,
        dry_run=args.dry_run,
    )
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
