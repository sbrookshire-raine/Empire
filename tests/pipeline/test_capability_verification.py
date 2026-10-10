from __future__ import annotations

import unittest
from unittest.mock import patch

from pipeline import capability_verification


class CapabilityVerificationTests(unittest.TestCase):
    def test_run_offline_returns_checks(self) -> None:
        checks = capability_verification.run_offline()
        self.assertGreater(len(checks), 5)
        names = {c.get("name") for c in checks}
        self.assertIn("playbook_coverage", names)
        self.assertTrue(any(str(n).startswith("mcp:") for n in names))

    def test_render_markdown_includes_eve_core(self) -> None:
        md = capability_verification.render_markdown(
            [{"name": "t", "ok": True, "tool": "x", "tier": "offline"}],
            live_ran=False,
        )
        self.assertIn("eve_core", md)
        self.assertIn("cognee_recall", md)


if __name__ == "__main__":
    unittest.main()
