import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Release session-scoped capability grants (after admit_for_goal / Research Autopilot). Call when scout work is finished so limbs do not linger.",
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
