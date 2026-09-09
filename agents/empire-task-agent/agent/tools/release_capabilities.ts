import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description: "Release session-scoped research capabilities (Research Autopilot TTL grants).",
  inputSchema: z.object({
    reason: z.string().optional().describe("Release reason (default manual)."),
  }),
  async execute({ reason }) {
    const args = ["release"];
    if (reason) {
      args.push("--reason", reason);
    }
    return runPythonModule("pipeline.admission_controller", args);
  },
});
