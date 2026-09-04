import { defineTool } from "eve/tools";
import { z } from "zod";
import {
  listWorkbenchDir,
  WORKBENCH_FOLDERS,
  WORKBENCH_ROOT,
} from "#lib/workbench";

export default defineTool({
  description:
    `List files and folders under the local Windows workbench at ${WORKBENCH_ROOT}. Pass ONLY a relative path (e.g. 00_Resource_Queue). Never pass /home/vercel-sandbox or absolute C:\\ paths — the tool always roots on the local machine.`,
  inputSchema: z.object({
    path: z
      .string()
      .min(1)
      .describe(
        `Relative directory under ${WORKBENCH_ROOT} only. Examples: 00_Resource_Queue, 01_Memory_Bank. Allowed tops: ${WORKBENCH_FOLDERS.join(", ")}.`,
      ),
  }),
  async execute({ path: dirPath }) {
    try {
      return await listWorkbenchDir(dirPath);
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      return {
        ok: false,
        error: message,
        workbenchRoot: WORKBENCH_ROOT,
        requested: dirPath,
      };
    }
  },
});
