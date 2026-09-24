import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

/**
 * Deep execution syntax on demand (refactor plan R-03).
 *
 * Tool documentation used to sit in the hot prompt: every turn paid for the full prose of every
 * enabled tool. Now the schema carries a one-line cue and this tool fetches the detail — call it
 * only when a call needs more than the cue (parameter semantics, gotchas), not before every tool
 * use. `tool_docs()` with no name lists what is documented.
 */
export default defineTool({
  description:
    "Look up deep syntax for one tool (parameters, semantics, gotchas) when a call needs more than its one-line cue.",
  inputSchema: z.object({
    name: z
      .string()
      .optional()
      .describe("Tool name to document, e.g. wiki_read_section. Omit to list all…"),
  }),
  async execute({ name }) {
    const args = name && name.trim() ? [name.trim()] : [];
    return runPythonModule("pipeline.tool_docs_cli", args);
  },
});