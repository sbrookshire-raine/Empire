---
area: reverse-engineering
one_line: Local reverse engineering via REA (JS/Electron, native, web, .NET) + Disassembly catalog.
tools: rea_doctor, rea_list_inbox, rea_analyze_javascript, rea_invoke, rea_skills, claim_ledger, disassembly_card_write, disassembly_card_list, disassembly_publish_heptabase, disassembly_mark_mature, app_visual_observe, browser_capture_screenshot, heptabase_health
skills: skill-reverse-engineering, skill-rea-skills, skill-claim-ledger
---

# Reverse engineering (REA)

Architect can **attach files in chat** (📎) — zips, EXE, DLL, ASAR, JS, etc. Paths land under `rea_inbox`; use `rea_list_inbox` when needed.

## REA analysis and readiness

- **Ask:** "is reverse engineering set up?" → **Do:** `rea_doctor()` → **Get:** Node OK / missing Ghidra / remediation.
- **Ask:** "analyze this Electron folder" → **Do:** `rea_analyze_javascript("C:/path")` after upload → **Get:** module graph summary.
- **Ask:** "inspect this native EXE" → **Do:** `rea_doctor()` → `rea_invoke("inspect", …)` → **Get:** evidence or unavailable reason.
- **Ask:** "what did we upload for RE?" → **Do:** `rea_list_inbox()` → **Get:** upload ids and `analysis_roots`.

## REA skills — proving a finding (local, offline)

Six skills from the Gumloop REA bundle, vendored under `vendor/rea-skills/`. They
*prove* things instead of asserting them.

- **Ask:** "is this evidence good enough to report?" → **Do:** `rea_skills(action="verify_evidence", files=[…])` → **Get:** a pass/fail audit of the record and the claims resting on it.
- **Ask:** "is this reconstruction actually correct?" → **Do:** `rea_skills(action="audit_reconstruction", config_dir=…)` → **Get:** per-check ledger audit (exact matches, digests, duplicates).
- **Ask:** "does my rebuild match the original?" → **Do:** `rea_skills(action="parity_check", reference="…", candidate="…", scenarios=…)` → **Get:** a parity report — both programs scored separately against frozen literals.
- **Ask:** "what can I read from this binary without a disassembler?" → **Do:** `rea_skills(action="build_fixtures")` → **Get:** local reader fixtures (Go/Rust/WASM/EVM/SQLite).
- **Ask:** "what have people actually built from this repo?" → **Do:** `rea_skills(action="forkdive", repo="OWNER/REPO")` → **Get:** proven use cases from its fork network (needs network).
- **Ask:** "which repos in this domain are worth reading?" → **Do:** `rea_skills(action="discover", topics=[…])` → **Get:** high-signal repos by topic and stars (needs network).
- **Ask:** "which REA skills can I actually run here?" → **Do:** `rea_skills(action="list")` → **Get:** the six approved skills, their scripts, and which need the network.

## Claim ledger — knowledge that is done, not read

Records a claim together with the command that would prove it wrong, so it
cannot go stale silently.

- **Ask:** "remember that X is true" → **Do:** `claim_ledger(action="add", claim="X", check_cmd="…")` → **Get:** the slug, and whether it is a document (no check) or a capability.
- **Ask:** "is that still true?" → **Do:** `claim_ledger(action="verify", slug=…)` → **Get:** pass/fail per claim with the output. A failure is the finding — report it.
- **Ask:** "how much of this can I trust?" → **Do:** `claim_ledger(action="health")` → **Get:** the fraction of claims that have a check and pass, plus a verdict.
- **Ask:** "what still needs a check?" → **Do:** `claim_ledger(action="list", unchecked=true)` → **Get:** the documents — the honest work queue.
- **Ask:** "what is known-false?" → **Do:** `claim_ledger(action="list", failing=true)` → **Get:** claims whose check failed.

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
