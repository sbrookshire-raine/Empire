---
name: thought-map
description: Use when the user asks to inspect signed influence graphs, feedback structure, or strongly connected components.
---

# Analyze a supplied signed directed graph

1. Read `docs/specification.md` and `mcp/input-schema.json`; require explicit user-supplied analytical assumptions. Done when inputs satisfy the documented bounds.
2. Use the installed CLI `thought-map run` with JSON on stdin, or the registered `thought_map` MCP tool. Done when a structured result or validation error is returned.
3. Interpret results with `docs/limitations-and-threat-model.md`. State the assumptions and avoid claims of causal proof or validated real-world prediction. Done when output and caveats are reported together.
