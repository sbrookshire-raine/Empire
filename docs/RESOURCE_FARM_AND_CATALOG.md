# Resource farm and disassembly catalog — direction

**One breath:** build a **fluid, stateless index** of GitHub (and local) study material as **Disassembly Cards** Eve can analyze later — optional **Heptabase** for the visual stack — without auto-ingesting **Cognee** unless the Architect asks.

Use this page when resuming work after a break. Details: [DISASSEMBLY_CATALOG.md](DISASSEMBLY_CATALOG.md), [REA_LIMB.md](REA_LIMB.md).

## Three depths (do not confuse them)

| Depth | What it is | How it is produced | Good for |
|-------|------------|--------------------|----------|
| **Scout** | README + metadata; hypotheses labeled | Eve **`resource_farm_run`** or `python -m pipeline.resource_farm "<query>"` | Fast catalog, dedupe by `source_repo`, “what repos exist?” |
| **Study seed** | Local tree under Resource Queue; 3–7 connections with **real paths** | Diagnostic **`_atomic_seed_card`** (atomic-agent template) or **outside agent** (see below) | Cards Eve can “play with” before full REA |
| **REA verified** | Evidence from analyze on disk | **`rea_doctor`** → **`rea_analyze_javascript`** / **`rea_invoke`** → update or new **`disassembly_card_write`** | Ground truth; replace scout guesses |

The **atomic-agent** card (`dc_dcb9251026`) is a **study seed**: seeded by `pipeline/rea_disassembly_diagnostic.py` from `00_Resource_Queue/atomic-agent` (package.json, README, `src/` layout) with a **repo-specific connection template** mapped to EMPIRE. Evolution note: deepen after `rea_js_atomic_src`. It is **not** the same as scout farm output.

## Where artefacts live

| Artefact | Path |
|----------|------|
| Cloned / copied repos | `C:/Empire_Workbench/00_Resource_Queue/` |
| GitHub search/readme cache | `C:/Empire_Workbench/04_Thought_Experiments/github_cache/` |
| Disassembly cards (`dc_*`) | `C:/Empire_Workbench/04_Thought_Experiments/disassembly_cards/` |
| Heptabase board | Config `config/heptabase.env` (gitignored); setup `scripts/ensure-heptabase-disassembly-board.ps1` |

Cards carry optional **`source_repo`** (`owner/name`) and **`farm_kind`** (`scout` | `study`) for indexing.

## Eve (minimal chat — no long prompt)

| Architect says | Eve action |
|----------------|------------|
| “Resource farm …” / “processed materials catalog” | **`resource_farm_run`** — skill **skill-resource-farm** |
| (no query) | **`resource_farm_run()`** → `farmed_repos` index |
| “… and put on the board — yes” | Same + **`architect_confirm: true`** (Heptabase if CLI + board healthy) |
| Repo already in Resource Queue | **skill-reverse-engineering** → REA → richer card |

Intent codex id: **`resource_farm`**. Playbook: **web-and-sources**.

## Heptabase (logic, not ad hoc)

- **Why:** Orange/blue/green board = **current study stack**, not long-term memory.
- **When:** New scout cards publish only if **`architect_confirm: true`**, whiteboard id set, desktop app + Local CLI healthy (`heptabase_health`).
- **Publish path:** `disassembly_publish_heptabase` or farm with confirm; notes use **`--content-file`** and body **without YAML front matter** (see `markdown_for_heptabase` / `repair-note` in `pipeline/disassembly_publish.py`).
- **Never** Cognee from farm or publish unless Architect runs remember flow separately.

## Outside agent (frontier Cursor / cloud)

Use when you want **study-depth** cards for many repos without typing Eve prompts. Copy the prompt in [prompts/external-resource-farm-agent.md](prompts/external-resource-farm-agent.md): GitHub → copy to Resource Queue → read manifest + tree → write `DisassemblyCard.v1` JSON → `python -m pipeline.disassembly_card write --file …`.

Eve **`resource_farm_run`** remains the **in-stack scout index**; the outside agent is the **bulk study-seed factory**.

## Mechanics shipped (revision-refactor)

- `pipeline/resource_farm.py` + Eve tool **`resource_farm_run`**
- Heptabase **`create_note`** via content file; **`repair-note`** recreates empty publishes
- Placement id fix (`instanceId`) in **`heptabase_cli.extract_placement_id_from_place`**
- Tests: `tests/pipeline/test_resource_farm.py`, publish/heptabase/disassembly tests

## Pick up next (suggested order)

1. **Restart Eve** after pull (`Restart-EMPIRE.bat` or `scripts/start-eve.ps1`) so **`resource_farm_run`** is in the bundle.
2. Run **`resource_farm_run()`** in chat — confirm `farmed_repos` includes `atomic-agent` if that card has `source_repo` set (legacy seed may only have URL in evidence; optional: patch sidecar with `source_repo: atomic-agent/…` when known).
3. **Study tier at scale:** run outside agent with a query list; or extend `_atomic_seed_card` pattern into a generic **`study_seed_from_repo(path)`** in Python (future — not required for scout loop).
4. **REA pass:** `rea_js_atomic_src` on `atomic-agent/src/cli` (battery path); update card evolution / connections from tool output.
5. Optional: promote one mature card → Cognee + **`disassembly_mark_mature`** (green) after Architect confirm.

## Verify

```powershell
.\venv\Scripts\python.exe -m pytest tests\pipeline\test_resource_farm.py tests\pipeline\test_disassembly_publish.py tests\pipeline\test_heptabase_cli.py -q
.\venv\Scripts\python.exe -m pipeline.playbook --coverage
.\scripts\diagnostic-rea-disassembly.ps1 -Fast
```
