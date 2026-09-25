import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

/**
 * Local web search (E-35) — the capability E-34 measured as missing.
 *
 * Self-hosted SearXNG behind `scripts/start-searxng.ps1`: a query with no URL and no archive hit is
 * the one ask no tool could serve (`web_search`/`web_fetch` are disabled — the provider-managed path
 * hung local Ollama; `web_scout` needs a URL you hand it). Results are leads, not sources: open one
 * with `web_scout` before quoting it. Admits Web Research first.
 */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("web_research")
        ? defineTool({
            description:
              "Search the public web through the local SearXNG instance and get result titles + URLs + snippets. Use when the question needs current or outside knowledge; then read a page with web_scout.",
            inputSchema: z.object({
              query: z.string().describe("What to search for — a few keywords, not a URL."),
              limit: z.number().optional().describe("Max results to return (default 5, hard cap 20)."),
            }),
            async execute({ query, limit }) {
              const args = [query.trim()];
              if (limit && limit > 0) {
                args.push("--limit", String(Math.trunc(limit)));
              }
              return runPythonModule("pipeline.search_scout", args);
            },
          })
        : null,
  },
});
