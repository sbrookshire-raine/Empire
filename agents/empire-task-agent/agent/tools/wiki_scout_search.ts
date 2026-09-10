import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { wikiScoutSearchViaMcp } from "#lib/wiki-scout-mcp";

/** Wiki Local limb — Wiki Interpreter over Weaviate; opt-in via Toolbelt. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("wiki_local")
        ? defineTool({
            description:
              "Search local Wikipedia (2017/2021/2026 Weaviate). Returns title + snippet cards only. " +
              "Pass the user's question verbatim — do NOT rewrite into keyword soup. " +
              "After calling: answer in 1–3 plain sentences from snippets. " +
              "NEVER paste rank, kind_hint, rank_why, or numbered card lists to the user. " +
              "If [[EMPIRE_WIKI_LOOKUP]] snippets are already in the turn, do NOT call this tool. " +
              "Default year 2026. Does NOT write Cognee.",
            inputSchema: z.object({
              query: z.string().min(1).describe("Search query for Wikipedia."),
              year: z
                .string()
                .optional()
                .describe(
                  "Snapshot year: 2017, 2021, or 2026 (default 2026). Use other years only when the user asks.",
                ),
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
