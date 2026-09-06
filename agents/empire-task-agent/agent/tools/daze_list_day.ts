import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { dazeListDayViaMcp } from "#lib/daze-mcp";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("time_reclaim")
        ? defineTool({
            description:
              "List DAZE day_blocks for a date (YYYY-MM-DD, default today). Requires Time Reclaim Toolbelt limb. Returns blocks + conflicts.",
            inputSchema: z.object({
              date: z.string().optional().describe("YYYY-MM-DD (default today)."),
              phase: z
                .string()
                .optional()
                .describe("planned or actual (optional filter)."),
            }),
            async execute({ date, phase }) {
              return dazeListDayViaMcp({ date, phase });
            },
          })
        : null,
  },
});
