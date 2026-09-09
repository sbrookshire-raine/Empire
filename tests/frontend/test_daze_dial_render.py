"""DAZE dial contract tests — JS renders sectors imperatively (Alpine SVG bind is unreliable)."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class DazeDialContractTests(unittest.TestCase):
    def test_daze_js_uses_imperative_sector_render(self) -> None:
        source = (ROOT / "frontend" / "daze.js").read_text(encoding="utf-8")
        self.assertIn("function sectorPath(", source)
        self.assertIn("renderDial()", source)
        self.assertIn("paintSectors(", source)
        self.assertIn("createElementNS", source)

    def test_daze_html_has_sector_mount_points(self) -> None:
        html = (ROOT / "frontend" / "daze.html").read_text(encoding="utf-8")
        source = (ROOT / "frontend" / "daze.js").read_text(encoding="utf-8")
        self.assertIn('id="daze-planned-sectors"', html)
        self.assertIn('id="daze-actual-sectors"', html)
        self.assertIn('id="daze-single-sectors"', html)
        self.assertIn('id="daze-hour-ticks"', html)
        self.assertIn("tool-dock-carousel", html)
        self.assertIn("dockScreen", source)
        self.assertIn("notifyDockScreen", source)
        self.assertIn("paintHourTicks", source)
        self.assertNotIn(":d=\"arc.d\"", html)


if __name__ == "__main__":
    unittest.main()
