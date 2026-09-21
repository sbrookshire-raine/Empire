"""bayes_update: finite categorical Bayes update from prior and likelihood.

Original generated implementation. License: MIT.
Not causal identification. Zero evidence is rejected.
"""
from __future__ import annotations

import math

SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "bayes_update_input",
    "type": "object",
    "additionalProperties": False,
    "required": ["hypotheses", "prior", "likelihood"],
    "properties": {
        "hypotheses": {
            "type": "array",
            "minItems": 1,
            "maxItems": 64,
            "items": {"type": "string", "minLength": 1, "maxLength": 64},
        },
        "prior": {
            "type": "array",
            "minItems": 1,
            "maxItems": 64,
            "items": {"type": "number"},
        },
        "likelihood": {
            "type": "array",
            "minItems": 1,
            "maxItems": 64,
            "items": {"type": "number"},
        },
    },
}

MAX_HYP = 64
MAX_NAME = 64
PRIOR_SUM_TOL = 1e-12

SAMPLE = {
    "hypotheses": ["rain", "dry"],
    "prior": [0.5, 0.5],
    "likelihood": [0.8, 0.2],
}

EXPECTED = {
    "hypotheses": ["rain", "dry"],
    "prior": [0.5, 0.5],
    "likelihood": [0.8, 0.2],
    "unnormalized": [0.4, 0.1],
    "evidence": 0.5,
    "posterior": [0.8, 0.2],
    "map_hypothesis": "rain",
    "map_probability": 0.8,
    "assumption": "finite categorical update; not causal identification",
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


def _validate(data: object) -> tuple:
    obj = _require_dict(data, "input")
    extra = set(obj) - {"hypotheses", "prior", "likelihood"}
    if extra:
        _err("unknown keys: %s" % ", ".join(sorted(extra)))
    for key in ("hypotheses", "prior", "likelihood"):
        if key not in obj:
            _err("%s is required" % key)
    hyp_raw = obj["hypotheses"]
    prior_raw = obj["prior"]
    like_raw = obj["likelihood"]
    if type(hyp_raw) is not list:
        _err("hypotheses must be an array")
    if type(prior_raw) is not list:
        _err("prior must be an array")
    if type(like_raw) is not list:
        _err("likelihood must be an array")
    if not hyp_raw:
        _err("hypotheses must be non-empty")
    if len(hyp_raw) > MAX_HYP:
        _err("at most %d hypotheses" % MAX_HYP)
    hypotheses = []
    seen = set()
    for i, item in enumerate(hyp_raw):
        name = _require_str(item, "hypotheses[%d]" % i)
        if name in seen:
            _err("duplicate hypothesis %s" % name)
        seen.add(name)
        hypotheses.append(name)
    if len(prior_raw) != len(hypotheses):
        _err("prior length must match hypotheses")
    if len(like_raw) != len(hypotheses):
        _err("likelihood length must match hypotheses")
    prior = []
    for i, v in enumerate(prior_raw):
        p = _require_num(v, "prior[%d]" % i)
        if p < 0.0:
            _err("prior[%d] must be >= 0" % i)
        prior.append(p)
    likelihood = []
    for i, v in enumerate(like_raw):
        ell = _require_num(v, "likelihood[%d]" % i)
        if ell < 0.0:
            _err("likelihood[%d] must be >= 0" % i)
        likelihood.append(ell)
    prior_sum = sum(prior)
    if abs(prior_sum - 1.0) > PRIOR_SUM_TOL:
        _err("prior must sum to 1")
    return hypotheses, prior, likelihood


def run(data):
    hypotheses, prior, likelihood = _validate(data)
    unnormalized = [prior[i] * likelihood[i] for i in range(len(hypotheses))]
    evidence = sum(unnormalized)
    if evidence == 0.0:
        _err("zero evidence; posterior undefined")
    posterior = [u / evidence for u in unnormalized]
    map_i = 0
    for i in range(1, len(posterior)):
        if posterior[i] > posterior[map_i]:
            map_i = i
        elif posterior[i] == posterior[map_i] and hypotheses[i] < hypotheses[map_i]:
            map_i = i
    return {
        "hypotheses": hypotheses,
        "prior": prior,
        "likelihood": likelihood,
        "unnormalized": unnormalized,
        "evidence": evidence,
        "posterior": posterior,
        "map_hypothesis": hypotheses[map_i],
        "map_probability": posterior[map_i],
        "assumption": "finite categorical update; not causal identification",
    }
