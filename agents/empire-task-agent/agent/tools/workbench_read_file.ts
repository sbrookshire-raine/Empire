import { defineTool } from "eve/tools";
import { z } from "zod";
import { readWorkbenchFile, WORKBENCH_ROOT } from "#lib/workbench";

export default defineTool({
  description:
    `Read a text file under the local Windows workbench at ${WORKBENCH_ROOT} (max 512 KiB). Pass ONLY a relative path (e.g. 00_Resource_Queue/notes.md). Never pass /home/vercel-sandbox or absolute C:\\ paths.`,
  inputSchema: z.object({
    path: z
      .string()
      .min(1)
      .describe(
        `Relative file path under ${WORKBENCH_ROOT} only. Example: 00_Resource_Queue/system_ping.py`,
      ),
    maxBytes: z
      .number()
      .int()
      .min(1024)
      .max(2 * 1024 * 1024)
      .optional()
      .describe("Optional read limit in bytes (default 512 KiB)."),
  }),
  async execute({ path: filePath, maxBytes }) {
    try {
      return await readWorkbenchFile(filePath, maxBytes);
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      return {
        ok: false,
        error: message,
        workbenchRoot: WORKBENCH_ROOT,
        requested: filePath,
      };
    }
  },
});
