import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Convert a local PDF/Office file to Markdown with Docling and stage it under the Resource Queue. Does not write Cognee — follow with cognee_remember or Workbench upload when ready.",
  inputSchema: z.object({
    input_path: z.string().min(1).describe("Absolute path to PDF/Office file."),
    output_path: z
      .string()
      .optional()
      .describe("Optional output .md path (default Resource Queue)."),
  }),
  async execute({ input_path, output_path }) {
    const args = [input_path];
    if (output_path) {
      args.push("-o", output_path);
    }
    return runPythonModule("pipeline.docling_convert", args, 600_000);
  },
});
