# Dify Documentation — REST API Reference

*This document was scraped from the official Dify documentation and cleaned/reformatted for ingestion into NotebookLM (for building a learning plan). It is part of a multi-file set covering the full Dify docs guide.*

- **Source:** https://docs.dify.ai/en/home
- **Total pages in this file:** 93
- **Date scraped:** 2026-07-18

## Table of Contents

- **[API Reference](#api-reference)**
  - [Annotations](#annotations)
    - [Configure Annotation Reply](#configure-annotation-reply)
    - [Create Annotation](#create-annotation)
    - [Delete Annotation](#delete-annotation)
    - [Get Annotation Reply Job Status](#get-annotation-reply-job-status)
    - [List Annotations](#list-annotations)
    - [Update Annotation](#update-annotation)
  - [Applications](#applications)
    - [Get App Info](#get-app-info)
    - [Get App Meta](#get-app-meta)
    - [Get App Parameters](#get-app-parameters)
    - [Get App WebApp Settings](#get-app-webapp-settings)
  - [Audio](#audio)
    - [Convert Audio to Text](#convert-audio-to-text)
    - [Convert Text to Audio](#convert-text-to-audio)
  - [Chat Messages](#chat-messages)
    - [Get Next Suggested Questions](#get-next-suggested-questions)
    - [Send Chat Message](#send-chat-message)
    - [Stop Chat Message Generation](#stop-chat-message-generation)
  - [Chunks](#chunks)
    - [Create Child Chunk](#create-child-chunk)
    - [Create Chunks](#create-chunks)
    - [Delete Child Chunk](#delete-child-chunk)
    - [Delete Chunk](#delete-chunk)
    - [Get Chunk](#get-chunk)
    - [List Child Chunks](#list-child-chunks)
    - [List Chunks](#list-chunks)
    - [Update Child Chunk](#update-child-chunk)
    - [Update Chunk](#update-chunk)
  - [Completion Messages](#completion-messages)
    - [Send Completion Message](#send-completion-message)
    - [Stop Completion Message Generation](#stop-completion-message-generation)
  - [Conversations](#conversations)
    - [Delete Conversation](#delete-conversation)
    - [List Conversation Messages](#list-conversation-messages)
    - [List Conversation Variables](#list-conversation-variables)
    - [List Conversations](#list-conversations)
    - [Rename Conversation](#rename-conversation)
    - [Update Conversation Variable](#update-conversation-variable)
  - [Documents](#documents)
    - [Create Document by File](#create-document-by-file)
    - [Create Document by Text](#create-document-by-text)
    - [Delete Document](#delete-document)
    - [Download Document](#download-document)
    - [Download Documents as ZIP](#download-documents-as-zip)
    - [Get Document](#get-document)
    - [Get Document Indexing Status](#get-document-indexing-status)
    - [List Documents](#list-documents)
    - [Update Document](#update-document)
    - [Update Document by File](#update-document-by-file)
    - [Update Document by Text](#update-document-by-text)
    - [Update Document Status in Batch](#update-document-status-in-batch)
  - [End Users](#end-users)
    - [Get End User Info](#get-end-user-info)
  - [Feedback](#feedback)
    - [List App Feedbacks](#list-app-feedbacks)
    - [Submit Message Feedback](#submit-message-feedback)
  - [Files](#files)
    - [Download File](#download-file)
    - [Upload File](#upload-file)
  - [Guides](#guides)
    - [New Agent API](#new-agent-api)
    - [Chat App API](#chat-app-api)
    - [Chatflow App API](#chatflow-app-api)
    - [Completion App API](#completion-app-api)
    - [End User Identity](#end-user-identity)
    - [Handle Errors and Rate Limits](#handle-errors-and-rate-limits)
    - [Get Started with the Dify API](#get-started-with-the-dify-api)
    - [Human Input API Integration Flow](#human-input-api-integration-flow)
    - [Knowledge API](#knowledge-api)
    - [Consume Streaming Responses](#consume-streaming-responses)
    - [Workflow App API](#workflow-app-api)
  - [Human Input](#human-input)
    - [Get Human Input Form](#get-human-input-form)
    - [Submit Human Input Form](#submit-human-input-form)
  - [Knowledge Bases](#knowledge-bases)
    - [Create an Empty Knowledge Base](#create-an-empty-knowledge-base)
    - [Delete Knowledge Base](#delete-knowledge-base)
    - [Get Knowledge Base](#get-knowledge-base)
    - [List Knowledge Bases](#list-knowledge-bases)
    - [Retrieve Chunks from a Knowledge Base / Test Retrieval](#retrieve-chunks-from-a-knowledge-base-test-retrieval)
    - [Update Knowledge Base](#update-knowledge-base)
  - [Knowledge Pipeline](#knowledge-pipeline)
    - [List Datasource Plugins](#list-datasource-plugins)
    - [Run Datasource Node](#run-datasource-node)
    - [Run Pipeline](#run-pipeline)
    - [Upload Pipeline File](#upload-pipeline-file)
  - [Metadata](#metadata)
    - [Create Metadata Field](#create-metadata-field)
    - [Delete Metadata Field](#delete-metadata-field)
    - [Get Built-in Metadata Fields](#get-built-in-metadata-fields)
    - [List Metadata Fields](#list-metadata-fields)
    - [Update Built-in Metadata Field](#update-built-in-metadata-field)
    - [Update Document Metadata in Batch](#update-document-metadata-in-batch)
    - [Update Metadata Field](#update-metadata-field)
  - [Models](#models)
    - [Get Available Models](#get-available-models)
  - [Tags](#tags)
    - [Create Knowledge Tag](#create-knowledge-tag)
    - [Create Tag Binding](#create-tag-binding)
    - [Delete Knowledge Tag](#delete-knowledge-tag)
    - [Delete Tag Binding](#delete-tag-binding)
    - [Get Knowledge Base Tags](#get-knowledge-base-tags)
    - [List Knowledge Tags](#list-knowledge-tags)
    - [Update Knowledge Tag](#update-knowledge-tag)
  - [Workflow Runs](#workflow-runs)
    - [Get Workflow Run Detail](#get-workflow-run-detail)
    - [List Workflow Logs](#list-workflow-logs)
    - [Run Workflow](#run-workflow)
    - [Run Workflow by ID](#run-workflow-by-id)
    - [Stop Workflow Task](#stop-workflow-task)
    - [Stream Workflow Events](#stream-workflow-events)

---

## API Reference

### Annotations

#### Configure Annotation Reply

***Available for**: Chatflow, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/annotations/configure-annotation-reply

/en/api-reference/openapi_service.json post /apps/annotation-reply/{action}
**Available for**: Chatflow, Chatbot, Agent apps.

Enables or disables annotation reply for the app. Runs asynchronously; track progress with [Get Annotation Reply Job Status](https://docs.dify.ai/en/api-reference/annotations/get-annotation-reply-job-status).

The body is validated before the action runs, so `score_threshold`, `embedding_provider_name`, and `embedding_model_name` are required even for `disable`.

#### Create Annotation

***Available for**: Chatflow, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/annotations/create-annotation

/en/api-reference/openapi_service.json post /apps/annotations
**Available for**: Chatflow, Chatbot, Agent apps.

Creates an annotation. Annotations are predefined question-answer pairs the app returns directly on a match, instead of generating a fresh response.

#### Delete Annotation

***Available for**: Chatflow, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/annotations/delete-annotation

/en/api-reference/openapi_service.json delete /apps/annotations/{annotation_id}
**Available for**: Chatflow, Chatbot, Agent apps.

Deletes an annotation and its associated hit history.

#### Get Annotation Reply Job Status

***Available for**: Chatflow, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/annotations/get-annotation-reply-job-status

/en/api-reference/openapi_service.json get /apps/annotation-reply/{action}/status/{job_id}
**Available for**: Chatflow, Chatbot, Agent apps.

Returns the status of an annotation reply configuration job started by [Configure Annotation Reply](https://docs.dify.ai/en/api-reference/annotations/configure-annotation-reply).

#### List Annotations

***Available for**: Chatflow, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/annotations/list-annotations

/en/api-reference/openapi_service.json get /apps/annotations
**Available for**: Chatflow, Chatbot, Agent apps.

Lists the app's annotations, optionally filtered by keyword.

#### Update Annotation

***Available for**: Chatflow, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/annotations/update-annotation

/en/api-reference/openapi_service.json put /apps/annotations/{annotation_id}
**Available for**: Chatflow, Chatbot, Agent apps.

Updates an annotation's question and answer.

### Applications

#### Get App Info

***Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.*

**Source:** https://docs.dify.ai/en/api-reference/applications/get-app-info

/en/api-reference/openapi_service.json get /info
**Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.

Returns basic information about the app: name, description, tags, mode, and author.

#### Get App Meta

***Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.*

**Source:** https://docs.dify.ai/en/api-reference/applications/get-app-meta

/en/api-reference/openapi_service.json get /meta
**Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.

Returns the display icons for the tools this app uses, keyed by tool name.

#### Get App Parameters

***Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.*

**Source:** https://docs.dify.ai/en/api-reference/applications/get-app-parameters

/en/api-reference/openapi_service.json get /parameters
**Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.

Returns the app's front-end configuration: the opening statement and suggested questions, feature toggles, the user input form, and file-upload limits. Use it to render the app's inputs and apply the correct upload limits.

#### Get App WebApp Settings

***Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.*

**Source:** https://docs.dify.ai/en/api-reference/applications/get-app-webapp-settings

/en/api-reference/openapi_service.json get /site
**Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.

Returns the branding and display settings for the app's hosted WebApp, such as its title, icon, theme colors, and default language.

### Audio

#### Convert Audio to Text

***Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.*

**Source:** https://docs.dify.ai/en/api-reference/audio/convert-audio-to-text

/en/api-reference/openapi_service.json post /audio-to-text
**Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.

Transcribes an uploaded audio file to text using the app's configured speech-to-text model.

#### Convert Text to Audio

***Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.*

**Source:** https://docs.dify.ai/en/api-reference/audio/convert-text-to-audio

/en/api-reference/openapi_service.json post /text-to-audio
**Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.

Converts text to speech audio. Pass `text` to synthesize arbitrary text, or `message_id` to voice an existing message's answer.

### Chat Messages

#### Get Next Suggested Questions

***Available for**: Chatflow, New Agent, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/chat-messages/get-next-suggested-questions

/en/api-reference/openapi_service.json get /messages/{message_id}/suggested
**Available for**: Chatflow, New Agent, Chatbot, Agent apps.

Returns the follow-up questions suggested for a message.

#### Send Chat Message

***Available for**: Chatflow, New Agent, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/chat-messages/send-chat-message

/en/api-reference/openapi_service.json post /chat-messages
**Available for**: Chatflow, New Agent, Chatbot, Agent apps.

Sends a message to a chat app and returns the assistant's reply. The events in the streaming response vary by app type.

#### Stop Chat Message Generation

***Available for**: Chatflow, New Agent, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/chat-messages/stop-chat-message-generation

/en/api-reference/openapi_service.json post /chat-messages/{task_id}/stop
**Available for**: Chatflow, New Agent, Chatbot, Agent apps.

Stops a chat message generation task. Only supported in `streaming` mode.

### Chunks

#### Create Child Chunk

*Create a child chunk under a parent chunk. Intended for documents that use the parent-child (`hierarchical_model`) chunking mode.*

**Source:** https://docs.dify.ai/en/api-reference/chunks/create-child-chunk

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks
Create a child chunk under a parent chunk. Intended for documents that use the parent-child (`hierarchical_model`) chunking mode.

#### Create Chunks

*Create one or more chunks within a document.*

**Source:** https://docs.dify.ai/en/api-reference/chunks/create-chunks

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/documents/{document_id}/segments
Create one or more chunks within a document.

#### Delete Child Chunk

*Permanently delete a child chunk from its parent chunk.*

**Source:** https://docs.dify.ai/en/api-reference/chunks/delete-child-chunk

/en/api-reference/openapi_service.json delete /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}
Permanently delete a child chunk from its parent chunk.

#### Delete Chunk

*Permanently delete a chunk from the document.*

**Source:** https://docs.dify.ai/en/api-reference/chunks/delete-chunk

/en/api-reference/openapi_service.json delete /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}
Permanently delete a chunk from the document.

#### Get Chunk

*Retrieve the full details of a single chunk.*

**Source:** https://docs.dify.ai/en/api-reference/chunks/get-chunk

/en/api-reference/openapi_service.json get /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}
Retrieve the full details of a single chunk.

#### List Child Chunks

*Returns a paginated list of child chunks under a specific parent chunk.*

**Source:** https://docs.dify.ai/en/api-reference/chunks/list-child-chunks

/en/api-reference/openapi_service.json get /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks
Returns a paginated list of child chunks under a specific parent chunk.

#### List Chunks

*Returns a paginated list of chunks within a document, optionally filtered by keyword or indexing status.*

**Source:** https://docs.dify.ai/en/api-reference/chunks/list-chunks

/en/api-reference/openapi_service.json get /datasets/{dataset_id}/documents/{document_id}/segments
Returns a paginated list of chunks within a document, optionally filtered by keyword or indexing status.

#### Update Child Chunk

*Update the content of an existing child chunk.*

**Source:** https://docs.dify.ai/en/api-reference/chunks/update-child-chunk

/en/api-reference/openapi_service.json patch /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}
Update the content of an existing child chunk.

#### Update Chunk

*Update a chunk's fields. The update re-triggers indexing for that chunk.*

**Source:** https://docs.dify.ai/en/api-reference/chunks/update-chunk

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}
Update a chunk's fields. The update re-triggers indexing for that chunk.

### Completion Messages

#### Send Completion Message

***Available for**: Text Generator apps.*

**Source:** https://docs.dify.ai/en/api-reference/completion-messages/send-completion-message

/en/api-reference/openapi_service.json post /completion-messages
**Available for**: Text Generator apps.

Sends a request to a text-generation app and returns the generated text.

#### Stop Completion Message Generation

***Available for**: Text Generator apps.*

**Source:** https://docs.dify.ai/en/api-reference/completion-messages/stop-completion-message-generation

/en/api-reference/openapi_service.json post /completion-messages/{task_id}/stop
**Available for**: Text Generator apps.

Stops a completion message generation task. Only supported in `streaming` mode.

### Conversations

#### Delete Conversation

***Available for**: Chatflow, New Agent, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/conversations/delete-conversation

/en/api-reference/openapi_service.json delete /conversations/{conversation_id}
**Available for**: Chatflow, New Agent, Chatbot, Agent apps.

Deletes a conversation.

#### List Conversation Messages

***Available for**: Chatflow, New Agent, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/conversations/list-conversation-messages

/en/api-reference/openapi_service.json get /messages
**Available for**: Chatflow, New Agent, Chatbot, Agent apps.

Returns a conversation's message history, newest first. Pass `first_id` to page backward into older messages.

#### List Conversation Variables

***Available for**: Chatflow, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/conversations/list-conversation-variables

/en/api-reference/openapi_service.json get /conversations/{conversation_id}/variables
**Available for**: Chatflow, Chatbot, Agent apps.

Lists the variables stored in a conversation.

#### List Conversations

***Available for**: Chatflow, New Agent, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/conversations/list-conversations

/en/api-reference/openapi_service.json get /conversations
**Available for**: Chatflow, New Agent, Chatbot, Agent apps.

Lists an end user's conversations, most recently active first.

#### Rename Conversation

***Available for**: Chatflow, New Agent, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/conversations/rename-conversation

/en/api-reference/openapi_service.json post /conversations/{conversation_id}/name
**Available for**: Chatflow, New Agent, Chatbot, Agent apps.

Renames a conversation, or auto-generates a name from its messages when `auto_generate` is `true`. The name is what clients display in a multi-conversation list.

#### Update Conversation Variable

***Available for**: Chatflow, Chatbot, Agent apps.*

**Source:** https://docs.dify.ai/en/api-reference/conversations/update-conversation-variable

/en/api-reference/openapi_service.json put /conversations/{conversation_id}/variables/{variable_id}
**Available for**: Chatflow, Chatbot, Agent apps.

Updates a conversation variable's value. The new value must match the variable's existing type.

### Documents

#### Create Document by File

*Creates a document in a knowledge base from an uploaded file. Common formats such as PDF, TXT, and DOCX are supported. Indexing runs asynchronously; track it with the returned `batch` ID via [Get Document Indexing Status](https://docs.dify.ai/en/api-reference/documents/get-document-indexing-status).*

**Source:** https://docs.dify.ai/en/api-reference/documents/create-document-by-file

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/document/create-by-file
Creates a document in a knowledge base from an uploaded file. Common formats such as PDF, TXT, and DOCX are supported. Indexing runs asynchronously; track it with the returned `batch` ID via [Get Document Indexing Status](https://docs.dify.ai/en/api-reference/documents/get-document-indexing-status).

#### Create Document by Text

*Creates a document in a knowledge base from raw text. Indexing runs asynchronously; track it with the returned `batch` ID via [Get Document Indexing Status](https://docs.dify.ai/en/api-reference/documents/get-document-indexing-status).*

**Source:** https://docs.dify.ai/en/api-reference/documents/create-document-by-text

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/document/create-by-text
Creates a document in a knowledge base from raw text. Indexing runs asynchronously; track it with the returned `batch` ID via [Get Document Indexing Status](https://docs.dify.ai/en/api-reference/documents/get-document-indexing-status).

#### Delete Document

*Permanently deletes a document and all its chunks from the knowledge base.*

**Source:** https://docs.dify.ai/en/api-reference/documents/delete-document

/en/api-reference/openapi_service.json delete /datasets/{dataset_id}/documents/{document_id}
Permanently deletes a document and all its chunks from the knowledge base.

#### Download Document

*Returns a signed URL for downloading a document's original uploaded file.*

**Source:** https://docs.dify.ai/en/api-reference/documents/download-document

/en/api-reference/openapi_service.json get /datasets/{dataset_id}/documents/{document_id}/download
Returns a signed URL for downloading a document's original uploaded file.

#### Download Documents as ZIP

*Downloads one or more documents as a single ZIP archive. Only documents that were uploaded as files can be included.*

**Source:** https://docs.dify.ai/en/api-reference/documents/download-documents-as-zip

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/documents/download-zip
Downloads one or more documents as a single ZIP archive. Only documents that were uploaded as files can be included.

#### Get Document

*Returns detailed information for a single document.*

**Source:** https://docs.dify.ai/en/api-reference/documents/get-document

/en/api-reference/openapi_service.json get /datasets/{dataset_id}/documents/{document_id}
Returns detailed information for a single document.

#### Get Document Indexing Status

*Returns indexing progress for every document in a batch: the current stage and chunk completion counts. Poll until each `indexing_status` reaches `completed` or `error`. Status advances through `waiting` → `parsing` → `cleaning` → `splitting` → `indexing` → `completed`.*

**Source:** https://docs.dify.ai/en/api-reference/documents/get-document-indexing-status

/en/api-reference/openapi_service.json get /datasets/{dataset_id}/documents/{batch}/indexing-status
Returns indexing progress for every document in a batch: the current stage and chunk completion counts. Poll until each `indexing_status` reaches `completed` or `error`. Status advances through `waiting` → `parsing` → `cleaning` → `splitting` → `indexing` → `completed`.

#### List Documents

*Returns a paginated list of documents in a knowledge base.*

**Source:** https://docs.dify.ai/en/api-reference/documents/list-documents

/en/api-reference/openapi_service.json get /datasets/{dataset_id}/documents
Returns a paginated list of documents in a knowledge base.

#### Update Document

*Updates a document by uploading a new file, then re-indexes it. This is the canonical endpoint for file-based document updates. Track progress with the returned `batch` ID via [Get Document Indexing Status](https://docs.dify.ai/en/api-reference/documents/get-document-indexing-status).*

**Source:** https://docs.dify.ai/en/api-reference/documents/update-document

/en/api-reference/openapi_service.json patch /datasets/{dataset_id}/documents/{document_id}
Updates a document by uploading a new file, then re-indexes it. This is the canonical endpoint for file-based document updates. Track progress with the returned `batch` ID via [Get Document Indexing Status](https://docs.dify.ai/en/api-reference/documents/get-document-indexing-status).

#### Update Document by File

*Deprecated. Use [Update Document](https://docs.dify.ai/en/api-reference/documents/update-document) instead. Updates a document by uploading a new file, then re-indexes it.*

**Source:** https://docs.dify.ai/en/api-reference/documents/update-document-by-file

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/documents/{document_id}/update-by-file
Deprecated. Use [Update Document](https://docs.dify.ai/en/api-reference/documents/update-document) instead. Updates a document by uploading a new file, then re-indexes it.

#### Update Document by Text

*Updates a document's text content, name, or processing configuration. Re-indexes the document when its text changes.*

**Source:** https://docs.dify.ai/en/api-reference/documents/update-document-by-text

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/documents/{document_id}/update-by-text
Updates a document's text content, name, or processing configuration. Re-indexes the document when its text changes.

#### Update Document Status in Batch

*Enables, disables, archives, or unarchives multiple documents in one request.*

**Source:** https://docs.dify.ai/en/api-reference/documents/update-document-status-in-batch

/en/api-reference/openapi_service.json patch /datasets/{dataset_id}/documents/status/{action}
Enables, disables, archives, or unarchives multiple documents in one request.

### End Users

#### Get End User Info

***Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.*

**Source:** https://docs.dify.ai/en/api-reference/end-users/get-end-user-info

/en/api-reference/openapi_service.json get /end-users/{end_user_id}
**Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.

Returns an end user's details by ID. Useful for resolving an end-user ID returned by another endpoint, such as `created_by` in the [Upload File](https://docs.dify.ai/en/api-reference/files/upload-file) response.

### Feedback

#### List App Feedbacks

***Available for**: Chatflow, Chatbot, Agent, Text Generator apps.*

**Source:** https://docs.dify.ai/en/api-reference/feedback/list-app-feedbacks

/en/api-reference/openapi_service.json get /app/feedbacks
**Available for**: Chatflow, Chatbot, Agent, Text Generator apps.

Returns a paginated list of all feedback on the app's messages, including both end-user and admin submissions.

#### Submit Message Feedback

***Available for**: Chatflow, Chatbot, Agent, Text Generator apps.*

**Source:** https://docs.dify.ai/en/api-reference/feedback/submit-message-feedback

/en/api-reference/openapi_service.json post /messages/{message_id}/feedbacks
**Available for**: Chatflow, Chatbot, Agent, Text Generator apps.

Records a `like` or `dislike` rating, plus an optional comment, on a message. Submitting `null` for `rating` revokes the message's existing feedback.

### Files

#### Download File

***Available for**: Chatflow, Chatbot, Agent, Text Generator apps.*

**Source:** https://docs.dify.ai/en/api-reference/files/download-file

/en/api-reference/openapi_service.json get /files/{file_id}/preview
**Available for**: Chatflow, Chatbot, Agent, Text Generator apps.

Returns the raw bytes of a file previously returned by [Upload File](https://docs.dify.ai/en/api-reference/files/upload-file). A file is reachable only through the app whose messages reference it.

#### Upload File

***Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.*

**Source:** https://docs.dify.ai/en/api-reference/files/upload-file

/en/api-reference/openapi_service.json post /files/upload
**Available for**: Chatflow, Workflow, New Agent, Chatbot, Agent, Text Generator apps.

Uploads a file and returns its `id` for later requests to reference. The file belongs to the uploading end user: only requests carrying the same `user` can reference it.

Which file types an app actually consumes depends on its file-upload settings; read them from [Get App Parameters](https://docs.dify.ai/en/api-reference/applications/get-app-parameters).

### Guides

#### New Agent API

*API for New Agent apps, covering streaming chat messages, conversation management, file uploads, and app configuration*

**Source:** https://docs.dify.ai/en/api-reference/guides/agent

API for New Agent apps, covering streaming chat messages, conversation management, file uploads, and app configuration

> **ℹ️ Info:**
>   New Agent is a separate app type from the Agent app (`agent-chat`) covered on [Chatbot and Agent](https://docs.dify.ai/en/api-reference/guides/chat).

[New Agent apps](https://docs.dify.ai/en/self-host/use-dify/build/new-agent/overview) run in `agent` mode: you send a message, stream the reply as it generates, and keep multi-turn context in conversations.

The model reasons and calls tools autonomously, and the stream shows that work: the reply text streams incrementally as `agent_message` events, with `agent_thought` events carrying each reasoning step and tool call alongside.

The turn closes with a single `message` event carrying the complete answer, then `message_end`. Render the `agent_message` deltas live and treat the closing `message` as the final answer rather than appending it.

Each `agent_thought` event carries the step's `thought`, the `tool` it called with its `tool_input`, and the tool's `observation`. The full stream shape is on [Send Chat Message](https://docs.dify.ai/en/api-reference/chat-messages/send-chat-message).

> **ℹ️ Info:**
>   Authentication, the base URL, and the `user` field that scopes end-user data are covered in [Get Started](https://docs.dify.ai/en/api-reference/guides/get-started) and [End User Identity](https://docs.dify.ai/en/api-reference/guides/end-user-identity).

#### Send Messages and Stream Replies

* **[Send Chat Message](https://docs.dify.ai/en/api-reference/chat-messages/send-chat-message)**: send a query to your New Agent app. Streaming mode only; blocking mode returns a 400 `bad_request` error.

  The closing `message_end` event reports token usage; it never includes knowledge-retrieval citations (`retriever_resources`).

* **[Stop Chat Message Generation](https://docs.dify.ai/en/api-reference/chat-messages/stop-chat-message-generation)**: interrupt a streaming reply before it finishes.

* **[Get Next Suggested Questions](https://docs.dify.ai/en/api-reference/chat-messages/get-next-suggested-questions)**: propose follow-up questions after a reply completes, based on the conversation so far.

#### Manage Conversations

* **[List Conversations](https://docs.dify.ai/en/api-reference/conversations/list-conversations)**: the current user's conversations, ordered by most recent activity.
* **[List Conversation Messages](https://docs.dify.ai/en/api-reference/conversations/list-conversation-messages)**: one conversation's message history, for a scrolling chat UI. Each message's `agent_thoughts` array carries the reasoning steps for that turn.
* **[Rename Conversation](https://docs.dify.ai/en/api-reference/conversations/rename-conversation)**: set a conversation's name, or have one generated from its content.
* **[Delete Conversation](https://docs.dify.ai/en/api-reference/conversations/delete-conversation)**: remove a conversation and its messages.

#### Upload Files

* **[Upload File](https://docs.dify.ai/en/api-reference/files/upload-file)**: upload an image, document, audio, or video file, scoped to the uploading end user.

  Files passed to [Send Chat Message](https://docs.dify.ai/en/api-reference/chat-messages/send-chat-message) are surfaced to the agent as downloadable references it can fetch and inspect in its sandbox.

* **[Get End User Info](https://docs.dify.ai/en/api-reference/end-users/get-end-user-info)**: look up an end user's details from an end-user ID, such as the `created_by` in the Upload File response.

#### Transcribe and Synthesize Speech

* **[Convert Audio to Text](https://docs.dify.ai/en/api-reference/audio/convert-audio-to-text)**: transcribe an uploaded audio file (MP3, M4A, WAV, AMR, or MPGA, up to 30 MB) so end users can speak their input instead of typing it.
* **[Convert Text to Audio](https://docs.dify.ai/en/api-reference/audio/convert-text-to-audio)**: synthesize a reply back into speech.

#### Retrieve App Info and Settings

* **[Get App Info](https://docs.dify.ai/en/api-reference/applications/get-app-info)**: the app's name, description, tags, and mode.
* **[Get App Parameters](https://docs.dify.ai/en/api-reference/applications/get-app-parameters)**: the fields your calls send in `inputs` (names, types, defaults) plus the app's feature switches—the basis for building requests or a client UI.
* **[Get App Meta](https://docs.dify.ai/en/api-reference/applications/get-app-meta)**: app metadata; the `tool_icons` map is empty for New Agent apps.
* **[Get App WebApp Settings](https://docs.dify.ai/en/api-reference/applications/get-app-webapp-settings)**: the WebApp's site configuration, theme, and customization options.

#### Chat App API

*API for Chatbot and Agent apps, covering chat messages, conversation management, file uploads, voice, and annotations*

**Source:** https://docs.dify.ai/en/api-reference/guides/chat

API for Chatbot and Agent apps, covering chat messages, conversation management, file uploads, voice, and annotations

[Chatbot apps](https://docs.dify.ai/en/cloud/use-dify/build/chatbot) (`chat` mode) and [Agent apps](https://docs.dify.ai/en/cloud/use-dify/build/agent) (`agent-chat` mode) share the same endpoints to send messages, manage conversations, handle files, and retrieve app settings. Only the streamed reply differs: Chatbot apps stream the reply as `message` events, while Agent apps stream `agent_thought` and `agent_message` events.

> **ℹ️ Info:**
>   Authentication, the base URL, and the `user` field that scopes end-user data are covered in [Get Started](https://docs.dify.ai/en/api-reference/guides/get-started) and [End User Identity](https://docs.dify.ai/en/api-reference/guides/end-user-identity).

#### Send Messages and Stream Replies

* **[Send Chat Message](https://docs.dify.ai/en/api-reference/chat-messages/send-chat-message)**: send a query to your Chatbot or Agent app. Blocking mode returns the full reply once it finishes; Agent apps support streaming mode only.
* **[Stop Chat Message Generation](https://docs.dify.ai/en/api-reference/chat-messages/stop-chat-message-generation)**: interrupt a streaming reply before it finishes.
* **[Get Next Suggested Questions](https://docs.dify.ai/en/api-reference/chat-messages/get-next-suggested-questions)**: propose follow-up questions after a reply completes, based on the conversation so far.

#### Manage Conversations

Conversations created through the API stay isolated from conversations started in the app's WebApp.

* **[List Conversations](https://docs.dify.ai/en/api-reference/conversations/list-conversations)**: the current user's conversations, ordered by most recent activity.
* **[List Conversation Messages](https://docs.dify.ai/en/api-reference/conversations/list-conversation-messages)**: one conversation's message history, for a scrolling chat UI.
* **[Rename Conversation](https://docs.dify.ai/en/api-reference/conversations/rename-conversation)**: set or auto-generate a display name.
* **[Delete Conversation](https://docs.dify.ai/en/api-reference/conversations/delete-conversation)**: remove a conversation.
* **[List Conversation Variables](https://docs.dify.ai/en/api-reference/conversations/list-conversation-variables)**: read the values the session persists across turns.
* **[Update Conversation Variable](https://docs.dify.ai/en/api-reference/conversations/update-conversation-variable)**: change one of those values directly.

#### Handle Files

* **[Upload File](https://docs.dify.ai/en/api-reference/files/upload-file)**: upload an image, document, audio, or video file for [Send Chat Message](https://docs.dify.ai/en/api-reference/chat-messages/send-chat-message) to reference. Files are scoped to the uploading end user.
* **[Download File](https://docs.dify.ai/en/api-reference/files/download-file)**: preview or download an uploaded file, as long as it belongs to a message in your app.
* **[Get End User Info](https://docs.dify.ai/en/api-reference/end-users/get-end-user-info)**: look up an end user's details from an end-user ID, such as the `created_by` in the Upload File response.

#### Transcribe and Synthesize Speech

* **[Convert Audio to Text](https://docs.dify.ai/en/api-reference/audio/convert-audio-to-text)**: transcribe an uploaded audio file (MP3, M4A, WAV, AMR, or MPGA, up to 30 MB) so end users can speak their input instead of typing it.
* **[Convert Text to Audio](https://docs.dify.ai/en/api-reference/audio/convert-text-to-audio)**: synthesize a reply back into speech.

#### Retrieve App Info and Settings

* **[Get App Info](https://docs.dify.ai/en/api-reference/applications/get-app-info)**: the app's name, description, tags, and mode.
* **[Get App Parameters](https://docs.dify.ai/en/api-reference/applications/get-app-parameters)**: the fields your calls send in `inputs` (names, types, defaults) plus the app's feature switches—the basis for building requests or a client UI.
* **[Get App Meta](https://docs.dify.ai/en/api-reference/applications/get-app-meta)**: tool icons and other configuration metadata.
* **[Get App WebApp Settings](https://docs.dify.ai/en/api-reference/applications/get-app-webapp-settings)**: the WebApp's site configuration, theme, and customization options.

#### Collect Feedback

* **[Submit Message Feedback](https://docs.dify.ai/en/api-reference/feedback/submit-message-feedback)**: end users rate a reply as `like` or `dislike`, with an optional text comment.
* **[List App Feedbacks](https://docs.dify.ai/en/api-reference/feedback/list-app-feedbacks)**: every feedback submitted across the app, from both end users and admins.

#### Manage Annotations

Annotations pair a question with a fixed answer that the app returns directly instead of generating a new response:

* **[Create Annotation](https://docs.dify.ai/en/api-reference/annotations/create-annotation)**, **[List Annotations](https://docs.dify.ai/en/api-reference/annotations/list-annotations)**, **[Update Annotation](https://docs.dify.ai/en/api-reference/annotations/update-annotation)**, **[Delete Annotation](https://docs.dify.ai/en/api-reference/annotations/delete-annotation)**: manage the annotation set.
* **[Configure Annotation Reply](https://docs.dify.ai/en/api-reference/annotations/configure-annotation-reply)**: turn annotation matching on or off. The change runs asynchronously.
* **[Get Annotation Reply Job Status](https://docs.dify.ai/en/api-reference/annotations/get-annotation-reply-job-status)**: poll with the returned job ID to confirm the change finished.

#### Chatflow App API

*API for Chatflow apps, covering chat messages, workflow-level streaming, conversation management, and Human Input pauses*

**Source:** https://docs.dify.ai/en/api-reference/guides/chatflow

API for Chatflow apps, covering chat messages, workflow-level streaming, conversation management, and Human Input pauses

[Chatflow apps](https://docs.dify.ai/en/cloud/use-dify/build/workflow-chatflow) run in `advanced-chat` mode, streaming workflow-level events (node starts, finishes, iterations, and pauses) alongside the reply. Previous turns persist as context, so later messages can reference earlier ones.

> **ℹ️ Info:**
>   Authentication, the base URL, and the `user` field that scopes end-user data are covered in [Get Started](https://docs.dify.ai/en/api-reference/guides/get-started) and [End User Identity](https://docs.dify.ai/en/api-reference/guides/end-user-identity).

#### Send Messages and Stream Replies

* **[Send Chat Message](https://docs.dify.ai/en/api-reference/chat-messages/send-chat-message)**: send a query to your Chatflow app. Streaming mode carries workflow and node events alongside the answer text; blocking mode returns once the run finishes.
* **[Stop Chat Message Generation](https://docs.dify.ai/en/api-reference/chat-messages/stop-chat-message-generation)**: interrupt a streaming reply before it finishes.
* **[Get Next Suggested Questions](https://docs.dify.ai/en/api-reference/chat-messages/get-next-suggested-questions)**: propose follow-up questions after a reply completes, based on the conversation so far.

#### Manage Conversations

* **[List Conversations](https://docs.dify.ai/en/api-reference/conversations/list-conversations)**: the current user's conversations, ordered by most recent activity.
* **[List Conversation Messages](https://docs.dify.ai/en/api-reference/conversations/list-conversation-messages)**: one conversation's message history, for a scrolling chat UI.
* **[Rename Conversation](https://docs.dify.ai/en/api-reference/conversations/rename-conversation)**: set or auto-generate a display name.
* **[Delete Conversation](https://docs.dify.ai/en/api-reference/conversations/delete-conversation)**: remove a conversation.
* **[List Conversation Variables](https://docs.dify.ai/en/api-reference/conversations/list-conversation-variables)**: read the values the session persists across turns.
* **[Update Conversation Variable](https://docs.dify.ai/en/api-reference/conversations/update-conversation-variable)**: change one of those values directly.

#### Handle Files

* **[Upload File](https://docs.dify.ai/en/api-reference/files/upload-file)**: upload an image, document, audio, or video file for [Send Chat Message](https://docs.dify.ai/en/api-reference/chat-messages/send-chat-message) to reference. Files are scoped to the uploading end user.
* **[Download File](https://docs.dify.ai/en/api-reference/files/download-file)**: preview or download an uploaded file, as long as it belongs to a message in your app.
* **[Get End User Info](https://docs.dify.ai/en/api-reference/end-users/get-end-user-info)**: look up an end user's details from an end-user ID, such as the `created_by` in the Upload File response.

#### Transcribe and Synthesize Speech

* **[Convert Audio to Text](https://docs.dify.ai/en/api-reference/audio/convert-audio-to-text)**: transcribe an uploaded audio file (MP3, M4A, WAV, AMR, or MPGA, up to 30 MB) so end users can speak their input instead of typing it.
* **[Convert Text to Audio](https://docs.dify.ai/en/api-reference/audio/convert-text-to-audio)**: synthesize a reply back into speech.

#### Pause for Human Input

When a run reaches a [Human Input node](https://docs.dify.ai/en/cloud/use-dify/nodes/human-input) whose delivery method is WebApp, complete the pause over the API:

  1. **Listen for the pause**
        The event stream emits `human_input_required` carrying a `form_token` and the run's `workflow_run_id`, then ends with the `workflow_paused` event.

  1. **Fetch the form**
        Load the form's contents with [Get Human Input Form](https://docs.dify.ai/en/api-reference/human-input/get-human-input-form), using the `form_token`.

  1. **Submit the response**
        Send the recipient's input with [Submit Human Input Form](https://docs.dify.ai/en/api-reference/human-input/submit-human-input-form). Submitting resumes the run.

  1. **Resume the stream**
        Open a new stream with [Stream Workflow Events](https://docs.dify.ai/en/api-reference/workflow-runs/stream-workflow-events), using the `workflow_run_id` from the paused stream, and follow the remaining events through the final answer.

For file-attached submissions and the full event sequence, see the [Human Input Flow](https://docs.dify.ai/en/api-reference/guides/human-input-flow) guide.

#### Inspect Workflow Runs

* **[Get Workflow Run Detail](https://docs.dify.ai/en/api-reference/workflow-runs/get-workflow-run-detail)**: a run's status and outputs, by the `workflow_run_id` that appears in the workflow and node events streamed alongside a chat reply.
* **[List Workflow Logs](https://docs.dify.ai/en/api-reference/workflow-runs/list-workflow-logs)**: run-level summaries covering status, token usage, step count, and timing, rather than a node-by-node execution log.

#### Retrieve App Info and Settings

* **[Get App Info](https://docs.dify.ai/en/api-reference/applications/get-app-info)**: the app's name, description, tags, and mode.
* **[Get App Parameters](https://docs.dify.ai/en/api-reference/applications/get-app-parameters)**: the fields your calls send in `inputs` (names, types, defaults) plus the app's feature switches—the basis for building requests or a client UI.
* **[Get App Meta](https://docs.dify.ai/en/api-reference/applications/get-app-meta)**: tool icons and other configuration metadata.
* **[Get App WebApp Settings](https://docs.dify.ai/en/api-reference/applications/get-app-webapp-settings)**: the WebApp's site configuration, theme, and customization options.

#### Collect Feedback and Annotations

* **[Submit Message Feedback](https://docs.dify.ai/en/api-reference/feedback/submit-message-feedback)**: end users rate a reply as `like` or `dislike`, with an optional text comment.
* **[List App Feedbacks](https://docs.dify.ai/en/api-reference/feedback/list-app-feedbacks)**: every feedback submitted across the app, from both end users and admins.

Annotations pair a question with a fixed answer that the app returns directly instead of generating a new response:

* **[Create Annotation](https://docs.dify.ai/en/api-reference/annotations/create-annotation)**, **[List Annotations](https://docs.dify.ai/en/api-reference/annotations/list-annotations)**, **[Update Annotation](https://docs.dify.ai/en/api-reference/annotations/update-annotation)**, **[Delete Annotation](https://docs.dify.ai/en/api-reference/annotations/delete-annotation)**: manage the annotation set.
* **[Configure Annotation Reply](https://docs.dify.ai/en/api-reference/annotations/configure-annotation-reply)**: turn annotation matching on or off. The change runs asynchronously.
* **[Get Annotation Reply Job Status](https://docs.dify.ai/en/api-reference/annotations/get-annotation-reply-job-status)**: poll with the returned job ID to confirm the change finished.

#### Completion App API

*API for Text Generator apps, covering completion messages, file uploads, voice, and feedback*

**Source:** https://docs.dify.ai/en/api-reference/guides/completion

API for Text Generator apps, covering completion messages, file uploads, voice, and feedback

[Text Generator apps](https://docs.dify.ai/en/cloud/use-dify/build/text-generator) run in `completion` mode: each call submits its own input values and returns one response, with no conversation state carried between calls.

> **ℹ️ Info:**
>   Authentication, the base URL, and the `user` field that scopes end-user data are covered in [Get Started](https://docs.dify.ai/en/api-reference/guides/get-started) and [End User Identity](https://docs.dify.ai/en/api-reference/guides/end-user-identity).

#### Generate Text

* **[Send Completion Message](https://docs.dify.ai/en/api-reference/completion-messages/send-completion-message)**: send `inputs` to fill the app's prompt template and generate a response. Blocking mode returns the full response once it finishes; streaming mode delivers `message` events ending in `message_end`, plus `tts_message` events when the app has text-to-speech auto-play enabled.
* **[Stop Completion Message Generation](https://docs.dify.ai/en/api-reference/completion-messages/stop-completion-message-generation)**: interrupt a streaming response before it finishes.

#### Handle Files

* **[Upload File](https://docs.dify.ai/en/api-reference/files/upload-file)**: upload an image, document, audio, or video file for [Send Completion Message](https://docs.dify.ai/en/api-reference/completion-messages/send-completion-message) to reference. Files are scoped to the uploading end user.
* **[Download File](https://docs.dify.ai/en/api-reference/files/download-file)**: preview or download an uploaded file, as long as it belongs to a message in your app.
* **[Get End User Info](https://docs.dify.ai/en/api-reference/end-users/get-end-user-info)**: look up an end user's details from an end-user ID, such as the `created_by` in the Upload File response.

#### Transcribe and Synthesize Speech

* **[Convert Audio to Text](https://docs.dify.ai/en/api-reference/audio/convert-audio-to-text)**: transcribe an uploaded audio file (MP3, M4A, WAV, AMR, or MPGA, up to 30 MB) so end users can speak their input instead of typing it.
* **[Convert Text to Audio](https://docs.dify.ai/en/api-reference/audio/convert-text-to-audio)**: synthesize the generated response back into speech.

#### Retrieve App Info and Settings

* **[Get App Info](https://docs.dify.ai/en/api-reference/applications/get-app-info)**: the app's name, description, tags, and mode.
* **[Get App Parameters](https://docs.dify.ai/en/api-reference/applications/get-app-parameters)**: the fields your calls send in `inputs` (names, types, defaults) plus the app's feature switches—the basis for building requests or a client UI.
* **[Get App Meta](https://docs.dify.ai/en/api-reference/applications/get-app-meta)**: tool icons and other configuration metadata.
* **[Get App WebApp Settings](https://docs.dify.ai/en/api-reference/applications/get-app-webapp-settings)**: the WebApp's site configuration, theme, and customization options.

#### Collect Feedback

* **[Submit Message Feedback](https://docs.dify.ai/en/api-reference/feedback/submit-message-feedback)**: end users rate a response as `like` or `dislike`, with an optional text comment.
* **[List App Feedbacks](https://docs.dify.ai/en/api-reference/feedback/list-app-feedbacks)**: every feedback submitted across the app, from both end users and admins.

#### End User Identity

*What the user field identifies, what it scopes, and why it must stay consistent across calls*

**Source:** https://docs.dify.ai/en/api-reference/guides/end-user-identity

What the user field identifies, what it scopes, and why it must stay consistent across calls

Most app endpoints take a `user` field: your own identifier for the end user a call acts on behalf of. Dify never authenticates it, so pick a stable value per person, such as an account ID, and send it consistently.

Dify starts tracking a new `user` the first time it appears, and one app key serves any number of end users.

#### What `user` Scopes

`user` controls what each call can see and do:

* **Conversations**: listing, history, renaming, and deletion all operate on that user's conversations only.

* **Files**: an upload belongs to the uploading user, and referencing it under a different `user` fails.

* **Stopping generation**: the chat-family stop endpoints act only when `user` matches the one that started the reply. A mismatch is silently ignored—the call succeeds either way, so it isn't detectable from the response.

  Workflow's Stop Workflow Task does not check `user`.

* **Resuming runs**: [Stream Workflow Events](https://docs.dify.ai/en/api-reference/workflow-runs/stream-workflow-events) returns a 404 when `user` doesn't match the run's creator.

Keep one `user` per person across every call in a flow—upload, send, stop, and resume all check it.

#### API Users and WebApp Users Stay Separate

Traffic through the API and Dify's hosted WebApp keep separate identities: conversations your API users create never appear in the WebApp, and WebApp conversations never appear through the API.

#### Resolve an End-User ID

Some responses carry an end-user ID instead of full details, such as `created_by` in the Upload File response. [Get End User Info](https://docs.dify.ai/en/api-reference/end-users/get-end-user-info) resolves it.

#### Handle Errors and Rate Limits

*The error envelope, what each status class means, and which failures are worth retrying*

**Source:** https://docs.dify.ai/en/api-reference/guides/errors

The error envelope, what each status class means, and which failures are worth retrying

Every documented error uses the same three-field JSON envelope:

```json theme={null}
{
  "code": "invalid_param",
  "message": "user is required",
  "status": 400
}
```

`status` mirrors the HTTP status; `code` is the stable identifier to branch on; `message` is human-readable detail. Each endpoint page lists exactly which codes it can raise.

#### Status Classes at a Glance

| Status    | Meaning                                                           | Typical codes                                                              |
| :-------- | :---------------------------------------------------------------- | :------------------------------------------------------------------------- |
| 400       | The request or the app's configuration is invalid                 | `invalid_param`, `bad_request`, `app_unavailable`, provider errors (below) |
| 401       | Missing or invalid API key                                        | `unauthorized`                                                             |
| 403       | The key can't act here: access restrictions or plan limits        | `forbidden`                                                                |
| 404       | The resource doesn't exist or isn't visible to this key or `user` | `not_found`                                                                |
| 413 / 415 | A file is too large or of an unsupported type                     | `file_too_large`, `unsupported_file_type`                                  |
| 429       | Too many requests right now, or a quota is exhausted              | `too_many_requests`, `rate_limit_error`                                    |
| 500       | Something failed on Dify's side                                   | `internal_server_error`                                                    |

#### Provider Errors Are Configuration Errors

Four common 400 codes point at the app's model setup rather than your request:

* `provider_not_initialize`: no valid model credentials
* `provider_quota_exceeded`: the model provider's own quota ran out
* `model_currently_not_support`: the model isn't currently supported
* `completion_request_error`: an error occurred while making a completion request

For these errors, retrying won't help. Fix the app's model configuration in Dify.

#### Rate Limits and Quotas

The two 429 codes mean different things:

* `too_many_requests` is a concurrency ceiling—too many simultaneous requests for the app right now. Back off and retry.
* `rate_limit_error` is a plan quota on Dify Cloud, such as workflow executions. Retrying won't clear it; it resets with the quota period or a plan change.

On Dify Cloud, knowledge write endpoints also enforce plan limits as `403` responses. These carry the same `forbidden` code as access restrictions—the `message` is what tells you it's a plan limit, so don't build a switch on `code` alone for 403s.

#### Errors Inside Streams

Once a stream opens, the HTTP status is already `200`: failures arrive as an `error` event and end the stream. The event's `code` values are the same ones documented here—classify them with the same rules. See [Consume Streaming Responses](https://docs.dify.ai/en/api-reference/guides/streaming) for details.

#### What to Retry

* **Retry with backoff**: `too_many_requests`, `500`, and network failures.

* **Don't retry as-is**: validation errors (fix the request first), authorization failures, or quota errors (they won't clear until the quota does).

* **Fix, don't retry**: a `404` from a resume call means the wrong `user` or a run that doesn't exist. Correct the identifier instead.

#### Get Started with the Dify API

*Get an API key, make your first call, and find the endpoints for your app type*

**Source:** https://docs.dify.ai/en/api-reference/guides/get-started

Get an API key, make your first call, and find the endpoints for your app type

Every app you publish in Dify doubles as a REST API, and so do your knowledge bases. You call the same app your end users interact with, from your own backend, with an API key.

#### Get an API Key

> **⚠️ Warning:**
>   Call the API from your backend only. A key embedded in frontend code or a client app can be extracted and abused.

* For an app, create an API key from inside the app itself. The key is scoped to that one app, and one key serves all your end users.

  > **ℹ️ Info:**
>     Your calls tell people apart with a per-person `user` value. See [End User Identity](https://docs.dify.ai/en/api-reference/guides/end-user-identity) for details.
>

* For knowledge bases, go to **Knowledge** and click **Service API** in the top-right corner.

  A knowledge API key is broader: it can reach every knowledge base visible to the account that created the key, so treat it with extra care. See [Knowledge API](https://docs.dify.ai/en/api-reference/guides/knowledge) for details.

#### Make Your First Call

Every request carries the key as a Bearer token. For Dify Cloud, the base URL is `https://api.dify.ai/v1`; for self-hosted deployments, use your own instance's API base URL.

The fastest first call needs no code: open [Get App Info](https://docs.dify.ai/en/api-reference/applications/get-app-info), click **Try it**, paste your key into the **Authorization** field, and press **Send**. It works for every app type.

The same call from a terminal:

```bash theme={null}
curl https://api.dify.ai/v1/info \
  -H "Authorization: Bearer $DIFY_API_KEY"
```

A response like this confirms the key works and shows which app it belongs to:

```json theme={null}
{
  "name": "My Chat App",
  "description": "A helpful assistant",
  "tags": ["assistant"],
  "mode": "chat",
  "author_name": "Dify Team"
}
```

Using a knowledge API key? Its endpoints are a separate family: start with [List Knowledge Bases](https://docs.dify.ai/en/api-reference/knowledge-bases/list-knowledge-bases) instead.

#### Find Your App Type's Endpoints

See each app type's own overview page for its full API surface:

* [Chatflow](https://docs.dify.ai/en/api-reference/guides/chatflow) (`advanced-chat`)
* [Workflow](https://docs.dify.ai/en/api-reference/guides/workflow) (`workflow`)
* [New Agent](https://docs.dify.ai/en/api-reference/guides/agent) (`agent`)
* [Chatbot and Agent](https://docs.dify.ai/en/api-reference/guides/chat) (`chat`, `agent-chat`)
* [Text Generator](https://docs.dify.ai/en/api-reference/guides/completion) (`completion`)
* [Knowledge](https://docs.dify.ai/en/api-reference/guides/knowledge)

#### Human Input API Integration Flow

*End-to-end sequence for handling a paused Human Input form via the API*

**Source:** https://docs.dify.ai/en/api-reference/guides/human-input-flow

End-to-end sequence for handling a paused Human Input form via the API

When a workflow reaches a [Human Input node](https://docs.dify.ai/en/cloud/use-dify/nodes/human-input), it pauses and emits a `human_input_required` event in the streaming response. The event carries a `form_token` that your integration uses to drive the form lifecycle until the workflow resumes.

For per-endpoint reference, see the [Human Input API](https://docs.dify.ai/en/api-reference/human-input/get-human-input-form).

#### Steps

The sequence below applies to both Workflow and Chatflow apps. Only the entry endpoint in Step 1 differs between the two.

  1. **Start the app in streaming mode**
        1. Call [Run Workflow](https://docs.dify.ai/en/api-reference/workflow-runs/run-workflow) (Workflow apps) or [Send Chat Message](https://docs.dify.ai/en/api-reference/chat-messages/send-chat-message) (Chatflow apps), passing your end user's `user` identifier.
        2. Watch the SSE stream for the `human_input_required` event and capture its `form_token`.

           If `form_token` is `null`, the form uses Email delivery and can't be driven via the API (see [Delivery Method Requirement](#delivery-method-requirement)).

           The `human_input_required` event also carries the run's `workflow_run_id`; keep it in case you need to resume listening in Step 5.

  1. **Get the form definition**
        Call [Get Human Input Form](https://docs.dify.ai/en/api-reference/human-input/get-human-input-form) with `form_token`. The response includes the rendered Markdown, input field definitions, available actions, pre-filled default values, and an `expiration_time` after which the form can no longer be submitted. Render the form for the recipient.

        If the form expires before it is submitted, the paused run follows the node's configured timeout behavior; a resumed stream then carries `human_input_form_timeout` rather than `human_input_form_filled`.

  1. **(File inputs only) Upload local files**
        If the recipient attaches a local file to a `file` or `file-list` input, upload it first with [Upload File](https://docs.dify.ai/en/api-reference/files/upload-file). It returns an `id` you reference as `upload_file_id` in the submit payload. Use one consistent `user` across the run, upload, and submit calls (see [End User Identity](https://docs.dify.ai/en/api-reference/guides/end-user-identity) for details).

        A remote file needs no upload step: attach it inline in the submit as a `{transfer_method: remote_url, url}` mapping.

  1. **Submit the response**
        Call [Submit Human Input Form](https://docs.dify.ai/en/api-reference/human-input/submit-human-input-form) with the recipient's input values, the selected `action`, and your `user`. The `action` must be one of the actions from the form definition in Step 2.

        File inputs accept either a `{transfer_method: local_file, upload_file_id}` mapping (from Step 3) or an inline `{transfer_method: remote_url, url}` mapping. See [Upload First vs. Inline Remote URL](#upload-first-vs-inline-remote-url) for the trade-off.

        A successful submit is final: it closes the form and resumes the run along the matching action branch, so the same `form_token` can't be submitted again.

        A rejected submit (an invalid action, a missing required input, or a failed remote-file fetch) leaves the form unchanged—fix the inputs and resubmit with the same `form_token`.

  1. **Resume listening to the workflow**
        If the original SSE stream closed, reopen it via [Stream Workflow Events](https://docs.dify.ai/en/api-reference/workflow-runs/stream-workflow-events) with the `workflow_run_id` from Step 1 and the same `user` that started the run—a different `user` gets a 404.

        The resumed stream includes `human_input_form_filled` confirming the submission (or `human_input_form_timeout` if the form expired), then the remaining node events through to completion, like a run that never paused.

        Add `include_state_snapshot=true` to first replay the status of nodes that already executed. If the workflow has more than one Human Input node in sequence, the stream closes at each pause by default; pass `continue_on_pause=true` to keep one stream open across all of them.

#### Upload First vs. Inline Remote URL

Both patterns work for file inputs:

* **Pre-upload, then reference `upload_file_id`** (recommended)

  [Upload File](https://docs.dify.ai/en/api-reference/files/upload-file) enforces the file size limits at upload time, so the recipient gets immediate feedback and can retry before committing the whole submission.

* **Submit inline with `transfer_method: remote_url`**

  The backend fetches the file at submit time. Faster to integrate, but any size, type, or fetch failure rejects the entire submission, forcing the recipient to redo other fields.

> **💡 Tip:**
>   For interactive forms with recipient feedback, prefer the pre-upload pattern. The trade-off only pays off when the integration is fully programmatic and no human is waiting to retype anything.

#### Delivery Method Requirement

The Human Input API works only with forms delivered via the Human Input node's WebApp method. Email-only delivery doesn't expose a `form_token`.

#### Example: File-Attached Submission

This example uses a form with a `feedback` paragraph input, an `attachments` file-list input, and `approve` / `reject` actions.

1. Call [Get Human Input Form](https://docs.dify.ai/en/api-reference/human-input/get-human-input-form) to get the form definition:

   ```http theme={null}
   GET /form/human_input/
   Authorization: Bearer {api-key}
   ```

   Returns the form definition:

   ```json theme={null}
   {
     "form_content": "Please review the draft and confirm or request changes.",
     "inputs": [
       {
         "type": "paragraph",
         "output_variable_name": "feedback",
         "default": {
           "type": "constant",
           "selector": [],
           "value": ""
         }
       },
       {
         "type": "file-list",
         "output_variable_name": "attachments",
         "allowed_file_types": [
           "image",
           "document"
         ],
         "allowed_file_extensions": [],
         "allowed_file_upload_methods": [
           "local_file",
           "remote_url"
         ],
         "number_limits": 5
       }
     ],
     "resolved_default_values": {},
     "user_actions": [
       {
         "id": "approve",
         "title": "Approve",
         "button_style": "primary"
       },
       {
         "id": "reject",
         "title": "Request changes",
         "button_style": "default"
       }
     ],
     "expiration_time": 1745510400
   }
   ```

2. For each local file, call [Upload File](https://docs.dify.ai/en/api-reference/files/upload-file):

   ```http theme={null}
   POST /files/upload
   Authorization: Bearer {api-key}
   Content-Type: multipart/form-data

   file=<binary>
   user=abc-123
   ```

   Returns `{"id": "1a77f0df-...", ...}`.

3. Call [Submit Human Input Form](https://docs.dify.ai/en/api-reference/human-input/submit-human-input-form) with the recipient's input and selected action:

   ```http theme={null}
   POST /form/human_input/
   Authorization: Bearer {api-key}
   Content-Type: application/json

   {
     "inputs": {
       "feedback": "Looks good to ship",
       "attachments": [
         {"transfer_method": "local_file", "upload_file_id": "1a77f0df-..."}
       ]
     },
     "action": "approve",
     "user": "abc-123"
   }
   ```

   Returns `{}`. The workflow resumes along the `approve` branch.

4. Reconnect to the run's stream with [Stream Workflow Events](https://docs.dify.ai/en/api-reference/workflow-runs/stream-workflow-events) to follow it through to completion, as in Step 5 of the sequence above.

#### Knowledge API

*API for managing knowledge bases, documents, chunks, metadata, tags, and knowledge pipelines*

**Source:** https://docs.dify.ai/en/api-reference/guides/knowledge

API for managing knowledge bases, documents, chunks, metadata, tags, and knowledge pipelines

Build and maintain [knowledge bases](https://docs.dify.ai/en/cloud/use-dify/knowledge/readme) from your own code, without going through the Dify console: create a knowledge base, load documents and chunks into it, organize them with metadata and tags, and query it directly for search or RAG.

> **📝 Note:**
>   A single Knowledge Base API key has access to every knowledge base visible to the account that created the key. Handle your keys carefully to avoid unintended data exposure.

#### Get Your API Endpoint and Key

In **Knowledge**, click **Service API** in the top-right corner to open the API configuration panel. From here:

* Copy the Service API endpoint, the base URL for every Knowledge API request.
* Click **API Key** to create and manage keys.

> **⚠️ Warning:**
>   Store your API key securely on the server side. Never expose it in client-side code or public repositories.

#### Manage API Access for a Knowledge Base

Every knowledge base is reachable through the API by default. To restrict a specific knowledge base, open it, click **API Access** in the bottom-left corner, and turn the toggle off.

#### Create and Manage Knowledge Bases

* **[Create an Empty Knowledge Base](https://docs.dify.ai/en/api-reference/knowledge-bases/create-an-empty-knowledge-base)**: create a knowledge base with no documents yet.
* **[List Knowledge Bases](https://docs.dify.ai/en/api-reference/knowledge-bases/list-knowledge-bases)**: a paginated list, filterable by keyword or tag.
* **[Get Knowledge Base](https://docs.dify.ai/en/api-reference/knowledge-bases/get-knowledge-base)**: one knowledge base's embedding model, retrieval configuration, and document statistics.
* **[Update Knowledge Base](https://docs.dify.ai/en/api-reference/knowledge-bases/update-knowledge-base)**: change the name, permissions, embedding model, or retrieval settings; only the fields you provide are updated.
* **[Delete Knowledge Base](https://docs.dify.ai/en/api-reference/knowledge-bases/delete-knowledge-base)**: permanently remove a knowledge base and every document inside it.
* **[Retrieve Chunks from a Knowledge Base / Test Retrieval](https://docs.dify.ai/en/api-reference/knowledge-bases/retrieve-chunks-from-a-knowledge-base-test-retrieval)**: search a knowledge base and return the most relevant chunks—the same endpoint serves production retrieval and retrieval testing.

#### Add and Update Documents

Document creation is asynchronous. Create the document, then poll until indexing finishes:

  1. **Create a knowledge base**
        Call [Create an Empty Knowledge Base](https://docs.dify.ai/en/api-reference/knowledge-bases/create-an-empty-knowledge-base), or use an existing knowledge base.

  1. **Add a document**
        Call [Create Document by Text](https://docs.dify.ai/en/api-reference/documents/create-document-by-text) or [Create Document by File](https://docs.dify.ai/en/api-reference/documents/create-document-by-file); both return a `batch` ID.

        If you didn't set `indexing_technique` (how content is indexed for search) when creating the knowledge base, set it on this first document; later documents inherit it automatically.

  1. **Poll the indexing status**
        Poll [Get Document Indexing Status](https://docs.dify.ai/en/api-reference/documents/get-document-indexing-status) with the `batch` ID until `indexing_status` reaches `completed` or `error`; it progresses through `waiting`, `parsing`, `cleaning`, `splitting`, and `indexing` along the way.

* **[List Documents](https://docs.dify.ai/en/api-reference/documents/list-documents)**: a paginated list, filterable by keyword or indexing status.
* **[Get Document](https://docs.dify.ai/en/api-reference/documents/get-document)**: one document's indexing status, metadata, and processing statistics; the `metadata` query parameter includes, omits, or returns only the metadata fields.
* **[Download Document](https://docs.dify.ai/en/api-reference/documents/download-document)**: a signed URL for the document's original uploaded file.
* **[Download Documents as ZIP](https://docs.dify.ai/en/api-reference/documents/download-documents-as-zip)**: bundle up to 100 uploaded-file documents into a single archive.
* **[Update Document](https://docs.dify.ai/en/api-reference/documents/update-document)**: replace a document's content by uploading a new file, re-triggering indexing; the canonical way to update a file-based document.
* **[Update Document by Text](https://docs.dify.ai/en/api-reference/documents/update-document-by-text)**: update a document's text content, name, or processing configuration inline; re-triggers indexing when the content changes.
* **[Update Document by File](https://docs.dify.ai/en/api-reference/documents/update-document-by-file)**: deprecated alias for uploading a replacement file; use Update Document instead.
* **[Update Document Status in Batch](https://docs.dify.ai/en/api-reference/documents/update-document-status-in-batch)**: enable, disable, archive, or unarchive multiple documents at once.
* **[Delete Document](https://docs.dify.ai/en/api-reference/documents/delete-document)**: permanently remove a document and every chunk inside it.

#### Manage Chunks and Child Chunks

* **[Create Chunks](https://docs.dify.ai/en/api-reference/chunks/create-chunks)**: add chunks to a document by hand—indexing already chunks uploaded content automatically. Each chunk requires `content`; documents in Q\&A mode also require `answer`.
* **[List Chunks](https://docs.dify.ai/en/api-reference/chunks/list-chunks)**: a paginated list, filterable by keyword or status.
* **[Get Chunk](https://docs.dify.ai/en/api-reference/chunks/get-chunk)**: one chunk's content, keywords, and indexing status.
* **[Update Chunk](https://docs.dify.ai/en/api-reference/chunks/update-chunk)**: change a chunk's content, keywords, or answer; re-triggers indexing for that chunk.
* **[Delete Chunk](https://docs.dify.ai/en/api-reference/chunks/delete-chunk)**: permanently remove a chunk.

For documents in Parent-child mode (`hierarchical_model`), child chunks nest under a parent chunk. Child chunks you create or update through the API are always typed `customized`, unlike the `automatic` ones the indexing pipeline generates.

* **[Create Child Chunk](https://docs.dify.ai/en/api-reference/chunks/create-child-chunk)**: add a child chunk under a parent chunk.
* **[List Child Chunks](https://docs.dify.ai/en/api-reference/chunks/list-child-chunks)**: a paginated list of one parent chunk's child chunks.
* **[Update Child Chunk](https://docs.dify.ai/en/api-reference/chunks/update-child-chunk)**: change a child chunk's content.
* **[Delete Child Chunk](https://docs.dify.ai/en/api-reference/chunks/delete-child-chunk)**: permanently remove a child chunk.

#### Manage Metadata Fields

Metadata fields annotate documents with structured information that retrieval can filter on:

* **[Create Metadata Field](https://docs.dify.ai/en/api-reference/metadata/create-metadata-field)**: add a custom field to the knowledge base, typed `string`, `number`, or `time`.
* **[List Metadata Fields](https://docs.dify.ai/en/api-reference/metadata/list-metadata-fields)**: every field, custom and built-in, with a count of documents using each.
* **[Update Metadata Field](https://docs.dify.ai/en/api-reference/metadata/update-metadata-field)**: rename a custom field.
* **[Delete Metadata Field](https://docs.dify.ai/en/api-reference/metadata/delete-metadata-field)**: remove a custom field; documents lose their values for it.
* **[Get Built-in Metadata Fields](https://docs.dify.ai/en/api-reference/metadata/get-built-in-metadata-fields)**: the system-provided fields, such as `document_name`, `uploader`, and `upload_date`.
* **[Update Built-in Metadata Field](https://docs.dify.ai/en/api-reference/metadata/update-built-in-metadata-field)**: enable or disable built-in fields for the knowledge base.
* **[Update Document Metadata in Batch](https://docs.dify.ai/en/api-reference/metadata/update-document-metadata-in-batch)**: set metadata key-value pairs across multiple documents in a single call.

Metadata also works as a stable external key: store your source system's ID on each document, then filter on it in later sync runs to find and update the same documents.

#### Organize Knowledge Bases with Tags

Tags live at the workspace level, independent of any single knowledge base:

* **[Create Knowledge Tag](https://docs.dify.ai/en/api-reference/tags/create-knowledge-tag)**: create a tag for organizing knowledge bases.
* **[List Knowledge Tags](https://docs.dify.ai/en/api-reference/tags/list-knowledge-tags)**: every tag in the workspace.
* **[Update Knowledge Tag](https://docs.dify.ai/en/api-reference/tags/update-knowledge-tag)**: rename a tag.
* **[Delete Knowledge Tag](https://docs.dify.ai/en/api-reference/tags/delete-knowledge-tag)**: remove a tag from every knowledge base it was bound to, without deleting those knowledge bases.
* **[Create Tag Binding](https://docs.dify.ai/en/api-reference/tags/create-tag-binding)**: bind one or more tags to a knowledge base; a knowledge base can carry multiple tags.
* **[Delete Tag Binding](https://docs.dify.ai/en/api-reference/tags/delete-tag-binding)**: remove tags from a knowledge base.
* **[Get Knowledge Base Tags](https://docs.dify.ai/en/api-reference/tags/get-knowledge-base-tags)**: the tags currently bound to one knowledge base.

#### Look Up Available Models

* **[Get Available Models](https://docs.dify.ai/en/api-reference/models/get-available-models)**: the models available for a given `model_type`; query `text-embedding` for embedding models or `rerank` for reranking models when configuring a knowledge base.

#### Run the Knowledge Pipeline

A knowledge pipeline is a workflow that ingests data from a datasource and turns it into documents:

* **[Upload Pipeline File](https://docs.dify.ai/en/api-reference/knowledge-pipeline/upload-pipeline-file)**: upload a file for the pipeline to process.
* **[List Datasource Plugins](https://docs.dify.ai/en/api-reference/knowledge-pipeline/list-datasource-plugins)**: the datasource nodes configured in the pipeline—published by default, or the draft version with `is_published=false`.
* **[Run Datasource Node](https://docs.dify.ai/en/api-reference/knowledge-pipeline/run-datasource-node)**: execute a single datasource node and stream its results, useful for testing one step in isolation.
* **[Run Pipeline](https://docs.dify.ai/en/api-reference/knowledge-pipeline/run-pipeline)**: execute the full pipeline in `streaming` or `blocking` response mode; `is_published` picks the published version or the current draft.

#### Consume Streaming Responses

*Choose a response mode, parse the SSE stream, dispatch events, and recover when a connection drops*

**Source:** https://docs.dify.ai/en/api-reference/guides/streaming

Choose a response mode, parse the SSE stream, dispatch events, and recover when a connection drops

Generation endpoints return either one complete response or a Server-Sent Events (SSE) stream, chosen per request with `response_mode`. Streaming is the usual choice: the reply renders as it generates, and long runs aren't cut off mid-flight.

#### Choose a Response Mode

`blocking` returns a single JSON body once generation finishes. It's the simpler integration for short, non-interactive calls, but long generations risk interruption: proxies cut long requests, and on Dify Cloud the edge proxy may end the connection if the upstream response doesn't arrive within its timeout.

`streaming` delivers the reply as SSE events. Use it for anything user-facing, for long runs, and for every flow that pauses for [Human Input](https://docs.dify.ai/en/api-reference/guides/human-input-flow).

> **ℹ️ Info:**
>   Agent and New Agent apps stream only.

#### Parse the Stream

Each event arrives as a `data: ` line holding one JSON object, terminated by a blank line.

Read the `event` field to decide what to do, and skip anything that isn't a `data: ` line: the keep-alive `ping` arrives as a bare `event: ping` line with no `data:` payload, every 10 seconds.

```python theme={null}
import json
import requests

body = {
    "query": "What are this month's top issues?",
    "inputs": {},
    "user": "customer-4821",
    "response_mode": "streaming",
}

with requests.post(url, headers=headers, json=body, stream=True) as r:
    for line in r.iter_lines(decode_unicode=True):
        if not line or not line.startswith("data: "):
            continue  # skips blank separators and ping lines
        event = json.loads(line[len("data: "):])
        handle(event)
```

On the wire, a stream looks like this:

```text theme={null}
data: {"event": "workflow_started", "task_id": "c3800678-…", "workflow_run_id": "fb47b2e6-…", "data": {…}}

event: ping

data: {"event": "node_finished", "task_id": "c3800678-…", "workflow_run_id": "fb47b2e6-…", "data": {…}}
```

#### Dispatch by Event Type

Which events arrive depends on the app type. See the event tables on [Send Chat Message](https://docs.dify.ai/en/api-reference/chat-messages/send-chat-message), [Run Workflow](https://docs.dify.ai/en/api-reference/workflow-runs/run-workflow), and [Send Completion Message](https://docs.dify.ai/en/api-reference/completion-messages/send-completion-message) for the contract.

The typical minimum:

1. Concatenate reply chunks in order:

   * `message` events for Chatbot and Chatflow apps
   * `agent_message` events for Agent and New Agent apps

   For New Agent apps, a single closing `message` event repeats the complete answer; treat it as the final answer, not extra text to append.

2. Close on the right terminal event:
   * `message_end` for Chatbot, Agent, and New Agent apps
   * `message_end` then `workflow_finished` (both arrive, in that order) for Chatflow apps
   * `workflow_finished` for Workflow apps

3. Surface `error`.

#### Handle Errors Mid-Stream

A failure after the stream opens doesn't change the HTTP status: the connection stays `200`. How the failure surfaces depends on where it happens:

* A workflow node failure arrives as `node_finished` and `workflow_finished` events with `status: "failed"`.
* Other failures end the stream with an `error` event carrying `status`, `code`, and `message`.

Handle both, and treat either as terminal for that request.

#### Reconnect and Resume

Two identifiers matter, and they're easy to mix up:

* `task_id` controls the in-flight generation and is what the stop endpoints ([Stop Chat Message Generation](https://docs.dify.ai/en/api-reference/chat-messages/stop-chat-message-generation) / [Stop Workflow Task](https://docs.dify.ai/en/api-reference/workflow-runs/stop-workflow-task)) take.
* `workflow_run_id` names the persistent run record.

Both arrive on the stream itself: every event except `error` carries `task_id`, and workflow and node events carry `workflow_run_id`. Save `workflow_run_id` as soon as it arrives: if the connection drops mid-run, it's the only handle you have for reconnecting or checking the outcome.

For workflow-backed runs (Workflow and Chatflow apps), a dropped connection isn't fatal. Reopen the stream with [Stream Workflow Events](https://docs.dify.ai/en/api-reference/workflow-runs/stream-workflow-events), passing the `workflow_run_id` and the same `user` that started the run. A mismatch returns 404.

Add `include_state_snapshot=true` to first replay the status of nodes that already ran, and `continue_on_pause=true` to keep one stream open across multiple Human Input pauses.

After reconnecting to a still-running workflow, confirm completion with [Get Workflow Run Detail](https://docs.dify.ai/en/api-reference/workflow-runs/get-workflow-run-detail) rather than relying on the reconnected stream's final event alone.

Other replies have no resume endpoint: if the connection drops mid-reply, issue a new request. For chat-style apps, [List Conversation Messages](https://docs.dify.ai/en/api-reference/conversations/list-conversation-messages) shows what was saved to the conversation.

#### Keep the Connection Alive

Set your client's read timeout comfortably above the 10-second `ping` interval so idle stretches between events don't kill the connection. The pings themselves need no handling beyond being skipped.

#### Workflow App API

*API for Workflow apps, covering workflow execution, run control and streaming, Human Input pauses, and run history*

**Source:** https://docs.dify.ai/en/api-reference/guides/workflow

API for Workflow apps, covering workflow execution, run control and streaming, Human Input pauses, and run history

[Workflow apps](https://docs.dify.ai/en/cloud/use-dify/build/workflow-chatflow) run in `workflow` mode, executing the published workflow once per call and returning its outputs. There's no conversation state between calls, so each run is independent of any previous one.

> **ℹ️ Info:**
>   Authentication, the base URL, and the `user` field that scopes end-user data are covered in [Get Started](https://docs.dify.ai/en/api-reference/guides/get-started) and [End User Identity](https://docs.dify.ai/en/api-reference/guides/end-user-identity).

#### Run a Workflow

* **[Run Workflow](https://docs.dify.ai/en/api-reference/workflow-runs/run-workflow)**: execute the app's currently published workflow with the input variables you provide.

  Streaming mode delivers events live as nodes execute; blocking mode returns once the run finishes.
* **[Run Workflow by ID](https://docs.dify.ai/en/api-reference/workflow-runs/run-workflow-by-id)**: execute a specific published version instead, identified by the `workflow_id` from an earlier run response or run detail lookup.

#### Follow and Control a Run

Whichever mode you run in, the response carries two IDs: `task_id` controls the run while it's active, and `workflow_run_id` identifies the persisted record afterward.

* **[Stop Workflow Task](https://docs.dify.ai/en/api-reference/workflow-runs/stop-workflow-task)**: cancel an active run by its `task_id`. Works in streaming mode only; a blocking call has already finished by the time it returns.
* **[Stream Workflow Events](https://docs.dify.ai/en/api-reference/workflow-runs/stream-workflow-events)**: resume a run's event stream from its `workflow_run_id` after a dropped connection or a pause.

  Pass `include_state_snapshot=true` to replay the status of already-executed nodes first, or `continue_on_pause=true` to stay open across multiple Human Input pauses.

#### Pause for Human Input

When a run reaches a [Human Input node](https://docs.dify.ai/en/cloud/use-dify/nodes/human-input) whose delivery method is WebApp, complete the pause over the API:

  1. **Listen for the pause**
        The run's event stream emits `human_input_required` carrying a `form_token` and the run's `workflow_run_id`, then ends with the `workflow_paused` event.

  1. **Fetch the form**
        Load the form's contents with [Get Human Input Form](https://docs.dify.ai/en/api-reference/human-input/get-human-input-form), using the `form_token`.

  1. **Submit the response**
        Send the recipient's input with [Submit Human Input Form](https://docs.dify.ai/en/api-reference/human-input/submit-human-input-form). Submitting resumes the run.

  1. **Resume the stream**
        Open a new stream with [Stream Workflow Events](https://docs.dify.ai/en/api-reference/workflow-runs/stream-workflow-events), using the `workflow_run_id` from the paused stream, and follow the remaining events through to the run's finish.

For file-attached submissions and the full event sequence, see the [Human Input Flow](https://docs.dify.ai/en/api-reference/guides/human-input-flow) guide.

#### Inspect Past Runs

* **[Get Workflow Run Detail](https://docs.dify.ai/en/api-reference/workflow-runs/get-workflow-run-detail)**: a run's status and outputs, by its `workflow_run_id`.
* **[List Workflow Logs](https://docs.dify.ai/en/api-reference/workflow-runs/list-workflow-logs)**: run-level summaries covering status, token usage, step count, and timing, rather than a node-by-node execution log; filter by keyword, status, date range, or who triggered the run.

For node-level events, stream the run instead of listing its logs: call [Run Workflow](https://docs.dify.ai/en/api-reference/workflow-runs/run-workflow) in streaming mode for a run you're starting, or [Stream Workflow Events](https://docs.dify.ai/en/api-reference/workflow-runs/stream-workflow-events) for one already in progress.

#### Work with Files

* **[Upload File](https://docs.dify.ai/en/api-reference/files/upload-file)**: upload an image, document, audio, or video file, then pass the returned `id` as `upload_file_id` in a file-type input variable when you run the workflow. Files are scoped to the uploading end user.
* **[Get End User Info](https://docs.dify.ai/en/api-reference/end-users/get-end-user-info)**: look up an end user's details from an end-user ID, such as the `created_by` in the Upload File response.

#### Transcribe and Synthesize Speech

* **[Convert Audio to Text](https://docs.dify.ai/en/api-reference/audio/convert-audio-to-text)**: transcribe an uploaded audio file (MP3, M4A, WAV, AMR, or MPGA, up to 30 MB) so end users can speak an input value instead of typing it.
* **[Convert Text to Audio](https://docs.dify.ai/en/api-reference/audio/convert-text-to-audio)**: synthesize a workflow's text output back into speech.

#### Retrieve App Info and Settings

* **[Get App Info](https://docs.dify.ai/en/api-reference/applications/get-app-info)**: the app's name, description, tags, and mode.
* **[Get App Parameters](https://docs.dify.ai/en/api-reference/applications/get-app-parameters)**: the fields your calls send in `inputs` (names, types, defaults) plus the app's feature switches—the basis for building requests or a client UI.
* **[Get App Meta](https://docs.dify.ai/en/api-reference/applications/get-app-meta)**: tool icons and other configuration metadata.
* **[Get App WebApp Settings](https://docs.dify.ai/en/api-reference/applications/get-app-webapp-settings)**: the WebApp's site configuration, theme, and customization options.

### Human Input

#### Get Human Input Form

***Available for**: Chatflow, Workflow apps.*

**Source:** https://docs.dify.ai/en/api-reference/human-input/get-human-input-form

/en/api-reference/openapi_service.json get /form/human_input/{form_token}
**Available for**: Chatflow, Workflow apps.

Returns the contents of a paused Human Input form. Requires WebApp delivery.

For the full sequence of Human Input calls, see [Human Input Flow](https://docs.dify.ai/en/api-reference/guides/human-input-flow).

#### Submit Human Input Form

***Available for**: Chatflow, Workflow apps.*

**Source:** https://docs.dify.ai/en/api-reference/human-input/submit-human-input-form

/en/api-reference/openapi_service.json post /form/human_input/{form_token}
**Available for**: Chatflow, Workflow apps.

Submits the recipient's response to a paused Human Input form. On acceptance the workflow resumes; follow the resumed run via [Stream Workflow Events](https://docs.dify.ai/en/api-reference/workflow-runs/stream-workflow-events). Requires WebApp delivery.

### Knowledge Bases

#### Create an Empty Knowledge Base

*Creates an empty knowledge base. Add documents to it with [Create Document by Text](https://docs.dify.ai/en/api-reference/documents/create-document-by-text) or [Create Document by File](https://docs.dify.ai/en/api-reference/documents/create-document-by-file).*

**Source:** https://docs.dify.ai/en/api-reference/knowledge-bases/create-an-empty-knowledge-base

/en/api-reference/openapi_service.json post /datasets
Creates an empty knowledge base. Add documents to it with [Create Document by Text](https://docs.dify.ai/en/api-reference/documents/create-document-by-text) or [Create Document by File](https://docs.dify.ai/en/api-reference/documents/create-document-by-file).

#### Delete Knowledge Base

*Permanently deletes a knowledge base and all of its documents.*

**Source:** https://docs.dify.ai/en/api-reference/knowledge-bases/delete-knowledge-base

/en/api-reference/openapi_service.json delete /datasets/{dataset_id}
Permanently deletes a knowledge base and all of its documents.

#### Get Knowledge Base

*Returns detailed information about a knowledge base, including its embedding model, retrieval configuration, and document statistics.*

**Source:** https://docs.dify.ai/en/api-reference/knowledge-bases/get-knowledge-base

/en/api-reference/openapi_service.json get /datasets/{dataset_id}
Returns detailed information about a knowledge base, including its embedding model, retrieval configuration, and document statistics.

#### List Knowledge Bases

*Returns a paginated list of knowledge bases, optionally filtered by keyword or tags.*

**Source:** https://docs.dify.ai/en/api-reference/knowledge-bases/list-knowledge-bases

/en/api-reference/openapi_service.json get /datasets
Returns a paginated list of knowledge bases, optionally filtered by keyword or tags.

#### Retrieve Chunks from a Knowledge Base / Test Retrieval

*Searches a knowledge base and returns the chunks most relevant to the query, for both production retrieval and test retrieval.*

**Source:** https://docs.dify.ai/en/api-reference/knowledge-bases/retrieve-chunks-from-a-knowledge-base-test-retrieval

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/retrieve
Searches a knowledge base and returns the chunks most relevant to the query, for both production retrieval and test retrieval.

#### Update Knowledge Base

*Updates a knowledge base. Only the fields included in the request body are changed.*

**Source:** https://docs.dify.ai/en/api-reference/knowledge-bases/update-knowledge-base

/en/api-reference/openapi_service.json patch /datasets/{dataset_id}
Updates a knowledge base. Only the fields included in the request body are changed.

### Knowledge Pipeline

#### List Datasource Plugins

*Returns the datasource nodes configured in the knowledge pipeline, each with the plugin it uses and the metadata needed to run it.*

**Source:** https://docs.dify.ai/en/api-reference/knowledge-pipeline/list-datasource-plugins

/en/api-reference/openapi_service.json get /datasets/{dataset_id}/pipeline/datasource-plugins
Returns the datasource nodes configured in the knowledge pipeline, each with the plugin it uses and the metadata needed to run it.

#### Run Datasource Node

*Runs a single datasource node in the knowledge pipeline and streams its execution events.*

**Source:** https://docs.dify.ai/en/api-reference/knowledge-pipeline/run-datasource-node

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/pipeline/datasource/nodes/{node_id}/run
Runs a single datasource node in the knowledge pipeline and streams its execution events.

#### Run Pipeline

*Runs the full knowledge pipeline over one or more datasources. `response_mode` selects a streaming or blocking response.*

**Source:** https://docs.dify.ai/en/api-reference/knowledge-pipeline/run-pipeline

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/pipeline/run
Runs the full knowledge pipeline over one or more datasources. `response_mode` selects a streaming or blocking response.

#### Upload Pipeline File

*Uploads a file for use in a knowledge pipeline. Use the returned `id` as the `reference` of a `local_file` item in [Run Pipeline](https://docs.dify.ai/en/api-reference/knowledge-pipeline/run-pipeline).*

**Source:** https://docs.dify.ai/en/api-reference/knowledge-pipeline/upload-pipeline-file

/en/api-reference/openapi_service.json post /datasets/pipeline/file-upload
Uploads a file for use in a knowledge pipeline. Use the returned `id` as the `reference` of a `local_file` item in [Run Pipeline](https://docs.dify.ai/en/api-reference/knowledge-pipeline/run-pipeline).

### Metadata

#### Create Metadata Field

*Create a custom metadata field for annotating documents in the knowledge base with structured information.*

**Source:** https://docs.dify.ai/en/api-reference/metadata/create-metadata-field

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/metadata
Create a custom metadata field for annotating documents in the knowledge base with structured information.

#### Delete Metadata Field

*Permanently delete a custom metadata field. Documents that used the field lose their values for it.*

**Source:** https://docs.dify.ai/en/api-reference/metadata/delete-metadata-field

/en/api-reference/openapi_service.json delete /datasets/{dataset_id}/metadata/{metadata_id}
Permanently delete a custom metadata field. Documents that used the field lose their values for it.

#### Get Built-in Metadata Fields

*Returns the built-in metadata fields provided by the system.*

**Source:** https://docs.dify.ai/en/api-reference/metadata/get-built-in-metadata-fields

/en/api-reference/openapi_service.json get /datasets/{dataset_id}/metadata/built-in
Returns the built-in metadata fields provided by the system.

#### List Metadata Fields

*Returns all metadata fields for the knowledge base, both custom and built-in, with the count of documents using each field.*

**Source:** https://docs.dify.ai/en/api-reference/metadata/list-metadata-fields

/en/api-reference/openapi_service.json get /datasets/{dataset_id}/metadata
Returns all metadata fields for the knowledge base, both custom and built-in, with the count of documents using each field.

#### Update Built-in Metadata Field

*Enable or disable built-in metadata fields for the knowledge base.*

**Source:** https://docs.dify.ai/en/api-reference/metadata/update-built-in-metadata-field

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/metadata/built-in/{action}
Enable or disable built-in metadata fields for the knowledge base.

#### Update Document Metadata in Batch

*Update metadata values for multiple documents in a single request.*

**Source:** https://docs.dify.ai/en/api-reference/metadata/update-document-metadata-in-batch

/en/api-reference/openapi_service.json post /datasets/{dataset_id}/documents/metadata
Update metadata values for multiple documents in a single request.

#### Update Metadata Field

*Rename a custom metadata field.*

**Source:** https://docs.dify.ai/en/api-reference/metadata/update-metadata-field

/en/api-reference/openapi_service.json patch /datasets/{dataset_id}/metadata/{metadata_id}
Rename a custom metadata field.

### Models

#### Get Available Models

*Returns the available models of a given type. Use it to find the `text-embedding` and `rerank` models to configure on a knowledge base.*

**Source:** https://docs.dify.ai/en/api-reference/models/get-available-models

/en/api-reference/openapi_service.json get /workspaces/current/models/model-types/{model_type}
Returns the available models of a given type. Use it to find the `text-embedding` and `rerank` models to configure on a knowledge base.

### Tags

#### Create Knowledge Tag

*Create a tag for organizing knowledge bases.*

**Source:** https://docs.dify.ai/en/api-reference/tags/create-knowledge-tag

/en/api-reference/openapi_service.json post /datasets/tags
Create a tag for organizing knowledge bases.

#### Create Tag Binding

*Bind one or more tags to a knowledge base. A knowledge base can have multiple tags.*

**Source:** https://docs.dify.ai/en/api-reference/tags/create-tag-binding

/en/api-reference/openapi_service.json post /datasets/tags/binding
Bind one or more tags to a knowledge base. A knowledge base can have multiple tags.

#### Delete Knowledge Tag

*Permanently delete a knowledge base tag. Does not delete the knowledge bases that were tagged.*

**Source:** https://docs.dify.ai/en/api-reference/tags/delete-knowledge-tag

/en/api-reference/openapi_service.json delete /datasets/tags
Permanently delete a knowledge base tag. Does not delete the knowledge bases that were tagged.

#### Delete Tag Binding

*Remove one or more tags from a knowledge base.*

**Source:** https://docs.dify.ai/en/api-reference/tags/delete-tag-binding

/en/api-reference/openapi_service.json post /datasets/tags/unbinding
Remove one or more tags from a knowledge base.

#### Get Knowledge Base Tags

*Returns the tags bound to a knowledge base.*

**Source:** https://docs.dify.ai/en/api-reference/tags/get-knowledge-base-tags

/en/api-reference/openapi_service.json get /datasets/{dataset_id}/tags
Returns the tags bound to a knowledge base.

#### List Knowledge Tags

*Returns all knowledge base tags in the workspace.*

**Source:** https://docs.dify.ai/en/api-reference/tags/list-knowledge-tags

/en/api-reference/openapi_service.json get /datasets/tags
Returns all knowledge base tags in the workspace.

#### Update Knowledge Tag

*Rename a knowledge base tag.*

**Source:** https://docs.dify.ai/en/api-reference/tags/update-knowledge-tag

/en/api-reference/openapi_service.json patch /datasets/tags
Rename a knowledge base tag.

### Workflow Runs

#### Get Workflow Run Detail

***Available for**: Chatflow, Workflow apps.*

**Source:** https://docs.dify.ai/en/api-reference/workflow-runs/get-workflow-run-detail

/en/api-reference/openapi_service.json get /workflows/run/{workflow_run_id}
**Available for**: Chatflow, Workflow apps.

Get a single workflow run's status, inputs, outputs, and execution metrics.

#### List Workflow Logs

***Available for**: Chatflow, Workflow apps.*

**Source:** https://docs.dify.ai/en/api-reference/workflow-runs/list-workflow-logs

/en/api-reference/openapi_service.json get /workflows/logs
**Available for**: Chatflow, Workflow apps.

List past workflow runs with optional filters. Each entry is a run-level summary (status, token usage, step count, and timing), not a node-by-node execution log.

To follow a run's node-level events, stream it instead:

- **A run you start**: use [Run Workflow](https://docs.dify.ai/en/api-reference/workflow-runs/run-workflow) in streaming mode, which emits `node_started` and `node_finished` as the run executes.
- **A run already in progress**: call [Stream Workflow Events](https://docs.dify.ai/en/api-reference/workflow-runs/stream-workflow-events) with `include_state_snapshot=true` to replay each executed node's status, then stream the rest.

A finished run's node-level logs aren't available through the Service API.

#### Run Workflow

***Available for**: Workflow apps.*

**Source:** https://docs.dify.ai/en/api-reference/workflow-runs/run-workflow

/en/api-reference/openapi_service.json post /workflows/run
**Available for**: Workflow apps.

Run the app's published workflow and return its outputs, either in a single `blocking` response or as a `streaming` Server-Sent Events feed. Requires a published workflow.

#### Run Workflow by ID

***Available for**: Workflow apps.*

**Source:** https://docs.dify.ai/en/api-reference/workflow-runs/run-workflow-by-id

/en/api-reference/openapi_service.json post /workflows/{workflow_id}/run
**Available for**: Workflow apps.

Run a specific published workflow version, identified by the `workflow_id` in the path. Request body, response, and streaming behavior match [Run Workflow](https://docs.dify.ai/en/api-reference/workflow-runs/run-workflow); only the executed version differs.

#### Stop Workflow Task

***Available for**: Workflow apps.*

**Source:** https://docs.dify.ai/en/api-reference/workflow-runs/stop-workflow-task

/en/api-reference/openapi_service.json post /workflows/tasks/{task_id}/stop
**Available for**: Workflow apps.

Stop a running workflow task. Only supported in `streaming` mode.

#### Stream Workflow Events

***Available for**: Chatflow, Workflow apps.*

**Source:** https://docs.dify.ai/en/api-reference/workflow-runs/stream-workflow-events

/en/api-reference/openapi_service.json get /workflow/{workflow_run_id}/events
**Available for**: Chatflow, Workflow apps.

Resume the Server-Sent Events stream for a workflow run after a pause or a dropped SSE connection. For runs that have already finished, the stream emits a single `workflow_finished` event and closes.

To check an in-progress run's node-level status and progress, call it with `include_state_snapshot=true`: the stream replays each already-executed node's status before streaming new events.

---
