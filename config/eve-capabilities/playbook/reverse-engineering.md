---
area: reverse-engineering
one_line: Local reverse engineering via REA (JS/Electron, native, web, .NET).
tools: rea_doctor, rea_analyze_javascript, rea_invoke
skills: skill-reverse-engineering
---

# Reverse engineering (REA)

Enable **REA** on the Toolbelt (session limb) before any `rea_*` tool. Analysis runs locally; targets must be paths the Architect owns or approves.

## JavaScript / Electron

- **Ask:** "how is the preload bridge wired in this Electron app?" → **Do:** `rea_doctor()` → `rea_analyze_javascript("C:/path/to/app")` → **Get:** modules, imports, and evidence JSON (summarize; do not dump the whole bundle into chat).
- **Ask:** "run a specific REA native inspect on this EXE" → **Do:** `rea_doctor()` → `rea_invoke("inspect", { ... })` per REA schema → **Get:** structured evidence or a clear unavailable reason.

## Readiness

- **Ask:** "is reverse engineering set up on this machine?" → **Do:** `rea_doctor()` → **Get:** Node OK / missing Ghidra or Hopper / remediation strings.
