import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("browser_local")
        ? defineTool({
            description:
              "Fetch title/text from an allowlisted localhost EMPIRE URL (Workbench/PocketBase). Blocks other origins. No form submit. No Cognee. Requires Browser Local Toolbelt.",
            inputSchema: z.object({
              url: z.string().url(),
              note: z.string().optional(),
            }),
            async execute({ url, note }) {
              const args = [url];
              if (note) {
                args.push("--note", note);
              }
              return runPythonModule("pipeline.browser_local", args);
            },
          })
        : null,
  },
});
