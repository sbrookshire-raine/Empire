# Cross-App Connection Guide
### MCP, CLI, API & Integration Surfaces Across the Scraped Documentation Set

*Built from the 27 previously scraped guide files already in this workspace. Purpose: a fast reference for wiring these apps together in future agent workflows — which ones can talk to which, and how.*

**Compiled:** 2026-07-18

---

## 1. Capability Matrix

Signal counts below are keyword-frequency scans across each app's full guide set — a rough proxy for "how much of this app's documentation is about connecting to other systems," not an exact feature count. Use it to prioritize which app's guide to open first for a given integration task.

| App | MCP | CLI | REST/API | Webhooks | OpenAPI spec | SDK | Primary role in a stack |
|---|---|---|---|---|---|---|---|
| **Gumloop** | ✅ Extensive (420+ MCP connector nodes) | ✅ | ✅ | ✅ | Partial | ✅ | Orchestration hub — connects everything else together |
| **Cursor** | ✅ (MCP client) | ✅ (full agent CLI) | ✅ | — | Partial | ✅ (TS/Python) | Coding agent — consumes MCP servers, drives repos |
| **AnythingLLM** | ✅ (MCP client support) | ✅ (small hub CLI) | ✅ | — | — | Light | RAG / chat frontend over local or cloud models |
| **Magic Patterns** | ✅ (has its own MCP *server*) | — | ✅ (v3, shared auth w/ MCP) | Minor | ✅ Per-endpoint | — | Design generation — exposes itself as a tool |
| **Dify** | ✅ (can *publish* apps as MCP servers) | ✅ (`difyctl`, plugin CLI) | ✅ Extensive | ✅ Extensive | ✅ | ✅ | Agentic app builder — workflow/chatflow backend |
| **Slashspace** | ✅ (MCP client, beta) + Composio (500+ services) | — (uses Cursor/Claude Code CLIs as "agent providers") | ✅ | — | — | — | Canvas-based multi-model chat workspace |
| **FlutterFlow** | — (not native MCP) | ✅ (build/deploy CLI) | ✅ (calls any REST API from app logic) | Minor | Partial | Light | No-code app builder — consumes backend APIs |
| **Ultimate Web Scraper** | — | — | — | ✅ (webhook export) | — | — | Data collection — feeds other tools via webhook/Sheets |
| **Ollama** | — (not itself an MCP server/client) | ✅ (primary interface) | ✅ (the whole product is an API) | — | ✅ Full | Light (Python/JS libs) | Local LLM runtime — backend for nearly everything above |
| **Heptabase** | — | — | Minimal | — | — | — | Knowledge base — mostly a manual, read-heavy tool |
| **PrompTessor** | — | — | — | — | — | — | Prompt-crafting workspace — manual/UI-only, no API surface found |
| **Sourclip** | — | — | — | — | — | — | NotebookLM export helper (Chrome extension) — no API surface |

**Reading the gaps:** Heptabase, PrompTessor, and Sourclip are consumer/manual tools with no meaningful programmatic surface in their docs — they're endpoints for a human, not for an agent pipeline. Everything else can plausibly sit in an automated workflow.

---

## 2. Per-App Connectivity Profile

**Ollama** is the connective tissue of this whole stack. It runs models locally and exposes a full REST API (`/api/chat`, `/api/generate`, `/api/embed`, etc.) plus OpenAI- and Anthropic-compatible endpoints — meaning any tool that can already talk to OpenAI or Claude's API can be pointed at a local Ollama instance with just a base-URL change. Its docs list 20+ first-party integrations (Cursor via "Agent Providers," Claude Code, VS Code, JetBrains, n8n, and more), making it the most natural **shared local-model backend** for the rest of the stack.

**Gumloop** is the natural **orchestration layer**: its MCP connector library (400+ nodes across CRM, dev tools, docs, comms, etc. per the Part 2/3 guide split) plus its own API/CLI/webhooks mean it can both *consume* other tools' MCP servers and *drive* them via API calls, then hand results to a schedule, trigger, or another app's webhook.

**Dify** and **Magic Patterns** both sit in an interesting dual role: each can be *consumed as an MCP server itself* (Dify apps publish as MCP servers; Magic Patterns exposes designs/artifacts via its own MCP server using the same auth as its REST API). That makes them natural "tool providers" for an MCP client like Cursor, Slashspace, or Gumloop, rather than only being orchestrated *by* something else.

