import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { getModelSuite, summarizeSuite } from "#lib/ollama";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("system_ops")
        ? defineTool({
  description:
    "Read the local model suite plan: skill routing, gaps to pull, duplicates to remove, and eveGuidance.",
  inputSchema: z.object({}),
  async execute() {
    const payload = await getModelSuite();
    return summarizeSuite(payload);
  },
})
        : null,
  },
});
