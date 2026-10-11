import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";

/** Always registered — one tool for web + GitHub intake → cards → optional Heptabase → optional memory. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      defineTool({
        description:
          "Intake a web page or GitHub repos into Disassembly Cards (analyze/learn pipeline). " +
          "Web: fetch+card. GitHub: scout search or single repo; depth study shallow-clones to Resource Queue. " +
          "Heptabase when architect_confirm=true. Memory: promote_memory stages; promote_confirm+confirm promotes to eve_memory and marks card mature. " +
          "Call this instead of chaining scout/farm/write/publish manually.",
        inputSchema: z.object({
          kind: z.enum(["web", "github"]).describe("web = URL fetch; github = search or repo slug."),
          url: z.string().optional().describe("Required for kind=web."),
          query: z
            .string()
            .optional()
            .describe("GitHub search keywords (kind=github). Omit with repo for catalog status."),
          repo: z
            .string()
            .optional()
            .describe("Single repo owner/name or github.com URL (kind=github)."),
          depth: z
            .enum(["scout", "study"])
            .optional()
            .describe("github only: scout=README ticket; study=shallow clone + study card (default scout)."),
          search_limit: z.number().int().min(1).max(30).optional(),
          max_new_cards: z.number().int().min(0).max(15).optional(),
          architect_confirm: z
            .boolean()
            .optional()
            .describe("true when Architect said yes to Heptabase publish / memory promote this turn."),
          publish_heptabase: z.boolean().optional(),
          promote_memory: z
            .boolean()
            .optional()
            .describe("Stage card summary to eve_staging (propose_remember)."),
          promote_confirm: z
            .boolean()
            .optional()
            .describe("With architect_confirm: confirm to eve_memory + mark Heptabase card mature."),
          note: z.string().optional(),
        }),
        async execute({
          kind,
          url,
          query,
          repo,
          depth,
          search_limit,
          max_new_cards,
          architect_confirm,
          publish_heptabase,
          promote_memory,
          promote_confirm,
          note,
        }) {
          const label =
            kind === "web"
              ? `intake web: ${(url || "").slice(0, 80)}`
              : `intake github: ${repo || query || "catalog"}`;
          if (kind === "web") {
            const gate = await ensureLightCapability("web_scout", label);
            if (!gate.ok) return gate;
          } else {
            const gh = await ensureLightCapability("github_scout", label);
            if (!gh.ok) return gh;
          }
          if (architect_confirm && publish_heptabase !== false) {
            const hb = await ensureLightCapability("heptabase", label);
            if (!hb.ok) return hb;
          }

          const args = ["--kind", kind];
          if (url?.trim()) args.push("--url", url.trim());
          if (query?.trim()) args.push("--query", query.trim());
          if (repo?.trim()) args.push("--repo", repo.trim());
          if (depth) args.push("--depth", depth);
          if (search_limit != null) args.push("--search-limit", String(search_limit));
          if (max_new_cards != null) args.push("--max-new-cards", String(max_new_cards));
          if (architect_confirm) args.push("--architect-confirm");
          if (promote_memory) args.push("--promote-memory");
          if (promote_confirm) args.push("--promote-confirm");
          if (publish_heptabase === true) args.push("--publish-heptabase");
          if (publish_heptabase === false) args.push("--no-publish-heptabase");
          if (note?.trim()) args.push("--note", note.trim());
          return runPythonModule("pipeline.intake_to_lego", args, 360_000);
        },
      }),
  },
});
