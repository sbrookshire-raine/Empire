---
name: forecast-baseline
description: Use when the user asks for naive, mean, drift, or seasonal-naive forecasts and chronological holdout evaluation.
---

# Produce transparent univariate forecast baselines

1. Read `docs/specification.md` and `mcp/input-schema.json`; require explicit user-supplied analytical assumptions. Done when inputs satisfy the documented bounds.
2. Use the installed CLI `forecast-baseline run` with JSON on stdin, or the registered `forecast_baseline` MCP tool. Done when a structured result or validation error is returned.
3. Interpret results with `docs/limitations-and-threat-model.md`. State the assumptions and avoid claims of causal proof or validated real-world prediction. Done when output and caveats are reported together.
