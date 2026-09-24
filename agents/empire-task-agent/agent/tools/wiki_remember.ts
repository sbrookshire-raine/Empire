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
              "Remember a successful Wikipedia EXTRACT (fields/tables/lists) into Cognee.",
            inputSchema: z.object({
              subject: z.string().min(1),
              year: z.string().optional(),
              dataset: z.string().optional(),
              need_hint: z.string().optional(),
              extract_id: z
                .string()
                .optional()
                ,
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
