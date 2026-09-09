# Skill: Tool Forge (local harvest)

Load when **Tool Forge** is enabled in the Workbench Toolbelt.

## What Tool Forge does locally

| Job | Tool | Output |
|-----|------|--------|
| Read harvested code | `read_active_tool` | `03_Active_Tools/*_flattened.txt` |
| Scrape vendor docs | `docs_guide_scrape` | `harvest_cache/*_Complete_Guide.md` |
| Triage skill dumps | `skill_triage_manifest` | `harvest_cache/SKILL_TRIAGE_MANIFEST.md` |

## Rules

1. **Never auto-promote** harvest_cache to Cognee — Architect triage first.
2. For **GitHub repo mining**, use **GitHub Scout** (`github_scout_search` / `github_scout_readme`) — no clone/install from Eve.
3. For **parallel multi-site doc scrapes** or **hosted artifact CDN**, defer to **Gumloop Cloud** (Toolbelt off by default) until MCP research limbs expand.
4. Do **not** use Gumloop Prompt Arsenal personas (Shadow Analyst, Focus Architect) as Eve system behavior.
5. After a successful docs scrape, tell the Architect the cache path and offer Resource Queue or curated ingest — do not run ingest silently.

## Typical prompts

- "Scrape the Ollama docs starting at https://docs.ollama.com"
- "Run skill triage on the zips I uploaded to Resource Queue"
- "List what's in harvest_cache"
- "Read the flattened tool-factory output from Active Tools"

## Gumloop lineage

Ported from Gumloop agents documented in `docs/reference/GUMLOOP_AGENT_PORT_INDEX.md`:
- TOOL_GATHERER V2 → docs scrape + tool-factory playbooks
- FVCC Skill Builder → 3-Bin triage (already applied to `.cursor/skills/`)
- THE_KEEPER → deferred (Loom intake — see Work Order)
