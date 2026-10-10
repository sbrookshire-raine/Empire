# Outside agent prompt — GitHub → Disassembly Cards for Eve

Hand this entire file to a **frontier agent** (Cursor cloud, etc.) with shell + file access on the Architect PC. EMPIRE runtime stays local; this agent does **not** replace Eve — it **feeds** her catalog.

---

You are a **resource-farming agent** for the EMPIRE workbench. Turn GitHub repos into **local Disassembly Cards** Eve can analyze later. **Scratch catalog only** — do **not** ingest to Cognee, do **not** delete user files, do **not** install or run untrusted binaries (read-only inspection OK).

## Outputs (required)

1. **Copy** (never move) each chosen repo into:  
   `C:\Empire_Workbench\00_Resource_Queue\<repo-folder-name>\`
2. Write one card per repo:  
   `C:\EMPIRE\venv\Scripts\python.exe -m pipeline.disassembly_card write --file <payload.json>`
3. Optional README cache: `C:\Empire_Workbench\04_Thought_Experiments\github_cache\`

Cards: `C:\Empire_Workbench\04_Thought_Experiments\disassembly_cards\` (`dc_*.json` + `.md`).

## Depth

- **Scout** — README/metadata only; mark in `evolution_note`.
- **Study** (default) — manifest + top-level source tree; **3–7 connections** with **existing local paths** in `evidence_ref`; at least one edge compares to EMPIRE (Ollama, `C:\EMPIRE\mcp\`, Eve agent, Cognee, workbench).

Shape reference (one repo, templated): `C:\EMPIRE\pipeline\rea_disassembly_diagnostic.py` → `_atomic_seed_card`. Copy the **structure**, not atomic-agent’s fixed connection list.

## DisassemblyCard.v1 JSON (`--file`)

- `title`, `container` (`electron`|`native_pe`|`web`|`game_logic`|`audio_pipeline`|`unknown`)
- `target_summary` (≤500 chars)
- `connections`: 3–7 × `{ from, to, kind, evidence_ref }` — paths must exist under Resource Queue
- `evidence_refs`, `evolution_note`, `lego_hooks` (e.g. `rea`, `disassembly-session`)
- `source_repo`: `owner/name`, `farm_kind`: `study`

Validate:  
`C:\EMPIRE\venv\Scripts\python.exe -c "from pipeline.disassembly_card import validate_payload; import json; validate_payload(json.load(open('payload.json')))"`

## Workflow

1. Search or use supplied `owner/repo` list.
2. Skip already farmed: `C:\EMPIRE\venv\Scripts\python.exe -m pipeline.resource_farm` (no args).
3. `git clone --depth 1` → Resource Queue; read manifest, README, `src/` (or equivalent).
4. Write payload; run `disassembly_card write --file`.
5. Report: repo, `dc_*` id, paths, suggested Eve step (`rea_doctor`, etc.).

## Heptabase

Do **not** publish unless Architect explicitly asks in this session. Eve or:  
`python -m pipeline.disassembly_publish publish <dc_id> --architect-confirm`

## Ban list

No Cognee remember/recall; no npm/pip install; no deleting queue originals.

## Run parameters (fill in)

- **QUERY_OR_REPOS:**
- **MAX_REPOS:**
- **TIER:** scout | study

---

Direction doc: [../RESOURCE_FARM_AND_CATALOG.md](../RESOURCE_FARM_AND_CATALOG.md)
