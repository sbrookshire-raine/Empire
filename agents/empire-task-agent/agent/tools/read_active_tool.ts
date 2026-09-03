import { defineTool } from "eve/tools";
import { z } from "zod";
import { readActiveToolViaMcp } from "#lib/workbench-mcp";

export default defineTool({
  description:
    "Read a flattened codebase or script from Empire Workbench 03_Active_Tools via the local empire-workbench MCP server (read-only). Pass the filename only, e.g. BANDAPP_flattened.txt.",
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
});
