---
name: rea_invoke
toolbelt: rea
one_line: Call any REA MCP tool by name (native, web, .NET, firmware, …)
---

# rea_invoke

Forward to REA's MCP tool surface (139 tools when REA 6.x is installed).

## When to use

- After `rea_doctor` and optional `binary_session` to pick an available tool.
- Native inspect/decompile, web capture, managed assemblies, firmware, etc.

## Parameters

- `tool` — REA MCP tool name (e.g. `inspect`, `decompile`, `capture_browser_scenario`).
- `arguments` — JSON object of arguments for that tool (default `{}`). Use `binary_session` via tool name `binary_session` for catalog and availability.

## Notes

Registered by the Toolbelt category `rea`. Prefer curated tools (`rea_analyze_javascript`) when they fit. Never analyze paths outside Architect-approved targets. Local-only.
