"""Tests for Eve chat mode sampling profiles."""

from __future__ import annotations

import unittest

from frontend.ollama_chat_profiles import (
    CHAT_MODES,
    GLOBAL_CHAT_OPTIONS,
    SHARED_NUM_CTX,
    chat_options_for_mode,
    resolve_mode_for_installed,
)


class OllamaChatProfileTests(unittest.TestCase):
    def test_shared_top_p_default(self) -> None:
        self.assertEqual(GLOBAL_CHAT_OPTIONS["top_p"], 0.90)

    def test_fast_mode_strict_tools(self) -> None:
        options = chat_options_for_mode("fast")
        self.assertEqual(options["num_ctx"], SHARED_NUM_CTX)
        self.assertEqual(options["temperature"], 0.2)

    def test_deep_mode_creative(self) -> None:
        options = chat_options_for_mode("deep")
        self.assertEqual(options["num_ctx"], SHARED_NUM_CTX)
        self.assertEqual(options["temperature"], 0.7)

    def test_librarian_mode_balanced(self) -> None:
        options = chat_options_for_mode("librarian")
        self.assertEqual(options["num_ctx"], SHARED_NUM_CTX)
        self.assertEqual(options["temperature"], 0.4)

    def test_all_modes_share_vram_safe_context(self) -> None:
        for mode in CHAT_MODES.values():
            self.assertEqual(mode["num_ctx"], 8_192)

    def test_resolve_installed_model_alias(self) -> None:
        installed = {
            "richardyoung/qwen2.5-14b-instruct-abliterated:latest",
            "qwen2.5:32b",
        }
        mode, model = resolve_mode_for_installed("fast", installed)
        self.assertEqual(mode["id"], "fast")
        self.assertEqual(
            model,
            "richardyoung/qwen2.5-14b-instruct-abliterated:latest",
        )

    def test_all_modes_have_models(self) -> None:
        self.assertEqual(set(CHAT_MODES), {"fast", "deep", "librarian"})


if __name__ == "__main__":
    unittest.main()
