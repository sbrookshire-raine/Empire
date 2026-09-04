import { defineTool } from "eve/tools";
import { z } from "zod";
import { checkWorkbenchHealthViaMcp } from "#lib/workbench-mcp";

/** Core diagnostic — always registered (not a Toolbelt limb). */
export default defineTool({
  description:
    "Check local EMPIRE Workbench health: path online, disk free space, Active Tools count, and folder entry counts under C:/Empire_Workbench.",
  inputSchema: z.object({}),
  async execute() {
    return checkWorkbenchHealthViaMcp();
  },
});
