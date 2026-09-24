import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

/** Persist a bridging fact into the Wikipedia research scratchpad. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("wiki_local")
        ? defineTool({
            description:
              "Save a short bridging fact to the Wikipedia research scratchpad for multi-hop work.",
            inputSchema: z.object({
              text: z.string().min(1),
              title: z.string().optional(),
              session_id: z.string().optional(),
            }),
            async execute({ text, title, session_id }) {
              const args = ["upsert", text];
              if (title) args.push("--title", title);
              if (session_id) args.push("--session", session_id);
              return runPythonModule("pipeline.wiki_scratchpad_cli", args);
            },
          })
        : null,
  },
});
