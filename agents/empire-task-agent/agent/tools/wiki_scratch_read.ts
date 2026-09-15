import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

/** Read the Wikipedia research scratchpad / recent Error Book entries. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("wiki_local")
        ? defineTool({
            description:
              "Read the Wikipedia research scratchpad (bridging facts) and optional Error Book misses. " +
              "Use for multi-hop briefs. Does NOT write Cognee.",
            inputSchema: z.object({
              session_id: z.string().optional().describe("Chat session id if known."),
              include_errors: z
                .boolean()
                .optional()
                .describe("If true, include recent Error Book misses."),
            }),
            async execute({ session_id, include_errors }) {
              const args = ["read"];
              if (session_id) args.push("--session", session_id);
              if (include_errors) args.push("--errors");
              return runPythonModule("pipeline.wiki_scratchpad_cli", args);
            },
          })
        : null,
  },
});
