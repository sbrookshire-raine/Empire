from __future__ import annotations

import json
import tempfile
import unittest
import zipfile
from email.message import EmailMessage
from pathlib import Path
from unittest.mock import patch

from pipeline import rea_inbox


class ReaInboxTests(unittest.TestCase):
    def test_save_multipart_upload_and_list(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(rea_inbox, "inbox_root", return_value=root):
                msg = EmailMessage()
                msg.add_attachment(b"console.log('hi')", maintype="application", subtype="octet-stream", filename="app.js")
                parts = list(msg.iter_attachments())
                bundle = rea_inbox.save_multipart_upload(parts)
                self.assertTrue(bundle["id"])
                self.assertEqual(len(bundle["files"]), 1)
                listed = rea_inbox.list_bundles(limit=5)
                self.assertEqual(listed[0]["id"], bundle["id"])

    def test_zip_extract_and_analysis_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            zip_path = root / "sample.zip"
            with zipfile.ZipFile(zip_path, "w") as archive:
                archive.writestr("bundle/index.html", "<html></html>")
            with patch.object(rea_inbox, "inbox_root", return_value=root / "inbox"):
                msg = EmailMessage()
                with zip_path.open("rb") as handle:
                    msg.add_attachment(handle.read(), maintype="application", subtype="zip", filename="sample.zip")
                parts = list(msg.iter_attachments())
                bundle = rea_inbox.save_multipart_upload(parts)
                roots = bundle.get("analysis_roots") or []
                self.assertTrue(any("index.html" in row or "bundle" in row for row in roots))

    def test_context_block_for_upload_ids(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(rea_inbox, "inbox_root", return_value=root):
                msg = EmailMessage()
                msg.add_attachment(b"{}", maintype="application", subtype="json", filename="meta.json")
                bundle = rea_inbox.save_multipart_upload(list(msg.iter_attachments()))
                block = rea_inbox.context_block_for_upload_ids([bundle["id"]])
                self.assertIn(rea_inbox.REA_UPLOAD_MARKER, block)
                self.assertIn('"uploads"', block)
                self.assertIn(bundle["id"], block)


if __name__ == "__main__":
    unittest.main()
