"""Unit tests for the vendored claim-ledger MCP server.

The upstream server was written for a POSIX host. Three things were wrong for
this Windows host, and each is pinned here so it cannot regress silently:

1. the root list was split on ``[;:]``, which shredded a Windows drive letter
   (``C:\\work`` became ``C`` and ``\\work``) and made every check fail with
   ``[WinError 267]``;
2. the check working directory was chosen with an expression that was always
   true, so it never actually checked that the root existed;
3. ``shell=True`` runs cmd.exe on Windows, where a POSIX check (pipe, grep)
   does not exist.
"""

from __future__ import annotations

import asyncio
import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SERVER = ROOT / "mcp" / "claim_ledger_mcp.py"


def _load(server: Path, env: dict[str, str]):
    """Import the server module with a given environment, as a fresh module."""

    for key, value in env.items():
        os.environ[key] = value
    spec = importlib.util.spec_from_file_location("claim_ledger_mcp_under_test", server)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["claim_ledger_mcp_under_test"] = module
    spec.loader.exec_module(module)
    return module


def _text(result) -> str:
    """Flatten an MCP tool result into text."""

    parts = result.content if hasattr(result, "content") else result
    if isinstance(parts, list):
        return " ".join(getattr(p, "text", str(p)) for p in parts)
    return str(parts)


class RootParsingTests(unittest.TestCase):
    def test_a_windows_drive_letter_survives_root_parsing(self) -> None:
        module = _load(SERVER, {"CLAIM_LEDGER_ROOTS": r"C:\work;D:\other"})
        roots = [str(r) for r in module.ROOTS]
        self.assertEqual(len(roots), 2)
        self.assertTrue(roots[0].endswith("work"))
        self.assertTrue(roots[1].endswith("other"))

    def test_a_single_drive_qualified_root_is_one_root(self) -> None:
        module = _load(SERVER, {"CLAIM_LEDGER_ROOTS": r"C:\work"})
        self.assertEqual(len(module.ROOTS), 1)
        self.assertTrue(str(module.ROOTS[0]).endswith("work"))

    def test_semicolon_and_newline_both_separate_roots(self) -> None:
        module = _load(SERVER, {"CLAIM_LEDGER_ROOTS": "C:\\a;C:\\b"})
        self.assertEqual(len(module.ROOTS), 2)
        module = _load(SERVER, {"CLAIM_LEDGER_ROOTS": "C:\\a\nC:\\b"})
        self.assertEqual(len(module.ROOTS), 2)

    def test_no_roots_declared_falls_back_to_the_database_directory(self) -> None:
        module = _load(SERVER, {"CLAIM_LEDGER_ROOTS": ""})
        self.assertEqual(len(module.ROOTS), 1)
        self.assertEqual(module.ROOTS[0], module.DB.parent.resolve())


class ToolContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.module = _load(
            SERVER,
            {
                "CLAIM_LEDGER_DB": str(self.root / "claims.db"),
                "CLAIM_LEDGER_ROOTS": str(self.root),
                "CLAIM_LEDGER_SHELL": "cmd.exe",
            },
        )

    def _call(self, name: str, args: dict | None = None):
        return asyncio.run(self.module.mcp.call_tool(name, args or {}))

    def test_the_four_tools_are_exposed(self) -> None:
        tools = asyncio.run(self.module.mcp.list_tools())
        self.assertEqual(
            sorted(t.name for t in tools),
            ["claim_add", "claim_health", "claim_list", "claim_verify"],
        )

    def test_a_claim_without_a_check_is_a_document(self) -> None:
        out = _text(self._call("claim_add", {"claim": "no check here"}))
        self.assertIn("document", out)

    def test_a_claim_with_a_check_is_a_capability(self) -> None:
        out = _text(self._call("claim_add", {"claim": "has a check", "check_cmd": "exit 0"}))
        self.assertIn("capability", out)

    def test_an_unknown_grade_is_refused(self) -> None:
        out = _text(self._call("claim_add", {"claim": "x", "grade": "invented"}))
        self.assertIn("grade must be one of", out)

    def test_verify_runs_a_check_and_records_the_result(self) -> None:
        self._call("claim_add", {"claim": "passing claim", "check_cmd": "exit 0"})
        out = _text(self._call("claim_verify", {"slug": ""}))
        self.assertIn("passed 1", out)
        self.assertIn("failed 0", out)

    def test_a_failing_check_is_reported_as_a_failure(self) -> None:
        self._call("claim_add", {"claim": "failing claim", "check_cmd": "exit 3"})
        out = _text(self._call("claim_verify", {"slug": ""}))
        self.assertIn("failed", out)

    def test_health_reports_a_number_and_a_verdict(self) -> None:
        self._call("claim_add", {"claim": "one", "check_cmd": "exit 0"})
        out = _text(self._call("claim_health", {}))
        self.assertIn("verdict", out)
        self.assertIn("total", out)

    def test_health_on_an_empty_store_says_empty(self) -> None:
        out = _text(self._call("claim_health", {}))
        self.assertIn("empty", out)

    def test_list_can_filter_to_unchecked_and_failing(self) -> None:
        self._call("claim_add", {"claim": "document claim"})
        self._call("claim_add", {"claim": "broken claim", "check_cmd": "exit 4"})
        self._call("claim_verify", {"slug": ""})
        unchecked = _text(self._call("claim_list", {"unchecked": True}))
        self.assertIn("document-claim", unchecked)
        self.assertNotIn("broken-claim", unchecked)
        failing = _text(self._call("claim_list", {"failing": True}))
        self.assertIn("broken-claim", failing)


if __name__ == "__main__":
    unittest.main()
