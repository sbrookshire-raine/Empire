import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

/** Write an .xlsx to eve-output (openpyxl, formula-injection blocked). */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("create_spreadsheet")
        ? defineTool({
  description:
    "Write an Excel (.xlsx) file into eve-output from headers + rows. Blocks formula injection (cells starting =,+,-,@ are escaped). Pure local, offline. Never writes Cognee.",
  inputSchema: z.object({
    filename: z.string().min(1).describe("Base filename (no path); .xlsx appended if missing."),
    headers: z.array(z.string()).min(1).describe("Column headers."),
    rows: z
      .array(z.array(z.union([z.string(), z.number(), z.boolean(), z.null()])))
      .describe("Data rows (list of lists)."),
    sheet_name: z.string().optional().describe("Worksheet name (default Sheet1)."),
    note: z.string().optional().describe("Optional Architect note."),
  }),
  async execute({ filename, headers, rows, sheet_name, note }) {
    const args = [
      "--filename", filename,
      "--headers-json", JSON.stringify(headers),
      "--rows-json", JSON.stringify(rows),
    ];
    if (sheet_name) {
      args.push("--sheet", sheet_name);
    }
    if (note) {
      args.push("--note", note);
    }
    return runPythonModule("pipeline.create_spreadsheet", args);
  },
})
        : null,
  },
});
