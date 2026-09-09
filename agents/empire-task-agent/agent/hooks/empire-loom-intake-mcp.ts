import { defineHook } from "eve/hooks";
import {
  connectEmpireLoomIntakeMcp,
  disconnectEmpireLoomIntakeMcp,
} from "#lib/loom-intake-mcp";

export default defineHook({
  events: {
    async "session.started"() {
      try {
        await connectEmpireLoomIntakeMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(`[eve] empire-loom-intake MCP connect failed: ${message}`);
      }
    },
    async "session.completed"() {
      try {
        await disconnectEmpireLoomIntakeMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(
          `[eve] empire-loom-intake MCP disconnect failed: ${message}`,
        );
      }
    },
  },
});
