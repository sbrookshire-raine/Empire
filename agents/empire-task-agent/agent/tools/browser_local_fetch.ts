import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("browser_local")
        ? defineTool({
            description: "Fetch title/text from an allowlisted localhost EMPIRE URL.",
            inputSchema: z.object({
              url: z.string().url(),
              note: z.string().optional(),
            }),
            async execute({ url, note }) {
              const gate = await ensureLightCapability(
                "browser_local",
                `browser fetch: ${url}`,
              );
              if (!gate.ok) {
                return gate;
              }
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
