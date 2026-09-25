import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

/**
 * Worked pathways on demand (the Architect's ask, 2026-09-24).
 *
 * The system prompt is only `eve_instructions.md` + `empire-routing.md`, so the 33
 * `agent/skills/*.md` files never entered context and "load skill-x" lines pointed at nothing. This
 * tool fetches the capability playbook instead: per area, the tool names and 3–7 worked
 * examples written as *ask → tools → artefact*, so a known route gets reused instead of a tool
 * being chosen at random. `playbook()` with no topic lists the areas.
 */
export default defineTool({
  description:
    "Look up worked examples for using a capability to actually get work done (ask -> tools -> artefact). Call with an area (e.g. wiki-archive, build-and-verify) or a tool name; omit to list areas.",
  inputSchema: z.object({
    topic: z
      .string()
      .optional()
      .describe("Area id, section title, or tool name, e.g. wiki-archive or create_spreadsheet."),
  }),
  async execute({ topic }) {
    const args = topic && topic.trim() ? [topic.trim()] : [];
    return runPythonModule("pipeline.playbook", args);
  },
});
