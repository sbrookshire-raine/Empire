import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { dazeComparePhasesViaMcp } from "#lib/daze-mcp";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("time_reclaim")
        ? defineTool({
            description:
              "Compare planned vs actual DAZE day blocks for coaching (free windows, conflicts, body/rest drift). Requires Time Reclaim Toolbelt.",
            inputSchema: z.object({
              date: z
                .string()
                .optional()
                .describe(
                  "YYYY-MM-DD only. Omit entirely for today — never pass 'today' or natural language.",
                ),
            }),
            async execute({ date }) {
              return dazeComparePhasesViaMcp({ date });
            },
          })
        : null,
  },
});
