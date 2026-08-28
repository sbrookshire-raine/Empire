---
name: cognee-memory-pipeline
description: Builds AI memory and knowledge graphs from unstructured data using the cognee Python library/CLI (add, cognify, search, remember, recall, memify, serve), configured to run fully locally against Ollama for both inference and embeddings. Use when a user wants to ingest documents/text into a queryable knowledge graph, run cognee's extract-cognify-load pipeline, expose it as an MCP server, or query stored memories. This IS Build1's Memory/RAG (Graph) layer — directly touches Cognee, Local Ollama, and FastMCP.
icon: brain
color: Purple
---

# Cognee — Build1's local AI memory & knowledge graph layer

Cognee (topoteretes/cognee) turns raw text/documents into a structured, queryable knowledge graph ("AI memory"). It ships as a Python library, a CLI, a FastAPI backend, an MCP server (`cognee-mcp/`), and a frontend. In Build1, Cognee is the designated Memory/RAG (Graph) component — it must be configured to use **local Ollama**, never a cloud LLM/embedding provider, and Cognee Cloud (the hosted offering) must not be used.

## 1. Install

```bash
pip install cognee
```

## 2. Configure for local-only operation (Ollama)

Set Cognee's LLM and embedding backends to point at the local Ollama server instead of any cloud provider. Exact environment variable names vary by installed cognee version — check `cognee/infrastructure/llm/` config or the shipped `.env.template` to confirm the current names before relying on this snippet as-is:

```python
import os

os.environ["LLM_PROVIDER"] = "ollama"
os.environ["LLM_MODEL"] = "llama3.1"
os.environ["LLM_ENDPOINT"] = "http://localhost:11434/v1"

os.environ["EMBEDDING_PROVIDER"] = "ollama"
os.environ["EMBEDDING_MODEL"] = "nomic-embed-text"
os.environ["EMBEDDING_ENDPOINT"] = "http://localhost:11434/v1"
```

Confirm the underlying graph/vector storage also stays local (cognee defaults to a local SQLite/embedded vector+graph store unless explicitly pointed at a hosted provider) — do not opt into any cloud-hosted vector DB or Cognee Cloud.

## 3. Core ECL (extract–cognify–load) pipeline

```python
import asyncio
import cognee

async def build_memory():
    await cognee.add("path/to/document.txt")
    await cognee.cognify()
    results = await cognee.search("What did the document say about X?")
    return results

asyncio.run(build_memory())
```

## 4. CLI usage

```bash
cognee add <file_or_text>
cognee cognify
cognee search "<query>"
```

## 5. Expose as an MCP server / FastMCP tool

Either run cognee's own `cognee-mcp` server and have Build1's FastMCP layer proxy to it, or wrap the calls directly as tools on the Build1 FastMCP server so the agent loop can `remember`/`recall` without a separate process:

```python
from fastmcp import FastMCP
import cognee

mcp = FastMCP("memory")

@mcp.tool()
async def remember(text: str) -> dict:
    """Ingest text into the knowledge graph."""
    await cognee.add(text)
    await cognee.cognify()
    return {"ok": True}

@mcp.tool()
async def recall(query: str) -> dict:
    """Search the knowledge graph."""
    results = await cognee.search(query)
    return {"ok": True, "result": results}
```

## Build1 Integration

- Cognee **is** Build1's Memory/RAG (Graph) layer — always configure both its LLM and embedding backends to hit **local Ollama** (`http://localhost:11434`), never a cloud provider, and never enable Cognee Cloud.
- Confirm the graph/vector store stays on local disk, not a hosted database.
- Expose `remember`/`recall` (`add`/`cognify`/`search`) as `@mcp.tool()` functions on the Build1 FastMCP server so the agent's local-Ollama-driven reasoning loop can read/write long-term memory.
- Other skills (e.g. `web-researcher`, `exercises-dataset-lookup`) that produce text worth remembering should feed it into this pipeline via `add`/`cognify` rather than building separate ad hoc memory stores.
- If structured records (not just free text) need to be remembered, consider storing the canonical record in PocketBase and only feeding the *text representation* into Cognee for semantic search, so PocketBase stays the source of truth and Cognee stays the recall index.
