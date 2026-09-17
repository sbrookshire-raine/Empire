"""Unit tests for the capability registry (governance foundation)."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from pipeline import capability_registry as cr


def _sample_tool(name: str = "workspace_search") -> dict:
    return {
        "name": name,
        "description": "Search allowlisted local roots.",
        "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}},
    }


class CapabilityRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.reg_path = self.root / "registry.json"
        self.snap_path = self.root / "snapshot.json"

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_register_and_verify_ok(self) -> None:
        reg = cr.empty_registry()
        cr.register_capability(
            reg,
            capability_id="workspace_search",
            label="Workspace Search",
            domain="local_evidence",
            tools=[_sample_tool()],
        )
        snap = cr.build_snapshot(reg)
        ok = cr.verify_capability("workspace_search", registry=reg, snapshot=snap)
        self.assertTrue(ok["ok"])
        self.assertTrue(ok["approved"])

    def test_verify_unknown_capability(self) -> None:
        reg = cr.empty_registry()
        res = cr.verify_capability("nope", registry=reg, snapshot={"tools": {}})
        self.assertFalse(res["ok"])
        self.assertFalse(res["approved"])

    def test_schema_drift_fails_closed(self) -> None:
        reg = cr.empty_registry()
        cr.register_capability(
            reg,
            capability_id="query_data",
            label="Query Data",
            domain="local_evidence",
            tools=[_sample_tool("query_data")],
        )
        snap = cr.build_snapshot(reg)

        # Drift the tool description after snapshotting.
        reg["capabilities"][0]["tools"][0]["description"] = "CHANGED description"
        reg["capabilities"][0]["tools"][0]["signature_hash"] = "stale"

        res = cr.verify_capability("query_data", registry=reg, snapshot=snap)
        self.assertFalse(res["ok"])
        self.assertFalse(res["approved"])
        self.assertIn("schema drift", res["reason"])

    def test_snapshot_persistence(self) -> None:
        reg = cr.empty_registry()
        cr.register_capability(
            reg,
            capability_id="read_document",
            label="Read Document",
            domain="local_evidence",
            tools=[_sample_tool("read_document")],
        )
        cr.write_snapshot(reg, path=self.snap_path)
        loaded = cr.load_snapshot(path=self.snap_path)
        self.assertIn("read_document", loaded["tools"])

    def test_bad_domain_rejected(self) -> None:
        reg = cr.empty_registry()
        with self.assertRaises(ValueError):
            cr.register_capability(
                reg,
                capability_id="x",
                label="X",
                domain="not_a_domain",
                tools=[_sample_tool()],
            )

    def test_ensure_layout_creates_dirs(self) -> None:
        res = cr.ensure_layout()
        self.assertTrue(res["ok"])
        for d in res["created"]:
            self.assertTrue(Path(d).is_dir())


if __name__ == "__main__":
    unittest.main()
