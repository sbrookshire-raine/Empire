---
area: intake-and-legos
one_line: Web or GitHub → Disassembly Card → optional Heptabase → optional staged memory — one tool.
tools: intake_to_lego_run, resource_farm_run, web_scout, github_scout_search, disassembly_card_list, propose_remember, confirm_remember, rea_doctor, rea_analyze_javascript, heptabase_health
skills: skill-intake-to-lego, skill-resource-farm, skill-reverse-engineering
---

# Intake and building legos

Architect should not run separate shell steps. Eve runs **`intake_to_lego_run`**.

## Web source

- **Ask:** "analyze this docs page and catalog it" → **Do:** `intake_to_lego_run({ kind: "web", url })` → **Get:** `dc_*` + web cache path.
- **Ask:** "…and put it on the board" (same turn) → **Do:** same with `architect_confirm: true` → **Get:** Heptabase orange placement or `publish.reason`.
- **Ask:** "remember the takeaway" → **Do:** `promote_memory: true`; if they said remember explicitly add `promote_confirm: true` + `architect_confirm: true` → **Get:** staging id or `eve_memory` promotion + mature green when published.

## GitHub source

- **Ask:** "find GitHub repos about X and catalog them" → **Do:** `intake_to_lego_run({ kind: "github", query: "X" })` → **Get:** created/skipped repos + card ids.
- **Ask:** "study owner/repo" → **Do:** `intake_to_lego_run({ kind: "github", repo: "owner/repo", depth: "study", architect_confirm: … })` → **Get:** clone under `00_Resource_Queue` + study card.
- **Ask:** "what's already in the catalog?" → **Do:** `intake_to_lego_run({ kind: "github" })` or `resource_farm_run()` → **Get:** `farmed_repos`.

## After scout/study (verified learning)

- **Ask:** "reverse engineer the clone" → **Do:** `playbook("reverse-engineering")` → REA on `local_path` from intake result → update card connections → publish/mature when Architect confirms.
- **Ask:** "what came out of the study for owner/repo?" → **Do:** `intake_to_lego_run({ kind: "github", repo: "owner/repo", depth: "study" })` → **Get:** the study card plus the `local_path` REA needs.
- **Ask:** "is REA ready to run on this machine?" → **Do:** `rea_doctor()` → **Get:** the readiness verdict (Node, engines, config) before any deep call.
- **Ask:** "map the modules in that clone" → **Do:** `rea_analyze_javascript({ path: "<local_path>" })` → **Get:** the module/import/IPC map REA writes to evidence.
- **Ask:** "which cards came out of that repo?" → **Do:** `disassembly_card_list({ limit: 20 })` → **Get:** the card ids to re-open or publish.

## Governance

- Caches and cards are **scratch** until Architect confirms memory.
- No auto-Cognee from wiki/github/web caches without `promote_memory` / confirm flow.
- **Ask:** "catalog it, but keep it out of my memory" → **Do:** `intake_to_lego_run({ kind: "web", url })` with no `promote_memory` → **Get:** a scratch card and a cache path; nothing reaches `eve_memory`.
- **Ask:** "remember the takeaway" → **Do:** `propose_remember({ content, reason })` → **Get:** a staging id in `eve_staging` and a crumb to recall it by.
- **Ask:** "yes, keep that one" → **Do:** `confirm_remember({ entry_id, dataset: "eve_memory" })` → **Get:** the entry promoted to `eve_memory` — only on an explicit keep.
- **Ask:** "what is still sitting in the queue?" → **Do:** `resource_farm_run()` → **Get:** `farmed_repos` — scratch work, never memory on its own.
- **Ask:** "can the board take this card?" → **Do:** `heptabase_health()` → **Get:** board readiness before any orange placement is promised.
