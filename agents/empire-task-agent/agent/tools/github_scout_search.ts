import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("github_scout")
        ? defineTool({
            description:
              "Search GitHub repositories by keyword; cache markdown under 04_Thought_Experiments/github_cache. Does NOT clone or write Cognee. Requires GitHub Scout Toolbelt or Research Partner session.",
            inputSchema: z.object({
              query: z.string().min(1).describe("Search keywords (e.g. fastmcp local mcp server)."),
              limit: z.number().int().min(1).max(30).optional().describe("Max results (default 10)."),
              note: z.string().optional().describe("Optional Architect note."),
            }),
            async execute({ query, limit, note }) {
              const args = ["search", query];
              if (limit != null) {
                args.push("--limit", String(limit));
              }
              if (note) {
                args.push("--note", note);
              }
              return runPythonModule("pipeline.github_scout", args);
            },
          })
        : null,
  },
});
