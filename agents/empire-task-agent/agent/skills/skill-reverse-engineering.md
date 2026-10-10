# Skill: Reverse engineering (REA)

Use when the Architect wants to **understand how software works without source** — JavaScript/Electron apps, native binaries, web bundles, or .NET assemblies — on **this PC only**.

## Rules

1. Enable the **REA** Toolbelt limb (or succeed at `admit_for_goal("rea")`) before calling `rea_*` tools.
2. Call **`rea_doctor`** first on a cold start or after errors.
3. Prefer **`rea_analyze_javascript`** for local JS/Electron folders; use **`rea_invoke`** for other REA tools once `binary_session` shows availability.
4. Only analyze paths the Architect named. Do not scan system directories or third-party installs without explicit approval.
5. Summarize evidence; cite REA limitations from the tool result. Never claim you uploaded the target.

## Routing

| Intent | Tool |
|--------|------|
| Is REA ready? | `rea_doctor` |
| JS/Electron app folder | `rea_analyze_javascript` |
| Other REA capability | `rea_invoke` |

Reference: [docs/REA_LIMB.md](../../../../docs/REA_LIMB.md) in the EMPIRE repo.
