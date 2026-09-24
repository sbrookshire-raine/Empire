import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import {
  isWikiLookupLocked,
  WIKI_LOOKUP_LOCK_REPLY,
} from "#lib/wiki-lookup-lock";
import { runPythonModule } from "#lib/python-pipeline";

/** Read the Wikipedia research scratchpad / recent Error Book entries. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("wiki_local") && !isWikiLookupLocked()
        ? defineTool({
            description:
              "Read the Wikipedia research scratchpad (bridging facts) and optional Error Book misses.",
            inputSchema: z.object({
              session_id: z.string().optional(),
              include_errors: z
                .boolean()
                .optional()
                ,
            }),
            async execute({ session_id, include_errors }) {
              if (isWikiLookupLocked()) {
                return {
                  ...WIKI_LOOKUP_LOCK_REPLY,
                  chat_reply_rule:
                    "LOOKUP/EXTRACT evidence was already injected. " +
                    "Do NOT narrate the scratchpad. Answer only from EXTRACT/LOOKUP fields, tables, and lists.",
                };
              }
              const args = ["read"];
              if (session_id) args.push("--session", session_id);
              if (include_errors) args.push("--errors");
              return runPythonModule("pipeline.wiki_scratchpad_cli", args);
            },
          })
        : null,
  },
});
