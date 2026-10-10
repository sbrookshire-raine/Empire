import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("browser_local")
        ? defineTool({
            description:
              "Playwright screenshot of allowlisted localhost URL or local HTML.",
            inputSchema: z.object({
              url: z
                .string()
                .optional()
                .describe("Allowlisted http(s) URL (e.g. http://127.0.0.1:8080/eve.html)."),
              html_path: z
                .string()
                .optional()
                .describe("Absolute path to a local .html file under Workbench or REA inbox."),
              full_page: z
                .boolean()
                .optional()
                .describe("Capture full scrollable page (default false)."),
              note: z.string().optional(),
            }),
            async execute({ url, html_path, full_page, note }) {
              const gate = await ensureLightCapability(
                "browser_local",
                `browser screenshot: ${url || html_path || "target"}`,
              );
              if (!gate.ok) {
                return gate;
              }
              const args = ["screenshot"];
              if (url) {
                args.push("--url", url);
              }
              if (html_path) {
                args.push("--html-path", html_path);
              }
              if (full_page) {
                args.push("--full-page");
              }
              if (note) {
                args.push("--note", note);
              }
              return runPythonModule("pipeline.browser_local", args);
            },
          })
        : null,
  },
});
