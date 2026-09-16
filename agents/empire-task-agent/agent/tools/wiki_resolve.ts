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
              "Resolve whether a Wikipedia title exists in the local Title DNS phone book. " +
              "Returns exact/alias/ambiguous/missing. Does NOT extract page content. Does NOT write Cognee.",
            inputSchema: z.object({
              subject: z.string().min(1).describe("Title or subject to resolve."),
              year: z.string().optional().describe("Snapshot year (default 2026)."),
              question: z.string().optional().describe("User question for disambiguation hints."),
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
