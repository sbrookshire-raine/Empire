import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
              "Request a session-scoped Toolbelt capability (Research Partner Autopilot path).",
  inputSchema: z.object({
    category: z
      .string()
      .min(1)
      ,
    reason: z.string().optional(),
    ttl_min: z.number().int().min(5).max(120).optional(),
  }),
  async execute({ category, reason, ttl_min }) {
    const args = ["request", category];
    if (reason) {
      args.push("--reason", reason);
    }
    if (ttl_min != null) {
      args.push("--ttl-min", String(ttl_min));
    }
    return runPythonModule("pipeline.admission_controller", args);
  },
});
