---
name: code-analyst
description: Analyze GitHub repos, audit security, map code structure, scan dependencies, and reverse-engineer binaries. Activate for "analyze this repo", "security scan", "audit this code", "find vulnerabilities", "reverse engineer this binary". Infra-agnostic developer-tooling skill; applies equally well to auditing any part of a Build1 stack (FastMCP server code, PocketBase schema/migrations, frontend JS) but has no dependency on Ollama/PocketBase/Cognee/FastMCP/HTMX-Alpine itself.
icon: code
color: Orange
---

# Code Analyst

## Activate when

- "Analyze this repo" / "What does this codebase do?"
- "Security scan" / "Find vulnerabilities" / "Check dependencies"
- "Reverse engineer this binary / APK / memory dump"
- "Build a call graph" / "Find all entry points"
- "Reconstruct the intent of this repo"

## How to use this skill

1. Clone or fetch only the specific files/repo needed — do not blindly clone huge
   monorepos when a targeted file fetch will answer the question.
2. Pick the script(s) below that match the request and run them from this skill's
   `scripts/` directory. Consult `references/05_code_analysis.md` for code-analysis
   parameter details and `references/06_reverse_engineering.md` for reverse-engineering
   detail — keep the exhaustive parameter catalog there rather than inline here.
3. Summarize findings for the user: what the code/binary does, key entry points,
   dependency/vulnerability findings, and any risk flags — do not dump raw tool output.

## Script catalog (place under `scripts/`)

| Script | Purpose |
|---|---|
| `github_analyzer.py` | Clone, analyze, score, and extract functions from any repo |
| `security_tools.py` | Secret scanning, CVE checks, SBOM, license audit |
| `ast_indexer.py` | Python symbol index, call graph, entry-point detection |
| `codebase_knowledge_graph.py` | Cross-file knowledge graph, Cypher/JSON/Markdown export |
| `repo_reverse_engineer.py` | Intent reconstruction from any GitHub URL |
| `binary_analysis_tools.py` | PE/ELF parsing, disassembly, checksec, symbolic execution |
| `malware_analysis_tools.py` | YARA scan, MITRE ATT&CK mapping, obfuscated string extraction |
| `forensics_tools.py` | Memory dump analysis, process listing, injected-code detection |
| `graph_tools.py` | General directed graph — BFS, cycles, centrality, DOT/Cypher export |

## Merged reverse-engineering capabilities (from `reverse-engineer`)

The binary/malware/forensics scripts above (`binary_analysis_tools.py`,
`malware_analysis_tools.py`, `forensics_tools.py`) absorb the dedicated RE toolkit that
previously lived in a separate skill — YARA rule scanning, `capa` capability
detection, Volatility3-style memory forensics, and Frida-based dynamic instrumentation
all run locally with no cloud dependency. If a hash-reputation lookup (e.g.
VirusTotal) is requested, treat it as an explicit, opt-in network call — never invoke
it by default, since Build1 is zero-cloud.

## Build1 Integration

Infra-agnostic. When used against a Build1 project itself, point it at the FastMCP
server source, PocketBase migration/schema files, or the HTMX/Alpine frontend assets —
the analysis approach is identical regardless of target. No cloud LLM API is required;
any summarization step should be done with the locally-run Ollama model rather than a
cloud endpoint.
