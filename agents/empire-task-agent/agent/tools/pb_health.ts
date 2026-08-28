import { defineTool } from "eve/tools";
import { z } from "zod";
import { checkPocketBaseHealth, listTasks } from "#lib/pocketbase";

export default defineTool({
  description: "Check whether the local PocketBase API is reachable.",
  inputSchema: z.object({}),
  async execute() {
    const health = await checkPocketBaseHealth();
    return { ok: true, ...health };
  },
});
