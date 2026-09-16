import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

/** List Eve staging proposals awaiting Architect keep/drop. */
export default defineTool({
  description:
    "List open eve_staging proposals (id, reason, expiry). Use before asking the Architect to confirm or drop.",
  inputSchema: z.object({}),
  async execute() {
    return runPythonModule("pipeline.eve_staging", ["list"]);
  },
});
