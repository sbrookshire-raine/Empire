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
              "Fetch a public http(s) URL and cache markdown under 04_Thought_Experiments/web_cache. Does NOT write Cognee. Requires Web Scout Toolbelt.",
            inputSchema: z.object({
              url: z.string().url().describe("http(s) URL to scout."),
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
