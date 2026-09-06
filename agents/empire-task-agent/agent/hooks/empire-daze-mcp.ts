import { defineHook } from "eve/hooks";
import {
  connectEmpireDazeMcp,
  disconnectEmpireDazeMcp,
} from "#lib/daze-mcp";

export default defineHook({
  events: {
    async "session.started"() {
      try {
        await connectEmpireDazeMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(`[eve] empire-daze MCP connect failed: ${message}`);
      }
    },
    async "session.completed"() {
      try {
        await disconnectEmpireDazeMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(`[eve] empire-daze MCP disconnect failed: ${message}`);
      }
    },
  },
});
