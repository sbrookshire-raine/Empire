import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { dazeFreeWindowsViaMcp } from "#lib/daze-mcp";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("time_reclaim")
        ? defineTool({
            description:
              "Compute free time arcs in the DAZE day for coaching (exercise/meditation). Requires Time Reclaim Toolbelt.",
            inputSchema: z.object({
              date: z
                .string()
                .optional()
                .describe(
                  "YYYY-MM-DD only. Omit entirely for today — never pass 'today' or natural language.",
                ),
              phase: z.string().optional().describe("planned|actual (default planned)."),
              min_minutes: z
                .number()
                .int()
                .min(5)
                .max(240)
                .optional()
                .describe("Minimum free window length (default 30)."),
            }),
            async execute({ date, phase, min_minutes }) {
              return dazeFreeWindowsViaMcp({ date, phase, min_minutes });
            },
          })
        : null,
  },
});
