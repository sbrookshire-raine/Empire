import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("web_scout")
        ? defineTool({
            description:
              "Fetch one public http(s) page URL and cache markdown under 04_Thought_Experiments/web_cache. Not a search engine — needs a full URL. Does NOT write Cognee. Requires Web Scout Toolbelt.",
            inputSchema: z.object({
              url: z
                .string()
                .min(1)
                .describe(
                  "Full page URL to fetch (https://…). Bare domains ok; not a search query.",
                ),
              note: z.string().optional().describe("Optional Architect note."),
            }),
            async execute({ url, note }) {
              const args = [url];
              if (note) {
                args.push("--note", note);
              }
              return runPythonModule("pipeline.web_scout", args);
            },
          })
        : null,
  },
});
