# Skill: Reverse engineering (REA)

Use when the Architect wants to **understand how software works without source** — JavaScript/Electron apps, native binaries, web bundles, games, audio pipelines — on **this PC only**.

## Rules

1. Call **`rea_doctor`** first on a cold start or after errors (auto-admits REA when headroom allows).
2. Prefer **`rea_analyze_javascript`** for local JS/Electron folders; use **`rea_invoke`** for other REA tools once `binary_session` shows availability.
3. After a **serious play session**, write exactly one **`disassembly_card_write`** with 3–7 **connections** and **evidence_refs** pointing at local paths only.
4. Ask the Architect before **`disassembly_publish_heptabase`** — must pass `architect_confirm: true`. Heptabase desktop app must be running.
5. After **`confirm_remember`**, offer **`disassembly_mark_mature`** (`architect_confirm: true`) to turn the board card green.
6. Only analyze paths the Architect named or uploaded. Do not scan system directories without explicit approval.
7. Summarize evidence; cite REA limitations from tool results. Never claim you uploaded the target off-machine.

## Routing

| Intent | Tool |
|--------|------|
| Is REA ready? | `rea_doctor` |
| JS/Electron app folder | `rea_analyze_javascript` |
| Chat/upload inbox | `rea_list_inbox` |
| End-of-session catalog | `disassembly_card_write` → `disassembly_publish_heptabase` |
| Visual UI (HTML/local) | `app_visual_observe` |
| Other REA capability | `rea_invoke` |

Reference: [docs/REA_LIMB.md](../../../../docs/REA_LIMB.md), [docs/DISASSEMBLY_CATALOG.md](../../../../docs/DISASSEMBLY_CATALOG.md).
