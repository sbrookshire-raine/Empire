---
name: bayes-update
description: Use when the user asks to update categorical hypothesis probabilities using explicitly supplied priors and likelihoods.
---

# Update finite hypotheses from supplied priors and likelihoods

1. Read `docs/specification.md` and `mcp/input-schema.json`; require explicit user-supplied analytical assumptions. Done when inputs satisfy the documented bounds.
2. Use the installed CLI `bayes-update run` with JSON on stdin, or the registered `bayes_update` MCP tool. Done when a structured result or validation error is returned.
3. Interpret results with `docs/limitations-and-threat-model.md`. State the assumptions and avoid claims of causal proof or validated real-world prediction. Done when output and caveats are reported together.
