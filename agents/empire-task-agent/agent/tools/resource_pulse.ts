import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

/** Headroom + inventory so Eve knows what she has and what she can safely admit. */
export default defineTool({
  description:
    "Resource pulse: RAM/disk/GPU lease, services, effective tools, which light skills are safe to admit now, and which GPU/heavy skills need Architect OK. Call before admitting capabilities or starting heavy work. Never auto-remembers Cognee.",
  inputSchema: z.object({}),
  async execute() {
    return runPythonModule("pipeline.resource_pulse", ["pulse"]);
  },
});
