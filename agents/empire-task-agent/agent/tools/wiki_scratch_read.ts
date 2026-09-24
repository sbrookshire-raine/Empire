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
              "Read the Wikipedia research scratchpad (bridging facts) and optional Error Book misses. " +
              "Only for multi-hop briefs after you already have page evidence from a wiki tool. " +
              "If [[EMPIRE_WIKI_EXTRACT]] or [[EMPIRE_WIKI_LOOKUP]] is already in the turn " +
              "(legacy middleware), answer from that instead of calling this. " +
              "An empty scratchpad is normal for single-page extracts. Does NOT write Cognee.",
            inputSchema: z.object({
              session_id: z.string().optional().describe("Chat session id if known."),
              include_errors: z
                .boolean()
                .optional()
                .describe("If true, include recent Error Book misses."),
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
