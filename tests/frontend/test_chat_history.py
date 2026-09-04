"""Tests for local Eve chat history persistence."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from frontend import chat_history


class ChatHistoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmpdir.cleanup)
        self.folder = Path(self._tmpdir.name)
        self.patcher = patch.object(chat_history, "history_dir", return_value=self.folder)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def test_upsert_list_get_round_trip(self) -> None:
        saved = chat_history.upsert_chat(
            "chat-demo-1",
            {
                "mode": "fast",
                "model": "qwen-test",
                "messages": [
                    {"id": "m1", "role": "user", "text": "Hello Eve", "createdAt": "2026-01-01T00:00:00+00:00"},
                    {
                        "id": "m2",
                        "role": "assistant",
                        "text": "Hey.",
                        "createdAt": "2026-01-01T00:00:01+00:00",
                    },
                ],
            },
        )
        self.assertEqual(saved["title"], "Hello Eve")
        self.assertEqual(saved["messageCount"], 2)

        listed = chat_history.list_chats()
        self.assertEqual(len(listed), 1)
        self.assertEqual(listed[0]["id"], "chat-demo-1")
        self.assertEqual(listed[0]["messageCount"], 2)

        loaded = chat_history.get_chat("chat-demo-1")
        self.assertEqual(loaded["messages"][0]["text"], "Hello Eve")
        self.assertEqual(chat_history.get_active_chat_id(), "chat-demo-1")

    def test_newest_first_ordering(self) -> None:
        chat_history.upsert_chat(
            "chat-older",
            {
                "messages": [{"role": "user", "text": "older"}],
                "updatedAt": "2026-01-01T00:00:00+00:00",
            },
        )
        # Force older timestamp after upsert overwrote updatedAt
        older_path = self.folder / "chat-older.json"
        older = chat_history.get_chat("chat-older")
        older["updatedAt"] = "2026-01-01T00:00:00+00:00"
        older_path.write_text(
            __import__("json").dumps(older, indent=2) + "\n",
            encoding="utf-8",
        )

        chat_history.upsert_chat(
            "chat-newer",
            {"messages": [{"role": "user", "text": "newer"}]},
        )
        ids = [item["id"] for item in chat_history.list_chats()]
        self.assertEqual(ids[0], "chat-newer")
        self.assertIn("chat-older", ids)

    def test_rejects_bad_ids_and_empty_create(self) -> None:
        with self.assertRaises(chat_history.ChatHistoryError):
            chat_history.validate_chat_id("../secret")
        with self.assertRaises(chat_history.ChatHistoryError):
            chat_history.validate_chat_id("active")
        with self.assertRaises(chat_history.ChatHistoryError):
            chat_history.upsert_chat("chat-empty", {"messages": []})

    def test_delete_and_clear_active(self) -> None:
        chat_history.upsert_chat(
            "chat-del",
            {"messages": [{"role": "user", "text": "bye"}]},
        )
        self.assertEqual(chat_history.get_active_chat_id(), "chat-del")
        chat_history.delete_chat("chat-del")
        self.assertIsNone(chat_history.get_active_chat_id())
        with self.assertRaises(chat_history.ChatHistoryError) as raised:
            chat_history.get_chat("chat-del")
        self.assertEqual(raised.exception.status, 404)

    def test_message_text_is_capped(self) -> None:
        huge = "x" * (chat_history.MAX_MESSAGE_CHARS + 50)
        saved = chat_history.upsert_chat(
            "chat-cap",
            {"messages": [{"role": "user", "text": huge}]},
        )
        self.assertLessEqual(len(saved["messages"][0]["text"]), chat_history.MAX_MESSAGE_CHARS)


if __name__ == "__main__":
    unittest.main()
