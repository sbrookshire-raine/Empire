from __future__ import annotations

import unittest
from unittest.mock import patch

from pipeline import capability_verification, tool_registry


class CapabilityVerificationTests(unittest.TestCase):
    def test_run_offline_returns_checks(self) -> None:
        checks = capability_verification.run_offline()
        self.assertGreater(len(checks), 5)
        names = {c.get("name") for c in checks}
        self.assertIn("playbook_coverage", names)
        self.assertTrue(any(str(n).startswith("mcp:") for n in names))

    def test_run_offline_includes_the_always_on_surface_check(self) -> None:
        names = {c.get("name") for c in capability_verification.run_offline()}
        self.assertIn("always_on_tools", names)

    def test_always_on_tools_check_passes_on_the_real_surface(self) -> None:
        check = capability_verification.probe_always_on_tools()
        self.assertTrue(check["ok"], check.get("detail"))

    def test_render_markdown_includes_eve_core(self) -> None:
        md = capability_verification.render_markdown(
            [{"name": "t", "ok": True, "tool": "x", "tier": "offline"}],
            live_ran=False,
        )
        self.assertIn("eve_core", md)
        self.assertIn("cognee_recall", md)

    def test_render_markdown_names_the_always_on_tools(self) -> None:
        """The report is what tells Eve what she can call.

        It used to list only the tools a check happened to touch, so
        `cognee_recall` — always registered, always available — never
        appeared in it.
        """

        md = capability_verification.render_markdown(
            [{"name": "t", "ok": True, "tool": "x", "tier": "offline"}],
            live_ran=False,
        )
        for name in tool_registry.always_on_tools():
            self.assertIn(f"`{name}`", md, f"{name} missing from the capabilities report")

    def test_render_markdown_says_when_the_live_tier_did_not_run(self) -> None:
        """An offline report must not read as a live one."""

        md = capability_verification.render_markdown(
            [{"name": "t", "ok": True, "tool": "x", "tier": "offline"}],
            live_ran=False,
        )
        self.assertIn("Live stack checks run: **False**", md)
        self.assertIn("Not run", md)

    def test_render_markdown_lists_the_live_tier_when_it_ran(self) -> None:
        md = capability_verification.render_markdown(
            [
                {"name": "off", "ok": True, "tool": "x", "tier": "offline"},
                {"name": "live_one", "ok": True, "tool": "y", "tier": "live", "detail": "ok"},
            ],
            live_ran=True,
        )
        self.assertIn("Live stack checks run: **True**", md)
        self.assertIn("live_one", md)
        self.assertNotIn("_Not run._", md)

    def test_render_markdown_is_not_degenerate(self) -> None:
        """A report that names no tools is not a report.

        The failure this guards against is silent: a report with an empty
        always-on section still "passes" (it is written, it is valid), so
        only an explicit assertion catches it.
        """

        md = capability_verification.render_markdown(
            [{"name": "t", "ok": True, "tool": "x", "tier": "offline"}],
            live_ran=False,
        )
        self.assertIn("## Always-on tools", md)
        self.assertIn("cognee_recall", md)
        self.assertNotIn("_(none detected", md)
        self.assertIn("## Live stack checks", md)


if __name__ == "__main__":
    unittest.main()
