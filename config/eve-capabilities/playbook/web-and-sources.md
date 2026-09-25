---
area: web-and-sources
one_line: Public web, GitHub, container images, docs scraping, document reading, multi-source research.
tools: web_scout, searxng_search, browser_local_fetch, github_scout_search, github_scout_readme, container_scout_search, container_scout_detail, container_scout_docker_status, research_orchestrate, research_start, research_status, research_read, docs_guide_scrape, read_document, docling_convert, structured_extract
skills: skill-browser-local, skill-container-scout, skill-read-document, skill-research-orchestrator, skill-structured-extract, skill-web-scout
---

# Web and outside sources — worked pathways

Local first: the archive answers encyclopedia questions. Reach outside only when the thing is not in
the archive (a live site, a repo, a package, a PDF on disk). Cite what you fetched.

## Public web pages
Use when: the ask is about a live page, a vendor doc, or something the archive cannot hold.

- **Ask:** "what's on the front page of producthunt.com?" → **Do:** `web_scout("<url>")` → **Get:** the page text as markdown (feed order, not official rank — say that).
- **Ask:** "summarize this link: <url>" → **Do:** `web_scout(url)` → **Get:** a short read with the URL named.
- **Ask:** "find the official docs for yt-dlp options" → **Do:** `web_scout("https://github.com/yt-dlp/yt-dlp#usage")` (there is no search tool — `web_search` is switched off on purpose) → **Get:** the option list, or a plan to scrape a docs index you already know.
- **Ask:** "check whether this page changed" → **Do:** `web_scout(url)` again (each fetch caches markdown under `04_Thought_Experiments/web_cache`) → **Get:** the current text to compare with the cached copy.
- **Ask:** "is my local Workbench page up?" → **Do:** `browser_local_fetch("<local url>")` → **Get:** the local page content (allowlist only, no public web, no form posts).

## Long research (the desk: start, leave, read)
Use when: the pass needs several pages, or it would hold the turn open for minutes. These are session
limbs — **admit Web Research first** (`admit_for_goal("web_research")`), then:

- **Ask:** "dig into what changed in yt-dlp and give me the short version" → **Do:** `research_start("yt-dlp changes")` — **no URLs needed**, the worker searches first → **Get:** a job id in about a second, and the turn *ends*; the fetching happens while the model is idle, so nothing evicts you and nothing blocks.
- **Ask:** "where did that research get to?" → **Do:** `research_status()` with no id → **Get:** every open job with its age and status (this is how you come back to your own work).
- **Ask:** "what did it find?" → **Do:** `research_read("<job_id>", budget=1200)` → **Get:** a bounded digest plus `more_available`, so your window stays small.
- **Ask:** "read me the whole thing" → **Do:** `research_read("<job_id>", budget=4000)` → **Get:** more of the digest; the full pages stay on the desk at `source_path` — never paste the corpus into the answer.
- **Ask:** "I don't have a URL — find it" → **Do:** `searxng_search("yt-dlp options documentation", limit=3)` → **Get:** titles + URLs + snippets from the local instance; then `web_scout` the best hit. Results are **leads, not sources** — open one before quoting it, and **name the page title + URL in your answer** (a number without its source is not an answer). If the instance is down the tool says so instead of inventing results.

## GitHub
Use when: repo discovery, "is there a tool for X?", reading a project's README.

- **Ask:** "find GitHub MCP servers for local DuckDB" → **Do:** `github_scout_search("mcp server duckdb")` → **Get:** candidate repos with stars and links.
- **Ask:** "what does this repo do?" → **Do:** `github_scout_readme("owner/repo")` → **Get:** the README summary, licence, and setup lines.
- **Ask:** "anything newer than what we have for X?" → **Do:** `github_scout_search("<X> local")` → compare against `search_catalog` → **Get:** a shortlist + an intake brief path.
- **Ask:** "build me a plan to try one of these" → **Do:** `draft_work_order(...)` → **Get:** a Work Order draft under the Workbench, not an auto-install.

## Container images
Use when: a service might already exist as an image, or a running container needs checking.

- **Ask:** "is there a local-first image for X?" → **Do:** `container_scout_search("X")` → **Get:** candidate images with sizes.
- **Ask:** "what tags does that image have?" → **Do:** `container_scout_detail("<image>")` → **Get:** tags + digest.
- **Ask:** "what containers are running?" → **Do:** `container_scout_docker_status()` → **Get:** the container list and state.
- **Ask:** "can we run it here?" → **Do:** `resource_pulse` first, then `container_scout_detail` → **Get:** a go/no-go on headroom before any pull.

## Documents on disk (PDF, DOCX, XLSX, HTML)
Use when: the answer is inside a file they dropped or a page they saved.

- **Ask:** "what does this PDF say about pricing?" → **Do:** `read_document("<path>")` → **Get:** markdown text; then answer only from it.
- **Ask:** "convert this binder PDF to markdown so we can search it" → **Do:** `docling_convert("<path>")` → **Get:** staged markdown for `workspace_search` or ingest.
- **Ask:** "pull the tables out of this report" → **Do:** `read_document(path)` then `structured_extract(text, fields=...)` → **Get:** JSON rows ready for `create_spreadsheet`.
- **Ask:** "make a spreadsheet from that table" → **Do:** `structured_extract` → `create_spreadsheet(rows, path="eve-output/<name>.xlsx")` → **Get:** an `.xlsx` in `eve-output`.
- **Ask:** "which of my local files mention X?" → **Do:** `workspace_search("X")` → **Get:** file hits, then `read_document` the best one.

## Multi-source research (the orchestrated path)
Use when: the answer needs **several** sources at once (archive + web + GitHub + PH), or the Architect says "research this".

- **Ask:** "research local-first vector DBs: what exists, what's active, what fits 16 GB?" → **Do:** `research_orchestrate(question, sources=["web","github"])` → **Get:** a compact multi-source brief with links (needs Research Partner on).
- **Ask:** "what's new on Product Hunt today, and does any of it matter to EMPIRE?" → **Do:** `research_orchestrate(...)` → **Get:** leads + a triage candidate list.
- **Ask:** "compare three options for X and recommend one" → **Do:** `research_orchestrate` → `query_data`/`create_spreadsheet` on the findings → **Get:** a decision table, not prose.
- **Ask:** "scrape the official docs into a guide" → **Do:** `docs_guide_scrape("<docs root url>")` → **Get:** `<name>_Complete_Guide.md` in `harvest_cache` (never auto-Cognee).
- **Ask:** "is this a 3-Bin skill zip or junk?" → **Do:** `skill_triage_manifest(path)` → **Get:** a triage manifest with USEFUL NOW / COOL IDEA / JUNK.

## Ranked retrieval instead of keyword guessing
Use when: a pile of candidates needs ordering before you read any of them.

- **Ask:** "which of these results actually answers the question?" → **Do:** `retrieval_rerank(query, candidates)` → **Get:** a ranked shortlist with scores.
- **Ask:** "the first search hit is wrong — try the others" → **Do:** `retrieval_rerank` on the existing cards → **Get:** a better order without another search.
- **Ask:** "show me how the ranking changes" → **Do:** compare `retrieval_rerank` output before/after a query rewrite → **Get:** evidence for the rewrite (eval only; production embeds unchanged).
