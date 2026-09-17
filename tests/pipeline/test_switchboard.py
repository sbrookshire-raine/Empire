"""Unit tests for the Eve switchboard (governed service control).

All mutation paths are exercised in dry-run only; real PowerShell/service
control is never invoked from these tests.
"""

from __future__ import annotations

import unittest
from unittest.mock import patch

from pipeline import switchboard


class SwitchboardTests(unittest.TestCase):
    def test_validate_targets_rejects_unknown(self) -> None:
        res = switchboard._validate_targets(["pocketbase", "not_a_service"])
        self.assertFalse(res["ok"])
        self.assertIn("not_a_service", res["error"])

    def test_plan_never_starts_external(self) -> None:
        with patch.object(switchboard, "load_services", return_value={
            "rollInOrder": ["ollama", "pocketbase", "frontend", "eve"],
            "rollOutOrder": ["eve", "frontend", "pocketbase"],
            "services": {
                "ollama": {"label": "Ollama", "managed": False, "port": 11434},
                "pocketbase": {"label": "PocketBase", "managed": True, "port": 8090},
                "frontend": {"label": "Frontend", "managed": True, "port": 8080},
                "eve": {"label": "Eve", "managed": True, "port": 2000},
            },
        }):
            p = switchboard.plan(["ollama", "pocketbase"])
            self.assertTrue(p["ok"])
            self.assertNotIn("ollama", p["start"])
            self.assertIn("pocketbase", p["start"])
            self.assertIn("ollama", p["external_verify"])

    def test_ensure_headroom_block(self) -> None:
        with patch.object(switchboard, "load_services", return_value={
            "rollInOrder": ["pocketbase"],
            "rollOutOrder": ["pocketbase"],
            "services": {"pocketbase": {"label": "PB", "managed": True, "port": 8090}},
        }), patch.object(switchboard, "_headroom_ok", return_value=(False, {"ok": False, "headroom_reasons": ["RAM unavailable — fail closed"]})):
            res = switchboard.ensure(["pocketbase"], dry_run=False)
            self.assertFalse(res["ok"])
            self.assertIn("Headroom not OK", res["error"])

    def test_ensure_dry_run_no_mutation(self) -> None:
        with patch.object(switchboard, "load_services", return_value={
            "rollInOrder": ["pocketbase"],
            "rollOutOrder": ["pocketbase"],
            "services": {"pocketbase": {"label": "PB", "managed": True, "port": 8090}},
        }), patch.object(switchboard, "_headroom_ok", return_value=(True, {"ok": True})):
            res = switchboard.ensure(["pocketbase"], dry_run=True)
            self.assertTrue(res["ok"])
            self.assertTrue(res["dry_run"])
            self.assertIn("pocketbase", res["targets"])

    def test_release_never_stops_eve_or_ollama(self) -> None:
        res = switchboard.release(["eve", "ollama", "frontend"], dry_run=True)
        self.assertTrue(res["ok"])
        # eve + ollama are filtered out of the actionable targets; only
        # frontend is managed+releasable. `requested` echoes the full input.
        self.assertNotIn("eve", res.get("targets") or [])
        self.assertNotIn("ollama", res.get("targets") or [])
        self.assertIn("frontend", res.get("targets") or [])
        self.assertIn("eve", res.get("requested") or [])

    def test_tenant_release(self) -> None:
        with patch.object(switchboard.gpu_lease, "release", return_value={"ok": True, "tenant": "idle"}):
            res = switchboard.tenant("release")
            self.assertTrue(res["ok"])
            self.assertEqual(res["tenant"], "idle")

    def test_tenant_acquire_invalid(self) -> None:
        with patch.object(switchboard.gpu_lease, "acquire", return_value={"ok": False, "error": "Invalid tenant: nope"}):
            res = switchboard.tenant("acquire", tenant_name="nope")
            self.assertFalse(res["ok"])


if __name__ == "__main__":
    unittest.main()
