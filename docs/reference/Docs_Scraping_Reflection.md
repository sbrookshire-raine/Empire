# Reflection: Scraping & Cleaning App Documentation for NotebookLM

*A retrospective on the multi-app documentation extraction project, covering 13 apps, ~30 files, and roughly 2,000+ pages of source documentation.*

**Compiled:** 2026-07-18

---

## 1. What This Project Did

Across this session, I crawled and cleaned the official documentation/guide sites for:

| App | Pages | Files | Doc platform |
|---|---|---|---|
| Magic Patterns | 91 | 1 | Mintlify |
| Slashspace (Rabbitholes AI) | 37 | 1 | Fumadocs (Next.js SSR) |
| Dify | 366 | 6 | Mintlify (llms-full.txt) |
| Heptabase | 29 | 1 | Docusaurus wiki |
| Gumloop | 420 | 3 | Mintlify |
| PrompTessor | 11 | 1 | Custom Next.js |
| Ultimate Web Scraper | 42 | 1 | Custom Next.js |
| Sourclip | 2 | 1 | Custom Next.js |
| AnythingLLM | 203 | 1 | Nextra |
| Cursor | 101 | 4 | Mintlify |
| FlutterFlow | 369 | 7 | Docusaurus-flavored (llms-full.txt) |
| Ollama | 65 | 1 | Mintlify |

**Total: ~1,736 documentation pages condensed into ~29 clean Markdown files**, each restructured with a title header, table of contents, category grouping, and per-page source citations, ready to upload directly into NotebookLM.

Docker and Hugging Face were intentionally excluded — both are multi-product documentation *hubs* (many independent doc sets, potentially tens of thousands of pages) rather than a single linear guide, and needed scope narrowing that wasn't provided.

---

## 2. Challenges Faced

**No two sites were built the same way.** Every site required first *identifying* its documentation platform before a scraping strategy could even be chosen. The biggest recurring risk was assuming one site's structure would work for the next.

**MDX/JSX components don't survive naive scraping.** Docs built with Mintlify (and similar) render custom components — `<Tip>`, `<Card>`, `<Steps>`, `<Accordion>`, `<ResponseField>`, and one-off widgets like Ollama's icon-based "capability list" — that have no meaning outside their site's own renderer. Left alone, these leak into the output as raw, unreadable tag soup. Every one had to be identified and converted to an equivalent plain-Markdown structure (blockquotes, bullet lists, bold sub-headers) by hand-writing a small MDX-to-Markdown converter, since generic tools don't know these custom tags exist.

**Large sites needed a splitting strategy, not just a size cap.** Gumloop (420 pages), Dify (366 pages), and FlutterFlow (369 pages) were too large for a single file. Splitting arbitrarily by character count would have cut a topic in half mid-guide; instead each was split along the site's own navigation categories, with an index file explaining the reading order for multi-part guides.

**Some content actively worked against extraction:**
- Heptabase's wiki pages embedded full **duplicate Chinese/Japanese translations** of every article, sometimes interleaved paragraph-by-paragraph with the English — this needed a language-detection filter to strip cleanly.
- PrompTessor's docs pages included **live interactive product demos** (buttons, token counters, carousels) with no distinguishing tag names, just generic `<div>`s — required pattern-matching on class names/button text rather than a generic cleaner.
- Ultimate Web Scraper's FAQ page used a **JS-lazy-loaded accordion** where only the first answer existed in the static HTML — required a Playwright click-through pass to recover the rest.
- Slashspace's `/llms.txt` described the product under its *old* brand name (Rabbitholes AI) even after the live docs had migrated to the new name — the sitemap was the more trustworthy source of truth.

**Two false "it didn't work" reports were UI display lag, not real failures** (the FlutterFlow Part 7 export, and the Ollama guide). In both cases the file was already complete and correctly sized — re-importing the artifact and checking the byte count confirmed this immediately, without needing to redo any scraping work.

**Scale required delegation, not brute force.** Running 5-6 large scraping jobs sequentially in one thread would have been slow and would have bloated a single conversation's context. Dispatching each app as an independent parallel sub-agent (with the full extraction methodology written into its prompt) cut wall-clock time dramatically and kept each job's noisy intermediate work out of the main thread.

---

## 3. Documentation Platforms Encountered & How to Extract From Them

