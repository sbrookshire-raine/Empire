"""Independent tests for forecast_baseline. Import by module name."""
import math
import unittest

from local_forecast_baseline import kernel as forecast_baseline


class ForecastBaselineTests(unittest.TestCase):
    def test_sample_matches_expected(self):
        self.assertEqual(
            forecast_baseline.run(forecast_baseline.SAMPLE), forecast_baseline.EXPECTED
        )

    def test_schema_bounds(self):
        self.assertFalse(forecast_baseline.SCHEMA.get("additionalProperties", True))
        self.assertEqual(forecast_baseline.SCHEMA["properties"]["series"]["maxItems"], 2000)

    def test_unknown_keys(self):
        payload = dict(forecast_baseline.SAMPLE)
        payload["ci"] = 0.95
        with self.assertRaises(ValueError) as ctx:
            forecast_baseline.run(payload)
        self.assertIn("unknown keys", str(ctx.exception))

    def test_bool_observation_rejected(self):
        with self.assertRaises(ValueError):
            forecast_baseline.run({"series": [1.0, True, 3.0], "method": "naive", "holdout": 1})

    def test_nan_rejected(self):
        with self.assertRaises(ValueError):
            forecast_baseline.run({"series": [1.0, math.nan], "method": "naive", "holdout": 1})

    def test_inf_rejected(self):
        with self.assertRaises(ValueError):
            forecast_baseline.run({"series": [1.0, math.inf], "method": "naive", "holdout": 1})

    def test_holdout_bool_rejected(self):
        with self.assertRaises(ValueError):
            forecast_baseline.run({"series": [1.0, 2.0], "method": "naive", "holdout": True})

    def test_holdout_too_large(self):
        with self.assertRaises(ValueError):
            forecast_baseline.run({"series": [1.0, 2.0], "method": "naive", "holdout": 2})

    def test_mean_no_leakage(self):
        out = forecast_baseline.run(
            {"series": [1.0, 3.0, 5.0, 100.0], "method": "mean", "holdout": 1}
        )
        self.assertEqual(out["n_train"], 3)
        self.assertEqual(out["forecast"], [3.0])
        self.assertEqual(out["mae"], 97.0)

    def test_drift(self):
        out = forecast_baseline.run(
            {"series": [1.0, 2.0, 3.0, 4.0], "method": "drift", "holdout": 2}
        )
        self.assertEqual(out["forecast"], [3.0, 4.0])
        self.assertEqual(out["holdout_actual"], [3.0, 4.0])
        self.assertEqual(out["mae"], 0.0)

    def test_drift_needs_two_train(self):
        with self.assertRaises(ValueError):
            forecast_baseline.run({"series": [1.0, 2.0], "method": "drift", "holdout": 1})

    def test_seasonal_naive(self):
        out = forecast_baseline.run(
            {
                "series": [10.0, 20.0, 30.0, 11.0, 21.0, 31.0],
                "method": "seasonal_naive",
                "holdout": 3,
                "season": 3,
            }
        )
        self.assertEqual(out["forecast"], [10.0, 20.0, 30.0])
        self.assertEqual(out["mae"], 1.0)

    def test_season_only_for_seasonal(self):
        with self.assertRaises(ValueError):
            forecast_baseline.run(
                {"series": [1.0, 2.0, 3.0], "method": "naive", "holdout": 1, "season": 2}
            )

    def test_season_required(self):
        with self.assertRaises(ValueError):
            forecast_baseline.run(
                {"series": [1.0, 2.0, 3.0, 4.0], "method": "seasonal_naive", "holdout": 1}
            )

    def test_season_too_large(self):
        with self.assertRaises(ValueError):
            forecast_baseline.run(
                {
                    "series": [1.0, 2.0, 3.0],
                    "method": "seasonal_naive",
                    "holdout": 1,
                    "season": 3,
                }
            )

    def test_too_many_obs(self):
        with self.assertRaises(ValueError):
            forecast_baseline.run(
                {"series": [0.0] * 2001, "method": "naive", "holdout": 1}
            )

    def test_invalid_method(self):
        with self.assertRaises(ValueError):
            forecast_baseline.run({"series": [1.0, 2.0], "method": "arima", "holdout": 1})

    def test_series_not_array(self):
        with self.assertRaises(ValueError):
            forecast_baseline.run({"series": 1.0, "method": "naive", "holdout": 1})

    def test_holdout_float_rejected(self):
        with self.assertRaises(ValueError):
            forecast_baseline.run({"series": [1.0, 2.0, 3.0], "method": "naive", "holdout": 1.0})


if __name__ == "__main__":
    unittest.main()
