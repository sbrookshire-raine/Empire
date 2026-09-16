import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isWikiLookupLocked } from "#lib/wiki-lookup-lock";
import { runPythonModule } from "#lib/python-pipeline";

/** Remember a successful structured wiki extract into Cognee (sparse). Never automatic. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      !isWikiLookupLocked()
        ? defineTool({
            description:
              "Remember a successful Wikipedia EXTRACT (fields/tables/lists) into Cognee. " +
              "Only when the Architect explicitly asks to save/keep/remember. " +
              "Rejects empty extracts. Never bulk-ingests wiki_md.",
            inputSchema: z.object({
              subject: z.string().min(1).describe("Encyclopedia title just extracted."),
              year: z.string().optional().describe("Snapshot year (default 2026)."),
              dataset: z.string().optional().describe("Cognee dataset (default eve_memory)."),
              need_hint: z.string().optional().describe("Same hint used for the extract."),
              extract_id: z
                .string()
                .optional()
                .describe("Optional extract_id from a prior wiki_extract ok result."),
            }),
            async execute({ subject, year, dataset, need_hint, extract_id }) {
              const args = ["remember", subject];
              if (year) args.push("--year", year);
              if (dataset) args.push("--dataset", dataset);
              if (need_hint) args.push("--need", need_hint);
              if (extract_id) args.push("--extract-id", extract_id);
              return runPythonModule("pipeline.wiki_extract", args);
            },
          })
        : null,
  },
});