**Cursor** and **Slashspace** are both MCP *clients* with agent capability — they consume external MCP servers/tools mid-conversation rather than hosting their own. Slashspace additionally bridges to 500+ SaaS tools indirectly through Composio, and can delegate to Cursor's or Claude Code's CLI as an "agent provider," which is a direct CLI-to-CLI bridge point between the two.

**AnythingLLM** functions as a RAG/chat frontend that can point its model backend at Ollama (local) or any cloud provider, and separately exposes a small CLI (`@mintplex-labs/anythingllm-hub-cli`) for hub/connection-key management — useful for scripted provisioning rather than end-user chat.

**FlutterFlow** has no native MCP surface, but its whole app-logic model is built around calling arbitrary REST APIs from within a generated app — meaning any of the above (Gumloop workflows, Dify apps, a local Ollama instance tunneled to a public URL, etc.) can be wired in as a FlutterFlow "API Call" action without FlutterFlow needing to know anything about MCP.

**Ultimate Web Scraper** is a one-directional data source: it feeds structured scrape results *out* via webhook or Google Sheets, making it a good front-of-pipeline step feeding into Gumloop, Dify, or a Sheet-reading trigger elsewhere in the stack.

---

## 3. Useful Connection Patterns for Agent Tasks

- **Local-first LLM stack:** AnythingLLM (or Slashspace) → Ollama (local model backend) for fully offline chat/RAG, with cloud providers as an optional BYOK fallback.
- **Expose-and-consume MCP loop:** Build a workflow in Dify or a design flow in Magic Patterns → publish it as an MCP server → consume it as a callable tool from Cursor or Slashspace mid-conversation.
- **Orchestration hub pattern:** Use Gumloop as the top-level controller — trigger on a webhook or schedule, call out to Ollama for local inference, call Dify's API for a published workflow, and write results wherever needed, all from one place using its MCP connector library instead of hand-rolling API clients for each service.
- **No-code app + real backend:** FlutterFlow app UI ↔ REST API calls ↔ a Dify Chatflow or a Gumloop-triggered automation as the actual backend logic, with FlutterFlow handling only presentation/state.
- **Scrape → automate pipeline:** Ultimate Web Scraper's webhook/Sheets export → a Gumloop trigger or Dify Workflow Webhook Trigger → downstream processing (summarization, notification, storage).
- **Coding-agent bridge:** Cursor CLI and Claude Code CLI are each usable as an "agent provider" backend inside Slashspace — meaning a Slashspace canvas node can delegate a coding task to either CLI without leaving the canvas.

---

## 4. Where To Look Next (file + section pointers)

| Need | Open this file, search for |
|---|---|
| Ollama's REST endpoints | `Ollama_Complete_Guide.md` → "API Reference" |
| Gumloop's full MCP connector catalog | `Gumloop_Complete_Guide_Part2_Node_Reference.md`, `Part3_MCP_Connectors.md` |
| Publishing a Dify app as an MCP server | `Dify_Guide_02_Using_Dify_Cloud.md` → "publish-mcp" |
| Magic Patterns MCP tool catalog | `Magic_Patterns_Complete_Guide.md` → "MCP Server" (API Reference section) |
| Cursor's MCP client + CLI usage | `Cursor_Guide_01...md` (Agent/MCP), `Cursor_Guide_03_CLI_Account.md` |
| Slashspace MCP + Composio bridge | `Slashspace_Complete_Guide.md` → "MCP Servers (Beta)", "Connected Tools" |
| AnythingLLM CLI + API | `AnythingLLM_Complete_Guide.md` → "Install the CLI tool" |
| FlutterFlow REST API actions | `FlutterFlow_Guide_04_ResourcesDataAndLogic.md` → "REST APIs" |
| Ultimate Web Scraper webhook export | `UltimateWebScraper_Complete_Guide.md` → "Cloud Integrations: Google Sheets & Webhooks" |

---

## 5. Caveats

- This guide was built from **keyword-frequency scans and summarization of the already-scraped guides**, not a fresh live-documentation crawl — treat specifics (exact endpoint names, current beta status of a feature) as a starting point and verify against the live docs before building production automations, since guide content reflects each site's state at scrape time (2026-07-18).
- Heptabase, PrompTessor, and Sourclip were excluded from the connection patterns section since their documentation shows no programmatic integration surface — they're best used as manual, human-in-the-loop steps in any pipeline that includes them.
