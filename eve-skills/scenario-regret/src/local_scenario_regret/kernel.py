"""scenario_regret: minimax regret ranking of options across scenarios.

Original generated implementation. License: MIT.
No probability weights. No causal claims.
"""
from __future__ import annotations

import math

SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "scenario_regret_input",
    "type": "object",
    "additionalProperties": False,
    "required": ["options", "scenarios", "payoffs", "objective"],
    "properties": {
        "options": {
            "type": "array",
            "minItems": 1,
            "maxItems": 64,
            "items": {"type": "string", "minLength": 1, "maxLength": 64},
        },
        "scenarios": {
            "type": "array",
            "minItems": 1,
            "maxItems": 64,
            "items": {"type": "string", "minLength": 1, "maxLength": 64},
        },
        "payoffs": {
            "type": "array",
            "minItems": 1,
            "maxItems": 64,
            "items": {
                "type": "array",
                "minItems": 1,
                "maxItems": 64,
                "items": {"type": "number"},
            },
        },
        "objective": {"type": "string", "enum": ["maximize", "minimize"]},
    },
}

MAX_DIM = 64
MAX_NAME = 64

SAMPLE = {
    "options": ["alpha", "beta"],
    "scenarios": ["s1", "s2"],
    "payoffs": [[10, 0], [5, 6]],
    "objective": "maximize",
}

EXPECTED = {
    "objective": "maximize",
    "regret": [
        {"option": "alpha", "regrets": [0.0, 6.0], "max_regret": 6.0},
        {"option": "beta", "regrets": [5.0, 0.0], "max_regret": 5.0},
    ],
    "ranking": [
        {"rank": 1, "option": "beta", "max_regret": 5.0, "regrets": [5.0, 0.0]},
        {"rank": 2, "option": "alpha", "max_regret": 6.0, "regrets": [0.0, 6.0]},
    ],
}


def _err(msg: str) -> None:
    raise ValueError(msg)


def _require_dict(data: object, label: str) -> dict:
    if type(data) is not dict:
        _err("%s must be an object" % label)
    return data


def _require_str(value: object, label: str) -> str:
    if type(value) is not str:
        _err("%s must be a string" % label)
    if not value or len(value) > MAX_NAME or value != value.strip():
        _err("%s must be a non-empty trimmed string of length 1..%d" % (label, MAX_NAME))
    return value


def _require_num(value: object, label: str) -> float:
    if type(value) is bool or type(value) not in (int, float):
        _err("%s must be a finite number" % label)
    number = float(value)
    if not math.isfinite(number):
        _err("%s must be a finite number" % label)
    return number


def _unique_names(raw: object, label: str) -> list:
    if type(raw) is not list:
        _err("%s must be an array" % label)
    if not raw:
        _err("%s must be non-empty" % label)
    if len(raw) > MAX_DIM:
        _err("%s at most %d items" % (label, MAX_DIM))
    names = []
    seen = set()
    for i, item in enumerate(raw):
        name = _require_str(item, "%s[%d]" % (label, i))
        if name in seen:
            _err("duplicate %s %s" % (label, name))
        seen.add(name)
        names.append(name)
    return names


def _validate(data: object) -> tuple:
    obj = _require_dict(data, "input")
    extra = set(obj) - {"options", "scenarios", "payoffs", "objective"}
    if extra:
        _err("unknown keys: %s" % ", ".join(sorted(extra)))
    for key in ("options", "scenarios", "payoffs", "objective"):
        if key not in obj:
            _err("%s is required" % key)
    options = _unique_names(obj["options"], "options")
    scenarios = _unique_names(obj["scenarios"], "scenarios")
    objective = obj["objective"]
    if type(objective) is not str or objective not in ("maximize", "minimize"):
        _err("objective must be maximize or minimize")
    payoffs_raw = obj["payoffs"]
    if type(payoffs_raw) is not list:
        _err("payoffs must be an array")
    if len(payoffs_raw) != len(options):
        _err("payoffs must have one row per option")
    matrix = []
    for i, row in enumerate(payoffs_raw):
        if type(row) is not list:
            _err("payoffs[%d] must be an array" % i)
        if len(row) != len(scenarios):
            _err("payoffs[%d] must have one value per scenario" % i)
        matrix.append([_require_num(v, "payoffs[%d][%d]" % (i, j)) for j, v in enumerate(row)])
    return options, scenarios, matrix, objective


def run(data):
    options, scenarios, matrix, objective = _validate(data)
    n_opt = len(options)
    n_scn = len(scenarios)
    reference = []
    for j in range(n_scn):
        col = [matrix[i][j] for i in range(n_opt)]
        reference.append(max(col) if objective == "maximize" else min(col))
    regret_rows = []
    for i, opt in enumerate(options):
        if objective == "maximize":
            regrets = [reference[j] - matrix[i][j] for j in range(n_scn)]
        else:
            regrets = [matrix[i][j] - reference[j] for j in range(n_scn)]
        regret_rows.append(
            {
                "option": opt,
                "regrets": regrets,
                "max_regret": max(regrets),
            }
        )
    indexed = list(enumerate(regret_rows))
    indexed.sort(key=lambda it: (it[1]["max_regret"], it[1]["regrets"], it[0]))
    ranking = []
    for rank, (_orig, row) in enumerate(indexed, start=1):
        ranking.append(
            {
                "rank": rank,
                "option": row["option"],
                "max_regret": row["max_regret"],
                "regrets": list(row["regrets"]),
            }
        )
    return {
        "objective": objective,
        "regret": regret_rows,
        "ranking": ranking,
    }
