import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import {
  isWikiLookupLocked,
  WIKI_LOOKUP_LOCK_REPLY,
} from "#lib/wiki-lookup-lock";
import { runPythonModule } from "#lib/python-pipeline";

/** Structured Wikipedia extract: Title DNS → fields/tables/lists (Evidence JSON). */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("wiki_local") && !isWikiLookupLocked()
        ? defineTool({
            description:
              "Extract structured facts from a local Wikipedia page (Title DNS).",
            inputSchema: z.object({
              subject: z.string().min(1),
              year: z.string().optional(),
              need_hint: z
                .string()
                .optional()
                .describe("Optional hint to rank fields/tables (e.g. release date, population)."),
              section: z.string().optional(),
              question: z.string().optional(),
            }),
            async execute({ subject, year, need_hint, section, question }) {
              if (isWikiLookupLocked()) {
                return WIKI_LOOKUP_LOCK_REPLY;
              }
              const args = ["extract", subject];
              if (year) args.push("--year", year);
              if (need_hint) args.push("--need", need_hint);
              if (section) args.push("--section", section);
              if (question) args.push("--question", question);
              return runPythonModule("pipeline.wiki_extract", args);
            },
          })
        : null,
  },
});
