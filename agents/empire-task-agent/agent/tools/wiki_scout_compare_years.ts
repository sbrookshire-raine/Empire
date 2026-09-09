import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { wikiScoutCompareYearsViaMcp } from "#lib/wiki-scout-mcp";

/** Wiki Local limb — Truth Drift compare with Wiki Interpreter. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("wiki_local")
        ? defineTool({
            description:
              "Truth Drift compare with Wiki Interpreter across local Wikipedia years (2017/2021/2026). " +
              "Returns cards_by_year — you MUST answer from those card titles/snippets only. " +
              "Do not invent year-by-year 'key findings' or maturity narratives without card text. " +
              "Archive years are not hypothetical futures. Does NOT write Cognee. Requires Wiki Local Toolbelt.",
            inputSchema: z.object({
              query: z.string().min(1).describe("Topic to compare across years."),
              years: z
                .string()
                .optional()
                .describe("Comma-separated years, default 2017,2021,2026."),
              limit_per_year: z
                .number()
                .int()
                .min(1)
                .max(10)
                .optional()
                .describe("Max ranked cards per year after interpret (default 4)."),
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
