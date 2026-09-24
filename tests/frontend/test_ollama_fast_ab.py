"""Unit tests for the Fast-mode A/B switch (frontend.ollama_fast_ab)."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from frontend import ollama_fast_ab
from frontend.ollama_chat_profiles import CHAT_MODES, SHARED_NUM_CTX


class FastAbTests(unittest.TestCase):
    def _config_dir(self) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        return Path(tmp.name)

    def test_default_is_variant_a(self) -> None:
        with patch.dict("os.environ", {"LOCALAPPDATA": str(self._config_dir())}):
            cfg = ollama_fast_ab.load_fast_ab()
        self.assertEqual(cfg["variant"], "a")
        self.assertEqual(cfg["active_model"], CHAT_MODES["fast"]["model"])
        self.assertEqual(cfg["num_ctx"], SHARED_NUM_CTX)

    def test_variant_b_resolves_to_the_alternate(self) -> None:
        local = self._config_dir()
        (local / "EMPIRE").mkdir(parents=True, exist_ok=True)
        (local / "EMPIRE" / "ollama-fast-ab.json").write_text(
            json.dumps({"variant": "b", "b_model": "empire-fast:7b"}), encoding="utf-8"
        )
        with patch.dict("os.environ", {"LOCALAPPDATA": str(local)}):
            self.assertEqual(ollama_fast_ab.resolve_fast_model(CHAT_MODES["fast"]["model"]),
                             "empire-fast:7b")

    def test_variant_a_does_not_keep_the_alternate_active(self) -> None:
        """Regression: after a variant-b run the stored Fast model is the alternate, and the old
        resolver returned it unchanged — so switching back to `a` silently stayed on `b`."""

        local = self._config_dir()
        (local / "EMPIRE").mkdir(parents=True, exist_ok=True)
        (local / "EMPIRE" / "ollama-fast-ab.json").write_text(
            json.dumps({"variant": "a", "b_model": "empire-fast:7b"}), encoding="utf-8"
        )
        with patch.dict("os.environ", {"LOCALAPPDATA": str(local)}):
            self.assertEqual(
                ollama_fast_ab.resolve_fast_model("empire-fast:7b"),
                CHAT_MODES["fast"]["model"],
            )

    def test_save_rejects_invalid_variant(self) -> None:
        with patch.dict("os.environ", {"LOCALAPPDATA": str(self._config_dir())}):
            self.assertFalse(ollama_fast_ab.save_fast_ab(variant="c")["ok"])

    def test_save_rejects_invalid_model_id(self) -> None:
        with patch.dict("os.environ", {"LOCALAPPDATA": str(self._config_dir())}):
            self.assertFalse(ollama_fast_ab.save_fast_ab(b_model="bad model!")["ok"])


if __name__ == "__main__":
    unittest.main()