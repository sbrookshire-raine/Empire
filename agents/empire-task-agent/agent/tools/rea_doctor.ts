import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { reaDoctorViaMcp } from "#lib/rea-mcp";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("rea")
        ? defineTool({
            description:
              "Check REA (Reverse Engineer Anything) readiness: Node, registrations, and analysis engines. " +
              "Enable the REA Toolbelt limb first. Local-only; does not upload targets.",
            inputSchema: z.object({}),
            async execute() {
              const gate = await ensureLightCapability("rea", "rea doctor");
              if (!gate.ok) {
                return gate;
              }
              return reaDoctorViaMcp();
            },
          })
        : null,
  },
});
