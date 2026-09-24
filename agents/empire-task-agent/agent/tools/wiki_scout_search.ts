import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import {
  isWikiLookupLocked,
  WIKI_LOOKUP_LOCK_REPLY,
} from "#lib/wiki-lookup-lock";
import { wikiScoutSearchViaMcp } from "#lib/wiki-scout-mcp";

/** Wiki Local limb — Title DNS first; Weaviate only if explicitly enabled. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("wiki_local") && !isWikiLookupLocked()
        ? defineTool({
            description:
              "Local Wikipedia lookup (Title DNS + article lead) for a subject you name.",
            inputSchema: z.object({
              query: z.string().min(1),
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
                ,
            }),
            async execute({ query, year, limit }) {
              if (isWikiLookupLocked()) {
                return WIKI_LOOKUP_LOCK_REPLY;
              }
              return wikiScoutSearchViaMcp({ query, year, limit });
            },
          })
        : null,
  },
});
