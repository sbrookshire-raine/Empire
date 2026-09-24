"""Prompt-budget ceiling (refactor plan R-01).

The measured floor before the user speaks is **~11.1k of a 16,384 window**: always-on instructions
(`eve_instructions.md` + `empire-routing.md`, composed by `agent/instructions.ts`) plus the enabled
tool schemas. That leaves ~5k for the conversation and tool results — which is why a repeat-search
loop or a fat evidence card used to break turns.

This test turns that measurement into an invariant: instruction growth and tool-surface growth now
fail the build instead of showing up later as "the model ignores its rules".

Numbers are deliberately explicit constants. When a change legitimately raises the floor, update
them here in the same commit and record the new measurement (see docs/VOICE_PRESENCE.md).
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

from frontend.ollama_chat_profiles import SHARED_NUM_CTX

ROOT = Path(__file__).resolve().parents[1]
# Exactly what instructions.ts loadSystemPrompt() always includes.
INSTRUCTION_FILES = (
    ROOT / "eve_instructions.md",
    ROOT / "agents" / "empire-task-agent" / "agent" / "empire-routing.md",
)
# chars -> tokens heuristic used for the estimates in AGENTS.md / VOICE_PRESENCE.md.
CHARS_PER_TOKEN = 3.8
# Measured 2026-09-24 (AGENTS.md troubleshooting section), for the ~32 enabled tools.
SCHEMA_BUDGET_TOKENS = 5_300
SCHEMA_CEILING_TOKENS = 6_000
INSTRUCTION_CEILING_TOKENS = 6_500
# num_ctx minus the floor must leave real room for the conversation + tool results.
MIN_CONVERSATION_HEADROOM = 4_096


def _estimate_tokens(path: Path) -> int:
    return int(len(path.read_text(encoding="utf-8")) / CHARS_PER_TOKEN)


class PromptBudgetTests(unittest.TestCase):
    def test_instruction_files_exist_and_are_sized_sanely(self) -> None:
        total = 0
        for path in INSTRUCTION_FILES:
            self.assertTrue(path.is_file(), f"instruction file missing: {path}")
            tokens = _estimate_tokens(path)
            self.assertGreater(tokens, 200, f"{path.name} looks truncated ({tokens} tokens)")
            total += tokens
        self.assertLessEqual(
            total,
            INSTRUCTION_CEILING_TOKENS,
            f"always-on instructions are ~{total} tokens (ceiling {INSTRUCTION_CEILING_TOKENS}); "
            "move detail into a skill or a subsystem doc instead of growing the system prompt",
        )

    def test_schema_budget_constant_is_honest(self) -> None:
        self.assertLessEqual(SCHEMA_BUDGET_TOKENS, SCHEMA_CEILING_TOKENS)

    def test_floor_leaves_conversation_headroom(self) -> None:
        instructions = sum(_estimate_tokens(path) for path in INSTRUCTION_FILES)
        floor = instructions + SCHEMA_BUDGET_TOKENS
        headroom = SHARED_NUM_CTX - floor
        self.assertGreaterEqual(
            headroom,
            MIN_CONVERSATION_HEADROOM,
            f"prompt floor ~{floor} of {SHARED_NUM_CTX} leaves only {headroom} tokens for the "
            "conversation; retire tools or trim instructions (refactor plan R-03/R-01)",
        )

    def test_enabled_tool_count_is_bounded(self) -> None:
        """Toolbelt categories stay a curated list; the prompt cost scales with this number."""

        toolbelt = ROOT / "agents" / "empire-task-agent" / "agent" / "lib" / "toolbelt.ts"
        text = toolbelt.read_text(encoding="utf-8")
        categories = re.findall(r'^\s*"([a-z_]+)",\s*$', text, flags=re.MULTILINE)
        self.assertGreaterEqual(len(categories), 2, "toolbelt categories not parsed")
        self.assertLessEqual(
            len(categories),
            30,
            f"{len(categories)} Toolbelt categories — above 30 the surface needs triage (R-03)",
        )


if __name__ == "__main__":
    unittest.main()