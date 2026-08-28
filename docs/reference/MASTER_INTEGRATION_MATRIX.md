# MASTER Integration Matrix — Build1 (EMPIRE)

**Date:** 2026-07-23  
**Source batch:** [Deep Research Resource URL Report.md](./Deep%20Research%20Resource%20URL%20Report.md)  
**Routing machine-readable:** [bin-routing-batch.json](./bin-routing-batch.json)  
**Filter:** Local Ollama only · PocketBase + Docker Postgres · Cognee 1.0 · FastMCP · HTMX/Alpine CDN · no React/Next/Webpack · no paid cloud LLM APIs

---

## Integration matrix

| Resource Name | Verdict: Bin 1/2/3 | Why it's Useful / Why it Failed | Integration Action |
|---|---|---|---|
| gabriel-herencia/postgres-mcp | Bin 1 | FastMCP+Python+psycopg3 for `empire-cognee-postgres` / `cognee_db`; fills gap PocketBase MCP cannot | **NEW skill** `.cursor/skills/postgres-mcp-specialist/` — register MCP readonly by default |
| tommypj/readable-mcp | Bin 1 | SSRF-safe Trafilatura URL→MD; preferred one-shot FastMCP fetch | **NEW skill** `.cursor/skills/readable-mcp-scrape/` — stage MD then Cognee ingest |
| modelcontextprotocol/servers (filesystem) | Bin 3 | Duplicates Desktop Commander FS/shell | Do not install; Desktop Commander remains winner |
| modelcontextprotocol/servers (fetch) | Bin 3 | Node fetch overlaps readable-mcp + docs-guide-scraper + web-researcher | Do not install; prefer FastMCP readable path |
| picocss/pico | Bin 2 | Classless CDN CSS fits HTMX; not a Cursor skill | Reference only — use CDN link; no new Pico skill (`css-framework-reference` covers CDN CSS) |
| Hypermedia Systems (htmx + Alpine) | Bin 2 | Canonical anti-SPA doctrine book | Read-only reference at https://hypermedia.systems/ — do not skill-ify |
| EMPIRE hallmark-design-skill | Bin 1 | Anti-slop UI rules already polished for HTMX/Alpine | **already installed; keep** — do not rewrite |
| EMPIRE css-framework-reference | Bin 1 | HTMX/Alpine-oriented CSS markup lookup already present | **already installed; keep** — do not rewrite |
| docling-project/docling | Bin 1 | Best local PDF/Office→MD for Cognee staging; air-gapped capable | **NEW skill** `.cursor/skills/docling-local-ingest/` |
| microsoft/markitdown | Bin 2 | Lean `convert_local` CLI; same job as Docling | Keep as secondary CLI reference; **skip Azure extras** |
| EMPIRE docs-guide-scraper | Bin 1 | Docs-site crawl → clean MD for Cognee | **already installed; keep** — winner for multi-page docs |
| EMPIRE no-mistakes | Bin 1 | Local git push gate; Ollama-capable review | **already installed; keep** |
| yangyixxxx/skillguard | Bin 1 | Zero-LLM static skill/script security scan | **NEW skill** `.cursor/skills/skillguard-offline/` |
| NVIDIA/SkillSpector | Bin 3 | Same audit job as SkillGuard; heavier AST surface | Do not install as active skill; SkillGuard wins |
| sandraschi/filesystem-mcp | Bin 3 | React webapp UI + FS redundancy | Graveyard |
| LiteDoc (0xovo/LiteDoc) | Bin 3 | Speculative PDF util overlapping Docling/MarkItDown | Graveyard |
| deepdiy/pdf2md | Bin 3 | Redundant PDF→MD converter | Graveyard |
| nutlope/hallmark + usehallmark.com | Bin 2 | Upstream rule-set/gallery for installed hallmark skill | Reference only — do not duplicate skill |
| markitdown `[az-doc-intel]` / `[az-content-understanding]` | Bin 3 | Paid Azure / cloud Document Intelligence | Graveyard |
| cursor-playbook Next.js CVE skill | Bin 3 | Targets banned Next.js stack | Graveyard |
| MCP servers requiring OpenAI/Anthropic keys | Bin 3 | Violates local-Ollama-only inference | Graveyard |
| Skills that scaffold React/Next/Vue/Svelte SPAs | Bin 3 | Banned frontend | Graveyard |
| Claude Status / Anthropic cookbooks (as runtime deps) | Bin 3 | Cloud vendor surface | Graveyard |
| topoteretes/cognee (upstream) | Bin 1 | Core Memory/RAG already wired | **already installed** via `cognee-memory-pipeline` + `empire-cognee` MCP — keep |
| EMPIRE desktop-commander-mcp | Bin 1 | Local FS/shell MCP winner | **already installed; keep** — blocks official FS MCP |
| EMPIRE web-researcher | Bin 1 | Multi-round research + Ollama synthesize | **already installed; keep** — readable-mcp is one-shot only |
| EMPIRE data-processor | Bin 1 | CSV/Excel/PocketBase SQLite wrangling | **already installed; keep** — Docling owns heavy doc→MD |
| EMPIRE html5-boilerplate-reference / visual-designer | Bin 2 | Scaffolding / node-graph pattern refs already present | Keep as reference skills; no Pico/Hypermedia duplicates |

