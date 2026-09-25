r"""Prompt-budget ceiling (refactor plan R-01) + the R-03 reduction it enforces.

The measured floor before the user speaks used to be **~5,677 tokens** on the chars/3.8 basis
(instructions 3,897 + default-enabled tool schema prose 1,780). R-03 moved tool *detail* out of the
hot prompt into `config/eve-capabilities/tool-docs/` (fetched with the `tool_docs` tool), taking it to
**~4,486 tokens** (−21%). These ceilings encode that reduction, so growing the prompt back is a build
failure rather than a silent slowdown.

Run `.\scripts\measure-prompt-budget.py` for the full breakdown and `--baseline HEAD` for the delta.
"""

from __future__ import annotations

import unittest

from frontend.ollama_chat_profiles import SHARED_NUM_CTX
from pipeline import prompt_budget, tool_registry
from pipeline.prompt_budget import tokens

# Measured 2026-09-24 after R-03 (see docs/REFACTOR_PLAN.md section 3).
INSTRUCTION_CEILING_TOKENS = 3_700  # measured 3,435; was 3,897 before R-03
DEFAULT_SCHEMA_CEILING_TOKENS = 850  # measured 695; was 1,780 before R-03
FLOOR_CEILING_TOKENS = 4_400  # measured 4,130; was 5,677 before R-03
MIN_CONVERSATION_HEADROOM = 4_096
TOOLBELT_CATEGORY_CEILING = 30


class PromptBudgetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data = prompt_budget.measure()

    def test_instruction_files_exist_and_are_sized_sanely(self) -> None:
        for path in prompt_budget.INSTRUCTIONS:
            self.assertTrue(path.is_file(), f"instruction file missing: {path}")
            self.assertGreater(
                tokens(len(path.read_text(encoding="utf-8"))), 200, f"{path.name} looks truncated"
            )

    def test_instruction_weight_under_ceiling(self) -> None:
        self.assertLessEqual(
            self.data["instruction_tokens"],
            INSTRUCTION_CEILING_TOKENS,
            f"always-on instructions are ~{self.data['instruction_tokens']} tokens "
            f"(ceiling {INSTRUCTION_CEILING_TOKENS}); move detail into a skill or a tool doc",
        )

    def test_default_schema_weight_under_ceiling(self) -> None:
        """R-03's measured reduction: the schemas of tools enabled by default carry cues, not prose."""

        self.assertLessEqual(
            self.data["default_schema_tokens"],
            DEFAULT_SCHEMA_CEILING_TOKENS,
            f"default-enabled schema prose is ~{self.data['default_schema_tokens']} tokens "
            f"(ceiling {DEFAULT_SCHEMA_CEILING_TOKENS}); put detail in the tool doc, keep the cue",
        )

    def test_floor_leaves_conversation_headroom(self) -> None:
        floor = self.data["floor_tokens"]
        self.assertLessEqual(floor, FLOOR_CEILING_TOKENS)
        headroom = SHARED_NUM_CTX - floor
        self.assertGreaterEqual(
            headroom,
            MIN_CONVERSATION_HEADROOM,
            f"prompt floor ~{floor} of {SHARED_NUM_CTX} leaves only {headroom} tokens for the "
            "conversation; retire tools or trim instructions (refactor plan R-03)",
        )

    def test_enabled_tool_count_is_bounded(self) -> None:
        toolbelt = prompt_budget.ROOT / "agents" / "empire-task-agent" / "agent" / "lib" / "toolbelt.ts"
        categories = [
            line.strip().strip(',').strip('"')
            for line in toolbelt.read_text(encoding="utf-8").splitlines()
            if line.strip().startswith('"') and line.strip().endswith('",')
        ]
        self.assertGreaterEqual(len(categories), 2, "toolbelt categories not parsed")
        self.assertLessEqual(
            len(categories),
            TOOLBELT_CATEGORY_CEILING,
            f"{len(categories)} Toolbelt categories — above {TOOLBELT_CATEGORY_CEILING} the surface "
            "needs triage (R-03)",
        )

    def test_every_default_enabled_tool_has_a_registry_doc(self) -> None:
        """The R-03 trade: prose leaves the prompt only if the registry actually holds it."""

        names = []
        for path in tool_registry.tool_sources():
            text = path.read_text(encoding="utf-8")
            gated = "isCapabilityActive" in text or "isCategoryEnabled" in text
            if not gated or '"wiki_local"' in text:
                names.append(path.stem)
        # 30 is the measured always-registered set once the nine `disableTool()` files
        # (`agent`, `bash`, `ask_question`, `glob`, `grep`, `read_file`, `write_file`,
        # `web_search`, `web_fetch`) stopped counting as part of her surface (2026-09-24).
        self.assertGreaterEqual(len(names), 30, "expected the default-enabled set to be substantial")
        undocumented = tool_registry.missing(names)
        self.assertEqual(
            undocumented,
            [],
            f"these enabled tools have no documentation in {tool_registry.docs_dir()}: {undocumented}",
        )


if __name__ == "__main__":
    unittest.main()
