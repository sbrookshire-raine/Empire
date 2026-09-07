import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { wikiScoutSearchViaMcp } from "#lib/wiki-scout-mcp";

/** Wiki Local limb — Wiki Interpreter over Weaviate; opt-in via Toolbelt. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("wiki_local")
        ? defineTool({
            description:
              "Wiki Interpreter: search the local Wikipedia Weaviate archive (2017/2021/2026). " +
              "Retrieves a wide candidate pool, ranks with Wikipedia heuristics (+ optional BGE rerank), " +
              "and returns structured cards (title, kind_hint, rank_why, snippet) plus cache paths. " +
              "Cards are page/chunk hits — NOT footnote/reference counts. Snapshot years are frozen " +
              "encyclopedia dumps, never 'hypothetical' unless the text says so. Does NOT write Cognee. " +
              "Requires Wiki Local Toolbelt. year: 2017, 2021, or 2026.",
            inputSchema: z.object({
              query: z.string().min(1).describe("Search query for Wikipedia."),
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
                .describe("Max ranked cards to keep after interpret (default 5)."),
            }),
            async execute({ query, year, limit }) {
              return wikiScoutSearchViaMcp({ query, year, limit });
            },
          })
        : null,
  },
});
