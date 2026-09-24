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
        # Must match SHARED_NUM_CTX in agents/empire-task-agent/agent/lib/ollama-config.ts and the
        # baked num_ctx in config/ollama/Modelfile.* (AGENTS.md: they must not drift).
        for mode in CHAT_MODES.values():
            self.assertEqual(mode["num_ctx"], 16_384)
        self.assertEqual(SHARED_NUM_CTX, 16_384)

    def test_family_fallback_is_deterministic(self) -> None:
        """Regression: the family fallback iterated an unordered set, so Fast could resolve to
        `qwen2.5:32b` (a Deep alias) depending on Python's hash seed."""

        installed = {"qwen2.5:14b-instruct", "qwen2.5:32b"}
        for _ in range(25):
            mode, model = resolve_mode_for_installed("fast", installed)
            self.assertEqual(mode["id"], "fast")
            self.assertEqual(model, "qwen2.5:14b-instruct")

    def test_resolve_installed_model_alias(self) -> None:
        installed = {
            "qwen2.5:14b-instruct",
            "qwen2.5:32b",
        }
        mode, model = resolve_mode_for_installed("fast", installed)
        self.assertEqual(mode["id"], "fast")
        # Fast's canonical model changed to the EMPIRE-owned `empire-fast:14b` (baked
        # num_ctx/num_predict); when only the upstream id is installed the alias resolves to it.
        self.assertIn(model, {"empire-fast:14b", "qwen2.5:14b-instruct"})

    def test_all_modes_have_models(self) -> None:
        self.assertEqual(set(CHAT_MODES), {"fast", "deep", "librarian"})

    def test_deep_prefers_qwen27_when_installed(self) -> None:
        installed = {
            "qwen2.5:14b-instruct",
            "logicbeat/qwen3.8-27B_GSQ_RCO:latest",
        }
        mode, model = resolve_mode_for_installed("deep", installed)
        self.assertEqual(mode["id"], "deep")
        self.assertIn("27B", model)

    def test_deep_falls_back_to_qwen3_14b(self) -> None:
        installed = {"qwen3:14b", "qwen2.5:14b-instruct"}
        mode, model = resolve_mode_for_installed("deep", installed)
        self.assertEqual(mode["id"], "deep")
        self.assertEqual(model, "qwen3:14b")


if __name__ == "__main__":
    unittest.main()
