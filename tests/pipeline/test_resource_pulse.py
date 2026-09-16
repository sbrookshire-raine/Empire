"""Unit tests for resource pulse + admit_for_goal policy B."""

from __future__ import annotations

import unittest
from unittest.mock import patch

from pipeline import resource_pulse


class ResourcePulseTests(unittest.TestCase):
    def test_pulse_ok_shape(self) -> None:
        with (
            patch.object(
                resource_pulse.gpu_lease,
                "_resource_snapshot",
                return_value={"ram_available_gb": 8.0, "disk_free_gb": 40.0},
            ),
            patch.object(
                resource_pulse,
                "_nvidia_snapshot",
                return_value={"ok": True, "vram_free_mb": 8000, "vram_total_mb": 16000},
            ),
            patch.object(
                resource_pulse.gpu_lease,
                "status",
                return_value={"ok": True, "tenant": "idle", "holder": ""},
            ),
            patch.object(
                resource_pulse.admission_controller,
                "status",
                return_value={
                    "manual_toolbelt": ["voice_presence", "wiki_local"],
                    "session_capabilities": [],
                    "effective_tools": ["voice_presence", "wiki_local"],
                    "research_partner_mode": False,
                    "ttl_remaining_sec": 0,
                },
            ),
            patch.object(
                resource_pulse,
                "_service_probes",
                return_value={
                    "services": {"ollama": True, "speaches": True},
                    "wiki_glasses_detail": {"glasses_ok": True},
                },
            ),
            patch.object(
                resource_pulse.admission_controller,
                "load_manifest",
                return_value={
                    "categories": {
                        "github_scout": {
                            "label": "GitHub Scout",
                            "auto_enable": True,
                            "gpu_tenant": "none",
                        },
                        "vision_local": {
                            "label": "Vision",
                            "auto_enable": False,
                            "gpu_tenant": "vision",
                        },
                    }
                },
            ),
        ):
            out = resource_pulse.pulse()
        self.assertTrue(out["ok"])
        self.assertTrue(out["headroom_ok"])
        self.assertIn("github_scout", out["can_admit_now"])
        self.assertTrue(any(i["id"] == "vision_local" for i in out["ask_architect_first"]))
        self.assertIn("summary", out)

    def test_admit_light_bypasses_partner_when_headroom_ok(self) -> None:
        with (
            patch.object(
                resource_pulse,
                "pulse",
                return_value={"ok": True, "headroom_ok": True, "summary": "ok"},
            ),
            patch.object(
                resource_pulse.admission_controller,
                "category_meta",
                return_value={"auto_enable": True, "gpu_tenant": "none"},
            ),
            patch.object(
                resource_pulse.admission_controller,
                "request_capability",
                return_value={"ok": True, "category": "github_scout", "source": "session"},
            ) as mock_req,
        ):
            out = resource_pulse.admit_for_goal("github_scout", reason="need repo search")
        self.assertTrue(out["ok"])
        self.assertTrue(out.get("resource_gated"))
        mock_req.assert_called_once()
        kwargs = mock_req.call_args.kwargs
        self.assertTrue(kwargs.get("bypass_partner_check"))

    def test_admit_gpu_asks_architect(self) -> None:
        with (
            patch.object(
                resource_pulse,
                "pulse",
                return_value={"ok": True, "headroom_ok": True, "summary": "ok", "gpu_lease": {}},
            ),
            patch.object(
                resource_pulse.admission_controller,
                "category_meta",
                return_value={"auto_enable": False, "gpu_tenant": "vision"},
            ),
        ):
            out = resource_pulse.admit_for_goal("vision_local", reason="screenshot")
        self.assertFalse(out["ok"])
        self.assertTrue(out.get("need_architect"))

    def test_admit_refuses_when_headroom_bad(self) -> None:
        with (
            patch.object(
                resource_pulse,
                "pulse",
                return_value={
                    "ok": True,
                    "headroom_ok": False,
                    "headroom_reasons": ["RAM available 0.5 GB below 2.0 GB"],
                    "summary": "blocked",
                },
            ),
            patch.object(
                resource_pulse.admission_controller,
                "category_meta",
                return_value={"auto_enable": True, "gpu_tenant": "none"},
            ),
        ):
            out = resource_pulse.admit_for_goal("web_scout", reason="fetch url")
        self.assertFalse(out["ok"])
        self.assertFalse(out.get("need_architect"))

    def test_live_manifest_stem_is_heavy(self) -> None:
        light, heavy = resource_pulse._classify_manifest()
        heavy_ids = {item["id"] for item in heavy}
        light_ids = {item["id"] for item in light}
        self.assertIn("stem_factory", heavy_ids)
        self.assertIn("github_scout", light_ids)
        stem = next(item for item in heavy if item["id"] == "stem_factory")
        self.assertEqual(stem["gpu_tenant"], "stem")


if __name__ == "__main__":
    unittest.main()
