---
name: page-agent-web-integration
description: Integrates page-agent, a JavaScript/TypeScript library (npm package page-agent) that embeds an in-page AI agent directly into any web page via a single script or npm import, using text-based DOM manipulation (no screenshots/multimodal model required) and a bring-your-own-LLM model — configured against local Ollama by default. Use when a user wants to add an AI copilot, natural-language form filling, or in-page automation to a web app, wants a one-line script-tag or npm integration, or asks about page-agent's Chrome extension or MCP server for multi-page tasks. Touches the Build1 frontend (HTMX & Alpine.js), Inference (Local Ollama), and optionally the Nervous System (FastMCP).
icon: mouse-pointer-click
color: Green
---

# Page Agent — In-Page AI Agent for Web Apps

`page-agent` (alibaba/page-agent, "The GUI Agent Living in Your Webpage") lets any web page get its own AI agent with one script, using text-based DOM manipulation — works with locally-deployed LLMs, no browser extension, Python, or headless browser required for the core use case. It builds on `browser-use`. Optional add-ons: a Chrome extension for multi-page tasks and a beta MCP server to control it externally.

## Integration options

**Option 1 — one-line script tag (fastest, no build step):**
```html
<script src="https://unpkg.com/page-agent/dist/page-agent.min.js"></script>
<script>
  PageAgent.init({
    llm: {
      baseURL: "http://localhost:11434/v1",  // local Ollama OpenAI-compatible endpoint
      model: "llama3"
    }
  });
</script>
```
For a strictly zero-cloud setup, self-host the `page-agent.min.js` bundle instead of loading it from a public CDN.

**Option 2 — npm import (for a build-tooled frontend):**
```bash
npm install page-agent
```
```js
import { PageAgent } from "page-agent";
PageAgent.init({ llm: { baseURL: "http://localhost:11434/v1", model: "llama3" } });
```

**Option 3 — MCP server (beta):** run page-agent's MCP server to let an external agent (e.g. a FastMCP-orchestrated Build1 agent) drive multi-page browser tasks rather than embedding the agent inside a single page.

## Build1 Integration
- **Inference**: point page-agent's `llm.baseURL` at the local Ollama OpenAI-compatible API (`http://localhost:11434/v1`) instead of a hosted LLM endpoint.
- **Frontend**: drop the script tag directly into Build1's HTMX/Alpine.js pages — page-agent's DOM-text approach doesn't fight with Alpine's reactivity or htmx swaps.
- **Nervous System**: if multi-page/cross-page automation is needed, run page-agent's MCP server and register it as a tool source for the broader FastMCP-based agent layer.
