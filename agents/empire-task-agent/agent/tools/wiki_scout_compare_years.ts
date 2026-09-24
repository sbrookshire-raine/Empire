import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import {
  isWikiLookupLocked,
  WIKI_LOOKUP_LOCK_REPLY,
} from "#lib/wiki-lookup-lock";
import { wikiScoutCompareYearsViaMcp } from "#lib/wiki-scout-mcp";

/** Wiki Local limb — Truth Drift compare with Wiki Interpreter. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("wiki_local") && !isWikiLookupLocked()
        ? defineTool({
            description:
              "Truth Drift compare with Wiki Interpreter across local Wikipedia years (2017/2021/2026).",
            inputSchema: z.object({
              query: z.string().min(1),
              years: z
                .string()
                .optional()
                ,
              limit_per_year: z
                .number()
                .int()
                .min(1)
                .max(10)
                .optional()
                ,
            }),
            async execute({ query, years, limit_per_year }) {
              if (isWikiLookupLocked()) {
                return {
                  ...WIKI_LOOKUP_LOCK_REPLY,
                  tool: "wiki_scout_compare_years",
                };
              }
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
