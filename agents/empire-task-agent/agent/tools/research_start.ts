import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

/**
 * Open a research desk job and leave — the deferred half of reading the web (E-37).
 *
 * Her window is ~24k tokens, about one long article, so a multi-page pass can never fit and holding
 * the turn open is what produced 300-second turns. This returns a job id immediately; a detached
 * worker fetches on CPU while the turn is closed; `research_read` returns a bounded digest later.
 *
 * Gated under Web Research so it costs no prompt budget until the limb is admitted.
 */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("web_research")
        ? defineTool({
            description:
              "Start a research job (query + URLs) and return a job id immediately. Use for slow or multi-page research instead of blocking the turn; read it back later with research_read.",
            inputSchema: z.object({
              query: z.string().describe("What the research is for — one line."),
              urls: z
                .array(z.string())
                .optional()
                .describe("Page URLs to fetch. Without one there is nothing to fetch yet (no search tool)."),
            }),
            async execute({ query, urls }) {
              const args = ["start", query.trim()];
              for (const url of urls || []) {
                if (url && url.trim()) {
                  args.push("--url", url.trim());
                }
              }
              return runPythonModule("pipeline.research_desk", args);
            },
          })
        : null,
  },
});
