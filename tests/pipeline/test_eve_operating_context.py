from __future__ import annotations

import unittest

from pipeline import eve_operating_context


class EveOperatingContextTests(unittest.TestCase):
    def test_render_includes_playbook_and_workflow(self) -> None:
        text = eve_operating_context.render_operating_context_md()
        self.assertIn("playbook", text.casefold())
        self.assertIn("tool_docs", text)
        self.assertIn("EMPIRE_RESOURCE_PULSE", text)


if __name__ == "__main__":
    unittest.main()
