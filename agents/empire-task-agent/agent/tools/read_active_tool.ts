import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { readActiveToolViaMcp } from "#lib/workbench-mcp";

/** Tool Forge limb — heavy Active Tools reads; opt-in via Toolbelt. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("tool_forge")
        ? defineTool({
            description:
              "Read a flattened codebase or script from Empire Workbench 03_Active_Tools via the local empire-workbench MCP server (read-only). Pass the filename only, e.g. BANDAPP_flattened.txt. Requires Tool Forge enabled in the Workbench Toolbelt.",
            inputSchema: z.object({
              filename: z
                .string()
                .min(1)
                .describe(
                  "Basename or relative path under C:/Empire_Workbench/03_Active_Tools/, e.g. cursor_HOL_flattened.txt",
                ),
            }),
            async execute({ filename }) {
              return readActiveToolViaMcp(filename);
            },
          })
        : null,
  },
});
