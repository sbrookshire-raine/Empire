import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import {
  isWikiLookupLocked,
  WIKI_LOOKUP_LOCK_REPLY,
} from "#lib/wiki-lookup-lock";
import { runPythonModule } from "#lib/python-pipeline";

/** Exact Title DNS resolve (phone book). Does not read article body or Cognee. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("wiki_local") && !isWikiLookupLocked()
        ? defineTool({
            description:
              "Resolve whether a Wikipedia title exists in the local Title DNS phone book.",
            inputSchema: z.object({
              subject: z.string().min(1),
              year: z.string().optional(),
              question: z.string().optional(),
            }),
            async execute({ subject, year, question }) {
              if (isWikiLookupLocked()) {
                return WIKI_LOOKUP_LOCK_REPLY;
              }
              const args = ["resolve", subject];
              if (year) args.push("--year", year);
              if (question) args.push("--question", question);
              return runPythonModule("pipeline.wiki_extract", args);
            },
          })
        : null,
  },
});
