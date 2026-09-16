import { defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Docker Hub repo detail + recent tags (e.g. semitechnologies/weaviate). " +
    "Auto-admits Container Scout when headroom allows. Cache only — never pull/run.",
  inputSchema: z.object({
    repo: z
      .string()
      .min(1)
      .describe("Image repo: namespace/name or official short name (redis)."),
    tag_limit: z
      .number()
      .int()
      .min(1)
      .max(50)
      .optional()
      .describe("Max tags to list (default 15)."),
    note: z.string().optional().describe("Optional Architect note."),
  }),
  async execute({ repo, tag_limit, note }) {
    const gate = await ensureLightCapability("container_scout", `container detail: ${repo}`);
    if (!gate.ok) {
      return gate;
    }
    const args = ["detail", repo];
    if (tag_limit != null) {
      args.push("--tag-limit", String(tag_limit));
    }
    if (note) {
      args.push("--note", note);
    }
    return runPythonModule("pipeline.container_scout", args);
  },
});
