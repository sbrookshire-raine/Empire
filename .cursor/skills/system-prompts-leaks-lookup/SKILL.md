---
name: system-prompts-leaks-lookup
description: Reference-lookup skill for a curated archive of leaked/extracted system prompts from major AI chatbots and coding agents (Claude, ChatGPT, Gemini, Grok, DeepSeek, Qwen, Kimi, GLM, Mistral, Perplexity, Cursor, Notion, Microsoft, Meta, etc.), organized by vendor folder. Use when a user asks what a specific AI product's system prompt says, wants to compare system-prompt structure across vendors, or wants prompt-engineering patterns to reuse when writing a system prompt for their own local Ollama model. Infra-agnostic reference archive — no runtime dependency on any Build1 component.
icon: file-search
color: Grey
---

# System Prompts Leaks — Reference Lookup

Static markdown archive, not executable code — browse and quote directly from the repo's files.

## Repository layout
Top-level folders are vendors: `Anthropic/`, `OpenAI/`, `Google/`, `xAI/`, `DeepSeek/`, `GLM/`, `Kimi/`,
`Meta/`, `Microsoft/`, `Mistral/`, `Notion/`, `Perplexity/`, `Qwen/`, `Cursor/`, `Misc/`. Each folder has one
markdown file per product/surface (e.g. `Google/gemini-2.5-pro-api.md`, `xAI/grok-build.md`). The root
`README.md` is the master index linking every file, often with separate API / web-app / CLI-agent variants
per product.

## How to answer a request
1. **"What's <Product>'s system prompt?"** — check the README index for that vendor to find the exact
   filename/variant, then fetch and quote that file's raw content.
2. **"Compare X vs Y's style"** — fetch both files and summarize structural differences (length, tag/section
   use, tool-definition style, refusal/safety language placement) rather than dumping both verbatim unless
   asked for full text.
3. **"I want prompt-engineering examples for coding agents"** — look at CLI-agent-labeled entries specifically
   (e.g. files tagged "System prompt (CLI Agent)"); check other vendor folders for similar labels.
4. Always attribute the source file/vendor when quoting, and note these are community-collected extractions
   (potentially outdated or slightly inaccurate) rather than official vendor documentation.

## Output
Return the requested system prompt text (quoted, with source file path/vendor noted) or a structured
comparison — do not paraphrase away specific instruction wording if the user asked for the prompt itself.

## Build1 Integration
This archive documents *other vendors'* cloud-hosted models' prompts — it is not something Build1 calls at
runtime. If the goal is to actually reuse a pattern, adapt the borrowed structure into a system prompt for
Build1's **local Ollama** model rather than pointing the user at a cloud API; note this explicitly if a user
seems to be looking for a live prompt they could call, since none of these vendors' APIs are part of
Build1's zero-cloud stack.
