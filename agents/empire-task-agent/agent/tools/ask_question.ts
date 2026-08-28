import { disableTool } from "eve/tools";

// EMPIRE Workbench uses normal chat for all user input. The built-in ask_question
// tool causes malformed tool calls on local Ollama and leaks framework errors into
// the transcript. Clarify in prose instead.
export default disableTool();
