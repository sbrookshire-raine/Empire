# Cursor Documentation — Complete Guide (Part 1: Getting Started, Agent, and Customizing)

> **NotebookLM ingestion note:** This is 1 of 3 companion files covering the official Cursor documentation. Upload all 3 parts (plus the index file, if provided) as sources in the same NotebookLM notebook to build a complete learning plan. Each page below is a cleaned, self-contained section with its original source URL cited.

- **Source:** https://cursor.com/docs (official Cursor documentation)
- **Pages in this file:** 34
- **Total pages across all parts:** 101
- **Date compiled:** 2026-07-18

## Table of Contents

- [Get Started](#get-started)
  - [Cursor Documentation](#cursor-documentation)
  - [Quickstart](#quickstart)
  - [Models & Pricing](#models-pricing)
  - [Claude Sonnet 5](#claude-sonnet-5)
  - [Claude Opus 4.8](#claude-opus-48)
  - [Claude Fable 5](#claude-fable-5)
  - [Gemini 3.1 Pro](#gemini-31-pro)
  - [Gemini 3.5 Flash](#gemini-35-flash)
  - [GPT 5.6 Sol](#gpt-56-sol)
  - [GPT 5.6 Terra](#gpt-56-terra)
  - [GPT 5.6 Luna](#gpt-56-luna)
  - [Grok 4.5](#grok-45)
  - [Cursor Composer 2.5](#cursor-composer-25)
- [Agent](#agent)
  - [Cursor Agent](#cursor-agent)
  - [Agents Window](#agents-window)
  - [Agent Review](#agent-review)
  - [Plan Mode](#plan-mode)
  - [Prompting agents](#prompting-agents)
  - [Debug Mode](#debug-mode)
  - [Design Mode](#design-mode)
  - [Terminal](#terminal)
  - [Browser](#browser)
  - [Semantic & agentic search](#semantic-agentic-search)
  - [Canvases](#canvases)
  - [Worktrees](#worktrees)
  - [Agent Security](#agent-security)
  - [Run Modes](#run-modes)
- [Customizing Cursor](#customizing-cursor)
  - [Customize Cursor](#customize-cursor)
  - [Plugins](#plugins)
  - [Rules](#rules)
  - [Agent Skills](#agent-skills)
  - [Subagents](#subagents)
  - [Hooks](#hooks)
  - [Model Context Protocol (MCP)](#model-context-protocol-mcp)

---
## Get Started

### Cursor Documentation

*Cursor is a coding agent for building ambitious software. Use it to understand your codebase, plan and build features, fix bugs, review changes, and work with the tools you already use.*

**Source:** https://cursor.com/docs

Cursor is a coding agent for building ambitious software. Use it to understand your codebase, plan and build features, fix bugs, review changes, and work with the tools you already use.

![Welcome to Cursor, the AI editor and coding agent](https://cursor.com/docs-static/images/agent/homepage-hero.png)

#### Start here

##### Get started

Go from install to your first useful change in Cursor

##### Models & Pricing

Compare models, usage pools, and plan pricing

##### Changelog

Stay up to date with the latest features and improvements

#### What you can do with Cursor

##### Understand your code

Trace how a repo fits together and find the right places to start

##### Plan and build features

Scope changes, use Plan Mode, and ship bigger work with confidence

##### Find and fix bugs

Reproduce issues, narrow the root cause, and verify the fix

##### Review changes

Inspect diffs, run checks, and catch problems before you merge

##### Customize Cursor

Add plugins, skills, MCPs, and rules from one place

##### Connect your workflow

Work with GitHub, GitLab, Azure DevOps, Bitbucket, JetBrains, Slack, Linear, and more

#### Models

See all model attributes on the [Models & Pricing](https://cursor.com/docs/models-and-pricing.md) page.

| Model                                                                                         | Provider  | Default context | Max context | Capabilities            | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------- | --------- | --------------- | ----------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Claude 4 Sonnet](https://www.anthropic.com/claude/sonnet)                                    | Anthropic | 200k            | -           | Agent, Thinking, Images | Hidden by default; Thinking variant counts as 2 requests in legacy pricing                                                                                                                                                                                                                                                                                                                                                                      |
| [Claude 4 Sonnet 1M](https://www.anthropic.com/claude/sonnet)                                 | Anthropic | -               | 1M          | Agent, Thinking, Images | Hidden by default; Thinking variant counts as 2 requests in legacy pricing; This model can be very expensive due to the large context window; The cost is 2x when the input exceeds 200k tokens                                                                                                                                                                                                                                                 |
| [Claude 4.5 Haiku](https://www.anthropic.com/claude/haiku)                                    | Anthropic | 200k            | -           | Thinking, Images        | Hidden by default; Bedrock/Vertex: regional endpoints +10% surcharge; Cache: writes 1.25x, reads 0.1x                                                                                                                                                                                                                                                                                                                                           |
| [Claude 4.5 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | 200k            | 200k        | Agent, Thinking, Images | Hidden by default; Requires Max Mode on legacy request-based plans                                                                                                                                                                                                                                                                                                                                                                              |
| [Claude 4.5 Sonnet](https://www.anthropic.com/claude/sonnet)                                  | Anthropic | 200k            | 1M          | Agent, Thinking, Images | Hidden by default; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                                                                               |
| [Claude 4.6 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | 200k            | 1M          | Agent, Thinking, Images | Hidden by default; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                                                                               |
| [Claude 4.6 Sonnet](https://www.anthropic.com/claude/sonnet)                                  | Anthropic | 200k            | 1M          | Agent, Thinking, Images | Hidden by default; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                                                                               |
| [Claude 4.7 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | 300k            | 1M          | Agent, Thinking, Images | Hidden by default; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                                                                               |
| [Claude Fable 5](https://www.anthropic.com/claude)                                            | Anthropic | 300k            | 1M          | Agent, Thinking, Images | Requires data retention approval for Enterprise customers, Teams and individual customers with Privacy Mode enabled; Anthropic stores agent input and output data for harm-prevention processes; this data is not used to train or improve Anthropic models or products; Requests that trip a security guardrail are automatically routed to Claude Opus; About 2x the cost of Claude Opus 4.8; Requires Max Mode on legacy request-based plans |
| [Claude Opus 4.7 (fast mode)](https://www.anthropic.com/claude/opus)                          | Anthropic | 200k            | 1M          | Agent, Thinking, Images | Hidden by default; Requires Max Mode on legacy request-based plans; Limited research preview; Up to 1M tokens with extended context at the same per-token rates as shorter context                                                                                                                                                                                                                                                              |
| [Claude Opus 4.8](https://www.anthropic.com/claude/opus)                                      | Anthropic | 300k            | 1M          | Agent, Thinking, Images | Requires Max Mode on legacy request-based plans; Fast mode (\`claude-opus-4-8-fast\`) requires Max Mode on legacy request-based plans; Fast mode is 3x lower per-token pricing than Opus 4.7 fast mode; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                           |
| [Claude Sonnet 5](https://www.anthropic.com/claude/sonnet)                                    | Anthropic | 200k            | 1M          | Agent, Thinking, Images | Launch promotion: $2/M input and $10/M output through August 31, 2026; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge); Uses an updated tokenizer, so the same input can map to more tokens                                                                                                                                                      |
| [Composer 1](https://cursor.com)                                                              | Cursor    | 200k            | -           | Agent, Images           | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Composer 2.5](https://cursor.com/blog/composer-2-5)                                          | Cursor    | 200k            | -           | Agent, Thinking, Images | -                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 2.5 Flash](https://developers.googleblog.com/en/start-building-with-gemini-25-flash/) | Google    | 200k            | 1M          | Agent, Thinking, Images | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 3 Flash](https://ai.google.dev/gemini-api/docs)                                       | Google    | 200k            | 1M          | Agent, Thinking, Images | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 3 Pro](https://ai.google.dev/gemini-api/docs)                                         | Google    | 200k            | 1M          | Agent, Thinking, Images | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 3 Pro Image Preview](https://ai.google.dev/gemini-api/docs)                           | Google    | 200k            | 1M          | Images                  | Hidden by default; Native image generation model optimized for speed, flexibility, and contextual understanding; Text input and output priced the same as Gemini 3 Pro; Image output: $120/1M tokens (\~$0.134 per 1K/2K image, \~$0.24 per 4K image); Preview models may change before becoming stable and have more restrictive rate limits                                                                                                   |
| [Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs)                                       | Google    | 200k            | 1M          | Agent, Thinking, Images | -                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs)                                     | Google    | 200k            | 1M          | Agent, Thinking, Images | -                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GLM 5.2](https://z.ai)                                                                       | Z.ai      | 200k            | -           | Agent, Thinking         | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GPT-5](https://openai.com/index/gpt-5/)                                                      | OpenAI    | 272k            | -           | Agent, Thinking, Images | Hidden by default; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5-high                                                                                                                                                                                                                                                                                                                                         |
| [GPT-5 Fast](https://openai.com/index/gpt-5/)                                                 | OpenAI    | 272k            | -           | Agent, Thinking, Images | Hidden by default; Faster speed but 2x price; Available reasoning effort variants are gpt-5-high-fast, gpt-5-low-fast                                                                                                                                                                                                                                                                                                                           |
| [GPT-5 Mini](https://openai.com/index/gpt-5/)                                                 | OpenAI    | 272k            | -           | Agent, Thinking, Images | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GPT-5-Codex](https://platform.openai.com/docs/models/gpt-5-codex)                            | OpenAI    | 272k            | -           | Agent, Thinking, Images | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                                                                                                                           |
| [GPT-5.1 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | 272k            | -           | Agent, Thinking, Images | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                                                                                                                           |
| [GPT-5.1 Codex Max](https://platform.openai.com/docs/models/gpt-5-codex)                      | OpenAI    | 272k            | -           | Agent, Thinking, Images | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GPT-5.1 Codex Mini](https://platform.openai.com/docs/models/gpt-5-codex)                     | OpenAI    | 272k            | -           | Agent, Thinking, Images | Hidden by default; Agentic and reasoning capabilities; 4x rate limits compared to GPT-5.1 Codex                                                                                                                                                                                                                                                                                                                                                 |
| [GPT-5.2](https://openai.com/index/gpt-5/)                                                    | OpenAI    | 272k            | -           | Agent, Thinking, Images | Hidden by default; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5.2-high                                                                                                                                                                                                                                                                                                                                       |
| [GPT-5.2 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | 272k            | -           | Agent, Thinking, Images | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                                                                                                                           |
| [GPT-5.3 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | 272k            | -           | Agent, Thinking, Images | Hidden by default; Requires Max Mode on legacy request-based plans; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5.3-codex-high                                                                                                                                                                                                                                                                                |
| [GPT-5.4](https://developers.openai.com/api/docs/models/gpt-5.4)                              | OpenAI    | 272k            | 1M          | Agent, Thinking, Images | Hidden by default; Requires Max Mode on legacy request-based plans; Agentic and reasoning capabilities; 90% discount on cached input tokens; Fast mode is 15% faster with 2x pricing; Long context supports up to 1M tokens with 2x input pricing                                                                                                                                                                                               |
| [GPT-5.4 Mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini)                    | OpenAI    | 272k            | -           | Agent, Thinking, Images | Hidden by default; Smaller, faster variant of GPT-5.4; 90% discount on cached input tokens                                                                                                                                                                                                                                                                                                                                                      |
| [GPT-5.4 Nano](https://developers.openai.com/api/docs/models/gpt-5.4-nano)                    | OpenAI    | 272k            | -           | Agent, Thinking, Images | Hidden by default; Smallest GPT-5.4 variant, optimized for cost; 90% discount on cached input tokens                                                                                                                                                                                                                                                                                                                                            |
| [GPT-5.5](https://developers.openai.com/api/docs/models/gpt-5.5)                              | OpenAI    | 272k            | 1M          | Agent, Thinking, Images | Hidden by default; Requires Max Mode on legacy request-based plans; Agentic and reasoning capabilities; More token-efficient than GPT-5.4 on comparable tasks; Improved persistence on long-running tasks; Fast mode is available at higher rates; Long context supports up to 1M tokens with 2x input pricing                                                                                                                                  |
| [GPT-5.6 Luna](https://openai.com/index/previewing-gpt-5-6-sol/)                              | OpenAI    | 272k            | -           | Agent, Thinking, Images | Smallest GPT-5.6 variant, optimized for cost and speed; Agentic and reasoning capabilities; Fast mode is available at 2x pricing; Cache writes are billed at 1.25x the uncached input rate                                                                                                                                                                                                                                                      |
| [GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)                               | OpenAI    | 272k            | 1M          | Agent, Thinking, Images | Requires Max Mode on legacy request-based plans; Agentic and reasoning capabilities; Fast mode is available at 2x pricing; Long context supports up to 1M tokens with 2x input pricing; Cache writes are billed at 1.25x the uncached input rate                                                                                                                                                                                                |
| [GPT-5.6 Terra](https://openai.com/index/previewing-gpt-5-6-sol/)                             | OpenAI    | 272k            | -           | Agent, Thinking, Images | Mid-tier GPT-5.6 variant between Sol and Luna; Agentic and reasoning capabilities; Fast mode is available at 2x pricing; Cache writes are billed at 1.25x the uncached input rate                                                                                                                                                                                                                                                               |
| Grok 4.5                                                                                      | Cursor    | 256k            | -           | Agent, Thinking         | Jointly trained by Cursor and SpaceXAI                                                                                                                                                                                                                                                                                                                                                                                                          |
| Kimi K2.7 Code                                                                                | Moonshot  | 262k            | -           | Agent, Thinking, Images | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |

#### More resources

##### Downloads

Get Cursor for your computer

##### Help

Find answers to common questions and troubleshooting guides

For account and billing questions, contact our support team


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Quickstart

*This guide gets you from install to your first useful change in Cursor. You'll sign in, ask Cursor to explain your codebase, make a small edit, and review the result.*

**Source:** https://cursor.com/docs/get-started/quickstart

This guide gets you from install to your first useful change in Cursor. You'll sign in, ask Cursor to explain your codebase, make a small edit, and review the result.

##### Install Cursor and sign in

Download Cursor. Open the app and sign in. Then pick a folder and start with a small task.

##### macOS

- macOS 12 (Monterey) and later
- Native installer (.dmg)
- Apple Silicon and Intel support

##### Windows

- Windows 10 and later
- Native installer (.exe)

##### Linux

**Debian/Ubuntu (recommended)**

```bash
# Add Cursor's GPG key
curl -fsSL https://downloads.cursor.com/keys/anysphere.asc | gpg --dearmor | sudo tee /etc/apt/keyrings/cursor.gpg > /dev/null

# Add the Cursor repository
echo "deb [arch=amd64,arm64 signed-by=/etc/apt/keyrings/cursor.gpg] https://downloads.cursor.com/aptrepo stable main" | sudo tee /etc/apt/sources.list.d/cursor.list > /dev/null

# Update and install
sudo apt update
sudo apt install cursor
```

**RHEL/Fedora**

```bash
# Add Cursor's repository
sudo tee /etc/yum.repos.d/cursor.repo << 'EOF'
[cursor]
name=Cursor
baseurl=https://downloads.cursor.com/yumrepo
enabled=1
gpgcheck=1
gpgkey=https://downloads.cursor.com/keys/anysphere.asc
EOF

# Install Cursor
sudo dnf install cursor
```

**AppImage (portable)**

Download the `.AppImage` file from [cursor.com/downloads](https://cursor.com/downloads), then:

```bash
chmod +x Cursor-*.AppImage
./Cursor-*.AppImage
```

The apt and yum packages are preferred over AppImage. They provide desktop icons, automatic updates, and CLI tools.

##### Ask Cursor to explain your codebase

After you pick a folder, open Agent with Cmd I. Ask Cursor to explain the codebase and point out the main areas to read first.

Explain this codebase. Point me to the main entry points, key modules, and anything I should read before making changes.

Cursor will search your repo, read relevant files, and summarize how the project fits together. This is one of the fastest ways to get oriented in an unfamiliar codebase.

Want a deeper walkthrough? See [Understand your codebase](https://cursor.com/learn/understanding-your-codebase.md).

##### Make one small change

Once you understand the project, ask Cursor to suggest a few safe improvements. Pick one and ask it to make the change.

Suggest three small, safe improvements in this codebase. Explain the tradeoffs and wait for me to choose one.

Good first tasks are low risk, like improving some copywriting or fixing small UI issues.

If you already know what you want to change, ask for it directly and describe the result you want.

##### Review the diff and verify the result

Now you can watch Cursor work. The diff view shows changes made by the agent.

When it finishes, review the diff and ask Cursor to run the checks your project already uses. That can mean tests, the type checker, linting, or a local build.

Want a stronger review workflow? See [Reviewing and testing code](https://cursor.com/learn/reviewing-testing.md).

##### Use Plan Mode for bigger changes

Now that you know the basics, use Plan Mode for bigger changes. It works well when the task spans multiple files, needs research, or needs approval before coding.

Press Shift+Tab in the agent input to toggle **Plan Mode**. Instead of writing code right away, Cursor will:

1. Research your codebase to find relevant files
2. Ask clarifying questions about your requirements
3. Create a detailed implementation plan
4. Wait for your approval before building

For a deeper walkthrough, see [Build new features](https://cursor.com/learn/creating-features.md).

#### Next steps

##### Agent Overview

Learn about Agent's tools and capabilities

##### Rules

Create persistent instructions for your project

##### Understand your code

Learn how to get oriented in an unfamiliar repo

##### Build new features

See a full workflow for shipping larger changes


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Models & Pricing

*Cursor supports frontier models from OpenAI, Anthropic, Google, SpaceXAI, and more. Every individual plan includes two usage pools so you can pick the right balance of intelligence, speed, and cost.*

**Source:** https://cursor.com/docs/models-and-pricing

Cursor supports frontier models from OpenAI, Anthropic, Google, SpaceXAI, and more. Every individual plan includes two usage pools so you can pick the right balance of intelligence, speed, and cost.

#### Usage pools

There are two separate usage pools for individual plans, each resetting with your monthly billing cycle:

- **First-party models**: Significantly more included usage with Auto, Composer 2.5, and Grok 4.5.
- **API**: Charged at the model's API price. Individual plans include at least $20 of API usage each month (more on higher tiers) with the option to pay for additional usage as needed.

Both pools are visible in your editor settings and on your [usage dashboard](https://cursor.com/dashboard/usage).

#### First-party models pool

Auto allows Cursor to select models that balance intelligence, cost efficiency, and reliability. It is useful for everyday tasks.

The First-party models pool includes Auto, Composer 2.5, and Grok 4.5.

##### Auto pricing

| Token type          | Price per 1M tokens |
| :------------------ | :------------------ |
| Input + Cache Write | $1.25               |
| Output              | $6.00               |
| Cache Read          | $0.25               |

##### Composer pricing

Composer 2.5 is Cursor's own model, trained to be highly capable for agentic coding.

##### Grok 4.5 pricing

Grok 4.5 is jointly trained by Cursor and SpaceXAI for long-running coding and knowledge work.

#### API pool

When you select a specific model, usage is drawn from the API pool at that model's API rate.

##### Model pricing

All prices are per million tokens:

| Model                                                                                         | Provider  | Input | Cache write | Cache read | Output | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------- | --------- | ----- | ----------- | ---------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Claude 4 Sonnet](https://www.anthropic.com/claude/sonnet)                                    | Anthropic | $3    | $3.75       | $0.3       | $15    | Hidden by default; Thinking variant counts as 2 requests in legacy pricing                                                                                                                                                                                                                                                                                                                                                                      |
| [Claude 4 Sonnet 1M](https://www.anthropic.com/claude/sonnet)                                 | Anthropic | $6    | $7.5        | $0.6       | $22.5  | Hidden by default; Thinking variant counts as 2 requests in legacy pricing; This model can be very expensive due to the large context window; The cost is 2x when the input exceeds 200k tokens                                                                                                                                                                                                                                                 |
| [Claude 4.5 Haiku](https://www.anthropic.com/claude/haiku)                                    | Anthropic | $1    | $1.25       | $0.1       | $5     | Hidden by default; Bedrock/Vertex: regional endpoints +10% surcharge; Cache: writes 1.25x, reads 0.1x                                                                                                                                                                                                                                                                                                                                           |
| [Claude 4.5 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | $5    | $6.25       | $0.5       | $25    | Hidden by default; Requires Max Mode on legacy request-based plans                                                                                                                                                                                                                                                                                                                                                                              |
| [Claude 4.5 Sonnet](https://www.anthropic.com/claude/sonnet)                                  | Anthropic | $3    | $3.75       | $0.3       | $15    | Hidden by default; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                                                                               |
| [Claude 4.6 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | $5    | $6.25       | $0.5       | $25    | Hidden by default; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                                                                               |
| [Claude 4.6 Sonnet](https://www.anthropic.com/claude/sonnet)                                  | Anthropic | $3    | $3.75       | $0.3       | $15    | Hidden by default; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                                                                               |
| [Claude 4.7 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | $5    | $6.25       | $0.5       | $25    | Hidden by default; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                                                                               |
| [Claude Fable 5](https://www.anthropic.com/claude)                                            | Anthropic | $10   | $12.5       | $1         | $50    | Requires data retention approval for Enterprise customers, Teams and individual customers with Privacy Mode enabled; Anthropic stores agent input and output data for harm-prevention processes; this data is not used to train or improve Anthropic models or products; Requests that trip a security guardrail are automatically routed to Claude Opus; About 2x the cost of Claude Opus 4.8; Requires Max Mode on legacy request-based plans |
| [Claude Opus 4.7 (fast mode)](https://www.anthropic.com/claude/opus)                          | Anthropic | $30   | $37.5       | $3         | $150   | Hidden by default; Requires Max Mode on legacy request-based plans; Limited research preview; Up to 1M tokens with extended context at the same per-token rates as shorter context                                                                                                                                                                                                                                                              |
| [Claude Opus 4.8](https://www.anthropic.com/claude/opus)                                      | Anthropic | $5    | $6.25       | $0.5       | $25    | Requires Max Mode on legacy request-based plans; Fast mode (\`claude-opus-4-8-fast\`) requires Max Mode on legacy request-based plans; Fast mode is 3x lower per-token pricing than Opus 4.7 fast mode; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                           |
| [Claude Sonnet 5](https://www.anthropic.com/claude/sonnet)                                    | Anthropic | $3    | $3.75       | $0.3       | $15    | Launch promotion: $2/M input and $10/M output through August 31, 2026; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge); Uses an updated tokenizer, so the same input can map to more tokens                                                                                                                                                      |
| [Composer 1](https://cursor.com)                                                              | Cursor    | $1.25 | -           | $0.125     | $10    | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Composer 2.5](https://cursor.com/blog/composer-2-5)                                          | Cursor    | $0.5  | -           | $0.2       | $2.5   | -                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 2.5 Flash](https://developers.googleblog.com/en/start-building-with-gemini-25-flash/) | Google    | $0.3  | -           | $0.03      | $2.5   | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 3 Flash](https://ai.google.dev/gemini-api/docs)                                       | Google    | $0.5  | -           | $0.05      | $3     | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 3 Pro](https://ai.google.dev/gemini-api/docs)                                         | Google    | $2    | -           | $0.2       | $12    | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 3 Pro Image Preview](https://ai.google.dev/gemini-api/docs)                           | Google    | $2    | -           | $0.2       | $12    | Hidden by default; Native image generation model optimized for speed, flexibility, and contextual understanding; Text input and output priced the same as Gemini 3 Pro; Image output: $120/1M tokens (\~$0.134 per 1K/2K image, \~$0.24 per 4K image); Preview models may change before becoming stable and have more restrictive rate limits                                                                                                   |
| [Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs)                                       | Google    | $2    | -           | $0.2       | $12    | -                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs)                                     | Google    | $1.5  | -           | $0.15      | $9     | -                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GLM 5.2](https://z.ai)                                                                       | Z.ai      | $1.4  | -           | $0.26      | $4.4   | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GPT-5](https://openai.com/index/gpt-5/)                                                      | OpenAI    | $1.25 | -           | $0.125     | $10    | Hidden by default; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5-high                                                                                                                                                                                                                                                                                                                                         |
| [GPT-5 Fast](https://openai.com/index/gpt-5/)                                                 | OpenAI    | $2.5  | -           | $0.25      | $20    | Hidden by default; Faster speed but 2x price; Available reasoning effort variants are gpt-5-high-fast, gpt-5-low-fast                                                                                                                                                                                                                                                                                                                           |
| [GPT-5 Mini](https://openai.com/index/gpt-5/)                                                 | OpenAI    | $0.25 | -           | $0.025     | $2     | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GPT-5-Codex](https://platform.openai.com/docs/models/gpt-5-codex)                            | OpenAI    | $1.25 | -           | $0.125     | $10    | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                                                                                                                           |
| [GPT-5.1 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | $1.25 | -           | $0.125     | $10    | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                                                                                                                           |
| [GPT-5.1 Codex Max](https://platform.openai.com/docs/models/gpt-5-codex)                      | OpenAI    | $1.25 | -           | $0.125     | $10    | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GPT-5.1 Codex Mini](https://platform.openai.com/docs/models/gpt-5-codex)                     | OpenAI    | $0.25 | -           | $0.025     | $2     | Hidden by default; Agentic and reasoning capabilities; 4x rate limits compared to GPT-5.1 Codex                                                                                                                                                                                                                                                                                                                                                 |
| [GPT-5.2](https://openai.com/index/gpt-5/)                                                    | OpenAI    | $1.75 | -           | $0.175     | $14    | Hidden by default; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5.2-high                                                                                                                                                                                                                                                                                                                                       |
| [GPT-5.2 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | $1.75 | -           | $0.175     | $14    | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                                                                                                                           |
| [GPT-5.3 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | $1.75 | -           | $0.175     | $14    | Hidden by default; Requires Max Mode on legacy request-based plans; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5.3-codex-high                                                                                                                                                                                                                                                                                |
| [GPT-5.4](https://developers.openai.com/api/docs/models/gpt-5.4)                              | OpenAI    | $2.5  | -           | $0.25      | $15    | Hidden by default; Requires Max Mode on legacy request-based plans; Agentic and reasoning capabilities; 90% discount on cached input tokens; Fast mode is 15% faster with 2x pricing; Long context supports up to 1M tokens with 2x input pricing                                                                                                                                                                                               |
| [GPT-5.4 Mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini)                    | OpenAI    | $0.75 | -           | $0.075     | $4.5   | Hidden by default; Smaller, faster variant of GPT-5.4; 90% discount on cached input tokens                                                                                                                                                                                                                                                                                                                                                      |
| [GPT-5.4 Nano](https://developers.openai.com/api/docs/models/gpt-5.4-nano)                    | OpenAI    | $0.2  | -           | $0.02      | $1.25  | Hidden by default; Smallest GPT-5.4 variant, optimized for cost; 90% discount on cached input tokens                                                                                                                                                                                                                                                                                                                                            |
| [GPT-5.5](https://developers.openai.com/api/docs/models/gpt-5.5)                              | OpenAI    | $5    | -           | $0.5       | $30    | Hidden by default; Requires Max Mode on legacy request-based plans; Agentic and reasoning capabilities; More token-efficient than GPT-5.4 on comparable tasks; Improved persistence on long-running tasks; Fast mode is available at higher rates; Long context supports up to 1M tokens with 2x input pricing                                                                                                                                  |
| [GPT-5.6 Luna](https://openai.com/index/previewing-gpt-5-6-sol/)                              | OpenAI    | $1    | $1.25       | $0.1       | $6     | Smallest GPT-5.6 variant, optimized for cost and speed; Agentic and reasoning capabilities; Fast mode is available at 2x pricing; Cache writes are billed at 1.25x the uncached input rate                                                                                                                                                                                                                                                      |
| [GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)                               | OpenAI    | $5    | $6.25       | $0.5       | $30    | Requires Max Mode on legacy request-based plans; Agentic and reasoning capabilities; Fast mode is available at 2x pricing; Long context supports up to 1M tokens with 2x input pricing; Cache writes are billed at 1.25x the uncached input rate                                                                                                                                                                                                |
| [GPT-5.6 Terra](https://openai.com/index/previewing-gpt-5-6-sol/)                             | OpenAI    | $2.5  | $3.125      | $0.25      | $15    | Mid-tier GPT-5.6 variant between Sol and Luna; Agentic and reasoning capabilities; Fast mode is available at 2x pricing; Cache writes are billed at 1.25x the uncached input rate                                                                                                                                                                                                                                                               |
| Grok 4.5                                                                                      | Cursor    | $2    | -           | $0.5       | $6     | Jointly trained by Cursor and SpaceXAI                                                                                                                                                                                                                                                                                                                                                                                                          |
| Kimi K2.7 Code                                                                                | Moonshot  | $0.95 | -           | $0.19      | $4     | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |

Opting in to regional data residency incurs a 10% uplift on Model pricing for eligible Models. See [Privacy and Data Governance](https://cursor.com/docs/enterprise/privacy-and-data-governance.md) for details on supported regions, Models, functions and data residency policies.

#### Plans

All individual plans include unlimited tab completions, extended agent usage limits on all models, access to Bugbot, and access to Cloud Agents.

| Plan         | Price   | API usage included | First-party models pool |
| :----------- | :------ | :----------------- | :---------------------- |
| **Pro**      | $20/mo  | $20                | Generous included usage |
| **Pro Plus** | $60/mo  | $70                | Generous included usage |
| **Ultra**    | $200/mo | $400               | Generous included usage |

Since different models have different API costs, your model selection affects how quickly your included usage is consumed.

##### How much usage do I need?

- **Daily Tab users**: Always stay within $20
- **Limited Agent users**: Often stay within the included $20
- **Daily Agent users**: Typically $60–$100/mo total usage
- **Power users (multiple agents/automation)**: Often $200+/mo total usage

##### What happens when I reach my limit?

When you exceed your included monthly usage, you can either:

- **Add on-demand usage**: Continue at the same API rates with pay-as-you-go billing
- **Upgrade your plan**: Move to a higher tier for more included usage

On-demand usage is billed monthly at the same rates. Requests are never downgraded in quality or speed.

##### Teams

There are two business plans: Teams and Enterprise (Custom). Teams offers two seat types: Standard ($40/user/mo) and Premium ($120/user/mo), where Premium adds 5x the Standard limits on Agent.

Team plans provide additional features like centralized team billing and administration, a team marketplace for internal rules, skills, and plugins, agentic code reviews with Bugbot, cloud agents and automations with shared team context, usage analytics, team-wide privacy mode enforcement, and SAML/OIDC SSO.

We recommend Teams for any customer that is happy self-serving. We recommend [Enterprise](https://cursor.com/contact-sales?source=docs-models-pricing) for customers that need priority support, pooled usage, invoicing, SCIM, or advanced security controls.

Learn more about [Teams pricing](https://cursor.com/docs/account/teams/pricing.md).

#### Cursor Token Rate

On Teams and Enterprise plans, non-Auto third-party model requests include a Cursor Token Rate of $0.25 per million tokens. This rate applies on top of model API pricing for included usage, on-demand usage, and BYOK usage. Auto requests and all first-party models, including Composer 2.5 and Grok 4.5, are exempt from the Cursor Token Rate.

#### Legacy request-based pricing

##### Max Mode

Max Mode is available only on legacy request-based plans. It extends a model's context window beyond the default limit and is billed at the model's API rate plus 20%. See [Max Mode on legacy plans](https://cursor.com/help/ai-features/max-mode.md) for details.

#### FAQ

##### Where are models hosted?

Models are hosted on US, Canada, & Iceland based infrastructure by the model's provider, a trusted partner, or Cursor directly. For details, see our list of [sub-processors](https://trust.cursor.com/subprocessors).

##### Where can I find pricing terms?

For enterprise pricing details, billing terms, and fee calculations, see the [Pricing Policy](https://cursor.com/terms/pricing).


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Claude Sonnet 5

*Claude Sonnet 5 is Anthropic's latest medium-tier model and replaces Sonnet 4.6. It pushes quality close to Opus 4.8 while keeping Sonnet's lower per-token price. It supports thinking mode and context windows up to 1M tokens, making it a strong default for everyday coding when you want frontier reasoning without Opus pricing.*

**Source:** https://cursor.com/docs/models/claude-sonnet-5

Claude Sonnet 5 is Anthropic's latest medium-tier model and replaces Sonnet 4.6. It pushes quality close to Opus 4.8 while keeping Sonnet's lower per-token price. It supports thinking mode and context windows up to 1M tokens, making it a strong default for everyday coding when you want frontier reasoning without Opus pricing.

#### Strengths

- Near-Opus quality. Sonnet 5 closes most of the gap to Opus 4.8 on real coding work while staying far cheaper per token.
- Strong reasoning. Thinking mode handles multi-step tasks, planning, and debugging with depth.
- Reliable tool use. It calls tools purposefully and chains results into follow-up actions.
- Same provider and style as Opus at a lower price point.

#### Limitations

- For peak quality on the hardest tasks, Opus 4.8 remains the stronger choice.
- The updated tokenizer maps the same input to more tokens, so token counts run higher than older Sonnet models.

#### Tools

Sonnet 5 has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

#### Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. Sonnet 5 draws from the **API** pool, which charges at the rates below. Individual plans include at least $20 of API usage each month (more on higher tiers). All prices are per million tokens.

A launch promotion lowers pricing to $2/M input and $10/M output through August 31, 2026. After that, standard pricing of $3/M input and $15/M output applies.

All Sonnet 5 prompts bill at the base per-token rates in the table above, including when context goes above 200k. There is no separate long-context multiplier for Sonnet 5.

A thinking variant is available for deeper reasoning.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Claude Opus 4.8

*Claude Opus 4.8 is Anthropic's strongest model and a meaningful jump over Opus 4.7 on [CursorBench](https://cursor.com/blog/cursorbench). It excels at autonomous, multi-step work: it holds intent across long sessions, self-corrects when it hits friction, and writes production-ready code without hand-holding. We recommend the high thinking variant for the best results.*

**Source:** https://cursor.com/docs/models/claude-opus-4-8

Claude Opus 4.8 is Anthropic's strongest model and a meaningful jump over Opus 4.7 on [CursorBench](https://cursor.com/blog/cursorbench). It excels at autonomous, multi-step work: it holds intent across long sessions, self-corrects when it hits friction, and writes production-ready code without hand-holding. We recommend the high thinking variant for the best results.

#### Strengths

- Autonomous and self-directed. Opus 4.8 drives multi-step tasks to completion without losing track of the goal, even across large codebases and long conversations.
- Creative reasoning. It approaches problems from unexpected angles, explores alternative solutions, and produces more inventive code than its predecessor.
- Strong at planning. It maps out work before executing, catches edge cases early, and builds coherent architectures across many files.
- Reliable tool use. It calls tools purposefully, chains tool results into follow-up actions, and adapts when tool output surprises it.

#### Limitations

- Most expensive model. Consumes usage limits faster than alternatives.
- Can over-elaborate in long sessions where brevity matters more than depth.

#### Tools

Opus 4.8 has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

#### Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. Opus 4.8 draws from the **API** pool, which charges at the rates below. Individual plans include at least $20 of API usage each month (more on higher tiers). All prices are per million tokens.

A **Fast mode** tier (`claude-opus-4-8-fast`) is available for roughly 2.5x faster output. On legacy request-based plans, it requires Max Mode. It bills at $10/M input and $50/M output tokens, 3x lower than Opus 4.7 fast mode. Use it selectively for time-sensitive or critical work.

All Opus 4.8 prompts bill at the base per-token rates in the table above, including when context goes above 300k. There is no separate long-context multiplier for Opus 4.8. Context windows up to 1M tokens use the same rates.

Opus 4.8 supports a thinking variant for deeper reasoning. We recommend using the high thinking variant for the strongest results.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Claude Fable 5

*Claude Fable 5 is Anthropic's most capable generally available model for autonomous knowledge work and coding. It is a Mythos-class model with strong safeguards, built to handle long-running, complex, and asynchronous tasks where earlier models needed more frequent check-ins.*

**Source:** https://cursor.com/docs/models/claude-fable-5

Claude Fable 5 is Anthropic's most capable generally available model for autonomous knowledge work and coding. It is a Mythos-class model with strong safeguards, built to handle long-running, complex, and asynchronous tasks where earlier models needed more frequent check-ins.

Fable 5 also leads every other model on [CursorBench](https://cursor.com/evals), our benchmark for real-world coding work. It costs about twice as much as Claude Opus 4.8, so it's a strong fit for your team's most complex agentic work.

#### Enabling Fable 5

Fable 5 has new privacy considerations because of how Anthropic handles data retention for these models. If Privacy Mode is enabled for your account, team, or organization, you will need to approve Fable 5's Data Retention Policy in the Cursor Dashboard before you can use the model. You can view the policy in the [Cursor Dashboard](https://cursor.com/dashboard/restricted_models/claude-fable-5).

For Teams accounts, approving the model policy applies to the entire Team.

For Enterprise accounts, model availability is approved at the Organization level but continues to be controlled at the team and group level in the [Model Access controls](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control).

Head to [Team Settings](https://cursor.com/dashboard/restricted_models/claude-fable-5) to enable Fable 5 for your Team, Organization, or account.

#### Strengths

- Highest capability in Cursor. Fable 5 tops CursorBench and handles the most complex, multi-step problems.
- Built for long-running, asynchronous work. It holds intent across long sessions and drives tasks to completion with fewer check-ins.
- Deep reasoning. A thinking variant is available for problems that reward extra deliberation.

#### Data retention

Anthropic's policy for Fable models is described in detail [here](https://trust.anthropic.com/resources?s=7ksqkied5hn0pocsj206m\&name=%5Banthropic%5D-security-and-privacy-design-of-anthropic-data-retention-and-review) and as follows:

- Retained customer data is being deleted after 30 days, automatically and permanently, unless subject to a safety investigation or legal hold
- Retained customer data is not readable by any person by default
- Retained enterprise data is not being used to train Claude
- Retained customer data is not being shared with other customers

Enabling and using Fable 5 does not change your Privacy Mode settings or Cursor's own retention of your data.

Because of how Fable 5 handles data, it is off by default in every Team that has Cursor [Privacy Mode](https://cursor.com/docs/enterprise/privacy-and-data-governance.md) enabled *and* for every Enterprise customer, regardless of Cursor Privacy Mode settings.

Fable 5 is on by default for every individual customer or Team account for which Cursor Privacy Mode is disabled.

For customers on the Enterprise plan or with Cursor Privacy Mode enabled, it requires explicit opt-in and the model won't be available until an admin explicitly enables it. Here's what to know before enabling it:

- **Data retention.** When Fable 5 is used, regardless of your Cursor [Privacy Mode](https://cursor.com/docs/enterprise/privacy-and-data-governance.md) settings, Anthropic stores agent input and output data to support automated and human harm-prevention processes. This data is not used to train or improve Anthropic's models or products.
- **Opt-in is team-wide.** Enabling Fable 5 requires opting in to Anthropic's data retention terms, and this applies to your entire team. Enterprise admins can restrict which user groups are able to use the model with [model access control](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control).

#### Automatic fallback to Opus

Fable 5 runs with tight security guardrails. When a request trips one of those guardrails, Cursor routes it to Claude Opus automatically so your work continues without an error. You don't need to retry or switch models yourself.

#### Tools

Fable 5 has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

#### Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. Fable 5 draws from the **API** pool, which charges at the rates below. All prices are per million tokens.

Fable 5 costs about twice as much as Claude Opus 4.8, at $10 per million input tokens and $50 per million output tokens.

Fable 5 supports a thinking variant for deeper reasoning. We recommend the high thinking variant for the strongest results.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Gemini 3.1 Pro

*Gemini 3.1 Pro is Google's latest model. It processes images alongside code, making it strong for UI/UX work from design mockups. It supports context windows up to 1M tokens.*

**Source:** https://cursor.com/docs/models/gemini-3-1-pro

Gemini 3.1 Pro is Google's latest model. It processes images alongside code, making it strong for UI/UX work from design mockups. It supports context windows up to 1M tokens.

#### Strengths

- Processes images alongside code. Strong for UI/UX coding from design mockups, frontend development, and visual code understanding.
- Up to 1M tokens of context for whole-codebase analysis.
- Strong capabilities at $2/1M input tokens.

#### Tools

Gemini 3.1 Pro has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

#### Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. Gemini 3.1 Pro draws from the **API** pool, which charges at the rates below. Individual plans include at least $20 of API usage each month (more on higher tiers). All prices are per million tokens.

When input exceeds 200k tokens (long context), input and output pricing increases. See the pricing table above for the long context rates.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Gemini 3.5 Flash

*Gemini 3.5 Flash is Google's newest speed-tier model. At $1.50 per million input tokens and $9.00 per million output tokens, it sits between Gemini 3 Flash and Gemini 3.1 Pro on price while bringing reasoning improvements over earlier Flash models. Use it for high-throughput coding tasks that need stronger reasoning than Gemini 3 Flash, but at a lower cost than Pro models.*

**Source:** https://cursor.com/docs/models/gemini-3-5-flash

Gemini 3.5 Flash is Google's newest speed-tier model. At $1.50 per million input tokens and $9.00 per million output tokens, it sits between Gemini 3 Flash and Gemini 3.1 Pro on price while bringing reasoning improvements over earlier Flash models. Use it for high-throughput coding tasks that need stronger reasoning than Gemini 3 Flash, but at a lower cost than Pro models.

#### Strengths

- Reasoning-capable Flash model. Better at multi-step coding tasks than Gemini 3 Flash while staying fast.
- 90% discount on cached input tokens ($0.15/1M). Strong for repeated context like large codebases.
- 1M token context window. Fits substantial portions of a repository in a single request.

#### Tools

Gemini 3.5 Flash has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

#### Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. Gemini 3.5 Flash draws from the **API** pool, which charges at the rates below. Individual plans include at least $20 of API usage each month (more on higher tiers). All prices are per million tokens.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### GPT 5.6 Sol

*GPT-5.6 Sol is OpenAI's flagship GPT-5.6 model in Cursor. It is the strongest of the Sol, Terra, and Luna family: persistent on long-running agent work, fast enough for interactive sessions, and notably concise in how it communicates.*

**Source:** https://cursor.com/docs/models/gpt-5-6-sol

GPT-5.6 Sol is OpenAI's flagship GPT-5.6 model in Cursor. It is the strongest of the Sol, Terra, and Luna family: persistent on long-running agent work, fast enough for interactive sessions, and notably concise in how it communicates.

#### Strengths

- Highest intelligence in the GPT-5.6 family for challenging coding and reasoning tasks.
- Strong persistence on long-running work; it keeps going through multi-hour agent sessions instead of stopping early.
- Clean, direct communication with less comment and final-message slop than many Claude models.
- Concise and easy to skim; strong as a rubber-duck partner for planning and debugging.
- Competitive speed relative to similarly intelligent models.

#### Limitations

- Higher per-token pricing than Terra and Luna.
- Can over-use subagents on mid-sized tasks.
- Sometimes waits for an explicit "do it" after agreeing with feedback, instead of executing immediately.
- Instruction-following can lag the strongest Claude models on some agent behavior evals.

#### Tools

GPT-5.6 Sol has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

#### Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. GPT-5.6 Sol draws from the **API** pool, which charges at the rates below. Individual plans include at least $20 of API usage each month (more on higher tiers). All prices are per million tokens.

A **Fast mode** tier (`gpt-5.6-sol-fast`) is available for priority processing at 2x the standard rates.

When input exceeds 272k tokens (long context), input pricing doubles and output pricing is 1.5x the standard rate.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### GPT 5.6 Terra

*GPT-5.6 Terra is the mid-tier model in OpenAI's GPT-5.6 family. It sits between Sol and Luna on intelligence and price, making it a strong pick for everyday agentic coding when you want more capability than Luna without Sol's cost.*

**Source:** https://cursor.com/docs/models/gpt-5-6-terra

GPT-5.6 Terra is the mid-tier model in OpenAI's GPT-5.6 family. It sits between Sol and Luna on intelligence and price, making it a strong pick for everyday agentic coding when you want more capability than Luna without Sol's cost.

#### Strengths

- Solid multi-step coding and tool use at roughly half Sol's per-token price.
- Faster and cheaper than Sol for routine agent workflows.
- Same GPT-5.6 family behavior: reasoning, tool calling, and agent loops.

#### Limitations

- Not the peak of the GPT-5.6 family. For the hardest long-running tasks, [GPT-5.6 Sol](https://cursor.com/docs/models/gpt-5-6-sol.md) is the stronger pick.
- Less capacity for open-ended reasoning chains than Sol.

#### Tools

GPT-5.6 Terra has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

#### Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. GPT-5.6 Terra draws from the **API** pool, which charges at the rates below. Individual plans include at least $20 of API usage each month (more on higher tiers). All prices are per million tokens.

A **Fast mode** tier (`gpt-5.6-terra-fast`) is available for priority processing at 2x the standard rates.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### GPT 5.6 Luna

*GPT-5.6 Luna is the smallest and lowest-cost model in OpenAI's GPT-5.6 family. Use it for high-volume, latency-sensitive, or cost-sensitive agent work where Sol or Terra would be more than you need.*

**Source:** https://cursor.com/docs/models/gpt-5-6-luna

GPT-5.6 Luna is the smallest and lowest-cost model in OpenAI's GPT-5.6 family. Use it for high-volume, latency-sensitive, or cost-sensitive agent work where Sol or Terra would be more than you need.

#### Strengths

- Lowest GPT-5.6 pricing; good for prototyping, subagents, and high-volume loops.
- Fast responses relative to larger GPT-5.6 variants.
- Same family tool-calling and agent support as Sol and Terra.

#### Limitations

- Not a frontier model. For harder problems where peak intelligence matters, [GPT-5.6 Sol](https://cursor.com/docs/models/gpt-5-6-sol.md) or [GPT-5.6 Terra](https://cursor.com/docs/models/gpt-5-6-terra.md) is the better pick.
- Smaller capacity for long, open-ended reasoning chains.

#### Tools

GPT-5.6 Luna has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

#### Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. GPT-5.6 Luna draws from the **API** pool, which charges at the rates below. Individual plans include at least $20 of API usage each month (more on higher tiers). All prices are per million tokens.

A **Fast mode** tier (`gpt-5.6-luna-fast`) is available for priority processing at 2x the standard rates.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Grok 4.5

*Grok 4.5 is a joint model from Cursor and SpaceXAI for long-running tasks across software engineering and knowledge work. It combines the Grok base with continued training on trillions of tokens of Cursor data and reinforcement learning on difficult, realistic problems.*

**Source:** https://cursor.com/docs/models/grok-4-5

Grok 4.5 is a joint model from Cursor and SpaceXAI for long-running tasks across software engineering and knowledge work. It combines the Grok base with continued training on trillions of tokens of Cursor data and reinforcement learning on difficult, realistic problems.

#### Strengths

- Handles long-running tasks that require using tools, checking results, recovering from mistakes, and adjusting its approach.
- Applies broad knowledge to software engineering, data science, finance, research, legal work, and other computer-based tasks.
- Solves multistep tasks in under half the steps of comparable frontier models.

#### Tools

Grok 4.5 has access to all agent tools when used with Cursor, including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

#### Pricing

Grok 4.5 is part of the [First-party models pool](https://cursor.com/docs/models-and-pricing.md#first-party-models-pool) on individual and team plans. This pool also includes Auto and Composer 2.5.

Included usage is doubled through July 21, 2026. Standard on-demand usage is priced at $2/M input tokens and $6/M output tokens. The Fast variant is priced at $4/M input tokens and $18/M output tokens. All prices are per million tokens.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Cursor Composer 2.5

*Composer 2.5 is Cursor's own agentic model. It builds on [Composer 2](https://cursor.com/blog/composer-2) with stronger intelligence on long agentic tasks, better effort calibration, tool selection, intent understanding, and reliability.*

**Source:** https://cursor.com/docs/models/cursor-composer-2-5

Composer 2.5 is Cursor's own agentic model. It builds on [Composer 2](https://cursor.com/blog/composer-2) with stronger intelligence on long agentic tasks, better effort calibration, tool selection, intent understanding, and reliability.

#### Strengths

- Strong on long-horizon tasks via [reinforcement learning](https://cursor.com/blog/real-time-rl-for-composer) on [long-horizon coding tasks](https://cursor.com/blog/self-driving-codebases).
- Default fast variant for interactive sessions; standard tier further optimized for cost per token.
- Tuned for tool use, file edits, and terminal operations inside Cursor.

#### Tools

Composer 2.5 has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

#### Pricing

A **faster variant** with the same intelligence is also available at $3/M input and $15/M output tokens. Fast is the default in the product and is priced lower than other fast models at similar speeds.

On individual and team plans, Composer 2.5 draws from the **First-party models pool** with Auto and Grok 4.5. On-demand usage is charged at the rates below. All prices are per million tokens.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

---

## Agent

### Cursor Agent

*Agent is Cursor's assistant that can complete complex coding tasks independently, run terminal commands, and edit code. Access in sidepane with Cmd+I.*

**Source:** https://cursor.com/docs/agent/overview

Agent is Cursor's assistant that can complete complex coding tasks independently, run terminal commands, and edit code. Access in sidepane with Cmd+I.

Learn more about [how agents work](https://cursor.com/learn/agents.md) and help you build faster.

#### How Agent works

An agent is built on three components:

1. **Instructions**: The system prompt and [rules](https://cursor.com/docs/rules.md) that guide agent behavior
2. **Tools**: File editing, codebase search, terminal execution, and more
3. **Model**: The agent model you pick for the task

Cursor's agent orchestrates these components for each model we support, tuning instructions and tools specifically for every frontier model. As new models are released, you can focus on building software while Cursor handles the model-specific optimizations.

#### Tools

Tools are the building blocks of Agent. They are used to search your codebase and the web to find relevant information, make edits to your files, run terminal commands, and more.

To understand how tool calling works under the hood, see our [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

There is no limit on the number of tool calls Agent can make during a task.

##### Search files and folders

Search for files by name, read directory structures, and find exact keywords or patterns within files.

##### Web

Generate search queries and perform web searches.

##### Fetch Rules

Retrieve specific [rules](https://cursor.com/docs/rules.md) based on type and description.

##### Read files

Intelligently read the content of a file. Also supports image files (.png, .jpg, .gif, .webp, .svg) and includes them in the conversation context for analysis by vision-capable models.

##### Edit files

Suggest edits to files and apply them automatically.

##### Run shell commands

Execute terminal commands and monitor output. By default, Cursor uses the first terminal profile available.

To set your preferred terminal profile:

1. Open Command Palette (`Cmd/Ctrl+Shift+P`)
2. Search for "Terminal: Select Default Profile"
3. Choose your desired profile

##### Browser

Control a browser to take screenshots, test applications, and verify visual changes. Agent can navigate pages, interact with elements, and capture the current state for analysis. See the [Browser documentation](https://cursor.com/docs/agent/tools/browser.md) for details.

##### Image generation

Generate images from text descriptions or reference images. Useful for creating UI mockups, product assets, and visualizing architecture diagrams. Images are saved to your project's `assets/` folder by default and shown inline in chat.

##### Ask questions

Ask clarifying questions during a task. While waiting for your response, the agent continues reading files, making edits, or running commands. Your answer is incorporated as soon as it arrives.

#### Checkpoints

Checkpoints save snapshots of your codebase during an Agent session. Agent automatically creates them before making significant changes, capturing the state of all modified files.

If Agent takes a wrong turn, click any checkpoint in the chat timeline to preview your files at that point, then restore to revert all files to that state. You can also restore from the `Restore Checkpoint` button on previous requests or the + button when hovering over a message.

Checkpoints are useful for exploratory work, complex refactoring, and iterative development where you want safe rollback points.

Checkpoints are stored locally and separate from Git. Only use them for undoing Agent changes; use Git for permanent version control.

#### Queued messages

Queue follow-up messages while Agent is working on the current task. Your instructions wait in line and execute automatically when ready.

[Media](https://cursor.com/docs-static/images/agent/planning/agent-queue.mp4)

##### Using the queue

1. While Agent is working, type your next instruction
2. Press Enter to add it to the queue
3. Messages appear in order below the active task
4. Drag to reorder queued messages as needed
5. Agent processes them sequentially after finishing

##### Keyboard shortcuts

While Agent is working:

- Press Enter to queue your message (it waits until Agent finishes the current task)
- Press Cmd+Enter to send immediately, bypassing the queue

##### Immediate messaging

When you use Cmd+Enter to send immediately, your message is appended to the most recent user message in the chat and processed right away without waiting in the queue.

- Your message attaches to tool results and sends immediately
- This creates a more responsive experience for urgent follow-ups
- Use this when you need to interrupt or redirect Agent's current work


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Agents Window

*The Agents Window is Cursor's agent-first interface. It provides a unified workspace to build with agents across repos and environments, including local, cloud, remote SSH, and more. It combines the power of parallel agents with the depth and control of a development environment.*

**Source:** https://cursor.com/docs/agent/agents-window

The Agents Window is Cursor's agent-first interface. It provides a unified workspace to build with agents across repos and environments, including local, cloud, remote SSH, and more. It combines the power of parallel agents with the depth and control of a development environment.

You can switch back to the editor anytime, or have both open simultaneously.

#### Open the Agents Window

If you're in the editor, type Cmd+Shift+P → Open Agents Window to open the Agents Window.

![Command Palette showing the Open Agents Window command](https://cursor.com/docs-static/images/agent/open-agents-window-final.png)

#### Switch Back to the IDE

To return to the classic Cursor IDE, type Cmd+Shift+P → Open IDE. This opens the current workspace in the editor.

![Actions menu showing the Open IDE command](https://cursor.com/docs-static/images/agent/open-editor-window-final.png)

If you want to view or edit files without leaving the Agents Window, you can type Cmd+P to search files, or Cmd+Shift+F to search all files.

![Agents Window showing file search and file viewing](https://cursor.com/docs-static/images/agent/file-agents-window-final.png)

#### Features Available Only in the Agents Window

The following features are available in the Agents Window:

- **Multi-workspace:** work with agents across all your projects from one place.
- **New diffs view:** review and commit changes, and manage PRs without leaving Cursor.
- **Parallel agents:** run many parallel agents in the cloud (and work with them from your phone, web, Slack, GitHub, and Linear).
- **Easier handoff between local and cloud:** quickly move an agent from cloud to local to iterate quickly, and move it back to the cloud so it keeps working on its own.
- **Cloud subagents:** hand off a task to a [cloud subagent](https://cursor.com/docs/subagents.md#cloud-subagents) with `/in-cloud`, or `/babysit` a PR, so long-running work runs on its own VM and branch while you keep working locally.
- **Worktrees:** [run agents in isolated Git checkouts](https://cursor.com/docs/configuration/worktrees.md) so each task has its own files and changes.

#### Choosing Between Agents Window and Editor

The Agents Window works well when you want to run and manage many agents in parallel. If you are using agents to write most of your code, the Agents Window helps pull you up to a higher level of abstraction.

The editor works well when you want the classic IDE with VS Code extensions and flexible screen splitting to see many files at once.

You can move between the two interfaces, and we will continue to support and improve both experiences.

#### Enterprise access

Agents Window is generally available with Cursor 3, released on April 2, 2026. For the two weeks following launch, Enterprise Admins can control rollout within their organizations by giving access to their entire team or to specific users via Team settings. After the rollout period, all users will have access by default.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Agent Review

*Agent Review runs a dedicated code review on your local changes from inside Cursor.*

**Source:** https://cursor.com/docs/agent/agent-review

Agent Review runs a dedicated code review on your local changes from inside Cursor.

#### Setup

To configure Agent Review:

1. Open **Cursor Settings**
2. Go to **Agents**
3. Find **Agent Review** and configure your preferences

Starting in Cursor 3.11, this setting moves to **Git & PRs** > **Pull Requests**.

Agent Review also reads repository rules from `BUGBOT.md` files. To set up these rule files, see [BugBot docs](https://cursor.com/docs/bugbot.md).

You can set it to run automatically after every agent task, or leave it manual and trigger it yourself.

#### Running a review

There are three ways to start a review:

- **Automatic**: When enabled in settings, Agent Review runs after every commit is made.
- **Slash command**: Type `/agent-review` in the agent window input to trigger a review on demand.
- **Source Control tab**: Open the Source Control tab and run Agent Review to compare all local changes against your main branch. This catches issues across your full set of changes, not only the latest edit.

[Media](https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/changelog/changelog-2-1-1.mp4)

#### Review depth

Agent Review supports two depth levels. Choose based on the thoroughness of review you need.

| Depth     | Speed | Cost | Best for                                                   |
| :-------- | :---- | :--- | :--------------------------------------------------------- |
| **Quick** | Fast  | Low  | Small diffs, formatting changes, or a fast sanity check    |
| **Deep**  | Slow  | High | Complex logic, security-sensitive code, or large refactors |


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Plan Mode

*Plan Mode creates detailed implementation plans before writing any code. Agent researches your codebase, asks clarifying questions, and generates a reviewable plan you can edit before building.*

**Source:** https://cursor.com/docs/agent/plan-mode

Plan Mode creates detailed implementation plans before writing any code. Agent researches your codebase, asks clarifying questions, and generates a reviewable plan you can edit before building.

Press Shift+Tab from the chat input to rotate to Plan Mode. Cursor also suggests it automatically when you type keywords that indicate complex tasks.

#### How it works

1. Agent asks clarifying questions to understand your requirements
2. Researches your codebase to gather relevant context
3. Creates a comprehensive implementation plan
4. You review and edit the plan through chat or markdown files
5. Click to build the plan when ready

Plans are saved by default in your home directory. Click "Save to workspace" to move it to your workspace for future reference, team sharing, and documentation.

#### When to use Plan Mode

Plan Mode works best for:

- Complex features with multiple valid approaches
- Tasks that touch many files or systems
- Unclear requirements where you need to explore before understanding scope
- Architectural decisions where you want to review the approach first

For quick changes or tasks you've done many times before, jumping straight to Agent mode is fine.

#### Starting over from a plan

Sometimes Agent builds something that doesn't match what you wanted. Instead of trying to fix it through follow-up prompts, go back to the plan.

Revert the changes, refine the plan to be more specific about what you need, and run it again. This is often faster than fixing an in-progress agent, and produces cleaner results.

For larger changes, spend extra time creating a precise, well-scoped plan. The hard part is often figuring out **what** change should be made. With the right instructions, delegate implementation to Agent.

#### Switching modes

- Use the mode picker dropdown in Agent
- Press Shift+Tab for quick switching


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Prompting agents

*Direct Agent with text prompts in the chat input. You can attach context, images, and voice, and switch models at any point.*

**Source:** https://cursor.com/docs/agent/prompting

Direct Agent with text prompts in the chat input. You can attach context, images, and voice, and switch models at any point.

#### @ mentions

Type `@` in the chat input to attach specific context to your prompt. Start typing after `@` and Cursor shows matching suggestions.

- **Files & Folders**: `@auth.ts` or `@src/components/` to include files or folders (type `/` after selecting a folder to navigate deeper)
- **Docs**: `@Docs` to search indexed documentation, including your own (add via `@Docs > Add new doc`)
- **Terminals**: `@Terminals` to include terminal output as context
- **Past Chats**: `@Past Chats` to reference context from a previous conversation
- **Git diffs**: `@Commit (Diff of Working State)` for uncommitted changes, or `@Branch (Diff with Main)` for your full branch diff
- **Browser**: `@Browser` to attach context from the built-in browser

Use @ mentions when you know which files are relevant. If you're not sure which files matter, skip it — Agent finds relevant files through its own search.

#### Image input

Attach images to your prompt to provide visual context for UI work, debugging, and design implementation.

- **Drag and drop** an image file into the chat input
- **Paste from clipboard** with Cmd+V, including screenshots

This is useful for implementing design mockups, debugging visual issues, and referencing error messages or stack traces without manual transcription.

#### Voice input

Click the microphone icon in the chat input to dictate your prompt instead of typing. Speak naturally, include technical details like file and function names, and review the transcription before sending.

#### Context usage

Every chat shares a fixed context window with the model. As you add files, run tools, and exchange messages, those tokens fill up. When the window gets close to full, Cursor compresses older parts of the conversation into a summary to leave more room for new conversation.

The context ring next to your prompt input shows how full the window is at a glance. Click the ring to open the breakdown tray, which shows the total tokens used split by category:

- **System prompt**: Cursor's built-in instructions for the model
- **Tools**: definitions of every tool available to the agent
- **Rules**: project and user rules included in the prompt
- **Skills**: skill descriptions injected into the system context
- **MCP**: instructions and catalog from connected MCP servers
- **Subagents**: documentation for subagent types the agent can launch
- **Summarized conversation**: compressed summaries of earlier turns
- **Conversation**: your messages, the agent's replies, and tool results

Hover a segment in the bar or a row in the list to highlight that category.

#### Changing models

Use the model picker dropdown at the top of the chat input to switch models, or press Cmd / to cycle through models. The change applies to the current conversation going forward. Set a default model in **Cursor Settings > Models**.

- **Faster models** work well for quick edits and routine tasks
- **More capable models** are better for complex reasoning and multi-file refactoring

You can switch models mid-conversation, for example when a faster model handled exploration but you need deeper reasoning for implementation. See [Models & Pricing](https://cursor.com/docs/models-and-pricing.md) for the full list.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Debug Mode

*Debug Mode helps you find root causes and fix tricky bugs that are hard to reproduce or understand. Instead of immediately writing code, the agent generates hypotheses, adds log statements, and uses runtime information to pinpoint the exact issue before making a targeted fix.*

**Source:** https://cursor.com/docs/agent/debug-mode

Debug Mode helps you find root causes and fix tricky bugs that are hard to reproduce or understand. Instead of immediately writing code, the agent generates hypotheses, adds log statements, and uses runtime information to pinpoint the exact issue before making a targeted fix.

#### When to use Debug Mode

Debug Mode works best for:

- **Bugs you can reproduce but can't figure out**: When you know something is wrong but the cause isn't obvious from reading the code
- **Race conditions and timing issues**: Problems that depend on execution order or async behavior
- **Performance problems and memory leaks**: Issues that require runtime profiling to understand
- **Regressions where something used to work**: When you need to trace what changed

When standard Agent interactions struggle with a bug, Debug Mode provides a different approach using runtime evidence rather than guessing at fixes.

#### How it works

1. **Explore and hypothesize**: The agent explores relevant files, builds context, and generates multiple hypotheses about potential root causes.

2. **Add instrumentation**: The agent adds log statements that send data to a local debug server running in a Cursor extension.

3. **Reproduce the bug**: Debug Mode asks you to reproduce the bug and provides specific steps. This keeps you in the loop and ensures the agent captures real runtime behavior.

4. **Analyze logs**: After reproduction, the agent reviews the collected logs to identify the actual root cause based on runtime evidence.

5. **Make targeted fix**: The agent makes a focused fix that directly addresses the root cause, often just a few lines of code.

6. **Verify and clean up**: You can re-run the reproduction steps to verify the fix. Once confirmed, the agent removes all instrumentation.

#### Tips for Debug Mode

- **Provide detailed context**: The more you describe the bug and how to reproduce it, the better the agent's instrumentation will be. Include error messages, stack traces, and specific steps.
- **Follow reproduction steps exactly**: Execute the steps the agent provides to ensure logs capture the actual issue.
- **Reproduce multiple times if needed**: Reproducing the bug multiple times may help the agent identify tricky problems like race conditions.
- **Be specific about expected vs. actual behavior**: Help the agent understand what should happen versus what is happening.

#### Switching modes

- Use the mode picker dropdown in Agent
- Press Shift+Tab for quick switching


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Design Mode

*Design Mode lets you direct agents with visual prompts. From the browser in the [Agents Window](https://cursor.com/docs/agent/agents-window.md), you can click an element, draw on the page, or describe a change by voice. Cursor captures the context it needs and edits the code while you move on to the next change.*

**Source:** https://cursor.com/docs/agent/design-mode

Design Mode lets you direct agents with visual prompts. From the browser in the [Agents Window](https://cursor.com/docs/agent/agents-window.md), you can click an element, draw on the page, or describe a change by voice. Cursor captures the context it needs and edits the code while you move on to the next change.

UI work tends to be spatial. Instead of describing a change in a sentence, your instruction can include the selected element, the code behind it, the surrounding layout, and the visual relationships on the page. This tightens the loop between noticing something and fixing it.

Click an element in the running app, prompt against that selected element, and let the agent edit the code.

#### Open Design Mode

Design Mode lives in the browser inside the Agents Window. Open the browser, then toggle Design Mode with Cmd + Shift + D. Toggle it off with the same shortcut to return to normal browsing.

#### Ways to direct the agent

Design Mode gives you several ways to convey intent.

##### Select an element

Click any element in the running product to target it. The agent gets the element and its code, so you can prompt against the exact thing you see without leaving the app.

##### Select multiple elements

Multi-select helps when the change depends on a relationship between elements. Reference two components and ask the agent to make one match the other, remove repeated content, or adjust a group together.

Select multiple elements and describe how they should change together.

##### Draw on the page

Drawing tells the agent which area of the page your instruction applies to. Circle a crowded section, box in a region, or mark part of an animated page. The annotation sits over a frozen frame of the viewport, so the agent sees the exact page state you were responding to.

##### Narrate by voice

You can narrate instructions with your voice instead of typing. The mic stays available while agents run, so you can queue the next change without waiting.

Use voice input and drawing together to describe a change.

#### Keyboard shortcuts

| Action               | Shortcut        |
| :------------------- | :-------------- |
| Toggle Design Mode   | Cmd + Shift + D |
| Select an area       | Shift + drag    |
| Add element to chat  | Cmd + L         |
| Add element to input | Option + click  |

#### What the agent sees

Picking an element adds two complementary signals to context:

- **Element identity**: the xpath, the component, attributes, computed styles, and props from the fiber tree. This helps the agent find the source and edit the right code.
- **A screenshot**: the layout, surrounding elements, and the exact page state. This gives the agent spatial context for the change.

#### Work in flow

When you refine an interface, one edit usually leads to the next. You adjust a component, notice the spacing around it, then see how another component should match.

Design Mode lets you send those edits away as you notice them. Point at one element, describe the change, move to another part of the page, and send another edit before the first one finishes. This makes it easy to multitask and manage several subagents at once. As agents finish, the app hot reloads and your changes appear in the running product.

This flow works best with a fast model that is strong at interface work. We recommend [Composer 2.5](https://cursor.com/blog/composer-2-5).

#### Related

- [Agents Window](https://cursor.com/docs/agent/agents-window.md)
- [Browser](https://cursor.com/docs/agent/tools/browser.md)


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Terminal

*Cursor runs shell commands directly in your terminal. Your [Run Mode](https://cursor.com/docs/agent/security/run-modes.md) controls when commands run, when Cursor asks, and when terminal commands enter the sandbox.*

**Source:** https://cursor.com/docs/agent/tools/terminal

Cursor runs shell commands directly in your terminal. Your [Run Mode](https://cursor.com/docs/agent/security/run-modes.md) controls when commands run, when Cursor asks, and when terminal commands enter the sandbox.

#### Sandbox

The sandbox runs terminal commands in a restricted environment that blocks unauthorized file access and network activity. For platform requirements, network modes, environment variables, and `sandbox.json` configuration, read [Run Modes > Sandboxing](https://cursor.com/docs/agent/security/run-modes.md#sandboxing).

#### Troubleshooting

Some shell themes (for example, Powerlevel9k/Powerlevel10k) can interfere with
the inline terminal output. If your command output looks truncated or
misformatted, disable the theme or switch to a simpler prompt when Cursor runs.

##### Disable heavy prompts for Cursor sessions

Use the `CURSOR_AGENT` environment variable in your shell config to detect when
Cursor is running and skip initializing fancy prompts/themes.

```zsh
# ~/.zshrc - disable Powerlevel10k when Cursor runs
if [[ -n "$CURSOR_AGENT" ]]; then
  # Skip theme initialization for better compatibility
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

```bash
# ~/.bashrc - fall back to a simple prompt in Cursor sessions
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \W \$ '
fi
```


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Browser

*Agent can control a web browser to test applications, visually edit layouts and styles, audit accessibility, convert designs into code, and more. With full access to console logs and network traffic, Agent can debug issues and automate comprehensive testing workflows.*

**Source:** https://cursor.com/docs/agent/tools/browser

Agent can control a web browser to test applications, visually edit layouts and styles, audit accessibility, convert designs into code, and more. With full access to console logs and network traffic, Agent can debug issues and automate comprehensive testing workflows.

For enterprise customers, browser controls are governed by MCP allowlist or denylist.

#### Native integration

Agent displays browser actions like screenshots and actions in the chat, as well as the browser window itself either in a separate window or an inline pane.

We've optimized the browser tools to be more efficient and reduce token usage, as well as:

- **Efficient log handling**: Browser logs are written to files that Agent can grep and selectively read. Instead of summarizing verbose output after every action, Agent reads only the relevant lines it needs. This preserves full context while minimizing token usage.
- **Visual feedback with images**: Screenshots are integrated directly with the file reading tool, so Agent actually sees the browser state as images rather than relying on text descriptions. This enables better understanding of visual layouts and UI elements.
- **Smart prompting**: Agent receives additional context about browser logs, including total line counts and preview snippets, helping it make informed decisions about what to inspect.
- **Development server awareness**: Agent is prompted to detect running development servers and use the correct ports instead of starting duplicate servers or guessing port numbers.

You can use Browser without installing or configuring any external tools.

#### Browser capabilities

Agent has access to the following browser tools:

##### Navigate

Visit URLs and browse web pages. Agent can navigate anywhere on the web by visiting URLs, following links, going back and forward in history, and refreshing pages.

##### Click

Interact with buttons, links, and form elements. Agent can identify and interact with page elements, performing click, double-click, right-click, and hover actions on any visible element.

##### Type

Enter text into input fields and forms. Agent can fill out forms, submit data, and interact with form fields, search boxes, and text areas.

##### Scroll

Navigate through long pages and content. Agent can scroll to reveal additional content, find specific elements, and explore lengthy documents.

##### Screenshot

Capture visual representations of web pages. Screenshots help Agent understand page layout, verify visual elements, and provide you with confirmation of browser actions.

##### Console Output

Read browser console messages, errors, and logs. Agent can monitor JavaScript errors, debugging output, and network warnings to troubleshoot issues and verify page behavior.

##### Network Traffic

Monitor HTTP requests and responses made by the page. Agent can track API calls, analyze request payloads, check response status codes, and diagnose network-related issues. This is currently only available in the Agent panel, coming soon to the layout.

#### Design sidebar

The browser includes a design sidebar for modifying your site directly in Cursor. Design and code simultaneously with real-time visual adjustments.

![Browser design sidebar showing layout controls, positioning, and CSS properties for a selected element.](https://cursor.com/docs-static/images/agent/browser-design-sidebar.png)

##### Visual editing capabilities

The sidebar provides powerful visual editing controls:

- **Position and layout**: Move and rearrange elements on the page. Change flex direction, alignment, and grid layouts.
- **Dimensions**: Adjust width, height, padding, and margins with precise pixel values.
- **Colors**: Update colors from your design system or add new gradients. Access color tokens through a visual picker.
- **Appearance**: Experiment with shadows, opacity, and border radius using visual sliders.
- **Theme testing**: Test your designs across light and dark themes instantly.

##### Applying changes

When your visual adjustments match your vision, click the apply button to trigger an agent that updates your codebase. The agent translates your visual changes into the appropriate code modifications.

You can also select multiple elements across your site and describe changes in text. Agents kick off in parallel, and your changes appear live on the page after hot-reload.

#### Session persistence

Browser state persists between Agent sessions based on your workspace. This means:

- **Cookies**: Authentication cookies and session data remain available across browser sessions
- **Local Storage**: Data stored in `localStorage` and `sessionStorage` persists
- **IndexedDB**: Database content is retained between sessions

The browser context is isolated per workspace, ensuring that different projects maintain separate storage and cookie states.

#### Use cases

##### Web development workflow

Browser integrates into web development workflows alongside tools like Figma and Linear. See the [Web Development cookbook](https://cursor.com/for/web-development.md) for a complete guide on using Browser with design systems, project management tools, and component libraries.

##### Accessibility improvements

Agent can audit and improve web accessibility to meet WCAG compliance standards.

@browser Check color contrast ratios, verify semantic HTML and ARIA labels, test keyboard navigation, and identify missing alt text

##### Automated testing

Agent can execute comprehensive test suites and capture screenshots for visual regression testing.

@browser Fill out forms with test data, click through workflows, test responsive designs, validate error messages, and monitor console for JavaScript errors

##### Design to code

Agent can convert designs into working code with responsive layouts.

@browser Analyze this design mockup, extract colors and typography, and generate pixel-perfect HTML and CSS code

##### Adjusting UI design from screenshots

Agent can refine existing interfaces by identifying visual discrepancies and updating component styles.

@browser Compare current UI against this design screenshot and adjust spacing, colors, and typography to match

#### Security

Browser runs as a secure web view and is controlled using an MCP server running as an extension. Multiple layers protect you from unauthorized access and malicious actions.
Cursor's Browser integrations have also been reviewed by multiple external security auditors.

##### Authentication and isolation

The browser implements several security measures:

- **Token authentication**: Agent layout generates a random authentication token before each browser session starts
- **Tab isolation**: Each browser tab receives a unique random ID to prevent cross-tab interference
- **Session-based security**: Tokens regenerate for each new browser session

##### Tool approval

Browser tools require your approval by default. Review each action before Agent executes it. This prevents unexpected navigation, data submission, or script execution.

You can configure approval settings in Agent Settings. Available modes:

| Mode                     | Description                                                                 |
| :----------------------- | :-------------------------------------------------------------------------- |
| **Manual approval**      | Review and approve each browser action individually (recommended)           |
| **Allow-listed actions** | Actions matching your allow list run automatically; others require approval |
| **Auto-run**             | All browser actions execute immediately without approval (use with caution) |

##### Allow and block lists

Browser tools integrate with Cursor's [security guardrails](https://cursor.com/docs/agent/security.md). Configure which browser actions run automatically:

- **Allow list**: Specify trusted actions that skip approval prompts
- **Block list**: Define actions that should always be blocked
- Access settings through: **Cursor Settings > Agents > Auto-Run**

The allow/block list system provides best-effort protection. AI behavior can be unpredictable due to prompt injection and other issues. Review auto-approved actions regularly.

Never use auto-run mode with untrusted code or unfamiliar websites. Agent could execute malicious scripts or submit sensitive data without your knowledge.

##### Browser context

The browser opens as a pane within Cursor, giving Agent full control through MCP tools.

#### Recommended models

We recommend using Sonnet 4.5, GPT-5, and Auto for the best performance.

#### Enterprise usage

For enterprise customers, browser functionality is managed through toggling availability under MCP controls. Admins have granular controls over each MCP server, as well as over browser access.

##### Enabling browser for enterprise

To enable browser capabilities for your enterprise team:

1. Navigate to your [Settings Dashboard](https://cursor.com/dashboard/settings)
2. Go to **MCP Configuration**
3. Toggle "browser features"

Once configured, users in your organization will have access to browser tools based on your MCP allowlist or denylist settings.

##### Origin allowlist

Enterprise administrators can configure an origin allowlist that restricts which sites the agent can automatically navigate to and where MCP tools can run. This provides granular control over browser access for security and compliance.

The Browser Origin Allowlist feature must be enabled for your organization before it appears in your dashboard. Contact your Cursor account team to request access.

###### Configuration

To configure the origin allowlist:

1. Navigate to your [Admin Dashboard](https://cursor.com/dashboard/settings)
2. Go to **MCP Configuration**
3. Ensure **Enable Browser Automation Features (v2.0+)** is enabled
4. Under **Browser Origin Allowlist (v2.1+)**, click **Add Origin**
5. Enter the origins you want to allow (e.g., `*`, `http://localhost:3000`, `https://internal.example.com`)

Leave the allowlist empty to allow all origins. Each origin should be added separately using the Add Origin button.

![MCP Configuration showing Browser Origin Allowlist settings with Add Origin button](https://cursor.com/docs-static/images/agent/browser-origin-allowlist.png)

###### Behavior

When an origin allowlist is configured:

- **Automatic navigation**: The agent can only use the `browser_navigate` tool to visit URLs matching origins in the allowlist
- **MCP tool execution**: MCP tools can only run on origins that are in the allowlist
- **Manual navigation**: Users can still manually navigate the browser to any URL, including origins outside the allowlist (useful for viewing documentation or inspecting external sites)
- **Tool restrictions**: Once the browser is on an origin not in the allowlist, browser tools (click, type, navigate) are blocked, even if the user navigated there manually

###### Edge cases

The origin allowlist provides best-effort protection. Be aware of these behaviors:

- **Link navigation**: If the agent clicks a link on an allowed domain that navigates to a non-allowed origin, the navigation will succeed
- **Redirects**: If the agent navigates to an allowed origin that subsequently redirects to a non-allowed origin, the redirect will be permitted
- **JavaScript navigation**: Client-side navigation (via `window.location` or similar) from an allowed origin to a non-allowed origin will succeed

The origin allowlist restricts automatic agent navigation but cannot prevent all navigation paths. Review your allowlist regularly and consider the security implications of allowing access to domains that may redirect or link to external sites.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Semantic & agentic search

*Agent combines multiple search tools to find relevant code across your codebase. You describe what you're looking for in natural language, and Agent picks the right strategy.*

**Source:** https://cursor.com/docs/agent/tools/search

Agent combines multiple search tools to find relevant code across your codebase. You describe what you're looking for in natural language, and Agent picks the right strategy.

#### Instant Grep

The fastest way to find code is an exact match: a function name, variable, error string, or regex pattern. Agent uses grep automatically when you reference specific symbols.

Cursor ships with [Instant Grep](https://cursor.com/changelog/2-1#instant-grep-beta), a custom search engine that outperforms `ripgrep` on large codebases. It runs automatically; no configuration needed.

Instant Grep supports full regex and word-boundary matching, so Agent can construct patterns like `import.*PaymentService` or `PaymentFailedError` to trace references across files.

#### Semantic search

When you don't know the exact name, semantic search finds code by meaning. Ask "where do we handle authentication?" and Agent can locate `middleware/session.ts` even though the word "authentication" never appears in the file.

This works because Cursor [indexes your codebase](https://cursor.com/blog/secure-codebase-indexing) into searchable vectors with a custom embedding model. Research on Cursor's [semantic search](https://cursor.com/blog/semsearch) shows that combining it with grep produces 12.5% higher accuracy answering codebase questions compared to grep alone. The improvement is largest on codebases with 1,000+ files.

##### How indexing works

Cursor breaks your code into meaningful chunks (functions, classes, logical blocks), converts each chunk into a vector embedding that captures its semantic meaning, and stores the results in a vector database. When you search, your query is converted into a vector using the same model and matched against the stored embeddings.

Indexing begins automatically when you open a workspace. Semantic search becomes available at 80% completion. The index stays current through automatic sync every 5 minutes, processing only changed files.

| Change         | Action                                   |
| :------------- | :--------------------------------------- |
| New files      | Added to the index automatically         |
| Modified files | Old embeddings removed, new ones created |
| Deleted files  | Removed from the index                   |

##### Configuration

Check indexing status or trigger a re-index from **Cursor Settings > Indexing**.

Cursor indexes all files except those in [ignore files](https://cursor.com/docs/reference/ignore-file.md) (`.gitignore`, `.cursorignore`). Ignoring large generated or content files improves search accuracy.

To view indexed file paths: **Cursor Settings > Indexing & Docs > View included files**.

##### Privacy and security

File paths are encrypted before being sent to Cursor's servers. Code content is never stored in plaintext; it is held in memory during indexing, then discarded. Embeddings are created without storing filenames or source code. When Agent searches, Cursor retrieves the embeddings and decrypts the chunks on the client side.

#### How Agent combines search tools

Agent picks the right tool based on your prompt:

| Prompt style              | Tools used                                         | Example                                                 |
| :------------------------ | :------------------------------------------------- | :------------------------------------------------------ |
| Specific symbol or string | Grep                                               | "Find all files that import `PaymentService`"           |
| Concept or behavior       | Semantic search, then grep to fill in details      | "How does our app handle failed payments?"              |
| Complex exploration       | Multiple searches, file reads, reference following | "Map the data flow from checkout to confirmation email" |

You don't choose the tool. Describe what you need and Agent decides. For complex tasks, it chains searches together: semantic search to find entry points, grep to trace references, and file reads to build full context.

#### Explore subagent

Agent can spawn an [Explore subagent](https://cursor.com/docs/subagents.md) that runs in its own context window with a faster model. It executes many parallel searches without bloating the main conversation, returning only the relevant findings.

Agent uses the Explore subagent automatically when it decides a task benefits from broad search. You can also request it directly: "use a subagent to find all the places we validate user input."

This is useful for context management. Searching through many files generates a lot of context. The subagent keeps the main conversation focused by summarizing results instead of dumping raw file contents.

#### Tips for better search results

- **Start specific, then go broad.** If you know the function name, say it. If you're exploring unfamiliar code, describe the behavior.
- **Explore before changing.** Ask Agent to show existing patterns before asking it to add new ones. This prevents it from creating duplicates or breaking conventions.
- **Reference concrete code.** Prompts like "find all callers of `processOrder`" give Agent an exact target. Prompts like "find the order code" force Agent to guess what you mean.

#### FAQ

##### Is my source code stored on Cursor servers?

No. Cursor creates embeddings without storing filenames or source code. Filenames are obfuscated and code chunks are encrypted. When Agent searches, Cursor retrieves the embeddings and decrypts the chunks on the client side.

##### How long are indexed codebases retained?

Indexed codebases are deleted after 6 weeks of inactivity. Reopening the project triggers re-indexing.

##### Can I customize path encryption?

Create a `.cursor/keys` file in your workspace root:

```json
{
  "path_decryption_key": "your-custom-key-here"
}
```

##### How does team sharing work?

Indexes can be shared across team members for faster indexing of similar codebases. Cursor respects file access permissions and only shares accessible content.

##### Does Cursor support multi-root workspaces?

Yes. Cursor supports [multi-root workspaces](https://code.visualstudio.com/docs/editor/workspaces#_multiroot-workspaces). All codebases get indexed automatically, and each codebase's context is available to Agent. Some features that rely on a single git root, like worktrees, are disabled for multi-root workspaces. Cloud Agents do not support multi-root workspaces.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Canvases

*Canvases let Cursor create interactive artifacts that render next to the chat. Instead of scrolling through a long markdown table or code block, you get a standalone view, laid out with sections, stats, and tables, that you can reopen, edit, and iterate on.*

**Source:** https://cursor.com/docs/agent/tools/canvas

Canvases let Cursor create interactive artifacts that render next to the chat. Instead of scrolling through a long markdown table or code block, you get a standalone view, laid out with sections, stats, and tables, that you can reopen, edit, and iterate on.

Ask agents for a dashboard, analysis, audit, or report, and Cursor opens the result in a canvas when that is a better fit.

#### How it works

1. Cursor decides that your task benefits from a visual or interactive view, or you ask for one directly.
2. Cursor builds the canvas and inserts a reference to it in your chat.
3. You review the rendered view, switch to the source to tweak it, or ask Cursor to change it.
4. Cursor saves the canvas so you can reopen and rerun it later with fresh data.

Each canvas appears in your workspace's canvas list, so you can jump back to past ones without rerunning them.

#### Opening a canvas

- **From Cursor**: when Cursor creates a canvas, a card appears at the end of the response. Click it to open.
- **Command Palette**: run **Open Canvas** from the palette, listed under View.
- **Agents Window**: open a canvas tab directly from the new tab menu in the [Agents Window](https://cursor.com/docs/agent/agents-window.md).

#### Sharing canvases

Shared canvases turn an interactive artifact into something your whole team can open, not just you. When you share a canvas, Cursor uploads a live snapshot of the view and gives you a link teammates can open in the browser — same layout, charts, and tables, without rerunning the agent or digging through chat history. Use **Publish** from the canvas toolbar to publish or refresh a share; browse everything your team has published from **Shared Canvases** on the [dashboard](https://cursor.com/dashboard).

Shared canvases are available on paid plans (Pro, Teams, and Enterprise). Free accounts cannot create shares. Because each share is team-visible, you need to be on a team — Pro users on a team can share too. Sharing also requires a privacy mode that allows data storage (Legacy Privacy Mode blocks it).

Team admins can turn shared canvases off for the organization from [team settings](https://cursor.com/dashboard/settings#shared-canvases) under **Shared Canvases**.

#### Iterating on a canvas

Canvases are designed to be easy to refine.

- If the layout isn't right, tell Cursor what to change instead of editing by hand.
- If the numbers look stale or off, ask Cursor to rerun the underlying query or show its work.
- For larger reworks, revert and prompt Cursor again with more details. This is usually faster than nudging through small follow-ups.
- For small tweaks, you can also manually edit the source code.

#### Packaging in skills

Common canvas workflows can be packaged as [skills](https://cursor.com/docs/skills.md) so Cursor produces a consistent layout every time you ask.

A canvas skill typically includes:

- **A trigger description** so Cursor knows when to reach for it, like "quarterly revenue report" or "dependency audit".
- **Layout instructions** that define the sections, stats, and tables the canvas should contain.
- **Data sources and queries** Cursor should run to populate the view, such as a SQL query, API call, or shell command.
- **Formatting rules** like units, date ranges, or sort order.

Once the skill is in place, a short prompt is enough to regenerate the canvas with fresh data, and every teammate using the skill gets the same output shape.

#### Related

- [Agents Window](https://cursor.com/docs/agent/agents-window.md)
- [Skills](https://cursor.com/docs/skills.md)
- [Prompting](https://cursor.com/docs/agent/prompting.md)


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Worktrees

*The UI-native worktrees feature described on this page is only available in the Agents Window. In the IDE, use the Worktree Skills commands below.*

**Source:** https://cursor.com/docs/configuration/worktrees

The UI-native worktrees feature described on this page is only available in the Agents Window. In the IDE, use the Worktree Skills commands below.

[Media](https://cursor.com/docs-static/images/configuration/worktrees/cursor-worktrees-2.mp4)

Worktrees let Agent work in isolated Git checkouts. Each task gets its own files, dependencies, and changes while your main checkout stays untouched.

Use worktrees when you want to start several agents on the same repo without conflicts.

#### Create a worktree in the Agents Window

When you start or move an agent into a worktree from the Agents Window, Cursor creates a separate checkout for that agent. The agent continues the task inside the worktree, so changes stay isolated from your main checkout.

After the agent finishes, review the result in the Agents Window. You can keep working in the worktree, create a commit or PR from that checkout, or bring the result back into your main workspace.

#### How does worktree setup work?

You can customize worktree setup with `.cursor/worktrees.json`. Cursor checks this file when it creates a worktree in the Agents Window, the IDE, or the [Cursor CLI](https://cursor.com/docs/cli/using.md#cli-worktrees).

Cursor looks for `.cursor/worktrees.json` in this order:

1. In the worktree path
2. In the root path of your project

##### Configuration options

The `worktrees.json` file supports three setup keys:

- **`setup-worktree-unix`**: Commands or a script path for macOS and Linux. This takes precedence over `setup-worktree` on Unix systems.
- **`setup-worktree-windows`**: Commands or a script path for Windows. This takes precedence over `setup-worktree` on Windows.
- **`setup-worktree`**: Generic fallback for all operating systems.

Each key accepts either:

- **An array of shell commands**: executed sequentially in the worktree
- **A string filepath**: path to a script file relative to `.cursor/worktrees.json`

#### Example setup configurations

##### Using command arrays

###### Node.js project

```json
{
  "setup-worktree": [
    "npm ci",
    "cp $ROOT_WORKTREE_PATH/.env .env"
  ]
}
```

We do not recommend symlinking dependencies into the worktree. This can cause issues in the main worktree. Use a fast package manager such as `bun`, `pnpm`, or `uv` instead.

###### Python project with virtual environment

```json
{
  "setup-worktree": [
    "python -m venv venv",
    "source venv/bin/activate && pip install -r requirements.txt",
    "cp $ROOT_WORKTREE_PATH/.env .env"
  ]
}
```

###### Project with database migrations

```json
{
  "setup-worktree": [
    "npm ci",
    "cp $ROOT_WORKTREE_PATH/.env .env",
    "npm run db:migrate"
  ]
}
```

###### Build and link dependencies

```json
{
  "setup-worktree": [
    "pnpm install",
    "pnpm run build",
    "cp $ROOT_WORKTREE_PATH/.env.local .env.local"
  ]
}
```

##### Using script files

For more complex setups, reference script files instead of inline commands:

```json
{
  "setup-worktree-unix": "setup-worktree-unix.sh",
  "setup-worktree-windows": "setup-worktree-windows.ps1",
  "setup-worktree": [
    "echo 'Using generic fallback. For better support, define OS-specific scripts.'"
  ]
}
```

Place your scripts in the `.cursor/` directory next to `worktrees.json`.

**setup-worktree-unix.sh** (Unix and macOS):

```bash
#!/bin/bash
set -e

# Install dependencies
npm ci

# Copy environment file
cp "$ROOT_WORKTREE_PATH/.env" .env

# Run database migrations
npm run db:migrate

echo "Worktree setup complete!"
```

**setup-worktree-windows.ps1** (Windows):

```powershell
$ErrorActionPreference = 'Stop'

# Install dependencies
npm ci

# Copy environment file
Copy-Item "$env:ROOT_WORKTREE_PATH\.env" .env

# Run database migrations
npm run db:migrate

Write-Host "Worktree setup complete!"
```

##### OS-specific configurations

You can provide different setup commands for different operating systems:

```json
{
  "setup-worktree-unix": [
    "npm ci",
    "cp $ROOT_WORKTREE_PATH/.env .env",
    "chmod +x scripts/*.sh"
  ],
  "setup-worktree-windows": [
    "npm ci",
    "copy %ROOT_WORKTREE_PATH%\\.env .env"
  ]
}
```

##### Debugging

If you want to debug worktree setup, open the Output panel in the editor and select `Worktrees Setup`.

#### How does Cursor discover existing worktrees?

Cursor 3.5 keeps a modified time checkpoint for the machine worktree root and for each workspace subdirectory. On startup, Cursor re-scans the filesystem unless those timestamps prove nothing changed since the last discovery. This avoids skipping new worktrees that were created while Cursor was closed and eliminates the older `worktree.discoveryComplete` flag.

#### Worktrees cleanup

The cleanup behavior in this section reflects Cursor 3.5 and later.

Cursor can clean up older worktrees automatically to limit disk usage. Cleanup runs on an interval and keeps the newest worktrees up to the configured machine-wide maximum count across every workspace on the device.

```json
{
  "cursor.worktreeCleanupIntervalHours": 6,
  "cursor.worktreeMaxCount": 25
}
```

Use these machine-scoped settings to control cleanup:

- **`cursor.worktreeCleanupIntervalHours`**: how often Cursor checks for old worktrees. Cursor 3.5 catches up after restarts by scheduling a delayed cleanup if the last successful run is older than this interval.
- **`cursor.worktreeMaxCount`**: the maximum number of worktrees Cursor keeps before cleaning up older ones. The default cap is 25 worktrees per machine, and all workspaces contribute toward the same limit.

Cursor re-discovers the worktree root on every cleanup pass, so worktrees created outside the manager (for example, worktrees created by `/worktree` skills or `git worktree add`) are eligible for deletion. When creating a worktree would exceed the cap, Cursor debounces bursts of events and starts an immediate cleanup instead of waiting for the next interval.

#### Worktree Skills in IDE

In the IDE, you can use the `/worktree` and `/best-of-n` commands to run tasks in isolated worktrees.

##### Use `/worktree` for one isolated run

Start a task with `/worktree` when you want Cursor to do the rest of that chat in a separate checkout.

- Keep experimental edits away from your main checkout
- Run installs, builds, and tests without disturbing your current branch
- Work on risky refactors with a simple cleanup path

```text
/worktree fix the failing auth tests and update the login copy
```

In many cases, you can commit and push directly from the worktree. Ask the agent:

```text
Commit and push these changes, then open a PR
```

If you want to bring the changes into your main checkout to test them, use `/apply-worktree`. When you are done with the isolated checkout, use `/delete-worktree`.

If you want to see all worktrees in your repository, run:

```bash
git worktree list
```

##### Use `/best-of-n` to compare multiple models

`/best-of-n` runs the same task across multiple models at once. Each run gets its own worktree, so the candidates stay isolated from each other and from your main checkout.

```text
/best-of-n sonnet,gpt,composer fix the flaky logout test
```

Use it when you want to:

- Compare different models on the same prompt
- Try multiple approaches for a hard change
- Pick the strongest result before applying anything

`/best-of-n` compares runs only. It does not merge changes back into your main checkout for you. After you pick a winner, you can commit and push directly from the worktree or use `/apply-worktree` to bring the changes into your main checkout.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Agent Security

*AI can behave unexpectedly due to prompt injection, hallucinations, and other issues. We protect users with guardrails that limit what agents can do. By default, sensitive actions require your manual approval. This document explains our guardrails and what they mean for you.*

**Source:** https://cursor.com/docs/agent/security

AI can behave unexpectedly due to prompt injection, hallucinations, and other issues. We protect users with guardrails that limit what agents can do. By default, sensitive actions require your manual approval. This document explains our guardrails and what they mean for you.

These controls and behaviors are our defaults. We recommend keeping them enabled.

#### First-party tool calls

Cursor includes tools that help agents write code: reading files, editing files, running terminal commands, searching the web, and more.

Reading files and searching code don't require approval. Use [.cursorignore](https://cursor.com/docs/reference/ignore-file.md) to block agent access to specific files. Actions that could expose sensitive data require your explicit approval.

Agents can modify workspace files without approval, except for configuration files. Changes save immediately to disk. Always use version control so you can revert changes. Configuration files (like workspace settings) need your approval first.

**Warning:** If you have auto-reload enabled, agent changes might execute before you can review them.

By default, terminal commands need your approval. To let trusted calls run without prompting, configure [Run Modes](https://cursor.com/docs/agent/security/run-modes.md). They range from a simple allowlist to the **Auto-review** classifier, and they're best-effort guardrails rather than a hard security boundary.

#### Third-party tool calls

You can connect external tools using [MCP](https://cursor.com/docs/mcp.md). All MCP connections need your approval. After you approve an MCP connection, each tool call still needs individual approval before running. You can pre-approve specific tools with an [MCP allowlist](https://cursor.com/docs/reference/permissions.md#mcp-allowlist-format).

#### Network requests

Attackers could use network requests to steal data. Our tools only make network requests to:

- GitHub
- Direct link retrieval
- Web search providers

Agents cannot make arbitrary network requests with default settings.

#### Workspace trust

Cursor supports [workspace trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust), but it's disabled by default. When enabled, it prompts you to choose between normal or restricted mode for new workspaces. Restricted mode breaks AI features. For untrusted repos, use a basic text editor instead.

To enable workspace trust:

1. Open your user settings.json file
2. Add the following configuration:

   ```json
   "security.workspace.trust.enabled": true
   ```

Organizations can enforce this setting through MDM solutions.

#### Responsible disclosure

Found a vulnerability? Email [security-reports@cursor.com](mailto:security-reports@cursor.com) with details and steps to reproduce.

We acknowledge vulnerability reports within 5 business days. For critical incidents, we notify all users via email.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Run Modes

*Run Modes control how the Cursor agent runs tool calls, and when Cursor interrupts you for approval.*

**Source:** https://cursor.com/docs/agent/security/run-modes

Run Modes control how the Cursor agent runs tool calls, and when Cursor interrupts you for approval.

Use them to decide how much autonomy the agent gets for shell commands, MCP tools, and Fetch calls. The safest useful setup for most people is **Auto-review**. It runs known-safe calls, sandboxes shell commands when it can, and asks a classifier to review anything else.

#### Pick a mode

In the desktop application, go to **Settings > Agents > Approvals & Execution**.

| Mode               | What runs without asking                                                                                                                                      | Sandbox                      | Classifier | Use it when                                                                 |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------- | :--------- | :-------------------------------------------------------------------------- |
| **Auto-review**    | Allowlisted calls run immediately. Other shell commands run in the sandbox when possible. Calls that do not use the sandbox go to the Auto-review classifier. | Yes, for shell commands      | Yes        | You want fewer prompts with a safety review before higher-risk calls run.   |
| **Allowlist**      | Actions in your allowlist run without approval. With sandboxing enabled, supported shell commands can run in the sandbox.                                     | Optional, for shell commands | No         | You want deterministic behavior with a small set of trusted repeat actions. |
| **Run Everything** | Every tool call runs automatically.                                                                                                                           | No                           | No         | You accept the risk and want zero prompts.                                  |

#### How Auto-review works

Auto-review applies to shell, MCP, and Fetch tool calls. Cursor checks each call in this order:

![The execution lifecycle of agent actions on Auto-review mode. Allowlisted calls run immediately, other shell commands run in the sandbox when possible, and anything else goes to the classifier, which can allow the call, ask the agent to take a different approach, or ask you to approve.](https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/uploads/kreview-auto-review-light.svg)

A shell command "can run in the sandbox" when it works under the sandbox's file and network limits. Commands that need full system access, like writes outside the workspace or privileged operations, can't be sandboxed, so they go to the classifier instead.

Sandboxing is a layer on top of Run Modes for shell commands. It controls where a supported terminal command runs, not whether the mode uses the Auto-review classifier.

When the classifier blocks a call, Cursor can try another approach. If the agent decides that the action makes sense despite what the classifier said, Cursor will show you an approval prompt.

##### Auto-review is not a security boundary

The classifier can make mistakes. It can allow a call you would have blocked, or block a call you would have allowed.

##### Configuring Auto-review

Configuration is not required for Auto-review to work well. If there are specific actions you always want to review manually, describe them in plain English.

The easiest way to set this up is to ask the Cursor agent to do it. Tell it something like "I want every AWS CLI command to go through approval first," and it edits your `permissions.json` for you.

You can also edit the file yourself. Auto-review reads `permissions.json` from two locations:

| Location                                 | Scope                                                                                        |
| :--------------------------------------- | :------------------------------------------------------------------------------------------- |
| `~/.cursor/permissions.json`             | Applies to all project directories on your machine.                                          |
| `<project-dir>/.cursor/permissions.json` | Applies to one project directory. Commit it when the project should share the same guidance. |

If both files exist, Cursor merges them. Your personal instructions and the project instructions both apply.

Teams can also define a global Auto-review configuration in the dashboard. When a team configuration is defined, it takes priority and Cursor ignores the user-level and project-level files.

Both local files use the same schema. Each instruction is a plain-English sentence, so a request like "I want every AWS CLI command to go through approval first" maps straight onto `block_instructions`:

```json
{
  "autoRun": {
    "allow_instructions": [],
    "block_instructions": [
      "Every AWS CLI command should go through approval first.",
      "Every command that modifies Kubernetes resources should go through approval first."
    ]
  }
}
```

- `allow_instructions` describe actions Auto-review should lean toward allowing.
- `block_instructions` describe actions Auto-review should lean toward blocking so the agent can choose another path or ask you to approve.

For more on policy design, read [Governing agent autonomy with Auto-review](https://cursor.com/blog/agent-autonomy-auto-review).

#### Sandboxing

Sandboxing lets Cursor run terminal commands without giving them full machine access. A sandboxed command can work in your project, but it cannot freely read protected files, write outside approved paths, or contact arbitrary network destinations.

For the engineering deep dive, read [Implementing a secure sandbox for local agents](https://cursor.com/blog/agent-sandboxing).

##### permissions.json and sandbox.json do different jobs

`permissions.json` steers which calls Auto-review runs automatically and which it reviews. `sandbox.json` controls what a sandboxed command can reach, like network domains and extra readable or writable paths. You don't need either file to get started.

| Access              | Default sandbox behavior for terminal commands                                                                           |
| :------------------ | :----------------------------------------------------------------------------------------------------------------------- |
| **Workspace files** | Read and write access inside the workspace. `.cursorignore` can hide files from the agent.                               |
| **Protected paths** | Cursor protects paths like `.git/config`, `.git/hooks`, `.vscode`, `.cursorignore`, and sensitive Cursor config files.   |
| **Network**         | Blocked by default, then opened by your network mode and [`sandbox.json`](https://cursor.com/docs/reference/sandbox.md). |
| **Temporary files** | `/tmp` and platform temp directories are writable unless disabled in `sandbox.json`.                                     |

Some commands need full system access and bypass the sandbox. Cursor will indicate when a command runs outside the sandbox and ask for your approval.

##### Sandbox configuration

Customize sandbox behavior with a `sandbox.json` file:

| Location                             | Scope                                                                                             |
| :----------------------------------- | :------------------------------------------------------------------------------------------------ |
| `~/.cursor/sandbox.json`             | Applies to all project directories on your machine.                                               |
| `<project-dir>/.cursor/sandbox.json` | Applies to one project directory. Commit it when the project should share the same sandbox rules. |

If both files exist, Cursor merges them with the project-level file taking priority. Team-admin policies and Cursor's hardcoded security rules layer on top, so local files cannot weaken those protections.

Use `sandbox.json` to control network policy, extra readable or writable paths, temporary directory writes, and shared build caches. See the [`sandbox.json` reference](https://cursor.com/docs/reference/sandbox.md) for the full schema.

##### How sandboxing works on your platform

##### macOS

Cursor uses Seatbelt through `sandbox-exec`. A generated sandbox profile limits file access, network access, and other process behavior for the full subprocess tree.

**Requirements**

- Cursor v2.0 or later
- No extra setup needed

##### Linux

Cursor uses Landlock and seccomp. Landlock applies filesystem restrictions. Seccomp blocks unsafe syscalls.

**Requirements**

- **Kernel 6.2 or later** with Landlock v3 support (`CONFIG_SECURITY_LANDLOCK=y`)
- **Unprivileged user namespaces** enabled

If your kernel does not meet these requirements, Cursor falls back to asking for approval before running commands.

##### AppArmor setup (remote environments and CLI only)

Local desktop installations need no setup. The Cursor desktop package ships with the required AppArmor profile.

Some distributions restrict user namespaces through AppArmor, and remote environments and the standalone [CLI](https://cursor.com/docs/cli/overview.md) do not ship the profile. If sandbox creation fails there with a user-namespace permissions error, install the AppArmor package for your distribution.

Debian / Ubuntu:

```bash
curl -fsSL https://downloads.cursor.com/lab/enterprise/cursor-sandbox-apparmor_0.6.0_all.deb -o cursor-sandbox-apparmor.deb
sudo dpkg -i cursor-sandbox-apparmor.deb
```

RHEL / Fedora:

```bash
curl -fsSL https://downloads.cursor.com/lab/enterprise/cursor-sandbox-apparmor-0.6.0-1.noarch.rpm -o cursor-sandbox-apparmor.rpm
sudo rpm -i cursor-sandbox-apparmor.rpm
```

After installing, restart Cursor or your CLI session for the sandbox to work.

##### Environment variables

Cursor injects environment variables into every sandboxed child process. These are available to your scripts, build tools, and automation running inside the sandbox.

| Variable                         | Platforms    | Description                                                                                                                  |
| :------------------------------- | :----------- | :--------------------------------------------------------------------------------------------------------------------------- |
| `CURSOR_SANDBOX`                 | macOS, Linux | Set to `"seatbelt"` (macOS) or `"native"` (Linux) when the process is running inside the sandbox.                            |
| `CURSOR_ORIG_UID`                | macOS, Linux | The UID of the user who launched Cursor, captured before the sandbox applies any namespace or identity changes.              |
| `CURSOR_ORIG_GID`                | macOS, Linux | The GID of the user who launched Cursor, captured before sandbox identity changes.                                           |
| `CURSOR_SANDBOX_LANDLOCK_STATUS` | Linux        | Reports the active sandbox backend: `fully_enforced` (Landlock), `bubblewrap` (Bubblewrap fallback). Useful for diagnostics. |

##### Linux: UID inside the sandbox may not match your real user

On Linux, the sandbox creates a user namespace and remaps the process to UID 0
(root) inside that namespace. This means `id -u` and `$UID` inside a sandboxed
command return 0, not your host user ID. If your scripts or automation need
the host user ID, for example, to set file ownership or pass `--user` to
Docker, read `CURSOR_ORIG_UID` and `CURSOR_ORIG_GID` instead.

###### Docker and container automation

A common pattern in automation rules and scripts is running Docker containers that need to match the host user's identity. Because the sandbox remaps the UID on Linux, relying on `$(id -u)` produces the wrong value. Use the `CURSOR_ORIG_*` variables instead:

```bash
docker run --rm \
  --user "${CURSOR_ORIG_UID:-$(id -u)}:${CURSOR_ORIG_GID:-$(id -g)}" \
  -v "$PWD:/work" -w /work \
  my-image build
```

The `${CURSOR_ORIG_UID:-$(id -u)}` fallback ensures the command also works outside the sandbox, where the variables are not set.

##### Network access

Choose how sandboxed terminal commands access the network:

| Mode                        | Behavior                                                                                                            |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| **sandbox.json Only**       | Network is limited to domains in your `sandbox.json` allowlist. Cursor defaults are not added.                      |
| **sandbox.json + Defaults** | Your allowlist plus Cursor's built-in defaults for common package managers and language tools. This is the default. |
| **Allow All**               | All network access is allowed in the sandbox, regardless of `sandbox.json`.                                         |

##### View default allowed domains

```text
*.cloudflarestorage.com
*.docker.com
*.docker.io
*.googleapis.com
*.githubusercontent.com
*.gvt1.com
*.public.blob.vercel-storage.com
*.yarnpkg.com
alpinelinux.org
anaconda.com
apache.org
apt.llvm.org
archive.ubuntu.com
archlinux.org
awscli.amazonaws.com
azure.com
binaries.prisma.sh
bitbucket.org
centos.org
cloudflarestorage.com
cocoapods.org
codeload.github.com
cpan.org
crates.io
debian.org
dl.google.com
docker.com
docker.io
dot.net
dotnet.microsoft.com
eclipse.org
fedoraproject.org
files.pythonhosted.org
fonts.gstatic.com
gcr.io
ghcr.io
github.com
gitlab.com
golang.org
google.com
goproxy.io
gradle.org
haskell.org
hashicorp.com
hex.pm
index.crates.io
java.com
java.net
json-schema.org
json.schemastore.org
k8s.io
launchpad.net
maven.org
mcr.microsoft.com
metacpan.org
microsoft.com
mise.run
nodejs.org
npm.duckdb.org
npmjs.com
npmjs.org
nuget.org
oracle.com
packagecloud.io
packages.microsoft.com
packagist.org
pkg.go.dev
playwright.azureedge.net
ppa.launchpad.net
proxy.golang.org
pub.dev
public.blob.vercel-storage.com
public.ecr.aws
pypa.io
pypi.org
pypi.python.org
pythonhosted.org
quay.io
registry.npmjs.org
registry.yarnpkg.com
repo.maven.apache.org
ruby-lang.org
rubygems.org
rubyonrails.org
rustup.rs
rvm.io
security.ubuntu.com
sh.rustup.rs
sourceforge.net
spring.io
static.crates.io
static.rust-lang.org
sum.golang.org
swift.org
ubuntu.com
visualstudio.com
yarnpkg.com
ziglang.org
```

#### Other protections

Run Modes and sandboxing are not the only safety controls. These protections can require approval even when a mode would otherwise run automatically:

| Protection                   | What it does                                                                                       |
| :--------------------------- | :------------------------------------------------------------------------------------------------- |
| **Browser Protection**       | Prevents the agent from automatically running Browser tools.                                       |
| **File-Deletion Protection** | Prevents the agent from automatically deleting files, including `rm` commands.                     |
| **External-File Protection** | Prevents the agent from automatically creating, modifying or deleting files outside the workspace. |

#### Team controls

Admins can override which modes are available for their users, as well as configure the sandbox networking rules for terminal commands, and more. All of these settings are available in the web dashboard.

Team settings take precedence over individual and project configuration. Use them when you want a consistent baseline for everyone.

#### Changelog

| Cursor version | Date         | Change                                                                                                                                                                                                    |
| :------------- | :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **3.6**        | May 29, 2026 | [Auto-review](https://cursor.com/changelog/auto-review) shipped as the recommended default.                                                                                                                                 |
| **3.5**        | May 22, 2026 | **Ask Every Time** was deprecated. New users cannot choose it. Use **Allowlist** with an empty allowlist for the same behavior. **Run in Sandbox** was folded into **Allowlist** with sandboxing enabled. |

##### Cloud Agents do not use Run Modes

Run Modes apply to local agents. Cloud Agents run inside their own dedicated machine, so the agent never asks you to approve an action.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

---

## Customizing Cursor

### Customize Cursor

*Plugins, skills, and MCPs let you customize Cursor for your workflows. The **Customize** page brings them into one place.*

**Source:** https://cursor.com/docs/customize-cursor

Plugins, skills, and MCPs let you customize Cursor for your workflows. The **Customize** page brings them into one place.

Open **Customize** from the sidebar in Cursor to add and manage extensions at the user, team, or workspace level. You can install official and community plugins, connect MCP servers (including your own), and control which rules, skills, subagents, commands, and hooks are active for each scope.

#### What you can do from Customize

From the Customize page, you can:

- **Browse and install** plugins, skills, and MCPs from the [Cursor Marketplace](https://cursor.com/marketplace) with one click
- **Install Team MCP servers** shared through your team's [Default marketplace](https://cursor.com/docs/plugins.md#default-team-marketplace)
- **See your team leaderboard** of the most popular plugins, skills, and MCPs across your team and the community
- **Add and manage** plugins, skills, MCPs, subagents, rules, commands, and hooks without switching between separate settings pages
- **Filter by scope** to see what is installed for you, your workspace, or your team
- **Open plugin canvases** for shared setup templates your team can reuse

Learn more in the [changelog](https://cursor.com/changelog/customize).

#### Extension components

Cursor extensions are built from composable pieces. Plugins often bundle several of these together, but you can also add each component on its own.

| Component     | Description                                                                                                                                                                                                                                                                                                                |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Plugins**   | Distributable bundles that package rules, skills, subagents, commands, MCP servers, and hooks. Install from the [marketplace](https://cursor.com/marketplace) or a [team marketplace](https://cursor.com/docs/plugins.md#team-marketplaces).                                                                                                 |
| **Rules**     | Persistent instructions that shape how Agent works with your code. Use [project rules](https://cursor.com/docs/rules.md#project-rules), [user rules](https://cursor.com/docs/rules.md#user-rules), [team rules](https://cursor.com/docs/rules.md#team-rules), or [`AGENTS.md`](https://cursor.com/docs/rules.md#agentsmd). |
| **Skills**    | Specialized capabilities Agent loads when relevant. Skills package domain knowledge, workflows, and scripts in `SKILL.md` files. See [Agent Skills](https://cursor.com/docs/skills.md).                                                                                                                                    |
| **Subagents** | Specialized assistants Agent delegates to for parallel or isolated work. Each subagent runs in its own context window. See [Subagents](https://cursor.com/docs/subagents.md).                                                                                                                                              |
| **Hooks**     | Scripts that observe, control, or extend the agent loop at specific lifecycle events. See [Hooks](https://cursor.com/docs/hooks.md).                                                                                                                                                                                       |
| **Commands**  | Reusable prompts you invoke with `/` in Agent chat. Commands are markdown files that define a focused workflow or action.                                                                                                                                                                                                  |

For MCP servers that connect Cursor to external tools and data sources, see [Model Context Protocol (MCP)](https://cursor.com/docs/mcp.md).

#### Marketplace leaderboard

Cursor shows a leaderboard of the most popular plugins, skills, and MCPs across your team.

Add any entry to your setup with one click from the Customize page and extend Cursor for your workflow. The leaderboard helps you discover what teammates and the community use most, so you can adopt proven setups quickly.

Browse the full catalog in the [Cursor Marketplace](https://cursor.com/marketplace). For community plugins and MCP servers, see [cursor.directory](https://cursor.directory).

#### Learn more

##### Plugins

Browse the marketplace, install plugins, and set up team marketplaces

##### Rules

Write project, user, and team rules that guide Agent behavior

##### Skills

Package specialized workflows in portable SKILL.md files

##### MCP

Connect Cursor to external tools, APIs, and data sources

##### Subagents

Delegate complex tasks to specialized agents

##### Hooks

Run scripts at key points in the agent loop


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Plugins

*Plugins package rules, skills, agents, commands, MCP servers, and hooks into distributable bundles. Install and manage them from the [Customize](https://cursor.com/docs/customize-cursor.md) page or browse official plugins in the [Cursor Marketplace](https://cursor.com/marketplace). For community plugins and MCP servers, browse [cursor.directory](https://cursor.directory). You can also [build your own](https://cursor.com/docs/plugins.md#creating-plugins) to share with other developers.*

**Source:** https://cursor.com/docs/plugins

Plugins package rules, skills, agents, commands, MCP servers, and hooks into distributable bundles. Install and manage them from the [Customize](https://cursor.com/docs/customize-cursor.md) page or browse official plugins in the [Cursor Marketplace](https://cursor.com/marketplace). For community plugins and MCP servers, browse [cursor.directory](https://cursor.directory). You can also [build your own](https://cursor.com/docs/plugins.md#creating-plugins) to share with other developers.

#### What plugins contain

A plugin can bundle any combination of these components:

| Component       | Description                                                |
| :-------------- | :--------------------------------------------------------- |
| **Rules**       | Persistent AI guidance and coding standards (`.mdc` files) |
| **Skills**      | Specialized agent capabilities for complex tasks           |
| **Agents**      | Custom agent configurations and prompts                    |
| **Commands**    | Agent-executable command files                             |
| **MCP Servers** | Model Context Protocol integrations                        |
| **Hooks**       | Automation scripts triggered by events                     |

#### Plugin canvases

Plugins now ship with prebuilt **canvases**: shared setup templates your team can open and reuse.

- **Hex Canvas** — Build data visualizations. At Cursor, we use the Hex Canvas to explore and share analytics.
- **Atlassian Canvas** — See a realtime view of your issues, projects, and documents from Jira and Confluence.

Open a canvas from an installed plugin in Customize to get a guided starting point instead of configuring everything from scratch.

#### The marketplace

The [Cursor Marketplace](https://cursor.com/marketplace) is where you discover and install official plugins. Plugins are distributed as Git repositories and submitted through the Cursor team. Every plugin is [manually reviewed](https://cursor.com/help/security-and-privacy/marketplace-security.md) before it's listed. Browse official plugins at [cursor.com/marketplace](https://cursor.com/marketplace) or search by keyword in **Customize**. For community plugins and MCP servers, browse [cursor.directory](https://cursor.directory).

#### Team marketplaces

Team marketplaces are available on Teams and Enterprise plans.

- Teams plan: up to 1 team marketplace
- Enterprise plan: unlimited team marketplaces

[Contact sales](https://cursor.com/contact-sales?source=docs-plugins) for unlimited team marketplaces and Enterprise admin controls.

Open **Dashboard -> Plugins** to manage Team Marketplaces.

On Enterprise plans, only admins can add team marketplaces from **Dashboard
-> Plugins**.

##### Default team marketplace

The **Default** team marketplace connects shared plugins and MCP servers across Cursor. Admins can add Team MCP servers that are already available to Cloud Agents, then make the same servers available for teammates to install and configure in the Agent Window, IDE, and CLI.

Adding a Team MCP server to the Default marketplace does not install or enable it for every developer. Admins still control marketplace access and plugin installation modes. Each developer may also need to authenticate with the MCP provider.

##### Migrate existing Team MCPs

Admins can link standalone Team MCP servers to the Default marketplace:

1. Open **Dashboard -> Integrations & MCP**.
2. Find **Team MCP Servers**.
3. Select **Add to Team Marketplace** in the migration prompt.
4. Open **Dashboard -> Plugins** to review the Default marketplace, its access, and plugin installation modes.

Cursor creates the Default marketplace if needed and links the existing MCP servers to it. The servers remain available to Cloud Agents while teammates gain the option to install and configure them locally.

Removing a linked MCP plugin from the marketplace or deleting the marketplace
can delete the Team MCP server. This removes it for local users and Cloud
Agents. Review the confirmation message before continuing.

##### Marketplace access

Team marketplaces are available to everyone in their team by default. Under **Marketplace Settings -> Marketplace Access**, admins can restrict a marketplace to selected [Organization Groups](https://cursor.com/docs/enterprise/organization-groups.md). Only members of the marketplace's team who belong to a selected group receive access. Team admins retain access.

##### How does SCIM work?

Organization Groups can sync membership from your identity provider through [SCIM](https://cursor.com/docs/account/teams/scim.md). Manage membership in your identity provider, and Cursor syncs those updates to the Organization Group.

Existing marketplaces that use team-level SCIM directory groups keep that configuration. Cursor does not migrate those assignments automatically. Organizations without Organization Groups continue to use SCIM directory groups.

##### Plugin installation modes

After setting marketplace access, choose how each plugin is distributed to that audience:

- **Default Off**: Developers can find the plugin and choose whether to install it.
- **Default On**: The plugin is installed by default, but developers can opt out.
- **Required**: The plugin is always installed and cannot be uninstalled.

#### Add a team marketplace

Use this flow to import a GitHub repository as a team marketplace:

1. Go to **Dashboard -> Plugins**.
2. In **Team Marketplaces**, click **Add Marketplace**.
3. Follow the instructions to create a marketplace from scratch, or use "Import from Repo" if importing from GitHub.
4. Add and review plugins using "Add to Marketplace".
5. Under **Marketplace Settings**, set **Marketplace Access**, optionally enable Auto Refresh, then save.

Example repository to try:

- [fieldsphere/cursor-team-marketplace-template](https://github.com/fieldsphere/cursor-team-marketplace-template)

#### Keep plugins up to date

When importing from GitHub, plugins are indexed when you first import the repository. You can refresh plugins in two ways:

- **Automatically**: Turn on **Enable Auto Refresh** to update plugins automatically whenever changes are pushed to the branch the marketplace tracks. This requires the [Cursor GitHub App](https://cursor.com/docs/integrations/github.md) installed on the repository. Cursor re-indexes a marketplace at most once every 10 minutes, batching rapid pushes to the latest commit.
- **Manually**: Click "Refresh" to manually update.

Auto Refresh updates plugins that are already part of the marketplace. Adding a brand-new plugin from the repository isn't automatic — re-import the repository URL to pick up newly added plugins.

#### Where developers find team marketplaces

Developers can find team marketplaces in Customize.

- Open **Customize** in the sidebar
- Look for plugins from your team marketplace.
- Install Default Off plugins directly from that panel.
- Default On plugins are installed automatically, but developers can opt out.
- Required plugins are installed automatically and cannot be uninstalled.
- Install and configure marketplace MCP servers for use in the Agent Window, IDE, and CLI.

#### Installing plugins

Install plugins from the marketplace. Plugins can be scoped to a project or installed at the user level.

##### MCP Apps deeplinks

Share MCP server configurations using install links:

```text
cursor://anysphere.cursor-deeplink/mcp/install?name=$NAME&config=$BASE64_ENCODED_CONFIG
```

See [MCP install links](https://cursor.com/docs/mcp/install-links.md) for details on generating these links.

#### Managing installed plugins

Open **Customize** in the sidebar to manage plugins, MCP servers, rules, and skills from one page. Filter by user, workspace, or team scope to see what is installed.

##### MCP servers

Toggle personal and team-distributed MCP servers on or off from Customize:

1. Open **Customize** in the sidebar
2. Find the MCP server you want to change
3. Use the toggle to enable or disable it

Disabled servers won't load or appear in chat.

##### Rules and skills

Manage rules and skills from Customize. Toggle individual rules between **Always**, **Agent Decides**, and **Manual** modes. Skills appear in the **Agent Decides** section and can be invoked manually with `/skill-name` in chat.

#### Using the workspaceOpen hook

A `workspaceOpen` hook can return plugin paths to load on workspace open, which is useful when the set of plugins depends on the workspace itself.

##### Hooks reference

Register plugin paths from a `workspaceOpen` hook script

#### Creating plugins

A plugin is a directory with a `.cursor-plugin/plugin.json` manifest and your components (rules, skills, agents, commands, hooks, or MCP servers). Start from the [plugin template repository](https://github.com/cursor/plugin-template) or create one from scratch:

```text
my-plugin/
├── .cursor-plugin/
│   └── plugin.json
├── rules/
│   └── coding-standards.mdc
├── skills/
│   └── code-reviewer/
│       └── SKILL.md
└── mcp.json
```

The manifest only requires a `name` field. Components are discovered automatically from their default directories, or you can specify custom paths in the manifest.

```json
{
  "name": "my-plugin",
  "description": "Custom development tools",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
```

##### Test plugins locally

Before you publish, load your plugin from `~/.cursor/plugins/local`:

1. Create a folder for your plugin:
   `~/.cursor/plugins/local/my-plugin`
2. Copy your plugin files into that folder. Make sure `.cursor-plugin/plugin.json` is at the plugin root.
3. Restart Cursor, or run **Developer: Reload Window**.
4. Verify your plugin components load in Cursor, such as rules, skills, or MCP servers.

For faster iteration, symlink your plugin repository:

```bash
ln -s /path/to/my-plugin ~/.cursor/plugins/local/my-plugin
```

When your plugin is ready, submit it for review at [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish). For multi-plugin repositories, add a marketplace manifest at `.cursor-plugin/marketplace.json`.

See the [Plugins reference](https://cursor.com/docs/reference/plugins.md) for the full manifest schema, component formats, and submission checklist.

##### Team and Enterprise marketplaces

Upgrade for private team marketplaces and organization-wide plugin distribution.

#### FAQ

##### Are marketplace plugins reviewed for security?

Yes. Every plugin is manually reviewed before it's listed. All plugins must be open source, and we review each update before publishing. See [Marketplace security](https://cursor.com/help/security-and-privacy/marketplace-security.md) for details on vetting, update reviews, and how to report issues.

##### How do I create a plugin?

Create a directory with a `.cursor-plugin/plugin.json` manifest file, add your rules, skills, agents, commands, or other components, and submit it to the Cursor team. See the [Plugins reference](https://cursor.com/docs/reference/plugins.md) for the full guide.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Rules

*Rules provide system-level instructions to Agent. They bundle prompts, scripts, and more together, making it easy to manage and share workflows across your team.*

**Source:** https://cursor.com/docs/rules

Rules provide system-level instructions to Agent. They bundle prompts, scripts, and more together, making it easy to manage and share workflows across your team.

Cursor supports four types of rules:

##### Project Rules

Stored in `.cursor/rules`, version-controlled and scoped to your codebase.

##### User Rules

Global to your Cursor environment. Used by Agent (Chat).

##### Team Rules

Team-wide rules managed from the dashboard. Available on Team and [Enterprise](https://cursor.com/docs/enterprise.md) plans.

##### AGENTS.md

Agent instructions in markdown format. Simple alternative to
`.cursor/rules`.

#### How rules work

Large language models don't retain memory between completions. Rules provide persistent, reusable context at the prompt level.

When applied, rule contents are included at the start of the model context. This gives the AI consistent guidance for generating code, interpreting edits, or helping with workflows.

#### Project rules

Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled. They are scoped using path patterns, invoked manually, or included based on relevance.

Use project rules to:

- Encode domain-specific knowledge about your codebase
- Automate project-specific workflows or templates
- Standardize style or architecture decisions

##### Rule file structure

Each rule is an `.mdc` file that you can name anything you want. Project rules must use the `.mdc` extension. A plain `.md` file in `.cursor/rules` is ignored by the rules system because it has no frontmatter to specify `description`, `globs`, and `alwaysApply`. If you prefer plain markdown, use [AGENTS.md](https://cursor.com/docs/rules.md#agentsmd) instead.

```bash
.cursor/rules/
  react-patterns.mdc       # Recognized as a project rule
  api-guidelines.md        # Ignored (wrong extension)
  frontend/                # Organize rules in folders
    components.mdc
```

##### Rule anatomy

Each rule is a markdown file with frontmatter metadata and content. Control how rules are applied from the type dropdown which changes properties `description`, `globs`, `alwaysApply`.

| Rule Type                 | Description                                           |
| :------------------------ | :---------------------------------------------------- |
| `Always Apply`            | Apply to every chat session                           |
| `Apply Intelligently`     | When Agent decides it's relevant based on description |
| `Apply to Specific Files` | When file matches a specified pattern                 |
| `Apply Manually`          | When @-mentioned in chat (e.g., `@my-rule`)           |

Under the hood, the three frontmatter fields interact to determine when a rule is included:

| `alwaysApply` | `description` | `globs`  | Behavior                                                         |
| :------------ | :------------ | :------- | :--------------------------------------------------------------- |
| `true`        | —             | —        | Always included. Globs and description are ignored.              |
| `false`       | —             | provided | Auto-attached when a matching file is in context.                |
| `false`       | provided      | omitted  | Agent reads the description and pulls the rule in when relevant. |
| `false`       | omitted       | omitted  | Included only when you `@`-mention the rule in chat.             |

```md title="Always applied"
---
alwaysApply: true
---

- All source files must include the company copyright header
- When you are unsure about implementation details, read the relevant
  source files before proposing changes
- Never modify generated files in the `dist/` or `build/` directories
```

```md title="Auto-attached by file pattern"
---
globs: src/components/**/*.tsx
alwaysApply: false
---

- Use named exports, not default exports
- Co-locate styles in a module CSS file next to the component
- Keep components under 200 lines. Extract subcomponents into the same
  directory when a file grows beyond that
- Prefer composition over prop drilling. Pass children or render props
  instead of threading data through multiple layers
```

```md title="Agent-selected based on description"
---
description: RPC service conventions and patterns for the backend
alwaysApply: false
---

- Define each service in its own file under `src/services/`
- Always validate inputs at the service boundary before passing data
  to internal functions
- Return structured error objects with a `code` and `message` field,
  never throw raw strings
- Add a `@service-template.ts` reference file when creating a new
  service for the standard boilerplate
```

```md title="Manual — only via @-mention"
---
alwaysApply: false
---

- Every database migration must have both `up` and `down` functions
  so it can be fully reversed
- Never alter a column type in-place. Add a new column, backfill,
  then drop the old one in a separate migration
- Reference the template for the expected file structure

@migration-template.sql
```

##### Glob pattern examples

Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas.

| Pattern                       | Matches                                                |
| :---------------------------- | :----------------------------------------------------- |
| `*`                           | Any single file name segment                           |
| `**`                          | Any number of directories (recursive)                  |
| `*.ts`                        | All `.ts` files in the root                            |
| `**/*.ts`                     | All `.ts` files in any directory                       |
| `src/**`                      | All files anywhere under `src/`                        |
| `src/**/*.tsx`                | All `.tsx` files anywhere under `src/`                 |
| `docs/**/*.md, docs/**/*.mdx` | `.md` and `.mdx` files under `docs/` (comma-separated) |
| `tailwind.config.*`           | `tailwind.config` with any extension                   |

##### Creating a rule

There are two ways to create rules:

- **`/create-rule` in chat**: Type `/create-rule` in Agent and describe what you want. Agent generates the rule file with proper frontmatter and saves it to `.cursor/rules`.
- **From Customize**: Open **Customize** in the sidebar, go to **Rules**, and click **Add Rule**. This creates a new rule file in `.cursor/rules`. From Customize you can see all rules and their status.

#### Best practices

Good rules are focused, actionable, and scoped.

- Keep rules under 500 lines
- Split large rules into multiple, composable rules
- Provide concrete examples or referenced files
- Avoid vague guidance. Write rules like clear internal docs
- Reuse rules when repeating prompts in chat
- Reference files instead of copying their contents—this keeps rules short and prevents them from becoming stale as code changes

##### What to avoid in rules

- **Copying entire style guides**: Use a linter instead. Agent already knows common style conventions.
- **Documenting every possible command**: Agent knows common tools like npm, git, and pytest.
- **Adding instructions for edge cases that rarely apply**: Keep rules focused on patterns you use frequently.
- **Duplicating what's already in your codebase**: Point to canonical examples instead of copying code.

Start simple. Add rules only when you notice Agent making the same mistake repeatedly. Don't over-optimize before you understand your patterns.

Check your rules into git so your whole team benefits. When you see Agent make a mistake, update the rule. You can even tag `@cursor` on a GitHub issue or PR to have Agent update the rule for you.

#### Rule file format

Each rule is a markdown file with frontmatter metadata and content. The frontmatter metadata is used to control how the rule is applied. The content is the rule itself.

```markdown
---
description: "This rule provides standards for frontend components and API validation"
alwaysApply: false
---

...rest of the rule content
```

If alwaysApply is true, the rule will be applied to every chat session. Otherwise, the description of the rule will be presented to the Cursor Agent to decide if it should be applied.

#### Examples

##### Standards for frontend components and API validation

This rule provides standards for frontend components:

When working in components directory:

- Always use Tailwind for styling
- Use Framer Motion for animations
- Follow component naming conventions

This rule enforces validation for API endpoints:

In API directory:

- Use zod for all validation
- Define return types with zod schemas
- Export types generated from schemas

##### Templates for Express services and React components

This rule provides a template for Express services:

Use this template when creating Express service:

- Follow RESTful principles
- Include error handling middleware
- Set up proper logging

@express-service-template.ts

This rule defines React component structure:

React components should follow this layout:

- Props interface at top
- Component as named export
- Styles at bottom

@component-template.tsx

##### Automating development workflows and documentation generation

This rule automates app analysis:

When asked to analyze the app:

1. Run dev server with `npm run dev`
2. Fetch logs from console
3. Suggest performance improvements

This rule helps generate documentation:

Help draft documentation by:

- Extracting code comments
- Analyzing README.md
- Generating markdown documentation

##### Adding a new setting in Cursor

First create a property to toggle in `@reactiveStorageTypes.ts`.

Add default value in `INIT_APPLICATION_USER_PERSISTENT_STORAGE` in `@reactiveStorageService.tsx`.

For beta features, add toggle in `@settingsBetaTab.tsx`, otherwise add in `@settingsGeneralTab.tsx`. Toggles can be added as `<SettingsSubSection>` for general checkboxes. Look at the rest of the file for examples.

```jsx
<SettingsSubSection
  label="Your feature name"
  description="Your feature description"
  value={
    vsContext.reactiveStorageService.applicationUserPersistentStorage
      .myNewProperty ?? false
  }
  onChange={(newVal) => {
    vsContext.reactiveStorageService.setApplicationUserPersistentStorage(
      "myNewProperty",
      newVal,
    );
  }}
/>
```

To use in the app, import reactiveStorageService and use the property:

```js
const flagIsEnabled =
  vsContext.reactiveStorageService.applicationUserPersistentStorage
    .myNewProperty;
```

Examples are available from providers and frameworks. Community-contributed rules are found across crowdsourced collections and repositories online.

#### Team Rules

Team and [Enterprise](https://cursor.com/docs/enterprise.md) plans can create and enforce rules across their entire organization from the [Cursor dashboard](https://cursor.com/dashboard/team-content). Admins can configure whether or not each rule is required for team members.

Team Rules work alongside other rule types and take precedence to ensure organizational standards are maintained across all projects. They provide a powerful way to ensure consistent coding standards, practices, and workflows across your entire team without requiring individual setup or configuration.

##### Managing Team Rules

Team administrators can create and manage rules directly from the Cursor dashboard:

![Empty team rules dashboard where team administrators can add new rules](https://cursor.com/docs-static/images/context/rules/team-rules-empty.png)

Once team rules are created, they automatically apply to all team members and are visible in the dashboard:

![Team rules dashboard showing a single team rule that will be enforced for all team members](https://cursor.com/docs-static/images/context/rules/team-rules-1.png)

##### Activation and enforcement

- **Enable this rule immediately**: When checked, the rule is active as soon as you create it. When unchecked, the rule is saved as a draft and does not apply until you enable it later.
- **Enforce this rule**: When enabled, the rule is required for all team members and cannot be disabled in Customize. When not enforced, team members can toggle the rule off under **Team Rules** in Customize.

By default, non‑enforced Team Rules can be disabled by users. Use Enforce this rule to prevent that.

##### Format and how Team Rules are applied

- **Content**: Team Rules are free‑form text. They do not use the folder structure of Project Rules.
- **Glob patterns**: Team Rules support glob patterns for file-scoped application. When a glob pattern is set (e.g., `**/*.py`), the rule only applies when matching files are in context. Rules without a glob pattern apply to every conversation.
- **Where they apply**: When a Team Rule is enabled (and not disabled by the user, unless enforced), it is included in the model context for Agent (Chat) across all repositories and projects for that team.
- **Precedence**: Rules are applied in this order: **Team Rules → Project Rules → User Rules**. All applicable rules are merged; earlier sources take precedence when guidance conflicts.

Some teams use enforced rules as part of internal compliance workflows. While this is supported, AI guidance should not be your only security control.

#### Importing Rules

You can import rules from external sources to reuse existing configurations or bring in rules from other tools.

##### Remote rules (via GitHub)

Import rules directly from any GitHub repository you have access to—public or private.

1. Open **Customize** in the sidebar
2. Go to **Rules** and click **Add Rule**
3. Select **Remote Rule (Github)**
4. Paste the GitHub repository URL containing the rules. Cursor will scan for all `.mdc` files in the repo.
5. Cursor will pull and sync the rule(s) into your project

Rules will be placed in `.cursor/rules/imported/<repoName>`. Rules will also keep their relative paths, so `dir/rule.mdc` will be imported as `.cursor/rule/imported/<repoName>/dir/rule.mdc`.

#### AGENTS.md

`AGENTS.md` is a simple markdown file for defining agent instructions. Place it in your project root as an alternative to `.cursor/rules` for straightforward use cases.

Unlike Project Rules, `AGENTS.md` is a plain markdown file without metadata or complex configurations. It's perfect for projects that need simple, readable instructions without the overhead of structured rules.

Cursor supports AGENTS.md in the project root and subdirectories.

```markdown
# Project Instructions

## Code Style

- Use TypeScript for all new files
- Prefer functional components in React
- Use snake_case for database columns

## Architecture

- Follow the repository pattern
- Keep business logic in service layers
```

##### Improvements

##### Nested AGENTS.md support

Nested `AGENTS.md` support in subdirectories is now available. You can place `AGENTS.md` files in any subdirectory of your project, and they will be automatically applied when working with files in that directory or its children.

This allows for more granular control of agent instructions based on the area of your codebase you're working in:

```bash
project/
  AGENTS.md              # Global instructions
  frontend/
    AGENTS.md            # Frontend-specific instructions
    components/
      AGENTS.md          # Component-specific instructions
  backend/
    AGENTS.md            # Backend-specific instructions
```

Instructions from nested `AGENTS.md` files are combined with parent directories, with more specific instructions taking precedence.

#### User Rules

User Rules are global preferences defined in **Customize → Rules** that apply across all projects. They are used by Agent (Chat) and are perfect for setting preferred communication style or coding conventions:

```md
Please reply in a concise style. Avoid unnecessary repetition or filler language.
```

#### FAQ

##### Why isn't my rule being applied?

Check the rule type. For `Apply Intelligently`, ensure a description is defined. For `Apply to Specific Files`, ensure the file pattern matches referenced files.

##### Can rules reference other rules or files?

Yes. Use `@filename.ts` to include files in your rule's context. You can also @mention rules in chat to apply them manually.

##### Can I create a rule from chat?

Yes, you can ask the agent to create a new rule for you.

##### Do rules impact Cursor Tab or other AI features?

No. Rules do not impact Cursor Tab or other AI features.

##### Do User Rules apply to Inline Edit (Cmd/Ctrl+K)?

No. User Rules are not applied to Inline Edit (Cmd/Ctrl+K). They are only
used by Agent (Chat).


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Agent Skills

*Agent Skills is an open standard for extending AI agents with specialized capabilities. Skills package domain-specific knowledge and workflows that agents can use to perform specific tasks.*

**Source:** https://cursor.com/docs/skills

Agent Skills is an open standard for extending AI agents with specialized capabilities. Skills package domain-specific knowledge and workflows that agents can use to perform specific tasks.

#### What are skills?

A skill is a portable, version-controlled package that teaches agents how to perform domain-specific tasks. Skills can include scripts, templates, and references that agents may act on using their tools.

##### Portable

Skills work across any agent that supports the Agent Skills standard.

##### Version-controlled

Skills are stored as files and can be tracked in your repository, or installed via GitHub repository links.

##### Actionable

Skills can include scripts, templates, and references that agents act on using their tools.

##### Progressive

Skills load resources on demand, keeping context usage efficient.

#### How skills work

When Cursor starts, it automatically discovers skills from skill directories and makes them available to Agent. The agent is presented with available skills and decides when they are relevant based on context.

Skills can also be manually invoked by typing `/` in Agent chat and searching for the skill name.

#### Built-in Cursor skills

Cursor includes a small set of built in skills to improve your general workflows. These skills are managed by Cursor and appear alongside the skills you add yourself.

| Skill                     | What it does                                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------------------- |
| `/automate`               | Creates Cursor Automations triggered by schedules, Slack messages, GitHub events, and other sources. |
| `/babysit`                | Monitors a pull request and addresses feedback, conflicts, failing checks, and follow-up work.       |
| `/canvas`                 | Creates interactive React artifacts that render alongside the conversation.                          |
| `/create-hook`            | Creates Cursor hooks and updates `hooks.json` for agent lifecycle events.                            |
| `/create-rule`            | Creates Cursor rules with the appropriate scope and instructions.                                    |
| `/create-skill`           | Creates Agent Skills, including their structure and `SKILL.md` files.                                |
| `/create-subagent`        | Creates custom subagents with focused roles and delegation instructions.                             |
| `/cursor-blame`           | Investigates AI-authored changes and the prompts that produced them.                                 |
| `/loop`                   | Runs a prompt or skill repeatedly at a specified interval.                                           |
| `/migrate-to-skills`      | Converts eligible dynamic rules and slash commands into Agent Skills.                                |
| `/review`                 | Selects and runs the appropriate code-review agent.                                                  |
| `/review-bugbot`          | Reviews code for likely bugs and regressions with Bugbot.                                            |
| `/review-security`        | Reviews code for security vulnerabilities with Security Review.                                      |
| `/sdk`                    | Helps you build applications and integrations with the Cursor SDK.                                   |
| `/shell`                  | Runs the provided text as a literal shell command.                                                   |
| `/split-to-prs`           | Splits large changes into smaller pull requests.                                                     |
| `/statusline`             | Configures the Cursor CLI status line.                                                               |
| `/update-cli-config`      | Updates Cursor CLI settings in `~/.cursor/cli-config.json`.                                          |
| `/update-cursor-settings` | Finds and updates the appropriate Cursor or VS Code setting.                                         |

You can run any built-in skill by typing `/` in Agent chat and selecting its name. Agent may also use some built-in skills automatically when your request clearly matches their purpose.

#### Skill directories

Skills are automatically loaded from these locations:

| Location            | Scope               |
| ------------------- | ------------------- |
| `.agents/skills/`   | Project-level       |
| `.cursor/skills/`   | Project-level       |
| `~/.agents/skills/` | User-level (global) |
| `~/.cursor/skills/` | User-level (global) |

For compatibility, Cursor also loads skills from Claude and Codex directories: `.claude/skills/`, `.codex/skills/`, `~/.claude/skills/`, and `~/.codex/skills/`.

Each skill should be a folder containing a `SKILL.md` file:

```text
.agents/
└── skills/
    └── my-skill/
        └── SKILL.md
```

Skills can also include optional directories for scripts, references, and assets:

```text
.agents/
└── skills/
    └── deploy-app/
        ├── SKILL.md
        ├── scripts/
        │   ├── deploy.sh
        │   └── validate.py
        ├── references/
        │   └── REFERENCE.md
        └── assets/
            └── config-template.json
```

##### Nested skill directories

Skill directories can be organized into subdirectories. This is useful for grouping related skills by category, team, or domain. Cursor walks the skills root recursively and picks up any `SKILL.md` it finds:

```text
.cursor/
└── skills/
    ├── shipping/
    │   ├── land-it/
    │   │   └── SKILL.md
    │   └── careful-merge-conflicts/
    │       └── SKILL.md
    ├── debugging/
    │   └── using-datadog-mcp/
    │       └── SKILL.md
    └── workflow/
        └── tdd/
            └── SKILL.md
```

The category folder is purely organizational. The skill's identity comes from the folder containing `SKILL.md` (here `land-it`, `tdd`, etc.), not the parent category.

Cursor also discovers skills inside nested project subdirectories. A `.cursor/skills/` (or `.agents/skills/`) folder anywhere inside your repository is picked up, so monorepos can colocate skills with the package they apply to:

```text
my-monorepo/
├── .cursor/skills/         # repo-wide skills
│   └── land-it/SKILL.md
└── apps/
    └── web/
        └── .cursor/skills/  # app-specific skills
            └── deploy-web/SKILL.md
```

Skills in nested project directories are automatically scoped to files inside that directory. In the example above, `deploy-web` is only surfaced when the agent works with files under `apps/web/`, while skills in the repo-wide `.cursor/skills/` are available everywhere. This is similar to the [`paths` frontmatter field](https://cursor.com/docs/skills.md#scoping-a-skill-to-specific-files) — you don't need to set `paths` on a nested skill to scope it to its directory.

#### SKILL.md file format

Each skill is defined in a `SKILL.md` file with YAML frontmatter:

```markdown
---
name: my-skill
description: Short description of what this skill does and when to use it.
---

# My Skill

Detailed instructions for the agent.

## When to Use

- Use this skill when...
- This skill is helpful for...

## Instructions

- Step-by-step guidance for the agent
- Domain-specific conventions
- Best practices and patterns
- Use the ask questions tool if you need to clarify requirements with the user
```

##### Frontmatter fields

| Field                      | Required | Description                                                                                                                                                                        |
| -------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                     | Yes      | Skill identifier. Lowercase letters, numbers, and hyphens only. Must match the parent folder name.                                                                                 |
| `description`              | Yes      | Describes what the skill does and when to use it. Used by the agent to determine relevance.                                                                                        |
| `paths`                    | No       | Glob patterns that scope the skill to matching files. Accepts a comma-separated string or a list. When set, the skill is only surfaced when the agent works with files that match. |
| `disable-model-invocation` | No       | When `true`, the skill is only included when explicitly invoked via `/skill-name`. The agent will not automatically apply it based on context.                                     |
| `metadata`                 | No       | Arbitrary key-value mapping for additional metadata.                                                                                                                               |

#### Scoping a skill to specific files

Use the `paths` field to limit a skill to files that match one or more glob patterns. The skill is then only surfaced to the agent when it is reading or editing matching files. This keeps file-specific guidance out of context for unrelated work.

```markdown
---
name: react-component-patterns
description: Conventions for writing React components in this codebase.
paths:
  - "**/*.tsx"
  - "packages/ui/**/*.ts"
---

# React component patterns

...
```

You can also pass a single comma-separated string:

```markdown
---
name: python-style
description: Style rules for Python files.
paths: "**/*.py, scripts/**/*.py"
---
```

Patterns follow standard glob syntax. Leave `paths` unset for a skill that should be available regardless of which files are open.

The legacy `globs` field is still accepted as a fallback for older skills, but new skills should use `paths`.

#### Disabling automatic invocation

By default, skills are automatically applied when the agent determines they are relevant. Set `disable-model-invocation: true` to make a skill behave like a traditional slash command, where it is only included in context when you explicitly type `/skill-name` in chat.

#### Including scripts in skills

Skills can include a `scripts/` directory containing executable code that agents can run. Reference scripts in your `SKILL.md` using relative paths from the skill root.

```markdown
---
name: deploy-app
description: Deploy the application to staging or production environments. Use when deploying code or when the user mentions deployment, releases, or environments.
---

# Deploy App

Deploy the application using the provided scripts.

## Usage

Run the deployment script: `scripts/deploy.sh <environment>`

Where `<environment>` is either `staging` or `production`.

## Pre-deployment Validation

Before deploying, run the validation script: `python scripts/validate.py`
```

The agent reads these instructions and executes the referenced scripts when the skill is invoked. Scripts can be written in any language—Bash, Python, JavaScript, or any other executable format supported by the agent implementation.

Scripts should be self-contained, include helpful error messages, and handle edge cases gracefully.

#### Optional directories

Skills support these optional directories:

| Directory     | Purpose                                                |
| ------------- | ------------------------------------------------------ |
| `scripts/`    | Executable code that agents can run                    |
| `references/` | Additional documentation loaded on demand              |
| `assets/`     | Static resources like templates, images, or data files |

Keep your main `SKILL.md` focused and move detailed reference material to separate files. This keeps context usage efficient since agents load resources progressively—only when needed.

#### Viewing skills

To view discovered skills, open **Customize** in the sidebar and go to **Skills**. Skills installed from plugins or your project appear alongside rules in the **Agent Decides** section.

#### Installing skills from GitHub

You can import skills from GitHub repositories:

1. Open **Customize** in the sidebar
2. Go to **Rules** and click **Add Rule**
3. Select **Remote Rule (Github)**
4. Enter the GitHub repository URL

#### Migrating rules and commands to skills

Cursor includes a built-in `/migrate-to-skills` skill in 2.4 that helps you convert existing dynamic rules and slash commands to skills.

The migration skill converts:

- **Dynamic rules**: Rules that use the "Apply Intelligently" configuration—rules with `alwaysApply: false` (or undefined) and no `globs` patterns defined. These are converted to standard skills.
- **Slash commands**: Both user-level and workspace-level commands are converted to skills with `disable-model-invocation: true`, preserving their explicit invocation behavior.

To migrate:

1. Type `/migrate-to-skills` in Agent chat
2. The agent will identify eligible rules and commands and convert them to skills
3. Review the generated skills in `.cursor/skills/`

Rules with `alwaysApply: true` or specific `globs` patterns are not migrated, as they have explicit triggering conditions that differ from skill behavior. User rules are also not migrated since they are not stored on the file system.

#### Learn more

Agent Skills is an open standard. Learn more at [agentskills.io](https://agentskills.io).


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Subagents

*Subagents are specialized AI assistants that Cursor's agent can delegate tasks to. Each subagent operates in its own context window, handles specific types of work, and returns its result to the parent agent. Use subagents to break down complex tasks, do work in parallel, and preserve context in the main conversation.*

**Source:** https://cursor.com/docs/subagents

Subagents are specialized AI assistants that Cursor's agent can delegate tasks to. Each subagent operates in its own context window, handles specific types of work, and returns its result to the parent agent. Use subagents to break down complex tasks, do work in parallel, and preserve context in the main conversation.

You can use subagents in the editor, CLI, and [Cloud Agents](https://cursor.com/docs/cloud-agent.md).

##### Context isolation

Each subagent has its own context window. Long research or exploration tasks don't consume space in your main conversation.

##### Parallel execution

Launch multiple subagents simultaneously. Work on different parts of your codebase without waiting for sequential completion.

##### Specialized expertise

Configure subagents with custom prompts, tool access, and models for domain-specific tasks.

##### Reusability

Define custom subagents and use them across projects.

#### How subagents work

When Agent encounters a complex task, it can launch a subagent automatically. The subagent receives a prompt with all necessary context, works autonomously, and returns a final message with its results.

Subagents start with a clean context. The parent agent includes relevant information in the prompt since subagents don't have access to prior conversation history.

##### Foreground vs background

Subagents run in one of two modes:

| Mode           | Behavior                                                             | Best for                                    |
| :------------- | :------------------------------------------------------------------- | :------------------------------------------ |
| **Foreground** | Blocks until the subagent completes. Returns the result immediately. | Sequential tasks where you need the output. |
| **Background** | Returns immediately. The subagent works independently.               | Long-running tasks or parallel workstreams. |

#### Built-in subagents

Cursor includes three built-in subagents that handle context-heavy operations automatically. These subagents were designed based on analysis of agent conversations where context window limits were hit.

| Subagent    | Purpose                         | Why it's a subagent                                                                                                                            |
| :---------- | :------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| **Explore** | Searches and analyzes codebases | Codebase exploration generates large intermediate output that would bloat the main context. Uses a faster model to run many parallel searches. |
| **Bash**    | Runs series of shell commands   | Command output is often verbose. Isolating it keeps the parent focused on decisions, not logs.                                                 |
| **Browser** | Controls browser via MCP tools  | Browser interactions produce noisy DOM snapshots and screenshots. The subagent filters this down to relevant results.                          |

##### Why these subagents exist

These three operations share common traits: they generate noisy intermediate output, benefit from specialized prompts and tools, and can consume significant context. Running them as subagents solves several problems:

- **Context isolation** — Intermediate output stays in the subagent. The parent only sees the final summary.
- **Model flexibility** — The explore subagent uses a faster model by default. This enables running 10 parallel searches in the time a single main-agent search would take.
- **Specialized configuration** — Each subagent has prompts and tool access tuned for its specific task.
- **Cost efficiency** — Faster models cost less. Isolating token-heavy work in subagents with appropriate model choices reduces overall cost.

You don't need to configure these subagents. Agent uses them automatically when appropriate.

#### When to use subagents

| Use subagents when...                                     | Use skills when...                                      |
| :-------------------------------------------------------- | :------------------------------------------------------ |
| You need context isolation for long research tasks        | The task is single-purpose (generate changelog, format) |
| Running multiple workstreams in parallel                  | You want a quick, repeatable action                     |
| The task requires specialized expertise across many steps | The task completes in one shot                          |
| You want an independent verification of work              | You don't need a separate context window                |

If you find yourself creating a subagent for a simple, single-purpose task like "generate a changelog" or "format imports," consider using a [skill](https://cursor.com/docs/skills.md) instead.

#### Quick start

Agent automatically uses subagents when appropriate. You can also create a custom subagent by asking Agent:

Create a subagent file at .cursor/agents/verifier.md with YAML frontmatter (name, description) followed by the prompt. The verifier subagent should validate completed work, check that implementations are functional, run tests, and report what passed vs what's incomplete.

For more control, create custom subagents manually in your project or user directory.

#### Custom subagents

Define custom subagents to encode specialized knowledge, enforce team standards, or automate repetitive workflows.

##### File locations

| Type                  | Location            | Scope                                                |
| :-------------------- | :------------------ | :--------------------------------------------------- |
| **Project subagents** | `.cursor/agents/`   | Current project only                                 |
|                       | `.claude/agents/`   | Current project only (Claude compatibility)          |
|                       | `.codex/agents/`    | Current project only (Codex compatibility)           |
| **User subagents**    | `~/.cursor/agents/` | All projects for current user                        |
|                       | `~/.claude/agents/` | All projects for current user (Claude compatibility) |
|                       | `~/.codex/agents/`  | All projects for current user (Codex compatibility)  |

Project subagents take precedence when names conflict. When multiple locations contain subagents with the same name, `.cursor/` takes precedence over `.claude/` or `.codex/`.

##### File format

Each subagent is a markdown file with YAML frontmatter:

```markdown
---
name: security-auditor
description: Security specialist. Use when implementing auth, payments, or handling sensitive data.
model: inherit
readonly: true
---

You are a security expert auditing code for vulnerabilities.

When invoked:
1. Identify security-sensitive code paths
2. Check for common vulnerabilities (injection, XSS, auth bypass)
3. Verify secrets are not hardcoded
4. Review input validation and sanitization

Report findings by severity:
- Critical (must fix before deploy)
- High (fix soon)
- Medium (address when possible)
```

##### Configuration fields

| Field           | Type    | Required | Default               | Description                                                                                                                          |
| :-------------- | :------ | :------- | :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `name`          | string  | No       | Derived from filename | Display name and identifier. Use lowercase letters and hyphens.                                                                      |
| `description`   | string  | No       | —                     | Short description shown in Task tool hints. Agent reads this to decide delegation.                                                   |
| `model`         | string  | No       | `inherit`             | Model to use: `inherit` or a specific model ID. See [model configuration](https://cursor.com/docs/subagents.md#model-configuration). |
| `readonly`      | boolean | No       | `false`               | If `true`, the subagent runs with restricted write permissions (no file edits, no state-changing shell commands).                    |
| `is_background` | boolean | No       | `false`               | If `true`, the subagent runs in the background without blocking the parent.                                                          |

##### Model configuration

The `model` field controls which model a subagent uses. There are two options:

| Value               | Behavior                                                                                                                                                              |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `inherit`           | Uses the same model as the parent agent. This is the default.                                                                                                         |
| A specific model ID | Uses the exact model you specify, such as `composer-2` or `gpt-5.6-sol`. See the [models reference](https://cursor.com/docs/models-and-pricing.md) for available IDs. |

Choose `inherit` when the subagent needs the same reasoning power as the parent. Use a specific model ID when you need a particular model's capabilities regardless of what the parent uses.

###### Model parameters

Append square brackets to a model ID to set per-model options like speed, reasoning effort, and context window. Write options as `id=value` pairs, and separate multiple options with commas.

| Example                                     | Behavior                                                                                 |
| :------------------------------------------ | :--------------------------------------------------------------------------------------- |
| `composer-2.5[]`                            | Pins the base model. Empty brackets select the standard variant instead of the fast one. |
| `composer-2.5[fast=false]`                  | Selects the standard (non-fast) variant explicitly.                                      |
| `claude-opus-4-8[effort=high]`              | Sets reasoning effort to `high`.                                                         |
| `claude-opus-4-8[context=300k]`             | Sets the context window to 300k tokens.                                                  |
| `claude-opus-4-8[effort=high,context=300k]` | Combines options.                                                                        |

Available options depend on the model, and use the same `id=value` pairs as the SDK's [model parameters](https://cursor.com/docs/sdk/typescript.md#model-parameters).

```markdown
---
name: planner
description: Plans complex changes before implementation.
model: claude-opus-4-8[effort=high]
---

Break the task into a clear, ordered implementation plan.
```

###### When the configured model won't be used

Cursor honors the `model` field in your subagent frontmatter unless one of these conditions applies:

- **Team admin restrictions** — Your organization's admin has blocked the specified model.
- **Legacy Max Mode setting** — On a legacy request-based plan, the model requires [Max Mode](https://cursor.com/help/ai-features/max-mode.md) and you don't have it enabled.
- **Plan limitations** — The model isn't available on your current plan.

In these cases, Cursor falls back to a compatible model. If you're seeing unexpected model behavior, check your plan and model settings.

```markdown
---
name: code-reviewer
description: Reviews code for correctness and style.
model: inherit
---

Review the code changes for bugs, style issues, and edge cases.
```

```markdown
---
name: search-agent
description: Searches the codebase for relevant files and symbols.
model: inherit
---

Search the codebase and return relevant file paths and code snippets.
```

```markdown
---
name: reasoning-agent
description: Handles complex architectural decisions.
model: gpt-5.6-sol
---

Analyze the architecture and recommend changes with detailed reasoning.
```

#### Using subagents

##### Automatic delegation

Agent proactively delegates tasks based on:

- The task complexity and scope
- Custom subagent descriptions in your project
- Current context and available tools

Include phrases like "use proactively" or "always use for" in your description field to encourage automatic delegation.

##### Explicit invocation

Request a specific subagent by using the `/name` syntax in your prompt:

```text
> /verifier confirm the auth flow is complete
> /debugger investigate this error
> /security-auditor review the payment module
```

You can also invoke subagents by mentioning them naturally:

```text
> Use the verifier subagent to confirm the auth flow is complete
> Have the debugger subagent investigate this error
> Run the security-auditor subagent on the payment module
```

##### Parallel execution

Launch multiple subagents concurrently for maximum throughput:

```text
> Review the API changes and update the documentation in parallel
```

Agent sends multiple Task tool calls in a single message, so subagents run simultaneously.

#### Cloud subagents

From a local agent session, you can hand off work to a cloud subagent that runs on its own VM and branch. Your local workspace stays clean and responsive while long-running or parallel work happens in the cloud. The parent agent keeps running locally or in the cloud without interruption. Cloud subagents run from the [Agents Window](https://cursor.com/docs/agent/agents-window.md) in the Cursor desktop app.

##### Start a cloud subagent with /in-cloud

Type `/in-cloud` and the next task you submit runs as a cloud subagent. It spins up its own VM and branch to work on the task.

This is useful for isolating long-running or parallel work, such as fixing CI, investigating an issue, or exploring a codebase while you keep working locally.

##### Babysit a PR with /babysit

Ask a cloud subagent to babysit a pull request with `/babysit` or by clicking the quick-action pill. The cloud agent iterates remotely to prepare the PR for merge without tying up your local session.

Cloud subagents use the [environment](https://cursor.com/docs/cloud-agent/setup.md) configured for your repo and follow the same model and capability rules as other [Cloud Agents](https://cursor.com/docs/cloud-agent.md). Because they run on a cloud VM, their [MCP servers](https://cursor.com/docs/cloud-agent/capabilities.md#mcp-tools) come from your team's configuration at [cursor.com/agents](https://cursor.com/agents), not from your local session.

#### Resuming subagents

Subagents can be resumed to continue previous conversations. This is useful for long-running tasks that span multiple invocations.

Each subagent execution returns an agent ID. Pass this ID to resume the subagent with full context preserved:

```text
> Resume agent abc123 and analyze the remaining test failures
```

Background subagents write their state as they run. You can resume a subagent after it completes to continue the conversation with preserved context.

#### Common patterns

##### Verification agent

A verification agent independently validates whether claimed work was actually completed. This addresses a common issue where AI marks tasks as done but implementations are incomplete or broken.

```markdown
---
name: verifier
description: Validates completed work. Use after tasks are marked done to confirm implementations are functional.
---

You are a skeptical validator. Your job is to verify that work claimed as complete actually works.

When invoked:
1. Identify what was claimed to be completed
2. Check that the implementation exists and is functional
3. Run relevant tests or verification steps
4. Look for edge cases that may have been missed

Be thorough and skeptical. Report:
- What was verified and passed
- What was claimed but incomplete or broken
- Specific issues that need to be addressed

Do not accept claims at face value. Test everything.
```

Create a subagent file at .cursor/agents/verifier.md with YAML frontmatter containing name and description. The description should be 'Validates completed work. Use after tasks are marked done to confirm implementations are functional.' The prompt body should instruct it to be skeptical, verify implementations actually work by running tests, and look for edge cases.

This pattern is useful for:

- Validating that features work end-to-end before marking tickets complete
- Catching partially implemented functionality
- Ensuring tests actually pass (not just that test files exist)

##### Orchestrator pattern

For complex workflows, a parent agent can coordinate multiple specialist subagents in sequence:

1. **Planner** analyzes requirements and creates a technical plan
2. **Implementer** builds the feature based on the plan
3. **Verifier** confirms the implementation matches requirements

Each handoff includes structured output so the next agent has clear context.

#### Example subagents

##### Debugger

```markdown
---
name: debugger
description: Debugging specialist for errors and test failures. Use when encountering issues.
---

You are an expert debugger specializing in root cause analysis.

When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Implement minimal fix
5. Verify solution works

For each issue, provide:
- Root cause explanation
- Evidence supporting the diagnosis
- Specific code fix
- Testing approach

Focus on fixing the underlying issue, not symptoms.
```

Create a subagent file at .cursor/agents/debugger.md with YAML frontmatter containing name and description. The debugger subagent should specialize in root cause analysis: capture stack traces, identify reproduction steps, isolate failures, implement minimal fixes, and verify solutions.

##### Test runner

```markdown
---
name: test-runner
description: Test automation expert. Use proactively to run tests and fix failures.
---

You are a test automation expert.

When you see code changes, proactively run appropriate tests.

If tests fail:
1. Analyze the failure output
2. Identify the root cause
3. Fix the issue while preserving test intent
4. Re-run to verify

Report test results with:
- Number of tests passed/failed
- Summary of any failures
- Changes made to fix issues
```

Create a subagent file at .cursor/agents/test-runner.md with YAML frontmatter containing name and description (mentioning 'Use proactively'). The test-runner subagent should proactively run tests when it sees code changes, analyze failures, fix issues while preserving test intent, and report results.

#### Best practices

- **Write focused subagents** — Each subagent should have a single, clear responsibility. Avoid generic "helper" agents.
- **Invest in descriptions** — The `description` field determines when Agent delegates to your subagent. Spend time refining it. Test by making prompts and checking if the right subagent gets triggered.
- **Keep prompts concise** — Long, rambling prompts dilute focus. Be specific and direct.
- **Add subagents to version control** — Check `.cursor/agents/` into your repository so the team benefits.
- **Start with Agent-generated agents** — Let Agent help you draft the initial configuration, then customize.
- **Use hooks for file output** — If you need subagents to produce structured output files, consider using [hooks](https://cursor.com/docs/hooks.md) to process and save their results consistently.

##### Anti-patterns to avoid

**Don't create dozens of generic subagents.** Having 50+ subagents with vague instructions like "helps with coding" is ineffective. Agent won't know when to use them, and you'll waste time maintaining them.

- **Vague descriptions** — "Use for general tasks" gives Agent no signal about when to delegate. Be specific: "Use when implementing authentication flows with OAuth providers."
- **Overly long prompts** — A 2,000-word prompt doesn't make a subagent smarter. It makes it slower and harder to maintain.
- **Duplicating slash commands** — If a task is single-purpose and doesn't need context isolation, use a [skill](https://cursor.com/docs/skills.md) or [command](https://cursor.com/docs/customize-cursor.md#extension-components) instead.
- **Too many subagents** — Start with 2-3 focused subagents. Add more only when you have clear, distinct use cases.

#### Managing subagents

##### Creating subagents

The easiest way to create a subagent is to ask Agent to create one for you:

Create a subagent file at .cursor/agents/security-reviewer.md with YAML frontmatter containing name and description. The security-reviewer subagent should check code for common vulnerabilities like injection, XSS, and hardcoded secrets.

You can also create subagents manually by adding markdown files to `.cursor/agents/` (project) or `~/.cursor/agents/` (user).

##### Viewing subagents

Agent includes all custom subagents in its available tools. You can see which subagents are configured by checking the `.cursor/agents/` directory in your project.

#### Performance and cost

Subagents have trade-offs. Understanding them helps you decide when to use them.

| Benefit            | Trade-off                                                     |
| :----------------- | :------------------------------------------------------------ |
| Context isolation  | Startup overhead (each subagent gathers its own context)      |
| Parallel execution | Higher token usage (multiple contexts running simultaneously) |
| Specialized focus  | Latency (may be slower than main agent for simple tasks)      |

##### Token and cost considerations

- **Subagents consume tokens independently** — Each subagent has its own context window and token usage. Running five subagents in parallel uses roughly five times the tokens of a single agent.
- **Evaluate the overhead** — For quick, simple tasks, the main agent is often faster. Subagents shine for complex, long-running, or parallel work.
- **Subagents can be slower** — The benefit is context isolation, not speed. A subagent doing a simple task may be slower than the main agent because it starts fresh.

#### FAQ

##### What are the built-in subagents?

Cursor includes three built-in subagents: `explore` for codebase search, `bash` for running shell commands, and `browser` for browser automation via MCP. These handle context-heavy operations automatically. You don't need to configure them.

##### Can subagents launch other subagents?

Yes, within a nesting limit. Since Cursor 2.5, subagents can launch child subagents to create a tree of coordinated work. The main agent and its direct subagents can launch subagents, but a subagent launched by another subagent can't launch further ones.
Nested launches also need Task tool access in the current mode, and hooks or tool policies can block spawning.

##### How do I see what a subagent is doing?

Background subagents write output to `~/.cursor/subagents/`. The parent agent can read these files to check progress.

##### What happens if a subagent fails?

The subagent returns an error status to the parent agent. The parent can retry, resume with additional context, or handle the failure differently.

##### Can I use MCP tools in subagents?

Yes. Subagents inherit all tools from the parent, including MCP tools from configured servers. [Cloud subagents](https://cursor.com/docs/subagents.md#cloud-subagents) are the exception: they run on a cloud VM and use the MCP servers configured for your team at [cursor.com/agents](https://cursor.com/agents), not the servers from your local session.

##### How do I debug a misbehaving subagent?

Check the subagent's description and prompt. Ensure the instructions are specific and unambiguous. You can also test the subagent by invoking it explicitly with a simple task.

##### Why is my subagent using a different model?

Cursor overrides the configured model when your team admin blocks it, your plan doesn't include it, or a legacy request-based plan requires [Max Mode](https://cursor.com/help/ai-features/max-mode.md) and you don't have it enabled. On legacy request-based plans without Max Mode, subagents run using Composer regardless of any `model` configuration. If your team admin has blocked Composer, subagents can run only when Max Mode is enabled. On usage-based plans and legacy request-based plans with Max Mode, subagents default to the parent model. See [model configuration](https://cursor.com/docs/subagents.md#model-configuration) for details.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Hooks

*Hooks let you observe, control, and extend the agent loop using custom scripts. Define hooks in `hooks.json` files at the project or user level, or install them through plugins from **Customize**. Hooks are spawned processes that communicate over stdio using JSON in both directions. They run before or after defined stages of the agent loop and can observe, block, or modify behavior.*

**Source:** https://cursor.com/docs/hooks

Hooks let you observe, control, and extend the agent loop using custom scripts. Define hooks in `hooks.json` files at the project or user level, or install them through plugins from **Customize**. Hooks are spawned processes that communicate over stdio using JSON in both directions. They run before or after defined stages of the agent loop and can observe, block, or modify behavior.

[Media](https://cursor.com/docs-static/images/agent/hooks.mp4)

With hooks, you can:

- Run formatters after edits
- Add analytics for events
- Scan for PII or secrets
- Gate risky operations (e.g., SQL writes)
- Control subagent (Task tool) execution
- Inject context at session start

Looking for ready-to-use integrations? See [Partner Integrations](https://cursor.com/docs/hooks.md#partner-integrations) for security, governance, and secrets management solutions from our ecosystem partners.

Cursor supports loading hooks from third-party tools like Claude Code. See [Third Party Hooks](https://cursor.com/docs/reference/third-party-hooks.md) for details on compatibility and configuration.

#### Hook categories

Hooks fall into three categories based on what triggers them:

**Agent hooks (Cmd+K/Agent Chat)** fire during an agent session:

- `sessionStart` / `sessionEnd` - Session lifecycle management
- `preToolUse` / `postToolUse` / `postToolUseFailure` - Generic tool use hooks (fires for all tools)
- `subagentStart` / `subagentStop` - Subagent (Task tool) lifecycle
- `beforeShellExecution` / `afterShellExecution` - Control shell commands
- `beforeMCPExecution` / `afterMCPExecution` - Control MCP tool usage
- `beforeReadFile` / `afterFileEdit` - Control file access and edits
- `beforeSubmitPrompt` - Validate prompts before submission
- `preCompact` - Observe context window compaction
- `stop` - Handle agent completion
- `afterAgentResponse` / `afterAgentThought` - Track agent responses

**Tab hooks (inline completions)** fire for autonomous Tab operations:

- `beforeTabFileRead` - Control file access for Tab completions
- `afterTabFileEdit` - Post-process Tab edits

**App lifecycle hooks** fire outside any agent session:

- `workspaceOpen` - Fires when Cursor opens a workspace and on every workspace folder change. Can return additional plugin paths to load for the current workspace.

These separate hook surfaces let you apply different policies to autonomous Tab operations, user-directed Agent operations, and workspace startup.

#### Cloud agent support

Cloud agents run command-based hooks from your repository. If you have hooks defined in `.cursor/hooks.json` at the root of your project, cloud agents pick them up and run them during their work.

On Enterprise plans, cloud agents also run team hooks and enterprise-managed hooks configured through the [web dashboard](https://cursor.com/dashboard/team-content?section=hooks).

Cloud agents sometimes begin in a read-only environment for early exploratory turns. Hooks do not run during those turns. They start once the agent has a writable environment.

##### Supported hooks

The following hooks run in cloud agents:

| Hook                   | Supported |
| ---------------------- | --------- |
| `beforeShellExecution` | Yes       |
| `afterShellExecution`  | Yes       |
| `beforeReadFile`       | Yes       |
| `afterFileEdit`        | Yes       |
| `preToolUse`           | Yes       |
| `postToolUse`          | Yes       |
| `postToolUseFailure`   | Yes       |
| `subagentStart`        | Yes       |
| `subagentStop`         | Yes       |
| `beforeSubmitPrompt`   | Yes       |
| `preCompact`           | Yes       |
| `afterAgentResponse`   | Yes       |
| `afterAgentThought`    | Yes       |
| `stop`                 | Yes       |

##### Hooks not available in cloud agents

Some hooks don't apply to cloud agents due to differences in the execution environment:

| Hook                                       | Reason                                                                                                                                                                                                   |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sessionStart`                             | Deferred while cloud agents can still start in a read-only environment. Hooks don't load there, so a cloud `sessionStart` would fire too late (after the first write) rather than at true session start. |
| `sessionEnd`                               | Cloud agents have no editor-lifetime session boundary. `sessionEnd` is tied to the IDE session, not a cloud agent chat.                                                                                  |
| `beforeMCPExecution` / `afterMCPExecution` | Deferred while cloud agents can still start in a read-only environment, where hooks don't load and MCP hook timing is unclear.                                                                           |
| `beforeTabFileRead` / `afterTabFileEdit`   | Tab completions are an IDE feature and don't run in cloud agents.                                                                                                                                        |
| `workspaceOpen`                            | This is an IDE lifecycle hook and doesn't apply to cloud agents.                                                                                                                                         |

##### Configuration sources

Cloud agents load hooks from these sources:

- **Project hooks** (`.cursor/hooks.json` in your repo): Loaded and run during cloud agent work.
- **Team hooks** (Enterprise): Distributed from the dashboard and run in cloud agents.
- **Enterprise hooks** (Enterprise): System-wide managed hooks run in cloud agents.

User-level hooks (`~/.cursor/hooks.json`) are not available in cloud agents. Cloud agent VMs don't have access to your local home directory configuration.

##### Execution type limits

Cloud agents run **command-based hooks** only. Prompt-based hooks require authentication wiring between the hook and the agent loop, which isn't available in the cloud execution environment.

#### Quickstart

Create a `hooks.json` file. You can create it at the project level (`<project>/.cursor/hooks.json`) or in your home directory (`~/.cursor/hooks.json`). Project-level hooks apply only to that specific project, while home directory hooks apply globally.

##### User hooks (\~/.cursor/)

For user-level hooks that apply globally, create `~/.cursor/hooks.json`:

```json
{
  "version": 1,
  "hooks": {
    "afterFileEdit": [{ "command": "./hooks/format.sh" }]
  }
}
```

Create your hook script at `~/.cursor/hooks/format.sh`:

```bash
#!/bin/bash
# Read input, do something, exit 0
cat > /dev/null
exit 0
```

Make it executable:

```bash
chmod +x ~/.cursor/hooks/format.sh
```

##### Project hooks (.cursor/)

For project-level hooks that apply to a specific repository, create `<project>/.cursor/hooks.json`:

```json
{
  "version": 1,
  "hooks": {
    "afterFileEdit": [{ "command": ".cursor/hooks/format.sh" }]
  }
}
```

Note: Project hooks run from the **project root**, so use `.cursor/hooks/format.sh` (not `./hooks/format.sh`).

Create your hook script at `<project>/.cursor/hooks/format.sh`:

```bash
#!/bin/bash
# Read input, do something, exit 0
cat > /dev/null
exit 0
```

Make it executable:

```bash
chmod +x .cursor/hooks/format.sh
```

Cursor watches hooks config files and reloads them automatically. Your hook runs after every file edit.

#### Hook Types

Hooks support two execution types: command-based (default) and prompt-based (LLM-evaluated).

##### Command-Based Hooks

Command hooks execute shell scripts that receive JSON input via stdin and return JSON output via stdout.

```json
{
  "hooks": {
    "beforeShellExecution": [
      {
        "command": "./scripts/approve-network.sh",
        "timeout": 30,
        "matcher": "curl|wget|nc"
      }
    ]
  }
}
```

**Exit code behavior:**

- Exit code `0` - Hook succeeded, use the JSON output
- Exit code `2` - Block the action (equivalent to returning `permission: "deny"`)
- Other exit codes - Hook failed, action proceeds (fail-open by default)

##### Prompt-Based Hooks

Prompt hooks use an LLM to evaluate a natural language condition. They're useful for policy enforcement without writing custom scripts.

```json
{
  "hooks": {
    "beforeShellExecution": [
      {
        "type": "prompt",
        "prompt": "Does this command look safe to execute? Only allow read-only operations.",
        "timeout": 10
      }
    ]
  }
}
```

**Features:**

- Returns structured `{ ok: boolean, reason?: string }` response
- Uses a fast model for quick evaluation
- `$ARGUMENTS` placeholder is auto-replaced with hook input JSON
- If `$ARGUMENTS` is absent, hook input is auto-appended
- Optional `model` field to override the default LLM model

#### Examples

The examples below use `./hooks/...` paths, which work for **user hooks** (`~/.cursor/hooks.json`) where scripts run from `~/.cursor/`. For **project hooks** (`<project>/.cursor/hooks.json`), use `.cursor/hooks/...` paths instead since scripts run from the project root.

```json title="hooks.json"
{
  "version": 1,
  "hooks": {
    "sessionStart": [
      {
        "command": "./hooks/session-init.sh"
      }
    ],
    "sessionEnd": [
      {
        "command": "./hooks/audit.sh"
      }
    ],
    "beforeShellExecution": [
      {
        "command": "./hooks/audit.sh"
      },
      {
        "command": "./hooks/block-git.sh"
      }
    ],
    "beforeMCPExecution": [
      {
        "command": "./hooks/audit.sh"
      }
    ],
    "afterShellExecution": [
      {
        "command": "./hooks/audit.sh"
      }
    ],
    "afterMCPExecution": [
      {
        "command": "./hooks/audit.sh"
      }
    ],
    "afterFileEdit": [
      {
        "command": "./hooks/audit.sh"
      }
    ],
    "beforeSubmitPrompt": [
      {
        "command": "./hooks/audit.sh"
      }
    ],
    "preCompact": [
      {
        "command": "./hooks/audit.sh"
      }
    ],
    "stop": [
      {
        "command": "./hooks/audit.sh"
      }
    ],
    "beforeTabFileRead": [
      {
        "command": "./hooks/redact-secrets-tab.sh"
      }
    ],
    "afterTabFileEdit": [
      {
        "command": "./hooks/format-tab.sh"
      }
    ]
  }
}
```

```sh title="audit.sh"
#!/bin/bash

# audit.sh - Hook script that writes all JSON input to /tmp/agent-audit.log
# This script is designed to be called by Cursor's hooks system for auditing purposes

# Read JSON input from stdin
json_input=$(cat)

# Create timestamp for the log entry
timestamp=$(date '+%Y-%m-%d %H:%M:%S')

# Create the log directory if it doesn't exist
mkdir -p "$(dirname /tmp/agent-audit.log)"

# Write the timestamped JSON entry to the audit log
echo "[$timestamp] $json_input" >> /tmp/agent-audit.log

# Exit successfully
exit 0
```

```sh title="block-git.sh"
#!/bin/bash

# Hook to block git commands and redirect to gh tool usage
# This hook implements the beforeShellExecution hook from the Cursor Hooks Spec

# Initialize debug logging
echo "Hook execution started" >> /tmp/hooks.log

# Read JSON input from stdin
input=$(cat)
echo "Received input: $input" >> /tmp/hooks.log

# Parse the command from the JSON input
command=$(echo "$input" | jq -r '.command // empty')
echo "Parsed command: '$command'" >> /tmp/hooks.log

# Check if the command contains 'git' or 'gh'
if [[ "$command" =~ git[[:space:]] ]] || [[ "$command" == "git" ]]; then
    echo "Git command detected - blocking: '$command'" >> /tmp/hooks.log
    # Block the git command and provide guidance to use gh tool instead
    cat << EOF
{
  "continue": true,
  "permission": "deny",
  "user_message": "Git command blocked. Please use the GitHub CLI (gh) tool instead.",
  "agent_message": "The git command '$command' has been blocked by a hook. Instead of using raw git commands, please use the 'gh' tool which provides better integration with GitHub and follows best practices. For example:\n- Instead of 'git clone', use 'gh repo clone'\n- Instead of 'git push', use 'gh repo sync' or the appropriate gh command\n- For other git operations, check if there's an equivalent gh command or use the GitHub web interface\n\nThis helps maintain consistency and leverages GitHub's enhanced tooling."
}
EOF
elif [[ "$command" =~ gh[[:space:]] ]] || [[ "$command" == "gh" ]]; then
    echo "GitHub CLI command detected - asking for permission: '$command'" >> /tmp/hooks.log
    # Ask for permission for gh commands
    cat << EOF
{
  "continue": true,
  "permission": "ask",
  "user_message": "GitHub CLI command requires permission: $command",
  "agent_message": "The command '$command' uses the GitHub CLI (gh) which can interact with your GitHub repositories and account. Please review and approve this command if you want to proceed."
}
EOF
else
    echo "Non-git/non-gh command detected - allowing: '$command'" >> /tmp/hooks.log
    # Allow non-git/non-gh commands
    cat << EOF
{
  "continue": true,
  "permission": "allow"
}
EOF
fi
```

##### TypeScript stop automation hook

Choose TypeScript when you need typed JSON, durable file I/O, and HTTP calls in the same hook. This Bun-powered `stop` hook tracks per-conversation failure counts on disk, forwards structured telemetry to an internal API, and can automatically schedule a retry when the agent fails twice in a row.

```json title="hooks.json"
{
  "version": 1,
  "hooks": {
    "stop": [
      {
        "command": "bun run .cursor/hooks/track-stop.ts --stop"
      }
    ]
  }
}
```

```ts title=".cursor/hooks/track-stop.ts"
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { stdin } from 'bun';

type StopHookInput = {
  conversation_id: string;
  generation_id: string;
  model: string;
  model_id?: string;
  model_params?: Array<{ id: string; value: string }>;
  status: 'completed' | 'aborted' | 'error';
  loop_count: number;
};

type StopHookOutput = {
  followup_message?: string;
};

type MetricsEntry = {
  lastStatus: StopHookInput['status'];
  errorCount: number;
  lastUpdatedIso: string;
};

type MetricsStore = Record<string, MetricsEntry>;

const STATE_DIR = '.cursor/hooks/state';
const METRICS_PATH = `${STATE_DIR}/agent-metrics.json`;
const TELEMETRY_URL = Bun.env.AGENT_TELEMETRY_URL;

async function parseHookInput<T>(): Promise<T> {
  const text = await stdin.text();
  return JSON.parse(text) as T;
}

async function readMetrics(): Promise<MetricsStore> {
  try {
    return JSON.parse(await readFile(METRICS_PATH, 'utf8')) as MetricsStore;
  } catch {
    return {};
  }
}

async function writeMetrics(store: MetricsStore) {
  await mkdir(STATE_DIR, { recursive: true });
  await writeFile(METRICS_PATH, JSON.stringify(store, null, 2), 'utf8');
}

async function sendTelemetry(payload: StopHookInput, entry: MetricsEntry) {
  if (!TELEMETRY_URL) return;
  await fetch(TELEMETRY_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      conversationId: payload.conversation_id,
      generationId: payload.generation_id,
      model: payload.model,
      modelId: payload.model_id,
      modelParams: payload.model_params,
      status: payload.status,
      errorCount: entry.errorCount,
      loopCount: payload.loop_count,
      timestamp: entry.lastUpdatedIso
    })
  });
}

async function main() {
  const payload = await parseHookInput<StopHookInput>();
  const metrics = await readMetrics();
  const entry =
    metrics[payload.conversation_id] ?? {
      lastStatus: payload.status,
      errorCount: 0,
      lastUpdatedIso: ''
    };

  entry.lastStatus = payload.status;
  entry.lastUpdatedIso = new Date().toISOString();
  entry.errorCount = payload.status === 'error' ? entry.errorCount + 1 : 0;

  metrics[payload.conversation_id] = entry;
  await writeMetrics(metrics);
  await sendTelemetry(payload, entry);

  const response: StopHookOutput = {};
  if (entry.errorCount >= 2 && payload.loop_count < 4) {
    response.followup_message =
      'Automated retry triggered after two failures. Double-check credentials before running again.';
  }

  process.stdout.write(JSON.stringify(response) + '\n');
}

main().catch(error => {
  console.error('[stop hook] failed', error);
  process.stdout.write('{}\n');
});
```

Set `AGENT_TELEMETRY_URL` to the internal endpoint that should receive run summaries.

##### Python manifest guard hook

Python shines when you need rich parsing libraries. This hook uses `pyyaml` to inspect Kubernetes manifests before `kubectl apply` runs; Bash would struggle to parse multi-document YAML safely.

```json title="hooks.json"
{
  "version": 1,
  "hooks": {
    "beforeShellExecution": [
      {
        "command": "python3 .cursor/hooks/kube_guard.py"
      }
    ]
  }
}
```

```python title=".cursor/hooks/kube_guard.py"
#!/usr/bin/env python3
import json
import shlex
import sys
from pathlib import Path

import yaml

SENSITIVE_NAMESPACES = {"prod", "production"}

def main() -> None:
    payload = json.load(sys.stdin)
    command = payload.get("command", "")
    cwd = Path(payload.get("cwd") or ".")
    response = {"continue": True, "permission": "allow"}

    try:
        args = shlex.split(command)
    except ValueError:
        print(json.dumps(response))
        return

    if len(args) < 2 or args[0] != "kubectl" or args[1] != "apply" or "-f" not in args:
        print(json.dumps(response))
        return

    f_index = args.index("-f")
    if f_index + 1 >= len(args):
        print(json.dumps(response))
        return

    manifest_arg = args[f_index + 1]
    manifest_path = (cwd / manifest_arg).resolve()

    if not manifest_path.exists():
        print(json.dumps(response))
        return

    cli_namespace = None
    for i, arg in enumerate(args):
        if arg in ("-n", "--namespace") and i + 1 < len(args):
            cli_namespace = args[i + 1]
        elif arg.startswith("--namespace="):
            cli_namespace = arg.split("=", 1)[1]
        elif arg.startswith("-n="):
            cli_namespace = arg.split("=", 1)[1]

    try:
        documents = list(yaml.safe_load_all(manifest_path.read_text()))
    except (OSError, yaml.YAMLError) as exc:
        sys.stderr.write(f"Failed to read/parse {manifest_path}: {exc}\n")
        print(json.dumps(response))
        return

    if cli_namespace in SENSITIVE_NAMESPACES or any(
        (doc or {}).get("metadata", {}).get("namespace") in SENSITIVE_NAMESPACES
        for doc in documents
    ):
        response.update(
            {
                "permission": "ask",
                "user_message": "kubectl apply to prod requires manual approval.",
                "agent_message": f"{manifest_path.name} includes protected namespaces; confirm with your team before continuing.",
            }
        )

    print(json.dumps(response))

if __name__ == "__main__":
    main()
```

Install PyYAML (for example, `pip install pyyaml`) wherever your hook scripts run so the parser import succeeds.

#### Partner Integrations

We partner with ecosystem vendors who have built hooks support with Cursor. These integrations cover security scanning, governance, secrets management, and more.

##### MCP governance and visibility

| Partner                                                                                 | Description                                                                                                                                   |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| [MintMCP](https://www.mintmcp.com/blog/mcp-governance-cursor-hooks)                     | Build a complete inventory of MCP servers, monitor tool usage patterns, and scan responses for sensitive data before it reaches the AI model. |
| [Oasis Security](https://www.oasis.security/blog/cursor-oasis-governing-agentic-access) | Enforce least-privilege policies on AI agent actions and maintain full audit trails across enterprise systems.                                |
| [Runlayer](https://www.runlayer.com/blog/cursor-hooks)                                  | Wrap MCP tools and integrate with their MCP broker for centralized control and visibility over agent-to-tool interactions.                    |

##### Code security and best practices

| Partner                                                          | Description                                                                                                                             |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| [Corridor](https://corridor.dev/blog/corridor-cursor-hooks/)     | Get real-time feedback on code implementation and security design decisions as code is being written.                                   |
| [Semgrep](https://semgrep.dev/blog/2025/cursor-hooks-mcp-server) | Automatically scan AI-generated code for vulnerabilities with real-time feedback to regenerate code until security issues are resolved. |

##### Dependency security

| Partner                                                                                                             | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| [Endor Labs](https://www.endorlabs.com/learn/bringing-malware-detection-into-ai-coding-workflows-with-cursor-hooks) | Intercept package installations and scan for malicious dependencies, preventing supply chain attacks before they enter your codebase. |

##### Agent security and safety

| Partner                                                          | Description                                                                                                                             |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| [Snyk](https://snyk.io/blog/evo-agent-guard-cursor-integration/) | Review agent actions in real-time with Evo Agent Guard, detecting and preventing issues like prompt injection and dangerous tool calls. |

##### Secrets management

| Partner                                                                 | Description                                                                                                                                                                               |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [1Password](https://marketplace.1password.com/integration/cursor-hooks) | Validate that environment files from 1Password Environments are properly mounted before shell commands execute, enabling just-in-time secrets access without writing credentials to disk. |

For more details about our hooks partners, see the [Hooks for security and platform teams](https://cursor.com/blog/hooks-partners) blog post.

#### Configuration

Define hooks in a `hooks.json` file. Configuration can exist at multiple levels. All matching hooks from every source run; when responses conflict, higher-priority sources take precedence during merge:

```sh
~/.cursor/
├── hooks.json
└── hooks/
    ├── audit.sh
    └── block-git.sh
```

- **Enterprise** (MDM-managed, system-wide):
  - macOS: `/Library/Application Support/Cursor/hooks.json`
  - Linux/WSL: `/etc/cursor/hooks.json`
  - Windows: `C:\\ProgramData\\Cursor\\hooks.json`
- **Team** (Cloud-distributed, enterprise only):
  - Configured in the [web dashboard](https://cursor.com/dashboard/team-content?section=hooks) and synced to all team members automatically
- **Project** (Project-specific):
  - `<project-root>/.cursor/hooks.json`
  - Project hooks run in any trusted workspace and are checked into version control with your project
- **User** (User-specific):
  - `~/.cursor/hooks.json`

Priority order (highest to lowest): Enterprise → Team → Project → User

The `hooks` object maps hook names to arrays of hook definitions. Each definition currently supports a `command` property that can be a shell string, an absolute path, or a relative path. The working directory depends on the hook source:

- **Project hooks** (`.cursor/hooks.json` in a repository): Run from the **project root**
- **User hooks** (`~/.cursor/hooks.json`): Run from `~/.cursor/`
- **Enterprise hooks** (system-wide config): Run from the enterprise config directory
- **Team hooks** (cloud-distributed): Run from the managed hooks directory

For project hooks, use paths like `.cursor/hooks/script.sh` (relative to project root), not `./hooks/script.sh` (which would look for `<project>/hooks/script.sh`).

##### Configuration file

This example shows a user-level hooks file (`~/.cursor/hooks.json`). For project-level hooks, change paths like `./hooks/script.sh` to `.cursor/hooks/script.sh`:

```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [{ "command": "./session-init.sh" }],
    "sessionEnd": [{ "command": "./audit.sh" }],
    "preToolUse": [
      {
        "command": "./hooks/validate-tool.sh",
        "matcher": "Shell|Read|Write"
      }
    ],
    "postToolUse": [{ "command": "./hooks/audit-tool.sh" }],
    "subagentStart": [{ "command": "./hooks/validate-subagent.sh" }],
    "subagentStop": [{ "command": "./hooks/audit-subagent.sh" }],
    "beforeShellExecution": [{ "command": "./script.sh" }],
    "afterShellExecution": [{ "command": "./script.sh" }],
    "afterMCPExecution": [{ "command": "./script.sh" }],
    "afterFileEdit": [{ "command": "./format.sh" }],
    "preCompact": [{ "command": "./audit.sh" }],
    "stop": [{ "command": "./audit.sh", "loop_limit": 10 }],
    "beforeTabFileRead": [{ "command": "./redact-secrets-tab.sh" }],
    "afterTabFileEdit": [{ "command": "./format-tab.sh" }],
    "workspaceOpen": [{ "command": "./register-workspace-plugins.sh" }]
  }
}
```

The Agent hooks (`sessionStart`, `sessionEnd`, `preToolUse`, `postToolUse`, `postToolUseFailure`, `subagentStart`, `subagentStop`, `beforeShellExecution`, `afterShellExecution`, `beforeMCPExecution`, `afterMCPExecution`, `beforeReadFile`, `afterFileEdit`, `beforeSubmitPrompt`, `preCompact`, `stop`, `afterAgentResponse`, `afterAgentThought`) apply to Cmd+K and Agent Chat operations. The Tab hooks (`beforeTabFileRead`, `afterTabFileEdit`) apply specifically to inline Tab completions. The app lifecycle hook (`workspaceOpen`) fires when a workspace opens and on workspace folder changes, independent of any agent session.

##### Global Configuration Options

| Option    | Type   | Default | Description           |
| --------- | ------ | ------- | --------------------- |
| `version` | number | `1`     | Config schema version |

##### Per-Script Configuration Options

| Option       | Type                      | Default          | Description                                                                                                                                    |
| ------------ | ------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `command`    | string                    | required         | Script path or command                                                                                                                         |
| `type`       | `"command"` \| `"prompt"` | `"command"`      | Hook execution type                                                                                                                            |
| `timeout`    | number                    | platform default | Execution timeout in seconds                                                                                                                   |
| `loop_limit` | number \| null            | `5`              | Per-script loop limit for stop/subagentStop hooks. `null` means no limit. Default is `5` for Cursor hooks, `null` for Claude Code hooks.       |
| `failClosed` | boolean                   | `false`          | When `true`, hook failures (crash, timeout, invalid JSON) block the action instead of allowing it through. Useful for security-critical hooks. |
| `matcher`    | object                    | -                | Filter criteria for when hook runs                                                                                                             |

##### Matcher Configuration

Matchers let you filter when a hook runs. Which field the matcher applies to depends on the hook:

```json
{
  "hooks": {
    "preToolUse": [
      {
        "command": "./validate-shell.sh",
        "matcher": "Shell"
      }
    ],
    "subagentStart": [
      {
        "command": "./validate-explore.sh",
        "matcher": "explore|shell"
      }
    ],
    "beforeShellExecution": [
      {
        "command": "./approve-network.sh",
        "matcher": "curl|wget|nc "
      }
    ]
  }
}
```

- **subagentStart**: The matcher runs against the **subagent type** (e.g. `explore`, `shell`, `generalPurpose`). Use it to run hooks only when a specific kind of subagent is started. The example above runs `validate-explore.sh` only for explore or shell subagents.
- **beforeShellExecution**: The matcher runs against the **shell command** string. Use it to run hooks only when the command matches a pattern (e.g. network calls, file deletions). The example above runs `approve-network.sh` only when the command contains `curl`, `wget`, or `nc `.

**Available matchers by hook:**

- **preToolUse / postToolUse / postToolUseFailure**: Filter by tool type. Values include `Shell`, `Read`, `Write`, `Grep`, `Delete`, `Task`, and MCP tools using the `MCP:<tool_name>` format.
- **subagentStart / subagentStop**: Filter by subagent type (`generalPurpose`, `explore`, `shell`, etc.).
- **beforeShellExecution / afterShellExecution**: Filter by the shell command text; the matcher is matched against the full command string.
- **beforeReadFile**: Filter by tool type (`TabRead`, `Read`, etc.).
- **afterFileEdit**: Filter by tool type (`TabWrite`, `Write`, etc.).
- **beforeSubmitPrompt**: Matched against the value `UserPromptSubmit`.
- **stop**: Matched against the value `Stop`.
- **afterAgentResponse**: Matched against the value `AgentResponse`.
- **afterAgentThought**: Matched against the value `AgentThought`.

#### Team Distribution

Hooks can be distributed to team members using project hooks (via version control), MDM tools, or Cursor's cloud distribution system.

##### Project Hooks (Version Control)

Project hooks are the simplest way to share hooks with your team. Place a `hooks.json` file at `<project-root>/.cursor/hooks.json` and commit it to your repository. When team members open the project in a trusted workspace, Cursor automatically loads and runs the project hooks.

Cloud agents also load these project hooks when they work on your repository in
the cloud.

Project hooks:

- Are stored in version control alongside your code
- Automatically load for all team members in trusted workspaces
- Can be project-specific (e.g., enforce formatting standards for a particular codebase)
- Require the workspace to be trusted to run (for security)

##### MDM Distribution

Distribute hooks across your organization using Mobile Device Management (MDM) tools. Place the `hooks.json` file and hook scripts in the target directories on each machine.

**User home directory** (per-user distribution):

- `~/.cursor/hooks.json`
- `~/.cursor/hooks/` (for hook scripts)

**Global directories** (system-wide distribution):

- macOS: `/Library/Application Support/Cursor/hooks.json`
- Linux/WSL: `/etc/cursor/hooks.json`
- Windows: `C:\\ProgramData\\Cursor\\hooks.json`

Note: MDM-based distribution is fully managed by your organization. Cursor does not deploy or manage files through your MDM solution. Ensure your internal IT or security team handles configuration, deployment, and updates in accordance with your organization's policies.

##### Cloud Distribution (Enterprise Only)

Enterprise teams can use Cursor's native cloud distribution to automatically sync hooks to all team members. Configure hooks in the [web dashboard](https://cursor.com/dashboard/team-content?section=hooks). Cursor automatically delivers configured hooks to all client machines when team members log in.

Cloud distribution provides:

- Automatic synchronization to all team members (every thirty minutes)
- Operating system targeting for platform-specific hooks
- Centralized management through the dashboard

Enterprise administrators can create, edit, and manage team hooks from the dashboard without requiring access to individual machines.

[Contact sales](https://cursor.com/contact-sales?source=docs-hooks-cloud) to get Enterprise cloud hook distribution.

#### Reference

##### Common schema

###### Input (all hooks)

All hooks receive a base set of fields in addition to their hook-specific fields:

```json
{
  "conversation_id": "string",
  "generation_id": "string",
  "model": "string",
  "model_id": "string",
  "model_params": [{ "id": "string", "value": "string" }],
  "hook_event_name": "string",
  "cursor_version": "string",
  "workspace_roots": ["<path>"],
  "user_email": "string | null",
  "transcript_path": "string | null"
}
```

| Field             | Type              | Description                                                                                               |
| ----------------- | ----------------- | --------------------------------------------------------------------------------------------------------- |
| `conversation_id` | string            | Stable ID of the conversation across many turns                                                           |
| `generation_id`   | string            | The current generation that changes with every user message                                               |
| `model`           | string            | Legacy model slug configured for the composer that triggered the hook                                     |
| `model_id`        | string (optional) | Structured ID for the selected model, when available                                                      |
| `model_params`    | array (optional)  | Selected model parameters, such as thinking, context, or effort. Each item has an `id` and `value`.       |
| `hook_event_name` | string            | Which hook is being run                                                                                   |
| `cursor_version`  | string            | Cursor application version (e.g. "1.7.2")                                                                 |
| `workspace_roots` | string\[]         | The list of root folders in the workspace (normally just one, but multiroot workspaces can have multiple) |
| `user_email`      | string \| null    | Email address of the authenticated user, if available                                                     |
| `transcript_path` | string \| null    | Path to the main conversation transcript file (null if transcripts disabled)                              |

App lifecycle hooks (`workspaceOpen`) fire outside any agent session, so the request omits `conversation_id`, `generation_id`, `model`, `session_id`, and `transcript_path`. They still receive `hook_event_name`, `cursor_version`, `workspace_roots`, and `user_email`.

##### Hook events

###### preToolUse

Called before any tool execution. This is a generic hook that fires for all tool types (Shell, Read, Write, MCP, Task, etc.). Use matchers to filter by specific tools.

```json
// Input
{
  "tool_name": "Shell",
  "tool_input": { "command": "npm install", "working_directory": "/project" },
  "tool_use_id": "abc123",
  "cwd": "/project",
  "model": "claude-opus-4-7-thinking-max",
  "model_id": "claude-opus-4-7",
  "model_params": [
    { "id": "thinking", "value": "true" },
    { "id": "context", "value": "1m" },
    { "id": "effort", "value": "max" }
  ],
  "agent_message": "Installing dependencies..."
}

// Output
{
  "permission": "allow" | "deny",
  "user_message": "<message shown in client when denied>",
  "agent_message": "<message sent to agent when denied>",
  "updated_input": { "command": "npm ci" }
}
```

| Output Field    | Type              | Description                                                                                                         |
| --------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `permission`    | string            | `"allow"` to proceed, `"deny"` to block. `"ask"` is accepted by the schema but not enforced for `preToolUse` today. |
| `user_message`  | string (optional) | Message shown to the user when the action is denied                                                                 |
| `agent_message` | string (optional) | Message fed back to the agent when the action is denied                                                             |
| `updated_input` | object (optional) | Modified tool input to use instead                                                                                  |

###### postToolUse

Called after successful tool execution. Useful for auditing, analytics, and injecting context.

```json
// Input
{
  "tool_name": "Shell",
  "tool_input": { "command": "npm test" },
  "tool_output": "{\"exitCode\":0,\"stdout\":\"All tests passed\"}",
  "tool_use_id": "abc123",
  "cwd": "/project",
  "duration": 5432,
  "model": "claude-opus-4-7-thinking-max",
  "model_id": "claude-opus-4-7",
  "model_params": [
    { "id": "thinking", "value": "true" },
    { "id": "context", "value": "1m" },
    { "id": "effort", "value": "max" }
  ]
}

// Output
{
  "updated_mcp_tool_output": { "modified": "output" },
  "additional_context": "Test coverage report attached."
}
```

| Input Field   | Type   | Description                                                           |
| ------------- | ------ | --------------------------------------------------------------------- |
| `duration`    | number | Execution time in milliseconds                                        |
| `tool_output` | string | JSON-stringified result payload from the tool (not raw terminal text) |

| Output Field              | Type              | Description                                                        |
| ------------------------- | ----------------- | ------------------------------------------------------------------ |
| `updated_mcp_tool_output` | object (optional) | For MCP tools only: replaces the tool output seen by the model     |
| `additional_context`      | string (optional) | Extra context injected into the conversation after the tool result |

###### postToolUseFailure

Called when a tool fails, times out, or is denied. Useful for error tracking and recovery logic.

```json
// Input
{
  "tool_name": "Shell",
  "tool_input": { "command": "npm test" },
  "tool_use_id": "abc123",
  "cwd": "/project",
  "error_message": "Command timed out after 30s",
  "failure_type": "timeout" | "error" | "permission_denied",
  "duration": 5000,
  "is_interrupt": false
}

// Output
{
  // No output fields currently supported
}
```

| Input Field     | Type    | Description                                                       |
| --------------- | ------- | ----------------------------------------------------------------- |
| `error_message` | string  | Description of the failure                                        |
| `failure_type`  | string  | Type of failure: `"error"`, `"timeout"`, or `"permission_denied"` |
| `duration`      | number  | Time in milliseconds until the failure occurred                   |
| `is_interrupt`  | boolean | Whether this failure was caused by a user interrupt/cancellation  |

###### subagentStart

Called before spawning a subagent (Task tool). Can allow or deny subagent creation.

```json
// Input
{
  "subagent_id": "abc-123",
  "subagent_type": "generalPurpose",
  "task": "Explore the authentication flow",
  "parent_conversation_id": "conv-456",
  "tool_call_id": "tc-789",
  "subagent_model": "claude-sonnet-4-20250514",
  "is_parallel_worker": false,
  "git_branch": "feature/auth"
}

// Output
{
  "permission": "allow" | "deny",
  "user_message": "<message shown when denied>"
}
```

| Input Field              | Type              | Description                                                  |
| ------------------------ | ----------------- | ------------------------------------------------------------ |
| `subagent_id`            | string            | Unique identifier for this subagent instance                 |
| `subagent_type`          | string            | Type of subagent: `generalPurpose`, `explore`, `shell`, etc. |
| `task`                   | string            | The task description given to the subagent                   |
| `parent_conversation_id` | string            | Conversation ID of the parent agent session                  |
| `tool_call_id`           | string            | ID of the tool call that triggered the subagent              |
| `subagent_model`         | string            | Model the subagent will use                                  |
| `is_parallel_worker`     | boolean           | Whether this subagent is running as a parallel worker        |
| `git_branch`             | string (optional) | Git branch the subagent will operate on, if applicable       |

| Output Field   | Type              | Description                                                                                                       |
| -------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------- |
| `permission`   | string            | `"allow"` to proceed, `"deny"` to block. `"ask"` is not supported for `subagentStart` and is treated as `"deny"`. |
| `user_message` | string (optional) | Message shown to the user when the subagent is denied                                                             |

###### subagentStop

Called when a subagent completes, errors, or is aborted. Can trigger follow-up actions.

```json
// Input
{
  "subagent_type": "generalPurpose",
  "status": "completed" | "error" | "aborted",
  "task": "Explore the authentication flow",
  "description": "Exploring auth flow",
  "summary": "<subagent output summary>",
  "duration_ms": 45000,
  "message_count": 12,
  "tool_call_count": 8,
  "loop_count": 0,
  "modified_files": ["src/auth.ts"],
  "agent_transcript_path": "/path/to/subagent/transcript.txt"
}

// Output
{
  "followup_message": "<auto-continue with this message>"
}
```

| Input Field             | Type           | Description                                                                                      |
| ----------------------- | -------------- | ------------------------------------------------------------------------------------------------ |
| `subagent_type`         | string         | Type of subagent: `generalPurpose`, `explore`, `shell`, etc.                                     |
| `status`                | string         | `"completed"`, `"error"`, or `"aborted"`                                                         |
| `task`                  | string         | The task description given to the subagent                                                       |
| `description`           | string         | Short description of the subagent's purpose                                                      |
| `summary`               | string         | Output summary from the subagent                                                                 |
| `duration_ms`           | number         | Execution time in milliseconds                                                                   |
| `message_count`         | number         | Number of messages exchanged during the subagent session                                         |
| `tool_call_count`       | number         | Number of tool calls the subagent made                                                           |
| `loop_count`            | number         | Number of times a `subagentStop` follow-up has already triggered for this subagent (starts at 0) |
| `modified_files`        | string\[]      | Files the subagent modified                                                                      |
| `agent_transcript_path` | string \| null | Path to the subagent's own transcript file (separate from the parent conversation)               |

| Output Field       | Type              | Description                                                                    |
| ------------------ | ----------------- | ------------------------------------------------------------------------------ |
| `followup_message` | string (optional) | Auto-continue with this message. Only consumed when `status` is `"completed"`. |

The `followup_message` field enables loop-style flows where subagent completion triggers the next iteration. Follow-ups are subject to the same configurable loop limit as the `stop` hook (default 5, configurable via `loop_limit`).

###### beforeShellExecution / beforeMCPExecution

Called before any shell command or MCP tool is executed. Return a permission decision.

By default, hook failures (crash, timeout, invalid JSON) allow the action through (fail-open). Set `failClosed: true` on the hook definition to block the action on failure instead. This is recommended for security-critical `beforeMCPExecution` hooks.

```json
// beforeShellExecution input
{
  "command": "<full terminal command>",
  "cwd": "<current working directory>",
  "sandbox": false
}

// beforeMCPExecution input
{
  "tool_name": "<tool name>",
  "tool_input": "<json params>"
}
// Plus either:
{ "url": "<server url>" }
// Or:
{ "command": "<command string>" }

// Output
{
  "permission": "allow" | "deny" | "ask",
  "user_message": "<message shown in client>",
  "agent_message": "<message sent to agent>"
}
```

###### afterShellExecution

Fires after a shell command executes; useful for auditing or collecting metrics from command output.

```json
// Input
{
  "command": "<full terminal command>",
  "output": "<full terminal output>",
  "duration": 1234,
  "sandbox": false
}
```

| Field      | Type    | Description                                                                              |
| ---------- | ------- | ---------------------------------------------------------------------------------------- |
| `command`  | string  | The full terminal command that was executed                                              |
| `output`   | string  | Full output captured from the terminal                                                   |
| `duration` | number  | Duration in milliseconds spent executing the shell command (excludes approval wait time) |
| `sandbox`  | boolean | Whether the command ran in a sandboxed environment                                       |

###### afterMCPExecution

Fires after an MCP tool executes; includes the tool's input parameters and full JSON result.

```json
// Input
{
  "tool_name": "<tool name>",
  "tool_input": "<json params>",
  "result_json": "<tool result json>",
  "duration": 1234
}
```

| Field         | Type   | Description                                                                         |
| ------------- | ------ | ----------------------------------------------------------------------------------- |
| `tool_name`   | string | Name of the MCP tool that was executed                                              |
| `tool_input`  | string | JSON params string passed to the tool                                               |
| `result_json` | string | JSON string of the tool response                                                    |
| `duration`    | number | Duration in milliseconds spent executing the MCP tool (excludes approval wait time) |

###### afterFileEdit

Fires after the Agent edits a file; useful for formatters or accounting of agent-written code.

```json
// Input
{
  "file_path": "<absolute path>",
  "edits": [{ "old_string": "<search>", "new_string": "<replace>" }]
}
```

###### beforeReadFile

Called before Agent reads a file. Use for access control to block sensitive files from being sent to the model.

By default, `beforeReadFile` hook failures (crash, timeout, invalid JSON) are logged and the read is allowed through. Set `failClosed: true` on the hook definition to block the read on failure instead.

```json
// Input
{
  "file_path": "<absolute path>",
  "content": "<file contents>",
  "attachments": [
    {
      "type": "file" | "rule",
      "file_path": "<absolute path>"
    }
  ]
}

// Output
{
  "permission": "allow" | "deny",
  "user_message": "<message shown when denied>"
}
```

| Input Field   | Type   | Description                                                                                                       |
| ------------- | ------ | ----------------------------------------------------------------------------------------------------------------- |
| `file_path`   | string | Absolute path to the file being read                                                                              |
| `content`     | string | Full contents of the file                                                                                         |
| `attachments` | array  | Context attachments associated with the prompt. Each entry has a `type` (`"file"` or `"rule"`) and a `file_path`. |

| Output Field   | Type              | Description                             |
| -------------- | ----------------- | --------------------------------------- |
| `permission`   | string            | `"allow"` to proceed, `"deny"` to block |
| `user_message` | string (optional) | Message shown to user when denied       |

###### beforeTabFileRead

Called before Tab (inline completions) reads a file. Enable redaction or access control before Tab accesses file contents.

**Key differences from `beforeReadFile`:**

- Only triggered by Tab, not Agent
- Does not include `attachments` field (Tab doesn't use prompt attachments)
- Useful for applying different policies to autonomous Tab operations

```json
// Input
{
  "file_path": "<absolute path>",
  "content": "<file contents>"
}

// Output
{
  "permission": "allow" | "deny"
}
```

###### afterTabFileEdit

Called after Tab (inline completions) edits a file. Useful for formatters or auditing of Tab-written code.

**Key differences from `afterFileEdit`:**

- Only triggered by Tab, not Agent
- Includes detailed edit information: `range`, `old_line`, and `new_line` for precise edit tracking
- Useful for fine-grained formatting or analysis of Tab edits

```json
// Input
{
  "file_path": "<absolute path>",
  "edits": [
    {
      "old_string": "<search>",
      "new_string": "<replace>",
      "range": {
        "start_line_number": 10,
        "start_column": 5,
        "end_line_number": 10,
        "end_column": 20
      },
      "old_line": "<line before edit>",
      "new_line": "<line after edit>"
    }
  ]
}

// Output
{
  // No output fields currently supported
}
```

###### beforeSubmitPrompt

Called right after user hits send but before backend request. Can prevent submission.

```json
// Input
{
  "prompt": "<user prompt text>",
  "attachments": [
    {
      "type": "file" | "rule",
      "file_path": "<absolute path>"
    }
  ]
}

// Output
{
  "continue": true | false,
  "user_message": "<message shown to user when blocked>"
}
```

| Output Field   | Type              | Description                                          |
| -------------- | ----------------- | ---------------------------------------------------- |
| `continue`     | boolean           | Whether to allow the prompt submission to proceed    |
| `user_message` | string (optional) | Message shown to the user when the prompt is blocked |

###### afterAgentResponse

Called after the agent has completed an assistant message.

```json
// Input
{
  "text": "<assistant final text>"
}
```

###### afterAgentThought

Called after the agent completes a thinking block. Useful for observing the agent's reasoning process.

```json
// Input
{
  "text": "<fully aggregated thinking text>",
  "duration_ms": 5000
}

// Output
{
  // No output fields currently supported
}
```

| Field         | Type              | Description                                            |
| ------------- | ----------------- | ------------------------------------------------------ |
| `text`        | string            | Fully aggregated thinking text for the completed block |
| `duration_ms` | number (optional) | Duration in milliseconds for the thinking block        |

###### stop

Called when the agent loop ends. Can optionally auto-submit a follow-up user message to keep iterating.

```json
// Input
{
  "status": "completed" | "aborted" | "error",
  "loop_count": 0
}
```

```json
// Output
{
  "followup_message": "<message text>"
}
```

- The optional `followup_message` is a string. When provided and non-empty, Cursor will automatically submit it as the next user message. This enables loop-style flows (e.g., iterate until a goal is met).
- The `loop_count` field indicates how many times the stop hook has already triggered an automatic follow-up for this conversation (starts at 0). The default limit is 5 auto follow-ups per script, configurable via the `loop_limit` option. Set `loop_limit` to `null` to remove the cap. The same limit applies to `subagentStop` follow-ups.

###### sessionStart

Called when a new composer conversation is created. This hook runs as fire-and-forget; the agent loop does not wait for or enforce a blocking response. Use it to set up session-specific environment variables or inject additional context.

```json
// Input
{
  "session_id": "<unique session identifier>",
  "is_background_agent": true | false,
  "composer_mode": "agent" | "ask" | "edit"
}
```

```json
// Output
{
  "env": { "<key>": "<value>" },
  "additional_context": "<context to add to conversation>"
}
```

| Input Field           | Type              | Description                                                         |
| --------------------- | ----------------- | ------------------------------------------------------------------- |
| `session_id`          | string            | Unique identifier for this session (same as `conversation_id`)      |
| `is_background_agent` | boolean           | Whether this is a background agent session vs interactive session   |
| `composer_mode`       | string (optional) | The mode the composer is starting in (e.g., "agent", "ask", "edit") |

| Output Field         | Type              | Description                                                                                |
| -------------------- | ----------------- | ------------------------------------------------------------------------------------------ |
| `env`                | object (optional) | Environment variables to set for this session. Available to all subsequent hook executions |
| `additional_context` | string (optional) | Additional context to add to the conversation's initial system context                     |

The schema also accepts `continue` and `user_message` fields, but current callers do not enforce them. Session creation is not blocked even when `continue` is `false`.

###### sessionEnd

Called when a composer conversation ends. This is a fire-and-forget hook useful for logging, analytics, or cleanup tasks. The response is logged but not used.

```json
// Input
{
  "session_id": "<unique session identifier>",
  "reason": "completed" | "aborted" | "error" | "window_close" | "user_close",
  "duration_ms": 45000,
  "is_background_agent": true | false,
  "final_status": "<status string>",
  "error_message": "<error details if reason is 'error'>"
}
```

```json
// Output
{
  // No output fields - fire and forget
}
```

| Input Field           | Type              | Description                                                                               |
| --------------------- | ----------------- | ----------------------------------------------------------------------------------------- |
| `session_id`          | string            | Unique identifier for the session that is ending                                          |
| `reason`              | string            | How the session ended: "completed", "aborted", "error", "window\_close", or "user\_close" |
| `duration_ms`         | number            | Total duration of the session in milliseconds                                             |
| `is_background_agent` | boolean           | Whether this was a background agent session                                               |
| `final_status`        | string            | Final status of the session                                                               |
| `error_message`       | string (optional) | Error message if reason is "error"                                                        |

###### preCompact

Called before context window compaction/summarization occurs. This is an observational hook that cannot block or modify the compaction behavior. Useful for logging when compaction happens or notifying users.

```json
// Input
{
  "trigger": "auto" | "manual",
  "context_usage_percent": 85,
  "context_tokens": 120000,
  "context_window_size": 128000,
  "message_count": 45,
  "messages_to_compact": 30,
  "is_first_compaction": true | false
}
```

```json
// Output
{
  "user_message": "<message to show when compaction occurs>"
}
```

| Input Field             | Type    | Description                                                |
| ----------------------- | ------- | ---------------------------------------------------------- |
| `trigger`               | string  | What triggered the compaction: "auto" or "manual"          |
| `context_usage_percent` | number  | Current context window usage as a percentage (0-100)       |
| `context_tokens`        | number  | Current context window token count                         |
| `context_window_size`   | number  | Maximum context window size in tokens                      |
| `message_count`         | number  | Number of messages in the conversation                     |
| `messages_to_compact`   | number  | Number of messages that will be summarized                 |
| `is_first_compaction`   | boolean | Whether this is the first compaction for this conversation |

| Output Field   | Type              | Description                                        |
| -------------- | ----------------- | -------------------------------------------------- |
| `user_message` | string (optional) | Message to show to the user when compaction occurs |

###### workspaceOpen

Fires once when Cursor opens a workspace and again on every workspace folder change. Skipped when the window has zero workspace folders. Runs in the Cursor desktop app and CLI.

```json
// Input
{
  "hook_event_name": "workspaceOpen",
  "cursor_version": "string",
  "workspace_roots": ["<absolute path>"],
  "user_email": "string | null"
}

// Output
{
  "pluginPaths": ["<absolute path>", "..."]
}
```

| Output Field  | Type                 | Description                                                             |
| ------------- | -------------------- | ----------------------------------------------------------------------- |
| `pluginPaths` | string\[] (optional) | Absolute paths to plugin directories to load for the current workspace. |

#### Environment Variables

Hook scripts receive environment variables when executed:

| Variable                 | Description                                                   | Always Present         |
| ------------------------ | ------------------------------------------------------------- | ---------------------- |
| `CURSOR_PROJECT_DIR`     | Workspace root directory                                      | Yes                    |
| `CURSOR_VERSION`         | Cursor version string                                         | Yes                    |
| `CURSOR_USER_EMAIL`      | Authenticated user email                                      | If logged in           |
| `CURSOR_TRANSCRIPT_PATH` | Path to the conversation transcript file                      | If transcripts enabled |
| `CURSOR_CODE_REMOTE`     | Set to the string `"true"` when running in a remote workspace | For remote workspaces  |
| `CLAUDE_PROJECT_DIR`     | Alias for project dir (Claude compatibility)                  | Yes                    |

Session-scoped environment variables from `sessionStart` hooks are passed to all subsequent hook executions within that session.

#### Troubleshooting

**How to confirm hooks are active**

There is a Hooks tab in **Customize** and a Hooks output channel to debug configured and executed hooks and see errors.

**If hooks are not working**

- Cursor watches `hooks.json` files and reloads them on save. If hooks still do not load, restart Cursor.
- Check that relative paths are correct for your hook source:
  - For **project hooks**, paths are relative to the **project root** (e.g., `.cursor/hooks/script.sh`)
  - For **user hooks**, paths are relative to `~/.cursor/` (e.g., `./hooks/script.sh` or `hooks/script.sh`)

**Exit code blocking**

Exit code `2` from command hooks blocks the action (equivalent to returning `permission: "deny"`). This matches Claude Code behavior for compatibility.

##### Enterprise hooks and distribution

Cloud distribution and team-wide hook management are available on Enterprise.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Model Context Protocol (MCP)

*[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) enables Cursor to connect to external tools and data sources. Install and manage MCP servers from the [Customize](https://cursor.com/docs/customize-cursor.md) page or configure them in `mcp.json`.*

**Source:** https://cursor.com/docs/mcp

#### What is MCP?

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) enables Cursor to connect to external tools and data sources. Install and manage MCP servers from the [Customize](https://cursor.com/docs/customize-cursor.md) page or configure them in `mcp.json`.

##### Why use MCP?

MCP connects Cursor to external systems and data. Instead of explaining your project structure repeatedly, integrate directly with your tools.

Write MCP servers in any language that can print to `stdout` or serve an HTTP endpoint - Python, JavaScript, Go, etc.

Browse official plugins in the [Cursor Marketplace](https://cursor.com/marketplace). For community plugins and MCP servers, browse [cursor.directory](https://cursor.directory).

##### How it works

MCP servers expose capabilities through the protocol, connecting Cursor to external tools or data sources.

Cursor supports three transport methods:

| Transport             | Execution environment | Deployment       | Users          | Input                   | Auth   |
| :-------------------- | :-------------------- | :--------------- | :------------- | :---------------------- | :----- |
| **`stdio`**           | Local                 | Cursor manages   | Single user    | shell command           | Manual |
| **`SSE`**             | Local/Remote          | Deploy as server | Multiple users | URL to an SSE endpoint  | OAuth  |
| **`Streamable HTTP`** | Local/Remote          | Deploy as server | Multiple users | URL to an HTTP endpoint | OAuth  |

##### Protocol and extension support

Cursor supports these MCP protocol capabilities and extensions:

| Feature              | Support   | Description                                                     |
| :------------------- | :-------- | :-------------------------------------------------------------- |
| **Tools**            | Supported | Functions for the AI model to execute                           |
| **Prompts**          | Supported | Templated messages and workflows for users                      |
| **Resources**        | Supported | Structured data sources that can be read and referenced         |
| **Roots**            | Supported | Server-initiated inquiries into URI or filesystem boundaries    |
| **Elicitation**      | Supported | Server-initiated requests for additional information from users |
| **Apps (extension)** | Supported | Interactive UI views returned by MCP tools                      |

##### MCP apps

Cursor supports the [MCP Apps extension](https://modelcontextprotocol.io/extensions/apps/overview). MCP tools can return interactive UI along with standard tool output.

MCP Apps follow progressive enhancement. If a host cannot render app UI, the same tool still works through normal MCP responses.

#### Installing MCP servers

##### One-click installation

Browse the [Cursor Marketplace](https://cursor.com/marketplace) for official plugins with one-click install from **Customize**, or configure custom servers with `mcp.json`. For community plugins and MCP servers, browse [cursor.directory](https://cursor.directory). Click "Add to Cursor" on a marketplace entry to install it and authenticate with OAuth.

Team admins can also distribute MCP servers through a [team marketplace](https://cursor.com/docs/plugins.md#team-marketplaces). Team-distributed servers appear in Customize alongside personal and workspace MCP servers.

##### Using `mcp.json`

Configure custom MCP servers with a JSON file:

```json title="CLI Server - Node.js"
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "mcp-server"],
      "env": {
        "API_KEY": "value"
      }
    }
  }
}
```

```json title="CLI Server - Python"
{
  "mcpServers": {
    "server-name": {
      "command": "python",
      "args": ["mcp-server.py"],
      "env": {
        "API_KEY": "value"
      }
    }
  }
}
```

```json title="Remote Server"
// MCP server using HTTP or SSE - runs on a server
{
  "mcpServers": {
    "server-name": {
      "url": "http://localhost:3000/mcp",
      "headers": {
        "API_KEY": "value"
      }
    }
  }
}
```

##### Static OAuth for remote servers

For MCP servers that use OAuth, you can provide **static OAuth client credentials** in `mcp.json` instead of dynamic client registration. Use this when:

- The MCP provider gives you a fixed **Client ID** (and optionally **Client Secret**)
- The provider requires **whitelisting a redirect URL** (e.g. Figma, Linear)
- The provider does not support OAuth 2.0 Dynamic Client Registration

Add an `auth` object to remote server entries that use `url`:

```json title="Remote Server with Static OAuth"
{
  "mcpServers": {
    "oauth-server": {
      "url": "https://api.example.com/mcp",
      "auth": {
        "CLIENT_ID": "your-oauth-client-id",
        "CLIENT_SECRET": "your-client-secret",
        "scopes": ["read", "write"]
      }
    }
  }
}
```

| Field              | Required | Description                                                                                                                   |
| :----------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **CLIENT\_ID**     | Yes      | OAuth 2.0 Client ID from the MCP provider                                                                                     |
| **CLIENT\_SECRET** | No       | OAuth 2.0 Client Secret (if the provider uses confidential clients)                                                           |
| **scopes**         | No       | OAuth scopes to request. If omitted, Cursor will use `/.well-known/oauth-authorization-server` to discover `scopes_supported` |

###### Static redirect URL

Cursor uses fixed OAuth redirect URLs for MCP servers. Register the callback for each surface your users authenticate from:

```text
https://www.cursor.com/agents/mcp/oauth/callback
http://localhost:8787/callback
```

- **Web and Cursor Agents**: `https://www.cursor.com/agents/mcp/oauth/callback`
- **Desktop app**: `http://localhost:8787/callback`

When configuring the MCP provider's OAuth app, register both URLs as allowed redirect URIs if users authenticate from both web and desktop. The server is identified via the OAuth `state` parameter, so these redirect URLs work for all MCP servers.

###### Combining with config interpolation

`auth` values support the same interpolation as other fields:

```json
{
  "mcpServers": {
    "oauth-server": {
      "url": "https://api.example.com/mcp",
      "auth": {
        "CLIENT_ID": "${env:MCP_CLIENT_ID}",
        "CLIENT_SECRET": "${env:MCP_CLIENT_SECRET}"
      }
    }
  }
}
```

Use environment variables for Client ID and Client Secret instead of hardcoding them.

##### STDIO server configuration

For STDIO servers (local command-line servers), configure these fields in your `mcp.json`:

| Field       | Required | Description                                                                                             | Examples                                  |
| :---------- | :------- | :------------------------------------------------------------------------------------------------------ | :---------------------------------------- |
| **type**    | Yes      | Server connection type                                                                                  | `"stdio"`                                 |
| **command** | Yes      | Command to start the server executable. Must be available on your system path or contain its full path. | `"npx"`, `"node"`, `"python"`, `"docker"` |
| **args**    | No       | Array of arguments passed to the command                                                                | `["server.py", "--port", "3000"]`         |
| **env**     | No       | Environment variables for the server                                                                    | `{"API_KEY": "${env:api-key}"}`           |
| **envFile** | No       | Path to an environment file to load more variables                                                      | `".env"`, `"${workspaceFolder}/.env"`     |

The `envFile` option is only available for STDIO servers. Remote servers (HTTP/SSE) do not support `envFile`. For remote servers, use [config interpolation](https://cursor.com/docs/mcp.md#config-interpolation) with environment variables set in your shell profile or system environment instead.

##### Using the Extension API

For programmatic MCP server registration, Cursor provides an extension API that allows dynamic configuration without modifying `mcp.json` files. This is particularly useful for enterprise environments and automated setup workflows.

##### Extension API reference

Register MCP servers programmatically using
`vscode.cursor.mcp.registerServer()`

##### Configuration locations

##### Project Configuration

Create `.cursor/mcp.json` in your project for project-specific tools.

##### Global Configuration

Create `~/.cursor/mcp.json` in your home directory for tools available everywhere.

##### Config interpolation

Use variables in `mcp.json` values. Cursor resolves variables in these fields: `command`, `args`, `env`, `url`, and `headers`.

Supported syntax:

- `${env:NAME}` environment variables
- `${userHome}` path to your home folder
- `${workspaceFolder}` project root (the folder that contains `.cursor/mcp.json`)
- `${workspaceFolderBasename}` name of the project root
- `${pathSeparator}` and `${/}` OS path separator

Examples

```json
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/mcp_server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

```json
{
  "mcpServers": {
    "remote-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    }
  }
}
```

##### Authentication

MCP servers use environment variables for authentication. Pass API keys and tokens through the config.

Cursor supports OAuth for servers that require it.

#### Enterprise admin controls

MCP distribution and MCP policy are configured separately. Team admins can distribute shared MCP servers. Enterprise admins can configure MCP policy.

##### Team MCP distribution

Configure shared Team MCP servers under **Dashboard > Integrations & MCP**. These servers are available to Cloud Agents.

To make an existing standalone Team MCP server available in the Agent Window, IDE, and CLI, select **Add to Team Marketplace** under **Team MCP Servers**. Cursor links the server to the Default team marketplace without interrupting Cloud Agent access. Teammates can then install and configure it from Customize.

Linking an MCP server to a marketplace does not install or enable it for everyone. Configure **Marketplace Access** and plugin installation modes under **Dashboard > Plugins**. See [Migrate existing Team MCPs](https://cursor.com/docs/plugins.md#migrate-existing-team-mcps) for the full flow.

##### MCP Allowlist

Enterprise admins can control which MCP servers users may run from the Cursor dashboard. Open [Team Settings > MCP Configuration](https://cursor.com/dashboard/team-settings#mcp-configuration) to configure which servers and tools the team may run. Allowlisting approves an MCP configuration. It does not distribute or install the server.

Use the MCP Allowlist to define approved servers:

- **Command entries** approve local `stdio` MCP servers by command pattern.
- **URL entries** approve remote HTTP/SSE MCP servers by URL entry pattern.
- **Tool allowlists** restrict which tools from an approved server can run automatically. Leave a tool allowlist empty to allow all tools from that server.

##### Network controls

Remote MCP URLs are restricted to the configured URL entry pattern.

Local command-based MCP servers use their per-server network mode:

- **Allow all**: allow outbound network access.
- **Allowlist**: allow only listed destinations.
- **Deny all**: block outbound network access.
- **No sandbox**: run without command or network sandboxing.

##### User MCP extensions

Admins can allow users to configure their own MCP servers outside admin-defined command or URL patterns. For user MCPs that do not match an admin-defined pattern, the User MCP Network Denylist can block matching network destinations.

#### Using MCP in chat

Cursor automatically uses MCP tools listed under `Available Tools` when relevant. This includes [Plan Mode](https://cursor.com/docs/agent/plan-mode.md#plan). Ask for a specific tool by name or describe what you need. Enable or disable MCP servers from **Customize** in the sidebar.

##### Tool approval

Cursor asks for approval before using MCP tools by default. Click the arrow next to the tool name to see arguments.

![Tool confirmation prompt](https://cursor.com/docs-static/images/context/mcp/tool-confirm.png)

###### Run Mode

MCP [follows the same Run Modes as terminal commands](https://cursor.com/docs/agent/security/run-modes.md#run-mode). For example, in **Auto-review** mode, allowlisted MCP tools run immediately and everything else is routed through the classifier.

##### Tool response

Cursor shows the response in chat with expandable views of arguments and responses:

![MCP tool call result](https://cursor.com/docs-static/images/context/mcp/tool-call.png)

##### Images as context

MCP servers can return images - screenshots, diagrams, etc. Return them as base64 encoded strings:

```js
const RED_CIRCLE_BASE64 = "/9j/4AAQSkZJRgABAgEASABIAAD/2w...";
// ^ full base64 clipped for readability

server.tool("generate_image", async (params) => {
  return {
    content: [
      {
        type: "image",
        data: RED_CIRCLE_BASE64,
        mimeType: "image/jpeg",
      },
    ],
  };
});
```

See this [example server](https://github.com/msfeldstein/mcp-test-servers/blob/main/src/image-server.js) for implementation details. Cursor attaches returned images to the chat. If the model supports images, it analyzes them.

#### Security considerations

When installing MCP servers, consider these security practices:

- **Verify the source**: Only install MCP servers from trusted developers and repositories
- **Review permissions**: Check what data and APIs the server will access
- **Limit API keys**: Use restricted API keys with minimal required permissions
- **Audit code**: For critical integrations, review the server's source code

Remember that MCP servers can access external services and execute code on your behalf. Always understand what a server does before installation.

#### Real-world examples

For practical examples of MCP in action:

- **[Xcode integration](https://cursor.com/docs/integrations/xcode.md)** — Connect Cursor to Xcode 26.3+ for builds, tests, SwiftUI previews, and Apple documentation search
- **[Web Development guide](https://cursor.com/for/web-development.md)** — Integrate Linear, Figma, and browser tools into your development workflow

#### FAQ

##### What's the point of MCP servers?

MCP servers connect Cursor to external tools like Google Drive, Notion, and
other services to bring docs and requirements into your coding workflow.

##### How do I debug MCP server issues?

View MCP logs by:

1. Open the Output panel in Cursor (Cmd+Shift+U)
2. Select "MCP Logs" from the dropdown
3. Check for connection errors, authentication issues, or server crashes

The logs show server initialization, tool calls, and error messages.

##### Can I temporarily disable an MCP server?

Yes! Toggle servers on/off without removing them:

1. Open **Customize** in the sidebar
2. Find the MCP server you want to change
3. Use the toggle to enable or disable it

Disabled servers won't load or appear in chat. This is useful for troubleshooting or reducing tool clutter.

##### What happens if an MCP server crashes or times out?

If an MCP server fails:

- Cursor shows an error message in chat
- The tool call is marked as failed
- You can retry the operation or check logs for details
- Other MCP servers continue working normally

Cursor isolates server failures to prevent one server from affecting others.

##### How do I update an MCP server?

For npm-based servers:

1. Remove the server from **Customize**
2. Clear npm cache: `npm cache clean --force`
3. Re-add the server to get the latest version

For custom servers, update your local files and restart Cursor.

##### Can I use MCP servers with sensitive data?

Yes, but follow security best practices:

- Use environment variables for secrets, never hardcode them
- Run sensitive servers locally with `stdio` transport
- Limit API key permissions to minimum required
- Review server code before connecting to sensitive systems
- Consider running servers in isolated environments


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

---
