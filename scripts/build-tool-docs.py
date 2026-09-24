"""Generate config/eve-capabilities/tool-docs/*.md from the agent tool sources (R-03).

The docs are *harvested*, never hand-written, so moving prose out of the hot prompt cannot lose it:
each doc carries the tool's current description verbatim plus its parameter names and parameter
descriptions, and records which Toolbelt category registers it.

Run:  .\\venv\\Scripts\\python.exe scripts\\build-tool-docs.py
      .\\venv\\Scripts\\python.exe scripts\\build-tool-docs.py --check   (fail if docs are stale)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pipeline.tool_registry import docs_dir  # noqa: E402

TOOLS = ROOT / "agents" / "empire-task-agent" / "agent" / "tools"
DESC_RE = re.compile(r'description:\s*\n?\s*((?:"[^"]*"(?:\s*\+\s*)?)+)', re.DOTALL)
STR_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')
PARAM_RE = re.compile(
    r"^\s{2,}([a-zA-Z_][a-zA-Z0-9_]*):\s*\n?\s*([a-zA-Z_][a-zA-Z0-9_.]*)\(", re.MULTILINE
)
PARAM_DESC_RE = re.compile(
    r"([a-zA-Z_][a-zA-Z0-9_]*)([\s\S]{0,400}?)\.describe\(\s*((?:\"[^\"]*\"(?:\s*\+\s*)?)+)",
    re.DOTALL,
)
SCHEMA_KEY_RE = re.compile(r"^ {2,}([a-zA-Z_][a-zA-Z0-9_]*)\s*:", re.MULTILINE)
DESCRIBE_RE = re.compile(r"\.describe\(\s*((?:\"[^\"]*\"(?:\s*\+\s*)?)+)", re.DOTALL)


def parse_params(schema: str) -> list[tuple[str, str]]:
    """Parameter name -> description, sliced between object keys so the name is the key itself."""

    keys = list(SCHEMA_KEY_RE.finditer(schema))
    params: list[tuple[str, str]] = []
    seen: set[str] = set()
    for position, match in enumerate(keys):
        name = match.group(1)
        if name in seen:
            continue
        end = keys[position + 1].start() if position + 1 < len(keys) else len(schema)
        block = schema[match.end() : end]
        described = DESCRIBE_RE.search(block)
        seen.add(name)
        params.append((name, _joined_strings(described.group(1)) if described else ""))
    return params


def _joined_strings(block: str) -> str:
    return "".join(STR_RE.findall(block)).replace("\\n", " ").strip()


def parse_tool(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = DESC_RE.search(text)
    description = _joined_strings(match.group(1)) if match else ""
    schema = text.split("inputSchema", 1)[1] if "inputSchema" in text else ""
    params = parse_params(schema)
    gated = "isCapabilityActive" in text or "isCategoryEnabled" in text
    categories = re.findall(r'isCapabilityActive\(\s*"([a-z_]+)"', text)
    return {
        "name": path.stem,
        "description": description,
        "params": params,
        "toolbelt": ",".join(categories) if gated else "always",
    }


def one_line(description: str, *, limit: int = 110) -> str:
    text = " ".join(description.split())
    head = text.split(". ")[0].strip().rstrip(".")
    return (head[: limit - 1] + "…") if len(head) > limit else head


def render(tool: dict) -> str:
    lines = [
        "---",
        f"name: {tool['name']}",
        f"toolbelt: {tool['toolbelt']}",
        f"one_line: {one_line(tool['description']) or 'See description below.'}",
        "---",
        "",
        "## Description (verbatim from the tool schema, pre-R-03)",
        "",
        tool["description"] or "(no description in the schema)",
        "",
        "## Parameters",
        "",
    ]
    if tool["params"]:
        for name, desc in tool["params"]:
            lines.append(f"- `{name}` — {desc or '(no description)'}")
    else:
        lines.append("- (no parameters)")
    lines.extend(
        [
            "",
            "## Usage",
            "",
            f"Registered by the Toolbelt category `{tool['toolbelt']}`. The model sees the name, the",
            "one-line cue and the parameter names in its schema; this document is the deep syntax it",
            "can fetch with `tool_docs` when a call needs more than the cue.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate tool documentation from tool sources.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="report tools with no documentation (coverage), change nothing",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite existing docs (only when a tool's schema text is still the long form)",
    )
    args = parser.parse_args()

    target = docs_dir()
    target.mkdir(parents=True, exist_ok=True)
    missing: list[str] = []
    written = 0
    for path in sorted(TOOLS.glob("*.ts")):
        tool = parse_tool(path)
        doc_path = target / f"{tool['name']}.md"
        if not doc_path.is_file():
            missing.append(tool["name"])
        if args.check:
            continue
        if doc_path.is_file() and not args.force:
            continue  # create-only: the docs hold the pre-R-03 long form, the schema holds the cue
        doc_path.write_text(render(tool), encoding="utf-8")
        written += 1

    if args.check:
        if missing:
            print(f"UNDOCUMENTED tools: {len(missing)}")
            for name in missing[:20]:
                print("  ", name)
            return 1
        print(f"docs cover all {len(list(target.glob('*.md')))} documented tools")
        return 0

    print(f"wrote {written} tool docs to {target} ({len(missing)} were missing)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())