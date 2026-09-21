---
name: scenario-regret
description: Use when the user asks to compare options across supplied scenarios using minimax regret.
---

# Rank decisions using minimax regret

1. Read `docs/specification.md` and `mcp/input-schema.json`; require explicit user-supplied analytical assumptions. Done when inputs satisfy the documented bounds.
2. Use the installed CLI `scenario-regret run` with JSON on stdin, or the registered `scenario_regret` MCP tool. Done when a structured result or validation error is returned.
3. Interpret results with `docs/limitations-and-threat-model.md`. State the assumptions and avoid claims of causal proof or validated real-world prediction. Done when output and caveats are reported together.
