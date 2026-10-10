import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { reaBinarySessionViaMcp, reaInvokeViaMcp } from "#lib/rea-mcp";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("rea")
        ? defineTool({
            description:
              "Call any REA MCP tool by name (reverse engineering: native, web, .NET, firmware, etc.). " +
              "Use rea_doctor first; use rea_binary_session (via tool binary_session) to see availability. " +
              "Arguments must match REA's schema for that tool. Local analysis only.",
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
          })
        : null,
  },
});
