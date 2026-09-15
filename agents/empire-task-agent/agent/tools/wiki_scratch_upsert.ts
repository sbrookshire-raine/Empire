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
              "Save a short bridging fact to the Wikipedia research scratchpad for multi-hop work. " +
              "Use between hops (retain facts, drop raw markdown). Does NOT write Cognee.",
            inputSchema: z.object({
              text: z.string().min(1).describe("Bridging fact to retain."),
              title: z.string().optional().describe("Source page title."),
              session_id: z.string().optional().describe("Chat session id if known."),
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
