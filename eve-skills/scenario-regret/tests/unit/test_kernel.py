"""Independent tests for scenario_regret. Import by module name."""
import math
import unittest

from local_scenario_regret import kernel as scenario_regret


class ScenarioRegretTests(unittest.TestCase):
    def test_sample_matches_expected(self):
        self.assertEqual(scenario_regret.run(scenario_regret.SAMPLE), scenario_regret.EXPECTED)

    def test_schema_bounds(self):
        self.assertFalse(scenario_regret.SCHEMA.get("additionalProperties", True))
        self.assertEqual(scenario_regret.SCHEMA["properties"]["options"]["maxItems"], 64)
        self.assertEqual(scenario_regret.SCHEMA["properties"]["scenarios"]["maxItems"], 64)

    def test_unknown_keys(self):
        payload = dict(scenario_regret.SAMPLE)
        payload["weights"] = [0.5, 0.5]
        with self.assertRaises(ValueError) as ctx:
            scenario_regret.run(payload)
        self.assertIn("unknown keys", str(ctx.exception))

    def test_bool_payoff_rejected(self):
        with self.assertRaises(ValueError):
            scenario_regret.run(
                {
                    "options": ["a"],
                    "scenarios": ["s"],
                    "payoffs": [[True]],
                    "objective": "maximize",
                }
            )

    def test_nan_payoff_rejected(self):
        with self.assertRaises(ValueError):
            scenario_regret.run(
                {
                    "options": ["a"],
                    "scenarios": ["s"],
                    "payoffs": [[math.nan]],
                    "objective": "maximize",
                }
            )

    def test_inf_payoff_rejected(self):
        with self.assertRaises(ValueError):
            scenario_regret.run(
                {
                    "options": ["a"],
                    "scenarios": ["s"],
                    "payoffs": [[math.inf]],
                    "objective": "maximize",
                }
            )

    def test_row_length_mismatch(self):
        with self.assertRaises(ValueError):
            scenario_regret.run(
                {
                    "options": ["a", "b"],
                    "scenarios": ["s1", "s2"],
                    "payoffs": [[1, 2], [3]],
                    "objective": "maximize",
                }
            )

    def test_minimize_objective(self):
        out = scenario_regret.run(
            {
                "options": ["low", "high"],
                "scenarios": ["s1", "s2"],
                "payoffs": [[1, 10], [4, 5]],
                "objective": "minimize",
            }
        )
        self.assertEqual(out["objective"], "minimize")
        self.assertEqual(out["ranking"][0]["option"], "high")
        self.assertEqual(out["regret"][0]["regrets"], [0.0, 5.0])
        self.assertEqual(out["regret"][1]["regrets"], [3.0, 0.0])

    def test_tie_preserves_lexicographic_then_index(self):
        out = scenario_regret.run(
            {
                "options": ["first", "second"],
                "scenarios": ["s1", "s2"],
                "payoffs": [[1, 1], [1, 1]],
                "objective": "maximize",
            }
        )
        self.assertEqual(out["ranking"][0]["option"], "first")
        self.assertEqual(out["ranking"][1]["option"], "second")
        self.assertEqual(out["ranking"][0]["max_regret"], 0.0)

    def test_lexicographic_regret_vector_breaks_max_tie(self):
        out = scenario_regret.run(
            {
                "options": ["a", "b"],
                "scenarios": ["s1", "s2"],
                "payoffs": [[10, 0], [5, 5]],
                "objective": "maximize",
            }
        )
        # max regret tied at 5; [0,5] < [5,0] so a ranks first
        self.assertEqual(out["ranking"][0]["option"], "a")
        self.assertEqual(out["ranking"][0]["max_regret"], 5.0)
        self.assertEqual(out["ranking"][1]["max_regret"], 5.0)
        self.assertEqual(out["ranking"][0]["regrets"], [0.0, 5.0])

    def test_invalid_objective(self):
        with self.assertRaises(ValueError):
            scenario_regret.run(
                {
                    "options": ["a"],
                    "scenarios": ["s"],
                    "payoffs": [[1]],
                    "objective": "max",
                }
            )

    def test_duplicate_option(self):
        with self.assertRaises(ValueError):
            scenario_regret.run(
                {
                    "options": ["a", "a"],
                    "scenarios": ["s"],
                    "payoffs": [[1], [2]],
                    "objective": "maximize",
                }
            )

    def test_too_many_options(self):
        opts = ["o%d" % i for i in range(65)]
        with self.assertRaises(ValueError):
            scenario_regret.run(
                {
                    "options": opts,
                    "scenarios": ["s"],
                    "payoffs": [[0] for _ in opts],
                    "objective": "maximize",
                }
            )

    def test_malformed_payoffs(self):
        with self.assertRaises(ValueError):
            scenario_regret.run(
                {
                    "options": ["a"],
                    "scenarios": ["s"],
                    "payoffs": [1],
                    "objective": "maximize",
                }
            )

    def test_not_object(self):
        with self.assertRaises(ValueError):
            scenario_regret.run(None)


if __name__ == "__main__":
    unittest.main()
