import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

/** The Architect's decoded ledger: mechanism + Universal Primitives + sibling, per thing. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("thought_experiments")
        ? defineTool({
            description:
              "Search the Architect's primitive ledger — every decoded thing with its mechanism, " +
              "Universal Primitives, and a sibling from another domain. Use for idea transfer " +
              '("does X apply to Y?"), cross-domain questions, and naming the mechanism underneath ' +
              "something. Returns the ledger's own vocabulary so you can speak its language.",
            inputSchema: z.object({
              text: z
                .string()
                .optional()
                .describe("What to look up, e.g. 'juggling timing rhythm' or 'pencil'."),
              primitive: z
                .string()
                .optional()
                .describe("Exact primitive name filter, e.g. 'Timing & Sync'."),
              domain: z.string().optional().describe("Domain filter, e.g. 'mechanical', 'software'."),
              limit: z.number().int().min(1).max(25).optional(),
            }),
            async execute({ text, primitive, domain, limit }) {
              const args = [text ?? ""];
              if (primitive) args.push("--primitive", primitive);
              if (domain) args.push("--domain", domain);
              if (limit != null) args.push("--limit", String(limit));
              return runPythonModule("pipeline.primitive_lookup", args);
            },
          })
        : null,
  },
});
