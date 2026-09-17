import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

/** Stop managed services a task no longer needs. Never stops Eve or Ollama. */
export default defineTool({
  description:
    "Release EMPIRE managed services a task no longer needs (pocketbase, frontend). Never stops Ollama or Eve. Defaults to dry-run planning; pass dry_run=false to actually stop.",
  inputSchema: z.object({
    services: z
      .array(z.string())
      .min(1)
      .describe("Service ids to release, e.g. ['frontend']."),
    dry_run: z
      .boolean()
      .optional()
      .describe("Plan only (default true). Set false to actually stop."),
  }),
  async execute({ services, dry_run }) {
    const args = ["release", ...services];
    if (dry_run !== false) {
      args.push("--dry-run");
    }
    return runPythonModule("pipeline.switchboard", args);
  },
});
