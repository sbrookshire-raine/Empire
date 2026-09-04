import { disableTool } from "eve/tools";

// Root self-delegation adds complexity and can stall local Ollama turns.
export default disableTool();
