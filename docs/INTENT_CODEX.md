# Intent codex (everyday vocabulary → Eve routes)

The Architect does not say `wiki_scout_search` or `admit_for_goal("web_scout")`. They say
**scrape**, **research**, **look up**, **remember**, **find**, **compare**. The codex is the
**adaptable vocabulary layer** that turns those words into:

1. **What you mean** (`say` — plain English)
2. **Local first or online** (`local_first`, `sequence`)
3. **Which tools and limbs** (`local_tools`, `online_tools`, `limbs`)
4. **Where the worked examples live** (`playbook` area)

It is editable data, not prompt stuffing: `config/eve-capabilities/intent-codex.json`.

## Three layers (how they fit)

| Layer | Tool / mechanism | Job |
|-------|------------------|-----|
| **Codex** | `resolve_intent(message)` + Workbench **pre-router injection** | Map **verbs** → intent policy |
| **Index** | `capability_route(query)` | Map **keywords** → tools / limbs / areas |
| **Depth** | `playbook` + `tool_docs` | How to call and complete the task |

Pre-router: when a user message matches strongly, `serve.py` attaches a compact
`[AUTHORITATIVE INTENT ROUTE]` block next to the ask (same pattern as catalog / ledger blocks).

## Example mappings (built-in)

| You might say | Intent | Local first | Then (if limb on) |
|---------------|--------|-------------|-------------------|
| scrape / fetch this URL | `scrape_gather_web` | — | `web_scout` |
| research / dig into X | `research_deep` | `cognee_recall`, `workspace_search` | `research_start`, `searxng_search` |
| look up / find out | `lookup_general` | `workspace_search`, `cognee_recall` | wiki or web per entity |
| who is / wiki / discography | `wiki_fact` | `wiki_scout_search`, … | — |
| remember (recall) | `remember_recall` | `cognee_recall` | — |
| remember (save) | `save_to_memory` | `propose_remember`, … | — |
| reverse engineer / decompile | `reverse_engineer` | REA tools | admit `rea` |
| query your catalog | `external_catalog` | `search_catalog` | — |

Full list: open `intent-codex.json`.

## Cognee (language barrier / recall)

The Architect's phrasing is also stored for **`cognee_recall`**:

- `data/curated_primitives/raw_materials/architect-intent-vocabulary.md` — session + codex-aligned phrases
- `data/curated_primitives/raw_materials/architect-vault-voice-supplement.md` — Obsidian daily-note voice + Gemini **user** turns (see `docs/audits/2026-09-28-vault-and-dialogue-digest.md`)
- Default dataset: **`eve_memory`**

Refresh vault lines from Obsidian (default **OneDrive SBX_Vault**):

```powershell
.\venv\Scripts\python.exe scripts\harvest-architect-voice-from-vault.py
# optional: $env:EMPIRE_SBX_VAULT = "C:\Users\m69nr\OneDrive\Documents\RESYNC_2026"
```

Seed language bridge (fresh file root + Postgres, no VHDX required):

```powershell
.\scripts\setup-architect-language-memory.ps1
```

Re-ingest vocabulary only:

```powershell
.\scripts\ingest-architect-intent-vocabulary.ps1
```

Eve should recall with queries like *"Architect intent vocabulary"* or *"how the Architect phrases scrape research backup"* before guessing. The JSON codex remains authoritative for routing; Cognee carries nuance and estate-specific phrases.

After bulk ingest, optional: `.\scripts\optimize-eve-memory.ps1` for **`eve_core`**.

## Extend the codex

1. Edit **`config/eve-capabilities/intent-codex.json`** — add `verbs`, `nouns`, `phrases` under an intent, or add a new intent block with `policy`.
2. Run harvest for ideas from playbook asks:

   ```powershell
   .\venv\Scripts\python.exe scripts\harvest-intent-verbs.py
   ```

3. Smoke one message:

   ```powershell
   .\venv\Scripts\python.exe -m pipeline.intent_codex "scrape this page https://example.com"
   ```

4. Rebuild Eve if you only changed JSON (pre-router picks it up on next message; no rebuild required for injection). Rebuild after TypeScript tool changes.

## Repo-wide verb harvest (future)

`harvest-intent-verbs.py` today mines **playbook Ask lines**. A later pass can scan attached repos
(read-only) for domain verbs and append to a **`intent-codex-suggestions.json`** for Architect review —
never auto-merge without human edit (avoid vocabulary drift).

## Related

- [`CAPABILITY_ROUTE.md`](CAPABILITY_ROUTE.md) — keyword index
- [`PLAYBOOK.md`](PLAYBOOK.md) — worked routes
- [`docs/REA_LIMB.md`](REA_LIMB.md) — example limb under `reverse_engineer` intent
