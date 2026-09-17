import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

/** Search allowlisted local roots (read-only). */
export default defineTool({
  description:
    "Search local text across allowlisted roots (C:/Empire_Workbench, C:/EMPIRE/docs) for a literal substring. Read-only; results are redacted. Use to find notes, files, or code references locally without the network.",
  inputSchema: z.object({
    query: z.string().min(1).describe("Literal substring to search for."),
    max_results: z
      .number()
      .int()
      .min(1)
      .max(500)
      .optional()
      .describe("Max results (default 100)."),
    note: z.string().optional().describe("Optional Architect note."),
  }),
  async execute({ query, max_results, note }) {
    const args = [query];
    if (max_results != null) {
      args.push("--max-results", String(max_results));
    }
    if (note) {
      args.push("--note", note);
    }
    return runPythonModule("pipeline.workspace_search", args);
  },
});
