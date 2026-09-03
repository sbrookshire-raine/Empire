import { defineHook } from "eve/hooks";
import {
  connectEmpireWorkbenchMcp,
  disconnectEmpireWorkbenchMcp,
} from "#lib/workbench-mcp";

export default defineHook({
  events: {
    async "session.started"() {
      try {
        await connectEmpireWorkbenchMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(`[eve] empire-workbench MCP connect failed: ${message}`);
      }
    },
    async "session.completed"() {
      try {
        await disconnectEmpireWorkbenchMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(`[eve] empire-workbench MCP disconnect failed: ${message}`);
      }
    },
  },
});
