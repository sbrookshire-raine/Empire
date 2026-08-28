import { defineTool } from "eve/tools";
import { z } from "zod";
import { getModelSuite, summarizeSuite } from "#lib/ollama";

export default defineTool({
  description:
    "Read the local model suite plan: skill routing, gaps to pull, duplicates to remove, and eveGuidance.",
  inputSchema: z.object({}),
  async execute() {
    const payload = await getModelSuite();
    return summarizeSuite(payload);
  },
});
