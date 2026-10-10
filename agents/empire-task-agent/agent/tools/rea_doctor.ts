import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { reaDoctorViaMcp } from "#lib/rea-mcp";

/** Always registered — auto-admits REA when resource headroom allows. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      defineTool({
        description:
          "REA readiness (Node, engines). Call first for reverse-engineering; auto-admits REA.",
        inputSchema: z.object({}),
        async execute() {
          const gate = await ensureLightCapability("rea", "rea doctor");
          if (!gate.ok) {
            return gate;
          }
          return reaDoctorViaMcp();
        },
      }),
  },
});
