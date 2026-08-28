---
name: tool-factory
description: Mines GitHub repositories or existing codebases for reusable Python functions and turns the good ones into FastMCP tool modules for Build1's nervous system. Activate for "mine this repo", "analyze this GitHub repo for useful functions", "add a new FastMCP tool", or "add a new capability". Touches Build1's FastMCP layer directly; any extracted function that calls an LLM must be rewired to call Local Ollama.
icon: wrench
color: Orange
---

# Tool Factory (Build1 edition)

Extracts reusable functions from a repo and turns qualifying ones into `@mcp.tool()` functions registered on Build1's FastMCP server — the "nervous system" that the local-Ollama-driven agent calls into.

## When to activate
- "Mine this GitHub repo for useful functions"
- "Analyze this codebase and extract tools"
- "Add a new FastMCP tool / capability"
- "What functions can we extract from X?"

For *using* already-built tools rather than mining new ones, route to the relevant domain skill instead (e.g. `web-researcher`, `report-builder`, `api-tester`, `cognee-memory-pipeline`).

## Mining workflow (8 steps)

```python
from github_analyzer import clone_repo, analyze_repo
from repo_reverse_engineer import reconstruct_intent
from security_tools import check_dep_safety
from ast_indexer import create_index

# 1. UNDERSTAND — reconstruct intent before cloning
intent = reconstruct_intent("https://github.com/owner/repo")

# 2. CLONE (shallow)
repo = clone_repo(intent["url"], depth=1)["result"]

# 3. ANALYZE
analysis = analyze_repo(repo["path"], min_score=4)["result"]

# 4. SECURE — check deps before running anything from the repo
check_dep_safety(analysis["dependencies"]["python_dependencies"])

# 5. INDEX — build a call graph of candidate functions
create_index("new_code.db", repo["path"])

# 6. JUDGE — keep score >= 5, skip <= 3 (see scoring guide below)

# 7. GENERATE — wrap qualifying functions as FastMCP tools (see pattern below)

# 8. REPORT — functions added, env vars needed, vulnerabilities found
```

## Scoring guide

| Score | Action |
|---|---|
| 8–10 | Add immediately — clear API, docstring, external value |
| 5–7 | Add as stub — useful pattern, needs light work |
| 3–4 | Note and skip — needs significant refactor |
| 0–2 | Skip — helper/test/glue code, not a standalone tool |

## New tool pattern — register on the FastMCP server

```python
from fastmcp import FastMCP

mcp = FastMCP("build1-tools")

@mcp.tool()
def tool_name(param: str, count: int = 10) -> dict:
    """One-line description of what this tool does."""
    try:
        result = ...  # extracted logic goes here
        return {"ok": True, "result": result}
    except Exception as e:
        return {"ok": False, "error": str(e)}
```

If the mined function calls an LLM, rewire it to call **local Ollama** instead of any cloud provider:

```python
import requests

def call_llm(prompt: str, model: str = "llama3.1") -> str:
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
    )
    r.raise_for_status()
    return r.json()["response"]
```

Never leave a mined tool depending on `OPENAI_API_KEY` or similar cloud credentials — either port it to Ollama's REST/`ollama` Python client, or drop it if it fundamentally requires a hosted-only model.

## Build1 Integration

- New tool modules live alongside the Build1 FastMCP server's tools package and are registered via `@mcp.tool()` so the agent loop (driven by local Ollama) can call them.
- If a mined tool needs persistence, have it write through PocketBase's REST API (`http://localhost:8090/api/...`) rather than a new local file or a cloud DB.
- If a mined tool needs semantic recall, route it through the `cognee-memory-pipeline` skill's `add`/`cognify`/`search` calls instead of building a bespoke vector store.
- Keep everything reachable at `localhost` — the mining process itself (cloning, analyzing) can use the network, but the *resulting tool's runtime behavior* must not require any external/cloud service to function.
