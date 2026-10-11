from __future__ import annotations

import unittest
from unittest.mock import patch

from pipeline import baseline_flush


class BaselineFlushTests(unittest.TestCase):
    @patch.object(baseline_flush, "_ollama_unload_loaded", return_value=["nomic-embed-text:latest"])
    @patch.object(baseline_flush, "_docker_stop_container", return_value=True)
    @patch.object(baseline_flush, "_stop_weaviate", return_value={"ok": True})
    @patch.object(baseline_flush.baseline_audit, "stop_eve_sbx_docker", return_value=0)
    @patch.object(baseline_flush.baseline_audit, "kill_orphan_llama_servers", return_value=[])
    @patch("pipeline.gpu_lease.release", return_value={"ok": True})
    @patch("pipeline.admission_controller.release_session", return_value={"ok": True})
    @patch("frontend.eve_toolbelt.write_active_tools")
    @patch("frontend.eve_toolbelt.load_active_tools", return_value=["wiki_local"])
    @patch("pipeline.resource_pulse.pulse")
    def test_flush_clears_toolbelt_and_returns_meters(
        self,
        mock_pulse,
        _load,
        write_tools,
        _rel,
        _gpu,
        _kill,
        _sbx,
        _wiki,
        _sp,
        _ollama,
    ) -> None:
        mock_pulse.side_effect = [
            {"ok": True, "capacity_meter": {"activation_on_count": 1, "ram_used_pct": 50, "vram_used_pct": 30, "disk_used_pct": 70}},
            {"ok": True, "capacity_meter": {"activation_on_count": 0, "ram_used_pct": 32, "vram_used_pct": 12, "disk_used_pct": 70}},
        ]
        out = baseline_flush.flush_baseline()
        self.assertTrue(out["ok"])
        write_tools.assert_called_once_with([])
        self.assertEqual(out["after"]["activation_on_count"], 0)


if __name__ == "__main__":
    unittest.main()
