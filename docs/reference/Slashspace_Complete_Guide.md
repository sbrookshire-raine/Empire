# Slashspace (Rabbitholes AI) — Complete Documentation Guide

> Scraped and cleaned from the official Slashspace documentation for offline reference and use in NotebookLM.
> Note: Slashspace was previously named "Rabbitholes AI" — some pages still reference the old name.
> Source: https://www.slashspace.ai/docs
> Total pages: 37
> Compiled: 2026-07-18

---

## Table of Contents

- **Get Started**
  - [Quickstart](#quickstart)
  - [Core concepts](#core-concepts)
  - [Moving from Rabbitholes](#moving-from-rabbitholes)
  - [Redeem Code](#redeem-code)
- **Canvas**
  - [Canvas Overview](#canvas-overview)
  - [Connections](#connections)
  - [Creating Nodes](#creating-nodes)
  - [Export](#export)
  - [Keyboard Shortcuts](#keyboard-shortcuts)
  - [Organizing the Canvas](#organizing-the-canvas)
  - [Search](#search)
  - [Side View](#side-view)
- **Nodes**
  - [Chat Node](#chat-node)
  - [Document Node (Beta)](#document-node-beta)
  - [Group Node](#group-node)
  - [Image Node](#image-node)
  - [Text Node](#text-node)
  - [Web Node](#web-node)
  - [Post Node (YouTube & more)](#post-node-youtube-more)
- **AI Features**
  - [Using MCP Tools in Chat](#using-mcp-tools-in-chat)
  - [Models & Providers](#models-providers)
  - [Personas](#personas)
  - [RAG Mode](#rag-mode)
  - [Slash Commands (Skills & Prompts)](#slash-commands-skills-prompts)
  - [Sub-Agents](#sub-agents)
  - [Voice Input](#voice-input)
- **Settings**
  - [Account Management](#account-management)
  - [Agent Providers](#agent-providers)
  - [Custom Providers](#custom-providers)
  - [Default Models](#default-models)
  - [Connected Tools](#connected-tools)
  - [MCP Servers (Beta)](#mcp-servers-beta)
  - [Ollama (Local Models)](#ollama-local-models)
  - [Persona Prompts](#persona-prompts)
  - [Cloud Providers](#cloud-providers)
  - [System Preferences](#system-preferences)
- **Troubleshooting**
  - [Troubleshooting & Support](#troubleshooting-support)

---

## Get Started

### Quickstart
*Install Slashspace, sign in, and send your first message*

**Source:** https://www.slashspace.ai/docs

#### Installation

1. **Download the app:**

   Go to [slashspace.ai](https://slashspace.ai) and download the installer for your OS.
2. **Install and Launch:**

   Run the Installer -> follow the on-screen installation prompts -> launch the app.
3. **Sign in:**

   Click **Sign in** and authenticate with your account in the browser window that opens. The app shows **"Waiting for browser sign-in..."** until it picks up the redirect automatically.

   If the browser doesn't redirect back (e.g. it's blocked or on a different device), click **Paste login token** and paste the token copied from the browser sign-in page to finish manually.

> **Don't have an account?** Create one at [slashspace.ai](https://slashspace.ai)

---

#### First Conversation

You can start chatting immediately after signing in — no setup required.

1. **Open the Untitled Canvas** (or create a new canvas) to begin.
2. In the chat box, **type a question or prompt** and press **Enter** to chat with the AI.

New canvases include a chat node by default, so you can start typing right away.

**Rabbitholes** models (the built-in AI provider) are available out of the box and ready to use.

---

#### How Credits Work

**Rabbitholes models** consume credits from your account balance. Every message you send to a Rabbitholes model deducts credits.

**Bring Your Own Key (BYOK) models** don't consume any credits. When you connect your own API key from a provider (OpenAI, Anthropic, Google, etc.), you pay the provider directly and no credits are used.

---

#### Connect Your Own Provider (Optional)

If you'd prefer to use your own API keys instead of credits:

1. **Open Settings → AI Settings** and choose the integration you want: **Cloud Providers** (OpenAI, Anthropic, Google, and more), **Ollama** (local models), **Custom Providers** (OpenAI-compatible endpoints), or **Agent Providers** (Cursor, Claude Code).
2. **Expand a provider** and click **`Get your API key here`**.

   This redirects you to the provider's website to get your API key.
3. **Paste your API key:**

   Paste the key into the field — a confirm button appears once you start typing. Click it to save the key.

Models from connected providers won't use any of your credits.

> **Note**: On the free (Starter) plan, only Rabbitholes and Ollama are available under Cloud Providers. Connecting other providers (OpenAI, Anthropic, Google, etc.) requires upgrading to Pro or higher.

---

#### Where to go next

- **[Core concepts](https://www.slashspace.ai/docs/core-concepts)** — the mental model: nodes, context flow, and the canvas
- **[Canvas](https://www.slashspace.ai/docs/canvas)** — navigation, creating nodes, connections, organizing, search, and export
- **[Nodes](https://www.slashspace.ai/docs/nodes/chat-node)** — every node type in depth, starting with the Chat Node
- **[AI Features](https://www.slashspace.ai/docs/ai-features/models)** — models, RAG mode, personas, slash commands, MCP tools, sub-agents, and voice input
- **[Settings](https://www.slashspace.ai/docs/settings/providers)** — providers, API keys, defaults, and account management
- **[Troubleshooting](https://www.slashspace.ai/docs/troubleshooting)** — common errors and how to get help

---

#### Support

Join our [Discord](https://links.rabbitholes.ai/discord) Community for faster response

Email our support team at [support@rabbitholes.ai](mailto:support@rabbitholes.ai)

For reporting bugs or requesting features, use the in-app `Bug / Feedback` (right-click the canvas, or find it under Settings → Troubleshoot)

> **Note**: Discord is the preferred contact, followed by email, then the in-app bug report

### Core concepts
*The mental model behind Slashspace: nodes, context flow, and the canvas*

**Source:** https://www.slashspace.ai/docs/core-concepts

Slashspace is a canvas for thinking with AI. Instead of one long chat thread, you work on a spatial canvas where every piece of content — a conversation, a document, a web page, an image — is a **node**, and connections between nodes control what context the AI sees.

Three ideas explain almost everything in the app:

1. **Everything is a node** — a single unit of content and context.
2. **Context flows left to right** — connect nodes to feed one node's content into another's conversation.
3. **You control the context** — connections, context modes, and RAG let you decide exactly what the AI reads.

---

#### Nodes

**A node is a single unit of context.** A chat node contains a back-and-forth conversation with an AI model. A Web node contains the parsed text of a URL. A Document node contains a processed file.

> When you connect the right handle of Node A to the left handle of Node B, Node B can derive context from Node A.

##### Types of nodes

###### Chat Node

The primary way to interact with AI. Accepts incoming context from connected nodes and can feed its conversation onward to other nodes. Supports slash commands, @ node mentions, personas, MCP tools, RAG mode, voice input, and sub-agents. See [Chat Node](https://www.slashspace.ai/docs/nodes/chat-node).

###### Text Node

Rich-text snippets with markdown formatting. Plug them into chat nodes to reuse instructions, notes, or drafts as context. Select text inside one to ask the AI about just that selection. See [Text Node](https://www.slashspace.ai/docs/nodes/text-node).

###### Image Node

Add images from your computer or generate them with AI (Straico, OpenAI, or Fal AI models). Connect image nodes together for image-to-image generation with reference images. See [Image Node](https://www.slashspace.ai/docs/nodes/image-node).

###### Post Node

Paste a YouTube, TikTok, Instagram, Facebook, X, or LinkedIn URL — the node fetches the transcript or post content so you can chat about it. See [Post Node](https://www.slashspace.ai/docs/nodes/youtube-node).

###### Web Node

Parses content from any publicly available URL — screenshot plus extracted text — so you can ask questions about the page. See [Web Node](https://www.slashspace.ai/docs/nodes/web-node).

###### Document Node (Beta)

Add a file (PDF, Word, PowerPoint, Excel, CSV, Markdown, and more) as context. Files are processed and indexed for [RAG Mode](https://www.slashspace.ai/docs/ai-features/rag-mode); you can chat about a document immediately while processing runs. See [Document Node](https://www.slashspace.ai/docs/nodes/file-node).

###### Group Node

A labeled container that keeps related nodes together — move, resize, and tidy them as a unit. See [Group Node](https://www.slashspace.ai/docs/nodes/group-node).

[](https://media.rabbitholes.download/docs/v5/nodes.mp4)

---

#### Context flow and branches

Context always flows **left to right**. You create branches by:

1. Double-clicking a node's right handle.
2. Dragging the right handle and dropping the connector on empty canvas.
3. Pressing `Cmd/Ctrl + B` on the active node, or using **Split** (`Cmd/Ctrl + Shift + Enter`) to send a prompt into a new branch.

> If Node A is connected to Node B, and Node B is connected to Node C, the chat inside Node C derives context from Node A + Node B.

> A single node can have multiple incoming and outgoing branches. A node cannot connect to itself.

Chat nodes also let you type `@` to mention another node by name — this creates a connection without leaving the keyboard. And each chat node has a **context mode** toggle: *Summarized context* (the default) or *Isolated context*, which ignores all incoming connections for that node.

For the full picture — handles, edge styles, token accounting — see [Connections & Context](https://www.slashspace.ai/docs/canvas/connections).

[](https://media.rabbitholes.download/docs/v5/connecting_branches.mp4)

---

#### The Canvas

The **Canvas** is your visual workspace: pan, zoom, organize nodes into groups, search everything with `⌘K`, and export your work as Markdown or JSON.

Start with the [Canvas Overview](https://www.slashspace.ai/docs/canvas), then [Creating Nodes](https://www.slashspace.ai/docs/canvas/creating-nodes) and [Organizing the Canvas](https://www.slashspace.ai/docs/canvas/organizing). The complete shortcut list lives in [Keyboard Shortcuts](https://www.slashspace.ai/docs/canvas/keyboard-shortcuts).

---

#### Models, credits, and plans

Slashspace runs AI three ways:

- **Rabbitholes managed models** (Basic / Pro / Advanced tiers) — built in, no setup, billed from your credit balance.
- **Bring Your Own Key** — connect API keys for OpenAI, Anthropic, Google, and more. No credits consumed; requires a Pro plan or higher.
- **Local models via Ollama** — free, private, offline.

Plus **Agent providers** (Cursor and Claude Code CLIs) and **Custom OpenAI-compatible providers**. See [Models & Providers](https://www.slashspace.ai/docs/ai-features/models) for how to choose.

---

#### RAG Mode

When you press **Ask** on a chat node with incoming context, everything connected is sent as-is. Toggle **RAG Mode** first and Slashspace instead retrieves only the most relevant chunks from the connected content — useful for large contexts and for cutting AI costs.

> For small context sizes (under ~10,000 tokens) RAG mode is not recommended.

See [RAG Mode](https://www.slashspace.ai/docs/ai-features/rag-mode) for statuses, savings, and constraints.

[](https://media.rabbitholes.download/docs/v5/rag-mode.mp4)

---

#### Where your data lives

Slashspace is local-first. Your canvases, files, and library live in a `SlashspaceOS` folder in your home directory:

- Canvases are stored as JSON files you can export or back up.
- `~/SlashspaceOS/.prompts` holds your reusable prompt library for [slash commands](https://www.slashspace.ai/docs/ai-features/slash-commands).
- Skills follow the cross-tool convention at `~/.agents/skills`.

Cloud features (RAG indexing, AI Search, analytics) are **opt-in** — manage them under **Settings → Account → Privacy Settings**. See [Account Management](https://www.slashspace.ai/docs/settings/account-management).

### Moving from Rabbitholes
*How to migrate your data and lifetime deal from Rabbitholes to Slashspace*

**Source:** https://www.slashspace.ai/docs/migration

Rabbitholes has a new name — it's now **Slashspace**. Your lifetime deal, your data, your bring-your-own-key access — all of it carries over. Nothing is lost.

This guide walks you through the switch. It takes about 5 minutes.

---

#### Before you start

You only need two things:

- **The email you used when you bought Rabbitholes.** This is how we match your lifetime deal to your new Slashspace account.
- **An internet connection** for the sign-in step.

That's it. You don't need your old license key, a receipt, or anything else.

---

#### Step 1: Download Slashspace

Go to the Slashspace website and download the app for your platform (Mac, Windows, or Linux). Install it like you would any other app.

You can keep Rabbitholes installed — nothing will conflict. But you won't need it after migration.

---

#### Step 2: Sign in with your purchase email

Open Slashspace. You'll be asked to sign in.

**Use the same email address you used to buy Rabbitholes.** This is the important part. Your lifetime deal is tied to that email, and we match it automatically behind the scenes.

##### "But It's asking me to create an account?"

That's fine. Last year, we moved from license keys to a regular email sign-in. If you've been using a license key this whole time and never set up an account, you'll be asked to create one now.

**Go ahead and create it.** Just make sure you use the same email from your purchase. Once you do, your lifetime deal will be linked automatically. You don't need to enter a license key or do anything extra.

---

#### Step 3: Finish sign-in

Complete the sign-in flow. Once you're in, the app will check whether you have existing Rabbitholes data on your computer.

---

#### Step 4: Run the migration

If you have an existing Rabbitholes folder on your computer, Slashspace will automatically offer to migrate your data right after you sign in. You don't need to go looking for this — it shows up on its own.

Here's what the migration does:

- It **copies** your files from the Rabbitholes folder to the new Slashspace folder.
- It does **not** delete anything from your old Rabbitholes folder. Your original files stay right where they are.

##### What if migration fails?

Sometimes a file in your Rabbitholes folder might be corrupted (this is rare, but it happens). If the migration fails partway through:

1. **Reach out to support** — we can help you figure out which file is causing the problem.
2. Or, if you're comfortable with it, **delete the problem file** from the Rabbitholes folder on your computer and run the migration again.

Either way, your original files are not touched during migration, so there's no risk of losing anything.

---

#### Your lifetime deal stays the same

Nothing about your deal changes. Here's what you keep:

- **Lifetime access** — no subscriptions, no renewals, no expiry. Ever.
- **Bring your own key** — keep using your own API keys with any provider, just like before.

The only thing that changed is the name on the box. We also added a managed provider for users who're not comfortable with using their own API keys. You can also use this but it's used with prepaid credits.

---

#### Common questions

**Can I delete the Rabbitholes folder after migrating?**
Yes, once you've confirmed everything looks good in Slashspace, you can safely delete the old Rabbitholes folder. But there's no rush — it's not hurting anything by sitting there. Except for consuimg space for your files.

**What if I used a different email to buy Rabbitholes?**
You need to sign in with the email that's on your original purchase. If you're not sure which one that is, check your inbox for the purchase confirmation email, or reach out to support and we'll help you find it.

**What if migration keeps failing?**
Reach out to support. It's almost always a single corrupted file, and we can help you sort it out quickly.

**Where does Slashspace store my files now?**
Your data now lives in a folder called `SlashspaceOS` in your home directory, instead of the old `rabbitholes` folder.

**Do I need to keep Rabbitholes installed?**
No. Once you've migrated, you can uninstall Rabbitholes whenever you like.

### Redeem Code
**Source:** https://www.slashspace.ai/docs/redeem-code

1. Go to [slashspace.ai/account](https://www.slashspace.ai/account).
2. Create an account.
3. Scroll down to the "Have a partner code?" section.
4. Enter your unique redemption code.
5. Click "Redeem."
6. Once verified, the license key is generated and will appear under "Active License."

> Next: Open the Slashspace app and follow the [Quickstart](https://www.slashspace.ai/docs) — click **Sign in** and authenticate with the same email you used to create your account. You no longer need to paste a license key.


---

## Canvas

### Canvas Overview
*Navigate the infinite canvas — panning, zooming, the mini map, viewport controls, and canvas settings.*

**Source:** https://www.slashspace.ai/docs/canvas

The canvas is your workspace in Slashspace. It's an infinite surface where you place nodes — chats, text, images, web pages, documents — and connect them to build context for AI conversations. Instead of one long chat thread, your thinking is laid out spatially, so you can see how ideas relate and branch off in any direction.

If you're new, start with [Core Concepts](https://www.slashspace.ai/docs/core-concepts) to understand how nodes and context work, then come back here to learn your way around.

#### Moving around

How scrolling behaves depends on the **Movement** mode you pick in [canvas settings](#canvas-settings):

| Action | Touchpad mode | Mouse mode |
| --- | --- | --- |
| Scroll | Pans the canvas | Zooms in and out |
| `Cmd` + scroll / pinch | Zooms in and out | Zooms in and out |
| Middle-click + drag | Pans | Pans |
| `Space` + drag | Pans | Pans |
| Left-click + drag | Draws a selection box | Draws a selection box |

> Left-click dragging on empty canvas selects nodes instead of panning. To pan with the mouse, use middle-click drag or hold `Space` while dragging. Double-click zoom is disabled so stray clicks never jump your view.

You can zoom out very far (down to 1%) to get a bird's-eye view of a large canvas, and zoom in up to 200% for detail work.

#### Viewport controls and mini map

The panel in the bottom-right corner gives you quick view controls:

1. **Fit View** — zooms and pans so every node fits on screen.
2. **Zoom In** / **Zoom Out** — step the zoom level.
3. **Show Mini Map** — toggles a small overview of the whole canvas. You can drag the viewport rectangle inside it, and pan or zoom directly on the mini map.

[](https://media.rabbitholes.download/mini-map.mp4)

**Use cases**

- Researching a big topic with 40+ nodes? Toggle the mini map to keep your bearings and jump between clusters.
- Presenting your canvas to someone — hit **Fit View** to frame everything, then zoom into the branch you're discussing.
- Zoom out to 10–20% to spot orphaned nodes you forgot to connect.

#### The toolbar

The main toolbar sits at the top-center of the canvas. It holds buttons for every node type (each with a letter hotkey), a **Tidy Up** button (`0`) that auto-arranges your nodes, and **Search** (`⌘K`).

[](https://media.rabbitholes.download/docs/v5/vertical-toolbar.mp4)

See [Creating Nodes](https://www.slashspace.ai/docs/canvas/creating-nodes) for all the ways to add nodes, and [Organizing](https://www.slashspace.ai/docs/canvas/organizing) for Tidy Up and layout tools.

#### Canvas header

Across the top of the canvas you'll find:

- **Sidebar toggle** — show or hide the canvas list.
- **Breadcrumb** — the folder path and canvas name (new canvases show "Untitled" until you name them).
- **Settings** (gear icon) — opens the canvas settings popover.
- **Side view toggle** (panel icon) — opens a right-hand panel that shows the active node full-height. See [Side View](https://www.slashspace.ai/docs/canvas/side-view).

#### Canvas settings

Click the **gear icon** in the canvas header to open the **Canvas settings** popover. These settings apply to the current canvas only:

1. **Movement** — choose **Touchpad** (scroll pans) or **Mouse** (scroll wheel zooms).
2. **Default model** — the AI model new chat nodes use on this canvas. A **Global default** badge shows when the canvas is inheriting your app-wide setting. See [Default Models](https://www.slashspace.ai/docs/settings/default-models).
3. **Agent workspace** — pick (or clear) a folder that agent-provider models can work in. See [Agent Providers](https://www.slashspace.ai/docs/settings/agent-providers).
4. **Edges** — pick one of five edge styles: Default, Straight, Step, Smooth step, or Simple bezier.

A **Go to Settings** link at the bottom takes you to the app-wide settings.

[](https://media.rabbitholes.download/canvas-settings.mp4)

**Use cases**

- Set a fast, cheap model as the default on a brainstorming canvas, and a stronger model on your deep-research canvas.
- Point the agent workspace at a project folder so coding-agent models can read and edit those files.
- Switch Movement to Mouse mode if you work with a scroll-wheel mouse and want scroll-to-zoom.

#### Next steps

- [Creating Nodes](https://www.slashspace.ai/docs/canvas/creating-nodes) — every way to get content onto the canvas.
- [Connections](https://www.slashspace.ai/docs/canvas/connections) — how context flows between nodes.
- [Keyboard Shortcuts](https://www.slashspace.ai/docs/canvas/keyboard-shortcuts) — the full shortcut reference.

### Connections
*Connect nodes to control exactly what context the AI sees — handles, branches, context modes, and token summaries.*

**Source:** https://www.slashspace.ai/docs/canvas/connections

Connections are what make the canvas more than a whiteboard. Every edge you draw is a statement about context: "the node on the right can see the node on the left." Instead of stuffing everything into one long chat, you engineer the exact context each conversation gets — which means more relevant answers, fewer tokens, and no context pollution between unrelated threads.

#### Handles: givers and takers

Every node has two connection points:

- **Right handle (giver)** — the source. It turns orange when connected. Drag from here to send this node's content onward.
- **Left handle (taker)** — the target. Hover it to see a tooltip with the incoming context size, e.g. "1,204 incoming tokens".

To connect two nodes, drag from one node's right handle to another node's left handle.

> You can't connect a node to itself ("Cannot connect a node to itself."), you can't create duplicate edges between the same pair, and Image nodes only accept other Image nodes as input ("Image nodes can only accept images nodes as input").

#### How context flows

Context flows **left to right** and chains through the whole upstream path. If A → B → C, then C sees both A and B. This is the core mental model:

- A chat node reads everything connected upstream of it — text notes, web pages, documents, other chats — as context for its conversation.
- Adding or removing an edge immediately changes what the AI knows in that chat.

You can also connect nodes from inside a chat: typing `@` in a chat node's input lets you mention another node, which creates the edge for you. See [Chat Node](https://www.slashspace.ai/docs/nodes/chat-node).

**Use cases**

- **Research**: connect three source Web nodes into one chat node and ask it to synthesize them — the answer draws only on those sources.
- **Writing**: chain outline → draft → editor-chat, so the editing conversation sees both the outline and the draft.
- **Studying**: connect a lecture PDF (Document node) to several chat nodes, one per exam topic, and quiz yourself in each without the threads bleeding into each other.
- **Planning**: keep a "project brief" Text node upstream of every chat on the canvas so all of them share the same ground truth.

#### Branches

A branch is a new chat node that continues from an existing node:

1. **Double-click the right handle** of any node — a tooltip says "Create a new branch" — and a connected Chat node is created.
2. Or press `⌘B` with a node active to branch from it.
3. Inside a chat, `⌘⇧Enter` sends your typed message into a brand-new branch instead of the current thread.

**Use cases**

- Mid-conversation, you want to explore a tangent without derailing the thread — branch it, and the tangent inherits all the context up to that point.
- Compare answers: branch the same source twice and ask each branch with a different framing or model.

#### Context modes

Chat nodes have a context-mode toggle on their left edge:

- **Summarized context** (zap icon) — the default. Incoming context is summarized and passed into the conversation.
- **Isolated context** — the chat ignores all incoming connections and runs standalone.

> The toggle is disabled while the chat is generating a response.

**Use cases**

- Flip a scratch-pad chat to **Isolated context** so a quick side question doesn't burn tokens re-reading a large upstream document.
- Keep a "devil's advocate" chat isolated so it critiques your conclusion without being anchored by the sources.

#### Token summary

Every chat node shows a small token pill (the asterisk icon). Click it to open the **Token Summary** popover, which breaks down what will be sent to the model:

- **Incoming** — tokens from connected upstream nodes (shows 0 in Isolated mode).
- **Own** — tokens from this node's own messages.
- **Input** — tokens in the message you're currently typing.
- **Total** — the sum.

> Treat these numbers as an estimate — they're tokenized with the OpenAI tokenizer, and other providers count slightly differently.

**Use cases**

- Before sending an expensive request, check whether an upstream document is dumping 50k tokens into the prompt — and disconnect or isolate if so.
- Debug a "context too long" error by finding which upstream branch carries the weight.

#### Edge styles and editing

- Choose from five edge styles in [canvas settings](https://www.slashspace.ai/docs/canvas#canvas-settings): Default, Straight, Step, Smooth step, or Simple bezier.
- Select an edge and press `Backspace`/`Delete` to remove it.
- Drag either end of an existing edge to reconnect it to a different node.

### Creating Nodes
*Every way to add nodes to the canvas — toolbar, right-click, Cmd+click, drag-and-drop, and paste.*

**Source:** https://www.slashspace.ai/docs/canvas/creating-nodes

Nodes are the building blocks of a canvas. There are several ways to create them — pick whichever fits the moment. On an empty canvas you'll see the hint: "Use the Toolbar or Cmd/Ctrl + Click anywhere to create a node".

#### From the toolbar

The toolbar at the top-center of the canvas has a button for each node type, each with a single-letter hotkey:

| Node type | Hotkey |
| --- | --- |
| Chat node | `C` |
| Text node | `T` |
| Image node | `I` |
| Post node | `V` |
| Document node | `D` |
| Web page node | `W` |

1. Click a node type in the toolbar (or press its hotkey).
2. The canvas enters add mode and shows "Click anywhere on the canvas to add" followed by the node type.
3. Click where you want the node. Press `Esc` to cancel.

The toolbar also has **Tidy Up** (`0`) and **Search** (`⌘K`).

**Use cases**

- Press `T`, click, and jot a quick note while reading — no menus needed.
- Press `C` repeatedly to lay out several chat nodes for parallel questions on a research canvas.

#### From the right-click menu

Right-click any empty spot on the canvas and open the **Add** menu:

- **Chat Node**
- **Text Node**
- **Web Node**
- **Post Node**
- **Document Node** (Beta)
- **Image Node** (Beta)

The node appears where you right-clicked.

[](https://media.rabbitholes.download/right-click-menu.mp4)

#### Quick chat node with Cmd+Click

Hold `Cmd` (Mac) or `Ctrl` (Windows) and click anywhere on empty canvas to instantly create a Chat node there. This is the fastest way to start a conversation.

[](https://media.rabbitholes.download/docs/v5/chat%20node.mp4)

**Use cases**

- Mid-reading, a question pops into your head — `Cmd`+click next to the source node and ask.
- Sketching a study plan: `Cmd`+click a row of chat nodes, one per subtopic, then connect them later.

#### Drag and drop files

Drop files from your computer straight onto the canvas:

- **Images** become Image nodes.
- **Documents and text files** become Document nodes.
- Dropping multiple files at once fans them out horizontally.

> Unsupported file types show a toast: "File type .ext is not supported" (with the file's actual extension). See [Document Node](https://www.slashspace.ai/docs/nodes/file-node) for the supported document formats.

**Use cases**

- Drop a folder's worth of lecture PDFs onto a canvas, then connect them to a chat node and quiz yourself.
- Drag in reference screenshots while planning a design, and annotate each with a connected chat.

#### Paste with ⌘V

Paste (`⌘V` / `Ctrl+V`) is content-aware:

- **Copied nodes** paste as nodes (see [Organizing](https://www.slashspace.ai/docs/canvas/organizing)).
- **A video or social URL** becomes a Post node.
- **Any other URL** becomes a Web node.
- **Plain text** becomes a Text node.
- **Image files on the clipboard** become Image nodes.

**Use cases**

- Copy a YouTube link from your browser, paste on the canvas, and get a Post node ready for transcript-aware chat.
- Paste a paragraph from an article as a Text node, then branch a chat off it to dig deeper.
- Collect sources fast: paste five article URLs one after another while researching, sort them out afterwards.

#### Drag from a node's handle

Drag from any node's right-side handle onto empty canvas and release — a new Chat node appears, already connected to the source node. This is the natural way to "ask a question about this node". See [Connections](https://www.slashspace.ai/docs/canvas/connections) for how context flows through that edge.

**Use cases**

- Pull a thread from a Web node to summarize the page.
- Branch three separate chats off one Document node — compare answers side by side.

### Export
*Download a canvas as Markdown or JSON for backup, sharing, or use in other tools.*

**Source:** https://www.slashspace.ai/docs/canvas/export

You can export any canvas from the right-click menu. Two formats are available, each suited to a different job.

#### Exporting a canvas

1. Right-click anywhere on the canvas.
2. Choose **Download Canvas**.
3. Pick **Markdown** or **JSON**.

[](https://media.rabbitholes.download/docs/v5/export_options.mp4)

#### Markdown (.md)

A readable document version of your canvas:

- The canvas name as the title.
- A section per node with its content.
- Chat nodes include every message under role headings, so full conversations are preserved in readable form.

**Use cases**

- Paste your research canvas into Notion, Obsidian, or a Google Doc as the starting point for a written report.
- Share a conversation's full transcript with a teammate who doesn't use Slashspace.
- Turn a studying canvas into printable revision notes.

#### JSON (.json)

The complete canvas file, pretty-printed — nodes, edges, positions, and settings.

**Use cases**

- Back up an important canvas before a big restructuring session.
- Process your canvas data with your own scripts or tools.
- Archive finished projects outside the app.

> The desktop app is local-first — your canvases already live as files on your machine (see [Core Concepts](https://www.slashspace.ai/docs/core-concepts)). Exports give you portable copies in standard formats.

### Keyboard Shortcuts
*Every keyboard shortcut in the desktop app, grouped by where it works.*

**Source:** https://www.slashspace.ai/docs/canvas/keyboard-shortcuts

On Windows and Linux, read `⌘` as `Ctrl`.

#### Canvas

| Shortcut | Action |
| --- | --- |
| `⌘K` | Open [search](https://www.slashspace.ai/docs/canvas/search) |
| `⌘A` | Select all nodes |
| `Esc` | Deselect / exit the current mode |
| `Space` + drag | Pan the canvas |
| `⌘` + click | Create a Chat node at the cursor |
| `0` | Tidy Up (auto-arrange nodes) |
| `Backspace` / `Delete` | Delete the selected nodes or edges |
| `⌘C` | Copy selected nodes |
| `⌘V` | Paste nodes (or clipboard content — see [Creating Nodes](https://www.slashspace.ai/docs/canvas/creating-nodes)) |

#### Node creation

Press a letter, then click the canvas to place the node:

| Shortcut | Node type |
| --- | --- |
| `C` | Chat node |
| `T` | Text node |
| `I` | Image node |
| `V` | Post node |
| `D` | Document node |
| `W` | Web page node |

#### Chat node

| Shortcut | Action |
| --- | --- |
| `Enter` | Send message |
| `Shift` + `Enter` | New line |
| `⌘⇧Enter` | Send the message into a new branch |
| `⌘B` | Create a branch from the active node |
| `Ctrl` + `M` | Start [voice input](https://www.slashspace.ai/docs/ai-features/voice-input) |
| `Enter` | Finish recording (while recording) |
| `Esc` | Cancel recording (while recording) |

#### Text formatting (bubble menu)

| Shortcut | Action |
| --- | --- |
| `Enter` | Submit |
| `Shift` + `Enter` | New line |
| `Esc` | Close the menu |

### Organizing the Canvas
*Select, align, group, color, copy, and auto-arrange nodes to keep large canvases readable.*

**Source:** https://www.slashspace.ai/docs/canvas/organizing

Canvases grow fast. These tools keep them readable — selection, alignment, groups, colors, and one-key auto-layout.

#### Selecting nodes

- **Box select** — left-click and drag across empty canvas to draw a selection box.
- **Add to selection** — hold `Shift` and click individual nodes to add or remove them.
- **Select all** — `⌘A`.
- **Deselect** — `Esc`.

[](https://media.rabbitholes.download/multi-selection.mp4)

#### Align, distribute, and group

When two or more nodes are selected, a floating toolbar appears with:

1. **Align top** — lines up the selected nodes along their top edges.
2. **Distribute horizontally** / **Distribute vertically** — evens out the spacing (needs at least 3 nodes).
3. **Group selection** — wraps the selection in a group.

**Use cases**

- Select a row of source nodes and **Align top** + **Distribute horizontally** for a clean reading order.
- Grab a messy cluster of brainstorm notes and group them into "Ideas" before moving on.

#### Groups

A group is a container with a dashed border and an editable label (it starts as "Untitled"):

- Drag the group to move all its children as a unit.
- Resize the group by dragging its edges.
- Select a group to get two extra actions: **Ungroup** (dissolve the container, keep the nodes) and **Tidy up** (auto-arrange just the nodes inside it).

See [Group Node](https://www.slashspace.ai/docs/nodes/group-node) for details.

**Use cases**

- Group each chapter's notes on a studying canvas so you can shuffle whole chapters around.
- Keep "raw sources" and "conclusions" in separate labeled groups on a research canvas.

#### Node colors

Give nodes a color to encode meaning:

1. Select a node and click the **Change Color** swatch.
2. Pick from the **Pick a color** grid.
3. Choosing stone (the default shade) resets the node to no color.

**Use cases**

- Color-code by status while planning: green = done, amber = in progress, red = blocked.
- Mark primary sources one color and your own commentary another.

#### Minimize and maximize

- Chat nodes have a per-node collapse toggle to shrink them down to a header.
- Right-click the canvas and use the **View** menu's **Minimize All** / **Maximize All** to collapse or expand every chat and text node at once.

**Use cases**

- Minimize all before a review pass — you see the structure of your thinking, not walls of text.

#### Focus a node

Double-click a Text node's header to center the view on it.

[](https://media.rabbitholes.download/docs/v5/focus-header.mp4)

#### Copy, paste, and duplicate

- **Copy** — `⌘C` copies the selected nodes (toast: "Copied N node(s)").
- **Paste** — `⌘V` pastes them at your cursor position (toast: "Pasted N node(s)").
- **Duplicate** — use the Duplicate action on a node to clone it, offset to the right.

**Use cases**

- Copy a configured chat node (model, persona, connections in place) as a template for new questions.
- Duplicate a text node to fork a draft while keeping the original intact.

#### Delete and restore

Select nodes and press `Backspace`/`Delete`. A toast appears with a **Restore** button so you can undo the deletion.

> Restoring a deleted node does not restore its RAG embeddings — re-index the content if you rely on AI Search or RAG over that node.

#### Tidy Up

**Tidy Up** runs an automatic left-to-right layout over the whole canvas, arranging nodes by their connections. Trigger it three ways:

1. Press `0`.
2. Click the broom icon in the toolbar.
3. Right-click → **View** → **Tidy Up**.

A selected group also offers its own **Tidy up** that only rearranges that group's children.

**Use cases**

- After a fast brainstorm where you dropped nodes everywhere, one keypress turns chaos into a readable flow.
- Before exporting or sharing a screenshot, tidy up so the context flow reads left to right.

### Search
*Find anything on the canvas with fuzzy Local Search or semantic AI Search.*

**Source:** https://www.slashspace.ai/docs/canvas/search

Press `⌘K` (or click **Search** in the toolbar) to open the search dialog — "What are you looking for?". It has two modes you can toggle between: **Local Search** and **AI Search**.

#### Local Search

Local Search (the zap icon) is instant, fuzzy, keyword-style search over the current canvas:

1. Press `⌘K` and start typing.
2. Results match against node labels, node content, and individual chat messages, each with a **% match** score.
3. Use the arrow keys to move through results and `Enter` to jump — the canvas centers on the node and highlights the matched message.

[](https://media.rabbitholes.download/docs/v5/local_search.mp4)

**Use cases**

- "Where did the AI mention 'transformer architecture'?" — jump straight to that message in a 30-node research canvas.
- Find the text node holding your thesis statement by typing a few of its words.
- Relocate a source node by its title without scrolling around the canvas.

#### AI Search

AI Search (the sparkles icon) is semantic: it understands meaning, not just keywords. It runs a RAG-style search over the indexed content of the current canvas and returns the 10 most relevant matches.

1. Open search with `⌘K` and switch to **AI Search**.
2. Describe what you're looking for in natural language.
3. Jump to any result.

> AI Search requires the cloud indexing privacy opt-in. If you haven't enabled it, the dialog shows "You have not opted in for cloud indexing!" with a button to enable it. Manage this in [Account Management](https://www.slashspace.ai/docs/settings/account-management). Learn how indexing powers other features in [RAG Mode](https://www.slashspace.ai/docs/ai-features/rag-mode).

**Use cases**

- Search "arguments against my main claim" — matches by meaning even if no node uses those words.
- On a studying canvas, ask "the part about enzyme inhibition" to surface the right lecture excerpt.
- Rediscover an idea you phrased differently weeks ago ("that analogy about rivers and attention").

#### Which one to use

|  | Local Search | AI Search |
| --- | --- | --- |
| Matching | Fuzzy keyword | Semantic (by meaning) |
| Speed | Instant | A moment to run |
| Needs opt-in | No | Yes (cloud indexing) |
| Best for | Exact words you remember | Concepts you can describe |

### Side View
*A full-height panel for reading and working in one node without losing your place on the canvas.*

**Source:** https://www.slashspace.ai/docs/canvas/side-view

Side View is a right-hand panel that shows the active node's content at full height. It gives you a focused, document-like view of a single node while the canvas stays visible next to it.

#### Opening Side View

1. Click the **panel icon** in the top-right of the canvas header to toggle the panel.
2. Click any node on the canvas — the panel shows its content.
3. Click a different node to switch the panel to it.

Until you select a node, the panel shows: "Select a node on the canvas to view its content here".

[](https://media.rabbitholes.download/docs/v5/sideview.mp4)

#### What each node type shows

- **Chat node** — the full conversation, with a compact message input pinned to the bottom so you can keep chatting from the panel.
- **Text node** — the text, editable right in the panel.
- **Image node** — the image at full size.
- **Web node** — the captured page content.
- **Document node** — the document's content.
- **Post node** — the post's content.

#### Use cases

- **Reading long AI answers** — a detailed response is much easier to read in a full-height column than inside a node on the canvas.
- **Writing** — open a draft Text node in Side View and edit it like a document, while glancing at your outline and source nodes on the canvas.
- **Research triage** — keep Side View open and click through your Web and Document nodes one by one to skim each source without opening and closing anything.
- **Chatting while navigating** — continue a conversation from the panel's input while you pan around the canvas connecting new context to it.


---

## Nodes

### Chat Node
*Talk to AI models on the canvas — with branching, connected context, tools, and voice input.*

**Source:** https://www.slashspace.ai/docs/nodes/chat-node

The Chat Node is the primary way to interact with AI models. It supports back-and-forth conversations, tool calling, context from connected nodes, and multiple AI providers.

[](https://media.rabbitholes.download/docs/v5/chat%20node.mp4)

---

#### Sending messages

Type your message in the input field at the bottom of the chat node.

- `Enter` submits your message
- `Shift+Enter` inserts a new line (also works inside code blocks and lists)
- `⌘⇧Enter` submits your prompt into a new branch node (the **Split** button — tooltip "Submit in new branch")
- `⌘B` creates an empty branch node

You can also click the **Send** button (up arrow) to submit. While a response is streaming, the Send and Split buttons combine into a single **Stop** button. When the input is empty, a microphone button appears in the send slot instead (title "Start recording") — see [Voice input](#voice-input).

---

#### Slash commands

Type `/` in the input to open the command menu. It contains three kinds of entries:

1. **MCP server toggles** — enable or disable an MCP server for this conversation
2. **Reasoning: Low / Medium / High / Max** — quick actions to set reasoning effort
3. Your **skills and prompts library** — reusable prompts you've saved (see [Slash Commands](https://www.slashspace.ai/docs/ai-features/slash-commands))

Inserted references render as chips in the input.

> If a referenced item is missing or too large, you'll see an error toast before the message is sent.

#### @ mentions

Type `@` to search the nodes on your canvas by name. Selecting a node inserts it as a chip in your message and creates a persistent connection (edge) from that node, so its content feeds this chat as context — a fast way to wire up context without dragging edges by hand. See [Connections](https://www.slashspace.ai/docs/canvas/connections) for how context flows between nodes.

---

#### Choosing a model

1. Click the **model dropdown** at the bottom left of the chat input
2. Use the **Search models…** box to filter, or browse the groups:
   - **Rabbitholes** tiers first — **Basic** ("Claude Haiku 3.5 or equivalent"), **Pro** ("Claude Sonnet 4.5 or equivalent"), and **Advanced** ("Opus 4.7 / Gpt 5.5 equivalent")
   - **Agent providers** (such as Cursor and Claude Code)
   - Your own **BYOK providers** (bring your own key)
3. Click a model to select it for this node

> On the Free plan, BYOK providers show a lock icon and an amber **Paid** tag. Use the **Manage AI Models** link in the dropdown to open Settings. See [Models](https://www.slashspace.ai/docs/ai-features/models) for details.

When an agent-provider model (Cursor or Claude Code) is selected, a folder button appears next to the input so you can pick the **agent workspace** — the working directory the agent operates in.

---

#### Tools dropdown

Click the **+** button in the chat input (tooltip "Tools") to configure this conversation:

- **MCP** — a checkbox list of your MCP servers, enabled per conversation. **Add New** opens Settings. See [MCP Tools](https://www.slashspace.ai/docs/ai-features/mcp-tools).
- **Personalities** — pick a persona for this chat, or choose **Add New** to create one inline. See [Personas](https://www.slashspace.ai/docs/ai-features/personas).
- **Reasoning** — radio options **Low / Medium / High / Max** for models that support extended thinking. The default is **Medium**.
- **RAG Mode** — a switch that turns on Retrieval Augmented Generation for this node.

> On the Free plan the RAG Mode switch shows a lock, and clicking it opens an upgrade modal: "RAG Mode Requires a Paid Plan".

---

#### RAG mode

RAG mode retrieves only the most relevant chunks from connected nodes instead of sending everything, which can dramatically reduce input size. Deep dive: [RAG Mode](https://www.slashspace.ai/docs/ai-features/rag-mode).

While RAG mode is on:

- A scissors icon labeled **RAG Mode Active** appears in the node footer
- The token pill is masked with asterisks (exact counts aren't known until retrieval runs)
- Status banners report progress: **Indexing documents…**, **Documents indexed**, **Retrieving relevant chunks…**, **Reranking results…**, and an error banner if something fails
- After a response, a summary shows the savings: "RAG Mode reduced your input size by N% from X to Y tokens."

> RAG mode with Rabbitholes managed models is temporarily unavailable in the desktop app — use a BYOK provider for RAG conversations.

> You can chat with document nodes immediately after adding them. Only RAG mode requires their processing to be complete.

---

#### Message actions

Hover over a **user message** to reveal:

- **Copy** — copy the message text
- **Rerun** — re-send the same text
- **Edit** — opens the **Edit Message** dialog with **Save** and **Save & Rerun** (`⌘Enter`). **Save & Rerun** removes all later messages and regenerates the response from this point.

**Assistant messages** offer:

- **Copy** and **Regenerate**
- A collapsible **reasoning** section when the model produced extended thinking
- **Tool-call cards** for any tools the model used
- **Source citations**, shown as stacked source pills

---

#### Tool calls and approvals

Each tool the AI invokes appears as a collapsible card with a state of **Running**, **Done**, or **Error**.

If a tool requires permission, the card asks **"Allow this tool to run?"** with **Approve** and **Reject** buttons. Long tool output is truncated with a **Show more** control.

---

#### Context modes

A toggle on the node's left edge controls how content from connected nodes is passed in:

- **Summarized context** (zap icon) — incoming context is condensed
- **Isolated context** (diamond icon) — the node ignores summarization and treats context separately

A badge on the toggle shows how many incoming connections the node has.

> The toggle is disabled while a response is generating — you'll see "Wait for the response to finish".

---

#### Token summary

The footer shows a token pill. Click it to open the **Token Summary** popover, which lists:

- **Incoming** — tokens flowing in from connected nodes
- **Own** — tokens from this node's conversation
- **Input** — what will be sent to the model
- **Total**

Counts are estimates produced with the OpenAI tokenizer. In RAG mode the pill shows asterisks until retrieval determines the real input size.

---

#### Voice input

1. Click the **microphone** button (visible when the input is empty) or press `Ctrl+M`
2. Speak — an overlay shows a timer and a live waveform
3. Click **Done** or press `Enter` to finish, or **Cancel** / `Esc` to discard
4. Wait for **Transcribing…** — the transcript replaces your input text
5. Edit if needed, then press `Enter` to send

Recording uses your preferred microphone from System Preferences. More: [Voice Input](https://www.slashspace.ai/docs/ai-features/voice-input).

---

#### Node controls

The node header and toolbar give you:

- **Color picker** — tag the node with a color
- **Duplicate Node**
- **Collapse** — the minimized view shows the last You/Assistant snippet with a **See More** button
- **Open in Sidebar** — read the conversation in the [side view](https://www.slashspace.ai/docs/canvas/side-view)
- **Delete Node**

Chat nodes get auto-generated titles based on the conversation.

---

#### Errors and sub-agents

- **Insufficient credits** — an amber banner appears with a **Reload usage** button
- **Plan-gated features** — the banner includes an **Upgrade** button
- **Other errors** — a red banner with a **Retry** button

The AI can also spawn child chat nodes as sub-agents to work on parts of a task. A live activity card shows progress ("Subagent is thinking…") with **Jump to node** and **Cancel** actions. See [Sub-agents](https://www.slashspace.ai/docs/ai-features/sub-agents).

---

#### Use cases

- **Research** — connect [web](https://www.slashspace.ai/docs/nodes/web-node), [document](https://www.slashspace.ai/docs/nodes/file-node), and [post](https://www.slashspace.ai/docs/nodes/youtube-node) nodes to a chat and ask questions across all your sources at once.
- **Writing** — draft in a chat, then use `⌘⇧Enter` to branch alternative directions without losing the original thread.
- **Studying** — turn lecture PDFs into a Q&A partner: attach them with `@`, enable RAG mode, and quiz yourself.
- **Content creation** — use personas to keep a consistent voice, and Rerun/Edit to iterate on hooks and titles quickly.
- **Planning** — let the AI spawn sub-agents to explore options in parallel, then compare the branches side by side on the canvas.

### Document Node (Beta)
*Upload PDFs, Office files, and more — the node indexes them so you can chat about their content.*

**Source:** https://www.slashspace.ai/docs/nodes/file-node

The Document Node brings your files onto the canvas. Drop in a PDF, spreadsheet, or presentation and it's uploaded, converted, and indexed so connected chats can read it.

> Also referred to as the "File Node" — its type ID and this page's URL are unchanged.

---

#### Supported files

- **Documents**: `pdf`, `doc`, `docx`, `rtf`, `txt`, `md`, `html`
- **Presentations**: `ppt`, `pptx`
- **Data**: `xls`, `xlsx`, `csv`, `json`, `xml`

---

#### Adding a document

You can add a document three ways:

1. Press `D` (or pick the file icon from the toolbar) and choose a file
2. Right-click the canvas and use the **Add** menu
3. **Drag and drop** a file directly onto the canvas

The file uploads and starts indexing automatically as soon as it's added.

---

#### Processing states

The node shows its progress:

- **Starting...** — upload is beginning
- A **progress** indicator while the file is processed and indexed
- An **error state** with a **Retry** button if something fails
- **Ready** — processing is complete, with buttons to open the converted `.md` and the `.pdf`

> Failed uploads don't retry automatically — click **Retry** on the node.

PDFs show an inline preview in the node. Non-PDF files show a file-type badge and a **Reveal in Folder** button to locate the original on disk.

---

#### Chatting about the document

Connect the document node to a chat node (or `@`-mention it from a chat) and its content becomes context.

> You can chat about a document **immediately** — you don't need to wait for processing to finish. Only [RAG mode](https://www.slashspace.ai/docs/ai-features/rag-mode) requires processing to be complete, since it depends on the index.

For large documents, RAG mode is the recommended way to chat: it retrieves only the relevant chunks instead of sending the whole file.

---

#### Use cases

- **Research** — load a folder of papers and use RAG mode to ask questions across all of them without blowing up your token budget.
- **Writing** — attach your source material (interviews, reports) and draft with a chat that can cite it.
- **Studying** — upload lecture slides (`pptx`) and readings, then generate summaries and practice questions.
- **Content creation** — turn a long PDF report into a thread, script, or newsletter with a connected chat.
- **Planning** — drop in spreadsheets (`xlsx`, `csv`) of budgets or timelines and ask the AI to spot risks or summarize totals.

### Group Node
*Bundle related nodes into a labeled, movable container to keep large canvases organized.*

**Source:** https://www.slashspace.ai/docs/nodes/group-node

The Group Node is a container that holds other nodes. Move the group and everything inside moves with it — ideal for keeping big canvases tidy.

---

#### Creating a group

1. Select **two or more nodes** (drag a selection box, or `Shift`-click nodes)
2. Click **Group selection** in the floating toolbar that appears

The selected nodes are wrapped in a dashed-border container.

---

#### Working with a group

- **Label** — click the title field (placeholder **"Untitled"**) above the group and type a name
- **Move** — drag the group; all child nodes move with it
- **Resize** — drag the group's edges to change its size

> A group can't be resized smaller than 100 × 100.

When the group is selected, two actions appear next to its label:

- **Ungroup** — detaches all child nodes from the group
- **Tidy up** — auto-arranges the nodes inside the group

---

#### Organizing large canvases

Groups pair well with the rest of the canvas tools — see [Organizing your canvas](https://www.slashspace.ai/docs/canvas/organizing). Use one group per topic, source cluster, or project phase, and give each a clear label so you can navigate by structure instead of by memory.

---

#### Use cases

- **Research** — group each source cluster (papers, web pages, and the chats about them) by theme so threads don't tangle.
- **Writing** — keep one group per chapter or section, each containing its notes, drafts, and revision chats.
- **Studying** — make a group per subject or week, then **Tidy up** before a review session to see everything at a glance.
- **Content creation** — separate ideation, drafting, and final-asset nodes into labeled stages of your pipeline.
- **Planning** — group nodes by project phase (discovery, build, launch) and move whole phases around as the plan evolves.

### Image Node
*Upload images or generate them with AI, then chat about their content on the canvas.*

**Source:** https://www.slashspace.ai/docs/nodes/image-node

The Image Node holds a picture on your canvas — one you upload, or one you generate with AI. Either way, the image's content is parsed so connected chats can discuss it.

---

#### Supported files

- JPG, PNG, GIF, WebP

---

#### Uploading an image

1. Double-click the canvas and choose the **image** icon
2. Click **Add From Computer**, or drag and drop an image file onto the node
3. The AI parses the image content automatically, so any connected chat can discuss what's in it

After parsing, open the **Parsed Content** dialog on the node to see what the AI extracted.

---

#### Generating an image

1. In an empty image node, type into the prompt input — **"Generate image with a description (BETA)..."**
2. Pick a model from the **model dropdown** — models from **Straico**, **OpenAI**, and **Fal AI** (e.g. Flux, Imagen4, GPT Image, Nano Banana)
3. Choose a size preset: **Square 1:1**, **Landscape 16:9**, or **Portrait 9:16**
4. Click **Generate ⏎**

While generating, a **Stop** button lets you cancel. The finished image appears in the node with a badge showing which model made it.

> Image generation requires an API key for at least one supported provider. Set your default generation models in [Settings → Default Models](https://www.slashspace.ai/docs/settings/default-models).

---

#### Image-to-image

Connect one or more Image nodes into an image node as reference inputs:

1. Draw a connection from an existing Image node into your image node
2. The node automatically switches to an edit-capable model
3. Write a prompt describing the change and click **Generate ⏎**

> Image nodes only accept Image-node inputs — you can't connect text, web, or document nodes as generation references.

---

#### After generation

- Click the prompt indicator to open the **Prompt** dialog, which shows the prompt used, the model, and a **Copy Prompt** button
- A **model badge** on the node shows which model produced the image
- The **Parsed Content** dialog shows the AI's description of the image, which is what connected chats receive as context

---

#### Use cases

- **Research** — drop in charts or diagrams from papers; the parsed content lets a connected chat explain or compare them.
- **Writing** — generate a mood or scene image to anchor a piece of descriptive writing.
- **Studying** — upload textbook figures and ask a connected chat to walk you through what they show.
- **Content creation** — iterate on thumbnails and social images with size presets, then refine with image-to-image passes.
- **Planning** — sketch or screenshot a layout, upload it, and have the AI critique or list next steps.

### Text Node
*A rich-text note on the canvas — write, format, and branch AI conversations from your own words.*

**Source:** https://www.slashspace.ai/docs/nodes/text-node

The Text Node is a rich-text editor that lives on your canvas. Use it for notes, outlines, drafts, and any writing you want the AI to see as context.

---

#### Creating a text node

1. Double-click the canvas (or use the toolbar) and choose the **text** icon
2. Type or paste your text
3. Connect it to a chat node — or branch directly from it — to discuss the content with AI

See [Creating Nodes](https://www.slashspace.ai/docs/canvas/creating-nodes) for all the ways to add nodes.

---

#### Formatting toolbar

Select the node and use the toolbar to format your text:

- **Heading 1**, **Heading 2**, **Heading 3**
- **Bold**, **Italic**, **Strikethrough**
- **Code** (inline)
- **Bullet list** and **Numbered list**
- **Blockquote**

Markdown syntax is also supported — type `#` , `**bold**`, `-` , `>` , and so on, and it renders as rich text.

> `Enter` inserts a newline inside a text node (unlike chat nodes, where it sends a message).

---

#### Editing behavior

- The node **auto-grows** as you write — no manual resizing needed
- **Double-click the node's header** to center it on your screen
- Edits sync with the [side view](https://www.slashspace.ai/docs/canvas/side-view), so you can read or edit the same text there

---

#### Ask about a selection

You can branch a conversation from any passage:

1. Select text inside the node
2. A floating input appears: **"Ask about this… (↵ to expand)"**
3. Type a question and press `Enter`

This spawns a connected branch chat node focused on your selection.

---

#### Voice input

Click the **microphone** icon or press `Ctrl+M` to dictate. Your speech is transcribed directly into the node. See [Voice Input](https://www.slashspace.ai/docs/ai-features/voice-input).

---

#### Use cases

- **Research** — keep running notes next to your sources, then select a claim and ask the AI to verify or expand it.
- **Writing** — draft an article in a text node and branch chats from individual paragraphs to rework them.
- **Studying** — summarize a lecture in your own words, then quiz yourself by asking about specific selections.
- **Content creation** — store your brand voice guidelines in a text node and connect it to every chat that writes copy.
- **Planning** — outline a project plan with headings and lists, and let connected chats flesh out each section.

### Web Node
*Capture a webpage's screenshot and content so the AI can read and discuss it.*

**Source:** https://www.slashspace.ai/docs/nodes/web-node

The Web Node pulls a live webpage into your canvas. It captures a screenshot, parses the page into readable content, and makes both available to connected chats.

---

#### Adding a webpage

1. Double-click the canvas and choose the **web** icon. The empty node prompts: **"Enter a webpage URL to capture a screenshot and parse its content…"**
2. Paste or type the URL into the input
3. Click **Go**

While the page loads, the button shows **Scraping...**. If the capture fails, red error text appears — you can correct the URL and try again.

---

#### What you get

Once scraping finishes, the node shows:

- A **screenshot** of the page, or the **parsed markdown** content
- The site's **domain** in the node footer
- A **full-content dialog** — open it to read everything that was extracted

---

#### Using it as context

Connect the web node to a chat node (drag an edge, or `@`-mention it from the chat). The parsed page content flows in as context, so you can ask questions about the article, compare it with other sources, or quote from it. See [Connections](https://www.slashspace.ai/docs/canvas/connections).

> Paywalled or heavily JavaScript-driven sites may fail to parse or return incomplete content. Retry, or use a different source (for example an archived or reader-friendly version of the page).

---

#### Use cases

- **Research** — capture several articles on a topic, connect them all to one chat, and ask for a synthesis with the sources side by side.
- **Writing** — pull in a reference piece and ask a connected chat to match its structure or argue against it.
- **Studying** — save documentation pages or tutorials and ask the AI to explain the parts you're stuck on.
- **Content creation** — capture a competitor's landing page and brainstorm how your version should differ.
- **Planning** — collect pricing pages, reviews, or specs for options you're comparing, and let the AI build the comparison.

### Post Node (YouTube & more)
*Bring videos and social posts onto the canvas — transcripts and content are fetched automatically.*

**Source:** https://www.slashspace.ai/docs/nodes/youtube-node

The Post Node embeds a video or social post on your canvas and fetches its transcript or content, so connected chats can discuss it.

> Originally YouTube-only, this node now supports **YouTube, TikTok, Instagram, Facebook, X, and LinkedIn** URLs. Existing YouTube nodes migrate automatically — the type ID and this page's URL are unchanged.

---

#### Adding a post

1. Double-click the canvas and choose the **Post** icon. The empty node shows **"Add a post URL"** with the hint "Supports YouTube, TikTok, Instagram, Facebook, X, and LinkedIn"
2. Paste the URL of a video or post
3. The node **auto-detects the platform** and loads an embedded player or post preview

Use the **open-external** button on the node to view the original in your browser.

---

#### Transcripts and content

- For videos, the **transcript is fetched automatically** after the post loads
- The node shows a **processing** state while content is being retrieved
- If fetching fails, the node shows a **failed** state with a **retry** option

> Transcript availability depends on the platform and the post — some videos have no captions to fetch. Retry, or try a different link for the same content.

---

#### Chatting about a post

Connect the post node to a chat node (or `@`-mention it). The transcript or post content flows in as context, so you can summarize, quote, or analyze it. See [Connections](https://www.slashspace.ai/docs/canvas/connections).

---

#### Use cases

- **Research** — collect conference talks and interviews on a topic and ask a connected chat to extract the key claims from each.
- **Writing** — quote accurately from a video by working from its transcript instead of your memory.
- **Studying** — paste a lecture or tutorial video and generate notes, summaries, and flashcard-style questions.
- **Content creation** — analyze a viral post or video's structure and hooks, then draft your own take in a branch chat.
- **Planning** — gather product reviews and walkthrough videos when evaluating tools, and let the AI compare what they say.


---

## AI Features

### Using MCP Tools in Chat
*Let the AI call external tools from your configured MCP servers during a conversation.*

**Source:** https://www.slashspace.ai/docs/ai-features/mcp-tools

MCP (Model Context Protocol) is an open standard for connecting AI models to external tool servers — things like file systems, databases, browsers, or your own scripts. Once a server is configured, the AI can call its tools mid-conversation and use the results in its answer.

Server setup lives in [Settings → MCP Servers (Beta)](https://www.slashspace.ai/docs/settings/mcp-servers). This page covers using those servers in a [Chat Node](https://www.slashspace.ai/docs/nodes/chat-node).

---

#### Enabling MCP servers for a conversation

MCP servers are enabled per conversation, so tools are only offered where you want them. Three ways to enable one:

1. Open the **+** tools dropdown and check servers in the **MCP** checkbox list
2. Or type `/` and use the MCP quick-toggles in the [slash menu](https://www.slashspace.ai/docs/ai-features/slash-commands)
3. Or click an existing server chip in the chat footer

Active servers show as removable pill chips in the chat footer — click a chip's remove control to disable that server for the conversation.

> MCP requires a model that supports tool calling. All Rabbitholes managed models do; for other providers, check the model's capabilities in [Models & Providers](https://www.slashspace.ai/docs/ai-features/models).

---

#### Tool calls in the transcript

When the AI decides to use a tool, a tool-call card appears in the conversation showing the tool's name and its state:

- **Running** — the call is in flight, with a spinner
- **Done** — the call finished; expand the card to inspect the output, with **Show more** for long results
- **Error** — the call failed; the card shows the error message

The AI can chain several tool calls in one turn — each gets its own card, and the final answer follows once the calls resolve.

---

#### Approving tool calls

Some tool calls pause for your confirmation before running. The card asks **Allow this tool to run?** with two choices:

1. **Approve** — the tool runs and the conversation continues with its result
2. **Reject** — the tool is skipped and the AI is told the call was declined

This keeps you in control of tools that touch your files, network, or accounts.

---

#### Use cases

- **Live data in answers**: a database MCP server lets the AI query real numbers instead of guessing, right inside your research canvas.
- **File operations**: a filesystem server lets the AI read a project folder and summarize it into connected [Text Nodes](https://www.slashspace.ai/docs/nodes/text-node).
- **Web automation**: a browser server fetches pages the AI needs mid-conversation, beyond what a [Web Node](https://www.slashspace.ai/docs/nodes/web-node) captured.
- **Safe experimentation**: enable a powerful server for one conversation only, approve each call manually, and remove the chip when done.

### Models & Providers
*Understand the three ways to run AI in the desktop app and how to configure models.*

**Source:** https://www.slashspace.ai/docs/ai-features/models

Every [Chat Node](https://www.slashspace.ai/docs/nodes/chat-node) runs against a model you choose. The desktop app gives you three ways to run AI, and you can mix them freely across a canvas.

---

#### Three ways to run AI

**1. Rabbitholes managed models (built-in)**

No setup required — these use your signed-in session and consume credits from your account. In the model dropdown they appear as tiers:

- **Basic** — Claude Haiku 3.5 or equivalent
- **Pro** — Claude Sonnet 4.5 or equivalent
- **Advanced** — Opus 4.7 / Gpt 5.5 equivalent

**2. Bring your own key (BYOK) cloud providers**

Add your own API key for OpenAI, Anthropic, Google, Perplexity, xAI, OpenRouter, Straico, Qolaba, DeepSeek, Groq, or Fal AI (Beta). Requests go directly through your key, so no credits are used. Set these up in [Settings → Providers](https://www.slashspace.ai/docs/settings/providers).

> BYOK providers require a Pro plan or higher.

**3. Local models via Ollama**

Run models entirely on your machine — free, private, and works offline. See [Settings → Ollama](https://www.slashspace.ai/docs/settings/ollama).

Two more options extend the list:

- **Agent providers** — use the Cursor or Claude Code CLIs installed on your machine as chat backends. See [Settings → Agent Providers](https://www.slashspace.ai/docs/settings/agent-providers).
- **Custom providers** — connect any OpenAI-compatible endpoint. See [Settings → Custom Providers](https://www.slashspace.ai/docs/settings/custom-providers) (Pro plan or higher).

---

#### The model dropdown

Click the model name at the bottom left of any chat input to open the model dropdown.

1. Models are grouped by source: **Rabbitholes** tiers first, then agent providers, then your configured cloud providers
2. Type in the search field to filter models by name
3. Click a model to select it for this node

> On the free plan, models that require a paid plan show a lock icon and a **Paid** tag.

Use the **Manage AI Models** link at the bottom of the dropdown to jump straight to provider settings.

---

#### Per-model settings

You can tune each model individually:

1. Open **Settings** and select the provider
2. Click a model in the provider's model list
3. Adjust the available fields:

   - **Alias** — a display name of your choosing
   - **System Prompt** — instructions prepended to every conversation with this model
   - **Advanced** — **Temperature** (0–1), **Top K** (1–20), **Top P** (0–1), **Presence Penalty**, **Frequency Penalty**, **Max Tokens**, **Max Steps**
4. Click **Save changes**, or **Restore defaults** to reset

---

#### Reasoning effort

For models that support extended thinking, you can control how long the model reasons before answering:

1. Open the **+** tools dropdown in a chat input (or type `/` for the slash menu)
2. Select a **Reasoning Effort** level: **Low**, **Medium**, **High**, or **Max**

The default is **Medium**. Higher levels give the model more thinking time for complex problems. See [Slash Commands](https://www.slashspace.ai/docs/ai-features/slash-commands) for the `/` shortcuts.

---

#### Default models

Set app-wide defaults in [Settings → Default Models](https://www.slashspace.ai/docs/settings/default-models):

- **Default Chat Model** — used by new chat nodes
- **Title Generation Model** — names your conversations; pick a lightweight low cost model
- **Text-to-Image** and **Image-to-Image** — used by [Image Nodes](https://www.slashspace.ai/docs/nodes/image-node)

You can also override the default chat model per canvas in the canvas settings — nodes inheriting the app-wide setting show a **Global default** badge.

---

#### Credits

Rabbitholes managed models consume dollar-denominated credits from your account balance. BYOK providers and Ollama never touch your credits. Check your balance and plan in [Settings → Account](https://www.slashspace.ai/docs/settings/account-management).

---

#### Use cases

- **Zero-setup start**: sign in and use the Rabbitholes **Pro** tier immediately, without hunting for API keys.
- **Cost control on heavy workloads**: add your own Anthropic or OpenAI key so long research sessions bill your provider account instead of credits.
- **Private offline work**: run a local Ollama model for sensitive documents that must never leave your machine.
- **Fast titles, smart chats**: set a cheap model as the Title Generation Model while keeping an Advanced-tier model for the actual conversation.
- **Per-project tuning**: give a coding canvas its own default model and a lower temperature via per-model settings, while your writing canvas inherits the global default.

### Personas
*Save reusable system prompts that shape the AI's role and tone in any conversation.*

**Source:** https://www.slashspace.ai/docs/ai-features/personas

A persona is a saved system prompt — a set of instructions that shapes the AI's role, tone, and behavior. Create a persona once and apply it to any [Chat Node](https://www.slashspace.ai/docs/nodes/chat-node) conversation.

---

#### Creating a persona

From settings:

1. Open **Settings → Persona Prompts**
2. Click **Create Persona**
3. Fill in the fields:

   - **Name** — how the persona appears in pickers
   - **Color** — an identifying color for its chip
   - **Prompt** — the instructions the AI should follow
4. Click **Create**

Or create one inline without leaving your chat:

1. Open the **+** tools dropdown in the chat input
2. Go to **Personalities**
3. Click **Add New** and fill in the same fields

---

#### Applying a persona to a conversation

There are two ways to select a persona:

1. Open the **+** tools dropdown, go to **Personalities**, and check the persona you want
2. Or click the persona chip dropdown in the chat footer and pick from the list — type to search personas by name

The selected persona appears as a colored chip in the chat footer, and the AI follows its prompt for that conversation.

> Re-selecting the active persona clears it — click it again to remove the persona from the conversation.

---

#### Editing and deleting personas

1. Open **Settings → Persona Prompts** (see [Persona Prompts settings](https://www.slashspace.ai/docs/settings/persona-prompts))
2. Click a persona to open the edit dialog and change its name, color, or prompt
3. To remove it, click **Delete** in the edit dialog and confirm

---

#### Use cases

- **Consistent voice for writing**: a "Brand copywriter" persona that always writes in your product's tone, applied to every drafting chat.
- **Role-based review**: a "Staff engineer" persona that critiques code for edge cases, and a "Security reviewer" persona for a second pass — switch chips between messages.
- **Teaching mode**: a "Patient tutor" persona that explains step by step and asks you questions back, for learning canvases.
- **Format enforcement**: a persona that instructs the AI to always answer as a structured brief (summary, risks, next steps) for meeting-notes workflows.

### RAG Mode
*Send only the most relevant chunks of connected-node content instead of everything.*

**Source:** https://www.slashspace.ai/docs/ai-features/rag-mode

By default, a [Chat Node](https://www.slashspace.ai/docs/nodes/chat-node) sends the full content of every connected node to the model. RAG Mode (Retrieval Augmented Generation) changes that: your connected content is indexed, and on each message only the chunks most relevant to your question are retrieved and sent.

---

#### When to use it

Use RAG Mode when the incoming context is large — long documents, many connected nodes, big web pages. Retrieval trims the input dramatically, which cuts cost and keeps you inside the model's context window.

> For small context sizes (under roughly 10,000 tokens), RAG Mode is not recommended — sending everything is simpler and often gives better answers.

---

#### Enabling RAG Mode

1. Open the **+** tools dropdown in the chat input
2. Toggle the **RAG Mode** switch — or click the scissors icon in the chat input directly
3. The scissors icon highlights and shows **RAG Mode Active** on hover

> RAG Mode requires a paid plan. On the free plan the toggle shows a lock icon, and clicking it opens a **RAG Mode Requires a Paid Plan** modal. See [Account Management](https://www.slashspace.ai/docs/settings/account-management).

> AI Search in the ⌘K command menu uses the same index and requires the cloud indexing opt-in under **Settings → Account → Privacy Settings**.

---

#### What happens when you send

While RAG Mode is active, the token pill in the chat input is masked with asterisks — the real input size isn't known until retrieval runs. When you send a message, indexing runs first, and status banners appear above the chat in this order:

1. **Indexing documents…** — connected content is being chunked and embedded
2. **Documents indexed** — the index is up to date
3. **Retrieving relevant chunks…** — your question is matched against the index
4. **Reranking results…** — the best chunks are ordered by relevance
5. A result banner reports the savings: **RAG Mode reduced your input size by N% from X to Y tokens.**

If any stage fails, a red banner appears with the error. You can turn RAG Mode off and retry without it.

---

#### Constraints

> RAG with Rabbitholes managed models is temporarily unavailable in the desktop app — you'll see **Use a BYOK provider for RAG**. Select a model from one of your own providers (see [Models & Providers](https://www.slashspace.ai/docs/ai-features/models)).

> [File Nodes](https://www.slashspace.ai/docs/nodes/file-node) must finish processing before their content joins the RAG index. You can still chat with them immediately without RAG — only RAG Mode waits for processing.

> Deleting a node removes its embeddings from the index, and undoing the delete does not restore them. The content is re-indexed on your next RAG message.

---

#### Use cases

- **Chatting with a 300-page PDF**: connect the [File Node](https://www.slashspace.ai/docs/nodes/file-node), enable RAG Mode, and ask targeted questions — only the relevant pages are sent.
- **Research canvas with many sources**: a chat node connected to a dozen [Web Nodes](https://www.slashspace.ai/docs/nodes/web-node) and [YouTube Nodes](https://www.slashspace.ai/docs/nodes/youtube-node) stays well under the context limit.
- **Cutting token spend**: on BYOK providers, a 90% input reduction is a 90% reduction in input cost for that message.
- **Fitting oversized context**: when the token pill warns your input exceeds the model's window, RAG Mode is usually the fix.

### Slash Commands (Skills & Prompts)
*Type / in a chat to toggle tools, set reasoning effort, and insert your own reusable prompts and skills.*

**Source:** https://www.slashspace.ai/docs/ai-features/slash-commands

Typing `/` in a [Chat Node](https://www.slashspace.ai/docs/nodes/chat-node) input opens the slash menu — a quick keyboard-driven way to configure the conversation and pull in your reusable prompt library.

---

#### What's in the menu

The slash menu has three groups:

1. **MCP server quick-toggles** — enable or disable your configured [MCP servers](https://www.slashspace.ai/docs/ai-features/mcp-tools) for this conversation
2. **Reasoning presets** — **Reasoning: Low**, **Reasoning: Medium**, **Reasoning: High**, **Reasoning: Max**, for models that support extended thinking (see [Models & Providers](https://www.slashspace.ai/docs/ai-features/models))
3. **Skills & prompts** — your local library of reusable markdown prompts and agent skills

Keep typing after `/` to filter the list, then press **Enter** to select.

---

#### Where the library lives on disk

Your skills and prompts are plain files you own:

- **Prompts** — any `.md` file in `~/SlashspaceOS/.prompts`. Optional frontmatter `name:` and `description:` control how it appears in the menu; otherwise the filename is used.
- **Skills** — folders containing a `SKILL.md` file under `~/.agents/skills`. This is the cross-tool agent-skills convention, so skills you already use with tools like Claude Code appear here automatically.

---

#### Using a skill or prompt

1. Type `/` and select an entry from the skills & prompts group
2. A chip is inserted into your message — you can keep typing around it
3. On send, the file's full content is injected into the message for the model, wrapped in a Skill or Prompt tag

> A single referenced file over 120,000 characters errors on send. The total expanded message is capped at 400,000 characters.

> If the file behind a chip has been deleted or renamed, sending fails with **Missing slash command reference…** — remove the chip and re-add it from the menu.

---

#### Creating your own prompts

1. Create a markdown file in `~/SlashspaceOS/.prompts`, for example `summarize-meeting.md`:

   ```
   ---
   name: Summarize meeting
   description: Turn raw notes into decisions and action items
   ---

   Summarize the following meeting notes. List decisions made,
   open questions, and action items with owners.
   ```
2. Type `/` in any chat — the new prompt appears in the menu immediately, no restart needed

---

#### Use cases

- **Repeatable workflows**: a `/summarize-meeting` prompt you run on pasted notes every week, instead of retyping instructions.
- **Shared skills across tools**: the same `~/.agents/skills` folders power both this app and Claude Code, so one skill library serves your whole toolkit.
- **Fast conversation setup**: `/` → toggle an MCP server → `/` → **Reasoning: High**, all without leaving the keyboard.
- **Prompt libraries in version control**: keep `~/SlashspaceOS/.prompts` in a git repo and sync your best prompts across machines.

### Sub-Agents
*Let the AI delegate work by spawning child chat nodes that run tasks and report back.*

**Source:** https://www.slashspace.ai/docs/ai-features/sub-agents

Sub-agents let the AI split work up. When a task is big or naturally parallel, the model can spawn one or more child [Chat Nodes](https://www.slashspace.ai/docs/nodes/chat-node) on your canvas — each sub-agent runs its own conversation independently and reports its final answer back to the parent, which then continues with the results.

You don't need to enable anything: just ask. Prompts like "run three sub-agents to research these topics in parallel" or "delegate this comparison to sub-agents" trigger the behavior on models that support tool calling.

---

#### How it works

1. The parent AI calls its run-subagent tool with a short **label** and a self-contained **task** for each delegation — multiple calls in the same turn run in parallel
2. A new chat node appears on your canvas, connected to the parent, and starts working immediately
3. The sub-agent inherits the parent conversation as connected-node context, plus its task instructions
4. When it finishes, its final answer flows back into the parent's tool result and the parent resumes

The AI can also read your canvas structure through a canvas-context tool, so it can see what nodes already exist when deciding what to spawn. See [Core Concepts](https://www.slashspace.ai/docs/core-concepts) for how connected-node context works.

> Depth is capped at 1 level: a sub-agent is not offered the run-subagent tool itself, so sub-agents cannot spawn their own sub-agents and delegation can't recurse indefinitely.

---

#### Running sub-agents on different models

Each sub-agent can run on a different model than the parent chat. Just name the models in your prompt and the AI assigns one per sub-agent when it spawns them:

> "Debate whether we should rewrite the backend in Rust. Run three sub-agents to argue it — one on @grok-4, one on @gpt-5.5, one on @opus — then synthesize a verdict."

- **Loose references work** — "@opus", a bare model id, an exact provider-and-model pair, or the model's display name all resolve to the closest match.
- **Only your enabled models can be picked** — the AI is offered the models you've turned on in [Models](https://www.slashspace.ai/docs/ai-features/models), plus the built-in Basic / Pro / Advanced tiers. If it names a model that isn't available, that sub-agent fails immediately with the list of valid options, and the parent can correct itself or ask you.
- **Say nothing about models and behavior is unchanged** — every sub-agent inherits the parent chat's model.
- **The child node shows its model** — check the spawned node's model picker to confirm which model is answering.

---

#### What you see while it runs

Inside the parent's tool-call card, a live activity card tracks each sub-agent:

- A status line — **Starting subagent…**, then **Subagent is thinking…** or **Subagent is responding…**, prefixed with the child node's label
- **Running tool:** the tool the sub-agent is currently using, when it makes its own tool calls
- A streaming preview of the last stretch of the sub-agent's response text
- **Jump to node** — pans and zooms the canvas to the child node so you can watch it work
- **Cancel** — stops that sub-agent's run

---

#### After the run

The child node persists on your canvas. You can:

1. Open it and read the full conversation, including every tool call it made
2. Continue chatting in it directly — it's a normal chat node
3. Keep it connected as context, or delete it if it was throwaway work

Runs can also end as failed, cancelled, or timed out — the parent is told the outcome either way and explains what happened.

---

#### Use cases

- **Parallel research**: "Spawn a sub-agent for each of these three competitors and compare their pricing" — three nodes work simultaneously, the parent synthesizes.
- **Multi-model debates**: run the same question past several models — "have @grok-4, @gpt-5.5, and @opus each take a position" — and let the parent weigh their answers.
- **Long side-quests**: delegate a deep document analysis to a sub-agent while the parent conversation stays focused on the main thread.
- **Auditable delegation**: unlike hidden background steps, every sub-agent is a visible node — you can inspect exactly how it reached its answer.
- **Iterating on a delegation**: if a sub-agent's answer is close but not right, jump to its node and continue the conversation there instead of re-running everything.

### Voice Input
*Dictate into any chat or text input with the microphone button or Ctrl+M.*

**Source:** https://www.slashspace.ai/docs/ai-features/voice-input

Instead of typing, you can speak. Voice input records your microphone, transcribes the audio, and drops the text into the input — where you can edit it before sending.

---

#### Starting a recording

1. Click the microphone button in a chat or text input — it appears when the input is empty
2. Or press `Ctrl+M` from the input
3. macOS asks for microphone permission the first time — click **Allow**

A recording overlay appears with:

- A recording timer
- A live waveform of your voice
- **Cancel (Esc)** — discard the recording
- **Done (Enter)** — finish and transcribe

---

#### Finishing and editing

1. Press **Enter** or click **Done (Enter)** when you finish speaking
2. A **Transcribing…** state appears while the audio is converted to text
3. The transcribed text lands in the input — edit it like any typed text
4. Press **Enter** to send

---

#### Choosing a microphone

If you have multiple input devices:

1. Open **Settings → System Preferences**
2. Under **Audio Settings**, pick your preferred microphone

See [System Preferences](https://www.slashspace.ai/docs/settings/system-preferences) for the rest of that page.

> Transcription runs via Groq Whisper in the cloud, so voice input requires an internet connection. If a recording fails to transcribe, check your connectivity and see [Troubleshooting](https://www.slashspace.ai/docs/troubleshooting).

---

#### Use cases

- **Long prompts, fast**: dictate a multi-paragraph brief into a [Chat Node](https://www.slashspace.ai/docs/nodes/chat-node) in the time it would take to type the first sentence.
- **Thinking out loud**: ramble an idea into a [Text Node](https://www.slashspace.ai/docs/nodes/text-node), then ask a connected chat to structure it.
- **Hands-busy capture**: press `Ctrl+M` and describe what you're looking at — a whiteboard, a book page — without switching to the keyboard.
- **Accessibility**: a full alternative to typing for anyone who finds sustained keyboard input difficult.


---

## Settings

### Account Management
*Your plan, credits, devices, and privacy opt-ins in one place*

**Source:** https://www.slashspace.ai/docs/settings/account-management

#### Account Information

**Settings → Account** in the desktop app shows:

- Your **email address** and a truncated **Device ID**
- Your **current plan** — name, price, Active/Cancelling status, and renewal date
- Your **credit balance**, shown as a dollar value, with a **Reload** button
- A **Devices** list, with a link to manage devices on the web
- **Refresh account** and **Sign out** buttons
- A **Privacy Settings** section with opt-in toggles for individual features

There's no license key or license type anymore — sign-in is email-based (see [Quickstart](https://www.slashspace.ai/docs)).

---

#### Privacy Settings

Slashspace is opt-in about anything that leaves your machine: "Control how your data is used and shared. We respect your privacy and only enable features with your consent."

Each feature is listed with a description and an Enable/Disable toggle:

- **Cloud vector DB** — allows your node content to be indexed in the cloud vector database. This is what powers [RAG Mode](https://www.slashspace.ai/docs/ai-features/rag-mode) and AI Search; with it disabled, cloud indexing simply doesn't happen.
- **Analytics** — anonymous usage telemetry that helps improve the app.

> Both features stay off until you explicitly enable them. You can disable either at any time from the same toggles.

---

#### Managing Your Account

##### Device Management

1. In the app, go to **Settings → Account** and click **Manage devices on web** (or visit [slashspace.ai/account/plan](https://www.slashspace.ai/account/plan) directly)
2. View authorized devices
3. Remove unused devices

---

##### Payment Details & Invoices

1. Visit [slashspace.ai/account/plan](https://www.slashspace.ai/account/plan)
2. Navigate to Payment Details
3. Download invoices

---

#### Use cases

- **Ran out of credits mid-chat**: click **Reload** next to your credit balance (or fix it from the error itself — see [Troubleshooting](https://www.slashspace.ai/docs/troubleshooting)).
- **Just upgraded on the web**: hit **Refresh account** so the desktop app picks up your new plan without signing out.
- **New laptop**: remove the old machine from the Devices list on the web, then sign in on the new one.
- **Turning on RAG**: enable the cloud vector DB opt-in here before expecting [RAG Mode](https://www.slashspace.ai/docs/ai-features/rag-mode) or AI Search to index your nodes.

### Agent Providers
*Connect Cursor and Claude Code to run code-aware agent models on your workspace*

**Source:** https://www.slashspace.ai/docs/settings/agent-providers

#### Overview

**Settings → Agent Providers** lets you connect agent runtimes like Cursor and Claude Code to run code-aware models on your workspace. Unlike [cloud providers](https://www.slashspace.ai/docs/settings/providers), agent-provider models don't just answer — they can read and edit files in a folder you choose.

Each provider is a row in an accordion. The key icon turns green when the provider is connected (an API key is saved for Cursor; the switch is enabled for Claude Code).

> Agent providers require Pro or higher. On the free plan the page is locked with an **Upgrade** button.

---

#### Cursor

Cursor connects with an API key:

1. Expand **Cursor** and click **Get your API key here** — it opens the cursor.com dashboard where you can create a key.
2. Paste it into the **Enter your API key** field and save with the check button.
3. Use **Refresh Models** in the **Models** list to pull the current model list from Cursor.

---

#### Claude Code

Claude Code doesn't use an API key. As the setting explains: "Uses your locally installed Claude Code CLI and its subscription — no API key needed."

1. Expand **Claude Code** and turn on the master switch. Enabling it automatically fetches the model list from the CLI.
2. Check the **CLI Status** card. A green check with the CLI version and its path means you're ready. Click **Re-check** after installing or moving the CLI.

If the CLI isn't found, the card shows install steps:

1. Install the CLI: `npm install -g @anthropic-ai/claude-code`
2. Authenticate once by running `claude` in a terminal

##### Options

- **Custom CLI path** — only needed when the CLI isn't auto-detected (e.g. a non-standard install location). Leave it empty to auto-detect.
- **Permission mode** — how much the agent is allowed to do:
  - **Default** — tools that need permission are denied (chat-only, safest)
  - **Accept edits** — file edits in the workspace are auto-approved
  - **Plan** — read-only planning mode, no changes are made
  - **Bypass permissions** — all tools run without asking (use with care)
- **Max agent turns** — how many tool-use rounds Claude Code may take per response. Between 1 and 100; default 10.

The **Models** list has a **Refresh Models** button; if the CLI can't be reached, a default model set is loaded instead.

---

#### Agent Workspace

When you chat with an agent-provider model, a folder picker appears in the chat input. The folder you pick is the agent's workspace — the directory it reads from and (depending on permission mode) writes to.

You can also set a canvas-level default workspace in the canvas settings, so every agent chat on that canvas starts in the same folder.

---

#### Use cases

- **Ask questions about a codebase**: point the workspace at a repo and use **Plan** or **Default** mode to explore and explain code without any risk of changes.
- **Delegate real edits**: switch to **Accept edits** and have Claude Code fix a bug or add a feature directly in your project folder, right from a [chat node](https://www.slashspace.ai/docs/nodes/chat-node).
- **Use your existing subscriptions**: run Claude Code through the CLI's own subscription and Cursor through its API key — no extra Slashspace credits consumed for agent runs.
- **Keep long tasks bounded**: raise **Max agent turns** for complex multi-file refactors, or keep it low so quick questions never spiral into long tool loops.

### Custom Providers
*Add and manage your own OpenAI-compatible API providers*

**Source:** https://www.slashspace.ai/docs/settings/custom-providers

#### Overview

**Settings → Custom Providers** lets you add and manage your own OpenAI-compatible API providers. Any endpoint that speaks the OpenAI API format works — self-hosted inference servers, gateways, and proxy services.

> Custom providers require Pro or higher. On the free plan the page shows a lock with an **Upgrade** button.

---

#### Adding a Custom Provider

1. Go to **Settings → Custom Providers** and click **Add Custom Provider**.
2. Fill in the dialog:

   - **ID** — a unique identifier for the provider
   - **Name** — just a name for your reference
   - **API Key (Optional)** — leave empty if your endpoint doesn't need one
   - **Base URL** — the endpoint's OpenAI-compatible base URL
3. Click **Add Provider**.

---

#### Managing Custom Providers

Each provider is a row in an accordion showing its Base URL and ID when expanded:

- **Enable/disable** — the switch on the row activates or deactivates the provider without deleting it.
- **Edit** — reopens the dialog to change the name, API key, or base URL (the button reads **Update Provider** when editing).
- **Delete** — removes the provider after a confirmation.

> Deleting a provider cannot be undone — it is permanently removed from your settings along with its configuration.

##### Models

Custom providers start with no models. Expand the provider and click **Add Model**, then enter the **Model ID** exactly as your endpoint expects it, plus an optional display name, description, and modalities — the same dialog as for [cloud providers](https://www.slashspace.ai/docs/settings/providers#managing-models).

---

#### Use cases

- **Local inference servers**: connect LM Studio, vLLM, or a LiteLLM proxy running on your machine or LAN and use those models everywhere in Slashspace.
- **Corporate gateways**: route requests through your company's internal AI gateway so usage stays compliant with internal policy.
- **Aggregators and alternatives**: plug in any OpenRouter-style aggregator or niche hosted provider that exposes an OpenAI-compatible API.
- **Testing your own models**: point a provider at a fine-tuned model you're serving yourself and compare it against commercial models side by side on a canvas.

### Default Models
*Choose which models Slashspace uses for chat, titles, and images by default*

**Source:** https://www.slashspace.ai/docs/settings/default-models

#### Overview

**Settings → Default Models** configures which models the app reaches for automatically. You can pick any active model from any of your connected providers.

#### The Four Defaults

- **Default Chat Model** — the model every new [chat node](https://www.slashspace.ai/docs/nodes/chat-node) starts with. You can still switch models per conversation.
- **Title Generation Model** — used to automatically name your nodes and canvases from their content. The setting's own advice: "Pick a lightweight low cost model" — it runs often and doesn't need to be smart.
- **For Text to Image** — the default model for image generation in [image nodes](https://www.slashspace.ai/docs/nodes/image-node).
- **For Image to Image** — the default model for image editing "when you connect nodes", i.e. when an image node receives another image as input.

Only models whose modalities match are offered — the image dropdowns list image-capable models, and the image-to-image picker only shows models that can edit images.

---

#### Per-Canvas Overrides

These settings are global. Each canvas can override the default chat model in its canvas settings — while a canvas is inheriting the global value, it shows a **Global default** badge there. Set a canvas-specific model and that canvas stops following the global setting.

---

#### Use cases

- **Cheap housekeeping, smart chat**: put a frontier model on **Default Chat Model** but a small, cheap model on **Title Generation Model** so auto-naming never eats your budget.
- **A canvas per model**: keep the global default on your everyday model, and override one research canvas to a long-context model via its canvas settings.
- **Consistent image style**: pin your favorite image model as the text-to-image default so every new image node starts from the same generator.
- **Offline-first setup**: set an [Ollama](https://www.slashspace.ai/docs/settings/ollama) model as the default chat model so new conversations work even without internet.

### Connected Tools
*Connect third-party services to extend what your AI can do*

**Source:** https://www.slashspace.ai/docs/settings/integrations

> This feature is in **Beta** and lives under **Settings → Connected Tools** (shown as "Integrations" below for historical reasons — the in-app label is "Connected Tools").

#### Overview

Slashspace can connect to external services — Gmail, GitHub, Slack, Notion, Linear, Google Calendar, and more — through [Composio](https://composio.dev). Once connected, your AI can read, write, and take actions across those services directly from chat.

---

#### Privacy Boundary

The settings page states the boundary up front:

> Composio stores connected-account credentials on its backend. Slashspace never persists Composio API keys, OAuth secrets, MCP URLs, or MCP headers in your local canvas files. Tool schemas, tool calls, and tool results may be sent to the selected AI provider when tools are used.

In short: your service credentials live with Composio, never in your canvas files — but the content a tool returns can flow to whichever AI model you're chatting with.

---

#### Connecting a Service

You don't need to set anything up ahead of time. Just ask the AI to do something that involves an external service:

> "Create a GitHub issue for this bug"

If the service isn't connected yet, the AI will respond with a connection link. Click it, authorize the service, confirm back in chat, and the AI will carry on with your request.

![Connection link shown in chat](https://www.slashspace.ai/assets/docs/open-composio-link.png)

Any AI model that supports tool calls (all Rabbitholes models do this out of the box) can trigger this flow automatically.

If you haven't connected anything yet, the settings page shows an empty state: "Ask chat to use a tool such as Gmail, GitHub, Slack, or Notion. If authentication is needed, it will open a Composio Connect Link for that account."

---

#### What You Can Do

Once a service is connected, just ask naturally:

- "Summarize my unread emails from today"
- "Create a GitHub issue for this bug"
- "Send a Slack message to #engineering with today's standup notes"
- "Add this meeting to my Google Calendar"

The AI figures out which service to use and handles everything behind the scenes.

---

#### Managing Connections

Go to **Settings → Connected Tools** to see all your connected accounts. Each connection card shows the service name, the account ID, and a status pill:

- **ACTIVE** (green) — connected and ready to use
- **INITIATED** (amber) — authorization was started but not finished
- **FAILED / EXPIRED / REVOKED** (red) — the connection no longer works

Each card has two buttons:

1. **Reconnect** — opens a fresh Composio Connect Link in your browser to re-authorize the account. Use this for amber or red statuses.
2. **Disconnect** — removes the connection. The AI won't be able to use that account until you connect it again.

The **Refresh** button at the top of the page re-fetches the latest connection statuses.

You can also connect multiple accounts for the same service (e.g., work and personal Gmail). The AI will pick the right one based on context, or ask you which to use.

---

#### Available Services

There are 500+ services available, including:

| Category | Examples |
| --- | --- |
| Communication | Gmail, Slack, Discord, Microsoft Teams |
| Development | GitHub, GitLab, Linear, Jira |
| Productivity | Google Calendar, Notion, Todoist |
| Storage | Google Drive, Dropbox, OneDrive |
| CRM | HubSpot, Salesforce |
| Social | Twitter/X, LinkedIn |

---

#### Troubleshooting

- **Connection stopped working** — check its status pill in **Settings → Connected Tools**; if it's red, click **Reconnect**. OAuth tokens refresh automatically, but disconnecting and reconnecting fixes a stuck account.
- **Rate limits** — some services limit how many requests can be made in a short period. If you hit a limit, wait a few minutes and try again.

More help in [Troubleshooting & Support](https://www.slashspace.ai/docs/troubleshooting).

---

#### Use cases

- **Inbox triage on a canvas**: connect Gmail once, then ask chat each morning to summarize unread email and draft replies.
- **Ship bugs straight from research**: while investigating an issue in a [chat node](https://www.slashspace.ai/docs/nodes/chat-node), have the AI file the GitHub or Linear issue with full context.
- **Work and personal side by side**: connect both Gmail accounts and let the AI ask which one to use when it's ambiguous.
- **Meeting logistics**: ask the AI to find a free slot and add the event to Google Calendar without leaving your canvas.

### MCP Servers (Beta)
*Extend your AI with external tools via the Model Context Protocol*

**Source:** https://www.slashspace.ai/docs/settings/mcp-servers

#### Overview

**Settings → MCP Servers** (labeled **Beta** in the sidebar) lets you connect Model Context Protocol servers — external tool providers your AI can call during chat. An MCP server might expose your filesystem, a database, an issue tracker, or any other capability.

For how MCP tools actually behave in a conversation — tool approval, streaming results — see [MCP Tools](https://www.slashspace.ai/docs/ai-features/mcp-tools).

> MCP servers are experimental and may not work as expected. They give the AI access to external tools which can read, modify, or transmit your data. Your conversations, prompts, and any data processed through MCP tools will be shared with the server. Only use MCP servers from sources you trust completely, and be extra careful with servers that can reach sensitive information.

---

#### Adding an MCP Server

1. Go to **Settings → MCP Servers** and click **Add MCP Server**.
2. Fill in the dialog:

   - **Name** (required) — how the server appears in the list
   - **Description** (optional)
   - **Transport Type** — how Slashspace talks to the server:
     - **stdio (Local)** — runs a local command to start the server. Provide the **Command** (e.g. `npx -y @modelcontextprotocol/server-filesystem`) and **Arguments** as a comma-separated list (e.g. a path the server is allowed to access).
     - **HTTP (Remote)** — connects to a remote server. Provide the **URL**, and optionally **Headers (JSON)**, e.g. `{"Authorization": "Bearer your-api-key"}`.
     - **SSE (Server-Sent Events)** — like HTTP, with the same **URL** and **Headers** fields, for servers that stream over SSE.
   - **Enabled** — the switch at the bottom controls whether the server is active right away.
3. Click **Add Server** (or **Update Server** when editing).

---

#### Managing Servers

Each server is a row in an accordion:

- The plug icon is green when the server is enabled.
- A pill shows the transport type (`stdio`, `http`, or `sse`).
- The switch enables or disables the server without deleting it.
- **Edit** reopens the dialog with the server's settings.
- The trash button deletes the server after a confirmation — this cannot be undone and permanently removes the server configuration.

Expanding a row shows the description, the full transport command or URL, and the server's ID.

---

#### Use cases

- **Filesystem access**: run the filesystem MCP server over stdio so chat can read and summarize files in a folder you allow.
- **Internal tooling**: connect a remote HTTP MCP server your team hosts — with an `Authorization` header — to let the AI query internal systems.
- **Trying community servers**: enable a community MCP server for a one-off task, then flip its switch off so it can't be called until you need it again.
- **Separating trust levels**: keep powerful servers disabled by default and only enable the specific one a task needs, instead of leaving everything on.

### Ollama (Local Models)
*Run local models like Llama, Mistral, and Gemma on your own hardware*

**Source:** https://www.slashspace.ai/docs/settings/ollama

#### Overview

Ollama runs LLMs locally, using your computer's hardware instead of the cloud. It has its own page at **Settings → Ollama**.

You can chat with local models without an internet connection, and since nothing leaves your machine, it's more private than cloud providers. It's also free to use — Ollama is available on all plans, including Starter.

> You need a decent internet connection to download models, plus enough disk space to store them. Local model speed depends entirely on your hardware — a capable CPU/GPU and enough RAM make a big difference.

---

#### Setting Up Ollama

1. **Install and run Ollama.** If Ollama isn't detected, the page shows **Please Start / Install Ollama** with two buttons: **Configure** (point Slashspace at a non-default Ollama address) and **Install Ollama** (opens the download page at [ollama.com](https://ollama.com)). Install it, start it, and come back.
2. Once Ollama is running, the page shows an **Installed** badge with the Ollama version.
3. **Find a model ID.** Browse [ollama.com/search](https://ollama.com/search) for the model you want and copy its ID.

   [](/assets/docs/providers/ollama-model-ids.mp4)
4. **Download it.** Back in **Settings → Ollama**, paste the model ID (e.g. `gemma3:3b`) into the input (placeholder: "ex: mistral") and click **Download Model**. Progress streams in as the model downloads. Once it finishes, the model appears in the list and is available across Slashspace.

   ![Ollama Models](https://www.slashspace.ai/assets/docs/providers/ollama-setup.webp)

The **Search Models on Ollama** link below the list takes you straight to the model catalog.

---

#### Managing Models

- Models that are currently loaded show a green **Running** indicator and sort to the top of the list.
- Each model row has a **Delete** button to remove it and free up disk space.

---

#### Configuration

Click the gear button next to the Ollama badge to open the **Ollama Configuration** dialog. It has a single **Hostname** field — the URL of your Ollama instance, `http://localhost:11434` by default (a "use the default" shortcut fills it in). Click **Save Configuration** to apply.

Point this at another address if you run Ollama on a different port or on another machine on your network.

---

#### Troubleshooting

- Verify Ollama is running at `http://localhost:11434`
- Check your firewall settings
- Restart Ollama if needed

More help in [Troubleshooting & Support](https://www.slashspace.ai/docs/troubleshooting).

---

#### Use cases

- **Fully offline work**: download a model once, then chat, take notes, and build canvases on a plane or anywhere without internet.
- **Private material**: keep sensitive documents and conversations entirely on your machine — nothing is sent to any cloud provider.
- **Zero-cost experimentation**: try prompts, [personas](https://www.slashspace.ai/docs/ai-features/personas), and node workflows freely on the Starter plan without spending credits or API budget.
- **A home LLM server**: run Ollama on a beefy desktop and point your laptop's **Hostname** setting at it over the local network.

### Persona Prompts
*Create and manage reusable AI personas with their own instructions*

**Source:** https://www.slashspace.ai/docs/settings/persona-prompts

#### Overview

**Settings → Persona Prompts** is where you create and manage personas — named, color-coded instruction sets you can apply to any conversation. For how personas behave in chat, see [Personas](https://www.slashspace.ai/docs/ai-features/personas).

#### Create Persona

1. **Name:** Enter persona name
2. **Color:** Select identifying color
3. **Prompt:** Enter instructions
4. Click **Create** button

---

#### Managing Personas

- View existing personas
- Update by selecting and editing (the same dialog's submit button reads **Update** when editing)
- Delete when no longer needed

---

#### Using a Persona

Once created, a persona can be applied to a conversation from the persona picker (search personas by name) available in the chat/canvas UI — the AI will follow that persona's prompt for the conversation. See [Personas](https://www.slashspace.ai/docs/ai-features/personas) for details.

---

#### Use cases

- **A stable of specialists**: keep an "Editor", a "Skeptical Reviewer", and a "Explain-like-I'm-five Teacher" and switch between them per conversation instead of retyping instructions.
- **Consistent voice**: give a "Brand Writer" persona your tone guidelines so every draft across canvases sounds the same.
- **Color-coded thinking**: assign distinct colors to personas so you can tell at a glance which perspective produced which [chat node](https://www.slashspace.ai/docs/nodes/chat-node).

### Cloud Providers
*Connect Rabbitholes and your own API keys for OpenAI, Anthropic, Google, and more*

**Source:** https://www.slashspace.ai/docs/settings/providers

#### Overview

**Settings → Cloud Providers** is where you connect AI providers that run in the cloud. The page shows an accordion with one row per provider:

- **Rabbitholes** — Slashspace's built-in managed provider (no API key needed)
- **OpenAI**, **Anthropic**, **Google**, **Perplexity**, **xAI**, **OpenRouter**, **Straico**, **Qolaba**, **DeepSeek**, **Groq**, and **Fal AI (BETA)** — bring your own API key

The key icon on each row turns green once an API key is saved for that provider, so you can see at a glance which providers are connected.

Local models ([Ollama](https://www.slashspace.ai/docs/settings/ollama)), OpenAI-compatible endpoints ([Custom Providers](https://www.slashspace.ai/docs/settings/custom-providers)), and coding-agent CLIs ([Agent Providers](https://www.slashspace.ai/docs/settings/agent-providers)) each have their own settings page.

> On the free (Starter) plan, only Rabbitholes is available here. The other providers appear blurred behind a lock — "Cloud providers require Pro or higher. Upgrade to use your own API keys with OpenAI, Anthropic, Google, and more." — with an **Upgrade** button.

---

#### Rabbitholes (built-in)

Rabbitholes needs no setup at all. As its card explains: "Rabbitholes uses your signed-in desktop session and routes chat through the managed backend endpoint."

- There's no API key to paste — usage is billed against your credit balance.
- The **Manage plan** link on the card opens your plan page on the web, where you can check or reload credits.

> Custom models are not available for the Rabbitholes provider — you can only add your own models to BYOK providers.

---

#### Adding an API Key

1. Go to **Settings → Cloud Providers** and expand the provider you want to connect.
2. Click **Get your API key here** — it opens that provider's dashboard in your browser, where you can create a key.
3. Paste the key into the **Enter your API key** field. It's a password field; use the eye button to show or hide the key.
4. A footer appears with a **Skip API key validation** checkbox, a red **X** (cancel your changes), and a check button (save).
5. Click the check button to save. Slashspace validates the key with the provider before saving, unless you ticked **Skip API key validation**.

When you save a key for the first time, a default set of models for that provider is added automatically, and if you haven't set a default chat model yet, one is picked for you (you can change it in [Default Models](https://www.slashspace.ai/docs/settings/default-models)).

---

#### Managing Models

Each provider row has a **Models** list:

- **Toggle** — the switch on each model row activates or deactivates the model. Only active models show up in model pickers across the app.
- **Delete** — the trash button removes a model after a confirmation: "This will remove the model from the active list."
- **Add New Model** — opens a dialog to register any model the provider supports. For providers whose model inventory can be fetched, a combobox lets you pick from the live list; otherwise fill in:
  - **Model ID** (required) — the provider's exact model identifier, e.g. `gpt-4o`
  - **Display Name / Alias** (optional) — the name shown in the UI
  - **Description** (optional)
  - **Modalities** — checkboxes such as Text to Text, Text to Image, Image to Text; the model type is derived from what you select
- **Refresh Models** — shown instead of the add button for providers that fetch their model list (like [agent providers](https://www.slashspace.ai/docs/settings/agent-providers)).

Chat models are validated against the provider before they're added, so a typo in the model ID fails fast.

##### Per-model settings

Click a model card to open its **Model Settings** dialog. You can set an alias, a model-specific system prompt, and advanced sampling parameters: Temperature, Top K, Top P, Presence Penalty, Frequency Penalty, Max Tokens, and Max Steps.

##### Provider-level advanced settings

Each provider also has a **Manage Advanced Settings** button. This dialog sets defaults for the whole provider — System Prompt plus the same sampling parameters and Max Steps / Max Tokens. Every field has a **Clear** control, and the dialog has **Reset Defaults** and **Save** buttons.

---

#### Use cases

- **Start with zero setup**: chat with Rabbitholes models right after signing in — no keys, no configuration — and reload credits from the **Manage plan** link when you run low.
- **Bring your own keys to control cost**: on Pro, add your OpenAI and Anthropic keys so heavy usage bills your own accounts at provider rates instead of consuming credits.
- **Pin a new model the day it ships**: when a provider releases a model that isn't in the default list yet, use **Add New Model** with its model ID and start using it immediately.
- **Tune a provider for one workflow**: set a provider-level system prompt and a low temperature via **Manage Advanced Settings** so every model from that provider answers in a consistent, deterministic style.

### System Preferences
*App-level hardware preferences*

**Source:** https://www.slashspace.ai/docs/settings/system-preferences

#### Audio Settings

- **Preferred Microphone**: Select the primary input device used for voice transcription — see [Voice Input](https://www.slashspace.ai/docs/ai-features/voice-input).


---

## Troubleshooting

### Troubleshooting & Support
*Fixes for common errors, plus how to reach us when you're stuck*

**Source:** https://www.slashspace.ai/docs/troubleshooting

#### Common Chat Errors

##### "You don't have enough usage balance…"

Your Rabbitholes credit balance is empty. Click the **Reload usage** button shown with the error, or reload credits from your account page at [slashspace.ai/account](https://www.slashspace.ai/account). Your current balance is also visible in [Settings → Account](https://www.slashspace.ai/docs/settings/account-management).

##### "Upgrade your plan to use this feature."

You've hit a plan-gated feature. Bring-your-own-key [cloud providers](https://www.slashspace.ai/docs/settings/providers), [RAG Mode](https://www.slashspace.ai/docs/ai-features/rag-mode), [custom providers](https://www.slashspace.ai/docs/settings/custom-providers), and [agent providers](https://www.slashspace.ai/docs/settings/agent-providers) all require Pro or higher. Upgrade, then hit **Refresh account** in Settings → Account so the app picks up the new plan.

##### A generic red error under the message

1. Click **Retry** — transient provider hiccups are common.
2. If it persists, check the provider's API key in [Settings → Cloud Providers](https://www.slashspace.ai/docs/settings/providers) (the key icon should be green) and check the provider's own status page for outages.

##### Missing slash command reference

The [slash command](https://www.slashspace.ai/docs/ai-features/slash-commands) you invoked points to a prompt or skill file that has been moved or deleted. Restore the file, or edit the command to point at the new location.

##### RAG isn't available with Rabbitholes models

RAG with Rabbitholes managed models is temporarily unavailable — you'll see **Use a BYOK provider for RAG**. Switch the conversation to a model from one of your own providers (see [Models & Providers](https://www.slashspace.ai/docs/ai-features/models)).

---

#### Ollama Issues

- Verify Ollama is running at `http://localhost:11434` (or whatever hostname you configured in [Settings → Ollama](https://www.slashspace.ai/docs/settings/ollama))
- Check your firewall settings
- Restart Ollama if needed

---

#### Web Node Failures

If a [web node](https://www.slashspace.ai/docs/nodes/web-node) fails to load a page, the source is usually blocked, paywalled, or refusing automated access. Try a different URL for the same content — an archive link, the AMP version, or another article covering the same material.

---

#### Document Processing Stuck

If a [file node](https://www.slashspace.ai/docs/nodes/file-node) sits in processing or shows an error, click its **Retry** button. If it keeps failing, check that the file type is supported and that the file isn't corrupted or empty.

---

#### Sign-In Issues

- If your browser completes sign-in but the app never picks it up, use the **Paste login token** fallback on the sign-in screen: copy the token shown in the browser and paste it into the app.
- Make sure you sign in with the same email you purchased with — a different address won't carry your plan.

---

#### App Updates

1. Click the version button in the footer of the Settings sidebar. It opens the **Software Update** dialog.
2. Click **Download Update** and wait for the progress to finish.
3. Click **Restart & Install** to apply the update.

---

#### Getting Help

- **In-app**: use **Bug / Feedback** (under **Settings → Troubleshoot**, or right-click the canvas). Describe the issue and optionally attach screenshots or screen recordings — your log file and device ID are attached automatically to help us diagnose.
- **Email**: [support@rabbitholes.ai](mailto:support@rabbitholes.ai)
- **Discord**: join the community at [links.rabbitholes.ai/discord](https://links.rabbitholes.ai/discord) for faster responses
