"""forecast_baseline: chronological holdout MAE for simple baseline forecasts.

Original generated implementation. License: MIT.
No confidence intervals, no calibration claims, no leakage from holdout.
"""
from __future__ import annotations

import math

SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "forecast_baseline_input",
    "type": "object",
    "additionalProperties": False,
    "required": ["series", "method", "holdout"],
    "properties": {
        "series": {
            "type": "array",
            "minItems": 2,
            "maxItems": 2000,
            "items": {"type": "number"},
        },
        "method": {
            "type": "string",
            "enum": ["naive", "mean", "drift", "seasonal_naive"],
        },
        "holdout": {"type": "integer", "minimum": 1, "maximum": 1998},
        "season": {"type": "integer", "minimum": 2, "maximum": 1998},
    },
}

MAX_OBS = 2000

SAMPLE = {
    "series": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
    "method": "naive",
    "holdout": 2,
}

EXPECTED = {
    "method": "naive",
    "n_obs": 6,
    "n_train": 4,
    "n_holdout": 2,
    "forecast": [4.0, 4.0],
    "holdout_actual": [5.0, 6.0],
    "mae": 1.5,
}


def _err(msg: str) -> None:
    raise ValueError(msg)


def _require_dict(data: object, label: str) -> dict:
    if type(data) is not dict:
        _err("%s must be an object" % label)
    return data


def _require_num(value: object, label: str) -> float:
    if type(value) is bool or type(value) not in (int, float):
        _err("%s must be a finite number" % label)
    number = float(value)
    if not math.isfinite(number):
        _err("%s must be a finite number" % label)
    return number


def _require_int(value: object, label: str) -> int:
    if type(value) is bool or type(value) is not int:
        _err("%s must be an integer" % label)
    return value


def _validate(data: object) -> tuple:
    obj = _require_dict(data, "input")
    extra = set(obj) - {"series", "method", "holdout", "season"}
    if extra:
        _err("unknown keys: %s" % ", ".join(sorted(extra)))
    for key in ("series", "method", "holdout"):
        if key not in obj:
            _err("%s is required" % key)
    series_raw = obj["series"]
    if type(series_raw) is not list:
        _err("series must be an array")
    if len(series_raw) < 2:
        _err("series must have at least 2 observations")
    if len(series_raw) > MAX_OBS:
        _err("at most %d observations" % MAX_OBS)
    series = [_require_num(v, "series[%d]" % i) for i, v in enumerate(series_raw)]
    method = obj["method"]
    if type(method) is not str or method not in ("naive", "mean", "drift", "seasonal_naive"):
        _err("method must be naive, mean, drift, or seasonal_naive")
    holdout = _require_int(obj["holdout"], "holdout")
    if holdout < 1:
        _err("holdout must be >= 1")
    n = len(series)
    n_train = n - holdout
    if n_train < 1:
        _err("holdout must leave at least 1 training observation")
    if method == "drift" and n_train < 2:
        _err("drift requires at least 2 training observations")
    season = None
    if method == "seasonal_naive":
        if "season" not in obj:
            _err("season is required for seasonal_naive")
        season = _require_int(obj["season"], "season")
        if season < 2:
            _err("season must be >= 2")
        if season > n_train:
            _err("season must be <= training length")
    elif "season" in obj:
        _err("season is only allowed for seasonal_naive")
    return series, method, holdout, season, n_train


def _forecast(train: list, method: str, holdout: int, season: object) -> list:
    last = train[-1]
    if method == "naive":
        return [last] * holdout
    if method == "mean":
        mu = sum(train) / float(len(train))
        return [mu] * holdout
    if method == "drift":
        slope = (train[-1] - train[0]) / float(len(train) - 1)
        return [last + slope * (k + 1) for k in range(holdout)]
    out = []
    for k in range(holdout):
        idx = len(train) - season + (k % season)
        out.append(train[idx])
    return out


def run(data):
    series, method, holdout, season, n_train = _validate(data)
    train = series[:n_train]
    actual = series[n_train:]
    forecast = _forecast(train, method, holdout, season)
    mae = sum(abs(forecast[i] - actual[i]) for i in range(holdout)) / float(holdout)
    return {
        "method": method,
        "n_obs": len(series),
        "n_train": n_train,
        "n_holdout": holdout,
        "forecast": forecast,
        "holdout_actual": actual,
        "mae": mae,
    }
