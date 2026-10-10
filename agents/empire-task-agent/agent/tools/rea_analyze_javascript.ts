import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { reaAnalyzeJavascriptViaMcp } from "#lib/rea-mcp";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("rea")
        ? defineTool({
            description:
              "Statically analyze a local JavaScript or Electron app directory (or extracted ASAR) with REA. " +
              "Returns modules, imports, and evidence. Path must be absolute. Requires REA limb enabled.",
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
          })
        : null,
  },
});
