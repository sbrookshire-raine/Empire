"""SearXNG search — the query capability E-34 measured as missing (E-35).

Why this exists
---------------
`docs/RESEARCH_CLOSURE.md` closed discovery until a hole was *measured*. `scripts/run-research-bench.py
--baseline` measured it: 2 of 8 cases blocked, both `search` — no callable tool for "a query with no
URL and no archive hit", because `web_search`/`web_fetch` are `disableTool()` (the provider-managed
path hung local Ollama) and `web_scout` needs a URL you hand it.

This talks to a **self-hosted** SearXNG (`scripts/start-searxng.ps1`, Docker, port 8888) whose JSON
output is enabled in `config/searxng/settings.yml`. No API key, no cloud meter, nothing leaves the box.

    python -m pipeline.search_scout "local first llm tool calling"
    python -m pipeline.search_scout "searxng json api" --limit 3

Failure modes are stated, never faked: a down instance says so and names the fix, and a 403 explains
that the JSON format is not enabled.
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Callable

DEFAULT_BASE = os.environ.get("EMPIRE_SEARXNG_URL", "http://127.0.0.1:8888")
DEFAULT_LIMIT = 5
MAX_LIMIT = 20
USER_AGENT = "EMPIRE-search-scout/1"
START_HINT = r"start it with .\scripts\start-searxng.ps1 (Docker Desktop must be running)"


def base_url() -> str:
    """The instance to talk to (env override so a different port/host is possible)."""

    return os.environ.get("EMPIRE_SEARXNG_URL", DEFAULT_BASE).rstrip("/")


def _clean(value: object, max_chars: int = 400) -> str:
    text = " ".join(str(value or "").split())
    return text[:max_chars]


def search(
    query: str,
    *,
    limit: int = DEFAULT_LIMIT,
    base: str | None = None,
    timeout: float = 25.0,
    opener: Callable[..., Any] | None = None,
) -> dict[str, Any]:
    """One query against the local instance. Returns `{ok, query, results, engine_count}`."""

    cleaned = _clean(query, 300)
    if not cleaned:
        return {"ok": False, "error": "a query is required"}
    capped = max(1, min(int(limit or DEFAULT_LIMIT), MAX_LIMIT))
    root = (base or base_url()).rstrip("/")
    url = f"{root}/search?" + urllib.parse.urlencode({"q": cleaned, "format": "json"})
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    fetch = opener or urllib.request.urlopen
    try:
        with fetch(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8", errors="replace"))
    except urllib.error.HTTPError as exc:
        if exc.code == 403:
            return {
                "ok": False,
                "error": "the instance refused the JSON format (403)",
                "hint": "enable `search.formats: [html, json]` — see config/searxng/settings.yml",
            }
        return {"ok": False, "error": f"search failed with HTTP {exc.code}"}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {
            "ok": False,
            "error": f"SearXNG is not reachable at {root} ({exc})",
            "hint": START_HINT,
        }
    except json.JSONDecodeError:
        return {"ok": False, "error": f"{root} did not return JSON", "hint": START_HINT}

    raw = payload.get("results") if isinstance(payload, dict) else None
    results: list[dict[str, Any]] = []
    for item in raw or []:
        if not isinstance(item, dict):
            continue
        link = str(item.get("url") or "").strip()
        if not link:
            continue
        results.append(
            {
                "title": _clean(item.get("title"), 160) or link,
                "url": link,
                "snippet": _clean(item.get("content") or item.get("snippet"), 400),
                "engine": _clean(item.get("engine"), 40),
            }
        )
    engines = payload.get("number_of_results") if isinstance(payload, dict) else None
    return {
        "ok": True,
        "query": cleaned,
        "base": root,
        "results": results[:capped],
        "available": len(results),
        "engine_reported_count": engines if isinstance(engines, int) else None,
        "note": "a metasearch result list is a lead, not a source — open a page with web_scout before quoting it",
    }


def urls_for(query: str, *, limit: int = 3, **kwargs: Any) -> dict[str, Any]:
    """Search, then hand back just the URLs — the shape the research desk fetches."""

    found = search(query, limit=limit, **kwargs)
    if not found.get("ok"):
        return found
    urls = [str(item["url"]) for item in found.get("results") or []]
    return {"ok": True, "query": found.get("query", query), "urls": urls, "results": found.get("results")}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Local SearXNG search (E-35)")
    parser.add_argument("query", help="What to search for")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    args = parser.parse_args(argv)
    payload = search(args.query, limit=args.limit)
    print(json.dumps(payload, indent=2, default=str))
    return 0 if payload.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
