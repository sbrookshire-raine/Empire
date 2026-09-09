# Gumloop Agent Port Index (EMPIRE)

Status as of 2026-09-09. Source briefs: `C:/Empire_Workbench/00_Resource_Queue/GL_*.md`.

## Ported locally (use Eve / Cursor / scripts)

| Gumloop agent | ID | Local limb | How to run |
|---|---|---|---|
| **TOOL_GATHERER V2** | `22cTHEm1NUdmYTxEo6aHZu` | Tool Forge + Web Scout | `docs_guide_scrape` (Eve) or `.\scripts\run-docs-guide-scrape.ps1`; skills in `.cursor/skills/docs-guide-scraper`, `tool-factory`; corpus in `docs/reference/*_Complete_Guide.md` |
| **FVCC Skill Builder** | `rCwBCMvrAPh8tvAACRERbj` | Skill compiler | `skill_triage_manifest` (Eve) or `.\scripts\run-skill-inventory.ps1`; July 2026 batch → `.cursor/skills/` + `MASTER_INTEGRATION_MATRIX.md` |
| **MASTER_0_THE_KEEPER** | `aWnpvYEwi6NMQZX4aq6q8U` | Loom Intake | `loom_process_shell_csv` / `loom_status` (Eve) or `.\scripts\run-loom-intake.ps1`; tree at `C:/Empire_Workbench/04_Thought_Experiments/loom/` (from Desktop `TOOL_FACTORY_GUMLOOP/loom`, scratch omitted) |

## Keep on Gumloop (for now)

| Gumloop agent | ID | Why |
|---|---|---|
| **TOOL_GATHERER** (parallel scrapes) | same | Multi-site `invoke_agent` clones + artifact CDN faster than single local run |
| **THE_KEEPER** (live weave) | `aWnpvYEwi6NMQZX4aq6q8U` | Parallel A1–A6 Gumloop subagent chat; local intake + ledger now on EMPIRE |

## Deferred Work Orders

- `WO-20260909T210100Z-gumloop-research-mcp.md` — expansive parallel research via MCP (post local MVP)
- Cognee ingest of `primitive_ledger.csv` — manual / curated only when Architect asks

## Do not port as Eve persona

- TOOL_GATHERER **Prompt Arsenal** (Shadow Analyst, Focus Architect, etc.) — store as reference only
- Gumloop platform executor voice — Eve uses `eve_instructions.md`

## Artifact export checklist (manual)

If Gumloop artifacts are missing locally, download:

1. `keeper_export.zip` (`8y828E5VCm9GfLwXcBeKWh`)
2. `build1_cursor_skills.zip` (`bNyLqUf6ZC9M9sAMNAZtyp`) — likely superseded by repo `.cursor/skills/`
3. `tool-factory-v4.zip` from TOOL_GATHERER artifacts → Resource Queue for `empire_sorter.py`
