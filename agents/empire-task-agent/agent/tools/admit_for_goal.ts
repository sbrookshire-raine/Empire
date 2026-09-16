import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

/**
 * Resource-gated session admit for light skills (policy B).
 * Does not require Research Partner toggle. GPU/heavy → need_architect.
 */
export default defineTool({
  description:
    "Admit a light session skill for the current goal when resource_pulse headroom is OK (GitHub/Web/Container scout, etc.). Does not require Research Partner. If need_architect is true, ask the Architect — do not force GPU/Vision/Stem. Never writes Cognee.",
  inputSchema: z.object({
    category: z
      .string()
      .min(1)
      .describe("Toolbelt category to admit (e.g. github_scout, web_scout, container_scout)."),
    reason: z.string().optional().describe("Why this skill is needed for the goal."),
    ttl_min: z.number().int().min(5).max(120).optional().describe("Session TTL minutes."),
  }),
  async execute({ category, reason, ttl_min }) {
    const args = ["admit", category];
    if (reason) {
      args.push("--reason", reason);
    }
    if (ttl_min != null) {
      args.push("--ttl-min", String(ttl_min));
    }
    return runPythonModule("pipeline.resource_pulse", args);
  },
});
