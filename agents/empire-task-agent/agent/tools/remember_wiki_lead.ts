import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isWikiLookupLocked } from "#lib/wiki-lookup-lock";
import { runPythonModule } from "#lib/python-pipeline";

export default defineDynamic({
  events: {
    "turn.started": () =>
      !isWikiLookupLocked()
        ? defineTool({
            description:
              "Explicitly remember one Wikipedia page lead into Cognee (eve_memory).",
            inputSchema: z.object({
              subject: z.string().min(1),
              year: z.string().optional(),
              dataset: z.string().optional(),
            }),
            async execute({ subject, year, dataset }) {
              const args = ["remember", subject];
              if (year) args.push("--year", year);
              if (dataset) args.push("--dataset", dataset);
              return runPythonModule("pipeline.wiki_title_dns", args);
            },
          })
        : null,
  },
});
