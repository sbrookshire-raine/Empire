---
name: rea_analyze_javascript
toolbelt: rea
one_line: Statically analyze a local JavaScript/Electron app directory with REA
---

# rea_analyze_javascript

Run REA's `analyze_javascript_application` on a local folder or ASAR path.

## When to use

- Inspect how an Electron or web-packaged app is structured without source.
- Trace modules, imports, and IPC boundaries before implementing a similar feature.

## Parameters

- `path` — Absolute path to the app root on this PC (Windows paths OK).

## Notes

Registered by the Toolbelt category `rea`. Evidence is written under `REA_EVIDENCE_ROOT` (default `C:/Empire_Workbench/04_Thought_Experiments/rea_cache`). Does not upload targets. Label conclusions with evidence limits REA returns.
