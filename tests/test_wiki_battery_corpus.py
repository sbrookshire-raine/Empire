"""The wiki extract battery must not report a partial corpus as a failure.

The green gate used to hardcode `I:\\EMPIRE_DATA\\...` as the precondition
for the wiki extract battery. The runtime resolves the corpus differently
(override, then I:, then D:), so on a machine where the T7 is not mounted
but the corpus lives on D:, the gate SKIPPED the battery entirely while the
runtime served wiki lookups from the very same corpus. A green gate that
skipped a real check proved nothing about the wiki limb.

Now that the battery actually runs, it has to be honest about the corpus it
ran against: a case whose page is not in the local corpus cannot be a
regression signal, and it must be reported as a SKIP with the reason - not
as a FAIL, and not silently.
"""

from __future__ import annotations

import importlib.util
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
GATE = ROOT / "scripts" / "mechanic-green.ps1"
HELPER = ROOT / "scripts" / "wiki-index-path.py"
BATTERY = ROOT / "scripts" / "wiki_extract_battery.py"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GateResolvesTheCorpusThroughTheRuntimeTests(unittest.TestCase):
    def test_gate_does_not_hardcode_a_drive_letter_for_the_wiki_battery(self) -> None:
        source = GATE.read_text(encoding="utf-8")
        self.assertNotIn("I:\\EMPIRE_DATA\\wiki-reports\\2026\\title-index.sqlite", source)

    def test_gate_asks_the_runtime_where_the_corpus_is(self) -> None:
        source = GATE.read_text(encoding="utf-8")
        self.assertIn("wiki-index-path.py", source)

    def test_gate_still_says_what_to_do_when_there_is_no_corpus(self) -> None:
        source = GATE.read_text(encoding="utf-8")
        self.assertIn("SKIP wiki extract battery", source)


class WikiIndexPathHelperTests(unittest.TestCase):
    def test_helper_prints_the_resolved_index(self) -> None:
        helper = load(HELPER, "wiki_index_path_helper")
        with tempfile.TemporaryDirectory() as temporary:
            index = Path(temporary) / "title-index.sqlite"
            index.write_bytes(b"")
            with patch.dict(os.environ, {"EMPIRE_WIKI_TITLE_INDEX": str(index)}):
                self.assertEqual(helper.resolve("2026"), index)
                self.assertEqual(helper.main(["2026"]), 0)

    def test_helper_prints_nothing_when_there_is_no_corpus(self) -> None:
        helper = load(HELPER, "wiki_index_path_helper_missing")
        with tempfile.TemporaryDirectory() as temporary:
            missing = Path(temporary) / "nope.sqlite"
            with patch.dict(os.environ, {"EMPIRE_WIKI_TITLE_INDEX": str(missing)}):
                self.assertIsNone(helper.resolve("2026"))
                self.assertEqual(helper.main(["2026"]), 1)


class BatteryCorpusAwarenessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.battery = load(BATTERY, "wiki_extract_battery_module")

    def _miss_result(self, status: str = "miss"):
        class _Result:
            def __init__(self, status: str) -> None:
                self.status = status
                self.hit = None

        return _Result(status)

    def _hit_result(self):
        class _Hit:
            title = "Some Page"

        class _Result:
            def __init__(self) -> None:
                self.status = "hit"
                self.hit = _Hit()

        return _Result()

    def test_a_case_whose_page_is_absent_is_skipped_not_failed(self) -> None:
        def resolve(subject: str, year: str, user_question: str = ""):
            # Only "Nintendo Switch" is missing from the partial corpus.
            return self._miss_result() if subject == "Nintendo Switch" else self._hit_result()

        with patch("pipeline.wiki_title_dns.resolve", side_effect=resolve):
            skipped = self.battery.corpus_skips(self.battery.CASES)
        self.assertIn("G1", skipped)
        self.assertIn("G6", skipped)
        self.assertNotIn("G2", skipped)
        self.assertNotIn("G4", skipped)

    def test_a_case_that_expects_a_miss_always_runs(self) -> None:
        """The miss IS the assertion, so the corpus is not a precondition."""

        with patch("pipeline.wiki_title_dns.resolve", return_value=self._miss_result()):
            skipped = self.battery.corpus_skips(self.battery.CASES)
        self.assertNotIn("R2", skipped)

    def test_a_probe_failure_never_skips_a_case(self) -> None:
        with patch("pipeline.wiki_title_dns.resolve", side_effect=RuntimeError("boom")):
            skipped = self.battery.corpus_skips(self.battery.CASES)
        self.assertEqual(skipped, {})

    def test_the_summary_reports_the_skip_count_and_the_corpus(self) -> None:
        source = BATTERY.read_text(encoding="utf-8")
        self.assertIn("case(s) SKIPPED", source)
        self.assertIn("not in this corpus", source)
        self.assertIn("require_full_corpus", source)

    def test_strict_mode_makes_a_skip_fatal(self) -> None:
        source = BATTERY.read_text(encoding="utf-8")
        self.assertIn("--require-full-corpus", source)
        self.assertIn("if args.require_full_corpus and cli_skipped:", source)
