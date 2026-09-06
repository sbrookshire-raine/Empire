import { defineHook } from "eve/hooks";
import {
  connectEmpireStemFactoryMcp,
  disconnectEmpireStemFactoryMcp,
} from "#lib/stem-factory-mcp";

export default defineHook({
  events: {
    async "session.started"() {
      try {
        await connectEmpireStemFactoryMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(
          `[eve] empire-stem-factory MCP connect failed: ${message}`,
        );
      }
    },
    async "session.completed"() {
      try {
        await disconnectEmpireStemFactoryMcp();
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.warn(
          `[eve] empire-stem-factory MCP disconnect failed: ${message}`,
        );
      }
    },
  },
});
