import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { docsGuideScrapeViaMcp } from "#lib/tool-forge-mcp";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("tool_forge")
        ? defineTool({
            description:
              "Scrape an official documentation site into one Markdown guide under harvest_cache (llms.txt / sitemap discovery). Does not auto-ingest to Cognee. Requires Tool Forge Toolbelt.",
            inputSchema: z.object({
              root_url: z
                .string()
                .url()
                .describe("Documentation root URL, e.g. https://docs.example.com"),
              max_pages: z
                .number()
                .int()
                .min(1)
                .max(300)
                .optional()
                .describe("Page cap (default 80)."),
              note: z.string().optional().describe("Optional provenance note."),
            }),
            async execute({ root_url, max_pages, note }) {
              return docsGuideScrapeViaMcp({ root_url, max_pages, note });
            },
          })
        : null,
  },
});
