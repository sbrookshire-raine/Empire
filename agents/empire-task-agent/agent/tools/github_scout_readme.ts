import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("github_scout")
        ? defineTool({
            description:
              "Fetch README excerpt for a GitHub repo (owner/name). Scratch cache only. Requires GitHub Scout Toolbelt or Research Partner session.",
            inputSchema: z.object({
              repo: z.string().min(1).describe("Repository slug owner/name (e.g. modelcontextprotocol/servers)."),
              note: z.string().optional().describe("Optional Architect note."),
            }),
            async execute({ repo, note }) {
              const args = ["readme", repo];
              if (note) {
                args.push("--note", note);
              }
              return runPythonModule("pipeline.github_scout", args);
            },
          })
        : null,
  },
});
