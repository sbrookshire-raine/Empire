"""Independent tests for bayes_update. Import by module name."""
import math
import unittest

from local_bayes_update import kernel as bayes_update


class BayesUpdateTests(unittest.TestCase):
    def test_sample_matches_expected(self):
        self.assertEqual(bayes_update.run(bayes_update.SAMPLE), bayes_update.EXPECTED)

    def test_schema_bounds(self):
        self.assertFalse(bayes_update.SCHEMA.get("additionalProperties", True))
        self.assertEqual(bayes_update.SCHEMA["properties"]["hypotheses"]["maxItems"], 64)

    def test_unknown_keys(self):
        payload = dict(bayes_update.SAMPLE)
        payload["causal"] = True
        with self.assertRaises(ValueError) as ctx:
            bayes_update.run(payload)
        self.assertIn("unknown keys", str(ctx.exception))

    def test_bool_prior_rejected(self):
        with self.assertRaises(ValueError):
            bayes_update.run(
                {"hypotheses": ["h"], "prior": [True], "likelihood": [1.0]}
            )

    def test_nan_likelihood_rejected(self):
        with self.assertRaises(ValueError):
            bayes_update.run(
                {"hypotheses": ["a", "b"], "prior": [0.5, 0.5], "likelihood": [math.nan, 1.0]}
            )

    def test_inf_prior_rejected(self):
        with self.assertRaises(ValueError):
            bayes_update.run(
                {"hypotheses": ["a", "b"], "prior": [math.inf, 0.0], "likelihood": [1.0, 1.0]}
            )

    def test_zero_evidence_rejected(self):
        with self.assertRaises(ValueError) as ctx:
            bayes_update.run(
                {"hypotheses": ["a", "b"], "prior": [1.0, 0.0], "likelihood": [0.0, 1.0]}
            )
        self.assertIn("zero evidence", str(ctx.exception))

    def test_prior_must_sum_to_one(self):
        with self.assertRaises(ValueError):
            bayes_update.run(
                {"hypotheses": ["a", "b"], "prior": [0.2, 0.2], "likelihood": [1.0, 1.0]}
            )

    def test_negative_prior(self):
        with self.assertRaises(ValueError):
            bayes_update.run(
                {"hypotheses": ["a", "b"], "prior": [-0.1, 1.1], "likelihood": [1.0, 1.0]}
            )

    def test_negative_likelihood(self):
        with self.assertRaises(ValueError):
            bayes_update.run(
                {"hypotheses": ["a", "b"], "prior": [0.5, 0.5], "likelihood": [-0.1, 1.0]}
            )

    def test_length_mismatch(self):
        with self.assertRaises(ValueError):
            bayes_update.run(
                {"hypotheses": ["a", "b"], "prior": [1.0], "likelihood": [1.0, 1.0]}
            )

    def test_duplicate_hypothesis(self):
        with self.assertRaises(ValueError):
            bayes_update.run(
                {"hypotheses": ["a", "a"], "prior": [0.5, 0.5], "likelihood": [1.0, 1.0]}
            )

    def test_too_many_hypotheses(self):
        hyps = ["h%d" % i for i in range(65)]
        with self.assertRaises(ValueError):
            bayes_update.run(
                {
                    "hypotheses": hyps,
                    "prior": [1.0 / 65.0] * 65,
                    "likelihood": [1.0] * 65,
                }
            )

    def test_posterior_sums_to_one(self):
        out = bayes_update.run(
            {"hypotheses": ["a", "b", "c"], "prior": [0.2, 0.3, 0.5], "likelihood": [1.0, 2.0, 0.0]}
        )
        self.assertAlmostEqual(sum(out["posterior"]), 1.0)
        self.assertEqual(out["map_hypothesis"], "b")
        self.assertEqual(out["assumption"], "finite categorical update; not causal identification")

    def test_map_tie_lexicographic(self):
        out = bayes_update.run(
            {"hypotheses": ["z", "a"], "prior": [0.5, 0.5], "likelihood": [1.0, 1.0]}
        )
        self.assertEqual(out["map_hypothesis"], "a")

    def test_not_object(self):
        with self.assertRaises(ValueError):
            bayes_update.run("nope")

    def test_malformed_arrays(self):
        with self.assertRaises(ValueError):
            bayes_update.run({"hypotheses": "a", "prior": [1.0], "likelihood": [1.0]})


if __name__ == "__main__":
    unittest.main()
