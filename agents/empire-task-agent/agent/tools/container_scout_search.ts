import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("container_scout")
        ? defineTool({
            description:
              "Search Docker Hub by keyword; cache markdown under 04_Thought_Experiments/container_cache. Does NOT pull images or write Cognee. Requires Container Scout Toolbelt.",
            inputSchema: z.object({
              query: z.string().min(1).describe("Search keywords (e.g. weaviate, vector database)."),
              limit: z.number().int().min(1).max(25).optional().describe("Max results (default 10)."),
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
              return runPythonModule("pipeline.container_scout", args);
            },
          })
        : null,
  },
});
