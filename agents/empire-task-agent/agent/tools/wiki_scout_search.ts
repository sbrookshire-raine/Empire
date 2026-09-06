import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { wikiScoutSearchViaMcp } from "#lib/wiki-scout-mcp";

/** Wiki Local limb — on-demand Weaviate Wikipedia scout; opt-in via Toolbelt. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("wiki_local")
        ? defineTool({
            description:
              "Query the local Wikipedia Weaviate index (Truth Drift snapshots), cache markdown under 04_Thought_Experiments/wiki_cache, and return short summaries plus file paths. Does NOT write to Cognee. Requires Wiki Local enabled in the Workbench Toolbelt. year: 2017, 2021, or 2026.",
            inputSchema: z.object({
              query: z.string().min(1).describe("Search query for Wikipedia chunks."),
              year: z
                .string()
                .optional()
                .describe("Snapshot year: 2017, 2021, or 2026 (default 2021)."),
              limit: z
                .number()
                .int()
                .min(1)
                .max(10)
                .optional()
                .describe("Max chunks to cache (default 3)."),
            }),
            async execute({ query, year, limit }) {
              return wikiScoutSearchViaMcp({ query, year, limit });
            },
          })
        : null,
  },
});
