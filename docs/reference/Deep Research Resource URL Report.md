### Deep Research Resource URL Report — Build1 Integration Pass

> **Canonical verdicts:** see [MASTER_INTEGRATION_MATRIX.md](./MASTER_INTEGRATION_MATRIX.md) (bins, redundancy winners, new skills). Machine routing: [bin-routing-batch.json](./bin-routing-batch.json).

**Date:** 2026-07-23  
**Filter:** Local Ollama only · PocketBase + Docker Postgres · Cognee 1.0 · FastMCP · HTMX/Alpine CDN · no React/Next/Webpack · no paid cloud LLM APIs  
**Upstream Cognee (Postgres era):** https://github.com/topoteretes/cognee  

---

## The Integration Matrix

| Resource Name/Repo | Category | Why it fits the Build1 Stack | Source URL |
|---|---|---|---|
| **gabriel-herencia/postgres-mcp** | Local MCP Servers | FastMCP + Python + psycopg3; Docker/stdio; readonly/readwrite/admin modes for EMPIRE’s `empire-cognee-postgres` admin without cloud DBaaS | https://github.com/gabriel-herencia/postgres-mcp |
| **tommypj/readable-mcp** | Local MCP Servers | FastMCP URL→Markdown via Trafilatura; SSRF-safe, local-only fetch — pairs with Cognee ingest and `docs-guide-scraper` | https://github.com/tommypj/readable-mcp |
| **modelcontextprotocol/servers (filesystem + fetch)** | Local MCP Servers | Official local filesystem roots + `mcp-server-fetch` HTML→Markdown; no paid API keys (prefer scoped paths under EMPIRE / `D:\wiki_md`) | https://github.com/modelcontextprotocol/servers |
| **picocss/pico** | UI/UX Design Skills | Classless CSS via CDN (`pico.classless.min.css`); semantic HTML only — zero React/Webpack | https://github.com/picocss/pico |
| **Hypermedia Systems (htmx + Alpine)** | UI/UX Design Skills | Canonical anti-SPA doctrine for HTMX + Alpine CDN patterns; free online book, no React components | https://hypermedia.systems/ |
| **EMPIRE `hallmark-design-skill` + `css-framework-reference`** | UI/UX Design Skills | Already installed Build1 skills: anti-slop design + HTMX/Alpine-oriented CSS markup lookup (Bootstrap/Foundation/etc. without Next.js) | Workspace: `.cursor/skills/hallmark-design-skill`, `.cursor/skills/css-framework-reference` |
| **docling-project/docling** | Data Ingestion/RAG Utilities | Local PDF/Office + Whisper ASR→Markdown; air-gapped capable; pipe `.md` into Cognee / wiki pipeline | https://github.com/docling-project/docling |
| **microsoft/markitdown** | Data Ingestion/RAG Utilities | Local multi-format→Markdown CLI (`convert_local`); skip Azure/YouTube extras — keep `[all]` installs lean / offline | https://github.com/microsoft/markitdown |
| **EMPIRE `docs-guide-scraper`** | Data Ingestion/RAG Utilities | Existing skill: docs sites→clean Markdown for Cognee; `llms.txt` / sitemap-first, no cloud LLM required | Workspace: `.cursor/skills/docs-guide-scraper` |
| **EMPIRE `no-mistakes` (→ Ollama)** | Code Quality/Security Auditing | Local git push gate; skill explicitly allows pointing review at **local Ollama** instead of cloud LLMs | Workspace: `.cursor/skills/no-mistakes` · https://github.com/kunchenguid/no-mistakes |
| **yangyixxxx/skillguard** (or Munir port) | Code Quality/Security Auditing | Offline static scan of `SKILL.md` / scripts (prompt injection, exfil, destructive ops); **zero LLM cost** | https://github.com/yangyixxxx/skillguard |
| **NVIDIA/SkillSpector (`--no-llm`)** | Code Quality/Security Auditing | Static skill/MCP pattern + AST analysis; run with `--no-llm` for fully offline audits | https://github.com/NVIDIA/SkillSpector |

---

## Bin 3: The Graveyard (discarded)

| Resource | Why discarded |
|---|---|
| sandraschi/filesystem-mcp | Ships a **React** webapp UI — violates zero-React frontend mandate |
| cursor-playbook Next.js CVE skill | Targets **Next.js** stack — out of Build1 frontend policy |
| markitdown `[az-doc-intel]` / `[az-content-understanding]` | Paid/cloud Azure Document Intelligence paths |
| MCP servers requiring OpenAI/Anthropic keys for core operation | Violates local Ollama–only inference |
| Any skill that scaffolds React/Next/Vue/Svelte SPAs | Banned frontend stack |
| Claude Status / Anthropic Support / anthropics cookbooks (as runtime deps) | Cloud vendor surface — not local Build1 runtime |

---

## Notes for EMPIRE wiring

1. **Postgres MCP:** Point `DATABASE_URI` at `postgresql://cognee:cognee@localhost:5432/cognee_db` (Docker Compose already running). Prefer `PG_MCP_ACCESS_MODE=readonly` for agents; `admin` only for explicit DBA tasks.
2. **Readable / Fetch MCP:** Use for one-off URL→Markdown before `pipeline` / Cognee remember — complements overnight wiki MD on `D:\wiki_md`.
3. **Docling / MarkItDown:** Drop outputs into `mock_data_ingest/` or a staging folder and reuse existing ingest scripts; do not introduce cloud embedding APIs.
4. **SkillGuard / SkillSpector:** Run against `.cursor/skills/**` before enabling new community skills — especially any that ship `scripts/`.
5. **UI:** Prefer Pico classless CDN + Hypermedia Systems patterns over adding daisyUI/Tailwind build steps.

---

## Prior URL inventory (preserved from earlier pass)

#### Hallmark gallery / PDF utilities / awesome-stars

See historical bullets below for Hallmark examples, LiteDoc, Markitdown, Docling, and curated awesome-stars links (unchanged fidelity archive).

* **Hallmark V1.1:** https://www.usehallmark.com/#top  
* **Hallmark Install:** https://www.usehallmark.com/#install  
* **nutlope/hallmark:** https://github.com/nutlope/hallmark  
* **LiteDoc:** http://litedoc.xyz/ · https://github.com/0xovo/LiteDoc  
* **microsoft/markitdown:** https://github.com/microsoft/markitdown  
* **docling-project/docling:** https://github.com/docling-project/docling  
* **deepdiy/pdf2md:** https://github.com/deepdiy/pdf2md  

#### Gumloop-style raw URL feed (Build1-relevant subset)

https://github.com/gabriel-herencia/postgres-mcp https://github.com/tommypj/readable-mcp https://github.com/modelcontextprotocol/servers https://github.com/picocss/pico https://hypermedia.systems/ https://github.com/docling-project/docling https://github.com/microsoft/markitdown https://github.com/yangyixxxx/skillguard https://github.com/NVIDIA/SkillSpector https://github.com/topoteretes/cognee https://github.com/kunchenguid/no-mistakes https://www.usehallmark.com/#top https://github.com/nutlope/hallmark http://litedoc.xyz/ https://github.com/0xovo/LiteDoc  

**Total unique Build1-matrix links this pass:** 12 primary + Cognee upstream + in-repo skills.
