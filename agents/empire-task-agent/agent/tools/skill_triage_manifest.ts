import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { skillTriageManifestViaMcp } from "#lib/tool-forge-mcp";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("tool_forge")
        ? defineTool({
            description:
              "Inventory SKILL.md files and run Build1 3-Bin heuristic triage. Writes skill_triage_manifest.json + SKILL_TRIAGE_MANIFEST.md under harvest_cache. Requires Tool Forge Toolbelt.",
            inputSchema: z.object({
              paths: z
                .string()
                .optional()
                .describe(
                  "Comma-separated zip files or directories to scan (optional).",
                ),
              include_installed: z
                .boolean()
                .optional()
                .describe(
                  "Also scan C:/EMPIRE/.cursor/skills (default true).",
                ),
            }),
            async execute({ paths, include_installed }) {
              return skillTriageManifestViaMcp({
                paths,
                include_installed,
              });
            },
          })
        : null,
  },
});
