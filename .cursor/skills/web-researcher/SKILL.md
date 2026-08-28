---
name: web-researcher
description: Searches the web, scrapes pages, researches topics across multiple rounds, and monitors URLs for changes. Activate for "research X", "find information about", "scrape this site", "monitor this page", "fetch this URL". Touches FastMCP (exposes research functions as tools), Local Ollama (synthesizes/summarizes findings instead of a cloud LLM), and optionally Cognee (stores findings into the knowledge graph for later recall).
icon: globe
color: Teal
---

# Web Researcher (Build1 edition)

## Activate when
- "Research X" / "Find information about..."
- "Scrape this site" / "Get the content of this URL"
- "Monitor this page for changes"
- "Search for packages / repos / news about X"
- "Deep research with multiple rounds"

## Capabilities → module

| Module | Purpose |
|---|---|
| `research_tools` | Multi-source research, deep_research with gap-filling |
| `scraper` | URL → Markdown, link extraction, batch scrape |
| `browser_tools` | Playwright-based: screenshots, JS-rendered pages, form fill |
| `search` | Web search, GitHub search, package registry search |
| `rest_client` | Authenticated HTTP GET/POST/PUT/PATCH/DELETE, pagination |

## Quick start — register as FastMCP tools

```python
from fastmcp import FastMCP
from research_tools import research, deep_research
from scraper import scrape_url_to_markdown, batch_scrape
from search import web_search, search_github

mcp = FastMCP("web-researcher")

@mcp.tool()
def scrape(url: str) -> dict:
    """Fetch a URL and return clean Markdown."""
    return scrape_url_to_markdown(url)

@mcp.tool()
def run_research(topic: str, rounds: int = 2) -> dict:
    """Search + scrape multiple sources, then synthesize a summary locally."""
    raw = deep_research(topic, rounds=rounds)
    summary = summarize_locally(raw["result"])
    return {"ok": True, "result": summary}
```

## Synthesize locally with Ollama (not a cloud LLM)

```python
import requests

def summarize_locally(text: str, model: str = "llama3.1") -> str:
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": f"Synthesize the key findings:\n\n{text}", "stream": False},
    )
    r.raise_for_status()
    return r.json()["response"]
```

## Build1 Integration

- Register scrape/search/research functions as `@mcp.tool()` entries on the Build1 FastMCP server so the local-Ollama-driven agent loop can call them directly.
- Any "deep research"/multi-round synthesis step must call **local Ollama**, never an external LLM API — the web fetch itself is the only network dependency in the pipeline, everything downstream stays local.
- After scraping/searching, push extracted text into Cognee via `cognee.add()` + `cognee.cognify()` (see `cognee-memory-pipeline` skill) so a later FastMCP-served `cognee.search()` call can recall this research as part of the agent's long-term memory, instead of re-scraping the same pages every time.
- Store fetched raw pages/snapshots as PocketBase records if the user wants a persisted history of what was researched and when.
