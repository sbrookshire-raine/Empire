import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { wikiScoutCompareYearsViaMcp } from "#lib/wiki-scout-mcp";

/** Wiki Local limb — Truth Drift compare across Wikipedia years. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("wiki_local")
        ? defineTool({
            description:
              "Compare the same topic across local Wikipedia snapshot years (2017/2021/2026), write one Truth Drift compare markdown under wiki_cache, and return a short summary. Does NOT write to Cognee. Requires Wiki Local in the Toolbelt.",
            inputSchema: z.object({
              query: z.string().min(1).describe("Topic to compare across years."),
              years: z
                .string()
                .optional()
                .describe(
                  "Comma-separated years, default 2017,2021,2026.",
                ),
              limit_per_year: z
                .number()
                .int()
                .min(1)
                .max(5)
                .optional()
                .describe("Max chunks per year (default 2)."),
            }),
            async execute({ query, years, limit_per_year }) {
              return wikiScoutCompareYearsViaMcp({
                query,
                years,
                limit_per_year,
              });
            },
          })
        : null,
  },
});
