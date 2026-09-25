"""Playbook coverage: every tool she can call, and every skill file, has worked examples.

The Architect's ask (2026-09-24): *"I would like her to have something to use that is tried and true
for every skill she has access to — it's literally her playbook."* `pipeline.playbook.coverage()` is
that measurement; this file fails the build when it stops being true, both for fixture shapes and
for the shipped content.
"""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import playbook

TOOL_DOC = """---
name: alpha_tool
toolbelt: always
one_line: Alpha.
---

## Description

Alpha tool.
"""

AREA = """---
area: example-area
one_line: One line about the area.
tools: alpha_tool
skills: example-skill
---

# Example area

## A capability
Use when: testing.

- **Ask:** "one?" -> **Do:** `alpha_tool()` -> **Get:** a thing.
- **Ask:** "two?" -> **Do:** `alpha_tool()` -> **Get:** another thing.
- **Ask:** "three?" -> **Do:** `alpha_tool()` -> **Get:** a third thing.
"""

THIN_BODY = """---
area: example-area
one_line: One line about the area.
tools: alpha_tool
skills: example-skill
---

# Example area

## A capability
Use when: testing.
"""


class CoverageFixtureTests(unittest.TestCase):
    """Each way coverage can break is reported by name."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        root = Path(self._tmp.name)
        self.play = root / "playbook"
        self.docs = root / "tool-docs"
        self.skills = root / "skills"
        for directory in (self.play, self.docs, self.skills):
            directory.mkdir()
        (self.docs / "alpha_tool.md").write_text(TOOL_DOC, encoding="utf-8")
        (self.skills / "example-skill.md").write_text("skill body", encoding="utf-8")
        (self.play / "example-area.md").write_text(AREA, encoding="utf-8")
        for patcher in (
            patch.dict(os.environ, {"EMPIRE_PLAYBOOK": str(self.play)}),
            patch.dict(os.environ, {"EMPIRE_TOOL_DOCS": str(self.docs)}),
            patch.dict(os.environ, {"EMPIRE_SKILLS": str(self.skills)}),
        ):
            patcher.start()
            self.addCleanup(patcher.stop)

    def rewrite_area(self, text: str) -> None:
        (self.play / "example-area.md").write_text(text, encoding="utf-8")

    def test_full_coverage_is_ok(self) -> None:
        result = playbook.coverage()
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["tool_docs"], 1)
        self.assertEqual(result["skill_files"], 1)

    def test_missing_tool_is_reported(self) -> None:
        """A registry tool no area claims → no worked example for a tool she can call."""

        (self.docs / "beta_tool.md").write_text(
            TOOL_DOC.replace("alpha_tool", "beta_tool"), encoding="utf-8"
        )
        result = playbook.coverage()
        self.assertFalse(result["ok"])
        self.assertEqual(result["missing_tools"], ["beta_tool"])

    def test_ghost_tool_is_reported(self) -> None:
        """An area promising a tool that is not in the registry → a route into nothing."""

        self.rewrite_area(AREA.replace("tools: alpha_tool", "tools: alpha_tool, never_a_tool"))
        result = playbook.coverage()
        self.assertFalse(result["ok"])
        self.assertEqual(result["ghost_tools"], ["never_a_tool"])


    def test_missing_skill_is_reported(self) -> None:
        """An agent/skills file no area claims → a skill with no worked example (E-29)."""

        (self.skills / "other-skill.md").write_text("skill body", encoding="utf-8")
        result = playbook.coverage()
        self.assertFalse(result["ok"])
        self.assertEqual(result["missing_skills"], ["other-skill"])

    def test_ghost_skill_is_reported(self) -> None:
        """A claimed skills entry with no file behind it."""

        self.rewrite_area(AREA.replace("skills: example-skill", "skills: ghost-skill"))
        result = playbook.coverage()
        self.assertFalse(result["ok"])
        self.assertEqual(result["ghost_skills"], ["ghost-skill"])


class ShippedPlaybookCoverageTests(unittest.TestCase):
    """The shipped tree: her playbook is complete, and stays complete."""

    def test_every_registry_tool_has_a_worked_example(self) -> None:
        result = playbook.coverage()
        self.assertEqual(
            result["missing_tools"],
            [],
            "these callable tools have no playbook area claiming them",
        )
        self.assertEqual(
            result["unused_tools"],
            [],
            "these tools are claimed but never shown in an example",
        )

    def test_every_skill_file_has_a_worked_home(self) -> None:
        result = playbook.coverage()
        self.assertEqual(
            result["missing_skills"],
            [],
            "these agent/skills files have no playbook area claiming them (E-29)",
        )
        self.assertEqual(result["ghost_skills"], [], "claimed skills with no file behind them")

    def test_no_route_points_at_a_tool_that_does_not_exist(self) -> None:
        """`load_skill_manifest` was a Python helper, not a tool — two routing lines and a
        playbook example still told her to call it (found 2026-09-24)."""

        self.assertEqual(playbook.coverage()["ghost_tools"], [])

    def test_the_shipped_playbook_passes_coverage(self) -> None:
        result = playbook.coverage()
        self.assertTrue(result["ok"], result)
        self.assertGreaterEqual(result["tool_docs"], 70, "expected a real tool registry")
        self.assertGreaterEqual(result["skill_files"], 30, "expected the authored skill set")


if __name__ == "__main__":
    unittest.main()

    def test_unused_tool_is_reported(self) -> None:
        """Claimed, but shown in no example anywhere → the claim is decoration."""

        self.rewrite_area(THIN_BODY)
        result = playbook.coverage()
        self.assertFalse(result["ok"])
        self.assertEqual(result["unused_tools"], ["alpha_tool"])
