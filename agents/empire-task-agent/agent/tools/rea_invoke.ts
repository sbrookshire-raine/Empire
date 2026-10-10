import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { reaBinarySessionViaMcp, reaInvokeViaMcp } from "#lib/rea-mcp";

/** Always registered — auto-admits REA when resource headroom allows. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      defineTool({
        description:
          "Invoke a REA MCP tool by name (after rea_doctor). Auto-admits REA; local only.",
        inputSchema: z.object({
          tool: z
            .string()
            .min(1)
            .describe(
              "REA MCP tool name (e.g. inspect, decompile, analyze_javascript_application).",
            ),
          arguments: z
            .record(z.string(), z.unknown())
            .optional()
            .describe("Tool arguments object (default {})."),
        }),
        async execute({ tool, arguments: toolArgs }) {
          const gate = await ensureLightCapability("rea", `rea ${tool}`);
          if (!gate.ok) {
            return gate;
          }
          if (tool === "binary_session") {
            return reaBinarySessionViaMcp();
          }
          return reaInvokeViaMcp({
            tool,
            arguments: toolArgs ?? {},
          });
        },
      }),
  },
});
