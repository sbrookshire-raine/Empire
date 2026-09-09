import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { stemStatusViaMcp } from "#lib/stem-factory-mcp";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("stem_factory")
        ? defineTool({
            description:
              "Check Stem Factory (Shard of the Division) readiness and inbox song count. Requires Stem Factory Toolbelt.",
            inputSchema: z.object({}),
            async execute() {
              return stemStatusViaMcp();
            },
          })
        : null,
  },
});
