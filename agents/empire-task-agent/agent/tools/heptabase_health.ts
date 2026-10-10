import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { heptabaseHealthViaMcp } from "#lib/heptabase-mcp";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("heptabase")
        ? defineTool({
            description: "Heptabase CLI + catalog board readiness.",
            inputSchema: z.object({}),
            async execute() {
              const gate = await ensureLightCapability("heptabase", "heptabase health");
              if (!gate.ok) {
                return gate;
              }
              return heptabaseHealthViaMcp();
            },
          })
        : null,
  },
});
