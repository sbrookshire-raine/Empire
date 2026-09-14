import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Explicitly remember one Wikipedia page lead into Cognee (eve_memory). " +
    "Only when the Architect asks to save/keep/remember a lookup. " +
    "Title DNS + lead only — never the full article, never automatic, never bulk.",
  inputSchema: z.object({
    subject: z.string().min(1).describe("Encyclopedia title or the subject just looked up."),
    year: z
      .string()
      .optional()
      .describe("Snapshot year (default 2026)."),
    dataset: z
      .string()
      .optional()
      .describe("Cognee dataset (default eve_memory)."),
  }),
  async execute({ subject, year, dataset }) {
    const args = ["remember", subject];
    if (year) {
      args.push("--year", year);
    }
    if (dataset) {
      args.push("--dataset", dataset);
    }
    return runPythonModule("pipeline.wiki_title_dns", args);
  },
});
