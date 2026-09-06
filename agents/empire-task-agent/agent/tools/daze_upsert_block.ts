import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { dazeUpsertBlockViaMcp } from "#lib/daze-mcp";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("time_reclaim")
        ? defineTool({
            description:
              "Create or update a DAZE day block (start/end minutes 0–1440). Requires Time Reclaim Toolbelt. Use for scheduling focus/body/rest arcs.",
            inputSchema: z.object({
              title: z.string().min(1),
              start_minute: z.number().int().min(0).max(1439),
              end_minute: z.number().int().min(1).max(1440),
              date: z.string().optional().describe("YYYY-MM-DD (default today)."),
              kind: z
                .string()
                .optional()
                .describe("focus|body|admin|creative|rest|other"),
              phase: z.string().optional().describe("planned|actual"),
              notes: z.string().optional(),
              record_id: z
                .string()
                .optional()
                .describe("If set, PATCH existing record."),
            }),
            async execute(input) {
              return dazeUpsertBlockViaMcp(input);
            },
          })
        : null,
  },
});
