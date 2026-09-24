import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import {
  isWikiLookupLocked,
  WIKI_LOOKUP_LOCK_REPLY,
} from "#lib/wiki-lookup-lock";
import { runPythonModule } from "#lib/python-pipeline";

/** Read a Title DNS page lead and/or named H2 section from D:\\wiki_md. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("wiki_local") && !isWikiLookupLocked()
        ? defineTool({
            description:
              "Read a local Wikipedia markdown page by title (Title DNS).",
            inputSchema: z.object({
              title: z.string().min(1),
              year: z.string().optional(),
              section: z
                .string()
                .optional()
                .describe(
                  "Optional H2 section key: cast, discography, filmography, charts, history, reception, plot, production.",
                ),
              question: z
                .string()
                .optional()
                ,
            }),
            async execute({ title, year, section, question }) {
              if (isWikiLookupLocked()) {
                return WIKI_LOOKUP_LOCK_REPLY;
              }
              const args = ["read", title];
              if (year) args.push("--year", year);
              if (section) args.push("--section", section);
              if (question) args.push("--question", question);
              return runPythonModule("pipeline.wiki_read_cli", args);
            },
          })
        : null,
  },
});
