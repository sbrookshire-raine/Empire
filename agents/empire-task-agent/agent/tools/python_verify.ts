import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

/** Verify Python in a disposable worktree (syntax + optional lint/tests). */
export default defineTool({
  description:
    "Verify Python code in a disposable worktree: syntax check (always) plus optional ruff lint and pytest/unittest. Never merges, pushes, or mutates production. Returns a report; if ok is false, do not merge.",
  inputSchema: z.object({
    worktree: z.string().min(1).describe("Worktree path to verify."),
    run_tests: z
      .boolean()
      .optional()
      .describe("Run tests too (default true)."),
  }),
  async execute({ worktree, run_tests }) {
    const args = [worktree];
    if (run_tests === false) {
      args.push("--no-tests");
    }
    return runPythonModule("pipeline.python_verify", args);
  },
});
