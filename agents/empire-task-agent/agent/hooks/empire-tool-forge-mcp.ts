import { defineHook } from "eve/hooks";
import {
  connectEmpireToolForgeMcp,
  disconnectEmpireToolForgeMcp,
} from "#lib/tool-forge-mcp";

export default defineHook({
  events: {
    async "session.started"() {
      try {
        await connectEmpireToolForgeMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(`[eve] empire-tool-forge MCP connect failed: ${message}`);
      }
    },
    async "session.completed"() {
      try {
        await disconnectEmpireToolForgeMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(
          `[eve] empire-tool-forge MCP disconnect failed: ${message}`,
        );
      }
    },
  },
});
