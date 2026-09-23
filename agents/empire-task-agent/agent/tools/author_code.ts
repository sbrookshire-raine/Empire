import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

/** Code autonomy: disposable worktree authoring with reviewable diffs. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("author_code")
        ? defineTool({
  description:
    "Author code in a disposable Git worktree. `create` makes a fresh worktree; `apply` writes one file and returns a reviewable diff; `remove` deletes a worktree. Never pushes, merges, or touches the production tree. Never writes credential files.",
  inputSchema: z.object({
    action: z.enum(["create", "apply", "remove"]).describe("Operation to perform."),
    worktree: z
      .string()
      .optional()
      .describe("Worktree path (required for apply/remove)."),
    relative_path: z
      .string()
      .optional()
      .describe("File path inside the worktree (apply only)."),
    content: z
      .string()
      .optional()
      .describe("File content (apply only)."),
    note: z.string().optional().describe("Optional note (create only)."),
  }),
  async execute({ action, worktree, relative_path, content, note }) {
    if (action === "create") {
      const args = ["create"];
      if (note) args.push("--note", note);
      return runPythonModule("pipeline.author_code", args);
    }
    if (action === "remove") {
      return runPythonModule("pipeline.author_code", ["remove", worktree ?? ""]);
    }
    // apply
    return runPythonModule("pipeline.author_code", [
      "apply",
      worktree ?? "",
      relative_path ?? "",
      content ?? "",
    ]);
  },
})
        : null,
  },
});
