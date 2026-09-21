"""Independent tests for graph_map. Import by module name."""
import math
import unittest

from local_thought_map import kernel as graph_map


class GraphMapTests(unittest.TestCase):
    def test_sample_matches_expected(self):
        self.assertEqual(graph_map.run(graph_map.SAMPLE), graph_map.EXPECTED)

    def test_schema_additional_properties_false(self):
        self.assertFalse(graph_map.SCHEMA.get("additionalProperties", True))
        self.assertEqual(graph_map.SCHEMA["type"], "object")

    def test_unknown_keys(self):
        with self.assertRaises(ValueError) as ctx:
            graph_map.run({"nodes": ["A"], "edges": [], "extra": 1})
        self.assertIn("unknown keys", str(ctx.exception))

    def test_unknown_edge_keys(self):
        with self.assertRaises(ValueError) as ctx:
            graph_map.run(
                {
                    "nodes": ["A", "B"],
                    "edges": [{"source": "A", "target": "B", "sign": 1, "w": 2}],
                }
            )
        self.assertIn("unknown keys", str(ctx.exception))

    def test_bool_sign_rejected(self):
        with self.assertRaises(ValueError):
            graph_map.run(
                {"nodes": ["A"], "edges": [{"source": "A", "target": "A", "sign": True}]}
            )

    def test_duplicate_node(self):
        with self.assertRaises(ValueError):
            graph_map.run({"nodes": ["A", "A"], "edges": []})

    def test_unknown_node_on_edge(self):
        with self.assertRaises(ValueError):
            graph_map.run(
                {"nodes": ["A"], "edges": [{"source": "A", "target": "B", "sign": 1}]}
            )

    def test_duplicate_edge(self):
        with self.assertRaises(ValueError):
            graph_map.run(
                {
                    "nodes": ["A", "B"],
                    "edges": [
                        {"source": "A", "target": "B", "sign": 1},
                        {"source": "A", "target": "B", "sign": -1},
                    ],
                }
            )

    def test_too_many_nodes(self):
        nodes = ["n%d" % i for i in range(65)]
        with self.assertRaises(ValueError):
            graph_map.run({"nodes": nodes, "edges": []})

    def test_too_many_edges(self):
        nodes = ["n%d" % i for i in range(64)]
        edges = []
        for i in range(64):
            for j in range(5):
                if len(edges) >= 257:
                    break
                tgt = nodes[(i + j + 1) % 64]
                edges.append({"source": nodes[i], "target": tgt, "sign": 1})
        self.assertGreaterEqual(len(edges), 257)
        with self.assertRaises(ValueError):
            graph_map.run({"nodes": nodes, "edges": edges[:257]})

    def test_empty_nodes(self):
        with self.assertRaises(ValueError):
            graph_map.run({"nodes": [], "edges": []})

    def test_not_object(self):
        with self.assertRaises(ValueError):
            graph_map.run(["A"])

    def test_dag_no_cycle(self):
        out = graph_map.run(
            {
                "nodes": ["A", "B"],
                "edges": [{"source": "A", "target": "B", "sign": 1}],
            }
        )
        self.assertFalse(out["has_cycle"])
        self.assertEqual(out["n_scc"], 2)
        self.assertEqual(out["self_loops"], [])

    def test_self_loop_is_cycle(self):
        out = graph_map.run(
            {
                "nodes": ["A"],
                "edges": [{"source": "A", "target": "A", "sign": -1}],
            }
        )
        self.assertTrue(out["has_cycle"])
        self.assertEqual(out["self_loops"][0]["polarity"], "balancing")

    def test_scc_two_components(self):
        out = graph_map.run(
            {
                "nodes": ["A", "B", "C"],
                "edges": [
                    {"source": "A", "target": "B", "sign": 1},
                    {"source": "B", "target": "A", "sign": 1},
                ],
            }
        )
        self.assertEqual(out["n_scc"], 2)
        self.assertTrue(out["has_cycle"])
        self.assertIn(["A", "B"], out["strongly_connected_components"])
        self.assertIn(["C"], out["strongly_connected_components"])

    def test_degrees_isolated(self):
        out = graph_map.run({"nodes": ["Z"], "edges": []})
        self.assertEqual(out["degrees"], [{"node": "Z", "in_degree": 0, "out_degree": 0}])
        self.assertFalse(out["has_cycle"])

    def test_malformed_edge_not_object(self):
        with self.assertRaises(ValueError):
            graph_map.run({"nodes": ["A"], "edges": ["A->A"]})

    def test_invalid_sign(self):
        with self.assertRaises(ValueError):
            graph_map.run(
                {"nodes": ["A", "B"], "edges": [{"source": "A", "target": "B", "sign": 0}]}
            )

    def test_float_sign_rejected(self):
        with self.assertRaises(ValueError):
            graph_map.run(
                {"nodes": ["A", "B"], "edges": [{"source": "A", "target": "B", "sign": 1.0}]}
            )

    def test_nan_not_applicable_nodes_are_strings(self):
        with self.assertRaises(ValueError):
            graph_map.run({"nodes": [math.nan], "edges": []})


if __name__ == "__main__":
    unittest.main()
