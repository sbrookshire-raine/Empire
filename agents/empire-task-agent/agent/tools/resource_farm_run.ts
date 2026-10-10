import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";

/** Always registered — GitHub scout → scout Disassembly Cards (+ optional Heptabase). */
export default defineDynamic({
  events: {
    "turn.started": () =>
      defineTool({
        description:
          "Resource farm: search GitHub, cache READMEs, write scout Disassembly Cards for processed-material catalog. " +
          "Omit query for catalog status only. Never writes Cognee. " +
          "Heptabase: publishes new orange cards when architect_confirm=true and board is healthy.",
        inputSchema: z.object({
          query: z
            .string()
            .optional()
            .describe(
              "GitHub search keywords. Omit to list already-farmed repos and recent scout cards.",
            ),
          search_limit: z
            .number()
            .int()
            .min(1)
            .max(30)
            .optional()
            .describe("Max GitHub search hits (default 10)."),
          max_new_cards: z
            .number()
            .int()
            .min(0)
            .max(15)
            .optional()
            .describe("Max new scout cards after dedupe (default 5)."),
          architect_confirm: z
            .boolean()
            .optional()
            .describe("Required true to publish new cards to Heptabase in this run."),
          publish_heptabase: z
            .boolean()
            .optional()
            .describe(
              "true=try board when confirmed; false=local cards only; omit=auto from confirm + board health.",
            ),
          note: z.string().optional().describe("Optional note stored in GitHub cache provenance."),
        }),
        async execute({
          query,
          search_limit,
          max_new_cards,
          architect_confirm,
          publish_heptabase,
          note,
        }) {
          const label = query?.trim() ? `resource farm: ${query.trim()}` : "resource farm catalog";
          for (const category of ["github_scout", "rea"] as const) {
            const gate = await ensureLightCapability(category, label);
            if (!gate.ok) {
              return gate;
            }
          }
          if (architect_confirm && publish_heptabase !== false) {
            const hb = await ensureLightCapability("heptabase", label);
            if (!hb.ok) {
              return hb;
            }
          }

          const args: string[] = [];
          if (query?.trim()) {
            args.push(query.trim());
          }
          if (search_limit != null) {
            args.push("--search-limit", String(search_limit));
          }
          if (max_new_cards != null) {
            args.push("--max-new-cards", String(max_new_cards));
          }
          if (architect_confirm) {
            args.push("--architect-confirm");
          }
          if (publish_heptabase === true) {
            args.push("--publish-heptabase");
          }
          if (publish_heptabase === false) {
            args.push("--no-publish-heptabase");
          }
          if (note?.trim()) {
            args.push("--note", note.trim());
          }
          return runPythonModule("pipeline.resource_farm", args);
        },
      }),
  },
});
