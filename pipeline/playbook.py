"""Capability playbook — worked examples for using a limb, on demand.

Why this exists
---------------
Measured 2026-09-24: the system prompt is only `eve_instructions.md` + `empire-routing.md`
(`agent/instructions.ts`), so **nothing loads `agent/skills/*.md`** — 33 skill files were inert, and
the routing index's "load skill-x" lines pointed at skills that never entered context. The Architect's
ask: give Eve worked pathways per capability (3–7 concrete examples each: *ask → tools → artefact*) so
she reuses a known route instead of reaching for a tool at random.

Layout
------
`config/eve-capabilities/playbook/<area>.md`, one area per file, one `## <skill>` section per
capability, each with a purpose line, the tool names it needs, and 3+ worked examples. Files keep
front matter so `index()` can list them without loading bodies:

    ---
    area: wiki-archive
    one_line: Local Wikipedia work — lookup, hops, sections, extracts, truth drift.
    tools: wiki_scout_search, wiki_read_section, wiki_extract, wiki_resolve
    ---
    ## Local Wikipedia lookup
    Use when: …
    - **Ask:** "what album has Seven Nation Army?" -> **Do:** `wiki_scout_search("The White Stripes")`
      then `wiki_read_section("Elephant")` -> **Get:** the album+track answer with the page named.

`tests/pipeline/test_playbook.py` enforces the Architect's requirement: every section carries at least
three examples (or an explicit "not enough real uses yet" note with a next step).
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PLAYBOOK_DIR = ROOT / "config" / "eve-capabilities" / "playbook"
# The R-03 tool registry: one doc per callable tool. Coverage is measured against this, because
# it is the same list the prompt-budget test uses to prove enabled tools stay documented.
DEFAULT_TOOL_DOCS_DIR = ROOT / "config" / "eve-capabilities" / "tool-docs"
# The authored skill files (E-29: they never enter context). The playbook is their runtime home,
# so every one of them has to be claimed by an area's `skills:` front matter.
DEFAULT_SKILLS_DIR = ROOT / "agents" / "empire-task-agent" / "agent" / "skills"
FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
MAX_AREA_CHARS = 9_000
MIN_EXAMPLES = 3


def playbook_dir() -> Path:
    """Directory holding one markdown area per file (overridable for tests)."""

    override = os.environ.get("EMPIRE_PLAYBOOK", "").strip()
    return Path(override) if override else DEFAULT_PLAYBOOK_DIR


def tool_docs_dir() -> Path:
    """The tool registry behind `tool_docs` — the list every claimed tool must exist in."""

    override = os.environ.get("EMPIRE_TOOL_DOCS", "").strip()
    return Path(override) if override else DEFAULT_TOOL_DOCS_DIR


def skills_dir() -> Path:
    """Where the authored `agent/skills/*.md` files live (overridable for tests)."""

    override = os.environ.get("EMPIRE_SKILLS", "").strip()
    return Path(override) if override else DEFAULT_SKILLS_DIR


def _front_matter(text: str) -> dict[str, str]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        if key.strip():
            fields[key.strip()] = value.strip()
    return fields


def _sections(body: str) -> list[dict[str, Any]]:
    """Each `## heading` with its line count and how many examples it holds."""

    matches = list(SECTION_RE.finditer(body))
    sections: list[dict[str, Any]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        chunk = body[start:end]
        examples = len(re.findall(r"^\s*[-*]\s+\*\*Ask", chunk, re.MULTILINE))
        sections.append(
            {
                "title": match.group(1).strip(),
                "examples": examples,
                "chars": len(chunk.strip()),
                "tools": sorted(set(re.findall(r"`([a-z][a-z0-9_]{2,})`", chunk))),
            }
        )
    return sections


def index() -> list[dict[str, Any]]:
    """Every playbook area with its front-matter one-liner and section titles."""

    directory = playbook_dir()
    if not directory.is_dir():
        return []
    entries: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fields = _front_matter(text)
        body = FRONT_MATTER_RE.sub("", text)
        sections = _sections(body)
        entries.append(
            {
                "area": fields.get("area") or path.stem,
                "one_line": fields.get("one_line", ""),
                "tools": fields.get("tools", ""),
                "skills": fields.get("skills", ""),
                "sections": [section["title"] for section in sections],
                "examples": sum(section["examples"] for section in sections),
            }
        )
    return entries


def _area_ids() -> list[str]:
    return [entry["area"] for entry in index()]


def _payload(text: str, area: str, max_chars: int) -> dict[str, Any]:
    fields = _front_matter(text)
    body = FRONT_MATTER_RE.sub("", text).strip()
    truncated = len(body) > max_chars
    return {
        "ok": True,
        "area": area,
        "one_line": fields.get("one_line", ""),
        "tools": fields.get("tools", ""),
        "skills": fields.get("skills", ""),
        "examples": len(re.findall(r"^\s*[-*]\s+\*\*Ask", body, re.MULTILINE)),
        "sections": [section["title"] for section in _sections(body)],
        "playbook": body[:max_chars] + ("\n\n[truncated — ask for a narrower topic]" if truncated else ""),
        "truncated": truncated,
        "chars": len(body),
    }


def topic(name: str, *, max_chars: int = MAX_AREA_CHARS) -> dict[str, Any]:
    """One area's worked examples, bounded. `name` is an area id, a section title, or a tool."""

    cleaned = str(name or "").strip()
    if not cleaned or "/" in cleaned or "\\" in cleaned or ".." in cleaned:
        return {"ok": False, "error": "invalid playbook topic", "topic": cleaned, "areas": _area_ids()}

    directory = playbook_dir()
    wanted = cleaned.casefold()

    direct = directory / f"{wanted}.md"
    if direct.is_file():
        return _payload(direct.read_text(encoding="utf-8"), wanted, max_chars)

    for path in sorted(directory.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fields = _front_matter(text)
        body = FRONT_MATTER_RE.sub("", text)
        haystacks = [fields.get("area", ""), fields.get("tools", "")]
        haystacks += [section["title"] for section in _sections(body)]
        haystacks += re.findall(r"`([a-z][a-z0-9_]{2,})`", body)
        if any(wanted in item.casefold() for item in haystacks if item):
            payload = _payload(text, fields.get("area") or path.stem, max_chars)
            payload["matched"] = cleaned
            return payload

    return {
        "ok": False,
        "error": f"no playbook area matches {cleaned!r}",
        "topic": cleaned,
        "areas": _area_ids(),
    }


def thin_sections() -> list[dict[str, Any]]:
    """Sections with fewer than `MIN_EXAMPLES` worked examples — the coverage check for tests."""

    thin: list[dict[str, Any]] = []
    directory = playbook_dir()
    if not directory.is_dir():
        return thin
    for path in sorted(directory.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fields = _front_matter(text)
        body = FRONT_MATTER_RE.sub("", text)
        for section in _sections(body):
            if section["examples"] < MIN_EXAMPLES:
                thin.append(
                    {
                        "area": fields.get("area") or path.stem,
                        "section": section["title"],
                        "examples": section["examples"],
                    }
                )
    return thin


def coverage() -> dict[str, Any]:
    """Does she have a worked example for every skill she can reach? Both directions, checked.

    The Architect's ask (2026-09-24): her playbook must be tried and true for **every** skill she
    has — so this measures instead of asserting:

    - `missing_tools` — a tool in the R-03 registry that no area claims (no worked example)
    - `ghost_tools`  — an area promising a tool that is not in the registry (a pointer into
      nothing, which is how `load_skill_manifest` fooled the routing lines: it was a Python
      helper, never a tool)
    - `unused_tools` — claimed by an area, but appearing in no example body anywhere
    - `missing_skills` — an `agent/skills/*.md` file no area claims (the E-29 blind spot)
    - `ghost_skills`  — a claimed `skills:` entry with no file behind it
    """

    doc_dir = tool_docs_dir()
    skill_dir = skills_dir()
    doc_names = {path.stem for path in doc_dir.glob("*.md")} if doc_dir.is_dir() else set()

    claimed: dict[str, str] = {}
    declared_skills: dict[str, str] = {}
    bodies: list[str] = []
    directory = playbook_dir()
    for path in sorted(directory.glob("*.md")) if directory.is_dir() else []:
        text = path.read_text(encoding="utf-8")
        fields = _front_matter(text)
        area = fields.get("area") or path.stem
        body = FRONT_MATTER_RE.sub("", text)
        bodies.append(body)
        for name in (fields.get("tools") or "").split(","):
            name = name.strip()
            if name:
                claimed.setdefault(name, area)
        for name in (fields.get("skills") or "").split(","):
            name = name.strip()
            if name:
                declared_skills.setdefault(name, area)

    examples = "\n".join(bodies)
    skill_names = {path.stem for path in skill_dir.glob("*.md")} if skill_dir.is_dir() else set()

    missing_tools = sorted(name for name in doc_names if name not in claimed)
    ghost_tools = sorted(name for name in claimed if name not in doc_names)
    unused_tools = sorted(
        name
        for name in claimed
        if name not in ghost_tools and not re.search(rf"`{re.escape(name)}\b", examples)
    )
    missing_skills = sorted(name for name in skill_names if name not in declared_skills)
    ghost_skills = sorted(name for name in declared_skills if name not in skill_names)

    return {
        "ok": not (missing_tools or ghost_tools or unused_tools or missing_skills or ghost_skills),
        "tool_docs": len(doc_names),
        "claimed_tools": len(claimed),
        "missing_tools": missing_tools,
        "ghost_tools": ghost_tools,
        "unused_tools": unused_tools,
        "skill_files": len(skill_names),
        "declared_skills": len(declared_skills),
        "missing_skills": missing_skills,
        "ghost_skills": ghost_skills,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Capability playbook: worked examples per area")
    parser.add_argument("topic", nargs="?", default="", help="Area id, section title, or tool name")
    parser.add_argument("--list", action="store_true", help="List areas with their sections")
    parser.add_argument(
        "--coverage",
        action="store_true",
        help="Check that every registry tool and every agent/skills file has worked examples",
    )
    parser.add_argument("--max-chars", type=int, default=MAX_AREA_CHARS)
    args = parser.parse_args(argv)

    if args.coverage:
        payload: dict[str, Any] = coverage()
    elif args.list or not args.topic:
        payload = {"ok": True, "areas": index()}
    else:
        payload = topic(args.topic, max_chars=max(500, min(args.max_chars, MAX_AREA_CHARS)))
    print(json.dumps(payload, indent=2, default=str))
    return 0 if payload.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
