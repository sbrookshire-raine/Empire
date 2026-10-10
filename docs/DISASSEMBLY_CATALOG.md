# Disassembly catalog (RE play sessions → LEGO memory)

Eve learns by **breaking things apart**, writing one **Disassembly Card** per serious reverse-engineering session, and optionally **publishing** it to a Heptabase whiteboard so you can see connections and colors accrue over time.

**Resume / strategy (scout vs study vs REA, Eve vs outside agent):** [RESOURCE_FARM_AND_CATALOG.md](RESOURCE_FARM_AND_CATALOG.md)

## Loop

1. Upload or path → REA tools (`rea_doctor`, analyze, visual observe). **Or** GitHub scout → **`resource_farm_run`** (scout tickets, deduped by repo — see Eve skill **skill-resource-farm**).
2. **`disassembly_card_write`** — local markdown + JSON under `C:/Empire_Workbench/04_Thought_Experiments/disassembly_cards/`.
3. Architect confirms → **`disassembly_publish_heptabase`** (`architect_confirm: true`).
4. Optional memory → **`propose_remember`** → **`confirm_remember`** → **`disassembly_mark_mature`** (green on board).

## Heptabase setup (once)

1. Heptabase desktop app running; Local CLI enabled (`heptabase --version` → 0.6+).
2. From repo root:

```powershell
.\scripts\ensure-heptabase-disassembly-board.ps1 -SeedLegend
```

3. Config lives in `config/heptabase.env` (gitignored). Example keys in [config/heptabase.env.example](../config/heptabase.env.example).

## Color legend

Defined in [config/heptabase-learning-map.json](../config/heptabase-learning-map.json):

| Color | Stage |
|-------|--------|
| Orange | Just published (new play session) |
| Blue | Dependency links drawn to earlier cards |
| Green | Matured (memory confirmed) |
| Purple | Evolved build (`depends_on` + evolution note) |

Connector arrows on the board = **catalog dependencies** (`depends_on`), not every semantic hop inside the note.

## MCP

- **Cursor:** `empire-heptabase` in `.cursor/mcp.json`
- **Eve:** Toolbelt **Heptabase Catalog** (`heptabase`); tools auto-admit when headroom allows

## Failures (plain English)

| Symptom | Fix |
|---------|-----|
| CLI not found | Install/enable Local CLI in Heptabase settings |
| Probe failed | Start the desktop app |

## Diagnostic battery

Mechanic-style checks for clone material, disassembly write/list, REA Node, optional Heptabase/Eve HTTP:

```powershell
.\scripts\diagnostic-rea-disassembly.ps1 -Fast    # static + material + catalog seed (no live REA analyze)
.\scripts\diagnostic-rea-disassembly.ps1          # includes optional live probes
.\scripts\diagnostic-rea-disassembly.ps1 -Full    # diagnostic + pytest slice
```

Report: `tmp/rea_disassembly_diagnostic.json`. Study repo default: `C:/Empire_Workbench/00_Resource_Queue/atomic-agent`.
| No whiteboard id | Run `ensure-heptabase-disassembly-board.ps1` |
| Publish blocked | Pass `architect_confirm: true` in the same approved turn |

See also [REA_LIMB.md](REA_LIMB.md) and [LEGO_WHITEBOARD.md](LEGO_WHITEBOARD.md) (Disassembly Session recipe).
