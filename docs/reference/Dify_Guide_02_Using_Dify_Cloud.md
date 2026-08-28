# Dify Documentation — Using Dify Cloud (User Guide)

*This document was scraped from the official Dify documentation and cleaned/reformatted for ingestion into NotebookLM (for building a learning plan). It is part of a multi-file set covering the full Dify docs guide.*

- **Source:** https://docs.dify.ai/en/home
- **Total pages in this file:** 90
- **Date scraped:** 2026-07-18

## Table of Contents

- **[Using Dify Cloud](#using-dify-cloud)**
  - [Build](#build)
    - [App Toolkit](#app-toolkit)
    - [Agent](#agent)
    - [Chatbot](#chatbot)
    - [Orchestration Logic](#orchestration-logic)
    - [Handle Errors](#handle-errors)
    - [Hotkeys](#hotkeys)
    - [Text Generator](#text-generator)
    - [Version Control](#version-control)
    - [Workflow & Chatflow](#workflow-chatflow)
  - [Debug](#debug)
    - [Error Types](#error-types)
    - [Run History](#run-history)
    - [Single Node](#single-node)
    - [Variable Inspector](#variable-inspector)
  - [Getting Started](#getting-started)
    - [Use Dify](#use-dify)
  - [Knowledge](#knowledge)
    - [Connect to External Knowledge Base](#connect-to-external-knowledge-base)
    - [Configure the Chunk Settings](#configure-the-chunk-settings)
    - [Upload Local Files](#upload-local-files)
    - [Sync Data from Notion](#sync-data-from-notion)
    - [Import Data from Website](#import-data-from-website)
    - [Create a Ready-to-Use Knowledge Base](#create-a-ready-to-use-knowledge-base)
    - [Specify the Index Method and Retrieval Settings](#specify-the-index-method-and-retrieval-settings)
    - [External Knowledge API](#external-knowledge-api)
    - [Integrate Knowledge within Apps](#integrate-knowledge-within-apps)
    - [Authorize Data Source](#authorize-data-source)
    - [Step 1: Create Knowledge Pipeline](#step-1-create-knowledge-pipeline)
    - [Step 2: Orchestrate Knowledge Pipeline](#step-2-orchestrate-knowledge-pipeline)
    - [Step 5: Manage and Use Knowledge Base](#step-5-manage-and-use-knowledge-base)
    - [Step 3: Publish Knowledge Pipeline](#step-3-publish-knowledge-pipeline)
    - [Build a Custom Knowledge Base](#build-a-custom-knowledge-base)
    - [Step 4: Upload Files](#step-4-upload-files)
    - [Knowledge Request Rate Limit](#knowledge-request-rate-limit)
    - [Manage Knowledge Settings](#manage-knowledge-settings)
    - [Manage Knowledge Content](#manage-knowledge-content)
    - [Manage Document Metadata](#manage-document-metadata)
    - [Knowledge](#knowledge-1)
    - [Test Knowledge Retrieval](#test-knowledge-retrieval)
  - [Monitor](#monitor)
    - [Dashboard](#dashboard)
    - [Annotation System](#annotation-system)
    - [Integrate with Alibaba Cloud Monitor](#integrate-with-alibaba-cloud-monitor)
    - [Integrate with Arize](#integrate-with-arize)
    - [Integrate with Langfuse](#integrate-with-langfuse)
    - [Integrate with LangSmith](#integrate-with-langsmith)
    - [Integrate with Opik](#integrate-with-opik)
    - [Integrate with Phoenix](#integrate-with-phoenix)
    - [Integrate with W&B Weave](#integrate-with-wb-weave)
    - [Logs](#logs)
  - [Nodes](#nodes)
    - [Agent](#agent-1)
    - [Answer](#answer)
    - [Code](#code)
    - [Document Extractor](#document-extractor)
    - [HTTP Request](#http-request)
    - [Human Input](#human-input)
    - [If-Else](#if-else)
    - [Iteration](#iteration)
    - [Knowledge Retrieval](#knowledge-retrieval)
    - [List Operator](#list-operator)
    - [LLM](#llm)
    - [Loop](#loop)
    - [Output](#output)
    - [Parameter Extractor](#parameter-extractor)
    - [Question Classifier](#question-classifier)
    - [Start Node](#start-node)
    - [Template](#template)
    - [Tool Node](#tool-node)
    - [Trigger](#trigger)
    - [Integration Trigger](#integration-trigger)
    - [Schedule Trigger](#schedule-trigger)
    - [Webhook Trigger](#webhook-trigger)
    - [User Input](#user-input)
    - [Variable Aggregator](#variable-aggregator)
    - [Variable Assigner](#variable-assigner)
  - [Publish](#publish)
    - [Overview](#overview)
    - [MCP Server](#mcp-server)
    - [Publish Apps to Marketplace](#publish-apps-to-marketplace)
    - [Chat Web Apps](#chat-web-apps)
    - [Embed Your Web App](#embed-your-web-app)
    - [Settings](#settings)
    - [Workflow Web Apps](#workflow-web-apps)
  - [Workspace](#workspace)
    - [Custom Endpoints](#custom-endpoints)
    - [Deploy Custom Endpoints Using Cloudflare Workers](#deploy-custom-endpoints-using-cloudflare-workers)
    - [External Data Tool](#external-data-tool)
    - [Sensitive Content Moderation](#sensitive-content-moderation)
    - [Manage Apps](#manage-apps)
    - [Model Providers](#model-providers)
    - [Personal Settings](#personal-settings)
    - [Integrations](#integrations)
    - [Overview](#overview-1)
    - [Billing](#billing)
    - [Manage Members](#manage-members)
    - [Dify Tools](#dify-tools)

---

## Using Dify Cloud

### Build

#### App Toolkit

*Optional features that make your Dify apps more useful*

**Source:** https://docs.dify.ai/en/cloud/use-dify/build/additional-features

Optional features that make your Dify apps more useful

Dify apps come with optional features you can enable to improve the end-user experience. Open the **Features** panel of the builder to see what's available for your app type.

      *[Image: Features Panel in Chatbots, Agents, and Text Generators]*

      *[Image: Features Panel in Chatflows]*

#### Conversation Opener

Set an opening message that greets users at the start of each conversation, with optional suggested questions to guide them toward what the app does well.

You can insert variables into the opening message and suggested questions to personalize the experience.

* In the opening message, type `{` or `/` to insert variables from the picker.

* In suggested questions, type variable names manually in `{{variable_name}}` format.

      *[Image: Configuration]*

      *[Image: WebApp]*

#### Follow-up

When enabled, follow-up questions are generated after each response to help users continue the conversation.

Click **Settings** to pick the model that generates the questions, or write a custom prompt (up to 1,000 characters) to adjust the number, wording, or length of the questions.

#### Text to Speech

Convert AI responses to audio. You can configure the language and voice to match your app's audience, and enable **Auto Play** to stream audio automatically as the AI responds.

> **ℹ️ Info:**
>   **Text to Speech** uses your workspace's text-to-speech model (set in **Integrations** > **Model Provider** > **Default Models**).
>
>   The feature only appears in the **Features** panel when a default TTS model is configured.

#### Speech to Text

Enable voice input for the chat interface. When enabled, your end users can dictate messages instead of typing by clicking the microphone button.

> **ℹ️ Info:**
>   **Speech to Text** uses your workspace's speech-to-text model (set in **Integrations** > **Model Provider** > **Default Models**).
>
>   The feature only appears in the **Features** panel when a default STT model is configured.

#### File Upload

Allow end users to send files at any point during a conversation. You can configure which file types to accept, the upload method, and the maximum number of files per message.

Per-file size limits:

* Images: 10 MB
* Documents: 15 MB
* Audio: 50 MB
* Video: 100 MB

#### Citations and Attributions

Show the source documents behind AI responses. When enabled, responses that draw from a connected knowledge base display numbered citations linking back to the original documents and chunks.

  *[Image: Citations and Attributions]*

#### Content Moderation

Filter inappropriate content in user inputs, AI outputs, or both. Choose a moderation provider based on your needs:

* **OpenAI Moderation**: Use OpenAI's dedicated moderation model to detect harmful content across multiple categories.

* **Keywords**: Define a list of blocked terms. Any match triggers the preset response.

* **Custom Endpoint**: Connect a custom moderation endpoint for your own filtering logic.

When content is flagged, the app replaces it with a preset response that you define.

#### Annotation Reply

Define curated Q\&A pairs that take priority over LLM responses. When a user's query **semantically** matches an annotation above the score threshold (how closely a query must match), the curated answer is returned directly without calling the LLM.

You can configure the score threshold and the embedding model used for semantic matching.

To create and manage your annotations:

* Convert existing conversations into annotations directly from **Debug & Preview** or **Logs** by clicking the **Add annotation** icon on any LLM response.

  Once a message is annotated, the icon changes to **Edit**, so you can modify the annotation in place.

    *[Image: Add Annotation Icon]*

* In **Annotations**, manually add new Q\&A pairs, manage existing annotations, and view hit history. Click `...` to bulk import or bulk export.

    *[Image: Bulk Annotation Operation]*

#### More Like This

Generate alternative outputs for the same input. Once enabled, each generated result includes a button to produce a variation, so you can explore different responses without re-entering your query.

  *[Image: More Like This]*

You can generate up to 2 variations per result. Each variation uses additional tokens.

#### Agent

*Chat-style apps where the model can reason, make decisions, and use tools autonomously*

**Source:** https://docs.dify.ai/en/cloud/use-dify/build/agent

Chat-style apps where the model can reason, make decisions, and use tools autonomously

Agents are chat-style apps where the model can reason through a task, decide what to do next, and use tools when needed to complete the user's request.

Use it when you want the model to autonomously decide how to approach a task using available tools, without designing a multi-step workflow. For example, building a data analysis assistant that can fetch live data, generate charts, and summarize findings on its own.

> **ℹ️ Info:**
>   Agents keep up to 500 messages or 2,000 tokens of history per conversation. If either limit is exceeded, the oldest messages will be removed to make room for new ones.

> **💡 Tip:**
>   Agents support optional features like conversation openers, follow-up suggestions, and more. See [App Toolkit](https://docs.dify.ai/en/cloud/use-dify/build/additional-features) for details.

#### Configure

##### Write the Prompt

The prompt tells the model what to do, how to respond, and what constraints to follow. For an agent, the prompt also guides how the model reasons through tasks and decides when to use tools, so be specific about the workflow you expect.

Here are some tips for writing effective prompts:

* **Define the persona**: Describe who the model should act as and the expertise it should draw on.

* **Specify the output format**: Describe the structure, length, or style you expect.

* **Set constraints**: Tell the model what to avoid or what rules to follow.

* **Guide tool usage**: Mention specific tools by name and describe when they should be used.

* **Outline the workflow**: Break down complex tasks into logical steps the model should follow.

###### Create Dynamic Prompts with Variables

To adapt the agent to different users or contexts without rewriting the prompt each time, add variables to collect the necessary information upfront.

Variables are placeholders in the prompt—each one appears as an input field that users fill in before the conversation starts, and their values are injected into the prompt at runtime. Users can also update variable values mid-conversation, and the prompt will adjust accordingly.

For example, a data analysis agent might use a domain variable so users can specify which area to focus on:

```text wrap theme={null}
You are a data analyst specializing in {{domain}}. Help users explore and understand their data.

When asked a question, use available data tools to fetch the relevant information. If the result suits a visual format, generate a chart. Explain your findings in plain language.

Keep responses concise. If a question is ambiguous, ask for clarification before fetching data.
```

> **💡 Tip:**
>   While drafting the prompt, type `/` > **New Variable** to quickly insert a named placeholder. You can configure its details in the **Variables** section later.

Choose the variable type that matches the input you expect:

  **Short Text:**

    Accepts up to 256 characters. Use it for names, email addresses, titles, or any brief text input that fits on a single line.

  **Paragraph:**

    Allows long-form text without length restrictions. It gives users a multi-line text area for detailed descriptions.

  **Select:**

    Displays a dropdown menu with predefined options.

  **Number:**

    Restricts input to numerical values only—ideal for quantities, ratings, IDs, or any data requiring mathematical processing.

  **Checkbox:**

    Provides a simple yes/no option. When a user checks the box, the output is `true`; otherwise, it's `false`. Use it for confirmations or any case that requires a binary choice.

  **API-based Variable:**

    Fetches variable values from an external API at runtime instead of collecting them from users.

    Use it when your prompt needs dynamic data from an external source, such as live weather conditions or database records. See [Custom Endpoints](https://docs.dify.ai/en/cloud/use-dify/workspace/api-extension/api-extension) for details.

> **ℹ️ Info:**
>   **Label Name** is what end users see for each input field.

###### Generate or Improve the Prompt with AI

If you're unsure where to start or want to refine the existing prompt, click **Generate** to let an LLM help you draft it.

Describe what you want from scratch, or reference `current_prompt` and specify what to improve. For more targeted results, add an example in **Ideal Output**.

Each generation is saved as a version, so you can experiment and roll back freely.

##### Extend the Agent with Dify Tools

Add [Dify tools](https://docs.dify.ai/en/cloud/use-dify/workspace/tools) to enable the model to interact with external services and APIs for tasks beyond text generation, such as fetching live data, searching the web, or querying databases.

The model decides when and which tools to use based on each query. To guide this more precisely, mention specific tool names in your prompt and describe when they should be used.

  *[Image: Tool Name]*

You can disable or remove added tools, and modify their configuration. If a tool requires authentication, select an existing credential or create a new one.

> **ℹ️ Info:**
>   To change the default credential, go to **Integrations** > **Tools** > **Tool Plugin**.

###### Maximum Iterations

**Maximum Iterations** in **Agent Settings** limits how many times the model can repeat its reasoning-and-action cycle (think, call a tool, process the result) for a single request.

Increase this value for complex, multi-step tasks that require multiple tool calls. Higher values increase latency and token costs.

##### Ground Responses in Your Own Data

To ground the model's responses in your own data rather than general knowledge, add a knowledge base.

The model evaluates each user query against your knowledge base descriptions and decides whether retrieval is needed—you don't need to mention knowledge bases in your prompt.

**The more detailed your knowledge base description, the better the model can determine relevance**, leading to more accurate and targeted retrieval.

> **ℹ️ Info:**
>   An Agent app has no app-level retrieval settings. Each knowledge base is queried independently using its own settings you've configured. When you add several, the agent picks which to query and does not rerank results across them.

###### Search Within Specific Documents

By default, retrieval searches across the entire knowledge base. To restrict retrieval to specific documents, enable manual or automatic metadata filtering.

This improves retrieval precision, especially when your knowledge base is large or contains content for different contexts.

For creating and managing document metadata, see [Metadata](https://docs.dify.ai/en/cloud/use-dify/knowledge/metadata).

##### Process Multimodal Inputs

To allow end users to upload files, select a model with the corresponding multimodal capabilities. The relevant file type toggles—**Vision**, **Audio**, or **Document**—appear once the model supports them, and you can enable each as needed.

> **💡 Tip:**
>   You can quickly identify a model's supported modalities by its tags.
>
>
>     *[Image: Model Tags]*
>

Click **Settings** under **Vision** to configure how files are accepted and processed. Upload settings apply across all enabled file types.

* **Resolution**: Controls the detail level for **image** processing only.

  * **High**: Better accuracy for complex images but uses more tokens

  * **Low**: Faster processing with fewer tokens for simple images

* **Upload Method**: Choose whether users can upload from their device, paste a URL, or both.

* **Upload Limit**: The maximum number of files a user can upload per message.

#### Debug & Preview

In the preview panel on the right, test your agent in real time. Select a model, type a message, and send it to see how the agent responds.

You can adjust a model's parameters to control how it generates responses. Available parameters and presets vary by model.

> **💡 Tip:**
>   To compare outputs across different models, click **Debug as Multiple Models** to run up to 4 models simultaneously.
>
>
>     *[Image: Debug with Multiple Models]*
>

We recommend selecting models that are strong at **reasoning** and **natively support tool calling**.

**Why This Matters:**

  An agent needs to judge *when* to use a tool, *which tool* fits the task, and *how* to interpret the result—this depends on the model's reasoning ability. Models with built-in tool-call support also execute these decisions more reliably.

You can verify your model's tool-call support in **Agent Settings**, where the system automatically displays the agent mode:

* **Function Calling** for models with native support, meaning they can call tools directly.

* **ReAct** for others, so Dify guides them to use tools through a prompting strategy.

#### Publish

When you're happy with the results, click **Publish** to make your app available. See [Publish](https://docs.dify.ai/en/cloud/use-dify/publish/README) for the full list of publishing options.

#### Chatbot

*The simplest way to build a conversational app with a model and a prompt*

**Source:** https://docs.dify.ai/en/cloud/use-dify/build/chatbot

The simplest way to build a conversational app with a model and a prompt

Chatbots are conversational apps where users interact with the model through a chat interface.

Use it for tasks that benefit from back-and-forth interaction but don't require tool calls or a multi-step workflow—for example, building an internal Q\&A assistant grounded in your team's knowledge base.

> **ℹ️ Info:**
>   Chatbots keep up to 500 messages or 2,000 tokens of history per conversation. If either limit is exceeded, the oldest messages will be removed to make room for new ones.

> **💡 Tip:**
>   Chatbots also support optional features like conversation openers, follow-up suggestions, and more. See [App Toolkit](https://docs.dify.ai/en/cloud/use-dify/build/additional-features) for details.

#### Configure

##### Write the Prompt

The prompt tells the model what to do, how to respond, and what constraints to follow. It shapes how the model behaves throughout the conversation, so think of it as defining a consistent persona rather than describing a one-off task.

Here are some tips for writing effective prompts:

* **Define the persona**: Describe who the model should act as and the tone it should use.

* **Specify the output format**: Describe the structure, length, or style you expect.

* **Set constraints**: Tell the model what to avoid or what rules to follow.

###### Create Dynamic Prompts with Variables

To adapt your chatbot to different users or contexts without rewriting the prompt each time, add variables to collect the necessary information upfront.

Variables are placeholders in the prompt—each one appears as an input field that users fill in before the conversation starts, and their values are injected into the prompt at runtime. Users can also update variable values mid-conversation, and the prompt will adjust accordingly.

For example, an onboarding assistant might use `role` and `language` to tailor its responses:

```text wrap theme={null}
You are an onboarding assistant for new {{role}} hires. Answer questions about company processes and policies. Keep answers friendly and concise, and respond in {{language}}.
```

> **💡 Tip:**
>   While drafting the prompt, type `/` > **New Variable** to quickly insert a named placeholder. You can configure its details in the **Variables** section later.

Choose the variable type that matches the input you expect:

  **Short Text:**

    Accepts up to 256 characters. Use it for names, email addresses, titles, or any brief text input that fits on a single line.

  **Paragraph:**

    Allows long-form text without length restrictions. It gives users a multi-line text area for detailed descriptions.

  **Select:**

    Displays a dropdown menu with predefined options.

  **Number:**

    Restricts input to numerical values only—ideal for quantities, ratings, IDs, or any data requiring mathematical processing.

  **Checkbox:**

    Provides a simple yes/no option. When a user checks the box, the output is `true`; otherwise, it's `false`. Use it for confirmations or any case that requires a binary choice.

  **API-based Variable:**

    Fetches variable values from an external API at runtime instead of collecting them from users.

    Use it when your prompt needs dynamic data from an external source, such as live weather conditions or database records. See [Custom Endpoints](https://docs.dify.ai/en/cloud/use-dify/workspace/api-extension/api-extension) for details.

> **ℹ️ Info:**
>   **Label Name** is what end users see for each input field.

###### Generate or Improve the Prompt with AI

If you're unsure where to start or want to refine the existing prompt, click **Generate** to let an LLM help you draft it.

Describe what you want from scratch, or reference `current_prompt` and specify what to improve. For more targeted results, add an example in **Ideal Output**.

Each generation is saved as a version, so you can experiment and roll back freely.

##### Ground Responses in Your Own Data

To ground the model's responses in your own data rather than general knowledge, add a knowledge base.

Each time a user sends a message, it is used as the search query to retrieve relevant content from the knowledge base, which is then injected into the prompt as context for the model.

###### Configure App-Level Retrieval Settings

To fine-tune how retrieval results are processed, click **Retrieval Setting**.

> **ℹ️ Info:**
>   There are two layers of retrieval settings—the knowledge base level and the app level.
>
>   Think of them as two consecutive filters: the knowledge base settings determine the initial pool of results, and the app settings further rerank the results or narrow down the pool.

* **Rerank Settings**

  * **Weighted Score**

    The relative weight between semantic similarity and keyword matching during reranking. Higher semantic weight favors meaning relevance, while higher keyword weight favors exact matches.

    Weighted Score is available only when all added knowledge bases are indexed with **High Quality** mode.

  * **Rerank Model**

    The rerank model to re-score and reorder all the results based on their relevance to the query.

    > **📝 Note:**
>       If any multimodal knowledge bases are added, select a multimodal rerank model (marked with a **Vision** tag) as well. Otherwise, retrieved images will be excluded from reranking and the final output.
>

* **Top K**

  The maximum number of top results to return after reranking.

  When a rerank model is selected, this value will be automatically adjusted based on the model's maximum input capacity (how much text the model can process at once).

* **Score Threshold**

  The minimum similarity score for returned results. Results scoring below this threshold are excluded. Use higher thresholds for stricter relevance or lower thresholds to include broader matches.

###### Search Within Specific Documents

By default, retrieval searches across the entire knowledge base. To restrict retrieval to specific documents, enable manual or automatic metadata filtering.

This improves retrieval precision, especially when your knowledge base is large or contains content for different contexts.

For creating and managing document metadata, see [Metadata](https://docs.dify.ai/en/cloud/use-dify/knowledge/metadata).

##### Process Multimodal Inputs

To allow end users to upload files, select a model with the corresponding multimodal capabilities. The relevant file type toggles—**Vision**, **Audio**, or **Document**—appear once the model supports them, and you can enable each as needed.

> **💡 Tip:**
>   You can quickly identify a model's supported modalities by its tags.
>
>
>     *[Image: Model Tags]*
>

Click **Settings** under **Vision** to configure how files are accepted and processed. Upload settings apply across all enabled file types.

* **Resolution**: Controls the detail level for **image** processing only.

  * **High**: Better accuracy for complex images but uses more tokens

  * **Low**: Faster processing with fewer tokens for simple images

* **Upload Method**: Choose whether users can upload from their device, paste a URL, or both.

* **Upload Limit**: The maximum number of files a user can upload per message.

#### Debug & Preview

In the preview panel on the right, test your chatbot in real time. Select a model that best fits your task, type a message, and send it to see how the model responds.

After selecting a model, you can adjust its parameters to control how it generates responses. Available parameters and presets vary by model.

> **💡 Tip:**
>   To compare outputs across different models, click **Debug as Multiple Models** to run up to 4 models simultaneously.
>
>
>     *[Image: Debug with Multiple Models]*
>

#### Publish

When you're happy with the results, click **Publish** to make your app available. See [Publish](https://docs.dify.ai/en/cloud/use-dify/publish/README) for the full list of publishing options.

#### Orchestration Logic

*How to arrange, nest, or reuse nodes when building a Workflow or Chatflow*

**Source:** https://docs.dify.ai/en/cloud/use-dify/build/orchestrate-node

How to arrange, nest, or reuse nodes when building a Workflow or Chatflow

#### Serial and Parallel Execution

  *[Image: Serial vs. Parallel Execution]*

When building a workflow, you can arrange nodes in series or in parallel:

* **In series**, nodes run one after another. Each node can read variables from any node earlier in the chain.

* **In parallel**, nodes run at the same time. They can't read each other's variables, but where parallel branches converge, the downstream node can read from all of them.

> **ℹ️ Info:**
>   A single execution path supports up to 50 nodes.

#### Node Reuse

All nodes except User Input can be copied and pasted within the same workflow, across workflows, or across Dify instances, though there might be compatibility issues between Dify versions.

> **📝 Note:**
>   Pasting across workflows or Dify instances requires the Dify page to be served over HTTPS or accessed via a loopback address (such as `http://localhost` or `http://127.0.0.1`).

When you paste a node, its configuration moves with it, but the availability of anything that depends on the surrounding environment is re-evaluated at the destination:

* **Workflow-specific resources**, such as variables
* **Workspace-specific resources**, such as integrations and knowledge bases

#### Iteration and Loop

For nodes that should run multiple times (once per item in a list or until a condition is met), place them inside an [Iteration](https://docs.dify.ai/en/cloud/use-dify/nodes/iteration) or [Loop](https://docs.dify.ai/en/cloud/use-dify/nodes/loop) node.

#### Handle Errors

**Source:** https://docs.dify.ai/en/cloud/use-dify/build/predefined-error-handling-logic

![](https://assets-docs.dify.ai/2024/12/6e2655949889d4d162945d840d698649.png)

[LLM](https://docs.dify.ai/en/cloud/use-dify/nodes/llm), [HTTP](https://docs.dify.ai/en/cloud/use-dify/nodes/http-request), [Code](https://docs.dify.ai/en/cloud/use-dify/nodes/code), and [Tool](https://docs.dify.ai/en/cloud/use-dify/nodes/tools)
nodes support error handling out-of-box. When a node fails, it can take one of the three behaviors below:

  **None:**

    The default behavior. When a node fails, the whole workflow stops. You get the original error message.

    Use this when:

    * You're testing and want to see what broke
    * The workflow can't continue without this step

  **Default Value:**

    When a node fails, use a backup value instead. The workflow keeps running.

      ![When a Node Fails, Use a Backup Value Instead](https://assets-docs.dify.ai/2024/12/e9e5e757090679243e0c9976093c7e6c.png)

    **Requirements**

    * The default value must match the node's output type -- if it outputs a string, your default must be a string.

    **Example**

    Your LLM node normally returns analysis, but sometimes it fails due to rate limits. Set a default value like:

    ```
    "Sorry, I'm temporarily unavailable. Please try again in a few minutes."
    ```

    Now users get a helpful message instead of a broken workflow.

  **Fail Branch:**

    When a node fails, trigger a separate flow to handle the error.

      ![When a Node Fails, Trigger a Separate Flow to Handle the Error](https://assets-docs.dify.ai/2024/12/e5ea1af947818bd9e27cab3042c1c4f3.png)

    The fail branch is highlighted in orange. You can:

    * Send error notifications
    * Try a different approach
    * Log the error for debugging
    * Use a backup service
      **Example**

    Your main API fails, so the fail branch calls a backup API instead. Users never know there was a problem.

#### Error in Loop/Iteration Nodes

When child nodes fail inside loops and iterations, these control flow nodes have their own error behaviors.

**Loop nodes** always stop immediately when any child node fails. The entire loop terminates and returns the error, preventing any further iterations from running.

**Iteration nodes** let you choose how to handle child node failures through the error handling mode setting:

* `terminated` - Stops processing immediately when any item fails (default)
* `continue-on-error` - Skips the failed item and continues with the next one
* `remove-abnormal-output` - Continues processing but filters out failed items from the final output

When you set an iteration to `continue-on-error`, failed items return `null` in the output array. When you use `remove-abnormal-output`, the output array only contains successful results, making it shorter than the input array.

#### Error variables

When using default value or fail branch, you get two special variables:

* `error_type` - What kind of error happened (see [Error Types](https://docs.dify.ai/en/cloud/use-dify/debug/error-type))
* `error_message` - The actual error details

Use these to:

* Show users helpful messages
* Send alerts to your team
* Choose different recovery strategies
* Log errors for debugging

**Example**

```
{% if error_type == "rate_limit" %}
Too many requests. Please wait a moment and try again.
{% else %}
Something went wrong. Our team has been notified.
{% endif %}
```

#### Hotkeys

*Keyboard shortcuts for building workflows faster in Dify*

**Source:** https://docs.dify.ai/en/cloud/use-dify/build/shortcut-key

Keyboard shortcuts for building workflows faster in Dify

Speed up your workflow building with keyboard shortcuts.

> **💡 Tip:**
>   **[Go to Anything](https://docs.dify.ai/en/cloud/use-dify/build/goto-anything)**: Press `Cmd+K` (macOS) or `Ctrl+K` (Windows) anywhere in Dify to find and jump to almost anything.
>
>   * Type `@` to search apps, integrations, knowledge bases, or workflow nodes.
>   * Type `/` to run a command like `/docs`, `/theme`, or `/language`.
>
>
>     *[Image: Go to Anything Search Interface]*
>

#### Selection and Editing

With one or more nodes selected on the canvas:

| Windows        | macOS          | Action                                             |
| :------------- | :------------- | :------------------------------------------------- |
| `Ctrl` + `C`   | `Cmd` + `C`    | Copy                                               |
| `Ctrl` + `V`   | `Cmd` + `V`    | Paste                                              |
| `Ctrl` + `D`   | `Cmd` + `D`    | Duplicate                                          |
| `Delete`       | `Delete`       | Delete selected nodes or edges                     |
| `Shift` (hold) | `Shift` (hold) | Highlight the selected node's variable connections |

#### Canvas Modes

| Windows | macOS | Action                |
| :------ | :---- | :-------------------- |
| `V`     | `V`   | Pointer mode (select) |
| `H`     | `H`   | Hand mode (pan)       |
| `C`     | `C`   | Comment mode          |

#### Zoom and Layout

| Windows       | macOS         | Action         |
| :------------ | :------------ | :------------- |
| `Ctrl` + `1`  | `Cmd` + `1`   | Zoom to fit    |
| `Ctrl` + `=`  | `Cmd` + `=`   | Zoom in        |
| `Ctrl` + `-`  | `Cmd` + `-`   | Zoom out       |
| `Shift` + `1` | `Shift` + `1` | Zoom to 100%   |
| `Shift` + `5` | `Shift` + `5` | Zoom to 50%    |
| `Ctrl` + `O`  | `Cmd` + `O`   | Organize nodes |

#### History

| Windows                | macOS                 | Action |
| :--------------------- | :-------------------- | :----- |
| `Ctrl` + `Z`           | `Cmd` + `Z`           | Undo   |
| `Ctrl` + `Y`           | `Cmd` + `Y`           | Redo   |
| `Ctrl` + `Shift` + `Z` | `Cmd` + `Shift` + `Z` | Redo   |

#### Testing

| Windows     | macOS          | Action   |
| :---------- | :------------- | :------- |
| `Alt` + `R` | `Option` + `R` | Test run |

#### Text Generator

*Simple single-turn apps for generating text from a prompt and user inputs*

**Source:** https://docs.dify.ai/en/cloud/use-dify/build/text-generator

Simple single-turn apps for generating text from a prompt and user inputs

Text Generators are simple single-turn apps: you write a prompt, provide inputs, and the model generates a response.

It's a good fit for tasks that don't require multi-turn conversation, tool calls, or a multi-step workflow. Just a clear input, one model call, and a ready-to-use output.

> **💡 Tip:**
>   Text Generators support optional features like generating multiple outputs at once, text to speech, and content moderation. See [App Toolkit](https://docs.dify.ai/en/cloud/use-dify/build/additional-features) for details.

#### Configure

##### Write the Prompt

The prompt tells the model what to do, how to respond, and what constraints to follow.

Since a Text Generator runs in a single turn with no conversation history, the prompt is the model's only source of context—include everything it needs to produce the right output in one pass.

Here are some tips for writing effective prompts:

* **Define the task clearly**: State what the model should produce (e.g., a translation, a summary, a SQL statement).

* **Specify the output format**: Describe the structure, length, or style you expect.

* **Set constraints**: Tell the model what to avoid or what rules to follow.

Because a Text Generator always requires user input to run, a paragraph-type `query` variable is automatically inserted into the prompt when you create a new app. You can rename `query` or change its type.

Variables are placeholders—each one becomes an input field that users fill in before running the app, and their values are substituted into the prompt at runtime. For example:

```text wrap theme={null}
You are a professional editor. Summarize the following text into 3 concise bullet points. Use neutral tone and avoid adding information not present in the original text.

{{query}}
```

> **💡 Tip:**
>   While drafting the prompt, type `/` > **New Variable** to quickly insert a named placeholder. You can configure its details in the **Variables** section later.

Choose the variable type that matches the input you expect:

  **Short Text:**

    Accepts up to 256 characters. Use it for names, email addresses, titles, or any brief text input that fits on a single line.

  **Paragraph:**

    Allows long-form text without length restrictions. It gives users a multi-line text area for detailed descriptions.

  **Select:**

    Displays a dropdown menu with predefined options.

  **Number:**

    Restricts input to numerical values only—ideal for quantities, ratings, IDs, or any data requiring mathematical processing.

  **Checkbox:**

    Provides a simple yes/no option. When a user checks the box, the output is `true`; otherwise, it's `false`. Use it for confirmations or any case that requires a binary choice.

  **API-based Variable:**

    Fetches variable values from an external API at runtime instead of collecting them from users.

    Use it when your prompt needs dynamic data from an external source, such as live weather conditions or database records. See [Custom Endpoints](https://docs.dify.ai/en/cloud/use-dify/workspace/api-extension/api-extension) for details.

> **ℹ️ Info:**
>   **Label Name** is what end users see for each input field.

###### Create Dynamic Prompts with Variables

To adapt your app to different users or contexts without rewriting the prompt each time, add more variables.

Each variable collects a specific piece of information upfront and injects it into the prompt at runtime.

For example, an SQL generator might use `database_type` to adapt the output dialect while `query` captures the user's natural language request:

```text wrap theme={null}
You are an SQL generator. Translate the following natural language query into a {{database_type}} SQL statement: {{query}}
```

###### Generate or Improve the Prompt with AI

If you're unsure where to start or want to refine the existing prompt, click **Generate** to let an LLM help you draft it.

Describe what you want from scratch, or reference `current_prompt` and specify what to improve. For more targeted results, add an example in **Ideal Output**.

Each generation is saved as a version, so you can experiment and roll back freely.

##### Ground Responses in Your Own Data

To ground the model's responses in your own data rather than general knowledge, add a knowledge base and select an existing variable as the **Query Variable**.

When a user runs the app and fills in that field, its value is used as the search query to retrieve relevant content from the knowledge base. The retrieved content is then injected into the prompt as context, so the model can generate a more informed response.

**Example: Use Content Type to Retrieve Style Guides in a Content Writing App:**

  For example, suppose your knowledge base contains style guides for different content types—blog posts, social media captions, product descriptions, and so on.

  In a content writing app, set `content_type` as the **Query Variable**. When a user selects a content type, the app retrieves the matching style guide and generates copy that follows the corresponding writing standards.

  Your prompt might look like this:

  ```text wrap theme={null}
  You are a brand content writer. Write a {{content_type}} based on the following brief: {{brief}}

  Follow the style and tone guidelines provided in the context.
  ```

###### Configure App-Level Retrieval Settings

To fine-tune how retrieval results are processed, click **Retrieval Setting**.

> **ℹ️ Info:**
>   There are two layers of retrieval settings—the knowledge base level and the app level.
>
>   Think of them as two consecutive filters: the knowledge base settings determine the initial pool of results, and the app settings further rerank the results or narrow down the pool.

* **Rerank Settings**

  * **Weighted Score**

    The relative weight between semantic similarity and keyword matching during reranking. Higher semantic weight favors meaning relevance, while higher keyword weight favors exact matches.

    Weighted Score is available only when all added knowledge bases are indexed with **High Quality** mode.

  * **Rerank Model**

    The rerank model to re-score and reorder all the results based on their relevance to the query.

    > **📝 Note:**
>       If any multimodal knowledge bases are added, select a multimodal rerank model (marked with a **Vision** tag) as well. Otherwise, retrieved images will be excluded from reranking and the final output.
>

* **Top K**

  The maximum number of top results to return after reranking.

  When a rerank model is selected, this value will be automatically adjusted based on the model's maximum input capacity (how much text the model can process at once).

* **Score Threshold**

  The minimum similarity score for returned results. Results scoring below this threshold are excluded. Use higher thresholds for stricter relevance or lower thresholds to include broader matches.

###### Search Within Specific Documents

By default, retrieval searches across the entire knowledge base. To restrict retrieval to specific documents, enable manual or automatic metadata filtering.

This improves retrieval precision, especially when your knowledge base is large or contains content for different contexts.

For creating and managing document metadata, see [Metadata](https://docs.dify.ai/en/cloud/use-dify/knowledge/metadata).

##### Process Multimodal Inputs

To allow end users to upload files, select a model with the corresponding multimodal capabilities. The relevant file type toggles—**Vision**, **Audio**, or **Document**—appear once the model supports them, and you can enable each as needed.

> **💡 Tip:**
>   You can quickly identify a model's supported modalities by its tags.
>
>
>     *[Image: Model Tags]*
>

Click **Settings** under **Vision** to configure how files are accepted and processed. Upload settings apply across all enabled file types.

* **Resolution**: Controls the detail level for **image** processing only.

  * **High**: Better accuracy for complex images but uses more tokens

  * **Low**: Faster processing with fewer tokens for simple images

* **Upload Method**: Choose whether users can upload from their device, paste a URL, or both.

* **Upload Limit**: The maximum number of files a user can upload per run.

#### Debug & Preview

In the preview panel on the right, test your app in real time. Select a model that best fits your task, fill in the input fields, and click **Run** to see the output.

After selecting a model, you can adjust its parameters to control how it generates responses. Available parameters and presets vary by model.

> **💡 Tip:**
>   To compare outputs across different models, click **Debug as Multiple Models** to run up to 4 models simultaneously.
>
>
>     *[Image: Debug with Multiple Models]*
>

#### Publish

When you're happy with the results, click **Publish** to make your app available. See [Publish](https://docs.dify.ai/en/cloud/use-dify/publish/README) for the full list of publishing options.

When running the web app, end users can save individual outputs for future reference.

  *[Image: Save Output]*

#### Version Control

**Source:** https://docs.dify.ai/en/cloud/use-dify/build/version-control

Track changes and manage versions in Chatflow and Workflow apps.

> **ℹ️ Info:**
>   Only available for Chatflow and Workflow apps right now.

#### How it works

**Current Draft**: Your working version. This is where you make changes. Not live for users.

  ![Current Draft](https://assets-docs.dify.ai/2025/03/38296a597c0ca31b5fb70be2234f2363.png)

**Latest Version**: The live version users see.

  ![Latest Version](https://assets-docs.dify.ai/2025/03/e4c06a0817c30cf9e8893487c889cb02.png)

**Previous Versions**: Older published versions.

  ![Previous Versions](https://assets-docs.dify.ai/2025/03/4cd05033b93d84b53496f3d02e88601f.png)

#### Publish versions

Click **Publish** → **Publish Update** to make your draft live.

  ![](https://assets-docs.dify.ai/2025/03/26f3f324ab4ecb965708d553ddd78d97.png)

Your draft becomes the new Latest Version, and you get a fresh draft to work in.

  ![](https://assets-docs.dify.ai/2025/03/67e95de17577bc272addad6c33f8ea59.png)

#### View versions

Click the history icon to see all versions:

  ![](https://assets-docs.dify.ai/2025/03/eed667bbc9498425342c09039054cf98.png)

Filter by:

* **All versions** or **only yours**
* **Only named versions** (skip auto-generated names)

  ![Only Named Versions (Skip Auto-Generated Names)](https://assets-docs.dify.ai/2025/03/0bf8fef8858671a8fef160f49dd83dad.jpg)

#### Manage versions

**Name a version**: Give it a proper name instead of the auto-generated one

  ![Name a Version](https://assets-docs.dify.ai/2025/03/ac149f63da6611d7080d305dd3fad65c.jpg)

**Edit version info**: Change the name and add release notes

  ![Edit Version Info](https://assets-docs.dify.ai/2025/03/1d840edf979132a9bbf1e065f95e663c.jpg)

**Delete old versions**: Clean up versions you don't need

  ![Delete Old Versions](https://assets-docs.dify.ai/2025/03/25ad1999fc9f6f44fcac04526ac5563a.jpg)

> **⚠️ Warning:**
>   You can't delete the Current Draft or Latest Version.

**Restore a version**: Load an old version back into your draft

  ![Restore a Version](https://assets-docs.dify.ai/2025/03/c96b714accc29df8e46e711782a7a6a9.jpg)

> **⚠️ Warning:**
>   This replaces your current draft completely. Make sure you don't have unsaved work.

> **ℹ️ Info:**
>   Restoring a version, exporting a specific version's DSL, and running a specific published version through the [Service API](https://docs.dify.ai/en/api-reference/workflow-runs/run-workflow-by-id) are available on paid plans. On the Sandbox plan, apps always run the latest published version.

#### Example workflow

Here's how versions work through a typical development cycle:

##### 1. Start with a draft

  ![How Versions Work Through a Typical Development Cycle](https://assets-docs.dify.ai/2025/03/35ece9d5d5d4d8c46a3fb5ceae4d0c15.jpeg)

##### 2. Publish first version

  ![](https://assets-docs.dify.ai/2025/03/3d1f66cdeb08710f01462a6b0f3ed0a8.jpeg)

##### 3. Publish second version

  ![](https://assets-docs.dify.ai/2025/03/92ffbf88a3cbeeeeab47c1bd8b4f7198.jpeg)

##### 4. Restore old version to draft

  ![](https://assets-docs.dify.ai/2025/03/541f1891416af90dab5b51bfec833249.jpeg)

##### 5. Publish the restored version

  ![](https://assets-docs.dify.ai/2025/03/3572a4f2edef166c3f14e4ec4e68b297.jpeg)

Complete demo:

  ![Complete Demo](https://assets-docs.dify.ai/2025/03/dc7c15a4dfafb72ce7fffea294d5b5e5.gif)

#### Tips

* Always test in draft before publishing
* Use descriptive version names for important releases
* Restore versions when you need to rollback quickly
* Keep old versions around for reference

#### Workflow & Chatflow

*Build agentic workflows that combine AI models, tools, and logic into reliable, repeatable processes*

**Source:** https://docs.dify.ai/en/cloud/use-dify/build/workflow-chatflow

Build agentic workflows that combine AI models, tools, and logic into reliable, repeatable processes

#### Why Agentic Workflows

AI models are powerful, but on their own they can be unpredictable—they may hallucinate, miss steps, or produce inconsistent outputs. In production environments, especially for teams and enterprises where reliability matters, you need more control over how AI operates.

Agentic workflows solve this by embedding AI capabilities within a structured, repeatable process. Instead of relying on a single model to figure everything out, you design a flow that orchestrates models, tools, and logic step by step—with clear conditions, checkpoints, and fallback paths.

The AI is still doing the heavy lifting, but within boundaries you define.

#### Workflow vs. Chatflow

Dify offers two app types for building agentic workflows: **Workflow** and **Chatflow**. Both are built on a shared visual canvas and node system.

To build a flow, connect nodes that each handle a specific step, such as calling a model, retrieving knowledge, running code, or branching on conditions. Most of the work is **drag, connect, and configure**—code is only needed when your logic calls for it.

Their core difference is how users interact with the app:

* A **Workflow** runs once from start to finish.

  It takes an input, processes it through the flow, and returns a result. Use it for tasks like automated report generation, data processing pipelines, or batch processing.

* A **Chatflow** adds a conversation layer.

  Users interact through a chat interface, and each message triggers the flow you designed before a response is generated. Use it for interactive assistants, guided Q\&A, or any conversational scenario that requires structured processing behind each reply.

  > **💡 Tip:**
>     Chatflows support optional features like content moderation, text to speech, and more. See [App Toolkit](https://docs.dify.ai/en/cloud/use-dify/build/additional-features) for details.
>

They also start and end with different nodes:

|             | Workflow                                                                                                  | Chatflow                                                  |
| :---------- | :-------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| Starts with | [User Input](https://docs.dify.ai/en/cloud/use-dify/nodes/user-input) or [Trigger](https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/overview) | User Input                                                |
| Ends with   | [Output](https://docs.dify.ai/en/cloud/use-dify/nodes/output) node (optional)                                                 | [Answer](https://docs.dify.ai/en/cloud/use-dify/nodes/answer) node (required) |

A Trigger runs a workflow automatically: on a schedule, when a webhook fires, or from an integration event. Chatflows always start from a user message, so they don't have Triggers.

For how to compose either type, see [Orchestration Logic](https://docs.dify.ai/en/cloud/use-dify/build/orchestrate-node).

### Debug

#### Error Types

**Source:** https://docs.dify.ai/en/cloud/use-dify/debug/error-type

Each node type throws specific error classes that help you understand what went wrong and how to fix it.

#### Node-specific errors

  **Code:**

    `CodeNodeError`
    > **ℹ️ Info:**
> Your Python or JavaScript code threw an exception during execution

      ![Code Error](https://assets-docs.dify.ai/2024/12/c86b11af7f92368180ea1bac38d77083.png)

    `OutputValidationError`
    > **ℹ️ Info:**
> The data type your code returned doesn't match the output variable type you configured

    `DepthLimitError`
    > **ℹ️ Info:**
> Your code created nested data structures deeper than 5 levels

    `CodeExecutionError`
    > **ℹ️ Info:**
> The sandbox service couldn't execute your code - usually means the service is down

      ![CodeExecutionError](https://assets-docs.dify.ai/2024/12/ab8cae01a590b037017dfe9ea4dbbb8b.png)

  **LLM:**

    `VariableNotFoundError`
    > **ℹ️ Info:**
> Your prompt template references a variable that doesn't exist in the workflow context

      ![VariableNotFoundError](https://assets-docs.dify.ai/2024/12/f20c5fbde345144de6183374ab277662.png)

    `InvalidContextStructureError`
    > **ℹ️ Info:**
> You passed an array or object to the context field, which only accepts strings

    `NoPromptFoundError`
    > **ℹ️ Info:**
> The prompt field is completely empty

    `ModelNotExistError`
    > **ℹ️ Info:**
> No model is selected in the LLM node configuration

    `LLMModeRequiredError`
    > **ℹ️ Info:**
> The selected model doesn't have valid API credentials configured

    `InvalidVariableTypeError`
    > **ℹ️ Info:**
> Your prompt template isn't valid Jinja2 syntax or plain text format

      ![InvalidVariableTypeError](https://assets-docs.dify.ai/2024/12/9882f7a5ee544508ba11b51fb469a911.png)

  **HTTP Request:**

    `AuthorizationConfigError`
    > **ℹ️ Info:**
> Missing or invalid authentication configuration for the API endpoint

    `InvalidHttpMethodError`
    > **ℹ️ Info:**
> HTTP method must be GET, HEAD, POST, PUT, PATCH, or DELETE

    `ResponseSizeError`
    > **ℹ️ Info:**
> API response exceeded the 10MB size limit

    `FileFetchError`
    > **ℹ️ Info:**
> Couldn't retrieve a file variable referenced in the request

    `InvalidURLError`
    > **ℹ️ Info:**
> The URL format is malformed or unreachable

  **Tool:**

    `ToolParameterError`
    > **ℹ️ Info:**
> Parameters passed to the tool don't match its expected schema

    `ToolFileError`
    > **ℹ️ Info:**
> The tool couldn't access required files

    `ToolInvokeError`
    > **ℹ️ Info:**
> The external tool API returned an error during execution

    

        ![](https://assets-docs.dify.ai/2024/12/84af0831b7cb23e64159dfbba80e9b28.jpg)

    

    `ToolProviderNotFoundError`
    > **ℹ️ Info:**
> The tool provider isn't installed or configured properly

#### System-level errors

`InvokeConnectionError`
> **ℹ️ Info:**
> Network connection failed to the external service

`InvokeServerUnavailableError`
> **ℹ️ Info:**
> External service returned a 503 status or is temporarily down

`InvokeRateLimitError`
> **ℹ️ Info:**
> You've hit rate limits on the API or model provider

`QuotaExceededError`
> **ℹ️ Info:**
> Your usage quota has been exceeded for this service

#### Run History

**Source:** https://docs.dify.ai/en/cloud/use-dify/debug/history-and-logs

Dify records detailed Run History every time your workflow runs. You can see what happened at both the application level and for individual nodes.

> **ℹ️ Info:**
>   For Run History from live users after publishing, see [Logs](https://docs.dify.ai/en/cloud/use-dify/monitor/logs).

#### Application Run History

Each workflow run creates a complete log entry. Click any entry to see three sections:

  ![Each Workflow Run Creates a Complete Log Entry](https://assets-docs.dify.ai/2025/04/08a885858cfa6e8863faac891a5be319.png)

##### Result

Shows the final output that users see. If the workflow failed, you'll see error messages here.

  ![Shows the Final Output That Users See](https://assets-docs.dify.ai/2025/06/22856751d278ffad99d0533d2d96e125.png)

> **⚠️ Warning:**
>   Only available for Workflow applications.

##### Detail

Shows the original input, final output, and system metadata from the execution.

  ![Shows the Original Input, Final Output, and System Metadata from the Execution](https://assets-docs.dify.ai/2025/06/882b783cd843ab666f5bc3c06f78521d.png)

##### Tracing

Shows exactly how your workflow executed, including which nodes ran in what order, how long each took, and where data flowed between them. This is useful for finding bottlenecks and understanding complex workflows with branches or loops.

  ![Shows Exactly How Your Workflow Executed, Including Which Nodes Ran in What](https://assets-docs.dify.ai/2025/06/9e614ac01b1f6e0aeadda78c91ce93b7.png)

#### Node Run History

You can also check the last execution of any individual node. Click "Last run" in the node's config panel to see its most recent input, output, and timing details.

  ![](https://assets-docs.dify.ai/2025/06/9c6e57236d85f426a930424863042d7d.png)

#### Single Node

**Source:** https://docs.dify.ai/en/cloud/use-dify/debug/step-run

Test individual nodes or run through your workflow step-by-step to catch issues before publishing.

#### Single node testing

You can test any node individually without running the entire workflow. Select the node, provide test input in its settings panel, and click Run to see the output.

  ![](https://assets-docs.dify.ai/2025/04/376c9de6f92cb7a5f97a6661c5e0e9eb.png)

After testing, click "Last run" to see execution details including inputs, outputs, timing, and any error messages.

> **⚠️ Warning:**
>   Answer and End nodes don't support single node testing.

#### Step-by-step execution

When you run nodes one at a time, their outputs are cached in the Variable Inspector. You can edit these cached variables to test different scenarios without re-running upstream nodes.

  ![When You Run Nodes One at a Time, Their Outputs Are Cached in the Variable](https://assets-docs.dify.ai/2025/06/f8656d8deeeaefeab0a8d9169f0ed2d3.png)

This is useful when you want to test how a node responds to different data without having to modify and re-run all the nodes before it. Just change the variable values in the inspector and run the node again.

#### View execution history

Every node execution creates a record. Click "Last run" on any node to see its most recent execution details including what data went in, what came out, and how long it took.

  ![Every Node Execution Creates a Record](https://assets-docs.dify.ai/2025/04/5ee92e6406979f5101d21865f95a86e5.png)

#### Variable Inspector

**Source:** https://docs.dify.ai/en/cloud/use-dify/debug/variable-inspect

The Variable Inspector shows you all the data flowing through your workflow. It captures inputs and outputs from each node after they run, so you can see what's happening and test different scenarios.

  ![](https://assets-docs.dify.ai/2025/06/38f26d7339f64abfdfb6955b1c34f4ae.png)

#### View variables

After any node runs, its output variables appear in the inspector panel at the bottom of the screen. Click any variable to see its full content.

  ![Any Node Runs, Its Output Variables Appear in the Inspector Panel at the Bottom](https://assets-docs.dify.ai/2025/06/94a4741c25204db5fd1281ec475093d9.png)

#### Edit variables

You can edit most variable values by clicking on them. When you run downstream nodes, they'll use your edited values instead of the original ones. This lets you test different scenarios without re-running the entire workflow.

> **ℹ️ Info:**
>   Editing variables here doesn't change the "Last run" record for the node that originally created them.

For example, if an LLM node generates SQL like `SELECT * FROM users`, you can edit it to `SELECT username FROM users` in the inspector and then re-run just the database node to see different results.

  ![](https://assets-docs.dify.ai/2025/06/fb8c49fc0c8c63866f1a9379e8752d9e.png)

#### Reset variables

Click the revert icon next to any variable to restore its original value, or click "Reset all" to clear all cached variables at once.

  ![](https://assets-docs.dify.ai/2025/06/b713290543a0feb95ecab65336e97483.png)

### Getting Started

#### Use Dify

*Orchestrate, publish, and monitor AI applications in your workspace*

**Source:** https://docs.dify.ai/en/cloud/use-dify/getting-started/introduction

Orchestrate, publish, and monitor AI applications in your workspace

  
    
      ## Use Dify

      
        Your workspace is where everything happens: build AI applications, ground them in your own data, then publish and monitor them.
      

      
        [Quick Start](https://docs.dify.ai/en/quick-start)

        
          [Key Concepts](https://docs.dify.ai/en/learn/key-concepts)
          ·
          [Tutorials](https://docs.dify.ai/en/learn/tutorials/workflow-101/lesson-01)
        
      
    
  

  
    - **[Orchestrate](https://docs.dify.ai/en/cloud/use-dify/build/workflow-chatflow)** — Build workflows and chatflows on the visual canvas, plus agents, chatbots, and more.

    - **[Knowledge](https://docs.dify.ai/en/cloud/use-dify/knowledge/readme)** — Import documents and data so your apps can retrieve and cite them.

    - **[Publish](https://docs.dify.ai/en/cloud/use-dify/publish/README)** — Ship your app as a web app, embed it in a website, or call it over the API.

    - **[Monitor](https://docs.dify.ai/en/cloud/use-dify/monitor/analysis)** — Track usage, review logs, and refine answers with annotations.

    - **[Integrations](https://docs.dify.ai/en/cloud/use-dify/workspace/plugins)** — Connect model providers, tools, data sources, and external services.

    - **Get Help** — Ask the community or report a problem.  [Discord](https://discord.gg/FngNHpbcY7) · [GitHub Issues](https://github.com/langgenius/dify/issues) · [Discussions](https://github.com/langgenius/dify/discussions) 
  


### Knowledge

#### Connect to External Knowledge Base

*Integrate external knowledge sources with Dify applications through API connections to leverage custom RAG systems or third-party knowledge services*

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/connect-external-knowledge-base

Integrate external knowledge sources with Dify applications through API connections to leverage custom RAG systems or third-party knowledge services

If your team maintains its own RAG system or hosts content in a third-party knowledge service like [AWS Bedrock](https://aws.amazon.com/bedrock/), you can connect these external sources to Dify instead of migrating content into Dify's built-in knowledge base.

This lets your AI applications retrieve information directly from your existing infrastructure while you retain full control over the retrieval logic and content management.

  ![External Knowledge Base Architecture](https://assets-docs.dify.ai/2025/03/f5fb91d18740c1e2d3938d4d106c4d3c.png)

**Connecting an external knowledge base involves three steps**:

1. [Build an API service that Dify can query](#step-1-build-the-retrieval-api).
2. [Register the API endpoint in Dify](#step-2-register-an-external-knowledge-api).
3. [Connect a specific knowledge source through the registered API](#step-3-create-an-external-knowledge-base).

When your application runs, Dify sends retrieval requests to your endpoint and uses the returned chunks as context for LLM responses.

> **💡 Tip:**
>   If you're connecting to LlamaCloud, install the [LlamaCloud plugin](https://marketplace.dify.ai/plugin/langgenius/llamacloud) instead of building a custom API. See the [video walkthrough](https://www.youtube.com/watch?v=FaOzKZRS-2E) for a complete setup demo.
>
>   If you're building a plugin for another knowledge service, the LlamaCloud plugin's [source code](https://github.com/langgenius/dify-official-plugins/tree/main/extensions/llamacloud) is available for reference.

> **ℹ️ Info:**
>   Dify only has retrieval access to external knowledge bases. It cannot modify or manage your external content. You maintain the knowledge base and its retrieval logic independently.

#### Step 1: Build the Retrieval API

Build an API service that implements the [External Knowledge API specification](https://docs.dify.ai/en/cloud/use-dify/knowledge/external-knowledge-api). Your service needs a single `POST` endpoint that accepts a search query and returns matching text chunks with similarity scores.

#### Step 2: Register an External Knowledge API

An External Knowledge API stores your endpoint URL and authentication credentials. Multiple knowledge bases can share one API connection.

1. Go to **Knowledge**, click **External Knowledge API** in the upper-right corner, then click **Add an External Knowledge API**.

2. Fill in the following fields:

   * **Name**: A label to distinguish this API connection from others.
   * **API Endpoint**: The base URL of your external knowledge service. Dify appends `/retrieval` automatically when sending requests.
   * **API Key**: The authentication credential for your service. Dify sends this as a Bearer token in the `Authorization` header.

Dify validates the connection by sending a test request to your endpoint when you save.

#### Step 3: Create an External Knowledge Base

With the API registered, connect an external knowledge source to Dify. This creates a knowledge base in Dify that is linked to your external system.

1. Go to **Knowledge** and click **Connect to an External Knowledge Base**.

     *[Image: Connect to External Knowledge Base]*

2. Fill in the following fields:
   * **External Knowledge Name** and **Knowledge Description** (optional).

   * **External Knowledge API**: Select the API connection you registered.

   * **External Knowledge ID**: The identifier of the specific knowledge source within your external system, passed to your API as the `knowledge_id` field.

     This is whatever ID your external service uses to distinguish between different knowledge bases. For example, a Bedrock knowledge base ARN or an ID you defined in your own system.

     > **📝 Note:**
>        The **External Knowledge API** and **External Knowledge ID** cannot be changed after creation. To use a different API or knowledge source, create a new external knowledge base.
>

   * **Retrieval Settings**:
     * **Top K**: Maximum number of chunks to retrieve per query. Higher values return more results but may include less relevant content.
     * **Score Threshold**: Minimum similarity score for returned chunks. Enable this to filter out low-relevance results. Use higher value for stricter relevance or lower value to include broader matches.

       When disabled, all results up to the Top K limit are returned regardless of score.

Once created, the external knowledge base is available for use in your applications just like any built-in knowledge base. See [Integrate Knowledge Within Application](https://docs.dify.ai/en/cloud/use-dify/knowledge/integrate-knowledge-within-application) for details.

#### Troubleshoot

##### API Response Format Issues

If retrieval fails or returns unexpected results, verify your API response against the [External Knowledge API specification](https://docs.dify.ai/en/cloud/use-dify/knowledge/external-knowledge-api#response).

Common issues:

* The `metadata` field in each record must be an object (`{}`), not `null`. A `null` value causes errors in the retrieval pipeline.
* The `content` and `score` fields must be present in every record.

#### Configure the Chunk Settings

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/chunking-and-cleaning-text

#### What is Chunking?

Documents imported into knowledge bases are split into smaller segments called **chunks**. Think of chunking like organizing a large book into chapters and paragraphs: you can't quickly find specific information in one massive block of text, but well-organized sections make retrieval efficient.

When users ask questions, the system searches through these chunks for relevant information and provides it to the LLM as context. Without chunking, processing entire documents for every query would be slow and inefficient.

**Key Chunk Parameters**

* **Delimiter**: The character or sequence where text is split. For example, `\n\n` splits at paragraph breaks, `\n` at line breaks.

  > **📝 Note:**
>     Delimiters are removed during chunking. For example, using `A` as the delimiter splits `CBACD` into `CB` and `CD`.
>
>     To avoid information loss, use non-content characters that don't naturally appear in your documents.
>

* **Maximum chunk length**: The maximum size of each chunk in characters. Text exceeding this limit is force-split regardless of delimiter settings.

#### Choose a Chunk Mode

> **📝 Note:**
>   The chunk mode cannot be changed once the knowledge base is created. However, chunk settings like the delimiter and maximum chunk length can be adjusted at any time.

##### Mode Overview

  **General:**

    In General mode, all chunks share the same settings. Matched chunks are returned directly as retrieval results.

    **Chunk Settings**

    Beyond delimiter and maximum chunk length, you can also configure **Chunk overlap** to specify how many characters overlap between adjacent chunks. This helps preserve semantic connections and prevents important information from being split across chunk boundaries.

    For example, with a 50-character overlap, the last 50 characters of one chunk will also appear as the first 50 characters of the next chunk.

  **Parent-child:**

    In Parent-child mode, text is split into two tiers: smaller **child chunks** and larger **parent chunks**. When a query matches a child chunk, its entire parent chunk is returned as the retrieval result.

    This solves a common retrieval dilemma: smaller chunks enable precise query matching but lack context, while larger chunks provide rich context but reduce retrieval accuracy.

    Parent-child mode balances both: retrieving with precision and responding with context.

    **Parent Chunk Settings**

    Parent chunks can be created in **Paragraph** or **Full Doc** mode.

      **Paragraph:**

        The document is split into multiple parent chunks based on the specified delimiter and maximum chunk length.

        Suitable for lengthy documents with well-structured sections where each section provides meaningful context independently.

      **Full Doc:**

        The entire document serves as a single parent chunk.

        Suitable for small, cohesive documents where the full context is essential for understanding any specific detail.

        > **📝 Note:**
>           In **Full Doc** mode:
>
>           * Only the first 10,000 tokens are processed. Content beyond this limit will be truncated.
>
>           * The parent chunk cannot be edited once created. To modify it, you must upload a new document.
>

    **Child Chunk Settings**

    Each parent chunk is further split into child chunks using their own delimiter and maximum chunk length settings.

##### Quick Comparison

| Dimension                                                                                         | General Mode                                           | Parent-child Mode                                                                                 |
| :------------------------------------------------------------------------------------------------ | :----------------------------------------------------- | :------------------------------------------------------------------------------------------------ |
| Chunking Strategy                                                                                 | Single-tier: all chunks use the same settings          | Two-tier: separate settings for parent and child chunks                                           |
| Retrieval Workflow                                                                                | Matched chunks are directly returned                   | Child chunks are used for matching queries; parent chunks are returned to provide broader context |
| Compatible [Index Method](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/setting-indexing-methods) | High Quality, Economical                               | High Quality only                                                                                 |
| Best For                                                                                          | Simple, self-contained content like glossaries or FAQs | Information-dense documents like technical manuals or research papers where context matters       |

#### Pre-process Text Before Chunking

Before splitting text into chunks, you can clean up irrelevant content to improve retrieval quality.

* **Replace consecutive spaces, newlines, and tabs**

  * Three or more consecutive newlines → two newlines

  * Multiple spaces → single space

  * Tabs, form feeds, and special Unicode spaces → regular space

* **Remove all URLs and email addresses**

  > **ℹ️ Info:**
>     This setting is ignored in **Full Doc** mode.
>

#### Preview Chunks

Click **Preview** to see how your content will be chunked. A limited number of chunks will be displayed for a quick review.

If the results don't perfectly match your expectations, choose the closest configuration; you can manually fine-tune chunks later. See [Manage Knowledge Content](https://docs.dify.ai/en/cloud/use-dify/knowledge/manage-knowledge/maintain-knowledge-documents) for details.

For multiple documents, click the file name at the top of the preview panel to switch between them.

#### Upload Local Files

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/import-text-data/readme

> **📝 Note:**
>   Once a knowledge base is created, its data source cannot be changed later.

When creating a ready-to-use knowledge base, you can upload local files as its data source:

1. Click **Knowledge** > **Create** > **Create a ready-to-use knowledge base**.

2. Select **Import from file** as the data source, then upload your files.

   * Maximum number of files per upload: 5

   * Maximum file size: 15 MB

   > **ℹ️ Info:**
>      Batch uploading (up to 50 files per upload) is available on **[Professional]** and **[Team]**. [Learn more](https://dify.ai/pricing).
>

***

**For Images in Uploaded Files**

JPG, JPEG, PNG, and GIF images under 2 MB are automatically extracted as attachments to their corresponding chunks. These images can be managed independently and are returned alongside their chunks during retrieval.

URLs of extracted images remain in the chunk text, but you can safely remove these URLs to keep the text clean; this won't affect the extracted images.

If you select a multimodal embedding model (marked with a **Vision** icon) in index settings, the extracted images will also be embedded and indexed for retrieval.

Each chunk supports up to 10 image attachments; images beyond this limit will not be extracted.

The above extraction rule applies to:

* Images embedded in DOCX and XLSX files

  > **💡 Tip:**
>     Images embedded in other file types (e.g., PDF) can be extracted by using appropriate document extraction plugins in [knowledge pipelines](https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/readme).
>

* Images referenced via accessible URLs using the following Markdown syntax in any file type:

  * `![alt text](image_url)`
  * `![alt text](image_url "optional title")`

#### Sync Data from Notion

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/import-text-data/sync-from-notion

Dify datasets support importing from Notion and setting up **synchronization** so that data updates in Notion are automatically synced to Dify.

> **ℹ️ Info:**
>   Notion is connected through Dify's pre-configured integration. Authorize your workspace once and you're ready to import; no Notion app setup required.

##### Authorization Verification

1. When creating a dataset and selecting the data source, click **Sync from Notion Content -- Bind Now** and follow the prompts to complete the authorization verification.
2. Alternatively, you can go to **Settings -- Data Sources -- Add Data Source**, click on the Notion source **Bind**, and complete the authorization verification.

  ![Alternatively, You Can Go to Settings -- Data Sources -- Add Data Source, Click](https://assets-docs.dify.ai/2024/12/f1d5bcdcfbd57407e0bce1597df4daad.png)

##### Import Notion Data

After completing the authorization verification, go to the create dataset page, click **Sync from Notion Content**, and select the authorized pages you need to import.

  ![Completing the Authorization Verification, Go to the Create Dataset Page, Click](https://assets-docs.dify.ai/2025/04/f9199ff4747b5aaff563e226412723d0.png)

##### Chunking and Cleaning

Next, choose a [chunking mode](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/chunking-and-cleaning-text) and [indexing method](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/setting-indexing-methods) for your knowledge base, then save it and wait for the automatically processing. Dify not only supports importing standard Notion pages but can also consolidate and save page attributes from database-type pages.

> **📝 Note:**
>   Images and files cannot be imported, and data from tables will be converted to text.

  ![_Note](https://assets-docs.dify.ai/2025/04/723f7782853698598726d09997383747.png)

##### Synchronize Notion Data

If your Notion content has been updated, you can sync the changes by clicking the **Sync** button for the corresponding page in the document list of your knowledge base. Syncing involves an embedding process, which will consume tokens from your embedding model.

  ![If Your Notion Content Has Been Updated, You Can Sync the Changes by Clicking](https://assets-docs.dify.ai/2024/12/af7cabd98c3aac392819d9041cc408de.png)

#### Import Data from Website

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/import-text-data/sync-from-website

The knowledge base supports crawling content from public web pages using third-party tools such as [Jina Reader](https://jina.ai/reader/) and [Firecrawl](https://www.firecrawl.dev/), parsing it into Markdown content, and importing it into the knowledge base.

> **ℹ️ Info:**
>   ​[Firecrawl](https://www.firecrawl.dev/) and [Jina Reader](https://jina.ai/reader/) are both open-source web parsing tools that can convert web pages into clean Markdown format text that is easy for LLMs to recognize, while providing easy-to-use API services.

The following sections will introduce the usage methods for Firecrawl and Jina Reader respectively.

#### Firecrawl

##### **1. Configure Firecrawl API credentials**

Click on the avatar in the upper right corner, then go to the **DataSource** page, and click the **Configure** button next to Firecrawl.

  ![Configuring Firecrawl Credentials](https://assets-docs.dify.ai/2024/12/d468cf996f591b4b2bd0ffb5de62bad4.png)

Log in to the [Firecrawl website](https://www.firecrawl.dev/) to complete registration, get your API Key, and then enter and save it in Dify.

  ![Get the API Key and Save It in Dify](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRncMhlfeYTrpujwzDIqw%2Fuploads%2FtAwcLoAYT1A2v12pfJC3%2Fimage.png?alt=media\&token=3b5b784f-2808-431f-8595-2638d038c190)

##### 2. Scrape target webpage

On the knowledge base creation page, select **Sync from website**, choose Firecrawl as the provider, and enter the target URL to be crawled.

The configuration options include: Whether to crawl sub-pages, Page crawling limit, Page scraping max depth, Excluded paths, Include only paths, and Content extraction scope. After completing the configuration, click **Run** to preview the parsed pages.

  ![Execute Scraping](https://assets-docs.dify.ai/2024/12/3e63b4ced9770e21d5132c3aa8e5d2de.png)

##### 3. Review import results

After importing the parsed text from the webpage, it is stored in the knowledge base documents. View the import results and click **Add URL** to continue importing new web pages.

#### Jina Reader

##### 1. Configure Jina Reader Credentials

Click on the avatar in the upper right corner, then go to the **DataSource** page, and click the **Configure** button next to Jina Reader.

  ![Configuring Jina Reader](https://assets-docs.dify.ai/2024/12/28b37f9b36fe808b2d3302c48fce5ea3.png)

Log in to the [Jina Reader website](https://jina.ai/reader/), complete registration, obtain the API Key, then fill it in and save.

##### 2. Use Jina Reader to Crawl Web Content

On the knowledge base creation page, select **Sync from website**, choose Jina Reader as the provider, and enter the target URL to be crawled.

  ![Web Crawling Configuration](https://assets-docs.dify.ai/2024/12/f9170b2a2ab1be94bc85ff3ed3c3e723.png)

Configuration options include: whether to crawl subpages, maximum number of pages to crawl, and whether to use sitemap for crawling. After completing the configuration, click the **Run** button to preview the page links to be crawled.

  ![Executing the Crawl Process](https://assets-docs.dify.ai/2024/12/a875f21a751551c03109c76308c577ee.png)

After importing the parsed text from web pages into the knowledge base, you can review the imported results in the documents section. To add more web pages, click the **Add URL** button on the right to continue importing new pages.

  ![Importing Parsed Web Text into the Knowledge Base](https://assets-docs.dify.ai/2024/12/03494dc3c882ac1c74b464ea931e2533.png)

After crawling is complete, the content from the web pages will be incorporated into the knowledge base.

#### Create a Ready-to-Use Knowledge Base

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/introduction

To create a ready-to-use knowledge base:

1. Click **Knowledge** > **Create** > **Create a ready-to-use knowledge base**, then [upload local files](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/import-text-data/readme), [sync data from Notion](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/import-text-data/sync-from-notion), or [webpages](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/import-text-data/sync-from-website), or create an empty knowledge base.

2. [Configure the chunk settings](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/chunking-and-cleaning-text) and preview the chunking results. This stage involves content preprocessing and structuring, where long texts are divided into multiple smaller chunks.

3. [Specify the index method and retrieval settings](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/setting-indexing-methods). Once the knowledge base receives a user query, it searches existing documents according to preset retrieval methods and extracts highly relevant content chunks.

4. Wait for the data processing to complete.

  ![Wait for the Data Processing to Complete](https://assets-docs.dify.ai/2024/12/a3362a1cd384cb2b539c9858de555518.png)

#### Specify the Index Method and Retrieval Settings

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/setting-indexing-methods

After selecting the chunking mode, the next step is to define the index method for structured content.

#### Select the Index Method

Similar to the search engines use efficient indexing algorithms to match search results most relevant to user queries, the selected index method directly impacts the retrieval efficiency of the LLM and the accuracy of its responses to knowledge base content.

The knowledge base offers two index methods: **High-Quality** and **Economical**, each with different retrieval setting options.

  **High Quality:**

    > **📝 Note:**
>       Once a knowledge base is created in the High Quality index method, it cannot switch to Economical later.
>

    The High Quality index method uses an embedding model to convert content chunks into vector representations. This process is called embedding.

    Think of these vectors as coordinates in a multi-dimensional space—the closer two points are, the more similar their meanings. This allows the system to find relevant information based on semantic similarity, not just exact keyword matches.

    > **💡 Tip:**
>       To enable cross-modal retrieval—retrieving both text and images based on semantic relevance—select a multimodal embedding model (marked with a **Vision** icon). Images extracted from documents will then be embedded and indexed for retrieval.
>
>       Knowledge bases using such embedding models are labeled **Multimodal** on their cards.
>
>
>         *[Image: Multimodal Knowledge Base]*
>
>

    The High-Quality index method supports three retrieval strategies: vector search, full-text search, or hybrid search. Learn more in [Configure the Retrieval Settings](#configure-the-retrieval-settings).

  **Economical:**

    Using 10 keywords per chunk for retrieval, no tokens are consumed at the expense of reduced retrieval accuracy. For the retrieved blocks, only the inverted index method is provided to select the most relevant blocks.

    If the performance of the economical indexing method does not meet your expectations, you can upgrade to the High-Quality indexing method in the Knowledge settings page.

      ![Economical Mode](https://assets-docs.dify.ai/2024/12/3b86e6b484da39452c164cb6372a7242.png)

#### Configure the Retrieval Settings

Once the knowledge base receives a user query, it searches existing documents according to preset retrieval methods and extracts highly relevant content chunks. These chunks provide essential context for the LLM, ultimately affecting the accuracy and credibility of its answers.

Common retrieval methods include:

1. Semantic Retrieval based on vector similarity—where text chunks and queries are converted into vectors and matched via similarity scoring.
2. Keyword Matching using an inverted index (a standard search engine technique). Both methods are supported in Dify’s knowledge base.

Both retrieval methods are supported in Dify’s knowledge base. The specific retrieval options available depend on the chosen indexing method.

  **High Quality:**

    **High Quality**

    In the **High-Quality** Indexing Method, Dify offers three retrieval settings: **Vector Search, Full-Text Search, and Hybrid Search**.

      ![Retrieval Settings](https://assets-docs.dify.ai/2024/12/9b02fc353324221cc91f185a350775b6.png)

    **Vector Search**

    **Definition**: Vectorize the user’s question to generate a query vector, then compare it with the corresponding text vectors in the knowledge base to find the nearest chunks.

      ![Vector Search Settings](https://assets-docs.dify.ai/2024/12/620044faa47a5037f85b32a27a56fce5.png)

    **Vector Search Settings**:

    **Rerank Model**: Disabled by default. When enabled, a third-party Rerank model will sort the text chunks returned by Vector Search to optimize results. This helps the LLM access more precise information and improve output quality. Before enabling this option, go to **Integrations** > **Model Provider** and configure the Rerank model's API key.

    > **📝 Note:**
>       If the selected embedding model is multimodal, select a multimodal rerank model (marked with a **Vision** icon) as well. Otherwise, retrieved images will be excluded from reranking and the retrieval results.
>

    > Enabling this feature will consume tokens from the Rerank model. For more details, refer to the associated model’s pricing page.

    **TopK**: Determines how many text chunks, deemed most similar to the user’s query, are retrieved. It also automatically adjusts the number of chunks based on the chosen model’s context window. The default value is **3**, and higher numbers will recall more text chunks.

    **Score Threshold**: Sets the minimum similarity score required for a chunk to be retrieved. Only chunks exceeding this score are retrieved. The default value is **0.5**. Higher thresholds demand greater similarity and thus result in fewer chunks being retrieved.

    > The TopK and Score configurations are only effective during the Rerank phase. Therefore, to apply either of these settings, it is necessary to add and enable a Rerank model.

    **Full-Text Search**

    **Definition**: Indexing all terms in the document, allowing users to query any terms and return text fragments containing those terms.

      ![Full-Text Search Settings](https://assets-docs.dify.ai/2024/12/513bff1ca38ec746b3246502b0311b39.png)

    **Rerank Model**: Disabled by default. When enabled, a third-party Rerank model will sort the text chunks returned by Full-Text Search to optimize results. This helps the LLM access more precise information and improve output quality. Before enabling this option, go to **Integrations** > **Model Provider** and configure the Rerank model's API key.

    > **📝 Note:**
>       If the selected embedding model is multimodal, select a multimodal rerank model (marked with a **Vision** icon) as well. Otherwise, retrieved images will be excluded from reranking and the retrieval results.
>

    > Enabling this feature will consume tokens from the Rerank model. For more details, refer to the associated model’s pricing page.

    **TopK**: Determines how many text chunks, deemed most similar to the user’s query, are retrieved. It also automatically adjusts the number of chunks based on the chosen model’s context window. The default value is **3**, and higher numbers will recall more text chunks.

    **Score Threshold**: Sets the minimum similarity score required for a chunk to be retrieved. Only chunks exceeding this score are retrieved. The default value is **0.5**. Higher thresholds demand greater similarity and thus result in fewer chunks being retrieved.

    > The TopK and Score configurations are only effective during the Rerank phase. Therefore, to apply either of these settings, it is necessary to add and enable a Rerank model.

    **Hybrid Search**

    **Definition**: This process combines full-text search and vector search, performing both simultaneously. It includes a reordering step to select the best-matching results from both search outcomes based on the user’s query.

      ![Hybrid Retrieval Setting](https://assets-docs.dify.ai/2024/12/bd2621bfe8a1a8e21fca0743ec495a9e.png)

    In this mode, you can specify **"Weight settings"** without needing to configure the Rerank model API, or enable **Rerank model** for retrieval.

    * **Weight Settings**

      This feature enables users to set custom weights for semantic priority and keyword priority. Keyword search refers to performing a full-text search within the knowledge base, while semantic search involves vector search within the knowledge base.

      * **Semantic Value of 1**

        This activates only the semantic search mode. Utilizing embedding models, even if the exact terms from the query do not appear in the knowledge base, the search can delve deeper by calculating vector distances, thus returning relevant content. Additionally, when dealing with multilingual content, semantic search can capture meaning across different languages, providing more accurate cross-language search results.
      * **Keyword Value of 1**

        This activates only the keyword search mode. It performs a full match against the input text in the knowledge base, suitable for scenarios where the user knows the exact information or terminology. This approach consumes fewer computational resources and is ideal for quick searches within a large document knowledge base.
      * **Custom Keyword and Semantic Weights**

        In addition to enabling only semantic search or keyword search, we provide flexible custom weight settings. You can continuously adjust the weights of the two methods to identify the optimal weight ratio that suits your business scenario.
        **Rerank Model**

      Disabled by default. When enabled, a third-party Rerank model will sort the text chunks returned by Hybrid Search to optimize results. This helps the LLM access more precise information and improve output quality. Before enabling this option, go to **Integrations** > **Model Provider** and configure the Rerank model's API key.

      > **📝 Note:**
>         If the selected embedding model is multimodal, select a multimodal rerank model (marked with a **Vision** icon) as well. Otherwise, retrieved images will be excluded from reranking and the retrieval results.
>

      > Enabling this feature will consume tokens from the Rerank model. For more details, refer to the associated model’s pricing page.

    The **"Weight Settings"** and **"Rerank Model"** settings support the following options:

    **TopK**: Determines how many text chunks, deemed most similar to the user’s query, are retrieved. It also automatically adjusts the number of chunks based on the chosen model’s context window. The default value is **3**, and higher numbers will recall more text chunks.

    **Score Threshold**: Sets the minimum similarity score required for a chunk to be retrieved. Only chunks exceeding this score are retrieved. The default value is **0.5**. Higher thresholds demand greater similarity and thus result in fewer chunks being retrieved.

  **Economical:**

    **Economical**

    In **Economical Indexing** mode, only the inverted index approach is available. An inverted index is a data structure designed for fast keyword retrieval within documents, commonly used in online search engines. Inverted indexing supports only the **TopK** setting.

    **TopK**: Determines how many text chunks, deemed most similar to the user’s query, are retrieved. It also automatically adjusts the number of chunks based on the chosen model’s context window. The default value is **3**, and higher numbers will recall more text chunks.

    

        ![](https://assets-docs.dify.ai/2025/04/b417cd028131d34779993fbcbb8dbdd7.png)

    

##### Reference

After specifying the retrieval settings, you can refer to the following documentation to review how keywords match with content chunks in different scenarios.

- **[Test Knowledge Retrieval](https://docs.dify.ai/en/cloud/use-dify/knowledge/test-retrieval)** — Learn how to test and cite your knowledge base retrieval

#### External Knowledge API

*API specification that your external knowledge service must implement to integrate with Dify*

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/external-knowledge-api

API specification that your external knowledge service must implement to integrate with Dify

This page defines the API contract your external knowledge service must implement for Dify to retrieve content from it. Once your API is ready, see [Connect to External Knowledge Base](https://docs.dify.ai/en/cloud/use-dify/knowledge/connect-external-knowledge-base) to register it in Dify.

#### Authentication

Dify sends the API Key you configured as a Bearer token in every request:

```text theme={null}
Authorization: Bearer {API_KEY}
```

You define the authentication logic on your side. Dify only passes the key—it does not validate it.

#### Request

```text theme={null}
POST {your-endpoint}/retrieval
Content-Type: application/json
Authorization: Bearer {API_KEY}
```

Dify appends `/retrieval` to the endpoint URL you configured. If you registered `https://your-service.com`, Dify sends requests to `https://your-service.com/retrieval`.

##### Body

| Property             | Required | Type   | Description                                                                                                                                                                                                    |
| :------------------- | :------- | :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `knowledge_id`       | Yes      | string | The identifier of the knowledge source in your external system. This is the value you entered in the **External Knowledge ID** field when connecting. Use it to route queries to the correct knowledge source. |
| `query`              | Yes      | string | The user's search query.                                                                                                                                                                                       |
| `retrieval_setting`  | Yes      | object | Retrieval parameters. See [below](#retrieval_setting).                                                                                                                                                         |
| `metadata_condition` | No       | object | Metadata filtering conditions. See [below](#metadata_condition).                                                                                                                                               |

###### `retrieval_setting`

| Property          | Required | Type  | Description                                                                                    |
| :---------------- | :------- | :---- | :--------------------------------------------------------------------------------------------- |
| `top_k`           | Yes      | int   | Maximum number of results to return.                                                           |
| `score_threshold` | Yes      | float | Minimum similarity score (0-1). When score threshold is disabled in Dify, this value is `0.0`. |

###### `metadata_condition`

> **ℹ️ Info:**
>   Dify passes metadata conditions to your API but does not currently provide a UI for users to configure them. This parameter is available for programmatic use only.

| Property           | Required | Type           | Description                    |
| :----------------- | :------- | :------------- | :----------------------------- |
| `logical_operator` | No       | string         | `and` or `or`. Default: `and`. |
| `conditions`       | Yes      | array[object] | List of filter conditions.     |

Each object in `conditions`:

| Property              | Required | Type                              | Description                                               |
| :-------------------- | :------- | :-------------------------------- | :-------------------------------------------------------- |
| `name`                | Yes      | string                            | Metadata field name to filter on.                         |
| `comparison_operator` | Yes      | string                            | Comparison operator. See supported values below.          |
| `value`               | No       | string, number, or array[string] | Comparison value. Omit when using `empty` or `not empty`. |

**Supported Comparison Operators:**

  | Operator       | Description                        |
  | :------------- | :--------------------------------- |
  | `contains`     | Contains a value                   |
  | `not contains` | Does not contain a value           |
  | `start with`   | Starts with a value                |
  | `end with`     | Ends with a value                  |
  | `is`           | Equals a value                     |
  | `is not`       | Does not equal a value             |
  | `in`           | Matches any value in a list        |
  | `not in`       | Does not match any value in a list |
  | `empty`        | Is empty                           |
  | `not empty`    | Is not empty                       |
  | `=`            | Equals (numeric)                   |
  | `≠`            | Not equal (numeric)                |
  | `>`            | Greater than                       |
  | `<`            | Less than                          |
  | `≥`            | Greater than or equal to           |
  | `≤`            | Less than or equal to              |
  | `before`       | Before a date                      |
  | `after`        | After a date                       |

##### Example Request

```json theme={null}
{
    "knowledge_id": "your-knowledge-id",
    "query": "What is Dify?",
    "retrieval_setting": {
        "top_k": 3,
        "score_threshold": 0.5
    }
}
```

#### Response

Return HTTP 200 with a JSON body containing a `records` array. If no results match the query, return an empty array: `{"records": []}`.

##### `records`

| Property   | Type   | Description                                                                    |
| :--------- | :----- | :----------------------------------------------------------------------------- |
| `content`  | string | The retrieved text chunk. Dify uses this as the context passed to the LLM.     |
| `score`    | float  | Similarity score (0–1). Used for score threshold filtering and result ranking. |
| `title`    | string | Source document title.                                                         |
| `metadata` | object | Arbitrary key-value pairs preserved by Dify.                                   |

Dify does not reject records with missing fields, but omitting `content` or `score` will produce incomplete or unranked results.

> **⚠️ Warning:**
>   If you include `metadata` in a record, it must be an object (`{}`), not `null`. A `null` metadata value causes errors in Dify's retrieval pipeline.

##### Example Response

```json theme={null}
{
    "records": [
        {
            "content": "This is the document for external knowledge.",
            "score": 0.98,
            "title": "knowledge.txt",
            "metadata": {
                "path": "s3://dify/knowledge.txt",
                "description": "dify knowledge document"
            }
        },
        {
            "content": "The Innovation Engine for GenAI Applications",
            "score": 0.66,
            "title": "introduce.txt",
            "metadata": {}
        }
    ]
}
```

#### Error Handling

Dify checks the HTTP status code of your response. A non-200 status raises an error that surfaces to the user.

You can optionally return structured error information in JSON:

| Property     | Type   | Description                                 |
| :----------- | :----- | :------------------------------------------ |
| `error_code` | int    | An application-level error code you define. |
| `error_msg`  | string | A human-readable error description.         |

The following are suggested error codes. These are conventions, not enforced by Dify:

| Code | Suggested Usage                     |
| :--- | :---------------------------------- |
| 1001 | Invalid Authorization header format |
| 1002 | Authorization failed                |
| 2001 | Knowledge base not found            |

##### Example Error Response

```json theme={null}
{
    "error_code": 1002,
    "error_msg": "Authorization failed. Please check your API key."
}
```

#### Integrate Knowledge within Apps

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/integrate-knowledge-within-application

##### Create an Application Integrated with Knowledge Base

A **"Knowledge Base"** can be used as an external information source to provide precise answers to user questions via LLM. You can associate an existing knowledge base with any [application type](https://docs.dify.ai/en/learn/key-concepts#dify-app) in Dify.

Taking a chat assistant as an example, the process is as follows:

1. Go to **Knowledge**, create a **ready-to-use knowledge base**, and upload your file
2. Go to **Studio**, create an application, and select **Chatbot**
3. Enter **Context**, click **Add**, and select one of the knowledge bases you created
4. Use **Metadata Filtering** to refine document search in your knowledge base
5. In **Context Settings -- Retrieval Setting**, configure the **Retrieval Setting**
6. Enable **Citation and Attribution** in **Add Features**
7. In **Debug and Preview**, input user questions related to the knowledge base for debugging
8. After debugging, click **Publish** button to make an AI application based on your own knowledge!

##### Connect Knowledge and Set Retrieval Mode

In applications that utilize multiple knowledge bases, it is essential to configure the retrieval mode to enhance the precision of retrieved content. To set the retrieval mode for the knowledge bases, navigate to **Context -- Retrieval Settings -- Rerank Setting**.

###### Retrieval Setting

The retriever scans all knowledge bases linked to the application for text content relevant to the user's question. The results are then consolidated. Below is the technical flowchart for the Multi-path Retrieval mode:

  ![](https://assets-docs.dify.ai/2025/03/037f48c5c162fb8902600674ab973c29.png)

This method simultaneously queries all knowledge bases connected in **"Context"**, seeking relevant text chucks across multiple knowledge bases, collecting all content that aligns with the user's question, and ultimately applying the Rerank strategy to identify the most appropriate content to respond to the user. This retrieval approach offers more comprehensive and accurate results by leveraging multiple knowledge bases simultaneously.

  ![](https://assets-docs.dify.ai/2024/12/fca4f030e71a857e15a753f508e1b042.png)

For instance, in application A, with three knowledge bases K1, K2, and K3. When a user send a question, multiple relevant pieces of content will be retrieved and combined from these knowledge bases. To ensure the most pertinent content is identified, the Rerank strategy is employed to find the content that best relates to the user's query, enhancing the precision and reliability of the results.

In practical Q\&A scenarios, the sources of content and retrieval methods for each knowledge base may differ. To manage the mixed content returned from retrieval, the Rerank strategy acts as a refined sorting mechanism. It ensures that the candidate content aligns well with the user's question, optimizing the ranking of results across multiple knowledge bases to identify the most suitable content, thereby improving answer quality and overall user experience.

Considering the costs associated with using Rerank and the needs of the business, the multi-path retrieval mode provides two Rerank settings:

**Weighted Score**

This setting uses internal scoring mechanisms and does not require an external Rerank model, thus **avoiding any additional processing costs**. You can select the most appropriate content matching strategy by adjusting the weight ratio sliders for semantics or keywords.

* **Semantic Value of 1**

  This mode activates semantic retrieval only. By utilizing the Embedding model, the search depth can be enhanced even if the exact words from the query do not appear in the knowledge base, as it calculates vector distances to return the relevant content. Furthermore, when dealing with multilingual content, semantic retrieval can capture meanings across different languages, yielding more accurate cross-language search results.
* **Keyword Value of 1**

  This mode activates keyword retrieval only. It matches the user's input text against the full text of the knowledge base, making it ideal for scenarios where the user knows the exact information or terminology. This method is resource-efficient, making it suitable for quickly retrieving information from large document repositories.
* **Custom Keyword and Semantic Weights**

  In addition to enabling only semantic or keyword retrieval modes, we offer flexible custom Weight Score. You can determine the best weight ratio for your business scenario by continuously adjusting the weights of both.

**Rerank Model**

The Rerank model is an external scoring system that calculates the similarity score between the user's question and each candidate document provided, improving the results of semantic ranking and returning a list of documents sorted by similarity score from high to low.

While this method incurs some additional costs, it is more adept at handling complex knowledge base content, such as content that combines semantic queries and keyword matches, or cases involving multilingual returned content.

Dify currently supports multiple Rerank models. To use external Rerank models, you'll need to provide an API Key. Enter the API Key for the Rerank model (such as Cohere, Jina AI, etc.) on the "Model Provider" page.

  ![Dify Currently Supports Multiple Rerank Models](https://assets-docs.dify.ai/2025/03/2ea86356a57f2ba8a57f9661cae4a305.png)

**Adjustable Parameters**

* **TopK**: Determines how many text chunks, deemed most similar to the user’s query, are retrieved. It also automatically adjusts the number of chunks based on the chosen model’s context window. The default value is **3**, and higher numbers will recall more text chunks.
* **Score Threshold**: Sets the minimum similarity score required for a chunk to be retrieved. Only chunks exceeding this score are retrieved. The default value is **0.5**. Higher thresholds demand greater similarity and thus result in fewer chunks being retrieved.

##### Metadata Filtering

###### Chatflow/Workflow

The **Knowledge Retrieval** node allows you to filter documents using metadata fields.

###### Steps

1. Select Filter Mode:

   * **Disabled (Default)**: No metadata filtering.

   * **Automatic**: Filters auto-configure from query variables in the **Knowledge Retrieval** node.

   > Note: Automatic Mode requires model selection for document retrieval.

     ![Model_Selection](https://assets-docs.dify.ai/2025/03/fe387793ad9923660f9f9470aacff01b.png)

   * **Manual**: Configure filters manually.

  ![Manual](https://assets-docs.dify.ai/2025/03/ec6329e265e035e3a0d6941c9313a19d.png)

2. For Manual Mode, follow these steps:

   1. Click **Conditions** to open the configuration panel.

     ![Conditions](https://assets-docs.dify.ai/2025/03/cd80d150f6f5646350b7ac8dfee46429.png)

   2. Click **+Add Condition**:
      * Select metadata fields within your chosen knowledge base from the dropdown list.
      > Note: When multiple knowledge bases are selected, only common metadata fields are shown in the list.
      * Use the search box to find specific fields.

     ![Add_Condition](https://assets-docs.dify.ai/2025/03/72678c4174f753f306378b748fbe6635.png)

   3. Click **+Add Condition** to add more fields.

     ![Add_More_Fields](https://assets-docs.dify.ai/2025/03/aeb518c40aabdf467c9d2c23016d0a16.png)

   4. Configure filter conditions:

   | Field Type | Operator     | Description and Examples                                                                                                      |
   | ---------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------- |
   | String     | is           | Exact match required. Example: `is "Published"` returns only documents marked exactly as "Published".                         |
   |            | is not       | Excludes exact matches. Example: `is not "Draft"` returns all documents except those marked as "Draft".                       |
   |            | is empty     | Returns documents where the field has no value.                                                                               |
   |            | is not empty | Returns documents where the field has any value.                                                                              |
   |            | contains     | Matches partial text. Example: `contains "Report"` returns "Monthly Report", "Annual Report", etc.                            |
   |            | not contains | Excludes documents containing specified text. Example: `not contains "Draft"` returns documents without "Draft" in the field. |
   |            | starts with  | Matches text at beginning. Example: `starts with "Doc"` returns "Doc1", "Document", etc.                                      |
   |            | ends with    | Matches text at end. Example: `ends with "2024"` returns "Report 2024", "Summary 2024", etc.                                  |
   | Number     | =            | Exact number match. Example: `= 10` returns documents marked with exactly 10.                                                 |
   |            | ≠            | Excludes specific number. Example: `≠ 5` returns all documents except those marked with 5.                                    |
   |            | >            | Greater than. Example: `&gt; 100` returns documents with values above 100.                                                    |
   |            | \<           | Less than. Example: `&lt; 50` returns documents with values below 50.                                                         |
   |            | ≥            | Greater than or equal to. Example: `≥ 20` returns documents with values 20 or higher.                                         |
   |            | ≤            | Less than or equal to. Example: `≤ 200` returns documents with values 200 or lower.                                           |
   |            | is empty     | Field has no value assigned. For example, `is empty` returns all documents where this field has no number assigned.           |
   |            | is not empty | Field has a value assigned. For example, `is not empty` returns all documents where this field has a number assigned.         |
   | Date       | is           | Exact date match. Example: `is "2024-01-01"` returns documents dated January 1, 2024.                                         |
   |            | before       | Prior to date. Example: `before "2024-01-01"` returns documents dated before January 1, 2024.                                 |
   |            | after        | After date. Example: `after "2024-01-01"` returns documents dated after January 1, 2024.                                      |
   |            | is empty     | Returns documents with no date value.                                                                                         |
   |            | is not empty | Returns documents with any date value.                                                                                        |

   5. Add filter values:

   * **Variable**: Select from existing **Chatflow/Workflow** variables.

     ![Variable](https://assets-docs.dify.ai/2025/03/4c2c55ffcf0f72553fabdf23f86597d0.png)

   * **Constant**: Enter specific values.

   > Time-type fields can only be filtered by constants The date picker is for time-type fields.

     ![Date_Picker](https://assets-docs.dify.ai/2025/03/593da1575ddc995d938bd0cc3847cf3c.png)

> **ℹ️ Info:**
>   Filter values are case-sensitive and require exact matches. Example: a filter `starts with "App"` or `contains "App"` will match "Apple" but not "apple" or "APPLE".

6. Set logic operators:
   * `AND`: Match all conditions
   * `OR`: Match any condition

  ![Logic](https://assets-docs.dify.ai/2025/03/822dac015308dc5c01768afc0697c1ad.png)

7. Click outside the panel to save your settings.

###### Chatbot

Access **Metadata Filtering** below **Knowledge** (bottom-left). Configuration steps are the same as in **Chatflow/Workflow**.

  ![Chatbot](https://assets-docs.dify.ai/2025/03/9d9a64bde687a686f24fd99d6f193c57.png)

##### View Linked Applications in the Knowledge Base

On the left side of the knowledge base, you can see all linked Apps. Hover over the circular icon to view the list of all linked apps. Click the jump button on the right to quickly browser them.

  ![](https://assets-docs.dify.ai/2024/12/28899b9b0eba8996f364fb74e5b94c7f.png)

##### Frequently Asked Questions

11. **How should I choose Rerank settings in multi-recall mode?**

If users know the exact information or terminology, you can use keyword search for precise matching. In that case, set **"Keywords" to 1** under Weight Settings.

If the knowledge base doesn't contain the exact terms or if a cross-lingual query is involved, we recommend setting **"Semantic" to 1** under Weight Settings.

If you are familiar with real user queries and want to adjust the ratio of semantics to keywords, they can manually tweak the ratio under **Weight Settings**.

If the knowledge base is complex, making simple semantic or keyword matches insufficient—and you need highly accurate answers and are willing to pay more—consider using a **Rerank Model** for content retrieval.

2. **What should I do if I encounter issues finding the "Weight Score" or the requirement to configure a Rerank model?**

Here's how the knowledge base retrieval method affects Multi-path Retrieval:

  ![How the Knowledge Base Retrieval Method Affects Multi-Path Retrieval](https://assets-docs.dify.ai/2025/03/a64394f5df4266c34ed10330d9518946.png)

3. **What should I do if I cannot adjust the "Weight Score" when referencing multiple knowledge bases and an error message appears?**

This issue occurs because the embedding models used in the multiple referenced knowledge bases are inconsistent, prompting this notification to avoid conflicts in retrieval content. It is advisable to set and enable the Rerank model in the "Model Provider" or unify the retrieval settings of the knowledge bases.

4. **Why can't I find the "Weight Score" option in multi-recall mode, and only see the Rerank model?**

Please check whether your knowledge base is using the "Economical" index mode. If so, switch it to the "High Quality" index mode.

#### Authorize Data Source

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/authorize-data-source

Dify supports connections to various external data sources. To ensure data security and access control, different data sources require appropriate authorization configurations. Dify provides two main authorization methods: **API Key** and **OAuth**.

#### Access Data Source Authorization

In Dify, you can access data source authorization through the following two methods:

##### I. Knowledge Pipeline Orchestration

When orchestrating a knowledge pipeline, select the data source node that requires authorization. Click **Connect** on the right panel.

  *[Image: Knowledge Pipeline Authorization]*

##### II. Settings

Click your avatar in the upper right corner and select **Settings**. Navigate to **Data Sources** and find the data source you wish to authorize.

  *[Image: Settings Authorization]*

#### Supported Data Source Authorization

| Data Source  | API Key | OAuth |
| ------------ | ------- | ----- |
| Notion       | ✅       | ✅     |
| Jina Reader  | ✅       |       |
| Firecrawl    | ✅       |       |
| Google Drive |         | ✅     |
| Dropbox      |         | ✅     |
| OneDrive     |         | ✅     |

#### Authorization Processes

##### API Key Authorization

API Key authorization is a key-based authentication method suitable for enterprise-level services and developer tools. You need to generate API Keys from the corresponding service providers and configure them in Dify.

###### Process

1. On the **Data Source** page, navigate to the corresponding data source. Click **Configure** and then **Add API Key**.

     *[Image: Add API Key]*

2. In the pop-up window, fill in the **Authorization Name** and **API Key**. Click **Save** to complete the setup.

     *[Image: API Key Configuration]*

The API key will be securely encrypted. Once completed, you can start using the data source (e.g., Jina Reader) for knowledge pipeline orchestration.

  *[Image: API Key Complete]*

##### OAuth Authorization

OAuth is an open standard authorization protocol that allows users to authorize third-party applications to access their resources on specific service providers without exposing passwords.

###### Process

1. On the **Data Source** page, select an OAuth-supported data source. Click **Configure** and then **Add OAuth**.

     *[Image: Add OAuth]*

2. Review the permission scope and click **Allow Access**.

  

      *[Image: OAuth Permissions]*

  

  

      *[Image: OAuth Allow]*

  

###### OAuth Client Settings

Dify provides two OAuth client configuration methods: **Default** and **Custom**.

  *[Image: OAuth Client Settings]*

  **Default:**

    The default client uses OAuth parameters that Dify pre-configures and maintains, so you can add credentials in one click without any extra setup.

  **Custom:**

    The custom client lets you register your own OAuth application on the third-party platform and provide its parameters. Use it for data sources without a default client, or when you have specific security or compliance requirements.

    **Process for Custom OAuth**

    1. On the **Data Source** page, select an OAuth-supported data source. Click **Configure** and then the **Setting icon** on the right side of **Add OAuth**.

         *[Image: Custom OAuth Settings]*

    2. Choose **Custom**, enter the **Client ID** and **Client Secret**. Click **Save and Authorize** to complete the authorization.

         *[Image: Custom OAuth Configuration]*

#### Step 1: Create Knowledge Pipeline

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/create-knowledge-pipeline

Navigate to **Knowledge** at the top, then click **Create** > **Build a custom knowledge base**. There are three ways for you to get started.

##### Build from Scratch

  *[Image: Build from Scratch]*

Click Blank Knowledge Pipeline to build a custom pipeline from scratch. Choose this option when you need custom processing strategies based on specific data source and business requirements.

##### Templates

Dify offers two types of templates: **Built-in Pipeline** and **Customized**. Both template cards display name of knowledge base, description, and tags (including chunk structure).

  *[Image: Create Knowledge Pipeline 4 01]*

###### Built-in Pipeline

Built-in pipelines are official knowledge base templates pre-configured by Dify. These templates are optimized for common document structures and use cases. Simply click **Choose** to get started.

  *[Image: Built-in Templates]*

**Types**

| Name                | Chunk Structure   | Index Method | Retrieval Setting              | Description                                                                                                                                                                                                                  |
| ------------------- | ----------------- | ------------ | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General Mode-ECO    | General           | Economical   | Inverted Index                 | Divide document content into smaller paragraphs, directly used for matching user queries and retrieval.                                                                                                                      |
| Parent-child-HQ     | Parent-Child      | High Quality | Hybrid Search                  | Adopt advanced chunking strategy, dividing document text into larger parent chunks and smaller child chunks. The parent chunks contain child chunks which ensure both retrieval precision and maintain contextual integrity. |
| Simple Q\&A         | Question & Answer | High Quality | Vector Search                  | Convert tabular data into question-answer format, using question matching to quickly hit corresponding answer information.                                                                                                   |
| LLM Generated Q\&A  | Question & Answer | High Quality | Vector Search                  | Generate structured question-answer pairs with large language models based on original text paragraphs. Find relevant answer by using question matching mechanism.                                                           |
| Convert to Markdown | Parent-child      | High Quality | Hybrid Search - Weighted Score | Designed for Office native file formats such as DOCX, XLSX, and PPTX, converting them to Markdown format for better information processing. ⚠️ Note: PDF files are not recommended.                                          |

To preview the selected built-in pipeline, click **Details** on any template card. Then, check information in the popup window, including: orchestration structure, pipeline description, and chunk structure. Click **Use this Knowledge Pipeline** for orchestration.

  *[Image: Template Details]*

###### Customized

  *[Image: Customized Templates]*

Customized templates are user-created and published knowledge pipeline. You can choose a template to start, export the DSL, or view detailed information for any template.

  *[Image: Template Actions]*

To create a knowledge base from a template, click **Choose** on the template card. You can also create knowledge base by clicking **Use this Knowledge Pipeline** when previewing a template. Click **More** to edit pipeline information, export pipeline, or delete the template.

##### Import Pipeline

  *[Image: Import DSL]*

Import a pipeline of a previously exported knowledge pipeline to quickly reuse existing configurations and modify them for different scenarios or requirements. Navigate to the bottom left of the page and click **Import from a DSL File**. Dify DSL is a YAML-based standard that defines AI application configurations, including model parameters, prompt design, and workflow orchestration. Similar to workflow DSL, knowledge pipeline uses the same YAML format standard to define processing workflows and configurations within a knowledge base.

What's in a knowledge pipeline DSL:

| Name                    | Description                                                        |
| ----------------------- | ------------------------------------------------------------------ |
| Data Sources            | Local files, websites, online documents, online drive, web crawler |
| Data Processing         | Document extraction, content chunking, cleaning strategies         |
| Knowledge Configuration | Indexing methods, retrieval settings, storage parameters           |
| Node Orchestration      | Arrangement and sequence                                           |
| User Input Form         | Custom parameter fields (if configured)                            |

#### Step 2: Orchestrate Knowledge Pipeline

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/knowledge-pipeline-orchestration

Imagine setting up a factory production line where each station (node) performs a specific task, and you connect them to assemble widgets into a final product. This is knowledge pipeline orchestration—a visual workflow builder that allows you to configure data processing sequences through a drag-and-drop interface. It provides control over document ingestion, processing, chunking, indexing, and retrieval strategies.

In this section, you'll learn about the knowledge pipeline process, understand different nodes, how to configure them, and customize your own data processing workflows to efficiently manage and optimize your knowledge base.

##### Interface Status

When entering the knowledge pipeline orchestration canvas, you’ll see:

* **Tab Status**: Documents, Retrieval Test, and Settings tabs will be grayed out and unavailable at the moment
* **Essential Steps**: You must complete knowledge pipeline orchestration and publishing before uploading files

Your starting point depends on the template choice you made previously. If you chose **Blank Knowledge Pipeline**, you'll see a canvas that contains Knowledge Base node only. There'll be a note with guide next to the node that walks you through the general steps of pipeline creation.

  *[Image: Blank Pipeline]*

If you selected a specific pipeline template, there'll be a ready-to-use workflow that you can use or modify on the canvas right away.

  *[Image: Template Pipeline]*

#### The Complete Knowledge Pipeline Process

Before we get started, let's break down the knowledge pipeline process to understand how your documents are transformed into a searchable knowledge base.

The knowledge pipeline includes these key steps:

> **💡 Tip:**
>   Data Source → Data Processing (Extractor + Chunker) → Knowledge Base Node (Chunk Structure + Retrieval Setting) → User Input Field → Test & Publish

1. **Data Source**: Content from various data sources (local files, Notion, web pages, etc.)
2. **Data Processing**: Process and transform data content
   * Extractor: Parse and structure document content
   * Chunker: Split structured content into manageable segments
3. **Knowledge Base**: Set up chunk structure and retrieval settings
4. **User Input Field**: Define parameters that pipeline users need to input for data processing
5. **Test & Publish**: Validate and officially activate the knowledge base

***

#### Step 1: Data Source

In a knowledge base, you can choose single or multiple data sources. Currently, Dify supports 4 types of data sources: **file upload, online drive, online documents, and web crawler**.

Visit the [Dify Marketplace](https://marketplace.dify.ai) for more data sources.

##### File Upload

Upload local files through drag-and-drop or file selection.

  

      *[Image: Knowledge Pipeline Orchestration 01]*

  

  
    **Configuration Options**

    | Item          | Description                                                                                       |
    | ------------- | ------------------------------------------------------------------------------------------------- |
    | File Format   | Support PDF, XLSX, DOCX, etc. Users can customize their selection                                 |
    | Upload Method | Upload local files or folders through drag-and-drop or file selection. Batch upload is supported. |

    **Limitations**

    | Item          | Description                                                        |
    | ------------- | ------------------------------------------------------------------ |
    | File Quantity | Maximum 50 files per upload                                        |
    | File Size     | Each file must not exceed 15MB                                     |
    | Storage       | Total document uploads and storage space vary by subscription plan |

    **Output Variables**

    | Output Variable | Format          |
    | --------------- | --------------- |
    | `{x} Document`  | Single document |
  

***

##### Online Document

###### Notion

Integrate with your Notion workspace to seamlessly import pages and databases, always keeping your knowledge base automatically updated.

  

      *[Image: Notion]*

  

  
    **Configuration Options**

    | Item      | Option   | Output Variable | Description                          |
    | --------- | -------- | --------------- | ------------------------------------ |
    | Extractor | Enabled  | `{x} Content`   | Structured and processed information |
    |           | Disabled | `{x} Document`  | Original text                        |
  

***

##### Web Crawler

Transform web content into formats that can be easily read by large language models. The knowledge base supports Jina Reader and Firecrawl.

###### Jina Reader

An open-source web parsing tool providing simple and easy-to-use API services, suitable for fast crawling and processing web content.

  

      *[Image: Jina Reader]*

  

  
    **Parameter Configuration**

    | Parameter        | Type     | Description                          |
    | ---------------- | -------- | ------------------------------------ |
    | URL              | Required | Target webpage address               |
    | Crawl sub-page   | Optional | Whether to crawl linked pages        |
    | Use sitemap      | Optional | Crawl by using website sitemap       |
    | Limit            | Required | Set maximum number of pages to crawl |
    | Enable Extractor | Optional | Choose data extraction method        |
  

###### Firecrawl

An open-source web parsing tool that provides more refined crawling control options and API services. It supports deep crawling of complex website structures, recommended for batch processing and precise control.

  

      *[Image: Knowledge Pipeline Orchestration 04]*

  

  
    **Parameter Configuration**

    | Parameter                 | Type     | Description                                                                |
    | ------------------------- | -------- | -------------------------------------------------------------------------- |
    | URL                       | Required | Target webpage address                                                     |
    | Limit                     | Required | Set maximum number of pages to crawl                                       |
    | Crawl sub-page            | Optional | Whether to crawl linked pages                                              |
    | Max depth                 | Optional | How many levels deep the crawler will traverse from the starting URL       |
    | Exclude paths             | Optional | Specify URL patterns that should not be crawled                            |
    | Include only paths        | Optional | Crawl specified paths only                                                 |
    | Extractor                 | Optional | Choose data processing method                                              |
    | Extract Only Main Content | Optional | Isolate and retrieve the primary, meaningful text and media from a webpage |
  

***

##### Online Drive

Connect your online cloud storage services (e.g., Google Drive, Dropbox, OneDrive) and let Dify automatically retrieve your files. Simply select and import the documents you need for processing, without manually downloading and re-uploading files.

> **💡 Tip:**
>   Need help with authorization? Please check [Authorize Data Source](https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/authorize-data-source) for detailed guidance on authorizing different data sources.

***

#### Step 2: Set Up Data Processing Tools

In this stage, these tools extract, chunk, and transform the content for optimal knowledge base storage and retrieval. Think of this step like meal preparation. We clean raw materials up, chop them into bite-sized pieces, and organize everything, so the dish can be cooked up quickly when someone orders it.

> **💡 Tip:**
>   To develop a custom data processing plugin that extracts multimodal data for multimodal embedding and retrieval, see [Build Tool Plugins for Multimodal Data Processing in Knowledge Pipelines](https://docs.dify.ai/en/develop-plugin/dev-guides-and-walkthroughs/develop-multimodal-data-processing-tool).

##### Doc Processor

Documents come in different formats - PDF, XLSX, DOCX. However, LLM can't read these files directly. That's where extractors come in. They support multiple formats and handle the conversion, so your content is ready for the next step of the LLMs.

You can choose Dify's Doc Extractor to process files, or select tools based on your needs from Marketplace which offers Dify Extractor and third-party tools such as Unstructured.

**For images in documents:**

  Images in documents can be extracted using appropriate document processors. Extracted images are attached to their corresponding chunks, can be managed independently, and are returned alongside those chunks during retrieval.

  URLs of extracted images remain in the chunk text, but you can safely remove these URLs to keep the text clean—this won't affect the extracted images.

  Each chunk supports up to 10 image attachments; images beyond this limit will not be extracted.

  If no images are extracted by the selected processor, Dify will automatically extract JPG, JPEG, PNG, and GIF images under 2 MB that are referenced via accessible URLs using the following Markdown syntax:

  * `![alt text](image_url)`
  * `![alt text](image_url "optional title")`

  If you select a multimodal embedding model (marked with a **Vision** icon) in index settings, the extracted images will also be embedded and indexed for retrieval.

###### Doc Extractor

  *[Image: Knowledge Pipeline Orchestration 4 01]*

As an information processing center, document extractor node identifies and reads files from input variables, extracts information, and finally converts them into a format that works with the next node.

> **💡 Tip:**
>   For more information, please refer to the [Document Extractor](https://docs.dify.ai/en/cloud/use-dify/nodes/doc-extractor).

###### Dify Extractor

Dify Extractor is a built-in document parser presented by Dify. It supports multiple common file formats and is specially optimized for Doc files. It can extract and store images from documents and return image URLs.

  *[Image: Dify Extractor]*

###### Unstructured

  

      *[Image: Unstructured]*

  

  
    [Unstructured](https://marketplace.dify.ai/plugin/langgenius/unstructured) transforms documents into structured, machine-readable formats with highly customizable processing strategies. It offers multiple extraction strategies (auto, hi_res, fast, OCR-only) and chunking methods (by_title, by_page, by_similarity) to handle diverse document types, offering detailed element-level metadata including coordinates, confidence scores, and layout information. It's recommended for enterprise document workflows, processing of mixed file types, and cases that require precise control over document processing parameters.
  

> **💡 Tip:**
>   Explore more tools in the [Dify Marketplace](https://marketplace.dify.ai).

***

##### Chunker

Similar to human limited attention span, large language models cannot process huge amount of information simultaneously. Therefore, after information extraction, the chunker splits large document content into smaller and manageable segments (called "chunks").

Different documents require different chunking strategies. A product manual works best when split by product features, while research papers should be divided by logical sections. Dify offers 3 types of chunkers for various document types and use cases.

###### Overview of Different Chunkers

| Chunker Type         | Highlights                                            | Best for                                              |
| -------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| General Chunker      | Fixed-size chunks with customizable delimiters        | Simple documents with basic structure                 |
| Parent-child Chunker | Dual-layer structure: precise matching + rich context | Complex documents requiring rich context preservation |
| Q\&A Processor       | Processes question-answer pairs from spreadsheets     | Structured Q\&A data from CSV/Excel files             |

###### Common Text Pre-processing Rules

All chunkers support these text cleaning options:

| Preprocessing Option                          | Description                                                                        |
| --------------------------------------------- | ---------------------------------------------------------------------------------- |
| Replace consecutive spaces, newlines and tabs | Clean up formatting by replacing multiple whitespace characters with single spaces |
| Remove all URLs and email addresses           | Automatically detect and remove web links and email addresses from text            |

###### General Chunker

Basic document chunking processing, suitable for documents with relatively simple structures. You can configure text chunking and text preprocessing rules according to the following configuration.

**Input and Output Variable**

| Type            | Variable           | Description                                                                 |
| --------------- | ------------------ | --------------------------------------------------------------------------- |
| Input Variable  | `{x} Content`      | Complete document content that the chunker will split into smaller segments |
| Output Variable | `{x} Array[Chunk]` | Array of chunked content, each segment optimized for retrieval and analysis |

**Chunk Settings**

| Configuration Item   | Description                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Delimiter            | Default value is `\n` (line breaks for paragraph segmentation). You can customize chunking rules following regex. The system will automatically execute segmentation when the delimiter appears in text. |
| Maximum Chunk Length | Specifies the maximum character limit within a segment. When this length is exceeded, forced segmentation will occur.                                                                                    |
| Chunk Overlap        | When segmenting data, there is some overlap between segments. This overlap helps improve information retention and analysis accuracy, enhancing recall effectiveness.                                    |

###### Parent-child Chunker

By using a dual-layer segmentation structure to resolve the contradiction between context and accuracy, parent-child clunker achieves the balance between precise matching and comprehensive contextual information in Retrieval Augmented Generation (RAG) systems.

**How Parent-child Chunker Works**

Child Chunks for query matching: Small, precise information segments (usually single sentences) to match user queries with high accuracy.

Parent Chunks provide rich context: Larger content blocks (paragraphs, sections, or entire documents) that contain the matching child chunks, giving the large language model (LLM) comprehensive background information.

| Type            | Variable                 | Description                                                                 |
| --------------- | ------------------------ | --------------------------------------------------------------------------- |
| Input Variable  | `{x} Content`            | Complete document content that the chunker will split into smaller segments |
| Output Variable | `{x} Array[ParentChunk]` | Array of parent chunks                                                      |

**Chunk Settings**

| Configuration Item          | Description                                                                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Parent Delimiter            | Set delimiter for parent chunk splitting                                                                                            |
| Parent Maximum Chunk Length | Set maximum character count for parent chunks                                                                                       |
| Child Delimiter             | Set delimiter for child chunk splitting                                                                                             |
| Child Maximum Chunk Length  | Set maximum character count for child chunks                                                                                        |
| Parent Mode                 | Choose between Paragraph (split text into paragraphs) or "Full Document" (use entire document as parent chunk) for direct retrieval |

###### Q\&A Processor

Combining extraction and chunking in one node, Q\&A Processor is specifically designed for structured Q\&A datasets from CSV and Excel files. Perfect for FAQ lists, shift schedules, and any spreadsheet data with clear question-answer pairs.

**Input and Output Variable**

| Type            | Variable             | Description   |
| --------------- | -------------------- | ------------- |
| Input Variable  | `{x} Document`       | A single file |
| Output Variable | `{x} Array[QAChunk]` | QA chunk      |

**Variable Configuration**

| Configuration Item         | Description                    |
| -------------------------- | ------------------------------ |
| Column Number for Question | Set content column as question |
| Column Number for Answer   | Set column answer as answer    |

***

#### Step 3: Configure Knowledge Base Node

Now that your documents are processed and chunked, it's time to set up how they'll be stored and retrieved. Here, you can select different indexing methods and retrieval strategies based on your specific needs.

Knowledge base node configuration includes: Input Variable, Chunk Structure, Index Method, and Retrieval Settings.

##### Chunk Structure

  *[Image: Chunk Structure]*

Chunk structure determines how the knowledge base organizes and indexes your document content. Choose the structure mode that best fits your document type, use case, and cost.

The knowledge base supports three chunk modes: **General Mode, Parent-child Mode, and Q\&A Mode**. If you're creating a knowledge base for the first time, we recommend choosing Parent-child Mode.

> **⚠️ Warning:**
>   **Important Reminder**: Chunk structure cannot be modified once saved and published. Please choose carefully.

###### General Mode

Suitable for most standard document processing scenarios. It provides flexible indexing options—you can choose appropriate indexing methods based on different quality and cost requirements.

General mode supports both high-quality and economical indexing methods, as well as various retrieval settings.

###### Parent-child Mode

It provides precise matching and corresponding contextual information during retrieval, suitable for professional documents that need to maintain complete context.

Parent-child mode supports HQ (High Quality) mode only, offering child chunks for query matching and parent chunks for contextual information during retrieval.

###### Q\&A Mode

Create documents that pair questions with answers when using structured question-answer data. These documents are indexed based on the question portion, enabling the system to retrieve relevant answers based on query similarity.

Q\&A Mode supports HQ (High Quality) mode only.

##### Input Variable

Input variables receive processing results from data processing nodes as the data source for knowledge base. You need to connect the output from chunker to the knowledge base as input.

The node supports different types of standard inputs based on the selected chunk structure:

* **General Mode**: x Array[Chunk] - General chunk array
* **Parent-child Mode**: x Array[ParentChunk] - Parent chunk array
* **Q\&A Mode**: x Array[QAChunk] - Q\&A chunk array

##### Index Method & Retrieval Settings

The index method determines how your knowledge base builds content indexes, while retrieval settings provide corresponding retrieval strategies based on the selected index method.

Think of it in this way: the index method determines how to organize your documents, while retrieval settings tell users what methods they can use to find documents.

The knowledge base provides two index methods: **High Quality** and **Economical**, each offering different retrieval setting options.

The High Quality method uses embedding models to convert chunks into numerical vectors, helping to compress and store large amounts of information more effectively. This enables the system to find semantically relevant accurate answers even when the user's question wording doesn't exactly match the document.

> **💡 Tip:**
>   To enable cross-modal retrieval—retrieving both text and images based on semantic relevance—select a multimodal embedding model (marked with a **Vision** icon). Images extracted from documents will then be embedded and indexed for retrieval.
>
>   Knowledge bases using such embedding models are labeled **Multimodal** on their cards.
>
>
>     *[Image: Multimodal Knowledge Base]*
>

In the Economical method, each block uses 10 keywords for retrieval without calling embedding models, generating no costs.

> **ℹ️ Info:**
>   For more details, see [Specify the Index Method and Retrieval Settings](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/setting-indexing-methods).

| Index Method | Available Retrieval Settings | Description                                                             |
| ------------ | ---------------------------- | ----------------------------------------------------------------------- |
| High Quality | Vector Retrieval             | Understand deeper meaning of queries based on semantic similarity       |
|              | Full-text Retrieval          | Keyword-based retrieval providing comprehensive search capabilities     |
|              | Hybrid Retrieval             | Combine both semantic and keywords                                      |
| Economical   | Inverted Index               | Common search engine retrieval method, matches queries with key content |

> **📝 Note:**
>   If the selected embedding model is multimodal, select a multimodal rerank model (marked with a **Vision** icon) as well. Otherwise, retrieved images will be excluded from reranking and the retrieval results.

You can also refer to the table below for information on configuring chunk structure, index methods, parameters, and retrieval settings.

| Chunk Structure   | Index Methods                                | Parameters                                              | Retrieval Settings                                                                        |
| ----------------- | -------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| General mode      | High Quality 
 
 
 Economical | Embedding Model 
 
 
 Number of Keywords | Vector Retrieval 
 Full-text Retrieval 
 Hybrid Retrieval 
 Inverted Index |
| Parent-child Mode | High Quality Only                            | Embedding Model                                         | Vector Retrieval 
 Full-text Retrieval 
 Hybrid Retrieval                       |
| Q\&A Mode         | High Quality Only                            | Embedding Model                                         | Vector Retrieval 
 Full-text Retrieval 
 Hybrid Retrieval                       |

***

#### Step 4: Create User Input Form

User input forms are essential for collecting the initial information your pipeline needs to run effectively. Similar to [the User Input node](https://docs.dify.ai/en/cloud/use-dify/nodes/user-input) in workflow, this form gathers necessary details from users - such as files to upload, specific parameters for document processing - ensuring your pipeline has all the information it needs to deliver accurate results.

This way, you can create specialized input forms for different use scenarios, improving pipeline flexibility and usability for various data sources or document processing steps.

##### Create User Input Form

There're two ways to create user input field:

1. **Pipeline Orchestration Interface**\
   Click on the **Input field** to start creating and configuring input forms.\\

     *[Image: ]*

2. **Node Parameter Panel**\
   Select a node. Then, in parameter input on the right-side panel, click + Create user input for new input items. New input items will also be collected in the Input Field. ![Node Parameter Panel]\(/images/use-dify/knowledge/knowledge-pipeline-orchestration-10.png)

##### Add User Input Fields

###### Unique Inputs for Each Entrance

  *[Image: Knowledge Pipeline Orchestration 11]*

These inputs are specific to each data source and its downstream nodes. Users only need to fill out these fields when selecting the corresponding data source, such as different URLs for different data sources.

**How to create**: Click the `+` button on the right side of a data source to add fields for that specific data source. These fields can only be referenced by that data source and its subsequently connected nodes. *[Image: These Inputs Are Specific to Each Data Source and Its Downstream Nodes]*

###### Global Inputs for All Entrances

  *[Image: Knowledge Pipeline Orchestration 13]*

Global shared inputs can be referenced by all nodes. These inputs are suitable for universal processing parameters, such as delimiters, maximum chunk length, document processing configurations, etc. Users need to fill out these fields regardless of which data source they choose.

**How to create**: Click the `+` button on the right side of Global Inputs to add fields that can be referenced by any node.

##### Supported Input Field Types

The knowledge pipeline supports seven types of input variables:

  

      *[Image: Knowledge Pipeline Orchestration 14]*

  

  
    | Field Type | Description                                                                                         |
    | ---------- | --------------------------------------------------------------------------------------------------- |
    | Text       | Short text input by knowledge base users, maximum length 256 characters                             |
    | Paragraph  | Long text input for longer character strings                                                        |
    | Select     | Fixed options preset by the orchestrator for users to choose from, users cannot add custom content  |
    | Boolean    | Only true/false values                                                                              |
    | Number     | Only accepts numerical input                                                                        |
    | Single     | Upload a single file, supports multiple file types (documents, images, audio, and other file types) |
    | File List  | Batch file upload, supports multiple file types (documents, images, audio, and other file types)    |
  

> **💡 Tip:**
>   For more information about supported field types, see [User Input](https://docs.dify.ai/en/cloud/use-dify/nodes/user-input).

##### Field Configuration Options

All input field types include: required, optional, and additional settings. You can set whether fields are required by checking the appropriate option.

| Setting                   | Name          | Description                                                             | Example                                                  |
| ------------------------- | ------------- | ----------------------------------------------------------------------- | -------------------------------------------------------- |
| Required Settings         | Variable Name | Internal system identifier, usually named using English and underscores | `user_email`                                             |
|                           | Display Name  | Interface display name, usually concise and readable text               | User Email                                               |
| Type-specific Settings    |               | Special requirements for different field types                          | Text field max length 100 characters                     |
| Additional Settings       | Default Value | Default value when user hasn't provided input                           | Number field defaults to 0, text field defaults to empty |
|                           | Placeholder   | Hint text displayed when input box is empty                             | "Please enter your email"                                |
|                           | Tooltip       | Explanatory text to guide user input, usually displayed on mouse hover  | "Please enter a valid email address"                     |
| Special Optional Settings |               | Additional setting options based on different field types               | Validation of email format                               |

After completing configuration, click the preview button in the upper right corner to browse the form preview interface. You can drag and adjust field groupings. If an exclamation mark appears, it indicates that the reference is invalid after moving.

  *[Image: Knowledge Pipeline Orchestration 15]*

***

#### Step 5: Name the Knowledge Base

  *[Image: Name Knowledge Base]*

By default, the knowledge base name will be "Untitled + number", permissions are set to "Only me", and the icon will be an orange book. If you import it from a DSL file, it will use the saved icon.

Edit knowledge base information by clicking **Settings** in the left panel and fill in the information below:

* **Name & Icon**\
  Pick a name for your knowledge base.\
  Choose an emoji, upload an image, or paste an image URL as the icon of this knowledge base.
* **Knowledge Description**\
  Provide a brief description of your knowledge base. This helps the AI better understand and retrieve your data. If left empty, Dify will apply the default retrieval strategy.
* **Permissions**\
  Select the appropriate access permissions from the dropdown menu.

***

#### Step 6: Testing

You're almost there! This is the final step of the knowledge pipeline orchestration.

After completing the orchestration, you need to validate all the configuration first. Then, do some running tests and confirm all the settings. Finally, publish the knowledge pipeline.

##### Configuration Completeness Check

Before testing, it's recommended to check the completeness of your configuration to avoid test failures due to missing configurations.

Click the checklist button in the upper right corner, and the system will display any missing parts.

  *[Image: Knowledge Pipeline Orchestration 16]*

After completing all configurations, you can preview the knowledge base pipeline's operation through test runs, confirm that all settings are accurate, and then proceed with publishing.

##### Test Run

  *[Image: Knowledge Pipeline Orchestration 17]*

1. **Start Test**: Click the "Test Run" button in the upper right corner
2. **Import Test File**: Import files in the data source window that pops up on the right

> **⚠️ Warning:**
>   **Important Note**: For better debugging and observation, only one file upload is allowed per test run.

3. **Fill Parameters**: After successful import, fill in corresponding parameters according to the user input form you configured earlier
4. **Start Test Run**: Click next step to start testing the entire pipeline

During testing, you can access [History Logs](https://docs.dify.ai/en/cloud/use-dify/monitor/logs) (track all run records with timestamps, execution status, and input/output summaries) and [Variable Inspector](https://docs.dify.ai/en/cloud/use-dify/debug/variable-inspect) (a dashboard at the bottom showing input/output data for each node to help identify issues and verify data flow) for efficient troubleshooting and error fixing.

  *[Image: Testing Tools]*

#### Step 5: Manage and Use Knowledge Base

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/manage-knowledge-base

After creating your knowledge base, continuous management and optimization will provide accurate contextual information for your applications. These are the  options for follow-up maintenance.

##### Knowledge Pipeline

View and modify your orchestrated pipeline nodes and configurations.

> **💡 Tip:**
>   Find more information in [Manage Knowledge](https://docs.dify.ai/en/cloud/use-dify/knowledge/manage-knowledge/maintain-knowledge-documents).

  *[Image: Knowledge Management]*

#### Step 3: Publish Knowledge Pipeline

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/publish-knowledge-pipeline

After completing pipeline orchestration and debugging, click **Publish** and **Confirm** in the pop-up window.

  

      *[Image: Publish Confirmation]*

  

  

      *[Image: Publish Success]*

  

> **⚠️ Warning:**
>   Important reminder: Once published, the chunk structure cannot be modified.

  

      *[Image: Publish Complete]*

  

  
    Once it is published, you can:

    **Add Documents (Go to add documents)**\
    Click this option to jump to the knowledge base data source selection interface, where you can directly upload documents.

    **Access API (Access API Reference)**\
    Go to the API documentation page where you can get the knowledge base API calling methods and instructions.

    **Publish as a Knowledge Pipeline**\
    you can optionally use **Publish as a Knowledge Pipeline** to save it as a reusable template that will appear in the Customized section for future use.
  

> **ℹ️ Info:**
>   **Publish as a Knowledge Pipeline** is available on **[Professional]** and **[Team]**. Sandbox accounts cannot publish pipelines as reusable templates. [Upgrade your plan](https://dify.ai/pricing) to unlock this feature.

#### Build a Custom Knowledge Base

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/readme

To build a custom knowledge base, you design a knowledge pipeline. A knowledge pipeline is a document processing workflow that transforms raw data into searchable knowledge bases. As with orchestrating a workflow, you can visually combine and configure different processing nodes and tools to optimize data processing for better accuracy and relevance.

Every knowledge pipeline normally follows a structured flow through four key steps:

**Data Sources → Data Extraction → Data Processing → Knowledge Storage**

Each step serves a specific purpose: gathering content from various sources, converting it to processable text, refining it for search, and storing it in a format that enables fast, accurate retrieval.

Dify provides built-in pipeline templates that is optimized for certain use cases, or you can also create knowledge pipelines from scratch. In this session, we will go through creating options, general process of building knowledge pipelines, and how to manage it.

  1. - **[Step 1: Create Knowledge Pipeline](https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/create-knowledge-pipeline)** — Start from built-in templates, blank knowledge pipeline or import existing pipeline.

  1. - **[Step 2: Orchestrate Knowledge Pipeline](https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/knowledge-pipeline-orchestration)** — Get to know how the knowledge pipeline works, orchestrate different nodes and make sure it’s ready to use.

  1. - **[Step 3: Publish Knowledge Pipeline](https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/publish-knowledge-pipeline)** — Let's make it ready for document processing.

  1. - **[Step 4: Upload Files](https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/upload-files)** — Add documents and process them into the searchable knowledge base.

  1. - **[Step 5: Manage and Use Knowledge Base](https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/manage-knowledge-base)** — Maintain documents, test retrieval, modify settings, and more.

#### Step 4: Upload Files

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/upload-files

After publishing knowledge pipeline, there're two ways to upload files as below:

A: Click **Go to Documents** in the success notification to add or manage documents. After entering Documents page, click **Add File** to upload.

  

      *[Image: Option A-1]*

  

  

      *[Image: Option A-2]*

  

B: Click **Go to Add Documents** to add documents.

  

      *[Image: Option B-1]*

  

  

      *[Image: Option B-2]*

  

##### Upload Process

1. **Select Data Source**\
   Choose from the data source types configured in your pipeline. Dify currently supports 4 types of data sources: File Upload (pdf, docx, etc.), Online Drive (Google Drive, OneDrive, etc.), Online Doc (Notion), and Web Crawler (Jina Reader, Firecrawl).
   Please visit [Dify Marketplace](https://marketplace.dify.ai/) to install additional data sources.

2. **Fill in Processing Parameters and Preview**\
   If you configured user input fields during pipeline orchestration, users will need to fill in the required parameters and variables at this step. After completing the form, click **Preview** to see chunking results. Click **Save & Process** to complete knowledge base creation and start data processing.

   > **⚠️ Warning:**
>      Important reminder: Chunk structure remains consistent with the pipeline configuration and won't change with user input parameters.
>

     *[Image: Parameter Input]*

3. **Process Documents**\
   Track the progress of document processing. After embedding is completed, click **Go to Document**.

     *[Image: Processing Progress]*

4. **Access Documents List**\
   Click **Go to Documents** to view the Documents page, where you can browse all uploaded file, processing status, etc.

     *[Image: Documents List]*

#### Knowledge Request Rate Limit

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-request-rate-limit

#### What is Knowledge Request Rate Limit?

The knowledge request rate limit refers to the maximum number of actions that a workspace can perform in the knowledge base within one minute. These actions include creating datasets, managing documents, and running queries in apps or workflows.

#### Limitations of Different Subscription Versions

Knowledge Request Rate Limit will vary by subscription level:

* **Sandbox**: 10/min
* **Professional**: 100/min
* **Team**: 1,000/min

For example, if a Sandbox user performs 10 hit tests within one minute, their workspace will be temporarily unable to perform the restricted actions during the following minute.

#### Which Actions will be Limited by Knowledge Request Rate Limit when I Perform them?

When you perform the following actions, you will be limited by the frequency of Knowledge Base requests:

1. Creating empty datasets
2. Deleting datasets
3. Updating dataset settings
4. Uploading documents
5. Deleting documents
6. Updating documents
7. Disabling documents
8. Enabling documents
9. Archiving documents
10. Restoring archived documents
11. Pausing document processing
12. Resuming document processing
13. Adding segments
14. Deleting segments
15. Updating segments
16. Bulk importing segments
17. Performing hit tests
18. Querying the knowledge in apps or workflows (*Note: Multi-path recalls count as a single request.*)

#### Manage Knowledge Settings

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/manage-knowledge/introduction

> **ℹ️ Info:**
>   Only the workspace owner, administrators, and editors can modify the knowledge base settings.

In a knowledge base, click the **Settings** icon in the left sidebar to enter its settings page.

| Settings           | Description                                                                                                                                                                                                                                                      |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name & Icon        | Identifies the knowledge base.                                                                                                                                                                                                                                   |
| Description        | Indicates the knowledge base's purpose and content.                                                                                                                                                                                                              |
| Permissions        | Defines which workspace members can access the knowledge base.> **📝 Note:**
> Members granted access to a knowledge base have all the permissions listed in [Manage Knowledge Content](https://docs.dify.ai/en/cloud/use-dify/knowledge/manage-knowledge/maintain-knowledge-documents).
 |
| Index Method       | Defines how document chunks are processed and organized for retrieval. For more details, see [Select the Index Method](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/setting-indexing-methods#select-the-index-method).                                          |
| Embedding Model    | Specifies the embedding model used to convert document chunks into vector representations.> **ℹ️ Info:**
> Changing the embedding model will re-embed all chunks.
                                                                                                    |
| Summary Auto-Gen   | Automatically generate summaries for document chunks.> **ℹ️ Info:**
> Once enabled, this only applies to newly added documents and chunks. For existing chunks, select the document(s) in the document list and click **Generate summary**.
                          |
| Retrieval Settings | Defines how the knowledge base retrieves relevant content. For more details, see [Configure the Retrieval Settings](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/setting-indexing-methods#configure-the-retrieval-settings).                                    |

#### Manage Knowledge Content

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/manage-knowledge/maintain-knowledge-documents

#### Manage Documents

In a knowledge base, each imported item—whether a local file, a Notion page, or a web page—becomes a document.

From the document list, you can view and manage all these documents to keep your knowledge accurate, relevant, and up-to-date.

> **💡 Tip:**
>   Click the knowledge base name at the top to quickly switch between knowledge bases.

  *[Image: Manage Knowledge Documents]*

| Action                | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Add                   | Import a new document.                                                                                                                                                                                                                                                                                                                                                                                              |
| Modify Chunk Settings | Modify a document's chunking settings (excluding the chunk structure).> **ℹ️ Info:**
> Each document can have its own chunking settings, while the chunk structure is shared across the knowledge base and cannot be changed once set.
                                                                                                                                                                                  |
| Delete                | Permanently remove a document. **Deletion cannot be undone**.                                                                                                                                                                                                                                                                                                                                                       |
| Enable / Disable      | Temporarily include or exclude a document from retrieval. > **📝 Note:**
> Documents that have not been updated or retrieved for a certain period are automatically disabled to optimize performance. The inactivity period varies by subscription plan:* Sandbox: 7 days
* Professional & Team: 30 days
 On Professional and Team plans, disabled documents can be re-enabled **with one click**.
 |
| Archive / Unarchive   | Archive a document that you no longer need for retrieval but still want to keep. Archived documents are read-only and can be unarchived at any time.                                                                                                                                                                                                                                                                |
| Edit                  | Modify the content of a document by editing its chunks. See [Manage Chunks](#manage-chunks) for details.                                                                                                                                                                                                                                                                                                            |
| Rename                | Change the name of a document.                                                                                                                                                                                                                                                                                                                                                                                      |

#### Manage Chunks

According to its chunk settings, every document is split into content chunks—the basic units for retrieval.

From the chunk list within a document, you can view and manage all its chunks to improve the retrieval efficiency and accuracy.

> **💡 Tip:**
>   Click the document name in the upper-left corner to quickly switch between documents.

  *[Image: Manage Knowledge Chunks]*

| Action                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :----------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add                            | Add one or batch add multiple new chunks. 

For documents chunked with Parent-child mode, both new parent and child chunks can be added. > **ℹ️ Info:**
> Adding chunks is available on **[Professional]** and **[Team]**. [Learn more](https://dify.ai/pricing).
                                                                                                                                                                                                                                                                                                |
| Delete                         | Permanently remove a chunk. **Deletion cannot be undone**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Enable / Disable               | Temporarily include or exclude a chunk from retrieval. Disabled chunks cannot be edited.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Edit                           | Modify the content of a chunk. Edited chunks are marked **Edited**.

For knowledge bases using the Parent-child chunk mode: * When editing a parent chunk, you can choose to regenerate its child chunks or keep them unchanged.
* Editing a child chunk does not update its parent chunk.
                                                                                                                                                                                                                                                              |
| Add / Edit / Delete Keywords   | Add or modify keywords (up to 10) for a chunk to improve its retrievability. Only available for knowledge bases using the Economical index method.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Add / Delete Image Attachments | Remove images extracted from documents or upload new ones within their corresponding chunk.

URLs of extracted images remain in the chunk text, but you can safely remove these URLs to keep the text clean—this won't affect the extracted images. > **📝 Note:**
> Each chunk can have up to 10 image attachments, which are returned alongside it during retrieval. Images beyond this limit will not be extracted.
> **💡 Tip:**
> If you select a multimodal embedding model (marked with a **Vision** icon), the extracted images will also be embedded and indexed for retrieval.
 |
| Add / Edit / Delete Summary    | Add, modify, or remove a summary for a chunk.

Summaries are embedded and indexed for retrieval as well. When a summary matches a query, its corresponding chunk is also returned.> **💡 Tip:**
> Add identical summaries to multiple chunks to enable grouped retrieval, allowing related chunks to be returned together (subject to the Top K limit).
                                                                                                                                                                                                                             |

#### Best Practices

##### Check Chunk Quality

After a document is chunked, carefully review each chunk to ensure it's semantically complete and appropriately sized for optimal retrieval accuracy and response relevance.

Common issues to watch for:

* Chunks are **too short**—may lack sufficient context, leading to semantic loss and inaccurate answers.

* Chunks are **too long**—may include irrelevant information, introducing semantic noise and lowering retrieval precision.

* Chunks are **semantically incomplete**—caused by forced chunking that cuts through sentences or paragraphs, resulting in missing or misleading content during retrieval.

##### Use Child Chunks as Retrieval Hooks for Parent Chunks

For documents chunked with Parent-child mode, the system searches across child chunks but returns the parent chunks. Since editing a child chunk does not update its parent, you can treat child chunks as semantic tags or retrieval hints for their parent chunks.

To do this, rewrite child chunks into **keywords**, **summaries**, or **common user queries**. For example, if a parent chunk covers technical "LED Status Indicators", you could rephrase its child chunks as:

* *blinking light, won't turn on, red light, connection error, frozen* (keywords)

* *Guide to interpreting LED colors and troubleshooting hardware power or pairing issues* (summaries)

* *What does a solid red light mean?* (queries)

##### Use Summaries to Bridge Query-Content Gaps

While high-quality indexing enables semantic search, raw chunks can still be hard to retrieve when they are too specific, noisy, or structurally complex to align well with user queries.

Summaries bridge this gap by providing a condensed semantic layer that makes the chunk's core intent explicit.

Use summaries when:

* **User queries differ from document language**: For technical documentation written formally, add summaries in the way users actually ask questions.

* **Concepts are implicit or buried in details**: Add high-level summaries that surface the core concepts and intent, so the chunk can be matched without relying on small details scattered across the text.

* **Raw text is non-textual**: When a chunk is primarily code, tables, logs, transcripts, or otherwise hard to match semantically, add descriptive summaries that clearly label what the chunk contains.

* **Related chunks should be retrieved together**: Apply identical summaries to a series of related chunks to enable grouped retrieval. This semantic glue allows multiple parts of a topic to be retrieved together, providing richer context.

  > **ℹ️ Info:**
>     The number of returned related chunks is subject to the Top K limit defined in the retrieval settings.
>

#### Manage Document Metadata

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/metadata

#### What is Metadata?

##### Overview

Metadata is information that describes your data - essentially "data about data". Just as a book has a table of contents to help you understand its structure, metadata provides context about your data's content, origin, purpose, etc., making it easier for you to find and manage information in your knowledge base.

This guide aims to help you understand metadata and effectively manage your knowledge base.

##### Core Concepts

* **Field**: The label of a metadata field (e.g., "author", "language").

* **Value**: The information stored in a metadata field (e.g., "Jack", "English").

  ![field_name_and_value](https://assets-docs.dify.ai/2025/03/b6a197aa21ab92db93869fcbfa156b62.png)

* **Value Count**: The number of values contained in a metadata field, including duplicates. (e.g., "3").

  ![metadata_field](https://assets-docs.dify.ai/2025/03/330f26e90438cf50167c4cb6ce30e458.png)

* **Value Type**: The type of value a field can contain.
  * Dify supports three value types:
    * String: For text-based information
    * Number: For numerical data
    * Time: For dates/timestamps

  ![value_type](https://assets-docs.dify.ai/2025/03/f6adc7418869334805361535c8cd6874.png)

#### How to Manage My Metadata?

##### Manage Metadata Fields in the Knowledge Base

You can create, modify, and delete metadata fields in the knowledge base.

> Any changes you make to metadata fields here affect your knowledge base globally.

###### Get Started with the Metadata Panel

**Access the Metadata Panel**

To access the Metadata Panel, go to **Knowledge Base** page and click **Metadata**.

  ![Metadata_Entrance](https://assets-docs.dify.ai/2025/03/bd43305d49cc1511683b4a098c8f6e5a.png)

  ![Metadata_Panel](https://assets-docs.dify.ai/2025/03/6000c85b5d2e29a2a5af5e0a047a7a59.png)

**Built-in vs Custom Metadata**

|  | Built-in Metadata | Custom Metadata |
| --- | --- | --- |
| Location | Lower section of the Metadata panel | Upper section of the Metadata panel |
| Activation | Disabled by default; requires manual activation | Add as needed |
| Generation | System automatically extracts and generates field values | User-defined and manually added |
| Editing | Fields and values cannot be modified once generated | Fields and values can be edited or deleted |
| Scope | Applies to all existing and new documents when enabled | Stored in metadata list; requires manual assignment to documents |
| Fields | System-defined fields include: document_name (string) uploader (string) upload_date (time) last_update_date (time) source (string) | No default fields; all fields must be manually created |
| Value Types | String: For text values Number: For numerical values Time: For dates and timestamps | String: For text values Number: For numerical values Time: For dates and timestamps |

###### Create New Metadata Fields

To create a new metadata field:

1. Click **+Add Metadata** to open the **New Metadata** dialog.

  ![New_Metadata](https://assets-docs.dify.ai/2025/03/5086db42c40be64e54926b645c38c9a0.png)

2. Choose the value type.

3. Name the field.

> Naming rules: Use lowercase letters, numbers, and underscores only.

  ![value_type](https://assets-docs.dify.ai/2025/03/f6adc7418869334805361535c8cd6874.png)

4. Click **Save** to apply changes.

  ![Save_Field](https://assets-docs.dify.ai/2025/03/f44114cc58d4ba11ba60adb2d04c9b4c.png)

###### Edit Metadata Fields

To edit a metadata field:

1. Click the edit icon next to a field to open the **Rename** dialog.

  ![Rename_Field](https://assets-docs.dify.ai/2025/03/94327185cbe366bf99221abf2f5ef55a.png)

2. Enter the new name in the **Name** field.

> Note: You can only modify the field name, not the value type.

  ![rename_field_2](https://assets-docs.dify.ai/2025/03/2f814f725df9aeb1a0048e51d736d969.png)

3. Click **Save** to apply changes.

> Note: Field changes update across all related documents in your knowledge base.

  ![Same_Renamed_Field](https://assets-docs.dify.ai/2025/03/022e42c170b40c35622b9b156c8cc159.png)

###### Delete Metadata Fields

To delete a metadata field, click the delete icon next to a field to delete it.

> Note: Deleting a field deletes it and all its values from all documents in your knowledge base.

  ![Delete_Field](https://assets-docs.dify.ai/2025/03/022e42c170b40c35622b9b156c8cc159.png)

##### Edit Metadata

###### Bulk Edit Metadata in the Metadata Editor

You can edit metadata in bulk in the knowledge base.

**Access the Metadata Editor**

To access the Metadata Editor:

1. In the knowledge base, select documents using the checkboxes on the left.

  ![Edit_Metadata_Entrance](https://assets-docs.dify.ai/2025/03/18b0c435604db6173acba41662474446.png)

2. Click **Metadata** in the bottom action bar to open the Metadata Editor.

  ![Edit_Metadata](https://assets-docs.dify.ai/2025/03/719f3c31498f23747fed7d7349fd64ba.png)

**Bulk Add Metadata**

To add metadata in bulk:

1. Click **+Add Metadata** in the editor to:

  ![add_metadata](https://assets-docs.dify.ai/2025/03/d4e4f87447c3e445d5b7507df1126c7b.png)

* Add existing fields from the dropdown or from the search box.

  ![existing_field](https://assets-docs.dify.ai/2025/03/ea9aab2c4071bf2ec75409b05725ac1f.png)

* Create new fields via **+New Metadata**.

  > New fields are automatically added to the knowledge base.

  ![new_metadata_field](https://assets-docs.dify.ai/2025/03/e32211f56421f61b788943ba40c6959e.png)

* Access the Metadata Panel to manage metadata fields via **Manage**.

  ![manage_field](https://assets-docs.dify.ai/2025/03/82561edeb747b100c5295483c6238ffa.png)

2. *(Optional)* Enter values for new fields.

  ![value_for_field](https://assets-docs.dify.ai/2025/03/aabfe789f607a1db9062beb493213376.png)

> The date picker is for time-type fields.

  ![date_picker](https://assets-docs.dify.ai/2025/03/65df828e605ebfb4947fccce189520a3.png)

3. Click **Save** to apply changes.

**Bulk Update Metadata**

To update metadata in bulk:

1. In the editor:

* **Add Values**: Type directly in the field boxes.

* **Reset Values**: Click the blue dot that appears on hover.

  ![reset_values](https://assets-docs.dify.ai/2025/03/01c0cde5a6eafa48e1c6e5438fc2fa6b.png)

* **Delete Values**: Clear the field or delete the **Multiple Value** card.

  ![multiple_values](https://assets-docs.dify.ai/2025/03/5c4323095644d2658881b783246914f1.png)

* **Delete fields**: Click the delete icon (fields appear struck through and grayed out).

  > Note: This only deletes the field from this document, not from your knowledge base.

  ![delete_fields](https://assets-docs.dify.ai/2025/03/1b0318b898f951e307e3dc8cdc2f48d3.png)

2. Click **Save** to apply changes.

**Set Update Scope**

Use **Apply to All Documents** to control changes:

* **Unchecked (Default)**: Updates only documents that already have the field.

* **Checked**: Adds or updates fields across all selected documents.

  ![apply_all_changes](https://assets-docs.dify.ai/2025/03/4550c68960802c24271492b63a39ad05.png)

###### Edit Metadata on the Document Details Page

You can edit a single document's metadata on its details page.

**Access Metadata Edit Mode**

To edit a single document's metadata:

On the document details page, click **Start labeling** to begin editing.

  ![Details_Page](https://assets-docs.dify.ai/2025/03/066cb8eaa89f6ec17aacd8b09f06771c.png)

  ![Start_Labeling](https://assets-docs.dify.ai/2025/03/4806c56e324589e1711c407f6a1443de.png)

**Add Metadata**

To add a single document's metadata fields and values:

1. Click **+Add Metadata** to:

  ![Add_Metadata](https://assets-docs.dify.ai/2025/03/f9ba9b10bbcf6eaca787eed4fcde44da.png)

* Create new fields via **+New Metadata**.

> New fields are automatically added to the knowledge base.

  ![New_Fields](https://assets-docs.dify.ai/2025/03/739e7e51436259fca45d16065509fabb.png)

* Add existing fields from the dropdown or from the search box.

  ![Existing_Fields](https://assets-docs.dify.ai/2025/03/5b1876e8bc2c880b3b774c97eba371ab.png)

* Access the Metadata Panel via **Manage**.

  ![Manage_Metadata](https://assets-docs.dify.ai/2025/03/8dc74a1d2cdd87294e58dbc3d6dd161b.png)

2. *(Optional)* Enter values for new fields.

  ![Values_for_Fields](https://assets-docs.dify.ai/2025/03/488107cbea73fd4583e043234fe2fd2e.png)

3. Click **Save** to apply changes.

**Edit Metadata**

To update a single document's metadata fields and values:

1. Click **Edit** in the top right to begin editing.

  ![Edit_Mode](https://assets-docs.dify.ai/2025/03/bb33a0f9c6980300c0f979f8dc0d274d.png)

2. Edit metadata:

   * **Update Values**: Type directly in value fields or delete it.

   > Note: You can only modify the value, not the value name.

   * **Delete Fields**: Click the delete icon.

   > Note: This only deletes the field from this document, not from your knowledge base.

  ![Edit_Metadata](https://assets-docs.dify.ai/2025/03/4c0c4d83d3ad240568f316abfccc9c2c.png)

3. Click **Save** to apply changes.

#### How to Filter Documents with Metadata?

See **Metadata Filtering** in *[Integrate Knowledge Base within Application](https://docs.dify.ai/en/cloud/use-dify/knowledge/integrate-knowledge-within-application)*.

#### FAQ

* **What can I do with metadata?**

  * Find information faster with smart filtering.

  * Control access to sensitive content.

  * Organize data more effectively.

  * Automate workflows based on metadata rules.

* **Fields vs Values: What is the difference?**

|                                            | Definition                                                           | Characteristics                                                       | Examples                                                                                                |
| ------------------------------------------ | -------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Metadata Fields in the Metadata Panel      | System-defined attributes that describe document properties          | Global fields accessible across all documents in the knowledge base   | Author, Type, Date, etc.                                                                                |
| Metadata Value on a document's detail page | Custom metadata tagged according to individual document requirements | Unique metadata values assigned based on document content and context | The "Author" field in Document A is set to "Mary" value, while in Document B it is set to "John" value. |

* **How do different delete options work?**

| Action                                   | Steps                                                   | Impact                         | Outcome                                                              |
| ---------------------------------------- | ------------------------------------------------------- | ------------------------------ | -------------------------------------------------------------------- |
| Delete field in the Metadata Panel       | In the Metadata Panel, click delete icon next to field  | Global - affects all documents | Field and all values permanently deleted from the knowledge base     |
| Delete field in the Metadata Editor      | In the Metadata Editor, click delete icon next to field | Selected documents only        | Field deleted from selected documents; remains in the knowledge base |
| Delete field on the document detail page | In the Edit Mode, click delete icon next to field       | Current document only          | Field deleted from current document; remains in the knowledge base   |

#### Knowledge

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/readme

#### Introduction

Knowledge in Dify is a collection of your own data that can be integrated into your AI apps. It allows you to provide LLMs with domain-specific information as context, ensuring their responses are more accurate, relevant, and less prone to hallucinations.

This is made possible through Retrieval-Augmented Generation (RAG). It means that instead of relying solely on its pre-trained public data, the LLM uses your custom knowledge as an additional source of truth:

1. (Retrieval) When a user asks a question, the system first **retrieves the most relevant** information from the incorporated knowledge.

2. (Augmented) This retrieved information is then combined with the user's original query and sent to the LLM as **augmented context**.

3. (Generation) The LLM uses this context to generate a **more precise** answer.

Knowledge is stored and managed in knowledge bases. You can create multiple knowledge bases, each tailored to different domains, use cases, or data sources, and selectively integrate them into your application as needed.

#### Build with Knowledge

With Dify knowledge, you can build AI apps that are grounded in your own data and domain-specific expertise. Here are some common use cases:

* **Customer support chatbots**: Build smarter support bots that provide accurate answers from your up-to-date product documentation, FAQs, and troubleshooting guides.

* **Internal knowledge portals**: Build AI-powered search and Q\&A systems for employees to quickly access company policies and procedures.

* **Content generation tools**: Build intelligent writing tools that generate reports, articles, or emails based on specific background materials.

* **Research & analysis applications**: Build applications that assist in research by retrieving and summarizing information from specific knowledge repositories like academic papers, market reports, or legal documents.

#### Create Knowledge

* **[Create a ready-to-use knowledge base](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/introduction)**: Import data, define processing rules, and let Dify handle the rest. Fast and beginner-friendly.

* **[Build a custom knowledge base](https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/readme)**: Orchestrate more complex, flexible data processing workflows with custom steps and various integrations.

* **[Connect to an external knowledge base](https://docs.dify.ai/en/cloud/use-dify/knowledge/connect-external-knowledge-base)**: Sync directly from external knowledge bases via APIs to leverage existing data without migration.

#### Manage & Optimize Knowledge

* **[Manage content](https://docs.dify.ai/en/cloud/use-dify/knowledge/manage-knowledge/maintain-knowledge-documents)**: View, add, modify, or delete documents and chunks to keep your knowledge current, accurate, and retrieval-ready.

* **[Test and validate retrieval](https://docs.dify.ai/en/cloud/use-dify/knowledge/test-retrieval)**: Simulate user queries to test how well your knowledge base retrieves relevant information.

* **[Enhance retrieval with metadata](https://docs.dify.ai/en/cloud/use-dify/knowledge/metadata)**: Add metadata to documents to enable filter-based searches and further improve retrieval precision.

* **[Adjust knowledge base settings](https://docs.dify.ai/en/cloud/use-dify/knowledge/manage-knowledge/introduction)**: Modify the index method, embedding model, and retrieval strategy at any time.

#### Use Knowledge

**[Integrate into applications](https://docs.dify.ai/en/cloud/use-dify/knowledge/integrate-knowledge-within-application)**: Ground your AI app in your own knowledge.

***

**Read More**:

* [Dify v1.1.0: Filtering Knowledge Retrieval with Customized Metadata](https://dify.ai/blog/dify-v1-1-0-filtering-knowledge-retrieval-with-customized-metadata)

* [Dify v0.15.0: Introducing Parent-child Retrieval for Enhanced Knowledge](https://dify.ai/blog/introducing-parent-child-retrieval-for-enhanced-knowledge)

* [Introducing Hybrid Search and Rerank to Improve the Retrieval Accuracy of the RAG System](https://dify.ai/blog/hybrid-search-rerank-rag-improvement)

* [Dify.AI's New Dataset Feature Enhancements: Citations and Attributions](https://dify.ai/blog/difyai-new-dataset-features)

* [Text Embedding: Basic Concepts and Implementation Principles](https://dify.ai/blog/text-embedding-basic-concepts-and-implementation-principles)

* [Enhance Dify RAG with InfraNodus: Expand Your LLM's Context](https://dify.ai/blog/enhance-dify-rag-with-infranodus-expand-your-llm-s-context)

* [Dify.AI x Jina AI: Dify now Integrates Jina Embedding Model](https://dify.ai/blog/integrating-jina-embeddings-v2-dify-enhancing-rag-applications)

#### Test Knowledge Retrieval

**Source:** https://docs.dify.ai/en/cloud/use-dify/knowledge/test-retrieval

In a knowledge base, click the **Retrieval Testing** icon in the left sidebar to enter the testing page.

Here, you can simulate user queries to test how well the knowledge base retrieves relevant information and experiment with different retrieval settings for optimal performance.

> **📝 Note:**
>   Retrieval settings adjusted here are temporary and only apply to the current test session.

> **💡 Tip:**
>   For more about retrieval settings, see [Configure the Retrieval Settings](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/setting-indexing-methods#configure-the-retrieval-settings).

The **Records** section logs all retrieval events associated with this knowledge base, including:

* Queries tested directly on the **Retrieval Testing** page
* Retrieval requests made by any linked app—whether during test runs or in production

> **ℹ️ Info:**
>   Test retrievals and regular retrievals share the same API endpoint.

### Monitor

#### Dashboard

*Monitor performance, costs, and user engagement through Dify's built-in analytics dashboard*

**Source:** https://docs.dify.ai/en/cloud/use-dify/monitor/analysis

Monitor performance, costs, and user engagement through Dify's built-in analytics dashboard

The dashboard tracks four metrics over time to show how your application performs:

  *[Image: Monitoring Dashboard]*

**Total Messages**: Conversation volume\
**Active Users**: Users with meaningful interactions (more than one exchange)\
**Average User Interactions**: Engagement depth per session\
**Token Usage**: Resource consumption and costs

Use the time selector to view trends over different periods. Click **"Tracing app performance"** to connect external observability platforms like Langfuse or LangSmith for deeper analytics.

#### Annotation System

*Build a curated library of high-quality responses to improve consistency and bypass AI generation*

**Source:** https://docs.dify.ai/en/cloud/use-dify/monitor/annotation-reply

Build a curated library of high-quality responses to improve consistency and bypass AI generation

Annotations let you create a curated library of perfect responses for specific questions. When users ask similar questions, Dify returns your pre-written answers instead of generating new responses, ensuring consistency and eliminating AI hallucinations for critical topics.

#### When to Use Annotations

**Enterprise Standards**
Create definitive answers for policy questions, product information, or customer service scenarios where consistency is critical.

**Rapid Prototyping**
Quickly improve demo applications by curating high-quality responses without retraining models or complex prompt engineering.

**Quality Assurance**
Ensure certain sensitive or important questions always receive your approved responses rather than potentially variable AI-generated content.

#### How Annotations Work

When annotation reply is enabled:

1. User asks a question
2. System searches existing annotations for semantic matches
3. If a match above the similarity threshold is found, returns the curated response
4. If no match, proceeds with normal AI generation
5. Track which annotations get used and how often

This creates a "fast path" for known good answers while maintaining AI flexibility for new questions.

#### Set Up Annotations

**Enable in App Configuration**
Navigate to **Orchestrate → Add Features** and enable annotation reply. Configure the similarity threshold and embedding model for matching.

**Similarity Threshold**: Higher values require closer matches. Start with moderate settings and adjust based on hit rates.

**Embedding Model**: Used to vectorize questions for semantic matching. Changing the model regenerates all embeddings.

#### Create Annotations

**From Conversations**
In debug mode or logs, click on AI responses and edit them into the perfect answer. Save as an annotation for future use.

**Bulk Import**
Download the template, create Q\&A pairs in the specified format, and upload for batch annotation creation.

**Manual Entry**
Add annotations directly in **Annotations** with custom questions and responses.

#### Manage Annotation Quality

**Hit Tracking**
Monitor which annotations are matched, how often they're used, and the similarity scores of matches. This shows which annotations provide value.

**Continuous Refinement**
Review hit history to improve annotation coverage and accuracy. Questions that consistently miss your annotations indicate gaps in coverage.

**A/B Testing**
Compare user satisfaction rates before and after annotation implementation to measure impact.

#### Annotation Analytics

**Hit Rate Analysis**
Track which annotations are frequently matched and which are never used. Remove unused annotations and expand successful patterns.

**Question Patterns**
Identify common user question types that would benefit from annotation coverage.

**Match Quality**
Review similarity scores to ensure annotations are triggering for appropriate questions without false matches.

#### Integrate with Alibaba Cloud Monitor

*Send traces and metrics from Dify applications to Alibaba Cloud Monitor (ARMS) via OpenTelemetry*

**Source:** https://docs.dify.ai/en/cloud/use-dify/monitor/integrations/integrate-aliyun

Send traces and metrics from Dify applications to Alibaba Cloud Monitor (ARMS) via OpenTelemetry

#### What is Alibaba Cloud Monitor

Alibaba Cloud provides a fully managed, maintenance-free observability platform that enables one-click monitoring, tracing, and evaluation of Dify applications.

> **ℹ️ Info:**
>   Alibaba Cloud Monitor natively supports Python/Golang/Java applications through [LoongSuite](https://github.com/alibaba/loongsuite-python-agent) agents and open-source OpenTelemetry agents. In addition to one-click monitoring of Dify LLM applications, it also supports end-to-end observability of Dify components and their upstream and downstream dependencies through non-invasive agents.
>
>   For more details, please refer to the [Cloud Monitor documentation](https://www.alibabacloud.com/help/en/cms/cloudmonitor-1-0/product-overview/what-is-cloudmonitor?spm=a3c0i.63551.2277339270.1.76c7112eeKEvSr).

#### How to Configure Alibaba Cloud Monitor

##### 1. Get Alibaba Cloud Endpoint and License Key

1. Log in to the [ARMS console](https://account.alibabacloud.com/login/login.htm?spm=5176.12901015-2.0.0.68d74b84XRatpU), and click **Integration Center** in the left navigation bar.
2. In the **Server-side Applications** area, click the **OpenTelemetry** card.
3. In the **OpenTelemetry** panel that appears, select **gRPC** as the export protocol, and select the connection method and region according to your actual deployment.

  ![Get Alibaba Cloud Access Point](https://dify-public-resources.oss-cn-hangzhou.aliyuncs.com/dify-doc/get_endpoint.png)

4. Save the **Public Endpoint** and **Authentication Token (License Key)**.

> **📝 Note:**
>   The Endpoint does not include a port number, for example `http://tracing-cn-heyuan.arms.aliyun.com`.

##### 2. Configure Cloud Monitor in Dify

1. Log in to the Dify console and navigate to the application you want to monitor.
2. Open **Monitoring** in the left navigation bar.
3. Click **Tracing app performance**, then click **Configure** in the **Cloud Monitor** area.

  ![Configure Alibaba Cloud Monitor](https://dify-public-resources.oss-cn-hangzhou.aliyuncs.com/dify-doc/config_cms.png)

4. In the dialog that appears, enter the **License Key** and **Endpoint** obtained in step 1, and customize the **App Name** (the application name displayed in the ARMS console), then click **Save & Enable**.

#### View Monitoring Data in Alibaba Cloud Monitor

After configuration, debug or production data from applications in Dify can be monitored in Cloud Monitor.

##### Method 1: Jump to ARMS Console from Dify Application

In the Dify console, select an application with tracing enabled, go to **Tracing Configuration**, and click **View** in the **Cloud Monitor** area.

##### Method 2: View Directly in ARMS Console

Go to the corresponding Dify application in the **LLM Application Monitoring > Application List** page of the ARMS console.

#### Access More Data

Cloud Monitor provides multi-language non-invasive agents that support accessing various components of the Dify cluster to achieve end-to-end tracing.

| Dify Component | Agent                   | Details                                                                                                                                                                                                                                                           |
| -------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nginx          | OpenTelemetry Agent     | [Use OpenTelemetry for Nginx Tracing](https://www.alibabacloud.com/help/en/opentelemetry/user-guide/use-opentelemetry-to-perform-tracing-analysis-on-nginx?spm=a2c63.l28256.help-menu-search-90275.d_1)                                                           |
| API            | LoongSuite-Python Agent | [loongsuite-python-agent](https://github.com/alibaba/loongsuite-python-agent/blob/main/README.md)                                                                                                                                                                 |
| Sandbox        | LoongSuite-Go Agent     | [loongsuite-go-agent](https://github.com/alibaba/loongsuite-go-agent/blob/main/README.md)                                                                                                                                                                         |
| Worker         | OpenTelemetry Agent     | [Submit Python Application Data via OpenTelemetry](https://www.alibabacloud.com/help/en/opentelemetry/user-guide/use-managed-service-for-opentelemetry-to-submit-the-trace-data-of-python-applications?spm=a2c63.p38356.help-menu-90275.d_2_0_5_0.18ee53a4EGoGuS) |
| Plugin-Daemon  | LoongSuite-Go Agent     | [loongsuite-go-agent](https://github.com/alibaba/loongsuite-go-agent/blob/main/README.md)                                                                                                                                                                         |

#### Monitoring Data List

Cloud Monitor supports collecting data from Dify's Workflow/Chatflow/Chat/Agent applications, including execution details of workflows and workflow nodes, covering model calls, tool calls, knowledge retrieval, execution details of various process nodes, as well as metadata such as conversations and user information.

##### Workflow/Chatflow Trace Information

| Workflow | Alibaba Cloud Monitor Trace |
| --- | --- |
| workflow_id | Unique identifier of the Workflow |
| conversation_id | Conversation ID |
| workflow_run_id | ID of this run |
| tenant_id | Tenant ID |
| elapsed_time | Duration of this run |
| status | Run status |
| version | Workflow version |
| total_tokens | Total tokens used in this run |
| file_list | List of processed files |
| triggered_from | Source that triggered this run |
| workflow_run_inputs | Input data for this run |
| workflow_run_outputs | Output data for this run |
| error | Errors that occurred during this run |
| query | Query used during runtime |
| workflow_app_log_id | Workflow application log ID |
| message_id | Associated message ID |
| start_time | Run start time |
| end_time | Run end time |

**Workflow Trace Metadata**

* workflow_id - Unique identifier of the Workflow
* conversation_id - Conversation ID
* workflow_run_id - ID of this run
* tenant_id - Tenant ID
* elapsed_time - Duration of this run
* status - Run status
* version - Workflow version
* total_tokens - Total tokens used in this run
* file_list - List of processed files
* triggered_from - Trigger source

##### Message Trace Information

| Message | Alibaba Cloud Monitor Trace |
| --- | --- |
| message_id | Message ID |
| message_data | Message data |
| user_session_id | User's session_id |
| conversation_model | Conversation model |
| message_tokens | Number of tokens in the message |
| answer_tokens | Number of tokens in the answer |
| total_tokens | Total tokens in message and answer |
| error | Error information |
| inputs | Input data |
| outputs | Output data |
| file_list | List of processed files |
| start_time | Start time |
| end_time | End time |
| message_file_data | File data associated with the message |
| conversation_mode | Conversation mode |

**Message Trace Metadata**

* conversation_id - ID of the conversation to which the message belongs
* ls_provider - Model provider
* ls_model_name - Model ID
* status - Message status
* from_end_user_id - ID of the sending user
* from_account_id - ID of the sending account
* agent_based - Whether it is agent-based
* workflow_run_id - Workflow run ID
* from_source - Message source
* message_id - Message ID

##### Dataset Retrieval Trace Information

| Dataset Retrieval | Alibaba Cloud Monitor Trace |
| --- | --- |
| message_id | Message ID |
| inputs | Input content |
| documents | Document data |
| start_time | Start time |
| end_time | End time |
| message_data | Message data |

**Dataset Retrieval Trace Metadata**

* message_id - Message ID
* ls_provider - Model provider
* ls_model_name - Model ID
* status - Message status
* from_end_user_id - ID of the sending user
* from_account_id - ID of the sending account
* agent_based - Whether it is agent-based
* workflow_run_id - Workflow run ID
* from_source - Message source

##### Tool Trace Information

| Tool | Alibaba Cloud Monitor Trace |
| --- | --- |
| message_id | Message ID |
| tool_name | Tool name |
| start_time | Start time |
| end_time | End time |
| tool_inputs | Tool inputs |
| tool_outputs | Tool outputs |
| message_data | Message data |
| error | Error information (if any) |
| inputs | Input content of the message |
| outputs | Answer content of the message |
| tool_config | Tool configuration |
| time_cost | Time cost |
| tool_parameters | Tool parameters |
| file_url | URL of associated file |

**Tool Trace Metadata**

* message_id - Message ID
* tool_name - Tool name
* tool_inputs - Tool inputs
* tool_outputs - Tool outputs
* tool_config - Tool configuration
* time_cost - Time cost
* error - Error information
* tool_parameters - Tool parameters
* message_file_id - Message file ID
* created_by_role - Creator role
* created_user_id - Creator user ID

#### Integrate with Arize

**Source:** https://docs.dify.ai/en/cloud/use-dify/monitor/integrations/integrate-arize

##### What is Arize

Enterprise-grade LLM observability, online & offline evaluation, monitoring, and experimentation—powered by OpenTelemetry. Purpose-built for LLM & agent-driven applications.

> **ℹ️ Info:**
>   For more details, please refer to [Arize](https://arize.com).

##### How to Configure Arize

###### 1. Register/Login to [Arize](https://app.arize.com/auth/join)

###### 2. Get your Arize API Key

Retrieve your Arize API Key from the user menu at the top-right. Click on **API Key**, then on the API Key to copy it:

  ![Arize API Key](https://i.ibb.co/JwBmQxnf/dify-docs-arize-api-key.png)

###### 3. Integrate Arize with Dify

Configure Arize in the Dify application. Open the application you need to monitor, open **Monitoring** in the side menu, and select **Tracing app performance** on the page.

  ![Tracing App Performance](https://i.ibb.co/v6cL6rPs/dify-docs-arize-in-use.png)

After clicking configure, paste the **API Key**, **Space ID** and **project name** created in Arize into the configuration and save.

  ![Configure Arize](https://i.ibb.co/m5Xww8gL/dify-docs-arize-config.png)

Once successfully saved, you can view the monitoring status on the current page.

  ![Configure Arize](https://i.ibb.co/xtggVmb7/dify-docs-arize-in-service.png)

##### Monitoring Data List

###### **Workflow/Chatflow Trace Information**

**Used to track workflows and chatflows**

| Workflow | Arize Trace |
| --- | --- |
| workflow_app_log_id/workflow_run_id | id |
| user_session_id | - placed in metadata |
| name |  |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| Model token consumption | usage_metadata |
| metadata | metadata |
| error | error |
| [workflow] | tags |
| "conversation_id/none for workflow" | conversation_id in metadata |

**Workflow Trace Info**

* workflow_id - Unique identifier of the workflow
* conversation_id - Conversation ID
* workflow_run_id - ID of the current run
* tenant_id - Tenant ID
* elapsed_time - Time taken for the current run
* status - Run status
* version - Workflow version
* total_tokens - Total tokens used in the current run
* file_list - List of processed files
* triggered_from - Source that triggered the current run
* workflow_run_inputs - Input data for the current run
* workflow_run_outputs - Output data for the current run
* error - Errors encountered during the current run
* query - Query used during the run
* workflow_app_log_id - Workflow application log ID
* message_id - Associated message ID
* start_time - Start time of the run
* end_time - End time of the run
* workflow node executions - Information about workflow node executions
* Metadata
  * workflow_id - Unique identifier of the workflow
  * conversation_id - Conversation ID
  * workflow_run_id - ID of the current run
  * tenant_id - Tenant ID
  * elapsed_time - Time taken for the current run
  * status - Run status
  * version - Workflow version
  * total_tokens - Total tokens used in the current run
  * file_list - List of processed files
  * triggered_from - Source that triggered the current run

###### **Message Trace Information**

**Used to track LLM-related conversations**

| Chat | Arize LLM |
| --- | --- |
| message_id | id |
| user_session_id | - placed in metadata |
| "llm" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| Model token consumption | usage_metadata |
| metadata | metadata |
| ["message", conversation_mode] | tags |
| conversation_id | conversation_id in metadata |

**Message Trace Info**

* message_id - Message ID
* message_data - Message data
* user_session_id - User session ID
* conversation_model - Conversation mode
* message_tokens - Number of tokens in the message
* answer_tokens - Number of tokens in the answer
* total_tokens - Total number of tokens in the message and answer
* error - Error information
* inputs - Input data
* outputs - Output data
* file_list - List of processed files
* start_time - Start time
* end_time - End time
* message_file_data - File data associated with the message
* conversation_mode - Conversation mode
* Metadata
  * conversation_id - Conversation ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * agent_based - Whether the message is agent-based
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Moderation Trace Information**

**Used to track conversation moderation**

| Moderation | Arize Tool |
| --- | --- |
| user_id | - placed in metadata |
| “moderation" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["moderation"] | tags |

**Moderation Trace Info**

* message_id - Message ID
* user_id: User ID
* workflow_app_log_id - Workflow application log ID
* inputs - Moderation input data
* message_data - Message data
* flagged - Whether the content is flagged for attention
* action - Specific actions taken
* preset_response - Preset response
* start_time - Moderation start time
* end_time - Moderation end time
* Metadata
  * message_id - Message ID
  * action - Specific actions taken
  * preset_response - Preset response

###### **Suggested Question Trace Information**

**Used to track suggested questions**

| Suggested Question | Arize LLM |
| --- | --- |
| user_id | - placed in metadata |
| "suggested_question" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["suggested_question"] | tags |

**Message Trace Info**

* message_id - Message ID
* message_data - Message data
* inputs - Input content
* outputs - Output content
* start_time - Start time
* end_time - End time
* total_tokens - Number of tokens
* status - Message status
* error - Error information
* from_account_id - ID of the sending account
* agent_based - Whether the message is agent-based
* from_source - Message source
* model_provider - Model provider
* model_id - Model ID
* suggested_question - Suggested question
* level - Status level
* status_message - Status message
* Metadata
  * message_id - Message ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Dataset Retrieval Trace Information**

**Used to track knowledge base retrieval**

| Dataset Retrieval | Arize Retriever |
| --- | --- |
| user_id | - placed in metadata |
| "dataset_retrieval" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["dataset_retrieval"] | tags |
| message_id | parent_run_id |

**Dataset Retrieval Trace Info**

* message_id - Message ID
* inputs - Input content
* documents - Document data
* start_time - Start time
* end_time - End time
* message_data - Message data
* Metadata
  * message_id - Message ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * agent_based - Whether the message is agent-based
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Tool Trace Information**

**Used to track tool invocation**

| Tool | Arize Tool |
| --- | --- |
| user_id | - placed in metadata |
| tool_name | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["tool", tool_name] | tags |

###### **Tool Trace Info**

* message_id - Message ID
* tool_name - Tool name
* start_time - Start time
* end_time - End time
* tool_inputs - Tool inputs
* tool_outputs - Tool outputs
* message_data - Message data
* error - Error information, if any
* inputs - Inputs for the message
* outputs - Outputs of the message
* tool_config - Tool configuration
* time_cost - Time cost
* tool_parameters - Tool parameters
* file_url - URL of the associated file
* Metadata
  * message_id - Message ID
  * tool_name - Tool name
  * tool_inputs - Tool inputs
  * tool_outputs - Tool outputs
  * tool_config - Tool configuration
  * time_cost - Time cost
  * error - Error information, if any
  * tool_parameters - Tool parameters
  * message_file_id - Message file ID
  * created_by_role - Role of the creator
  * created_user_id - User ID of the creator

**Generate Name Trace Information**

**Used to track conversation title generation**

| Generate Name | Arize Tool |
| --- | --- |
| user_id | - placed in metadata |
| "generate_conversation_name" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["generate_name"] | tags |

**Generate Name Trace Info**

* conversation_id - Conversation ID
* inputs - Input data
* outputs - Generated conversation name
* start_time - Start time
* end_time - End time
* tenant_id - Tenant ID
* Metadata
  * conversation_id - Conversation ID
  * tenant_id - Tenant ID

#### Integrate with Langfuse

**Source:** https://docs.dify.ai/en/cloud/use-dify/monitor/integrations/integrate-langfuse

##### What is Langfuse

Langfuse is an open-source LLM engineering platform that helps teams collaborate on debugging, analyzing, and iterating their applications.

> **ℹ️ Info:**
>   Introduction to Langfuse: [https://langfuse.com/](https://langfuse.com/)

##### How to Configure Langfuse

1. Register and log in to Langfuse on the [official website](https://langfuse.com/)
2. Create a project in Langfuse. After logging in, click **New** on the homepage to create your own project. The **project** will be used to associate with **applications** in Dify for data monitoring.

  ![Create a Project in Langfuse](https://assets-docs.dify.ai/2025/04/34ca6a973c4a1230be659b313b99fd90.png)

Edit a name for the project.

  ![Create a Project in Langfuse](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/26cfbb94e312a100c39e217fdd0b4406.png)

3. Create project API credentials. In the left sidebar of the project, click **Settings** to open the settings.

  ![Create Project API Credentials](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/2ed72a6761f2977201c29e67e5bc634c.png)

In Settings, click **Create API Keys** to create project API credentials.

  ![Create Project API Credentials](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/3c3fbd5392d37fbccf1f9ef76c54f0bc.png)

Copy and save the **Secret Key**, **Public Key**, and **Host**.

  ![Get API Key Configuration](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/a2ff67951ce300082d875eae8458c8c7.png)

4. Configure Langfuse in Dify. Open the application you need to monitor, open **Monitoring** in the side menu, and select **Tracing app performance** on the page.

  ![Configure Langfuse](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/ebc84b328ad37c0f6dbca6101e1f90ab.png)

After clicking configure, paste the **Secret Key, Public Key, Host** created in Langfuse into the configuration and save.

  ![Configure Langfuse](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/5bfa409e7a073f133f21146535401512.png)

Once successfully saved, you can view the status on the current page. If it shows as started, it is being monitored.

  ![View Configuration Status](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/1aa086a1aead0e29948e7d6d5815d5d1.png)

##### View Monitoring Data in Langfuse

After configuration, debugging or production data of the application in Dify can be viewed in Langfuse.

  ![Configuration, Debugging or Production Data of the Application in Dify Can Be](https://assets-docs.dify.ai/2025/04/a2c02ccc559743b85b0f972aa513e47a.png)

  ![](https://assets-docs.dify.ai/2025/04/88f3adfb03f325d2ea800ba5685b9ec9.png)

##### List of monitoring data

###### Trace the information of Workflow and Chatflow

**Tracing Workflow and Chatflow**

| Workflow | LangFuse Trace |
| --- | --- |
| workflow_app_log_id/workflow_run_id | id |
| user_session_id | user_id |
| name |  |
| start_time | start_time |
| end_time | end_time |
| inputs | input |
| outputs | output |
| Model token consumption | usage |
| metadata | metadata |
| error | level |
| error | status_message |
| [workflow] | tags |
| ["message", conversation_mode] | session_id |
| conversion_id | parent_observation_id |

**Workflow Trace Info**

* workflow_id - Unique ID of Workflow
* conversation_id - Conversation ID
* workflow_run_id - Workflow ID of this runtime
* tenant_id - Tenant ID
* elapsed_time - Elapsed time at this runtime
* status - Runtime status
* version - Workflow version
* total_tokens - Total token used at this runtime
* file_list - List of files processed
* triggered_from - Source that triggered this runtime
* workflow_run_inputs - Input of this workflow
* workflow_run_outputs - Output of this workflow
* error - Error Message
* query - Queries used at runtime
* workflow_app_log_id - Workflow Application Log ID
* message_id - Relevant Message ID
* start_time - Start time of this runtime
* end_time - End time of this runtime
* workflow node executions - Workflow node runtime information
* Metadata
  * workflow_id - Unique ID of Workflow
  * conversation_id - Conversation ID
  * workflow_run_id - Workflow ID of this runtime
  * tenant_id - Tenant ID
  * elapsed_time - Elapsed time at this runtime
  * status - Operational state
  * version - Workflow version
  * total_tokens - Total token used at this runtime
  * file_list - List of files processed
  * triggered_from - Source that triggered this runtime

###### Message Trace Info

**For trace llm conversation**

| Message | LangFuse Generation/Trace |
| --- | --- |
| message_id | id |
| user_session_id | user_id |
| name |  |
| start_time | start_time |
| end_time | end_time |
| inputs | input |
| outputs | output |
| Model token consumption | usage |
| metadata | metadata |
| error | level |
| error | status_message |
| ["message", conversation_mode] | tags |
| conversation_id | session_id |
| conversion_id | parent_observation_id |

**Message Trace Info**

* message_id - Message ID
* message_data - Message data
* user_session_id - Session ID for user
* conversation_model - Conversation model
* message_tokens - Message tokens
* answer_tokens - Answer Tokens
* total_tokens - Total Tokens from Message and Answer
* error - Error Message
* inputs - Input data
* outputs - Output data
* file_list - List of files processed
* start_time - Start time
* end_time - End time
* message_file_data - Message of relevant file data
* conversation_mode - Conversation mode
* Metadata
  * conversation_id - Conversation ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - Sending user's ID
  * from_account_id - Sending account's ID
  * agent_based - Whether agent based
  * workflow_run_id - Workflow ID of this runtime
  * from_source - Message source
  * message_id - Message ID

###### Moderation Trace Information

**Used to track conversation moderation**

| Moderation | LangFuse Generation/Trace |
| --- | --- |
| user_id | user_id |
| moderation | name |
| start_time | start_time |
| end_time | end_time |
| inputs | input |
| outputs | output |
| metadata | metadata |
| [moderation] | tags |
| message_id | parent_observation_id |

**Message Trace Info**

* message_id - Message ID
* user_id - user ID
* workflow_app_log_id workflow_app_log_id
* inputs - Input data for review
* message_data - Message Data
* flagged - Whether it is flagged for attention
* action - Specific actions to implement
* preset_response - Preset response
* start_time - Start time of review
* end_time - End time of review
* Metadata
  * message_id - Message ID
  * action - Specific actions to implement
  * preset_response - Preset response

###### Suggested Question Trace Information

**Used to track suggested questions**

| Suggested Question | LangFuse Generation/Trace |
| --- | --- |
| user_id | user_id |
| suggested_question | name |
| start_time | start_time |
| end_time | end_time |
| inputs | input |
| outputs | output |
| metadata | metadata |
| [suggested_question] | tags |
| message_id | parent_observation_id |

**Message Trace Info**

* message_id - Message ID
* message_data - Message data
* inputs - Input data
* outputs - Output data
* start_time - Start time
* end_time - End time
* total_tokens - Total tokens
* status - Message Status
* error - Error Message
* from_account_id - Sending account ID
* agent_based - Whether agent based
* from_source - Message source
* model_provider - Model provider
* model_id - Model ID
* suggested_question - Suggested question
* level - Status level
* status_message - Message status
* Metadata
  * message_id - Message ID
  * ls_provider - Model Provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - Sending user's ID
  * from_account_id - Sending Account ID
  * workflow_run_id - Workflow ID of this runtime
  * from_source - Message source

###### Dataset Retrieval Trace Information

**Used to track knowledge base retrieval**

| Dataset Retrieval | LangFuse Generation/Trace |
| --- | --- |
| user_id | user_id |
| dataset_retrieval | name |
| start_time | start_time |
| end_time | end_time |
| inputs | input |
| outputs | output |
| metadata | metadata |
| [dataset_retrieval] | tags |
| message_id | parent_observation_id |

**Dataset Retrieval Trace Info**

* message_id - Message ID
* inputs - Input Message
* documents - Document data
* start_time - Start time
* end_time - End time
* message_data - Message data
* Metadata
  * message_id - Message ID
  * ls_provider - Model Provider
  * ls_model_name - Model ID
  * status - Model status
  * from_end_user_id - Sending user's ID
  * from_account_id - Sending account's ID
  * agent_based - Whether agent based
  * workflow_run_id - Workflow ID of this runtime
  * from_source - Message Source

###### Tool Trace Information

**Used to track tool invocation**

| Tool | LangFuse Generation/Trace |
| --- | --- |
| user_id | user_id |
| tool_name | name |
| start_time | start_time |
| end_time | end_time |
| inputs | input |
| outputs | output |
| metadata | metadata |
| ["tool", tool_name] | tags |
| message_id | parent_observation_id |

**Tool Trace Info**

* message_id - Message ID
* tool_name - Tool Name
* start_time - Start time
* end_time - End time
* tool_inputs - Tool inputs
* tool_outputs - Tool outputs
* message_data - Message data
* error - Error Message, if exist
* inputs - Input of Message
* outputs - Output of Message
* tool_config - Tool config
* time_cost - Time cost
* tool_parameters - Tool Parameters
* file_url - URL of relevant files
* Metadata
  * message_id - Message ID
  * tool_name - Tool Name
  * tool_inputs - Tool inputs
  * tool_outputs - Tool outputs
  * tool_config - Tool config
  * time_cost - Time. cost
  * error - Error Message
  * tool_parameters - Tool parameters
  * message_file_id - Message file ID
  * created_by_role - Created by role
  * created_user_id - Created user ID

###### Generate Name Trace

**Used to track conversation title generation**

| Generate Name | LangFuse Generation/Trace |
| --- | --- |
| user_id | user_id |
| generate_name | name |
| start_time | start_time |
| end_time | end_time |
| inputs | input |
| outputs | output |
| metadata | metadata |
| [generate_name] | tags |

**Generate Name Trace Info**

* conversation_id - Conversation ID
* inputs - Input data
* outputs - Generated session name
* start_time - Start time
* end_time - End time
* tenant_id - Tenant ID
* Metadata
  * conversation_id - Conversation ID
  * tenant_id - Tenant ID

##### Langfuse Prompt Management

The [Langfuse Prompt Management Plugin](https://github.com/gao-ai-com/dify-plugin-langfuse) (community maintained) lets you use prompts that are [managed and versioned in Langfuse](https://langfuse.com/docs/prompt-management/get-started) in your Dify applications, enhancing your LLM application development workflow. Key features include:

* **Get Prompt**: Fetch specific prompts managed in Langfuse.
* **Search Prompts**: Search for prompts in Langfuse using various filters.
* **Update Prompt**: Create new versions of prompts in Langfuse and set tags/labels.

This integration streamlines the process of managing and versioning your prompts, contributing to more efficient development and iteration cycles. You can find the plugin and installation instructions [here](https://github.com/gao-ai-com/dify-plugin-langfuse).

#### Integrate with LangSmith

**Source:** https://docs.dify.ai/en/cloud/use-dify/monitor/integrations/integrate-langsmith

##### What is LangSmith

LangSmith is a platform for building production-grade LLM applications. It is used for developing, collaborating, testing, deploying, and monitoring LLM applications.

> **ℹ️ Info:**
>   For more details, please refer to [LangSmith](https://www.langchain.com/langsmith).

##### How to Configure LangSmith

###### 1. Register/Login to [LangSmith](https://www.langchain.com/langsmith)

###### 2. Create a Project

Create a project in LangSmith. After logging in, click **New Project** on the homepage to create your own project. The **project** will be used to associate with **applications** in Dify for data monitoring.

  ![Create a Project in LangSmith](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/58e20105fcc0771ca2431e8e5dcc42d3.png)

Once created, you can view all created projects in the Projects section.

  ![View Created Projects in LangSmith](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/642c0ff7edfdfe77fba43aa22cc3fa71.png)

###### 3. Create Project Credentials

Find the project settings **Settings** in the left sidebar.

  ![Project Settings](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/c49a1fc769215193928ff0d880422f89.png)

Click **Create API Key** to create project credentials.

  ![Create a Project API Key](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/7082286b0d12af4bc0c84d9a3acf8b1b.png)

Select **Personal Access Token** for subsequent API authentication.

  ![Create an API Key](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/75a69bd4dd02f0ffc0313589ae12fb36.png)

Copy and save the created API key.

  ![Copy API Key](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/723e96a13e8f722d6df714b11ffd0bb1.png)

###### 4. Integrate LangSmith with Dify

Configure LangSmith in the Dify application. Open the application you need to monitor, open **Monitoring** in the side menu, and select **Tracing app performance** on the page.

  ![Tracing App Performance](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/b6c7e5d4c2ca2092d59465cca27bc69c.png)

After clicking configure, paste the **API Key** and **project name** created in LangSmith into the configuration and save.

  ![Configure LangSmith](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/93dfabcadb7b2ff597f54beb5e642124.png)

> **ℹ️ Info:**
>   The configured project name needs to match the project set in LangSmith. If the project names do not match, LangSmith will automatically create a new project during data synchronization.

Once successfully saved, you can view the monitoring status on the current page.

  ![View Configuration Status](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/43369dc4de8f606c166fae2efab97d73.png)

##### View Monitoring Data in LangSmith

Once configured, the debug or production data from applications within Dify can be monitored in LangSmith.

  ![Debugging Applications in Dify](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/a1370fdbb79257cba31a565ac6764802.png)

When you switch to LangSmith, you can view detailed operation logs of Dify applications in the dashboard.

  ![Viewing Application Data in LangSmith](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/2833b2ffa20927b5328e9624b065beea.png)

Detailed LLM operation logs through LangSmith will help you optimize the performance of your Dify application.

  ![Viewing Application Data in LangSmith](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/beeb4ee50c80de8db7400c1f65727c8c.png)

##### Monitoring Data List

###### **Workflow/Chatflow Trace Information**

**Used to track workflows and chatflows**

| Workflow | LangSmith Chain |
| --- | --- |
| workflow_app_log_id/workflow_run_id | id |
| user_session_id | - placed in metadata |
| name |  |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| Model token consumption | usage_metadata |
| metadata | extra |
| error | error |
| [workflow] | tags |
| "conversation_id/none for workflow" | conversation_id in metadata |
| conversion_id | parent_run_id |

**Workflow Trace Info**

* workflow_id - Unique identifier of the workflow
* conversation_id - Conversation ID
* workflow_run_id - ID of the current run
* tenant_id - Tenant ID
* elapsed_time - Time taken for the current run
* status - Run status
* version - Workflow version
* total_tokens - Total tokens used in the current run
* file_list - List of processed files
* triggered_from - Source that triggered the current run
* workflow_run_inputs - Input data for the current run
* workflow_run_outputs - Output data for the current run
* error - Errors encountered during the current run
* query - Query used during the run
* workflow_app_log_id - Workflow application log ID
* message_id - Associated message ID
* start_time - Start time of the run
* end_time - End time of the run
* workflow node executions - Information about workflow node executions
* Metadata
  * workflow_id - Unique identifier of the workflow
  * conversation_id - Conversation ID
  * workflow_run_id - ID of the current run
  * tenant_id - Tenant ID
  * elapsed_time - Time taken for the current run
  * status - Run status
  * version - Workflow version
  * total_tokens - Total tokens used in the current run
  * file_list - List of processed files
  * triggered_from - Source that triggered the current run

###### **Message Trace Information**

**Used to track LLM-related conversations**

| Chat | LangSmith LLM |
| --- | --- |
| message_id | id |
| user_session_id | - placed in metadata |
| name |  |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| Model token consumption | usage_metadata |
| metadata | extra |
| error | error |
| ["message", conversation_mode] | tags |
| conversation_id | conversation_id in metadata |
| conversion_id | parent_run_id |

**Message Trace Info**

* message_id - Message ID
* message_data - Message data
* user_session_id - User session ID
* conversation_model - Conversation mode
* message_tokens - Number of tokens in the message
* answer_tokens - Number of tokens in the answer
* total_tokens - Total number of tokens in the message and answer
* error - Error information
* inputs - Input data
* outputs - Output data
* file_list - List of processed files
* start_time - Start time
* end_time - End time
* message_file_data - File data associated with the message
* conversation_mode - Conversation mode
* Metadata
  * conversation_id - Conversation ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * agent_based - Whether the message is agent-based
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Moderation Trace Information**

**Used to track conversation moderation**

| Moderation | LangSmith Tool |
| --- | --- |
| user_id | - placed in metadata |
| “moderation" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | extra |
| [moderation] | tags |
| message_id | parent_run_id |

**Moderation Trace Info**

* message_id - Message ID
* user_id: User ID
* workflow_app_log_id - Workflow application log ID
* inputs - Moderation input data
* message_data - Message data
* flagged - Whether the content is flagged for attention
* action - Specific actions taken
* preset_response - Preset response
* start_time - Moderation start time
* end_time - Moderation end time
* Metadata
  * message_id - Message ID
  * action - Specific actions taken
  * preset_response - Preset response

###### **Suggested Question Trace Information**

**Used to track suggested questions**

| Suggested Question | LangSmith LLM |
| --- | --- |
| user_id | - placed in metadata |
| suggested_question | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | extra |
| [suggested_question] | tags |
| message_id | parent_run_id |

**Message Trace Info**

* message_id - Message ID
* message_data - Message data
* inputs - Input content
* outputs - Output content
* start_time - Start time
* end_time - End time
* total_tokens - Number of tokens
* status - Message status
* error - Error information
* from_account_id - ID of the sending account
* agent_based - Whether the message is agent-based
* from_source - Message source
* model_provider - Model provider
* model_id - Model ID
* suggested_question - Suggested question
* level - Status level
* status_message - Status message
* Metadata
  * message_id - Message ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Dataset Retrieval Trace Information**

**Used to track knowledge base retrieval**

| Dataset Retrieval | LangSmith Retriever |
| --- | --- |
| user_id | - placed in metadata |
| dataset_retrieval | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | extra |
| [dataset_retrieval] | tags |
| message_id | parent_run_id |

**Dataset Retrieval Trace Info**

* message_id - Message ID
* inputs - Input content
* documents - Document data
* start_time - Start time
* end_time - End time
* message_data - Message data
* Metadata
  * message_id - Message ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * agent_based - Whether the message is agent-based
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Tool Trace Information**

**Used to track tool invocation**

| Tool | LangSmith Tool |
| --- | --- |
| user_id | - placed in metadata |
| tool_name | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | extra |
| ["tool", tool_name] | tags |
| message_id | parent_run_id |

###### **Tool Trace Info**

* message_id - Message ID
* tool_name - Tool name
* start_time - Start time
* end_time - End time
* tool_inputs - Tool inputs
* tool_outputs - Tool outputs
* message_data - Message data
* error - Error information, if any
* inputs - Inputs for the message
* outputs - Outputs of the message
* tool_config - Tool configuration
* time_cost - Time cost
* tool_parameters - Tool parameters
* file_url - URL of the associated file
* Metadata
  * message_id - Message ID
  * tool_name - Tool name
  * tool_inputs - Tool inputs
  * tool_outputs - Tool outputs
  * tool_config - Tool configuration
  * time_cost - Time cost
  * error - Error information, if any
  * tool_parameters - Tool parameters
  * message_file_id - Message file ID
  * created_by_role - Role of the creator
  * created_user_id - User ID of the creator

**Generate Name Trace Information**

**Used to track conversation title generation**

| Generate Name | LangSmith Tool |
| --- | --- |
| user_id | - placed in metadata |
| generate_name | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | extra |
| [generate_name] | tags |

**Generate Name Trace Info**

* conversation_id - Conversation ID
* inputs - Input data
* outputs - Generated conversation name
* start_time - Start time
* end_time - End time
* tenant_id - Tenant ID
* Metadata
  * conversation_id - Conversation ID
  * tenant_id - Tenant ID

#### Integrate with Opik

**Source:** https://docs.dify.ai/en/cloud/use-dify/monitor/integrations/integrate-opik

##### What is Opik

Opik is an open-source platform designed for evaluating, testing, and monitoring large language model (LLM) applications. Developed by Comet, it aims to facilitate more intuitive collaboration, testing, and monitoring of LLM-based applications.

> **ℹ️ Info:**
>   For more details, please refer to [Opik](https://www.comet.com/site/products/opik/).

***

##### How to Configure Opik

###### 1. Register/Login to [Opik](https://www.comet.com/signup?from=llm)

###### 2. Get your Opik API Key

Retrieve your Opik API Key from the user menu at the top-right. Click on **API Key**, then on the API Key to copy it:

  ![Opik API Key](https://assets-docs.dify.ai/2025/01/a66603f01e4ffaa593a8b78fcf3f8204.png)

###### 3. Integrate Opik with Dify

Configure Opik in the Dify application. Open the application you need to monitor, open **Monitoring** in the side menu, and select **Tracing app performance** on the page.

  ![Tracing App Performance](https://assets-docs.dify.ai/2025/01/9d52a244e3b6cef1874ee838cd976111.png)

After clicking configure, paste the **API Key** and **project name** created in Opik into the configuration and save.

  ![Configure Opik](https://assets-docs.dify.ai/2025/01/7f4c436e2dc9fe94a3ed49219bb3360c.png)

Once successfully saved, you can view the monitoring status on the current page.

##### View Monitoring Data in Opik

Once configured, you can debug or use the Dify application as usual. All usage history can be monitored in Opik.

  ![Viewing Application Data in Opik](https://assets-docs.dify.ai/2025/01/a1c5aa80325e6d0223d48a178393baec.png)

When you switch to Opik, you can view detailed operation logs of Dify applications in the dashboard.

  ![Viewing Application Data in Opik](https://assets-docs.dify.ai/2025/01/09601d45eaf8ed90a4dfb07c34de36ff.png)

Detailed LLM operation logs through Opik will help you optimize the performance of your Dify application.

  ![Viewing Application Data in Opik](https://assets-docs.dify.ai/2025/01/708533b4fc616f852b5601fe602e3ef5.png)

##### Monitoring Data List

###### **Workflow/Chatflow Trace Information**

**Used to track workflows and chatflows**

| Workflow | Opik Trace |
| --- | --- |
| workflow_app_log_id/workflow_run_id | id |
| user_session_id | - placed in metadata |
| name |  |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| Model token consumption | usage_metadata |
| metadata | metadata |
| error | error |
| [workflow] | tags |
| "conversation_id/none for workflow" | conversation_id in metadata |

**Workflow Trace Info**

* workflow_id - Unique identifier of the workflow
* conversation_id - Conversation ID
* workflow_run_id - ID of the current run
* tenant_id - Tenant ID
* elapsed_time - Time taken for the current run
* status - Run status
* version - Workflow version
* total_tokens - Total tokens used in the current run
* file_list - List of processed files
* triggered_from - Source that triggered the current run
* workflow_run_inputs - Input data for the current run
* workflow_run_outputs - Output data for the current run
* error - Errors encountered during the current run
* query - Query used during the run
* workflow_app_log_id - Workflow application log ID
* message_id - Associated message ID
* start_time - Start time of the run
* end_time - End time of the run
* workflow node executions - Information about workflow node executions
* Metadata
  * workflow_id - Unique identifier of the workflow
  * conversation_id - Conversation ID
  * workflow_run_id - ID of the current run
  * tenant_id - Tenant ID
  * elapsed_time - Time taken for the current run
  * status - Run status
  * version - Workflow version
  * total_tokens - Total tokens used in the current run
  * file_list - List of processed files
  * triggered_from - Source that triggered the current run

###### **Message Trace Information**

**Used to track LLM-related conversations**

| Chat | Opik LLM |
| --- | --- |
| message_id | id |
| user_session_id | - placed in metadata |
| "llm" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| Model token consumption | usage_metadata |
| metadata | metadata |
| ["message", conversation_mode] | tags |
| conversation_id | conversation_id in metadata |

**Message Trace Info**

* message_id - Message ID
* message_data - Message data
* user_session_id - User session ID
* conversation_model - Conversation mode
* message_tokens - Number of tokens in the message
* answer_tokens - Number of tokens in the answer
* total_tokens - Total number of tokens in the message and answer
* error - Error information
* inputs - Input data
* outputs - Output data
* file_list - List of processed files
* start_time - Start time
* end_time - End time
* message_file_data - File data associated with the message
* conversation_mode - Conversation mode
* Metadata
  * conversation_id - Conversation ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * agent_based - Whether the message is agent-based
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Moderation Trace Information**

**Used to track conversation moderation**

| Moderation | Opik Tool |
| --- | --- |
| user_id | - placed in metadata |
| “moderation" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["moderation"] | tags |

**Moderation Trace Info**

* message_id - Message ID
* user_id: User ID
* workflow_app_log_id - Workflow application log ID
* inputs - Moderation input data
* message_data - Message data
* flagged - Whether the content is flagged for attention
* action - Specific actions taken
* preset_response - Preset response
* start_time - Moderation start time
* end_time - Moderation end time
* Metadata
  * message_id - Message ID
  * action - Specific actions taken
  * preset_response - Preset response

###### **Suggested Question Trace Information**

**Used to track suggested questions**

| Suggested Question | Opik LLM |
| --- | --- |
| user_id | - placed in metadata |
| "suggested_question" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["suggested_question"] | tags |

**Message Trace Info**

* message_id - Message ID
* message_data - Message data
* inputs - Input content
* outputs - Output content
* start_time - Start time
* end_time - End time
* total_tokens - Number of tokens
* status - Message status
* error - Error information
* from_account_id - ID of the sending account
* agent_based - Whether the message is agent-based
* from_source - Message source
* model_provider - Model provider
* model_id - Model ID
* suggested_question - Suggested question
* level - Status level
* status_message - Status message
* Metadata
  * message_id - Message ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Dataset Retrieval Trace Information**

**Used to track knowledge base retrieval**

| Dataset Retrieval | Opik Retriever |
| --- | --- |
| user_id | - placed in metadata |
| "dataset_retrieval" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["dataset_retrieval"] | tags |
| message_id | parent_run_id |

**Dataset Retrieval Trace Info**

* message_id - Message ID
* inputs - Input content
* documents - Document data
* start_time - Start time
* end_time - End time
* message_data - Message data
* Metadata
  * message_id - Message ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * agent_based - Whether the message is agent-based
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Tool Trace Information**

**Used to track tool invocation**

| Tool | Opik Tool |
| --- | --- |
| user_id | - placed in metadata |
| tool_name | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["tool", tool_name] | tags |

###### **Tool Trace Info**

* message_id - Message ID
* tool_name - Tool name
* start_time - Start time
* end_time - End time
* tool_inputs - Tool inputs
* tool_outputs - Tool outputs
* message_data - Message data
* error - Error information, if any
* inputs - Inputs for the message
* outputs - Outputs of the message
* tool_config - Tool configuration
* time_cost - Time cost
* tool_parameters - Tool parameters
* file_url - URL of the associated file
* Metadata
  * message_id - Message ID
  * tool_name - Tool name
  * tool_inputs - Tool inputs
  * tool_outputs - Tool outputs
  * tool_config - Tool configuration
  * time_cost - Time cost
  * error - Error information, if any
  * tool_parameters - Tool parameters
  * message_file_id - Message file ID
  * created_by_role - Role of the creator
  * created_user_id - User ID of the creator

**Generate Name Trace Information**

**Used to track conversation title generation**

| Generate Name | Opik Tool |
| --- | --- |
| user_id | - placed in metadata |
| "generate_conversation_name" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["generate_name"] | tags |

**Generate Name Trace Info**

* conversation_id - Conversation ID
* inputs - Input data
* outputs - Generated conversation name
* start_time - Start time
* end_time - End time
* tenant_id - Tenant ID
* Metadata
  * conversation_id - Conversation ID
  * tenant_id - Tenant ID

#### Integrate with Phoenix

**Source:** https://docs.dify.ai/en/cloud/use-dify/monitor/integrations/integrate-phoenix

##### What is Phoenix

Open-source & OpenTelemetry-based observability, evaluation, prompt engineering and experimentation platform for your LLM workflows and agents.

> **ℹ️ Info:**
>   For more details, please refer to [Phoenix](https://phoenix.arize.com).

##### How to Configure Phoenix

###### 1. Register/Login to [Phoenix](https://app.arize.com/auth/phoenix/signup)

###### 2. Get your Phoenix API Key

Retrieve your Phoenix API Key from the user menu at the top-right. Click on **API Key**, then on the API Key to copy it:

  ![Phoenix API Key](https://i.ibb.co/pB1W0pk8/dify-docs-phoenix-api-key.png)

###### 3. Integrate Phoenix with Dify

Configure Phoenix in the Dify application. Open the application you need to monitor, open **Monitoring** in the side menu, and select **Tracing app performance** on the page.

  ![Tracing App Performance](https://i.ibb.co/gMmXxfhQ/dify-docs-phoenix-in-use.png)

After clicking configure, paste the **API Key** and **project name** created in Phoenix into the configuration and save.

  ![Configure Phoenix](https://i.ibb.co/jv6QFbp7/dify-docs-phoenix-config.png)

Once successfully saved, you can view the monitoring status on the current page.

  ![Configure Phoenix](https://i.ibb.co/HTJsj9x2/dify-docs-phoenix-in-service.png)

##### How to Configure Phoenix Cloud

###### 1. Register/Login to [Phoenix Cloud](https://app.arize.com/auth/phoenix/signup)

###### 2. Create your Phoenix Space

You can create your Phoenix Space from the user menu at the top-right. Click on **Create Space**, then provide a unique URL identifier for your space:

  ![Phoenix Cloud Create Space](https://i.ibb.co/7JYPzZBf/dify-docs-phoenix-cloud-create-space.png)

Once successfully saved, you can view the space status on the overview page.

  ![Phoenix Cloud Space Overview](https://i.ibb.co/Z6RqMhhq/dify-docs-phoenix-cloud-space-overview.png)

###### 3. Create your Phoenix API Key

After launching your space, you can create your Phoenix API Key from the **Settings** option in the user menu at the bottom-left. Click on **System Key**, then provide a name for your Phoenix API Key:

  ![Phoenix Cloud API Key](https://i.ibb.co/SXMyX9K3/dify-docs-phoenix-cloud-api-key.png)

###### 4. Integrate Phoenix Cloud with Dify

Configure Phoenix in the Dify application. Open the application you need to monitor, open **Monitoring** in the side menu, and select **Tracing app performance** on the page.

  ![Tracing App Performance](https://i.ibb.co/gMmXxfhQ/dify-docs-phoenix-in-use.png)

After clicking configure, paste the **API Key** and **project name** along with **Space Hostname** created in Phoenix Cloud into the configuration and save.

  ![Configure Phoenix](https://i.ibb.co/jv6QFbp7/dify-docs-phoenix-config.png)

Once successfully saved, you can view the monitoring status on the current page.

  ![Configure Phoenix](https://i.ibb.co/HTJsj9x2/dify-docs-phoenix-in-service.png)

##### Monitoring Data List

###### **Workflow/Chatflow Trace Information**

**Used to track workflows and chatflows**

| Workflow | Phoenix Trace |
| --- | --- |
| workflow_app_log_id/workflow_run_id | id |
| user_session_id | - placed in metadata |
| name |  |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| Model token consumption | usage_metadata |
| metadata | metadata |
| error | error |
| [workflow] | tags |
| "conversation_id/none for workflow" | conversation_id in metadata |

**Workflow Trace Info**

* workflow_id - Unique identifier of the workflow
* conversation_id - Conversation ID
* workflow_run_id - ID of the current run
* tenant_id - Tenant ID
* elapsed_time - Time taken for the current run
* status - Run status
* version - Workflow version
* total_tokens - Total tokens used in the current run
* file_list - List of processed files
* triggered_from - Source that triggered the current run
* workflow_run_inputs - Input data for the current run
* workflow_run_outputs - Output data for the current run
* error - Errors encountered during the current run
* query - Query used during the run
* workflow_app_log_id - Workflow application log ID
* message_id - Associated message ID
* start_time - Start time of the run
* end_time - End time of the run
* workflow node executions - Information about workflow node executions
* Metadata
  * workflow_id - Unique identifier of the workflow
  * conversation_id - Conversation ID
  * workflow_run_id - ID of the current run
  * tenant_id - Tenant ID
  * elapsed_time - Time taken for the current run
  * status - Run status
  * version - Workflow version
  * total_tokens - Total tokens used in the current run
  * file_list - List of processed files
  * triggered_from - Source that triggered the current run

###### **Message Trace Information**

**Used to track LLM-related conversations**

| Chat | Phoenix LLM |
| --- | --- |
| message_id | id |
| user_session_id | - placed in metadata |
| "llm" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| Model token consumption | usage_metadata |
| metadata | metadata |
| ["message", conversation_mode] | tags |
| conversation_id | conversation_id in metadata |

**Message Trace Info**

* message_id - Message ID
* message_data - Message data
* user_session_id - User session ID
* conversation_model - Conversation mode
* message_tokens - Number of tokens in the message
* answer_tokens - Number of tokens in the answer
* total_tokens - Total number of tokens in the message and answer
* error - Error information
* inputs - Input data
* outputs - Output data
* file_list - List of processed files
* start_time - Start time
* end_time - End time
* message_file_data - File data associated with the message
* conversation_mode - Conversation mode
* Metadata
  * conversation_id - Conversation ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * agent_based - Whether the message is agent-based
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Moderation Trace Information**

**Used to track conversation moderation**

| Moderation | Phoenix Tool |
| --- | --- |
| user_id | - placed in metadata |
| “moderation" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["moderation"] | tags |

**Moderation Trace Info**

* message_id - Message ID
* user_id: User ID
* workflow_app_log_id - Workflow application log ID
* inputs - Moderation input data
* message_data - Message data
* flagged - Whether the content is flagged for attention
* action - Specific actions taken
* preset_response - Preset response
* start_time - Moderation start time
* end_time - Moderation end time
* Metadata
  * message_id - Message ID
  * action - Specific actions taken
  * preset_response - Preset response

###### **Suggested Question Trace Information**

**Used to track suggested questions**

| Suggested Question | Phoenix LLM |
| --- | --- |
| user_id | - placed in metadata |
| "suggested_question" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["suggested_question"] | tags |

**Message Trace Info**

* message_id - Message ID
* message_data - Message data
* inputs - Input content
* outputs - Output content
* start_time - Start time
* end_time - End time
* total_tokens - Number of tokens
* status - Message status
* error - Error information
* from_account_id - ID of the sending account
* agent_based - Whether the message is agent-based
* from_source - Message source
* model_provider - Model provider
* model_id - Model ID
* suggested_question - Suggested question
* level - Status level
* status_message - Status message
* Metadata
  * message_id - Message ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Dataset Retrieval Trace Information**

**Used to track knowledge base retrieval**

| Dataset Retrieval | Phoenix Retriever |
| --- | --- |
| user_id | - placed in metadata |
| "dataset_retrieval" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["dataset_retrieval"] | tags |
| message_id | parent_run_id |

**Dataset Retrieval Trace Info**

* message_id - Message ID
* inputs - Input content
* documents - Document data
* start_time - Start time
* end_time - End time
* message_data - Message data
* Metadata
  * message_id - Message ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * agent_based - Whether the message is agent-based
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Tool Trace Information**

**Used to track tool invocation**

| Tool | Phoenix Tool |
| --- | --- |
| user_id | - placed in metadata |
| tool_name | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["tool", tool_name] | tags |

###### **Tool Trace Info**

* message_id - Message ID
* tool_name - Tool name
* start_time - Start time
* end_time - End time
* tool_inputs - Tool inputs
* tool_outputs - Tool outputs
* message_data - Message data
* error - Error information, if any
* inputs - Inputs for the message
* outputs - Outputs of the message
* tool_config - Tool configuration
* time_cost - Time cost
* tool_parameters - Tool parameters
* file_url - URL of the associated file
* Metadata
  * message_id - Message ID
  * tool_name - Tool name
  * tool_inputs - Tool inputs
  * tool_outputs - Tool outputs
  * tool_config - Tool configuration
  * time_cost - Time cost
  * error - Error information, if any
  * tool_parameters - Tool parameters
  * message_file_id - Message file ID
  * created_by_role - Role of the creator
  * created_user_id - User ID of the creator

**Generate Name Trace Information**

**Used to track conversation title generation**

| Generate Name | Phoenix Tool |
| --- | --- |
| user_id | - placed in metadata |
| "generate_conversation_name" | name |
| start_time | start_time |
| end_time | end_time |
| inputs | inputs |
| outputs | outputs |
| metadata | metadata |
| ["generate_name"] | tags |

**Generate Name Trace Info**

* conversation_id - Conversation ID
* inputs - Input data
* outputs - Generated conversation name
* start_time - Start time
* end_time - End time
* tenant_id - Tenant ID
* Metadata
  * conversation_id - Conversation ID
  * tenant_id - Tenant ID

#### Integrate with W&B Weave

*Send traces from Dify applications to W&B Weave for LLM observability*

**Source:** https://docs.dify.ai/en/cloud/use-dify/monitor/integrations/integrate-weave

Send traces from Dify applications to W&B Weave for LLM observability

##### What is W\&B Weave

Weights & Biases (W\&B) Weave is a framework for tracking, experimenting with, evaluating, deploying, and improving LLM-based applications. Designed for flexibility and scalability, Weave supports every stage of your LLM application development workflow.

> **ℹ️ Info:**
>   For more details, please refer to [Weave](https://docs.wandb.ai/weave).

##### How to Configure Weave

###### 1. Register/Login

Register/Login to [W\&B Weave](https://wandb.ai/signup) and get your API key. Then, copy your API key from [here](https://wandb.ai/authorize).

###### 2. Integrate W\&B Weave with Dify

Configure Weave in the Dify application. Open the application you need to monitor, open **Monitoring** in the side menu, and select **Tracing app performance** on the page.

  ![Configure Weave in the Dify Application](https://assets-docs.dify.ai/2025/04/c33e8fda75ee9052ed23c8690e314862.png)

After clicking configure, paste the **API Key** and **project name**, also specify the **W\&B entity**(optionally, default is your username) into the configuration and save.

  ![Configure, Paste the API Key and Project Name, Also Specify the W\&B](https://assets-docs.dify.ai/2025/04/60bce1ae7b883825b13526d172ae0073.png)

Once successfully saved, you can view the monitoring status on the current page.

  ![Once Successfully Saved, You Can View the Monitoring Status on the Current Page](https://assets-docs.dify.ai/2025/04/9486cee7bbb61f069842c9ea860e679c.png)

##### View Monitoring Data in Weave

Once configured, the debug or production data from applications within Dify can be monitored in Weave.

  ![Once Configured, the Debug or Production Data from Applications Within Dify Can](https://assets-docs.dify.ai/2025/04/a1c5aa80325e6d0223d48a178393baec.png)

When you switch to Weave, you can view detailed operation logs of Dify applications in the dashboard.

  ![When You Switch to Weave, You Can View Detailed Operation Logs of Dify](https://assets-docs.dify.ai/2025/04/2cb04027c00b606029fcc26af2801bfe.png)

Detailed LLM operation logs through Weave will help you optimize the performance of your Dify application.

##### Monitoring Data List

###### **Workflow/Chatflow Trace Information**

**Used to track workflows and chatflows**

| Workflow                                 | Weave Trace                  |
| ---------------------------------------- | ---------------------------- |
| workflow_app_log_id/workflow_run_id | id                           |
| user_session_id                        | placed in metadata           |
| workflow_\{id}                          | name                         |
| start_time                              | start_time                  |
| end_time                                | end_time                    |
| inputs                                   | inputs                       |
| outputs                                  | outputs                      |
| Model token consumption                  | usage_metadata              |
| metadata                                 | extra                        |
| error                                    | error                        |
| workflow                                 | tags                         |
| "conversation_id/none for workflow"     | conversation_id in metadata |
| conversion_id                           | parent_run_id              |

**Workflow Trace Info**

* workflow_id - Unique identifier of the workflow
* conversation_id - Conversation ID
* workflow_run_id - ID of the current run
* tenant_id - Tenant ID
* elapsed_time - Time taken for the current run
* status - Run status
* version - Workflow version
* total_tokens - Total tokens used in the current run
* file_list - List of processed files
* triggered_from - Source that triggered the current run
* workflow_run_inputs - Input data for the current run
* workflow_run_outputs - Output data for the current run
* error - Errors encountered during the current run
* query - Query used during the run
* workflow_app_log_id - Workflow application log ID
* message_id - Associated message ID
* start_time - Start time of the run
* end_time - End time of the run
* workflow node executions - Information about workflow node executions
* Metadata
  * workflow_id - Unique identifier of the workflow
  * conversation_id - Conversation ID
  * workflow_run_id - ID of the current run
  * tenant_id - Tenant ID
  * elapsed_time - Time taken for the current run
  * status - Run status
  * version - Workflow version
  * total_tokens - Total tokens used in the current run
  * file_list - List of processed files
  * triggered_from - Source that triggered the current run

###### **Message Trace Information**

**Used to track LLM-related conversations**

| Chat                          | Weave Trace                  |
| ----------------------------- | ---------------------------- |
| message_id                   | id                           |
| user_session_id             | placed in metadata           |
| "message_\{id}"              | name                         |
| start_time                   | start_time                  |
| end_time                     | end_time                    |
| inputs                        | inputs                       |
| outputs                       | outputs                      |
| Model token consumption       | usage_metadata              |
| metadata                      | extra                        |
| error                         | error                        |
| "message", conversation_mode | tags                         |
| conversation_id              | conversation_id in metadata |
| conversion_id                | parent_run_id              |

**Message Trace Info**

* message_id - Message ID
* message_data - Message data
* user_session_id - User session ID
* conversation_model - Conversation mode
* message_tokens - Number of tokens in the message
* answer_tokens - Number of tokens in the answer
* total_tokens - Total number of tokens in the message and answer
* error - Error information
* inputs - Input data
* outputs - Output data
* file_list - List of processed files
* start_time - Start time
* end_time - End time
* message_file_data - File data associated with the message
* conversation_mode - Conversation mode
* Metadata
  * conversation_id - Conversation ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * agent_based - Whether the message is agent-based
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Moderation Trace Information**

**Used to track conversation moderation**

| Moderation   | Weave Trace        |
| ------------ | ------------------ |
| user_id     | placed in metadata |
| “moderation" | name               |
| start_time  | start_time        |
| end_time    | end_time          |
| inputs       | inputs             |
| outputs      | outputs            |
| metadata     | extra              |
| moderation   | tags               |
| message_id  | parent_run_id    |

**Moderation Trace Info**

* message_id - Message ID
* user_id: User ID
* workflow_app_log_id - Workflow application log ID
* inputs - Moderation input data
* message_data - Message data
* flagged - Whether the content is flagged for attention
* action - Specific actions taken
* preset_response - Preset response
* start_time - Moderation start time
* end_time - Moderation end time
* Metadata
  * message_id - Message ID
  * action - Specific actions taken
  * preset_response - Preset response

###### **Suggested Question Trace Information**

**Used to track suggested questions**

| Suggested Question  | Weave Trace        |
| ------------------- | ------------------ |
| user_id            | placed in metadata |
| suggested_question | name               |
| start_time         | start_time        |
| end_time           | end_time          |
| inputs              | inputs             |
| outputs             | outputs            |
| metadata            | extra              |
| suggested_question | tags               |
| message_id         | parent_run_id    |

**Message Trace Info**

* message_id - Message ID
* message_data - Message data
* inputs - Input content
* outputs - Output content
* start_time - Start time
* end_time - End time
* total_tokens - Number of tokens
* status - Message status
* error - Error information
* from_account_id - ID of the sending account
* agent_based - Whether the message is agent-based
* from_source - Message source
* model_provider - Model provider
* model_id - Model ID
* suggested_question - Suggested question
* level - Status level
* status_message - Status message
* Metadata
  * message_id - Message ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Dataset Retrieval Trace Information**

**Used to track knowledge base retrieval**

| Dataset Retrieval  | Weave Trace        |
| ------------------ | ------------------ |
| user_id           | placed in metadata |
| dataset_retrieval | name               |
| start_time        | start_time        |
| end_time          | end_time          |
| inputs             | inputs             |
| outputs            | outputs            |
| metadata           | extra              |
| dataset_retrieval | tags               |
| message_id        | parent_run_id    |

**Dataset Retrieval Trace Info**

* message_id - Message ID
* inputs - Input content
* documents - Document data
* start_time - Start time
* end_time - End time
* message_data - Message data
* Metadata
  * message_id - Message ID
  * ls_provider - Model provider
  * ls_model_name - Model ID
  * status - Message status
  * from_end_user_id - ID of the sending user
  * from_account_id - ID of the sending account
  * agent_based - Whether the message is agent-based
  * workflow_run_id - Workflow run ID
  * from_source - Message source

###### **Tool Trace Information**

**Used to track tool invocation**

| Tool               | Weave Trace        |
| ------------------ | ------------------ |
| user_id           | placed in metadata |
| tool_name         | name               |
| start_time        | start_time        |
| end_time          | end_time          |
| inputs             | inputs             |
| outputs            | outputs            |
| metadata           | extra              |
| "tool", tool_name | tags               |
| message_id        | parent_run_id    |

###### **Tool Trace Info**

* message_id - Message ID
* tool_name - Tool name
* start_time - Start time
* end_time - End time
* tool_inputs - Tool inputs
* tool_outputs - Tool outputs
* message_data - Message data
* error - Error information, if any
* inputs - Inputs for the message
* outputs - Outputs of the message
* tool_config - Tool configuration
* time_cost - Time cost
* tool_parameters - Tool parameters
* file_url - URL of the associated file
* Metadata
  * message_id - Message ID
  * tool_name - Tool name
  * tool_inputs - Tool inputs
  * tool_outputs - Tool outputs
  * tool_config - Tool configuration
  * time_cost - Time cost
  * error - Error information, if any
  * tool_parameters - Tool parameters
  * message_file_id - Message file ID
  * created_by_role - Role of the creator
  * created_user_id - User ID of the creator

**Generate Name Trace Information**

**Used to track conversation title generation**

| Generate Name  | Weave Trace        |
| -------------- | ------------------ |
| user_id       | placed in metadata |
| generate_name | name               |
| start_time    | start_time        |
| end_time      | end_time          |
| inputs         | inputs             |
| outputs        | outputs            |
| metadata       | extra              |
| generate_name | tags               |

**Generate Name Trace Info**

* conversation_id - Conversation ID
* inputs - Input data
* outputs - Generated conversation name
* start_time - Start time
* end_time - End time
* tenant_id - Tenant ID
* Metadata
  * conversation_id - Conversation ID
  * tenant_id - Tenant ID

#### Logs

*Monitor real-time conversations, debug issues, and collect user feedback*

**Source:** https://docs.dify.ai/en/cloud/use-dify/monitor/logs

Monitor real-time conversations, debug issues, and collect user feedback

Conversation logs provide detailed visibility into every interaction with your AI application. Use them to debug specific issues, understand user behavior patterns, and collect feedback for continuous improvement.

#### What Gets Logged

**All User Interactions**
Every conversation through your web app or API is logged with complete input/output history, timing data, and system metadata.

**User Feedback**
Thumbs up/down ratings and user comments are captured alongside the conversations they reference.

**System Context**
Model used, token consumption, response times, and any errors or warnings during processing.

**Exclusions**: Debugging sessions and prompt testing are not included in logs.

#### Use the Logs Console

Access logs from your application's navigation menu. The interface shows:

* **Conversation Timeline**: Chronological list of user interactions
* **Message Details**: Full conversation context with AI responses
* **Performance Data**: Response times and token usage per interaction
* **User Feedback**: Ratings and comments from users and team members

#### Debug with Logs

**Failed Interactions**
Quickly identify conversations where the AI provided poor responses, failed to understand user intent, or encountered errors.

**Performance Issues**
Spot slow responses, high token usage, or system errors that affect user experience.

**User Journey Analysis**
Follow individual users through multiple conversations to understand usage patterns and pain points.

#### Feedback Collection

**User Ratings**
Users can provide thumbs up/down feedback on AI responses. Track satisfaction trends over time.

**Team Annotations**
Team members can add internal notes and improved responses directly in the log interface.

**Feedback Analysis**
Identify common complaint patterns, successful interaction types, and areas needing improvement.

#### Log Retention

> **⚠️ Warning:**
>   Ensure your application complies with local data privacy regulations. Publish a privacy policy and obtain user consent where required.

Logs on the **Sandbox** plan are retained for 30 days. Older entries are pruned automatically.

> **ℹ️ Info:**
>   Unlimited log retention is available on **[Professional]** and **[Team]** for the duration of the active subscription. [Learn more](https://dify.ai/pricing).

#### Improve Applications with Logs

**Pattern Recognition**
Look for recurring user questions that your application handles poorly. These indicate opportunities for prompt improvements or knowledge base updates.

**Response Quality**
Use feedback patterns to identify which types of responses work well and which need refinement.

**Performance Optimization**
Track response times and token usage to identify inefficient prompts or model configurations.

**Content Gaps**
Spot topics or question types where your application consistently struggles, indicating areas for knowledge base expansion.

#### Privacy Considerations

Logs contain complete user conversations and may include sensitive information. Implement appropriate access controls and ensure compliance with applicable data protection regulations.

### Nodes

#### Agent

*Give LLMs autonomous control over tools for complex task execution*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/agent

Give LLMs autonomous control over tools for complex task execution

The Agent node gives your LLM autonomous control over tools, enabling it to iteratively decide which tools to use and when to use them. Instead of pre-planning every step, the Agent reasons through problems dynamically, calling tools as needed to complete complex tasks.

  ![Agent Node Configuration Interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/1f4d803ff68394d507abd3bcc13ba0f3.png)

#### Agent Strategies

Agent strategies define how your Agent thinks and acts. Choose the approach that best matches your model's capabilities and task requirements.

  ![Available Agent Strategy Options](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/f14082c44462ac03955e41d66ffd4cca.png)

  **Function Calling:**

    Uses the LLM's native function calling capabilities to directly pass tool definitions through the tools parameter. The LLM decides when and how to call tools using its built-in mechanism.

    Best for models like GPT-4, Claude 3.5, and other models with robust function calling support.

  **ReAct (Reason + Act):**

    Uses structured prompts that guide the LLM through explicit reasoning steps. Follows a **Thought → Action → Observation** cycle for transparent decision-making.

    Works well with models that may not have native function calling or when you need explicit reasoning traces.

> **ℹ️ Info:**
>   Install additional strategies from **Marketplace → Agent Strategies** or contribute custom strategies to the [community repository](https://github.com/langgenius/dify-plugins).

  ![Function Calling Strategy Configuration](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/10505cd7c6f0b3ba10161abb88d9e36b.png)

#### Configuration

##### Model Selection

Choose an LLM that supports your selected agent strategy. More capable models handle complex reasoning better but cost more per iteration. Ensure your model supports function calling if using that strategy.

##### Tool Configuration

Configure the tools your Agent can access. Each tool requires:

**Authorization** - API keys and credentials for external services configured in your workspace

**Description** - Clear explanation of what the tool does and when to use it (this guides the Agent's decision-making)

**Parameters** - Required and optional inputs the tool accepts with proper validation

##### Instructions and Context

Define the Agent's role, goals, and context using natural language instructions. Use Jinja2 syntax to reference variables from upstream workflow nodes.

**Query** specifies the user input or task the Agent should work on. This can be dynamic content from previous workflow nodes.

  ![Agent Configuration Parameters](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/54c8e4f0eaa7379bd8c1b5ac6305b326.png)

##### Execution Controls

**Maximum Iterations** sets a safety limit to prevent infinite loops. Configure based on task complexity - simple tasks need 3-5 iterations, while complex research might require 10-15.

**Memory** controls how many previous messages the Agent remembers using TokenBufferMemory. Larger memory windows provide more context but increase token costs. This enables conversational continuity where users can reference previous actions.

##### Tool Parameter Auto-Generation

Tools can have parameters configured as **auto-generated** or **manual input**. Auto-generated parameters (`auto: false`) are automatically populated by the Agent, while manual input parameters require explicit values that become part of the tool's permanent configuration.

*[Video demonstration]*

#### Output Variables

Agent nodes provide comprehensive output including:

**Final Answer** - The Agent's ultimate response to the query

**Tool Outputs** - Results from each tool invocation during execution

**Reasoning Trace** - Step-by-step decision process (especially detailed with ReAct strategy) available in the JSON output

**Iteration Count** - Number of reasoning cycles used

**Success Status** - Whether the Agent completed the task successfully

**Agent Logs** - Structured log events with metadata for debugging and monitoring tool invocations

#### Use Cases

**Research and Analysis** - Agents can autonomously search multiple sources, synthesize information, and provide comprehensive answers.

**Troubleshooting** - Diagnostic tasks where the Agent needs to gather information, test hypotheses, and adapt its approach based on findings.

**Multi-step Data Processing** - Complex workflows where the next action depends on intermediate results.

**Dynamic API Integration** - Scenarios where the sequence of API calls depends on responses and conditions that can't be predetermined.

#### Best Practices

**Clear Tool Descriptions** help the Agent understand when and how to use each tool effectively.

**Appropriate Iteration Limits** prevent runaway costs while allowing sufficient flexibility for complex tasks.

**Detailed Instructions** provide context about the Agent's role, goals, and any constraints or preferences.

**Memory Management** balance context retention with token efficiency based on your use case requirements.

#### Answer

*Define response content in Chatflow applications*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/answer

Define response content in Chatflow applications

The Answer node defines what content gets delivered to users in Chatflow applications. Use it to format responses, combine text with variables, and stream multimodal content including text, images, and files.

> **ℹ️ Info:**
>   The Answer node is only available for Chatflow applications. Workflow applications use the End node instead.

#### Content Configuration

The Answer node provides a flexible text editor where you can craft responses using fixed text, variables from previous nodes, or combinations of both.

Reference variables from any previous workflow node using the `{{variable_name}}` syntax. The editor supports rich content formatting and variable insertion to create dynamic, contextual responses.

  ![Plain Text Answer Configuration](https://assets-docs.dify.ai/2025/04/42bb6bdef101bf79f959f4fc56a50ff3.png)

#### Multimodal Responses

Answer nodes support rich content delivery including text, images, and files in a single response stream.

  ![Multimodal Answer with Image and Text Content](https://assets-docs.dify.ai/2025/04/d2c901e821029756ebf95f4e099d833f.png)

**Text Content** can include variable substitution, markdown formatting, and dynamic content based on workflow processing results.

**Image Content** displays images generated by tools, uploaded by users, or processed by workflow nodes. Images stream alongside text for rich user experiences.

**File Content** delivers documents, spreadsheets, or other files generated or processed during the workflow execution.

  ![Answer Node User Interface in Chat](https://assets-docs.dify.ai/2025/04/5a70a5e568dded3975e54cfa84085c93.png)

#### Streaming Behavior

Answer nodes stream content progressively based on variable availability. The node outputs all content up to the first unresolved variable, then waits for that variable to resolve before continuing.

**Variable Order Matters** - The sequence of variables in your Answer node determines streaming behavior, not the execution order of upstream nodes.

For example, with nodes executing as `Node A -> Node B -> Answer`:

* If the Answer contains `{{A}}` then `{{B}}`, it streams A's content immediately when available, then waits for B
* If the Answer contains `{{B}}` then `{{A}}`, it waits for B to complete before streaming any content

This streaming behavior enables responsive user experiences while maintaining content coherence.

#### Multiple Answer Nodes

You can place multiple Answer nodes throughout your Chatflow to deliver content at different stages of processing.

#### Variable Integration

Answer nodes seamlessly integrate with outputs from all workflow node types. Common variable sources include:

**LLM Responses** - Display generated text, analysis results, or structured outputs from language models

**Knowledge Retrieval** - Show relevant information found in knowledge bases with automatic citation tracking

**Tool Results** - Present data from external APIs, calculations, or service integrations

**File Processing** - Display extracted text, analysis results, or processed document content

The variable system maintains type safety and automatically handles different content types for optimal display in the chat interface.

#### Code

*Execute custom Python or JavaScript for data processing*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/code

Execute custom Python or JavaScript for data processing

The Code node executes custom Python or JavaScript to handle complex data transformations, calculations, and logic within your workflow. Use it when preset nodes aren't sufficient for your specific processing needs.

  ![Code Node Configuration Interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/9969aa1bc1912aebe366f5d8f5dde296.png)

#### Configuration

Define **Input Variables** to access data from other nodes in your workflow, then reference these variables in your code. Your function must return a dictionary containing the **Output Variables** you've declared.

```python theme={null}
def main(input_variable: str) -> dict:
    # Process the input
    result = input_variable.upper()
    return {
        'output_variable': result
    }
```

#### Language Support

Choose between **Python** and **JavaScript** based on your needs and familiarity. Both languages run in secure sandboxes with access to common libraries for data processing.

  **Python:**

    Python includes standard libraries like `json`, `math`, `datetime`, and `re`. Ideal for data analysis, mathematical operations, and text processing.

    ```python theme={null}
    def main(data: list) -> dict:
        import json
        import math

        average = sum(data) / len(data)
        return {'result': math.ceil(average)}
    ```

  **JavaScript:**

    JavaScript provides standard built-in objects and methods. Good for JSON manipulation and string operations.

    ```javascript theme={null}
    function main(data) {
        const processed = data.map(item => item.toUpperCase());
        return { result: processed };
    }
    ```

#### Error Handling and Retries

Configure automatic retry behavior for failed code executions and define fallback strategies when code encounters errors.

  ![Error Handling Configuration Options](https://assets-docs.dify.ai/2024/12/58f392734ce44b22cd8c160faf28cd14.png)

**Retry Settings** allow up to 10 automatic retries with configurable intervals (maximum 5000ms). Enable this for handling temporary processing issues.

**Error Handling** lets you define fallback paths when code execution fails, allowing your workflow to continue running even when the code encounters problems.

  ![Retry Configuration Interface](https://assets-docs.dify.ai/2024/12/9fdd5525a91dc925b79b89272893becf.png)

#### Output Limits

Before an output passes to the next node, Dify checks that it isn't too large:

* **Strings**: up to 400,000 characters.
* **Numbers**: whole numbers up to 19 digits, and decimals up to 20 places.
* **Objects and arrays**: nested up to five levels deep.

An output that exceeds a limit fails the check, so trim or split large results before returning them.

#### Security Considerations

Code runs in an isolated sandbox that blocks file system access, outbound network requests, and system commands. The sandbox keeps execution separated from the underlying infrastructure while still giving you the flexibility of writing custom code.

Because of this isolation, operations that reach outside the sandbox are blocked automatically. Avoid reading system files, opening network connections, or running shell commands; restructure your logic to work with the input variables and libraries available inside the sandbox instead.

#### Dependencies Support

Code nodes support external dependencies for both Python and JavaScript:

```python theme={null}
# Python: Import numpy, pandas, requests, etc.
import numpy as np
import pandas as pd

def main(data: list) -> dict:
    df = pd.DataFrame(data)
    return {'mean': float(np.mean(df['values']))}
```

```javascript theme={null}
// JavaScript: Import lodash, moment, etc.
const _ = require('lodash');

function main(data) {
    return { unique: _.uniq(data) };
}
```

A standard set of packages is pre-installed in the sandbox environment. Imports outside that set will fail at execution time.

#### Document Extractor

*Extract text content from uploaded documents for AI processing*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/doc-extractor

Extract text content from uploaded documents for AI processing

The Document Extractor node converts uploaded files into text that LLMs can process. Since language models can't directly read document formats like PDF or DOCX, this node serves as the essential bridge between file uploads and AI analysis.

  ![Document Extractor Node Configuration](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/f3853b40904e275da895711107e9c72f.png)

#### Supported File Types

The node handles most text-based document formats:

**Text Documents** - TXT, Markdown, HTML files with direct text content

**Office Documents** - DOCX files from Microsoft Word and compatible applications

**PDF Documents** - Text-based PDFs

**Office Files** - DOC files require Unstructured API, DOCX files support direct parsing with table extraction converted to Markdown format

**Spreadsheets** - Excel (.xls/.xlsx) and CSV files converted to Markdown tables

**Presentations** - PowerPoint (.ppt/.pptx) files processed via Unstructured API

**Email Formats** - EML and MSG files for email content extraction

**Specialized Formats** - EPUB books, VTT subtitles, JSON/YAML data, and Properties files

Files containing primarily binary content like images, audio, or video require specialized processing tools or external services.

#### Input and Output

##### Input Configuration

Configure the node to accept either:

**Single File** input from a file variable (typically from the Start node)

**Multiple Files** as an array for batch document processing

##### Output Structure

The node outputs extracted text content:

* Single file input produces a `string` containing the extracted text
* Multiple file input produces an `array[string]` with each file's content

The output variable is named `text` and contains the raw text content ready for downstream processing.

#### Implementation Example

Here's a complete document Q\&A workflow using the Document Extractor:

  ![ChatPDF-style Workflow Implementation](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/f6ea094b30b240c999a4248d1fc21a1c.png)

##### Workflow Setup

**File Upload Configuration** - Enable file input in your Start node to accept document uploads from users.

**Text Extraction** - Connect the Document Extractor to process uploaded files and extract their text content.

**AI Processing** - Use the extracted text in LLM prompts for analysis, summarization, or question answering.

  ![Document Processing in Action](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/83bca46bcde07069660ff649e5c7cf4c.png)

  ![Chat Interface with Document Upload](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/d05301438e8aab7393bb5863554f1009.png)

#### Processing Considerations

The Document Extractor uses specialized parsing libraries optimized for different file formats. It preserves text structure and formatting where possible, making extracted content more useful for LLM processing.

##### File Format Processing

**Encoding Detection** - Uses chardet library to automatically detect file encoding with UTF-8 fallback for text-based files

**Table Conversion** - Excel and CSV data becomes Markdown tables for better LLM comprehension

**Document Structure** - DOCX files maintain paragraph and table ordering with proper table-to-Markdown conversion

**Multi-line Content** - VTT subtitle files merge consecutive utterances by the same speaker

##### External Dependencies

Some file formats are processed through the **Unstructured API** service:

* DOC files (legacy Word documents)
* PowerPoint presentations (if using API processing)
* EPUB books (if using API processing)

For very large documents, consider the LLM's context limits and implement chunking strategies if needed. The extracted text maintains the original document's logical structure to preserve meaning and context.

#### HTTP Request

*Connect to external APIs and web services*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/http-request

Connect to external APIs and web services

The HTTP Request node connects your workflow to external APIs and web services. Use it to fetch data, send webhooks, upload files, or integrate with any service that accepts HTTP requests.

  ![HTTP Request Node Configuration](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/07c5e952eb4c9d6a32d0b7c2d855d4a5.png)

#### HTTP Methods

The node supports all standard HTTP methods for different types of operations:

  **Data Retrieval:**

    **GET** retrieves data from servers without modifying anything. Use for fetching user profiles, searching databases, or getting current status.

    **HEAD** gets response headers without the full response body. Useful for checking if resources exist or getting metadata.

  **Data Submission:**

    **POST** sends data to servers, typically for creating new resources. Use for form submissions, file uploads, or sending JSON payloads.

    **PUT** creates or completely replaces resources. Use when you want to set the entire state of a resource.

    **PATCH** makes partial updates to existing resources. Use when you only need to modify specific fields.

  **Resource Management:**

    **DELETE** removes resources from servers. Use for deleting files, user accounts, or any resource that should be removed.

#### Configuration

Configure every aspect of your HTTP request including URL, headers, query parameters, request body, and authentication. Variables from previous workflow nodes can be dynamically inserted anywhere in your request configuration.

##### Variable Substitution

Reference workflow variables using double curly braces: `{{variable_name}}`. Dify supports deep object access, so you can extract nested values like `{{api_response.data.items[0].id}}` from previous HTTP responses.

##### Timeout Configuration

HTTP requests have configurable timeouts to prevent hanging:

* **Connect timeout**: Maximum time to establish connection
* **Read timeout**: Maximum time to read response data
* **Write timeout**: Maximum time to send request data

Timeouts are enforced to maintain workflow performance and prevent resource exhaustion.

##### Authentication

The node supports multiple authentication types:

**No Auth** (`type: "no-auth"`) - No authentication headers added

**API Key** (`type: "api-key"`) with three subtypes:

* **Basic** (`type: "basic"`) - Adds Basic Auth header with base64 encoding
* **Bearer** (`type: "bearer"`) - Adds `Authorization: Bearer <token>` header
* **Custom** (`type: "custom"`) - Adds custom header with specified name and value

##### Request Body

Choose the appropriate body type based on your API requirements:

* **JSON** for structured data
* **Form Data** for traditional web forms
* **Binary** for file uploads
* **Raw Text** for custom content types

#### File Detection

The HTTP Request node automatically detects file responses using sophisticated logic:

1. **Content-Disposition analysis** - Checks for `attachment` disposition or filename parameters
2. **MIME type evaluation** - Analyzes content types to distinguish text from binary
3. **Content sampling** - For ambiguous types, samples first 1024 bytes to detect text patterns

Text-based responses (JSON, XML, HTML, etc.) are treated as regular data, while binary content becomes file variables.

#### File Operations

The HTTP Request node handles file uploads and downloads seamlessly:

  ![File Upload Configuration Example](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/1f2e33cf7bed33096b5aee145006193d.png)

**File Uploads** use the binary request body option. Select file variables from previous nodes to send files to external services for document storage, media processing, or backup.

**File Downloads** are automatically handled when responses contain file content. Downloaded files become available as file variables for use in downstream nodes.

#### Error Handling and Retries

Configure robust error handling for production workflows that depend on external services:

  ![HTTP Retry Configuration](https://assets-docs.dify.ai/2024/12/2e7c6080c0875e31a074c2a9a4543797.png)

**Retry Settings** automatically retry failed requests up to 10 times with configurable intervals (maximum 5000ms). This handles temporary network issues or service unavailability.

  ![HTTP Error Handling Options](https://assets-docs.dify.ai/2024/12/91daa86d9770390ab2a41d6d0b6ed1e7.png)

**Error Handling** defines alternative workflow paths when HTTP requests fail, ensuring your workflow continues executing even when external APIs are unavailable.

#### Response Processing

HTTP responses become structured variables in subsequent nodes with separate access to:

* **Response Body** - The main content returned by the API
* **Status Code** - HTTP status for conditional logic
* **Headers** - Response metadata as key-value pairs
* **Files** - Any file content returned by the API
* **Size Information** - Content size in bytes with readable formatting (KB/MB)

##### SSL Verification

SSL certificate verification is configurable per node (`ssl_verify` parameter). This allows connections to internal services with self-signed certificates while maintaining security for external APIs.

  ![Dynamic API Integration Example Workflow](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/090975269f8998f906c5636dde8d9540.png)

#### Human Input

*Pause workflows to request human input*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/human-input

Pause workflows to request human input

The Human Input node pauses workflows at key points to deliver a customizable request form. Recipients can use the form to review information, provide input, and choose from predefined decisions that determine how the workflow proceeds.

By embedding human judgement directly where it matters, you can *balance automated efficiency with human oversight*.

> **💡 Tip:**
>   For a workflow design example, see [Example: Content Review Workflow](#example-content-review-workflow).

#### Configuration

Configure the following to define how the node requests and processes human input:

* **Delivery method**: How the request form reaches recipients.

* **Form content**: What information recipients will see and what they can interact with.

* **User action**: What decisions recipients can make and how the workflow proceeds accordingly.

* **Timeout strategy**: How long to wait and what happens if no recipient responds.

##### Delivery Method

Choose the channel through which the request is delivered. Currently available methods:

* **Web app**: Displays the request form to the WebApp end user. Not available in workflows started by a Trigger.

  > **ℹ️ Info:**
>     External clients can drive the WebApp form lifecycle through the Service API. See [API Integration Flow](https://docs.dify.ai/en/api-reference/guides/human-input-flow).
>

* **Email**: Sends a request link via email to specific workspace members, external email addresses, or every member of the workspace. Anyone with the link can respond, no Dify account required.

> **📝 Note:**
>   The request closes after the first response regardless of delivery method.

##### Form Content

Customize the form recipients see and interact with:

* **Format and structure with Markdown**

  Use headings, lists, bold text, links, and other Markdown elements to present information clearly.

* **Display dynamic data with variables**

  Reference workflow variables to show dynamic content, such as AI-generated text for review or a file someone uploaded at an upstream Human Input node for approval.

  In WebApp delivery, the form itself displays to end users. Any variables you reference render their values directly in the form, so **no Answer or Output node is needed before the Human Input node**.

  > **💡 Tip:**
>     Reasoning models emit their thinking process alongside the final answer. Referencing the `text` output variable shows both by default.
>
>     To show only the answer, toggle on **Enable Reasoning Tag Separation** for the corresponding LLM node.
>

* **Collect input with form fields**

  Add fields into the request form to capture different types of input from recipients. Each field becomes a variable for downstream use.

  For example, in a blog review workflow, you can pass recipient feedback to a downstream LLM node for content revision.

  | Field Type              | Description                                                                                                                                                                                                                        |
  | :---------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Paragraph               | Text input. Can start empty, or pre-filled with variables (e.g., LLM output to refine) or static text (examples or default values). 

No maximum length, but very long inputs may exceed downstream LLM context windows. |
  | Select                  | Single-choice selection from a list of options. Define options manually, or reference an `array[string]` variable to use its items as options.                                                                                     |
  | Single File / File List | Single or multiple file uploads.

Per-file upload limits: 10 MB for images, 15 MB for documents and other files, 50 MB for audio, and 100 MB for video. A File List field accepts up to 10 files.                        |

  > **📝 Note:**
> Only Paragraph is optional; Select, Single File, and File List are mandatory. The form's action buttons stay disabled until all mandatory fields are filled.

After the recipient responds, the form content with all values filled in is available downstream as the `__rendered_content` variable. File field values render as plain-text placeholders: `[file]` for Single File and `[N files]` for File List.

##### User Action

Define the decision buttons that recipients can click, each routing the workflow to a different execution path.

For example, a `Post` branch might lead to nodes that trigger content publishing, while a `Regenerate` branch might loop back to an LLM node to revise the content.

Each button has a display title and an action ID. When a button is clicked, its ID is exposed downstream as `__action_id` and its title (button text) as `__action_value`.

  *[Image: Action Button Configuration]*

> **💡 Tip:**
>   Use preset button styles to visually distinguish actions.
>
>   For example, use a prominent style for key actions like `Approve` and a subtler one for secondary options.

##### Timeout Strategy

Configure how long the request stays open before it expires. The default is 3 days.

If no recipient responds before the timeout, the workflow follows the timeout branch from the node. Wire this branch to a fallback path, such as a notification or a retry loop.

If no timeout branch is connected, the workflow ends.

#### Example: Content Review Workflow

    *[Image: Workflow Example]*

    *[Image: Request Form Example]*

This workflow drafts a blog post from the `topic` and `language` that a workflow initiator inputs, emails the draft to a reviewer, and finalizes the output based on the reviewer's choice.

It is designed around three things the reviewer should be able to do:

1. **See the AI-generated draft**: Reference the upstream LLM node's `text` variable in the form so the rendered form displays the draft directly.

2. **Edit the draft directly if needed**: Add a Paragraph field named `edits` in the form, pre-filled with the same `text` variable, so the reviewer sees the draft as starting content and can edit in place.

   Because blog posts are long, the form's Markdown display (point 1) reads better than a Paragraph field on its own. For shorter content, the pre-filled Paragraph field alone can handle both reading and editing.

3. **Provide feedback for an AI revision**:

   1. Add a Paragraph field named `feedback` in the form for the reviewer's feedback.
   2. Connect two downstream LLM nodes in sequence:
      1. A Regenerate node that takes the original draft `text` and the reviewer's `feedback` to produce a revised draft.
      2. A Check Revision node that takes `feedback` and the revised draft to verify whether the revision addresses the feedback. The verified result is what flows downstream.

On the received request form, the reviewer fills the relevant Paragraph fields (or leaves them blank) based on their judgment, then clicks the matching action button. Each action wires to a different output:

* **Approve**: the original draft from the upstream LLM
* **Apply Edit**: the reviewer's edited content from the `edits` field
* **Regenerate**: the revised draft from the downstream LLM pipeline

**LLM Node Prompts for Reference:**

    **Generate Draft:**

      **System**

      ```text wrap theme={null}
      Write a marketing blog post around the given topic in the specified language.
      ```

      **User**

      ```text theme={null}
      Topic: {{#user_input.topic#}}
      Language: {{#user_input.language#}}
      ```

    **Regenerate:**

      **System**

      ```text wrap theme={null}
      Regenerate the draft based on user feedback.
      ```

      **User**

      ```text theme={null}
      Draft: {{#generate_draft.text#}}
      User Feedback: {{#human_input.feedback#}}
      ```

    **Check Revision:**

      **System**

      ```text wrap theme={null}
      Check whether the draft below addresses the user's feedback. Return the draft unchanged if it does; revise it to address the feedback if it doesn't.
      ```

      **User**

      ```text theme={null}
      User Feedback: {{#human_input.feedback#}}
      Regenerated Draft: {{#regenerate.text#}}
      ```

#### If-Else

*Add conditional logic and branching to workflows*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/ifelse

Add conditional logic and branching to workflows

The If-Else node adds decision-making logic to your workflows by routing execution down different paths based on conditions you define. It evaluates variables and determines which branch your workflow should follow.

  ![If-Else Conditional Branching Example](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/d26ffff1b2ad0989d46e80d6812cf2e7.png)

#### Branching Logic

The node supports multiple branching paths to handle complex decision trees:

**IF Path** executes when the primary condition evaluates to true.

**ELIF Paths** provide additional conditions to check in sequence when the IF condition is false. You can add multiple ELIF branches for complex logic.

**ELSE Path** serves as the fallback when no conditions match, ensuring your workflow always has a path to follow.

#### Condition Types

Configure conditions to test variables using various comparison operators:

  **Text Operations:**

    **Contains** / **Not contains** - Check if the value includes specific words or phrases

    **Starts with** / **Ends with** - Test text beginnings or endings for pattern matching

    **Is** / **Is not** - Exact value matching

  **Value Checks:**

    **Is empty** / **Is not empty** - Check for blank, null, or missing values

    **Greater than** / **Less than** - Numerical comparisons for numbers and dates

    **Equals** / **Not equals** - Exact matching for any data type

#### Complex Conditions

Combine multiple conditions using logical operators for sophisticated decision-making:

  ![Complex Condition Configuration with AND/OR Logic](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/0b71ee7363e07298348e0c81e63481b0.png)

**AND Logic** requires all conditions to be true. Use this when you need multiple criteria to be met simultaneously.

**OR Logic** requires any condition to be true. Use this when you want to trigger the same action for different scenarios.

#### Variable References

Reference any variable from previous workflow nodes in your conditions. Variables can come from user input, LLM responses, API calls, or any other workflow node output.

Use the variable selector to choose from available variables, or type variable names directly using the `{{variable_name}}` syntax.

#### Iteration

*Process arrays by applying workflows to each element*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/iteration

Process arrays by applying workflows to each element

The Iteration node processes arrays by running the same workflow steps on each element sequentially or in parallel. Use it for batch processing tasks that would otherwise hit limits or be inefficient as single operations.

  ![Iteration Node Processing Workflow](https://assets-docs.dify.ai/2025/04/5f3f124c16b9e3565853f125f7db0e32.png)

#### How Iteration Works

The node takes an array input and creates a sub-workflow that runs once for each array element. During each iteration, the current item and its index are available as variables that internal nodes can reference.

**Core Components**:

* **Input Variables** - Array data from upstream nodes
* **Internal Workflow** - The processing steps to perform on each element
* **Output Variables** - Collected results from all iterations (also an array)

#### Configuration

##### Array Input

Connect an array variable from upstream nodes such as Parameter Extractor, Code nodes, Knowledge Retrieval, or HTTP Request responses.

##### Built-in Variables

Each iteration provides access to:

* `items[object]` - The current array element being processed
* `index[number]` - The current iteration index (starting from 0)

##### Processing Mode

  **Sequential Mode:**

    **Sequential Processing** - Items processed one after another in order

    **Streaming Support** - Results can be output progressively using Answer nodes

    **Resource Management** - Lower memory usage, predictable execution order

    **Best For** - When order matters or when using streaming output

  **Parallel Mode:**

    **Concurrent Processing** - Up to 10 items processed simultaneously

    **Improved Performance** - Faster execution for independent operations

    **Batch Processing** - Handles large arrays efficiently

    **Best For** - Independent operations where order doesn't matter

  ![Sequential vs Parallel Processing Comparison](https://assets-docs.dify.ai/2024/12/2656dec26d6357556a280fcd69ccd9a7.png)

  ![Enable Parallel Mode in Iteration Settings](https://assets-docs.dify.ai/2024/12/516af5e7427fce9a58fa9d9b583230d4.png)

#### Error Handling

Configure how to handle processing failures for individual array elements:

**Terminate** - Stop processing when any error occurs and return the error message

**Continue on Error** - Skip failed items and continue processing, outputting null for failed elements

**Remove Failed Results** - Skip failed items and return only successful results

Input-output correspondence examples:

* Input: `[1, 2, 3]`
* Output with Continue on Error: `[result-1, null, result-3]`
* Output with Remove Failed: `[result-1, result-3]`

#### Long Article Generation Example

Generate lengthy content by processing chapter outlines individually:

  ![Long Article Generation Workflow](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/3a403551d48b178d0a41ce2a5748dd2d.png)

**Workflow Steps**:

1. **Start Node** - User provides story title and outline
2. **LLM Node** - Generate detailed chapter breakdown
3. **Parameter Extractor** - Convert chapter list to structured array
4. **Iteration Node** - Process each chapter with internal LLM
5. **Answer Node** - Stream chapter content as it's generated

  ![Start Node Configuration for Story Input](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/3af1c2ed0df00f19e584bcf511302f55.png)

  ![Parameter Extraction for Chapter Structure](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/d3beee536ff3c35f4e1eb1ab610f35d7.png)

  ![Iteration Configuration with LLM Processing](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/ac91582998868004b298afe2f04e5589.png)

> **ℹ️ Info:**
>   Parameter extraction effectiveness depends on model capabilities and instruction quality. Use stronger models and provide examples in instructions to improve results.

#### Output Processing

Iteration nodes output arrays that often need conversion for final use:

##### Convert Array to Text

  **Using Code Node:**

    ```python theme={null}
    def main(articleSections: list):
        return {
            "result": "\n".join(articleSections)
        }
    ```

      ![Code Node Array Conversion](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/8be2372b00a802e981efe6f0ceff815b.png)

  **Using Template Node:**

    ```jinja theme={null}
    {{ articleSections | join("\n") }}
    ```

      ![Template Node Array Conversion](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/8c0bcc5de453dea2776d2755449bd971.png)

#### Knowledge Retrieval

*Retrieve relevant content from knowledge bases and use it as context for downstream nodes*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/knowledge-retrieval

Retrieve relevant content from knowledge bases and use it as context for downstream nodes

Use the Knowledge Retrieval node to integrate existing knowledge bases into your workflows. The node searches specific knowledge for information relevant to queries and outputs results as contextual content for use in downstream nodes (e.g., LLMs).

Below is an example of using the Knowledge Retrieval node in a Chatflow:

1. The **User Input** node collects the user query.

2. The **Knowledge Retrieval** node searches the selected knowledge base(s) for content related to the user query and outputs the retrieval results.

3. The **LLM** node generates a response based on both the user query and the retrieved knowledge.

4. The **Answer** node returns the LLM's response to the user.

  *[Image: Knowledge Retrieval Node Use Case]*

Before using a Knowledge Retrieval node, ensure that you have at least one available knowledge base. To learn about creating knowledge bases, see [Knowledge](https://docs.dify.ai/en/cloud/use-dify/knowledge/readme#create-knowledge).

> **ℹ️ Info:**
>   Knowledge retrieval operations are subject to per-minute rate limits that vary by subscription plan. See [Knowledge Request Rate Limit](https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-request-rate-limit) for the per-plan numbers.

#### Configure the Node

To make the Knowledge Retrieval node work properly, you need to specify:

* *What* it should search for (the query)

* *Where* it should search (the knowledge base)

* *How* to process the retrieval results (the node-level retrieval settings)

You can also use document metadata to enable filter-based searches and further improve retrieval precision.

##### Specify the Query

Provide the query content that the node should search for in the selected knowledge base(s).

* **Query Text**: Select a text variable. For example, use `userinput.query` to reference user input in Chatflows, or a custom text-type user input variable in Workflows.

* **Query Images**: Select an image variable, e.g., the image(s) uploaded by the user through a User Input node, to search by image. Each image must be 2 MB or smaller.

  > **ℹ️ Info:**
>     The **Query Images** option is available only when at least one multimodal knowledge base is added.
>
>     Such knowledge bases are marked with the **Vision** tag, indicating that they are using a multimodal embedding model.
>

##### Select Knowledge to Search

Add one or more existing knowledge bases for the node to search for content relevant to the query.

When multiple knowledge bases are added, knowledge is first retrieved from all of them simultaneously, then combined and processed according to the [node-level retrieval settings](#configure-node-level-retrieval-settings).

> **ℹ️ Info:**
>   Knowledge bases marked with the **Vision** tag support cross-modal retrieval: they return both text and images based on semantic relevance.

You can click the **Edit** icon next to any added knowledge base to modify its [settings](https://docs.dify.ai/en/cloud/use-dify/knowledge/manage-knowledge/introduction).

##### Configure Node-Level Retrieval Settings

To fine-tune how the node processes retrieval results after they are fetched from the knowledge base(s), click **Retrieval Setting**.

> **ℹ️ Info:**
>   Retrieval settings exist at two layers: the knowledge base level and the knowledge retrieval node level.
>
>   Think of them as two consecutive filters: the knowledge base settings determine the initial pool of results, and the node settings further rerank the results or narrow down the pool.

* **Rerank Settings**

  * **Weighted Score**

    The relative weight between semantic similarity and keyword matching during reranking. Higher semantic weight favors meaning relevance, while higher keyword weight favors exact matches.

    Weighted Score is available only when all added knowledge bases are indexed with **High Quality** mode.

  * **Rerank Model**

    The rerank model to re-score and reorder all the results based on their relevance to the query.

    > **📝 Note:**
>       If any multimodal knowledge bases are added, select a multimodal rerank model (marked with a **Vision** tag) as well. Otherwise, retrieved images will be excluded from reranking and the final output.
>

* **Top K**

  The maximum number of top results to return after reranking.

  When a rerank model is selected, this value will be automatically adjusted based on the model's maximum input capacity (how much text the model can process at once).

* **Score Threshold**

  The minimum similarity score for returned results. Results scoring below this threshold are excluded. Use higher thresholds for stricter relevance or lower thresholds to include broader matches.

##### Enable Metadata Filtering

By default, retrieval searches across the entire knowledge base. To restrict retrieval to specific documents, enable manual or automatic metadata filtering.

This improves retrieval precision, especially when your knowledge base is large or contains content for different contexts.

For creating and managing document metadata, see [Metadata](https://docs.dify.ai/en/cloud/use-dify/knowledge/metadata).

#### Output

The Knowledge Retrieval node outputs the retrieval results as a variable named `result`, which is an array of retrieved document chunks containing their content, metadata, title, and other attributes.

When the retrieval results contain image attachments, the `result` variable also includes a field named `files` containing image details.

#### Use with LLM Nodes

To use the retrieval results as context in an LLM node:

1. In **Context**, select the Knowledge Retrieval node's `result` variable.

2. In the system instruction, reference the `Context` variable.

3. Optional: If the LLM is vision-capable, enable **Vision** so it can process image attachments in the retrieval results.

   > **ℹ️ Info:**
>      You don't need to specify the retrieval results as the vision input. Once **Vision** is enabled, the LLM will automatically access any retrieved images.
>

In chatflows, citations are shown alongside responses that reference knowledge by default. You can turn this off by disabling **[Citation and Attributions](https://docs.dify.ai/en/cloud/use-dify/build/additional-features#citations-and-attributions)** in **Features** at the top right corner of the canvas.

#### List Operator

*Filter, sort, and select elements from arrays*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/list-operator

Filter, sort, and select elements from arrays

The List Operator node processes arrays by filtering, sorting, and selecting specific elements. Use it when you need to work with mixed file uploads, large datasets, or any array data that requires separation or organization before downstream processing.

Supported input data types include `array[string]`, `array[number]`, `array[file]`, and `array[boolean]`.

  ![List Operator Node Interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/522a0c932aab93d4f3970168412f759e.png)

#### The Array Processing Problem

Most workflow nodes expect single values, not arrays. When you have mixed content like `[image.png, document.pdf, audio.mp3]` in one variable, you need to separate this into focused streams that downstream nodes can process effectively.

The List Operator acts as an intelligent router, using filters to separate mixed arrays and prepare them for specialized processing.

  ![Array Processing Workflow Example](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/812d1b2f167065e17df8392b2cb3cc8a.png)

#### Operations

##### Filtering

Extract specific items based on their attributes. For file arrays, filter by:

  **Content Properties:**

    **Type** - Filter by content category: image, document, audio, video

    **MIME Type** - Precise content type identification (image/jpeg, application/pdf, etc.)

    **Extension** - File extensions (.pdf, .jpg, .mp3, .docx, etc.)

  **File Properties:**

    **Size** - File size constraints for processing limits

    **Name** - Filename patterns or specific names

    **Transfer Method** - Distinguish between local uploads and URL-based files

##### Sorting

Organize filtered results by any attribute:

**Ascending (ASC)** - Smallest to largest values, A-Z alphabetical order

**Descending (DESC)** - Largest to smallest values, Z-A reverse order

##### Selection

Choose specific elements from the processed array:

**Take First N** - Select the first 1-20 items after filtering and sorting

**First Record** - Return only the first matching element as a single value

**Last Record** - Return only the last matching element as a single value

#### Output Variables

**result** - Complete filtered and sorted array for bulk processing

**first_record** - Single element from the beginning, perfect for "primary" or "latest" item selection

**last_record** - Single element from the end, useful for "most recent" or "final" selection

#### Mixed File Processing Example

Handle workflows where users upload both documents and images:

  ![Mixed File Processing Workflow](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/610358293217e54b55b7e1d4d16bf83c.png)

**Implementation Steps**:

1. **Configure Mixed Uploads** - Enable file upload features to accept multiple file types
2. **Split by Type** - Use separate List Operator nodes with different filters:
   * Filter for `type = "image"` → route to LLM with vision capabilities
   * Filter for `type = "document"` → route to Document Extractor
3. **Process Appropriately** - Images get analyzed directly, documents get text extraction
4. **Combine Results** - Merge processed outputs into unified responses

This pattern automatically routes different file types to appropriate processors, creating seamless multi-modal user experiences.

#### LLM

*Invoke language models for text generation and analysis*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/llm

Invoke language models for text generation and analysis

The LLM node invokes language models to process text, images, and documents. It sends prompts to your configured models and captures their responses, supporting structured outputs, context management, and multimodal inputs.

  ![LLM Node Configuration Interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/85730fbfa1d441d12d969b89adf2670e.png)

> **ℹ️ Info:**
>   Configure at least one model provider in **Integrations** > **Model Provider** before using LLM nodes.

#### Model Selection and Parameters

Choose from any model provider you've configured. Different models excel at different tasks - GPT-4 and Claude 3.5 handle complex reasoning well but cost more, while GPT-3.5 Turbo balances capability with affordability.

  ![Model Selection and Parameter Configuration](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/43f81418ea70d4d79e3705505e777b1b.png)

Model parameters control response generation. **Temperature** ranges from 0 (deterministic) to 1 (creative). **Top P** limits word choices by probability. **Frequency Penalty** reduces repetition. **Presence Penalty** encourages new topics. You can also use presets: **Precise**, **Balanced**, or **Creative**.

#### Prompt Configuration

Your interface adapts based on model type. Chat models use message roles (**System** for behavior, **User** for input, **Assistant** for examples), while completion models use simple text continuation.

Reference workflow variables in prompts using double curly braces: `{{variable_name}}`. Variables are replaced with actual values before reaching the model.

```text theme={null}
System: You are a technical documentation expert.
User: {{user_input}}
```

#### Context Variables

Context variables inject external knowledge while preserving source attribution. This enables RAG applications where LLMs answer questions using your specific documents.

  ![Using Context Variables for RAG Applications](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/5aefed96962bd994f8f05bac96b11e22.png)

Connect a Knowledge Retrieval node's output to your LLM node's context input, then reference it:

```text theme={null}
Answer using only this context:
{{knowledge_retrieval.result}}

Question: {{user_question}}
```

When using context variables from knowledge retrieval, Dify automatically tracks citations so users see information sources.

#### Structured Outputs

Force models to return specific data formats like JSON for programmatic use. Configure through three methods:

  **Visual Editor:**

    User-friendly interface for simple structures. Add fields with names and types, mark required fields, set descriptions. The editor generates JSON Schema automatically.

  **JSON Schema:**

    Write schemas directly for complex structures with nested objects, arrays, and validation rules.

    ```json theme={null}
    {
      "type": "object",
      "properties": {
        "sentiment": {
          "type": "string",
          "enum": ["positive", "negative", "neutral"]
        }
      },
      "required": ["sentiment"]
    }
    ```

  **AI Generation:**

    Describe needs in plain language and let AI generate the schema.

> **⚠️ Warning:**
>   Models with native JSON support handle structured outputs reliably. For others, Dify includes the schema in prompts, but results may vary.

#### Memory and File Processing

  *[Image: LLM Memory]*

Enable Memory to maintain context across multiple LLM calls within a Chatflow conversation. When enabled, previous interactions will be included in subsequent prompts as formatted user - assistant outputs. You can customize what goes into the user prompts by editing the `USER` template. Memory is node-specific and doesn't persist between different conversations.

For **File Processing**, add file variables to prompts for multimodal models. GPT-4V handles images, Claude processes PDFs directly, while other models might need preprocessing.

##### Vision Configuration

When processing images, you can control the detail level:

* **High detail** - Better accuracy for complex images but uses more tokens
* **Low detail** - Faster processing with fewer tokens for simple images

The default variable selector for vision is `userinput.files` which automatically picks up files from the User Input node.

  ![File Processing with Multimodal LLMs](https://assets-docs.dify.ai/2024/11/05b3d4a78038bc7afbb157078e3b2b26.png)

#### Jinja2 Template Support

LLM prompts support Jinja2 templating for advanced variable handling. When you use Jinja2 mode (`edition_type: "jinja2"`), you can:

```jinja theme={null}
{% for item in search_results %}
{{ loop.index }}. {{ item.title }}: {{ item.content }}
{% endfor %}
```

Jinja2 variables are processed separately from regular variable substitution, allowing for loops, conditionals, and complex data transformations within prompts.

#### Streaming Output

LLM nodes support streaming output by default. Each text chunk is yielded as a `RunStreamChunkEvent`, enabling real-time response display. File outputs (images, documents) are processed and saved automatically during streaming.

#### Separate Reasoning from Responses

Some reasoning models wrap their thinking in `...</think>` tags inside their response. By default, those tags are included in the `text` output, so the reasoning flows downstream together with the answer.

Turn on the **Enable reasoning tag separation** toggle to split them: the `text` output keeps only the answer, and the thinking moves to a separate `reasoning_content` output variable. While the toggle is off, `reasoning_content` stays empty.

In API calls, this toggle appears as the `reasoning_format` parameter. When the toggle is on, `reasoning_format` is `separated`, and streaming API clients receive the reasoning as dedicated `reasoning_chunk` events, outside the answer stream. For event details, see [Send Chat Message](https://docs.dify.ai/en/api-reference/chat-messages/send-chat-message) and [Run Workflow](https://docs.dify.ai/en/api-reference/workflow-runs/run-workflow).

> **ℹ️ Info:**
>   This setting affects only models that wrap their reasoning in `` tags.

#### Error Handling

Configure retry behavior for failed LLM calls. Set maximum retry attempts, intervals between retries, and backoff multipliers. Define fallback strategies like default values, error routing, or alternative models when retries aren't sufficient.

#### Loop

*Execute repetitive workflows with progressive refinement*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/loop

Execute repetitive workflows with progressive refinement

The Loop node executes repetitive workflows where each cycle builds on the results of the previous one. Unlike iteration, which processes array elements independently, loops create progressive workflows that evolve with each repetition.

#### Loop vs Iteration

Understanding when to use each repetition pattern:

  **Loop:**

    **Sequential Processing** - Each cycle depends on previous results

    **Progressive Refinement** - Outputs improve or evolve over iterations

    **State Management** - Variables persist and accumulate across cycles

    **Use Cases** - Content refinement, problem solving, quality assurance

  **Iteration:**

    **Independent Processing** - Each item processed separately

    **Parallel Execution** - Items can be processed simultaneously

    **Batch Operations** - Same operation applied to multiple data points

    **Use Cases** - Data transformation, bulk processing, parallel analysis

#### Configuration

##### Loop Variables

Define variables that persist across loop iterations and remain accessible after the loop completes. These variables maintain state and enable progressive workflows.

##### Termination Conditions

Configure when the loop should stop executing:

**Loop Termination Condition** - Expression that determines when to exit (e.g., `quality_score > 0.9`)

**Maximum Loop Count** - Safety limit to prevent infinite loops

**Exit Loop Node** - Immediate termination when this node is reached

> **ℹ️ Info:**
>   The loop terminates when either the termination condition is met, the maximum count is reached, or an Exit Loop node executes. If no conditions are specified, the loop continues until the maximum count.

#### Basic Loop Example

Generate random numbers until finding one less than 50:

  ![Basic Loop Workflow for Random Number Generation](https://assets-docs.dify.ai/2025/04/282013c48b46d3cc4ebf99323da10a31.png)

**Workflow Steps**:

1. **Code node** generates random integers between 1-100
2. **If-Else node** checks if number is less than 50
3. **Template node** returns "done" for numbers \< 50 to trigger loop termination
4. Loop continues until termination condition is met

  ![Loop Execution Steps and Results](https://assets-docs.dify.ai/2025/04/9d9fb4db7093521000ac735a26f86962.png)

#### Advanced Loop Example

Create a poem through iterative refinement, with each version building upon the previous one:

*[Video demonstration]*

**Loop Variables**:

* `num` - Counter starting at 0, incrementing each iteration
* `verse` - Text variable holding the current poem version

**Workflow Logic**:

1. **If-Else node** checks if `num > 3` to determine when to exit
2. **LLM node** generates improved poem based on previous version
3. **Variable Assigner** updates both counter and poem content
4. **Exit Loop node** terminates after 4 refinement cycles

The LLM prompt references both the current verse and iteration context:

```text theme={null}
You are a European literary figure creating poetic verses.

Current verse: {{verse}}

Refine and improve this poem based on your previous work.
```

#### Output

*Return workflow results to the end user or API caller*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/output

Return workflow results to the end user or API caller

Use the Output node to deliver specific variable values from your workflow to the end user or API caller. Add it where you need to surface results.

> **ℹ️ Info:**
>   The Output node was previously named *End* and was required in every workflow.
>
>   It is now optional—workflows run successfully without one, but any workflow or branch without an Output node returns no data to the caller.
>
>   Output nodes are only available in Workflows. Chatflows use the [Answer](https://docs.dify.ai/en/cloud/use-dify/nodes/answer) node instead.

#### Configure Output Variables

Each Output node requires at least one output variable. To add a variable, assign a name and select the source from any upstream node's output.

> **ℹ️ Info:**
>   The variable name you assign becomes the key in API responses.

You can add multiple output variables to a single Output node and reorder them by dragging.

#### Supported Variable Types

Output variables support the following types:

`string`, `number`, `integer`, `boolean`, `object`, `file`, `array[string]`, `array[number]`, `array[object]`, `array[boolean]`, `array[file]`

#### Multiple Output Nodes

A workflow can contain more than one Output node. The Output node does not stop workflow execution—other parallel branches (if any) continue running after it completes.

All output variables from every executed Output node are combined into one final result. Each Output node adds its variables to the result as the workflow reaches it:

* On the **same branch**, variables are added in the order the Output nodes are placed.

* On **parallel branches**, whichever Output node executes first adds its variables first.

> **⚠️ Warning:**
>   Always use unique variable names across all Output nodes in a workflow.
>
>   When two Output nodes use the same output variable name, the later one overwrites the earlier value.

#### API Response Structure

When you call a workflow through the API, output variables appear in the `outputs` object of the response.

  **Blocking Mode:**

    All outputs return in a single response once the workflow completes:

    ```json theme={null}
    {
      "workflow_run_id": "...",
      "status": "succeeded",
      "outputs": {
        "result_text": "The processed output...",
        "score": 95
      }
    }
    ```

  **Streaming Mode:**

    Outputs arrive in the final `workflow_finished` event:

    ```json theme={null}
    {
      "event": "workflow_finished",
      "data": {
        "outputs": {
          "result_text": "The processed output...",
          "score": 95
        }
      }
    }
    ```

Each output variable name maps directly to a key in the `outputs` object.

#### For Workflow Tools

When you [publish a workflow as a tool](https://docs.dify.ai/en/cloud/use-dify/workspace/tools#workflow), the Output node defines the tool's return schema. Each output variable name becomes a key in the tool's result, accessible to the parent workflow that invokes the tool.

#### Parameter Extractor

*Convert natural language to structured data using LLM intelligence*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/parameter-extractor

Convert natural language to structured data using LLM intelligence

The Parameter Extractor node converts unstructured text into structured data using LLM intelligence. It bridges the gap between natural language input and the structured parameters that tools, APIs, and other workflow nodes require.

#### Configuration

##### Input and Model Selection

Select the **Input Variable** containing the text you want to extract parameters from. This typically comes from user input, LLM responses, or other workflow nodes.

Choose a **Model** with strong structured output capabilities. The Parameter Extractor relies on the LLM's ability to understand context and generate structured JSON responses.

##### Parameter Definition

Define the parameters you want to extract by specifying:

* **Parameter Name** - The key that will appear in the output JSON
* **Data Type** - String, number, boolean, array, or object
* **Description** - Helps the LLM understand what to extract
* **Required Status** - Whether the parameter must be present

You can manually define parameters or **quickly import from existing tools** to match the parameter requirements of downstream nodes.

##### Extraction Instructions

Write clear instructions describing what information to extract and how to format it. Providing examples in your instructions improves extraction accuracy and consistency for complex parameters.

  ![Parameter Extraction for Arxiv Paper Retrieval](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/a8bae4106a015c76ebb0a165f2409458.png)

#### Advanced Configuration

##### Inference Mode

Choose between two extraction approaches based on your model's capabilities:

**Function Call/Tool Call** uses the model's structured output features for reliable parameter extraction with strong type compliance.

**Prompt-based** relies on pure prompting for models that may not support function calling or when prompt-based extraction performs better.

##### Memory

Enable memory to include conversation history when extracting parameters. This helps the LLM understand context in interactive dialogues and improves extraction accuracy for conversational workflows.

#### Output Variables

The node provides both extracted parameters and built-in status variables:

**Extracted Parameters** appear as individual variables matching your parameter definitions, ready for use in downstream nodes.

**Built-in Variables** include status information:

* `__is_success` - Extraction success status (1 for success, 0 for failure)
* `__reason` - Error description when extraction fails

  ![Data Format Conversion Example](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/71d8e48d842342668f92e6dd84fc03c1.png)

#### Question Classifier

*Intelligently categorize user input to route workflow paths*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/question-classifier

Intelligently categorize user input to route workflow paths

The Question Classifier node intelligently categorizes user input to route conversations down different workflow paths. Instead of building complex conditional logic, you define classes and let the LLM determine which one fits best based on semantic understanding.

#### Configuration

##### Input and Model Setup

**Input Variable** - Select what to classify, typically `sys.query` for user questions, but can be any text variable from previous workflow nodes.

**Model Selection** - Choose an LLM for classification. Faster models work well for simple classes, while more powerful models handle nuanced distinctions better.

  ![Question Classifier Configuration Interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/2f039c5ff3f095b0eed291101d9bff15.png)

##### Class Definition

Each class has two independent pieces of text:

* **Class description** (the editor body) is what the LLM reads when choosing a branch.

  Write a precise, distinguishing description of what belongs in the class; boundary phrases like "anything related to..." or "excluding..." help when classes overlap. Exposed downstream as `class_name`.

* **Class title** (the small heading above the editor) is the label shown on the canvas.

  Double-click the default **CLASS N** title to rename it. Exposed downstream as `class_label`.

The title and the description edit independently, so you can keep a short, scannable label on the canvas while giving the LLM a longer, more specific description.

Each class becomes a potential output path that you can connect to different downstream nodes like specialized knowledge bases, response templates, or processing workflows.

#### Classification Example

Here's how the Question Classifier works in a customer service scenario:

  ![Customer Service Classification Workflow](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/2f06ecce149c844c23be70a8fcff09bc.png)

**Classes Defined**:

* **After-sales service** - Warranty claims, returns, repairs, and post-purchase support
* **Product usage** - Setup instructions, troubleshooting, feature explanations
* **Other questions** - General inquiries not covered by specific classes

**Classification Results**:

* "How to set up contacts on iPhone 14?" → **Product usage**
* "What is the warranty period for my purchase?" → **After-sales service**
* "What's the weather like today?" → **Other questions**

Each classification result routes to different knowledge bases and response strategies, ensuring users receive relevant, specialized assistance.

#### Advanced Configuration

##### Instructions and Guidelines

Add detailed classification guidelines in the **Instructions** field to handle edge cases, ambiguous scenarios, or specific business rules. This helps the LLM understand nuanced distinctions between classes.

#### Start Node

*Choose how your workflow begins, on demand or automatically*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/start

Choose how your workflow begins, on demand or automatically

When you create a new workflow, you choose a start node that decides whether the workflow waits for someone to run it or runs on its own.

#### User Input

Use [User Input](https://docs.dify.ai/en/cloud/use-dify/nodes/user-input) when someone (or an API call) should kick off the workflow and supply information it needs. You define input fields for text, numbers, files, and other data, and downstream nodes reference those values.

Only User Input workflows can be published as web apps, MCP servers, backend service APIs, or reused as tools in other Dify apps.

> **ℹ️ Info:**
>   Chatflows always start with User Input. Only Workflows can use triggers.

#### Trigger

Use a [trigger](https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/overview) when the workflow should run automatically, without anyone invoking it. Three types are available:

* **[Schedule Trigger](https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/schedule-trigger)**: runs at specified times or intervals.
* **[Integration Trigger](https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/plugin-trigger)**: runs when an event occurs in an external system, via a subscription through a trigger integration.
* **[Webhook Trigger](https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/webhook-trigger)**: runs when the workflow receives an HTTP request from an external system.

#### Switch Between Start Nodes

User Input and triggers are mutually exclusive on a canvas. To switch, right-click the current start node and select **Change Node**, or delete it and add a new one.

#### Template

*Transform and format data using Jinja2 templating*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/template

Transform and format data using Jinja2 templating

The Template node transforms and formats data from multiple sources into structured text using Jinja2 templating. Use it to combine variables, format outputs, and prepare data for downstream nodes or end users.

  ![Template Node Configuration Interface](https://assets-docs.dify.ai/2025/04/0838bb5c7e1d1a58ed30fcd9fc48920f.png)

#### Jinja2 Templating

Template nodes use Jinja2 templating syntax to create dynamic content that adapts based on workflow data. This provides programming-like capabilities including loops, conditionals, and filters for sophisticated text generation.

##### Variable Substitution

Reference workflow variables using double curly braces: `{{ variable_name }}`. You can access nested object properties and array elements using dot notation and bracket syntax.

```jinja theme={null}
{{ user.name }}
{{ items[0].title }}
{{ data.metrics.score }}
```

##### Conditional Logic

Show different content based on data values using if-else statements:

```jinja theme={null}
{% if user.subscription == 'premium' %}
Welcome back, Premium Member! You have access to all features.
{% else %}
Consider upgrading to Premium for additional capabilities.
{% endif %}
```

##### Loops and Iteration

Process arrays and objects with for loops to generate repetitive content:

```jinja theme={null}
{% for item in search_results %}
### Result {{ loop.index }}
**Score**: {{ item.score | round(2) }}
{{ item.content }}
---
{% endfor %}
```

  ![Template Processing Knowledge Retrieval Results](https://assets-docs.dify.ai/2025/04/0ae3f13cf725cb2c52c72cc354e592ee.png)

#### Data Formatting

##### Filters

Jinja2 filters transform data during template rendering:

```jinja theme={null}
{{ name | upper }}
{{ price | round(2) }}
{{ content | replace('\n', '
') }}
{{ tags | join(', ') }}
{{ score | default('No score available') }}
```

##### Error Handling

Handle missing or invalid data gracefully using default values and conditional checks:

```jinja theme={null}
{{ user.email | default('No email provided') }}
{{ metrics.accuracy | round(2) if metrics.accuracy else 'Not calculated' }}
```

#### Interactive Forms

Templates can generate interactive HTML forms for structured data collection in Chatflows.

On submit, the form values are sent to the chat as the end user's next message. The format depends on the ``'s `data-format` attribute:

* **`data-format="json"`**: values are serialized as a JSON object. A downstream Code node or Parameter Extractor can `JSON.parse` it (or pattern-match it) to pull out each field.
* **Unset (or any other value)**: values are sent as plain text, one `name: value` per line. Easier for an LLM to read.

For example:

    ```html theme={null}
    
      <label for="username">Username:</label>
      <input type="text" name="username" placeholder="Please enter" />
      <label for="password">Password:</label>
      <input type="password" name="password" placeholder="Please enter" />
      <label for="content">Content:</label>
      <textarea name="content"></textarea>
      <label for="date">Date:</label>
      <input type="date" name="date" />
      <label for="time">Time:</label>
      <input type="time" name="time" />
      <label for="datetime">Datetime:</label>
      <input type="datetime" name="datetime" />
      <label for="select">Select:</label>
      <input type="select" name="select" data-options='["Option A","Option B","Option C"]' />
      <input type="checkbox" name="agreed" data-tip="By checking this means you agreed" />
      <button data-variant="primary">Login</button>
    
    ```

      *[Image: Interactive Form Rendered in Chat Interface]*

##### Supported Tags

| Tag | Attributes                                                                    | Notes                                                                                                                                                                                                                                                                                                                                                                                            |
| :------------- | :---------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ``       | `data-format`                                                                 | Container for form fields.

Set `data-format="json"` to receive submissions as JSON; any other value (or unset) sends plain text.                                                                                                                                                                                                                                                      |
| `<label>`      | `for`                                                                         | Renders the inner text as a field label.

Set `for` to the field's `name` to associate them. Place the `<label>` before its field in the source so it appears above.                                                                                                                                                                                                                   |
| `<input>`      | `type`, `name`, `value`, `placeholder`, `checked`, `data-tip`, `data-options` | See input types below. `name` is required for the field to appear in the submission and must match `[A-Za-z][A-Za-z0-9_-]*`.                                                                                                                                                                                                                                                                     |
| `<textarea>`   | `name`, `placeholder`, `value`                                                | Multi-line text input.                                                                                                                                                                                                                                                                                                                                                                           |
| `<button>`     | `data-variant`, `data-size`                                                   | Submits the form. * Variants: `primary`, `warning`, `secondary`, `secondary-accent`, `ghost`, `ghost-accent`, `tertiary`.
* Sizes: `small`, `medium`, `large`.
Values outside these lists are ignored and the button falls back to the default styling.

Ignores `data-message` and `data-link`, which only apply to [quick-reply buttons](#quick-reply-buttons). |

> **📝 Note:**
>   Do not leave blank lines between tags inside ``. A blank line ends the HTML block during markdown parsing, and any tags after the break will fail to render as form fields.

##### Supported Input Types

| `type` value                          | Renders as                                                           | Submitted as                                                 |
| :------------------------------------ | :------------------------------------------------------------------- | :----------------------------------------------------------- |
| `text`, `password`, `email`, `number` | Single-line input with matching HTML semantics                       | String                                                       |
| `date`                                | Date picker                                                          | ISO date string (e.g., `2026-01-10`)                         |
| `datetime`                            | Date picker with time selection                                      | ISO date-time string (e.g., `2026-01-10T14:30:00.000+08:00`) |
| `time`                                | Time picker                                                          | String (includes a full date prefix, not just the time)      |
| `checkbox`                            | Checkbox followed by the `data-tip` text as a label                  | Boolean (`true` or `false`)                                  |
| `select`                              | Dropdown built from the `data-options` JSON array of strings         | Selected option string                                       |
| `hidden`                              | Renders as an `<input type="hidden">` element; not visible in the UI | String                                                       |

* Any other `type` value renders an "Unsupported tag" fallback in place of the field.

* HTML5 validation attributes such as `required`, `min`, `max`, and `pattern` are not enforced.

* Browsers may autofill `<input type="password">` and `<input type="email">` with saved credentials for the current site; use `<input type="text">` for fields that should not be prefilled.

##### Quick-Reply Buttons

A standalone `<button>` placed outside any `` renders as a clickable button in the chat. Use these to offer canned responses or external links inline with the assistant's message. For example:

```html wrap theme={null}
Would you like to see more options?
<button data-variant="primary" data-message="Yes, show me more">Yes</button> <button data-variant="secondary" data-message="No, that is enough">No</button> <button data-variant="secondary-accent" data-link="https://docs.dify.ai">Read the docs</button>
```

  *[Image: Quick Reply Button]*

| Attribute      | Click behavior                                      |
| :------------- | :-------------------------------------------------- |
| `data-message` | Sends the text as the end user's next chat message. |
| `data-link`    | Opens the URL in a new tab. Must be a valid URL.    |

If both are set, `data-link` takes precedence. A button with neither renders but performs no action when clicked.

Apply `data-variant` and `data-size` for styling, using the same values listed for [form buttons above](#supported-tags).

> **📝 Note:**
>   Unlike form buttons, standalone buttons pass `data-variant` and `data-size` through to the underlying component without validation. An unrecognized value can leave the button rendered as plain text rather than a styled button.
>
>   Use only the values listed above.

#### Output Limits

Template output is limited to **400,000 characters**. This prevents memory issues and ensures reasonable processing times for large template outputs.

#### Tool Node

*Connect to external services and APIs*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/tools

Connect to external services and APIs

Add [Dify tools](https://docs.dify.ai/en/cloud/use-dify/workspace/tools) to your workflows as standalone nodes.

This lets your workflows interact with external services and APIs to access real-time data and perform actions, like web searches, database queries, or content processing.

**To add and configure a tool node**:

1. On the canvas, click **Add Node** > **Tools**, then select an action from an available tool.

2. Optional: If a tool requires authentication, select an existing credential or create a new one.

   > **ℹ️ Info:**
>      To change the default credential, go to **Integrations** > **Tools** > **Tool Plugin**.
>

3. Complete any other required tool settings.

#### Trigger

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/overview

> **ℹ️ Info:**
>   Triggers are available for Workflow applications only.

A trigger is a type of Start node that lets your workflow run automatically on a schedule or in response to events from external systems (such as GitHub, Gmail, or your own internal systems), rather than waiting for active initiation from a user or an API call.

Use triggers to automate repetitive tasks or synchronize data with third-party applications.

A workflow can have multiple triggers running in parallel. You can also build several independent workflows on the same canvas, each starting with its own triggers.

> **ℹ️ Info:**
>   Sandbox accounts are limited to 2 triggers per workflow. Higher trigger counts are available on **[Professional]** and **[Team]**. [Learn more](https://dify.ai/pricing).

The trigger source for each workflow execution is displayed in the **Logs** section.

> **ℹ️ Info:**
>   Trigger events (workflow executions initiated by triggers) are subject to a monthly quota that varies by plan. For per-plan limits, see the [Plan Comparison](https://dify.ai/pricing). The workspace owner and admins can check the remaining quota in **Settings** > **Billing**.

#### Trigger Types

* [Schedule Trigger](https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/schedule-trigger)

  * Runs your workflow at specified times or intervals.

  * Example: Automatically generate a daily sales report every morning at 9 AM and email it to your team.

  > **ℹ️ Info:**
>     Each workflow can have at most one schedule trigger.
>

* [Integration Trigger](https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/plugin-trigger)

  * Runs your workflow when a specific event occurs in an external system, via an event subscription through a trigger integration.

  * Example: Automatically analyze and archive new messages in a specific Slack channel via a subscription to the `New Message in Channel` event through a Slack trigger integration.

* [Webhook Trigger](https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/webhook-trigger)

  * Runs your workflow when a specific event occurs in an external system via a custom webhook.

  * Example: Automatically process new orders in response to an HTTP request containing the order details from your e-commerce platform.

> **💡 Tip:**
>   Both integration triggers and webhook triggers make your workflow *event-driven*. Here's how to choose:
>
>   1. Use an **integration trigger** when a trigger integration is available for your target external system. You can simply subscribe to the supported events.
>
>   2. Use a **webhook trigger** when no trigger integration exists or when you need to capture events not covered by available trigger integrations. In such cases, you'll need to set up custom webhooks in the external system.

#### Enable or Disable Triggers

In the **Quick Settings** side menu, you can enable or disable published triggers. Disabled triggers do not initiate workflow execution.

> **📝 Note:**
>   Only published triggers appear in **Quick Settings**. If you don't see an added trigger listed, ensure it has been published first.

  *[Image: Enable or Disable Published Triggers]*

#### Test Multiple Triggers

When a workflow has multiple triggers, you can click **Test Run** > **Run all triggers** to test them at once. The first trigger that activates will initiate the workflow, and the others will then be ignored.

After you click **Run all triggers**:

* Schedule triggers will run at the next scheduled execution time.

* Integration triggers will listen for subscribed events.

* Webhook triggers will listen for external HTTP requests.

#### Integration Trigger

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/plugin-trigger

> **ℹ️ Info:**
>   Triggers are available for Workflow applications only.

An Integration Trigger starts your workflow automatically when a specific event occurs in an external system. You subscribe to those events through an integration, then add the matching trigger to your workflow.

For example, after installing a GitHub trigger integration, you can subscribe to events such as `Pull Request`, `Push`, and `Issue`. Subscribe to `Pull Request` and add its trigger, and the workflow runs whenever someone opens a pull request in the chosen repository.

#### Add and Configure an Integration Trigger

1. On the workflow canvas, right-click and select **Add Node** > **Start**, then choose the integration trigger event you want to start the workflow. To find more integrations, search the [Marketplace](https://marketplace.dify.ai/?language=en-US\&category=trigger).

   > **💡 Tip:**
>      * If no integration exists for your target system, [request one](https://github.com/langgenius/dify-plugins/issues/new?template=plugin_request.yaml), [build one yourself](https://docs.dify.ai/en/develop-plugin/dev-guides-and-walkthroughs/trigger-plugin), or use a [Webhook Trigger](https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/webhook-trigger) instead.
>      * A workflow can have multiple Integration Triggers. If their branches share downstream nodes, add a [Variable Aggregator](https://docs.dify.ai/en/cloud/use-dify/nodes/variable-aggregator) to converge them.
>

2. Select an existing subscription or [create a new one](https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/plugin-trigger#create-a-subscription). The trigger needs a subscription to receive events.

3. Configure any other required settings.

> **ℹ️ Info:**
>   The output variables of an integration trigger are defined by the integration and can't be modified.

#### Create a Subscription

A subscription is a webhook that listens for events from an external system. Each integration supports up to 10 subscriptions per workspace.

**What is a webhook?:**

  A webhook lets one system send real-time data to another. When an event occurs, the source system packages the details into an HTTP request and sends it to a URL the destination system provides.

Dify supports two ways to create a subscription, depending on what the integration supports.

* **Automatic**: You pick the events to subscribe to, and Dify creates the webhook in the external system for you. This requires prior authorization, through OAuth or an API key, so Dify can set it up on your behalf.
* **Manual**: You create the webhook yourself using the callback URL Dify provides. No authorization needed.

  **OAuth (Automatic):**

    On Dify Cloud, many popular trigger plugins are pre-configured with default OAuth clients, so you can authorize in one click without registering your own OAuth application. To use your own OAuth application instead, choose **Custom**.

    **Default**

    1. Select **Create with OAuth** > **Default**, then click **Save and Authorize**.
    2. On the authorization page that opens, grant Dify access.
    3. Name the subscription, select the events to subscribe to, and configure any other required settings.
       > **💡 Tip:**
>          Subscribe to all available events. A trigger only fires for events its subscription covers, so a broad subscription can be reused by any trigger you add later instead of creating new ones.
>

    4. Click **Create**.

    **Custom**

    1. Select **Create with OAuth** > **Custom**.
    2. In the external system, create an OAuth application using the callback URL Dify provides.
    3. Back in Dify, enter the application's client ID and client secret, then click **Save and Authorize**.
       > **ℹ️ Info:**
> Once saved, the same credentials can be reused for future subscriptions.

    4. Name the subscription, select the events to subscribe to, and configure any other required settings.
       > **💡 Tip:**
>          Subscribe to all available events. A trigger only fires for events its subscription covers, so a broad subscription can be reused by any trigger you add later instead of creating new ones.
>

    5. Click **Create**.

  **API Key (Automatic):**

    1. Select **Create with API Key**.
    2. Enter the required authentication details, then click **Verify**.
    3. Name the subscription, select the events to subscribe to, and configure any other required settings.
       > **💡 Tip:**
>          Subscribe to all available events. A trigger only fires for events its subscription covers, so a broad subscription can be reused by any trigger you add later instead of creating new ones.
>

    4. Click **Create**.

  **Paste URL to create a new subscription (Manual):**

    1. Select **Paste URL to create a new subscription**.
    2. Name the subscription and use the callback URL Dify provides to create a webhook in the external system.
    3. (Optional) Test it: trigger a subscribed event, then check the **Request Logs** at the bottom of the **Manual Setup** page for the received request and Dify's response.

         *[Image: Request Logs]*

    4. Click **Create**.

#### Manage Subscriptions

Manage an integration's subscriptions from **Integrations** > **Trigger**. Open the integration to see its subscriptions, including how many workflows use each one, and to edit or delete them.

#### Test an Integration Trigger

To test an unpublished trigger, first click **Run this step** or test-run the whole workflow. This puts the trigger into a listening state so it can capture subscribed events; otherwise events are ignored even when they occur.

#### Schedule Trigger

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/schedule-trigger

> **ℹ️ Info:**
>   * Triggers are available for Workflow applications only.
>
>   * Each workflow can have at most one schedule trigger.

Schedule triggers enable your workflow to run at specified times or intervals. They are ideal for recurring tasks like generating daily reports or sending scheduled notifications.

#### Add a Schedule Trigger

On the workflow canvas, right-click and select **Add Node** > **Start** > **Schedule Trigger**.

#### Configure a Schedule Trigger

You can configure the schedule using either the default visual picker or a cron expression.

After configuration, you can see the next 5 scheduled execution times.

> **ℹ️ Info:**
>   Schedule triggers do not produce output variables, but they update the system variable `sys.timestamp` (the start time of each workflow execution) each time they initiate the workflow.

##### With the Visual Picker

Use this for simple hourly, daily, weekly, or monthly schedules. For weekly and monthly frequencies, you can select multiple days or dates.

##### With a Cron Expression

Use this for more complex and precise timing patterns, such as every 15 minutes from 9 AM to 5 PM on weekdays.

> **💡 Tip:**
>   You can use LLMs to generate cron expressions.

###### Standard Format

A cron expression is a string that defines the schedule for executing your workflow. It consists of five fields separated by spaces, each representing a different time unit.

> **📝 Note:**
>   Ensure that there is a single space between each field.

```
* * * * *
| | | | |
| | | | |── Day of week (0-7 or SUN-SAT, where both 0 and 7 = Sunday)
| | | |──── Month (1-12 or JAN-DEC)
| | |────── Day of month (1-31)
| |──────── Hour (0-23)
|────────── Minute (0-59)
```

> **ℹ️ Info:**
>   When both the **day-of-month** and **day-of-week** fields are specified, the trigger activates on dates that match *either* field.
>
>   For example, `1 2 3 4 4` will trigger your workflow on the 3rd of April *and* every Thursday in April, not just on Thursdays that fall on the 3rd.

###### Special Characters

| Character | Description                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                                |
| :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `*`       | Means "every".                                                                                                                                                                                                                                                                                               | `*` in the **hour** field means "every hour".                                                                                                                                                                                          |
| `,`       | Separates multiple values.                                                                                                                                                                                                                                                                                   | `1,3,5` in the **day-of-week** field means "Monday, Wednesday, and Friday".                                                                                                                                                            |
| `-`       | Defines a range of values.                                                                                                                                                                                                                                                                                   | `9-17` in the **hour** field means "from 9 AM to 5 PM".                                                                                                                                                                                |
| `/`       | Specifies step values.                                                                                                                                                                                                                                                                                       | `*/15` in the **minute** field means "every 15 minutes".                                                                                                                                                                               |
| `L`       | Means "the last". 

In the **day-of-month** field, means "the last day of the month".

In the **day-of-week** field:* When used alone, means "the last day of the week".
* When combined with a number, means "the last occurrence of that weekday in the month".
 | `L` in the **day-of-month** field means "Jan 31, April 30, or Feb 28 in a non-leap year".

`L` in the **day-of-week** field means Sunday.

`5L` in the **day-of-week** field means "the last Friday of the month". |
| `?`       | Means "any" or "no specific value".

If you specify a value for the **day-of-week** field, you can use `?` for the **day-of-month** field to ignore it, and vice versa.

Not required, because `*` works as well.                                                                        | To run a task every Monday, it's more precise to set the **day-of-month** field to `?` instead of `*`.                                                                                                                                 |

###### Predefined Expressions

* `@yearly`: Run once a year at 12 AM on January 1.
* `@monthly`: Run once a month at 12 AM on the first day of the month.
* `@weekly`: Run once a week at 12 AM on Sunday.
* `@daily`: Run once a day at 12 AM.
* `@hourly`: Run at the beginning of every hour.

###### Examples

| Schedule                                | Cron Expression                    |
| :-------------------------------------- | :--------------------------------- |
| Weekdays at 9 AM                        | `0 9 * * MON-FRI` or `0 9 * * 1-5` |
| Every Wednesday at 2:30 PM              | `30 14 * * WED`                    |
| Every Sunday at 12 AM                   | `0 0 * * 0`                        |
| Every 2 hours on Tuesday                | `0 */2 * * 2`                      |
| The first day of every month at 12 AM   | `0 0 1 * *`                        |
| At 12 PM on January 1 and June 1        | `0 12 1 JAN,JUN *`                 |
| The last day of every month at 5 PM     | `0 17 L * *`                       |
| The last Friday of every month at 10 PM | `0 22 * * 5L`                      |

#### Test a Schedule Trigger

* **Run this step**: The schedule trigger runs immediately, ignoring the configured schedule.

* **Test Run**: The schedule trigger waits for its next scheduled execution time.

#### Webhook Trigger

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/webhook-trigger

> **ℹ️ Info:**
>   Triggers are available for Workflow applications only.

A webhook allows one system to automatically send real-time data to another. When a certain event occurs, the source system packages the event details into an HTTP request and sends it to a designated URL provided by the destination system.

Following the same mechanism, webhook triggers enable your workflow to run in response to third-party events. Here's how you work with it:

1. When you add a webhook trigger to your workflow, Dify generates a unique webhook URL that listens for external HTTP requests. This URL is hosted on the Dify Cloud domain and is publicly reachable by external systems.

2. You use this URL to create a webhook subscribing to the events you want to monitor in an external system. Then you configure the webhook trigger to define how it processes incoming requests and extracts request data.

   > **📝 Note:**
>      For testing purposes, always use the test webhook URL to keep test data separate from production data.
>
>
>        *[Image: Test Webhook URL]*
>
>

3. When a subscribed event occurs, the external system sends an HTTP request with the event data to that provided webhook URL. Once the request is received and processed successfully, your workflow is triggered, and the specified event data is extracted into variables that can be referenced by downstream nodes.

> **💡 Tip:**
>   If there's a ready-made trigger integration for your target external system, consider using an [Integration Trigger](https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/plugin-trigger) instead.

#### Add a Webhook Trigger

On the workflow canvas, right-click and select **Add Node** > **Start** > **Webhook Trigger**.

> **💡 Tip:**
>   A workflow can have multiple webhook triggers. If these trigger branches share identical downstream nodes, add a [Variable Aggregator](https://docs.dify.ai/en/cloud/use-dify/nodes/variable-aggregator) to converge them and avoid duplicating those nodes on each branch.

#### Configure a Webhook Trigger

You can define how a webhook trigger handles incoming HTTP requests, including:

* The expected HTTP method for the webhook URL

* The request's content-type

* The data you wish to extract from the request

* The response sent back to the external system when your workflow is successfully triggered

> **📝 Note:**
>   To test an unpublished webhook trigger, make sure to click **Run this step** or test-run the entire workflow first. This puts the trigger into a listening state so that it can receive external requests. Otherwise, no request will be captured.

##### HTTP Method

To ensure the incoming request can be received successfully, you need to specify which HTTP method the webhook URL accepts.

The method you select here must match the one used by the external system to send requests; otherwise, the requests will be rejected.

> **💡 Tip:**
>   You can typically find this information in the external system's webhook documentation or setup interface.

##### Content-Type

To ensure the request body can be properly parsed and the data you need extracted, you need to specify the expected content type of the incoming request.

The content-type you select here must match the content type of the request sent from the external system; otherwise, the request will be rejected.

##### Query Parameters, Header Parameters, and Request Body Parameters

You can extract specific data from the query parameters, headers, and body of the incoming request. **Each extracted parameter becomes an output variable that can be used in your workflow.**

Some external systems provide a delivery log for each request, where you can view all the data included in the request and decide which parameters to extract.

Alternatively, you can send a test request to the webhook trigger and check the received request data in its last run logs:

1. Create a webhook in the external system using the provided test webhook URL.

2. Set the correct HTTP method and content-type in the trigger.

3. Click the **Run this step** icon. The trigger will start listening for external requests.

4. Trigger the subscribed event in the external system so it sends an HTTP request to the provided webhook URL.

5. Go to the trigger's **Last Run** tab and check the received request data in **Input**.

> **📝 Note:**
>   The variable name you define in the trigger must match the key name of the corresponding parameter in the request.

  **Query Parameters:**

    * Parameters in key-value pairs added to the webhook URL (after `?`) by external systems when sending requests, each pair separated by `&`.

    * Typically simple, non-sensitive identifiers or filter data about the event.

    * Example: From the URL `{webhook url}?userID=u-456&source=email`, you can extract the `userID` (`u-456`) or the `source` (`email`).

  **Header Parameters:**

    * Request metadata included in the request headers.

    * Technical information needed for processing the request, such as an authentication token or the request body's data format.

    * Example: From headers like `Authorization: Bearer sk-abc... `and `Content-Type: application/json`, you can extract the authorization information (`Bearer sk-abc...`) or the content-type (`application/json`).

  **Request Body Parameters:**

    * The main payload where the core event data is sent, such as a customer profile, order details, or the content of a Slack message.

    * Example: From the following request body, you can extract the `customerName` (`Alex`), the list of items, or the `isPriority` status (`true`).

    ```json theme={null}
    "customerName": "Alex",
    "items":
    [
            { "sku": "A42", "quantity": 2 },
            { "sku": "B12", "quantity": 1 }
    ],
    "isPriority": true
    ```

    > **ℹ️ Info:**
>       The content-type determines which data types can be extracted from the request body.
>
>       | Content-Type                      | `String` | `Number` | `Boolean` | `Object` | `File` | `Array[String]` | `Array[Number]` | `Array[Boolean]` | `Array[Object]` | `Array[File]` |
>       | :-------------------------------- | :------: | :------: | :-------: | :------: | :----: | :-------------: | :-------------: | :--------------: | :-------------: | :-----------: |
>       | application/json                  |     ✅    |     ✅    |     ✅     |     ✅    |    ❌   |        ✅        |        ✅        |         ✅        |        ✅        |       ❌       |
>       | application/x-www-form-urlencoded |     ✅    |     ✅    |     ✅     |     ❌    |    ❌   |        ✅        |        ✅        |         ✅        |        ❌        |       ❌       |
>       | multipart/form-data               |     ✅    |     ✅    |     ✅     |     ❌    |    ✅   |        ✅        |        ✅        |         ✅        |        ❌        |       ✅       |
>       | text/plain                        |     ✅    |     ✅    |     ✅     |     ❌    |    ❌   |        ❌        |        ❌        |         ❌        |        ❌        |       ❌       |
>

**Parameter Settings**

For each parameter to be extracted, you can specify the following:

* **Variable Name**: The key name of the parameter in the incoming request (e.g., `userID` in `userID=u-456`).

  > **📝 Note:**
>     For header parameters, any hyphen (`-`) in the variable name will be automatically converted to an underscore (`_`) in the output variable.
>

* **Data Type**: The expected data format. Available for query and request body parameters only, as header parameters are always treated as strings.

* **Required**: Whether the parameter is required for your workflow to execute properly. If any required parameter is missing from an incoming request, your workflow will not be triggered.

##### Response

When your workflow is successfully triggered by an external HTTP request, a default `200 OK` response is sent back to the external system.

If the external system requires a specific success response format, you can customize the status code and response body. The default one will be overridden.

* **Status Code**: Supports any status code in the range [200, 399].

* **Response Body**: Supports JSON or plain text.

> **📝 Note:**
>   In the returned response body, non-JSON content will be automatically converted to JSON.
>
>   For example, `OK` will be wrapped as `"message": "OK"`.

> **ℹ️ Info:**
>   The following error responses are system-defined and cannot be customized. Error details can be found in the response body.
>
>   * 400 Bad Request
>   * 404 Not Found
>   * 413 Payload Too Large
>   * 500 Internal Server Error

#### Test a Webhook Trigger

To test an unpublished webhook trigger, you must first click **Run this step** or test-run the entire workflow. This puts the trigger into a listening state so that it can receive external requests. Otherwise, incoming requests will not be captured.

#### User Input

*Collects user inputs to start Workflow and Chatflow applications*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/user-input

Collects user inputs to start Workflow and Chatflow applications

The User Input node allows you to define what to collect from end users as inputs for your applications.

Applications that start with this node run *on demand* and can be initiated by direct user interaction or API calls.

You can also publish these applications as standalone web apps or MCP servers, expose them through backend service APIs, or use them as tools in other Dify applications.

> **ℹ️ Info:**
>   Each application canvas can contain only one User Input node.

#### Input Variable

##### Preset

Preset input variables are system-defined and available by default.

* `userinput.files`: Files uploaded by end users when they run the application.

  > **📝 Note:**
>     For Workflow applications, this preset variable has been considered *legacy* and kept only for backward compatibility.
>
>     We recommend using a [custom file input field](#file-input) instead to collect user files.
>

* `userinput.query` (for chatflows only): The text message automatically captured from the user's latest chat turn.

##### Custom

You can configure custom input fields in a User Input node to collect different kinds of user input. Each field becomes a variable that can be referenced by downstream nodes.

> **ℹ️ Info:**
>   **Label Name** is displayed to your end users.

> **💡 Tip:**
>   If a field's value is something you already know (like a product identifier or tenant ID) and doesn't have to come from end users, mark it as **Hidden & Pre-Filled** and supply it yourself. See [Hide and Pre-Fill Input Fields](#hide-and-pre-fill-input-fields) for details.

###### Text Input

  **Short Text:**

    Accepts up to 256 characters. Use it for names, email addresses, titles, or any brief text input that fits on a single line.

  **Paragraph:**

    Allows long-form text without length restrictions. It gives users a multi-line text area for detailed responses or descriptions.

###### Structured Input

  **Select:**

    Displays a dropdown menu with predefined options. Users can choose only from listed options, ensuring data consistency and preventing invalid inputs.

  **Number:**

    Restricts input to numerical values only—ideal for quantities, ratings, IDs, or any data requiring mathematical processing.

  **Checkbox:**

    Provides a simple yes/no option. When a user checks the box, the output is `true`; otherwise, it's `false`. Use it for confirmations or any case that requires a binary choice.

  **JSON Code:**

    Accepts data in JSON object format, ideal for passing complex, nested data structures into your application.

    You can optionally define a JSON schema to validate the input and guide end users on the expected structure and validation requirements. This also allows you to reference individual properties of the object in other nodes.

###### File Input

  **Single File:**

    Allows users to upload one file of any supported type, either from their device or via a file URL. The uploaded file is available as a variable containing file metadata (name, size, type, etc.).

  **File List:**

    Supports multiple file uploads at once. It's useful for handling batches of documents, images, or other files together.

    > **💡 Tip:**
>       Use a List Operator node to filter, sort, or extract specific files from the uploaded file list for further processing.
>

**File Processing**

Since the User Input node only collects files—it does not read or parse their content—uploaded files must be processed appropriately by subsequent nodes. For example:

* Document files can be routed to a Doc Extractor node for text extraction so that LLMs can understand their content.

* Images can be sent to LLM nodes with vision capabilities or specialized image processing tool nodes.

* Structured data files such as CSV or JSON can be processed with Code nodes to parse and transform the data.

> **💡 Tip:**
>   When users upload multiple files with mixed types (e.g., images and documents), you can use a List Operator node to separate them by file type before routing them to different processing branches.

#### Hide and Pre-Fill Input Fields

Sometimes the workflow needs an input you already know, and asking end users to type it would be friction. Mark such a field as **Hidden & Pre-Filled**: you supply the value, end users never see the field, and the workflow still receives it.

Imagine your company runs landing pages for many different products, each featuring an AI chatbot. The workflow behind every chatbot is essentially the same; only the product identifier differs.

Rather than maintain a separate workflow per product, you keep just one (with a hidden `productName` field) and pre-fill a different value on each landing page. End users perceive each page as having its own product-specific chatbot, but behind the scenes, every page passes a different `productName` into the same workflow.

> **⚠️ Warning:**
>   Hidden fields are **not secret**. Values travel in the URL query string and are visible in the browser address bar, browser history, and network traffic. For credentials and API keys, use [Environment Variables](https://docs.dify.ai/en/learn/key-concepts#variables) instead.

> **ℹ️ Info:**
>   Single File and File List fields do not support this feature.

  1. **Enable the Feature**
        1. In the **Edit Input Field** window, uncheck **Required** if it's checked. These two options are mutually exclusive.
        2. Check **Hidden & Pre-Filled**. Optionally set a default value as a fallback when no value is pre-filled at runtime.

        Hidden fields still appear in the **Preview** panel so you can test the flow without publishing.

  1. **Pre-Fill the Field**
        1. Publish your app.
        2. Choose the method that fits how your end users reach the app.

             **Shareable Link:**

               Use this when end users open the WebApp directly from its link.

               1. In the app's publishing panel, within the **Web App** section, click the gear icon next to **Launch**.

                    *[Image: Hidden Fields Pre-Fill Icon]*

               2. Fill in the hidden fields and click **Launch**. The WebApp opens with your values applied as URL query parameters; copy the URL from the address bar to share.

               **To generate many links with different values**, use the same pattern to write more yourself, or have a system fill in the values automatically:

               ```text wrap theme={null}
               {WEBAPP_URL}?{VARIABLE_NAME}={VALUE}&{VARIABLE_NAME}={VALUE}

               # Example: https://udify.app/chat/abc123?productName=Acme&region=us-east
               ```

               > **📝 Note:**
>                  URL-encode any values that contain spaces or special characters (for example, `Acme Corp` becomes `Acme%20Corp`).
>

               **Example: A CRM Auto-Fills the Customer ID:**

                 A support team using a CRM can add `?customerId={{customer.id}}` to the end of the WebApp URL in their ticket-response templates.

                 The CRM substitutes the real customer ID when the rep sends the link, so the chatbot knows which customer it's talking to without having to ask.

             **Embed on Your Site:**

               Use this when the app is embedded as an iframe or script on your site.

                 **Same Value for Every Visitor:**

                   Use this when every visitor should receive the same values (a site-wide region, the embedded page's product ID, etc.).

                   1. In the app's publishing panel, within the **Web App** section, click **Embedded** > **Pre-Fill Hidden Fields**.

                        *[Image: Embedded Icon]*

                   2. Fill in the hidden fields. Entered values are baked into the iframe URL and the `inputs` object of the script snippet.

                 **Different Value Per Visitor:**

                   Use this when each visitor should receive their own values (the logged-in user's ID, the page they're on, etc.).

                   In the embed snippet on your site, set each hidden field as a key in the `inputs` object of `window.difyChatbotConfig`. Each value is computed at render time from your site's context, so every visitor gets their own.

                   ```html theme={null}
                   <script>
                     window.difyChatbotConfig = {
                       token: 'YOUR_TOKEN',
                       inputs: {
                         productName: getCurrentProduct(),    // from the current page
                         tenantId: getCurrentTenant(),        // from your auth system
                       },
                     };
                   </script>
                   ```

#### Variable Aggregator

*Converge exclusive workflow branches into a single output*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/variable-aggregator

Converge exclusive workflow branches into a single output

Use the Variable Aggregator node to converge **exclusive** workflow branches into a single output, so you only need to define downstream processing once.

Nodes like If/Else and Question Classifier create exclusive branches—only one path executes per run. When these branches produce the same type of output, you would normally duplicate downstream nodes on every branch.

The Variable Aggregator eliminates this duplication. It provides a single output variable for downstream nodes to reference, regardless of which branch ran.

  *[Image: Without Variable Aggregator]*

  *[Image: With Variable Aggregator]*

> **📝 Note:**
>   The Variable Aggregator is designed for exclusive branches where **only one path runs at a time**. It does not combine outputs from multiple branches that execute in parallel.
>
>   To merge results from parallel branches, use a [Code](https://docs.dify.ai/en/cloud/use-dify/nodes/code) or [Template](https://docs.dify.ai/en/cloud/use-dify/nodes/template) node.

#### Select the Variables to Converge

From each branch, add variables that need the same downstream processing. All variables must share the same data type.

Supported types: `string`, `number`, `object`, `boolean`, `array`, `file`.

The node outputs whichever variable has a value at runtime. Since only one branch executes, only one variable will have a value, and that value becomes the node's output.

#### Converge Multiple Sets of Variables

When you have multiple sets of variables that each need to be converged separately, enable **Aggregation Group** to create groups within a single Variable Aggregator.

Each group converges its own set of variables and produces a separate output.

#### Variable Assigner

*Manage persistent conversation variables in Chatflow applications*

**Source:** https://docs.dify.ai/en/cloud/use-dify/nodes/variable-assigner

Manage persistent conversation variables in Chatflow applications

The Variable Assigner node manages persistent data in Chatflow applications by writing to conversation variables (Understand the different types of variables [here](https://docs.dify.ai/en/learn/key-concepts#variables)). Unlike regular workflow variables that reset with each execution, conversation variables persist throughout an entire chat session.

  ![Variable Assigner Node Configuration](https://assets-docs.dify.ai/2024/11/83d0b9ef4c1fad947b124398d472d656.png)

#### Conversation Variables vs Workflow Variables

**Workflow Variables** exist only during a single workflow execution and reset when the workflow completes.

**Conversation Variables** persist across multiple conversation turns within the same chat session, enabling stateful interactions and contextual memory.

This persistence enables contextual conversations, user personalization, stateful workflows, and progress tracking across multiple user interactions.

#### Configuration

Configure which conversation variables to update and specify their source data. You can assign multiple variables in a single node.

  ![Variable Assignment Configuration Interface](https://assets-docs.dify.ai/2024/11/ee15dee864107ba5a93b459ebdfc32cf.png)

**Variable** - Select the conversation variable to write to

**Set Variable** - Choose the source data from upstream workflow nodes

**Operation Mode** - Determine how to update the variable (overwrite, append, clear, etc.)

#### Operation Modes

Different variable types support different operations based on their data structure:

  **String:**

    * **Overwrite** - Replace with another string variable

    * **Clear** - Remove the current value

    * **Set** - Manually assign a fixed value

  **Number:**

    * **Overwrite** - Replace with another number variable

    * **Clear** - Remove the current value

    * **Set** - Manually assign a fixed value

    * **Arithmetic** - Add, subtract, multiply, or divide the current value by another number

  **Boolean:**

    * **Overwrite** - Replace with another boolean variable

    * **Clear** - Remove the current value

    * **Set** - Manually assign a fixed value

  **Object:**

    * **Overwrite** - Replace with another object variable

    * **Clear** - Remove the current value

    * **Set** - Manually define the object structure and values

  **Array:**

    * **Overwrite** - Replace with another array variable of the same type

    * **Clear** - Remove all elements from the array

    * **Append** - Add a single element to the end of the array

    * **Extend** - Add all elements from another array of the same type

    * **Remove First/Last** - Remove the first or last element from the array

    > **💡 Tip:**
>       Array operations are particularly powerful for building memory systems, checklists, and conversation histories that grow over time.
>

#### Common Implementation Patterns

##### Smart Memory System

Build chatbots that automatically detect and store important information from conversations:

  ![Smart Memory System Workflow](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/8d0492814b1515f50e87b2900ff400db.png)

The system analyzes user input for memorable facts, extracts structured information, and appends it to a persistent memories array for future reference in conversations.

##### User Preferences Storage

Store user preferences like language settings, notification preferences, or display options:

  ![User Preferences Management](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/1867d608a7d009431b73377ed65b427b.png)

Use **Overwrite** mode to capture initial preferences from user input, then reference them in all subsequent LLM responses for personalized interactions.

##### Progressive Checklists

Build guided workflows that track completion status across multiple conversation turns:

  ![Progressive Checklist Implementation](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/c4362b01298b12e7d6fcd9e798f3165a.png)

Use array conversation variables to track completed items. The Variable Assigner updates the checklist each turn, while the LLM references it to guide users through remaining tasks.

### Publish

#### Overview

*Get your Dify applications into users' hands with web apps, APIs, embeds, and integrations*

**Source:** https://docs.dify.ai/en/cloud/use-dify/publish/README

Get your Dify applications into users' hands with web apps, APIs, embeds, and integrations

  *[Image: Publish Methods]*

You've built something great in Dify. Now let's get it to your users. Every Dify application becomes available in multiple ways automatically—choose what works best for your situation.

#### Start with Web Apps

Your fastest path to sharing is through web apps. These are generated automatically when you create any application and work immediately without setup.

  1. **Hit Publish**
        Click "Publish" in your app to activate the latest version.

  1. **Copy the URL**
        Find your web app link in the publish section.

  1. **Share immediately**
        Send the link to users—they can start using your app right away.

> **💡 Tip:**
>   Web apps work on any device and automatically adapt to screen sizes. No app store approvals or installation required.

#### Publishing Options

  - **[Web Apps](https://docs.dify.ai/en/cloud/use-dify/publish/webapp/chatflow-webapp)** — Instant, shareable applications. Perfect for testing ideas or serving end users directly.

  - **[API Integration](https://docs.dify.ai/en/api-reference/guides/get-started)** — Build AI into your existing products. Full control over user experience and data flow.

  - **[Embed on Websites](https://docs.dify.ai/en/cloud/use-dify/publish/webapp/embedding-in-websites)** — Deploy your web app as chat widgets or inline frames on any website.

  - **[MCP Server](https://docs.dify.ai/en/cloud/use-dify/publish/publish-mcp)** — Connect to AI tools like Claude Desktop and Cursor. Great for development workflows.

#### How Publishing Works

When you publish an app, Dify creates a web app and API endpoint with your latest configuration:

* **Web apps** update immediately with new features and responses
* **API endpoints** serve the latest model and workflow configurations
* **Website embeds** (which display your web app) automatically reflect all changes
* **MCP servers** provide access to current app capabilities

> **⚠️ Warning:**
>   Publishing replaces your live app with the current configuration. Users will immediately see changes in their next interaction.

#### Choose Your Approach

  **I want immediate user feedback:**

    Use **Web Apps**. Share a link and start collecting feedback within minutes. Perfect for validating ideas or serving non-technical users.

  **I'm building a product:**

    Use **API Integration**. You control the interface, user authentication, and data handling. Your app becomes part of your product ecosystem.

  **I have an existing website:**

    Use **Embed on Websites**. Display your web app as a chat widget or inline frame on your current site. Works with any website technology.

  **I want to extend AI tools:**

    Use **MCP Server**. Make your app available to Claude Desktop, Cursor, and other AI development environments as a native tool.

#### Publishing Best Practices

Before you share your app, ensure you've configured these settings:

* **App description** - Helps users understand what your app does
* **Icon and branding** - Makes your app recognizable and professional
* **Access controls** - Decide if your app should be public or require authentication
* **Rate limits** - Protect your app from overuse (especially important for API access)

> **✅ Check:**
>   All publishing methods use the same app configuration. Set it once, publish everywhere.

#### MCP Server

*Expose your Dify applications as MCP servers for integration with Claude Desktop, Cursor, and other AI development tools*

**Source:** https://docs.dify.ai/en/cloud/use-dify/publish/publish-mcp

Expose your Dify applications as MCP servers for integration with Claude Desktop, Cursor, and other AI development tools

Dify now supports exposing your applications as [MCP](https://modelcontextprotocol.io/docs/getting-started/intro) (Model Context Protocol) servers, enabling seamless integration with AI assistants like Claude Desktop and development environments like Cursor. This allows these tools to directly interact with your Dify apps as if they were native extensions.

> **📝 Note:**
>   If you're looking to use MCP tools within Dify workflows & agents, see [here](https://docs.dify.ai/en/cloud/use-dify/workspace/tools#mcp).

#### Configure Your Dify App as an MCP Server

Navigate to your application's configuration interface in Dify, you'll find an MCP Server configuration module. The feature is disabled by default. When you toggle it on, Dify generates an unique MCP Server address for your application. This address serves as the connection point for external tools.

> **🚨 Danger:**
>   Your MCP Server URL contains authentication credentials, so treat it like an API key. If you suspect it's been compromised, use the regenerate button to create a new URL. The old one will immediately stop working.

  *[Image: App Publish MCP Panel]*

#### Integration with Claude Desktop

To connect your Dify app to Claude Desktop, you'll need to add a Claude integration. Go to your Claude Profile > Settings > Integrations > Add integration. Replace the Integration URL with your Dify app's Server URL.

#### Integration with Cursor

For Cursor, create or edit the `.cursor/mcp.json` file in your project root:

```json theme={null}
{
  "mcpServers": {
    "your-server-name": {
      "url": "your-server-url"
    }
  }
}
```

Simply replace the URL with your Dify app's MCP Server address. Cursor will automatically detect this configuration and make your Dify app available as a tool. You can add multiple Dify apps by including additional entries in the `mcpServers` object.

#### Practical Considerations

* Descriptiveness

  When designing descriptions for your tool and its input parameters, think about how an AI would interpret them. Clear, specific descriptions lead to better invocations. Instead of "input data," specify "JSON object containing user profile with required fields: name, email, preferences."
* Latency

  The MCP protocol handles the communication layer, but your Dify app's performance still matters. If your app typically takes 30 seconds to process, that latency will be felt in the client application. Consider adding progress indicators or breaking complex workflows into smaller, faster operations.

#### Publish Apps to Marketplace

*Publish your apps to Dify Marketplace and share them with the world*

**Source:** https://docs.dify.ai/en/cloud/use-dify/publish/publish-to-marketplace

Publish your apps to Dify Marketplace and share them with the world

Publish your apps as templates to Dify Marketplace, where other Dify users can discover and use them.

#### Submit a Template

To publish a template, submit it through the [Creator Center](https://creators.dify.ai). After you submit, the template enters **Pending** status while we review it. Once approved, it's published to Marketplace.

While a template is **Pending**, you can withdraw it at any time. Withdrawing returns it to **Draft**, where you can edit any part of the template before resubmitting.

> **📝 Note:**
>   Before submission:
>
>   * Make sure all plugins used in the app are **installed directly from Marketplace**.
>   * Run the app at least once to confirm it works as expected.

##### Submit as Individual or Organization

You can submit templates under your personal account or an organization.

* **Individual**: For independent creators. When you first log in to the Creator Center, you're signed in with your personal account by default.

* **Organization**: For teams that want to build and manage templates together. To get started, click your avatar in the top-left corner and click **Create an organization**, then invite members to collaborate.

You can switch between your personal account and organizations anytime.

##### Submission Methods

  **From Dify Studio:**

    In your app, click **Publish** > **Publish Update**, then click **Publish to Marketplace**.

    This takes you to the Creator Center with your app file automatically uploaded. Fill in the template details and submit for review.

  **In the Creator Center:**

    Export your app, then go to the Creator Center and upload the export file. Fill in the template details and submit for review.

#### Update a Published Template

How you update a published template depends on what you want to change.

* **To change anything inside the app** (its prompts, tools, model settings, and so on)

  Submit the updated app as a new template. This creates a separate listing rather than replacing the original, so you can manually unpublish the old version once the new one is published.

* **To change only the listing** (such as the Overview or Setup steps)

  Unpublish the template to take it off Marketplace and return it to **Draft**. Make your edits, then resubmit for review.

#### Template Writing Guidelines

##### Language Requirements

Keep the template library consistent and searchable.

**The following fields must be written in English**:

* Template name
* Overview
* Setup steps

**Inside the app, you can use any language (e.g. Chinese) for**:

* Node names
* Prompts / system messages
* Messages shown to end-users

If your template mainly targets non-English users, you can add a tag in the title. For example, `Stock Investment Analysis Copilot [ZH]`.

##### Template Name & Icon

From the name alone, users should know where it runs and what it does.

* Use a short English phrase, typically 3–7 words.
* Recommended pattern: [Channel / target] + [core task], for example:
  * WeChat Customer Support Bot
  * CSV Data Analyzer with Natural Language
  * Internal Docs Q\&A Assistant
  * GitHub Issue Triage Agent
* Include keywords users might search for: channel names (Slack, WeChat, Email, Notion) and task names (Summarizer, Assistant, Generator, Bot).
* Use an icon that clearly reflects the template's theme and purpose, rather than the default avatar.

##### Categories

Help users discover your template when browsing or filtering by category.

* Select only **1–3** categories that best describe your template.
* Do not check every category just for exposure.

##### Language

Help users discover your template via the language filter.

* Select the language your template is designed for in real usage.
* This refers to the language of the template's use case, input, or output, **not** the title or overview (which must be in English).

##### Overview

In 2–4 English sentences, explain what it does and who it is for.

> **ℹ️ Info:**
> You don't need to list prerequisites, inputs, or outputs here.

**Recommended structure**

1. Sentence 1: **What it does**

   A one-sentence summary of the main function.
2. Sentence 2–3: **Who and when**

   Typical user roles or scenarios (support team, marketers, founders, individual knowledge workers, etc.).

**Example: Description for Stock Investment Analysis Copilot:**

  This template creates a stock investment analysis copilot that uses Yahoo Finance tools to fetch news, analytics, and ticker data for any listed company.

  It helps investors and analysts quickly generate structured research summaries, compare companies, and prepare reports without manually switching between multiple finance websites.

##### Setup Steps

Write Setup steps as a numbered Markdown list (1., 2., 3.), with one short sentence per step, starting with a verb.

A new user should be able to get the template running in a few minutes just by following these steps.

**Writing principles**

1. Follow the real setup order, usually:
   1. Use/import the template
   2. Connect accounts / add API keys
   3. Connect data sources (docs, databases, sheets, etc.)
   4. Optional customization (assistant name, tone, filters)
   5. Activate the workflow and run a test

2. Each step should answer:
   * Where to click in the UI
   * What to configure or fill in

3. Aim for 3–8 steps. Too few feels incomplete; too many feels overwhelming.

**Example: Setup Steps for Stock Investment Analysis Copilot (Yahoo Finance tools):**

  1) Click **Use template** to copy the "Investment Analysis Copilot (Yahoo Finance)" agent into your workspace.

  2) Go to **Integrations** > **Model Provider** and add your LLM API key. For example, OpenAI, Anthropic, or another supported provider.

  3) Open the agent's **Orchestrate** page and make sure the Yahoo Finance tools are enabled in the **Tools** section:

  * `yahoo Analytics`
  * `yahoo News`
  * `yahoo Ticker`

  4. (Optional) Customize the analysis style:
     * In the **INSTRUCTIONS** area, adjust the system prompt to match your target users. For example, tone, report length, preferred language, or risk preference.
     * Update the suggested questions in the **Debug & Preview** panel if you want different example queries.

  5. Click **Publish** to make the agent available, then use the preview panel to test it:
     * Enter a company name or ticker (e.g., `Nvidia`, `AAPL`, `TSLA`).
     * Confirm that the copilot calls the Yahoo Finance tools and returns a structured investment analysis report.

##### Quick Checklist Before You Submit

* The name is a short English phrase that clearly shows where it runs and what it does.
* The overview uses 2–4 English sentences to explain the value and typical use cases.
* Only 1–3 relevant categories are selected.
* Setup steps are a clear numbered list.
* Internal workflow texts and prompts are written in appropriate languages for your target users.

#### Chat Web Apps

*Turn your Chatflow into a fully-featured conversation interface with persistent history and interactive features*

**Source:** https://docs.dify.ai/en/cloud/use-dify/publish/webapp/chatflow-webapp

Turn your Chatflow into a fully-featured conversation interface with persistent history and interactive features

Chat web apps transform your Chatflow into a complete conversation experience. Users get persistent chat sessions, smart interactions, and all the features you've configured—without installing anything.

#### How Chat Apps Work

Your Chatflow automatically becomes a web app when you publish it. The system creates a responsive interface that:

* **Maintains conversation context** across user sessions
* **Inherits all orchestration settings** from your Chatflow configuration
* **Adapts to any screen size** from mobile to desktop
* **Handles user authentication** if you've enabled access controls

> **💡 Tip:**
>   Unlike single-use text generators, chat apps maintain conversation memory and let users build on previous exchanges.

#### Interactive Features

Your web app automatically includes these capabilities based on your Chatflow settings:

  - **Pre-conversation Forms** — Collect context before chatting starts—better than asking mid-conversation

  - **AI Conversation Starters** — Eliminate the blank page problem with helpful opening messages

  - **Smart Follow-ups** — System generates 3 contextual next questions after each response

  - **Voice Input** — Speech-to-text lets users talk instead of type

  - **Source Citations** — References show exactly where information comes from

  - **Response Feedback** — Users can rate responses to help improve your app

#### Pre-conversation Setup

When your Chatflow uses variables, users complete a form before chatting starts. This front-loads context gathering instead of interrupting the conversation flow.

  ![Pre-conversation Variable Form](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/8decae00eeea24622e1f2ef73d4c447e.png)

Here's how the user experience works:

  1. **User lands on your app**
        They see a clean form requesting necessary context information.

  1. **Form completion unlocks chat**
        The "Start Conversation" button activates only after required fields are filled.

  1. **AI has full context**
        The conversation begins with all the background information it needs.

> **⚠️ Warning:**
>   Every form field adds friction. Only ask for information that meaningfully improves responses.

#### Conversation Experience

Once chatting begins, users get an interface designed for natural interaction:

  ![Chat Interface with Response Options](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/5b7a6f950ed8a2ce3a705f362b4813fe.png)

Every AI response includes these actions:

* **Copy button** - One-click copying for easy sharing or note-taking
* **Feedback buttons** - Like/dislike ratings to improve your app over time
* **Follow-up suggestions** - AI generates 3 contextually relevant next questions

#### Session Management

Users can manage multiple conversation threads like modern messaging apps:

  ![Conversation Management Sidebar](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/46372ad4d79a3ea943d43f9434974956.png)

**Conversation Controls**:

* **Start new** - Begin fresh conversations without losing context from previous ones
* **Pin important** - Keep crucial conversations accessible at the top of the list
* **Delete finished** - Clean up conversations that are no longer relevant

> **ℹ️ Info:**
>   Each conversation thread maintains its own memory and context. Users can seamlessly switch between different topics or projects.

#### Conversation Openers

Enable conversation openers to eliminate the intimidating blank chat screen:

  ![AI Conversation Opener Message](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/22e59e509296d25eb85cbd541e161c6d.png)

When users start new conversations, the AI proactively introduces itself and explains its capabilities. This immediately shows users what they can accomplish and increases engagement.

> **💡 Tip:**
>   Conversation openers work especially well for specialized apps where users might not know all available features.

#### Follow-up Questions

The system automatically generates contextual follow-up questions after each AI response:

  ![Follow-up Question Suggestions](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/f88a7ffd777d51299f8b604249c044b3.png)

These suggestions are:

* **Contextually relevant** to the current conversation topic
* **Dynamically generated** based on the AI's response
* **Clickable shortcuts** that help users explore deeper or pivot to related topics

#### Voice Input

Speech-to-text transforms your chat app into a voice-first experience:

  ![Speech-to-text Microphone Button](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/3a64c79792f1166301403f6c44cf4c85.png)

**How it works**:

1. The microphone button appears when you enable speech-to-text in your Chatflow
2. Users click to start recording their question
3. Speech converts to text in real-time as they speak
4. They can edit the text before sending or send immediately

> **⚠️ Warning:**
>   Users must grant microphone permissions in their browser. The app will prompt for this permission when they first try to use voice input.

#### Citations and Attributions

When this feature is enabled, if the AI references content from the knowledge base while answering a user question, the specific knowledge sources will be displayed below the response.

Citations build user trust by providing transparency about information sources. Users can click through to verify details or explore source materials further.

#### Embed Your Web App

*Deploy your published web app on any website through iframes, chat widgets, or custom integrations*

**Source:** https://docs.dify.ai/en/cloud/use-dify/publish/webapp/embedding-in-websites

Deploy your published web app on any website through iframes, chat widgets, or custom integrations

Your published web app can be embedded directly into any website. This isn't a separate publishing method: it's how you deploy the same web app you've already created, just presented within your existing website instead of as a standalone page.

#### How Web App Embedding Works

When you publish an app in Dify, you get a web app URL. You can share this URL directly, or embed the same app into your website using these methods:

  - **Chat Bubble Widget** — Your web app as a floating button that visitors click to open the full interface

  - **Iframe Integration** — Your web app embedded directly in page content, always visible and ready

  - **JavaScript Control** — Advanced embedding with custom styling and behavior control

  - **Responsive Design** — Same web app adapts automatically to any presentation format

> **ℹ️ Info:**
>   All embedding methods use your published web app. Changes to your app configuration automatically apply everywhere it's embedded.

#### Chat Bubble Widget

The chat bubble presents your web app as a floating button. Visitors click it to open your app in an overlay, keeping them on your page while accessing your AI features.

##### Configuration Options

The chat bubble can be customized through the `difyChatbotConfig` object:

```javascript theme={null}
window.difyChatbotConfig = {
    // Required: Your app's token from Dify
    token: 'YOUR_TOKEN',

    // Optional: Environment settings
    isDev: false,
    baseUrl: 'https://udify.app', // Auto-set based on isDev

    // Optional: Visual customization
    containerProps: {
        style: {
            right: '20px',
            bottom: '20px'
        },
        className: 'custom-chat-button'
    },

    // Optional: Interactive behavior
    draggable: false,              // Allow users to drag the button
    dragAxis: 'both',             // 'x', 'y', or 'both'

    // Optional: Pre-fill user context
    inputs: {
        name: "John Doe",          // Variable names from your Dify app
        department: "Support"
    },

    // Optional: System variables for tracking
    systemVariables: {
        user_id: 'USER_123',
        conversation_id: 'CONV_456'
    },

    // Optional: User profile information
    userVariables: {
        avatar_url: 'https://example.com/avatar.jpg',
        name: 'John Doe'
    }
}
```

  1. **Get your embed token**
        In your Dify app, go to **Publish → Embed** to find your unique token.

  1. **Add the script**
        Include the configuration and Dify's embed script in your website's HTML.

  1. **Customize appearance**
        Adjust the `containerProps` to match your website's design.

  1. **Test functionality**
        Open your website and try the chat button to ensure everything works correctly.

#### Iframe Integration

Embed your web app directly into your page content. This displays your app as an integral part of your website:

```html theme={null}
*[Embedded content]*
</iframe>
```

##### Why Use Iframe Embedding

* **Always visible** - Your web app is immediately accessible, not hidden behind a button
* **Full functionality** - Everything from your web app works identically in the iframe
* **Page integration** - Appears as native content, not an overlay
* **Simple setup** - Just HTML, no JavaScript configuration needed

##### Customization Options

**Size and Position**:

```html theme={null}
*[Embedded content]*
</iframe>
```

**Responsive Design**:

```html theme={null}

  *[Embedded content]*
  </iframe>

```

#### Choose Your Embedding Method

  **Customer Support Apps:**

    **Chat bubble** works best, staying out of the way until needed. The floating button lets visitors continue browsing while having quick access to help.

  **Form & Workflow Apps:**

    **Iframe embed** for dedicated pages where the app is the main content. Visitors see and use your app immediately without extra clicks.

  **Product Demonstrations:**

    **Iframe embed** on landing pages to let visitors try your AI capabilities instantly. No barriers between interest and engagement.

  **Multi-page Integration:**

    **Chat bubble** when you want the same app accessible across your entire site. One embed code provides access from every page.

#### Troubleshooting

**Widget not appearing**:

* Verify your app token matches what's shown in Dify's Publish → Embed section
* Check that configuration loads before the embed script
* Look for JavaScript errors in browser console

**Iframe not loading**:

* Confirm the web app URL includes your correct token
* Ensure your site allows iframe content (check Content Security Policy)
* Both your site and Dify app should use HTTPS

> **⚠️ Warning:**
>   Your web app must be published before embedding. If you update your app configuration, republish to see changes in embedded versions.

You can override the default button style using CSS variables or the `containerProps` option. Apply these methods based on CSS specificity to achieve your desired customizations.

##### 1. Modify CSS Variables

The following CSS variables are supported for customization:

```css theme={null}
/* Button distance to bottom, default is `1rem` */
--dify-chatbot-bubble-button-bottom

/* Button distance to right, default is `1rem` */
--dify-chatbot-bubble-button-right

/* Button distance to left, default is `unset` */
--dify-chatbot-bubble-button-left

/* Button distance to top, default is `unset` */
--dify-chatbot-bubble-button-top

/* Button background color, default is `#155EEF` */
--dify-chatbot-bubble-button-bg-color

/* Button width, default is `50px` */
--dify-chatbot-bubble-button-width

/* Button height, default is `50px` */
--dify-chatbot-bubble-button-height

/* Button border radius, default is `25px` */
--dify-chatbot-bubble-button-border-radius

/* Button box shadow, default is `rgba(0, 0, 0, 0.2) 0px 4px 8px 0px)` */
--dify-chatbot-bubble-button-box-shadow

/* Button hover transform, default is `scale(1.1)` */
--dify-chatbot-bubble-button-hover-transform
```

To change the background color to #ABCDEF, add this CSS:

```css theme={null}
#dify-chatbot-bubble-button {
    --dify-chatbot-bubble-button-bg-color: #ABCDEF;
}
```

##### 2. Use `containerProps`

Set inline styles using the `style` attribute:

```javascript theme={null}
window.difyChatbotConfig = {
    // ... other configurations
    containerProps: {
        style: {
            backgroundColor: '#ABCDEF',
            width: '60px',
            height: '60px',
            borderRadius: '30px',
        },
        // For minor style overrides, you can also use a string value for the `style` attribute:
        // style: 'background-color: #ABCDEF; width: 60px;',
    },
}
```

Apply CSS classes using the `className` attribute:

```javascript theme={null}
window.difyChatbotConfig = {
    // ... other configurations
    containerProps: {
        className: 'dify-chatbot-bubble-button-custom my-custom-class',
    },
}
```

##### 3. Pass `inputs`

There are four types of inputs supported:

1. **`text-input`**: Accepts any value. The input string will be truncated if its length exceeds the maximum allowed length.
2. **`paragraph`**: Similar to `text-input`, it accepts any value and truncates the string if it's longer than the maximum length.
3. **`number`**: Accepts a number or a numerical string. If a string is provided, it will be converted to a number using the `Number` function.
4. **`options`**: Accepts any value, provided it matches one of the pre-configured options.

Example configuration:

```javascript theme={null}
window.difyChatbotConfig = {
    // Other configuration settings...
    inputs: {
        name: 'apple',
    },
}
```

Note: When using the embed.js script to create an iframe, each input value will be processed (compressed using GZIP and encoded in base64) before being appended to the URL.

For example, the URL with processed input values will look like this:
`http://localhost/chatbot/{token}?name=H4sIAKUlmWYA%2FwWAIQ0AAACDsl7gLuiv2PQEUNAuqQUAAAA%3D`

#### Settings

*Configure branding, basic access controls, and user experience settings for your published web applications*

**Source:** https://docs.dify.ai/en/cloud/use-dify/publish/webapp/web-app-settings

Configure branding, basic access controls, and user experience settings for your published web applications

Web app settings control how your published applications look and behave for end users. Every Dify application automatically generates a web interface that adapts to different devices and screen sizes.

#### How Settings Work

Your web app reflects your application's current configuration. When you modify settings and click **Publish**, changes flow immediately to the live web application that users are accessing.

> **ℹ️ Info:**
>   Web apps are public by default. Anyone with the URL can access them, which works well for demos, public tools, and customer-facing applications.

#### Branding and Appearance

Make your web app look professional and recognizable:

  - **App Identity** — Set your app name, description, and icon to create a clear first impression

  - **Visual Design** — Choose colors, themes, and layout options that match your brand

  - **Language Settings** — Configure interface language for your target audience

  - **Legal Pages** — Add copyright information and privacy policy links for compliance

##### Essential Branding Elements

**App Icon and Name**

* Your icon appears in browser tabs and when users bookmark your app
* Choose a clear, recognizable name that explains what your app does
* Icons can be images or emojis; pick what fits your app's personality

**Description and Messaging**

* Write a concise description that helps users understand your app's purpose
* This text appears on the app's landing page and in search results
* Keep it under 160 characters for best results

**Visual Consistency**

* Choose colors that align with your brand
* Consider your audience when selecting light or dark themes
* Test your app on different devices to ensure it looks good everywhere

#### Access and Legal

Web apps are public by default. Anyone with the URL can open them, which works well for demos, public tools, and customer-facing applications.

**Privacy and Legal**:

* Add copyright information and privacy policy links
* Configure data handling preferences
* Set terms of service for compliance

#### Feature Inheritance

Your web app automatically includes features you've enabled in your application configuration:

**Interactive Features**:

* Conversation openers and suggested follow-ups
* Pre-conversation forms for context gathering
* Voice input and speech-to-text capabilities
* Source citations and reference links
* Feedback collection and rating systems

**Functionality**:

* All workflow steps and AI model configurations
* Knowledge base integrations and tool connections
* Custom prompts and response formatting
* Rate limiting and usage controls

> **⚠️ Warning:**
>   Disabling features in your app configuration immediately removes them from the published web app.

#### App Types and Behavior

Your web app automatically adapts its interface based on your application type:

  **Chat Applications:**

    **Interface**: Conversation-style with message history
    **Features**: Persistent sessions, conversation management, real-time responses
    **Best for**: Customer support, consulting tools, interactive assistants

  **Workflow Applications:**

    **Interface**: Form-based with result display
    **Features**: Single runs, batch processing, result saving
    **Best for**: Content generation, data processing, analysis tools

#### Deployment Options

Once published, your web app can be accessed in multiple ways:

  - **Direct Link** — Share the web app URL for immediate access

  - **[Website Embedding](https://docs.dify.ai/en/cloud/use-dify/publish/webapp/embedding-in-websites)** — Deploy as chat widgets or iframes on existing websites

#### Publishing Best Practices

Before sharing your web app:

  1. **Test the user experience**
        Try your app on different devices and browsers to ensure it works smoothly.

  1. **Configure essential settings**
        Set up your app name, icon, description, and any required legal information.

  1. **Confirm the URL is safe to share**
        Web apps are public, so anyone with the link can use them. Share the URL only with the audience you intend to reach.

  1. **Choose deployment method**
        Determine whether to share directly or embed on your website.

> **💡 Tip:**
>   Your web app configuration applies everywhere it's deployed. Changes to settings automatically update embedded versions too.

#### Workflow Web Apps

*Turn your workflows into powerful web applications with batch processing, result management, and streamlined user experiences*

**Source:** https://docs.dify.ai/en/cloud/use-dify/publish/webapp/workflow-webapp

Turn your workflows into powerful web applications with batch processing, result management, and streamlined user experiences

Workflow web apps transform your Dify workflows into production-ready applications that handle everything from single runs to large-scale batch operations. Users get a clean interface for input, real-time processing feedback, and comprehensive result management.

#### How Workflow Apps Work

When you publish a workflow, Dify automatically creates a web interface that:

* **Collects input parameters** through forms based on your workflow's start variables
* **Processes requests** using your complete workflow logic
* **Handles results** with built-in saving, copying, and management features
* **Scales automatically** from single runs to batch processing hundreds of items

> **ℹ️ Info:**
>   Unlike chat apps that maintain conversation context, Workflow apps are designed for discrete tasks that produce specific outputs.

  - **Single Execution** — Run workflows one at a time with immediate results and feedback

  - **Batch Processing** — Process hundreds of inputs simultaneously with CSV upload/download

  - **Result Management** — Save, organize, and export outputs with built-in storage

  - **More Like This** — Generate variations of successful outputs automatically

#### Single Execution

The default mode for Workflow apps handles individual requests with real-time processing:

  ![Single Workflow Execution Interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/4c5380cf71066d933082f7c30deacb01.png)

**User Experience**:

1. **Fill input form** - Users provide parameters based on your workflow's start variables
2. **Click run** - The workflow executes with real-time progress indication
3. **View results** - Output appears with immediate access to copy, save, and feedback options
4. **Take actions** - Users can save important results, provide feedback, or generate similar outputs

Each result includes built-in actions:

* **Copy** - One-click copying to clipboard for easy sharing
* **Save** - Store results in the app's saved items for later access
* **Feedback** - Like/dislike ratings to help improve your workflow
* **More like this** - Generate variations based on the current result (if enabled)

#### Batch Processing

When you need to run the same workflow on multiple inputs, batch processing handles hundreds of executions simultaneously:

> **💡 Tip:**
>   Perfect for tasks like generating content for multiple topics, processing customer data, or analyzing large datasets.

##### Set Up Batch Runs

  1. **Switch to batch mode**
        Click the "Run Batch" tab to access batch processing features.

          ![Batch Run Tab Interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/c8381ab7fad14a54c86835dc4b1b6b5d.png)

  1. **Get the CSV template**
        Download the template file to see the required column structure for your workflow's input variables.

          ![CSV Template Download](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/bae4859c5cb7404ce901b7979237bb93.png)

  1. **Prepare your data**
        Fill the template with your input data. Each row becomes one workflow execution.

  1. **Upload and run**
        Upload your completed CSV file and start batch processing.

          ![Batch Processing Execution](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/fc84f62f41c12e14ff85b29e6bf43d27.png)

##### Batch Processing Benefits

* **Parallel execution** - Multiple workflow runs happen simultaneously
* **Progress tracking** - Real-time updates on completion status
* **Bulk export** - Download all results as a CSV file when finished
* **Error handling** - Failed items are clearly marked with error details

> **⚠️ Warning:**
>   CSV files must use Unicode encoding to prevent import failures. When saving from Excel or similar tools, explicitly select "Unicode (UTF-8)" encoding.

#### Result Management

Workflow apps include comprehensive result management to help users organize and reuse outputs:

##### Save Results

  ![Saved Results Interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/3cdd15e87aa1f1aae9f6abadb0f16d1f.png)

**How saving works**:

* Users click "Save" on any result they want to keep
* Saved items appear in the dedicated "Saved" tab
* Each saved result includes the original inputs and full outputs
* Users can organize saved results and access them anytime

> **ℹ️ Info:**
>   Saved results persist across user sessions, making Workflow apps useful for building personal libraries of outputs.

##### Generate Variations

When you enable "More like this" in your workflow settings, users can generate variations of successful results:

  ![More Like This Feature](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/65fb111d8e89a8f7b761859265e42f0a.png)

**How it works**:

1. User gets a result they like
2. They click "More like this" to generate similar outputs
3. The workflow runs again with slight variations to produce different but related results
4. Users can iterate until they find the perfect output

> **💡 Tip:**
>   "More like this" works especially well for creative workflows like content generation, where users want to explore different approaches to the same topic.

### Workspace

#### Custom Endpoints

**Source:** https://docs.dify.ai/en/cloud/use-dify/workspace/api-extension/api-extension

You can extend module capabilities through custom endpoints. Currently, the following extension types are supported:

* `moderation` Sensitive content moderation
* `external_data_tool` External data tools

Before extending module capabilities, you need to prepare an API and an API Key for authentication.

In addition to developing the corresponding module capabilities, you also need to follow the specifications below to ensure Dify correctly calls the API.

#### API Specification

Dify will call your interface with the following specification:

```
POST {Your-API-Endpoint}
```

##### Header

| Header          | Value              | Desc                                                                                                                                                 |
| --------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Content-Type`  | application/json   | The request content is in JSON format.                                                                                                               |
| `Authorization` | Bearer \{api_key} | The API Key is transmitted as a Token. You need to parse the `api_key` and verify that it matches the provided API Key to ensure interface security. |

##### Request Body

```
{
    "point":  string, //  Extension point, different modules may contain multiple extension points
    "params": {
        ...  // Parameters passed to each module extension point
    }
}
```

##### API Response

```
{
    ...  // Content returned by the API, see the specification design of different modules for different extension point returns
}
```

#### Validation

When configuring a custom endpoint in Dify, Dify will send a request to the API Endpoint to verify API availability.

When the API Endpoint receives `point=ping`, the interface should return `result=pong`, as follows:

##### Header

```
Content-Type: application/json
Authorization: Bearer {api_key}
```

##### Request Body

```
{
    "point": "ping"
}
```

##### Expected API Response

```
{
    "result": "pong"
}
```

#### Example

Here we use an external data tool as an example, where the scenario is to retrieve external weather information by region as context.

##### API Example

```
POST https://fake-domain.com/api/dify/receive
```

**Header**

```
Content-Type: application/json
Authorization: Bearer 123456
```

**Request Body**

```
{
    "point": "app.external_data_tool.query",
    "params": {
        "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",
        "tool_variable": "weather_retrieve",
        "inputs": {
            "location": "London"
        },
        "query": "How's the weather today?"
    }
}
```

**API Response**

```
{
    "result": "City: London\nTemperature: 10°C\nRealFeel®: 8°C\nAir Quality: Poor\nWind Direction: ENE\nWind Speed: 8 km/h\nWind Gusts: 14 km/h\nPrecipitation: Light rain"
}
```

##### Code Example

The code is based on the Python FastAPI framework.

1. Install dependencies

   ```
   pip install fastapi[all] uvicorn
   ```

2. Write code according to the interface specification

   ```
   from fastapi import FastAPI, Body, HTTPException, Header
   from pydantic import BaseModel

   app = FastAPI()

   class InputData(BaseModel):
       point: str
       params: dict = {}

   @app.post("/api/dify/receive")
   async def dify_receive(data: InputData = Body(...), authorization: str = Header(None)):
       """
       Receive API query data from Dify.
       """
       expected_api_key = "123456"  # TODO Your API key of this API
       auth_scheme, _, api_key = authorization.partition(' ')

       if auth_scheme.lower() != "bearer" or api_key != expected_api_key:
           raise HTTPException(status_code=401, detail="Unauthorized")

       point = data.point

       # for debug
       print(f"point: {point}")

       if point == "ping":
           return {
               "result": "pong"
           }
       if point == "app.external_data_tool.query":
           return handle_app_external_data_tool_query(params=data.params)
       # elif point == "{point name}":
           # TODO other point implementation here

       raise HTTPException(status_code=400, detail="Not implemented")

   def handle_app_external_data_tool_query(params: dict):
       app_id = params.get("app_id")
       tool_variable = params.get("tool_variable")
       inputs = params.get("inputs")
       query = params.get("query")

       # for debug
       print(f"app_id: {app_id}")
       print(f"tool_variable: {tool_variable}")
       print(f"inputs: {inputs}")
       print(f"query: {query}")

       # TODO your external data tool query implementation here,
       #  return must be a dict with key "result", and the value is the query result
       if inputs.get("location") == "London":
           return {
               "result": "City: London\nTemperature: 10°C\nRealFeel®: 8°C\nAir Quality: Poor\nWind Direction: ENE\nWind "
                         "Speed: 8 km/h\nWind Gusts: 14 km/h\nPrecipitation: Light rain"
           }
       else:
           return {"result": "Unknown city"}
   ```

3. Start the API service. The default port is 8000, the complete API address is: `http://127.0.0.1:8000/api/dify/receive`, and the configured API Key is `123456`.

   ```
   uvicorn main:app --reload --host 0.0.0.0
   ```

4. Configure this API in Dify.

5. Select this custom endpoint in the App.

When debugging the App, Dify will request the configured API and send the following content (example):

```
{
    "point": "app.external_data_tool.query",
    "params": {
        "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",
        "tool_variable": "weather_retrieve",
        "inputs": {
            "location": "London"
        },
        "query": "How's the weather today?"
    }
}
```

The API response is:

```
{
    "result": "City: London\nTemperature: 10°C\nRealFeel®: 8°C\nAir Quality: Poor\nWind Direction: ENE\nWind Speed: 8 km/h\nWind Gusts: 14 km/h\nPrecipitation: Light rain"
}
```

#### Local Debugging

Because Dify cannot reach API services on your private network, you can use [Ngrok](https://ngrok.com) to expose the API service endpoint to the public network to enable cloud debugging of local code. Steps:

1. Go to [https://ngrok.com](https://ngrok.com), register and download the Ngrok file.

     ![Download](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/extension/api-based-extension/c44d6cc5425508daac8d31bc4af113df.png)

2. After downloading, go to the download directory, extract the archive according to the instructions below, and execute the initialization script in the instructions.
   ```shell theme={null}
   unzip /path/to/ngrok.zip
   ./ngrok config add-authtoken your-token
   ```

3. Check the port of your local API service:

     ![Check Port](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/extension/api-based-extension/7ac8ee0f0955f36255e0261b36499db7.png)

   And run the following command to start:

   ```shell theme={null}
   ./ngrok http port-number
   ```

   A successful startup example looks like this:

     ![Ngrok Startup](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/extension/api-based-extension/2b4adbe0bb1ff203da521ea6eea401f8.png)

4. Find the Forwarding address, as shown above: `https://177e-159-223-41-52.ngrok-free.app` (this is an example domain, please replace with your own), which is the public domain.

Following the example above, we expose the locally started service endpoint and replace the code example interface: `http://127.0.0.1:8000/api/dify/receive` with `https://177e-159-223-41-52.ngrok-free.app/api/dify/receive`

This API endpoint can now be accessed publicly. At this point, we can configure this API endpoint in Dify for local code debugging. For configuration steps, please refer to [External Data Tool](https://docs.dify.ai/en/cloud/use-dify/workspace/api-extension/external-data-tool-api-extension).

#### Deploy Custom Endpoints Using Cloudflare Workers

We recommend using Cloudflare Workers to deploy your custom endpoints because Cloudflare Workers can conveniently provide a public network address and can be used for free.

For detailed instructions, see [Deploy Custom Endpoints Using Cloudflare Workers](https://docs.dify.ai/en/cloud/use-dify/workspace/api-extension/cloudflare-worker).

#### Deploy Custom Endpoints Using Cloudflare Workers

**Source:** https://docs.dify.ai/en/cloud/use-dify/workspace/api-extension/cloudflare-worker

#### Procedure

Since Dify custom endpoints require a publicly accessible address as the API Endpoint, the endpoint needs to be deployed to a public address.

Here we use Cloudflare Workers to deploy the custom endpoint.

Clone the [Example GitHub Repository](https://github.com/crazywoola/dify-extension-workers). This repository contains a simple custom endpoint that can be modified as a starting point.

```bash theme={null}
git clone https://github.com/crazywoola/dify-extension-workers.git
cp wrangler.toml.example wrangler.toml
```

Open the `wrangler.toml` file and modify `name` and `compatibility_date` to your application name and compatibility date.

The configuration we need to pay attention to here is the `TOKEN` in `vars`. When adding a custom endpoint in Dify, we need to fill in this Token. For security reasons, we recommend using a random string as the Token. You should not write the Token directly in the source code, but pass it through environment variables. Therefore, please do not commit wrangler.toml to your code repository.

```toml theme={null}
name = "dify-extension-example"
compatibility_date = "2023-01-01"

[vars]
TOKEN = "bananaiscool"
```

This custom endpoint will return a random Breaking Bad quote. You can modify the logic of this custom endpoint in `src/index.ts`. This example demonstrates how to interact with third-party APIs.

```typescript theme={null}
// ⬇️ implement your logic here ⬇️
// point === "app.external_data_tool.query"
// https://api.breakingbadquotes.xyz/v1/quotes
const count = params?.inputs?.count ?? 1;
const url = `https://api.breakingbadquotes.xyz/v1/quotes/${count}`;
const result = await fetch(url).then(res => res.text())
// ⬆️ implement your logic here ⬆️
```

This repository simplifies all configurations except business logic. You can directly use `npm` commands to deploy your custom endpoint.

```bash theme={null}
npm install
npm run deploy
```

After successful deployment, you will get a public address that you can add in Dify as the custom endpoint. Please note not to omit the `endpoint` path. The specific definition of this path can be found in `src/index.ts`.

  ![Add Custom Endpoint in Dify](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/extension/api-based-extension/9433a486a441713ade6270e9dc6c0544.png)

Alternatively, you can use the `npm run dev` command to deploy locally for testing.

```bash theme={null}
npm install
npm run dev
```

Related output:

```bash theme={null}
$ npm run dev
> dev
> wrangler dev src/index.ts

 ⛅️ wrangler 3.99.0
-------------------

Your worker has access to the following bindings:
- Vars:
  - TOKEN: "ban****ool"
⎔ Starting local server...
[wrangler:inf] Ready on http://localhost:58445
```

After that, you can use tools like Postman for local interface debugging.

#### About Bearer Auth

```typescript theme={null}
import { bearerAuth } from "hono/bearer-auth";

(c, next) => {
    const auth = bearerAuth({ token: c.env.TOKEN });
    return auth(c, next);
},
```

Our Bearer validation logic is in the above code. We use the `hono/bearer-auth` package to implement Bearer validation. You can use `c.env.TOKEN` in `src/index.ts` to get the Token.

#### About Parameter Validation

```typescript theme={null}
import { z } from "zod";
import { zValidator } from "@hono/zod-validator";

const schema = z.object({
  point: z.union([
    z.literal("ping"),
    z.literal("app.external_data_tool.query"),
  ]), // Restricts 'point' to two specific values
  params: z
    .object({
      app_id: z.string().optional(),
      tool_variable: z.string().optional(),
      inputs: z.record(z.any()).optional(),
      query: z.any().optional(),  // string or null
    })
    .optional(),
});

```

We use `zod` to define parameter types here. You can use `zValidator` in `src/index.ts` to validate parameters. Use `const { point, params } = c.req.valid("json");` to get the validated parameters.

The `point` here has only two values, so we use `z.union` to define it. `params` is an optional parameter, so we use `z.optional` to define it. There will be an `inputs` parameter, which is a `Record<string, any>` type. This type represents an object with string keys and any values. This type can represent any object. You can use `params?.inputs?.count` in `src/index.ts` to get the `count` parameter.

#### Get Cloudflare Workers Logs

```bash theme={null}
wrangler tail
```

***

**Reference**:

* [Cloudflare Workers](https://workers.cloudflare.com/)
* [Cloudflare Workers CLI](https://developers.cloudflare.com/workers/cli-wrangler/install-update)
* [Example GitHub Repository](https://github.com/crazywoola/dify-extension-workers)

#### External Data Tool

**Source:** https://docs.dify.ai/en/cloud/use-dify/workspace/api-extension/external-data-tool-api-extension

When creating AI applications, you can use external tools to obtain additional data through [Custom Endpoints](https://docs.dify.ai/en/cloud/use-dify/workspace/api-extension/api-extension) and assemble it into the prompt as additional information for the LLM.

#### Extension Point

`app.external_data_tool.query`: Application external data tool query extension point.

This extension point passes the application variable content input by the end user and the conversation input content (fixed parameter for conversational applications) to the API as parameters.

You need to implement the corresponding tool query logic and return query results as string type.

##### Request Body

```
{
    "point": "app.external_data_tool.query", // Extension point type, fixed as app.external_data_tool.query
    "params": {
        "app_id": string,  // Application ID
        "tool_variable": string,  // External data tool variable name, indicating the source of the corresponding variable tool call
        "inputs": {  // Variable values passed by end user, key is variable name, value is variable value
            "var_1": "value_1",
            "var_2": "value_2",
            ...
        },
        "query": string | null  // Current conversation input content from end user, fixed parameter for conversational applications.
    }
}
```

**Example**:

```
{
    "point": "app.external_data_tool.query",
    "params": {
        "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",
        "tool_variable": "weather_retrieve",
        "inputs": {
            "location": "London"
        },
        "query": "How's the weather today?"
    }
}
```

##### API Response

```
{
    "result": string
}
```

**Example**:

```
{
    "result": "City: London\nTemperature: 10°C\nRealFeel®: 8°C\nAir Quality: Poor\nWind Direction: ENE\nWind Speed: 8 km/h\nWind Gusts: 14 km/h\nPrecipitation: Light rain"
}
```

#### Sensitive Content Moderation

**Source:** https://docs.dify.ai/en/cloud/use-dify/workspace/api-extension/moderation-api-extension

This module is used to review the content input by end users and the content output by LLM in applications. It is divided into two extension point types.

#### Extension Points

* `app.moderation.input`: End user input content review extension point
  * Used to review variable content passed in by end users and conversation input content in conversational applications.
* `app.moderation.output`: LLM output content review extension point
  * Used to review content output by LLM.
  * When the LLM output is streaming, the output content will be segmented into 100-character chunks for API requests to avoid delayed reviews when output content is lengthy.

##### app.moderation.input

When **Content Moderation > Review Input Content** is enabled in applications such as Chatflow, Agent, or Chatbot, Dify will send the following HTTP POST request to the corresponding custom endpoint:

###### Request Body

```
{
    "point": "app.moderation.input", // Extension point type, fixed as app.moderation.input
    "params": {
        "app_id": string,  // Application ID
        "inputs": {  // Variable values passed by end user, key is variable name, value is variable value
            "var_1": "value_1",
            "var_2": "value_2",
            ...
        },
        "query": string | null  // Current conversation input content from end user, fixed parameter for conversational applications.
    }
}
```

**Example**:

```
{
    "point": "app.moderation.input",
    "params": {
        "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",
        "inputs": {
            "var_1": "My SSN is 123-45-6789.",
            "var_2": "My phone number is 123-456-7890."
        },
        "query": "Please help me update my account."
    }
}
```

###### API Response

```
{
    "flagged": bool,  // Whether it violates validation rules
    "action": string, // Action: direct_output outputs preset response; overridden overwrites input variable values
    "preset_response": string,  // Preset response (returned only when action=direct_output)
    "inputs": {  // Variable values passed by end user, key is variable name, value is variable value (returned only when action=overridden)
        "var_1": "value_1",
        "var_2": "value_2",
        ...
    },
    "query": string | null  // Overwritten current conversation input content from end user, fixed parameter for conversational applications. (returned only when action=overridden)
}
```

**Example**:

* `action=direct_output`
  ```
  {
      "flagged": true,
      "action": "direct_output",
      "preset_response": "Your content violates our usage policy."
  }
  ```
* `action=overridden`
  ```
  {
      "flagged": true,
      "action": "overridden",
      "inputs": {
          "var_1": "My SSN is ***-**-****.",
          "var_2": "My phone number is ***-***-****."
      },
      "query": "Please help me update my account."
  }
  ```

##### app.moderation.output

When **Content Moderation > Review Output Content** is enabled in applications such as Chatflow, Agent, or Chat Assistant, Dify will send the following HTTP POST request to the corresponding custom endpoint:

###### Request Body

```
{
    "point": "app.moderation.output", // Extension point type, fixed as app.moderation.output
    "params": {
        "app_id": string,  // Application ID
        "text": string  // LLM response content. When LLM output is streaming, this is content segmented into 100-character chunks.
    }
}
```

**Example**:

```
{
    "point": "app.moderation.output",
    "params": {
        "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",
        "text": "My SSN is 123-45-6789."
    }
}
```

###### API Response

```
{
    "flagged": bool,  // Whether it violates validation rules
    "action": string, // Action: direct_output outputs preset response; overridden overwrites input variable values
    "preset_response": string,  // Preset response (returned only when action=direct_output)
    "text": string  // Overwritten LLM response content. (returned only when action=overridden)
}
```

**Example**:

* `action=direct_output`
  ```
  {
      "flagged": true,
      "action": "direct_output",
      "preset_response": "Your content violates our usage policy."
  }
  ```
* `action=overridden`
  ```
  {
      "flagged": true,
      "action": "overridden",
      "text": "My SSN is ***-**-****."
  }
  ```

#### Code Example

Below is a piece of `src/index.ts` code that can be deployed on Cloudflare. (For complete Cloudflare usage, please refer to [this documentation](https://docs.dify.ai/en/cloud/use-dify/workspace/api-extension/cloudflare-worker))

The code works by performing keyword matching to filter both Input (content entered by users) and Output (content returned by the model). Users can modify the matching logic according to their needs.

```
import { Hono } from "hono";
import { bearerAuth } from "hono/bearer-auth";
import { z } from "zod";
import { zValidator } from "@hono/zod-validator";
import { generateSchema } from '@anatine/zod-openapi';

type Bindings = {
  TOKEN: string;
};

const app = new Hono<{ Bindings: Bindings }>();

// API format validation ⬇️
const schema = z.object({
  point: z.union([
    z.literal("ping"),
    z.literal("app.external_data_tool.query"),
    z.literal("app.moderation.input"),
    z.literal("app.moderation.output"),
  ]), // Restricts 'point' to two specific values
  params: z
    .object({
      app_id: z.string().optional(),
      tool_variable: z.string().optional(),
      inputs: z.record(z.any()).optional(),
      query: z.any(),
      text: z.any()
    })
    .optional(),
});

// Generate OpenAPI schema
app.get("/", (c) => {
  return c.json(generateSchema(schema));
});

app.post(
  "/",
  (c, next) => {
    const auth = bearerAuth({ token: c.env.TOKEN });
    return auth(c, next);
  },
  zValidator("json", schema),
  async (c) => {
    const { point, params } = c.req.valid("json");
    if (point === "ping") {
      return c.json({
        result: "pong",
      });
    }
    // ⬇️ implement your logic here ⬇️
    // point === "app.external_data_tool.query"
    else if (point === "app.moderation.input"){
    // Input check ⬇️
    const inputkeywords = ["input filter test 1", "input filter test 2", "input filter test 3"];

    if (inputkeywords.some(keyword => params.query.includes(keyword)))
      {
      return c.json({
        "flagged": true,
        "action": "direct_output",
        "preset_response": "The input contains illegal content. Please try a different question!"
      });
    } else {
      return c.json({
        "flagged": false,
        "action": "direct_output",
        "preset_response": "Input is normal"
      });
    }
    // Input check complete
    }

    else {
      // Output check ⬇️
      const outputkeywords = ["output filter test 1", "output filter test 2", "output filter test 3"];

  if (outputkeywords.some(keyword => params.text.includes(keyword)))
    {
      return c.json({
        "flagged": true,
        "action": "direct_output",
        "preset_response": "The output contains sensitive content and has been filtered by the system. Please try a different question!"
      });
    }

  else {
    return c.json({
      "flagged": false,
      "action": "direct_output",
      "preset_response": "Output is normal"
    });
  };
    }
    // Output check complete
  }
);

export default app;

```

#### Manage Apps

*Organize, maintain, and share your AI applications with powerful management tools and best practices*

**Source:** https://docs.dify.ai/en/cloud/use-dify/workspace/app-management

Organize, maintain, and share your AI applications with powerful management tools and best practices

Managing your apps well is crucial for productive AI development. Dify provides comprehensive tools to organize, share, and maintain your applications throughout their lifecycle.

#### App Organization

  - **Edit & Customize** — Update names, descriptions, icons, and branding for better organization

  - **Duplicate & Template** — Create variations or use existing apps as templates for new projects

  - **Import & Export** — Share apps between workspaces using Dify's DSL format

  - **Lifecycle Management** — Safely delete apps when no longer needed

#### Edit Application Information

Keep your apps organized with clear, descriptive information:

  ![Edit App Info Interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/management/63a449e9a8ae337b9c067165d1674a45.png)

  1. **Access app settings**
        Click "Edit info" in the upper left corner of your application.

  1. **Update details**
        Modify the icon, name, or description to better reflect the app's purpose.

  1. **Consider your team**
        Use names and descriptions that help team members understand what the app does.

> **💡 Tip:**
>   Use consistent naming conventions across your workspace. Consider prefixes like "Draft-", "Test-", or "Prod-" to indicate app status.

#### Create App Variations

Duplication is perfect for creating variations or starting new projects from existing work:

**When to duplicate**:

* Creating A/B test versions with different prompts or models
* Adapting an app for different audiences or use cases
* Starting a new project based on successful patterns
* Creating backups before major changes

**How duplication works**:

* All configuration, prompts, and workflows are copied
* The new app gets a default name you can customize
* Original app remains unchanged
* Both apps run independently

#### App Export and Import

Dify's DSL (Domain Specific Language) format lets you share apps between workspaces and teams:

  ![Export DSL Interface](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/management/544c18d770e230db93d6756bba98d8a7.png)

##### Export Applications

**Two ways to export**:

1. **From Studio page** - Click "Export DSL" in the application menu
2. **From orchestration** - Click "Export DSL" in the upper left corner

**What gets exported**:

* App configuration and metadata
* Workflow orchestration and node settings
* Model parameters and prompt templates
* Knowledge base connections (not the data itself)

**What doesn't get exported**:

* API keys for third-party tools (security measure)
* Actual knowledge base content
* Usage logs and analytics data

> **⚠️ Warning:**
>   If your app uses Secret-type environment variables, you'll be asked whether to include them in the export. Be careful with sensitive information.

  ![Secret Variables Export Prompt](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/management/25ce002ef7f0392fc6b3b6975ae137ec.png)

##### Import Applications

  ![Import Application Interface](https://assets-docs.dify.ai/2024/11/487d2c1cc8b86666feb35ea8a346c053.png)

**Import process**:

1. Upload your DSL file (YAML format)
2. System checks version compatibility
3. Warning appears if DSL version is older than current platform
4. App is created with all configurations from the file

**Version compatibility**: Your platform always runs the latest DSL version, so imported files are always compatible.

> **ℹ️ Info:**
>   Dify DSL is the AI application engineering standard (v0.6+) that captures complete app configurations in YAML format.

#### Safe App Deletion

Before deleting apps, understand the impact:

**What gets deleted**:

* All app configurations and prompts
* Workflow orchestration and settings
* Usage logs and analytics
* Published web apps and API access
* All user conversations and data

**Impact on users**:

* Published web apps stop working immediately
* API calls start returning errors
* All existing user sessions are terminated

  1. **Consider alternatives**
        Could you duplicate the app for backup, or just unpublish instead of deleting?

  1. **Notify stakeholders**
        Let team members and users know about planned deletions.

  1. **Export if needed**
        Create DSL backups of valuable configurations before deletion.

  1. **Confirm deletion**
        Click "Delete" and confirm—this action cannot be undone.

> **⚠️ Warning:**
>   App deletion is permanent and cannot be undone. All associated data, logs, and user access will be lost immediately.

#### Model Providers

*Use models with your AI Credits, or connect your own provider accounts and keys*

**Source:** https://docs.dify.ai/en/cloud/use-dify/workspace/model-providers

Use models with your AI Credits, or connect your own provider accounts and keys

Every AI app you build runs on a model. Dify Cloud comes with popular models, and lets you connect your own provider accounts when you need more.

Models are shared across the workspace, so your whole team works with the same ones.

> **⚠️ Warning:**
>   Only the workspace owner and admins can manage providers. Any key you add works across the whole workspace and bills to your own account with that provider.

#### Use Models with Your AI Credits

Dify Cloud gives you AI Credits to use models from a set of popular providers, so you don't need your own API key to start.

Install one of these providers from **Integrations** > **Model Provider** (or the [Marketplace](https://marketplace.dify.ai/)), and its models are ready to use. Each AI response consumes your AI Credits.

An AI response is a single model call (one input and one output), and it counts as one response no matter how many tokens it uses. The number of credits a response costs depends on the model, with larger models costing more than smaller ones.

See the [Dify pricing page](https://dify.ai/pricing) for which providers AI Credits support and how many credits each model costs.

#### Use Your Own Account with a Supported Provider

Add your own API key to a supported provider when you want higher rate limits or billing through your own provider account.

1. In **Integrations** > **Model Provider**, install the provider if it isn't already.

2. Click **Setup** on its card, then enter your API key and any other required details. Dify checks the key before making the provider available.

Your key and AI Credits can coexist. Set **Usage Priority** on the provider card to control which one Dify draws from first and falls back to the other, so a key you add can simply take over once your credits run out.

#### Connect a Provider AI Credits Don't Support

To use a provider that AI Credits don't support, install it first and run it on your own account. AI Credits don't apply to these providers.

1. In **Integrations** > **Model Provider**, browse **Install model providers**, or open the [Marketplace](https://marketplace.dify.ai/) for the full list.

2. Install the provider, click **Setup**, and enter your API key along with any other required details.

#### Add a Custom Model

A provider's models are ready as soon as you connect it, so you only add one by hand when the model you need isn't listed, such as a brand-new or fine-tuned model.

Click **Add Model** on the provider's card, then give the model a name and its credentials. Providers that serve only a fixed set of models don't offer this option.

> **ℹ️ Info:**
>   If the model you add matches the name and type of an existing one, Dify attaches the new key to that model instead of creating a duplicate.

#### Manage Your Keys

Add more than one key to a provider when you want to keep development and production apart or spread usage across several accounts.

* For a provider's own models, click **Configure** on its card to manage the keys they share.

    *[Image: Manage Credentials for a Provider's Models]*

* For a custom model you added, click **Configure** on that model to manage its own keys.

      *[Image: Custom Model Configuration]*

      *[Image: Custom Model Credentials]*

  > **⚠️ Warning:**
>     A custom model relies on its own keys. Deleting its only key removes the model too.
>

  To view every custom model's keys in one place, click **Manage Credentials** on the provider card.

    *[Image: Manage Credentials for All Custom Models]*

  Keys stay here even after the custom model is removed, so you can re-add the model later without re-entering its keys.

    *[Image: Re-add a Removed Model]*

#### Choose the Models Apps Use by Default

Apps and nodes that don't pick a model fall back to your workspace defaults. Click **Default Models** at the top-right corner to set one for each job:

* **System Reasoning Model**: the default for general LLM tasks.
* **Embedding Model**: indexes and retrieves knowledge base content.
* **Rerank Model**: reorders retrieval results by relevance.
* **Speech-to-Text Model**: turns audio into text.
* **Text-to-Speech Model**: turns text into audio.

#### Spread Requests Across Keys with Load Balancing **[Professional]** **[Team]**

When one key handles many requests at once, it can hit the provider's rate limit and start failing.

Use load balancing to spread requests across several keys for the same model, so no single key becomes the bottleneck. Dify rotates through the keys in turn and rests any that hits its limit for a minute before trying it again.

1. Find the model in the list, click **Configure**, and select **Load Balancing**.

2. Click **Add credential** to add keys to the pool.

   > **💡 Tip:**
>      Add a higher-quota or faster key more than once to send more of the traffic its way.
>

     *[Image: Add Credentials for Load Balancing]*

3. Turn on at least two keys, then click **Save**. A model using load balancing shows a marker in the list.

> **ℹ️ Info:**
>   Switch back to a single key anytime; your load balancing setup is kept for later use.

#### Personal Settings

*Manage your profile and preferences across all workspaces*

**Source:** https://docs.dify.ai/en/cloud/use-dify/workspace/personal-account-management

Manage your profile and preferences across all workspaces

Your personal account spans all workspaces you belong to. Profile settings, language preferences, and login credentials follow you everywhere, while each workspace maintains its own team dynamics and permissions.

#### Account Setup

Your account is created automatically on first login. Sign in with GitHub, Google, or email verification code. Accounts with matching email addresses are linked automatically, so signing up with GitHub using `you@company.com` and later using email verification with the same address resolves to one account.

#### Multi-Workspace Access

Your personal account can belong to multiple workspaces. Each workspace has its own team, applications, and billing, but your profile remains consistent across all of them.

**Switching workspaces**: Use the workspace selector in the top-left corner to switch between workspaces you have access to.

**Workspace independence**: Your role and permissions are set per workspace. You might be an Owner in one workspace and a Member in another.

#### Profile Management

Update your profile information in **Settings → Account → Profile**. Changes apply across all workspaces you belong to.

**Profile picture**: Upload a custom avatar. This replaces the default initials-based avatar and appears in all workspaces.

**Display name**: How you appear to team members across all workspaces. Choose something that helps teammates identify you.

**Email address**: Your primary login credential and unique identifier. Changing your email affects every workspace using the old address.

#### Language and Interface

**Display language**: Available languages include English, Simplified Chinese, and Traditional Chinese. This setting affects interface elements but not your application content.

**Change language**: Click your avatar, choose **Language**, then select your preferred language.

#### Login Methods

Sign in with any of the following:

* **GitHub**: OAuth via your GitHub account.
* **Google**: OAuth via your Google account.
* **Email verification code**: One-time code delivered to your email address.

#### Security

Social login (GitHub or Google) inherits the security posture of your chosen provider. Review the provider's security settings and monitor login activity through their platform.

Your personal settings follow you everywhere, but each workspace has its own roles and permissions.

> **⚠️ Warning:**
>   Changing your email address affects all workspaces. If you want to change the email for just one workspace, ask that workspace to invite the new email as a separate user account.

#### Integrations

*Connect Dify to model providers, tools, data sources, and external services*

**Source:** https://docs.dify.ai/en/cloud/use-dify/workspace/plugins

Connect Dify to model providers, tools, data sources, and external services

Integrations connect your Dify apps to the outside world. They supply the model providers that power your apps, the tools your agents and workflows call, the data sources behind your knowledge bases, and the services that extend what you build.

Install an integration once, and every app in your workspace can use it. Browse and manage them all from **Integrations**.

#### Integration Types

* [**Model Provider**](https://docs.dify.ai/en/cloud/use-dify/workspace/model-providers): The models that power your apps, from LLMs to embedding and rerank models.

* [**Tool**](https://docs.dify.ai/en/cloud/use-dify/workspace/tools): Capabilities your agents and workflows can call, including tool plugins, MCP servers, published workflows, and OpenAPI services.

* [**Data Source**](https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/authorize-data-source): External content for pipeline-built knowledge bases, such as Google Drive or Notion pages.

* [**Trigger**](https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/plugin-trigger): Start a workflow automatically when an external event fires.

* **Agent Strategy**: The reasoning strategy an [Agent node](https://docs.dify.ai/en/cloud/use-dify/nodes/agent) follows to make decisions, select and call tools, and act on the results.

* [**Custom Endpoint**](https://docs.dify.ai/en/cloud/use-dify/workspace/api-extension/api-extension): Connect your own API to add content moderation or external data tools to your apps.

* **Extension**: Integrations that expose custom HTTP endpoints, extending Dify with capabilities the other categories don't cover.

#### Install Integrations

Add integrations from three sources:

* [**Marketplace**](https://marketplace.dify.ai/): Official and partner integrations, tested and maintained.
* **GitHub**: Install from any public repository by URL and version.
* **Local upload**: Custom `.zip` packages for private or internal integrations.

#### Permissions and Updates

The workspace owner and admins can set two workspace-wide permissions for integrations, each to **Everyone**, **Admins**, or **No one**:

* **Who can install and manage integrations**: Installing, upgrading, and removing. Defaults to **Everyone**.
* **Who can debug integrations**: Access to the debugging key. Defaults to **No one**.

Integrations can also be set to update automatically. Each category (tools, models, data sources, and so on) has its own update strategy (off, patch versions only, or always the latest), applied to every integration in the category or a chosen subset.

#### Build Your Own

> **ℹ️ Info:**
>   Need an integration that doesn't exist yet? Build it with Dify's plugin SDK, then keep it private or publish it to the Marketplace. See [Develop a Plugin](https://docs.dify.ai/en/develop-plugin/getting-started/getting-started-dify-plugin).

#### Overview

*Workspaces are the foundational organizational unit in Dify—everything your team builds, configures, and manages exists within a workspace*

**Source:** https://docs.dify.ai/en/cloud/use-dify/workspace/readme

Workspaces are the foundational organizational unit in Dify—everything your team builds, configures, and manages exists within a workspace

A workspace is your team's complete AI environment in Dify. It contains and isolates everything your organization needs: applications, knowledge bases, team members, model configurations, integrations, and billing.

#### The Workspace Mental Model

Every resource in Dify belongs to a workspace. When you create an app, it inherits the workspace's model configurations. When you add team members, they get access to workspace resources based on their role. When you configure models or install integrations, they become available to the entire workspace.

```
🏢 Your Organization
└── 📁 Workspace
    ├── 🤖 Apps (chatbots, workflows, agents)
    ├── 📊 Knowledge Bases (documents, embeddings)
    ├── 👥 Team Members (roles & permissions)
    ├── 🧠 Model Providers (API keys, configurations)
    ├── 🔧 Integrations (model providers, tools, custom code)
    └── 💳 Billing (subscription, limits, usage)
```

This workspace-first design means your resources are completely isolated from other organizations, team members can only access what they're permitted to see, and you configure models and billing once for the entire workspace.

#### Workspace Creation

A workspace is created automatically on your first login. You become the owner with full permissions. Each account can create only one workspace.

> **ℹ️ Info:**
>   Your personal account can belong to multiple workspaces. Switch between them using the workspace selector in the top-left corner.

#### How Resources Connect

Applications you build can use any model providers configured in the workspace, access all workspace knowledge bases, and use installed integrations. Team members see applications based on their workspace permissions.

Workspace roles determine access across all resources:

* **Owners** control billing, model providers, and workspace settings
* **Admins** manage team members and configure models and integrations
* **Editors** build applications and manage knowledge bases
* **Members** use published applications

#### Billing

*Manage your workspace subscription, plan changes, and the Dify for Education discount*

**Source:** https://docs.dify.ai/en/cloud/use-dify/workspace/subscription-management

Manage your workspace subscription, plan changes, and the Dify for Education discount

Billing in Dify is workspace-scoped. Your subscription sets the team member limit, feature access, and usage quotas for the entire workspace.

For the available plans, what each includes, and pricing, see the [Dify pricing page](https://dify.ai/pricing).

#### Manage Subscriptions

Only the workspace owner and admins can manage the workspace's subscription in **Settings** > **Billing**.

* **View subscription details**: see your current plan, usage, and billing history, or download invoices.

* **Upgrade**: click **Upgrade** and choose a higher plan. It takes effect immediately, once you pay the difference for the rest of the current billing period.

* **Downgrade**: click **Manage** to open the Stripe billing portal, then click **Update subscription** and choose a lower plan. It takes effect at the start of your next billing cycle; you keep your current plan until then.

* **Cancel or update billing**: click **Manage** to open the Stripe billing portal, where you can cancel the subscription or change the payment method. After cancellation, the workspace keeps its current plan until the end of the paid period, then returns to the free Sandbox plan.

#### Dify for Education

Students, teachers, and educational staff can verify their educational affiliation to use the Yearly Professional plan for free. Re-verification is required annually.

##### Prerequisites

* 18 years of age or older
* Current student, teacher, or educational staff member
* School-issued educational email (e.g., `.edu`)

##### Steps

  1. **Create Account**
        Register at [cloud.dify.ai](https://cloud.dify.ai/signin) with your educational email.

  1. **Apply for Verification**
        Go to **Settings** > **Billing** > **Get Education Verified**, then enter your school's full name and select your role. The result appears immediately.

  1. **Apply Discount to Workspace**
        1. After approval, select the workspace you want to use the education discount with, then click **Use education discount**.

           You'll be redirected to checkout with the **Yearly Professional Plan** and discount pre-applied.

           > **📝 Note:**
>              The education discount only applies to the Yearly Professional plan.
>

        2. Complete payment to activate the subscription.

##### FAQ

  **Why was I charged $59?:**

    You likely selected the Monthly Professional plan. The education discount applies only to the Yearly plan, so the Monthly plan charges the full \$59.

    To resolve this, cancel the current subscription, wait for the billing cycle to end, then subscribe to the *Yearly* Professional plan with the education discount.

  **What if I already have a paid subscription?:**

    The education discount cannot be applied to an existing paid plan.

    To resolve this, cancel your current subscription, wait for the billing cycle to end, then subscribe to the *Yearly* Professional plan with the education discount.

  **Why was my verification rejected?:**

    Common reasons: non-educational email, inaccurate information, or misuse of privileges. Appeal via [support@dify.ai](mailto:support@dify.ai).

  **Can I use a personal email?:**

    No. Verification requires an educational email issued by your school.

#### Manage Members

*Add teammates to your workspace and manage the roles that control their access*

**Source:** https://docs.dify.ai/en/cloud/use-dify/workspace/team-members-management

Add teammates to your workspace and manage the roles that control their access

Workspace members are added and managed in **Settings** > **Members**. Each member's access is determined by the role they hold.

#### Team Size Limits

The number of members your workspace can include depends on your subscription plan:

* **Sandbox**: 1 member
* **Professional**: 3 members
* **Team**: 50 members

To raise your team size limit, upgrade your plan from **Settings** > **Billing**.

#### Roles

There are four built-in roles:

* **Owner**: Full control of the workspace. One per workspace.
* **Admin**: Manage members and model providers, plus everything an Editor can do.
* **Editor**: Create, edit, and delete apps and knowledge bases.
* **Normal**: Use published apps only.

> **ℹ️ Info:**
>   The Owner, Admin, and Editor roles can *create* knowledge bases, while who can *see and use* an existing one is controlled in its own settings. See [Manage Knowledge Settings](https://docs.dify.ai/en/cloud/use-dify/knowledge/manage-knowledge/introduction) for details.

#### Add Members

The Owner and Admins can add members.

Select **Add**, enter one or more email addresses, choose a role, and send the invitation. An invitation link will be emailed to each address. The links also appear in the **Invitation sent** dialog, where you can copy and share them directly.

Invitation links expire after 72 hours; if someone doesn't accept in time, invite again to send a fresh link.

#### Manage Members

**Change a role:** The Owner and Admins can change any member's role, and it takes effect on the member's next action, even if they're currently signed in. The Owner's role can only be changed through an ownership transfer.

**Remove a member:** The Owner and Admins can remove any member. This revokes the member's workspace access right away. The apps and knowledge bases they created stay in the workspace. The Owner can't be removed.

**Transfer ownership:** Only the Owner can transfer ownership. The transfer is confirmed with a verification code emailed to the Owner. Once verified, the chosen member becomes the new Owner and the previous Owner becomes an Admin.

#### Dify Tools

*Manage tools that enable LLMs to interact with external services and APIs*

**Source:** https://docs.dify.ai/en/cloud/use-dify/workspace/tools

Manage tools that enable LLMs to interact with external services and APIs

Add tools to your apps so the LLM can call external services and APIs to access real-time data or perform actions, such as web searches, database queries, or content processing.

Use tools in:

* Workflow / Chatflow apps, as standalone [Tool nodes](https://docs.dify.ai/en/cloud/use-dify/nodes/tools) or within [Agent nodes](https://docs.dify.ai/en/cloud/use-dify/nodes/agent#tool-configuration)
* [Agent apps](https://docs.dify.ai/en/cloud/use-dify/build/agent#extend-the-agent-with-dify-tools)

Manage all your tools from **Integrations** > **Tools**.

#### Tool Types

  **Tool Plugin:**

    Ready-to-use tools from Dify and the community for common utilities and popular services. Built-in ones like Current Time work out of the box; install more from the [Marketplace](https://marketplace.dify.ai/).

    Some tool plugins, such as Google and GitHub, need authentication first. Set workspace-level credentials in **Integrations** > **Tools** > **Tool Plugin**, or in the tool's settings inside an app or node.

  **Swagger API:**

    Integrate a service that isn't available as a tool plugin by importing its OpenAPI (Swagger) specification.

    Paste the schema, import it from a URL, or start from the provided example, and Dify generates the tool interface for you.

  **Workflow:**

    Turn any Workflow that starts with a User Input node into a tool, so you can reuse multi-step logic across apps. Chatflows cannot be used as tools.

      *[Image: Workflow as Tool]*

  **MCP:**

    Connect an [MCP server](https://modelcontextprotocol.io/) to import its tools into Dify. An MCP server wraps external resources, such as databases, file systems, or APIs, and exposes them through a standard interface, so your apps can call them like any other tool.

    > **💡 Tip:**
>       To publish one of your own Dify apps *as* an MCP server instead, see [Publish as an MCP Server](https://docs.dify.ai/en/cloud/use-dify/publish/publish-mcp).
>

    ### Connect an MCP Server

    > **ℹ️ Info:**
>       Only MCP servers with [HTTP transport](https://modelcontextprotocol.io/docs/learn/architecture#transport-layer) are supported.
>

    Add a server by providing its URL, a name, and a unique server identifier. Dify connects, authorizes if needed, and imports the server's tools so your apps can call them.

    You can update the tool list later to pull the server's latest tools, though doing so can break an app if a tool it uses is removed or changed.

    > **📝 Note:**
>       * Apps reference a server by its identifier. If you change it later, the server's tools stop working in apps that used the old one; re-add the tools in each affected app to restore them.
>       * Exported apps reference servers by identifier too, so to run one in another workspace, recreate the same servers there with matching identifiers.
>

    ### Authentication

    **Dynamic Client Registration** (on by default) lets Dify obtain OAuth credentials from the server automatically, so you don't register an application yourself. Leave it on whenever the server supports it.

    Turn it off when the server doesn't support automatic registration, or when you must use your team's existing OAuth application. Enter its **Client ID** and **Client Secret**, then register the redirect URL Dify shows.

    ### Advanced Options

    **Custom headers**: Send additional HTTP headers with every request to the server. Commonly used for servers that authenticate with a static token or API key (e.g., `Authorization: Bearer <token>`) rather than OAuth, but applicable whenever the server expects custom headers.

    **Timeouts**: Control how long Dify waits on the server. Raise the request timeout when the server is slow to respond, and the SSE read timeout for long-running, streamed results. Change them only if you hit timeout errors.

---
