"""On-demand tool documentation registry (refactor plan R-03).

Why this exists
---------------
Tool documentation was living in the hot prompt: every turn paid for the full prose of every
enabled tool's schema plus the always-loaded routing file. Measured 2026-09-24: **1,863 tokens**
of schema prose for the default-enabled set (29 always-on + 8 `wiki_local`) and **2,574 tokens**
for `empire-routing.md`.

What moves where
----------------
- **Stays in the schema** (the model needs it to *choose*): the tool name, a one-line cue, and the
  parameter names.
- **Moves here** (the model needs it only when *executing* something non-obvious): the full
  description, parameter semantics, examples, and gotchas — retrieved by name on demand.

Layout
------
`config/eve-capabilities/tool-docs/<tool>.md`, front matter + prose:

    ---
    name: wiki_read_section
    toolbelt: wiki_local
    one_line: Read one H2 section of a resolved local Wikipedia page.
    ---
    ## Description (verbatim, pre-R-03)
    ## Parameters

`scripts/build-tool-docs.py` generates the docs from the tool sources so nothing is invented or
lost; `tests/pipeline/test_tool_registry.py` asserts every hot-set tool still has a doc.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DOCS_DIR = ROOT / "config" / "eve-capabilities" / "tool-docs"
FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
MAX_DOC_CHARS = 2_400
TOOLS_DIR = ROOT / "agents" / "empire-task-agent" / "agent" / "tools"
DISABLED_RE = re.compile(r"export\s+default\s+disableTool\s*\(")


def tools_dir() -> Path:
    """Directory holding the agent's tool sources (overridable for tests)."""

    import os

    override = os.environ.get("EMPIRE_TOOLS_DIR", "").strip()
    return Path(override) if override else TOOLS_DIR


def tool_sources() -> list[Path]:
    """Sources of tools that actually exist for her — `disableTool()` files excluded.

    `export default disableTool()` switches a tool OFF on purpose: root self-delegation (`agent`),
    the Eve sandbox filesystem (`read_file` / `glob` / `grep` / `write_file`), provider-managed
    search (`web_search` / `web_fetch`), `bash`, and `ask_question` (malformed calls on local
    Ollama — she clarifies in prose instead).

    A doc for one of those is a **phantom**: it makes the registry — and anything quoting it, like
    the playbook or the routing lines — promise a tool she cannot call. Measured 2026-09-24: nine
    such docs existed, and two routing lines plus a playbook example pointed at
    `load_skill_manifest`, which was a Python helper, never a tool at all. This is the single place
    that decides what counts as a tool, so the three checks that used to each glob `*.ts` agree.
    """

    directory = tools_dir()
    if not directory.is_dir():
        return []
    return [
        path
        for path in sorted(directory.glob("*.ts"))
        if not DISABLED_RE.search(path.read_text(encoding="utf-8"))
    ]


def tool_names() -> list[str]:
    """Names of the tools in her surface, sorted."""

    return [path.stem for path in tool_sources()]


def docs_dir() -> Path:
    """Directory holding one markdown doc per tool (overridable for tests)."""

    import os

    override = os.environ.get("EMPIRE_TOOL_DOCS", "").strip()
    return Path(override) if override else DEFAULT_DOCS_DIR


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


def index() -> list[dict[str, Any]]:
    """All documented tools as {name, one_line, toolbelt} sorted by name."""

    directory = docs_dir()
    if not directory.is_dir():
        return []
    entries: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*.md")):
        fields = _front_matter(path.read_text(encoding="utf-8"))
        entries.append(
            {
                "name": fields.get("name") or path.stem,
                "one_line": fields.get("one_line", ""),
                "toolbelt": fields.get("toolbelt", ""),
            }
        )
    return entries


def doc(name: str, *, max_chars: int = MAX_DOC_CHARS) -> dict[str, Any]:
    """One tool's documentation, bounded so a lookup can never blow the prompt budget."""

    cleaned = str(name or "").strip()
    if not cleaned or "/" in cleaned or "\\" in cleaned or ".." in cleaned:
        return {"ok": False, "error": "invalid tool name", "name": cleaned}
    directory = docs_dir()
    path = directory / f"{cleaned}.md"
    if not path.is_file():
        available = [entry["name"] for entry in index()]
        return {
            "ok": False,
            "error": f"no documentation for {cleaned!r}",
            "name": cleaned,
            "documented_tools": available[:60],
        }
    text = path.read_text(encoding="utf-8")
    front = _front_matter(text)
    body = FRONT_MATTER_RE.sub("", text).strip()
    truncated = len(body) > max_chars
    return {
        "ok": True,
        "name": front.get("name") or cleaned,
        "toolbelt": front.get("toolbelt", ""),
        "one_line": front.get("one_line", ""),
        "doc": body[:max_chars] + ("\n\n[truncated — ask for a narrower aspect]" if truncated else ""),
        "truncated": truncated,
        "chars": len(body),
    }


def missing(names: list[str]) -> list[str]:
    """Tool names without documentation — the coverage check used by the budget test."""

    documented = {entry["name"] for entry in index()}
    return sorted({str(n).strip() for n in names if str(n).strip()} - documented)