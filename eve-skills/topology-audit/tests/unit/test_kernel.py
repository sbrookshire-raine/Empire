"""Independent tests for topology_audit. Import by module name."""
import unittest

from local_topology_audit import kernel as topology_audit


class TopologyAuditTests(unittest.TestCase):
    def test_sample_matches_expected(self):
        self.assertEqual(topology_audit.run(topology_audit.SAMPLE), topology_audit.EXPECTED)

    def test_schema_bounds(self):
        self.assertFalse(topology_audit.SCHEMA.get("additionalProperties", True))
        self.assertEqual(topology_audit.SCHEMA["properties"]["nodes"]["maxItems"], 64)
        self.assertEqual(topology_audit.SCHEMA["properties"]["edges"]["maxItems"], 256)

    def test_unknown_keys(self):
        payload = dict(topology_audit.SAMPLE)
        payload["weights"] = 1
        with self.assertRaises(ValueError) as ctx:
            topology_audit.run(payload)
        self.assertIn("unknown keys", str(ctx.exception))

    def test_unknown_edge_keys(self):
        with self.assertRaises(ValueError) as ctx:
            topology_audit.run(
                {
                    "nodes": ["a", "b"],
                    "edges": [{"source": "a", "target": "b", "kind": "hard"}],
                    "outage": "b",
                }
            )
        self.assertIn("unknown keys", str(ctx.exception))

    def test_outage_unknown_node(self):
        with self.assertRaises(ValueError):
            topology_audit.run({"nodes": ["a"], "edges": [], "outage": "b"})

    def test_leaf_outage_isolated(self):
        out = topology_audit.run(
            {
                "nodes": ["app", "api", "db"],
                "edges": [
                    {"source": "app", "target": "api"},
                    {"source": "api", "target": "db"},
                ],
                "outage": "app",
            }
        )
        self.assertEqual(out["affected"], ["app"])
        self.assertEqual(out["unaffected"], ["api", "db"])
        self.assertFalse(out["has_cycle"])

    def test_cycle_detected_via_scc(self):
        out = topology_audit.run(
            {
                "nodes": ["a", "b", "c"],
                "edges": [
                    {"source": "a", "target": "b"},
                    {"source": "b", "target": "a"},
                ],
                "outage": "c",
            }
        )
        self.assertTrue(out["has_cycle"])
        self.assertEqual(out["cyclic_components"], [["a", "b"]])
        self.assertEqual(out["affected"], ["c"])

    def test_cycle_propagates_all_members(self):
        out = topology_audit.run(
            {
                "nodes": ["a", "b"],
                "edges": [
                    {"source": "a", "target": "b"},
                    {"source": "b", "target": "a"},
                ],
                "outage": "a",
            }
        )
        self.assertEqual(out["affected"], ["a", "b"])
        self.assertTrue(out["has_cycle"])

    def test_self_loop_is_cycle(self):
        out = topology_audit.run(
            {"nodes": ["a", "b"], "edges": [{"source": "a", "target": "a"}], "outage": "b"}
        )
        self.assertTrue(out["has_cycle"])
        self.assertEqual(out["cyclic_components"], [["a"]])
        self.assertEqual(out["affected"], ["b"])

    def test_duplicate_edge(self):
        with self.assertRaises(ValueError):
            topology_audit.run(
                {
                    "nodes": ["a", "b"],
                    "edges": [
                        {"source": "a", "target": "b"},
                        {"source": "a", "target": "b"},
                    ],
                    "outage": "b",
                }
            )

    def test_too_many_nodes(self):
        nodes = ["n%d" % i for i in range(65)]
        with self.assertRaises(ValueError):
            topology_audit.run({"nodes": nodes, "edges": [], "outage": "n0"})

    def test_not_object(self):
        with self.assertRaises(ValueError):
            topology_audit.run([])

    def test_malformed_edges(self):
        with self.assertRaises(ValueError):
            topology_audit.run({"nodes": ["a"], "edges": "a->a", "outage": "a"})

    def test_bool_node_rejected(self):
        with self.assertRaises(ValueError):
            topology_audit.run({"nodes": [True], "edges": [], "outage": "True"})


if __name__ == "__main__":
    unittest.main()
