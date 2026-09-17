import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

/** Read a local document to text/markdown. */
export default defineTool({
  description:
    "Extract text/markdown from a local document (md/txt/csv/json/pdf/docx/pptx/xlsx/html). Uses MarkItDown with Docling fallback; read-only, offline. Returns provenance-stamped content. Never writes Cognee.",
  inputSchema: z.object({
    input_path: z
      .string()
      .min(1)
      .describe("Allowlisted local file path to read."),
    max_chars: z
      .number()
      .int()
      .min(1)
      .optional()
      .describe("Max characters to return (default 200000)."),
  }),
  async execute({ input_path, max_chars }) {
    const args = [input_path];
    if (max_chars != null) {
      args.push("--max-chars", String(max_chars));
    }
    return runPythonModule("pipeline.read_document", args);
  },
});
