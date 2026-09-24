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
              "Read a local Wikipedia markdown page by title (Title DNS). " +
              "Optional section: cast, discography, filmography, charts, history, reception, plot, production. " +
              "Use when the landing lead is too thin for the question; pass the self-contained title. " +
              "If [[EMPIRE_WIKI_LOOKUP]] / [[EMPIRE_WIKI_EXTRACT]] evidence is already in the turn " +
              "(legacy middleware), answer from that instead of calling this. Does NOT write Cognee.",
            inputSchema: z.object({
              title: z.string().min(1).describe("Exact encyclopedia title."),
              year: z.string().optional().describe("Snapshot year (default 2026)."),
              section: z
                .string()
                .optional()
                .describe(
                  "Optional H2 section key: cast, discography, filmography, charts, history, reception, plot, production.",
                ),
              question: z
                .string()
                .optional()
                .describe("User question for section preference when section omitted."),
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
