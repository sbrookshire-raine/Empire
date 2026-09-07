import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

/** Core brain — persist Architect corrections that beat old journal distillations. */
export default defineTool({
  description:
    "Persist a durable CURRENT fact about the Architect into ARCHITECT_NOW.md (overrides old Obsidian companion distillations). Use when they correct timeline, work status, goals, or say to remember something lasting. Not Cognee; not a PocketBase task.",
  inputSchema: z.object({
    fact: z
      .string()
      .min(3)
      .describe(
        "One clear current fact, e.g. 'Fall term now; contract secured; focusing on AI development with Eve.'",
      ),
    replace_all: z
      .boolean()
      .optional()
      .describe("If true, replace the entire NOW file with this fact. Default append."),
  }),
  async execute({ fact, replace_all }) {
    const args = ["update", fact];
    if (replace_all) {
      args.push("--replace-all");
    }
    return runPythonModule("pipeline.architect_now", args, 30_000);
  },
});
