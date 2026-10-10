import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { reaAnalyzeJavascriptViaMcp } from "#lib/rea-mcp";

/** Always registered — auto-admits REA when resource headroom allows. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      defineTool({
        description: "REA static JS/Electron/ASAR analysis (absolute path). Auto-admits REA.",
        inputSchema: z.object({
          path: z
            .string()
            .min(1)
            .describe(
              "Absolute path to app folder or ASAR on this PC (e.g. C:/apps/example).",
            ),
        }),
        async execute({ path: targetPath }) {
          const gate = await ensureLightCapability(
            "rea",
            `rea js: ${targetPath}`,
          );
          if (!gate.ok) {
            return gate;
          }
          return reaAnalyzeJavascriptViaMcp({ path: targetPath });
        },
      }),
  },
});
