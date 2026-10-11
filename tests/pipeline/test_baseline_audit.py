from __future__ import annotations

import unittest
from unittest.mock import patch

from pipeline import baseline_audit


class BaselineAuditTests(unittest.TestCase):
    def test_docker_layer_flags_eve_sbx(self) -> None:
        with patch.object(baseline_audit, "_eve_sbx_count", return_value=3):
            with patch.object(baseline_audit, "_docker_ps_all", return_value=[]):
                with patch.object(baseline_audit, "_orphan_llama_servers", return_value=[]):
                    with patch.object(baseline_audit, "_load_toolbelt_active", return_value=[]):
                        with patch.object(baseline_audit, "_fetch_resource_pulse", return_value={"ok": True}):
                            with patch.object(
                                baseline_audit,
                                "_port_open",
                                return_value=True,
                            ):
                                report = baseline_audit.run()
        self.assertFalse(report["ok"])
        self.assertTrue(any("eve-sbx" in b for b in report["blockers"]))

    def test_toolbelt_wiki_mismatch_warns(self) -> None:
        with patch.object(baseline_audit, "_eve_sbx_count", return_value=0):
            with patch.object(baseline_audit, "_docker_ps_all", return_value=[]):
                with patch.object(baseline_audit, "_orphan_llama_servers", return_value=[]):
                    with patch.object(baseline_audit, "_load_toolbelt_active", return_value=[]):

                        def ports(host: str, port: int, timeout: float = 1.5) -> bool:
                            return port == 8091

                        with patch.object(baseline_audit, "_port_open", side_effect=ports):
                            with patch.object(
                                baseline_audit,
                                "_fetch_resource_pulse",
                                return_value={"ok": True, "inventory": {"effective_tools": []}},
                            ):
                                report = baseline_audit.run()
        self.assertTrue(any("Weaviate" in w for w in report["warnings"]))


if __name__ == "__main__":
    unittest.main()