| Platform | Signature | Best discovery method | Best fetch method | Primary cleanup need |
|---|---|---|---|---|
| **Mintlify** | `/llms.txt`, pages work with `.md` appended | `llms.txt` / `llms-full.txt` | Raw `.md` via direct HTTP request | MDX components (Tip/Card/Steps/Accordion/Tabs/ResponseField/Expandable/CodeGroup) |
| **Fumadocs** (Next.js) | `<article id="nd-page"><div class="prose">` | `sitemap.xml` | Raw HTML + BeautifulSoup + markdownify | Isolate `.prose` specifically — pagination cards are siblings, not children |
| **Nextra** (Next.js) | No llms.txt/sitemap; MDX-flavored HTML | Extract links from rendered nav | Raw HTML + BeautifulSoup | `nextra-callout` divs → blockquotes; changelog bloat |
| **Docusaurus** | Admonition blocks, "Direct link to X" anchors | `sitemap.xml` or `llms.txt` | `web_fetch_tool` is often sufficient alone | Admonitions → blockquotes; wikis may embed duplicate-language content |
| **Custom/bespoke Next.js** | No consistent signature | Check `sitemap.xml` and `llms.txt` anyway | `web_fetch_tool` first, HTML fallback | Interactive demo widgets, lazy-loaded accordions |

**The single highest-leverage move across this entire project: always check for `llms.txt` / `llms-full.txt` first**, at both the site root and the docs subpath. When present, it turns a multi-step crawl-fetch-clean pipeline into "fetch one file, split it by page." Six of the twelve apps had this available.

---

## 4. What I Changed As a Result

I've turned this experience into a persistent skill (`docs-guide-scraper`) in my skill library, so future documentation-scraping requests — for you or in any other conversation on this agent — start from this playbook instead of rediscovering it from scratch. It includes:

- **A discovery decision tree**: llms.txt → llms-full.txt → sitemap.xml → nav-link crawling, in that priority order, with the exact URLs to check.
- **A fetch decision tree**: web_fetch_tool first (cheap, often sufficient) → raw `.md` fetch if available (Mintlify) → raw HTML + BeautifulSoup + markdownify → Playwright only as a last resort for JS-heavy or lazy-loaded content.
- **A reusable Python module** (`mdx_cleaners.py`) with the tag-stripping engine and formatter functions for every MDX component encountered (callouts, cards, steps, accordions, tabs, response fields, etc.), so future cleanups reuse tested code instead of rewriting regex from scratch.
- **A platform notes reference** documenting the exact quirks of Mintlify, Fumadocs, Nextra, Docusaurus, and custom sites, keyed off their structural signatures, so a new site can be pattern-matched against a known platform quickly.
- **A standardized output format and quality checklist** (heading-shift rules, leftover-tag scan, relative-link scan, size-based splitting threshold) so every future scrape produces a consistently structured file without needing to re-derive the format each time.
- **A documented rule to distrust "it didn't finish" signals** until the file's actual size/line count has been checked — since this came up twice and both times was a false alarm.

---

## 5. Appendix: Full File Manifest

- Magic Patterns — `Magic_Patterns_Complete_Guide.md`
- Slashspace — `Slashspace_Complete_Guide.md`
- Dify — `Dify_Guide_01_Getting_Started.md`, `Dify_Guide_02_Using_Dify_Cloud.md`, `Dify_Guide_03_Self_Hosting.md`, `Dify_Guide_04_Plugin_Development.md`, `Dify_Guide_05_CLI_Reference.md`, `Dify_Guide_06_API_Reference.md`
- Heptabase — `Heptabase_Complete_Guide.md`
- Gumloop — `Gumloop_Complete_Guide_Part1_Core_Concepts_and_API.md`, `Gumloop_Complete_Guide_Part2_Node_Reference.md`, `Gumloop_Complete_Guide_Part3_MCP_Connectors.md`
- PrompTessor — `Promptessor_Complete_Guide.md`
- Ultimate Web Scraper — `UltimateWebScraper_Complete_Guide.md`
- Sourclip — `Sourclip_Complete_Guide.md`
- AnythingLLM — `AnythingLLM_Complete_Guide.md`
- Cursor — `Cursor_Guide_00_Index.md`, `Cursor_Guide_01_GettingStarted_Agent_Customizing.md`, `Cursor_Guide_02_CloudAgents_Integrations_SDK.md`, `Cursor_Guide_03_CLI_Account.md`
- FlutterFlow — `FlutterFlow_Guide_01` through `FlutterFlow_Guide_07` (7 parts)
- Ollama — `Ollama_Complete_Guide.md`

Not yet scraped, pending scope narrowing: **Docker** (docs.docker.com), **Hugging Face** (huggingface.co/docs).
