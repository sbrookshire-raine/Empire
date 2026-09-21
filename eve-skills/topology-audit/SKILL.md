---
name: topology-audit
description: Use when the user asks to analyze supplied system dependencies or the transitive impact of one component outage.
---

# Analyze declared dependencies and outage propagation

1. Read `docs/specification.md` and `mcp/input-schema.json`; require explicit user-supplied analytical assumptions. Done when inputs satisfy the documented bounds.
2. Use the installed CLI `topology-audit run` with JSON on stdin, or the registered `topology_audit` MCP tool. Done when a structured result or validation error is returned.
3. Interpret results with `docs/limitations-and-threat-model.md`. State the assumptions and avoid claims of causal proof or validated real-world prediction. Done when output and caveats are reported together.
