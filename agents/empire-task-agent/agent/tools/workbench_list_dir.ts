import { defineTool } from "eve/tools";
import { z } from "zod";
import { listWorkbenchDir, WORKBENCH_ROOTS } from "#lib/workbench";

export default defineTool({
  description:
    "List files and folders in the Empire Workbench (Memory Bank, Skills/Prompts, or Active Tools).",
  inputSchema: z.object({
    path: z
      .string()
      .describe(
        `Directory path. Roots: ${WORKBENCH_ROOTS.join(", ")}`,
      ),
  }),
  async execute({ path: dirPath }) {
    return listWorkbenchDir(dirPath);
  },
});
