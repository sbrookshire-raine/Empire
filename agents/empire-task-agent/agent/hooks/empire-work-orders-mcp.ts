import { defineHook } from "eve/hooks";
import {
  connectEmpireWorkOrdersMcp,
  disconnectEmpireWorkOrdersMcp,
} from "#lib/work-order-mcp";

export default defineHook({
  events: {
    async "session.started"() {
      try {
        await connectEmpireWorkOrdersMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(`[eve] empire-work-orders MCP connect failed: ${message}`);
      }
    },
    async "session.completed"() {
      try {
        await disconnectEmpireWorkOrdersMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(
          `[eve] empire-work-orders MCP disconnect failed: ${message}`,
        );
      }
    },
  },
});
