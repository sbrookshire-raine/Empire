import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { stemListInboxViaMcp } from "#lib/stem-factory-mcp";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("stem_factory")
        ? defineTool({
            description:
              "List songs waiting in C:/Empire_Workbench/stem_factory/input. Requires Stem Factory Toolbelt.",
            inputSchema: z.object({}),
            async execute() {
              return stemListInboxViaMcp();
            },
          })
        : null,
  },
});
