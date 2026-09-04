import { disableTool } from "eve/tools";

// Provider-managed web_search is unsupported on local Ollama (causes AI SDK warnings / hangs).
export default disableTool();
