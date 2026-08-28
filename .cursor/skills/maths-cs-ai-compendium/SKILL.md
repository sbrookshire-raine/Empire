---
name: maths-cs-ai-compendium
description: Reference lookup skill over HenryNdubuaku/maths-cs-ai-compendium, an open-access textbook (20 chapters of Markdown) covering mathematics, computing, and AI from first principles. Use when the user asks a conceptual maths/CS/AI question, wants an intuitive explanation or citation-worthy reference, or wants to browse a specific chapter. Infra-agnostic reference dataset; its optional MCP server can be wired into Build1's FastMCP nervous system so a local Ollama model can query the compendium as a tool.
icon: book-open
color: Yellow
---

# Maths, CS & AI Compendium (HenryNdubuaku/maths-cs-ai-compendium)

A static reference/dataset repo (no executable application) — treat every request as
"look up and summarize/quote the relevant chapter," not "run a program."

## Chapter map (directory → topic)

| # | Directory | Topic |
|---|---|---|
| 01 | `chapter 01: vectors` | Vector spaces, norms, metrics, dot/cross/outer products, basis, duality |
| 02 | `chapter 02: matrices` | Matrix properties, operations, linear transforms, LU/QR/SVD |
| 03 | `chapter 03: calculus` | Derivatives, integrals, multivariate calculus, Taylor approx., gradient descent |
| 04 | `chapter 04: statistics` | Statistics fundamentals |
| 05 | `chapter 05: probability` | Probability fundamentals |
| 06 | `chapter 06: machine learning` | Core ML concepts |
| 07 | `chapter 07: computational linguistics` | NLP/linguistics foundations |
| 08 | `chapter 08: computer vision` | CV foundations |
| 09 | `chapter 09: audio and speech` | Audio/speech processing |
| 10 | `chapter 10: multimodal learning` | Multimodal models |
| 11 | `chapter 11: autonomous systems` | Robotics/autonomy |
| 12 | `chapter 12: graph neural networks` | GNNs |
| 13 | `chapter 13: computing and OS` | Systems/OS fundamentals |
| 14 | `chapter 14: data structures and algorithms` | DSA |
| 15 | `chapter 15: production software engineering` | Applied SWE practices |
| 16 | `chapter 16: SIMD and GPU programming` | Low-level performance programming |
| 17 | `chapter 17: AI inference` | Inference systems/optimization |
| 18 | `chapter 18: ML systems design` | ML infra/design |
| 19 | `chapter 19: applied AI` | Applied AI case studies |
| 20 | `chapter 20: bleeding edge AI` | Emerging AI research |

Each chapter directory contains numbered Markdown lesson files (e.g.
`chapter 01: vectors/01. vector spaces.md`); the repo is also published as a browsable
site at `https://henryndubuaku.github.io/maths-cs-ai-compendium/`.

## How to answer a user's question

1. Identify which chapter(s) above best match the question's topic.
2. Fetch the relevant file(s) directly rather than cloning the whole repo, e.g.:
   ```
   https://raw.githubusercontent.com/HenryNdubuaku/maths-cs-ai-compendium/main/chapter%2001%3A%20vectors/01.%20vector%20spaces.md
   ```
   (URL-encode spaces/colons in the chapter directory name.) Or browse the rendered
   site link above.
3. Summarize/quote the relevant section, citing the chapter/section and the compendium
   itself.
4. If the user wants an entire chapter's raw text, list the files in that chapter
   directory (via the GitHub API or the rendered site's nav) and fetch each one needed.

## Optional MCP server

The repo ships an MCP server (`mcp/` directory) that exposes the compendium as a
knowledge base to MCP-compatible assistants. It requires a local clone of the repo to
run. Only set this up if the user explicitly wants it wired permanently into a tool —
for a one-off Q&A, prefer the direct file-fetch approach above.

## Citation

If the user wants to cite this resource, credit "HenryNdubuaku/maths-cs-ai-compendium"
with the repository URL (`https://github.com/HenryNdubuaku/maths-cs-ai-compendium`)
and the specific chapter/file used.

## Build1 Integration

Infra-agnostic by default (plain file fetch + summarize). If the user wants this
compendium available as a standing tool for their local stack, register the
compendium's `mcp/` server as one more tool exposed through Build1's **FastMCP**
nervous system, so the locally-run **Ollama** model can call it directly instead of
relying on a cloud LLM to do the lookup. No PocketBase/Cognee/frontend involvement is
required for this skill.
