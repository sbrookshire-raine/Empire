"""Idea store: the queryable view of `docs/ideas/*.md` (front matter is canonical).

Files are the source of truth; this module is the index. `scripts/list-ideas.py` is a thin CLI over
it, `tests/test_idea_docs.py` enforces the convention, and the PocketBase mirror planned in E-20 will
import from `load_ideas()` rather than re-parsing markdown.

Convention: docs/ideas/README.md  ·  entry template: docs/ideas/_TEMPLATE.md
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
IDEAS_DIR = ROOT / "docs" / "ideas"
QUEUE_PATH = ROOT / "docs" / "EMPIRE_IDEA_QUEUE.md"

# Must match the status legend in docs/EMPIRE_IDEA_QUEUE.md.
STATUSES = ("idea", "ready", "in_progress", "blocked", "parked", "done")
REQUIRED_FIELDS = ("id", "slug", "title", "status", "area", "priority", "created", "source")
REQUIRED_SECTIONS = (
    "## Intent",
    "## Why it matters",
    '## What "done" looks like (acceptance)',
    "## Stack plan (how it applies in EMPIRE)",
    "## Constraints and identity",
    "## Open questions",
)

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_front_matter(text: str) -> dict[str, str]:
    """Flat `key: value` front matter (values are strings; lists stay as written)."""

    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        key = key.strip()
        if key:
            fields[key] = value.strip()
    return fields


def is_idea_file(path: Path) -> bool:
    return not path.name.startswith("_") and path.name.casefold() != "readme.md"


def idea_files() -> list[Path]:
    if not IDEAS_DIR.is_dir():
        return []
    return [path for path in sorted(IDEAS_DIR.glob("*.md")) if is_idea_file(path)]


def load_ideas() -> list[dict[str, Any]]:
    """All recorded ideas, with their front matter plus `path` and `body`."""

    ideas: list[dict[str, Any]] = []
    for path in idea_files():
        text = path.read_text(encoding="utf-8")
        fields = parse_front_matter(text)
        ideas.append(
            {
                "id": fields.get("id", ""),
                "slug": fields.get("slug") or path.stem,
                "title": fields.get("title", ""),
                "status": fields.get("status", ""),
                "area": fields.get("area", ""),
                "priority": fields.get("priority", ""),
                "depends_on": fields.get("depends_on", ""),
                "created": fields.get("created", ""),
                "source": fields.get("source", ""),
                "path": path.relative_to(ROOT).as_posix(),
                "body": FRONT_MATTER_RE.sub("", text).strip(),
            }
        )
    return ideas


def filter_ideas(
    ideas: list[dict[str, Any]], *, status: str = "", area: str = ""
) -> list[dict[str, Any]]:
    result = ideas
    if status.strip():
        result = [idea for idea in result if idea["status"] == status.strip()]
    if area.strip():
        result = [idea for idea in result if idea["area"] == area.strip()]
    return result


def read_idea(slug: str) -> dict[str, Any]:
    """One idea by slug (or by `E-xx` id) — this is what Eve's `read_idea` will call."""

    wanted = str(slug or "").strip().casefold()
    if not wanted:
        return {"ok": False, "error": "slug is required"}
    for idea in load_ideas():
        if wanted in {str(idea["slug"]).casefold(), str(idea["id"]).casefold()}:
            return {"ok": True, **idea}
    return {"ok": False, "error": f"no idea matches {slug!r}", "available": [i["slug"] for i in load_ideas()]}