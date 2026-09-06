import { defineHook } from "eve/hooks";
import {
  connectEmpireWikiScoutMcp,
  disconnectEmpireWikiScoutMcp,
} from "#lib/wiki-scout-mcp";

export default defineHook({
  events: {
    async "session.started"() {
      try {
        await connectEmpireWikiScoutMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(`[eve] empire-wiki-scout MCP connect failed: ${message}`);
      }
    },
    async "session.completed"() {
      try {
        await disconnectEmpireWikiScoutMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(
          `[eve] empire-wiki-scout MCP disconnect failed: ${message}`,
        );
      }
    },
  },
});
