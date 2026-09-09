import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Run Research Autopilot: admit read-only limbs, query Wikipedia (Weaviate), GitHub, Product Hunt feed, optional web URL. Requires Research Partner mode ON. Never writes Cognee.",
  inputSchema: z.object({
    query: z.string().min(1).describe("Research question or search terms."),
    sources: z
      .array(z.enum(["wiki", "github", "producthunt", "web"]))
      .optional()
      .describe("Sources to query (default wiki+github+producthunt)."),
    github_limit: z.number().int().min(1).max(30).optional().describe("Max GitHub repos (default 8)."),
    web_url: z.string().optional().describe("Required when sources includes web."),
    note: z.string().optional().describe("Optional Architect note for caches."),
  }),
  async execute({ query, sources, github_limit, web_url, note }) {
    const args = [query];
    if (sources?.length) {
      args.push("--sources", sources.join(","));
    }
    if (github_limit != null) {
      args.push("--github-limit", String(github_limit));
    }
    if (web_url) {
      args.push("--web-url", web_url);
    }
    if (note) {
      args.push("--note", note);
    }
    return runPythonModule("pipeline.research_orchestrator", args);
  },
});
