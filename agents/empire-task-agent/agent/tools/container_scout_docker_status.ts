import { defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "List local Docker containers matching EMPIRE names (default empire-*). " +
    "Auto-admits Container Scout when headroom allows. Status only — does not start/stop.",
  inputSchema: z.object({
    name_filter: z
      .string()
      .optional()
      .describe("Substring filter for container names (default empire-)."),
  }),
  async execute({ name_filter }) {
    const gate = await ensureLightCapability(
      "container_scout",
      "container docker-status",
    );
    if (!gate.ok) {
      return gate;
    }
    const args = ["docker-status"];
    if (name_filter) {
      args.push("--filter", name_filter);
    }
    return runPythonModule("pipeline.container_scout", args);
  },
});
