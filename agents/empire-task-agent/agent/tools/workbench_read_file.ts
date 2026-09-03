import { defineTool } from "eve/tools";
import { z } from "zod";
import { readWorkbenchFile } from "#lib/workbench";

export default defineTool({
  description:
    "Read a text file from the Empire Workbench (max 512 KiB per call; use for flattened codebases and notes).",
  inputSchema: z.object({
    path: z.string().describe("Full path to a file under the Workbench roots."),
    maxBytes: z
      .number()
      .int()
      .min(1024)
      .max(2 * 1024 * 1024)
      .optional()
      .describe("Optional read limit in bytes (default 512 KiB)."),
  }),
  async execute({ path: filePath, maxBytes }) {
    return readWorkbenchFile(filePath, maxBytes);
  },
});
