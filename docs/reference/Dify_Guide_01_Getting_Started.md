# Dify Documentation — Getting Started & Tutorials

*This document was scraped from the official Dify documentation and cleaned/reformatted for ingestion into NotebookLM (for building a learning plan). It is part of a multi-file set covering the full Dify docs guide.*

- **Source:** https://docs.dify.ai/en/home
- **Total pages in this file:** 17
- **Date scraped:** 2026-07-18

## Table of Contents

- **[Getting Started](#getting-started)**
  - [Key Concepts](#key-concepts)
    - [Key Concepts](#key-concepts-1)
  - [Tutorials](#tutorials)
    - [Article Reader Using File Upload](#article-reader-using-file-upload)
    - [AI Image Generation App](#ai-image-generation-app)
    - [Customer Service Bot With Knowledge Base](#customer-service-bot-with-knowledge-base)
    - [Simple Chatbot](#simple-chatbot)
    - [Twitter Account Analyzer](#twitter-account-analyzer)
    - [Lesson 1: What is a Workflow?](#lesson-1-what-is-a-workflow)
    - [Lesson 2: Head and Tail (Start & Output Node)](#lesson-2-head-and-tail-start-output-node)
    - [Lesson 3: The Brain of the Workflow (LLM Node)](#lesson-3-the-brain-of-the-workflow-llm-node)
    - [Lesson 4: The Cheat Sheet (Knowledge Retrieval)](#lesson-4-the-cheat-sheet-knowledge-retrieval)
    - [Lesson 5: The Crossroads of Your Workflow (Sorting and Executing)](#lesson-5-the-crossroads-of-your-workflow-sorting-and-executing)
    - [Lesson 6: Handle Multiple Tasks (Parameter Extraction & Iteration)](#lesson-6-handle-multiple-tasks-parameter-extraction-iteration)
    - [Lesson 7: Enhance Workflows (Tools)](#lesson-7-enhance-workflows-tools)
    - [Lesson 8: The Agent Node](#lesson-8-the-agent-node)
    - [Lesson 9: Layout Designer (Template)](#lesson-9-layout-designer-template)
    - [Lesson 10: Publish and Monitor Your AI App](#lesson-10-publish-and-monitor-your-ai-app)
  - [Introduction](#introduction)
    - [30-Minute Quick Start](#30-minute-quick-start)

---

## Getting Started

### Key Concepts

#### Key Concepts

*Quick overview of essential Dify concepts*

**Source:** https://docs.dify.ai/en/learn/key-concepts

Quick overview of essential Dify concepts

##### Dify App

Dify is made for agentic app building. In **Studio**, you can quickly build agentic workflows via a drag & drop interface and publish them as apps. You can access published apps via API, the web, or as an [MCP server](https://docs.dify.ai/en/cloud/use-dify/publish/publish-mcp). Dify offers two main app types: Workflow and Chatflow. You will need to choose an app type when creating a new app.

> **ℹ️ Info:**
>   We recommend choosing Workflow or Chatflow your app type. But in addition to these, Dify also offers 3 more basic app types: Chatbot, Agent, and Text Generator.
>
>
>     *[Image: App Type Selector]*
>
>
>   These app types run on the same workflow engine underneath, but comes with simpler legacy interfaces:
>
>
>     *[Image: Chatbot Interface]*
>

##### Workflow

Build Workflow apps to handle single-turn tasks. The webapp interface and API provides easy access to batch execute many tasks at once.

> **ℹ️ Info:**
>   Underneath it all, workflow forms the basis for all other app types in Dify.

Every workflow begins with a [start node](https://docs.dify.ai/en/cloud/use-dify/nodes/start): either User Input (on-demand, triggered by a user or API call) or a Trigger (automatic, on a schedule or in response to external events).

##### Chatflow

Chatflow is a special type of workflow app that gets triggered at every turn of a conversation. Other than workflow features, Chatflow comes with the ability to store and update custom conversation-specific variables, enable memory in LLM nodes, and stream formatted text, images, and files at different points throughout the Chatflow run.

Chatflows always start with User Input.

##### Dify DSL

All Dify apps can be exported into a YAML file in Dify's own DSL (Domain-Specific Language) and you may create Dify apps from these DSL files directly. This makes it easy to port apps to other Dify instances and share with others.

##### Variables

A variable is a labeled container to store information, so you can find and use that information later by referencing its name. You'll come across different types of variables when building a Dify app:

**Inputs**: You can specify any number of input variables at the [User Input](https://docs.dify.ai/en/cloud/use-dify/nodes/user-input) node for your app's end users to fill in.

  *[Image: User Input Node Variables]*

Additionally, the User Input node comes with a set of input variables that you can reference later in the flow. Depending on the app type (Workflow or Chatflow), different variables are provided.

  **Workflow:**

    | Variable Name         | Data Type | Description                                                                                                                                                      | Notes                                                                                                                                          |
    | :-------------------- | :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
    | `sys.user_id`         | String               | User ID: A unique identifier automatically assigned by the system to each user when they use a Workflow application. It is used to distinguish different users.  |                                                                                                                                                |
    | `sys.app_id`          | String               | App ID: A unique identifier automatically assigned by the system to each App. This parameter is used to record the basic information of the current application. | This parameter is used to differentiate and locate distinct Workflow applications for users with development capabilities.                     |
    | `sys.workflow_id`     | String               | Workflow ID: This parameter records information about all nodes information in the current Workflow application.                                                 | This parameter can be used by users with development capabilities to track and record information about the nodes contained within a workflow. |
    | `sys.workflow_run_id` | String               | Workflow Run ID: Used to record the runtime status and execution logs of a Workflow application.                                                                 | This parameter can be used by users with development capabilities to track the application's historical execution records.                     |
    | `sys.timestamp`       | Number               | The start time of each workflow execution.                                                                                                                       |                                                                                                                                                |

  **Chatflow:**

    | Variable Name         | Data Type | Description                                                                                                                                                                                                                                                                                                                                                           | Notes                                                                                                                                                                              |
    | :-------------------- | :------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `sys.conversation_id` | String               | A unique ID for the chatting box interaction session, grouping all related messages into the same conversation, ensuring that the LLM continues the chatting on the same topic and context.                                                                                                                                                                           |                                                                                                                                                                                    |
    | `sys.dialogue_count`  | Number               | The number of conversations turns during the user's interaction with a Chatflow application. The count automatically increases by one after each chat round and can be combined with if-else nodes to create rich branching logic.

For example, LLM will review the conversation history at the X conversation turn and automatically provide an analysis. |                                                                                                                                                                                    |
    | `sys.user_id`         | String               | A unique ID is assigned for each application user to distinguish different conversation users.                                                                                                                                                                                                                                                                        | The Service API does not share conversations created by the WebApp. This means users with the same ID will have separate conversation histories between API and WebApp interfaces. |
    | `sys.app_id`          | String               | App ID: A unique identifier automatically assigned by the system to each App. This parameter is used to record the basic information of the current application.                                                                                                                                                                                                      | This parameter is used to differentiate and locate distinct applications for users with development capabilities.                                                                  |
    | `sys.workflow_id`     | String               | Workflow ID: This parameter records information about all nodes information in the current application.                                                                                                                                                                                                                                                               | This parameter can be used by users with development capabilities to track and record information about the nodes contained within a workflow.                                     |
    | `sys.workflow_run_id` | String               | Workflow Run ID: Used to record the runtime status and execution logs of an application.                                                                                                                                                                                                                                                                              | This parameter can be used by users with development capabilities to track the application's historical execution records.                                                         |

User inputs are set at the start of each workflow run and cannot be updated.

**Outputs**: Each node produces one or more outputs that can be referenced in subsequent nodes. For instance, the LLM node has outputs:

  *[Image: LLM Node Output Variables]*

Like inputs, node outputs cannot be updated either.

**Environment Variables**: Use environment variable to store sensitive information like API keys specific to your app. This allows a clean separation between secrets and the Dify app itself, so you don't have to risk exposing passwords and keys when sharing your app's DSL. Environment variables are also constants and cannot be updated.

**Conversation Variables (Chatflow only)**: These variables are conversation-specific -- meaning they persist over multi-turn Chatflow runs in a single conversation so you can store and access dynamic information like to-do list and token cost. You can update the value of a conversation variable via the Variable Assigner node:

  *[Image: Conversation Variables Panel]*

##### Variable Referencing

You can easily pass variables to any node when configuring its input field by selecting from a dropdown:

  *[Image: Variable Picker Dropdown]*

You can also insert variable values into complex text inputs by typing `/` slash, and selecting the desired variable from the dropdown.

  *[Image: Variable Slash Insert]*

### Tutorials

#### Article Reader Using File Upload

**Source:** https://docs.dify.ai/en/learn/tutorials/article-reader

In Dify, you can use the knowledge base to allow agent to obtain accurate information from a large amount of text content. However, in many cases, the local files provided are not large enough to warrant the use of the knowledge base. In such cases, you can use the file upload feature to directly provide local files as context for the LLM to read.

In this experiment, we will build the article reader as a case study. This assistant will ask questions based on the uploaded document, helping users to read papers and other materials with those questions in mind.

#### You Will Learn

* File upload usage
* Basic usage of Chatflow
* Prompt writing skill
* Iteration node usage
* Doc extractor and list operator usage

#### **Prerequisites**

Create a Chatflow in Dify. Make sure you have added a model provider and have sufficient quota.

#### **Add Nodes**

In this experiment, at least four types of nodes are required: start node, document extractor node, LLM node, and answer node.

##### **Start Node**

In the start node, you need to add a file variable. File upload is supported in v0.10.0 Dify, allowing you to add files as variable.

In the start node, you need to add a file variable and check the document in the supported file types.

Some readers might notice the `sys.files` in the system variables, which are files or file lists uploaded by users in the dialog box.

The difference between creating your own file variables is that this feature requires enabling file upload in the functions and setting the upload file types, and each time a new file is uploaded in the dialog, this variable will be overwritten.

Please choose the appropriate file upload method according to your business scenario.

##### **Doc Extractor**

**LLM cannot read files directly.** This is a common misconception among many users when they first use file upload, as they might think simply using the file as a variable in an LLM node would work. However, in reality, the LLM reads nothing from file variables.

Thus, Dify introduced the **doc extractor** node, which can extract text from the file variable and output it as a text variable.

The **doc extractor** node takes the file variable from the **start** node as input and converts document files into text output.

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/bc4b1492bd10ef782457ec6a709997f9.png)

##### **LLM**

In this experiment, two LLM nodes need to be designed: structure extraction and question generation.

###### **Structure Extraction**

The structure extraction node can extract the structure of the original text, summarizing key content.

The prompts are as follow:

```
Read the following article content and perform the task
{{Result variable of the document extractor}}
# Task

- **Main Objective**: Thoroughly analyze the structure of the article.
- **Objective**: Detail the content of each part of the article.
- **Requirements**: Analyze as detailed as possible.
- **Restrictions**: No specific format restrictions, but the analysis must be organized and logical.
- **Expected Output**: A detailed analysis of the article structure, including the main content and role of each part.

# Reasoning Order

- **Reasoning Part**: By carefully reading the article, identify and analyze its structure.
- **Conclusion Part**: Provide specific content and role for each part.

# Output Format

- **Analysis Format**: Each part should be listed in a headline format, followed by a detailed explanation of that part's content.
- **Structure Form**: Markdown, to enhance readability.
- **Specific Description**: The content and role of each part, including but not limited to the introduction, body, conclusion, citations, etc.
```

###### **Question Generation**

The question generation node can summarize the issues of the article from the content summarized by the structure extraction node, assisting the reader in thinking through the questions during the reading process.

The prompts are as follow:

```
Read the following article content and perform the task
{{Output of the structure extraction}}
# Task

- **Main Objective**: Thoroughly read the above text, and propose as many questions as possible for each part of the article.
- **Requirements**: Questions should be meaningful and valuable, worthy of consideration.
- **Restrictions**: No specific restrictions.
- **Expected Output**: A series of questions for each part of the article, each question should have depth and thinking value.

# Reasoning Order

- **Reasoning Part**: Thoroughly read the article, analyze the content of each part, and consider the deep questions each part may raise.
- **Conclusion Part**: Pose meaningful and valuable questions, ensuring they provoke in-depth thought.

# Output Format

- **Format**: Each question should be listed separately, numbered.
- **Content**: Propose questions for each part of the article (such as introduction, background, methods, results, discussion, conclusion, etc.).
- **Quantity**: As many as possible, but each question should be meaningful and valuable.
```

#### **Question 1: Handling Multiple Uploaded Files**

To handle multiple uploaded files, an iterative node is needed.

The iterative node is similar to the while loop in many programming languages, except that Dify has no conditional restrictions, and the **input variable can only be of type `array` (list)**. The reason is that Dify will execute all the content in the list until it is done.

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/cc9cbf8b718b8abbf84cd8649a08c1a3.png)

Therefore, you need to adjust the file variable in the start node to an `array` type, i.e., a file list.

  ![Therefore, You Need to Adjust the File Variable in the Start Node to an Array](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/8eff802e3e1e3da466c5dc9ac56c50f2.png)

#### **Question 2: Handling Specific Files from a File List**

In Question 1, some readers might notice that Dify will process all files before ending the loop, while in some cases, only a part of the files need to be operated on, not all. For this issue, you can process the file list in Dify using the **list operation** node. List operations can operate on all array-type variables, not just file lists.

For example, limit the analysis to only document-type files and sort the files to be processed in order of file names.

Before the iterative node, add a list operation, adjust the **filter condiftion** and **order by**, then change the input of the iterative node to the output of the list operation node.

  ![Before the Iterative Node, Add a List Operation, Adjust the Filter Condiftion](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/287690e1fef87af270c0d5020d25d6cf.png)

#### AI Image Generation App

**Source:** https://docs.dify.ai/en/learn/tutorials/build-ai-image-generation-app

With the rise of image generation, many excellent image generation products have emerged, such as Dall-e, Flux, Stable Diffusion, etc.

In this article, you will learn how to develop an AI image generation app using Dify.

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/05ff829cf382e82c9ece2676032d2383.png)

#### You Will Learn

* Methods for building an Agent using Dify
* Basic concepts of Agent
* Fundamentals of prompt engineering
* Tool usage
* Concepts of large model hallucinations

#### 1. Set Stability API Key

[Click here](https://platform.stability.ai/account/keys) to go to the Stability API key management page.

If you haven't registered yet, you will be asked to register before entering the API management page.

After entering the management page, click `copy` to copy the key.

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/f73d82756bdf93c8863ac0b1f55fa5af.png)

Next, fill in the key under **Tools** > **Stability** in your Dify instance by following these steps:

* Log in to Dify
* Enter Tools
* Select Stability
* Click `Authorize`

  ![Authorize](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/bcc961ffc8a341c8ba3137e475072f99.png)

* Fill in the key and save

#### 2. Configure Model Providers

To optimize interaction, we need an LLM to concretize user instructions, i.e., to write prompts for generating images. Next, we will configure model providers in Dify following these steps.

Add a model provider by following the steps in the image below:

Go to **Integrations** > **Model Provider**

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/4b4102f9027e2bda3fc520eaa8ea2354.png)

If you haven't found a suitable model provider, the groq platform provides free call credits for LLMs like Llama.

Log in to [groq API Management Page](https://console.groq.com/keys)

Click **Create API Key**, set a desired name, and copy the API Key.

Back to **Dify - Model Providers**, select **groqcloud**, and click **Setup**.

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/0fda6e81dc23974576ddc21bda96e26d.png)

Paste the API Key and save.

  ![Paste the API Key and Save](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/b250952afad12b39613aa27da5335fa3.png)

#### 3. Build an Agent

Back to **Dify - Studio**, select **Create from Blank**.

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/3b86940eadfe0ce14d175a9bb80fe5a9.png)

In this experiment, we only need to understand the basic usage of Agent.

> **ℹ️ Info:**
>   **What is an Agent**
>
>   An Agent is an AI system that simulates human behavior and capabilities. It interacts with the environment through natural language processing, understands input information, and generates corresponding outputs. The Agent also has "perception" capabilities, can process and analyze various forms of data, and can call and use various external tools and APIs to complete tasks, extending its functional scope. This design allows the Agent to handle complex situations more flexibly and simulate human thinking and behavior patterns to some extent.

Select **Agent**, fill in the name.

  ![Agent, Fill in the Name](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/139ac0d2f4a10e2ec0e191457f4687a1.png)

Next, you will enter the Agent orchestration interface as shown below.

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/9045dbab8600e9c9d9632add787f26a6.png)

Select the LLM. Here we use Llama-3.1-70B provided by groq as an example:

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/47edc14c1d3c68eeb4ee4807b35df185.png)

Select Stability in **Tools**:

  ![Stability in Tools](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/6e1c3dd63925fd9ba60568deb2602044.png)

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/539060be4e014126f9c5fc96c53dc5a4.png)

##### Write Prompts

Prompts are the soul of the Agent and directly affect the output effect. Generally, the more specific the prompts, the better the output, but overly lengthy prompts can also lead to negative effects.

The engineering of adjusting prompts is called Prompt Engineering.

In this experiment, you don't need to worry about not mastering Prompt Engineering; we will learn it step by step later.

Let's start with the simplest prompts:

```
Draw the specified content according to the user's prompt using stability_text2image.
```

Each time the user inputs a command, the Agent will know this system-level instruction, thus understanding that when executing a user's drawing task, it needs to call stability tool.

For example: Draw a girl holding an open book.

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/05ff829cf382e82c9ece2676032d2383.png)

##### Don't want to write prompts? Of course you can!

Click **Generate** in the upper right corner of Instructions.

  ![Generate in the Upper Right Corner of Instructions](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/426a416e468b9f495eb13ac2986acdca.png)

Enter your requirements in the **Instructions** and click **Generate**. The generated prompts on the right will show AI-generated prompts.

  ![Your Requirements in the Instructions and Click Generate](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/d750983264182e7af5014d5df4477e31.png)

However, to develop a good understanding of prompts, we should not rely on this feature in the early stages.

#### Publish

Click the publish button in the upper right corner, and after publishing, select **Run App** to get a web page for an online running Agent.

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/38a1bf752ca1fc71eccbbfd18046f5bc.png)

Copy the URL of this web page to share with other friends.

#### Question 1: How to Specify the Style of Generated Images?

We can add style instructions in the user's input command, for example: Anime style, draw a girl holding an open book.

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/d2d883d887272786ee19d97894cbb307.png)

But if we want set the default style to anime style, we can add it to the system prompt because we previously learned that the system prompt is known each time the user command is executed and has a higher priority.

```
Draw the specified content according to the user's prompt using stability_text2image, the picture is in anime style.
```

#### Question 2: How to Reject Certain Requests from Some Users?

In many business scenarios, we need to avoid outputting some unreasonable content, but LLMs are often "dumb" and will follow user instructions without question, even if the output content is wrong. This phenomenon of the model trying hard to answer users by fabricating false content is called **model hallucinations**. Therefore, we need the model to refuse user requests when necessary.

Additionally, users may also ask some content unrelated to the business, and we also need the Agent to refuse such requests.

We can use markdown format to categorize different prompts, writing the prompts that teach the Agent to refuse unreasonable content under the "Constraints" title. Of course, this format is just for standardization, and you can have your own format.

```
## Task
Draw the specified content according to the user's prompt using stability_text2image, the picture is in anime style.

## Constraints
If the user requests content unrelated to drawing, reply: "Sorry, I don't understand what you're saying."
```

For example, let's ask: What's for dinner tonight?

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/06dcf569989d797919fbe49ab8d5cadc.png)

In some more formal business scenarios, we can call a sensitive word library to refuse user requests.

Add the keyword "dinner" in **Add Feature - Content Moderation**. When the user inputs the keyword, the Agent app outputs "Sorry, I don't understand what you're saying."

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/828b27d1a873ff7b4b44f76d93229225.png)

#### Customer Service Bot With Knowledge Base

*Build a Chatflow that answers customer questions from a knowledge base*

**Source:** https://docs.dify.ai/en/learn/tutorials/customer-service-bot

Build a Chatflow that answers customer questions from a knowledge base

In the last experiment, we learned the basic usage of file uploads. However, when the text we need to read exceeds the LLM's context window, we need to use a knowledge base.

> **ℹ️ Info:**
>   **What is context?**
>
>   The context window refers to the range of text that the LLM can "see" and "remember" when processing text. It determines how much previous text information the model can refer to when generating responses or continuing text. The larger the window, the more contextual information the model can utilize, and the generated content is usually more accurate and coherent.

Previously, we learned about the concept of LLM hallucinations. In many cases, an LLM knowledge base allows the Agent to locate accurate information, thus accurately answering questions. It has applications in specific fields such as customer service and search tools.

Traditional customer service bots are often based on keyword retrieval. When users input questions outside of the keywords, the bot cannot solve the problem. The knowledge base is designed to solve this problem, enabling semantic-level retrieval and reducing the burden on human agents.

Before starting the experiment, remember that the core of the knowledge base is retrieval, not the LLM. The LLM enhances the output process, but the real need is still to generate answers.

##### What You Will Learn in This Experiment

* Basic usage of Chatflow
* Usage of knowledge bases and external knowledge bases
* The concept of embeddings

##### Prerequisites

###### Create an Application

In Dify, select **Create from Blank** > **Chatflow**.

  ![Create from Blank Chatflow](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/0147e0d6fa1412dcf38ff0b12d30e5fe.png)

###### Add a Model Provider

This experiment involves using embedding models. Currently, supported embedding model providers include OpenAI and Cohere. In Dify's model providers, those with the `TEXT EMBEDDING` label are supported. Ensure you have added at least one and have sufficient balance.

  ![Add an Embedding Model Provider](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/ebfb40e8b80adb8d7e1096ee5da16fad.png)

> **ℹ️ Info:**
>   **What is embedding?**
>
>   "Embedding" is a technique that converts discrete variables (such as words, sentences, or entire documents) into continuous vector representations.
>
>   Simply put, when we process natural language into data, we convert text into vectors. This process is called embedding. Vectors of semantically similar texts will be close together, while vectors of semantically opposite texts will be far apart. LLMs use this data for training, predicting subsequent vectors, and thus generating text.

##### Create a Knowledge Base

Go to **Knowledge** > **Create Knowledge**.

Dify supports three data sources: documents, Notion, and web pages.

For local text files, note the file type and size limitations; syncing Notion content requires binding a Notion account; syncing a website requires using the **Jina** or **Firecrawl API**.

We will start with uploading a local document as an example.

###### Chunk Settings

After uploading the document, you will enter the following page:

  ![Uploading the Document, You Will Enter the Following Page](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/0dab2d0a607d9486ae973d897b0c08bd.png)

You can see a segmentation preview on the right. The default selection is automatic segmentation and cleaning. Dify will automatically divide the article into many paragraphs based on the content. You can also set other segmentation rules in the custom settings.

###### Index Method

Normally we prefer to select **High Quality**, but this will consume extra tokens. Selecting **Economical** will not consume any tokens.

###### Embedding Model

Please refer to the model provider's documentation and pricing information before use.

Different embedding models are suitable for different scenarios. For example, Cohere's `embed-english` is suitable for English documents, and `embed-multilingual` is suitable for multilingual documents.

###### Retrieval Settings

Dify provides three retrieval functions: vector retrieval, full-text retrieval, and hybrid retrieval. Hybrid retrieval is the most commonly used.

In hybrid retrieval, you can set weights or use a reranking model. When setting weights, you can set whether the retrieval should focus more on semantics or keywords. For example, in the image below, semantics account for 70% of the weight, and keywords account for 30%.

  ![In Hybrid Retrieval, You Can Set Weights or Use a Reranking Model](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/6a1f2b4a6e1b63febdaee3e01c1d39a4.png)

Clicking **Save and Process** will process the document. After processing, the document can be used in the application.

  ![Save and Process Will Process the Document](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/fdc20eb804ec39a308726324f6b33f45.png)

###### Sync from a Website

In many cases, we need to build a smart customer service bot based on help documentation. Taking Dify as an example, we can convert the [Dify help documentation](https://docs.dify.ai) into a knowledge base.

Currently, Dify supports processing up to 50 pages. Please pay attention to the quantity limit. If exceeded, you can create a new knowledge base.

  ![Sync from a Website](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/8936a4f7952c7aefe5f9d58ee730883c.png)

###### Adjust Knowledge Base Content

After the knowledge base has processed all documents, it is best to check the coherence of the segmentation in the knowledge base. Incoherence will affect the retrieval effect and needs to be manually adjusted.

Click on the document content to browse the segmented content. If there is irrelevant content, you can disable or delete it.

If content is segmented into another paragraph, it also needs to be adjusted back.

###### Recall Test

In the document page of the knowledge base, click **Retrieval Testing** in the left sidebar to input keywords to test the accuracy of the retrieval results.

##### Add Nodes

Enter the created app, and let's start building the smart customer service bot.

###### Question Classification Node

You need to use a Question Classifier node to separate different user needs. In some cases, users may even chat about irrelevant topics, so you need to set a classification for this as well.

To make the classification more accurate, you need to choose a better LLM, and the classification needs to be specific enough with sufficient distinction.

Here is a reference classification:

* User asks irrelevant questions
* User asks Dify-related questions
* User requests explanation of technical terms
* User asks about joining the community

  ![Question Classifier Node Configuration](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/627566df2b28b58ab84e53d3737c6927.png)

###### Direct Reply Node

In the question classification, "User asks irrelevant questions" and "User asks about joining the community" do not need LLM processing to reply. Therefore, you can directly connect an Answer node after these two questions.

For "User asks irrelevant questions", you can guide the user to the help documentation, allowing them to try to solve the problem themselves, for example:

```text theme={null}
I'm sorry, I can't answer your question. If you need more help, please check the [help documentation](https://docs.dify.ai).
```

Dify supports Markdown formatted text output. You can use Markdown to enrich the text format in the output. You can even insert images in the text using Markdown.

###### Knowledge Retrieval Node

Add a Knowledge Retrieval node after "User asks Dify-related questions" and check the knowledge base to be used.

###### LLM Node

In the next node after the Knowledge Retrieval node, you need to select an LLM node to organize the content retrieved from the knowledge base.

The LLM needs to adjust the reply based on the user's question to make the reply more appropriate.

Context: You need to use the output of the Knowledge Retrieval node as the context of the LLM node.

System prompt: Based on `{{context}}`, answer `{{user question}}`.

  ![LLM Node System Prompt](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/0052ebf236d55dc0c143c5dbfe5f1e76.png)

You can use `/` or `{` to reference variables in the prompt writing area. Variables starting with `sys.` are system variables.

In addition, you can enable LLM memory to make the user's conversation experience more coherent.

##### Question 1: How to Connect External Knowledge Bases

In the knowledge base function, you can connect external knowledge bases through external knowledge base APIs, such as the AWS Bedrock knowledge base.

  ![Connect External Knowledge Bases via External Knowledge API](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/7bcfb95e806966a868885814f0d7dc35.png)

##### Question 2: How to Manage Knowledge Bases Through APIs

You can add, delete, and query the status of knowledge bases through the knowledge base API.

  ![Manage Knowledge Bases via the API](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/cda4458ccb9be9e1c3ec9821fb5c5f99.png)

In the knowledge base detail page, go to **API Access** and create an API key. Please keep the API key safe.

##### Question 3: How to Embed the Customer Service Bot into a Webpage

After application deployment, select **Embed Into Site**, choose a suitable embedding method, and paste the code into the appropriate location on the webpage.

#### Simple Chatbot

*Hello World*

**Source:** https://docs.dify.ai/en/learn/tutorials/simple-chatbot

Hello World

The real value of Dify lies in how easily you can build, deploy, and scale an idea no matter how complex. It's built for fast prototyping, smooth iteration, and reliable deployment at any level.

Let's start by learning reliable LLM integration into your applications. In this guide, you'll build a simple chatbot that classifies the user's question, respond directly using the LLM, and enhance the response with a country-specific fun fact.

*[Embedded: Dify Quick Start Video]*

#### Step 1: Create a New Workflow (2 min)

1. Go to **Studio** > **Workflow** > **Create from Blank** > **Orchestrate** > **New Chatflow** > **Create**

#### Step 2: Add Workflow Nodes (6 min)

> **💡 Tip:**
>   When you want to reference any variable, type `{` or `/` first and you can see the different variables available in your workflow.

##### 1. LLM Node and Output: Understand and Answer the Question

> **ℹ️ Info:**
>   `LLM` node sends a prompt to a language model to generate a response based on user input. It abstracts away the complexity of API calls, rate limits, and infrastructure, so you can just focus on designing logic.

  1. **Create LLM Node**
        Create an LLM node using the `Add Node` button and connect it to your Start node

  1. **Configure Model**
        Choose a default model

  1. **Set System Prompt**
        Paste this into the System Prompt field:

        ```text theme={null}
        The user will ask a question about a country. The question is {{sys.query}}
        Tasks:
        1. Identify the country mentioned.
        2. Rephrase the question clearly.
        3. Answer the question using general knowledge.

        Respond in the following JSON format:
        {
          "country": "<country name>",
          "question": "<rephrased question>",
          "answer": "<direct answer to the question>"
        }
        ```

  1. **Enable Structured Output**
        **Enable Structured Output** allows you to easily control what the LLM will return and ensure consistent, machine-readable outputs for downstream use in precise data extraction or conditional logic.

        * Toggle Output Variables Structured ON > `Configure` and click `Import from JSON`
        * Paste:

        ```json theme={null}
        {
          "country": "string",
          "question": "string",
          "answer": "string"
        }
        ```

##### 2. Code Block: Get Fun Fact

> **ℹ️ Info:**
>   `Code` node executes custom logic using code. It lets you inject code exactly where needed—within a visual workflow—saving you from wiring up an entire backend.

  1. **Create Code Node**
        Create a `Code` Node using the `Add Node` button and connect to LLM block

  1. **Configure Input Variable**
        Change one `Input Variable` name to "country" and set the variable to `structured_output` > `country`

  1. **Add Python Code**
        Paste this code into `PYTHON3`:

        ```python theme={null}
        def main(country: str) -> dict:
          country_name = country.lower()
          fun_facts = {
            "japan": "Japan has more than 5 million vending machines.",
            "france": "France is the most visited country in the world.",
            "italy": "Italy has more UNESCO World Heritage sites than any other country."
          }
          fun_fact = fun_facts.get(country_name, f"No fun fact available for {country.title()}.")
          return {"fun_fact": fun_fact}
        ```

  1. **Rename Output Variable**
        Change output variable `result` to `fun_fact` to have a better labeled variable

##### 3. Answer Node: Final Answer to User

> **ℹ️ Info:**
>   `Answer` Node creates a clean final output to return.

  1. **Create Answer Node**
        Create an `Answer` Node using the `Add Node` button

  1. **Configure Answer Field**
        Paste into the Answer Field:

        ```text theme={null}
        Q: {{ structured_output.question }}

        A: {{ structured_output.answer }}

        Fun Fact: {{ fun_fact }}
        ```

End Workflow:

  *[Image: Complete workflow diagram showing LLM, Code, and Answer nodes connected]*

***

#### Step 3: Test the Bot (3 min)

Click `Preview`, then ask:

* "What is the capital of France?"
* "Tell me about Japanese cuisine"
* "Describe the culture in Italy"
* Any other questions

Make sure your Bot works as expected!

#### You've Completed the Bot!

This guide showed how to integrate language models reliably and scalably without reinventing infrastructure. With Dify's visual workflows and modular nodes, you're not just building faster, you're adopting a clean, production-ready architecture for LLM-powered apps.

#### Twitter Account Analyzer

*Build a Chatflow that scrapes a Twitter profile via Crawlbase and analyzes the user's tweets with an LLM*

**Source:** https://docs.dify.ai/en/learn/tutorials/twitter-chatflow

Build a Chatflow that scrapes a Twitter profile via Crawlbase and analyzes the user's tweets with an LLM

#### Introduction

In Dify, you can use some crawler tools, such as Jina, which can convert web pages into markdown format that LLMs can read.

Recently, [wordware.ai](https://www.wordware.ai/) has brought to our attention that we can use crawlers to scrape social media for LLM analysis, creating more interesting applications.

However, knowing that X (formerly Twitter) stopped providing free API access on February 2, 2023, and has since upgraded its anti-crawling measures. Tools like Jina are unable to access X's content directly.

> Starting February 9, we will no longer support free access to the Twitter API, both v2 and v1.1. A paid basic tier will be available instead 🧵
>
> — Developers (@XDevelopers) [February 2, 2023](https://twitter.com/XDevelopers/status/1621026986784337922?ref_src=twsrc%5Etfw)

Fortunately, Dify also has an HTTP tool, which allows us to call external crawling tools by sending HTTP requests. Let's get started!

#### Prerequisites

##### Register Crawlbase

Crawlbase is an all-in-one data crawling and scraping platform designed for businesses and developers. Crawlbase Scraper can pull data from social platforms like X, Facebook, and Instagram.

Register at [crawlbase.com](https://crawlbase.com).

##### Sign in to Dify

Open Dify in your browser and sign in. You'll need access to a running Dify instance to follow along.

##### Configure LLM Providers

Go to **Integrations** > **Model Provider**, install at least one model provider (for example, OpenAI), and configure its credentials.

  ![Configure Model Provider in Account Setting](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/4b4102f9027e2bda3fc520eaa8ea2354.png)

#### Create a Chatflow

Now, let's get started on the Chatflow.

Click on `Create from Blank` to start:

  ![Create from Blank to Start](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/b2955735f5c122d8a2fc08ef13654239.png)

The initialized Chatflow should be like:

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/baee341b771d1cd77780fd4845b467b2.png)

#### Add nodes to Chatflow

  ![The Final Chatflow Looks Like This](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/bad3185d9f2c92994c24de65a5414182.png)

##### Start node

In start node, we can add some system variables at the beginning of a chat. In this article, we need a Twitter user's ID as a string variable. Let's name it `id`.

Click on Start node and add a new variable:

  ![Start Node and Add a New Variable](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/a041be2230364d7e729527f3f7af34d8.png)

##### Code node

According to [Crawlbase docs](https://crawlbase.com/docs/crawling-api/scrapers/#twitter-profile), the variable `url` (this will be used in the following node) should be `https://twitter.com/` + `user id`, such as `https://twitter.com/elonmusk` for Elon Musk.

To convert the user ID into a complete URL, we can use the following Python code to integrate the prefix `https://twitter.com/` with the user ID:

```python theme={null}
def main(id: str) -> dict:
    return {
        "url": "https://twitter.com/"+id,
    }
```

Add a code node and select python, and set input and output variable names:

  ![Add a Code Node and Select Python, and Set Input and Output Variable Names](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/e5523ba1f801f4009b74e7cf03e2ef2f.png)

##### HTTP request node

Based on the [Crawlbase docs](https://crawlbase.com/docs/crawling-api/scrapers/#twitter-profile), to scrape a Twitter user's profile in http format, we need to complete HTTP request node in the following format:

  ![Based on the Crawlbase Docs, to Scrape a Twitter User's Profile in HTTP Format,](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/13899d88abeb3b3be20c44d40565a5f9.png)

Importantly, it is best not to directly enter the token value as plain text for security reasons, as this is not a good practice. Actually, in the latest version of Dify, we can set token values in **`Environment Variables`**. Click `env` - `Add Variable` to set the token value, so plain text will not appear in the node.

Check [https://crawlbase.com/dashboard/account/docs](https://crawlbase.com/dashboard/account/docs) for your crawlbase API Key.

  ![Check HTTPS](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/c99b66ac8d30289615a8869bae5a6455.png)

By typing `/`, you can easily insert the API Key as a variable.

  ![By Typing / , You Can Easily Insert the API Key as a Variable](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/51f9350677acb396bad5841fa80c903c.png)

Tap the start button of this node to check whether it works correctly:

  ![Tap the Start Button of This Node to Check Whether It Works Correctly](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/094b96e513169a47f1749e46e1357893.png)

##### LLM node

Now, we can use LLM to analyze the result scraped by crawlbase and execute our command.

The value `context` should be `body` from HTTP Request node.

The following is a sample system prompt.

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/46f4e15ac1e9d3ca3f47dc5bb921ff01.png)

#### Test run

Click `Preview` to start a test run and input twitter user id in `id`.

  ![Preview to Start a Test Run and Input Twitter User ID in ID](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/a25b122dfa14f0c65fcd3498ccf1898e.png)

For example, I want to analyze Elon Musk's tweets and write a tweet about global warming in his tone.

  ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/835a01082e74723138d9f97bee0c6c4b.png)

Does this sound like Elon? lol

Click `Publish` in the upper right corner and add it in your website.

Have fun!

#### Lastly...

##### Other X(Twitter) Crawlers

In this article, I've introduced crawlbase. It should be the cheapest Twitter crawler service available, but sometimes it cannot correctly scrape the content of user tweets.

The Twitter crawler service used by [wordware.ai](https://www.wordware.ai/) mentioned earlier is **Tweet Scraper V2**, but the subscription for the hosted platform **apify** is \$49 per month.

#### Links

* [X@dify_ai](https://x.com/dify_ai)
* Dify's repo on GitHub: [https://github.com/langgenius/dify](https://github.com/langgenius/dify)

#### Lesson 1: What is a Workflow?

**Source:** https://docs.dify.ai/en/learn/tutorials/workflow-101/lesson-01

#### 👋 Welcome to Dify 101

We are going to take you from Zero to Hero. By the end of this course, you will build your very own Advanced AI Email Assistant.

Let's leave coding behind for a second and talk about cooking.

Imagine you want to cook a dish that you haven't made before. To make that happen, you need a **Recipe**. A recipe is just like a workflow! It tells you exactly what to do, in what order, to get the dish you want.

#### Meet Workflow

In Dify, you are the head chef who writes a Recipe for the AI to follow. Here're the things you need to prepare beforehand:

1. Input (Ingredients): The information you give the AI. This could be a user's question, a PDF document, or a messy email draft.
2. Process (Instructions): The steps you force the AI to take. For example: First, summarize this text. Next, translate it into Spanish. Finally, format it as a LinkedIn post.
3. Output (The Dish): The final result the AI hands back to you.

To sum up, a workflow is a flowchart that asks AI to complete tasks in a specific order.

This is a Smart ID Scanner workflow. Its job is to extract the information on front and back of an ID card, then send these texts back to you.

  *[Image: Workflow Example]*

##### Node

Let's have a closer look of the workflow above. That whole process is simply made up of a few connected steps: **Uploading the image, Extracting the information, and Combining the results**.

Each of these steps is called a **Node**.

Think of them like runners in a relay race: each node has a specific task. Once it finishes its turn, it passes the baton to the next node in line.

Dify offers you a box of ready-to-use nodes, such as the LLM, Knowledge Retrieval, If/Else, Tools, etc.

You can connect these nodes just by dragging and dropping—it's like building with the Lego blocks! You can easily snap them together to create a powerful automated workflow.

#### It's Your Turn

1. Go [Dify](https://dify.ai/) and click **Get Started** in the upper right corner.
2. Click on Explore. This is a library which collects different workflow of different scenarios.

     *[Image: Explore]*

3. Pick a template that looks like a right fit for you. Don't worry if you don't understand every setting yet—just look at how the nodes are connected.

#### Lesson 2: Head and Tail (Start & Output Node)

**Source:** https://docs.dify.ai/en/learn/tutorials/workflow-101/lesson-02

In the last lesson, we compared a Workflow to a Recipe. Today, we are stepping into the professional kitchen to prep our ingredients (Start) and get our serving plates ready (Output).

#### Create the App

  1. **Create from Blank**
        Click on **Studio** at the top of the screen. Under Create App on the left, click **Create from Blank**.

          *[Image: Create the App]*

  1. **Configure App Type**
        Select **Workflow** as the app type, fill up **App Name & Icon**, then click **Create**.

          *[Image: App Name & Icon]*

  1. **Choose Start Node Type**
        Click User Input, and you'll see a new popup window. There are two options here that decide how your app starts running:

        * **User Input**

          This is **Manual Mode**. The workflow only starts working when you (the user) type something into the chat box.

          Best for: Most AI apps. For example, chatbots, writing assistants, translation, etc.
        * **Trigger**

          This is **Automatic Mode**. It runs automatically based on a signal (like 8:00 AM every morning, or a specific event).

          Best for: Repetitive task that runs on a specific time, or run this workflow after a task is completed else where. For example, daily news summary.

          *[Image: Trigger]*

#### Meet the Orchestration Canvas

After selecting the Start node, you will see a large blank area. This is your orchestration canvas where you will design, build, and test your workflow.

  *[Image: Orchestration Studio]*

Remember the Nodes we learned in Lesson 1? The user input node you see on the canvas now is where everything begins.

Every complete workflow relies on a basic skeleton: the Start Node (The Head) and the Output Node (The Tail).

#### The Start Node

  *[Image: Start Node]*

The Start Node is the only entrance to your entire workflow. It's like the Prep Ingredients step in cooking. Its job is to define what information the workflow needs to receive from the user to get started.

We just selected **User Input** as our Start Node.

##### Core Concept: Variables

Inside the Start Node, you will see the word **Variable**. Don't panic! You can think of a variable as a **Storage Box with a Label**.

Each box is designed to hold a specific type of information:

For example, if you are building a Travel Planner, you need the user to provide two pieces of information: `Destination` and `Travel Days`.

User A might want to go to Japan for 5 days. User B might want to go to Paris for 3 days.

Every user provides different content, so every time the app runs, the stuff inside these boxes changes.

This is the meaning of a Variable—digging a hole for the user to fill, helping your workflow to handle different requests flexibly every time.

#### The End Node (Output)

  *[Image: Output]*

This is the finish line of the workflow. Think of it as Serving the Dish and it defines what the user actually sees at the very end.

For example, remember that Travel Planner we talked about? If the user inputs Destination: Paris and Duration: 5 Days in the User Input Node. The Output Node is where the system finally hands over the result: Here is your complete 5-Day Itinerary for Paris.

To sum up, the Start Node and End Node define the basic input and output, shaping the skeleton of your app.

#### Hands-On Practice: Start Building an AI Email Assistant

Let's build the basic framework for an AI Assistant that helps you write emails.

  1. **Create the App**
        You can either:

        * Continue on the canvas you just opened, or
        * Go back to Studio → Create Blank App → select Workflow, and name it Email Assistant (Remember to select **User Input** in the popup!)

  1. **Configure the Start Node (Prep Ingredients)**
        If you need AI to help you with a email reply, what information do you need to give it?

        That's right: usually the Customer's Name and the Original Email Content.

        1. Click on the **Start** node. In the panel on the right, look for **Input Field** and click the **+** button.

          *[Image: User Input Field]*

        2. In the popup, we will create two variables (two storage boxes):

           **Variable 1 (For the Customer Name)**

             *[Image: Add First Variable]*

           * Field Type: Text (Short Text)
           * Variable Name: `customer_name`
           * Label Name: Customer Name
           * Keep other options as default

           **Variable 2 (For the Email Content)**

             *[Image: Add Second Variable]*

           * Field Type: Click the dropdown and select **Paragraph** (Since emails are usually long, a Paragraph box is bigger and holds more text)
           * Variable Name: `email_content`
           * Label Name: Original Email
           * Max Length: Manually change this to **2000** to ensure it fits long emails

           > **💡 Tip:**
>              **Variable Name vs. Label Name**
>
>              You might notice we had to fill in two names. What's the difference?
>
>              * **Variable Name**: This is the ID card for the system. It must be unique, use English letters, and cannot have spaces.
>              * **Label Name**: This is the Label for the users. You can name it with any language (English, Chinese, etc.). It will be shown on the screen.
>

  1. **Create the End Node (Set the Goal)**
        Right-click anywhere on the blank white space of the canvas. Select **Add Node** and select **Output** from the list.

          *[Image: Create the End Node]*

Here's everything on your canvas: a **Start Node** ready to receive a name and an email, and an **Output Node** waiting to send the final result.

  *[Image: Start Node and Output]*

We have successfully built basic frame of the workflow. The empty space in the middle is where we will place the LLM (AI Brain) Node in the next lesson to process this information.

#### Mini Challenge

**Task**: If you needed to create a Travel Plan Generator, what variables should the Start Node include?

> **💡 Tip:**
>   Try exploring the Field Types in **Add Variable**.

#### Lesson 3: The Brain of the Workflow (LLM Node)

**Source:** https://docs.dify.ai/en/learn/tutorials/workflow-101/lesson-03

*[Image: LLM Node]*

In Lesson 2, we set up the Ingredients (Start Node) and the Serving Plate (Output Node).

If the Start Node is the prep cook, the LLM Node is the Master Chef. It is the brain and core of your workflow.

It handles all the thinking, analyzing, and creative writing. Whether you want to summarize an article, write code, or draft an email, this is the node that does the heavy lifting.

#### Configure the Model

Before getting started, we need to connect to a model provider.

  1. **Open Integrations**
        Go to **Integrations** > **Model Provider**.

          *[Image: Model Provider]*

  1. **Install OpenAI Provider**
        Find OpenAI, and click **Install**.

          *[Image: Choose OpenAI]*

          *[Image: Install OpenAI]*

  1. **Return to the Canvas**
        Once installed, you are ready to go! Click **ESC** (or the **X**) in the upper right corner to return to your canvas.

#### Understand the Tags

A pastry chef is great at cakes but terrible at sushi. Similarly, different AI models have different strengths.

When selecting a model in Dify, you will see tags next to their names. Here's how to read them so you can pick the right one for you.

  **CHAT (The Conversationalist):**

    This is the bread and butter of AI. It's best for:

    * Dialogue
    * Writing articles
    * Summarizing text
    * Answering questions

  **128K (The Great Memory):**

    This number represents the **Context Window**. You can think of it as short-term memory.

    Here, K stands for thousand. **128K** means the model can hold 128,000 tokens (roughly equals to a word or a syllable). The bigger the number is, the better its memory is.

    > **ℹ️ Info:**
>       If you need to analyze a massive PDF report or a whole book, you need a model with a big number here.
>

  **Multi-modal (The Evolved Senses):**

    Modal just means **Type of Information**. Most early AI models could only read text. Multi-modal models are evolved—they have senses like eyes and ears.

    **VISION (The Eyes)**

    Models with this tag can do more than read; they can see! You can upload a photo of a sunset and ask, What colors are in this? or upload a picture of your fridge ingredients and ask, What can I cook with this?

    **AUDIO (The Ears)**

    Models with this tag can hear. You can upload an audio recording of a meeting or a lecture, and the model can transcribe it into text or write a summary for you.

    **VIDEO (The Movie Analyst)**

    These models can watch and understand video content. They can analyze what is happening in a video clip, just like a human watching a movie.

    **DOCUMENT (The Reader)**

    These models are expert readers. Instead of copying and pasting text, you can just upload a file (like a PDF or Word document). The model will read the file directly and answer questions based on what is written inside.

For our Email Assistant, the LLM with the **CHAT** tag is exactly what we need.

#### Hands-On 1: Add the LLM Node

Let's put the brain into our workflow.

  1. **Open your App**
        Go back to the **AI Email Assistant** workflow we created in Lesson 2.

  1. **Add the Node**
        Right-click in the empty space between Start and Output node. Click on the new **LLM** block. In the right-side panel, look for **Model**. Select **gpt-4o-mini**.

          *[Image: Add the Node]*

  1. **Connect the Nodes**
        Drag a line from the Start node to the LLM node. Drag a line from the LLM node to the Output node. Your flow should look like this: **Start → LLM → Output**.

          *[Image: Connect the Nodes]*

Now we need to tell LLM exactly what to do by sending instructions which is called a **Prompt**.

  *[Image: Add Prompt]*

##### Key Concept: The Prompt (The Instructions)

**What is a Prompt?** Think of the Prompt as the specific note you attach to the order ticket. It tells the AI exactly **what to do** and **how to do it**.

The most critical part is the ability to use **Variables** from the Start Node directly within your Prompt. This allows the AI to adapt its output based on the different raw materials you provide each time.

In Dify, when you insert a variable like `customer_name` into the prompt, you are telling the AI: Go and look in the box labeled Customer Name and use the text inside.

#### Hands-On 2: Write the Prompt

Now, let's apply this. We are going to write a prompt that mixes instructions with our variables.

  1. **Draft the Instructions**
        Click the LLM Node to open the panel and find the **system** box. **System instructions** set the rules for how the model should respond—its role, tone, and behavioral guidelines.

        Let's start by writing out the instructions. You can copy and paste the text below.

        ```plaintext wrap theme={null}
        You are a professional customer service manager. Based on the customer's email, please draft a professional reply.
        Requirements:
        1. Start by addressing the customer name with a friendly tone.
        2. Thank them for their email.
        3. Let them know we have received it.
        4. Sign off as Anne.
        ```

  1. **Add User Messages**
        User messages are what you send to the model—a question, request, or task for the model to work on.

        In this workflow, the customer's name and the email content change every single time. Instead of typing them out manually, we add Variables in user messages.

        1. Click **Add Message** button below system box.
        2. In the User Message box, type **customer name**:.
        3. Press `/` on your keyboard.
        4. The Variable Selection menu pops out, and click `customer_name`.
        5. Press Enter to start a new line, and type **email content:.** Then, Press the / key again and click on `email_content`.

          *[Image: Add User Message]*

        > **💡 Tip:**
>           You don't need to type out those curly brackets manually! Just hit `/`, then pick your variable from the menu.
>

        4. Finally, your final Prompt will look like this:

          *[Image: Final Prompt]*

> **✅ Check:**
>   **Hooray!** You've finished your first AI workflow in Dify!

#### Run and Test

The ingredients are prepared, the chef is stand-by, and the instructions are ready. But does the dish taste good? Before we serve it to the customer, let's do a recipe testing.

Testing is the secret sauce to a stable workflow. It helps us catch those sneaky little issues before they are put into work.

##### Quick Concept: The Checklist

Think of the **Checklist** as your workflow's personal Health Check Doctor.

It monitors your work in real-time, automatically spotting incomplete settings or mistakes (like a node that isn't connected to anything).

Glancing at the Checklist before you hit **Publish** button is the best way to catch unnecessary errors early.

##### Hands-On 3: Test & Debug

  1. **The Pre-flight Check**
        Look at the top right corner of your canvas. Do you see the **Checklist** icon with a little number **1** on it? This is Dify telling you: Wait a second! There's one small thing missing here_._

          *[Image: Checklist]*

  1. **Analyze the Warning**
        Click on it, and you will see a warning: **output variable is required**. It means that the output node receives nothing.

        Imagine your Head Chef (the LLM) has finished cooking the food, but the Waiter (the Output Node) has empty hands.

  1. **Fix the Issue**
        1. Click on the **Output Node**
        2. Look for **Output Variable** and click the **Plus (+)** icon next to it
        3. Type `email_reply` in the **Variable Name** field
        4. Select the value: Click the variable selector and choose `{x} text` from the LLM Node

          *[Image: Fix the Issue]*

  1. **Make a Test Run**
        Now, there's no pop-up number on checklist. Let's do a test run.

        Click **Test Run** at the top right corner of the canvas. Enter the customer's name and the email, then click **Start Run**.

          *[Image: Test Run]*

          ```text Sample Email for Testing theme={null}
          Customer Name: Amanda

          Original Email:
          Hi there,

          I'm writing to ask for more information about Dify. Could you please tell me more on it?

          Best regards,
          Amanda
          ```

  1. **Success!**
        This time, you will see green checkmarks ✅ on each of the nodes and the generated reply from AI.

> **✅ Check:**
>   **Great job!**
>
>   You didn't just build a workflow, but also know how to use the checklist and check before it goes live.

#### Mini Challenge

Use the same structure to build a travel planner.

> **💡 Tip:**
>   Explore the **Prompt Generator** to help you craft better prompts!
>
>
>     *[Image: Prompt Generator]*
>

#### Lesson 4: The Cheat Sheet (Knowledge Retrieval)

**Source:** https://docs.dify.ai/en/learn/tutorials/workflow-101/lesson-04

In the previous lessons, our AI email assistant can draft basic emails. But what if a customer asks about specific pricing plans or refund policy, the AI might start Hallucinating—which is a fancy way of saying it's confidently making things up.

How do we stop the AI from hallucination? We give it a Cheat Sheet.

#### What is Retrieval Augmented Generation (RAG)

The technical name for this is RAG (Retrieval-Augmented Generation). Think of it as turning the AI from a chef who memorizes general recipes into a chef who has a Specific Cookbook right on the counter.

It happens in three simple steps:

**1. Retrieval (Find the Recipe)**

When a user asks a question, the AI flips through your Cookbook (the files you uploaded) to find the most relevant pages.

Example: Someone asks for Grandma's Special Apple Pie. You go find that specific recipe page.

**2. Augmentation (Prepare the Ingredients)**

The AI takes that specific recipe and puts it right in front of its eyes so it doesn't have to rely on memory.

Example: You lay the recipe on the counter and get the exact apples and cinnamon ready.

**3. Generation (The Baking)**

The AI writes the answer based only on the facts it just found.

Example: You bake the pie exactly as the recipe says, ensuring it tastes like Grandma's, not a generic store-bought version.

#### The Knowledge Retrieval Node

Think of this as placing a stack of reference materials right next to your AI Assistant. When a user asks a question, the AI first flips through this Cheat Sheet to find the most relevant pages. Then, it combines those findings with the user's original question to think of the best answer.

In this practice, we will use the Knowledge Retrieval node to provide our AI Assistant with official Cheat Sheets, ensuring its answers are always backed by facts!

##### Hands-On 1: Create the Knowledge Base

  1. **Enter the Library**
        Click **Knowledge** in the top navigation bar and click **Create Knowledge**.

          *[Image: Create Knowledge]*

        In Dify, you can sync from Notion or a website, but for today, let's upload a file from your device. Click [here](https://drive.google.com/file/d/1imExB0-rtwASbmKjg3zdu-FAqSSI7-7K/view) to download Dify Intro for the upload later.

  1. **Upload the File**
        Click **Import from file**. Then, select the file we just downloaded for upload.

          *[Image: Import from File]*

  1. **The 'Chopping' Step (Text Segmentation)**
        High-relevance chunks are crucial for AI applications to provide precise and comprehensive responses. Imagine a long book. It's hard to find one sentence in 500 pages. Dify chops the book into different Knowledge Cards so it can find the right answer faster.

        **Chunk Structure**

        Here, Dify automatically splits your long text into smaller, easier-to-retrieve chunks. We'll just stick with the General Mode here.

          *[Image: Chunk Structure]*

        **Index Method**

        * **High Quality**: Use LLM model to process documents for more precise retrieval helps LLM generate high-quality answers
        * **Economical**: Using 10 keywords per chunk for retrieval, no tokens are consumed at the expense of reduced retrieval accuracy

          *[Image: Index Method]*

  1. **Retrieval Settings**
        After the document has been processed, we need to do one final check on the retrieval settings. Here, you can configure how Dify looks up the information.

        In Economical mode, only the inverted index approach is available.

          *[Image: Retrieval Setting]*

        * **Inverted Index**

          This is the default structure Dify uses. Think of it like the Index at the back of a book—it lists key terms and tells Dify exactly which pages they appear on.

          This allows Dify to instantly jump to the right knowledge card based on keywords, rather than reading the whole book from start.
        * **Top K**

          You'll see a slider set to 3. This tells Dify: When the user asks a question, find the top 3 most relevant Knowledge Cards from the cookbook to show the AI.

          If you set it higher, the AI gets more context to read, but if it's too high, it might get overwhelmed with too much information.

        For now, let's just keep the default settings—they are already perfectly suited for our needs.

          *[Image: Document Processing]*

  1. **Save and Process**
        Click **Save and Process**. Your knowledge base is ready!

> **✅ Check:**
>   **Awesome!**
>
>   You have successfully created your first Knowledge Base. Next, we'll use this Knowledge Base to upgrade our AI Email Assistant.

##### Hands-On 2: Add the Knowledge Retrieval Node

  1. **Add the Node**
        1. Go back to your Email Assistant Workflow.
        2. Hover over the line between the Start and LLM nodes.
        3. Click the **Plus (+)** icon and select the **Knowledge Retrieval** node.

          *[Image: Add Knowledge Retrieval Node]*

  1. **Connect Knowledge Base**
        1. Click the node, and head to the right panel.
        2. Click the **plus (+)** button next to **Knowledge** to add knowledge.

             *[Image: Add Knowledge]*

        3. Choose **What's Dify**, and click **Add**.

             *[Image: Select Knowledge]*

  1. **Configure Query Text**
        Now the knowledge base is ready, how can we make sure that AI is looking through the knowledge base to search the answer with the email?

        Stay at the panel, navigate to **Query text** above, and select `email_content`.

        By doing this, we are telling AI: Take the customer's message and use it as a search keyword to flip through our cookbook and find the matching info. Without a query, the AI is just staring at a closed book.

          *[Image: Query Text]*

In this way, the Email Assistant will use the customer's original email as a search keyword to find the most relevant answers in the Knowledge Base.

##### Hands-On 3: Upgrade the Email Assistant

Now, the knowledge base is ready. We need to tell the LLM node to actually read the knowledge as context before generating the reply.

  1. **Add Context**
        1. Click the **LLM Node**. You'll see a new section called **Context**.
        2. Click it and select **result** from the Knowledge Retrieval node.

             *[Image: Add Context]*

  1. **Update the Prompt**
        We need to tell the AI to generate reply based on the context.

        In **System**, add additional requirement **Generate response based on** `/` and select **Context**.

          *[Image: Update Prompt]*

**Whoo!** You've just completed the most challenging part. Now, your email assistant has a knowledge base to check when generating responses. Let's see how it works.

Feel free to use the sample texts below to do the testing.

  ```text Sample Email for Testing theme={null}
  Customer Name: Amanda

  Original Email:
  Hi,

  What does the name 'Dify' actually stand for, and what can it do for my business?

  Best regards,
  Amanda
  ```

Check on the result and you'll find that instead of a generic guess, the AI will look at the knowledge base and explain what Dify stands for.

  *[Image: Test Result]*

#### Mini Challenge

1. What happens if a customer asks a question that isn't in the knowledge base?
2. What kind of information could you upload as a knowledge base?
3. Explore Chunk Structure, Index Method, and Retrieval Setting.

#### Lesson 5: The Crossroads of Your Workflow (Sorting and Executing)

**Source:** https://docs.dify.ai/en/learn/tutorials/workflow-101/lesson-05

Right now, our Email Assistant treats every message following the same path of the workflow. That's not smart enough. An email asking about Dify's price should be handled differently than an email on bug reporting.

To make our assistant truly intelligent, we need to teach it how to Read the Room. We're going to set up a Crossroads that sends different types of emails down different tracks.

#### The If/Else Node

  *[Image: If/Else Node]*

If/Else node is just like a traffic light. It checks a condition (like Does this email mention pricing? ) and sends the flow left or right based on the result.

##### Hands-On 1: Set up the Crossroads

Let's upgrade our assistant so it can tell the difference between Dify-related emails and Everything else.

  1. **Insert the Node**
        Hover over the line between the Start and Knowledge Retrieval nodes. Click the **Plus (+)** icon and select the **If/Else** node.

  1. **Set the Rules**
        1. Click the node to open the panel
        2. Click **+ Add Condition** in the IF section. Choose the variable: `{x} email_content`

          *[Image: Add Condition]*

        3. The Logic: Keep it as **Contains**. Type **Dify** in the input box

          *[Image: Contains]*

        Now, the complete logic for the IF branch is: `If the email content contains the word Dify`.

> **ℹ️ Info:**
>   **Understanding the Traffic Light**
>
>   When setting conditions, Dify offers several ways to judge information, much like the different signals at a crossroads:
>
>   * **Is / Is Not**
>
>     Like a perfect key for a lock. The content must match your value exactly.
>   * **Contains / Not Contains**
>
>     Like a magnifying glass. It checks if a specific keyword exists anywhere in the text. This is what we are using today.
>   * **Starts with / Ends with**
>
>     Check if the text begins or ends with specific characters.
>   * **Is Empty / Is Not Empty**
>
>     Check if the variable has any content. For example: Checking if a user actually uploaded an attachment. Understanding these helps you set accurate and flexible rules, building a much smarter workflow!

##### Hands-On 2: Plan Different Paths

Now that we have the crossroad here, we need to decide what happens on each road.

###### A. The Dify-Related Email Track (IF Branch)

Click the **plus (+)** icon on the right side of the IF branch, drag out a line, and connect it to **Knowledge Retrieval** node.

What this means: When the email contains the word Dify, the flow will execute the professional reply process we built in the last lesson (which looks up information in the Knowledge Base).

  *[Image: Connect IF Branch]*

###### B. The Unrelated Email Track (ELSE Branch)

For emails that are not related or mention Dify, we want to create a simple, polite, and general reply process.

  1. **Create a new Node**
        Click the **(+)** next to ELSE and select a new **LLM Node (LLM 2)**

  1. **Add Prompt to this LLM node**
        Copy and paste the prompt below

        ```plaintext wrap theme={null}
        You are a professional customer service manager. Based on the customer's email, kindly inform the user that no relevant information was found and provide relevant guidance.

        Requirements:
        1. Address the customer name in a friendly tone.
        2. Thank them for their letter.
        3. Keep the tone professional and friendly.
        4. Sign off as "Anne."
        ```

  1. **Add User Message**
        1. Click **Add Message** button below system.
        2. In the User Message box, type **customer name**:.
        3. Press `/` on your keyboard.
        4. You can see the Variable Selection menu pops out, and click `customer_name`.
        5. Press Enter to start a new line, and type **email content**:
        6. Press the / key again and click on `email_content`.

          *[Image: Prompt for LLM 2]*

Now we have two tracks generating two different replies. Imagine if we had 10 tracks, our workflow would look like a messy plate of spaghetti.

To keep things clean, we use a Variable Aggregator. Think of it as a Traffic Hub where all the different roads merge back into one main highway.

#### Variable Aggregator

  *[Image: Variable Aggregator]*

Variable Aggregator is like a traffic hub where all the different roads merge back into one main highway.

##### Hands-On 3: Add Variable Aggregator

  1. **Add the Aggregator**
        1. Select the connection line between the End Node and the LLM node and delete it.
        2. Right-click on the canvas, select **Add Node**, and choose the **Variable Aggregator** node.

          *[Image: Add Variable Aggregator]*

  1. **Merge the Paths**
        Connect LLM and LLM 2 node to the Variable Aggregator.

  1. **Assign the Output**
        1. Click the Variable Aggregator node.
        2. Click the **plus (+)** icon next to **Assign Variables**.
        3. Select the **text** from LLM 1 AND the **text** from LLM 2.

          *[Image: Assign Variable]*

        Now, no matter which LLM node generates the response, the Variable Aggregator node gathers the content and hands it to the Output Node.

  1. **The Final Step**
        1. Connect the Variable Aggregator to the Output node.
        2. Update the Output Variable to the Variable Aggregator's result instead of previous LLM results.

          *[Image: Update Output Variable]*

        Here's how the workflow looks:

          *[Image: Final Workflow]*

  1. **Test and Run**
        Click **Test Run**, enter a customer name, and try testing with inputs that both include and exclude the keyword Dify to see the different results.

#### Mini Challenge

For business inquiry emails, how should we edit this workflow to generate proper response?

> **💡 Tip:**
>   Don't forget to update knowledge base with business-related files.

#### Lesson 6: Handle Multiple Tasks (Parameter Extraction & Iteration)

**Source:** https://docs.dify.ai/en/learn/tutorials/workflow-101/lesson-06

Imagine you get an email saying:

> Hi! What exactly is Dify? Also, which models does it support? And do you have a free plan?

If we send this to our current AI assistant, it might only answer the first question or give a vague response to both.

We need a way to identify every question first, and then loop through our Knowledge Base to answer them one by one.

#### Parameter Extractor

  *[Image: Parameter Extractor]*

You can take Parameter Extractor as a highly organized scout. It reads a paragraph of texts (like an email) and picks out the specific piece of information you asked for, putting them into a neat and organized list.

##### Hands-On 1: Add Parameter Extractor

Before we upgrade the email assistant, let's remove these nodes: Knowledge Retrieval, If/Else, LLM, LLM 2, and Variable Aggregator.

  1. **Add the Node**
        Right after the Start node, add the **Parameter Extractor** node.

          *[Image: Add Parameter Extractor]*

  1. **Set the Input**
        Click Parameter Extractor, and in the **Input Variable** section on the right panel, choose `email_content`.

          *[Image: Set the Input]*

        Since AI doesn't automatically know which specific information we need from the email, we must tell it to collect all the questions.

  1. **Add Extract Parameter**
        Click the **plus (+)** icon next to **Extract Parameters** to start defining what the AI should look for. Let's call it `question_list`.

          *[Image: Add Extract Parameter]*

        > **ℹ️ Info:**
>           **Parameter Types**
>
>           If Parameter Extractor is a scout, then Type is the bucket they use to carry the info. You need the right bucket for the right information.
>
>           **Single Items (The Small Buckets)**
>
>           * **String (Text)**: For a single piece of text, e.g. customer's name
>           * **Number**: For a single digit, e.g. order quantity
>           * **Boolean**: A simple Yes or No (True/False), good for a judgement result or a decision
>
>           **List Items (The Arrays)**
>
>           * **Array[String]**: Array means List, and String means Text. So, `Array[String]` means we are using a basket that can hold multiple pieces of text—like all the separate questions in an email
>           * **Array[Number]**: A container that holds different numbers, e.g. a list of prices or commodities
>           * **Array[Boolean]**: Used to store multiple Yes/No judgment results. For example, checking a list containing multiple to-do items and returning whether each item is completed, such as `[Yes, No, Yes]`
>           * **Array[Object]**: An advanced folder that holds sets of data (like a contact list where each entry has a Name and a Phone Number)
>

  1. **Finish Adding Extract Parameter**
        1. Based on our needs, choose `Array[String]` for the email content.
        2. Add description for providing additional context. You can write: All the questions raised by the user in the email. After that, click **Add**.

          *[Image: Finish Adding Extract Parameter]*

  1. **Add Instructions**
        In the **Instructions** box below the extracted parameters, type a clear command to tell the AI how to act.

        For example: Extract all questions from the email, and make each question as a single item on the list.

By doing this, the node will be able to find all the questions in the email. Now that our scout has successfully gathered the Golden Nuggets, we need to move to the next step: teaching the AI to process each question.

#### Iteration

  *[Image: Iteration]*

With iteration, your assistant has a team of identical twins. When you hand over a list (like questions in the mail list), a twin appears for every single item on that list.

Each twin takes their assigned item and performs the exact same task you've set up, ensuring nothing gets missed.

##### Hands-On 2: Set up Iteration Node

  1. **Add the Node**
        1. Add an Iteration node after the Parameter Extractor.
        2. Click on the Iteration node and navigate to the Input panel on the right.
        3. Select `{x} question_list` from the Parameter Extractor. Leave the output variable blank for now.

          *[Image: Add Iteration Node]*

        **Advanced Options in Iteration**

        In the Iteration panel, you'll see more settings. Let's have a quick walk-through.

          *[Image: Advanced Options in Iteration]*

        **Parallel Mode**: OFF (Default)

        * When disabled, the workflow processes each item in the list one after another (finish Question 1, then move to Question 2).
        * When enabled, the workflow attempts to process all items in the list simultaneously (similar to 5 chefs cooking 5 different dishes at the same time).

        **Error Response Method**: Terminate on error by default.

        * **Terminate**: This means if any single item in the list (e.g., the 2nd question) fails during the sub-process, the entire workflow will stop immediately
        * **Ignore Error and Continue**: This means even if the 2nd question fails, the workflow will skip it and move on to process the remaining questions
        * **Remove Abnormal Output**: Similar to ignore, but it also removes that specific failed item from the final output list results

        Back to the workflow, you'll see a sub-process area under the Iteration node. Every node inside this box will run once for every question.

  1. **Add Knowledge Retrieval Node**
        1. Inside the Iteration box, add a Knowledge Retrieval node.
        2. Set the query text to `{x} item`. In Iteration, item always refers to the question that is currently being processed.

          *[Image: Add Knowledge Retrieval Node and Set Query Text]*

  1. **Add LLM Node**
        1. Add an LLM node after Knowledge Retrieval.
        2. Configure it to answer the question based on the retrieved context.

        > **💡 Tip:**
>           Remember Lesson 4? Use those Prompt skills and don't forget context!
>

        Feel free to use the prompt below:

        **System**:

        ```plaintext wrap theme={null}
        You are a professional Dify Customer Service Manager. Please provide a response to questions strictly based on the `Context`.
        ```

        **User**:

        ```plaintext wrap theme={null}
        questions: Iteration/{x} item
        ```

          *[Image: Add LLM Prompt]*

        Since the iteration node generates an answer for each individual question, we need to gather all these answers to create one complete reply email.

  1. **Set Iteration Output**
        1. Click the Iteration node.
        2. In the **Output Variable**, select the variable representing the LLM's answer inside the loop. Now, the Iteration node will collect every answer and gather them into a new list.

          *[Image: Set Iteration Output]*

  1. **Add Final LLM Node**
        Finally, connect one last LLM node. This final editor will take all the collected answers and polish them into one professional email.

        Don't forget to add prompt in system and user message. Feel free to refer the prompt below.

        ```plaintext wrap theme={null}
        You are a professional customer service assistant. Please organize the answers prepared for customer into a clear and complete email reply.
        Sign the email as Anne.
        ```

        **User**:

        ```plaintext wrap theme={null}
        answers: Iteration/{x}output
        customer: User Input/{x}customer_name
        ```

          *[Image: Add Final LLM Node]*

  1. **Final Check**
        1. Click on the checklist to see if there's any missing spot. According to the notes, we need to connect Output node while fix the invalid variable issue.
        2. Connect Output node with LLM 2 node before it, remove its previous variable, then select text in LLM 2 as the output variable.

          *[Image: Select Output Variable]*

Now, you can write a test email with 3 different questions and check on the generated reply.

#### Mini Challenge

What else could Parameter Extractor find?

> **💡 Tip:**
>   Try exploring the parameter type in it.

#### Lesson 7: Enhance Workflows (Tools)

**Source:** https://docs.dify.ai/en/learn/tutorials/workflow-101/lesson-07

Our email assistant can now flip through our knowledge base. But what if a customer asks a beyond-knowledge-base question, like: What is in the latest Dify release?

If the knowledge base hasn't been updated yet, the workflow will be at a loss. To fix this, we need to equip it with a Live Search skill!

#### Tools

  *[Image: Tools]*

Tools are the superpower for your AI workflow.

The [Dify Marketplace](https://marketplace.dify.ai/) is like a supermarket of ready-made tools—searching Google, checking the weather, drawing images, or calculating complex math. You just install and plug them into your workflow with several clicks.

Now, let's continue to upgrade on current workflow.

##### Hands-On 1: Upgrade the Sub-process Area in Iteration

We are going to add a new logic to our assistant: Check the Knowledge Base first; if the answer isn't there, go search Google.

To focus on the new logic, let's keep only these nodes: **User input, Parameter Extractor, and Iteration**.

###### Step 1: Knowledge Query and the Judge

  1. **Enter the Iteration**
        1. Click to enter the sub-process area of the Iteration node.
        2. Keep Knowledge Retrieval node, and make sure the query variable is `{x} item`.
        3. Delete the previous LLM node.

  1. **Add the Judge (LLM Node)**
        Add an LLM node right after Knowledge Retrieval node. Its job is to decide if the Knowledge Base info can actually respond to the questions.

        * **For Context session**: Select the `Knowledge Retrieval / {x} result Array [Object]` from Knowledge Retrieval
        * **System Prompt**:

        ```plaintext wrap theme={null}
        Based on the `Context`, determine if the answer contains enough information to answer the questions. If the information is insufficient, you MUST reply with: "Information not found in knowledge base".
        ```

        * **User Message**:

        ```plaintext wrap theme={null}
        questions: Iteration/{x} item
        ```

          *[Image: LLM Settings]*

Here's what it looks like on the canvas.

  *[Image: Workflow Preview]*

###### Step 2: Setting the Crossroads

  1. **Add If/Else Node**
        After LLM node, let's add If/Else node. Set the rule: If LLM Output **Contains** **Information not found in knowledge base**.

        This means, when we can't respond with the information in knowledge base.

          *[Image: Add if/Else Node]*

  1. **Add Tool for Searching**
        Let's connect a search tool after the IF branch. This indicates that when the knowledge base cannot find relevant answer information, we use web search to find the answers.

        1. After the IF node, click plus(+) icon and select Tool.
        2. In the search box, type Google. Hover over Google, click Install on the right, and then click Install again in the pop-up window.

          *[Image: Install Tool]*

  1. **Install Google Search**
        Click Google Search in Google.

          *[Image: Install Google Search]*

  1. **Get Your API Key**
        Using Google Search for the first time requires authorization—it's like needing a Wi-Fi password.

          *[Image: Google Search Setup]*

        1. Click API Key Authorization Configuration, then click Get your SerpApi API key from SerpApi. Sign in to get your private API key.

           > **📝 Note:**
>              Your API Key is your passport to the outside world. Keep it safe and avoid sharing it with others.
>

             *[Image: API Key Authorization Configuration]*

        2. Copy and paste the API key in SerpApi API key. Click **Save**.
        3. Once the API key is successfully authorized, the settings panel shows up immediately. Head to Query string field, and select `Iteration/{x} item`.

          *[Image: Add Query String]*

  1. **Configure the Two Paths**
        Now, we need different ways to answer depending on which path we're looking at.

        **The Search Answer Path**

        Add a new LLM node to answer the question based on the search results. Connect it to the Google Search node.

        **System**:

        ```plaintext wrap theme={null}
        You are a Web Research Specialist. Based on Google Search, concisely answer the user's questions. Please do not mention the knowledge base in your response.
        ```

        **User Message**:

        ```plaintext wrap theme={null}
        results: GOOGLESEARCH/{x} text
        questions: Iteration/{x} item
        ```

          *[Image: Prompt for LLM 2]*

        **The Knowledge Searching Path**

        After the Else node, add a new LLM node to handle answers based on the knowledge base.

        **System**:

        ```plaintext wrap theme={null}
        You are a professional Dify Customer Service Manager. Strictly follow the `Context` to reply to questions.
        ```

        **User Message**:

        ```plaintext wrap theme={null}
        questions: Iteration/{x} item
        ```

          *[Image: Prompt for LLM 3]*

  1. **Combine the Information**
        1. In the sub-process (inside the Iteration box), add a Variable Aggregator node that connects both LLM 2 and LLM 3 at the very end.
        2. In the Variable Aggregator panel, select the variables `LLM 2/{x}text String` and `LLM 3/{x}text String` as the Assign Variables.

        In this way, we're merging the two possible answers into a single path.

          *[Image: Variable Aggregator Setup]*

This is how the current workflow looks.

  *[Image: Workflow Preview 2]*

###### Step 3: The Final Email Assembly

Now that our logic branches have finished processing, let's combine all the answers into a single, polished email.

  1. **Configure Iteration Output**
        Click on the Iteration node, and set `{x}Variable Aggregator/{x}output String` as the output variables.

          *[Image: Iteration Output]*

  1. **Connect the Summary LLM**
        After the Iteration node, connect a new LLM node to summarize all outputs. Feel free to use the prompt below.

        **System**:

        ```plaintext wrap theme={null}
        You are a professional Customer Service Manager. Summarize all the answers of the questions, and organize a clear and complete email reply for the customer.
        Do not include content where the knowledge base could not find relevant information.
        Signature: Anne.
        ```

        **User Message**:

        ```plaintext wrap theme={null}
        questions: Iteration/ {x} output
        customer: User Input / {x} customer_name
        ```

          *[Image: Prompt for LLM 4]*

  1. **Finalize with the Output Node**
        After the LLM node, add an End node. Set the output variable as `LLM 4/{x}text String`.

          *[Image: Output Setup]*

We have now completed the entire setup and configuration of the workflow. Our email assistant can now answer questions based on the Knowledge Base and use Google Search for supplementary answers when needed.

  *[Image: Final Workflow Preview]*

Try sending an email with question that definitely isn't in the knowledge base. Let's see if the AI successfully uses Google to find the related answers.

#### Mini Challenge

1. What are other conditions you can choose in If/Else node?
2. Browse marketplace to see if you can add another tool for this workflow?

#### Lesson 8: The Agent Node

**Source:** https://docs.dify.ai/en/learn/tutorials/workflow-101/lesson-08

Let's look back the upgrades we've made for our email assistants.

* Learned to Read: It can search a Knowledge Base
* Learned to Choose: It uses Conditions to make decisions
* Learned to Multitask: It handles multiple questions via Iteration
* Learned to Use Tools: It can access the Internet via Google Search

You might have noticed that our workflow is no longer just a straight line (Step 1 → Step 2 → Step 3).

It's becoming a system that analyzes, judges, and calls upon different abilities to solve problems. This advanced pattern is what we call an Agentic Workflow.

#### Agentic Workflow

An Agentic Workflow isn't just Input > Process > Output.

It involves thinking, planning, using tools, and adjusting based on results. It transforms the AI from a simple Executor (who just follows orders) into an intelligent Agent (who solves problems autonomously).

#### Agent Strategies

To make Agents work smarter, researchers designed Strategies—think of these as different modes of thinking that guide the Agent.

* **ReAct (Reason + Act)**

  The Think, then Do approach. The Agent thinks (What should I do?), acts (calls a tool), observes the result, and then thinks again. It loops until the job is done.
* **Plan-and-Execute**

  Make a full plan first, then do it step-by-step.
* **Chain of Thought (CoT)**

  Writing out the reasoning steps before giving an answer to improve accuracy.
* **Self-Correction**

  Checking its own work and fixing mistakes.
* **Memory**

  Equipping the Agent with short-term or long-term memory allows it to recall previous conversations or key details, enabling more coherent and personalized responses.

In Lesson 7, we manually built a Brain using Knowledge Retrieval -> LLM to Decide-> If/Else -> Search. It worked, but it was complicated to build.

Is there a simpler way? Yes, and here it is.

#### Agent Node

The Agent Node is a highly packaged intelligent unit.

You just need to set a Goal for it through instructions and provide the Tools it might need. Then, it can autonomously think, plan, select, and call tools internally (using the selected Agent Strategy, such as ReAct, and the model's Function Calling capability) until it completes your set goal.

In Dify, this greatly simplifies the process of building complex Agentic Workflows.

#### Hands-on 1: Build with Agent Node

Our goal is to replace that complex manual logic inside our Iteration loop with a single, smart Agent Node.

  1. **Clean up the Iteration**
        Go to the sub-process of the Iteration. Keep knowledge retrieval node, and delete other nodes in side it.

          *[Image: Iteration]*

  1. **Add the Agent Node**
        Add an Agent node right after the Knowledge Retrieval node.

          *[Image: Add Agent Node]*

  1. **Install Agent Strategy**
        Since we haven't used this before, we need to install a strategy from the Marketplace.

        Click the Agent node. In the right panel, look for Agent Strategy. Click Find more in Marketplace.

          *[Image: Search Agent Strategy]*

  1. **Pick an Agent Strategy**
        In the Marketplace, find Dify Agent Strategy and install it.

          *[Image: Choose Agent Strategy]*

  1. **Select ReAct**
        Back in your workflow (refresh if needed), select ReAct under Agent Strategy.

          *[Image: Select ReAct]*

        **Why ReAct here?**

        ReAct (Reason + Act) is a strategy that mimics human problem-solving using a Think → Do → Check loop.

        1. Reason: The Agent thinks, What should I do next? (e.g., Check the Knowledge Base).
        2. Act: It performs the action.
        3. Observe: It checks the result. If the answer isn't found, it repeats the cycle (e.g., Okay, I need to search Google).

        This thinking-while-doing approach is perfect for complex tasks where the next step depends on the previous result.

  1. **Choose a Model**
        ReAct is a thinking strategy, but to actually pull off the action part, AI needs the right "physical" skills which is called **Function Calling**. Select a model that supports Function Calling. Here, we choose gpt-5.

        **Why Function Calling?**

        One of the core capabilities of an Agent Node is to autonomously call tools. Function Calling is the key technology that allows the model to understand when and how to use the tools you provide (like Google Search).

        If the model doesn't support this feature, the Agent cannot effectively interact with tools and loses most of its autonomous decision-making capabilities.

          *[Image: Choose a Model]*

  1. **Add Tool**
        Click Agent node. Click plus(+) icon in tool list and select Google Search.

          *[Image: Add Tool]*

  1. **Add Instructions**
        We need to tell the Agent specifically what to do with the tools and context we are giving it. Use and paste the instructions into the Instruction field:

        ```plaintext wrap theme={null}
        Goal: Answer user questions about Dify products.

        Steps:
        1. I have provided a relevant internal knowledge base retrieval result. First, judge if this result can fully answer the user's questions.
        2. If the context clearly answers it, generate the final answer based on the context.
        3. If the answer is insufficient or irrelevant, use the Google Search tool to find the latest information and generate the answer based on search results.

        Requirement: Keep the final answer concise and accurate.
        ```

          *[Image: Add Instructions]*

  1. **Context and Query**
        Your configuration here is crucial for the Agent to see the data.

        * **Context**: Select `Knowledge Retrieval / (x) result Array[Object]` from the Knowledge Retrieval node (This passes the knowledge base content to the Agent).
        * **Query**: Select `Iteration/{x} item` from the Iteration node.

        **Why item instead of the original email_content?**

        We used the Parameter Extractor to extract a list of questions (`question_list`) from the `email_content`. The Iteration node is processing this list one by one, where item represents the specific question currently being handled.

        Using item as the query input allows Agent to focus on the current task, improving the accuracy of decision-making and actions.

          *[Image: Context and Query]*

  1. **Set Iteration Output**
        Click `Agent/{x}text String` as the output variables.

          *[Image: Set Iteration Output]*

> **✅ Check:**
>   🎉 The Iteration node is now upgraded.

Since the Iteration node generates a list of answers, we need to stitch them back together into one email.

#### Hands-on 2: Final Assembly

  1. **The Final Editor (LLM)**
        1. Add an LLM node after the Iteration node.
        2. Click on it and add prompt into the system. Feel free to check on the prompt below, or edit by yourself.

           ```plaintext wrap theme={null}
           Combine all answers for the original email.
           Write a complete, clear, and friendly reply to the customer.
           Signature: Anne
           ```
        3. Add user message to replace answers, email content and customer name with variables respectively. Here's how the LLM looks like right now.

             *[Image: Final LLM]*

  1. **Add Output Node**
        Set the output variable to the LLM's text and name it `email_reply`.

          *[Image: Add Output Node]*

Here comes the final workflow.

  *[Image: Final Workflow]*

Click **Test Run**. Ask a mix of questions. Watch how the Agent Node autonomously decides when to use the context and when to use Google search.

#### Mini Challenge

1. Could we use an Agent Node to replace the entire Iteration loop? How would you design the prompt to handle a list of questions all at once?
2. What other information could you feed into the Agent's Context field to help it make better decisions?

#### Lesson 9: Layout Designer (Template)

**Source:** https://docs.dify.ai/en/learn/tutorials/workflow-101/lesson-09

In Lesson 8, we successfully built a powerful Agent that can think and search. However, you might have noticed a tiny issue: even though we asked the final LLM to list the answers, sometimes the formatting can be a bit messy or inconsistent (e.g., mixing bullet points with paragraphs).

To fix this, we need a dedicated format assistant to organize the answers into a beautiful, standardized format before the final LLM writes the email.

#### Template

It takes the original data (like your list of answers), follows a strict design template/standards you provide, and generates a perfectly formatted block of text, ensuring consistency every single time.

#### Hands-On: Polish the Email Layout

  1. **Update the LLM Node**
        Since the Template node will be handling the greetings, we need to tell LLM to focus solely on the questions and answers. Copy and paste the prompt below or feel free to edit it.

        ```plaintext wrap theme={null}
        Combine all answers for the original email. Write a complete, clear, and friendly reply that only includes the summarized answers.

        IMPORTANT: Focus SOLELY on the answers. Do NOT include greetings (like "Hi Name"), do
        NOT write intro paragraphs (like "Thank you for reaching out"), and do NOT include
        signatures.
        ```

  1. **Add User Message**
        List the different variables respectively.

          *[Image: Edit LLM Node]*

  1. **Add Template Node**
        After LLM node, click to add Template node.

          *[Image: Add Template Node]*

  1. **Set up the Input Variables**
        Click the Template node, go to the Input Variables section, and add these two items:

        * `customer`: Choose `User Input / {x} customer_name String`
        * `body`: Choose `LLM / {x} text String`

            *[Image: Template Input Variable]*

  1. **Format with Jinja**
        **What is Jinja2?**

        In simple terms, Jinja2 is a tool that allows you to format variables (like your list of answers) into a text template exactly how you want. It uses simple symbols to mark where variables go and perform basic logic. With it, we can turn a raw list of data into a neat, standardized text block.

        Here, we can put together opening, signatures, and email body to make sure the email is professional and consistent every time.

        Copy and paste this exact layout into the Template code box:

        ```jinja theme={null}
        Hi {{ customer }},

        Thank you for reaching out to us, and we are more than happy to provide you with the information you are seeking.

        Here are the details regarding your specific questions:

        {{ body }}

        ---
        Thank you for reaching out to us!
        Best regards,
        Anne
        ```

Here's the final workflow.

  *[Image: Final Workflow]*

Click **Test Run**. Ask multiple questions in one email. Notice how your final output has a perfectly written custom intro, the LLM's beautifully summarized answers in the middle, and a standard, professional signature at the bottom.

#### Mini Challenge

1. How would you change the Jinja2 code to make a numbered list (1. Answer, 2. Answer) instead of bullet points?

   > **💡 Tip:**
>      Check the [Template Designer Documentation](https://jinja.palletsprojects.com/en/stable/templates/) or ask an LLM about it.
>

2. What else can Template node do?

#### Lesson 10: Publish and Monitor Your AI App

**Source:** https://docs.dify.ai/en/learn/tutorials/workflow-101/lesson-10

After building and tuning, your Email Assistant is now fully ready. It can read knowledge bases, use search tools, and generate beautifully formatted replies. But right now, it's still sitting inside your Dify Studio and only you can see it.

How do we share it with others? How do we know if it's working correctly when we aren't watching?

It's time for the final two critical steps: Publish and Monitor.

#### Publish Your Application

1. Move your mouse to the top right corner of the canvas and click the **Publish** button. You'll see other buttons light up.

   > **📝 Note:**
>      Whenever you make changes to your workflow, you must click **Publish → Update** to save them.
>
>      If you don't update, the live version will remain the old one.
>

     *[Image: Publish]*

2. Once published, the gray-out buttons turned clickable now.
   1. **Share Your App**

      Click **Run App**. Dify automatically generates a WebApp for you. This is a ready-to-use chat interface for your Email Assistant.

      You can send this URL to colleagues or friends. They don't need to log in to Dify to use the email assistant.

        *[Image: WebApp]*

   2. **Batch Run App**

      If you have 100 emails to reply, copying and pasting them one by one will drag you down.

      In Dify, all you need to do is to prepare a CSV file with the 100 emails. Upload it to Dify's Batch Run feature. Dify processes all 100 emails automatically and gives you back a spreadsheet with all the generated replies.

      Since we set specific variables (like `email_content`), your CSV must match that format. Dify provides a template you can download to make this easy.

        *[Image: Download Template]*

   3. **Others**
      * **Access API Reference**: If you know coding, you can get an API Key to integrate this workflow directly into your own website or mobile app
      * **Open in Explore**: Pin this app to your workspace sidebar for quick access next time
      * **Publish as a Tool**: Package your workflow as a tool so other Agents can use your Email Assistant

#### Monitor Your App

As the creator, you need to understand the status of this assistant. By monitoring and using logs, you can check the health, performance, and costs.

##### The Command Center: Monitoring

Click **Monitoring** on the left sidebar to see how your app is performing.

| Name                   | Explanation                                                                          |
| :--------------------- | :----------------------------------------------------------------------------------- |
| Total Messages         | How many times users interacted with the AI today. It shows how popular your app is. |
| Active Users           | The number of unique people engaging with the AI.                                    |
| Token Usage            | How much tokens the AI used. Watch for sudden spikes to control costs.               |
| Avg. User Interactions | Do the users ask follow-up questions?                                                |

##### The Magnifying Glass: Logs

Logs record the details of every single run: time, input, duration, and output. To access detailed records, click Logs in the left sidebar.

**Why Logs?**

* **Debugging**: User says *It doesn't work*? Check the logs to replay the *crime scene* and see exactly which node failed.
* **Performance**: See how long each node took. Find the blocker that is slowing things down.
* **Understand Users**: Read what users are actually asking. Use this real data to update your Knowledge Base or improve your Prompts.
* **Cost Control**: Check exactly how many tokens a specific run cost.

| Name                | Explanation                                                 |
| :------------------ | :---------------------------------------------------------- |
| Start Time          | The time when the workflow was triggered                    |
| Status              | Success or Failure.                                         |
| Run Time            | How long the whole process took.                            |
| Tokens              | The tokens consumed by this run.                            |
| End User or Account | The specific user ID or account that initiated the session. |
| Triggered By        | WebApp interface or called via API.                         |

You can click on each log entry to view more details. For example, you can identify frequently asked user questions and use them to timely update and modify your Knowledge Base.

Building AI app is a new starting point, and this is the core of **LLMOps** (Large language model operations).

1. **Observe**: Look at the Logs. What are users asking? Are they happy with the answers?
2. **Analyze**: Hallucination happens on certain questions or some tools run out often
3. **Optimize**: Go back to the Canvas. Edit the Prompt, add a document to the Knowledge Base, or tweak the workflow logic
4. **Publish**: Release the upgraded version

By repeating this cycle, your Email Assistant gets smarter and faster.

#### Thank You

**Thank you for your time and you're now a Dify builder with a new way of thinking**:

```plaintext wrap theme={null}
Break down the task → Choose Nodes and Tools → Connect them with the right logic → Monitor and upgrade
```

Now, feel free to open a template in Dify explore. Break it down, analyze it, or start building a workflow that solves a task in your daily work from the scratch.

May your workload get lighter and your imagination goes higher. Happy building with Dify.

### Introduction

#### 30-Minute Quick Start

*Dive into Dify through an example app*

**Source:** https://docs.dify.ai/en/quick-start

Dive into Dify through an example app

> **ℹ️ Info:**
>   This quick start uses **Dify Cloud**, the fastest way to get going: free to start, AI credits included, and nothing to install. Prefer to run Dify yourself? [Self-host Dify](https://docs.dify.ai/en/self-host/deploy/quick-start/docker-compose), then follow the same steps on your own instance.

This step-by-step tutorial will walk you through creating a multi-platform content generator from scratch.

Beyond basic LLM integration, you'll discover how to use powerful Dify nodes to orchestrate sophisticated AI applications faster with less effort.

By the end of this tutorial, you'll have a workflow that takes whatever content you throw at it (text, documents, or images), adds your preferred voice and tone, and spits out polished, platform-specific social media posts in your chosen language.

The complete workflow is shown below. Feel free to refer back to this as you build to stay on track and see how all the nodes work together.

  *[Image: Workflow Overview]*

#### Before You Start

  1. **Sign Up**
        Go to [cloud.dify.ai](https://cloud.dify.ai) and sign up for free.

        New accounts start on the Sandbox plan, which includes 200 AI Credits for calling models from providers like OpenAI, Anthropic, and Gemini.

        > **ℹ️ Info:**
>           The Sandbox AI Credits are a one-time allocation and don't renew monthly.
>

  1. **Set Up the Model Provider**
        Go to **Integrations** > **Model Provider** and install the OpenAI model provider. This tutorial uses `gpt-5.2` for the examples.

        No API key is required for the models covered by your AI Credits; they're ready to use once the provider is installed. You can also configure your own API key and use it instead.

  1. **Configure the Default Model**
        1. In the top-right corner of the **Model Provider** page, click **Default Models**.

        2. Set the **System Reasoning Model** to `gpt-5.2`. This becomes the default model in the workflow.

#### Step 1: Create a New Workflow

1. Go to **Studio**, then select **Create from Blank** > **Workflow**.

2. Name the workflow `Multi-platform content generator` and click **Create**. You'll automatically land on the workflow canvas to start building.

3. Select the User Input node to start our workflow.

#### Step 2: Orchestrate & Configure

> **📝 Note:**
>   Keep any unmentioned settings at their default values.

> **💡 Tip:**
>   Give nodes and variables clear, descriptive names to make them easier to identify and reference.

##### 1. Collect User Inputs: User Input Node

> **ℹ️ Info:**
>   First, we need to define what information to gather from users for running our content generator, such as the draft text, target platforms, desired tone, and any reference materials.
>
>   The User Input node is where we can easily set this up. Each input field we add here becomes a variable that all downstream nodes can reference and use.

Click the User Input node to open its configuration panel, then add the following input fields.

**Reference materials - text:**

  * Field type: `Paragraph`
  * Variable Name: `draft`
  * Label Name: `Draft`
  * Max length: `2048`
  * Required: `Yes`

**Reference materials - files:**

  * Field type: `File list`
  * Variable Name: `user_file`
  * Label Name: `Upload File (≤ 10)`
  * Support File Types: `Document`, `Image`
  * Upload File Types: `Both`
  * Max number of uploads: `10`
  * Required: `No`

**Voice and tone:**

  * Field type: `Paragraph`
  * Variable Name: `voice_and_tone`
  * Label Name: `Voice & Tone`
  * Max length: `2048`
  * Required: `No`

**Target platform:**

  * Field type: `Short Text`
  * Variable Name: `platform`
  * Label Name: `Target Platform (≤ 10)`
  * Max length: `256`
  * Required: `Yes`

**Language requirements:**

  * Field type: `Select`
  * Variable Name: `language`
  * Label Name: `Language`
  * Options:
    * `English`
    * `日本語`
    * `简体中文`
  * Required: `Yes`

  *[Image: User Input]*

##### 2. Identify Target Platforms: Parameter Extractor Node

> **ℹ️ Info:**
>   Since our platform field accepts free-form text input, users might type in various ways: `x and linkedIn`, `post on Twitter and LinkedIn`, or even `Twitter + LinkedIn please`.
>
>   However, we need a clean and structured list, like `["Twitter", "LinkedIn"]`, that downstream nodes can work with reliably.
>
>   This is the perfect job for the Parameter Extractor node. In our case, it uses the gpt-5.2 model to analyze users' natural language, recognize all these variations, and output a standardized array.

After the User Input node, add a Parameter Extractor node and configure it:

1. In the **Input Variable** field, select `User Input/platform`.

2. Add an extract parameter:

   * Name: `platform`

   * Type: `Array[String]`

   * Description: `The platform(s) for which the user wants to create tailored content.`

   * Required: `Yes`

3. In the **Instruction** field, paste the following to guide the LLM in parameter extraction:

   ```markdown INSTRUCTION theme={null}
   # TASK DESCRIPTION
   Parse platform names from input and output as a JSON array.

   ## PROCESSING RULES
   - Support multiple delimiters: commas, semicolons, spaces, line breaks, "and", "&", "|", etc.
   - Standardize common platform name variants (twitter/X→Twitter, insta→Instagram, etc.)
   - Remove duplicates and invalid entries
   - Preserve unknown but reasonable platform names
   - Preserve the original language of platform names

   ## OUTPUT REQUIREMENTS
   - Success: ["Platform1", "Platform2"]
   - No platforms found: [No platforms identified. Please enter a valid platform name.]

   ## EXAMPLES
   - Input: "twitter, linkedin" → ["Twitter", "LinkedIn"]
   - Input: "x and insta" → ["Twitter", "Instagram"]
   - Input: "invalid content" → [No platforms identified. Please enter a valid platform name.]
   ```

   > **✅ Check:**
>      Note that we've instructed the LLM to output a specific error message for invalid inputs, which will serve as the end trigger for our workflow in the next step.
>

  *[Image: Parameter Extractor]*

##### 3. Validate Platform Extraction Results: IF/ELSE Node

> **ℹ️ Info:**
>   What if a user enters an invalid platform name, like `ohhhhhh` or `BookFace`? We don't want to waste time and tokens generating useless content.
>
>   In such cases, we can use an IF/ELSE node to create a branch that stops the workflow early. We'll set a condition that checks for the error message from the Parameter Extractor node; if that message is detected, the workflow will route directly to an Output node and end.

  *[Image: IF Branch]*

1. After the Parameter Extractor node, add an IF/ELSE node.

2. On the IF/ELSE node's panel, define the **IF** condition:

   **IF** `Parameter Extractor/platform` **contains** `No platforms identified. Please enter a valid platform name.`

3. After the IF/ELSE node, add an Output node to the IF branch.

4. On the Output node's panel, set `Parameter Extractor/platform` as the output variable.

##### 4. Separate Uploaded Files by Type: List Operator Node

> **ℹ️ Info:**
>   Our users can upload both images and documents as reference materials, but these two types require different handling with `gpt-5.2`: images can be interpreted directly via its vision capability, while documents must first be converted to text before the model can process them.
>
>   To manage this, we'll use two List Operator nodes to filter and split the uploaded files into separate branches: one for images and one for documents.

  *[Image: List Operator]*

1. After the IF/ELSE node, add **two** parallel List Operator nodes to the ELSE branch.

2. Rename one node to `Image` and the other to `Document`.

3. Configure the Image node:
   1. Set `User Input/user_file` as the input variable.

   2. Enable **Filter Condition**: `{x}type` **in** `Image`.

4. Configure the Document node:
   1. Set `User Input/user_file` as the input variable.

   2. Enable **Filter Condition**: `{x}type` **in** `Doc`.

##### 5. Extract Text from Documents: Doc Extractor Node

> **ℹ️ Info:**
>   `gpt-5.2` cannot directly read uploaded documents like PDF or DOCX, so we must first convert them into plain text.
>
>   This is exactly what a Doc Extractor node does. It takes document files as input and outputs clean, usable text for the next steps.

  *[Image: Doc Extractor]*

1. After the Document node, add a Doc Extractor node.

2. On the Doc Extractor node's panel, set `Document/result` as the input variable.

##### 6. Integrate All Reference Materials: LLM Node

> **ℹ️ Info:**
>   When users provide multiple reference types (draft text, documents, and images) simultaneously, we need to consolidate them into a single, coherent summary.
>
>   An LLM node will handle this task by analyzing all the scattered pieces to create a comprehensive context that guides subsequent content generation.

  *[Image: Integrate Information]*

1. After the Doc Extractor node, add an LLM node.

2. Connect the Image node to this LLM node as well.

3. Click the LLM node to configure it:

   1. Rename it to `Integrate Info`.

   2. Enable **VISION** and set `Image/result` as the vision variable.

   3. In the system instruction field, paste the following:

      ```markdown wrap theme={null}
      # ROLE & TASK
      You are a content strategist. Analyze the provided draft and reference materials (if any), then create a comprehensive content foundation for multi-platform social media optimization.

      # ANALYSIS PRINCIPLES
      - Work exclusively with provided information—no external assumptions
      - Focus on extraction, synthesis, and strategic interpretation
      - Identify compelling and actionable elements
      - Prepare insights adaptable across different platforms

      # REQUIRED ANALYSIS
      Deliver structured analysis with:

      ## 1. CORE MESSAGE
      - Central theme, purpose, objective
      - Key value or benefit being communicated

      ## 2. ESSENTIAL CONTENT ELEMENTS
      - Primary topics, facts, statistics, data points
      - Notable quotes, testimonials, key statements
      - Features, benefits, characteristics mentioned
      - Dates, locations, contextual details

      ## 3. STRATEGIC INSIGHTS
      - What makes content compelling/unique
      - Emotional/rational appeals present
      - Credibility factors, proof points
      - Competitive advantages highlighted

      ## 4. ENGAGEMENT OPPORTUNITIES
      - Discussion points, questions emerging
      - Calls-to-action, next steps suggested
      - Interactive/participation opportunities
      - Trending themes touched upon

      ## 5. PLATFORM OPTIMIZATION FOUNDATION
      - High-impact: Quick, shareable formats
      - Professional: Business-focused discussions
      - Community: Interaction and sharing
      - Visual: Enhanced with strong visuals

      ## 6. SUPPORTING DETAILS
      - Metrics, numbers, quantifiable results
      - Direct quotes, testimonials
      - Technical details, specifications
      - Background context available
      ```

   4. Click **Add Message** to add a user message, then paste the following. Type `{` or `/` to replace `Doc Extractor/text` and `User Input/draft` with the corresponding variables from the list.

      ```markdown USER theme={null}
      Draft: User Input/draft
      Reference material: Doc Extractor/text
      ```

        *[Image: User Message]*

##### 7. Create Customized Content for Each Platform: Iteration Node

> **ℹ️ Info:**
>   Now that the integrated references and target platforms are ready, let's generate a tailored post for each platform using an Iteration node.
>
>   The node will loop through the list of platforms and run a sub-workflow for each: first analyze the specific platform's style guidelines and best practices, then generate optimized content based on all available information.

  *[Image: Iteration Node]*

1. After the Integrate Info node, add an Iteration node.

2. Inside the Iteration node, add an LLM node and configure it:

   1. Rename it to `Identify Style`.

   2. In the system instruction field, paste the following:

      ```markdown wrap theme={null}
      # ROLE & TASK
      You are a social media expert. Analyze the platform and provide content creation guidelines.

      # ANALYSIS REQUIRED
      For the given platform, provide:

      ## 1. PLATFORM PROFILE
      - Platform type and category
      - Target audience characteristics

      ## 2. CONTENT GUIDELINES
      - Optimal content length (characters/words)
      - Recommended tone (professional/casual/conversational)
      - Formatting best practices (line breaks, emojis, etc.)

      ## 3. ENGAGEMENT STRATEGY
      - Hashtag recommendations (quantity and style)
      - Call-to-action best practices
      - Algorithm optimization tips

      ## 4. TECHNICAL SPECS
      - Character/word limits
      - Visual content requirements
      - Special formatting needs

      ## 5. PLATFORM-SPECIFIC NOTES
      - Unique features or recent changes
      - Industry-specific considerations
      - Community engagement approaches

      # OUTPUT REQUIREMENTS
      - For recognized platforms: Provide specific guidelines
      - For unknown platforms: Base recommendations on similar platforms
      - Focus on actionable, practical advice
      - Be concise but comprehensive
      ```

   3. Click **Add Message** to add a user message, then paste the following. Type `{` or `/` to replace `Current Iteration/item` with the corresponding variable from the list.

      ```markdown USER theme={null}
      Platform: Current Iteration/item
      ```

3. After the Identify Style node, add another LLM node and configure it:

   1. Rename it to `Create Content`.

   2. In the system instruction field, paste the following:

      ```markdown wrap theme={null}
      # ROLE & TASK
      You are an expert social media content creator. Generate publication-ready content that matches platform guidelines, incorporates source information, and follows specified voice/tone and language requirements.

      # LANGUAGE REQUIREMENT
      - Generate ALL content exclusively in the target language specified in the user message. You MUST write the entire post in that language, regardless of the language of any source materials.
      - No mixing of languages whatsoever
      - Adapt platform terminology to the target language

      # CONTENT REQUIREMENTS
      - Follow platform guidelines exactly (format, length, tone, hashtags)
      - Integrate source information effectively (key messages, data, value props)
      - Apply voice & tone consistently (if provided)
      - Optimize for platform-specific engagement
      - Ensure cultural appropriateness for the specified language

      # OUTPUT FORMAT
      - Generate ONLY the final social media post content. No explanations or meta-commentary. Content must be immediately copy-paste ready.
      - Maximum heading level: ## (H2) - never use # (H1)
      - No horizontal dividers: avoid ---

      # QUALITY CHECKLIST
      ✅ Platform guidelines followed
      ✅ Source information integrated
      ✅ Voice/tone consistent (when provided)
      ✅ Language consistency maintained
      ✅ Engagement optimized
      ✅ Publication ready
      ```

   3. Click **Add Message** to add a user message, then paste the following. Type `{` or `/` to replace all inputs with the corresponding variable from the list.

      ```markdown USER theme={null}
      Platform Name: Current Iteration/item
      Target Language: User Input/language
      Platform Guidelines: Identify Style/text
      Source Information: Integrate Info/text
      Voice & Tone: User Input/voice_and_tone
      ```

   4. Enable structured output.

      > **ℹ️ Info:**
>         This allows us to extract specific pieces of information from the LLM's response in a more reliable way, which is crucial for the next step where we format the final output.
>

        *[Image: Structured Output]*

      1. Next to **Output Variables**, toggle **Structured** on. The `structured_output` variable will appear below. Click **Configure**.

      2. In the pop-up schema editor, click **Import From JSON** in the top-right corner, and paste the following:

         ```json theme={null}
         {
           "platform_name": "string",
           "post_content": "string"
         }
         ```

           *[Image: Import from JSON]*

4. Click the Iteration node to configure it:

   1. Set `Parameter Extractor/platform` as the input variable.

   2. Set `Create Content/structured_output` as the output variable.

   3. Enable **Parallel Mode** and set the maximum parallelism to `10`.

      > **✅ Check:**
>         This is why we included `(≤10)` in the label name for the target platform field back in the User Input node.
>

     *[Image: Iteration Configuration]*

##### 8. Format the Final Output: Template Node

> **ℹ️ Info:**
>   The Iteration node generates a post for each platform, but its output is a raw array of data (e.g., `[{"platform_name": "Twitter", "post_content": "..."}]`) that isn't very readable. We need to present the results in a clearer format.
>
>   That's where the Template node comes in. It lets us format this raw data into well-organized text using [Jinja2](https://jinja.palletsprojects.com/en/stable/) templating, ensuring the final output is user-friendly and easy to read.

  *[Image: Template Node]*

1. After the Iteration node, add a Template node.

2. On the Template node's panel, set `Iteration/output` as the input variable and name it `output`.

3. Paste the following Jinja2 code:

   ```
   {% for item in output %}
   # 📱 {{ item.platform_name }}
   {{ item.post_content }}

   {% endfor %}
   ```

   * `{% for item in output %}` / `{% endfor %}`: Loops through each platform-content pair in the input array.
   * `{{ item.platform_name }}`: Displays the platform name as an H1 heading with a phone emoji.
   * `{{ item.post_content }}`: Displays the generated content for that platform.
   * The blank line between `{{ item.post_content }}` and `{% endfor %}` adds spacing between platforms in the final output.

> **💡 Tip:**
>   While LLMs can handle output formatting as well, their outputs can be inconsistent and unpredictable. For rule-based formatting that requires no reasoning, the Template node gets things done in a more stable and reliable way at zero token cost.
>
>   LLMs are incredibly powerful, but knowing when to use the right tool is key to building more reliable and cost-effective AI applications.

##### 9. Return the Results to Users: Output Node

1. After the Template node, add an Output node.
2. On the Output node's panel, set the `Template/output` as the output variable.

#### Step 3: Test

Your workflow is now complete! Let's test it out.

1. Make sure your Checklist is clear.

     *[Image: Check Checklist]*

2. Check your workflow against the reference diagram provided at the beginning to ensure all nodes and connections match.

3. Click **Test Run** in the top-right corner, fill in the input fields, then click **Start Run**.

   If you're not sure what to enter, try these sample inputs:

   * **Draft**: `We just launched a new AI writing assistant that helps teams create content 10x faster.`

   * **Upload File**: Leave empty

   * **Voice & Tone**: `Friendly and enthusiastic, but professional`

   * **Target Platform**: `Twitter and LinkedIn`

   * **Language**: `English`

A successful run produces a formatted output with a separate post for each platform, like this:

  *[Image: Test Output]*

> **📝 Note:**
>   Your results may vary depending on the model you're using. Higher-capability models generally produce better output quality.

> **💡 Tip:**
>   To test how a node reacts to different inputs from previous nodes, you don't need to re-run the entire workflow. Just click **View cached variables** at the bottom of the canvas, find the variable you want to change, and edit its value.

If you encounter any errors, check the **Last Run** logs of the corresponding node to identify the exact cause of the problem.

#### Step 4: Publish & Share

Once the workflow runs as expected and you're happy with the results, click **Publish** > **Publish Update** to make it live and shareable.

> **⚠️ Warning:**
>   If you make any changes later, always remember to publish again so the updates take effect.

---