---

## Redundancy Alerts

Single **WINNER** kept per job:

| Job | Competitors | WINNER |
|---|---|---|
| Local filesystem / shell MCP | official MCP filesystem, sandraschi/filesystem-mcp, desktop-commander-mcp | **desktop-commander-mcp** |
| One-shot URL → Markdown MCP | readable-mcp, mcp-server-fetch, web-researcher scrape | **readable-mcp** (FastMCP) |
| Full documentation site → Markdown | docs-guide-scraper, readable-mcp, web-researcher | **docs-guide-scraper** |
| Multi-round web research + synthesis | web-researcher, readable-mcp | **web-researcher** (+ local Ollama) |
| Local PDF/Office → Markdown for RAG | Docling, MarkItDown, LiteDoc, pdf2md, data-processor pdf_tools | **Docling** (`docling-local-ingest`) |
| Lean offline MD convert CLI (secondary) | MarkItDown vs Docling | **MarkItDown** as Bin 2 fallback only |
| Cognee Postgres SQL MCP | postgres-mcp vs PocketBase MCP vs data-processor connectors | **postgres-mcp** for `cognee_db`; PocketBase for tasks |
| Anti-slop UI design rules | hallmark-design-skill, nutlope/hallmark upstream, usehallmark.com | **hallmark-design-skill** (installed) |
| Classless / CDN CSS for HTMX | Pico.css, css-framework-reference | **css-framework-reference** (+ Pico as Bin 2 CDN note) |
| Offline skill security audit | SkillGuard, SkillSpector | **SkillGuard** (`skillguard-offline`) |
| Pre-push AI quality gate | no-mistakes (unique) | **no-mistakes** |
| Graph memory remember/recall | cognee-memory-pipeline / empire-cognee (unique stack role) | **cognee-memory-pipeline** + empire MCP |

---

## NEW skills written this run

Under `.cursor/skills/`:

1. `postgres-mcp-specialist/` — `SKILL.md`, `scripts/main.py`, `references/docs.md`
2. `readable-mcp-scrape/` — `SKILL.md`, `scripts/main.py`, `references/docs.md`
3. `docling-local-ingest/` — `SKILL.md`, `scripts/main.py`, `references/docs.md`
4. `skillguard-offline/` — `SKILL.md`, `scripts/main.py`, `references/docs.md`

**Not rewritten (already installed):** `hallmark-design-skill`, `css-framework-reference`, `docs-guide-scraper`, `no-mistakes`, `cognee-memory-pipeline`, `desktop-commander-mcp`, `web-researcher`, `data-processor`.

---

## Bin counts (this batch)

| Bin | Count | Meaning |
|---|---|---|
| Bin 1 | 12 | Core runtime / keep or new Tool Specialist |
| Bin 2 | 5 | Reference library only |
| Bin 3 | 11 | Graveyard (cloud, React, redundant, speculative) |

*Counts match `bin-routing-batch.json` (28 rows), including redundancy-scan winners and graveyard items from the Deep Research report.*
