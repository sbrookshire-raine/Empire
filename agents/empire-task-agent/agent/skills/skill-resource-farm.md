# Skill: Resource farm (GitHub → scout catalog)

Use when the Architect wants **processed GitHub materials** as a **fluid scratch catalog** — not Cognee memory — so Eve can later analyze clones from Resource Queue or compare repos at a glance on Heptabase.

## Triggers (no long prompt required)

- "Farm resources", "resource farm", "grow the scout catalog", "process GitHub for X"
- "What repos have we already farmed?", "show the processed materials catalog"
- After triage: "turn those GitHub hits into disassembly cards"

## One action

Call **`resource_farm_run`** once per request:

| Architect intent | Tool call |
|------------------|-----------|
| Status only | `resource_farm_run()` — no `query` |
| Farm new repos | `resource_farm_run({ query: "<terms>", max_new_cards: 5 })` |
| Farm + show on Heptabase board | Same, plus `architect_confirm: true` (Architect said yes **this turn**) |

Do **not** chain manual `github_scout_search` → `disassembly_card_write` unless the farm tool failed; the pipeline dedupes by repo slug and writes consistent scout tickets.

## Rules

1. **Never** `propose_remember` / `confirm_remember` unless the Architect explicitly asks to promote into Cognee.
2. **Never** clone, install, or run third-party repos from this skill — cards point at README cache + URL; REA waits for Resource Queue.
3. **Heptabase logic (built into the tool):**
   - New scout cards publish as **orange** only when `architect_confirm: true`, board id is configured, and desktop CLI is healthy.
   - If board is down or confirm missing, cards still land under `04_Thought_Experiments/disassembly_cards/` — report `heptabase.reason` from the tool result.
   - Do not call `disassembly_publish_heptabase` one-by-one after a successful farm with confirm unless the tool reported publish errors for specific cards.
4. After a farm run, reply with a **short table**: repo, `dc_*` id, skipped/already farmed, and next step (clone path vs REA).
5. For deep truth on code, hand off to **skill-reverse-engineering** after material is in `00_Resource_Queue`.

## Artefacts

- GitHub cache: `C:/Empire_Workbench/04_Thought_Experiments/github_cache/`
- Scout cards: `C:/Empire_Workbench/04_Thought_Experiments/disassembly_cards/` (`farm_kind: scout`, `source_repo: owner/name`)
- Visual catalog: EMPIRE Disassembly Catalog whiteboard (optional)

Reference: [docs/DISASSEMBLY_CATALOG.md](../../../../docs/DISASSEMBLY_CATALOG.md), [docs/REA_LIMB.md](../../../../docs/REA_LIMB.md).
