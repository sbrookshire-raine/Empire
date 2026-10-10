import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { disassemblyMarkMatureViaMcp } from "#lib/heptabase-mcp";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("heptabase")
        ? defineTool({
            description:
              "Mark a published Disassembly Card mature on Heptabase (architect_confirm required).",
            inputSchema: z.object({
              card_id: z.string().min(1),
              architect_confirm: z.boolean(),
            }),
            async execute({ card_id, architect_confirm }) {
              const gate = await ensureLightCapability(
                "heptabase",
                `disassembly mature: ${card_id}`,
              );
              if (!gate.ok) {
                return gate;
              }
              return disassemblyMarkMatureViaMcp({
                card_id,
                architect_confirm: Boolean(architect_confirm),
              });
            },
          })
        : null,
  },
});
