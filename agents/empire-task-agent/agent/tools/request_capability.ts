import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Request a session-scoped Toolbelt capability (read-only research limbs). Requires Research Partner mode for auto-enable categories.",
  inputSchema: z.object({
    category: z
      .string()
      .min(1)
      .describe("Toolbelt category (wiki_local, web_scout, github_scout, container_scout)."),
    reason: z.string().optional().describe("Why Eve needs this capability."),
    ttl_min: z.number().int().min(5).max(120).optional().describe("Session TTL minutes."),
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
