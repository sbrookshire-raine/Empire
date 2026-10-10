---
area: reverse-engineering
one_line: Local reverse engineering via REA (JS/Electron, native, web, .NET) + Disassembly catalog.
tools: rea_doctor, rea_list_inbox, rea_analyze_javascript, rea_invoke, disassembly_card_write, disassembly_card_list, disassembly_publish_heptabase, disassembly_mark_mature, app_visual_observe, browser_capture_screenshot, heptabase_health
skills: skill-reverse-engineering
---

# Reverse engineering (REA)

Architect can **attach files in chat** (📎) — zips, EXE, DLL, ASAR, JS, etc. Paths land under `rea_inbox`; use `rea_list_inbox` when needed.

## REA analysis and readiness

- **Ask:** "is reverse engineering set up?" → **Do:** `rea_doctor()` → **Get:** Node OK / missing Ghidra / remediation.
- **Ask:** "analyze this Electron folder" → **Do:** `rea_analyze_javascript("C:/path")` after upload → **Get:** module graph summary.
- **Ask:** "inspect this native EXE" → **Do:** `rea_doctor()` → `rea_invoke("inspect", …)` → **Get:** evidence or unavailable reason.
- **Ask:** "what did we upload for RE?" → **Do:** `rea_list_inbox()` → **Get:** upload ids and `analysis_roots`.

## Disassembly catalog (one card per play)

- **Ask:** after an RE session → **Do:** `disassembly_card_write` (3–7 connections + evidence refs) → **Get:** local `dc_*` id.
- **Ask:** "publish that card to Heptabase" → **Do:** `heptabase_health()` → `disassembly_publish_heptabase(card_id, architect_confirm=true)` → **Get:** orange/blue board placement.
- **Ask:** "we kept that in memory" → **Do:** `disassembly_mark_mature(card_id, architect_confirm=true)` → **Get:** green placement on catalog board.

## Visual, catalog board, and helpers

- **Ask:** "what does this HTML UI look like?" → **Do:** `app_visual_observe(html_path=…)` → **Get:** screenshot + UI regions.
- **Ask:** "list prior disassembly sessions" → **Do:** `disassembly_card_list()` → **Get:** recent cards and stages.
- **Ask:** "screenshot the workbench page" → **Do:** `browser_capture_screenshot(url=http://127.0.0.1:8080/eve.html)` → **Get:** PNG path.
- **Ask:** "is Heptabase wired?" → **Do:** `heptabase_health()` → **Get:** CLI + board id or fix hint.
- **Ask:** "show new RE cards on the board" → **Do:** publish with confirm → **Get:** orange card on EMPIRE Disassembly Catalog.
- **Ask:** "what do the board colors mean?" → **Do:** read [docs/DISASSEMBLY_CATALOG.md](../../../docs/DISASSEMBLY_CATALOG.md) → **Get:** orange publish, blue deps, green mature, purple evolved.
