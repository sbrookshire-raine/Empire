from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from frontend import ollama_api


TAGS = {
    "models": [
        {
            "name": "richardyoung/qwen2.5-14b-instruct-abliterated:latest",
            "model": "richardyoung/qwen2.5-14b-instruct-abliterated:latest",
            "details": {"parameter_size": "14.0B", "family": "qwen2"},
            "capabilities": ["completion", "tools"],
        },
        {
            "name": "qwen2.5:32b",
            "model": "qwen2.5:32b",
            "details": {"parameter_size": "32.0B", "family": "qwen2"},
            "capabilities": ["completion", "tools"],
        },
        {
            "name": "command-r:35b",
            "model": "command-r:35b",
            "details": {"parameter_size": "35.0B", "family": "command-r"},
            "capabilities": ["completion", "tools"],
        },
        {
            "name": "nomic-embed-text:latest",
            "model": "nomic-embed-text:latest",
            "details": {"family": "nomic-bert"},
            "capabilities": ["embedding"],
        },
    ]
}


class OllamaApiTests(unittest.TestCase):
    def test_lists_only_chat_models_and_keeps_active_selection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ollama-active-model.json"
            path.write_text(
                json.dumps(
                    {
                        "mode": "deep",
                        "model": "qwen2.5:32b",
                    }
                ),
                encoding="utf-8",
            )
            with patch.object(ollama_api, "active_model_path", return_value=path):
                payload = ollama_api.models_status(TAGS, connected=True)

        ids = [model["id"] for model in payload["models"]]
        self.assertEqual(payload["ok"], True)
        self.assertEqual(payload["connected"], True)
        self.assertEqual(payload["active"], "qwen2.5:32b")
        self.assertEqual(payload["activeMode"], "deep")
        self.assertEqual(len(payload["chatModes"]), 3)
        self.assertEqual(
            ids,
            [
                "richardyoung/qwen2.5-14b-instruct-abliterated:latest",
                "qwen2.5:32b",
                "command-r:35b",
            ],
        )
        self.assertTrue(payload["models"][0]["tools"])

    def test_set_active_mode_writes_config(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ollama-active-model.json"
            with patch.object(ollama_api, "active_model_path", return_value=path):
                saved = ollama_api.set_active_model("", TAGS, mode="librarian")

            self.assertEqual(saved["activeMode"], "librarian")
            self.assertEqual(saved["active"], "command-r:35b")
            stored = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(stored["mode"], "librarian")
            self.assertEqual(stored["options"]["temperature"], 0.4)
            self.assertEqual(stored["options"]["num_ctx"], 8192)

    def test_rejects_embedding_models_and_unknown_ids(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ollama-active-model.json"
            with patch.object(ollama_api, "active_model_path", return_value=path):
                with self.assertRaises(ollama_api.OllamaRequestError) as embed:
                    ollama_api.set_active_model("nomic-embed-text:latest", TAGS)
                with self.assertRaises(ollama_api.OllamaRequestError) as missing:
                    ollama_api.set_active_model("not-a-real-model", TAGS)
                saved = ollama_api.set_active_model(
                    "richardyoung/qwen2.5-14b-instruct-abliterated:latest",
                    TAGS,
                )

            self.assertEqual(embed.exception.status, 400)
            self.assertEqual(missing.exception.status, 400)
            self.assertEqual(saved["active"], "richardyoung/qwen2.5-14b-instruct-abliterated:latest")
            self.assertEqual(saved["activeMode"], "fast")
            self.assertEqual(
                json.loads(path.read_text(encoding="utf-8"))["model"],
                "richardyoung/qwen2.5-14b-instruct-abliterated:latest",
            )

    def test_unavailable_ollama_keeps_fallback_without_pretending_connected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ollama-active-model.json"
            with patch.object(ollama_api, "active_model_path", return_value=path):
                payload = ollama_api.models_status(
                    None, connected=False, error="Ollama is unavailable."
                )
        self.assertEqual(payload["ok"], False)
        self.assertEqual(payload["connected"], False)
        self.assertEqual(payload["models"], [])
        self.assertEqual(payload["active"], ollama_api.DEFAULT_MODEL)
        self.assertIn("unavailable", payload["error"].casefold())

    def test_summarize_tasks_without_tasks_is_plain_message(self) -> None:
        with patch.object(ollama_api, "load_active_model", return_value="llama3.1:8b"):
            payload = ollama_api.summarize_tasks([])
        self.assertEqual(payload["ok"], True)
        self.assertIn("No PocketBase tasks", payload["summary"])
        self.assertEqual(payload["taskCount"], 0)

    def test_summarize_tasks_uses_ollama_chat_completion(self) -> None:
        class FakeResponse:
            status = 200

            def read(self, _limit: int = -1) -> bytes:
                return json.dumps(
                    {"choices": [{"message": {"content": "- Focus on open tasks."}}]}
                ).encode("utf-8")

        class FakeConnection:
            def request(self, *_args, **_kwargs) -> None:
                return None

            def getresponse(self) -> FakeResponse:
                return FakeResponse()

            def close(self) -> None:
                return None

        tasks = [{"title": "Ship workbench", "status": "in_progress", "priority": 1, "description": ""}]
        with patch.object(ollama_api, "load_active_model", return_value="llama3.1:8b"):
            with patch.object(ollama_api, "HTTPConnection", return_value=FakeConnection()):
                payload = ollama_api.summarize_tasks(tasks)
        self.assertEqual(payload["summary"], "- Focus on open tasks.")
        self.assertEqual(payload["model"], "llama3.1:8b")
        self.assertEqual(payload["taskCount"], 1)


if __name__ == "__main__":
    unittest.main()
