from __future__ import annotations

import unittest

from frontend import ollama_inventory


TAGS = {
    "models": [
        {
            "name": "llama3.1:8b",
            "model": "llama3.1:8b",
            "size": 4.9 * 1024**3,
            "digest": "digest-llama",
            "details": {"parameter_size": "8.0B", "quantization_level": "Q4_K_M", "family": "llama"},
            "capabilities": ["completion", "tools"],
        },
        {
            "name": "llama3.1:latest",
            "model": "llama3.1:latest",
            "size": 4.9 * 1024**3,
            "digest": "digest-llama",
            "details": {"parameter_size": "8.0B", "quantization_level": "Q4_K_M", "family": "llama"},
            "capabilities": ["completion", "tools"],
        },
        {
            "name": "qwen2.5:14b-instruct",
            "model": "qwen2.5:14b-instruct",
            "size": 9 * 1024**3,
            "digest": "digest-fast",
            "details": {"parameter_size": "14.0B", "quantization_level": "Q4_K_M", "family": "qwen2"},
            "capabilities": ["completion", "tools"],
        },
        {
            "name": "qwen2.5-coder:14b",
            "model": "qwen2.5-coder:14b",
            "size": 9 * 1024**3,
            "digest": "digest-coder",
            "details": {"parameter_size": "14.8B", "quantization_level": "Q4_K_M", "family": "qwen2"},
            "capabilities": ["completion", "tools"],
        },
        {
            "name": "qwen3.8:latest",
            "model": "qwen3.8:latest",
            "size": 17 * 1024**3,
            "digest": "digest-qwen",
            "details": {"parameter_size": "27.3B", "quantization_level": "Q4_K_M", "family": "qwen35"},
            "capabilities": ["completion"],
        },
        {
            "name": "nomic-embed-text:latest",
            "model": "nomic-embed-text:latest",
            "size": 274 * 1024**2,
            "digest": "digest-embed",
            "details": {"parameter_size": "137M", "quantization_level": "F16", "family": "nomic-bert"},
            "capabilities": ["embedding"],
        },
    ]
}


class OllamaInventoryTests(unittest.TestCase):
    def test_build_inventory_marks_fit_and_suite_slots(self) -> None:
        payload = ollama_inventory.build_inventory(TAGS)
        by_id = {model["id"]: model for model in payload["models"]}
        self.assertEqual(by_id["llama3.1:8b"]["fit16gb"], "excellent")
        self.assertEqual(by_id["qwen3.8:latest"]["fit16gb"], "heavy")
        self.assertEqual(by_id["nomic-embed-text:latest"]["role"], "embed")

        recommendations = payload["recommendations"]
        self.assertIn("suite", recommendations)
        self.assertIn("pullGaps", recommendations)
        self.assertIn("removeSuggestions", recommendations)
        self.assertIn("eveBriefing", recommendations)

        daily = next(slot for slot in recommendations["suite"] if slot["id"] == "dailyChat")
        self.assertEqual(daily["status"], "covered")
        self.assertEqual(daily["installedId"], "qwen2.5:14b-instruct")

        deep = next(slot for slot in recommendations["suite"] if slot["id"] == "deepQuality")
        self.assertIn(deep["status"], ("gap", "weak"))

        remove_ids = [item["id"] for item in recommendations["removeSuggestions"]]
        self.assertIn("llama3.1:latest", remove_ids)

    def test_duplicate_groups_surface_shared_digests(self) -> None:
        payload = ollama_inventory.build_inventory(TAGS)
        self.assertTrue(
            any(
                set(group) == {"llama3.1:8b", "llama3.1:latest"}
                for group in payload["duplicateGroups"]
            )
        )


if __name__ == "__main__":
    unittest.main()
