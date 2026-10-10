import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { disassemblyPublishHeptabaseViaMcp } from "#lib/heptabase-mcp";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("heptabase")
        ? defineTool({
            description:
              "Publish a Disassembly Card to Heptabase (architect_confirm required).",
            inputSchema: z.object({
              card_id: z.string().min(1).describe("Local disassembly card id (dc_…)."),
              architect_confirm: z
                .boolean()
                .describe("Must be true — Architect approved publish in this turn."),
            }),
            async execute({ card_id, architect_confirm }) {
              const gate = await ensureLightCapability(
                "heptabase",
                `disassembly publish: ${card_id}`,
              );
              if (!gate.ok) {
                return gate;
              }
              return disassemblyPublishHeptabaseViaMcp({
                card_id,
                architect_confirm: Boolean(architect_confirm),
              });
            },
          })
        : null,
  },
});
