"""Prompt-budget measurement (refactor plan R-01/R-03).

One source of truth for "what does the model pay for before the user speaks": the always-on
instruction files and the tool-schema prose of the default-enabled Toolbelt set. Used by
`scripts/measure-prompt-budget.py` (human output) and `tests/test_prompt_budget.py` (ceilings).

Estimates are chars / 3.8 — the same heuristic as AGENTS.md — so absolute values are approximate but
comparisons are consistent. Authoritative totals come from Ollama's `prompt_tokens` on a real turn.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import Any

from frontend.ollama_chat_profiles import SHARED_NUM_CTX

ROOT = Path(__file__).resolve().parents[1]
CHARS_PER_TOKEN = 3.8
INSTRUCTIONS = (
    ROOT / "eve_instructions.md",
    ROOT / "agents" / "empire-task-agent" / "agent" / "empire-routing.md",
)
TOOLS = ROOT / "agents" / "empire-task-agent" / "agent" / "tools"

DESC_RE = re.compile(r'description:\s*\n?\s*((?:"[^"]*"(?:\s*\+\s*)?)+)', re.DOTALL)
STR_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')
DESCRIBE_RE = re.compile(r'\.describe\(\s*((?:"[^"]*"(?:\s*\+\s*)?)+)\s*\)', re.DOTALL)


def tokens(chars: int) -> int:
    """chars -> approximate tokens (kept in one place so every report uses one basis)."""

    return int(chars / CHARS_PER_TOKEN)


def schema_chars(text: str) -> tuple[int, int]:
    """(description chars, parameter-description chars) in one tool source."""

    desc = DESC_RE.search(text)
    main = len("".join(STR_RE.findall(desc.group(1)))) if desc else 0
    params = sum(len("".join(STR_RE.findall(m.group(1)))) for m in DESCRIBE_RE.finditer(text))
    return main, params


def _tool_files() -> list[Path]:
    return sorted(TOOLS.glob("*.ts"))


def _classify(text: str) -> str:
    gated = "isCapabilityActive" in text or "isCategoryEnabled" in text
    if not gated:
        return "always"
    return "wiki_local" if '"wiki_local"' in text else "gated"


def measure() -> dict[str, Any]:
    """Component breakdown for the working tree."""

    instructions = {path.name: len(path.read_text(encoding="utf-8")) for path in INSTRUCTIONS}
    return _summarise(instructions, {path: path.read_text(encoding="utf-8") for path in _tool_files()})


def _git_show(rev: str, path: Path) -> str:
    relative = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "show", f"{rev}:{relative}"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return result.stdout if result.returncode == 0 else ""


def measure_rev(rev: str) -> dict[str, Any]:
    """Same measurement against a git revision, so before/after is reproducible."""

    instructions = {path.name: len(_git_show(rev, path)) for path in INSTRUCTIONS}
    sources = {path: _git_show(rev, path) for path in _tool_files()}
    return _summarise(instructions, {p: t for p, t in sources.items() if t})


def _summarise(instructions: dict[str, int], sources: dict[Path, str]) -> dict[str, Any]:
    instruction_chars = sum(instructions.values())
    buckets = {"always": 0, "wiki_local": 0}
    counts = {"always": 0, "wiki_local": 0, "gated": 0}
    for path, text in sources.items():
        kind = _classify(text)
        counts[kind] += 1
        if kind in buckets:
            main, params = schema_chars(text)
            buckets[kind] += main + params

    default_schema = buckets["always"] + buckets["wiki_local"]
    floor = instruction_chars + default_schema
    return {
        "instructions": instructions,
        "instruction_chars": instruction_chars,
        "instruction_tokens": tokens(instruction_chars),
        "always_tools": counts["always"],
        "always_schema_tokens": tokens(buckets["always"]),
        "default_gated_tools": counts["wiki_local"],
        "default_gated_schema_tokens": tokens(buckets["wiki_local"]),
        "default_schema_tokens": tokens(default_schema),
        "floor_tokens": tokens(floor),
        "num_ctx": SHARED_NUM_CTX,
        "headroom_tokens": SHARED_NUM_CTX - tokens(floor),
    }