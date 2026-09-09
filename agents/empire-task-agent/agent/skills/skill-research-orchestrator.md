Use when the Architect asks for multi-source research, discovery of MCP/CLI repos, Product Hunt launches, encyclopedia facts, or "research partner" style investigation.

## Prerequisites

- **Research Partner mode** must be ON (Workbench More tab) OR the relevant Toolbelt limbs manually enabled.
- Call **`research_orchestrate`** for combined Wikipedia + GitHub + Product Hunt in **one turn** (preferred).
- Or call **`request_capability`** then individual scouts on later turns.

## Source routing

| Intent | Tool | Source |
|--------|------|--------|
| Encyclopedia / history / Truth Drift | `research_orchestrate` with `wiki` or `wiki_scout_search` | Local Weaviate |
| GitHub MCP/CLI/repo discovery | `research_orchestrate` with `github` or `github_scout_search` | GitHub API |
| Product Hunt / launches | `research_orchestrate` with `producthunt` | Public `/feed` via web_scout |
| Known URL | `web_scout` or orchestrator `web` + `web_url` | Single page fetch |

## Workflow

1. If unsure whether Partner mode is on, call **`capability_status`** silently.
2. For broad research, call **`research_orchestrate`** with the user's question — default sources: wiki, github, producthunt.
3. Summarize from returned cache paths and summaries — **never invent** page/repo content.
4. GitHub hits may produce an **intake brief** under `00_Resource_Queue` — mention path for triage; do **not** auto-forge.
5. After a manual multi-step research chain (not orchestrator), call **`release_capabilities`**.

## Hard rules

- **Never** `cognee_remember` or `promote_wiki_cache` unless the Architect explicitly asks.
- **Never** clone, install, or `ollama pull` from scout results.
- Web Scout is **not** a search engine — no invented URLs.
- If Weaviate is down and wiki fails, say so briefly — do not pretend you browsed Wikipedia live.
- If Research Partner is off, tell them to enable it in Workbench More tab (one toggle) — do not narrate tool loading.

## Good triggers

- "Find GitHub MCP servers for local DuckDB"
- "What's on Product Hunt today?"
- "Compare what Wikipedia says about X across years" (wiki scout / orchestrator wiki)
- "Research local-first meeting transcription tools"

## Bad

- Auto-ingesting scout caches into memory
- Calling `research_orchestrate` when Partner mode is off without telling the user how to enable it
