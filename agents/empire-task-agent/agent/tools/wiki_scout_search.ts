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
              "Local Wikipedia lookup (Title DNS + article lead) for a subject you name. " +
              "Returns the article **lead only** — it usually will NOT contain songs, albums, " +
              "dates, or table rows. Resolve pronouns and follow-ups yourself first — pass a " +
              "self-contained subject (not \"that page\"). If the asked fact is not in the " +
              "returned lead, hop to the page that holds it (wiki_resolve + " +
              "wiki_read_section / wiki_extract) instead of guessing. " +
              "After calling: answer in 1–3 plain sentences from the result. " +
              "NEVER paste rank, kind_hint, rank_why, or numbered card lists to the user. " +
              "Do NOT tell the user to boot Weaviate/Docker for a normal who/what/cast question. " +
              "If the turn already carries [[EMPIRE_WIKI_LOOKUP]] evidence (legacy middleware), " +
              "answer from it instead of calling this. Default year 2026. Does NOT write Cognee.",
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
              if (isWikiLookupLocked()) {
                return WIKI_LOOKUP_LOCK_REPLY;
              }
              return wikiScoutSearchViaMcp({ query, year, limit });
            },
          })
        : null,
  },
});
