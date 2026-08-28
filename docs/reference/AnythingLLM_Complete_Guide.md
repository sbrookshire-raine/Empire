# AnythingLLM Documentation — Complete Guide

> **NotebookLM Ingestion Note:** This single Markdown file consolidates the entire official AnythingLLM documentation into one clean, structured document optimized for upload as a NotebookLM source — ideal for building a learning plan, generating study guides, or asking questions across the full doc set.

- **Source:** https://docs.useanything.com
- **Pages included:** 203
- **Generated on:** 2026-07-18

## Table of Contents

- [Getting Started](#getting-started)
  - [Home](#home)
  - [What is AnythingLLM](#what-is-anythingllm)
- [Desktop App Installation](#desktop-app-installation)
  - [Desktop Installation Overview](#desktop-installation-overview)
  - [Debug](#debug)
  - [Linux Installation](#linux-installation)
  - [MacOS Installation](#macos-installation)
  - [Privacy Policy](#privacy-policy)
  - [General Desktop Information](#general-desktop-information)
  - [System Requirements](#system-requirements)
  - [Terms of Use](#terms-of-use)
  - [Uninstall](#uninstall)
  - [Update](#update)
  - [Windows Installation](#windows-installation)
- [Docker Installation](#docker-installation)
  - [Installation Overview](#installation-overview)
  - [Available Images](#available-images)
  - [Cloud Docker Installation](#cloud-docker-installation)
  - [Debug](#debug)
  - [Local Docker Installation](#local-docker-installation)
  - [A note about localhost](#a-note-about-localhost)
  - [Quickstart](#quickstart)
  - [System Requirements](#system-requirements)
- [LLM Configuration](#llm-configuration)
  - [Overview](#overview)
  - [Anthropic LLM](#anthropic-llm)
  - [APIpie](#apipie)
  - [AWS Bedrock LLM](#aws-bedrock-llm)
  - [Azure OpenAI LLM](#azure-openai-llm)
  - [Cohere LLM](#cohere-llm)
  - [Google Gemini LLM](#google-gemini-llm)
  - [Groq LLM](#groq-llm)
  - [HuggingFace LLM](#huggingface-llm)
  - [Mistral AI LLM](#mistral-ai-llm)
  - [OpenAI LLM](#openai-llm)
  - [OpenAI (Generic) LLM](#openai-generic-llm)
  - [OpenRouter LLM](#openrouter-llm)
  - [Perplexity AI LLM](#perplexity-ai-llm)
  - [Together AI LLM](#together-ai-llm)
  - [TrueFoundry AI gateway](#truefoundry-ai-gateway)
  - [AnythingLLM Default LLM](#anythingllm-default-llm)
  - [KobaldCPP LLM](#kobaldcpp-llm)
  - [LMStudio LLM](#lmstudio-llm)
  - [Local AI LLM](#local-ai-llm)
  - [Ollama LLM](#ollama-llm)
  - [oMLX LLM](#omlx-llm)
- [Embedding Model Configuration](#embedding-model-configuration)
  - [Overview](#overview)
  - [Azure OpenAI Embedder](#azure-openai-embedder)
  - [Cohere Embedder](#cohere-embedder)
  - [OpenAI Embedder](#openai-embedder)
  - [AnythingLLM Default Embedder](#anythingllm-default-embedder)
  - [LM Studio Embedder](#lm-studio-embedder)
  - [Local AI Embedder](#local-ai-embedder)
  - [Ollama Embedder](#ollama-embedder)
- [Vector Database Configuration](#vector-database-configuration)
  - [Vector Databases](#vector-databases)
  - [AstraDB Vector Database](#astradb-vector-database)
  - [Pinecone Vector Database](#pinecone-vector-database)
  - [QDrant Vector Database](#qdrant-vector-database)
  - [Weaviate Vector Database](#weaviate-vector-database)
  - [Zilliz Vector Database](#zilliz-vector-database)
  - [Chroma Vector Database](#chroma-vector-database)
  - [Lance DB Vector Database](#lance-db-vector-database)
  - [Milvus Vector Database](#milvus-vector-database)
- [Transcription Model Configuration](#transcription-model-configuration)
  - [Transcription Models](#transcription-models)
  - [OpenAI Transcription Model](#openai-transcription-model)
  - [AnythingLLM Default Transcription Model](#anythingllm-default-transcription-model)
- [Core Configuration](#core-configuration)
  - [Configuration](#configuration)
- [Features](#features)
  - [Clarifying Questions](#clarifying-questions)
  - [AI Agents](#ai-agents)
  - [All Features](#all-features)
  - [API Access & Keys](#api-access-keys)
  - [Authenticated Scraping](#authenticated-scraping)
  - [Workspace Chat Logs](#workspace-chat-logs)
  - [Chat Modes](#chat-modes)
  - [Embedded Chat Widgets](#embedded-chat-widgets)
  - [Appearance Customization](#appearance-customization)
  - [Embedding Models](#embedding-models)
  - [Event Logs](#event-logs)
  - [Large Language Models](#large-language-models)
  - [Memories & Personalization](#memories-personalization)
  - [Privacy & Data](#privacy-data)
  - [Security and Access](#security-and-access)
  - [System Prompt Variables](#system-prompt-variables)
  - [Transcription Models](#transcription-models)
  - [Vector Databases](#vector-databases)
- [Chatting with Documents (RAG)](#chatting-with-documents-rag)
  - [Using Documents in AnythingLLM](#using-documents-in-anythingllm)
  - [Why does the LLM not use my documents](#why-does-the-llm-not-use-my-documents)
- [Chat UI](#chat-ui)
  - [ChatUI Walkthrough](#chatui-walkthrough)
- [AI Agents - Overview & Setup](#ai-agents-overview-setup)
  - [AI Agents](#ai-agents)
  - [AI Agent Setup](#ai-agent-setup)
  - [Intelligent Tool Selection](#intelligent-tool-selection)
  - [Why is my AI Agent not using tools!](#why-is-my-ai-agent-not-using-tools)
- [AI Agents - Usage Guides](#ai-agents-usage-guides)
  - [AI Agent Usage](#ai-agent-usage)
  - [Chart Generation](#chart-generation)
  - [Create Scheduled Jobs](#create-scheduled-jobs)
  - [Document Generation Agent](#document-generation-agent)
  - [File System Agent](#file-system-agent)
  - [Gmail Agent](#gmail-agent)
  - [Google Calendar Agent](#google-calendar-agent)
  - [List Documents](#list-documents)
  - [Outlook Agent](#outlook-agent)
  - [RAG Search](#rag-search)
  - [Save Files](#save-files)
  - [SQL Agent](#sql-agent)
  - [Summarize Documents](#summarize-documents)
  - [Web Browsing](#web-browsing)
  - [Web Scraping](#web-scraping)
- [AI Agents - Custom Skill Development](#ai-agents-custom-skill-development)
  - [Introduction to custom agent skills](#introduction-to-custom-agent-skills)
  - [Custom Agent Skill Developer Guide](#custom-agent-skill-developer-guide)
  - [handler.js reference](#handlerjs-reference)
  - [plugin.json reference](#pluginjson-reference)
- [Agent Flows (No-Code Automation)](#agent-flows-no-code-automation)
  - [Getting Started with Flows](#getting-started-with-flows)
  - [What is an Agent Flow?](#what-is-an-agent-flow)
  - [API Call](#api-call)
  - [LLM Instruction](#llm-instruction)
  - [Read File](#read-file)
  - [Web Scraper](#web-scraper)
  - [Write File](#write-file)
  - [Debugging flows](#debugging-flows)
  - [Tutorial: HackerNews Flow](#tutorial-hackernews-flow)
- [Scheduled Jobs](#scheduled-jobs)
  - [Creating Your First Job](#creating-your-first-job)
  - [Scheduled Jobs](#scheduled-jobs)
  - [Configuration & Limits](#configuration-limits)
  - [Scheduling & The Cron Builder](#scheduling-the-cron-builder)
  - [Viewing Runs & Results](#viewing-runs-results)
- [Model Router](#model-router)
  - [What is the Model Router?](#what-is-the-model-router)
  - [Setting up a Model Router](#setting-up-a-model-router)
- [MCP Compatibility](#mcp-compatibility)
  - [MCP Compatibility in AnythingLLM](#mcp-compatibility-in-anythingllm)
  - [MCP on AnythingLLM Desktop](#mcp-on-anythingllm-desktop)
  - [MCP on AnythingLLM Docker](#mcp-on-anythingllm-docker)
- [Browser Extension](#browser-extension)
  - [AnythingLLM Browser Extension](#anythingllm-browser-extension)
- [Messaging Channels](#messaging-channels)
  - [Telegram Bot](#telegram-bot)
- [Desktop Assistant](#desktop-assistant)
  - [AnythingLLM's Desktop Assistant](#anythingllms-desktop-assistant)
  - [Features](#features)
- [Meeting Assistant](#meeting-assistant)
  - [Introduction](#introduction)
  - [Features](#features)
- [Mobile App](#mobile-app)
  - [Introduction](#introduction)
  - [Privacy Policy](#privacy-policy)
  - [Terms of Use](#terms-of-use)
- [Community Hub](#community-hub)
  - [What is the Community Hub?](#what-is-the-community-hub)
  - [FAQ](#faq)
  - [Importing from the AnythingLLM Community Hub](#importing-from-the-anythingllm-community-hub)
  - [Uploading to the AnythingLLM Community Hub](#uploading-to-the-anythingllm-community-hub)
- [AnythingLLM Cloud](#anythingllm-cloud)
  - [AnythingLLM Cloud](#anythingllm-cloud)
  - [502 Error on AnythingLLM Hosted](#502-error-on-anythingllm-hosted)
  - [Limitations](#limitations)
  - [AnythingLLM Cloud Privacy Policy](#anythingllm-cloud-privacy-policy)
  - [AnythingLLM Cloud Terms & Conditions](#anythingllm-cloud-terms-conditions)
- [AnythingLLM Pro](#anythingllm-pro)
  - [Getting Your Pro Key](#getting-your-pro-key)
  - [Why AnythingLLM Pro?](#why-anythingllm-pro)
  - [Magic Beacon](#magic-beacon)
  - [Magic Echo](#magic-echo)
  - [Magic Tab](#magic-tab)
  - [Managing Your Subscription](#managing-your-subscription)
- [Beta Preview Features](#beta-preview-features)
  - [AnythingLLM Beta Previews](#anythingllm-beta-previews)
  - [AI Computer use](#ai-computer-use)
  - [Automatic document sync](#automatic-document-sync)
  - [Enable feature previews](#enable-feature-previews)
- [Troubleshooting](#troubleshooting)
  - ['Fetch failed' error on embed](#fetch-failed-error-on-embed)
  - [Import an LLM into AnythingLLM](#import-an-llm-into-anythingllm)
  - [Manual QNN Model Download](#manual-qnn-model-download)
  - [General Help](#general-help)
- [Project Info](#project-info)
  - [Contribute](#contribute)
  - [Roadmap](#roadmap)
  - [Support](#support)
- [Changelog](#changelog)
  - [Desktop Changelog Overview](#desktop-changelog-overview)
  - [v1.10.0](#v1100)
  - [v1.11.0](#v1110)
  - [v1.11.1](#v1111)
  - [v1.11.2](#v1112)
  - [v1.12.0](#v1120)
  - [v1.12.1](#v1121)
  - [v1.13.0](#v1130)
  - [v1.14.0](#v1140)
  - [v1.14.1](#v1141)
  - [v1.14.2](#v1142)
  - [v1.15.0](#v1150)
  - [v1.6.0](#v160)
  - [v1.6.1](#v161)
  - [v1.6.10](#v1610)
  - [v1.6.11](#v1611)
  - [v1.6.2](#v162)
  - [v1.6.3](#v163)
  - [v1.6.4](#v164)
  - [v1.6.5](#v165)
  - [v1.6.6](#v166)
  - [v1.6.7](#v167)
  - [v1.6.8](#v168)
  - [v1.6.9](#v169)
  - [v1.7.0](#v170)
  - [v1.7.1](#v171)
  - [v1.7.2](#v172)
  - [v1.7.3](#v173)
  - [v1.7.4](#v174)
  - [v1.7.5](#v175)
  - [v1.7.6](#v176)
  - [v1.7.7](#v177)
  - [v1.7.8](#v178)
  - [v1.8.0](#v180)
  - [v1.8.1](#v181)
  - [v1.8.2](#v182)
  - [v1.8.3](#v183)
  - [v1.8.4](#v184)
  - [v1.8.5](#v185)
  - [v1.9.0](#v190)
  - [v1.9.1](#v191)

---

## Getting Started

### Home

*Learn about AnythingLLM's features and how to use them*

**Source:** https://docs.useanything.com/

### AnythingLLM Documentation

Learn about AnythingLLM's features and how to use them

  

[![AnythingLLM Get Started](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Fheader-image.png&w=3840&q=100)Get Started→](https://docs.useanything.com/introduction)[![AnythingLLM Installation](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fheader-image.png&w=3840&q=100)Installation→](https://docs.useanything.com/installation-desktop/overview)[![AnythingLLM Features](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fheader-image.png&w=3840&q=100)Features→](https://docs.useanything.com/features/all-features)[![AnythingLLM Cloud](https://docs.useanything.com/_next/image?url=%2Fimages%2Fcloud%2Fheader-image.png&w=3840&q=100)AnythingLLM Cloud→](https://docs.useanything.com/cloud/overview)[![AnythingLLM Roadmap](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Froadmap%2Fheader-image.png&w=3840&q=100)Roadmap→](https://docs.useanything.com/roadmap)[![AnythingLLM Changelog](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog→](https://docs.useanything.com/changelog/overview)

### What is AnythingLLM

*AnythingLLM is the easiest to use, all-in-one AI application that can do RAG, AI Agents, and much more with no code or infrastructure headaches.*

**Source:** https://docs.useanything.com/introduction

![AnythingLLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Fintroduction%2Fheader-image.png&w=3840&q=100)

AnythingLLM is the easiest to use, **all-in-one** AI application that can do RAG, AI Agents, and much more with no code or infrastructure headaches.

AnythingLLM is built by [Mintplex Labs, Inc](https://github.com/Mintplex-Labs) - founded by [Timothy Carambat](https://twitter.com/tcarambat) and went through [YCombinator Summer 2022](https://www.ycombinator.com/companies/mintplex-labs).

AnythingLLM is **not a one-person project**. The Mintplex Labs team also includes:

- Sean Hatfield (Engineer)
- Marcello Fitton (Engineer)
- Tiff Tang (Designer)
- Our community of volunteer contributors
- [You?](https://www.ycombinator.com/companies/mintplex-labs/jobs)

  

### Why use AnythingLLM?

You want a **zero-setup**, **private**, and all-in-one AI application for local LLMs, RAG, and AI Agents all in one place without painful developer-required set up.

[Learn more about AnythingLLM Desktop →](https://docs.useanything.com/installation-desktop/overview)

*or*

You need a **fully-customizable**, **private**, and all-in-one AI app for your *business or organization* that is basically a full ChatGPT with permissioning but with any LLM, embedding model, or vector database.

[Learn more about AnythingLLM for Docker →](https://docs.useanything.com/installation-docker/local-docker)

If either of these things excite you - you will love watching the video below.

  

[Embedded video/content](https://www.youtube.com/embed/-Rs8-M-xBFI?si=IdsgmFwdJuouqeMd)


---

## Desktop App Installation

### Desktop Installation Overview

*AnythingLLM desktop is the easiest way to use AnythingLLM for most people.*

**Source:** https://docs.useanything.com/installation-desktop/overview

![AnythingLLM Installation](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fheader-image.png&w=3840&q=100)

#### Installation Overview

AnythingLLM Desktop is a "**single-player**" application you can install on any Mac, Windows, or Linux operating system and get local LLMs, RAG, and Agents with little to zero configuration and full privacy.

#### Docker vs Desktop Version

AnythingLLM offers two main ways to use AnythingLLM. There are some distinct differences in functionality between each offering. Both are open source.

##### You want AnythingLLM Desktop if...

- You want a one-click installable app to use local LLMs, RAG, and Agents locally
- You do not need multi-user support
- Everything needs to stay only on your device
- You do not need to "publish" anything to the public internet. Eg: Chat widget for website

##### You want AnythingLLM Docker if...

- You need an easy setup, but server-based service for AnythingLLM to use local LLMs, RAG, and Agents locally
- You want to run an AnythingLLM instance that many people can use at the same time
- You want to be able to share information with our users on your instance you invite
- You need admin and rule-based access for workspaces and documents.
- You will publish chat widgets to the public internet
- You want to access AnythingLLM from the browser

The below table is a non-exhaustive list of features supported between platforms.

| Feature | Available on Desktop | Available on Docker |
| --- | --- | --- |
| Multi-user support | ❌ | ✅ |
| Embeddable chat widgets | ❌ | ✅ |
| One-click install | ✅ | ❌ |
| Private documents | ✅ | ✅ |
| Connect to any vector database | ✅ | ✅ |
| Use any LLM | ✅ | ✅ |
| Built-in embedding provider | ✅ | ✅ |
| Built-in LLM provider | ✅ | ❌ |
| White-labeling | ❌ | ✅ |
| Chat logs | ✅ | ✅ |
| Agent support | ✅ | ✅ |
| Agent skills | ✅ | ✅ |
| Third-party data connectors | ✅ | ✅ |
| Password protection | ❌ | ✅ |
| Invite new users to instance | ❌ | ✅ |
| Text splitting configuration | ✅ | ✅ |
| Whisper model support | ✅ | ✅ |
| Full developer API | ✅ | ✅ |
| User management | ❌ | ✅ |
| Workspace access management | ❌ | ✅ |
| Website scraping | ✅ | ✅ |

> **Tip:**
>
> **Tip:** AnythingLLM Desktop is the easiest way to use AnythingLLM.

  

#### Quick Links

[![AnythingLLM System Requirements](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fsystem-requirements.png&w=3840&q=100)System Requirements→](https://docs.useanything.com/installation-desktop/system-requirements)[![AnythingLLM MacOS Install](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fmacos%2Fheader-image.png&w=3840&q=100)MacOS Install→](https://docs.useanything.com/installation-desktop/macos)[![AnythingLLM Windows Install](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fwindows%2Fheader-image.png&w=3840&q=100)Windows Install→](https://docs.useanything.com/installation-desktop/windows)[![AnythingLLM Linux Install](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Flinux%2Fheader-image.png&w=3840&q=100)Linux Install→](https://docs.useanything.com/installation-desktop/linux)[![AnythingLLM Local Docker Install](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Flocal-docker%2Fheader-image.png&w=3840&q=100)Local Docker Install→](https://docs.useanything.com/installation-docker/local-docker)[![AnythingLLM Cloud Docker Install](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fcloud-docker%2Fheader-image.png&w=3840&q=100)Cloud Docker Install→](https://docs.useanything.com/installation-docker/cloud-docker)

### Debug

*Learn how to run AnythingLLM in debug mode*

**Source:** https://docs.useanything.com/installation-desktop/debug

![AnythingLLM Debug Mode](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fdebug.png&w=3840&q=100)

#### General Debugging

If you are having issues with AnythingLLM, the first thing you should do is check the logs. You can find the logs in the `logs` folder of your AnythingLLM storage - which you can find [on your computer using this guide.](https://docs.useanything.com/installation-desktop/storage#where-is-my-data-located)

#### AnythingLLM Debug mode on MacOS

To run the AnythingLLM Application in debug mode (if you are getting errors) you can open a Terminal and navigate to `~/Applications/AnythingLLM/Content/MacOs` where you can then run the executable and see all application logs while running AnythingLLM.

#### AnythingLLM Debug mode on Windows

To run the AnythingLLM Application in debug mode (if you are getting errors) you can open a CMD or Powershell window and run the path to the AnythingLLM executable. Typically this is in `C:\Users\usr\AppData\Local\Programs\anythingllm-desktop\AnythingLLMDesktop.exe`.
This will print all logs to the powershell window while running and should display a verbose error once encountered that is critical for debugging.

#### AnythingLLM Debug mode on Linux

To run the AnythingLLM Application in debug mode (if you are getting errors) you can open a Terminal and navigate to `~/.config/anythingllm-desktop/AnythingLLMDesktop.AppImage` where you can then run the executable and see all AppImage logs while running AnythingLLM.

### Linux Installation

*Linux Installation guide for AnythingLLM*

**Source:** https://docs.useanything.com/installation-desktop/linux

![AnythingLLM Installation](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Flinux%2Fheader-image.png&w=3840&q=100)

#### Install using the installer script

> **Note:**
>
> **Heads up!**
>
> ➤ The AnythingLLM Desktop app is packaged as an AppImage and is available for **x64** and **arm64** architectures.
>
> ➤ The Linux Arm64 AppImage is currently only available for AnythingLLM Desktop **1.9.0** and higher.
>
> ➤ Please open a [Github Issue](https://github.com/Mintplex-Labs/anything-llm/issues) if you have installation or bootup troubles.

First, open a terminal on your Linux machine and run this command.

```
### Download the installer script to wherever you want to run it from
curl -fsSL https://cdn.anythingllm.com/latest/installer.sh -o installer.sh
 
### Make the script executable
chmod +x installer.sh
 
### Run the script
./installer.sh
```

> **Note:**
>
> By default, the installer will download the appropriate architecture of AnythingLLM Desktop for your system into the `$HOME` directory. If you wish to install to a different location, set the `ANYTHING_LLM_INSTALL_DIR` environment variable before running the installer. The target path must be writable by the current user — the installer will not run as root.
>
> You can also re-run the installer script to update the app to the latest version as new versions are released.

This will download the latest version of AnythingLLM's AppImage as well as **ask to create** the Ubuntu `apparmor` rule to allow the app to run
without any additional configuration. **You need to create an `apparmor` rule to allow the app to run or else you will run into SUID issues during bootup.**

Lastly, it will create a simple `.desktop` file so the app can be launched from the desktop and pinned to the launcher.

You can start the app via the UI or from the command line at any time by running `./AnythingLLMDesktop.AppImage`. This will boot the app with full logging.

#### Uninstalling

To uninstall AnythingLLM, you can run the following commands:

```
### Remove the installer script
rm installer.sh
 
### Remove the AppImage
rm AnythingLLMDesktop.AppImage
 
### Remove the .desktop file
rm ~/.local/share/applications/anythingllmdesktop.desktop
 
### Remove the apparmor rules
sudo rm /etc/apparmor.d/anythingllmdesktop
 
### Remove the app data fully
rm -rf ~/.config/anythingllm-desktop
```

### MacOS Installation

*MacOS Installation guide for AnythingLLM*

**Source:** https://docs.useanything.com/installation-desktop/macos

![AnythingLLM Installation](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fmacos%2Fheader-image.png&w=3840&q=100)

There are **two** ways to install AnythingLLM on MacOS

**[1. Install using the Installation `.dmg` file](https://docs.useanything.com/installation-desktop/macos#install-using-the-installation-file)**

**[2. Install using Homebrew](https://docs.useanything.com/installation-desktop/macos#install-using-homebrew)**

#### Install using the installation file

> **Warning:**
>
> **Install the right dmg!**
>
> ➤ Make sure you downloaded the correct `dmg` for your device! We support both types of chips found in MacOS devices.
>
> ➤ Apple Silicon devices (M1/M2/M3) - `AnythingLLMDesktop-AppleSilicon.dmg`
>
> ➤ Apple (Intel) - `AnythingLLMDesktop.dmg`

> **Tip:**
>
> **PERFORMANCE** ➤➤ Apple M-Series chips run local LLM inferencing
> **considerably** faster than Intel-based Mac.

##### Downloading the installation file

Here is the download links for the latest version of Anything LLM MacOS.

[MacOS (Intel-based CPU)→](https://cdn.anythingllm.com/latest/AnythingLLMDesktop.dmg)[MacOS (M-Series CPU)→](https://cdn.anythingllm.com/latest/AnythingLLMDesktop-Silicon.dmg)

Your internet browser may need you to verify you want to download and run the AnythingLLM Desktop app since it may be marked as "untrusted" depending on your browser security settings.

Click "**Keep**" when downloading to allow the file to download.

![AnythingLLM Mac Install Browser Warning](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fmacos%2Fbrowser-warning.png&w=3840&q=100)

##### Installing the application

After downloading the `.dmg` file from the link in the invitation email, you will want to double-click on the resulting installed file.

Once the dmg opens, you can drag the AnythingLLM logo into `Applications`

![AnythingLLM Mac Installation](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fmacos%2Finstall.png&w=3840&q=100)

Once installed, you will find AnythingLLM in your Applications folder as well as you can use `cmd + spacebar` and type in AnythingLLM to run.

---

#### Install using Homebrew

Make sure you have installed [Homebrew](https://brew.sh/) on your machine, if you don't have Homebrew installed then you can install it by following this [guide](https://mac.install.guide/homebrew/3)

Run the following command on your terminal

```
 brew install --cask anythingllm
```

Once installed, you will find AnythingLLM in your Applications folder as well as you can use `cmd + spacebar` and type in AnythingLLM to run.

### Privacy Policy

*AnythinglLM Desktop Privacy Policy*

**Source:** https://docs.useanything.com/installation-desktop/privacy

> **Tip:**
>
> This is the privacy policy for AnythingLLM Desktop **only**. All other products and services are covered by their respective privacy policies (MIT).

### AnythingLLM Desktop App Privacy Policy

*Effective July 14, 2025*

> **Tip:**
>
> **TL;DR:**
> None of your messages, chat histories, and documents are ever transmitted from your system - everything is saved locally on your device by default.
>
> We do collect some information about your usage of AnythingLLM Desktop, but never anything that can be used to identify you, your chats, documents, content, or anything else.
>
> You can see a list of all the information we collect in this codebase [here](https://github.com/search?q=repo%3AMintplex-Labs%2Fanything-llm%20.sendTelemetry).
>
> You can **fully opt out** of this telemetry by disabling it in the app settings.
>
> For more information, please refer to the [Terms of Use](https://docs.useanything.com/installation-desktop/terms).

#### Introduction

AnythingLLM Desktop processes as little info as possible, and can run entirely offline. This Privacy Policy ("Policy") describes what information Mintplex Labs ("we", "us", "our") may gather and how we use it when you download and use AnythingLLM Desktop (the "App").

We may update this policy occasionally. When we do, we'll post the new version on this page with a reasonable amount of time before the changes take effect.

#### Contact us

If you have any questions, comments or concerns regarding this Policy or our processing of information, please contact us at [team@mintplexlabs.com](mailto:team@mintplexlabs.com).

#### What we process and why

We only process information in the following occasions:

- When Telemetry is enabled and some usage stats are sent to our servers (see above)
- When you email us directly
- When you interact with the [AnythingLLM Community Hub](https://hub.anythingllm.com)

Here's what this means in practice, and the situations when we would receive data:

##### When You Email Us

- What: Your email address and the content of your email
- Why: So we can respond to your questions or provide the support you need

##### When You Interact with the AnythingLLM Community Hub

- What: General connection information (IP address, user agent, etc.)
- Why: The community hub is a public website with resources you can use freely inside the app. This service is operated by Mintplex Labs and is optional to use.

#### Our Commitment to Privacy

Privacy is core to AnythingLLM Desktop - it is the reason over 1M people have downloaded the app.

We process as little information as possible to facilitate your usage of the app, and regularly review our data practices to process only what's necessary. Even then, we only collect information that is anonymous and cannot be used to identify you, your chats, documents, content, or anything else.

Even then, you can turn it off fully once and forever in the app settings.

##### Never sell your information to third parties

We are not in the business of selling your information to third parties. We simply care about how people use the app, and how we can improve it. That is the only reason we collect any information at all.

In no way, shape, or form do we sell your information to third parties or use it as leverage for any other purpose.

##### Others involved in handling information

We use service providers who help us with our business operations. These providers are only authorized to store the information as necessary to provide these services to us and not for their own promotional purposes.

Service Providers we use:

- PostHog (Telemetry service) - Privacy Policy: <https://posthog.com/privacy>
- Cloudflare (CDN service) - Privacy Policy: <https://www.cloudflare.com/privacypolicy/>

##### Legal Requirements

In rare cases, we may need to disclose information to authorities, legal counsels, and advisors:

- To comply with legal obligations forced upon us by law
- When working with legal counsel on matters that could impact us

##### Business Changes

If our company undergoes organizational changes (like a merger or acquisition), information may be transferred to a new business as part of that process.

##### Data Subject Rights

AnythingLLM Desktop processes very limited data, none of which can be linked directly to individual users. Because the application does not include user-telemetry or user-specific tracking, we are unable to fulfill data subject requests such as providing a copy of your data or deleting your information. In other words, there's no way for us to identify or retrieve your specific data, and any information we do collect is anonymous and only kept briefly.

##### Additional information for individuals in the EU or UK

###### Controller

The data controller of the data described in this policy is:

Mintplex Labs, Inc., a Delaware corporation. Our registered address: 1950 W Corporate Way Ste. 25340, Anaheim, CA 92801.

###### Data subject rights

If you are in the EU or the UK, you have the following rights under the GDPR:

- Right to Access and receive a copy of your information that we process.
- Right to Rectify inaccurate information we have concerning you and to have incomplete information completed.
- Right to Data Portability, that is, to receive the information that you provided to us, in a structured, commonly used, and machine-readable format. You have the right to transmit this data to another person or entity. Where technically feasible, you have the right to have your information transmitted directly from us to the person or entity you designate.
- Right to Object to our processing of your information based on our legitimate interest. However, we may override the objection if we demonstrate compelling legitimate grounds, or if we need to process such information for the establishment, exercise, or defense of legal claims.
- Right to Restrict us from processing your information (except for storing it): (a) if you contest the accuracy of the information (in which case the restriction applies only for a period enabling us to determine the accuracy of the information); (b) if the processing is unlawful and you prefer to restrict the processing of the information rather than requiring the deletion of such data by us; (c) if we no longer need the information for the purposes outlined in this Policy, but you require the information to establish, exercise or defend legal claims; or (d) if you object to our processing based on our legitimate interest (in which case the restriction applies only for the period enabling us to determine whether our legitimate grounds for processing override yours).
- Right to be Forgotten. Under certain circumstances, such as when you object to our processing of your information based on our legitimate interest and there are no overriding legitimate grounds for the processing, you have the right to ask us to erase your information. However, notwithstanding such a request, we may still process your information if it is necessary to comply with our legal obligations, or for the establishment, exercise, or defense of legal claims. If you wish to exercise any of these rights, please contact us through the channels listed in this Policy.

When you contact us, we reserve the right to ask for reasonable evidence to verify your identity before we provide you with information. Where we are not able to provide you with information that you have asked for, we will explain the reason.

Subject to applicable law, you have the right to lodge a complaint with your local data protection authority. If you are in the EU, then according to Article 77 of the GDPR, you can lodge a complaint to the supervisory authority, in the Member State of your residence, place of work or place of alleged infringement of the GDPR.

If you are in the UK, you can lodge a complaint to the Information Commissioner's Office (ICO) pursuant to the instructions provided [here](https://ico.org.uk/make-a-complaint/).

###### Additional information for individuals in the United States

If you are an individual residing in the United States, we provide you with the following information pursuant to the applicable state privacy laws.

We do not sell your information and have not done so ever.

###### Your rights under U.S. State privacy laws

###### Right to deletion

Subject to certain exceptions set out below, on receipt of a verifiable request from you, we will:

- Delete your information from our records; and
- Direct any service providers to delete your information from their records.

Please note that we may not delete your information if it is necessary to:

Complete the transaction for which the information was collected, fulfill the terms of a written warranty or product recall conducted in accordance with federal law, provide a good or service requested by you, or reasonably anticipated within the context of our ongoing business relationship with you, or otherwise perform a contract between you and us.

Help to ensure security and integrity to the extent the use of the consumer's information is reasonably necessary and proportionate for those purposes.

Debug to identify and repair errors that impair existing intended functionality.

Exercise free speech, ensure the right of another consumer to exercise his or her right of free speech, or exercise another right provided for by law.

Engage in public or peer-reviewed scientific, historical, or statistical research that conforms or adheres to all other applicable ethics and privacy laws, when our deletion of the information is likely to render impossible or seriously impair the ability to complete such research, provided we have obtained your informed consent.

Enable solely internal uses that are reasonably aligned with your expectations based on your relationship with us and compatible with the context in which you provided the information.

We also will deny your request to delete if it proves impossible or involves disproportionate effort, or if another exception under the law applies. We will provide you with a detailed explanation that includes enough facts to give you a meaningful understanding as to why we cannot comply with the request to delete your information.

###### Right to correction

###### Right to correct inaccurate information

If we receive a verifiable request from you to correct your information and we determine the accuracy of the corrected information you provide, we will correct inaccurate information that we maintain about you.

In determining the accuracy of the information that is the subject of your request to correct, we will consider the totality of the circumstances relating to the contested information.

We also may require that you provide documentation if we believe it is necessary to rebut our own documentation that the information is accurate.

We may deny your request to correct in the following cases:

- We have a good-faith, reasonable, and documented belief that your request to correct is fraudulent or abusive.
- We determine that the contested information is more likely than not accurate based on the totality of the circumstances.
- Conflict with federal or state law.
- Another exception under the law.

###### Inadequacy in the required documentation

Compliance proves impossible or involves disproportionate effort.

We will provide you a detailed explanation that includes enough facts to give you a meaningful understanding as to why we cannot comply with the request to correct your information

###### Protection against discrimination

You have the right to not be discriminated against because you exercised any of your rights under applicable laws. If you exercise your rights, we cannot:

- deny you services.
- charge different prices or fees for services, also through discounts, benefits, or fines.
- provide you with a different level or quality of services.
- propose that you receive different prices or tariffs for services.

Please note that we may charge a different fee or provide a different level or quality of services, if the difference is reasonably related to the value we gain from your information.

###### Our response to your requests

We will respond to your requests within 45 days (or within 90 days, where the law permits, and we determine it necessary considering the complexity and number of the requests you have filed). If we take longer than 45 days, we will inform you of the extension within the initial forty-five-day response period, together with the reason for the extension.

We may deny your request in the following cases:

- If we believe in good faith, based on reasons which are documented in writing, that your request is fraudulent or is an abuse of your rights under applicable law.
- If we conclude that the request is irrelevant, based on all the circumstances at issue (e.g., if you requested to correct your information, and we find that it is likely to be accurate).
- If it is contrary to federal or state law.
- Due to discrepancy in the required documentation.
- If the fulfilment of your request turns out to be impossible or involves disproportionate effort.

We will provide you with a detailed explanation including sufficient facts, to enable you to meaningfully understand why we cannot fulfil your request.

You may appeal our decision to deny your request by sending us an email at [team@mintplexlabs.com](mailto:team@mintplexlabs.com).

### General Desktop Information

*General Desktop Information*

**Source:** https://docs.useanything.com/installation-desktop/storage

### General information

#### Where is my data located?

All data pertaining to AnythingLLM Desktop will be in the following locations. Please replace `<usr>` with your
device username.

On Mac:
`/Users/<usr>/Library/Application\ Support/anythingllm-desktop/storage`

On Linux:
`~/.config/anythingllm-desktop/storage/`

On Windows:
`C:\Users\<usr>\AppData\Roaming\anythingllm-desktop\storage`

##### What is each folder?

- `lancedb`: This it where your local vector database and its tables are stored.
- `documents`: This is the parsed document content of any uploaded files.
- `vector-cache`: This folder is the *cached* and embedded representation of a previous uploaded and embedded file. Its filename is hashed.
- `models`: Any locally stored LLMs or Embedder models used by the system are stored here. Typically are GGUF files.
- `anythingllm.db`: This is the AnythingLLM SQLite database.
- `plugins`: This is the folder where your custom agent skills are stored.
- `direct-uploads`: This is the folder where files drag-and-dropped into the AnythingLLM Desktop chat window are stored. This is for full-text insertion of files into the chat window.
- `logs`: This is the folder where the AnythingLLM Desktop logs are stored.

### System Requirements

*System Requirements to run AnythingLLM*

**Source:** https://docs.useanything.com/installation-desktop/system-requirements

![AnythingLLM System Requirements](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fsystem-requirements.png&w=3840&q=100)

#### System Requirements

AnythingLLM is fully customizable in every regard.

Given this customizable nature, your exact requirements to run AnythingLLM depend on many factors. You can use the tables below to get a rough idea of what it will take to run AnythingLLM.

AnythingLLM can be a wrapper around many external services that all accomplish some task - making AnythingLLM so lightweight it can run on the smallest machines - even Raspberry Pis!

#### Recommended configuration for AnythingLLM

The minimum requirements for running AnythingLLM vary based on your use case. Fundamentally, if want to use a local LLM on-device this will be the main factor in determining your requirements.
AnythingLLM itself is very lightweight and can run on very small machines, but the LLM is often the bottleneck to a decent experience and will limit what kind and size of models you can use.

In general, better model = better AnythingLLM experience. If you are wondering what the minimum requirements are for a "basic" AnythingLLM experience, they are as follows:

| Property | Recommended Value |
| --- | --- |
| RAM | 16GB |
| CPU | 8-core CPU (any) |
| Storage | *varies* |

On Windows, a GPU is recommended to leverage your GPU for faster processing of local LLMs (8-12GB+ VRAM is great!)
On MacOS, any M-Series chip will be able to handle local LLMs with no additional hardware. Intel-based Macs will be a bit slower - mostly limited by RAM.

The storage requirements are based on the size of the local LLM model you want to use since AnythingLLM stores the models on your PC.

If you are using a cloud-based LLM, the requirements will be much lower since the AnythingLLM client is very lightweight and does not need to store the models on your PC.

#### LLM selection impact

This is how you get chat responses. Popular hosted solutions like [OpenAI](https://openai.com/) tend to provide state-of-the-art responses with almost **zero overhead**. However, you will need an API key for any cloud-based LLM provider.

> **Tip:**
>
> **Tip:** Host a local LLM on another machine that has a GPU if the device
> running AnythingLLM does not have a GPU. AnythingLLM can connect to any LLM
> running anywhere via API.

#### Embedder selection impact

This is the model which you use to "**embed**" or vectorize text. Likewise, external services connected to AnythingLLM have **zero overhead** impact.

> **Tip:**
>
> **Tip:** Host a local embedder on another machine that has a GPU if the device
> running AnythingLLM does not have a GPU. AnythingLLM can connect to to a
> provider via API.

#### Vector database selection impact

All supported vector databases either have no impact as they are externally hosted or can scale to hundreds of millions of vectors at the minimum recommended settings.

*the default LanceDB vector database can handle anything you can throw at it*

### Terms of Use

*AnythingLLM Desktop Terms of Use*

**Source:** https://docs.useanything.com/installation-desktop/terms

> **Tip:**
>
> This is the terms of use for AnythingLLM Desktop **only**. All other products and services are covered by their respective terms of use (MIT).

### AnythingLLM Desktop App Terms of Use

Version: July 14, 2025

This page contains the Terms of Use for the AnythingLLM Desktop App.

For the Privacy Policy, please refer to the [AnythingLLM Privacy Policy](https://docs.useanything.com/installation-desktop/privacy).

Please read these Terms and Conditions ("Terms") carefully as they govern your use of the Software and Services (each as defined below).

#### Terms of Service

These Terms constitute an agreement between Mintplex Labs, Inc. ("Mintplex Labs", "Company", "we", "us") and the person or entity that downloads or uses the Software and uses the Services ("You", "Your", "User", "Customer"). If the person downloading or using the Software or Services is an employee, agent or contractor of a corporate entity and using the Software or Services within the scope of their employment, agency or primarily for the benefit of the corporate entity, the Terms are between the corporate entity and Mintplex Labs -- and the corporate entity is the Customer.

You represent and warrant that: (i) the person agreeing to these Terms is authorized to enter into these Terms on behalf of Customer and (ii) these Terms are binding on Customer.

If You do not agree to these Terms, then You must not download or use the Software or Services

##### Definitions

**Software** means the software made available by Mintplex Labs to You (e.g., via download) where these terms are identified as the governing terms, and any modified, updated or enhanced versions of such programs or modules that Mintplex Labs makes available to You.

**Services** mean the support services, including responses to community forums, and any other services provided by Mintplex Labs pursuant to these Terms.

**Intellectual Property Rights** means all copyrights, trademarks, service marks, trade secrets, patents, patent applications, moral rights, contract rights and other proprietary rights.

**Content** means the data or content uploaded into the Software or otherwise used by You in connection with the Software.

**Documentation** means any published instructions and user manuals provided to You along with the Software or the [AnythingLLM Documentation](https://docs.anythingllm.com). The Certified System Requirements are a subset of the Documentation.

**Confidential Information** means the Software and all written or oral information, disclosed by Mintplex Labs related to the business, products, services or operations of Mintplex Labs that by the nature of the information or the circumstances surrounding disclosure ought reasonably to be treated as confidential. Confidential Information will not include information that: (a) was already known without restriction to You at the time of disclosure; (b) was disclosed to You by a third party who had the right to make such disclosure without any confidentiality restrictions; (c) is, or through no fault of Yours has become, generally available to the public or (d) was independently developed by You without access to, or use of, the Disclosing Party's Confidential Information.

##### License Grant and Other Rights

Subject to the terms and conditions of these Terms, Mintplex Labs grants to You a non-exclusive, non-transferable, license to use the Software solely for Your personal and / or internal business purposes and solely in accordance with the Documentation.

##### Restrictions On Use

You acknowledge that the Software and its structure, organization, and source code constitute valuable trade secrets and Confidential information of Mintplex Labs and its suppliers. Except as expressly permitted by these Terms, You agree that You will not permit any third party to, and You will not itself: (a) modify, adapt, alter, translate, or create derivative works from the Software or the Documentation; (b) integrate the Software with other software other than through Mintplex Labs published interfaces made available with the Software; (c) use any open source products with the Software in a manner that imposes, or could impose, a requirement or condition that the Software or any part thereof: (i) be disclosed or distributed in source code for; (ii) be licensed for the purpose of making modifications or derivative works or (iii) be redistributable at no charge; (d) sublicense, distribute, sell, use for service bureau use, as an application service provider, or a software-as-a-service, lease, rent, loan, or otherwise transfer the Software or the Documentation to any third party; (e) reverse engineer, decompile, disassemble, or otherwise attempt to derive the source code for the Software, except and only to the extent that such activity is expressly permitted by applicable law notwithstanding this limitation; (f) remove, alter, cover or obfuscate any copyright notices or other proprietary rights notices included in the Software; or (g) otherwise use or copy the Software except as expressly permitted hereunder. You will notify Mintplex Labs of any unauthorized use or disclosure of the

##### Content

You are solely responsible for any and all obligations with respect to the Content including its accuracy, quality, legality and appropriateness and that it complies with Mintplex Labs's Authorized Use Policy, as it may be updated from time-to-time. In the event that You make any Content available to Mintplex Labs, You will obtain all third party licenses, consents and permissions needed for Mintplex Labs to use the Content to provide the Services. For the avoidance of doubt, Mintplex Labs reserves the right, but does not undertake the responsibility, to investigate any breach of the Authorized Use Policy or a breach of this Section

You also understand that the Software is not designed to be used for any illegal or unauthorized purposes. You are responsible for ensuring that You are in compliance with all applicable laws and regulations.

##### Installation

You are responsible for installing the Software in compliance with the Certified System Requirements as permitted under these Terms.

##### Feedback

Mintplex Labs in its sole discretion, may utilize, all comments and suggestions, whether written or oral, furnished by You to Mintplex Labs in connection with its access to and use of the Software, Services and Documentation (all reports, comments and suggestions provided by You hereunder constitute, collectively, the "Feedback"). You hereby grant Mintplex Labs a worldwide, non-exclusive, irrevocable, perpetual, royalty-free right and license to incorporate the Feedback into Mintplex Labs products and services.

##### Proprietary Rights

As between You and Mintplex Labs, You own all rights, title and interest in the Content and all rights not expressly granted to Mintplex Labs in these Terms in the Content are reserved to You. The Software and Documentation, and all worldwide Intellectual Property Rights therein, are the exclusive property of Mintplex Labs and its suppliers. All rights in and to the Software not expressly granted to You in these Terms are reserved by Mintplex Labs and its suppliers. You will not remove, alter, or obscure any proprietary notices (including copyright notices) of Mintplex Labs or its suppliers on the Software or the Documentation.

##### Disclaimers

###### General Disclaimers

THE SOFTWARE AND SERVICES ARE MADE AVAILABLE BY MINTPLEX LABS "AS IS", "WITH ALL FAULTS" AND WITHOUT WARRANTY OF ANY KIND, INCLUDING THAT THERE ARE NO EXPRESS, IMPLIED OR STATUTORY WARRANTIES, INCLUDING ANY WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, AND NON-INFRINGEMENT OF THIRD PARTY RIGHTS. MINTPLEX LABS DOES NOT WARRANT THAT THE SOFTWARE WILL MEET YOUR REQUIREMENTS OR THAT THE SOFTWARE WILL WORK UNINTERRUPTED.

###### Specific Disclaimers

(A) THE SOFTWARE IS DESIGNED TO WORK WITH THIRD PARTY PRODUCTS ("THIRD PARTY PRODUCTS") INCLUDING THIRD PARTY ARTIFICIAL INTELLIGENCE MODELS ("THIRD PARTY AI MODELS", WHICH ARE A SUBSET OF THIRD PARTY PRODUCTS). MINTPLEX LABS MAY FACILITATE YOUR ABILITY TO DOWNLOAD AND INTEGRATE THE THIRD PARTY PRODUCTS WITH THE SOFTWARE WITH THE UNDERSTANDING THAT SUCH THIRD PARTY PRODUCTS ARE MADE AVAILABLE TO YOU PURSUANT TO A LICENSE AGREEMENT BETWEEN YOU AND THE THIRD PARTY PROVIDER OF SUCH THIRD PARTY PRODUCTS (THE "CUSTOMER – THIRD PARTY PROVIDER AGREEMENT"). YOU WILL UNDERTAKE ALL MEASURES NECESSARY TO ENSURE THAT ITS USE OF THE THIRD PARTY PRODUCTS IN CONNECTION WITH THE SOFTWARE AND SERVICES COMPLIES IN ALL RESPECTS WITH APPLICABLE LAW, THE CUSTOMER – THIRD PARTY PROVIDER AGREEMENT, AND ANY OTHER CONTRACTUAL OR LEGALLY BINDING OBLIGATIONS IN CONNECTION WITH THE THIRD PARTY PRODUCTS, INCLUDING THIRD PARTY LICENSES FOR THE USE OF FREE AND OPEN SOURCE SOFTWARE. IN NO EVENT IS MINTPLEX LABS LIABLE TO YOU FOR ANY FAILURE OF THE THIRD PARTY PRODUCTS OR

###### Export Controls and Sanctions

The Software maybe be subject to trade control laws, including the export control and economic sanctions laws of the United States, including but not limited to the Export Administration Regulations maintained by the U.S. Department of Commerce, trade and economic sanctions maintained by the U.S. Treasury Department's Office of Foreign Assets Control ("OFAC"), the International Traffic in Arms Regulations maintained by the U.S. Department of State (collectively, "Trade Control Laws"). You represents and warrants that You are (a) not located in, organized under the laws of, or ordinarily resident in any country or territory subject to territorial sanctions ("Sanctioned Country"), nor owned by or acting on behalf of a Government subject to asset-blocking sanctions or any person or entity organized, located or ordinarily resident in a Sanctioned Country; and (b) not a person identified on, or more than 50% owned or controlled, directly or indirectly, by or acting on behalf or, at the direction of, any entity identified on applicable government restricted party lists, such as the Specially Designated Nationals List maintained by OFAC. You further agree to comply with all applicable Trade Control Laws in its use of the Software. Specifically, You agree not to, directly or indirectly, use, sell, supply, export, reexport, transfer, divert, release, or otherwise dispose of any products, software, or technology (including products derived from or based on such technology) received from Mintplex Labs to any destination, entity, or person or for any end use prohibited by applicable Trade Controls Laws.

###### Indemnification

You will indemnify, defend and hold harmless Mintplex Labs, its directors, officers, employees and representatives from and against any and all damages, losses, and expenses of any kind (including reasonable attorneys' fees and costs) arising out of or related to: (a) Your breach of any of these Terms. Including any representation or warranty; (b) any Content; (3) any activity in which You engage on or through the use of the Software or Services and (d) Your violation of any law or the rights of a third party.

###### Disclaimers and limitations on Remedies

YOU AGREES THAT ITS SOLE AND EXCLUSIVE REMEDY FOR ANY PROBLEMS OR DISSATISFACTION WITH THE SOFTWARE AND SERVICES IS TO UNINSTALL THE SOFTWARE AND TO STOP USING THE SERVICES. TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT WILL MINTPLEX LABS, ITS OFFICERS, SHAREHOLDERS, EMPLOYEES, AGENTS, DIRECTORS, SUBSIDIARIES, AFFILIATES, SUCCESSORS, ASSIGNS, SUPPLIERS, OR LICENSORS BE LIABLE FOR: (A) ANY INDIRECT, SPECIAL, INCIDENTAL, PUNITIVE, EXEMPLARY, OR CONSEQUENTIAL DAMAGES; (B) ANY LOSS OF USE, DATA, BUSINESS, OR PROFITS (WHETHER DIRECT OR INDIRECT), IN ALL CASES ARISING OUT OF THE USE OF OR INABILITY TO USE THE SOFTWARE, SERVICES, THIRD PARTY PRODUCTS, THIRD PARTY AI MODELS, OR CUSTOMER’S OWN SOFTWARE, HARDWARE OR OPERATIONS, REGARDLESS OF LEGAL THEORY, WITHOUT REGARD TO WHETHER MINTPLEX LABS HAS BEEN WARNED OF THE POSSIBILITY OF THOSE DAMAGES, AND EVEN IF A REMEDY FAILS OF ITS ESSENTIAL PURPOSE; OR (C) AGGREGATE LIABILITY FOR ALL CLAIMS RELATING TO THE SOFTWARE OR SERVICES IS $50.00. For clarification, these Terms do not limit Mintplex Labs’s liability for fraud, fraudulent misrepresentation, death or personal injury to the extent that applicable law would prohibit such a limitation.

###### Confidentiality

Your use of the Software and Services is subject to the [Mintplex Labs & AnythingLLM Desktop Privacy Policy](https://docs.anythingllm.com/privacy).

###### Notices

All notices or demands required hereunder will be sent through email by email addresses provided or be delivered by certified or registered mail to; in the case of Mintplex Labs, 1950 W Corporate Way Ste. 25340, Anaheim, CA 92801 or in the case of Yours via any means available to Mintplex Labs .

###### Governing Law and Venue

These Terms and all Statements of Work will be governed by and interpreted in accordance with the laws of the State of California, without reference to its choice of laws rules. Any action or proceeding arising from or relating to these Terms will be brought in a state court in Orange County, or federal court in Orange County, California, and each party irrevocably submits to the jurisdiction and venue of any such court in any such action or proceeding.

###### Remedies

You acknowledge that the Software contains valuable trade secrets and proprietary information of Mintplex Labs, that any actual or threatened breach of Section 2 will constitute immediate, irreparable harm to Mintplex Labs for which monetary damages would be an inadequate remedy, that injunctive relief is an appropriate remedy for such breach, and that if granted, You agree to waive any bond that would otherwise be required.

###### Waivers

All waivers must be in writing. Any waiver or failure to enforce any provision of the Terms on one occasion will not be deemed a waiver of any other provision or of such provision on any other occasion.

###### Severability

If any provision of the Terms are unenforceable, such provision will be changed and interpreted to accomplish the objectives of such provision to the greatest extent possible under applicable law and the remaining provisions will continue in full force and effect.

###### Entire Agreement

These Terms and the exhibits hereto, constitute the entire agreement between the parties regarding the subject hereof and supersedes all prior or contemporaneous agreements, understandings, and communication, whether written or oral. These Terms will not be modified except by a subsequently dated written amendment signed on behalf of Mintplex Labs and You by their duly authorized representatives.

### Uninstall

*Learn how to completely uninstall AnythingLLM*

**Source:** https://docs.useanything.com/installation-desktop/uninstall

![AnythingLLM Uninstall](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Funinstall.png&w=3840&q=100)

#### Uninstalling on MacOS

Open your `Finder` and navigate to the `Applications` folder. Then, drag the AnythingLLM application into the `Trashcan`, and the application will be uninstalled.

To remove all AnythingLLM desktop data from your system, please also delete the `/Users/<usr>/Library/Application Support/anythingllm-desktop` folder. This folder is where your database, documents, and vector cache are located.

#### Uninstalling on macOS using Homebrew

Run this command and the application will be uninstalled:

```
brew uninstall --cask anythingllm
```

To remove the AnythingLLM desktop app and all app data from your system (this deletes the `/Users/<usr>/Library/Application Support/anythingllm-desktop` folder, which contains your database, documents, and vector cache), run this command:

```
brew uninstall --zap --cask anythingllm
```

---

#### Uninstalling on Linux

Delete the `.AppImage` from your system. Once done, follow the instructions below to erase all related data.

To completely remove all application data, including your local database, documents, and vector cache, delete the folder located at `/home/{user}/.config/anythingllm-desktop`.

You can delete the entire directory or just the storage folder to reset your current install.

---

#### Uninstalling on Windows

Utilize the uninstallation `executable` located in `/Users/{user}/AppData/Local/Programs/AnythingLLM` (or) `/Users/{user}/AppData/Local/Programs/anythingllm-desktop`

To completely remove all application data from your system, including your local database, documents, and vector cache, delete the folder located at `/Users/{user}/AppData/Roaming/anythingllm-desktop/storage`.

You have the option to delete either the entire `/Users/{user}/AppData/Roaming/anythingllm-desktop` folder or just the storage folder to reset your installation

### Update

*Learn how to update AnythingLLM*

**Source:** https://docs.useanything.com/installation-desktop/update

![AnythingLLM Update](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fupdate.png&w=3840&q=100)

#### Updating on MacOS

##### Updating using Installation file

Simply download the latest version of the installation `dmg` from the [download page](https://anythingllm.com/download) and then re-install the app and it will overwrite the existing application while persisting your storage and progress.

##### Updating using Homebrew

> **Warning:**
>
> **Note:** ➤➤ You can only update using Homebrew if you initially installed
> AnythingLLM using Homebrew.

Simply run the below command on your terminal

```
 brew update && brew upgrade --cask anythingllm
```

This command will overwrite the existing application with the new version while persisting your storage and progress.

---

#### Updating on Windows

Simply download the latest version of the installation `.exe` from the [download page](https://anythingllm.com/download) and then re-install the app and it will overwrite the existing application while persisting your storage and progress.

---

#### Updating on Linux

Simply download the latest version of the installation `.AppImage` from the [download page](https://anythingllm.com/download) and then execute this new `.AppImage` and delete the old one. This will persist your data, but allow you to use the latest version of the software.

### Windows Installation

*Windows Installation guide for AnythingLLM*

**Source:** https://docs.useanything.com/installation-desktop/windows

![AnythingLLM Windows Installation](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fwindows%2Fheader-image.png&w=1080&q=100)

#### Install using the installation file

> **Warning:**
>
> **OPERATING SYSTEM NOTICE**
>
> ➤ AnythingLLM is intended to be used on an user account of Windows Home. Other versions of windows (Enterprise or Server) may not work. We target for Windows 11.

**[1. Download the installer for your hardware](https://docs.useanything.com/installation-desktop/windows#downloading-the-installation-file)**

##### Downloading the installation file

Here is the download link for the latest version of Anything LLM Windows.

[Windows 10+ (Home, Professional - x86 64-bit)→](https://cdn.anythingllm.com/latest/AnythingLLMDesktop.exe)
  
[Windows 10+ (Home, Professional - ARM 64-bit)→](https://cdn.anythingllm.com/latest/AnythingLLMDesktop-Arm64.exe)

#### Installing the application

> **Warning:**
>
> We **do not** recommend installing AnythingLLM Desktop for "all users" on a Windows machine.
> Instead, install for "Current User" only. Installing for all users will cause issues with the app and is not supported.

After downloading the windows `exe` installer for AnythingLLM, you can double-click the installer and it will display the installation process.

After which, now the regular installer can run to install AnythingLLM Desktop!

![AnythingLLM Windows Install](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fwindows%2Finstall.png&w=3840&q=100)
> **Tip:**
>
> **Local LLM support**
>
> ➤ AnythingLLM desktop includes a built-in local LLM powered via [Ollama](https://ollama.com/). This is a super convenient way to get started with LLMs without any additional setup.
>
> In order for AnythingLLM to leverage your GPU (NVIDIA or AMD) or even NPU we need to install some extra dependencies. This will be done automatically during installation.
>
> If these extra dependencies are not installed, you will see a warning in the UI and you will get reduced performance for local LLMs since you will be limited to CPU processing.

Click on the application name "**AnythingLLM**" on your desktop to boot up AnythingLLM!

*your first boot may take a minute or two to complete on some systems, but subsequent boots will be near instant.*

![AnythingLLM Windows Open](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fwindows%2Fdesktop.png&w=3840&q=100)

#### Troubleshooting

##### "AnythingLLM cannot be closed" when trying to install

![AnythingLLM Windows Installation Error](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fwindows%2Finstallation-error-cc.png&w=1080&q=100)

If you are trying to install AnythingLLM and you are getting an error that says "AnythingLLM cannot be closed" during installation the following steps will solve your issue.

1. **You previously installed AnythingLLM and it is still running in the background.**

- Since v1.11.0, AnythingLLM minimizes to the system tray when closed. Check your system tray for the AnythingLLM icon and click on it. "Quit AnythingLLM" to close it.
- You can then click on "Retry" and the installation will continue.

2. **You previously installed AnythingLLM for all users instead of just the current user.**

- Prior to v1.11.0, AnythingLLM was allowed to be installed for all users. This is no longer the case - this can cause issues during installation since you must run the installer as administrator to uninstall programs from your primary drive.
- To fix this, you must uninstall AnythingLLM for all users and then reinstall for the current user only. Right- Click on the AnythingLLM Desktop icon and click "Open File Location" to open the installation folder.
- Click on the "Uninstall AnythingLLM.exe" file and run it. You may or may not have to run it as administrator.
- After uninstalling, you can then reinstall for the current user only.

**Performing the above steps WILL NOT remove your data or settings. You can do this safely without losing any of your data.**

##### Failed to install/extract GPU support from CDN

> **Warning:**
>
> If we update to a new version of Ollama, we will update the engine version to the new version. Which again, may fail to install/extract the GPU support file leading to this error again.
>
> You can avoid all of this by just installing AnythingLLM and Ollama separately and then connecting AnythingLLM to your local Ollama instance - which will be automatically detected and less frustrating between updates.
>
> We do not recommend trying to fix this issue manually as it is very prone to user error and would break when we upgrade to later versions of Ollama in AnythingLLM.

During installation, we pull in the vendor specific GPU support from our CDN so that you can leverage your GPU for local LLM inferencing for an optimal experience.

Depending on your network connection, firewall, device settings, or other factors, you may encounter an error during installation or extraction of the GPU support where it fails to download or extract the files. Our CDN
is globally accessible, so it is extremely unlikely that the issue is with our CDN.

Before attempting to fix the issue, be sure to check your network connection, firewall, device settings, or other factors that may be blocking the download or extraction of the files. You can relaunch the installer and try again.
If the error contines, open the `ollama_install.log` file in the `%APPDATA%\Local\Programs\AnythingLLM` folder and check for any errors but also the version of `Ollama` that is being installed.

From the `ollama_install.log` file, you will see the version of `Ollama` that is being installed. Keep this version number handy for the next steps.

If you encounter this error, you can try the following steps to fix it:

> **Tip:**
>
> **Example:**
>
> - If the version of `Ollama` that is being installed is `0.13.0`, you should download the following files:
>   - <https://cdn.anythingllm.com/support/ollama/0.13.0/bins.7z>
>   - <https://cdn.anythingllm.com/support/ollama/0.13.0/cudav13.7z>
>   - <https://cdn.anythingllm.com/support/ollama/0.13.0/cudav12.7z>
>   - <https://cdn.anythingllm.com/support/ollama/0.13.0/rocm_vulkan.7z>

1. **Download the GPU support files manually**

- **Required base binaries:** `https://cdn.anythingllm.com/support/ollama/<version>/bins.7z`

*if you have an NVIDIA GPU, you can download the CUDA support from the following link:*

- **Ollama Cudav13:** `https://cdn.anythingllm.com/support/ollama/<version>/cudav13.7z`
- **Ollama CUDAv12:** `https://cdn.anythingllm.com/support/ollama/<version>/cudav12.7z`

*if you have an AMD GPU, you can download the ROCm support from the following link:*

- **Ollama ROCm:** `https://cdn.anythingllm.com/support/ollama/<version>/rocm_vulkan.7z`

2. **Extract the `bins.7z` folder**

- Open the storage location for AnythingLLM, typically `%APPDATA%\Roaming\anythingllm-desktop\storage\engines\ollama`
- In this folder you should see `llm.exe`
- Create and open the following folder: `%APPDATA%\Roaming\anythingllm-desktop\storage\engines\ollama\lib\ollama`
- Unzip the `bins.7z` file into this folder.
- You should now see several DLL files directly in this folder.

3. Extract relevant GPU support files

- If you have an NVIDIA GPU, you can extract the `cudav13` or `cudav12` folder into the `%APPDATA%\Roaming\anythingllm-desktop\storage\engines\ollama\lib\ollama` folder.
- If you have an AMD GPU, you can extract the `rocm_vulkan.7z` file into the `%APPDATA%\Roaming\anythingllm-desktop\storage\engines\ollama\lib\ollama` folder.

Your explorer should now look like this:

```
%APPDATA%\Roaming\anythingllm-desktop\storage\engines\ollama
├── lib
│   └── ollama
│       ├── ggml-base.dll
│       ├── ggml-cpu-**.dll (several DLL files from bins.7z)
│       ├── cudav13/ (if you have an NVIDIA GPU)
│       │   └── cublas64_11.dll (several DLL files from cudav13.7z)
│       ├── cudav12/ (if you have an NVIDIA GPU)
│       │   └── cublas64_11.dll (several DLL files from cudav12.7z)
│       ├── rocm/ (if you have an AMD GPU)
│       │   └── **.dll (files and folders)
│       └── vulkan/ (if you have an AMD GPU)
│           └── vulkan_layer.dll (several DLL files from rocm_vulkan.7z)
└── llm.exe
```

4. Create a new dot-file in the `%APPDATA%\Roaming\anythingllm-desktop\storage\engines\ollama` folder called `.ollama-version` (no extension!) and add the following content:

- `<version>` eg: (0.13.0, 0.12.0, etc.)

5. Restart the AnythingLLM desktop app.

- Delete all the 7z files from the `%APPDATA%\Roaming\anythingllm-desktop\storage\engines\ollama` folder as they are no longer needed.
- You should now be able to use your GPU for local LLM inferencing.


---

## Docker Installation

### Installation Overview

*AnythingLLM offers two main ways to use AnythingLLM. There are some distinct differences in functionality between each offering*

**Source:** https://docs.useanything.com/installation-docker/overview

#### Installation Overview

AnythingLLM Docker is both a **single-user** and **multi-user** application you can install on any webserver using docker and leverage local LLMs, RAG, and Agents with little to zero configuration and full privacy.

Self hosting AnythingLLM via Docker is very popular and can be done locally or on cloud servicers (aws, google cloud, railway etc..).

#### Docker vs Desktop Version

> **Tip:**
>
> **Tip:** AnythingLLM Desktop is the easiest way to get started with AnythingLLM.
>
> If you dont need multi-user support - you should use AnythingLLM Desktop.

There are some distinct differences in functionality between each offering. Both are open source.

##### You want AnythingLLM Docker if...

- You need an easy setup, but server-based service for AnythingLLM to use local LLMs, RAG, and Agents locally
- You want to run an AnythingLLM instance that many people can use at the same time
- You want to be able to share information with our users on your instance you invite
- You need admin and rule-based access for workspaces and documents.
- You will publish chat widgets to the public internet
- You want to access AnythingLLM from the browser

##### You want AnythingLLM Desktop if...

- You want a one-click installable app to use local LLMs, RAG, and Agents locally
- You do not need multi-user support
- Everything needs to stay only on your device
- You do not need to "publish" anything to the public internet. Eg: Chat widget for website

The below table is a non-exhaustive list of features supported between platforms.

| Feature | Available on Desktop | Available on Docker |
| --- | --- | --- |
| Multi-user support | ❌ | ✅ |
| Emeddable chat widgets | ❌ | ✅ |
| One-click install | ✅ | ❌ |
| Private documents | ✅ | ✅ |
| Connect to any vector database | ✅ | ✅ |
| Use any LLM | ✅ | ✅ |
| Built-in embedding provider | ✅ | ✅ |
| Built-in LLM provider | ✅ | ❌ |
| White-labeling | ❌ | ✅ |
| Chat logs | ✅ | ✅ |
| Agent support | ✅ | ✅ |
| Agent skills | ✅ | ✅ |
| Third-party data connectors | ✅ | ✅ |
| Password protection | ❌ | ✅ |
| Invite new users to instance | ❌ | ✅ |
| Text splitting configuration | ✅ | ✅ |
| Whisper model support | ✅ | ✅ |
| Full developer API | ✅ | ✅ |
| User management | ❌ | ✅ |
| Workspace access management | ❌ | ✅ |
| Website scraping | ✅ | ✅ |

### Available Images

*There are a number of pre-built images for AnythingLLM that you can use to get started*

**Source:** https://docs.useanything.com/installation-docker/available-images

#### Available Images

##### `latest`

- **Architecture:** `amd64` & `arm64`
- **Deployment Frequency:** On every commit to the `master` branch
- **Pull Command:** `docker pull mintplexlabs/anythingllm:latest`

The latest image is the most recent version of AnythingLLM. It is updated on a near-daily basis and will always be up to date with the latest features and bug fixes
that are committed to the `master` branch in the [AnythingLLM GitHub repository](https://github.com/Mintplex-Labs/anything-llm).

##### `v*.*.*`

- **Architecture:** `amd64` & `arm64`
- **Deployment Frequency:** On new releases
- **Pull Command:** `docker pull mintplexlabs/anythingllm:v*.*.*`

The `v*.*.*` images are the pinned versioned releases of AnythingLLM. These images are published when a new release is made - you can find the latest release [here](https://github.com/Mintplex-Labs/anything-llm/releases).

##### `render` or `railway`

> **Tip:**
>
> **Warning:** You **should only** specify this image if you are deploying AnythingLLM via [Render](https://render.com/deploy?repo=https://github.com/Mintplex-Labs/anything-llm&branch=render) or [Railway](https://railway.app/template/HNSCS1?referralCode=WFgJkn).

- **Architecture:** `amd64`
- **Deployment Frequency:** On new releases
- **Pull Command:** `docker pull mintplexlabs/anythingllm:render`

The `render` or `railway` images are the latest versions of AnythingLLM and are in sync with the [**versioned** releases of AnythingLLM](https://github.com/Mintplex-Labs/anything-llm/releases).

##### `pg`

- **Architecture:** `amd64` & `arm64`
- **Deployment Frequency:** On new releases
- **Pull Command:** `docker pull mintplexlabs/anythingllm:pg`

The `pg` image is the latest version of AnythingLLM that are **specifically** built to use with a local or remote PostgreSQL database.

This image has a slightly different startup command to support the PostgreSQL deployment and does the following:

- Will store all AnythingLLM data in the PostgreSQL database
- Will by default use **PGVector** for vector storage - **requires** a PGVector extension to be installed on the PostgreSQL database

See the [PostgreSQL image deployment command](https://docs.useanything.com/installation-docker/quickstart#pg-image-startup-command) for more information.

### Cloud Docker Installation

*Cloud Docker Installation guide for AnythingLLM*

**Source:** https://docs.useanything.com/installation-docker/cloud-docker

![AnythingLLM Installation Cloud Docker](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fcloud-docker%2Fheader-image.png&w=3840&q=100)

### Run AnythingLLM on Cloud using Docker

Running AnythingLLM on a cloud service is the best way to run a private multi-user instance of AnythingLLM with full control while not having to worry about the underlying infrastructure.

> **Tip:**
>
> **Easy Cloud Deployment**
>
> AnythingLLM offers easily integrated one-click docker deployment templates with [Railway](https://railway.app/template/HNSCS1?referralCode=WFgJkn) and [Render](https://render.com/deploy?repo=https://github.com/Mintplex-Labs/anything-llm&branch=render).
>
> *This is the easiest way to self-host a cloud server version of AnythingLLM*

| Provider | Minimum Instance size |
| --- | --- |
| Amazon Web Services | t3.small |
| Google Cloud Provider | e2-standard-2 |
| Azure Cloud | B2ps v2 |

> **Tip:**
>
> AnythingLLM offers community-maintained deployment templates for cloud
> providers
> <https://github.com/Mintplex-Labs/anything-llm/tree/master/cloud-deployments>

Once you are prepared to run AnythingLLM on your server the process is quite simple.

You should provision a folder somewhere on the host machine so that you can re-pull the latest versions of AnythingLLM and persist data between container rebuilds.

> **Warning:**
>
> **BACKWARDS COMPATIBILITY**
>
> The Mintplex Labs team takes great care to ensure AnythingLLM is always backward compatible.
>
> In the event this changes you will be alerted via code, deployment, or our regular communication channels on social, Discord, and email.

> **Tip:**
>
> **Note** `--cap-add SYS_ADMIN` is a **required** command if you want to scrape
> webpages. We use [PuppeeteerJS](https://github.com/puppeteer/puppeteer) to
> scrape websites links and `--cap-add SYS_ADMIN` lets us use sandboxed Chromium
> across all runtimes for best security practices.

```
 # Assuming that you want to store app data in a folder at /var/lib/anythingllm
 
 # Pull in the latest image
 docker pull mintplexlabs/anythingllm:master
 
 export STORAGE_LOCATION="/var/lib/anythingllm" && \
 mkdir -p $STORAGE_LOCATION && \
 touch "$STORAGE_LOCATION/.env" && \
 docker run -d -p 3001:3001 \ # expose on port 3001 (can be any host port)
 --cap-add SYS_ADMIN \
 -v ${STORAGE_LOCATION}:/app/server/storage \
 -v ${STORAGE_LOCATION}/.env:/app/server/.env \
 -e STORAGE_DIR="/app/server/storage" \
 mintplexlabs/anythingllm:master
 
 # visit http://localhost:3001 to use AnythingLLM!
```

Done! You are using AnythingLLM!

#### More Information

##### Backwards Compatibility

The Mintplex Labs team takes great care to ensure AnythingLLM is always backward compatible.
In the event this changes you will be alerted via code, deployment, or our regular communication channels on social, Discord, and email.

##### Scaling

Since the AnythingLLM backend uses SQLite for its database, it is not recommended to attempt to scale the AnythingLLM backend horizontally
since you would then need to have many containers all reading and writing to the same database.

In this case, we recommend using a more robust database like PostgreSQL and our [PostgreSQL image](https://docs.useanything.com/installation-docker/available-images#pg) which will centralize the database as well as set `PGVector` as the vector database.

##### SSL/HTTPS Support

In order to use SSL/HTTPS with AnythingLLM you should use a reverse proxy like [NGINX](https://www.nginx.com/) with a TLS certificate you can get from [Let's Encrypt](https://letsencrypt.org/).

##### NGINX Configuration

Here is an example NGINX configuration that you can use to reverse proxy to AnythingLLM:

```
### Default server configuration
### Example config for regular setup + SSL + Websockets.
server {
	listen 80;
	server_name your-domain.com;
	return 301 https://your-domain.com$request_uri;
}
 
server {
	listen 443 ssl;
	ssl on;
	server_name your-domain.com;
	ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;	
 
  # Enable websocket connections for agent protocol.
	location ~* ^/api/agent-invocation/(.*) {
		proxy_pass http://localhost:3001;
		proxy_http_version 1.1;
		proxy_set_header Upgrade $http_upgrade;
		proxy_set_header Connection "Upgrade";
	}
 
	# Enable a custom 502 error page.
	# Must define template at /usr/share/nginx/html/502.html
	# error_page 502 /502.html;
    # location /502.html {
    #   index 502.html;
    # }
 
	location / {
		proxy_connect_timeout       605;
    proxy_send_timeout          605;
    proxy_read_timeout          605;
    send_timeout                605;
    keepalive_timeout           605;
    proxy_buffering off;
    proxy_cache off;
    proxy_pass         http://your-server-ip:3001$request_uri;
  }
}
```

### Debug

*Learn how to run AnythingLLM in debug mode*

**Source:** https://docs.useanything.com/installation-docker/debug

![AnythingLLM Debug Mode](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fdebug.png&w=3840&q=100)

#### General Debugging

If you are having issues with AnythingLLM, the first thing you should do is check the logs. You can find the logs in the `logs` folder of your container.

#### AnythingLLM Debug mode on Docker

Open `Container Logs` in Docker desktop or print the logs via `docker container <CONTAINER_ID> logs`

### Local Docker Installation

*Local Docker Installation guide for AnythingLLM*

**Source:** https://docs.useanything.com/installation-docker/local-docker

![AnythingLLM Installation Local Docker](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Flocal-docker%2Fheader-image.png&w=3840&q=100)

### Get Started with AnythingLLM in Docker

#### Pull the latest image

```
docker pull mintplexlabs/anythingllm:latest
```

#### Run the image

> **Warning:**
>
> If you do not use the command below - all of your data will be lost when the container is restarted!
>
> The `-v ${STORAGE_LOCATION}:/app/server/storage` is required to persist your data on your host machine in a persistent way.

Linux/MacWindows

#### Open the application

To access the full application, visit `http://localhost:3001` in your browser.

#### Other information

##### About UID and GID in the ENV

- The UID and GID are set to 1000 by default. This is the default user in the Docker container and on most host operating systems.
- If there is a mismatch between your host user UID and GID and what is set in the `.env` file, you may experience permission issues.

##### Build locally from source *not recommended for casual use*

- `git clone` this repo and `cd anything-llm` to get to the root directory.
- `touch server/storage/anythingllm.db` to create empty SQLite DB file.
- `cd docker/`
- `cp .env.example .env` **you must do this before building**
- `docker-compose up -d --build` to build the image - this will take a few moments.

Your docker host will show the image as online once the build process is completed. This will build the app to `http://localhost:3001`.

---

#### Common questions and fixes

##### Cannot connect to service running on localhost!

Please see [How to connect to localhost](https://docs.useanything.com/installation-docker/localhost) services.

##### Having issues with Ollama?

See [Ollama Connection Troubleshooting](https://docs.useanything.com/ollama-connection-troubleshooting) and also read about [How to connect to localhost](https://docs.useanything.com/installation-docker/localhost) services. This is 100% of the time the issue.

##### Still not working?

Ask for help on our Discord [Community Server](https://discord.gg/6UyHPeGZAC)

### A note about localhost

*A note about connecting to localhost from AnythingLLM running in Docker*

**Source:** https://docs.useanything.com/installation-docker/localhost

*The provided instructions below assume you are running AnythingLLM via the [official startup command](https://docs.useanything.com/installation-docker/quickstart).*

##### Using any `localhost` service when running AnythingLLM in Docker

When running AnythingLLM in Docker, you may need to connect to a service running on localhost.

This could be be any of the following:

- A PostgreSQL database
- An LLM, Embedding, or Vector Database provider (LMStudio, Ollama, Chroma, etc)
- Any other service running on the same machine where you are using `localhost`, `127.0.0.1`, or `0.0.0.0` to connect it with AnythingLLM

#### `localhost`, `127.0.0.1`, `0.0.0.0` Will Not Work!

When running AnythingLLM in Docker, the `localhost`, `127.0.0.1`, or `0.0.0.0` addresses do not exist in the container!

This means when you are using `localhost`, `127.0.0.1`, or `0.0.0.0` in any connection configuration, they will not work as expected because these connections never leave the AnythingLLM container.

#### How to connect to a service running on localhost

If you need to connect to a service running on localhost or even a service running in another Docker container simply
modify anywhere you are using `localhost`, `127.0.0.1`, or `0.0.0.0` to use the `host.docker.internal` address instead.

##### Note about Linux

On Linux, you must use the `172.17.0.1` address instead of `host.docker.internal` to connect to the host machine.

##### Examples

```
### PostgreSQL
postgresql://dbuser:dbpassword@localhost:5432/dbname => postgresql://dbuser:dbpassword@host.docker.internal:5432/dbname

### Ollama
http://localhost:11434" => http://host.docker.internal:11434

### Chroma
http://localhost:8000" => http://host.docker.internal:8000

### LMStudio
http://localhost:1234" => http://host.docker.internal:1234
```

### Quickstart

*Quickstart guide for AnythingLLM via Docker*

**Source:** https://docs.useanything.com/installation-docker/quickstart

### How to use Dockerized Anything LLM

Use the Dockerized version of AnythingLLM for a much faster and complete startup of AnythingLLM compared to running the source code directly.

#### Start AnythingLLM via Docker

Linux/MacWindows

Go to `http://localhost:3001` and you are now using AnythingLLM! All your data and progress will persist between
container rebuilds or pulls from Docker Hub.

#### How to use the user interface

To access the full application, visit `http://localhost:3001` in your browser.

#### About UID and GID in the ENV

- The UID and GID are set to 1000 by default. This is the default user in the Docker container and on most host operating systems.
- If there is a mismatch between your host user UID and GID and what is set in the `.env` file, you may experience permission issues.

#### `pg` image startup command

The `pg` image has a slightly different startup command to support the PostgreSQL database connection.

First, ensure you have a PostgreSQL database running and a [PGVector extension installed on that database](https://github.com/pgvector/pgvector).

LinuxMacWindows

### System Requirements

*System Requirements to run AnythingLLM*

**Source:** https://docs.useanything.com/installation-docker/system-requirements

![AnythingLLM System Requirements](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fsystem-requirements.png&w=3840&q=100)

#### System Requirements

AnythingLLM is fully customizable in every regard.

Given this customizable nature, your exact requirements to run AnythingLLM depend on many factors. You can use the tables below to get a rough idea of what it will take to run AnythingLLM.

AnythingLLM can be a wrapper around many external services that all accomplish some task - making AnythingLLM so lightweight it can run on the smallest machines - even Raspberry Pis!

#### Recommended configuration for AnythingLLM

This is the minimum value for running AnythingLLM. This will be enough for you to store some documents, send chats, and use AnythingLLM features.

| Property | Recommended Value |
| --- | --- |
| RAM | 2GB |
| CPU | 2-core CPU (any) |
| Storage | 5GB |

#### LLM selection impact

This is how you get chat responses. Popular hosted solutions like [OpenAI](https://openai.com/) tend to provide state-of-the-art responses with almost **zero overhead**. However, you will need an API key for any cloud-based LLM provider.

> **Tip:**
>
> **Tip:** Host a local LLM on another machine that has a GPU if the device
> running AnythingLLM does not have a GPU. AnythingLLM can connect to any LLM
> running anywhere via API.

#### Embedder selection impact

This is the model which you use to "**embed**" or vectorize text. Likewise, external services connected to AnythingLLM have **zero overhead** impact.

The default embedder runs on the same machine as AnythingLLM using **CPU-only** vectorization. If your documents are large or you need to vectorize a lot of data, you may want to use an external embedder provider and model.

#### Vector database selection impact

All supported vector databases either have no impact as they are externally hosted or can scale to hundreds of millions of vectors at the minimum recommended settings.

*the default LanceDB vector database can handle anything you can throw at it*


---

## LLM Configuration

### Overview

*Large language models are AI systems capable of understanding and generating human language by processing vast amounts of text data.*

**Source:** https://docs.useanything.com/setup/llm-configuration/overview

![LLM Configuration](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fheader-image.png&w=3840&q=100)

### Large Language Models

> **Tip:**
>
> **Tip:** Models that are multi-modal (text-to-text & image-to-text) are
> supported for System & Workspace models.

Large language models are AI systems capable of understanding and generating human language by processing vast amounts of text data.

#### Types of LLMs in AnythingLLM

AnythingLLM allows you to get as specific or general as you want with your LLM selection. You can even have multiple LLMs configured at the same time all in the same application!

##### System LLM

This is the default LLM AnythingLLM will interface with. This is the LLM configuration that will be used when a workspace or agent-specific agent LLM has not been defined.

##### Workspace LLM

AnythingLLM allows you to set workspace-specific LLMs, this will override the system LLM **but only when chatting with the specific workspace**. This allows you to have many workspaces that each have their own provider, model, or both!

##### Agent LLM

AnythingLLM supports AI-agents. When it comes to agents, not all LLMs were created equal. Some LLMs directly support tool calling for better ai-agent functionality. The model is the model that is explicitly used for use with agents.

#### Supported LLM Providers

AnythingLLM supports many LLMs out of the box with very little, if any setup.

The LLM is the foundational integration that will determine how your workspace or agents respond to your questions and prompts.

You can modify your LLM provider, model, or any other details at any time in AnythingLLM with no worry.

We allow you to connect to both local and cloud-based LLMs - even at the same time!

##### Local Language Model Providers

[![AnythingLLM Built-in (default)](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Fbuilt-in%2Fheader-image.png&w=3840&q=100)Built-in (default)→](https://docs.useanything.com/setup/llm-configuration/local/built-in)[![Ollama](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Follama%2Fheader-image.png&w=3840&q=100)Ollama→](https://docs.useanything.com/setup/llm-configuration/local/ollama)[![LM Studio](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Flmstudio%2Fheader-image.png&w=3840&q=100)LM Studio→](https://docs.useanything.com/setup/llm-configuration/local/lmstudio)[![Local AI](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Flocalai%2Fheader-image.png&w=3840&q=100)Local AI→](https://docs.useanything.com/setup/llm-configuration/local/localai)[![KobaldCPP](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Fkobaldcpp%2Fheader-image.png&w=3840&q=100)KobaldCPP→](https://docs.useanything.com/setup/llm-configuration/local/kobaldcpp)[![oMLX](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Fomlx%2Fheader-image.png&w=3840&q=100)oMLX→](https://docs.useanything.com/setup/llm-configuration/local/omlx)

##### Cloud Language Model Providers

[![OpenAI](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fopenai%2Fheader-image.png&w=3840&q=100)OpenAI→](https://docs.useanything.com/setup/llm-configuration/cloud/openai)[![Azure OpenAI](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fazure-openai%2Fheader-image.png&w=3840&q=100)Azure OpenAI→](https://docs.useanything.com/setup/llm-configuration/cloud/azure-openai)[![Anthropic](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fanthropic%2Fheader-image.png&w=3840&q=100)Anthropic→](https://docs.useanything.com/setup/llm-configuration/cloud/anthropic)[![Cohere](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fcohere%2Fheader-image.png&w=3840&q=100)Cohere→](https://docs.useanything.com/setup/llm-configuration/cloud/cohere)[![Google Gemini Pro](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fgoogle-gemini%2Fheader-image.png&w=3840&q=100)Google Gemini Pro→](https://docs.useanything.com/setup/llm-configuration/cloud/google-gemini)[![Hugging Face](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fhugging-face%2Fheader-image.png&w=3840&q=100)Hugging Face→](https://docs.useanything.com/setup/llm-configuration/cloud/huggingface)[![Together AI](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Ftogether-ai%2Fheader-image.png&w=3840&q=100)Together AI→](https://docs.useanything.com/setup/llm-configuration/cloud/together-ai)[![OpenRouter](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fopenrouter%2Fheader-image.png&w=3840&q=100)OpenRouter→](https://docs.useanything.com/setup/llm-configuration/cloud/openrouter)[![Perplexity AI](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fperplexity-ai%2Fheader-image.png&w=3840&q=100)Perplexity AI→](https://docs.useanything.com/setup/llm-configuration/cloud/perplexity-ai)[![Mistral API](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fmistral-ai%2Fheader-image.png&w=3840&q=100)Mistral API→](https://docs.useanything.com/setup/llm-configuration/cloud/mistral-ai)[![Groq](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fgroq%2Fheader-image.png&w=3840&q=100)Groq→](https://docs.useanything.com/setup/llm-configuration/cloud.groq)[![OpenAI (generic)](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fopenai-generic%2Fheader-image.png&w=3840&q=100)OpenAI (generic)→](https://docs.useanything.com/setup/llm-configuration/cloud/openai-generic)

### Anthropic LLM

*Anthropic is a model provider popular for hosting models like Claude-3 that boast much larger context windows and high-end performance.*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/anthropic

![Anthropic LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fanthropic%2Fheader-image.png&w=3840&q=100)

[Anthropic](https://Anthropic.com) is a model provider popular for hosting models like Claude-3 that boast much larger context windows and high-end performance.

#### Connecting to Anthropic

> **Tip:**
>
> **Valid API Key required!**
>
> You must obtain a valid API key from [console.anthropic.com](https://console.anthropic.com/) for this integration to work.

Like other LLM providers, the Chat Model Selection dropdown will automatically populate when your API key is entered.

All Anthropic models are currently available for use with AnythingLLM.

You can update your model to a different model at any time in the **Settings**.

![Anthropic LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fanthropic%2Fanthropic-llm.png&w=3840&q=100)

### APIpie

*Seamlessly access 100's of Open and Closed Source LLMs with APIpie — zero infrastructure, instant availability.*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/apipie

![APIpie](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fapipie%2Fheader-image.png&w=3840&q=100)

[APIpie](https://APIpie.ai) makes it easy to use any LLM without the hassle of infrastructure.

Whether you're experimenting or deploying in production, APIpie simplifies access to powerful models with a single endpoint.

#### Connecting to APIpie

> **Tip:**
>
> **Valid API Key required!**
>
> You must obtain a valid API key from [APIpie.ai](https://apipie.ai/profile/api-keys) for this integration to work.

Like other LLM providers, the Chat Model Selection dropdown will automatically populate when your API key is entered.

All APIpie models are currently available for use with AnythingLLM. [View the full list of models supported.](https://apipie.ai/dashboard)

You can update your model to a different model at any time in the **Settings**.

![APIPpie settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fapipie%2Fapipie.png&w=3840&q=100)

### AWS Bedrock LLM

*Use full-parameter foundational and custom models hosted on AWS via Bedrock for RAG + Agents.*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/aws-bedrock

![Azure OpenAI LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Faws-bedrock%2Fheader-image.png&w=3840&q=100)

AWS Bedrock offers a very simple deployment service of full state of the art foundational LLMs for you to run on your AWS account. While these models and their data should be private to your account each model does have its own EULA and can vary from model to model.

#### Connecting to AWS Bedrock

> **Tip:**
>
> **Valid account setup required!**
>
> You must have a valid [AWS Account](https://aws.amazon.com) to use AWS Bedrock - this service is not free.
>
> You **must** be an administrator or root user of the account to follow the below steps. Otherwise, consult with your account admin.

  
![AWS Bedrock LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Faws-bedrock%2Faws-bedrock-llm.png&w=3840&q=100)

##### Obtain API Key to use for Bedrock

AnythingLLM only supports AWS Bedrock via long-term API keys. Generate a new key from the AWS Bedrock console and set its expiry to whatever you feel comfortable with.

This will be the key you use to connect to AWS Bedrock in AnythingLLM to send chats and do agentic operations.

![AWS Bedrock API Key settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Faws-bedrock%2Faws-bedrock-api-key.png&w=3840&q=100)

Paste this key into the AnythingLLM interface as well as set the correct region if needed. You should see the model dropdown populated with the models available to you
for that key in that region.

##### AWS region

This is the region that your account is enabled to use with AWS Bedrock - this depends on your region preference and account settings.
An example is `us-west-2` Oregon. Yours may be elsewhere.

##### Model ID

This is the model id copied from the screenshot above.

##### Model context window

This is the maximum amount of tokens that can exist in a single query for a model. This is a model specific parameter and will vary from model to model.
Consult with AWS Bedrock's UI or the model provider documentation for what this limit may be.

### Azure OpenAI LLM

*Use GPT models in a private and enterprise environment that is managed by Microsoft.*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/azure-openai

![Azure OpenAI LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fazure-openai%2Fheader-image.png&w=3840&q=100)

Microsoft Azure OpenAI offers the same LLM models the base [OpenAI provider](https://docs.useanything.com/setup/llm-configuration/cloud/openai) does, but running on your Azure account with all privacy and agreements pertaining to that subscription.

#### Connecting to Azure OpenAI

> **Tip:**
>
> **Valid account setup required!**
>
> You must have a valid [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) subscription set up to use this integration.

It is possible to use Microsoft Azure for your LLM chat model.

This allows you to use GPT models in a private and enterprise environment that is managed by Microsoft.

You can update your model to a different model at any time in the **Settings**.

![Azure OpenAI LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fazure-openai%2Fazure-openai-llm.png&w=3840&q=100)

### Cohere LLM

*Cohere provides industry-leading large language models (LLMs) and RAG capabilities tailored to meet the needs of enterprise use cases that solve real-world problems*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/cohere

![Cohere LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fcohere%2Fheader-image.png&w=3840&q=100)

[Cohere](https://cohere.com/) provides industry-leading large language models (LLMs) and RAG capabilities tailored to meet the needs of enterprise use cases that solve real-world problems

#### Connecting to Cohere

> **Tip:**
>
> **Valid API Key required!**
>
> You must obtain a valid API key from [Cohere.com](https://cohere.com/) for this integration to work.

Like other LLM providers, the Chat Model Selection dropdown will automatically populate when your API key is entered.

All Cohere models are currently available for use with AnythingLLM.

You can update your model to a different model at any time in the **Settings**.

![Cohere LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fcohere%2Fcohere-llm.png&w=3840&q=100)

### Google Gemini LLM

*Google Gemini Pro is a model that runs with GPT equivalent responses and currently is free to use.*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/google-gemini

![Google Gemini LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fgoogle-gemini%2Fheader-image.png&w=3840&q=100)

[Google Gemini Pro](https://ai.google.dev/) is a model that runs with GPT equivalent responses and currently is free to use - you just need to sign up for an API key.

#### Connecting to Google Gemini

> **Tip:**
>
> **Valid API Key required!**
>
> You must obtain a valid API key from [ai.google.dev](https://ai.google.dev/) for this integration to work.

Like other LLM providers, the Chat Model Selection dropdown will automatically populate when your API key is entered.

All Google Gemini models are currently available for use with AnythingLLM.

You can update your model to a different model at any time in the **Settings**.

![Google Gemini LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fgoogle-gemini%2Fgemini-llm.png&w=3840&q=100)

### Groq LLM

*Groq AI is a model provider popular for pioneering the fastest way to run open-source models.*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/groq

![Groq LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fgroq%2Fheader-image.png&w=3840&q=100)

[Groq](https://groq.com) is a model provider popular for pioneering the fastest way to run open-source models.

This provider enables you to get near-instant replies back from your LLM.

If speed is your primary concern - there is no competition.

#### Connecting to Groq

> **Tip:**
>
> **Valid API Key required!**
>
> You must obtain a valid API key from [Groq AI](https://wow.groq.com/) for this integration to work.

Like other LLM providers, the Chat Model Selection dropdown will automatically populate when your API key is entered.

All Groq models are currently available for use with AnythingLLM.

You can update your model to a different model at any time in the **Settings**.

![Groq LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fgroq%2Fgroq-llm.png&w=3840&q=100)

### HuggingFace LLM

*HuggingFace is where the world puts open-source LLMs and other AI models online.*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/hugging-face

![Hugging Face LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fhugging-face%2Fheader-image.png&w=3840&q=100)

[HuggingFace](https://huggingface.co) is where the world puts open-source LLMs and other AI models online.

All of the raw model files of over 100,000 LLMs can be found here and run while connected to AnythingLLM.

#### Connecting to Hugging Face

> **Tip:**
>
> **Valid Configuration required!**
>
> This integration is specific to the HuggingFace serverless inference service that HuggingFace runs.

> **Tip:**
>
> **Tip:**
>
> This integration works best when a model's chat template is defined. You may get unexpected results otherwise.

You can update your model to a different model at any time in the **Settings**.

![Hugging Face LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fhugging-face%2Fhugging-face-llm.png&w=3840&q=100)

### Mistral AI LLM

*Mistral AI is the creator of the popular, uncensored, open-source Mistral-7B model.*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/mistral-ai

![Mistral AI LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fmistral-ai%2Fheader-image.png&w=3840&q=100)

[Mistral AI](https://mistral.ai/) is the creator of the popular, uncensored, open-source **Mistral-7B** model.

They provide an API for a simple interface that you can use for chatting.

#### Connecting to Mistral AI

> **Tip:**
>
> **Valid API Key required!**
>
> You must obtain a valid API key from [mistral.ai](https://mistral.ai/) for this integration to work.

> **Tip:**
>
> **Notice!**
>
> The API-based model is subject to censoring of sensitive topics, the open-source model is uncensored.
>
> To use the full model - use a local LLM provider like [LocalAI](https://docs.useanything.com/llms/localai), [LMStudio](https://docs.useanything.com/llms/lmstudio), or [Ollama](https://docs.useanything.com/llms/ollama)

Like other LLM providers, the Chat Model Selection dropdown will automatically populate when your API key is entered.

All Mistral models are currently available for use with AnythingLLM.

You can update your model to a different model at any time in the **Settings**.

![Mistral LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fmistral-ai%2Fmistral-llm.png&w=3840&q=100)

### OpenAI LLM

*OpenAI is the most popular closed-source option for many AnythingLLM users*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/openai

![OpenAI LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fopenai%2Fheader-image.png&w=3840&q=100)

[OpenAI](https://OpenAI.com) is the most popular closed-source option for many AnythingLLM users.

We support all of the current chat models for System, Workspace, and Agent execution.

#### Connecting to OpenAI

> **Tip:**
>
> **Valid API Key required!**
>
> You must obtain a valid API key from [platform.openai.com](https://platform.openai.com) for this integration to work.
>
> Ensure you also have attached a billing account or you may still be unable to use this provider.

All OpenAI models are currently available for use with AnythingLLM.

You can update your model to a different model at any time in the **Settings**.

![OpenAI LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fopenai%2Fopenai-llm.png&w=3840&q=100)

### OpenAI (Generic) LLM

*The Generic OpenAI wrapper is an easy way to interact with any LLM provider that we do not explicitly integrate with and is OpenAi-compatible in both API functionality and inference response.*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/openai-generic

![OpenAI (Generic) LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fopenai-generic%2Fheader-image.png&w=3840&q=100)

> **Note:**
>
> **Caution!**
>
> This is a developer-focused llm provider - you should not use it unless you know what you are doing.

The `Generic` OpenAI wrapper is an easy way to interact with any LLM provider that we do not explicitly integrate with and is `OpenAi-compatible` in both API functionality and inference response.

You should only use this provider if you know the LLM provider you wish it interact with is OpenAI compatible and you understand what each input is for.

#### Connecting to OpenAI (Generic)

> **Warning:**
>
> **Use with Caution**
>
> Generic OpenAI is a highly configurable and as such may not function as intended if you input any configuration setting incorrectly.

You can update your configuration at any time in the **Settings**.

![OpenAI (Generic) LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fopenai-generic%2Fopenai-generic-llm.png&w=3840&q=100)

### OpenRouter LLM

*OpenRouter is a model provider popular for hosting open-source LLM models with zero infra all in one simple place*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/openrouter

![OpenRouter LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fopenrouter%2Fheader-image.png&w=3840&q=100)

[OpenRouter](https://openrouter.ai) is a model provider popular for hosting open-source LLM models with zero infra all in one simple place.

The minute a new model is live - it will appear on OpenRouter first.

#### Connecting to OpenRouter

> **Tip:**
>
> **Valid API Key required!**
>
> You must obtain a valid API key from [openrouter.ai](https://openrouter.ai/) for this integration to work.

Like other LLM providers, the Chat Model Selection dropdown will automatically populate when your API key is entered.

All OpenRouter models are currently available for use with AnythingLLM.

You can update your model to a different model at any time in the **Settings**.

![OpenRouter LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2FOpenRouter%2FOpenRouter-llm.png&w=3840&q=100)

### Perplexity AI LLM

*Perplexity AI is a model provider popular internet-enabled models which seem to always have the most up-to-date response with no-RAG required for current and public information.*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/perplexity-ai

![Perplexity AI LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fperplexity-ai%2Fheader-image.png&w=3840&q=100)

[Perplexity AI](https://www.perplexity.ai/) is a model provider popular "internet-enabled" models which seem to always have the most up-to-date response with no-RAG required for current and public information.

#### Connecting to Perplexity AI

> **Tip:**
>
> **Valid API Key required!**
>
> You must obtain a valid API key from [perplexity.ai](https://www.perplexity.ai/) for this integration to work.

Like other LLM providers, the Chat Model Selection dropdown will automatically populate when your API key is entered.

All Perplexity AI models are currently available for use with AnythingLLM.

You can update your model to a different model at any time in the **Settings**.

![Perplexity AI LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Fperplexity-ai%2Fperplexityai-llm.png&w=3840&q=100)

### Together AI LLM

*Together AI is an online service that provides API access to hundreds of various open-source models without having to spin up any infrastructure yourself.*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/together-ai

![Together AI LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Ftogether-ai%2Fheader-image.png&w=3840&q=100)

[Together AI](https://www.together.ai/) is an online service that provides API access to hundreds of various open-source models without having to spin up any infrastructure yourself.

#### Connecting to Together AI

> **Tip:**
>
> **Valid API Key required!**
>
> You must obtain a valid API key from [Together.ai](https://www.Together.ai/) for this integration to work.

Like other LLM providers, the Chat Model Selection dropdown will automatically populate when your API key is entered.

All Together AI models are currently available for use with AnythingLLM. [View the full list of models supported.](https://docs.together.ai/docs/inference-models#chat-models)

You can update your model to a different model at any time in the **Settings**.

![Together AI LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Fcloud%2Ftogether-ai%2Ftogetherai-llm.png&w=3840&q=100)

### TrueFoundry AI gateway

*All-in-one AI application that can do RAG, AI Agents, and much more with no code or infrastructure headaches.*

**Source:** https://docs.useanything.com/setup/llm-configuration/cloud/truefoundry

TrueFoundry provides an enterprise-ready [AI Gateway](https://www.truefoundry.com/ai-gateway) which can integrate with applications like AnythingLLM and provides governance and observability for your AI Applications. TrueFoundry AI Gateway serves as a unified interface for LLM access, providing:

- **Unified API Access**: Connect to 250+ LLMs (OpenAI, Claude, Gemini, Groq, Mistral) through one API
- **Low Latency**: Sub-3ms internal latency with intelligent routing and load balancing
- **Enterprise Security**: SOC 2, HIPAA, GDPR compliance with RBAC and audit logging
- **Quota and cost management**: Token-based quotas, rate limiting, and comprehensive usage tracking
- **Observability**: Full request/response logging, metrics, and traces with customizable retention

#### Prerequisites

Before integrating AnythingLLM with TrueFoundry, ensure you have:

1. **TrueFoundry Account**: Create a [Truefoundry account](https://www.truefoundry.com/register) and follow our [Quick Start Guide](https://docs.truefoundry.com/gateway/quick-start)
2. **AnythingLLM Installation**: Set up AnythingLLM using either the [Desktop application](https://anythingllm.com/download) or [Docker deployment](https://github.com/Mintplex-Labs/anything-llm)

#### Integration Steps

This guide assumes you have AnythingLLM installed and running, and have obtained your TrueFoundry AI Gateway base URL and authentication token.

##### Step 1: Access AnythingLLM LLM Settings

1. Launch your AnythingLLM application (Desktop or Docker).
2. Navigate to **Settings** and go to **LLM Preference**:

![AnythingLLM settings page showing LLM provider selection interface](https://docs.useanything.com/_next/image?url=%2Fimages%2Fsetup%2Fllm-providers%2Ftruefoundry%2Fllmprovider.png&w=2048&q=75)

##### Step 3: Configure Generic OpenAI Provider

1. In the LLM provider search box, type "Generic OpenAI" and select it from the available options.
2. Configure the TrueFoundry connection with the following settings:

   - **Base URL**: Enter your TrueFoundry Gateway base URL (e.g., `https://internal.devtest.truefoundry.tech/api/llm/api/inference/openai`)
   - **API Key**: Enter your TrueFoundry Personal Access Token
   - **Chat Model Name**: Enter the model name from the unified code snippet (e.g., `openai-main/gpt-4o`)
   - **Token Context Window**: Set based on your model's limits (e.g., 16000, 128000)
   - **Max Tokens**: Configure according to your needs (e.g., 1024, 2048)

##### Step 4: Get Configuration from TrueFoundry

Get the api key, base URL and model name from the unified code snippet in our playground (ensure you use the same model name as written):

![Get API key, Base URL and Model Name from Unified Code Snippet](https://docs.useanything.com/_next/image?url=%2Fimages%2Fsetup%2Fllm-providers%2Ftruefoundry%2Fnew-code-snippet.png&w=2048&q=75)

Copy the api key, base URL and model ID and paste them into AnythingLLM's configuration fields.

##### Step 5: Test Your Integration

1. Save your configuration in AnythingLLM.
2. Create a new workspace or open an existing one to test the integration:

![AnythingLLM chat interface showing successful test message with TrueFoundry integration](https://docs.useanything.com/_next/image?url=%2Fimages%2Fsetup%2Fllm-providers%2Ftruefoundry%2Ftest-anythingllm.png&w=2048&q=75)

3. Send a test message to verify that AnythingLLM is successfully communicating with TrueFoundry's AI Gateway.

Your AnythingLLM application is now integrated with TrueFoundry's AI Gateway and ready for AI chat, RAG, and agent operations.

### AnythingLLM Default LLM

*AnythingLLM ships with a built-in LLM engine and provider that enables you to download popular and highly-rated LLMs like LLama-3, Phi-3 and more that can run locally on your CPU and GPU.*

**Source:** https://docs.useanything.com/setup/llm-configuration/local/built-in

![AnythingLLM Default LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Fbuilt-in%2Fheader-image.png&w=3840&q=100)

> **Tip:**
>
> **DESKTOP ONLY!**
>
> This default llm provider feature is only present on Desktop Version of AnythingLLM

AnythingLLM ships with a built-in LLM engine and provider that enables you to download popular and highly-rated LLMs like LLama-3, Phi-3 and more that can run locally on your CPU and GPU.

When you boot up AnythingLLM Desktop you will be able to select the model you wish to download. Its progress will be tracked in the top-right of the application window.

You can update your model to a different model at any time in the **Settings**.

![AnythingLLM Default LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Fbuilt-in%2Fdefault-llm.png&w=3840&q=100)

### KobaldCPP LLM

*KobaldCPP is a simple one-file way to run various GGML and GGUF models with KoboldAI's UI*

**Source:** https://docs.useanything.com/setup/llm-configuration/local/kobaldcpp

![KobaldCPP LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Fkobaldcpp%2Fheader-image.png&w=3840&q=100)

[KobaldCPP](https://KobaldCPP.com) is a simple one-file way to run various GGML and GGUF models with KoboldAI's UI

KobaldCPP is a *separate* application that you need to download first and connect to.

#### Connecting to KobaldCPP

You can update your model to a different model at any time in the **Settings**.

![KobaldCPP LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Fkobaldcpp%2Fkobaldcpp-llm.png&w=3840&q=100)

### LMStudio LLM

*LMStudio is a popular user-interface, API, and LLM engine that allows you to download any GGUF model from HuggingFace and run it on CPU or GPU.*

**Source:** https://docs.useanything.com/setup/llm-configuration/local/lmstudio

![LMStudio LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Flmstudio%2Fheader-image.png&w=3840&q=100)

[LMStudio](https://lmstudio.ai) is a popular user-interface, API, and LLM engine that allows you to download any GGUF model from HuggingFace and run it on CPU or GPU.

LMStudio is a *separate* application that you need to download first and connect to.

#### Connecting to LMStudio

When running LMStudio locally, you **should** connect to LMStudio by first running the built-in inference server.

You can update your model to a different model at any time in the **Settings**.

![LMStudio LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Flmstudio%2Flmstudio-llm.png&w=3840&q=100)

### Local AI LLM

*LocalAI is a popular open-source, API, and LLM engine that allows you to download and run any GGUF model from HuggingFace and run it on CPU or GPU.*

**Source:** https://docs.useanything.com/setup/llm-configuration/local/localai

![Local AI LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Flocalai%2Fheader-image.png&w=3840&q=100)

[LocalAI](https://localai.io) is a popular [open-source](https://github.com/mudler/LocalAI), API, and LLM engine that allows you to download and run any GGUF model from HuggingFace and run it on CPU or GPU.

LocalAI supports both LLMs, Embedding models, and image-generation models.

#### Connecting to Local AI

LocalAI is a Docker container image that you must configure and run.

You can update your model to a different model at any time in the **Settings**.

![Local AI LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Flocalai%2Flocalai-llm.png&w=3840&q=100)

### Ollama LLM

*Ollama is a popular open-source command-line tool and engine that allows you to download quantized versions of the most popular LLM chat models*

**Source:** https://docs.useanything.com/setup/llm-configuration/local/ollama

![Ollama LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Follama%2Fheader-image.png&w=3840&q=100)

[Ollama](https://ollama.com) is a popular [open-source](https://github.com/ollama/ollama) command-line tool and engine that allows you to download quantized versions of the most popular LLM chat models.

Ollama is a *separate* application that you need to download first and connect to. Ollama supports both running LLMs on CPU and GPU.

#### Connecting to Ollama

When running ollama locally, you should connect to Ollama with `http://127.0.0.1:11434` when using the default settings.

You can update your model to a different model at any time in the **Settings**.

![Ollama LLM settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Follama%2Follama-llm.png&w=3840&q=100)

### oMLX LLM

*oMLX is an LLM inference server for Apple Silicon Macs built on MLX, with continuous batching and SSD caching - managed from the macOS menu bar.*

**Source:** https://docs.useanything.com/setup/llm-configuration/local/omlx

![oMLX LLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fllm-configuration%2Flocal%2Fomlx%2Fheader-image.png&w=3840&q=100)

[oMLX](https://omlx.ai/) is an LLM inference server for Apple Silicon Macs built on [MLX](https://github.com/ml-explore/mlx), Apple's machine learning framework. It supports continuous batching for concurrent requests, a tiered KV cache (RAM + SSD), multi-model serving, and is managed from the macOS menu bar.

oMLX is a *separate* application that you need to download and run first before connecting to it.

#### Connecting to oMLX

When running oMLX locally, you **should** first start the oMLX server with at least one MLX model available. By default, the server runs at `http://localhost:8000`.

Select **oMLX** as your LLM provider in AnythingLLM. The base URL will be auto-detected when the server is running, or you can set it manually under advanced settings. Then select the model you want to use from the list of models available on your oMLX server.

The model's context window is automatically detected and cached, but you can override it manually under advanced settings. If your oMLX server requires authentication, you can also provide an API key there.

You can update your model to a different model at any time in the **Settings**.


---

## Embedding Model Configuration

### Overview

*Embedding models are specific types of models that turn text into vectors, which can be stored and searched in a vector database - which is the foundation of RAG.*

**Source:** https://docs.useanything.com/setup/embedder-configuration/overview

![Embedder Configuration](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Fheader-image.png&w=3840&q=100)

### Embedder Configuration

Embedding models are specific types of models that turn text into vectors, which can be stored and searched in a vector database - which is the foundation of RAG.

> **Tip:**
>
> **Tip:**
>
> Embedding models are set system-wide and cannot be configured atomically per-workspace like LLMs can.

#### Supported Embedding Model Providers

> **Warning:**
>
> **HEADS UP!**
>
> Once you select your embedding model provider and begin uploading and embedding documents it is best to not change it.
>
> While you can change embedders, doing so will mean you will have to delete your uploaded documents and re-embed them so the new embedder can re-embed them.

AnythingLLM supports many embedding model providers out of the box with very little, if any setup.

You can modify your embedding provider and model at any time in AnythingLLM. However doing so can result in broken queries and needing to re-embed uploaded and stored documents.

##### Local Embedding Model Providers

[![AnythingLLM Built-in (default)](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Flocal%2Fbuilt-in%2Fheader-image.png&w=3840&q=100)Built-in (default)→](https://docs.useanything.com/setup/embedder-configuration/local/built-in)[![Ollama](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Flocal%2Follama%2Fheader-image.png&w=3840&q=100)Ollama→](https://docs.useanything.com/setup/embedder-configuration/local/ollama)[![LM Studio](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Flocal%2Flmstudio%2Fheader-image.png&w=3840&q=100)LM Studio→](https://docs.useanything.com/setup/embedder-configuration/local/lmstudio)[![Local AI](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Flocal%2Flocalai%2Fheader-image.png&w=3840&q=100)Local AI→](https://docs.useanything.com/setup/embedder-configuration/local/localai)

##### Cloud Model Providers

[![OpenAI](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Fcloud%2Fopenai%2Fheader-image.png&w=3840&q=100)OpenAI→](https://docs.useanything.com/setup/embedder-configuration/cloud/openai)[![Azure OpenAI](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Fcloud%2Fazure-openai%2Fheader-image.png&w=3840&q=100)Azure OpenAI→](https://docs.useanything.com/setup/embedder-configuration/cloud/azure-openai)[![Cohere](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Fcloud%2Fcohere%2Fheader-image.png&w=3840&q=100)Cohere→](https://docs.useanything.com/setup/embedder-configuration/cloud/cohere)

### Azure OpenAI Embedder

*Microsoft Azure OpenAI offers the same embedding models the base OpenAI provider does, but running on your Azure account.*

**Source:** https://docs.useanything.com/setup/embedder-configuration/cloud/azure-openai

![Azure OpenAI Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Fcloud%2Fazure-openai%2Fheader-image.png&w=3840&q=100)

Microsoft Azure OpenAI offers the same embedding models the base [OpenAI provider](https://docs.useanything.com/setup/embedder-configuration/cloud/openai) does, but running on your Azure account with all privacy and agreements pertaining to that subscription.

#### Connecting to Azure OpenAI

> **Tip:**
>
> **Valid account setup required!**
>
> You must have a valid [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) subscription set up to use this integration.

You can update your model to a different model at any time in the **Settings**.

![Azure OpenAI Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Fcloud%2Fazure-openai%2Fazure-openai-embedder.png&w=3840&q=100)

### Cohere Embedder

*Cohere provides industry-leading large language models (LLMs) and Embedding models tailored to meet the needs of enterprise use cases that solve real-world problems*

**Source:** https://docs.useanything.com/setup/embedder-configuration/cloud/cohere

![Cohere Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Fcloud%2Fcohere%2Fheader-image.png&w=3840&q=100)

[Cohere](https://cohere.com/) provides industry-leading large language models (LLMs) and Embedding models tailored to meet the needs of enterprise use cases that solve real-world problems

#### Connecting to Cohere

> **Tip:**
>
> **Valid API Key required!**
>
> You must obtain a valid API key from [Cohere.com](https://cohere.com/) to use this integration.

All Cohere models are currently available for use with AnythingLLM.

You can update your model to a different model at any time in the **Settings**.

![Cohere Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Fcloud%2Fcohere%2Fcohere-embedder.png&w=3840&q=100)

### OpenAI Embedder

*OpenAI offers 3 embedding models that vary between performance and dimension..*

**Source:** https://docs.useanything.com/setup/embedder-configuration/cloud/openai

![OpenAI Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Fcloud%2Fopenai%2Fheader-image.png&w=3840&q=100)

OpenAI offers 3 embedding models that vary between performance and dimension. Check with OpenAI for up to date pricing.

When you attempt to embed documents in AnythingLLM we will provide a price estimate.

| MODEL | ~ PAGES PER DOLLAR | MAX INPUT |
| --- | --- | --- |
| text-embedding-3-small | 62,500 | 8,191 |
| text-embedding-ada-002 | 12,500 | 8,191 |
| text-embedding-3-large | 9,615 | 8,191 |

#### Connecting to OpenAI

> **Tip:**
>
> **Valid API Key required!**
>
> You must obtain a valid API key from [platform.openai.com](https://platform.openai.com) for this integration to work.
>
> Ensure you also have attached a billing account or you may still be unable to use this provider.

You can update your model to a different model at any time in the **Settings**.

![OpenAI Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Fcloud%2Fopenai%2Fopenai-embedder.png&w=3840&q=100)

### AnythingLLM Default Embedder

*AnythingLLM ships with a built-in embedder model that runs on CPU*

**Source:** https://docs.useanything.com/setup/embedder-configuration/local/built-in

![AnythingLLM Default Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Flocal%2Fbuilt-in%2Fheader-image.png&w=3840&q=100)

> **Warning:**
>
> **Heads up!**
>
> This embedding model will download (25mb) on the very first embed **and** runs on CPU. You should have at least 2GB of RAM available to ensure the process does not bottleneck.

AnythingLLM ships with a built-in embedder model that runs on CPU.

The model is the popular [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model, which is primarily trained on English documents.

![AnythingLLM Default Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Flocal%2Fbuilt-in%2Fdefault-embedder.png&w=3840&q=100)

### LM Studio Embedder

*LMStudio supports LLM and embedding GGUF models from HuggingFace that can be run on CPU or GPU.*

**Source:** https://docs.useanything.com/setup/embedder-configuration/local/lmstudio

![LM Studio Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Flocal%2Flmstudio%2Fheader-image.png&w=3840&q=100)

[LMStudio](https://lmstudio.ai) supports LLM **and** embedding GGUF models from HuggingFace that can be run on CPU or GPU.

LMStudio is a *separate* application that you need to download first and connect to.

#### Connecting to LM Studio

When running LMStudio locally, you should connect to LMStudio by first running the built-in inference server.

You **must** explicitly load the embedding model before starting the inference server.

You can update your model to a different model at any time in the **Settings**.

![LM Studio Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Flocal%2Flmstudio%2Flmstudio-embedder.png&w=3840&q=100)

### Local AI Embedder

*LocalAI is both an LLM engine and supports running embedding models on CPU and GPU*

**Source:** https://docs.useanything.com/setup/embedder-configuration/local/localai

![Local AI Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Flocal%2Flocalai%2Fheader-image.png&w=3840&q=100)

[LocalAI](https://localai.io) is both an LLM engine **and** supports running embedding models on CPU and GPU. Any HuggingFace model or GGUF embedding model can be used.

This can be configured independently of the LocalAI LLM setting and can be used for both at the same time.

You can update your model to a different model at any time in the **Settings**.

![Local AI Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Flocal%2Flocalai%2Flocalai-embedder.png&w=3840&q=100)

### Ollama Embedder

*Ollama supports the running of both LLMs and embedding models.*

**Source:** https://docs.useanything.com/setup/embedder-configuration/local/ollama

![Ollama Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Flocal%2Follama%2Fheader-image.png&w=3840&q=100)

> **Note:**
>
> **Heads up!**
>
> Ollama's `/models` endpoint will show both LLMs and Embedding models in the dropdown selection. **Please** ensure you are using an embedding model for embedding.
>
> **llama2** for example, is an LLM. Not an embedder.

#### Connecting to Ollama

When running ollama locally, you should connect to Ollama with `http://127.0.0.1:11434` when using the default settings.

[Ollama](https://ollama.com) supports the running of both LLMs **and** embedding models.

Please download the relevant embedding model you wish to use and select that during onboarding or in **Settings** to have your uploaded documents embed via Ollama.

You can update your model to a different model at any time in the **Settings**.

![Ollama Embedder](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fembedder-configuration%2Flocal%2Follama%2Follama-embedder.png&w=3840&q=100)


---

## Vector Database Configuration

### Vector Databases

*Your vector database is set system-wide and cannot be configured atomically per-workspace like LLMs can..*

**Source:** https://docs.useanything.com/setup/vector-database-configuration/overview

![AnythingLLM Vector Databases](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Fheader-image.png&w=3840&q=100)

Your vector database is set system-wide and cannot be configured atomically per-workspace like LLMs can.

> **Note:**
>
> **Caution!**
>
> You should prevent "hopping" between vector databases. AnythingLLM will not automatically port over your already embedded information.
>
> You would need to delete and re-embed each document in every workspace to migrate to another vector database.

AnythingLLM supports many vector databases providers out of the box.

#### Supported Vector Databases

##### Local Vector Databases Providers

[![LanceDB](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Flancedb.png&w=3840&q=100)LanceDB (Built-in)→](https://docs.useanything.com/setup/vector-database-configuration/local/lancedb)[![Chroma](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fchroma.png&w=3840&q=100)Chroma→](https://docs.useanything.com/setup/vector-database-configuration/local/chroma)[![Milvus](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fmilvus.png&w=3840&q=100)Milvus→](https://docs.useanything.com/setup/vector-database-configuration/local/milvus)

##### Cloud Vector Databases Providers

[![Pinecone](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fpinecone.png&w=3840&q=100)Pinecone→](https://docs.useanything.com/setup/vector-database-configuration/cloud/pinecone)[![Zilliz](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fzilliz.png&w=3840&q=100)Zilliz→](https://docs.useanything.com/setup/vector-database-configuration/cloud/zilliz)[![AstraDB](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fastra-db.png&w=3840&q=100)AstraDB→](https://docs.useanything.com/setup/vector-database-configuration/cloud/astradb)[![QDrant](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fqdrant.png&w=3840&q=100)QDrant→](https://docs.useanything.com/setup/vector-database-configuration/cloud/qdrant)[![Weaviate](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fweaviate.png&w=3840&q=100)Weaviate→](https://docs.useanything.com/setup/vector-database-configuration/cloud/weaviate)

### AstraDB Vector Database

*Astra DB is a vector database for developers, that can be used to get Generative AI applications into production quickly.*

**Source:** https://docs.useanything.com/setup/vector-database-configuration/cloud/astradb

![AstraDB Vector Database](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Fcloud%2Fastradb%2Fheader-image.png&w=3840&q=100)

[Astra DB](https://www.datastax.com/products/datastax-astra) is a vector database for developers, that can be used to get Generative AI applications into production quickly

#### Connecting to AstraDB Vector Database

You can configure AstraDB in the **Settings**.

![AstraDB Vector Database Settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Fcloud%2Fastradb%2Fastradb-vectordb.png&w=3840&q=100)

### Pinecone Vector Database

*Pinecone is the developer-favorite vector database that's fast and easy to use at any scale.*

**Source:** https://docs.useanything.com/setup/vector-database-configuration/cloud/pinecone

![Pinecone Vector Database](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Fcloud%2Fpinecone%2Fheader-image.png&w=3840&q=100)

[Pinecone](https://www.pinecone.io/) is the developer-favorite vector database that's fast and easy to use at any scale.

Pinecone serves fresh, filtered query results with low latency at the scale of billions of vectors.

#### Connecting to Pinecone Vector Database

You can configure Pinecone in the **Settings**.

![Pinecone Vector Database Settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Fcloud%2Fpinecone%2Fpinecone-vectordb.png&w=3840&q=100)

### QDrant Vector Database

*Qdrant is a vector database & vector similarity search engine. It deploys as an API service providing search for the nearest high-dimensional vectors.*

**Source:** https://docs.useanything.com/setup/vector-database-configuration/cloud/qdrant

![QDrant Vector Database](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Fcloud%2Fqdrant%2Fheader-image.png&w=3840&q=100)

[Qdrant](https://qdrant.tech/) is a vector database & vector similarity search engine.

It deploys as an API service providing search for the nearest high-dimensional vectors.

#### Connecting to QDrant Vector Database

You can configure QDrant in the **Settings**.

![QDrant Vector Database Settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Fcloud%2Fqdrant%2Fqdrant-vectordb.png&w=3840&q=100)

### Weaviate Vector Database

*Weaviate is an open source vector database which allows you to store and retrieve data objects based on their semantic properties by indexing them with vectors.*

**Source:** https://docs.useanything.com/setup/vector-database-configuration/cloud/weaviate

![Weaviate Vector Database](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Fcloud%2Fweaviate%2Fheader-image.png&w=3840&q=100)

[Weaviate](https://weaviate.io/) is an open source vector database which allows you to store and retrieve data objects based on their semantic properties by indexing them with vectors.

#### Connecting to Weaviate Vector Database

You can configure Weaviate in the **Settings**.

![Weaviate Vector Database Settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Fcloud%2Fweaviate%2Fweaviate-vectordb.png&w=3840&q=100)

### Zilliz Vector Database

*Zilliz is a leading vector database company for production-ready AI which is built by the engineers who created Milvus*

**Source:** https://docs.useanything.com/setup/vector-database-configuration/cloud/zilliz

![Zilliz Vector Database](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Fcloud%2Fzilliz%2Fheader-image.png&w=3840&q=100)

[Zilliz](https://zilliz.com/) is a open source vector database which is built by the engineers who created [Milvus](https://milvus.io/)

#### Connecting to Zilliz Vector Database

You can configure Zilliz in the **Settings**.

![Zilliz Vector Database Settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Fcloud%2Fzilliz%2Fzilliz-vectordb.png&w=3840&q=100)

### Chroma Vector Database

*Chroma is an open-source and ai-native vector database that is easy to run and host anywhere.*

**Source:** https://docs.useanything.com/setup/vector-database-configuration/local/chroma

![Chroma Vector Database](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Flocal%2Fchroma%2Fheader-image.png&w=3840&q=100)

[Chroma](https://trychroma.com) is an [open-source](https://github.com/chroma-core/chroma) and ai-native vector database that is easy to run and host anywhere.

AnythingLLM can connect to your local or cloud-hosted Chroma instance running so that AnythingLLM can store and search embeddings on it automatically.

#### Connecting to Chroma Vector Database

> **Warning:**
>
> **Developer Notice**
>
> Chroma [requires a server](https://docs.trychroma.com/usage-guide#running-chroma-in-clientserver-mode) to be running so that Chroma can embed or index your embeddings automatically.
>
> AnythingLLM will use the embedding model set and **will not** use Chroma's built-in embedders even if defined.

You can configure Chroma at any time in the **Settings**.

![Chroma Vector Database Settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Flocal%2Fchroma%2Fchroma-vectordb.png&w=3840&q=100)

#### How to run Chroma Locally via Docker

  

[Embedded video/content](https://www.youtube.com/embed/61kaK-e3Owc?si=5mdkTqKCZG4Nvn0-)

### Lance DB Vector Database

*LanceDB can scale to millions of vectors all on disk with zero configuration and incredible retrieval speed.*

**Source:** https://docs.useanything.com/setup/vector-database-configuration/local/lancedb

![Lance DB Vector Database](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Flocal%2Flancedb%2Fheader-image.png&w=3840&q=100)

LanceDB can scale to millions of vectors all on disk with zero configuration and incredible retrieval speed.

> **Tip:**
>
> **HEADS UP!**
>
> By default, AnythingLLM will use an open-source on-instance of [LanceDB](https://lancedb.com/) vector database so that your document text and embeddings never leave the AnythingLLM application.

#### Connecting to Lance DB

There is no configuration or options required for LanceDB

![Lance DB Vector Database Settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Flocal%2Flancedb%2Flancedb-vectordb.png&w=3840&q=100)

### Milvus Vector Database

*Milvus is an open-source vector database built to power embedding similarity search and AI applications.*

**Source:** https://docs.useanything.com/setup/vector-database-configuration/local/milvus

![Milvus Vector Database](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Flocal%2Fmilvus%2Fheader-image.png&w=3840&q=100)

[Milvus](https://github.com/milvus-io/milvus) is an open-source vector database built to power embedding similarity search and AI applications.

Milvus makes unstructured data search more accessible, and provides a consistent user experience regardless of the deployment environment.

#### Connecting to Milvus Vector Database

You can configure Milvus at any time in the **Settings**.

![Milvus Vector Database Settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fvector-database-configuration%2Flocal%2Fmilvus%2Fmilvus-vectordb.png&w=3840&q=100)


---

## Transcription Model Configuration

### Transcription Models

*AnythingLLM supports custom audio transcription providers.*

**Source:** https://docs.useanything.com/setup/transcription-model-configuration/overview

![AnythingLLM Transcription Models](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Ftranscription-model-configuration%2Fheader-image.png&w=3840&q=100)

AnythingLLM supports custom audio transcription providers.

#### Supported Transcription Model Providers

##### Local Transcription Model Providers

[![AnythingLLM Built-in (Xenova)](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Ftranscription-model-configuration%2Flocal%2Fbuilt-in%2Fheader-image.png&w=3840&q=100)Built-in (Xenova)→](https://docs.useanything.com/setup/transcription-model-configuration/local/built-in)

##### Cloud Transcription Model Providers

[![OpenAI](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Ftranscription-model-configuration%2Fcloud%2Fopenai%2Fheader-image.png&w=3840&q=100)OpenAI→](https://docs.useanything.com/setup/transcription-model-configuration/cloud/openai)

### OpenAI Transcription Model

*AnythingLLM ships with a built-in LLM engine and provider that enables you to download popular and highly-rated LLMs like LLama-3, Phi-3 and more that can run locally on your CPU and GPU.*

**Source:** https://docs.useanything.com/setup/transcription-model-configuration/cloud/openai

![OpenAI Transcription Model](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Ftranscription-model-configuration%2Fcloud%2Fopenai%2Fheader-image.png&w=3840&q=100)

[OpenAI](https://OpenAI.com) is the most popular closed-source option for many AnythingLLM users.

#### Connecting to OpenAI

> **Tip:**
>
> **Valid API Key required!**
>
> You must obtain a valid API key from [platform.openai.com](https://platform.openai.com) for this integration to work.
>
> Ensure you also have attached a billing account or you may still be unable to use this provider.

All OpenAI transcription models are currently available for use with AnythingLLM.

![OpenAI Transcription Model](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Ftranscription-model-configuration%2Fcloud%2Fopenai%2Fopenai-transcription.png&w=3840&q=100)

### AnythingLLM Default Transcription Model

*AnythingLLM ships with a built-in LLM engine and provider that enables you to download popular and highly-rated LLMs like LLama-3, Phi-3 and more that can run locally on your CPU and GPU.*

**Source:** https://docs.useanything.com/setup/transcription-model-configuration/local/built-in

![AnythingLLM Default Transcription Model](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Ftranscription-model-configuration%2Flocal%2Fbuilt-in%2Fheader-image.png&w=3840&q=100)

> **Tip:**
>
> **Note:**
>
> Using the local whisper model on machines with limited RAM or CPU can stall AnythingLLM when processing media files.
> We recommend at least 2GB of RAM and upload files less than 10MB.

AnythingLLM ships with a built-in Transcription Model [Xenova Whisper](https://huggingface.co/Xenova/whisper-small) which will automatically download on the first use.

![AnythingLLM Default Transcription Model Settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Ftranscription-model-configuration%2Flocal%2Fbuilt-in%2Fdefault-transcription.png&w=3840&q=100)


---

## Core Configuration

### Configuration

*Other settings, environment variables, and configurations for AnythingLLM*

**Source:** https://docs.useanything.com/configuration

> **Warning:**
>
> **Warning:**
> If you are not a developer, you should not set environment variables directly. Instead, you should use the in-app interface to manage environment variables.
>
> **Desktop:**
> If you are using AnythingLLM Desktop, do not edit the `.env` file. This guide is only for users who are using AnythingLLM Self-hosted or Docker.

### Configuration of AnythingLLM

In general, the majority of configurations you can set are through environment variables and there is typically an associated in-app interface to manage these settings so you don't have to edit them directly.

However, there are a few configurations that are not configurable via the in-app interface and require you to set environment variables directly. These are usually for more niche use cases that most users will not need.

> **Tip:**
>
> **Tip:** After you set these environment variables, you will need to restart
> the AnythingLLM service or container for the changes to take effect.

#### Disable View Chat History

Modification of the `DISABLE_VIEW_CHAT_HISTORY` environment variable allows you to disable the **frontend** ability to view chat history by anyone with an account on the instance as well as the instance administrator.
This blocks any user, including yourself, from viewing chat history from users using the AnythingLLM chat interface **and** via external embed widgets.

- **This does not impact users from seeing their own chat histories in chat or the LLM from being able to use them for continuous conversations.**
- This **does not** impact the ability to use API keys to access chat histories via the associated API endpoints.
- This will impact the ability to export chat histories via the in-app interface as well as the ability to delete chat histories.
- **Chat history is not deleted when this is enabled. It is simply hidden and blocked from being viewed via the frontend admin interfaces.**

##### Enable

Set the `DISABLE_VIEW_CHAT_HISTORY` environment variable to ***any value*** to enable.

```
### This can be any value, number, boolean, or string and it will have the same effect.
DISABLE_VIEW_CHAT_HISTORY="enable"
```

##### Disable

Fully remove or comment out the `DISABLE_VIEW_CHAT_HISTORY` environment variable to return to the default behavior.

#### Workspace Deletion Protection

Modification of the `WORKSPACE_DELETION_PROTECTION` environment variable prevents workspaces from being deleted from both the frontend UI and the API.

- This hides the delete workspace button in workspace settings as well as the delete action in the admin workspaces interface.
- This blocks workspace deletion via the developer API endpoint (`DELETE /v1/workspace/:slug`), which will return a `403` error.
- **No workspaces or their data are deleted when this is enabled. Existing workspaces are simply protected from being removed.**

##### Enable

Set the `WORKSPACE_DELETION_PROTECTION` environment variable to ***any value*** to enable.

```
### This can be any value, number, boolean, or string and it will have the same effect.
WORKSPACE_DELETION_PROTECTION="enable"
```

##### Disable

Fully remove or comment out the `WORKSPACE_DELETION_PROTECTION` environment variable to return to the default behavior.

#### Simple SSO Passthrough

> **Note:**
>
> **Important:** You should use an independent API key for using this feature so
> you can revoke it if needed. This feature configuration is best used for
> internally facing AnythingLLM instances that are not exposed to the public
> internet for the best security practices.

Modification of the `SIMPLE_SSO_ENABLED` environment variable allows easily enable third party SSO solutions that do not require a full OAuth integration. This environment variable
will enable you to generate a temporary authentication link **per user** that can be visited in browser to automatically login the user.

This feature is most useful for when you have AnythingLLM as a simple sub-service within a much larger system and you want to leverage existing user authentication flows within that system and want to provide a seamless login experience for your users to your AnythingLLM instance.

##### Prerequisites

> **Warning:**
>
> **NOTE:** You should enable these configurations *after* you have enabled multi-user mode, created at least one `admin` user, and have completed the onboarding flow
> in the AnythingLLM instance.
>
>   
>
> Do **not** enabled these configurations before you have done this or else you may find yourself soft-locked out of the instance until you disable these flags.

- **Your instance must be in multi-user mode** to use this feature.
- You should provision an API key for AnythingLLM so you can create new users as well as issue temporary authentication links for users.
- The user must already exist within AnythingLLM before using this feature. You can create a user via the in-app interface or the API.
- You may want to disable the login page for all users in addition to using this feature. See [Disable Login Page](https://docs.useanything.com/configuration#disable-login-page).

##### Enable

Set the `SIMPLE_SSO_ENABLED` environment variable to ***any value*** to enable.

```
### This can be any value, number, boolean, or string and it will have the same effect.
SIMPLE_SSO_ENABLED="enable"
```

##### Integration

Once enabled, you can issue a temporary authentication link for a user leveraging the `/api/v1/users/{id}/issue-auth-token` endpoint via the AnythingLLM API.
You simply need to provide the user ID and the API key you created earlier to generate a temporary authentication token that can be used by the target user to login to AnythingLLM.

```
curl -X GET "https://your-anythingllm-instance.com/api/v1/users/{id}/issue-auth-token" \
  -H "Authorization: Bearer {api_key}"
### Example Response
### {
###   "token": "1234567890",
###   "loginPath": "/sso/simple?token=1234567890"
### }
```

Now, the user can visit the provided `loginPath` URL in their browser to be automatically logged in to AnythingLLM!

```
https://your-anythingllm-instance.com/sso/simple?token=1234567890
```

All temporary authentication tokens expire after 1 hour and are single-use only. Once logged in, the user sessions will be valid for 30 days.
The user will be redirected to the home page of AnythingLLM after logging in.
You can optionally redirect the user to a different URL after successfully logging in by appending `&redirectTo={path/to/redirect}` to the query string of the login path.

For example:

```
https://your-anythingllm-instance.com/sso/simple?token=1234567890&redirectTo=/workspaces/sample-workspace
```

Will redirect the user to the `/workspaces/sample-workspace` chat page after a successful login. This can be useful if you want to redirect the user to a specific workspace they have access to after logging in.

##### Disable Login Page

If you are using the `SIMPLE_SSO_ENABLED` feature, you can disable the login page by setting the `SIMPLE_SSO_NO_LOGIN` environment variable to ***any value***.

Setting `SIMPLE_SSO_NO_LOGIN` to ***any value*** in addition to `SIMPLE_SSO_ENABLED` & multi-user mode enabled will:

- Disable the traditional login page for any users including the instance administrator
- Prevent creation of new **Invitations** by any user
- Prevent any existing **Invitations** from being used for new users to create an account with.

```
### This can be any value, number, boolean, or string and it will have the same effect.
SIMPLE_SSO_ENABLED="enable"
SIMPLE_SSO_NO_LOGIN="enable"
```

##### Disable

Fully remove or comment out the `SIMPLE_SSO_ENABLED` environment variable to return to the default behavior.

##### Automatic Redirect for unauthenticated users

If you are using the `SIMPLE_SSO_ENABLED` feature, you can automatically redirect unauthenticated users to your bespoke login page by setting the `SIMPLE_SSO_NO_LOGIN_REDIRECT` environment variable to ***any valid full URL***.

Setting `SIMPLE_SSO_NO_LOGIN_REDIRECT` to ***any valid full URL*** in addition to `SIMPLE_SSO_ENABLED` & `SIMPLE_SSO_NO_LOGIN` will:

- Automatically redirect unauthenticated users to the provided URL when they attempt to access the AnythingLLM instance home URL.
- If the user is using a token URL `/sso/simple?token=123...abcd`, they will still see the error page if their token is invalid or expired.

```
SIMPLE_SSO_ENABLED="enable"
SIMPLE_SSO_NO_LOGIN="enable"
### This must be a valid full URL - invalid or relative URLs will be ignored.
SIMPLE_SSO_NO_LOGIN_REDIRECT="https://your-bespoke-login-page.com"
```

##### Disable

Fully remove or comment out the `SIMPLE_SSO_NO_LOGIN_REDIRECT` environment variable to return to the default behavior.

#### AnythingLLM Hub Agent Skills

> **Note:**
>
> **Important:** Agent skills can enable running untrusted code from untrusted
> sources. By default, AnythingLLM will not allow downloading agent skills from
> the AnythingLLM Hub.

Modification of the `COMMUNITY_HUB_BUNDLE_DOWNLOADS_ENABLED` environment variable allows you to pull in agent skills from the AnythingLLM Hub.

**By default, this feature is disabled.** The reason for this is that running untrusted code from untrusted sources can be very risky and we want to err on the side of caution for self-hosted instances.

There are two settings you can configure to control how this feature works:

- `COMMUNITY_HUB_BUNDLE_DOWNLOADS_ENABLED=1`: This configures enables AnythingLLM to download agent skills from the AnythingLLM Hub but **only if the item is verified or a private item**.
- `COMMUNITY_HUB_BUNDLE_DOWNLOADS_ENABLED=allow_all`: This configures enables AnythingLLM to download agent skills - including unverified public items - from the AnythingLLM Hub.

##### Enable

Set the `COMMUNITY_HUB_BUNDLE_DOWNLOADS_ENABLED` environment variable to **1** or **allow\_all** to enable.

```
### This can be any value, number, boolean, or string and it will have the same effect.
COMMUNITY_HUB_BUNDLE_DOWNLOADS_ENABLED="1"
### or to allow all (not recommended)
#COMMUNITY_HUB_BUNDLE_DOWNLOADS_ENABLED="allow_all"
```

##### Disable

Fully remove or comment out the `COMMUNITY_HUB_BUNDLE_DOWNLOADS_ENABLED` environment variable to return to the default behavior.

#### Local IP Address Scraping

> **Tip:**
>
> **Note:** Enabling this flag should be done at your own risk since it will enable the collector to scrape or reach services running on local IP addresses.

Modification of the `COLLECTOR_ALLOW_ANY_IP` environment variable allows you to enable scraping of local IP addresses.
By default, the collector does not allow scraping of [local IP addresses](https://github.com/Mintplex-Labs/anything-llm/blob/master/collector/utils/url/index.js#L24).

However, for many reasons you may want to enable this feature - so we've added this configuration option to allow you to do so.

When enabled, you will see a log message in the collector logs indicating that local IP address scraping is enabled when using the web-scraping feature

##### Enable

Set the `COLLECTOR_ALLOW_ANY_IP` environment variable to **`"true"`** to enable.
*It must be set to a string value of `"true"` to be effective.*

```
### Must be set to a string value of "true" to be effective.
COLLECTOR_ALLOW_ANY_IP="true"
```

##### Disable

Fully remove or comment out the `COLLECTOR_ALLOW_ANY_IP` environment variable to return to the default behavior.

#### Disable Streaming for Generic OpenAI Provider

> **Tip:**
>
> **Note:** This setting only affects the Generic OpenAI provider and does not impact other LLM providers. Use this when your custom LLM endpoint does not support streaming responses.

Modification of the `GENERIC_OPENAI_STREAMING_DISABLED` environment variable allows you to disable streaming responses when using the Generic OpenAI provider. This is particularly useful when you're using a custom LLM that doesn't support streaming responses.

By default, AnythingLLM attempts to use streaming for a better user experience. However, some custom LLM implementations may not support this feature, resulting in errors or unexpected behavior.

When this setting is enabled, all responses from your Generic OpenAI provider will be returned as complete responses rather than streamed chunks.

##### Enable

Set the `GENERIC_OPENAI_STREAMING_DISABLED` environment variable to **`"true"`** to enable.
*It must be set to a string value of `"true"` to be effective.*

```
### Must be set to a string value of "true" to be effective.
GENERIC_OPENAI_STREAMING_DISABLED="true"
```

##### Disable

Fully remove or comment out the `GENERIC_OPENAI_STREAMING_DISABLED` environment variable to return to the default behavior of using streaming responses.

#### Custom TTL for Sessions

> **Tip:**
>
> **Note:** This configuration is only available for *self-hosted instances*.

Modification of the `JWT_EXPIRY` environment variable allows you to set a custom TTL for sessions.

By default, AnythingLLM will use a TTL of **30 days** for sessions.

##### Enable

> **Warning:**
>
> **Notice:** The minimum TTL is 5 minutes.

Set the `JWT_EXPIRY` environment variable to **a valid duration string** to enable.
Valid duration strings can be found [from the Vercel `ms` library](https://github.com/vercel/ms?tab=readme-ov-file#examples).

```
### Must be set to a string value of a valid duration string.
JWT_EXPIRY="1d" # 1 day
#JWT_EXPIRY="60d" # 60 days
#JWT_EXPIRY="30m" # 30 minutes
```

##### Disable

Fully remove or comment out the `JWT_EXPIRY` environment variable to return to the default behavior.

#### Disable Swagger API Documentation

> **Tip:**
>
> **Note:** It is recommended to disable this endpoint in production deployments for security purposes.

Modification of the `DISABLE_SWAGGER_DOCS` environment variable allows you to disable the Swagger API documentation endpoint at `/api/docs`.

By default, AnythingLLM exposes the Swagger API documentation at the `/api/docs` endpoint. While this can be useful for development and testing, it is recommended to disable this endpoint in production deployments to prevent exposing your API structure and available endpoints.

##### Enable

Set the `DISABLE_SWAGGER_DOCS` environment variable to **`"true"`** to enable.
*It must be set to a string value of `"true"` to be effective.*

```
### Must be set to a string value of "true" to be effective.
DISABLE_SWAGGER_DOCS="true"
```

##### Disable

Fully remove or comment out the `DISABLE_SWAGGER_DOCS` environment variable to return to the default behavior and re-enable the Swagger documentation endpoint.

#### Native Tool Calling for LLM Providers

> **Tip:**
>
> **Note:** This setting only applies to local LLM providers. It has no impact on cloud LLMs like OpenAI, Anthropic, or Azure.

Native tool calling is now **enabled by default** for all providers that support it. The `PROVIDER_DISABLE_NATIVE_TOOL_CALLING` environment variable lets you force specific providers to fall back to prompt-based (UnTooled) tool calling instead.

Previously, native tool calling was opt-in via `PROVIDER_SUPPORTS_NATIVE_TOOL_CALLING`. That variable has been replaced — you no longer need to enable native tool calling, only to disable it for providers where it misbehaves.

Only `OpenAI` and `Anthropic` are unaffected by this setting and will always use native tool calling regardless of this ENV config.

> **Tip:**
>
> Because native tool calling is now on by default, workspaces in automatic chat mode using these providers will run the agent automatically without requiring the `@agent` prefix. Disabling native tool calling for a provider restores the previous behavior, where the agent must be invoked explicitly.

##### Disable

Set the `PROVIDER_DISABLE_NATIVE_TOOL_CALLING` environment variable to a comma-separated list of provider identifiers you want to revert to prompt-based tool calling. Add a provider here only if its native tool calling misbehaves and you want to fall back.

```
### Disable native tool calling for specific providers.
PROVIDER_DISABLE_NATIVE_TOOL_CALLING="groq,openrouter"
 
### Disable for all affected providers.
PROVIDER_DISABLE_NATIVE_TOOL_CALLING="generic-openai,bedrock,localai,groq,litellm,openrouter,lemonade"
```

##### Enable

Native tool calling is enabled by default. Fully remove or comment out the `PROVIDER_DISABLE_NATIVE_TOOL_CALLING` environment variable (or omit a provider from the list) to use native tool calling.

#### Automatic Tool Call Approval

Modification of the `AGENT_AUTO_APPROVED_SKILLS` environment variable allows you to automatically approve tool calls for all users.

Not all agent-skills ask for approval. Only skills that can be long-running, computationally expensive, or otherwise risky should ask for approval.

##### Enable

Set the `AGENT_AUTO_APPROVED_SKILLS` environment variable to a comma-separated list of agent-skill-ids you want to automatically approve tool calls for. You can find the agent-skill-id by the `name` property in the [AnythingLLM Repository](https://github.com/Mintplex-Labs/anything-llm/tree/master/server/utils/agents/aibitat/plugins).

Optionally, you can just use the special `<all>` keyword to automatically approve tool calls for every agent-skill.

```
AGENT_AUTO_APPROVED_SKILLS="<all>" # Automatically approve tool calls for every agent-skill.
AGENT_AUTO_APPROVED_SKILLS="create-pdf-file,create-docx-file" # Automatically approve tool calls for specific agent-skills.
```

##### Disable

Fully remove or comment out the `AGENT_AUTO_APPROVED_SKILLS` environment variable to return to the default behavior.

#### LLM Provider Timeout

> **Tip:**
>
> **Note:** This setting is useful for users with slow local models that need longer request timeouts.

Modification of the `ANYTHINGLLM_FETCH_TIMEOUT` environment variable allows you to override the default timeout (10 minutes) for all outbound SDK requests to LLM providers.

Both the underlying HTTP transport layer (undici) and the SDK-level AbortController deadline are raised to the specified value.

##### Enable

Set the `ANYTHINGLLM_FETCH_TIMEOUT` environment variable to a timeout value in **milliseconds**.

```
ANYTHINGLLM_FETCH_TIMEOUT="1200000" # 20 minutes
```

##### Disable

Fully remove or comment out the `ANYTHINGLLM_FETCH_TIMEOUT` environment variable to return to the default behavior (10 minutes).

#### SDK Max Retries

> **Tip:**
>
> **Note:** By default, retries are disabled (set to 0) to avoid duplicate requests to local models.

Modification of the `ANYTHINGLLM_MAX_RETRIES` environment variable allows you to configure how many times a failed SDK request to an LLM provider will be retried before giving up.

##### Enable

Set the `ANYTHINGLLM_MAX_RETRIES` environment variable to a non-negative integer.

```
ANYTHINGLLM_MAX_RETRIES="2" # Retry failed requests up to 2 times.
```

##### Disable

Fully remove or comment out the `ANYTHINGLLM_MAX_RETRIES` environment variable to return to the default behavior (0 retries).

#### Require Allowlist for Embed Widgets

By default, a public chat embed widget created **without** an allowed-domains allowlist responds to requests from **any** origin. Setting the `EMBED_REQUIRE_ALLOWLIST` environment variable makes embeds that have no allowlist configured reject all requests (deny-by-default). Embeds that already have an allowlist set are unaffected.

- Useful for administrators who want to ensure an embed cannot be queried cross-origin until its allowed domains are explicitly set.
- Added in [Mintplex-Labs/anything-llm#5759](https://github.com/Mintplex-Labs/anything-llm/pull/5759).

##### Enable

Set the `EMBED_REQUIRE_ALLOWLIST` environment variable to any value to enable.

```
EMBED_REQUIRE_ALLOWLIST="enable"
```

##### Disable

Fully remove or comment out the `EMBED_REQUIRE_ALLOWLIST` environment variable to return to the default behavior, where an embed with no allowlist answers requests from any origin.


---

## Features

### Clarifying Questions

*Give your AI agents the ability to pause and ask clarifying questions before proceeding, resulting in better and more accurate responses.*

**Source:** https://docs.useanything.com/features/agent-surveys

When an agent receives an ambiguous or incomplete prompt, it typically has to guess at the missing details. The **Clarifying Questions** skill gives your agent a structured way to pause mid-turn and ask the user for the information it needs before continuing — no need to restart the conversation.

This opt-in agent skill presents an interactive survey card directly in the chat. The agent decides when to invoke it and what to ask, then resumes with the user's answers fully in context.

#### Why use Clarifying Questions?

- **More accurate results** — Instead of guessing, the agent gets the exact details it needs before acting.
- **Fewer back-and-forth messages** — The agent can batch multiple independent questions into a single survey card.
- **Structured input** — Supports free-form text, URLs, numbers, dates, emails, and single/multi-select choice lists so answers are clean and unambiguous.
- **Persistent context** — Answers are saved with the chat history, so both the agent and normal chat can reference them in follow-up turns.

> **Tip:**
>
> This skill is **off by default** and must be enabled by an admin. It only works in the desktop/browser UI (websocket sessions) — it is not available for API or programmatic agent runs.

#### Enabling the Skill

1. Navigate to **Settings → Agent Skills** in the admin sidebar.
2. Under agent skills, click on the slider icon in the top right corner to open agent skill settings modal.
3. Toggle on **Allow agent to ask clarifying questions** to enable the skill.
4. Set the **Max questions per turn** (1–10, default 3). This caps how many questions the agent can ask in a single invocation.

> **Warning:**
>
> This skill is model-dependent. Smaller or less capable models may not reliably choose to call the tool, even when clarification would be helpful. For best results, use a capable model as your agent LLM.

![AnythingLLM Agent Settings Menu Icon Location](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fagent-configuration%2Fsettings-menu-icon-location.png&w=3840&q=100)
![AnythingLLM Agent Settings Menu](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fagent-surveys%2Fmodal.png&w=3840&q=100)

#### How It Works

Once enabled, the agent has access to a tool that lets it present questions to the user. The agent autonomously decides when clarification is needed based on the prompt it received.

##### Question Types

| Type | Description |
| --- | --- |
| **Text input** | Free-form text, URL, number, date, or email fields |
| **Single-select choice** | Pick one option from a list |
| **Multi-select choice** | Pick one or more options from a list |

Choice questions can optionally include an "Other" field so the user can provide a custom answer that wasn't in the original list.

##### User Experience

When the agent asks questions, the user sees an interactive card in the chat:

- **Single question** — A simple form with the question and input or choices.
- **Multiple questions** — A paginated card the user can navigate through.
- **Skip** — Users can skip individual questions or dismiss the entire survey if they'd rather let the agent proceed on its own.

After the user responds (or skips/times out), the agent receives the answers and continues its task with that information in context.

![AnythingLLM Multi-Choice Survey](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fagent-surveys%2Fmulti-choice.png&w=3840&q=100)

##### Persistence

Completed surveys are saved alongside the chat message. When you reload a conversation, surveys render as read-only cards showing the questions and answers that were provided. The Q&A transcript is also injected into prompt history, so the agent retains awareness of what was discussed in future turns.

![AnythingLLM Saved Survey](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fagent-surveys%2Fsaved-survey.png&w=3840&q=100)

### AI Agents

*Agents on AnythingLLM can scrape websites, list and summarize your documents, search the web, make charts, and even save files to desktop and their own memory.*

**Source:** https://docs.useanything.com/features/ai-agents

![AnythingLLM AI Agents](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fai-agents%2Fheader-image.png&w=3840&q=100)

Agents are basically an LLM that has access to some simple tools. We will be adding much more customization in this area soon. All agents share the same tools across workspaces, but operate within the workspace they were invoked via `@agent`.

You can start an agent session by going into any workspace and typing `@agent <your prompt>` and exit by just typing `exit`

Agents can scrape websites, list and summarize your documents, search the web, make charts, and even save files to desktop and their own memory.

> **Tip:**
>
> **Examples:**   
> 1: `@agent` what documents can you see - > LLM will "look" at what are the documents it can see
>
> 2: `@agent` summarize readme.pdf - > LLM will summarize that specific embedded file

![AnythingLLM AI Agents](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fai-agents%2Fai-agent.png&w=3840&q=100)

[**View all the available `@agent` skills →**](https://docs.useanything.com/agent/usage/overview)

### All Features

*All the features of AnythingLLM*

**Source:** https://docs.useanything.com/features/all-features

![AnythingLLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fheader-image.png&w=3840&q=100)

Click the below cards to know more about the features

[![AnythingLLM AI Agents](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fai-agents%2Fheader-image.png&w=3840&q=100)AI Agents→](https://docs.useanything.com/features/ai-agents)[![AnythingLLM API Access & Keys](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fapi%2Fheader-image.png&w=3840&q=100)API Access & Keys→](https://docs.useanything.com/features/api)[![AnythingLLM Appearance Customization](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fcustomization%2Fheader-image.png&w=3840&q=100)Appearance Customization→](https://docs.useanything.com/features/customization)[![AnythingLLM Chat Logs](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fchat-logs%2Fheader-image.png&w=3840&q=100)Chat Logs→](https://docs.useanything.com/features/chat-logs)[![AnythingLLM Chat Modes](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fchat-logs%2Fheader-image.png&w=3840&q=100)Chat Modes→](https://docs.useanything.com/features/chat-modes)[![AnythingLLM Embedded Chat Widgets](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fchat-widgets%2Fheader-image.png&w=3840&q=100)Embedded Chat Widgets→](https://docs.useanything.com/features/chat-widgets)[![AnythingLLM Event Logs](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fevent-logs%2Fheader-image.png&w=3840&q=100)Event Logs→](https://docs.useanything.com/features/event-logs)[![AnythingLLM Large Language Models](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Flanguage-models%2Fheader-image.png&w=3840&q=100)Large Language Models→](https://docs.useanything.com/features/language-models)[![AnythingLLM Embedding Models](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fembedding-models%2Fheader-image.png&w=3840&q=100)Embedding Models→](https://docs.useanything.com/features/embedding-models)[![AnythingLLM Transcription Models](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Ftranscription-models%2Fheader-image.png&w=3840&q=100)Transcription Models→](https://docs.useanything.com/features/transcription-models)[![AnythingLLM Vector Database](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fheader-image.png&w=3840&q=100)Vector Databases→](https://docs.useanything.com/features/vector-databases)[![AnythingLLM Security & Access](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fsecurity-and-access%2Fheader-image.png&w=3840&q=100)Security & Access→](https://docs.useanything.com/features/security-and-access)[![AnythingLLM Privacy & Data Handling](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fprivacy-and-data-handling%2Fheader-image.png&w=3840&q=100)Privacy & Data Handling→](https://docs.useanything.com/features/privacy-and-data-handling)[![AnythingLLM Cloud Deployment](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Finstallation%2Fcloud-docker%2Fheader-image.png&w=3840&q=100)Cloud Deployment→](https://docs.useanything.com/installation-docker/cloud-docker)[![AnythingLLM System Prompt Variables](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Ftranscription-models%2Fheader-image.png&w=3840&q=100)System Prompt Variables→](https://docs.useanything.com/features/system-prompt-variables)[![AnythingLLM Memories](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fmemories%2Fheader-image.png&w=3840&q=100)Memories→](https://docs.useanything.com/features/memories)[![AnythingLLM Model Router](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fapi%2Fheader-image.png&w=3840&q=100)Model Router→](https://docs.useanything.com/model-router/overview)

### API Access & Keys

*API keys are managed by accounts with the correct access level.*

**Source:** https://docs.useanything.com/features/api

![AnythingLLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fapi%2Fheader-image.png&w=3840&q=100)

You can find the API documentation for available endpoints on your instance at `/api/docs`

API keys are managed by accounts with the correct access level.

However, anyone with the API key can use the AnythingLLM API, so do not share or publish this key anywhere.

AnythingLLM supports a full developer API that you can use to manage, update, embed, and even chat with your workspaces.

You can create and delete API keys on the fly if you are allowed permission to do so.

![AnythingLLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fapi%2Fapi-keys.png&w=3840&q=100)

### Authenticated Scraping

*Have your LLM access and scrape authenticated content with AnythingLLM's Authenticated Scraping tool*

**Source:** https://docs.useanything.com/features/browser-tool

> **Note:**
>
> **Desktop Only Feature (v1.8.3+)**  
> The Authenticated Scraping tool is exclusively available in the AnythingLLM Desktop application!

### Authenticated Scraping

> **Warning:**
>
> **Security Note**
> All credentials and session data are stored locally on your machine. AnythingLLM never transmits or stores your login information outside of your local machine.

The Authenticated Scraping tool enables you to access and scrape gated online content from websites or services that require authentication but hold critical contexual content you might want to use in your workflows, such as your personal LinkedIn feed or internal company portals that you have access to.

Your LLM can now access these websites and scrape and view content just like you would in a regular browser!

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fbrowser-tool%2Fbrowser-tool.png&w=1080&q=100)

#### Key Features

- **Secure Session Storage**: Credentials are stored locally using isolated browser sessions
- **Session Persistence**: Login sessions persist between app restarts until explicitly cleared or the authentication expires for the associated service
- **Isolated Environment**: Separate from your actual web browser
- **Full User Control**: Clear stored data or sessions at any time with a single click

#### Using the Authenticated Scraping Tool

##### Accessing the Tool

1. Open AnythingLLM Desktop
2. Navigate to Settings > Tools > Browser Tool
3. Click "Open Private Browser" to launch the isolated browser window

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fbrowser-tool%2Fmanager.png&w=2048&q=100)

##### Authentication Process

1. Log into your desired service (e.g., LinkedIn, Gmail) through the Authenticated Scraping tool.
2. Your session will persist until you explicitly clear the browser data or the authentication expires for the associated service.
3. AnythingLLM can now access authenticated content from these services when scraping or via agentic workflow execution.
4. The returned content will be text only. No images, videos, or other media will be returned.

> **Tip:**
>
> **Heads up!**
> The Authenticated Scraping tool is not a magic bullet. It is a tool that allows you to access authenticated content from websites that require authentication. It cannot currently **interact** with the content of the page you are accessing (eg: browser automation, RPA, etc).

##### Managing Browser Data

- **Clearing Data**: Use the "Clear Browser Data" button to remove all stored credentials and sessions
- **When should you clear the browser data?**:
  - When switching between different service accounts
  - If you encounter authentication issues when the LLM tries to access the site you want to scrape

#### Common Use Cases

> **Warning:**
>
> **Warning!**
> Some web services may detect and restrict automated access, even though this tool functions as a standard browser. Use this feature responsibly and at your own discretion, as certain services may suspend or block accounts that they perceive as engaging in automated activity.

- Scraping your personal linkedin profile or feed.
- Accessing internal company documentation that is behind a login or SSO portal.
- Collecting or accessing data from paid or authenticated web service you have access to normally.

#### Troubleshooting

If you encounter issues:

1. Clear the browser data and try again
2. Ensure you're fully logged into the service by opening the private browser and navigating to the site you want the LLM to access.

Some services have very short lived sessions, those services may require you to log in again after a certain amount of time or might be a bad use-case for this tool. You can always re-authenticate with the service by opening the private browser and navigating to the site you want the LLM to access and logging in again to refresh the session.

### Workspace Chat Logs

*AnythingLLM Workspace Chat Logs*

**Source:** https://docs.useanything.com/features/chat-logs

![AnythingLLM Workspace Chat Logs](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fchat-logs%2Fheader-image.png&w=3840&q=100)

AnythingLLM supports exporting chats as:

- **CSV**
- **JSON**
- **JSON (Alpaca)**
- **JSONL (OpenAI fine-tune)**

Just click export at the top of the screen once at least 10 chat logs are available! Provided you have the correct account permissions, you can view the chat logs per workspace and per user of your AnythingLLM instance.

![AnythingLLM Workspace Chat Logs](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fchat-logs%2Fworkspace-chat.png&w=3840&q=100)

### Chat Modes

*Understanding the difference between Query and Chat modes in AnythingLLM*

**Source:** https://docs.useanything.com/features/chat-modes

AnythingLLM offers multiple ways to chat with your documents. Let's understand what each does and how to get the best results for your use case and expectations.

#### Available Chat Modes

**Agent Mode** (recommended):

> **Tip:**
>
> All versions later than v1.11.1 have agent mode available as an option for workspaces, enabled by default for new workspaces.
>
> You can change the chat mode in the workspace's settings by clicking the "Gear" icon under the "Chat Settings" tab.

- Will automatically use available agent-skills, tools, and MCPs to answer your questions
- This feature is fully dependent on the capabilities of your LLM provider and model to call tools natively.
- Native tool calling is enabled by default for providers that support it, giving you an always-on agent experience. If a provider's native tool calling misbehaves, you can fall back to prompt-based tool calling with the [`PROVIDER_DISABLE_NATIVE_TOOL_CALLING`](https://docs.useanything.com/configuration#native-tool-calling-for-llm-providers) environment variable.

*if you see the "@" symbol in your prompt input you will need to use `@agent` to start an agentic chat session. If it is not there, you are using agentic chat mode.*

**Chat Mode**:

- Uses both your documents and the AI's general knowledge
- More conversational and flexible
- Good for brainstorming and exploring topics

**Query Mode**:

- Only uses information from your uploaded documents
- Will tell you if it can't find relevant information
- Best for when you need accurate, document-based answers and nothing else

#### Common Questions

##### "It keeps saying 'No relevant information found' in Query mode"

This usually means one of three things:

1. The information might be in your document but worded differently
2. The similarity settings might be too strict
3. The document might be too large and split in a way that makes finding information difficult

**Quick fixes to try:**

1. Go to workspace settings → Vector Database Settings
2. Change "Document similarity threshold" to "No restriction"
3. Try asking your question using words that match how it's written in your document

> **Tip:**
>
> Instead of asking "How do I start the app?", try using terms from your document like "How do I initialize the application?"

##### "When should I use Query mode vs Chat mode?"

Use **Query mode** when:

- You need factual answers from your documents
- You're working with technical documentation
- You want to prevent made-up information

Use **Chat mode** when:

- You want more conversational responses
- You need additional context or examples
- You're brainstorming ideas

##### "Why does it work better with some documents than others?"

Documents are processed in chunks, and each chunk is analyzed separately. This means:

- Large documents might need more specific questions
- Technical documents work better with technical questions

#### Tips for Better Results

1. **Start with Query mode** and "No restriction" similarity if you're not finding information
2. **Use specific terms** from your documents in your questions
3. **Switch to Chat mode** if you need more context or explanation
4. **Try rephrasing your question** if you're not getting good results

> **Warning:**
>
> If you're still not getting good results, check your workspace settings and try adjusting the "Document similarity threshold" between No restriction, Low (≥ .25), Medium (≥ .50), or High (≥ .75) to find what works best for your documents.

### Embedded Chat Widgets

*AnythingLLM allows you to create embedded chat widgets that can be easily integrated into any website*

**Source:** https://docs.useanything.com/features/chat-widgets

![AnythingLLM Embedded Chat Widgets](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fchat-widgets%2Fheader-image.png&w=3840&q=100)

> **Tip:**
>
> **DOCKER VERSION ONLY!**
>
> These settings are only available in the Docker version of AnythingLLM

![Embedded Chat Widget](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fchat-widgets%2Fchat-widget.png&w=3840&q=100)

AnythingLLM allows you to create embedded chat widgets that can be easily integrated into any website using a simple `<script>` tag. These embedded chat widgets provide a convenient way for users to interact with your chatbot directly from your website.

#### Configuration Options

When creating an embedded chat widget, you have several configuration options available to customize its behavior and appearance.

![Embedded Chat Options 1](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fchat-widgets%2Fconfiguration-options.png&w=3840&q=100)

##### Workspace

The workspace setting determines which workspace your chat window will be based on. All defaults will be inherited from the selected workspace unless overridden by the specific configuration options.

##### Allowed Chat Method

You can set how your chatbot should operate using the allowed chat method. There are two options:

- **Chat**: The chatbot will respond to all questions regardless of context.
- **Query**: The chatbot will only respond to chats related to documents in the workspace.

##### Restrict Requests from Domains

This filter allows you to block any requests that come from domains other than the specified list. Leaving this field empty means anyone can use your embedded chat widget on any site.

![Embedded Chat Options 2](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fchat-widgets%2Fdomain-blacklist.png&w=3840&q=100)

##### Max Chats per Day

You can limit the number of chats this embedded chat widget can process in a 24-hour period. Setting this value to zero means unlimited chats per day.

##### Max Chats per Session

You can limit the number of chats a session user can send with this embedded chat widget in a 24-hour period. Setting this value to zero means unlimited chats per session.

##### Enable Dynamic Model Use

By enabling dynamic model use, you allow the setting of the preferred LLM model to override the workspace default.

##### Enable Dynamic LLM Temperature

Enabling dynamic LLM temperature allows the setting of the LLM temperature to override the workspace default.

##### Enable Prompt Override

By enabling prompt override, you allow the setting of the system prompt to override the workspace default.

#### Embedding the Chat Widget

![Embedded Chat Code](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fchat-widgets%2Fembed-code.png&w=3840&q=100)

After creating an embedded chat widget, you will be provided with a link that you can publish on your website using a simple `<script>` tag. This allows you to easily integrate the chat widget into your website's HTML code.

### Appearance Customization

*AnythingLLM allows you to customize the look and feel of your instance to match your brand and identity.*

**Source:** https://docs.useanything.com/features/customization

![AnythingLLM Appearance Customization](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fcustomization%2Fheader-image.png&w=3840&q=100)

> **Tip:**
>
> **DOCKER VERSION ONLY!**
>
> These settings are only available in the Docker version of AnythingLLM

AnythingLLM allows you to customize the look and feel of your instance to match your brand and identity.

![Appearance Settings Page](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fcustomization%2Fappearance-settings-page.png&w=3840&q=100)

Overview of all the appearance settings available in AnythingLLM.

#### Custom Logo

![Custom Logo](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fcustomization%2Fcustom-logo.png&w=3840&q=100)

You can replace the AnythingLLM branded logo that appears on the login page and throughout the app with your own brand's logo. In this example, we have used a green square image for demonstration purposes.

#### Custom Welcome Messages

![Custom Welcome Messages](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fcustomization%2Fcustom-welcome-messages.png&w=3840&q=100)

By default, when you first log in to AnythingLLM and you have not yet selected a workspace, you will be shown the default messages explaining AnythingLLM. Using the system messages inputs, you can simulate both system and user response messages. Take this opportunity to tell users what specific workspaces are for - or just say hello!

#### Custom Footer Links and Icons

![Custom Footer Links and Icons](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fcustomization%2Fcustom-footer-links-and-icons.png&w=3840&q=100)

The footer icons can be replaced with custom links and icons to provide quick access to relevant resources or web pages.

### Embedding Models

*AnythingLLM supports many embedding model providers out of the box with very little, if any setup*

**Source:** https://docs.useanything.com/features/embedding-models

AnythingLLM supports many embedding model providers out of the box with very little, if any setup.

Embedding models are specific types of models that turn text into vectors, which can be stored and searched in a vector database - which is the foundation of RAG.

#### Supported Embedding Model Providers

##### Local Embedding Model Providers

[Built-in (default)](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)[Ollama](https://ollama.com/)[LM Studio](https://lmstudio.ai/)[Local AI](https://localai.io/)[Lemonade](https://lemonade-server.ai/)

##### Cloud Embedding Model Providers

[OpenAI](https://platform.openai.com/)[Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service)[Cohere](https://cohere.com/)[Voyage AI](https://www.voyageai.com/)[LiteLLM](https://litellm.ai/)[Mistral](https://mistral.ai/)[Generic OpenAI](https://openai.com/)[Gemini](https://ai.google.dev/)[OpenRouter](https://openrouter.ai/)

### Event Logs

*All the features of AnythingLLM*

**Source:** https://docs.useanything.com/features/event-logs

![AnythingLLM Event Logs](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fevent-logs%2Fheader-image.png&w=3840&q=100)

The Event Logs page in AnythingLLM allows users to view and monitor various events that occur within the application.

![AnythingLLM Event Logs](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fevent-logs%2Fevent-logs.png&w=3840&q=100)

This feature provides insights into user activities and system-related events.

#### Event Types

The Event Logs page captures a variety of events, such as:

- User login attempts (successful and failed)
- Messages sent by users
- Changes made to application settings
- Document uploads

#### Event Details

Each event in the Event Logs page includes relevant information, such as the event type, associated user (if applicable), timestamp, and any additional details specific to the event type.

Useful for monitoring your AnythingLLM instance.

### Large Language Models

*AnythingLLM allows you to use a host of LLM providers for chatting and generative AI.*

**Source:** https://docs.useanything.com/features/language-models

> **Tip:**
>
> **Tip:** Models that are multi-modal (text-to-text & image-to-text) are
> supported for System & Workspace models.

AnythingLLM allows you to use a host of LLM providers for chatting and generative AI.

Depending on your selection additional configuration might be required.

#### Supported Language Model Providers

##### Local Language Model Providers

[Built-in (default)](https://docs.useanything.com/features/language-models)[Ollama](https://ollama.com/)[LM Studio](https://lmstudio.ai/)[Local AI](https://localai.io/)[KoboldCPP](https://github.com/LostRuins/koboldcpp)[Text Generation WebUI](https://github.com/oobabooga/text-generation-webui)[Docker Model Runner](https://docs.docker.com/desktop/features/model-runner/)[Lemonade](https://lemonade-server.ai/)[oMLX](https://omlx.ai/)

##### Cloud Language Model Providers

[OpenAI](https://platform.openai.com/)[Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service)[AWS Bedrock](https://aws.amazon.com/bedrock)[Anthropic](https://anthropic.com/)[Cohere](https://cohere.com/)[Cerebras](https://cerebras.ai/)[Google Gemini](https://ai.google.dev/)[Hugging Face](https://huggingface.co/)[Together AI](https://www.together.ai/)[Fireworks AI](https://fireworks.ai/)[OpenRouter](https://openrouter.ai/)[Perplexity AI](https://www.perplexity.ai/)[Mistral](https://mistral.ai/)[Groq](https://groq.com/)[LiteLLM](https://litellm.ai/)[DeepSeek](https://www.deepseek.com/)[APIPie](https://apipie.ai/)[Novita AI](https://novita.ai/)[xAI](https://x.ai/)[NVIDIA NIM](https://www.nvidia.com/en-us/ai/)[PPIO](https://www.ppinfra.com/)[Dell Pro AI Studio](https://www.dell.com/en-us/dt/solutions/artificial-intelligence/index.htm)[Moonshot AI](https://www.moonshot.cn/)[Comet API](https://www.comet.com/)[Foundry](https://www.foundrylocal.ai/)[zAI](https://zai.chat/)[Gitee AI](https://ai.gitee.com/)[SambaNova](https://sambanova.ai/)[Minimax](https://www.minimaxi.com/)[OpenAI (generic)](https://docs.useanything.com/anythingllm-setup/llm-configuration/cloud/openai-generic)

##### Specialized Providers

*The model router is not a provider, but it is a feature that allows you to route your sessions to different LLM providers and models based on rules you define within a chat without having to change the model manually.*

[AnythingLLM Model Router](https://docs.useanything.com/model-router/overview)

### Memories & Personalization

*Let AnythingLLM remember facts about you across conversations and inject them into the system prompt for more personalized responses.*

**Source:** https://docs.useanything.com/features/memories

Memories let AnythingLLM remember useful facts about you (your name, preferences, ongoing projects, communication style, etc.) and use them to give more personalized responses.

There are two kinds of memories:

- **Workspace memories** only affect chats inside a single workspace. Up to **20** per workspace.
- **Global memories** apply to every workspace you use. Up to **5** total.

> **Tip:**
>
> Memories are always tied to your user account. In multi-user mode, every user
> has their own separate memories. No one else can see yours.

#### Enabling Personalization

Memories are **off by default**. An admin (or the single user on a non multi-user instance) has to turn the feature on before any memories are created or used.

1. Open any workspace and start a chat.
2. Click the **settings** icon in the top right of the chat window.
3. Choose **Memories** from the menu to open the Memories sidebar.
4. Toggle **Enable Personalization** on.

![Opening the Memories sidebar from the chat settings menu](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fmemories%2Fchat-settings-menu.png&w=3840&q=100)

Once it's on, the Memories sidebar will show the workspace and global tabs. In multi-user mode, non-admin users can still open the sidebar and manage their own memories, but only an admin can turn the feature on or off.

#### Managing memories manually

From the Memories sidebar you can add, edit, delete, and move memories between scopes.

![Memories sidebar showing the Personalization toggle, workspace and global tabs, and memory cards](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fmemories%2Fmemories-sidebar.png&w=3840&q=100)

- **Add**: Click the **+** button in the tab header and write a single-sentence fact (for example, *"User prefers Python over JavaScript"*).
- **Edit**: Open a memory's menu (the three-dot icon on the card) and choose **Edit**.
- **Delete**: Open the memory's menu and choose **Delete**.
- **Move to global**: From a workspace memory's menu, choose **Move to global** to make it apply everywhere.
- **Move to workspace**: From a global memory's menu, choose **Move to workspace** to scope it back to just the current workspace.

Each tab shows how many memories you have versus the limit (like `3/20` for workspace or `1/5` for global). If the destination is already full, adding or moving a memory will fail. Delete or move another memory out of that scope to make room.

#### Automatic memory extraction

AnythingLLM can build memories for you automatically by reviewing your recent chats and extracting useful facts — your name, what you're working on, your preferences, and so on.

Automatic extraction is a separate toggle from Personalization itself. You can keep Personalization **on** (so manually created memories are still injected into chats) while turning automatic extraction **off** if you prefer to manage memories entirely by hand.

To toggle automatic extraction, open the Memories sidebar and look for the **Automatic Memory Extraction** toggle below the main Personalization toggle. It is on by default when Personalization is enabled.

##### How extraction works

Extraction uses a two-phase **Observer/Reflector** pipeline:

1. **Observer** — Reviews your recent conversations and identifies candidate facts (up to 3 per run). Each candidate includes a confidence rating. The Observer is deliberately selective: it looks for things like your name, role, what you're working on, and stated preferences. It skips assistant opinions, emotional assessments, and conversational filler.
2. **Reflector** — Reviews the Observer's candidates against your existing memories. For each candidate it:

   - **Classifies scope**: Would this fact be useful in a completely different workspace? If yes, it becomes a **global** memory. If it's specific to the current project, it becomes a **workspace** memory.
   - **Deduplicates**: Drops candidates that overlap with existing memories, even if worded differently.
   - **Consolidates**: If a candidate updates an existing workspace memory, the existing memory is revised rather than creating a duplicate.
   - **Filters**: Drops low-confidence candidates unless they are clear identity facts.

This two-phase approach means the system is conservative about what it saves and accurate about scope. A conversation about a specific project will produce workspace memories, while your name or communication preferences become global memories.

##### When it runs

- On a schedule (default: every **3hours**).
- Only when your workspace has been idle (defined by `MEMORY_IDLE_THRESHOLD_MS` which defaults to **20 minutes**). If you've chatted in a given workspace within the idle threshold, extraction for that workspace is skipped that round so it doesn't process a conversation that's still going. Other users and workspaces aren't affected.
- Only when both Personalization and Automatic Memory Extraction are turned on. Default is both are enabled if you have Personalization turned on.
- Only when there are at least **5 unprocessed chats** in a workspace — short exchanges are skipped since they are not likely to contain useful information.

You can change the schedule and idle window with the environment variables listed in this document in the instance/installation .env

##### Model requirements

Automatic extraction uses the workspace's configured chat model (falling back to the agent model, then the system default). The model must support **tool calling** — if the model can't produce structured tool calls, extraction will log a warning and skip the run. Most modern models (OpenAI, Anthropic, Ollama, LM Studio, etc.) support this.

#### How memories are used in chat

When Personalization is on and you send a message, AnythingLLM adds a short `## Things I Remember About You` section to the end of the workspace's system prompt before sending it to the model.

That section includes:

- **All of your global memories** (up to 5).
- **Your top 5 workspace memories** for the current workspace.

If you have more than 5 workspace memories, AnythingLLM scores them against your current message and recent chat history and picks the 5 most relevant. If that scoring step fails for any reason, it falls back to the 5 most recently created memories.

This happens for regular chats, streamed chats, agent chats, and chats made through the API.

> **Warning:**
>
> Memory content is sent to your LLM provider as part of the system prompt.
> If you're using a third-party provider, assume they can see it. Don't store
> passwords, API keys, or sensitive personal information as memories.

#### Single-user vs. multi-user mode

Memories work the same way in both modes. A few things to know:

- **Single-user mode**: All memories belong to the one local user. Enabling Personalization and managing memories are done by the same person.
- **Multi-user mode**: Memories are always tied to the user who created them. Only admins can turn Personalization on or off, but every user can view and manage their own memories from the Memories sidebar. No user can see, edit, move, or delete another user's memories.
- **Switching from single-user to multi-user**: When you turn on multi-user mode on an existing instance, any memories created beforehand are reassigned to the new admin account so nothing is lost.

#### Configuration

These environment variables control the background extraction job. All are optional.

| Variable | Default | Description |
| --- | --- | --- |
| `MEMORY_EXTRACTION_INTERVAL` | `3hr` | How often the extraction job runs. |
| `MEMORY_IDLE_THRESHOLD_MS` | `1200000` | How long (in milliseconds) a user's workspace has to be idle before its chats are processed. Default is 20 minutes. |

#### Limits

| Scope | Limit per user |
| --- | --- |
| Global memories | 5 |
| Workspace memories | 20 (per workspace) |
| Memories injected per chat | All global + top 5 workspace |
| Candidates per extraction | 3 (per run, per workspace) |

### Privacy & Data

*Security features of AnythingLLM*

**Source:** https://docs.useanything.com/features/privacy-and-data-handling

![AnythingLLM Privacy & Data](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fprivacy-and-data-handling%2Fheader-image.png&w=3840&q=100)

> **Tip:**
>
> **Tip:**
>
> AnythingLLM is transparent telling you who and what has access to your data.

![Privacy & Data](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fprivacy-and-data-handling%2Fprivacy-and-data.png&w=3840&q=100)

#### Anonymous Telemetry

AnythingLLM collects anonymous telemetry and never collects any of your personal data.

We collect telemetry to help improve our product.

If for any reason you would not like to participate in sharing telemetry with us, you can disable it in this menu.

#### Deleting documents and full erasure

Removing a document can mean two different things in AnythingLLM, and they behave differently:

- **Removing a document from a workspace** stops that workspace from using it and deletes its vectors from that workspace — but the document stays in **My Documents** (your document library) so it can be re-used in other workspaces without re-parsing.
- **Deleting a document from My Documents** removes it from the system entirely: it deletes the parsed source file and the cached embeddings, and removes the document from **every** workspace.

> **Warning:**
>
> **Right-to-erasure / data-deletion requests:**
>
> To completely erase a document — both its parsed text and its cached
> embeddings — delete it from **My Documents**, not just from a workspace.
> Removing a document from a single workspace intentionally leaves the parsed
> file and cache in place so it can be re-used.

### Security and Access

*Security features of AnythingLLM*

**Source:** https://docs.useanything.com/features/security-and-access

![AnythingLLM Security and Access](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fsecurity-and-access%2Fheader-image.png&w=3840&q=100)

> **Tip:**
>
> **DOCKER VERSION ONLY!**
>
> These settings are only available in the Docker version of AnythingLLM

AnythingLLM supports two types of use cases: **single-user** and **multi-user** mode.

#### Single-user Mode

Single-user mode is preferred for those who only themselves or a select group of trusted people will use the instance. If you want to have per-user permissions, you should switch to multi-user mode.

In single-user mode, you (and only you) have complete control over the instance. Anyone with the password to the instance, if set, will be able to use the instance, change any configuration or settings, and view all chats.

##### Password Protecting the Instance

When using AnythingLLM in "single user mode," you can password protect the instance by toggling on the "Password Protect Instance" option. This will display an input where you can enter the password to protect the instance.

![Password Protect Instance](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fsecurity-and-access%2Fpassword-protection.png&w=3840&q=100)

You can turn off password protection at any time or reset the password to the instance while logged in.

#### Multi-user Mode

> **Warning:**
>
> **Warning**
>
> Once in multi-user mode, you cannot revert back to single-user mode

The preferred method of use for AnythingLLM is **multi-user mode**. In this mode, you can set per-user role-based access permissions.

By default, you will create the administrator account, which has the highest level of privilege. As an administrator, you will have access to the entire system, logs, analytics, and more.

##### User Roles

- **Admin**: Full access to the entire system
- **Manager**: Can view all workspaces and manage all properties except for settings for LLM, Embedder, and Vector database
- **Default**: Can only send chats to workspaces they are explicitly added to. Cannot see or edit any workspaces or system settings.

##### Enabling Multi-user Mode

To enable multi-user mode, toggle on the "Enable multi-user mode" option. This will display an input where you can enter the username and password for the first admin account.

![Enable Multi-user Mode](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fsecurity-and-access%2Fmulti-user-mode.png&w=3840&q=100)

This will be the default admin account that you will use to control the instance. Once set, you will be logged out so you can log in with the new password.

### System Prompt Variables

*Inject dynamic and static variables into your system prompt on the fly*

**Source:** https://docs.useanything.com/features/system-prompt-variables

System prompt variables allow you to inject **dynamic** and **static** variables into your system prompt on the fly. This is useful for a variety of use cases, such as:

- Injecting the user's name into the system prompt
- Injecting the current date and time into the system prompt
- Injecting static information into the system prompt like your company's name
- and more!

#### Default Variables

> **Tip:**
>
> AnythingLLM can have varying default variables depending on if you are using the **AnythingLLM via Docker** or **AnythingLLM Desktop** version.

AnythingLLM comes with a set of default variables that you can use in your system prompt. You can view the full list of active variables by clicking on the **System Prompt Variables** link in the sidebar under **Tools** when on the settings page.

![AnythingLLM System Prompt Variables](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fsystem-prompt-variables%2Fsidebar-link.png&w=3840&q=100)

| Variable | Description | Available in |
| --- | --- | --- |
| `{date}` | The current date | ALL VERSIONS |
| `{time}` | The current time | ALL VERSIONS |
| `{datetime}` | The current date and time | ALL VERSIONS |
| `{user.name}` | The name of the user | AnythingLLM Docker (with multi-user mode enabled) |
| `{user.bio}` | The bio field of the user | AnythingLLM Docker (with multi-user mode enabled) |
| `{os.name}` | The name of the operating system | AnythingLLM Desktop |
| `{os.arch}` | The architecture of the operating system | AnythingLLM Desktop |

*Note: Any time based variable will the current time **of the machine** AnythingLLM is running on. Keep this in mind in Docker based versions of AnythingLLM.*

#### Custom Variables

You can also create your own custom variables by clicking the **Add Variable** button on the **System Prompt Variables** page.

![AnythingLLM Custom Variables](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fsystem-prompt-variables%2Fadd-variable.png&w=3840&q=100)

All user created variables are static values and will not change when expanded into a system prompt.

#### How to use system prompt variables

> **Tip:**
>
> Invalid variables will simply not be expanded into the system prompt - you will not see an error message during an LLM request.
>
> You can tell if a variable is invalid once you stop editing the system prompt and it is **not highlighted in blue** in the UI.

System prompt variables can be used any workspace's **System Prompt** field. You can inject a variable by editing the system prompt and using the variable in the prompt.

Example:

```
You are a helpful assistant.
Today is {date} and the current time is {time}.
The user's name is {user.name}, they work at {company_name} and this is what we know about them:
{user.bio}
```

When expanded into a system prompt, it will look like this:

```
You are a helpful assistant.
Today is 2024-01-01 and the current time is 12:00:00.
The user's name is John Doe, they work at Google and this is what we know about them:
Rock climbing is my favorite hobby and I am obsessed with optimizing AI agents and workflows.
```

##### UI Example:

![AnythingLLM System Prompt Variables](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fsystem-prompt-variables%2Fsystem-prompt-var.png&w=3840&q=100)

### Transcription Models

*AnythingLLM supports custom audio transcription providers.*

**Source:** https://docs.useanything.com/features/transcription-models

![AnythingLLM Transcription Models](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Ftranscription-models%2Fheader-image.png&w=3840&q=100)

AnythingLLM supports custom audio transcription providers.

#### Supported Transcription Model Providers

##### Local Transcription Model Providers

[![AnythingLLM Built-in (Xenova)](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Ftranscription-models%2Fxenova.png&w=3840&q=100)Built-in (Xenova)→](https://huggingface.co/Xenova/whisper-small)

##### Cloud Transcription Model Providers

[![OpenAI](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Ftranscription-models%2Fopenai.png&w=3840&q=100)OpenAI→](https://platform.openai.com/)

### Vector Databases

*AnythingLLM allows you to use a host of LLM providers for chatting and generative AI.*

**Source:** https://docs.useanything.com/features/vector-databases

![AnythingLLM Vector Databases](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fheader-image.png&w=3840&q=100)

AnythingLLM comes with a private built-in vector database powered by [LanceDB](https://lancedb.com/). Your vectors never leave AnythingLLM when using the default option.

AnythingLLM supports many vector databases providers out of the box.

#### Supported Vector Databases

##### Local Vector Databases Providers

[![LanceDB](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Flancedb.png&w=3840&q=100)LanceDB (Built-in)→](https://github.com/lancedb/lancedb)[![PGVector](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fpgvector.png&w=3840&q=100)PGVector→](https://github.com/Mintplex-Labs/anything-llm/blob/master/server/utils/vectorDbProviders/pgvector/SETUP.md)[![Chroma](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fchroma.png&w=3840&q=100)Chroma→](https://github.com/chroma-core/chroma)[![Milvus](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fmilvus.png&w=3840&q=100)Milvus→](https://github.com/milvus-io/milvus)

##### Cloud Vector Databases Providers

[![Pinecone](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fpinecone.png&w=3840&q=100)Pinecone→](https://www.pinecone.io/)[![Zilliz](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fzilliz.png&w=3840&q=100)Zilliz→](https://zilliz.com/)[![AstraDB](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fastra-db.png&w=3840&q=100)AstraDB→](https://www.datastax.com/)[![QDrant](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fqdrant.png&w=3840&q=100)QDrant→](https://qdrant.tech/)[![Weaviate](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fvector-databases%2Fweaviate.png&w=3840&q=100)Weaviate→](https://weaviate.io/)


---

## Chatting with Documents (RAG)

### Using Documents in AnythingLLM

*Learn about how to use documents in chat - and how to make the LLM use them for better answers.*

**Source:** https://docs.useanything.com/chatting-with-documents/introduction

*This documentation only applies to any version of AnythingLLM 1.8.5 and above.*

### Using Documents in AnythingLLM

Leveraging custom and uploaded documents in your chats is the most powerful use-case for AnythingLLM has a fully customizable document management system that is both
easy to use and powerful right out of the box.

AnythingLLM supports both **attaching documents** and **embedding documents** (RAG & Reranking) for your convenience and flexibility.

#### Attaching documents in chat

> **Tip:**
>
> Uploaded documents in the chat are **workspace** and **thread** scoped. This means that documents uploaded in one thread will not be available in another chat. If you want a document
> to be available in multiple threads, you will need to upload it to the workspace as an embedded document.
>
> [Learn more about RAG vs Attached Documents](https://docs.useanything.com/chatting-with-documents/introduction#rag-vs-attached-documents)

Using documents in chat is simple - simply drag and drop your documents into the chat window **or** click on the `+` icon in the prompt input.

[Video](https://docs.useanything.com/images/document-chat/upload-documents.mp4)

##### Documents and Context

By default, AnythingLLM will insert the **full text** of your documents into the chat window. This is a powerful feature, but it can also be overwhelming for really large documents or situations where the model's context window is limited.

If you exceed the context window while adding documents, AnythingLLM will ask you if you want to chunk the documents into smaller pieces (aka: `embed`). Embedding documents is called [**RAG**](https://docs.useanything.com/chatting-with-documents/introduction#what-is-rag) and is a powerful technique that allows LLMs to use external data sources to answer questions without
overloading the model's context window. There are tradeoffs to this approach, but it is a powerful way to get the best of both worlds.

You can monitor the context window size in the chat window by hovering over the `+` icon in the prompt input when documents are attached to the chat. Which is denoted by the number above the `+` icon.

![Manage Attached Documents](https://docs.useanything.com/_next/image?url=%2Fimages%2Fdocument-chat%2Fmanage-attached-docs.png&w=2048&q=75)

##### You exceed the context window - what now?

If you exceed the context window of your current model, AnythingLLM will ask you if you want to chunk the documents into smaller pieces (aka: `embed`).

Embedding documents is called [**RAG**](https://docs.useanything.com/chatting-with-documents/introduction#what-is-rag) and is a powerful technique that allows LLMs to use external data sources to answer questions without

![Context Warning](https://docs.useanything.com/_next/image?url=%2Fimages%2Fdocument-chat%2Fcontext-warning.png&w=2048&q=75)

**Cancel**: Will remove the documents from the chat window.

**Continue Anyway**: Will continue to add the document full text to the chat window, but data will be lost in this process as AnythingLLM will automatically prune the context to fit. You should not do this as you will expierence inaccurate LLM behavior.

**Embed**: Will embed the document (RAG) and add it to the workspace. This will allow the LLM to use the document as a source of information, but it will not be able to use the full text of the document. This option may or may not be visible depending on your permissions on the workspace.

> **Warning:**
>
> **Embedding** a document makes the document available to every thread in the workspace.
>
> In multi-user mode, embedding a document will make the document available to every user who has access to the workspace.

#### RAG vs Attached Documents

**RAG (Retrieval Augmented Generation)**

RAG is a technique of splitting and chunking documents into smaller pieces and **only retrieving a small amount of semantically relevant context** to the LLM. This reduces the amount of information the LLM has to process, but it also reduces the amount of information the LLM can use to answer the question.

**Attached Documents**

Attached documents are documents that are uploaded to the workspace and are available to the LLM. This means that the LLM can use the **full text of the document** to answer the question. This will take longer and potentially cost more to process but your answers will be very accurate.

##### RAG settings

AnythingLLM exposes many many options to tune your workspace to better fit with your selection of LLM, embedder, and vector database.

The workspace options are the easiest to mess with and you should start there first. AnythingLLM makes some default assumptions in each workspace. These work for some but certainly not all use cases.

You can find these settings by hovering over a workspace and clicking the "Gear" icon.

![AnythingLLM Workspace settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffaq%2Fllm-not-using-my-docs%2Fworkspace-settings-icon.png&w=3840&q=100)

##### Vector Database Settings > Search Preference (Reranking)

> **Tip:**
>
> For now, this option is only available if you are using LanceDB (default) as your vector database.

![AnythingLLM Workspace RAG Search Preference](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffaq%2Fllm-not-using-my-docs%2Fvector-search-preference.png&w=3840&q=100)

By default, AnythingLLM will search for the most relevant chunks of text. For the majority of use cases this is the best option since it is very simple to run and very fast to calculate.

However, if you are getting bad results, you may want to try "Accuracy Optimized" instead. This will search *more* chunks of text and then re-rank them to the top chunks that are most relevant to your query. This process is slightly slower but will yield better results in almost all cases.

Reranking is computationally more expensive and on slower machines it may take more time that the you are willing to wait. Like the embedder model, this model will download **once** on it's first use. This is a workspace specific setting so you can experiment with it in different workspaces.

> From our testing, the reranking process will add about 100-500ms to the response time depending on your computer or instance performance.

##### Vector Database Settings > Max Context Snippets

This is a very critical item during the "retrieval" part of RAG. This determines "How many relevant snippets of text do I want to send to the LLM". Intuitively you may think "Well, I want all of them", but that is not possible since there is an upper limit to how many tokens each model can process. This window, called the context window, is shared with the system prompt, context, query, and history.

AnythingLLM will trim data from the context if you are going to overflow the model - which will crash it. So it's best to keep this value anywhere from 4-6 for the majority of models. If using a large-context model like Claude-3, you can go higher but beware that too much "noise" in the context may mislead the LLM in response generation.

##### Vector Database Settings > Document similarity threshold

This setting is likely the cause of the issue you are having! This property will filter out low-scoring vector chunks that are likely irrelevant to your query. Since this is based on mathematical values and not based on the true semantic similarity it is possible the text chunk that contains your answer was filtered out.

If you are getting hallucinations or bad LLM responses, you should set this to No Restriction. By default the minimum score is 20%, which works for some but this calculated values depends on several factors:

- Embedding model used (dimensions and ability to vectorize your specific text)
  - Example: An embedder used to vectorize English text may not do well on Mandarin text.
  - The default embedder is <https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2>
- The density of vectors in your specific workspace.
- More vectors = more possible noise, and matches that are actually irrelevant.
- Your query: This is what the matching vector is based on. Vague queries get vague results.

#### Document Pinning

As a last resort, if the above settings do not seem to change anything for you - then document pinning may be a good solution.

Document Pinning is where we do a full-text insertion of the document into the context window. If the context window permits this volume of text, you will get full-text comprehension and far better answers at the expense of speed and cost.

Document Pinning should be reserved for documents that can either fully fit in the context window or are extremely critical for the use-case of that workspace.

![AnythingLLM Document Pinning](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffaq%2Fllm-not-using-my-docs%2Fdocument-pinning.png&w=3840&q=100)

You can only pin a document that has already been embedded. Clicking the pushpin icon will toggle this setting for the document. Pinned documents will not be duplicated as RAG results and are excluded from the RAG process.

### Why does the LLM not use my documents

*We get this question many times a week - here are some common reasons for why an LLM may not appear to 'use' your documents.*

**Source:** https://docs.useanything.com/chatting-with-documents/rag-in-anythingllm

> **Tip:**
>
> This is the legacy documentation for how documents in AnythingLLM worked.
>
> As of AnythingLLM 1.8.5, we have a new way to use documents in chat. Upgrade to the latest version to get the best experience.
>
> [Learn about the new UX for documents in chat](https://docs.useanything.com/chatting-with-documents/introduction)

### Why does the LLM not use my documents?

We get this question many times a week, where someone is confused, or even upset the LLM does not appear to "just know everything" about the documents that are embedded into a workspace.

So to understand why this occurs we first need to clear up some confusion on how RAG (retrieval augmented generation) works inside of AnythingLLM.

This will not be deeply technical, but once you read this you will be an expert on how traditional RAG works.

#### LLMs are not omnipotent

Unfortunately, LLMs are not yet sentient and so it is vastly unrealistic with even the most powerful models for the model you are using to just "know what you mean".

That being said there are a ton of factors and moving parts that can impact the output and salience of an LLM and even to complicate things further, each factor can impact your output depending on what your specific use case is!

#### LLMs do not introspect

In AnythingLLM, we do not read your entire filesystem and then report that to the LLM, as it would waste tokens 99% of the time.

Instead, your query is processed against your vector database of document text and we get back 4-6 text chunks from the documents that are deemed "relevant" to your prompt.

For example, let's say you have a workspace of hundreds of recipes, don't ask "Get me the title of the 3 high-calorie meals". This LLM will outright refuse this! but why?

When you use RAG for document chatbots your entire document text cannot possibly fit in most LLM context windows. Splitting the document into chunks of text and then saving those chunks in a vector database makes it easier to "augment" an LLM's base knowledge with snippets of relevant information based on your query.

Your entire document set is not "embedded" into the model. It has no idea what is in each document nor where those documents even are.

If this is what you want, you are thinking of agents, which are coming to AnythingLLM soon.

#### So how does AnythingLLM work?

Let's think of AnythingLLM as a framework or pipeline.

1. A workspace is created. The LLM can only "see" documents embedded in this workspace. If a document is not embedded, there is no way the LLM can see or access that document's content.
2. You upload a document, this makes it possible to "Move into a workspace" or "embed" the document. Uploading takes your document and turns it into text - that's it.
3. You "Move document to workspace". This takes the text from step 2 and chunks it into more digestable sections. Those chunks are then sent to your embedder model and turned into a list of numbers, called a vector.
4. This string of numbers is saved to your vector database and is fundamentally how RAG works. There is no guarantee that relevant text stays together during this step! This is an area of active research.
5. You type a question into the chatbox and press send.
6. Your question is then embedded just like your document text was.
7. The vector database then calculates the "nearest" chunk-vector. AnythingLLM filters any "low-score" text chunks (you can modify this). Each vector has the original text it was derived from attached to it.

> **Warning:**
>
> **IMPORTANT!**
>
> This is not a purely semantic process so the vector database would not "know what you mean".
>
> It's a mathematical process using the "Cosine Distance" formula.
>
> However, here is where the embedder model used and other AnythingLLM settings can make the most difference. Read more in the next section.

8. Whatever chunks deemed valid are then passed to the LLM as the original text. Those texts are then appended to the LLM as its "System message". This context is inserted below your system prompt for that workspace.
9. The LLM uses the system prompt + context, your query, and history to answer the question as best as it can.

Done.

*This informative document is now deprecated. [Learn more about using documents in chat](https://docs.useanything.com/chatting-with-documents/introduction)*


---

## Chat UI

### ChatUI Walkthrough

*Learn how the basics of chatting in AnythingLLM*

**Source:** https://docs.useanything.com/chat-ui

![AnythingLLM Chat UI](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fchat-ui.png&w=3840&q=100)

### Overview of the chat interface

The chat interface of AnythingLLM is where you will spend most of your time when using AnythingLLM, as such you should familiarize yourself with the basics. This page could have some additional
icons that are not in the above image, as we are always improving AnythingLLM.

The above image may seem like a lot, but you will soon find the interface intuitive and familiar with other interfaces you have used.

#### User messages

User messages are messages that you have sent. This is the text that is used to find similar documents as well as what is sent to the LLM.

##### Actions

- Copy: Copy the content of this text box.
- Edit: Editing a message allows you to amend and automatically resubmit the conversation from that point to the LLM. **Beware** that this will truncate all messages below the edited content.
- Speak: Use the operating system native text-to-speech module, OpenAI Voice, or an 11Labs voice to speak your text.

#### LLM messages

LLM messages are responses from your LLM that are active in this chat session. This is the text that is used to find similar documents as well as what is sent in future conversations. History is automatically managed when the context window is exceeded.

##### Actions

- Copy: Copy the content of this text box.
- Edit: Editing a message allows you to amend the *output* of an LLM message for correctness. This does *not* resubmit your prompt and simply will update the history.
- Regenerate: Resend a prompt back to the LLM with the same prompt and history to get a new answer.
- Feedback (Thumbs Up & Thumbs Down): Allow the user to leave qualitative feedback on an LLM response. Leaving feedback **has no impact on message history or future responses**. Feedback metrics are most useful for [exporting of chats](https://docs.useanything.com/features/chat-logs) to be able to sort through good responses for creating fine-tunes outside of AnythingLLM.

#### Prompt Input Controls

- Slash Commands: `Slash Commands` are ways to inject some standard text into your prompt where that command is present. It is basically a short-key for text snippets. You can create and manager your slash commands here.
  - Default Slash Commands: These are special commands built by the core-team that have special functions like `/reset`
- `@agent` Invocation: View all available `@agents` and their available skill sets. Using `@agent` at the start of a prompt will start an agent session. [Learn more about agents here.](https://docs.useanything.com/agent/overview)
- Font Size: Set the default font size for your profile of AnythingLLM.
- Microphone: Enable voice-to-text inputs for your LLM prompts.**This feature is not available on Desktop.**


---

## AI Agents - Overview & Setup

### AI Agents

*What are AI Agents in AnythingLLM and how to use them?*

**Source:** https://docs.useanything.com/agent/overview

[Video](https://webassets.anythingllm.com/docs-agent-example.mov)

### AI Agents

Agents are LLMs that have the ability to use tools to perform tasks to complete your requests. There are a number of pre-provided tools by default, but you can also create your [own custom tools](https://docs.useanything.com/agent/custom/introduction), [use MCPs](https://docs.useanything.com/mcp-compatibility/overview), or even use [Agent Flows](https://docs.useanything.com/agent-flows/overview) to build your own custom tools.

AnythingLLM will automatically determine if your LLM can use tools so that every chat is more intelligent. However, now all LLMs can use tools, you can still choose to use the `@agent` directive at the start of your chat to start an agentic chat session.

#### Quick Links

[Agent Setup Guide](https://docs.useanything.com/agent/setup)[Intelligent Tool Selection](https://docs.useanything.com/agent/setup#intelligent-tool-selection)[Agent Usage Guide](https://docs.useanything.com/agent/usage/overview)

### AI Agent Setup

*This guide explain how to setup AI Agents on AnythingLLM*

**Source:** https://docs.useanything.com/agent/setup

### Setting up AI Agents

#### Configure your Agent

By default, your workspace will use the system LLM for agentic chat sessions. You can optionally change the model and provider *per workspace* if you want to use a different LLM for agentic chat sessions for a given workspace.

Open the workspace settings and go to the agent configuration menu

![AnythingLLM Agent Workspace Configuration Menu](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fagent-configuration%2Fconfiguration-menu.png&w=3840&q=100)

#### Configure your available skills

On the Agent Skills page via `Settings > Agent Skills`, you can granularly choose which skills you want your Agent to be able to use. Some skills are enabled by default. Some skills require additional configuration.
You can click on a skill to see more information about it, including the required configuration - if any.

Be sure to click the "Save" button to save your changes.

![AnythingLLM Agent Skills Configuration](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fagent-configuration%2Fconfigure-agent-skills-button.png&w=3840&q=100)

You can also toggle skills from the prompt input in the chat UI by clicking on the "Tools" button.

![AnythingLLM Agent Prompt Tools Menu](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fagent-configuration%2Fprompt-tools-menu.png&w=3840&q=100)

#### Example: Configure your search provider

One of the tools agents can use is `Web-Browsing` which allows agents to browse the internet.

By default, AnythingLLM will use the DuckDuckGo search engine to browse the internet - this requires no additional configuration. You can change this to use a different search provider by clicking on the "Search Provider" button.

![AnythingLLM Agent Search Provider Configuration](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fagent-configuration%2Fsearch.png&w=3840&q=100)

### Intelligent Tool Selection

AnythingLLM is pioneering the concept of **Intelligent Tool Selection**. This allows any model to have access to **unlimited** tools but without the trade-off bloated token usage and performance bottlenecks saving up to 80% every single chat.

In other providers like OpenWebUI, Claude, or others, every single tool and MCP will be added to the prompt window **every chat!** This is a major performance bottleneck and can quickly lead to context limits being reached within a few chats as well
as decreased performance and increased token usage or costs.

With Intelligent Tool Selection, AnythingLLM will only add the tools and MCPs that are actually useful for the chat to the prompt window.

#### How to enable Intelligent Tool Selection?

In the Agent Skills page via `Settings > Agent Skills`, you can enable Intelligent Tool Selection by clicking the settings icon on this page.

![AnythingLLM Agent Intelligent Tool Selection Configuration](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fagent-configuration%2Fintelligent-tool-selection.png&w=3840&q=100)

### Intelligent Tool Selection

*Load unlimited tools into context with better performance and save up to 80% on token usage every single chat*

**Source:** https://docs.useanything.com/agent/intelligent-tool-selection

> **Tip:**
>
> Intelligent Tool Selection is an enabled by default feature. You can disable it in the Agent Skills page via `Settings > Agent Skills`.

AnythingLLM ships with the concept of **Intelligent Tool Selection**. This allows any model to have access to **unlimited** tools but without the trade-off bloated token usage and performance bottlenecks **saving up to 80% every single chat**.

In other providers like OpenWebUI, Claude, or others, every single tool and MCP will be added to the prompt window **every chat!** This is a major performance bottleneck and can quickly lead to context limits being reached within a few chats as well
as decreased performance and increased token usage or costs.

With Intelligent Tool Selection, AnythingLLM will only add the tools that are actually useful for the chat to the prompt window.

Intelligent Tool Selection adds a small overhead to each chat, but it is worth it to save on token usage and performance. It only kicks in when you have more than the `Max Tools` value set in the Agent Skills panel.

#### How to enable Intelligent Tool Selection?

In the Agent Skills page via `Settings > Agent Skills`, you can enable Intelligent Tool Selection by clicking the settings icon on this page.

![AnythingLLM Agent Settings Menu Icon Location](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fagent-configuration%2Fsettings-menu-icon-location.png&w=3840&q=100)

From this menu, you can enable Intelligent Tool Selection by clicking the "Intelligent Tool Selection" toggle.

![AnythingLLM Agent Settings Menu](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fagent-configuration%2Fsettings-menu.png&w=3840&q=100)

#### Benefits of Intelligent Tool Selection

- **Better Performance**: Only add the tools that are actually useful for the chat to the prompt window. This means less tokens overall so you get a faster response time - this is especially useful for local models
- **Save up to 80% on token usage every single chat**: This is a major performance improvement and can help you save on token usage and costs. For local models, this leads to much faster response times. For cloud models, this leads to lower costs and faster response times.
- **Better Context Management**: This allows you to keep your context for actual chats and information instead of just tools that are not useful for the chat.

With Intelligent Tool Selection, you dont have to worry about the granular selection of tools every single chat - it is automatically done for you so you can continue to just add more and more tools to help you be more productive.

#### Why would I want to disable Intelligent Tool Selection?

There are really only two reasons to disable Intelligent Tool Selection:

1. If you are on a very low-end device with limited resources, you may want to disable Intelligent Tool Selection to save on resources and decrease the overall load on your system.
2. You want to save the extra 100-500ms on each chat since we rerank each chat so tools are managed every query.

### Why is my AI Agent not using tools!

*AI Agents unlock new use cases for LLMs, but they are not foolproof. Read on for common issues with OSS LLMs not using tools.*

**Source:** https://docs.useanything.com/agent-not-using-tools

### Why is my `@agent` not using tools!

AI Agents unlock new and exciting ways to use and leverage LLMs to *do things* for you as opposed to just reply with text. However, these LLMs are still not fully intelligent and like other implementations
of LLMs - this method is not without its "gotchas".

Like other LLM problems, this mostly comes down to the model you are using and as always a more powerful & capable model yields better results. When using agents, we recommend the best model you can run.

*caveat*: There are some smaller models that are specifically trained for JSON/function calling and they can be used in lieu of just a larger model, but this has its own drawbacks when you want to
then get the final response back as a normal chat. In general, you should use a general text/instruct model.

#### What even is an agent?

Without getting too technical there is some foundational knowledge to understand *what* an "AI Agent" even is. The below graphics really
describe what LLMs are doing and "reasoning" about. As you can see, its no different that a specifically formatted text response!

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffaq%2Fagent-not-using-tools%2Fregular.png&w=3840&q=100)
![](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffaq%2Fagent-not-using-tools%2Fllm.png&w=3840&q=100)

So now that we know LLMs are basically doing an extra step in between your prompt and it's final answer, any agent's implementation usually goes wrong in the JSON generation part.

Okay, so now that we know how this pipeline works in order for an agent to even function works, how can we solve and debug issues?

#### Some LLMs are *bad* at generating JSON and even worse at following instructions.

> **Tip:**
>
> **Tip:**
> Cloud based (un-quantized) models are typically *dramatically* better at following instructions and forming valid JSON matching the required tool-call.
>
> You can use a cloud based model for *just agent calls* in AnythingLLM and use an open-source model for normal chatting.

The main issue we see with agents are people who want to use a smaller parameter model that is heavily quantized and want to get GPT-level quality tool interactions.
Below are the reasons + ways to mitigate the effects of bad tool calls and their common solutions.

#### Model is hallucinating a tool call.

When a tool is *actually* called you will see what we call a "thought" output to the UI. This indicates that the tool was actually called. If the LLM responds with information and you don't see a thought-chain, it is likely
making up the output and pretended to call a tool.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffaq%2Fagent-not-using-tools%2Fthought.png&w=3840&q=100)

##### Common Solutions

- Swap to a high quantization version or larger param model
- `/reset` chat history and re-ask the prompt

#### LLM says it cannot call `XYZ` tool.

Some models are aligned too heavily and will refuse to use some tools because of their training. This is common for requests like website scraping.

##### Common Solutions

- Swap to a high quantization version, larger param model, or less restricted model
- `/reset` chat history and re-ask the prompt
- Turn off tools you are not using to reduce prompt window size

#### LLM is refusing to even detect or call a tool at all.

Open-source models, with their quantization and limited context window are susceptible to just refusing to discover or call a tool properly.

When tools are injected into the LLMs prompt for discovery and execution they can quite often be "overloaded" with information or due to their quantization are unable
to create valid JSON that *exactly matches* the schema required for a tool call to succeed. The LLM is simply generating JSON, something lower-param and quantized models are *particularly bad at*!

AnythingLLM however does make some significant corrections to have slightly invalid JSON be formatted properly so a call can succeed, but we can only do so much on this front.

##### Common Solutions

- Swap to a high quantization version, larger param model, or less restricted model
- `/reset` chat history and re-ask the prompt (chat history can sometimes impact output of JSON)
- Turn off tools you are not using to reduce prompt window size and load on prompt.


---

## AI Agents - Usage Guides

### AI Agent Usage

*How to use AI Agents on AnythingLLM*

**Source:** https://docs.useanything.com/agent/usage/overview

![AI Agent Usage](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fusage.png&w=3840&q=100)

#### How to use AI Agents?

> **Warning:**
>
> **Note**
>
> Before you use AI Agents, you have to configure your AI Agents by following our [Agent Setup Guide](https://docs.useanything.com/agent/setup)

When in the main chat UI, check to see if the `@` symbol is present in the prompt input.
If this symbol is present, you **must** mention the agent by `@agent` to start an agent session to use tools.
If this symbol is not present, you are automatically in agentic chat mode with every chat.

![AnythingLLM AI Agents Trigger](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Ftrigger.png&w=3840&q=100)

When you mention the agent, you will see a popup with the tools enabled for the agent on the workspace.

  

**Agents have access to the following tools:**

[RAG Search](https://docs.useanything.com/agent/usage/rag-search)[Web Browsing](https://docs.useanything.com/agent/usage/web-browsing)[Web Scraping](https://docs.useanything.com/agent/usage/web-scraping)[Save Files](https://docs.useanything.com/agent/usage/save-files)[List Documents](https://docs.useanything.com/agent/usage/list-documents)[Summarize Documents](https://docs.useanything.com/agent/usage/summarize-documents)[Chart Generation](https://docs.useanything.com/agent/usage/chart-generation)[SQL Agent](https://docs.useanything.com/agent/usage/sql-agent)[File System Agent](https://docs.useanything.com/agent/usage/file-system-agent)[Create Scheduled Jobs](https://docs.useanything.com/agent/usage/create-scheduled-job)

#### Frequently Asked Questions

##### 1) How can I know if the agent session is started or ended?

When a Agent session is started you will see the log `Agent @agent invoked` on your chat.

When a Agent session is ended you will see the log `Agent session completed` on your chat.

##### 2) How can I end a Agent Session?

Simply use the slash command `/exit` to end a agent session

##### 3) Do I have to always mention `@agent` to interact with the agent?

AnythingLLM will automatically determine if your LLM can use tools so that every chat is more intelligent. However, you can still choose to use the `@agent` directive at the start of your chat to start an agentic chat session.

Not all providers allow AnythingLLM to automatically determine if your LLM can use tools so you may need to use the `@agent` directive at the start of your chat to start an agentic chat session.

You will notice the `@` symbol in the prompt input if you are required to use the `@agent` directive at the start of your chat to start an agentic chat session.

If this symbol is not present, you are automatically in agentic chat mode with every chat.

### Chart Generation

*Use Chart Generation to create charts from data*

**Source:** https://docs.useanything.com/agent/usage/chart-generation

#### What is Chart Generation and how to use it?

Chart Generation tool allows the agent to create charts based on the given prompt/data.

Example 1: `@agent can you plot y=mx+b where m=10 and b=0?`

Example 2: `@agent can you look at data.csv and plot that as a pie chat by age?` (*assuming data.csv is in the workspace*)

### Create Scheduled Jobs

*Use the Create Scheduled Jobs agent skill to set up recurring agent tasks conversationally.*

**Source:** https://docs.useanything.com/agent/usage/create-scheduled-job

#### Create Scheduled Jobs

> **Tip:**
>
> This agent skill is **only available in single-user mode**. Self-hosted
> instances running in multi-user mode will not see this skill, and it is hidden
> from the agent in those environments.

The **Create Scheduled Jobs** agent skill lets you set up a [Scheduled Job](https://docs.useanything.com/scheduled-jobs/overview)
just by talking to the agent — no need to open **Settings > Scheduled Jobs** and fill out
the form yourself. Describe what you want done and when, and the agent will create the job
for you.

This is the conversational counterpart to the [Scheduled Jobs](https://docs.useanything.com/scheduled-jobs/overview)
settings page. Anything you can build by hand in that form — a name, a prompt, a schedule, and
a set of allowed tools — the agent can create from a single natural-language request.

#### Enabling the skill

Create Scheduled Jobs is an **opt-in default agent skill**. To turn it on:

1. Open **Settings** > **Agent Skills**
2. Find **Create Scheduled Jobs** in the skills list and enable it.

Once enabled, the skill is available to the agent in any workspace on that instance.

#### How to use it

Just ask the agent to schedule something, in plain language. Be clear about three things:

- **What** the job should do (the task/prompt)
- **When** it should run (the frequency and time)
- **Which tools** it needs, if any

**Example:** `@agent every weekday at 9am, summarize my inbox and email me a digest`

**Example:** `@agent schedule a job to check anythingllm.com every Monday at 8am and note anything new`

**Example:** `@agent create a job that runs every 6 hours and pulls the latest numbers into a report`

When you describe a time, give it in **your local time**. AnythingLLM converts your local
schedule to the correct UTC cron expression deterministically, so you don't need to do any
timezone math — "9am" means 9am where you are.

The agent will only let a job use tools that are actually configured and ready on your instance,
mirroring the tool list you'd see in the manual job form. You can also create a job with no
tools at all, in which case it runs against the LLM alone.

#### After the job is created

When the agent successfully creates a job, it returns a clickable card in the conversation.
Click it to jump straight to that job in **Settings > Scheduled Jobs**, where you can review,
edit the prompt or schedule, run it now, or disable it.

> **Tip:**
>
> New jobs are **enabled by default** as soon as they're created and will fire
> on their next scheduled time. See [Creating Your First
> Job](https://docs.useanything.com/scheduled-jobs/getting-started) for everything you can configure, and
> [Viewing Runs & Results](https://docs.useanything.com/scheduled-jobs/viewing-runs) for how to review what
> each run produced.

### Document Generation Agent

*Use Document Generation Agent to create various document types*

**Source:** https://docs.useanything.com/agent/usage/document-generation-agent

#### Document Generation Agent

> **Tip:**
>
> **Note** We recommend using 8B+ models for PowerPoint generation as they are the most accurate and performant for complex tooling.

Document Generation agent allows your LLM to create documents based on the given prompt/data. This is a built-in agent that is available in AnythingLLM v1.12.0+ but must be enabled in the Agent Skills page via `Settings > Agent Skills`.

**Available document types:**

- Text files
- PDFs
- Excel files
- Docx files
- PowerPoint presentations

[Video](https://webassets.anythingllm.com/docgen.mp4)

### File System Agent

*Use File System Agent to search and manage files on your machine*

**Source:** https://docs.useanything.com/agent/usage/file-system-agent

#### File System Agent

[Video](https://webassets.anythingllm.com/filesearch-agent-demo.mp4)

The file search agent is a skill that you can leverage to search for files across your entire filesystem on the host machine or specific folders you allow it to search.

By default, this skill is disabled and you can granularly choose which folders you want the agent to have read/write access to in the Configuration menu.

![AnythingLLM AI Agents File Search Agent Main Panel](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Ffs-main-panel.png&w=3840&q=100)

#### Docker setup

On Docker, you **must bind volumes** to the container to the `/app/server/storage/anythingllm-fs/` directory. The file search tool **will not** search outside of this directory to prevent any security risks or unauthorized access to your host machine.
This is easy to do by simply modifying the startup command to include the following:

```
export STORAGE_LOCATION=$HOME/anythingllm && \
mkdir -p $STORAGE_LOCATION && \
touch "$STORAGE_LOCATION/.env" && \
docker run -d -p 3001:3001 \
--cap-add SYS_ADMIN \
-v ${STORAGE_LOCATION}:/app/server/storage \
-v ${STORAGE_LOCATION}/.env:/app/server/.env \
### This is an example of binding a volume to the container to 
### the /app/server/storage/anythingllm-fs directory as subfolders.
-v /home/ubuntu/Documents:/app/server/storage/anythingllm-fs/docs
-v /home/ubuntu/Downloads:/app/server/storage/anythingllm-fs/downloads
-v /home/ubuntu/special-folder/subfolder:/app/server/storage/anythingllm-fs/special-folder
### ... and so on and so forth. 
### You can also use suffixes to make a folder read-only at the OS level.
-v /home/ubuntu/readonly-folder:/app/server/storage/anythingllm-fs/readonly:ro
-e STORAGE_DIR="/app/server/storage" \
mintplexlabs/anythingllm
```

Changing files in the host will automatically be reflected and available to the agent since it is a bound volume.

#### Desktop setup

> **Tip:**
>
> **Note** The file system agent is a available as a feature in AnythingLLM v1.12.0+

On Desktop, you will have a `Permissions` section in the skills config panel that allows you to grant the agent access to **specific folders** on your host machine. The permissions are applied to the entire folder and subfolders for both read and write access.

By default, the file system agent has no access to any folders. You will need to grant access to the folders you want the agent to have access to.

![AnythingLLM AI Agents File Search Agent Main Panel](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Ffs-desktop-config.png&w=3840&q=100)

### Gmail Agent

*Use Gmail Agent to search, read, send, and manage emails*

**Source:** https://docs.useanything.com/agent/usage/gmail-agent

#### Gmail Agent

> **Tip:**
>
> This agent skill is only available in AnythingLLM v1.12.1 and later.
>
> **This skill is only available in single-user mode.** It will not be visible in multi-user mode.

> **Tip:**
>
> **Tip:** Any read-only actions will not ask for approval, but any actions that could potentially modify your inbox in any way will ask for approval so nothing can be modified without your explicit permission.
>
> Any skill below that has the ✏️ icon next to it will ask for approval before performing the action.

The Gmail Agent skill allows your LLM to interact with your Gmail account. It can search emails, read messages and threads, compose and send emails, manage drafts, and organize your inbox.

#### Setup

Setup of the Gmail Agent skill is **much** easier than other applications you may have used in the past, since we do not want to inconvenience you by setting up a Google Cloud Project and OAuth2 credentials.

Instead, we will use a simple [Google App Script](https://developers.google.com/apps-script) you
can simply **copy and paste** to provide the same functionality. Google App Scripts are 100% free and have very generous usage limits for your usage.

##### Grab the script

You can grab the open-source script designed for AnythingLLM from [our GApps Github Repository](https://github.com/Mintplex-Labs/anythingllm-gapps/blob/main/gmail/index.gs).

##### Paste the script into the Google App Script editor

Open the [Google App Script editor](https://script.google.com/home) click on the "New Project" button.

Click on the "Untitled Project" and give it a name like "AnythingLLM Gmail Bridge".

Paste the script you copied from the Github Repository into the `Code.gs` file. This should overwrite the existing script text if any exists.

> **Tip:**
>
> **IMPORTANT**
>
> Edit the line near the top of the script that says `const API_KEY = "CHANGE_ME_TO_SOMETHING_SECURE";` and replace `CHANGE_ME_TO_SOMETHING_SECURE` with a unique and random string
> of your choice. This is used as an additional layer of security to authenticate your script with only AnythingLLM.

Once you have edited the `API_KEY` click on the "Deploy > New deployment" button.

On the "Select Type" side of the panel, click on the gear icon and select "Web App".

![AnythingLLM AI Agents Gmail Select Type](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fgmail-select-type.png&w=3840&q=100)

Ensure your "Execute as" is set to "Me" and "Who has access to the app" is set to "Anyone".

![AnythingLLM AI Agents Gmail Deployment Options](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fgmail-deployment-options.png&w=3840&q=100)

Click on the "Deploy" button! You will then be prompted to authorize the script to access your Gmail account. Click on the "Review Permissions" button and configure the permissions as needed or desired for what you want the agent to be able to do.

You will see a popup with the `Deployment Id` of the new deployment. Copy this Id and paste that into the "Deployment ID" field in the AnythingLLM configuration page along with the `API_KEY` you edited earlier.

![AnythingLLM AI Agents Gmail Deployment Id](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fgmail-deployment-id.png&w=3840&q=100)

Dont worry, if you mess up, you can always edit the script and redeploy it!

> **Tip:**
>
> **NOTE:** Once you deploy, you may have to wait a few minutes for the deployment to be fully activated.

#### Capabilities

The Gmail Agent provides a comprehensive set of tools organized into the following categories:

##### Search & Read

These tools allow the agent to search and read your emails without making any changes.

**A note on attachments**

> If your email has attachments, the agent will be able to download the attachments and use them in context. You will be asked before the agent downloads any attachments so you can curate which attachments are used in context.

###### Gmail Search

Search emails using Gmail's powerful query syntax. Supports keywords and operators like:

- `is:inbox`, `is:unread`, `is:starred`
- `from:email`, `to:email`
- `subject:word`
- `has:attachment`
- `newer_than:7d`, `older_than:1m`

The agent can combine operators with search terms, e.g., `is:inbox meeting notes` finds inbox emails containing "meeting notes".

**Example:** `@agent search for unread emails in my inbox about the project`

###### Gmail Read Thread

Read a full email thread by its ID. Returns all messages in the conversation including sender, recipients, subject, body, date, and attachment information.

**Example:** `Can you read the email about the project update?` -> will find thread by search and read it.

##### Drafts

These tools allow the agent to create, manage, and send draft emails.

###### Create Draft ✏️

Create a new draft email. Supports:

- Multiple recipients (To, CC, BCC)
- Plain text and HTML body content
- File attachments (up to 20MB total)

**Example:** `@agent create a draft email to john@example.com about the meeting tomorrow`

###### Create Draft Reply ✏️

Create a draft reply to an existing email thread. You can choose to reply to just the sender or reply all.

**Example:** `@agent create a draft reply to thread 18abc123def thanking them for the update`

###### Update Draft ✏️

Update an existing draft email with new content, recipients, or attachments.

**Example:** `@agent update draft r123456 to change the subject to "Updated: Meeting Tomorrow"`

###### Get Draft

Retrieve a specific draft email by its ID to view its current content.

**Example:** `@agent show me the draft with ID r123456`

###### List Drafts

List all draft emails in your Gmail account. Returns a summary of each draft including ID, recipient, subject, and date.

**Example:** `@agent list my email drafts`

###### Delete Draft ✏️

Permanently delete a draft email. This action cannot be undone.

**Example:** `@agent delete the draft with ID r123456`

###### Send Draft ✏️

Send an existing draft email immediately. This removes the draft and sends the email.

**Example:** `@agent send the draft with ID r123456`

##### Send & Reply

These tools send emails immediately without creating drafts first.

###### Send Email ✏️

Send an email immediately. Supports:

- Multiple recipients (To, CC, BCC)
- Plain text and HTML body content
- Reply-To address
- File attachments (up to 20MB total)

**Example:** `@agent send an email to john@example.com about the project update`

###### Reply to Thread ✏️

Reply to an existing email thread immediately. You can choose to reply to just the sender or reply all. Supports file attachments.

**Example:** `@agent reply to thread 18abc123def saying I agree with the proposal`

##### Thread Management

These tools help you organize and manage your email threads.

###### Mark as Read ✏️

Mark an email thread as read. This marks all messages in the thread as read.

**Example:** `@agent mark thread 18abc123def as read`

###### Mark as Unread ✏️

Mark an email thread as unread so it appears as a new message.

**Example:** `@agent mark thread 18abc123def as unread`

###### Move to Trash ✏️

Move an email thread to trash. The thread can be recovered from trash within 30 days.

**Example:** `@agent move thread 18abc123def to trash`

###### Move to Archive ✏️

Archive an email thread. The thread is removed from inbox but can still be found in All Mail or by searching.

**Example:** `@agent archive thread 18abc123def`

###### Move to Inbox ✏️

Move an email thread back to inbox. Use this to unarchive a thread or move it from other locations.

**Example:** `@agent move thread 18abc123def to inbox`

##### Account

These tools provide information about your Gmail account.

###### Get Mailbox Stats

Get Gmail mailbox statistics including unread counts for:

- Inbox
- Priority Inbox
- Starred messages
- Spam folder
- Remaining Quote for sending emails

**Example:** `@agent how many unread emails do I have?`

---

#### Update the script

If you ever need to update the script to sync with the latest version of script, you can do the following:

1. Go to the [Google App Script editor](https://script.google.com/home)
2. Click on the "AnythingLLM Gmail Bridge" project or the project name you gave it when you created it.
3. Click on the "Code.gs" file.
4. Edit the script and click on the "Deploy > Manage deployments" button.
5. Click on the "Pencil" icon to edit the script.

![AnythingLLM AI Agents Gmail Manage Deployments](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fgmail-manage-deployments.png&w=3840&q=100)

6. In the first dropdown, select "New Version" and give is some short description.

![AnythingLLM AI Agents Gmail Manage Deployments](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fgmail-new-version.png&w=3840&q=100)

7. Click Deploy New Version!

When updating, you don't need to update AnythingLLM's configuration page, it will automatically point to the new version of the script.

#### Delete the app connection

If you ever need to delete the app connection, you can do the following:

1. Go to the [Google App Script editor](https://script.google.com/home)
2. Click on the "AnythingLLM Gmail Bridge" project or the project name you gave it when you created it.
3. Click on the "Deploy > Manage deployments" button.
4. Click on the "Archive" button for the deployment(s).

![AnythingLLM AI Agents Gmail Archive Deployment](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fgmail-archive-deployment.png&w=3840&q=100)

5. You can now delete the project by clicking on the "Delete" button in the "Project Settings" page.

### Google Calendar Agent

*Use Google Calendar Agent to view, create, and manage calendar events*

**Source:** https://docs.useanything.com/agent/usage/google-calendar-agent

#### Google Calendar Agent

> **Tip:**
>
> This agent skill is only available in AnythingLLM v1.12.1 and later.
>
> **This skill is only available in single-user mode.** It will not be visible in multi-user mode.

> **Tip:**
>
> **Tip:** Any read-only actions will not ask for approval, but any actions that could potentially modify your calendar in any way will ask for approval so nothing can be modified without your explicit permission.
>
> Any skill below that has the ✏️ icon next to it will ask for approval before performing the action.

The Google Calendar Agent skill allows your LLM to interact with your Google Calendar account. It can list calendars, view events, create new events, update existing events, and manage your RSVP status.

#### Setup

Setup of the Google Calendar Agent skill is **much** easier than other applications you may have used in the past, since we do not want to inconvenience you by setting up a Google Cloud Project and OAuth2 credentials.

Instead, we will use a simple [Google App Script](https://developers.google.com/apps-script) you
can simply **copy and paste** to provide the same functionality. Google App Scripts are 100% free and have very generous usage limits for your usage.

##### Grab the script

You can grab the open-source script designed for AnythingLLM from [our GApps Github Repository](https://github.com/Mintplex-Labs/anythingllm-gapps/blob/main/calendar/index.gs).

##### Paste the script into the Google App Script editor

Open the [Google App Script editor](https://script.google.com/home) click on the "New Project" button.

Click on the "Untitled Project" and give it a name like "AnythingLLM Calendar Bridge".

Paste the script you copied from the Github Repository into the `Code.gs` file. This should overwrite the existing script text if any exists.

> **Tip:**
>
> **IMPORTANT**
>
> Edit the line near the top of the script that says `const API_KEY = "CHANGE_ME_TO_SOMETHING_SECURE";` and replace `CHANGE_ME_TO_SOMETHING_SECURE` with a unique and random string
> of your choice. This is used as an additional layer of security to authenticate your script with only AnythingLLM.

Once you have edited the `API_KEY` click on the "Deploy > New deployment" button.

On the "Select Type" side of the panel, click on the gear icon and select "Web App".

![AnythingLLM AI Agents Google Calendar Select Type](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fgmail-select-type.png&w=3840&q=100)

Ensure your "Execute as" is set to "Me" and "Who has access to the app" is set to "Anyone".

![AnythingLLM AI Agents Google Calendar Deployment Options](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fgmail-deployment-options.png&w=3840&q=100)

Click on the "Deploy" button! You will then be prompted to authorize the script to access your Google Calendar account. Click on the "Review Permissions" button and configure the permissions as needed or desired for what you want the agent to be able to do.

You will see a popup with the `Deployment Id` of the new deployment. Copy this Id and paste that into the "Deployment ID" field in the AnythingLLM configuration page along with the `API_KEY` you edited earlier.

![AnythingLLM AI Agents Google Calendar Deployment Id](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fgmail-deployment-id.png&w=3840&q=100)

Dont worry, if you mess up, you can always edit the script and redeploy it!

> **Tip:**
>
> **NOTE:** Once you deploy, you may have to wait a few minutes for the deployment to be fully activated.

#### Capabilities

The Google Calendar Agent provides a comprehensive set of tools organized into the following categories:

##### Calendars

These tools allow the agent to view your calendars.

###### List Calendars

List all calendars the user owns or is subscribed to. Returns calendar names, IDs, time zones, and ownership information.

**Example:** `@agent list all my calendars`

###### Get Calendar

Get details of a specific calendar by ID, including name, description, time zone, and settings.

**Example:** `@agent show me details about my work calendar`

##### View Events

These tools allow the agent to view and search your calendar events without making any changes.

###### Get Event

Get a single event by its ID. Returns full event details including title, time, location, description, guests, and RSVP status.

**Example:** `@agent show me the details of event abc123`

###### Get Events for Day

Get all events for a specific day. Useful for checking your schedule for a particular date.

**Example:** `@agent what's on my calendar for tomorrow?`

###### Get Events

Get events within a date range, optionally filtered by a search query. Supports searching for specific keywords in event titles and descriptions.

**Example:** `@agent find all meetings next week`

**Example:** `@agent search for events containing "standup" in January`

###### Get Upcoming Events

Get upcoming events starting from now. A convenient way to see what's coming up on your calendar.

**Example:** `@agent what are my upcoming events?`

##### Create Events

These tools allow the agent to create new calendar events.

###### Quick Add ✏️

Create an event from a natural language description. Google Calendar will parse the description to extract the event title, date, and time automatically.

**Example:** `@agent add a meeting with John tomorrow at 3pm`

**Example:** `@agent schedule lunch with Sarah next Tuesday at noon`

###### Create Event ✏️

Create a calendar event with full control over all event properties. Supports:

- **Timed events**: Specify start and end times
- **All-day events**: Create events that span entire days
- **Multi-day events**: Create events spanning multiple days
- **Recurring events**: Create daily, weekly, monthly, or yearly recurring events
- **Guests**: Invite attendees by email
- **Location**: Add a physical or virtual location
- **Description**: Add notes or details

**Example:** `@agent create a meeting called "Team Standup" tomorrow from 9am to 9:30am`

**Example:** `@agent create an all-day event for my birthday on March 15th`

**Example:** `@agent create a weekly team meeting every Monday at 10am`

##### Update Events

These tools allow the agent to modify existing calendar events.

###### Update Event ✏️

Update an existing calendar event. You can change:

- Title
- Description
- Location
- Start and end times
- Guest list

Only provide the fields you want to update - other fields will remain unchanged.

**Example:** `@agent change the title of event abc123 to "Updated Meeting"`

**Example:** `@agent move event xyz789 to 3pm`

**Example:** `@agent add Conference Room A as the location for event abc123`

##### RSVP

These tools allow the agent to manage your attendance status for events.

###### Set My Status ✏️

Set your RSVP status for a calendar event. Available statuses:

- **YES**: Accept the invitation
- **NO**: Decline the invitation
- **MAYBE**: Tentatively accept
- **INVITED**: Reset to invited status

**Example:** `@agent accept the meeting invitation for event abc123`

**Example:** `@agent decline event xyz789`

**Example:** `@agent mark myself as maybe for event def456`

---

#### Update the script

If you ever need to update the script to sync with the latest version of script, you can do the following:

1. Go to the [Google App Script editor](https://script.google.com/home)
2. Click on the "AnythingLLM Calendar Bridge" project or the project name you gave it when you created it.
3. Click on the "Code.gs" file.
4. Edit the script and click on the "Deploy > Manage deployments" button.
5. Click on the "Pencil" icon to edit the script.

![AnythingLLM AI Agents Google Calendar Manage Deployments](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fgmail-manage-deployments.png&w=3840&q=100)

6. In the first dropdown, select "New Version" and give is some short description.

![AnythingLLM AI Agents Google Calendar Manage Deployments](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fgmail-new-version.png&w=3840&q=100)

7. Click Deploy New Version!

When updating, you don't need to update AnythingLLM's configuration page, it will automatically point to the new version of the script.

#### Delete the app connection

If you ever need to delete the app connection, you can do the following:

1. Go to the [Google App Script editor](https://script.google.com/home)
2. Click on the "AnythingLLM Calendar Bridge" project or the project name you gave it when you created it.
3. Click on the "Deploy > Manage deployments" button.
4. Click on the "Archive" button for the deployment(s).

![AnythingLLM AI Agents Google Calendar Archive Deployment](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fgmail-archive-deployment.png&w=3840&q=100)

5. You can now delete the project by clicking on the "Delete" button in the "Project Settings" page.

### List Documents

*Use List Documents to see all documents the agent can access*

**Source:** https://docs.useanything.com/agent/usage/list-documents

#### What is List Documents and how to use it?

List Documents tool allows the agent to see and tell you all the documents it can access (documents that are embedded in the workspace)

Example: `@agent could you please tell me the list of files you can access now?`

![AnythingLLM AI Agents List Documents](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Flist-document.png&w=3840&q=100)

### Outlook Agent

*Use Outlook Agent to search, read, send, and manage emails*

**Source:** https://docs.useanything.com/agent/usage/outlook-agent

> **Tip:**
>
> This agent skill is only available in AnythingLLM v1.12.1 and later.
>
> **This skill is only available in single-user mode.** It will not be visible in multi-user mode.

> **Tip:**
>
> **Tip:** Any read-only actions will not ask for approval, but any actions that could potentially modify your mailbox in any way will ask for approval so nothing can be modified without your explicit permission.
>
> Any skill below that has the ✏️ icon next to it will ask for approval before performing the action.

The Outlook Agent skill allows your LLM to interact with your Microsoft Outlook account. It can search emails, read messages and threads, compose and send emails, manage drafts, and view mailbox statistics.

#### Before you start

- This guide **only** supports Single user mode in AnythingLLM.
- You should be familiar with Azure/Entra as their UI is complex and not easily understandable for non-technical users.
- If you encounter any issues with this integration, AnythingLLM core-team is not able to help you with the integration. We will close any support tickets related to this integration that are not bugs for non-Enterprise users.

#### Prerequisites

- Admin account with access to [Microsoft Entra admin center](https://entra.microsoft.com)

#### Create an Entra Application

1. Navigate to the [Microsoft Entra admin center](https://entra.microsoft.com) and sign in with your admin account.
2. Click on "App registrations" in the left sidebar.
3. Click on "+ New registration" button.
4. Enter a name for your application, select the appropriate "Supported account types" (we recommend "Accounts in this organizational directory only" for single-tenant applications)
5. For the "Redirect URI", use the **Web** option and enter the following URL:

DockerDesktop

![AnythingLLM AI Agents Outlook Agent Register App](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Foutlook%2Foutlook-register-app.png&w=3840&q=100)

#### Configure API Permissions

While on your application's overview page, click on the "API permissions" tab.

You will need to add the following permissions:

- email
- Mail.Read
- Mail.ReadWrite
- Mail.Send
- offline\_access
- User.Read

*You **must** add all of these permissions for the agent to work correctly.*

![AnythingLLM AI Agents Outlook Agent API Permissions](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Foutlook%2Foutlook-permissions.png&w=3840&q=100)

Save these changes.

#### Get the Client Secret (Docker only)

> **Tip:**
>
> **Desktop users:** You can skip this section. The Desktop app uses PKCE (Proof Key for Code Exchange) authentication which does not require a client secret.

1. Navigate to your application's overview page and click on the "Certificates & secrets" tab.
2. Click on "+ New client secret" button.
3. Enter a name for your client secret and assign a reasonable expiration date for your use.
4. Click on the "Add" button to create the client secret.
5. Copy the client secret and paste it into the "Client Secret" field in the AnythingLLM configuration page. **Copy the Value Field, not the Id**

![AnythingLLM AI Agents Outlook Agent Copy Client Secret](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Foutlook%2Foutlook-copy-secret.png&w=3840&q=100)

##### Copy other credentials

Depending on your application type, you may need to copy other credentials. They can be found in the "Overview" tab of your application.

![AnythingLLM AI Agents Outlook Agent Client Tenant IDs](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Foutlook%2Foutlook-client-tenant-ids.png&w=3840&q=100)

##### Configure AnythingLLM

1. Navigate to the `Settings > Agent Skills` page and click on the "Outlook Agent" skill.
2. Select the appropriate Application Type, and paste in the credentials you obtained earlier.

![AnythingLLM AI Agents Outlook Agent Start Auth Flow](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Foutlook%2Foutlook-start-auth-flow.png&w=3840&q=100)

3. Click "Authenticate with Microsoft" button to start the authentication flow.

![AnythingLLM AI Agents Outlook Agent Start Auth Flow](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Foutlook%2Foutlook-approve-app.png&w=3840&q=100)

You will be redirected back to your instance of AnythingLLM and you should see the "Outlook Agent" skill enabled and ready to use.

#### Capabilities

The Outlook Agent provides a comprehensive set of tools organized into the following categories:

##### Search & Read

These tools allow the agent to search and read your emails without making any changes.

**A note on attachments**

> If your email has attachments, the agent will be able to download the attachments and use them in context. You will be asked before the agent downloads any attachments so you can curate which attachments are used in context.

###### Outlook Get Inbox

Get recent emails from your Outlook inbox. Returns a list of recent messages with subject, sender, date, and read status.

**Example:** `@agent show me my recent emails` or `@agent what's in my inbox?`

###### Outlook Search

Search emails using Microsoft Search syntax. Supports searching by keywords, sender, subject, and more. Common search terms include:

- `from:email` - emails from a specific sender
- `subject:word` - emails with a specific word in the subject
- `hasAttachments:true` - emails with attachments

The agent can combine search terms, e.g., `from:john@example.com project update` finds emails from John containing "project update".

**Example:** `@agent search for emails about the project` or `@agent find emails from john@example.com`

###### Outlook Read Thread

Read a full email conversation thread by its conversation ID. Returns all messages in the thread including sender, recipients, subject, body, date, and attachment information. Use this after searching to read the full conversation.

**Example:** `Can you read the email about the project update?` -> will find thread by search and read it.

##### Drafts

These tools allow the agent to create, manage, and send draft emails.

###### Create Draft ✏️

Create a new draft email in Outlook. The draft will be saved but not sent. Supports:

- Multiple recipients (To, CC, BCC)
- Plain text and HTML body content
- File attachments

Can also create a draft reply to an existing message by providing a reply-to message ID, with the option to reply all.

**Example:** `@agent create a draft email to john@example.com about the meeting tomorrow`

**Example (reply):** `@agent create a draft reply to the last email thanking them for the update`

###### Update Draft ✏️

Update an existing draft email with new content. You can modify the recipients, subject, body, or CC fields.

**Example:** `@agent update the draft to change the subject to "Updated: Meeting Tomorrow"`

###### List Drafts

List all draft emails in your Outlook account. Returns a summary of each draft including ID, subject, recipients, last modified date, and a preview.

**Example:** `@agent list my email drafts`

###### Delete Draft ✏️

Permanently delete a draft email. This action cannot be undone.

**Example:** `@agent delete the draft about the meeting`

###### Send Draft ✏️

Send an existing draft email immediately. This removes the draft and sends the email. This action cannot be undone.

**Example:** `@agent send the draft I just created`

##### Send & Reply

These tools send emails immediately without creating drafts first.

###### Send Email ✏️

Send an email immediately through Outlook. Supports:

- Multiple recipients (To, CC, BCC)
- Plain text and HTML body content
- File attachments

For composing emails that need review before sending, use the Create Draft tool instead.

**Example:** `@agent send an email to john@example.com about the project update`

###### Reply to Thread ✏️

Reply to an existing email thread immediately. You can choose to reply to just the sender or reply all. Supports file attachments.

**Example:** `@agent reply to the last email saying I agree with the proposal`

**Example (reply all):** `@agent reply all to the team thread confirming the meeting time`

##### Account

These tools provide information about your Outlook account.

###### Get Mailbox Stats

Get Outlook mailbox statistics including folder counts and user profile information. Returns the total and unread counts for:

- Inbox
- Drafts
- Sent Items
- Deleted Items

**Example:** `@agent how many unread emails do I have?`

---

#### Delete the app connection

If you ever need to delete the app connection, you can do the following after disabling the skill in AnythingLLM.

1. Navigate to the [Microsoft Entra admin center](https://entra.microsoft.com) and sign in with your admin account.
2. Click on "App registrations" in the left sidebar.
3. Click on your application and then click on the "Overview" tab.
4. Click on the "Delete" button to delete the application.
5. Click on the "Delete" button to confirm the deletion.

![AnythingLLM AI Agents Outlook Agent Delete App](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Foutlook%2Foutlook-delete-app.png&w=3840&q=100)

### RAG Search

*Use RAG Search to query embedded knowledge in your workspace*

**Source:** https://docs.useanything.com/agent/usage/rag-search

#### What is RAG Search and how to use it?

RAG search allows the agent to check what are the things the agent already know about a specific topic (requires some data to be embedded in workspace)

You can use RAG search by asking the agent something like `@agent can you check what you already know about AnythingLLM?`

![AnythingLLM AI Agents RAG Search](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Frag-search.png&w=3840&q=100)

RAG search can update agent's own memory and that can be later used for recall in agent or regular chat. This embeds a virtual document you cannot manage.

Example: `Ah, great point. Can you summarize and save that summary for later to your memory`

### Save Files

*Use Save Files to save information to your local machine*

**Source:** https://docs.useanything.com/agent/usage/save-files

#### What is Save Files and how to use it?

Save Files tool allows the agent to save any information into a file on your local machine.

Example: `@agent can save this information as a PDF on my desktop folder?`

![AnythingLLM AI Agents Save Files](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fsaving.png&w=3840&q=100)
> **Tip:**
>
> **Note**
>
> AnythingLLM will show you an popup to choose the file location and file name to save the file.

### SQL Agent

*Use SQL Agent to run queries against relational databases*

**Source:** https://docs.useanything.com/agent/usage/sql-agent

#### What is SQL Agent and how to use it?

The built-in SQL agent is a skill that you can leverage to run real-time analytics and queries against a real relational database. The agent can do all of the following:

- `list-databases`: View its current connections and sources it can leverage.
- `list-tables`: View all of the available tables within a database.
- `check-table-schema`: Check the available columns of a table for types and possible value stores.
- `query`: Run a valid SQL query on a database to product a set of `rows` that will later be used in your answer.

> **Note:**
>
> **Caution!**
>
> You should use the SQL agent with a **read-only** database user. While the agent is instructed to not provide anything other than SELECT statements, this does not prevent it from running other SQL commands that could modify your data!

*Example 1:*   
`@agent can you summarize all of the sales volume for May 2024 in the backend-office DB?`

*Example 2:* (*assuming you have the `save-file` skill enabled*)  
`@agent can you grab the emails of the most recent 10 customers and save that to customer.csv?`

### Summarize Documents

*Use Summarize Documents to get summaries of your documents*

**Source:** https://docs.useanything.com/agent/usage/summarize-documents

#### What is Summarize Documents and how to use it?

Summarize Documents tool allows the agent to give you a summary of a document.

Example: `@agent can you summarize the content on https://docs.anythingllm.com/features/chat-logs`

![AnythingLLM AI Agents Summarize Documents](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fsummarize.png&w=3840&q=100)

### Web Browsing

*Use Web Browsing to search the internet for information*

**Source:** https://docs.useanything.com/agent/usage/web-browsing

#### What is Web Browsing and how to use it?

Web Browsing tool allows the agent to search on internet and give you answer for your questions. This basically gives LLM the ability to access internet.

Example: `@agent can you do a web search for "What is the issue going on with MKBHD and Humane AI Pin?" and give me the key information that I need to know`

![AnythingLLM AI Agents Web Browsing](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fbrowsing.png&w=3840&q=100)

### Web Scraping

*Use Web Scraping to extract and embed website content*

**Source:** https://docs.useanything.com/agent/usage/web-scraping

#### What is Web Scraping and how to use it?

Web Scraping tool allows the agent to scrape a website and give you answer for your questions. This embeds a website's content into the workspace and asking question to the LLM to respond based on the content on the embedded website, with agent you don't have to manually embed the website -- the agent will do it automatically for you.

Example: `@agent can you scrape the website anythingllm.com and give me a summary of features AnythingLLM have?`

![AnythingLLM AI Agents Web Scraping](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Fscrape.png&w=3840&q=100)


---

## AI Agents - Custom Skill Development

### Introduction to custom agent skills

*How to create custom agent skills*

**Source:** https://docs.useanything.com/agent/custom/introduction

> **Warning:**
>
> **Warning:** Only run custom agent skills you trust.
>
> Custom agent skills are a powerful feature of AnythingLLM, but they can also be dangerous if misused.
>
> Always make sure to test your skills thoroughly before using them in a production environment & never install untrusted code on any machine.

### Introduction to custom agent skills

AnythingLLM allows you to create custom agent skills that can be used to extend the capabilities of your `@agent` invocations. These skills can be anything you want from a simple API call to even operating-system invocations.

The sky is the limit! Depending on how you run AnythingLLM, you can create custom agent skills that can run extra processes like running a local Python script or, on Desktop, even operating-system invocations.

If it can be done in NodeJS, it can likely be done in AnythingLLM.

#### The current state of custom agent skills

> **Tip:**
>
> Custom agent skills are newly supported in AnythingLLM and may have some bugs, quirks, missing features, unsupported features, etc.
>
> Please report any feature requests or bugs you find to the [GitHub repository](https://github.com/Mintplex-Labs/anything-llm).

1. NodeJS programming experience is required to create custom agent skills. Go to the [developer guide](https://docs.useanything.com/agent/custom/developer-guide) to get started.
2. Custom agent skills must *exactly* match the requirements listed on this help page.
3. There are built in functions and utilities to help you log data or thoughts for an agent.
4. There is currently no established tooling for creating custom agent skills - so follow this guide if developing skills for AnythingLLM.
5. All skills must return a `string` type response - anything else may break the agent invocation.

#### Availability

Custom agent skills are available in the Docker image since [commit `d1103e`](https://github.com/Mintplex-Labs/anything-llm/commit/d1103e2b71ae5550fa33d7d74be5fe3e35e6b1b1) or [release v1.2.2](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.2.2).

Custom agent skills are available in AnythingLLM Desktop version **1.6.5 and later.**

Custom agent skills are **not** available in the AnythingLLM Cloud offering.

#### View loaded custom agent skills

You can view the loaded custom agent skills by opening the `Agent Skills` tab in the settings of AnythingLLM.

Any valid custom agent skills loaded into AnythingLLM will be displayed here.

See [where to place your custom agent skills](https://docs.useanything.com/agent/custom/developer-guide#where-to-place-your-custom-agent-skill-code) for more information.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fcustom-skills%2Fsidebar.png&w=3840&q=100)

#### Dynamic UI of custom agent skills

Custom agent skills can also have a dynamic UI inputs associated with them. This is useful for providing runtime arguments to your custom agent skills or configurable properties of them.

See [how the dynamic UI for a custom agent skill](https://docs.useanything.com/agent/custom/plugin-json#setup_args) is setup via the `plugin.json` file.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fcustom-skills%2Fdynamic-ui.png&w=3840&q=100)

### Custom Agent Skill Developer Guide

*How to create custom agent skills for developers*

**Source:** https://docs.useanything.com/agent/custom/developer-guide

**This guide is intended for developers who want to create custom agent skills for AnythingLLM.**

### How to develop custom agent skills

#### Prerequisites

1. NodeJS 18+
2. Yarn
3. AnythingLLM running in some supported environment see [here](https://docs.useanything.com/agent/custom/introduction) for more information.

#### Guidelines for creation of custom agent skills

1. Custom agent skills must be written in JavaScript and will execute within a NodeJS environment.
2. You can bundle any NodeJS package you want within your custom agent skill, but it must be present in the folder structure of your custom agent skill.
3. All functions must return a string value, anything else may break the agent invocation.
4. You *should* provide a `README.md` file at the root of your custom agent skill with a description, any additional requirements and how to use the custom agent skill.
5. You *must* define your plugin with an associated `plugin.json` file at the root of your custom agent skill folder.
6. The *must* define your entry point of your custom agent skill as a `handler.js` file.
7. You *must* wrap your entire custom agent skill in a folder with the same `name` property that is defined in the `plugin.json` file.

#### Hot loading of custom agent skills

> **Tip:**
>
> If you are in an active agent invocation when you make changes to your custom agent skill, you will need to `/exit` the current session for the changes to take effect.
>
> If you just added a new custom agent skill you will need to revisit or reload the page for the new skill to be shown in the UI.

AnythingLLM supports hot loading of custom agent skills. This means that you can make changes to your custom agent skill and see the changes without having to restart the agent or the instance of AnythingLLM.

#### Where to place your custom agent skill code

All agents skills must be placed in the appropriate folder in your AnythingLLM storage directory folder. This can be found in multiple locations depending on the environment you are running AnythingLLM in.
In all versions you are looking for the matching folder of the `STORAGE_DIR` environment variable.

> **Tip:**
>
> Your entire custom agent skill folder should be wrapped in a folder with the
> same `hubId` property as the associated `plugin.json` file.

##### Docker

Your storage directory should be mounted as a volume in your Docker container startup command - [which can be found here](https://docs.useanything.com/installation-docker/local-docker).
This will be the value of the `STORAGE_LOCATION` command variable.

Then you will need to create this subfolder within the storage directory:
`plugins/agent-skills`

##### Local Development

When running AnythingLLM locally, your storage directory is likely mounted in the `server/storage` directory.

Then you will need to create this subfolder within the storage directory:
`plugins/agent-skills`

##### Desktop

When running AnythingLLM on Desktop, your storage directory can be [found using this guide](https://docs.useanything.com/installation-desktop/storage#where-is-my-data-located).

Then you will need to create this subfolder within the storage directory:
`plugins/agent-skills`

#### File structure

Your custom agent skill should be wrapped in a folder with the same `hubId` property that is defined in the `plugin.json` file.

*See the plugin.json [reference](https://docs.useanything.com/agent/custom/plugin-json) for more information on the plugin.json file, its properties and how to use them.*

```
// example plugin.json
{
  "name": "This is my human readable name",
  "hubId": "my-custom-agent-skill" // THIS MUST BE THE SAME AS THE parent folder name. Can be any string.
}
```

Folder structure for associated agent skill:
NOTE: The folder name must match the `hubId` property in the `plugin.json` file.

```
plugins/agent-skills/my-custom-agent-skill
|-- plugin.json
|-- handler.js
|-- // You can add any additional files you want to the folder and reference them in the handler.js file!
```

#### Plugin.json Reference

See [here](https://docs.useanything.com/agent/custom/plugin-json) for more information on the plugin.json file, its properties and how to use them.

### handler.js reference

*An example of what the handler.js file should look like.*

**Source:** https://docs.useanything.com/agent/custom/handler-js

**This page is intended for developers who want to create custom agent skills for AnythingLLM.**

#### Rules & Guidelines

- The `handler.js` file must export a `runtime` object with a `handler`
  function.
- The `handler` function must accept a single argument which is an object
  containing the parameters defined in the `plugin.json` `entrypoint`
  property, if any.
- The `handler` function must return a string value, anything else may break
  the agent invocation or loop indefinitely.
- You must use `require` to import any modules you need from the NodeJS
  standard library or any modules you have bundled with your custom agent
  skill.
- You must use `await` when making any calls to external APIs or services.
- You must wrap your entire custom agent skill in a `try`/`catch` block and
  return any error messages to the agent at invocation time.

#### Available runtime properties and methods

##### `this.runtimeArgs`

The `this.runtimeArgs` object contains the arguments that were passed to the `setup_args` from the `plugin.json` file.

You can access the value of a specific argument by using the `propertyName` as the key.

```
// plugin.json excerpt
// "setup_args": {
//     "OPEN_METEO_API_KEY": {
//       "type": "string",
//       "required": false,
//       "input": {
//         "type": "text",
//         "default": "YOUR_OPEN_METEO_API_KEY",
//         "placeholder": "sk-1234567890",
//         "hint": "The API key for the open-meteo API"
//       },
//       "value": "sk-key-for-service",
//     }
//   },
 
this.runtimeArgs["OPEN_METEO_API_KEY"]; // 'sk-key-for-service'
```

##### `this.introspect`

The `this.introspect` function is used to log "thoughts" or "observations" to the user interface while the agent is running.

```
this.introspect("Hello, world!"); // must be a string - will be shown to user
```

##### `this.logger`

The `this.logger` function is used to log messages to the console. This is useful for debugging your custom agent skill via logs.

```
this.logger("Hello, world!"); // must be a string - will be printed to console while the agent is running
```

##### `this.config`

The `this.config` object contains the configuration for your custom agent skill. Useful for when you need to know the name of your custom agent skill or the version or for logs.

```
this.config.name; // 'Get Weather'
this.config.hubId; // 'open-meteo-weather-api'
this.config.version; // '1.0.0'
```

##### `this.requestToolApproval`

The `this.requestToolApproval` method pauses the agent and asks the user to approve a potentially destructive action **before** your skill performs it. It shows the same Approve/Reject card that AnythingLLM's built-in tools use (for example, the Gmail send/reply tools), and resolves once the user responds.

Use this whenever your skill is about to do something irreversible or high-impact — deleting records, sending messages, making purchases, writing to external systems, etc.

```
const approval = await this.requestToolApproval({
  payload: { recordId }, // optional: arbitrary data shown/recorded alongside the request
  description: `Permanently delete record ${recordId}? This cannot be undone.`,
});
 
if (!approval.approved) return approval.message; // user rejected - stop and report back
// ...proceed with the destructive action
```

It returns a `{ approved, message }` object:

- `approved` (`boolean`) — `true` if the user approved (or if approval is not
  required in the current context), `false` if they rejected.
- `message` (`string`) — a human-readable result message. On rejection, return
  this string from your handler so the agent and user know the action was
  declined.

Both arguments are optional — `payload` defaults to `{}` and `description` defaults to `null` — but you should always pass a clear `description` so the user understands exactly what they are approving.

A few behaviors worth knowing:

- The approval is keyed to **your** skill automatically (by its `hubId`). You
  cannot pass a `skillName` to impersonate another tool, and the "Always
  allow" whitelist a user grants applies only to your skill.
- In non-interactive contexts where there is no user to approve (for example,
  a scheduled agent run), the method resolves as approved
  (`{ approved: true, message: "Approval not required in this context." }`) so
  your skill still runs.
- The user has 120 seconds to respond. If they do not respond in time, the
  request is treated as rejected.

### Example `handler.js`

Objective: Get the weather for a given location latitude and longitude using the open-meteo API.

```
// handler.js
// NOT RECOMMENDED: We're using an external module here for demonstration purposes
// this would be a module we bundled with our custom agent skill and would be located in the same folder as our handler.js file
// Do not require modules outside of the plugin folder. It is recommended to use require within a function scope instead of the global scope.
// const _ExternalApiCaller = require('./external-api-caller.js');
 
module.exports.runtime = {
  handler: async function ({ latitude, longitude }) {
    const callerId = `${this.config.name}-v${this.config.version}`;
    try {
      this.introspect(
        `${callerId} called with lat:${latitude} long:${longitude}...`
      );
      const response = await fetch(
        `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m`
      );
      const data = await response.json();
      const averageTemperature = this._getAverage(data, "temperature_2m");
      const averageHumidity = this._getAverage(data, "relativehumidity_2m");
      const averageWindSpeed = this._getAverage(data, "windspeed_10m");
      return JSON.stringify({
        averageTemperature,
        averageHumidity,
        averageWindSpeed,
      });
    } catch (e) {
      this.introspect(
        `${callerId} failed to invoke with lat:${latitude} long:${longitude}. Reason: ${e.message}`
      );
      this.logger(
        `${callerId} failed to invoke with lat:${latitude} long:${longitude}`,
        e.message
      );
      return `The tool failed to run for some reason. Here is all we know ${e.message}`;
    }
  },
  // Helper function to get the average of an array of numbers!
  _getAverage(data, property) {
    return (
      data.hourly[property].reduce((a, b) => a + b, 0) /
      data.hourly[property].length
    );
  },
 
  // Recommended: Use this method to call external APIs or services
  // by requiring the module in the function scope and only if the code execution reaches that line
  // this is to prevent any unforseen issues with the global scope and module loading/unloading.
  // This file should be placed in the same folder as your handler.js file.
  _doExternalApiCall(myProp) {
    const _ScopedExternalCaller = require("./external-api-caller.js");
    return _ScopedExternalCaller.doSomething(myProp);
  },
};
```

### plugin.json reference

*Understand the plugin.json file and how to use it to define custom agent skills for AnythingLLM.*

**Source:** https://docs.useanything.com/agent/custom/plugin-json

**This page is intended for developers who want to create custom agent skills for AnythingLLM.**

### `plugin.json` reference

The `plugin.json` file is used to define a custom agent skill for AnythingLLM. It is a **JSON** file that contains the following properties:

```
{
  // see #active for more information
  "active": true,
 
  // see #hubId for more information
  "hubId": "open-meteo-weather-api",
 
  // see #name for more information
  "name": "Get Weather",
 
  // see #other_properties for more information
  "schema": "skill-1.0.0",
  "version": "1.0.0",
  "description": "Gets the weather for a given location latitude and longitude using the open-meteo API",
  "author": "@tcarambat",
  "author_url": "https://github.com/tcarambat",
  "license": "MIT",
 
  // see #setup_args for more information
  "setup_args": {
    "OPEN_METEO_API_KEY": {
      "type": "string",
      "required": false,
      "input": {
        "type": "text",
        "default": "YOUR_OPEN_METEO_API_KEY",
        "placeholder": "sk-1234567890",
        "hint": "The API key for the open-meteo API"
      },
    }
  },
 
  // see #examples for more information
  "examples": [
    {
      "prompt": "What is the weather in Tokyo?",
      "call": "{\"latitude\": 35.6895, \"longitude\": 139.6917}"
    },
    {
      "prompt": "What is the weather in San Francisco?",
      "call": "{\"latitude\": 37.7749, \"longitude\": -122.4194}"
    },
    {
      "prompt": "What is the weather in London?",
      "call": "{\"latitude\": 51.5074, \"longitude\": -0.1278}"
    }
  ],
 
  // see #entrypoint for more information
  "entrypoint": {
    "file": "handler.js",
    "params": {
      "latitude": {
        "description": "Latitude of the location",
        "type": "string"
      },
      "longitude": {
        "description": "Longitude of the location",
        "type": "string"
      }
    }
  },
 
  // see #imported for more information
  "imported": true
}
```

#### `active`

The `active` property is a boolean that determines if the custom agent skill is active. If it is set to `false`, the custom agent skill will not be loaded.

#### `name`

The `name` property is a string that is used to identify the custom agent skill. This is the human-readable name of the skill that is displayed in the AnythingLLM UI.

#### `hubId`

The `hubId` property is a string that is used to identify the custom agent skill. This must be the same as the parent folder name.

#### `other_properties`

The `other_properties` property is a list of other properties that are used to define the custom agent skill. These are mostly optional and will not impact performance of the skill directly. See reference below for more information.

```
{
  "schema": "skill-1.0.0", // REQUIRED - do not change
  "version": "1.0.0", // REQUIRED - can be defined by user
  "description": "short description of the custom agent skill", // REQUIRED
  "author": "@tcarambat", // OPTIONAL - author tag of the custom agent skill
  "author_url": "https://github.com/tcarambat", // OPTIONAL - url of the author of the custom agent skill
  "license": "MIT" // OPTIONAL - license of the custom agent skill
}
```

#### `setup_args`

Setup arguments are used to configure the custom agent skill from the UI and make runtime arguments accessible in the handler.js file when the skill is called.
The key of the setup argument is the name of the argument that is used in the handler.js file, while its properties automatically generate the UI and inputs for the argument in the AnythingLLM UI.

```
"setup_args": {
    "OPEN_METEO_API_KEY": {
      "type": "string", // What type of value is expected
      "required": false, // Is the argument required
      // Defines the UI of the input to be rendered in the AnythingLLM UI
      "input": {
        "type": "text", // What type of input to be rendered
        "default": "YOUR_OPEN_METEO_API_KEY", // Default value of the input
        "placeholder": "sk-1234567890", // Placeholder text for the input
        "hint": "The API key for the open-meteo API" // Hint text for the input
      },
      "value": "" // (optional) preset value of the argument - will be replaced by the user input in the AnythingLLM UI, but can be hardcoded.
    }
  },
```

#### `examples`

The `examples` property is a array of examples that are used to pre-inject examples into the custom agent skill. These are optional but highly encouraged as providing some expected examples helps LLMs determine the more "use-case" oriented implementation of the skill.
Try to provide anywhere from 1-3 examples that are relevant to the skill as these are injected into the prompt and can help guide the LLM in the correct direction.

The `call` property should match the expected input format of the custom agent skill in the `handler.js` file.

```
// handler.js
module.exports.runtime = {
  // latitude and longitude are the expected parameters for the custom agent skill
  handler: async function ({ latitude, longitude }) {
    // ... do something with latitude and longitude
  },
};
```

```
"examples": [
  // Example prompts and expected invocation format for the custom agent skill
  // these are optional but highly encouraged since they help the LLM understand the expected format of the custom agent skill
  // and when to use the associated skill with respect to the user prompt.
  // This is known as "few-shot prompting" and is a best practice when creating custom agent skills.
  {
    "prompt": "What is the weather in Tokyo?",
    "call": "{\"latitude\": 35.6895, \"longitude\": 139.6917}"
  },
  {
    "prompt": "What is the weather in San Francisco?",
    "call": "{\"latitude\": 37.7749, \"longitude\": -122.4194}"
  },
  {
    "prompt": "What is the weather in London?",
    "call": "{\"latitude\": 51.5074, \"longitude\": -0.1278}"
  }
]
```

#### `entrypoint`

The `entrypoint` property is used to define the entrypoint of the custom agent skill **and the expected inputs!** This is the file location and invocation parameters that are used to execute the custom agent skill.

```
"entrypoint": {
  "file": "handler.js", // location of the file to be executed with respect to the plugin.json file
  "params": {
    // all properties require a description and type and should match the expected input format of the custom agent skill in the handler.js file
    "latitude": {
      "description": "Latitude of the location", // Short description of the parameter purpose
      "type": "string" // supported types: string, number, boolean
    },
    "longitude": {
      "description": "Longitude of the location",
      "type": "string"
    }
  }
}
```

#### `imported`

this value must be set to `true`.


---

## Agent Flows (No-Code Automation)

### Getting Started with Flows

*Learn how to access and use the flow builder in AnythingLLM*

**Source:** https://docs.useanything.com/agent-flows/getting-started

> **Tip:**
>
> The below walkthrough is from the Docker version of AnythingLLM, but the
> desktop version works the exact same way.

### Getting Started with Flows

Let's walk through how to access and use the flow builder in AnythingLLM.

#### Accessing the Flow Builder

To create a new flow, navigate to your workspace's agent skills page and click the "Create Flow" button. This will open the flow builder with a blank canvas.

![UI when no flows exist](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fno-flows.png&w=3840&q=100)

#### Understanding the Canvas

When you first open the flow builder, you'll see a blank canvas with some basic blocks. These are the foundation of every flow:

![UI when creating a new flow](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fnew-flow.png&w=3840&q=100)

##### Default Blocks

Every new flow starts with three essential blocks:

1. **Flow Information Block** - Defines the flow's name and description

   ![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fflow-info.png&w=1080&q=100)
2. **Flow Variables Block** - Sets up any variables needed in your flow

   ![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fflow-vars.png&w=1080&q=100)
3. **Flow Complete Block** - Marks the end of your flow

   ![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fflow-complete.png&w=1080&q=100)

You can learn more about these blocks in the [Default Blocks documentation](https://docs.useanything.com/agent-flows/blocks/default-blocks).

#### Adding New Blocks

To add functionality to your flow, you'll need to add blocks. Click the "Add Block" button between any existing blocks to see available options:

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fadd-block.png&w=1080&q=100)

> **Tip:**
>
> Available blocks will vary depending on your AnythingLLM version. Check the
> [blocks documentation](https://docs.useanything.com/agent-flows/blocks/intro) to see which blocks are
> available in your deployment.

#### Saving and Managing Flows

- All new flows are automatically saved as "Enabled"
- Click the "Save" button in the top right to save changes
- Access existing flows from the agent skills page
- Click the gear icon on a flow to edit or delete it

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fhas-flows.png&w=3840&q=100)

#### Next Steps

Now that you understand the basics of the flow builder, try creating your first flow by following our [HackerNews Flow Tutorial](https://docs.useanything.com/agent-flows/tutorial-hackernews)!

### What is an Agent Flow?

*What are Agent Flows in AnythingLLM and how to use them?*

**Source:** https://docs.useanything.com/agent-flows/overview

![AnythingLLM Agent Flow example](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fflow-example.png&w=3840&q=100)

### Agent Flows

Agent Flows are a no-code way to build [agentic skills](https://docs.useanything.com/agent/overview). Using a visual interface, you can build "flows" that can be used in your agents.

The capabilities of agent flows are only limited by your imagination and the tools you have access to. Docker and Desktop versions of AnythingLLM have a built-in agent flow editor and
have various tools available to use in your flows. In general, the desktop version has more tools available to use in your flows.

#### Agent Flows vs Agent skills

In general, agent flows are a more simplified way to build custom agent skills than the traditional [agent skills](https://docs.useanything.com/agent/overview) method. The end result is the same, but the
process of building the skill is different.

- **Agent flows:** No-code way to build agentic skills. Built for everyone.
- **Agent skills:** Code way to build agentic skills. Built for power users and developers.

#### How to use agent flows

Agent flows *work exactly the same* as agent skills, the only difference is the way you build them. You can use agent flows in the same way you use agent skills via the `@agent` directive or by asking
a relevant question while in an agentic chat.

Agent flows are a very flexible way to build agentic skills and depending on the power of your LLM, you can even expect
the LLM to *chain multiple flows together* to complete a task, or call a series of flows in a row to complete a task.

### API Call

*Learn about the API call block and how to use it.*

**Source:** https://docs.useanything.com/agent-flows/blocks/api-call

![API Call](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fapi-call.png&w=3840&q=100)

#### Usage

The API call block is used to make a call to an API. Here you can make a call to any API that you have access to. You can define the body, headers, and method for the API call.
All of the fields are able to leverage variables so you can dynamically change the API call contents and body.

##### POST body usage

The body of a POST request can be a JSON, Raw text, or form data.
Anywhere you want to inject a variable into the body, you can use a the `${variableName}` syntax.

```
{
  "variableProperty": "${variableName}",
  "staticProperty": "staticValue",
  "${variableName}": "staticValue"
}
```

#### Input Variables

- `URL`: The URL of the API to call.
- `Method`: The HTTP method to use.
- `Headers`: The headers to send with the API call.
- `Body`: The body of the API call. (POST only)
- `Result Variable`: The variable to store the result of the API call.

### LLM Instruction

*Learn about the LLM instruction block and how to use it.*

**Source:** https://docs.useanything.com/agent-flows/blocks/llm-instruction

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fllm-instruction.png&w=3840&q=100)
> **Warning:**
>
> Like **any agent call** the LLM instruction block is subject to the ability of
> the LLM to follow the instructions. If the LLM is unable to follow the
> instructions, you will not get the desired output.
>
>   
>   
>
> **Please do not open a support ticket about "my LLM is not following the
> instructions" without first understanding [how LLM tool calling
> works](https://docs.useanything.com/agent-not-using-tools).**

#### Usage

*This block will always use the LLM of the workspace agent that is executing the flow.*

The LLM instruction block is used to provide instructions to the LLM. This is the most flexible and powerful block in the flow editor.

The LLM instruction block is able to leverage variables so you can drive the output of the LLM based on the flow variables and outputs. The more descriptive and detailed you can be in the prompt, the better the output will be.

The ability for the LLM to follow the instructions is subject to the LLM's ability to follow the instructions and the quality of the prompt. If you are having issues with the LLM not following the instructions, you may need to try a different prompt or model.
Do not expect a 3B Q4\_K\_M model to follow the instructions as well as GPT-4, or a 70B Q4\_K\_M model.

#### Input Variables

- `Instructions`: The instructions to send to the LLM.
- `Result Variable`: The variable to store the result of the LLM.

### Read File

*Learn about the Read File block and how to use it.*

**Source:** https://docs.useanything.com/agent-flows/blocks/read-file

> **Warning:**
>
> The **Read File** block is only available on the [**Desktop Version (v1.8.1+)**](https://docs.useanything.com/installation-desktop/overview) of AnythingLLM.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fread-file.png&w=3840&q=100)

#### Usage

> **Tip:**
>
> You can use `${variable}` string to dynamically insert the file path or file name in a fixed folder path.

*This block allows you to read a file from the local file system. Only text file types are supported.*

The Read File block is used to read the contents of a file and store the result in a variable for use in subsequent blocks. This is useful for workflows that require file input or need to process file data.

#### Input Variables

- `File Path`: The path to the file you want to read.
- `Result Variable`: The variable to store the file content.

### Web Scraper

*Learn about the web scraper block and how to use it.*

**Source:** https://docs.useanything.com/agent-flows/blocks/web-scraper

![Web Scraper](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fweb-scraping.png&w=3840&q=100)

#### Usage

The web scraper block is used to scrape a website and extract the content. Currently the web-scraper will return the parsed TEXT content of the page - not the HTML.

The purpose of this block is to allow you to scrape a website and extract the content you need as if you were accessing the website directly. If you are looking for more programmatic access to the HTML, you should use the [API call block](https://docs.useanything.com/agent-flows/blocks/api-call).

#### Input Variables

- `URL to scrape`: The URL of the website to scrape.
- `Result Variable`: The variable to store the result of the web scraping.

### Write File

*Learn about the Write File block and how to use it.*

**Source:** https://docs.useanything.com/agent-flows/blocks/write-file

> **Warning:**
>
> The **Write File** block is only available on the [**Desktop Version (v1.8.1+)**](https://docs.useanything.com/installation-desktop/overview) of AnythingLLM.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fwrite-file.png&w=3840&q=100)

#### Usage

> **Tip:**
>
> You can use `${variable}` string to dynamically insert the file path or file name in a fixed folder path.

*This block allows you to write content to a file on the local file system. Only text output is supported.*

The Write File block is used to save content to a file, which can be useful for exporting results, logging, or passing data to other applications or processes.

#### Input Variables

- `File Path`: The path to the file you want to write to.
- `Content`: The content to write to the file.

### Debugging flows

*How to debug agent flows in AnythingLLM*

**Source:** https://docs.useanything.com/agent-flows/debugging-flows

Often times you will want to debug your flows to ensure they are working as expected. When developing flows, you can use the flow editor to debug your flows while also using the workspace chat
to test the flow and ensure that it is working as expected.

When debugging flows, you will want to **disable all other agent skills** to ensure that the flow is always executed as it will be the only tool available to the LLM.

#### Logs

You can view the logs of an executed flow by [opening the logs of AnythingLLM](https://docs.useanything.com/installation-desktop/debug).
In these log files you will see more verbose output about the flow and the blocks that were executed so you can see what happened.

### Tutorial: HackerNews Flow

*Create your first agent flow by building a HackerNews article filter*

**Source:** https://docs.useanything.com/agent-flows/tutorial-hackernews

### Tutorial: Building a HackerNews Filter Flow

In this tutorial, we'll create a flow that scrapes HackerNews and uses an LLM to filter posts based on topics you're interested in. This flow will help you quickly find articles about topics you care about.

#### Overview of What We're Building

This flow will:

1. Scrape content from HackerNews (from either the front page or newest posts)
2. Use an LLM to filter and extract articles matching your topic of interest
3. Return the relevant articles as clickable links

#### Step 1: Create a New Flow

Start by clicking "Create Flow" in your workspace's agent skills page.

![UI when no flows exist](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fno-flows.png&w=3840&q=100)

#### Step 2: Configure Flow Information

In the Flow Information block, set up:

**Name**:

```
Hacker News Headline Viewer
```

**Description**:

```
This tool can be used to visit hacker news webpage and extract ALL headlines and links from the page that have to do with a particular topic.

Available options for `page`:
(empty) - front page
"newest" - newest posts page

Examples of how to use this flow:
"Find AI-related posts on HackerNews"
"Show me political discussions from the newest HackerNews posts"

The flow will return relevant articles as clickable markdown links.
```

Your flow info block should look like this:

![UI when no flows exist](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fhn-flow-info.png&w=1080&q=100)

#### Step 3: Set Up Flow Variables

In the Flow Variables block, create these variables:

1. **hackerNewsURLPath**

```
Name: hackerNewsURLPath
Default Value: (leave empty)
```

2. **topicOfInterest**

```
Name: topicOfInterest
Default Value: Political discussions or items
```

3. **pageContentFromSite**

```
Name: pageContentFromSite
Default Value: (leave empty)
```

Your flow start block should look like this:

![UI when no flows exist](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fhn-flow-start.png&w=1080&q=100)

#### Step 4: Add Web Scraping Block

1. Click "Add Block" below the Flow Variables block
2. Select "Web Scraper"
3. Configure the block:

```
URL to scrape: https://news.ycombinator.com/${hackerNewsURLPath}
Result Variable: pageContentFromSite
```

Your web scraping block should look like this:

![UI when no flows exist](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fhn-web-scraping.png&w=1080&q=100)

> **Tip:**
>
> The `${hackerNewsURLPath}` syntax allows us to dynamically change which
> HackerNews page we scrape based on user input.

#### Step 5: Add LLM Instruction Block

1. Click "Add Block" below the Web Scraper block
2. Select "LLM Instruction"
3. Configure the block:

**Instructions**:

```
Extract all links from this content that would be relevant to this topic: ${topicOfInterest}

Content:
${pageContentFromSite}

Format your response as a list of markdown links, with a brief description of why each link is relevant.
If no relevant links are found, say "No relevant articles found."
```

```
Result Variable: (leave empty)
```

Your LLM instruction block should look like this:

![UI when no flows exist](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fhn-llm-instruction.png&w=1080&q=100)

#### Step 6: Save and Test

1. Click "Save" in the top right corner
2. Disable other agent skills to ensure this flow is used
3. Test the flow with prompts like:

```
Find AI-related posts on HackerNews

Show me political discussions from the newest HackerNews posts

What are the latest cryptocurrency articles on HackerNews?
```

Example output:

![Example of HackerNews flow results](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fexample-run.png&w=3840&q=100)

#### Customizing the Flow

You can enhance this flow by:

- Adding more specific filtering criteria in the LLM instructions
- Including additional variables for more complex filtering
- Modifying the output format to include more details about each article

#### Troubleshooting

If you're not getting the expected results:

1. Check that your flow variables are correctly named
2. Verify the Web Scraper URL is correct
3. Make sure your LLM instructions are clear and specific
4. Review the [debugging flows guide](https://docs.useanything.com/agent-flows/debugging-flows) for more help

> **Tip:**
>
> Remember that the quality of results depends on your LLM's capabilities. More
> powerful models like Claude 3.5 Sonnet will generally provide better filtering
> and summaries.


---

## Scheduled Jobs

### Creating Your First Job

*Walk through creating, editing, and managing a scheduled job in AnythingLLM.*

**Source:** https://docs.useanything.com/scheduled-jobs/getting-started

This page walks through creating a scheduled job from scratch. Everything is done from **Settings > Scheduled Jobs**.

> **Tip:**
>
> Prefer to just ask? You can also create a job by talking to the agent with the
> [**Create Scheduled Jobs** agent skill](https://docs.useanything.com/agent/usage/create-scheduled-job) — describe the task
> and schedule in plain language and the agent fills out this form for you.

#### 1. Open the Scheduled Jobs page

Click the **wrench icon** to open Settings, expand the **Tools** section in the sidebar, and click **Scheduled Jobs**.

![Settings sidebar with the Tools section expanded and Scheduled Jobs highlighted](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Fscheduled-jobs-settings-sidebar-location.png&w=1080&q=100)

You'll land on a list of your existing jobs (empty the first time) along with a **New Job** button.

![The Scheduled Jobs page with no jobs yet and a New Job button in the middle](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Fscheduled-jobs-empty.png&w=3840&q=100)

#### 2. Click "New Job"

Clicking **New Job** opens a form with four things to fill out:

- **Name** — what you want to call the job
- **Prompt** — the instruction sent to the agent each time it runs
- **Schedule** — when the job should run
- **Tools** — which agent tools the job is allowed to use

![The New Scheduled Job modal with name, prompt, schedule, and tools fields filled in](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Fnew-scheduled-job.png&w=3840&q=100)

New jobs are **enabled by default** as soon as they're created — there's no toggle in the modal itself. If you want to pause a job after creating it, use the enable/disable toggle on its row in the main jobs list.

#### 3. Give the job a name and prompt

##### Name

Pick something descriptive — you'll see this in the jobs list and in notifications. Examples: "Morning inbox digest", "Weekly sales report", "Competitor news check".

##### Prompt

The prompt is the message the agent receives every time the job runs. Treat it exactly like the first message you would send in an agentic chat. Be specific about:

- **What the agent should do** — the task itself
- **What format you want** — summary, bullet list, table, etc.
- **Any constraints** — date ranges, sources to use, things to ignore

> **Tip:**
>
> A scheduled job starts with a clean slate each run — there is no back-and-forth.
> Write the prompt as a complete, self-contained instruction the agent can act
> on without any follow-up questions.

**Example prompt:**

> Search my inbox for emails received in the last 24 hours that appear to require a response. For each one, list: sender, subject, a one-sentence summary, and a suggested reply. Ignore newsletters and automated notifications.

#### 4. Pick a schedule

The schedule is a standard cron expression that tells AnythingLLM when to run the job.

You have two ways to set it:

- **Cron Builder** — a visual editor with dropdowns for frequency, time, and day selection. Recommended for most people.
- **Custom cron** — type a cron expression directly if you know exactly what you want.

Either way, the form shows a live, human-readable description below your schedule (for example, *"At 09:00 AM, only on Monday"*) so you can confirm it matches your intent before saving.

For a deep dive on cron expressions and the builder, see [Scheduling & The Cron Builder](https://docs.useanything.com/scheduled-jobs/scheduling).

#### 5. Choose tools

The **Tools** picker controls which agent capabilities are available when the job runs. This includes:

- Built-in agent skills (web search, web scraping, document search, chart generation, etc.)
- Imported plugins
- Agent flows you have built
- MCP servers you have connected

Use the search box at the top to filter. Click a category header to toggle every tool inside it at once, or check individual tools.

> **Warning:**
>
> If you leave the tool list **empty**, the job will run without any tools — the
> agent will only be able to produce a response from the LLM alone. Be sure to
> select at least the tools your prompt needs (for example, web search if you're
> asking it to look things up online).

#### 6. Create the job

Click **Create**. The job is registered with the scheduler immediately and will fire on its next scheduled time. New jobs are enabled by default; if you'd rather not have it run right away, flip the enable/disable toggle off on its row in the jobs list after creating it.

#### Managing existing jobs

From the main Scheduled Jobs page, each job row shows:

- **Name**
- **Schedule** — a human-readable description of the cron (e.g. *"At 10:00 AM"*, *"Every 6 hours"*)
- **Status** — the status of the most recent run, or *"Never run"* for brand-new jobs
- **Last run** — timestamp of the most recent run (or `—` if it hasn't run yet)
- **Next run** — timestamp of the next scheduled run (or `—` if the job is disabled)

Clicking anywhere on the row opens the job's run history. The icons on the right side of the row are where you act on the job itself:

| Icon | Action | Description |
| --- | --- | --- |
| Delete icon | **Delete** | Permanently remove the job and all of its run history. |
| Edit icon | **Edit** | Open the job in the same form you used to create it, letting you change the name, prompt, schedule, or tools. |
| Run Now icon | **Run Now** | Trigger an immediate run, bypassing the schedule. Greyed out while a run is already queued or running for this job. |
| Enable/disable toggle | **Enable/disable** | Flip it off to pause the job without deleting it; flip it back on to resume scheduling. |

![The Scheduled Jobs page with one job listed and action icons on the right side of the row](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Fscheduled-jobs-populated.png&w=3840&q=100)
> **Tip:**
>
> **Run Now** still respects the one-run-at-a-time rule. If a run is already in
> progress for that job, a second one won't start until the first finishes.

#### What happens next

Once the job is enabled, AnythingLLM runs it on schedule in the background. Every run is saved — see [Viewing Runs & Results](https://docs.useanything.com/scheduled-jobs/viewing-runs) to learn how to review them, download generated files, and continue a run as a workspace thread.

### Scheduled Jobs

*Automate recurring agent tasks in AnythingLLM with Scheduled Jobs.*

**Source:** https://docs.useanything.com/scheduled-jobs/overview

> **Warning:**
>
> Scheduled Jobs is available in AnythingLLM v1.13.0 and later.
>
> **Note:** It is also **only available in single-user mode** — self-hosted instances running in
> multi-user mode will not see the Scheduled Jobs settings page.

### Scheduled Jobs

Scheduled Jobs let you run an AI agent on a recurring schedule — unattended, with access to your agent tools, and with every result saved for you to review later.

Pick a prompt, pick a schedule, pick which tools the agent is allowed to use, and let it run. Every time a job runs, AnythingLLM records what the agent thought, which tools it called, any files it produced, and its final response — a complete trace of the run that you can inspect later or carry forward into a new conversation thread.

#### What you can do with Scheduled Jobs

Scheduled Jobs are useful any time you want an agent to do the same kind of work on a regular cadence. A few examples:

- **Daily digests** — "Every morning at 8 AM, search my inbox for overnight messages and summarize anything that needs a response."
- **Weekly reports** — "Every Monday at 9 AM, pull this week's numbers and write a status report."
- **Routine data pulls** — "Every 6 hours, check this site and note anything new."
- **Scheduled reminders** — "Every Friday at 4 PM, draft a recap of what I worked on this week."
- **Long-running research** — "Once a week, run a deep-dive research task using the web search tool and save the results."

Anything you can do by talking to an agent in a chat, you can schedule — with the added benefit that results are archived and can be continued as a normal workspace thread whenever you want to follow up.

#### Key concepts

- **Job** — A saved task with a name, prompt, schedule, and list of allowed tools. A job can be enabled or disabled at any time.
- **Run** — A single execution of a job. Every run has a status (`queued`, `running`, `completed`, `failed`, or `timed out`), a start time, a duration, and — once it finishes — a full result including the agent's thoughts, tool calls, and final response.
- **Schedule** — A [cron expression](https://docs.useanything.com/scheduled-jobs/scheduling) that tells AnythingLLM when to run the job. You can build it visually or enter it directly.
- **Tools** — The subset of agent skills, plugins, flows, and MCP servers the job is allowed to use when it runs. See the [Creating Your First Job](https://docs.useanything.com/scheduled-jobs/getting-started#choosing-tools) guide for details.
- **Generated files** — Any files the agent creates while running (charts, documents, exports) are saved with the run and can be downloaded later.
- **Scheduled Jobs workspace** — A workspace that AnythingLLM creates automatically the first time a job runs. It stores job results and backs the "Continue in Thread" button.
- **Push notifications** — Optional browser notifications sent when a job finishes, so you don't have to keep the AnythingLLM tab open to know a result is ready. See [Push notifications on job completion](https://docs.useanything.com/scheduled-jobs/configuration#push-notifications-on-job-completion) for setup.

#### Where to find it

Open **Settings** and look for **Scheduled Jobs** in the sidebar. From there you can:

- See all your jobs at a glance, including their schedule and next run time
- Create, edit, enable, disable, or delete jobs
- Trigger a job immediately with **Run Now**
- Open a job's run history to see past results

#### Creating jobs conversationally

You don't have to use the settings form to create a job. If you enable the
[**Create Scheduled Jobs** agent skill](https://docs.useanything.com/agent/usage/create-scheduled-job), you can ask the agent
to set up a job for you in plain language — for example, *"@agent every weekday at 9am, summarize
my inbox and email me a digest"*. The agent builds the job (name, prompt, schedule, and tools) and
hands you a clickable card to review or edit it. Like the rest of Scheduled Jobs, this skill is
**single-user mode only**.

#### Next steps

Start with [Creating Your First Job](https://docs.useanything.com/scheduled-jobs/getting-started), then dig into [Scheduling & The Cron Builder](https://docs.useanything.com/scheduled-jobs/scheduling) for everything you can do with cron expressions. When you're ready to look at results, see [Viewing Runs & Results](https://docs.useanything.com/scheduled-jobs/viewing-runs).

### Configuration & Limits

*Environment variables, limits, and caveats for the Scheduled Jobs feature in AnythingLLM.*

**Source:** https://docs.useanything.com/scheduled-jobs/configuration

Scheduled Jobs works out of the box with sensible defaults — you don't need to configure anything to create your first job. This page covers the knobs you can turn if you want to fine-tune how jobs execute, plus the important limits and caveats to know about.

#### Environment variables

Both environment variables below are optional. If you don't set them, AnythingLLM uses the defaults listed here.

##### `SCHEDULED_JOB_MAX_CONCURRENT`

The maximum number of scheduled jobs that can run **at the same time** across the entire instance.

- **Default:** `1` (jobs run one at a time)
- **When to raise it:** if you use a cloud LLM provider with high rate limits and you have several jobs that need to run close together. Setting this to, say, `3` lets up to three jobs run in parallel.
- **When to keep it at 1:** if you use a local model, a provider with strict rate limits, or if your jobs compete for the same resources (the same MCP server, the same external API, etc.).

##### `SCHEDULED_JOB_TIMEOUT_MS`

The per-run time limit, in milliseconds. Any run that takes longer than this is forcibly stopped and marked **timed out**.

- **Default:** `300000` (5 minutes)
- **When to raise it:** if you have jobs that do legitimately long work — large research tasks, summarizing a lot of content, chaining many tool calls.
- **When to lower it:** if you want runaway jobs to fail fast and you know your jobs should never take more than a minute or two.

##### Example `.env` configuration

```
### Allow up to 3 scheduled jobs to run in parallel
SCHEDULED_JOB_MAX_CONCURRENT=3

### Give jobs up to 15 minutes before they're killed
SCHEDULED_JOB_TIMEOUT_MS=900000
```

> **Tip:**
>
> Environment variables apply at startup. If you change either value, restart
> AnythingLLM for the new value to take effect.

#### Availability & requirements

- **Single-user mode only.** Scheduled Jobs is not available on instances running in multi-user mode. The settings page and all related features are hidden in that configuration.
- **Supported on Docker and Desktop.** The feature works the same way on both.
- **The host must be running.** Jobs only fire when AnythingLLM is running. If the machine is off, asleep, or the Docker container is stopped, any scheduled times that pass during that window are missed. The next run still happens on the next scheduled time.

#### Limits to know about

##### One run at a time per job

A single job can only have one run in flight at any moment. If a scheduled time fires while the previous run is still going (or still queued), the new firing is dropped. This prevents a long-running job from stacking up and overwhelming your instance.

> **Tip:**
>
> Different jobs can run at the same time (subject to `SCHEDULED_JOB_MAX_CONCURRENT`),
> but the same job can't overlap itself.

##### Global concurrency cap

Across all jobs, the number of simultaneous runs is capped by `SCHEDULED_JOB_MAX_CONCURRENT`. When the cap is reached, additional firings are queued and picked up as soon as a worker frees up.

##### Per-run timeout

Every run is bounded by `SCHEDULED_JOB_TIMEOUT_MS`. A run that exceeds it is stopped mid-execution and marked **timed out**. Any partial thoughts, tool calls, or output captured before the timeout are still visible on the run detail page.

##### Run history depth

The run history page shows the **50 most recent runs** per job, newest first. Older runs remain in the database but aren't displayed in the UI.

##### Generated file access

Files produced during a scheduled job run are only retrievable from within the Scheduled Jobs UI, and only while the instance is in single-user mode. Switching to multi-user mode hides these files.

#### Push notifications on job completion

Scheduled Jobs can send a browser push notification every time a job finishes, so you don't have to keep the AnythingLLM tab open to find out when a run is ready. Notifications are delivered by your browser — the same mechanism websites use to alert you about new messages or updates — and work even when the AnythingLLM tab is in the background or closed (as long as your browser is still running).

##### What you'll see

Each notification includes:

- **Title** — `Scheduled Job: <job name>`
- **Body** — a short preview of the agent's final response (first 100 characters), or *"Job completed"* if the run produced no text output
- **Click action** — clicking the notification opens AnythingLLM directly on that run's detail page, so you can jump straight to the full result

##### Enabling notifications

Notifications are opt-in and controlled by your browser's standard permissions.

1. Open **Settings > Scheduled Jobs** in AnythingLLM.
2. The first time you visit the page, your browser will ask whether you want to allow notifications from AnythingLLM. Click **Allow**.
3. That's it — any future scheduled-job completion will trigger a notification.

There's nothing to configure inside AnythingLLM itself. Once the browser permission is granted, a service worker is registered automatically and the server will push notifications to it whenever jobs finish.

> **Tip:**
>
> If you dismissed the permission prompt or clicked **Block**, you won't get
> notifications. Re-enable them from your browser's site settings for your
> AnythingLLM URL (look for the lock or tune icon in the address bar and find
> the **Notifications** setting), then reload the Scheduled Jobs page.

##### Requirements & caveats

- **Browser support.** Push notifications require a browser that supports the Notifications and Push APIs — all modern desktop browsers (Chrome, Edge, Firefox, Brave, Safari 16+) do. Mobile browser support varies.
- **HTTPS (or localhost).** Browsers only allow notifications on secure origins. If you're running AnythingLLM over plain HTTP on a non-localhost address, notifications will not work. Access the app over HTTPS or through `localhost` for push notifications to register successfully.
- **Your browser must be running.** Notifications are delivered by the browser, not by AnythingLLM directly. If the browser is fully closed, the notification will typically appear the next time the browser launches (behavior depends on the browser and OS). Keep your browser running in the background to get notifications in real time.
- **Single-user mode.** Because Scheduled Jobs itself is single-user-only, notifications are sent to the single "primary" subscription for this instance.

##### Turning notifications off

To stop receiving notifications, revoke the permission from your browser's site settings:

- **Chrome / Edge / Brave:** click the tune/lock icon to the left of the address bar → **Site settings** → set **Notifications** to **Block**.
- **Firefox:** click the lock icon → **Clear permissions and cookies** or adjust **Notifications** to **Block**.
- **Safari:** **Safari > Settings > Websites > Notifications** and set the AnythingLLM site to **Deny**.

The job itself will keep running on schedule — you just won't be alerted when it finishes. You can still open the run history at any time to see results.

### Scheduling & The Cron Builder

*How to schedule scheduled jobs using the visual Cron Builder or a custom cron expression.*

**Source:** https://docs.useanything.com/scheduled-jobs/scheduling

Every scheduled job needs a schedule — a rule that tells AnythingLLM when to run it. Schedules use standard cron expressions, and you have two ways to set one.

#### The Cron Builder

The Cron Builder is the default view on the schedule field. It's a visual editor with dropdowns and controls that let you describe a schedule in plain terms and then converts it into the right cron expression for you.

You'll pick a **frequency** first, and the builder shows the relevant options for that frequency.

##### Every minute

Runs the job every N minutes. You choose the interval (1, 5, 15, 30, etc.).

![Cron Builder set to 'Run every minute' with an 'Every 1 minute' interval dropdown](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Fcron-builder-minute.png&w=3840&q=100)
> *Use case:* a very fast polling job. Most jobs don't need this frequency — it can produce a lot of runs quickly.

##### Hourly

Runs at a chosen minute-offset every hour. For example, "at minute 15 of every hour" means 12:15, 1:15, 2:15, and so on.

![Cron Builder set to 'Run hourly' with an 'At minute 00 past every hour' selector](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Fcron-builder-hourly.png&w=3840&q=100)
> *Use case:* hourly checks, periodic scrapes.

##### Daily

Runs once a day at a time you choose using a time picker.

![Cron Builder set to 'Run daily' with a time picker showing 09:00 AM](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Fcron-builder-daily.png&w=3840&q=100)
> *Use case:* a morning digest, an end-of-day recap, a nightly backup summary.

##### Weekly

Runs on one or more selected days of the week at a chosen time. Click the day pills (Mon, Tue, Wed…) to toggle which days are included.

![Cron Builder set to 'Run weekly' with 09:00 AM time picker and Mon, Tue, Wed day pills selected](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Fcron-builder-weekly.png&w=3840&q=100)
> *Use case:* Monday planning summary, Friday recap, weekday-only checks.

##### Monthly

Runs once a month on a day number you pick, at a chosen time.

![Cron Builder set to 'Run monthly' with a 09:00 AM time picker and 'On day 1 of every month' selector](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Fcron-builder-monthly.png&w=3840&q=100)
> *Use case:* monthly reports, first-of-month cleanup, end-of-month summaries.

> **Tip:**
>
> No matter which frequency you pick, the form shows a live, human-readable
> description of the schedule below the controls — for example,
> *"At 09:00 AM, only on Monday"*. Confirm this matches what you want before saving.

#### Custom cron expressions

If you know exactly what you want, switch to **Custom cron** and type an expression directly. AnythingLLM uses the standard 5-field cron format:

```
┌───────────── minute        (0–59)
│ ┌─────────── hour          (0–23)
│ │ ┌───────── day of month  (1–31)
│ │ │ ┌─────── month         (1–12)
│ │ │ │ ┌───── day of week   (0–6, Sunday = 0)
│ │ │ │ │
* * * * *
```

The input validates the expression as you type. If it's invalid, you'll see an error; if it's valid, you'll see the same plain-English description you get from the Cron Builder.

##### Common cron patterns

| Goal | Cron expression |
| --- | --- |
| Every 5 minutes | `*/5 * * * *` |
| Every hour on the hour | `0 * * * *` |
| Every 6 hours | `0 */6 * * *` |
| Every day at 9:00 AM | `0 9 * * *` |
| Every weekday at 8:00 AM | `0 8 * * 1-5` |
| Every Monday at 9:00 AM | `0 9 * * 1` |
| Every Friday at 4:00 PM | `0 16 * * 5` |
| First day of every month at midnight | `0 0 1 * *` |
| 15th of every month at noon | `0 12 15 * *` |
| Every Sunday at 11:30 PM | `30 23 * * 0` |

##### Field reference

| Field | Allowed values | Notes |
| --- | --- | --- |
| Minute | 0–59 |  |
| Hour | 0–23 | 24-hour clock |
| Day of month | 1–31 | Use `*` when you want "every day" |
| Month | 1–12 | Use `*` when you want "every month" |
| Day of week | 0–6 | Sunday = 0, Saturday = 6 |

##### Special characters

| Symbol | Meaning |
| --- | --- |
| `*` | Every value in this field |
| `,` | List of values — `1,3,5` |
| `-` | Range of values — `1-5` |
| `/` | Step values — `*/10` means every 10 |

> **Warning:**
>
> Schedules run in your server's **local time zone** — whatever time zone the
> machine running AnythingLLM is set to. "9:00 AM" means 9:00 AM on the server,
> not 9:00 AM for whoever is viewing the job.

#### When the next run is calculated

When you save or enable a job, AnythingLLM calculates the next run time from your schedule and displays it on the job row. If the server restarts, next run times are recalculated on boot — you won't miss the start of a window just because the machine was down.

> **Tip:**
>
> If the server is **off** when a scheduled time passes (for example, your
> laptop was asleep), that specific firing is missed. The next run will still
> happen at the following scheduled time.

#### Tips

- **Avoid too-frequent schedules.** Jobs that run every minute or every five minutes pile up fast and can burn through LLM credits. Start with hourly or daily.
- **Offset overlapping jobs.** If two jobs both run "every hour on the hour", they'll both try to start at the same time. Stagger them (e.g., `0 * * * *` vs `15 * * * *`) so they don't compete for resources.
- **Use the builder to prototype.** Even if you want to end up with a custom cron, the Cron Builder is the fastest way to sketch out a schedule — switch to Custom afterward if you need to fine-tune it.

### Viewing Runs & Results

*Review scheduled job runs, download generated files, and continue a run as a workspace thread.*

**Source:** https://docs.useanything.com/scheduled-jobs/viewing-runs

Every time a scheduled job runs, AnythingLLM saves a complete record of what happened. This page covers where to find those records, how to read them, and what you can do with them afterward.

#### Run statuses

Each run moves through a small set of statuses:

| Status | Meaning |
| --- | --- |
| **Queued** | The run is waiting for a worker. This is usually brief. |
| **Running** | A worker has picked up the run and the agent is actively executing it. |
| **Completed** | The run finished successfully. A full result is available. |
| **Failed** | The run stopped because of an error. The error message is shown on the run detail page. |
| **Timed out** | The run exceeded the configured per-run time limit and was stopped. See [Configuration & Limits](https://docs.useanything.com/scheduled-jobs/configuration). |

#### Run history

From the main **Scheduled Jobs** page, click **View Runs** on any job to open its run history.

Run history shows the **50 most recent runs**, newest first, with:

- **Status** — one of the statuses above
- **Start time** — when the run actually began
- **Duration** — how long it took, once finished
- **Error** — a short message if the run failed

The page polls automatically, so new runs and status changes show up without a manual refresh. You can also click **Run Now** from this page to trigger a fresh run on demand.

![Run History page showing one completed run with status, started timestamp, duration, and error columns](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Frun-history-populated.png&w=3840&q=100)

Click any row to open the run detail page.

#### Stopping a run

If a run is taking too long or doing the wrong thing, you can stop it before it finishes. Any run in **Queued** or **Running** status can be stopped — completed, failed, and timed-out runs cannot.

There are two places to do this.

**From the run history list** — click the small red stop icon next to the status badge on any in-flight row.

![A Running status badge with a small red square stop button next to it on the run history page](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Fstop-in-flight-run.png&w=640&q=100)

**From the run detail page** — click the red **Stop Job** button in the header. It only appears while the run is queued or running.

![The run detail page header for a Running run, with a red Stop Job button on the right](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Fstop-in-flight-run-run-details-page.png&w=1920&q=100)

A stopped run is recorded as **Failed** with the error *"Job killed by user"* and is automatically marked as read, so it won't show up in your unread indicator. Any thoughts, tool calls, or output captured before the stop are preserved on the run detail page.

#### Run detail page

The run detail page is where you go to see exactly what the agent did. It's organized into collapsible sections so you can scan the parts you care about and ignore the rest.

![Run detail page with Prompt and Metrics visible and Thinking, Tool Calls, Files, and Response sections collapsed](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Frun-details-sections-collapsed.png&w=3840&q=100)
> **Tip:**
>
> While a run is still in progress, the detail page updates live. Status, new
> thinking steps, and tool calls appear as they happen, so you can watch a run
> unfold in real time.

##### Prompt

The exact prompt the job was configured with at the time of this run. Handy for checking what the agent was told to do on this particular occurrence.

![Prompt section showing the job's configured instruction for this run](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Frun-details-prompt.png&w=3840&q=100)

##### Thinking

A numbered, step-by-step record of what the agent did while working through the task — each entry is a short, narrated note from the agent (e.g. *"Using DuckDuckGo to search for..."*, *"Scraping the content of..."*, *"Creating PDF document..."*). The section header shows the total step count so you can tell at a glance how much work the agent did.

![Expanded Thinking section showing 6 numbered steps the agent took during the run](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Frun-details-thinking-expanded.png&w=3840&q=100)

This section is useful for understanding *why* the agent did what it did — especially when the final response is unexpected.

##### Tool calls

Every tool the agent invoked during the run, in order. Each entry shows:

- **The tool's name** (for example, `web-browsing`, `web-scraping`, or the name of a custom skill)
- **The time it was called**
- **The arguments** the agent passed to it, displayed as JSON
- **A "Show result" toggle** that expands to reveal what the tool returned

![Expanded Tool Calls section showing three tool invocations with their arguments and Show result toggles](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Frun-details-tool-calls-expanded.png&w=3840&q=100)

Tool calls are the most detailed view of what the agent actually *did*, as opposed to what it concluded.

##### Files

Any files the agent produced during the run — exports, charts, documents, reports — appear here with their filename, size, and type, ready to download. Files stay attached to the run for as long as the run itself exists.

![Expanded Files section showing a PDF file generated by the run with a download button](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Frun-details-files-expanded.png&w=3840&q=100)
> **Warning:**
>
> Files generated by a scheduled job are only accessible from within scheduled
> jobs in single-user mode. If you switch an instance to multi-user mode, these
> files are no longer retrievable through AnythingLLM.

##### Response

The agent's final, human-readable answer — the same kind of message you'd see at the end of an agentic chat. This is rendered as markdown, so tables, code blocks, bullet lists, and links all display properly.

![Expanded Response section showing the agent's final markdown-rendered reply](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Frun-details-responses-expanded.png&w=3840&q=100)

##### Metrics

Usage information for the run, including prompt and completion token counts. Useful for keeping an eye on cost, especially for jobs that run many times a day.

![Metrics section showing prompt tokens and completion tokens for the run](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fscheduled-jobs%2Frun-details-metrics-expanded.png&w=3840&q=100)

#### Continue in Thread

Scheduled jobs are one-shot by design — there's no back-and-forth inside a run. But once a run has **completed**, you can carry the conversation forward.

Click **Continue in Thread** on the run detail page and AnythingLLM:

1. Opens the **Scheduled Jobs** workspace (creating it first if it doesn't exist yet)
2. Starts a new thread pre-filled with the job's prompt and the agent's final response
3. Drops you into that thread so you can reply, ask follow-up questions, or refine the output as a normal chat

From there, the thread behaves like any other workspace thread — same tools, same history, same agent capabilities.

> **Tip:**
>
> The **Scheduled Jobs** workspace is created automatically the first time a
> job runs or the first time you continue a run in a thread. You can treat it
> like any other workspace — rename it, change its LLM provider, adjust its
> settings — but it's generally simplest to leave it as-is and use it as your
> archive of scheduled-job output.

#### Mark as read

New runs show up with an unread indicator. Opening a run's detail page marks it as read, so your run history doubles as a lightweight inbox for "things the agent did while you weren't looking".


---

## Model Router

### What is the Model Router?

*Dynamically route your sessions to different LLM providers and models based on rules you define*

**Source:** https://docs.useanything.com/model-router/overview

AnythingLLM is the first and only platform to offer a **user-defined model router** that truly unlocks the power of AI and a hybrid AI assistant experience.

The Model Router lets you dynamically route your chat sessions to different LLM providers and models based on rules you define within a chat without having to change the model manually. Instead of locking a workspace to a single model, the same chat input can route math questions to a reasoning model, translations to a fast multilingual model, and legal questions to your most capable model.

> **Tip:**
>
> **Availability**
>
> - Available on **AnythingLLM Self-hosted** (single-user and multi-user mode)
> - Available since **AnythingLLM Desktop**: [v1.13.0](https://docs.useanything.com/changelog/v1.13.0)

#### Why use a Model Router?

A single LLM rarely fits every kind of question. Some are best answered by a fast, cheap model. Others benefit from a reasoning model. Some require your most capable (and most expensive) model. The Model Router picks the right one for each message automatically, without forcing your users to pick a model themselves.

Common reasons to use it:

- **Save money.** Send simple messages to cheap or local models and only the hard ones to expensive or remote models.
- **Use the right tool for the job.** Pair specific topics (math, code, translation, legal) with the model that handles them best.

#### How it works

A router is made up of:

- A **primary** provider and model, used when no rule matches and to evaluate LLM-classified rules. This is the model that will be used if no rules match.
- One or more **rules**, evaluated top to bottom by priority. The first rule that matches wins.

![Empty Model Router page](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmodel-router%2Frules-example.png&w=3840&q=100)

There are two types of rules:

##### Calculated rules

Calculated rules match on properties of the message itself, like keywords in the prompt, conversation token count, time of day, or whether an image is attached. These are fast and don't call an LLM.

##### LLM-classified rules

LLM-classified rules use a plain-English description (for example, "When I ask a question about legal topics, contracts, or compliance"). The router's fallback model reads the current conversation history and the new message and decides what, if any, provider and model to use.

Once a router is set up, it shows up as its own provider in the **LLM Provider** picker. Pick **Model Router**, choose your router, and every message in that workspace is routed by your rules.

Ready to set one up? → [**Setting up a Model Router**](https://docs.useanything.com/model-router/setup)

### Setting up a Model Router

*Create a router, add rules, and use it as a workspace's LLM provider*

**Source:** https://docs.useanything.com/model-router/setup

> **Tip:**
>
> The Model Router is available in AnythingLLM v1.13.0 and later.

### Setting up a Model Router

The Model Router lets you send each chat message to a different LLM provider and model based on rules you define. Instead of locking a workspace to a single model, you can route math questions to a reasoning model, translations to a fast multilingual model, and legal questions to your most capable model, all from the same chat input.

This is useful when:

- You want to save money by sending simple messages to cheap models and only the hard ones to expensive models.
- You have a model that is best at one task (math, code, translation) and want to use it only when relevant.
- You want a fallback model to handle anything that doesn't match a specific rule.

#### Creating a Router

Open the settings page and go to **AI Providers → Model Router**. The first time you visit, the page will be empty.

![Empty Model Router page](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmodel-router%2Fempty-state.png&w=3840&q=100)

Click **New Router** and fill out the form:

- **Name**: what you want to call this router.
- **Description**: optional, just a short note about what the router does.
- **Fallback Provider & Model**: used whenever no rule matches the incoming message. This same model is also used to evaluate any LLM-classified rules (more on that below), so pick something reliable.
- **Cache Cooldown (seconds)**: how long a routing decision is remembered for the conversation before rules are re-evaluated. Set to `0` to evaluate every message.

![Create a new Model Router](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmodel-router%2Fnew-router-modal.png&w=3840&q=100)

After saving, your router shows up in the list with a count of its rules and the workspaces using it.

![Model Router list](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmodel-router%2Frouter-list.png&w=3840&q=100)

#### Adding Rules

Click into your router to open the rule builder. Rules are evaluated top to bottom by priority, and the first matching rule wins. You can drag rules to reorder them.

![Empty rules page for a Model Router](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmodel-router%2Fempty-rules.png&w=3840&q=100)

There are two types of rules.

##### Calculated rules

Calculated rules match on properties of the message itself, like keywords in the prompt, total token count, message count, time of day, or whether an image is attached. These are fast and free to evaluate because they don't call an LLM.

For example, here's a rule that catches math questions and routes them to OpenAI's `o4-mini` reasoning model:

- **Title**: `route_math_to_o4_mini`
- **Rule Type**: Calculated
- **Property**: Prompt Content
- **Comparator**: contains
- **Value**: `math, mathematics, equation, calculate, solve`
- **Route to**: OpenAI / `o4-mini`

![Creating a calculated rule for math](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmodel-router%2Fcalculated-rule.png&w=3840&q=100)
> **Tip:**
>
> When the comparator is **contains**, the value is a comma-separated list and matching is case-insensitive. The rule fires if the prompt contains **any** of the values.

You can also add multiple conditions to a single rule and toggle between **AND** and **OR** logic by clicking the badge between conditions.

##### LLM-classified rules

Sometimes you can't catch a topic with keywords alone. For these cases, use an **LLM Classified** rule. You write a plain-English description of when the rule should match, and the router's fallback model reads each incoming message and decides whether it fits.

For example, a rule that catches legal questions:

- **Title**: `route_legal_to_gpt_5`
- **Rule Type**: LLM Classified
- **Match Description**: `The user is asking for help with legal documentation, contracts, terms of service, compliance, or any law-related topic`
- **Route to**: OpenAI / `gpt-5`

![Creating an LLM-classified rule for legal questions](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmodel-router%2Fllm-rule.png&w=3840&q=100)
> **Warning:**
>
> LLM-classified rules add one extra LLM call per message (the classification step) using your router's **fallback model**. Use them when keyword matching isn't enough, and prefer a fast, cheap fallback model so the classification doesn't add noticeable latency.

#### Putting it all together

With three rules in place, the router will:

1. Send anything that mentions math to `o4-mini`.
2. Send anything that mentions translation or another language to `gpt-4o`.
3. Send anything the fallback model classifies as a legal question to `gpt-5`.
4. Send everything else to the fallback model (`gpt-4o-mini`).

![All three routing rules in priority order](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmodel-router%2Frules-list.png&w=3840&q=100)

#### Using a router

Once a router exists, it shows up as its own provider in the **LLM Provider** picker where you can select it and use it in your workspace.

![Model Router shown in the LLM provider list](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmodel-router%2Fllm-provider-option.png&w=3840&q=100)

From then on, every message will be evaluated against your rules and a small badge above each response will show which model and rule handled it.

![Chat showing routing notifications above each response](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmodel-router%2Fchat-routed.png&w=3840&q=100)

#### Cooldowns and Caching

Obviously, having the router evaluate every message would be too slow and expensive and also be very annoying if you were being bounced around between models every chat! To solve this, AnythingLLM implements an advanced cooldown and caching system that we believe serves an ideal balance of performance and user experience.

The router uses a **two-layer caching strategy**:

1. **LLM classification cache** — prevents expensive LLM calls on every message. When an LLM rule evaluation occurs, the result is cached for the duration of the sticky window.
2. **Sticky route** — when a rule matches, that model "sticks" so follow-up messages that don't match any rule stay on the same model instead of bouncing back to the fallback.

##### Evaluation flow

This is the logic that happens behind the scenes on every message:

1. **Evaluate calculated rules** — these are always re-evaluated since they are instant (regex, keyword matching, token counts, etc). If a calculated rule matches, route to that model immediately.
2. **Evaluate LLM rules (with cache)** — if no calculated rule matched, check the LLM classification cache. If there's a cached result, use it. If not, call the LLM to classify the message against all LLM rules and cache the result.
3. **Check sticky route** — if no rule matched at all, check if a previous rule match is still within the sticky window. If so, keep using that model.
4. **Fall back to default** — if the sticky route has expired and no rules matched, use the fallback (primary) model.

##### TTL and timing

All caching is purely time-based — no additional model or service is used for cache invalidation.

- **Sticky window**: Defaults to **5 minutes**. This is the cooldown period configured in your router settings. When a rule matches, the routed model stays active for this duration. The timer **resets on every message** that uses the sticky route, so continuous conversation keeps the same model active.
- **LLM "match" cache**: When the LLM classifies a message and finds a matching rule, that result is cached for the full sticky window (5 minutes by default).
- **LLM "no match" cooldown**: When the LLM classifies a message but finds **no** matching rule, the "no match" result is only cached for **30 seconds**. This short cooldown avoids spamming the LLM with repeated calls on rapid messages, while still re-evaluating quickly when the conversation topic changes.

##### Why this matters

This design means:

- You won't be bounced between models on every message — once a model is selected, it stays for the sticky window.
- Calculated rules (keywords, regex, token thresholds) are always checked first and are free to evaluate.
- LLM classification only happens when the cache expires, keeping overhead low.
- If you change topics after the short 30s "no match" cooldown, the router will re-evaluate and potentially route to a different model.

Since LLM-evaluated rules are more complex and expensive to evaluate, we are very careful about how often we call the LLM so that your responses remain fast and responsive, but you are still able to use this "semantic" routing to save money and get the best model for the job without complex rulesets.


---

## MCP Compatibility

### MCP Compatibility in AnythingLLM

*Use existing MCP Servers with AnythingLLM Agents*

**Source:** https://docs.useanything.com/mcp-compatibility/overview

![Model Context Protocol](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmcp-compatibility%2Fmcp.png&w=1920&q=100)

### Model Context Protocol (MCP) in AnythingLLM

AnythingLLM supports the all [Model Context Protocol (MCP) tools](https://github.com/modelcontextprotocol/modelcontextprotocol) for use with [AI Agents](https://docs.useanything.com/agent/overview).

#### What is MCP?

MCP is an open-source protocol developed by [Anthropic](https://www.anthropic.com/) to enable seamless integration between LLM applications and external data sources and tools.

There are [many tools](https://github.com/modelcontextprotocol/servers) that exist already built with MCP in mind and AnythingLLM can work with any of them.

> The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. Whether you're building an AI-powered IDE, enhancing a chat interface, or creating custom AI workflows, MCP provides a standardized way to connect LLMs with the context they need.

#### How to use MCP in AnythingLLM

[![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmcp-compatibility%2Fdocker-header.png&w=3840&q=100)AnythingLLM Docker→](https://docs.useanything.com/mcp-compatibility/docker)[![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmcp-compatibility%2Fdesktop-header.png&w=3840&q=100)AnythingLLM Desktop→](https://docs.useanything.com/mcp-compatibility/desktop)

MCP Servers can be added to AnythingLLM by editing the `anythingllm_mcp_servers.json` configuration file in your AnythingLLM storage `plugins` directory.

The structure of the file is the same as the [MCP Server Specification](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#using-an-mcp-client).

AnythingLLM will automatically detect the MCP Servers and attempt to boot them up as needed - you can also manage your servers directly in the AnythingLLM UI.

##### AnythingLLM MCP Configuration UI

![Model Context Protocol](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmcp-compatibility%2Fuser-interface.png&w=1920&q=100)

The MCP Management UI will show you all the MCP Servers that are available to use in AnythingLLM. You can also:

- Reload/Restart all MCP Servers from the configuration file (if changes are made)
- View the status of the MCP Servers found
- View error logs from the MCP Servers
- Stop or start the MCP Servers on the fly
- View all available tools from the MCP Servers loaded successfully
- Delete the MCP Servers (will remove the server from the configuration file)

##### Example configuration file

*this file will be automatically generated in the proper directory if it doesn't exist before it is needed. It will be empty by default.*

```
// anythingllm_mcp_servers.json
{
  "mcpServers": {
    "face-generator": {
      "command": "npx",
      "args": [
        "@dasheck0/face-generator"
      ],
      "env": { // optional, some MCP servers may require additional environment variables
        "MY_ENV_VAR": "my-env-var-value"
      }
    },
    "mcp-youtube": {
      "command": "uvx",
      "args": [
        "mcp-youtube"
      ],
    },
    "postgres-http": {
      "type": "streamable", // or "sse"
      "url": "http://localhost:3003",
      "headers": {
        "X-API-KEY": "api-key"
      }
    }
  }
}
```

#### Supported Transport Types

###### StdIO

The `stdio` transport type is the default and simplest transport type. It is a simple text-based protocol that is easy to implement and use.
All MCP servers that use the stdio transport type require the `command` field to be set.

###### SSE & Streamable

> **Note:**
>
> The transport type is dependent on the MCP server implementation you are adding. So you should check the documentation for the MCP server you are adding to see what transport types is supported.
>
> Keep in mind, that both `sse` and `streamable` **require** the `url` field to be set. It will not work with the `command` field set.

The `SSE` and `Streamable` transport types are alternative transport type that is supported by many MCP servers for streaming responses.
In your configuration file, you can use the `type` field to specify the transport (`sse` or `streamable`). If not provided, `sse` is assumed.

The optional headers field can be used to send custom HTTP headers with requests to the MCP server.

#### Autostart prevention

*This property is **specific to AnythingLLM only** and will have no effect on other tools.*

Sometimes, you may want to optionally start an MCP server manually to prevent it from starting automatically and consuming resources.

To do this, AnythingLLM respects the `anythingllm.autoStart` property in the MCP Server configuration file.

For example, if you want to prevent the `face-generator` MCP Server from starting automatically, you can set the `autoStart` property to `false` in the configuration file.

Any tool that does not have `autoStart: false` explicitly set will be started automatically when the rest of the MCP servers are started. This is useful if you want to manually start an MCP server when you need it because of resource constraints.

```
{
  "mcpServers": {
    "face-generator": {
      "command": "npx",
      "args": [
        "@dasheck0/face-generator"
      ],
      "anythingllm": {
        "autoStart": false
      }
    },
    "mcp-youtube": {
      "command": "mcp-youtube",
      "args": []
    }
  }
}
```

### MCP on AnythingLLM Desktop

*How to use and debug MCP tools on AnythingLLM Desktop*

**Source:** https://docs.useanything.com/mcp-compatibility/desktop

> **Tip:**
>
> The use of MCP for AnythingLLM Desktop is available in the [v1.8.0 release](https://docs.useanything.com/changelog/v1.8.0) - please [update to at least this version](https://docs.useanything.com/changelog/v1.8.0#pinned-download-links) to use this feature.

#### Things to know about MCP on AnythingLLM Desktop

> **Note:**
>
> As always, **never run MCPs you do not trust** - we **do not** endorse or guarantee the security of any MCPs you may find on the internet.

##### MCP Server support

AnythingLLM Desktop supports `Tools` loading via MCP Servers. We **do not** support Resources, Prompts, or Sampling.

##### Startup sequence

> **Tip:**
>
> The more MCP servers you have defined, the longer it will take for them to start up.

AnythingLLM *does not* automatically start MCP servers when the application starts to prevent any overloading of resources on boot or unexpected resource consumption.

AnythingLLM *will* automatically start MCP servers when you open the "Agent Skills" page in the AnythingLLM UI **or** invoke the `@agent` directive.
All MCP servers will be started in the background - subsequent "boots" will then be much faster since the MCP servers will already be running.

If you mark a tool as `anythingllm.autoStart: false` in your configuration file, it will not be started automatically - you will need to start it manually from the UI.

##### Command availability

> **Warning:**
>
> It is not within the scope of AnythingLLM Desktop to debug when a command is not working or available. This is not a bug and you should instead check the [MCP Server documentation](https://modelcontextprotocol.io/introduction) or [community support channels](https://github.com/orgs/modelcontextprotocol/discussions).

In order for the `command` of **any MCP Server** to work, you **must** have the respective command installed on your host machine.

AnythingLLM **does not** automatically install the commands for you - you **must** install them manually and also ensure the command is available in your `PATH` or the command is a path directly to the binary being used.
eg: `npx`, `uv`, `uvx`, `node`, `bash`, etc.

##### Where is the MCP Server configuration file?

> **Tip:**
>
> The configuration file is automatically created if you open the "Agent Skills" page in the AnythingLLM UI and it does not exist.

The MCP Server configuration file is located in the `plugins/anythingllm_mcp_servers.json` file in the [AnythingLLM storage directory](https://docs.useanything.com/installation-desktop/storage).

##### Reloading MCP Servers

You can reload MCP Servers *on the fly* by clicking the "Refresh" button in the "Agent Skills" page. This will reload the MCP Servers from the configuration file and restart them.
This does not require you to restart the AnythingLLM Desktop application - the currently running MCPs will be killed and rebooted with whatever changes you made to the configuration file.

You can also click "Refresh" to reload the MCP Servers if you are debugging a specific MCP Server.

##### Starting and stopping MCP Servers

You can start and stop MCP Servers *on the fly* by clicking the "Start" or "Stop" action via the gear icon in the "Agent Skills" page while selecting the MCP Server you want to start or stop.

This does not require you to restart the AnythingLLM Desktop application - the target MCP Server will be started or stopped immediately.

If you wish to stop an MCP Server from automatically starting - see the [Autostart prevention](https://docs.useanything.com/mcp-compatibility/desktop#autostart-prevention) section.

##### How do I add/remove an MCP Server?

###### Adding an MCP Server

Adding an MCP Server is as simple as adding a new tool to the `mcpServers` object in the `anythingllm_mcp_servers.json` file in your [AnythingLLM storage directory](https://docs.useanything.com/installation-desktop/storage).

###### Removing an MCP Server

You can remove an MCP Server by clicking on an MCP Server in the "Agent Skills" page, select the gear icon, and clicking "Delete".
Deleting the MCP Server from the UI **will remove** the MCP Server from the file and kill the process running that MCP Server.

You can also manually remove an MCP Server by removing the object from the `mcpServers` object in the `anythingllm_mcp_servers.json` file and clicking "Refresh" in the "Agent Skills" page on the UI afterwards.

##### Viewing the status of an MCP Server

On the "Agent Skills" page, you can view the status of an MCP Server by clicking on the MCP Server in the list - if there is an error, it will be displayed in the card.

Additionally, you can quickly see the status of all MCP Servers by clicking the "Agent Skills" page and looking at the MCP Servers list.

##### Debugging MCP Servers

If you are having issues with an MCP Server, you can best debug these by looking at the [Desktop application logs](https://docs.useanything.com/installation-desktop/debug#general-debugging).

##### Issues installing a tool

> **Tip:**
>
> **Please do not open issues about tool issues on GitHub - we are not the MCP authors or maintainers.**
>
> If you are having issues, you should post on the [MCP Discussion board](https://github.com/orgs/modelcontextprotocol/discussions) - or ask in the AnythingLLM Discord server.

Sometimes, an MCP Server will require a tool to be installed via `uv tool install xyz`.
The easiest way to do this is to open command line and run the command manually on your machine. Then you can click "Refresh" in the "Agent Skills" and see if the tool now boots successfully.

##### Tool persistence

Since AnythingLLM Desktop is a desktop application, the tools downloaded for MCP are stored on your host machine and will persist across application restarts and even application uninstalls.

MCP tools are stored outside of AnythingLLM and you should delete them manually if you want to remove them.

##### Writing files to the host machine

Often, you may want to write or even read files from the host machine - since the MCP Server is running on your host machine you can use any path on your host machine that would normally function in a command line.

##### My LLM is not calling my MCP Server!

First, ensure that the MCP Server is running and that the tool is available in the "Agent Skills" page.

Next, your issue is probably the model you are using - this is especially true if you are using a small local model with a limited context window.

[Learn more about LLMs with Agent Skills →](https://docs.useanything.com/agent-not-using-tools)

### MCP on AnythingLLM Docker

*How to use and debug MCP tools on AnythingLLM Docker*

**Source:** https://docs.useanything.com/mcp-compatibility/docker

> **Note:**
>
> The use of MCP for AnythingLLM Docker is **self-hosting only** and is not available in the AnythingLLM Cloud service.

#### Things to know about MCP on AnythingLLM Docker

> **Note:**
>
> As always, **never run MCPs you do not trust** - we **do not** endorse or guarantee the security of any MCPs you may find on the internet.

##### MCP Server support

AnythingLLM Docker supports `Tools` loading via MCP Servers. We **do not** support Resources, Prompts, or Sampling.

##### Startup sequence

> **Tip:**
>
> The more MCP servers you have defined, the longer it will take for them to start up. Your container should have enough resources to account for this.

AnythingLLM *does not* automatically start MCP servers when the container starts to prevent any overloading of resources on boot.

AnythingLLM *will* automatically start MCP servers when you open the "Agent Skills" page in the AnythingLLM UI **or** invoke the `@agent` directive.
All MCP servers will be started in the background - subsequent "boots" will then be much faster since the MCP servers will already be running.

If you mark a tool as `anythingllm.autoStart: false` in your configuration file, it will not be started automatically - you will need to start it manually from the UI.

##### Command availability

The majority of commands that are required to run a MCP server are available in the AnythingLLM Docker container already.

The base image of AnythingLLM Docker is `ubuntu:jammy-20240627.1`, so generic Ubuntu commands will be available as the user running the services inside of the container.

Additionally - we have pre-installed the following commands:

- `npx`
- `uv` or `uvx`
- `node`
- `bash`

##### Where is the MCP Server configuration file?

The MCP Server configuration file is located in the `plugins/anythingllm_mcp_servers.json` file in the AnythingLLM storage directory.

> **Tip:**
>
> The configuration file is automatically created if you open the "Agent Skills" page in the AnythingLLM UI.

The storage directory is defined by the `STORAGE_LOCATION` environment variable when you start the AnythingLLM Docker container - [see example](https://docs.useanything.com/installation-docker/local-docker)

##### Reloading MCP Servers

You can reload MCP Servers *on the fly* by clicking the "Refresh" button in the "Agent Skills" page. This will reload the MCP Servers from the configuration file and restart them.
This does not require you to restart the AnythingLLM Docker container - the currently running MCPs will be killed and rebooted with whatever changes you made to the configuration file.

You can also click "Refresh" to reload the MCP Servers if you are debugging a specific MCP Server.

##### Starting and stopping MCP Servers

You can start and stop MCP Servers *on the fly* by clicking the "Start" or "Stop" action via the gear icon in the "Agent Skills" page while selecting the MCP Server you want to start or stop.

This does not require you to restart the AnythingLLM Docker container - the target MCP Server will be started or stopped immediately.

If you wish to stop an MCP Server from automatically starting - see the [Autostart prevention](https://docs.useanything.com/mcp-compatibility/docker#autostart-prevention) section.

##### How do I add/remove an MCP Server?

###### Adding an MCP Server

Adding an MCP Server is as simple as adding a new tool to the `mcpServers` object in the `anythingllm_mcp_servers.json` file in your AnythingLLM storage directory.

###### Removing an MCP Server

You can remove an MCP Server by clicking on an MCP Server in the "Agent Skills" page, select the gear icon, and clicking "Delete".
Deleting the MCP Server from the UI **will remove** the MCP Server from the file and kill the process running that MCP Server.

You can also manually remove an MCP Server by removing the object from the `mcpServers` object in the `anythingllm_mcp_servers.json` file and clicking "Refresh" in the "Agent Skills" page on the UI afterwards.

##### Viewing the status of an MCP Server

On the "Agent Skills" page, you can view the status of an MCP Server by clicking on the MCP Server in the list - if there is an error, it will be displayed in the card.

Additionally, you can quickly see the status of all MCP Servers by clicking the "Agent Skills" page and looking at the MCP Servers list.

##### Debugging MCP Servers

If you are having issues with an MCP Server, you can best debug these by looking at the docker container logs.

##### Issues installing a tool

> **Tip:**
>
> **Please do not open issues about tool issues on GitHub - we are not the MCP authors or maintainers.**
>
> If you are having issues, you should post on the [MCP Discussion board](https://github.com/orgs/modelcontextprotocol/discussions) - or ask in the AnythingLLM Discord server.

Sometimes, an MCP Server will require a tool to be installed via `uv tool install xyz`.
The easiest way to do this is to open a shell into the container and run the command manually. Then you can click "Refresh" in the "Agent Skills" and see if the tool now boots successfully.

##### Tool persistence

If you stop or delete the AnythingLLM Docker container the libraries cached for the MCP servers will be lost and need to be re-downloaded on first start. Typically, this takes much longer for MCP servers that have a large number of dependencies or build steps and can increase boot times when starting MCP servers.

The also applies to any tools that you may have manually installed to get an MCP server to work - your changes are within the container and will be lost when the container is deleted.

##### Writing files to the host machine

Often, you may want to write or even read files from the host machine - since the MCP Server runs within the context of the container - you **must** use this path:

```
/app/server/storage/...
```

This path will then be using the `STORAGE_LOCATION` directory that you defined when you [started the AnythingLLM Docker container](https://docs.useanything.com/installation-docker/local-docker). From here you can then write and read files to the host machine.

##### My LLM is not calling my MCP Server!

First, ensure that the MCP Server is running and that the tool is available in the "Agent Skills" page.

Next, your issue is probably the model you are using - this is especially true if you are using a small local model with a limited context window.

[Learn more about LLMs with Agent Skills →](https://docs.useanything.com/agent-not-using-tools)


---

## Browser Extension

### AnythingLLM Browser Extension

*How to install the AnythingLLM Browser Extension*

**Source:** https://docs.useanything.com/browser-extension/install

![AnythingLLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fbrowser-extension%2Fheader-image.png&w=3840&q=100)

The AnythingLLM Browser Extension is a tool that allows you to connect your AnythingLLM instance to your browser. This allows you to send and embed information from the web directly to AnythingLLM or embed directly into your workspaces for later!

With the browser extension, you can:

- Send entire webpages or just highlighted text snippets to AnythingLLM
- Embed information directly into your AnythingLLM workspaces
- Collect or embed web content that is password protected, VPN protected, or otherwise inaccessible to the public internet straight from your browser.

*All offerings of AnythingLLM support the browser extension.*

#### Installing the AnythingLLM Browser Extension

**Supported Browsers:**

- Chrome
- Edge
- Brave
- Firefox

You can find the AnythingLLM Browser Extension in the [Chrome Web Store →](https://chromewebstore.google.com/detail/anythingllm-browser-compa/pncmdlebcopjodenlllcomedphdmeogm)

After installing the browser extension, you should see a new icon in your browser toolbar.

##### Connecting the Browser Extension to AnythingLLM

Connecting to your specific AnythingLLM instance is simple.

1. Open the AnythingLLM instance you want to connect to in your browser or on Desktop.
2. Open settings and Click on the `Browse Extension` sidebar element under `Tools`.

![AnythingLLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fbrowser-extension%2Fsidebar.png&w=640&q=100)

3. You will land on a page with a `Generate API Key` button. Click on the button to generate an API key. Click `Create API Key` to create the key.

![AnythingLLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fbrowser-extension%2Fgenerate.png&w=3840&q=100)

4. If possible the browser extension will automatically connect to your AnythingLLM instance. If not, you can manually connect by copying and pasting the connection string into the browser extension.

*Automatically connected to AnythingLLM*

![AnythingLLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fbrowser-extension%2Fauto-connect.png&w=3840&q=100)

*Manually connect to AnythingLLM*

![AnythingLLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fbrowser-extension%2Fmanual.png&w=3840&q=100)

5. You are now connected to your AnythingLLM instance! You can now use the browser extension to collect and send information on any website directly into AnythingLLM or embed directly into your workspaces for later!

*Send an entire webpage to AnythingLLM*

![AnythingLLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fbrowser-extension%2Fwhole-page.png&w=3840&q=100)

*Send a snippet of text you highlight on page*

![AnythingLLM](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fbrowser-extension%2Fsnippet.png&w=3840&q=100)

### Customizing the Browser Extension

***Docker only:***
By default, the image in the browser extension is the AnythingLLM logo. However, it will automatically use the logo of the instance you are connected to if set in the `Customization` section of the settings page.

If you want to further customize the browser extension, you can do so by forking the [AnythingLLM Browser Extension GitHub Repository](https://github.com/Mintplex-Labs/anythingllm-extension) and making your own changes.

Once you have made your changes, you can build the extension using the `yarn build` command.

After building the extension, you can load it into your browser by clicking the `Load unpacked.` button in Chrome and selecting the `dist` folder.


---

## Messaging Channels

### Telegram Bot

*Connect your AnythingLLM instance to Telegram and chat with your workspaces from any device.*

**Source:** https://docs.useanything.com/channels/telegram

> **Tip:**
>
> The Telegram Bot connector is available on **Docker** and **Desktop** (Mac,
> Windows, Linux) in AnythingLLM **>v1.11.2**.

### Telegram Bot

Connect your AnythingLLM instance to Telegram so you can chat with your workspaces from any device. Send text, images, and voice messages directly through Telegram and get responses powered by your configured LLM, complete with document context and agent capabilities.

![Telegram chat with AnythingLLM bot](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fchannels%2Ftelegram%2Ftelegram-chat-demo.png&w=3840&q=100)

#### Setup

> **Warning:**
>
> The Telegram Bot connector **only works in single-user mode** (or single-user
> with password protection) on Docker. Enabling multi-user mode will
> automatically disconnect the bot.

##### Step 1: Create your Telegram bot

1. Open [BotFather](https://t.me/BotFather) in Telegram (or scan the QR code shown in the setup screen)
2. Send `/newbot` to **@BotFather**
3. Choose a name and username for your bot
4. Copy the API token you receive

![AnythingLLM Telegram setup - BotFather instructions](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fchannels%2Ftelegram%2Fsetup-step1.png&w=3840&q=100)

##### Step 2: Connect your bot

1. Navigate to **Settings > Channels > Telegram** in AnythingLLM
2. Paste the API token from BotFather
3. Click **Connect Bot**

![AnythingLLM Telegram setup - connect bot token](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fchannels%2Ftelegram%2Fsetup-step2.png&w=3840&q=100)

##### Step 3: Verify users

When someone messages your bot for the first time, they'll receive a pairing code. You'll see their request in the **Users** section of the Telegram settings page. Match the pairing code displayed in their Telegram chat with the one shown in AnythingLLM and click **the check mark** to grant access.

![AnythingLLM Telegram user verification with pairing code](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fchannels%2Ftelegram%2Fuser-verification.png&w=3840&q=100)

##### Recommended security settings

For additional security, configure these settings in **@BotFather**:

- **Disable group joins** — Prevents the bot from being added to group chats
- **Disable inline mode** — Prevents the bot from being used in inline search
- **Use a non-obvious username** — Reduces discoverability of your bot

#### Capabilities

##### Text chat

Send any message to your bot and it will respond using the connected workspace's LLM provider and model, including any embedded document context.

##### Image understanding

Send photos to your bot and it will analyze them using your configured vision-capable LLM. Great for asking questions about screenshots, diagrams, or any visual content.

![Telegram bot analyzing an image](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fchannels%2Ftelegram%2Fimage-understanding.png&w=3840&q=100)

##### Voice messages

Send voice messages to your bot and it will transcribe and respond to them.

##### Automatic mode and @agent support

The Telegram bot supports **Automatic mode** for native tool calling when your model and provider support it. You can also use `@agent` to invoke agent skills directly from Telegram, including the chart renderer which generates and sends PNG charts directly in chat.

![Telegram bot generating a chart with @agent](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fchannels%2Ftelegram%2Fagent-chart.png&w=3840&q=100)

##### Workspace and thread management

Switch between workspaces and threads, start new conversations, and manage your chat context all from within Telegram using slash commands.

##### Citations

Use the `/proof` command after a response to see the document sources that were used to generate the answer.

#### Telegram commands

| Command | Description |
| --- | --- |
| `/start` | Welcome message with current workspace info |
| `/switch` | Switch workspace or thread |
| `/new` | Start a new thread in the current workspace |
| `/history [count]` | Show recent messages (default 10, max 50) |
| `/status` | Show current workspace, thread, provider, and model |
| `/reset` | Clear chat history context (messages stay visible but are not used as context) |
| `/proof` | Show citations from the previous response |
| `/model` | Select a different model mid-chat |
| `/help` | Show available commands |

#### Managing your connection

Once connected, the Telegram settings page shows your bot's status, a direct link to your bot, and the list of approved users. From here you can:

- **Reconnect** if the bot token expires or becomes invalid
- **Disconnect** the bot entirely
- **Approve or deny** pending user requests
- **Remove** access for previously approved users

![AnythingLLM Telegram connected view with user management](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fchannels%2Ftelegram%2Fconnected-view.png&w=3840&q=100)

#### Limitations

- **Requires your instance to be running** — If you shut down your computer, put it to sleep, or your Docker container stops, the bot will not respond until the instance is back online.
- **Single-user mode only** — The bot is automatically disconnected when multi-user mode is enabled. It works in single-user and single-user with password protection modes.
- **One bot per instance** — Each AnythingLLM instance supports a single Telegram bot connection.


---

## Desktop Assistant

### AnythingLLM's Desktop Assistant

*AnythingLLM's Desktop Assistant is an on-screen overlay that exists across your entire OS. Instantly available to you for any application for chats, agents, and more.*

**Source:** https://docs.useanything.com/desktop-assistant/introduction

> **Tip:**
>
> **Note:** The Desktop Assistant is a **free** and **desktop exclusive** feature and is available in AnythingLLM Desktop v1.11.0 and later.
>
> The Desktop Assistant is an on-screen overlay that exists across your entire OS. It is the preferred way to interact with AnythingLLM.

### AnythingLLM's Desktop Assistant

The AnythingLLM Desktop Assistant is an on-screen overlay that exists across your entire OS. In a single keystroke, you can open the Desktop Assistant and start chatting, creating agents, and more with full context from any open applications.

[Video](https://webassets.anythingllm.com/anythingllm-assistant-desktop-promo.mp4)

#### The Desktop Assistant does this and more...

- Instantly open with `CMD+/` (MacOS) or `CTRL+/` (Windows/Linux) anywhere on your screen
- Chat with any open application using the full context of any application (Chrome, Slack, VS Code, etc.)
- Leverage any installed agent skills or MCPs to perform tasks and answer questions
- Uses your LLM provider and model of choice (Cloud or Local) to perform tasks and answer questions

> The Desktop Assistant is the preferred way to interact with AnythingLLM. It is faster, more efficient, and more powerful than the traditional AnythingLLM UI.

#### Privacy

Any chats, agentic tasks, or MCPs are processed using your LLM provider and model of choice (Cloud or Local). If you are using non-local models then your interactions are under the terms of your LLM provider's privacy policy.

##### Supported Platforms

- MacOS Silicon (M-Series)
- MacOS Intel
- Windows x64
- Windows ARM64
- Linux x64 (limited)
- Linux ARM64 (limited)

> **Note:**
>
> **Linux limitations:** The Desktop Assistant on Linux cannot capture individual applications, displays, or screen regions. Features that depend on screen capture - including [chat with any open application](https://docs.useanything.com/desktop-assistant/features#chat-with-any-open-application) and [full screen & area capture](https://docs.useanything.com/desktop-assistant/features#full-screen--area-capture) - are unavailable on Linux.

#### Frequently Asked Questions

##### What is the default shortcut to open the Desktop Assistant?

The default shortcut to open the Desktop Assistant is `CMD+/` (MacOS) or `CTRL+/` (Windows/Linux).

##### What if I want to change the shortcut?

You can change the shortcut by going to the main AnythingLLM menu and clicking on "Settings" > "Desktop Assistant". Here you can change the shortcut to your liking.

##### What if I want to use a cloud model?

If you are using a cloud model, we will blindly send the text + image content to the provider. If you cloud provider model does not support images - you will likely get an error back from the model.
Most models are multi-modal and support images, but some do not. It is up to you to choose a model that supports images when using the Desktop Assistant.

##### What if my model is not a Vision-enabled model?

> **Tip:**
>
> If you are using the **default LLM provider**, **Ollama**, or **LM Studio**, we will automatically handle the image processing for you on device, even if your model does not support images.

If your model is not a Vision-enabled model, we will instead OCR the text from the screen and use that to answer your questions. This is not as efficient and will impact the accuracy of your answers.

##### What models are supported?

Any model is supported, but we highly recommend using a local multi-modal model that can process images. Something like Gemma3 4B+ or Qwen3-VL 4B are great choices. This selection and performance will vary depending on your hardware.

**Recommended Models:**

- Qwen3-VL 2B Instruct (Q8)
- Qwen3-VL 4B Instruct (Q4)
- Qwen3-VL 8B Instruct (Q4)
- Gemma3 4B+ (Q4)

### Features

*Features of AnythingLLM's Desktop Assistant*

**Source:** https://docs.useanything.com/desktop-assistant/features

> **Tip:**
>
> The Desktop Assistant is only available in AnythingLLM Desktop v1.11.0 and later for [supported platforms](https://docs.useanything.com/desktop-assistant/introduction#supported-platforms).

In general, anything you can do in the main AnythingLLM UI you can do in the Desktop Assistant - chat with documents, agents, MCPs, and more.

#### Chat with any open application

> **Note:**
>
> **Not supported on Linux:** Application capture is unavailable on Linux. The Desktop Assistant on Linux cannot capture individual applications for screenshots.

By default, the Desktop Assistant is able to chat with any open application using the full context of any application (Chrome, Slack, VS Code, etc.).

You can select the current active application suggestion in the chat window or click the "+" icon show all available applications.

> This takes a screenshot of the current active application and uses that to answer your questions. It does not access the application's raw data or files - it can only see what is on the screen.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fdesktop-assistant%2Fchat-with-application.png&w=640&q=100)

#### Full screen & area capture

> **Note:**
>
> **Not supported on Linux:** Full display and area capture are unavailable on Linux. The Desktop Assistant on Linux cannot capture displays or screen regions for screenshots.

In the "+" menu, you can select "Area Capture" to capture a specific area of the screen or select a display to capture the full screen of that display.

![](https://docs.useanything.com/_next/image?url=https%3A%2F%2Fwebassets.anythingllm.com%2Fdesktop-area-capture.gif&w=1920&q=100)

#### Settings & Keyboard Shortcuts

> By default, the Desktop Assistant is bound to the `CMD+/` (MacOS) or `CTRL+/` (Windows/Linux) keyboard shortcut. You can change this in the settings.

You can customize the Desktop Assistant by clicking the "Desktop Assistant Settings" in the 3-dot menu in the top right corner of the Desktop Assistant.

You can also customize the Desktop Assistant by clicking the "Settings" > "Desktop Assistant" in the main AnythingLLM menu.

##### Open thread behavior

The "Open thread behavior" setting determines what happens when the Desktop Assistant is opened.

- Open a new thread (default)
- Open the previous thread

> All threads created in the Desktop Assistant are saved to the "Assistant Chat" workspace in AnythingLLM so you can interact with them in the main AnythingLLM UI.

#### Chat functionality

All chat functionality in the Desktop Assistant is the same as in the main AnythingLLM UI. You can use the same tools and features to chat with the Desktop Assistant.

- Drag and drop documents into the chat window
- Attach images to the chat
- Use agent skills and MCPs to perform tasks and answer questions (using `@agent`)
- Use custom Slash Commands
- Set the system prompt for the Desktop Assistant and even embed documents like you would in the main AnythingLLM UI


---

## Meeting Assistant

### Introduction

*Introduction to AnythingLLM's Meeting Assistant*

**Source:** https://docs.useanything.com/meeting-assistant/introduction

> **Tip:**
>
> **Note:** The Meeting Assistant is a **free** and **desktop exclusive** feature and is available in AnythingLLM Desktop v1.10.0 and later.
>
> The Meeting Assistant is a tool that helps you record, transcribe, and summarize meetings complete with agentic follow-up actions.

> **Note:**
>
> **Coming soon to Linux:** The Meeting Assistant is not yet available on Linux (both x64 and ARM64). This feature is currently only available on MacOS and Windows.

### Meeting Assistant

The AnythingLLM Meeting Assistant is a tool that brings all the power of paid SaaS meeting assistants to your local device, all using local models with absolutely no data leaving your device.

[Video](https://webassets.anythingllm.com/preview.mp4)

#### The Meeting Assistant does this and more...

- Record and transcribe meetings
- Upload meetings or recordings that you have already have.
  - This includes podcasts, YouTube videos, or any other audio or video file.
- Identify speakers in the transcript
- Joined meeting notifications to start recording the meeting in the background
- Summarize meetings using your LLM provider and model of choice (Cloud or Local)
  - You can fully customize the summary prompt to your liking or use case and apply it to any meeting.
- Propose agentic follow-up actions based on the meeting summary and transcript to run in a click.
  - Every agent skill or MCP is now instantly available to the Meeting Assistant.
- Indexes and makes every meeting searchable
  - You can search for meetings by topic, speaker, date, or even semantically.
- Chat with your transcript to ask specific questions about the meeting.

**all of this done locally on your device - 100% free with no limits.**

#### Watch the product overview

[Embedded video/content](https://www.youtube.com/embed/TrM1FzKrz5I?si=sqbGPJoOtPUpsft_)

#### Performance & Privacy

##### Privacy

All processing is done locally on your device - 100% free with no limits. We download a [transcription model](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) to support this feature
as needed on the first time a file is uploaded or a recording is made. These models are stored locally on your device for re-use.

Your meetings, recordings, and other files are never uploaded to **any** servers. They are all processed locally on your device and never leave your device.

*If you are using a cloud model, only the transcript is sent to produce your summary and follow-up actions. If you are using a local model everything is processed locally on your device.*

##### Performance

The Meeting Assistant is designed to be fast and efficient as possible on all ranges of hardware. That being said, your experience and speeds may vary depending on your hardware and the length of the meeting.

We currently have dedicated hardware to support that is highly performant on:

- Apple Silicon M-Series CPUs
- NVIDIA RTX GPUs

All other hardware is supported, but may not be as performant, but will still work and run exclusively on CPU.

##### Supported Platforms

- MacOS Silicon (M-Series)
- MacOS Intel
- Windows x64
- Windows ARM64
- Linux x64 (Coming Soon)
- Linux ARM64 (Coming Soon)

##### Minimum System Requirements

We recommend a minimum of 16GB of RAM to run the Meeting Assistant. All CPU architectures are supported.

### Features

*Features of AnythingLLM's Meeting Assistant*

**Source:** https://docs.useanything.com/meeting-assistant/features

> **Tip:**
>
> The Meeting Assistant is only available in AnythingLLM Desktop v1.10.0 and later for [supported platforms](https://docs.useanything.com/meeting-assistant/introduction#supported-platforms).

> **Note:**
>
> **Coming soon to Linux:** The Meeting Assistant is not yet available on Linux (both x64 and ARM64). None of the features described on this page are available on Linux today.

#### Record and transcribe meetings

> **Tip:**
>
> The Meeting Assistant is not limited to just recording and transcribing meetings. You can also upload meetings, audio files, or recordings that you have already have.
>
> You can also just start a recording in AnythingLLM and speak to your computer if you want!

By default, the Meeting Assistant is able to record and transcribe meetings you join on any software like Zoom, Google Meet, Microsoft Teams, etc. You can also upload meetings, audio files, or recordings that you have already have.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmeeting-assistant%2Fsummary.png&w=3840&q=100)

#### Speaker identification

The Meeting Assistant is able to identify unique speakers in the transcript. It **does not** rename the speakers in the transcript based on your meeting, it simply identifies them by their unique voice characteristics.
This process is done using a combination of LLM-based speaker identification and speaker diarization. That being said, it is not perfect and may not always be able to identify speakers correctly.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmeeting-assistant%2Ftranscript.png&w=3840&q=100)

##### Types of speaker identification

There are three types of speaker identification available - each with their own unique benefits and trade-offs.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmeeting-assistant%2Fspeaker-identification.png&w=640&q=100)

###### No Diarization

If you dont care about speaker identification, you can disable it entirely but you will not be able to see speaker names in the transcript.
This can lead to worse summaries since the models will be unable to identify even you from other speakers.

###### Basic Diarization

This is the default mode and is the most basic form of speaker identification. It is able to identity **what you are saying** from other speakers. However, the "Other" speaker will be used for any audio that is not you.
This takes a minimal amount of additional processing power or time to run and is the fastest way to get speaker identification and yeilds great results for most meetings since you will at least be able to identify yourself from other speakers and the summary
will reflect that.

###### Full Diarization

This is the most advanced form of speaker identification and is able to identify speakers based on their unique voice characteristics. It is also able to identify speakers based on their unique voice characteristics.
This takes more processing power and time to run and is not recommended for most meetings. However, it is the most accurate way to get speaker identification and will yield the best results for most meetings.

This can lead to a 20-40% increase in processing time depending on your hardware and the length of the meeting. GPU hardware is recommended for this mode for optimal performance.

##### Edit speaker names

For any transcript with speaker identification enabled, you can click on a speaker to rename them across the entire transcript as well as correct any mis-identifications.

After editing, any speakers who are no longer mentioned will be removed from the speaker list.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmeeting-assistant%2Fedit-speaker.png&w=3840&q=100)

##### Edit transcript text

For any transcript, you can double-click on a piece of text to edit it. This will allow you to correct any mis-transcriptions or add any additional context that was not captured by the transcription.

After editing, the transcript will be updated. However, you may want to re-summarize the meeting to apply the changes to the meeting summary.

##### Play from a specific time

For any transcript, you can replay the audio from the top recording player as well as click to jump to a specific time in the transcript. If you have speaker identification enabled, you can also click on a speaker segment to jump to that exact time in the audio.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmeeting-assistant%2Fplay-segment.png&w=3840&q=100)

#### Real-time transcription

> **Warning:**
>
> This feature is only available when recording a meeting and is **disabled** by default. It is purely for convenience and to help you follow along with the meeting if you wish
> and we only recommend enabling it if you are on high-end hardware.

The Meeting Assistant is able show a rolling transcript of the meeting as it is happening. This can be helpful to follow along with the meeting if you wish and is purely for convenience.

#### Joined meeting Notification

The Meeting Assistant is able to send you a desktop notification when you join a meeting. Clicking the notification will open the Meeting Assistant and start recording the meeting in the background.

When you stop or leave a meeting, the Meeting Assistant will automatically stop recording and save the meeting to your local device. You will be notified about the summary processing as it completes.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmeeting-assistant%2Fnotifications.png&w=3840&q=100)

#### Meeting summary

The Meeting Assistant is able to summarize your meetings using your LLM provider and model of choice (Cloud or Local). By default, this is using whatever model you have configured as the "system" model in the AnythingLLM Settings > AI Providers > LLM.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmeeting-assistant%2Fsummary.png&w=3840&q=100)

##### Meeting summary templates

By default, the Meeting Assistant will use a generic summary template that is designed to be a good starting point for most meetings. AnythingLLM provides 3 pre-built summary templates for you to choose from:

- **General Meeting**: This is a basic summary template that is designed to be a good starting point for most meetings.
- **Sales Call**: This is a summary template that is designed to be a good starting point for sales calls.
- **Engineering Meeting**: This is a summary template that is designed to be a good starting point for engineering meetings.

You can change the summary template you want to use by clicking on the 3-dot menu icon next to the meeting recording and selecting the summary template you want to use.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmeeting-assistant%2Fcustom-template.png&w=3840&q=100)

##### Custom summary templates

On any meeting recording, you can also click on the 3-dot menu icon next to the meeting recording and create a custom summary template for that specific meeting or re-use an existing summary template.

If you change the summary template for a meeting you can instantly apply it to the meeting summary by clicking the "Apply Summary Template" action at the top of the meeting summary. This will apply the summary template to the meeting summary that will be sent to your LLM for processing.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmeeting-assistant%2Fapply-template.png&w=3840&q=100)

##### Regenerate meeting summary

By clicking the 3-dot menu next to the recording player, you can click `Regenerate Summary` to regenerate the meeting summary. This will regenerate the meeting summary available.

You may want to do this if you apply major changes to your summary template or transcript.

#### Agentic follow-up actions

The Meeting Assistant is able to propose agentic follow-up actions based on the meeting summary and transcript. **No action is taken until you click the "Run" button.**

Every "Agent Skill", including MCPs, Agent Flows, and anything else you can use in AnythingLLM, is instantly available to the Meeting Assistant as a possible follow-up action.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmeeting-assistant%2Fagent-items.png&w=3840&q=100)

##### View action item details

For any action item, you can click on the `View Arguments` hint text to get a breakdown of the arguments that will be passed to the action item and how they will be used in the tool of choice.

##### Regenerate action items

By clicking the 3-dot menu next to the recording player, you can click `Regenerate Action Items` to regenerate the action items. This will regenerate the action items available.

You may want to do this if you apply major changes to your summary template or transcript.

##### Meeting title

On summary, we will automatically generate a title for the meeting based on the meeting summary. You can also manually edit the title by clicking on the title and typing in the new title.

#### Ask Questions

Clicking on the `Ask Questions` tab at the top of the meeting UI will open new workspace with the meeting transcript embedded in the workspace where you can ask questions about the meeting.

This is a great way to get quick answers to questions about the meeting without having to re-summarize the meeting.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmeeting-assistant%2Fask-questions.png&w=3840&q=100)

#### Meeting Search

> **Tip:**
>
> Meeting search is run using a local on-device vector database and embedding model. No data is sent to the cloud.

On the right sidebar of the meeting UI, you will find every meeting you have recorded or uploaded in the Meeting Assistant.

You can use the search bar to find a specific meeting by name, date, or even semantically. Every transcript and summary for every meeting is indexed and searchable.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmeeting-assistant%2Fsearch.png&w=3840&q=100)

#### Preferences

The Meeting Assistant has a set of preferences that you can configure to your liking. You can access them by click on the "Sliders" icon in the top right corner of the meeting UI.

Any changes you make to the preferences will be saved and applied to the Meeting Assistant and will be applied to all future meetings recorded or uploaded.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmeeting-assistant%2Fpreferences.png&w=3840&q=100)


---

## Mobile App

### Introduction

*AnythingLLM Mobile Introduction*

**Source:** https://docs.useanything.com/mobile/overview

> **Tip:**
>
> You can download the app from the [Google Play Store](https://play.google.com/store/apps/details?id=com.anythingllm) or [Direct APK Download](https://anythingllm.com/mobile).

### Introduction

AnythingLLM Mobile is a mobile app that brings the entire AnythingLLM experience onto your phone.

It is currently **only available for Android** for now. The app is available in the Google Play Store and can be downloaded directly from the [AnythingLLM Mobile website](https://anythingllm.com/mobile).

#### Features

- **Chat with local SLM** - Chat with your local SLM (small language model) on your phone. Supports both reasoning and non-reasoning models.
- **Change models on the fly** - Easily swap between different models
- **Workspace and Threads** - Create workspaces and threads to organize your chats
- **On device RAG** - Locally process your documents and use them in your chats all fully offline
- **Agentic Tools** - Leverage the power of AnythingLLM's agentic tools like web search, web scraping, deep research, and even cross app interactions like drafting emails or managing your calendar
- **Sync with AnythingLLM Desktop & Cloud** - Sync your chats, workspaces, and threads with AnythingLLM Desktop or AnythingLLM Cloud/Self-hosted instances

If you have any general questions, please join the `#anythingllm-mobile` channel in the [AnythingLLM Discord](https://discord.gg/Dh4zSZCdsC) and we'll help you out.

###### Feedback Reporting

All feedback should be officially reported via the [AnythingLLM Discord](https://discord.gg/Dh4zSZCdsC) in the `#anythingllm-mobile` channel.

##### Syncing with AnythingLLM Desktop or Cloud

> **Tip:**
>
> Note: For AnythingLLM Desktop you need to enable "Enable Network Discovery" in the Settings > "Admin" > "General" page so that the Desktop app is available on the LAN via 0.0.0.0 bindings.

AnythingLLM Mobile while functional and complete standalone, is designed to be also be a companion to AnythingLLM Desktop and AnythingLLM Cloud.
You can sync your chats, workspaces, and threads with AnythingLLM Desktop or AnythingLLM Cloud/Self-hosted instances to leverage the full power of AnythingLLM.

To do this, click on the `AnythingLLM Mobile` text on the sidebar settings under `Tools`. From here you can scan the QR code with AnythingLLM Mobile app to connect the two apps.

![AnythingLLM Mobile Menu](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmobile%2Fmenu.png&w=3840&q=100)

##### Common Questions

###### IOS support?

We are planning to support iOS in the future. Currently, we are focusing on Android for a full release by the end of September 2025. iOS support coming after that in October 2025.

###### Can I download any model I want?

Right now, for performance reasons, we only support a hand-picked models. Eventually we will support any model you want, but for now, we are focusing on performance and stability.

###### How does the on device RAG work?

AnythingLLM Mobile runs a small embedding model + local vector database on your device to provide RAG capabilities with citations.

###### How can I add my own agent tools?

Currently, to use custom agent tools, MCPs or otherwise, you should use the sync feature with AnythingLLM Desktop or AnythingLLM Cloud. Customization of agent tools on mobile standalone is not yet supported.

### Privacy Policy

*AnythingLLM Mobile Privacy Policy*

**Source:** https://docs.useanything.com/mobile/privacy

> **Tip:**
>
> This is the privacy policy for AnythingLLM Mobile **only**. All other products and services are covered by their respective privacy policies.

### AnythingLLM Mobile App Privacy Policy

*Effective July 29, 2025*

> **Tip:**
>
> **TL;DR:**
> None of your messages, chat histories, and documents are ever transmitted from your system - everything is saved locally on your device by default.
>
> We do collect some information about your usage of AnythingLLM Mobile, but never anything that can be used to identify you, your chats, documents, content, or anything else.
>
> You can fully opt out of this telemetry by disabling it in the app settings.

#### Introduction

AnythingLLM Mobile processes as little info as possible, and can run entirely offline. This Privacy Policy ("Policy") describes what information Mintplex Labs ("we", "us", "our") may gather and how we use it when you download and use AnythingLLM Mobile (the "App").

We may update this policy occasionally. When we do, we'll post the new version on this page with a reasonable amount of time before the changes take effect.

#### Contact us

If you have any questions, comments or concerns regarding this Policy or our processing of information, please contact us at [team@mintplexlabs.com](mailto:team@mintplexlabs.com).

#### What we process and why

We only process information in the following occasions:

- When Telemetry is enabled and some usage stats are sent to our servers (see above)
- When you email us directly
- When you interact with the [AnythingLLM Community Hub](https://hub.anythingllm.com)

Here's what this means in practice, and the situations when we would receive data:

##### When You Email Us

- What: Your email address and the content of your email
- Why: So we can respond to your questions or provide the support you need

##### When You Interact with the AnythingLLM Community Hub

- What: General connection information (IP address, user agent, etc.)
- Why: The community hub is a public website with resources you can use freely inside the app. This service is operated by Mintplex Labs and is optional to use.

#### Our Commitment to Privacy

Privacy is core to AnythingLLM Mobile - as it is for all our products.

We process as little information as possible to facilitate your usage of the app, and regularly review our data practices to process only what's necessary. Even then, we only collect information that is anonymous and cannot be used to identify you, your chats, documents, content, or anything else.

You can turn it off fully once and forever in the app settings.

##### Never sell your information to third parties

We are not in the business of selling your information to third parties. We simply care about how people use the app, and how we can improve it. That is the only reason we collect any information at all.

In no way, shape, or form do we sell your information to third parties or use it as leverage for any other purpose.

##### Others involved in handling information

We use service providers who help us with our business operations. These providers are only authorized to store the information as necessary to provide these services to us and not for their own promotional purposes.

Service Providers we use:

- PostHog (Telemetry service) - Privacy Policy: <https://posthog.com/privacy>
- Cloudflare (CDN service) - Privacy Policy: <https://www.cloudflare.com/privacypolicy/>

##### Legal Requirements

In rare cases, we may need to disclose information to authorities, legal counsels, and advisors:

- To comply with legal obligations forced upon us by law
- When working with legal counsel on matters that could impact us

##### Business Changes

If our company undergoes organizational changes (like a merger or acquisition), information may be transferred to a new business as part of that process.

##### Data Subject Rights

AnythingLLM Mobile processes very limited data, none of which can be linked directly to individual users. Because the application does not include user-telemetry or user-specific tracking, we are unable to fulfill data subject requests such as providing a copy of your data or deleting your information. In other words, there's no way for us to identify or retrieve your specific data, and any information we do collect is anonymous and only kept briefly.

##### Additional information for individuals in the EU or UK

###### Controller

The data controller of the data described in this policy is:

Mintplex Labs, Inc., a Delaware corporation. Our registered address: 1950 W Corporate Way Ste. 25340, Anaheim, CA 92801.

###### Data subject rights

If you are in the EU or the UK, you have the following rights under the GDPR:

- Right to Access and receive a copy of your information that we process.
- Right to Rectify inaccurate information we have concerning you and to have incomplete information completed.
- Right to Data Portability, that is, to receive the information that you provided to us, in a structured, commonly used, and machine-readable format. You have the right to transmit this data to another person or entity. Where technically feasible, you have the right to have your information transmitted directly from us to the person or entity you designate.
- Right to Object to our processing of your information based on our legitimate interest. However, we may override the objection if we demonstrate compelling legitimate grounds, or if we need to process such information for the establishment, exercise, or defense of legal claims.
- Right to Restrict us from processing your information (except for storing it): (a) if you contest the accuracy of the information (in which case the restriction applies only for a period enabling us to determine the accuracy of the information); (b) if the processing is unlawful and you prefer to restrict the processing of the information rather than requiring the deletion of such data by us; (c) if we no longer need the information for the purposes outlined in this Policy, but you require the information to establish, exercise or defend legal claims; or (d) if you object to our processing based on our legitimate interest (in which case the restriction applies only for the period enabling us to determine whether our legitimate grounds for processing override yours).
- Right to be Forgotten. Under certain circumstances, such as when you object to our processing of your information based on our legitimate interest and there are no overriding legitimate grounds for the processing, you have the right to ask us to erase your information. However, notwithstanding such a request, we may still process your information if it is necessary to comply with our legal obligations, or for the establishment, exercise, or defense of legal claims. If you wish to exercise any of these rights, please contact us through the channels listed in this Policy.

When you contact us, we reserve the right to ask for reasonable evidence to verify your identity before we provide you with information. Where we are not able to provide you with information that you have asked for, we will explain the reason.

Subject to applicable law, you have the right to lodge a complaint with your local data protection authority. If you are in the EU, then according to Article 77 of the GDPR, you can lodge a complaint to the supervisory authority, in the Member State of your residence, place of work or place of alleged infringement of the GDPR.

If you are in the UK, you can lodge a complaint to the Information Commissioner's Office (ICO) pursuant to the instructions provided [here](https://ico.org.uk/make-a-complaint/).

###### Additional information for individuals in the United States

If you are an individual residing in the United States, we provide you with the following information pursuant to the applicable state privacy laws.

We do not sell your information and have not done so ever.

###### Your rights under U.S. State privacy laws

###### Right to deletion

Subject to certain exceptions set out below, on receipt of a verifiable request from you, we will:

- Delete your information from our records; and
- Direct any service providers to delete your information from their records.

Please note that we may not delete your information if it is necessary to:

Complete the transaction for which the information was collected, fulfill the terms of a written warranty or product recall conducted in accordance with federal law, provide a good or service requested by you, or reasonably anticipated within the context of our ongoing business relationship with you, or otherwise perform a contract between you and us.

Help to ensure security and integrity to the extent the use of the consumer's information is reasonably necessary and proportionate for those purposes.

Debug to identify and repair errors that impair existing intended functionality.

Exercise free speech, ensure the right of another consumer to exercise his or her right of free speech, or exercise another right provided for by law.

Engage in public or peer-reviewed scientific, historical, or statistical research that conforms or adheres to all other applicable ethics and privacy laws, when our deletion of the information is likely to render impossible or seriously impair the ability to complete such research, provided we have obtained your informed consent.

Enable solely internal uses that are reasonably aligned with your expectations based on your relationship with us and compatible with the context in which you provided the information.

We also will deny your request to delete if it proves impossible or involves disproportionate effort, or if another exception under the law applies. We will provide you with a detailed explanation that includes enough facts to give you a meaningful understanding as to why we cannot comply with the request to delete your information.

###### Right to correction

###### Right to correct inaccurate information

If we receive a verifiable request from you to correct your information and we determine the accuracy of the corrected information you provide, we will correct inaccurate information that we maintain about you.

In determining the accuracy of the information that is the subject of your request to correct, we will consider the totality of the circumstances relating to the contested information.

We also may require that you provide documentation if we believe it is necessary to rebut our own documentation that the information is accurate.

We may deny your request to correct in the following cases:

- We have a good-faith, reasonable, and documented belief that your request to correct is fraudulent or abusive.
- We determine that the contested information is more likely than not accurate based on the totality of the circumstances.
- Conflict with federal or state law.
- Another exception under the law.

###### Inadequacy in the required documentation

Compliance proves impossible or involves disproportionate effort.

We will provide you a detailed explanation that includes enough facts to give you a meaningful understanding as to why we cannot comply with the request to correct your information

###### Protection against discrimination

You have the right to not be discriminated against because you exercised any of your rights under applicable laws. If you exercise your rights, we cannot:

- deny you services.
- charge different prices or fees for services, also through discounts, benefits, or fines.
- provide you with a different level or quality of services.
- propose that you receive different prices or tariffs for services.

Please note that we may charge a different fee or provide a different level or quality of services, if the difference is reasonably related to the value we gain from your information.

###### Our response to your requests

We will respond to your requests within 45 days (or within 90 days, where the law permits, and we determine it necessary considering the complexity and number of the requests you have filed). If we take longer than 45 days, we will inform you of the extension within the initial forty-five-day response period, together with the reason for the extension.

We may deny your request in the following cases:

- If we believe in good faith, based on reasons which are documented in writing, that your request is fraudulent or is an abuse of your rights under applicable law.
- If we conclude that the request is irrelevant, based on all the circumstances at issue (e.g., if you requested to correct your information, and we find that it is likely to be accurate).
- If it is contrary to federal or state law.
- Due to discrepancy in the required documentation.
- If the fulfilment of your request turns out to be impossible or involves disproportionate effort.

We will provide you with a detailed explanation including sufficient facts, to enable you to meaningfully understand why we cannot fulfil your request.

You may appeal our decision to deny your request by sending us an email at [team@mintplexlabs.com](mailto:team@mintplexlabs.com).

### Terms of Use

*AnythingLLM Mobile Terms of Use*

**Source:** https://docs.useanything.com/mobile/terms

> **Tip:**
>
> This is the terms of use for AnythingLLM Mobile **only**. All other products and services are covered by their respective terms of use.

### AnythingLLM Mobile Terms of Use

Version: July 29, 2025

This page contains the Terms of Use for the AnythingLLM Mobile App.

For the Privacy Policy, please refer to the [AnythingLLM Privacy Policy](https://docs.useanything.com/mobile/privacy).

Please read these Terms and Conditions ("Terms") carefully as they govern your use of the Software and Services (each as defined below).

#### Terms of Service

These Terms constitute an agreement between Mintplex Labs, Inc. ("Mintplex Labs", "Company", "we", "us") and the person or entity that downloads or uses the Software and uses the Services ("You", "Your", "User", "Customer"). If the person downloading or using the Software or Services is an employee, agent or contractor of a corporate entity and using the Software or Services within the scope of their employment, agency or primarily for the benefit of the corporate entity, the Terms are between the corporate entity and Mintplex Labs -- and the corporate entity is the Customer.

You represent and warrant that: (i) the person agreeing to these Terms is authorized to enter into these Terms on behalf of Customer and (ii) these Terms are binding on Customer.

If You do not agree to these Terms, then You must not download or use the Software or Services

##### Definitions

**Software** means the software made available by Mintplex Labs to You (e.g., via download) where these terms are identified as the governing terms, and any modified, updated or enhanced versions of such programs or modules that Mintplex Labs makes available to You.

**Services** mean the support services, including responses to community forums, and any other services provided by Mintplex Labs pursuant to these Terms.

**Intellectual Property Rights** means all copyrights, trademarks, service marks, trade secrets, patents, patent applications, moral rights, contract rights and other proprietary rights.

**Content** means the data or content uploaded into the Software or otherwise used by You in connection with the Software.

**Documentation** means any published instructions and user manuals provided to You along with the Software or the [AnythingLLM Documentation](https://docs.anythingllm.com). The Certified System Requirements are a subset of the Documentation.

**Confidential Information** means the Software and all written or oral information, disclosed by Mintplex Labs related to the business, products, services or operations of Mintplex Labs that by the nature of the information or the circumstances surrounding disclosure ought reasonably to be treated as confidential. Confidential Information will not include information that: (a) was already known without restriction to You at the time of disclosure; (b) was disclosed to You by a third party who had the right to make such disclosure without any confidentiality restrictions; (c) is, or through no fault of Yours has become, generally available to the public or (d) was independently developed by You without access to, or use of, the Disclosing Party's Confidential Information.

##### License Grant and Other Rights

Subject to the terms and conditions of these Terms, Mintplex Labs grants to You a non-exclusive, non-transferable, license to use the Software solely for Your personal and / or internal business purposes and solely in accordance with the Documentation.

##### Restrictions On Use

You acknowledge that the Software and its structure, organization, and source code constitute valuable trade secrets and Confidential information of Mintplex Labs and its suppliers. Except as expressly permitted by these Terms, You agree that You will not permit any third party to, and You will not itself: (a) modify, adapt, alter, translate, or create derivative works from the Software or the Documentation; (b) integrate the Software with other software other than through Mintplex Labs published interfaces made available with the Software; (c) use any open source products with the Software in a manner that imposes, or could impose, a requirement or condition that the Software or any part thereof: (i) be disclosed or distributed in source code for; (ii) be licensed for the purpose of making modifications or derivative works or (iii) be redistributable at no charge; (d) sublicense, distribute, sell, use for service bureau use, as an application service provider, or a software-as-a-service, lease, rent, loan, or otherwise transfer the Software or the Documentation to any third party; (e) reverse engineer, decompile, disassemble, or otherwise attempt to derive the source code for the Software, except and only to the extent that such activity is expressly permitted by applicable law notwithstanding this limitation; (f) remove, alter, cover or obfuscate any copyright notices or other proprietary rights notices included in the Software; or (g) otherwise use or copy the Software except as expressly permitted hereunder. You will notify Mintplex Labs of any unauthorized use or disclosure of the

##### Content

You are solely responsible for any and all obligations with respect to the Content including its accuracy, quality, legality and appropriateness and that it complies with Mintplex Labs's Authorized Use Policy, as it may be updated from time-to-time. In the event that You make any Content available to Mintplex Labs, You will obtain all third party licenses, consents and permissions needed for Mintplex Labs to use the Content to provide the Services. For the avoidance of doubt, Mintplex Labs reserves the right, but does not undertake the responsibility, to investigate any breach of the Authorized Use Policy or a breach of this Section

You also understand that the Software is not designed to be used for any illegal or unauthorized purposes. You are responsible for ensuring that You are in compliance with all applicable laws and regulations.

##### Installation

You are responsible for installing the Software in compliance with the Certified System Requirements as permitted under these Terms.

##### Feedback

Mintplex Labs in its sole discretion, may utilize, all comments and suggestions, whether written or oral, furnished by You to Mintplex Labs in connection with its access to and use of the Software, Services and Documentation (all reports, comments and suggestions provided by You hereunder constitute, collectively, the "Feedback"). You hereby grant Mintplex Labs a worldwide, non-exclusive, irrevocable, perpetual, royalty-free right and license to incorporate the Feedback into Mintplex Labs products and services.

##### Proprietary Rights

As between You and Mintplex Labs, You own all rights, title and interest in the Content and all rights not expressly granted to Mintplex Labs in these Terms in the Content are reserved to You. The Software and Documentation, and all worldwide Intellectual Property Rights therein, are the exclusive property of Mintplex Labs and its suppliers. All rights in and to the Software not expressly granted to You in these Terms are reserved by Mintplex Labs and its suppliers. You will not remove, alter, or obscure any proprietary notices (including copyright notices) of Mintplex Labs or its suppliers on the Software or the Documentation.

##### Disclaimers

###### General Disclaimers

THE SOFTWARE AND SERVICES ARE MADE AVAILABLE BY MINTPLEX LABS "AS IS", "WITH ALL FAULTS" AND WITHOUT WARRANTY OF ANY KIND, INCLUDING THAT THERE ARE NO EXPRESS, IMPLIED OR STATUTORY WARRANTIES, INCLUDING ANY WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, AND NON-INFRINGEMENT OF THIRD PARTY RIGHTS. MINTPLEX LABS DOES NOT WARRANT THAT THE SOFTWARE WILL MEET YOUR REQUIREMENTS OR THAT THE SOFTWARE WILL WORK UNINTERRUPTED.

###### Specific Disclaimers

(A) THE SOFTWARE IS DESIGNED TO WORK WITH THIRD PARTY PRODUCTS ("THIRD PARTY PRODUCTS") INCLUDING THIRD PARTY ARTIFICIAL INTELLIGENCE MODELS ("THIRD PARTY AI MODELS", WHICH ARE A SUBSET OF THIRD PARTY PRODUCTS). MINTPLEX LABS MAY FACILITATE YOUR ABILITY TO DOWNLOAD AND INTEGRATE THE THIRD PARTY PRODUCTS WITH THE SOFTWARE WITH THE UNDERSTANDING THAT SUCH THIRD PARTY PRODUCTS ARE MADE AVAILABLE TO YOU PURSUANT TO A LICENSE AGREEMENT BETWEEN YOU AND THE THIRD PARTY PROVIDER OF SUCH THIRD PARTY PRODUCTS (THE "CUSTOMER – THIRD PARTY PROVIDER AGREEMENT"). YOU WILL UNDERTAKE ALL MEASURES NECESSARY TO ENSURE THAT ITS USE OF THE THIRD PARTY PRODUCTS IN CONNECTION WITH THE SOFTWARE AND SERVICES COMPLIES IN ALL RESPECTS WITH APPLICABLE LAW, THE CUSTOMER – THIRD PARTY PROVIDER AGREEMENT, AND ANY OTHER CONTRACTUAL OR LEGALLY BINDING OBLIGATIONS IN CONNECTION WITH THE THIRD PARTY PRODUCTS, INCLUDING THIRD PARTY LICENSES FOR THE USE OF FREE AND OPEN SOURCE SOFTWARE. IN NO EVENT IS MINTPLEX LABS LIABLE TO YOU FOR ANY FAILURE OF THE THIRD PARTY PRODUCTS OR

###### Export Controls and Sanctions

The Software maybe be subject to trade control laws, including the export control and economic sanctions laws of the United States, including but not limited to the Export Administration Regulations maintained by the U.S. Department of Commerce, trade and economic sanctions maintained by the U.S. Treasury Department's Office of Foreign Assets Control ("OFAC"), the International Traffic in Arms Regulations maintained by the U.S. Department of State (collectively, "Trade Control Laws"). You represents and warrants that You are (a) not located in, organized under the laws of, or ordinarily resident in any country or territory subject to territorial sanctions ("Sanctioned Country"), nor owned by or acting on behalf of a Government subject to asset-blocking sanctions or any person or entity organized, located or ordinarily resident in a Sanctioned Country; and (b) not a person identified on, or more than 50% owned or controlled, directly or indirectly, by or acting on behalf or, at the direction of, any entity identified on applicable government restricted party lists, such as the Specially Designated Nationals List maintained by OFAC. You further agree to comply with all applicable Trade Control Laws in its use of the Software. Specifically, You agree not to, directly or indirectly, use, sell, supply, export, reexport, transfer, divert, release, or otherwise dispose of any products, software, or technology (including products derived from or based on such technology) received from Mintplex Labs to any destination, entity, or person or for any end use prohibited by applicable Trade Controls Laws.

###### Indemnification

You will indemnify, defend and hold harmless Mintplex Labs, its directors, officers, employees and representatives from and against any and all damages, losses, and expenses of any kind (including reasonable attorneys' fees and costs) arising out of or related to: (a) Your breach of any of these Terms. Including any representation or warranty; (b) any Content; (3) any activity in which You engage on or through the use of the Software or Services and (d) Your violation of any law or the rights of a third party.

###### Disclaimers and limitations on Remedies

YOU AGREES THAT ITS SOLE AND EXCLUSIVE REMEDY FOR ANY PROBLEMS OR DISSATISFACTION WITH THE SOFTWARE AND SERVICES IS TO UNINSTALL THE SOFTWARE AND TO STOP USING THE SERVICES. TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT WILL MINTPLEX LABS, ITS OFFICERS, SHAREHOLDERS, EMPLOYEES, AGENTS, DIRECTORS, SUBSIDIARIES, AFFILIATES, SUCCESSORS, ASSIGNS, SUPPLIERS, OR LICENSORS BE LIABLE FOR: (A) ANY INDIRECT, SPECIAL, INCIDENTAL, PUNITIVE, EXEMPLARY, OR CONSEQUENTIAL DAMAGES; (B) ANY LOSS OF USE, DATA, BUSINESS, OR PROFITS (WHETHER DIRECT OR INDIRECT), IN ALL CASES ARISING OUT OF THE USE OF OR INABILITY TO USE THE SOFTWARE, SERVICES, THIRD PARTY PRODUCTS, THIRD PARTY AI MODELS, OR CUSTOMER’S OWN SOFTWARE, HARDWARE OR OPERATIONS, REGARDLESS OF LEGAL THEORY, WITHOUT REGARD TO WHETHER MINTPLEX LABS HAS BEEN WARNED OF THE POSSIBILITY OF THOSE DAMAGES, AND EVEN IF A REMEDY FAILS OF ITS ESSENTIAL PURPOSE; OR (C) AGGREGATE LIABILITY FOR ALL CLAIMS RELATING TO THE SOFTWARE OR SERVICES IS $50.00. For clarification, these Terms do not limit Mintplex Labs’s liability for fraud, fraudulent misrepresentation, death or personal injury to the extent that applicable law would prohibit such a limitation.

###### Confidentiality

Your use of the Software and Services is subject to the [Mintplex Labs & AnythingLLM Desktop Privacy Policy](https://docs.anythingllm.com/privacy).

###### Notices

All notices or demands required hereunder will be sent through email by email addresses provided or be delivered by certified or registered mail to; in the case of Mintplex Labs, 1950 W Corporate Way Ste. 25340, Anaheim, CA 92801 or in the case of Yours via any means available to Mintplex Labs .

###### Governing Law and Venue

These Terms and all Statements of Work will be governed by and interpreted in accordance with the laws of the State of California, without reference to its choice of laws rules. Any action or proceeding arising from or relating to these Terms will be brought in a state court in Orange County, or federal court in Orange County, California, and each party irrevocably submits to the jurisdiction and venue of any such court in any such action or proceeding.

###### Remedies

You acknowledge that the Software contains valuable trade secrets and proprietary information of Mintplex Labs, that any actual or threatened breach of Section 2 will constitute immediate, irreparable harm to Mintplex Labs for which monetary damages would be an inadequate remedy, that injunctive relief is an appropriate remedy for such breach, and that if granted, You agree to waive any bond that would otherwise be required.

###### Waivers

All waivers must be in writing. Any waiver or failure to enforce any provision of the Terms on one occasion will not be deemed a waiver of any other provision or of such provision on any other occasion.

###### Severability

If any provision of the Terms are unenforceable, such provision will be changed and interpreted to accomplish the objectives of such provision to the greatest extent possible under applicable law and the remaining provisions will continue in full force and effect.

###### Entire Agreement

These Terms and the exhibits hereto, constitute the entire agreement between the parties regarding the subject hereof and supersedes all prior or contemporaneous agreements, understandings, and communication, whether written or oral. These Terms will not be modified except by a subsequently dated written amendment signed on behalf of Mintplex Labs and You by their duly authorized representatives.


---

## Community Hub

### What is the Community Hub?

*The AnythingLLM Community Hub is a repository of agent skills that can be used in AnythingLLM.*

**Source:** https://docs.useanything.com/community-hub/about

### What is the AnythingLLM Community Hub?

The [AnythingLLM Community Hub](https://hub.anythingllm.com) is a platform and marketplace for AnythingLLM users to share system prompts, slash commands, agent skills, and more.

The community hub enables you to share your own items, skills, and workflows with the AnythingLLM community both **publicly** and **privately**.

Currently, the AnythingLLM Community Hub is in **beta** and as such, not all types of items are supported.

##### Current Supported Item Types

- Agent Skills
- System Prompts
- Slash Commands

*More item types are coming soon!*

- Workspaces
- Data Connectors
- Authentication Providers

### FAQ

*Frequently asked questions about the AnythingLLM Community Hub.*

**Source:** https://docs.useanything.com/community-hub/faq

#### Connecting to the AnythingLLM Community Hub

> **Note:**
>
> Only pulling **private** items from the AnythingLLM Community Hub requires a
> Connection key. Public items do not require a Connection key and can be pulled
> in without one. To create a Connection key, visit your [profile page on the
> AnythingLLM Hub](https://hub.anythingllm.com/me) and click the **Create
> Connection Key** button.

Connecting to the AnythingLLM Community Hub requires a Connection key. You can find your Connection key by visting your [profile page on the AnythingLLM Hub](https://hub.anythingllm.com/me) and copying or creating a new Connection key.

![Connection key](https://docs.useanything.com/_next/image?url=%2Fimages%2Fcommunity-hub%2Fconnection-key-hub.png&w=3840&q=75)

Next, you can use the Connection key to connect to the AnythingLLM Community Hub in AnythingLLM.

![Connection key](https://docs.useanything.com/_next/image?url=%2Fimages%2Fcommunity-hub%2Fconnection-key.png&w=3840&q=75)

#### No private items

The AnythingLLM Community Hub offers both public and private items. When you create an item, you can choose to make it private or public.

Public items are visible to all users of AnythingLLM. **Private items are only visible to you and Teams** you share the tools with that you also have access to.

If you are trying to pull in a private item from the AnythingLLM Community Hub:

- Ensure you are logged in with the same account you used to create the item.
- You are using the correct [Connection key](https://docs.useanything.com/community-hub/faq#connecting-to-the-anythingllm-community-hub) in AnythingLLM.
- The item has been shared with at **least** one of your Teams.

#### Verification

Some items in the AnythingLLM Community Hub are verified by the AnythingLLM team. These items are marked with a blue checkmark and a label that says **Verified**.

![Verified badge](https://docs.useanything.com/_next/image?url=%2Fimages%2Fcommunity-hub%2Fverification.png&w=3840&q=75)

Verified items have been reviewed by the AnythingLLM team to ensure they are safe and working as expected. Verification is not a guarantee of quality or safety, but rather a signal that the AnythingLLM team has reviewed the item and believes it is safe to use.

You will only see verification badges for public items that are:

- Agent Skills
- Data Connectors
- Workspaces

The AnythingLLM team will review and verify items on a best-effort basis. If you believe an item should be verified, please let us know by [contacting support](mailto:team@anythingllm.com).

### Importing from the AnythingLLM Community Hub

*How to import items from the AnythingLLM Community Hub into AnythingLLM.*

**Source:** https://docs.useanything.com/community-hub/import

Every item in the AnythingLLM Community Hub can be imported into AnythingLLM. The process for importing each type is mostly the same.

#### Locate the item on the AnythingLLM Hub

Given a public or private item on the AnythingLLM Hub, you can get the import string from the item by clicking on the **Import to AnythingLLM** button.

![Import button](https://docs.useanything.com/_next/image?url=%2Fimages%2Fcommunity-hub%2Fimport-button.png&w=3840&q=75)

Clicking this button will show you a modal with the import string for the item.

*On desktop this may prompt you to automatically open AnythingLLM to automatically handle the import via a deep links.*

![Import modal](https://docs.useanything.com/_next/image?url=%2Fimages%2Fcommunity-hub%2Fimport-modal.png&w=3840&q=75)

Paste the import string into AnythingLLM to begin the import process.

![Import modal](https://docs.useanything.com/_next/image?url=%2Fimages%2Fcommunity-hub%2Fimport-anythingllm.png&w=3840&q=75)

From here, you can follow the on-screen instructions to complete the import.

#### Failed to import agent skill?

On self-hosted or the dockerized versions of AnythingLLM, you may encounter an error when importing an agent skill.

This is because the agent skill requires you to enable imports of agent skills in the AnythingLLM configuration. By default, this is disabled to prevent malicious users from adding harmful agent skills to your instance.

If you are the administrator of the AnythingLLM instance, you can enable imports of agent skills by modifying the `COMMUNITY_HUB_BUNDLE_DOWNLOADS_ENABLED` configuration value to the appropriate security setting.

See the [configuration page](https://docs.useanything.com/configuration#anythingllm-hub-agent-skills) for more information.

### Uploading to the AnythingLLM Community Hub

*How to upload items to the AnythingLLM Community Hub.*

**Source:** https://docs.useanything.com/community-hub/upload

AnythingLLM allows you to upload items to the AnythingLLM Community Hub to share with the world or privately with just your team.

Some items can be created directly on the [AnythingLLM Community Hub](https://hub.anythingllm.com):

- System prompts
- Slash commands

However, other items can only be uploaded to the AnythingLLM Community Hub as they require custom code and are more like "plugins" for AnythingLLM.

These items are:

- Agent skills
- Data connectors
- Workspaces

#### Uploading Agent Skills

Agent skills extend the functionality of AnythingLLM by allowing you to add custom tools for your local LLM to leverage when using the [`@agent` directive.](https://docs.useanything.com/agent/overview)

Custom agents skills allow you to build *anything* that you can imagine and have that work natively within AnythingLLM with minimal setup and technical knowledge.

[Learn more about how to create agent skills →](https://docs.useanything.com/agent/custom/developer-guide)

##### The Anythingllm-hub-cli tool

AnythingLLM offers a CLI tool called [`anythingllm-hub-cli`](https://www.npmjs.com/package/@mintplex-labs/anythingllm-hub-cli) that allows you to upload items to the AnythingLLM Community Hub easily.

To upload an agent skill to the AnythingLLM Community Hub, you can use the following commands to upload your skill privately or publicly.

```
### Install the CLI tool
npm install -g @mintplex-labs/anythingllm-hub-cli@latest
```

To create a new agent skill from our template, you can run the following command:

```
npx @mintplex-labs/anythingllm-hub-cli init --type agent-skill --output ./my-new-skill
### Creates a folder called `my-new-skill` with the agent skill template
### This should contain your plugin.json and handler.js file to get started.
```

To being the upload process you will need a [Connection key](https://docs.useanything.com/community-hub/faq#connecting-to-the-anythingllm-community-hub).

```
npx @mintplex-labs/anythingllm-hub-cli login
### You will be prompted to enter your connection key
### this will authenticate you and save your connection key to the CLI
### this will also save your profile information so you don't have to login again in the future
 
### You can check your connection key by running `npx @mintplex-labs/anythingllm-hub-cli config`
```

Next, you can upload your agent skill to the AnythingLLM Community Hub by running the following command:

```
### Assumes you are in the root of the agent skill directory you want to upload
npx @mintplex-labs/anythingllm-hub-cli upload --type agent-skill --path .
### > Any missing details like name, description, etc. will be prompted for
### > You will be prompted if you would like to make the item public or private
### > You will be asked to confirm the files being uploaded
### > This will begin the upload process - it is automatic and will notify you once complete
 
### > You will be given a URL to view your item on the AnythingLLM Community Hub once it is uploaded
```

🎉 **Congratulations!** You have now uploaded your agent skill to the AnythingLLM Community Hub.

*it's that easy!*

#### Uploading Data Connectors

*data connectors are currently not supported*

#### Uploading Workspaces

*workspaces are currently not supported*


---

## AnythingLLM Cloud

### AnythingLLM Cloud

*Private Cloud Instance hosted by AnythingLLM*

**Source:** https://docs.useanything.com/cloud/overview

![AnythingLLM Cloud](https://docs.useanything.com/_next/image?url=%2Fimages%2Fcloud%2Fheader-image.png&w=3840&q=100)

### Private managed AnythingLLM

AnythingLLM cloud is the easiest way to trial and scale AnythingLLM for your business or personal use.

The Mintplex Labs team offers **isolated** and **private** instances of AnythingLLM that you can use to try out or scale up AnythingLLM for your business or personal use.

Each instance is hosted on an isolated AWS instance that is automatically updated and managed by the Mintplex Labs core team. Your data and resources are not shared with any other customers who are using our managed service.

##### [You can get a hosted AnythingLLM instance here!](https://my.mintplexlabs.com/aio-checkout?product=anythingllm)

![AnythingLLM Cloud Pricing](https://docs.useanything.com/_next/image?url=%2Fimages%2Fcloud%2Fpricing.png&w=3840&q=100)

### 502 Error on AnythingLLM Hosted

*How to reboot your crashed instance from too large of a document*

**Source:** https://docs.useanything.com/cloud/error-502

> **Warning:**
>
> **Notice**
> This page only applies to the Hosted Cloud version of AnythingLLM and only applies to those using the built-in embedder model.
>
> Following these instructions are the preferred way to get your instance back online.
>
> **Please do not e-mail [team@mintplexlabs.com](mailto:team@mintplexlabs.com) unless this process does not work for you.**

##### I am getting a 502 on my hosted AnythingLLM!

> **Warning:**
>
> **Notice** This "crash" resulted from your actions on uploading of a document.
> If you upload the same document again it **will crash again**.

**What happened?** You uploaded too large of a document to your instance (word count, not file size) and on your tier likely overwhelmed the CPU causing the process to be killed to prevent the instance from freezing. This same error can occur from uploading *many* files that are all medium sized at the same time.

Recommendations for maximum file size based on tier:

- **Starter Tier**: 10k words per file
- **Professional Tier**: 50k words per file

##### How do I get my instance back up?

- Visit [Your My.Mintplexlabs.com](https://my.mintplexlabs.com/dashboard) account.

Click on your subscription item that is currently offline (Click the gear icon)

![AnythingLLM Subscription Item](https://docs.useanything.com/_next/image?url=%2Fimages%2Fcloud%2Fsubitem.png&w=1080&q=100)

You will now see a screen that looks like this

![AnythingLLM Subscription Dashboard](https://docs.useanything.com/_next/image?url=%2Fimages%2Fcloud%2Fdashboard.png&w=1080&q=100)

Scroll down and you will see a button labeled "Reboot". Clicking this will reboot your instance and it will be available again shortly after.

![AnythingLLM Subscription Reboot](https://docs.useanything.com/_next/image?url=%2Fimages%2Fcloud%2Freboot.png&w=1080&q=100)

##### How do I prevent this from happening again?

> **Tip:**
>
> **Pro tip!**
>
> If you have a large amount of really large files you want to embed - using a cloud based embedder will unlock the ability to quickly upload and
> use these files with zero concern for overloading of the instance.

There are a few ways to prevent this situation from occurring again.

- Upload smaller documents, one at a time.
- Break larger documents into more "digestible" files.
- [Switch to a cloud based embedder](https://docs.useanything.com/anythingllm-setup/embedder-configuration/overview#cloud-model-providers)

### Limitations

*Limitations of AnythingLLM Hosted Cloud Instances*

**Source:** https://docs.useanything.com/cloud/limitations

AnythingLLM Hosted Cloud is the quickest way to get a multi-user, managed, and hosted version of AnythingLLM on a custom domain.

While this form of accessing AnythingLLM there are some acute limitations you may not experience with other forms of AnythingLLM, like Desktop or self hosted.

#### No "built-in" LLM

AnythingLLM hosted cloud does not ship with a built-in LLM you can use like in our desktop instance. This is due to CPU limitations of the instance we provide for you, which has no GPU and limited CPUs and RAM.

Due to this, we limit access **only** to local LLMs that you can run yourself and connect to, or any supported cloud-based LLM provider.

#### Limited capacity for built-in embedder

> **Note:**
>
> **Beware!** The built-in embedder will not block you from trying to embed a
> 5,000pg PDF, but it will crash your instance. (502 error).

AnythingLLM **does allow** you to use the built-in embedder model, which is extremely convenient, cannot embed on CPU any arbitrarily large document.

The Starter tier ships with **very minimal** compute resources while Professional ships with much more compute. This means that uploading a large document (in words, not file size) can overwhelm the CPU and cause
the process to exit. This will result in a 502 error.

##### 

#### Issues with "Accuracy Optimized" Search in Workspace

Sometimes, your instance may become unresponsive or slow when using the "Accuracy Optimized" search in the Workspace if the workspace has a large number of files.

This is because the "Accuracy Optimized" search requires a lot of memory and CPU to run - which again are limited on the instance we provide for you.

You can prevent this by using the `Default` search mode in the Workspace settings.

#### No custom Agent supported

While AnythingLLM does support [custom coded Agents](https://docs.useanything.com/agent/custom/introduction), we do not support custom Agents in the hosted cloud due to security concerns
as well other general limitations to running arbitrary code in a hosted environment.

If attempting to use a custom Agent, you will see an error about the system administrator not allowing custom Agents. This cannot be changed on hosted cloud.

If you need to use a custom Agent, you can use the [AnythingLLM Desktop](https://docs.useanything.com/installation-desktop/overview) or a [self-hosted AnythingLLM](https://docs.useanything.com/installation-docker/overview) instance.

#### No MCP support

AnythingLLM does not support [MCP (Model-Context Protocol)](https://docs.useanything.com/cloud/mcp-compatibility/overview) in the hosted cloud due to security concerns as well other general limitations to running arbitrary code in a hosted environment.

If you need to use MCPs, you can use the [AnythingLLM Desktop](https://docs.useanything.com/installation-desktop/overview) or a [self-hosted AnythingLLM](https://docs.useanything.com/installation-docker/overview) instance.

### AnythingLLM Cloud Privacy Policy

*Privacy Policy for AnythingLLM Cloud*

**Source:** https://docs.useanything.com/cloud/privacy-policy

This policy was last updated on July 1, 2024.

We at Mintplex Labs Inc prioritize the protection of your privacy. This Privacy Policy explains our practices regarding the collection, use and disclosure of information that we receive through our hosted cloud service of AnythingLLM. This Privacy Policy does not apply to any third-party websites, services or applications, even if they are accessible through our Services, nor does it apply to self-hosted instances of AnythingLLM. For any inquiries regarding this privacy policy or to exercise your legal rights, please reach out to us at [team@mintplexlabs.com](mailto:team@mintplexlabs.com).

#### How We Use Your Data

##### AnythingLLM Cloud Registration

Upon registering for AnythingLLM cloud, we collect your name, email and organization to establish a contractual relationship enabling access to our platform. We utilize PostHog to enhance our product understanding and optimize user experience. Additionally, our Payment Provider - Stripe, collects further details, such as address and credit card information, to facilitate payment processing. You retain the option to delete your AnythingLLM cloud account.

##### Instance Access and Management

Our team may access your AnythingLLM hosted instance solely for the purposes of debugging, maintenance, and regular customer satisfaction services. This access is strictly limited to necessary operational functions and maintaining service quality.

##### Data Privacy and Sharing

We do not share, make visible, or disseminate any generated content, uploaded materials, or activity generated on your instance beyond anonymous telemetry data. Users have the option to disable telemetry collection through the application user interface.

##### Website Usage Information

With consent, we collect website usage data to enhance user experience and website performance. PostHog may be utilized for this purpose.

#### Third-Party Services

We utilize the following third-party services:

- Stripe for payment processing
- PostHog for analytics
- Amazon Web Services for infrastructure

#### Data Storage and Security

Your data is stored and processed using Amazon Web Services infrastructure. We implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk.

#### Deletion of Data

Upon cancellation of service, failure to pay, or manual termination, no information about your instance, use, or data is retained. The instance and its associated data is permanently deleted from our systems and cannot be recovered at the exact time of cancellation for any reason.

#### Your Rights

Under applicable data protection laws, you have various rights, including:

- Access to your personal data
- Correction of inaccurate data
- Erasure of your data
- Restriction of processing
- Data portability
- Objection to processing
- Withdrawal of consent
- Right to lodge a complaint with the relevant supervisory authority

#### Data Retention

We retain personal data only as long as necessary for its intended purpose, including legal and reporting requirements. Upon service termination or account deletion, all instance data is permanently removed from our systems.

#### Changes to This Policy

We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the "last updated" date.

#### Contact Information

For any questions about this Privacy Policy, please contact us at:

- Email: [team@mintplexlabs.com](mailto:team@mintplexlabs.com)

### AnythingLLM Cloud Terms & Conditions

*Terms & Conditions for AnythingLLM Cloud*

**Source:** https://docs.useanything.com/cloud/terms-and-conditions

### Terms of Service

We, Mintplex Labs Inc, is located in California, United States.

For any inquiries regarding these Terms, please reach out to us at [team@mintplexlabs.com](mailto:team@mintplexlabs.com).

Platform is defined as our cloud-hosted managed AnythingLLM product and associated services in our managed cloud environment.

Your acceptance of these Terms is implied upon using our Platform. If you do not agree with them, refraining from using our Platform is necessary.

For non-consumer entities, confirmation of authority to bind the business to these Terms is required. References to "you" or "your" pertain to the business entity accepting these Terms unless specified otherwise.

#### SCOPE OF AGREEMENT

These Terms of Service specifically govern the hosted, Software-as-a-Service (SaaS) version of AnythingLLM accessed through our managed cloud infrastructure. This agreement does not cover self-hosted or other deployment methods of AnythingLLM.

#### ACCOUNT CREATION AND SECURITY

Account creation is mandatory to access our Platform. Accuracy and currency of information provided during registration are essential. Upon registration, you are granted a personal, non-transferable right and license to use the Platform for internal business purposes until termination as outlined in these Terms.

Safeguarding your account details, including username and password, is imperative. Prompt notification to us at [team@mintplexlabs.com](mailto:team@mintplexlabs.com) is required if unauthorized access is suspected.

#### SUBSCRIPTION AND PAYMENT

These terms are legally binding. Usage of our Platform indicates acknowledgment and agreement to these terms, provided you have the legal capacity to enter contracts in your residing country. For business representations, authority to bind them to these terms is essential.

Subscription fees apply. Payment terms vary depending on subscription plans. You are responsible for maintaining current payment information and monitoring your subscription status for payment failures through my.mintplexlabs.com or your contact email used during subscription creation.

We reserve the right to cancel your subscription for any reason at any time.

#### PLATFORM USAGE AND LIMITATIONS

Our Platform encompasses AnythingLLM and associated services in our managed cloud environment.

Platform performance is maintained to described standards, although security and bug-free operation are not guaranteed. Users are responsible for configuring their systems for Platform access.

Platform suspension or restriction may occur for operational reasons.

Users must ensure compliance with these Terms among all accessing parties.

#### DATA RETENTION AND DELETION

Deletion of services is final and non-recoverable. Upon cancellation of service, failure to pay, or manual termination, no information about your instance, use, or data is retained.

#### INTELLECTUAL PROPERTY

Platform intellectual property rights are retained by us, with limited access for internal use only.

User data transmitted through or generated through use of the Platform remains owned by the account owner, with granted usage rights for Platform improvement.

#### CANCELLATION AND TERMINATION

Subscription termination options are available via the Platform or email.

We reserve the right to terminate or suspend access to our services at any time, for any reason, without prior notice.

#### LIABILITY

Limitations on liability are outlined, excluding certain liabilities prohibited by law.

We do not guarantee Services quality or suitability for individual purposes, with no liability assumed for user due diligence lapses.

If you are not satisfied with our services, you can cancel your subscription at any time or cancel your account at any time via my.mintplexlabs.com.

If your service is offline or otherwise unavailable, please contact us at [team@mintplexlabs.com](mailto:team@mintplexlabs.com) for us to investigate the issue and get you back online as soon as possible.

#### REFUNDS

Agreement to these terms is implied upon using our Platform. If you request a refund, we will refund your subscription prorated for the time you have used the service during the current billing cycle.

This refund will be issued to the original payment method you used to purchase the subscription.

Refunds will not be issued for any other reason and are at the sole discretion of Mintplex Labs or any other authorized representative.

#### INSTANCE OFFLINE RECOVERY

If your instance goes offline **it is your responsibility** to get it back online via the my.mintplexlabs.com dashboard **or** you can contact us at [team@mintplexlabs.com](mailto:team@mintplexlabs.com) to engage our support team to get it back online manually.

Under no circumstances will Mintplex Labs be liable for any loss of data or any other issues arising from your instance being offline, nor are you entitled to any refunds or credits in any form for any subscription that is offline for any period of time and for any reason.

#### GOVERNING LAW

These Terms shall be governed by and construed in accordance with the laws of California, United States.

#### CHANGES TO TERMS

We reserve the right to modify these Terms at any time. Changes will be communicated via updated versions with effective dates indicated.

This terms was last updated on July 1, 2024


---

## AnythingLLM Pro

### Getting Your Pro Key

*How to purchase and activate your AnythingLLM Pro license key.*

**Source:** https://docs.useanything.com/pro/getting-started

Setting up AnythingLLM Pro takes less than a minute. Purchase a license key, paste it into the app, and you're done — all Magic features become unlimited immediately.

#### Step 1: Purchase a Pro License

Visit the [AnythingLLM Pro checkout page](https://my.mintplexlabs.com/aio-checkout?product=anything_llm_desktop_pro) to purchase your license. You'll receive a license key immediately after checkout.

![AnythingLLM Pro checkout page](https://docs.useanything.com/_next/image?url=%2Fimages%2Fpro%2Fpro-checkout.png&w=2048&q=75)

#### Step 2: Open Pro Settings in AnythingLLM

In AnythingLLM Desktop, navigate to **Settings** → **AnythingLLM Pro** in the sidebar. This opens the Pro subscription management page.

![AnythingLLM Pro settings page](https://docs.useanything.com/_next/image?url=%2Fimages%2Fpro%2Fdesktop-pro-page.png&w=2048&q=75)

#### Step 3: Activate Your License Key

Paste your license key into the **License Key** input field and click **Activate**. AnythingLLM will validate your key — once confirmed, you'll see a green "Pro License Active" badge.

![AnythingLLM Pro settings page](https://docs.useanything.com/_next/image?url=%2Fimages%2Fpro%2Fdesktop-pro-active.png&w=2048&q=75)
> **Tip:**
>
> You can also just click the "Open in AnythingLLM" button on the subscription
> management page to automatically open AnythingLLM and activate your license.

#### What happens after activation?

Once your Pro license is active:

- **All daily limits are removed** — Magic Echo, Magic Beacon, and Magic Tab become unlimited.
- **Watermark-free documents** — Any documents generated by AI will no longer include AnythingLLM branding.
- **Future features included** — Any new Pro features we ship are automatically available to you.

Your license is validated periodically to ensure it remains active. If your subscription lapses, features will revert to their free-tier daily limits — you never lose access to the features themselves.

#### Don't have a license key yet?

If you're not sure whether Pro is right for you, you can try every Magic feature for free first. Each feature includes a daily free-usage allowance so you can experience the full capability before purchasing.

When you're ready, visit the [AnythingLLM Pro checkout page](https://my.mintplexlabs.com/aio-checkout?product=anything_llm_desktop_pro) to get your key.

### Why AnythingLLM Pro?

*AnythingLLM Pro are paid features for AnythingLLM Desktop that extend our on-device agent experience to your entire OS.*

**Source:** https://docs.useanything.com/pro/overview

> **Tip:**
>
> AnythingLLM Pro is only available on AnythingLLM Desktop v1.15.0 and later.
>
> All features are available on Windows and macOS.

### AnythingLLM Pro?

AnythingLLM Pro unlocks unlimited Magic features — AI tools that work system-wide across your entire computer, privately and on-device. With AnythingLLM Pro, the entire idea is to
deliver on the full promise of AI Agents that exist across an entire computer, but work alongside you without being constrained by the limitations of a browser or app window.

#### What's included in Pro?

Pro unlocks **unlimited daily usage** of all Magic features — the AI tools that work system-wide across your entire computer. Every Magic feature has a generous free tier, and Pro simply removes those daily limits.

[[Video](https://webassets.anythingllm.com/magic-feature-promos-desktop/MagicEcho-promo.mp4)

##### Magic Echo

Smart dictation that cleans your words and knows what's on your screen — anywhere on your computer.

Learn more →](https://docs.useanything.com/pro/magic-echo)[[Video](https://webassets.anythingllm.com/magic-feature-promos-desktop/MagicBeacon-promo.mp4)

##### Magic Beacon

Highlight anything on your screen and instantly ask, revise, or research it — without switching apps.

Learn more →](https://docs.useanything.com/pro/magic-beacon)[[Video](https://webassets.anythingllm.com/magic-feature-promos-desktop/MagicTab-promo.mp4)

##### Magic Tab

Finishes your sentences as you type, in any app. Press Tab to accept — only what you accept counts.

Learn more →](https://docs.useanything.com/pro/magic-tab)

**Additional Pro perks:**

- **Watermark-Free Documents** — Documents your AI generates are clean, professional, and ready to share with no AnythingLLM branding.
- **Future Pro Features** — Every Pro feature we ship is yours automatically. One subscription, everything we build.

#### So, is AnythingLLM free anymore?

100% absolutely. AnythingLLM Desktop will and forever will be free to use for 99% of our features. We are committed to open-source in our self-hosted offering and always offering
a hyper-accessible desktop experience for everyone. Pro does not change this commitment, in fact — it allows us to continue to improve that entire ambition for everyone.

The Pro features are **opt-in**, will always have a free-usage tier, do not require payment or signup to use, and are **not required to use AnythingLLM**.

The goal with AnythingLLM Pro is to unlock new use cases and features for people who are serious about on-device agentic experiences and want to use AnythingLLM to its full potential.

#### Will there be more free features added to AnythingLLM Desktop?

Of course! Not only will we continue to add more free features to AnythingLLM Desktop, but we will also continue to improve and add more novel features to the free features we already have.

Whatever is free today stays free — forever. Pro is purely additive. Nothing is taken away, ever.

#### Why even have Pro?

AnythingLLM strives to be the best tool on the market for on-device agentic experiences and we are committed to making that real. However, we must make money to be able to continue to build, sustain, and improve AnythingLLM.

If you love AnythingLLM and use it every day, Pro is the best way to show it — and the most direct way to help us keep building.

#### Ready to get started?

- [Get your Pro key](https://docs.useanything.com/pro/getting-started) — Purchase and activate your license in under a minute.
- [Manage your subscription](https://docs.useanything.com/pro/manage-subscription) — View, update, or cancel your plan at any time.

### Magic Beacon

*Highlight text in any application and instantly revise, research, summarize, or ask questions about it — fully local and offline.*

**Source:** https://docs.useanything.com/pro/magic-beacon

> **Tip:**
>
> Magic Beacon is an [AnythingLLM Pro](https://docs.useanything.com/pro/overview) feature with a free daily
> usage tier. It is available in AnythingLLM Desktop for macOS and Windows.
>
> Magic Beacon is only available on AnythingLLM Desktop v1.15.0 and later.

### Magic Beacon

Magic Beacon is an on-screen AI tool that lets you highlight text anywhere on your computer and instantly take action on it — revise, research, summarize, translate, or ask questions — without ever leaving the app you're working in.

[Video](https://webassets.anythingllm.com/magic-feature-promos-desktop/MagicBeacon-promo.mp4)

#### How it works

1. **Highlight text** in any application — an email, a document, a webpage, a code editor, anything.
2. **A small beacon dot appears** near your selection.
3. **Click the dot** (or interact with it) to open the Magic Beacon panel.
4. **Choose a Quick Action** or type a custom prompt to process the highlighted text.
5. **The response appears inline** — you can insert it directly (in editable fields) or copy it to your clipboard.

Magic Beacon uses your local LLM to process everything, so it works fully offline and your data never leaves your machine.

#### Quick Actions

Magic Beacon comes with two categories of configurable Quick Actions that appear when you highlight text:

##### Edit Actions

These appear when you highlight text in **editable fields** (text inputs, text areas, code editors, etc.). The response can be **inserted directly** to replace the selected text.

Default edit actions typically include things like fixing grammar, making text more professional, simplifying language, and more.

##### Static Actions

These appear when you highlight **non-editable text** (web pages, PDFs, rendered documents, etc.). The response can be **copied to clipboard**.

Default static actions typically include summarizing, explaining, translating, and researching the selected text.

##### Customizing Quick Actions

You can fully customize Quick Actions in **Settings** → **Magic Beacon** → **Customize Quick Actions**:

- Add, edit, or remove actions for both Edit and Static categories
- Each action has a **Label** (what you see in the menu) and a **Prompt** (the instruction sent to the LLM along with your highlighted text)
- Reset to defaults at any time

![Magic Beacon Quick Actions configuration](https://docs.useanything.com/_next/image?url=%2Fimages%2Fpro%2Fmagic-beacon-settings.png&w=2048&q=75)

#### Use cases

Magic Beacon shines in workflows where you're constantly switching between reading and acting on text:

- **Writing & editing** — Highlight a paragraph and ask to rephrase, shorten, or make it more formal
- **Research** — Highlight a technical term or passage and ask for an explanation or deeper context with agentic search capabilities
- **Code review** — Highlight a code snippet and ask what it does, or request improvements
- **Email triage** — Highlight an email and get a quick summary or draft a reply
- **Translation** — Highlight text in any language and get an instant translation
- **Learning** — Highlight unfamiliar text and ask questions about it

#### Agent & Chat Modes

Magic Beacon sessions can operate in different modes:

- **Chat** — Simple question and response about the highlighted text
- **Agent** — Uses your configured agent skills, MCPs, and tools for more complex tasks (like generating files, running searches, etc.)

Past sessions show which mode was used and can include generated files and sources.

#### Ignored Apps

If Magic Beacon is distracting in certain applications, you can dismiss it with **"Ignore this app"** from the options menu in the widget. Ignored apps are managed in **Settings** → **Magic Beacon** → **Ignored Apps**, where you can remove apps from the ignore list at any time.

![Magic Beacon Ignore App](https://docs.useanything.com/_next/image?url=%2Fimages%2Fpro%2Fmagic-beacon-ignore.png&w=2048&q=75)

#### Past Beacon Sessions

Every Magic Beacon interaction is saved and viewable in the **Past Beacon Sessions** panel on the settings page. Each session includes:

- The input text and prompt
- The AI-generated output
- Any generated files or sources
- Whether it was a Chat or Agent session

#### Settings & Configuration

Navigate to **Settings** → **Magic Beacon** to configure:

| Setting | Description |
| --- | --- |
| **Enable Magic Beacon** | Toggle the feature on or off |
| **Quick Actions** | Customize the actions available for editable and static text selections |
| **Ignored Apps** | Manage which applications should not trigger Magic Beacon |

#### Platform Requirements

- **macOS**: Requires **Accessibility permission** for text highlighting detection. You'll be prompted to grant this on first use. See [MacOS permissions & Troubleshooting](https://docs.useanything.com/pro/magic-beacon#macos-permissions--troubleshooting) for more details.
- **Windows**: No special permissions required.
- **Linux**: Not currently supported.

#### Privacy

All processing is done on device using your configured LLM provider and model. The highlighted text is sent to your provider for processing — if you're using a local model, nothing ever leaves your machine. If you're using a cloud provider, the text is sent under the terms of that provider's privacy policy.

#### Free Tier & Pro

Magic Beacon includes a daily allowance of free invocations.

With [AnythingLLM Pro](https://docs.useanything.com/pro/overview), Beacon invocations become unlimited. [Get your Pro key](https://docs.useanything.com/pro/getting-started) to remove all daily limits.

#### MacOS permissions & Troubleshooting

Due to how MacOS stores permissions, sometimes just flicking the switch on the Privacy & Security settings window seems to not take effect. In this case, you can try the following:

1. Quit AnythingLLM fully.
2. Open the Privacy & Security settings window and add an entry for AnythingLLM for `Input Monitoring` and `Accessibility` permissions.
3. Restart AnythingLLM.
4. Go to Magic Beacon settings, disable the feature and re-enable it.
5. Now open an application and highlight some text. If the feature is working, you should see a beacon dot appear near the selection by your cursor.

##### Permissions required

- `Input Monitoring` permission is required to detect text highlighting in any application.
- `Accessibility` permission is required to detect text highlighting in any application.

### Magic Echo

*Dictate anywhere on your computer and get back clean, punctuated text — even aware of what's on your screen. Powered by your local models.*

**Source:** https://docs.useanything.com/pro/magic-echo

> **Tip:**
>
> Magic Echo is an [AnythingLLM Pro](https://docs.useanything.com/pro/overview) feature with a free daily
> usage tier. It is available in AnythingLLM Desktop for macOS and Windows.
>
> It is available in AnythingLLM Desktop v1.15.0 and later.

### Magic Echo

Magic Echo is voice-to-text dictation that works in any application on your computer. Speak naturally and your words are transcribed, cleaned up, and inserted right where your cursor is — no copy-pasting, no switching apps. It even uses on-screen context to improve accuracy.

[Video](https://webassets.anythingllm.com/magic-feature-promos-desktop/MagicEcho-promo.mp4)

#### How it works

1. Press the activation shortcut (default: `Option+Z` on macOS, `Alt+Z` on Windows/Linux) to start dictating.
2. Speak naturally — Magic Echo listens and transcribes your speech in real-time.
3. When you stop speaking (or press the shortcut again), the transcribed text is automatically inserted at your cursor position in whatever app you're using.

Magic Echo runs entirely on-device using a local transcription model that is downloaded automatically when you first enable the feature.

#### Two modes of dictation

##### Quick dictation

A short press-and-speak interaction. Magic Echo listens until it detects a pause in your speech, then auto-submits the transcription. The **Silence Detection** setting lets you control how aggressively it detects pauses.

> You can press `Esc` while in quick dictation mode to cancel a quick dictation session.
>
> You can press `Enter` while in quick dictation mode to submit a quick dictation session - useful if you have a loud background keeping the microphone open.

##### Extended dictation

Hold the shortcut for a longer dictation session. This mode is useful for longer-form content where you want to keep speaking without auto-submission interrupting your flow.

> You can press `Esc` while in extended dictation mode to cancel the session without submitting.
>
> You must manually click the "Stop" button in the widget to submit the extended dictation session.

#### Smart Transcription vs. Raw Transcription

Magic Echo offers two processing modes:

- **Smart Transcription** — Your speech is transcribed and then processed by your configured LLM to clean up grammar, add punctuation, fix formatting, and apply context-aware corrections. Smart transcriptions count toward your daily free-tier limit (unlimited with [Pro](https://docs.useanything.com/pro/overview)).
- **Raw Transcription** — Your speech is transcribed directly without any LLM processing. This is faster and does not count toward any usage limits, but the output may include filler words and lack proper punctuation.

You can set your **Default Processing Mode** in settings and use the alternate keybind to quickly switch between modes.

> **Tip:**
>
> If you are doing a smart transcription and for whatever reason it fails to process, we will automatically fall back to the raw transcription and use that instead.
>
> This way, you dont lose what you said and can still review it in the past echoes section.

#### On-Screen Awareness

When enabled, Magic Echo can see what's currently on your screen and use that visual context to improve transcription accuracy. For example, if you're looking at a PDF on your screen and dictating a comment into a Microsoft Teams chat, Magic Echo can use the visible PDF to better understand the context of the comment you're saying **if you mention it** in your dictation.

> **Tip:**
>
> On-Screen Awareness requires your LLM provider to support vision/multi-modal
> models. If your provider doesn't report vision capabilities, this setting will
> be unavailable.
>
> We know that some providers do support vision/multi-modal models, but they don't report it properly. If you're using a provider that is not reporting vision capabilities, you can still use Magic Echo with on-screen awareness disabled. We are working on a solution to this.

#### Voice Commands

Define trigger phrases that instantly paste a predefined snippet when spoken. Voice commands bypass smart processing entirely and **don't count** toward Pro invocations.

For example, you could set up:

- **"PRD Template"** → pastes a markdown template into whatever application you're using
- **"sign off"** → pastes `Best regards,\nYour Name`
- **"boilerplate header"** → pastes a code template

Voice commands are configured in **Settings** → **Magic Echo** → **Voice Commands**.

You can have as many voice commands as you want, and they will all be available to you when you speak. Keep in mind, voice commands should have very clear and distinct names to avoid confusion
they must also be the **exact phrase** you speak to trigger them. AnythingLLM Magic Echo will do some basic fuzzy matching to help you out when it comes to dialect, punctuation, and other variations.

#### Custom Vocabulary

> **Tip:**
>
> Custom vocabulary is only applied to Smart Transcriptions. Raw Transcriptions will not use custom vocabulary.

Add words to help with transcription accuracy — names, technical terms, brand names, or jargon specific to your use case. This is especially useful for uncommon words that the transcription model might not recognize.

Examples: `AnythingLLM`, `GPT-4`, `Kubernetes`, your company name, etc.

#### Settings & Configuration

Navigate to **Settings** → **Magic Echo** to configure:

| Setting | Description |
| --- | --- |
| **Activation Key** | The key used with `Option` (macOS) / `Alt` (Windows/Linux) to activate dictation. Default: `Z` |
| **Default Processing Mode** | Choose Smart or Raw transcription as default |
| **On-Screen Awareness** | Let Magic Echo use visual screen context for better accuracy |
| **Preferred Microphone** | Select which microphone to use for dictation |
| **Silence Detection** | How quickly Magic Echo auto-submits after you stop speaking (Aggressive / Average / Relaxed) |
| **Widget Size** | Adjust the on-screen widget size (Default / Large / Huge / Max) |
| **Voice Commands** | Define trigger phrases that paste predefined snippets |
| **Custom Vocabulary** | Add words to improve transcription accuracy |

![Magic Echo Settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fpro%2Fmagic-echo-settings.png&w=2048&q=75)

#### Past Echoes

Every dictation session is saved and can be reviewed in the **Past Echoes** panel on the settings page. Each session shows:

- The raw transcription
- The processed output (for Smart sessions)
- Any context screenshots used (if On-Screen Awareness was active)
- Which model processed the transcription

#### Platform Requirements

- **macOS**: Requires **Accessibility permission** to insert text into other applications. You'll be prompted to grant this on first use. See [MacOS permissions & Troubleshooting](https://docs.useanything.com/pro/magic-echo#macos-permissions--troubleshooting) for more details.
- **Windows**: No special permissions required.
- **Linux**: Not currently supported.

#### Tips for Magic Echo

##### On screen awareness

When using on screen awareness, you should mention the app name in your dictation. For example, if you're dictating a comment into a Microsoft Teams chat, you should say "Microsoft Teams, comment". This will help Magic Echo understand the context of the comment you're saying.

##### Speeding up dictation

- Usually your first dictation session will slightly slower than subsequent sessions. AnythingLLM keeps the model warm for you so subsequent sessions are much faster but unloads it after a few minutes of inactivity.
- Disabling on screen awareness will speed up dictation significantly since you do not need to process any image data which takes a lot of time compared to raw-text processing.
- Change you default processing mode to Raw Transcription for faster dictation. You lose the "intelligence" of the transcription, but you gain speed and get your raw transcription back faster.

#### Privacy

For Raw Dictations, all processing is done on device using our internal transcription pipeline - the same one used for the [Meeting Assistant](https://docs.useanything.com/meeting-assistant/introduction). Nothing is sent to the cloud.

When using Smart Transcriptions, the transcribed text and screenshots are sent to your provider for processing — if you're using a local model, nothing ever leaves your machine. If you're using a cloud provider, the text and screenshots are sent under the terms of that provider's privacy policy.

#### Free Tier & Pro

Magic Echo includes a daily allowance of free **Smart Transcriptions**. Raw transcriptions and Voice Commands are always free and unlimited.

With [AnythingLLM Pro](https://docs.useanything.com/pro/overview), Smart Transcriptions become unlimited. [Get your Pro key](https://docs.useanything.com/pro/getting-started) to remove all daily limits.

#### MacOS permissions & Troubleshooting

Due to how MacOS stores permissions, sometimes just flicking the switch on the Privacy & Security settings window seems to not take effect. In this case, you can try the following:

1. Quit AnythingLLM fully.
2. Open the Privacy & Security settings window and add an entry for AnythingLLM for `Accessibility` and `Screen Recording` permissions.
3. Restart AnythingLLM.
4. Go to Magic Echo settings, disable the feature and re-enable it.
5. Now open an application and start a dictation session. If the feature is working, you should see a transcription appear within a few milliseconds (depending on your hardware, model, provider, etc.)

### Magic Tab

*Inline text completions as you type in any application — press Tab to accept. Powered by your own LLM, fully on-device.*

**Source:** https://docs.useanything.com/pro/magic-tab

> **Tip:**
>
> Magic Tab is an [AnythingLLM Pro](https://docs.useanything.com/pro/overview) feature with a free daily
> usage tier. It is available in AnythingLLM Desktop for macOS and Windows.
>
> Magic Tab is only available on AnythingLLM Desktop v1.15.0 and later.

### Magic Tab

Magic Tab suggests inline text completions that are **context aware** to what you are actively working on as you type in any application on your computer.

It is more than simple autocomplete based on what you type! As you write, Magic Tab predicts what comes next and shows a ghost-text suggestion — press **Tab** to accept, or just keep typing to ignore it.

[Video](https://webassets.anythingllm.com/magic-feature-promos-desktop/MagicTab-promo.mp4)

#### How it works

1. **Start typing** in any application — an email, a document, a chat app, a code editor, anything.
2. **Pause briefly** — Magic Tab detects the pause and generates a suggestion based on what you've typed and the surrounding context.
3. **A ghost-text suggestion appears** inline, styled as a subtle overlay near your cursor.
4. **Press Tab** to accept the suggestion, or keep typing to dismiss it.

Magic Tab runs entirely on-device using a local model or the system provider and model of your choice. Suggestions are generated only when you pause typing, and only accepted completions count toward usage.

#### Suggestion Modes

##### Typeahead completions

As you type and pause, Magic Tab generates a suggestion that continues your current thought. The delay before a suggestion appears is configurable via the **Typing Pause Delay** setting.

##### On-Focus Suggestions

> **Tip:**
>
> To save on compute or cloud costs for if you are using a cloud provider,
> **this setting is disabled by default** even though it is very cool!

When enabled, Magic Tab generates a suggestion as soon as you click into a text field — even before you start typing. This can feel proactive and helpful for starting a new paragraph or reply. The suggestion is dismissed as soon as you begin typing.

##### Suggestion Chaining

When enabled, accepting a suggestion immediately generates another one, so you can keep pressing Tab to continue writing a full passage. When disabled, Magic Tab waits until you start typing again before generating the next suggestion.

#### Settings & Configuration

Navigate to **Settings** → **Magic Tab** to configure:

| Setting | Description |
| --- | --- |
| **Enable Magic Tab** | Toggle the feature on or off |
| **Model** | Choose the model for generating suggestions (see below) |
| **Completion Suggestion Length** | How much text to suggest at once — Short (faster), Medium, or Lengthy (full sentences) |
| **Typing Pause Delay** | How long you must pause typing before a suggestion appears. Lower values are more responsive but generate more unused suggestions |
| **Suggestion Chaining** | Automatically generate a new suggestion after accepting one |
| **On Focus Suggestion** | Generate a suggestion when clicking into a text field |
| **Animated Border** | Show a gradient border around the focused input while generating a suggestion |
| **Personalization** | Custom instructions that guide suggestion style (e.g., "Always write in British English" or "Keep a formal tone") |
| **Ignored Apps** | Applications where Magic Tab should not suggest completions |

![Magic Tab Settings](https://docs.useanything.com/_next/image?url=%2Fimages%2Fpro%2Fmagic-tab-settings.png&w=2048&q=75)

#### Model Selection

Magic Tab can use different models for generating suggestions. You can choose based on your hardware and preference:

| Model Tier | Description |
| --- | --- |
| **Default** | Uses your system model — no extra download required |
| **Lightweight** | Fastest responses, lowest memory usage |
| **Balanced** | Better quality suggestions with moderate resource usage |
| **Intelligent** | Best quality suggestions, slower and more memory-intensive |

New models are downloaded automatically in the background when selected.

> **Tip:**
>
> **Tip:** Start with your default system model to get a feel for Magic Tab,
> then move up to Balanced or Intelligent if you want higher-quality
> suggestions.

#### Personalization

Add custom instructions (one per line) that guide how Magic Tab writes suggestions. These instructions are included as context every time a suggestion is generated.

Examples:

- `Always write in British English`
- `Keep a formal, professional tone`
- `Use technical language appropriate for a software engineering audience`
- `Prefer short, concise sentences`

#### Ignored Apps

If Magic Tab suggestions are distracting in certain applications (for example, a terminal or a game), add those apps to the ignore list in **Settings** → **Magic Tab** → **Ignored Apps**.

#### Typing Pause Delay

The typing pause delay controls how responsive Magic Tab is. A shorter delay (e.g., 500ms) means suggestions appear quickly after you stop typing, but may generate many suggestions you don't use — wasting GPU compute and draining battery. A longer delay (e.g., 1500ms) feels more natural but may slow down the suggestion flow.

> **Warning:**
>
> Very low delay values will generate many suggestions that go unused, wasting
> GPU compute and draining battery. **750ms is recommended** for most users.

#### Platform Requirements

- **macOS**: Requires **Input Monitoring** and **Accessibility** permissions to detect keystrokes and insert text. You'll be prompted to grant these on first use. A restart of AnythingLLM may be needed after granting permissions. See [MacOS permissions & Troubleshooting](https://docs.useanything.com/pro/magic-tab#macos-permissions--troubleshooting) for more details.
- **Windows**: No special permissions required.
- **Linux**: Not currently supported.

#### Privacy

All suggestion generation is done on device using your configured LLM provider and model. The text context around your cursor is processed by your provider to generate suggestions — nothing is sent to the cloud (unless you've explicitly configured a cloud LLM provider).

#### Free Tier & Pro

Magic Tab suggestions are always generated for free. **Only accepted completions** (when you press Tab) count toward your daily free-tier limit.

With [AnythingLLM Pro](https://docs.useanything.com/pro/overview), accepted completions become unlimited. [Get your Pro key](https://docs.useanything.com/pro/getting-started) to remove all daily limits.

#### MacOS permissions & Troubleshooting

Due to how MacOS stores permissions, sometimes just flicking the switch on the Privacy & Security settings window seems to not take effect. In this case, you can try the following:

1. Quit AnythingLLM fully.
2. Open the Privacy & Security settings window and add an entry for AnythingLLM for `Accessibility`, `Input Monitoring`, and `Screen Recording` permissions.
3. Restart AnythingLLM.
4. Go to Magic Tab settings, disable the feature and re-enable it.
5. Now open an application and start typing. If the feature is working, you should see a suggestion appear within a few milliseconds (depending on your hardware, model, provider, etc.)

An easy way to really test is to enable "On Focus Suggestion" with Animated Border enabled and go to a website or app and click into a text field. If the field border highlights, then Magic Tab is working and will do typeahead suggestions as you type.

##### Permissions required

- `Accessibility` permission is required to grab context from the active application.
- `Input Monitoring` permission is required to insert text into the active application as well as detect when you stop typing.
- `Screen Recording` permission is required **only** if you have On-Focus Suggestions enabled.

### Managing Your Subscription

*How to view, update, or cancel your AnythingLLM Pro subscription and manage your license key.*

**Source:** https://docs.useanything.com/pro/manage-subscription

All AnythingLLM Pro subscriptions are managed through your Mintplex Labs account dashboard. From there you can update payment methods, view billing history, or cancel your plan.

#### Viewing Your License Status

In AnythingLLM Desktop, go to **Settings** → **AnythingLLM Pro**. If your license is active, you'll see:

- A green **Pro License Active** badge
- A masked display of your current key
- A **Last verified** timestamp showing when your license was last validated
- A link to **Manage Subscription**

![AnythingLLM Pro settings page](https://docs.useanything.com/_next/image?url=%2Fimages%2Fpro%2Fdesktop-pro-active.png&w=2048&q=75)

#### Managing Your Subscription Online

Click **Manage Subscription** from the Pro settings page, or visit [my.mintplexlabs.com/dashboard](https://my.mintplexlabs.com/dashboard) directly. From your dashboard you can:

- **Update your payment method**
- **View billing history and invoices**
- **Change your plan**
- **Cancel your subscription**

#### Removing Your License Key

If you need to remove your license key from a device (for example, when switching to a new computer), click the **trash icon** next to your active license in **Settings** → **AnythingLLM Pro**.

> **Warning:**
>
> Removing your license key will immediately revert all Pro features to their
> free-tier daily limits on that device. You can re-enter the key at any time to
> restore Pro access.

![AnythingLLM Pro settings page](https://docs.useanything.com/_next/image?url=%2Fimages%2Fpro%2Fdesktop-pro-active.png&w=2048&q=75)

#### What happens if my subscription expires?

If your subscription lapses or is cancelled:

- Your license key will fail validation on the next periodic check.
- All Magic features revert to their **free-tier daily limits** — you do not lose access to the features, only unlimited usage.
- You can re-subscribe at any time and use the same or a new license key to restore Pro.

#### Invalid or Expired License Keys

If your key is shown as **invalid or expired** in the Pro settings page:

1. **Check your subscription status** at [my.mintplexlabs.com/dashboard](https://my.mintplexlabs.com/dashboard) to confirm your plan is active.
2. **Re-enter your key** — click "Remove license key" and paste it again to force a fresh validation.
3. **Contact support** if the issue persists — reach out to [team@mintplexlabs.com](mailto:team@mintplexlabs.com).

#### Frequently Asked Questions

##### Can I use my license key on multiple devices?

Yes — we don't enforce device limits. Use your license key on as many devices as you want. Just keep it secret and don't share it with others.

We don't track or log your usage, but we may reach out if we suspect abuse.

##### Is my data sent anywhere when using Pro?

No. Pro simply unlocks unlimited usage of features that already run entirely on your device. Your data never leaves your machine — Pro does not change the privacy model of AnythingLLM in any way.

##### Do Pro features use my own LLM?

Yes, they use whatever LLM you have configured in the AnythingLLM settings.

##### Do Pro features work offline?

Yes, but keep in mind that the license key must be validated periodically to ensure it is still active. If you are offline for more than a continuous 48 hours, your license key will be considered invalid and you will need to re-enter it or reconnect to the internet to restore Pro features.

> The license key server is **license.anythingllm.com** if you need to permit it in your firewall.

If you need an entire airgapped experience with a license for IT or compliance reasons - you can contact us at [team@mintplexlabs.com](mailto:team@mintplexlabs.com) to get a lifetime license key.

##### What is the refund policy?

We do not offer refunds for any reason. If you are not satisfied with the product, you can cancel your subscription at any time.

You can review the subscription terms and conditions at [my.mintplexlabs.com/anythingllm-pro-terms](https://my.mintplexlabs.com/anythingllm-pro-terms).


---

## Beta Preview Features

### AnythingLLM Beta Previews

*Access cutting-edge beta previews and features of AnythingLLM*

**Source:** https://docs.useanything.com/beta-preview/overview

![AnythingLLM Beta Previews](https://docs.useanything.com/_next/image?url=%2Fimages%2Fbeta-preview%2Fheader-image.png&w=3840&q=100)

### What are beta previews?

Beta previews of AnythingLLM are versions *or* features of AnythingLLM that are either:

- In active development
- Unstable or untested
- Features that are not fully completed, but are looking for feedback from the community.

### Types of beta previews

There a few ways we may publish beta previews of AnythingLLM:

- As a fully separated Docker image
- A special publication of the [desktop application](https://docs.useanything.com/installation-desktop/macos)
- A hidden feature already present in the AnythingLLM Application

### How can I access a beta preview or feature?

[![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fbeta-preview%2Ffeature-preview.png&w=3840&q=100)Enable feature previews→](https://docs.useanything.com/beta-preview/enable-feature)

### AI Computer use

*Enable an AI to autonomously use your computer to complete tasks*

**Source:** https://docs.useanything.com/beta-preview/active-features/computer-use

> **Caution:**
>
> **Caution!** Allowing an AI to use your computer is a powerful feature. It comes with inherent risks and should be used with caution.
>
> **NEVER** allow an AI to use your computer unsupervised. You should always be present when the AI is using your computer.
>
> *The following risks are relevant to any AI using your computer, not just AnythingLLM*
>
> - **Data loss:** The AI could in theory delete files via the UI.
> - **Security risks:** The AI could access sensitive files or data on your computer
> - [Read more about the risks and how to mitigate them](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)

### About Computer use

The **Computer use** feature for AnythingLLM is an experimental feature that allows you to enable an AI to use your computer to complete tasks.

This feature is powered by Anthropic's Claude 3.5 Sonnet model and is an implementation of Anthropic's [Computer use API](https://docs.anthropic.com/en/docs/build-with-claude/computer-use).

Currently, the feature is in beta while we work on ways to bring this same functionality to **locally hosted open-source models**.

#### Known limitations

- **Model:** The Anthropic model that enables computer use is fixed to `claude-3-5-sonnet` and cannot be changed. We also currently don't support BedRock or Vertex hosted providers.
- **Guardrails:** This feature also has guardrails that may prevent it from doing specific tasks, like reading emails, writing content, or opening applications that could be considered harmful.
- **Accessibility:** (MacOS only) This feature requires the `Accessibility` and `Screen Recording` permissions to be enabled for AnythingLLM.
- **Primary Display:** This feature currently only works on the primary display.

#### What can I do with this?

> **Note:**
>
> **Note:** The Anthropic model that enables computer use is fixed to `claude-3-5-sonnet` and cannot be changed. We also currently don't support BedRock or Vertex hosted providers.
>
> It is also important to note that the model is not perfect and may not always behave as expected - you can abort the computer use session if things go wrong or the AI is not behaving as expected.
> You can do this by clicking the pause icon in the UI, pressing `CMD+K` or `CTRL+K`, or by quitting the AnythingLLM application.
>
> This feature also has guardrails that may prevent it from doing specific tasks, like reading emails, writing content, or opening applications that could be considered harmful.

Computer use is a powerful feature that can be used to complete complex tasks using the power of the host machine and its local files, applications, and more.

Some example tasks you can complete include:

- **Browsing the web** - The AI can browse the web to find information, research topics, and even post to social media (sometimes)
- **Searching files** - The AI can search your file system for specific files
- **Running applications** - The AI can open applications and navigate GUIs

#### Permissions

*This section is relevant to users running AnythingLLM Desktop on MacOS*

Certain permissions are required to use computer use. Please follow the instructions below to enable the necessary permissions.

##### Accessibility

In order to use the computer use feature, you need to have the `Accessibility` permissions enabled for AnythingLLM on your system.

This is done by opening the `Security & Privacy` settings on MacOS and clicking on the `Privacy` tab. From there, find `Accessibility` on the left and click on the `+` button to add AnythingLLM.

This will allow AnythingLLM to control your computer's mouse and keyboard.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fbeta-preview%2Fcomputer-use%2Faccessibility.png&w=3840&q=100)

##### Screen recording

In order to use the computer use feature, you need to have the `Screen Recording` permissions enabled for AnythingLLM on your system.

This is done by opening the `Security & Privacy` settings on MacOS and clicking on the `Privacy` tab. From there, find `Screen Recording` on the left and click on the `+` button to add AnythingLLM.

This will allow AnythingLLM to take screenshots of your display.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fbeta-preview%2Fcomputer-use%2Fscreen-recording.png&w=3840&q=100)

#### Enable the feature

First, you need to enable the feature from the feature preview management page.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fbeta-preview%2Fcomputer-use%2Ftoggle.png&w=3840&q=100)

#### Configure the feature with your API key

Before you can use the feature, you need to configure it with your Anthropic API key to be able to use the feature. Do this by clicking the `Manage OS Agent Settings` link in the feature preview management page.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fbeta-preview%2Fcomputer-use%2Fconfig.png&w=3840&q=100)

#### How to use the computer use feature

> **Note:**
>
> **Note:** Be ready at any time to abort the computer use session if things are
> not going as expected. You can do this by clicking the pause icon in the UI,
> pressing `CMD+K` (MacOS) or `CTRL+K` (Windows/Linux), or by quitting the
> AnythingLLM application.

Once you have enabled the feature and configured it with your API key, you can invoke computer use by typing in `@os` in the AnythingLLM chat along with a prompt.

Shortly after, you should see some outputs in the UI indicating that the OS agent is starting up as well as an additional popup (lower-left or lower-center of display) allowing you to control or halt the OS agent.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fbeta-preview%2Fcomputer-use%2Finvoke.png&w=3840&q=100)

##### OS Agent control popup

Once the OS agent is running, AnythingLLM will minimize to get out of the way and you should see a popup in your display allowing you to control or halt the OS agent.

Clicking the Pause button will halt the OS agent immediately. The same can be done by pressing `CMD+K` (MacOS) or `CTRL+K` (Windows/Linux).

You can also quit the AnythingLLM application which will halt the OS agent as well. You can drag the popup around to get it out of the way, but this may interfere with the OS agent's ability to control your mouse position if needed.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fbeta-preview%2Fcomputer-use%2Fpopup.png&w=1080&q=100)

##### OS Agent output

The OS agent will output its actions and any relevant information to the AnythingLLM chat as it executes. These actions are currently **not** saved or stored your workspace's chat history.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fbeta-preview%2Fcomputer-use%2Flogging.png&w=3840&q=100)

#### What about open-source models?

We are actively working on bringing this same functionality to locally hosted open-source models. While everything for local models is working, the main blocker is finding a vision model that is capable of understanding a UI image and translating that into an action in addition to knowing the proper x,y coordinates to click.

If you are interested in helping us work on this, please reach out to us on [Discord](https://discord.gg/Dh4zSZCdsC) and we can talk about how you can help!

### Automatic document sync

*Access the automatic remote and local document sync beta preview*

**Source:** https://docs.useanything.com/beta-preview/active-features/live-document-sync

> **Warning:**
>
> **Caution!** The following list are concerns when using the **Automatic Document Sync** feature preview.
>
> - Increased Embedder use *or* cost if using third party embedder
> - Corruption of local database
> - Corruption of local vector database

### About Automatic document sync

The **Automatic Document Sync** feature for AnythingLLM allows you to "watch" a document for active changes. When changes are detected the file will be re-embed and all workspaces using this file will automatically be updated.

This enables you to reference a document and have its content consistently updated so answers are always accurate to the original source.

#### Scope of documents

##### Docker

- Any website link
- Any file collected via a **Data connector** *(eg: Confluence, Github, and YouTube)*
- Manually uploaded files **are not synced** since the browser cannot read from your computer

##### Desktop

- **[Any manually uploaded local file](https://docs.useanything.com/beta-preview/active-features/live-document-sync#how-does-document-sync-work-with-local-files)**
- Any website link
- Any file collected via a **Data connector** *(eg: Confluence, Github, and YouTube)*

#### Enable the feature

First, you need to enable the feature from the feature preview management page.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fbeta-preview%2Flive-document-sync%2Fenable.png&w=3840&q=100)

#### How to watch a file for changes

Once enabled, you will see an "eye" icon on an **currently embedded file**. You currently *cannot* watch an entire directory. If this option on the row is not available - this file is not available for watching.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fbeta-preview%2Flive-document-sync%2Fwatch.png&w=3840&q=100)

If you add the same file in any other workspace you will notice the file is automatically watched. If you delete the document totally from the system, it will automatically be unwatched.

#### Manage and observe watched files easily

Any watched file is checked **hourly** if it is stale. A *stale* file is any file that has not had its content refreshed in the last *7 days*.

**In the future, you will be able to force-refresh a document or change its default stale time**.

![](https://docs.useanything.com/_next/image?url=%2Fimages%2Fbeta-preview%2Flive-document-sync%2Fmanage.png&w=3840&q=100)

### Summary and notes

Watching a file with AnythingLLM's Automatic Document Sync will periodically fetch and replace all embeddings of that document across all of your active workspace.

This requires use of the connected embedder and therefore you may want to only watch a few files for resource reasons or cost concerns.

Currently, if you close the application or docker container, the watched files will not be synced as the background worker does not run if the process is killed.

### Troubleshooting

If you are having issue with the document sync feature simply disable the toggle for the feature and it will not run any background workers while using AnythingLLM or on reboots.

Please ping the core team with a GitHub issue or Discord message for any questions or bug reports.

#### How does document sync work with local files?

> **Note:**
>
> While in beta, you should use this feature with files that update frequently. Otherwise, it wont help much!
>
> *Reminder:* this is only available on AnythingLLM Desktop

On AnythingLLM Desktop you can now "watch" any locally uploaded file! Functionally, this works the exact same as watching content that comes from a website or elsewhere, but there
are some tips and things to know before watching every locally uploaded file.

##### Only watch relevant files!

While you can watch any local files it only really makes sense to use this feature on files that can or do change a lot. For example, PDF files don't change that often.

##### How often does it sync?

Files will be checked for new content every **10 minutes**. The app must be open for this to occur as AnythingLLM does not minimize to the tray or taskbar when closed. If changes are found, the document content and all workspaces will be updated automatically.

##### How can I check it synced?

Open the feature dashboard and see when the last sync was. Currently there is no easy way to verify the content synced - it will be live soon.

##### How can I change how often documents sync?

You cannot modify the sync time currently.

##### What if I move or delete the original document from where it was during upload?

AnythingLLM cannot and does not know where a file is relocated should you move it. On the next interval sync the document will be marked as "Not Found" and it will
become automatically unwatched. The existing content and embeddings will not change. You cannot update its current location reference.

##### Why can't I watch a file I already uploaded?

Prior to v1.5.9 the required changes to track file locations did not exist. Any files uploaded prior are not available to be watched and should be
uploaded & embedded again.

### Enable feature previews

*Learn how to enable feature previews of AnythingLLM*

**Source:** https://docs.useanything.com/beta-preview/enable-feature

> **Note:**
>
> **HEADS UP!** Feature previews are **not stable**. Please read on to
> understand the dangers of using a beta feature before using one.

### Understanding the implications of beta previews

While we take great care to craft features carefully we also want to proactively offer non-standard features to users of AnythingLLM when in development or when we are looking for feedback.

When possible, we will proactively alert you to any particular dangers of a specific feature.

### Possible dangers of using a beta feature

- Partial or full data loss of AnythingLLM's local database, source files, stored documents, or datastores
- Increased LLM, Embedder, or third party provider usage
- Increased costs for third-party providers should they be used as a provider for an LLM, Embedder, or VectorDatabase
- Increase resource usage on the device
- Corruption of local DB or vector database
- Unhandled bugs, exceptions, and crashes of AnythingLLM

### How to enable feature previews

> **Tip:**
>
> If you follow this procedure and nothing happens then this means that there
> are no active previews available for your version of AnythingLLM.

To enable feature previews in AnythingLLM in *any* form (Docker, Desktop, Hosted) open the settings page by clicking on the "wrench" icon on the left sidebar.

Next, press and hold the `Command` (Mac) or `Control` (Windows/Linux) key on your keyboard for 3 seconds. You should see an alert that Experimental Features have been enabled.

You can now access the feature management page and after understanding and accepting the warning modal you can now manage experimental features.


---

## Troubleshooting

### 'Fetch failed' error on embed

*So you got an 'Fetch failed' error on embed. Here's how to fix it.*

**Source:** https://docs.useanything.com/fetch-failed-on-upload

#### What is this?

When you try to embed a file in AnythingLLM, you might see a "Fetch failed" error. There are a few reasons why this might happen and all of them are fixable quite easily and are all related to the machine running AnythingLLM or firewall permissions.

Below are the most common fixes for this error ordered from the **most** likely to the **least** likely.

#### Check if the machine running AnythingLLM is blocking downloads from HuggingFace or AWS.

This error applies to you if:

- You are using the default AnythingLLM embedder model
- You may have a firewall blocking downloads from HuggingFace or AWS either by default or because you have a custom firewall installed by whoever manages your network.

##### Why is this happening?

This error happens when the machine running AnythingLLM is blocking downloads from HuggingFace or AWS. We do not pre-bundle the embedding model into the app, so the machine needs to download the model for its very first use. After it is downloaded, the model is cached so it doesn't need to be downloaded again.
Your embeddings for the default embedder model are always done locally, this is just a problem with downloading the model GGUF and tokenizer.

##### How to fix it?

1. Check your [storage folder](https://docs.useanything.com/installation-desktop/storage#where-is-my-data-located) and see if a folder named `models/Xenova` exists.

- If this folder does not exist, it's likely that the machine is blocking downloads from HuggingFace or AWS.
- Unblock the `huggingface.co` and `api.huggingface.co` domains on your machine.
- Try embedding again.
- Unblock this origin: `https://cdn.anythingllm.com/support/models/`
- Try embedding again.

Still not working? Try the next solution.

#### Windows Visual C++ Redistributable

This error applies to you if:

- You are using the default AnythingLLM embedder model
- You are on Windows

##### Why is this happening?

This error happens when the machine running AnythingLLM is missing the Windows Visual C++ Redistributable. This is a library that is required to run the model.

##### How to fix it?

1. Download the [Visual C++ Redistributable v14.x](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version) and install it.
2. Try embedding again.

Still not working? Try the next solution.

#### Your CPU is not supported

This error applies to you if:

- You are using the default AnythingLLM vector database

##### Why is this happening?

[LanceDB](https://lancedb.github.io/lancedb/) is a vector database that is used to store the embeddings. It is the default vector database for AnythingLLM.

Your CPU is not supported if you are using a CPU that does not support AVX2.

##### How to fix it?

1. Use a machine with a supported CPU.
2. Use another vector database provider for vector storage. We support most of the popular vector databases.

### Import an LLM into AnythingLLM

*How to import an LLM into AnythingLLM*

**Source:** https://docs.useanything.com/import-custom-models

### Importing custom LLMs into AnythingLLM

AnythingLLM allows you to easily load into any valid `GGUF` file and select that as your LLM with zero-setup. Please only use text based LLMs
for this process. Embedder models will not function in this capacity.

#### Import model into AnythingLLM.

> **Note:**
>
> **Desktop only!**
>
> This LLM provider is only available in the desktop version. If you are using the browser based version you will need to import the model into your local LLM provider. We recommend
> Ollama or LMStudio.

Importing any `GGUF` file into AnythingLLM for use as you LLM is quite simple. On the LLM selection screen you will see an `Import custom model` button.

Clicking this button will open a file picker. Simply select your GGUF file and wait 2-3 minutes while the model is imported. Now you can select and save this
model as your LLM!

  
![](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffine-tuning%2Flocal-llm.png&w=3840&q=100)

After import you should see your model displayed.

  
![](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffine-tuning%2Flocal-llm-loaded.png&w=3840&q=100)

#### How to import into Ollama

Importing to Ollama is also quite simple and we provide instructions in your download email on how to accomplish this. Please refer to this
video segment.

[Embedded video/content](https://www.youtube.com/embed/1B50IDUl5D4?si=2SdTcSFxMzbQiD8e&start=710)

#### How to import into LMStudio

Importing to LMStudio is even more simple to load. Simply drag the instructions + `GGUF` folder into the LMStudio model location. Please refer to this
video segment.

[Embedded video/content](https://www.youtube.com/embed/1B50IDUl5D4?si=lVYaAlLHxFuonepb&start=1050)

### Manual QNN Model Download

*Sometimes you need to download the NPU models manually due to connection issues.*

**Source:** https://docs.useanything.com/manual-qnn-model-download

#### What is this?

Sometimes you need to download the NPU models manually due to connection issues. This is a manual process but it's quite simple
to do and should only be done if you are unable to download the models automatically from selecting them in the GUI on the desktop app.

#### Download the models

You can download the models from the following links:

- [Llama-3.2-3B-Chat (8k context)](https://cdn.anythingllm.com/support/qnn/llama_v3_2_3b_chat_8k.zip)
- [Llama-3.2-3B-Chat (16k context)](https://cdn.anythingllm.com/support/qnn/llama_v3_2_3b_chat_16k.zip)
- [Llama-3.1-8B-Chat (8k context)](https://cdn.anythingllm.com/support/qnn/llama_v3_1_8b_chat_8k.zip)
- [Phi 3.5-mini-instruct (4k context)](https://cdn.anythingllm.com/support/qnn/phi_3_5_mini_instruct_4k.zip)

#### Once your zip file is downloaded

1. Open the `models/QNN` folder (or create it if it doesn't exist) in the [desktop storage folder](https://docs.useanything.com/installation-desktop/storage).
2. Move the zip file into this folder.
3. Extract the zip file.

You should now have a folder named with the same name as the zip file and inside it will be the model files.

```
### Example folder structure
models/QNN/
└── llama_v3_2_3b_chat_8k/
    ├── genie_config.json
    ├── htp_backend_etc.bin
    ├── related-model-bin-file.bin
    └── tokenizer.json
```

3. Restart the desktop app. Now the model should be available in the GUI to be selected and used for inference.

### General Help

*General help for connecting to Ollama*

**Source:** https://docs.useanything.com/ollama-connection-troubleshooting

Connecting to Ollama is a very simple process, but sometimes things can appear to not being working depending on if you are using the
AnythingLLM Desktop version or running AnythingLLM via Docker.

In general, all AnythingLLM instances just need a valid URL to connect to Ollama running anywhere, however there can be some nuances depending on how you are running AnythingLLM or Ollama - in any case, all that is needed is a reachable URL to connect to Ollama.

The most common issue people run into is trying to use `localhost` or `127.0.0.1` to connect to Ollama running on their local machine when running AnythingLLM via Docker - see the [Troubleshooting (Docker)](https://docs.useanything.com/ollama-connection-troubleshooting#troubleshooting-docker) section for how to fix this.

#### General Troubleshooting (Desktop & Docker)

On both the Desktop and Docker versions of AnythingLLM, the Ollama URL is automatically detected *if we can detect it*.
If the Ollama URL is not detected, you will need to manually set the Ollama URL in the AnythingLLM settings.

The list of automatically detected URLs is as follows:

- `http://127.0.0.1:11434`
- `http://host.docker.internal:11434`
- `http://172.17.0.1:11434`

If your Ollama URL is not detected because it is not in the list above, you will need to manually set the Ollama URL in the AnythingLLM settings - which will be shown in the UI for you to modify.

##### Ensure Ollama `server` is Running

Before attempting any fixes or URL changes, verify that Ollama is running properly on your device:

1. Open your web browser and navigate to `http://127.0.0.1:11434`
2. You should see a page similar to this:

![Ollama running in background](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffaq%2Follama-models-not-loading%2Follama-running.png&w=3840&q=100)

If you don't see this page, troubleshoot your Ollama installation and ensure that it is running properly before moving forward as well as make sure you run the `ollama serve` command.
Most of the time, Ollama will automatically start the server when ollama is running.

> **Note:**
>
> Running `ollama run model-name` will not start the server - this is only for running models in your command line and you will not be able to use the Ollama API with this command.

#### Troubleshooting (Docker)

If you are running AnythingLLM via Docker and you are trying to connect to Ollama running locally on your machine.

If you are seeing no models loaded in AnythingLLM or getting error responses from Ollama - 100% of the time this is beacause you are using the wrong URL in the connection in AnythingLLM.

##### `localhost` and `127.0.0.1` do not work on Docker.

On Docker, `localhost` and `127.0.0.1` are **not valid URLs** for the Docker container Ollama connection in AnythingLLM because both of these refer to the *container* network and **not the host machine**.

To fix this, you can use the `host.docker.internal` (Windows/MacOS) or `172.17.0.1` (Linux) URLs to connect to the host machine from the Docker container with the same port (default `11434`).

Running Docker on Windows or MacOS ([available since Docker version 18.03](https://docs.docker.com/desktop/features/networking/#i-want-to-connect-from-a-container-to-a-service-on-the-host)):

```
http://localhost:11434 => http://host.docker.internal:11434
http://127.0.0.1:11434 => http://host.docker.internal:11434
```

Running Docker on Linux:

```
http://localhost:11434 => http://172.17.0.1:11434
http://127.0.0.1:11434 => http://172.17.0.1:11434
```

#### Troubleshooting (Remote Ollama)

If you are running AnythingLLM via Docker and are trying to connect to Ollama running on another machine the underlying principle is the same where the Ollama URL is the IP address of the machine running Ollama.

> **Note:**
>
> In the case of a remote Ollama, the Ollama URL is the IP address of the machine running Ollama and it is **your responsibility** to ensure that the IP address is correct, your firewall rules are correct, and that the machine is running ollama.
> There is no way for AnythingLLM to automatically detect the IP address of the machine running Ollama.

#### AnythingLLM Cloud + Local Ollama

You **cannot** connect to Ollama running on your local machine when using AnythingLLM Cloud. This would require you to expose your local machine to the internet long-term via a service like [ngrok](https://ngrok.com/) which is **not recommended** and **not secure**.

While it is possible, we do not recommend it and it is your discretion to do so if you understand the security implications of SSH tunneling your local machine to the internet. We will not provide support for any issues related to exposing your local machine to the internet.


---

## Project Info

### Contribute

*Contribute to AnythingLLM*

**Source:** https://docs.useanything.com/contribute

![AnythingLLM Contribute](https://docs.useanything.com/_next/image?url=%2Fimages%2Fhome%2Fcontribute.png&w=3840&q=100)

### Contributing

We welcome and appreciate any contributions from the community to help improve AnythingLLM and this Documentation.

#### How to Contribute

##### Create Issues

If you encounter any bugs, have suggestions for new features, or want to discuss improvements, please create an issue on our GitHub repository.

Clearly describe the problem or enhancement you're proposing, and our team will review it promptly.

##### Pull Requests (PR)

Contributions through Pull Requests are highly encouraged.

Whether it's fixing a bug, implementing a new feature, or improving documentation, your PRs are valuable to us.

##### Tutorials

Share your knowledge and expertise by creating tutorials for AnythingLLM.

Tutorials can help users understand the project better and learn how to use its features effectively.

##### Engage on Discord

Join our Discord community to discuss ideas, seek help, and collaborate with other contributors and users.

Engaging on Discord is a great way to stay updated with project developments and connect with the community.

#### Getting Started

If you're new to contributing to open source projects or to AnythingLLM specifically, here's how you can get started:

##### Familiarize Yourself:

Take some time to understand the project's goals, architecture, and existing codebase. You can explore our GitHub repository and documentation to get acquainted.

##### Pick an Issue:

Browse through our GitHub issues and look for tasks which you think you can solve.

##### Reach Out:

If you need assistance or have any questions, don't hesitate to ask for help on Discord or in the comments of the GitHub issue you're working on.

We're here to support you throughout the contribution process.

##### Submit Your Contribution:

Once you've made your changes, submit a Pull Request on GitHub. Be sure to include a clear description of your changes and any relevant details.

Thank you for considering contributing to AnythingLLM. Your support helps make this project better for everyone!

#### Quick Links

[![AnythingLLM Github Issues](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Fintroduction%2Fheader-image.png&w=3840&q=100)AnythingLLM Github→](https://github.com/Mintplex-Labs/anything-llm/issues)[![AnythingLLM Github Issues](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Fsupport%2Fgithub.png&w=3840&q=100)AnythingLLM Docs Github→](https://github.com/Mintplex-Labs/anythingllm-docs/issues)[![AnythingLLM Discord Community](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Fsupport%2Fdiscord.png&w=3840&q=100)Discord Community Invite→](https://discord.gg/Dh4zSZCdsC)

### Roadmap

*Feature & product roadmap for AnythingLLM Docker & Desktop*

**Source:** https://docs.useanything.com/roadmap

At AnythingLLM, we're dedicated to making the most advanced LLM application available to everyone. We want to empower everyone to be able leverage LLMs for their own use for both non-technical and technical users.

With the community's help, we're making progress towards our goals and this roadmap is a guide for what we're working on and what we plan to work on.

This roadmap is not set in stone and is subject to change. We welcome any feedback and suggestions from the community as that is what ultimately drives the product roadmap.

**This is for tracking high-level features. Other tracking is done via our [GitHub issues](https://github.com/mintplex-labs/anything-llm/issues).**

---

- = Completed
- [~] = In Progress
- = Planned

*we are working on a public 2026 roadmap and will update this page soon*

### Support

*Support for AnythingLLM*

**Source:** https://docs.useanything.com/support

![AnythingLLM Support](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Fsupport%2Fheader-image.png&w=3840&q=100)

##### Need a hand? No problem! You can get help in three different ways.

###### 1. GitHub Issues:

Feel free to open an issue on the AnythingLLM [GitHub Repository](https://github.com/Mintplex-Labs/anything-llm/issues). Both the Mintplex Labs Team and the AnythingLLM Community are there to offer support.

###### 2. Email the Mintplex Labs Team:

Send an email outlining your issue to [Team@MintplexLabs.com](mailto:Team@MintplexLabs.com). Be sure to provide a clear description of the problem you're facing.

###### 3. Discord Community:

Join Mintplex Labs Discord [Community Server](https://discord.gg/Dh4zSZCdsC) and post your support queries on the server to get help from the community.

> **Warning:**
>
> **NOTE**
>
> The Mintplex Labs Team is less active on Discord.
>
> For direct assistance from the team, consider opening an issue on [github](https://github.com/Mintplex-Labs/anything-llm/issues) or sending an email to the provided address.

#### Quick Links

[![AnythingLLM Github Issues](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Fsupport%2Fgithub.png&w=3840&q=100)Github Issues→](https://github.com/Mintplex-Labs/anything-llm/issues)[![AnythingLLM Email](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Fsupport%2Femail.png&w=3840&q=100)Email→](mailto:team@mintplexlabs.com)[![AnythingLLM Discord Community](https://docs.useanything.com/_next/image?url=%2Fimages%2Fgetting-started%2Fsupport%2Fdiscord.png&w=3840&q=100)Discord Community Invite→](https://discord.gg/Dh4zSZCdsC)


---

## Changelog

### Desktop Changelog Overview

*AnythingLLM Deskop Changelog*

**Source:** https://docs.useanything.com/changelog/overview

![AnythingLLM Changelog](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

### Desktop Changelogs

We're using this log to jot down everything we've finished working on. It helps us see the progress we've made. This changelog is only tracking the changes in the [AnythingLLM Desktop App](https://anythingllm.com/download).

You can read the recent changelogs by clicking the cards below:

[![AnythingLLM Desktop Changelog v1.15.0](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.15.0→](https://docs.useanything.com/changelog/v1.15.0)[![AnythingLLM Desktop Changelog v1.14.2](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.14.2→](https://docs.useanything.com/changelog/v1.14.2)[![AnythingLLM Desktop Changelog v1.14.1](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.14.1→](https://docs.useanything.com/changelog/v1.14.1)[![AnythingLLM Desktop Changelog v1.14.0](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.14.0→](https://docs.useanything.com/changelog/v1.14.0)[![AnythingLLM Desktop Changelog v1.13.0](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.13.0→](https://docs.useanything.com/changelog/v1.13.0)[![AnythingLLM Desktop Changelog v1.12.1](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.12.1→](https://docs.useanything.com/changelog/v1.12.1)[![AnythingLLM Desktop Changelog v1.12.0](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.12.0→](https://docs.useanything.com/changelog/v1.12.0)[![AnythingLLM Desktop Changelog v1.11.2](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.11.2→](https://docs.useanything.com/changelog/v1.11.2)[![AnythingLLM Desktop Changelog v1.11.1](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.11.1→](https://docs.useanything.com/changelog/v1.11.1)[![AnythingLLM Desktop Changelog v1.11.0](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.11.0→](https://docs.useanything.com/changelog/v1.11.0)[![AnythingLLM Desktop Changelog v1.10.0](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.10.0→](https://docs.useanything.com/changelog/v1.10.0)[![AnythingLLM Desktop Changelog v1.9.1](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.9.1→](https://docs.useanything.com/changelog/v1.9.1)[![AnythingLLM Desktop Changelog v1.9.0](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.9.0→](https://docs.useanything.com/changelog/v1.9.0)[![AnythingLLM Desktop Changelog v1.8.5](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.8.5→](https://docs.useanything.com/changelog/v1.8.5)[![AnythingLLM Desktop Changelog v1.8.4](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.8.4→](https://docs.useanything.com/changelog/v1.8.4)[![AnythingLLM Desktop Changelog v1.8.3](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.8.3→](https://docs.useanything.com/changelog/v1.8.3)[![AnythingLLM Desktop Changelog v1.8.2](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.8.2→](https://docs.useanything.com/changelog/v1.8.2)[![AnythingLLM Desktop Changelog v1.8.1](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.8.1→](https://docs.useanything.com/changelog/v1.8.1)[![AnythingLLM Desktop Changelog v1.8.0](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.8.0→](https://docs.useanything.com/changelog/v1.8.0)[![AnythingLLM Desktop Changelog v1.7.8](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.7.8→](https://docs.useanything.com/changelog/v1.7.8)[![AnythingLLM Desktop Changelog v1.7.7](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.7.7→](https://docs.useanything.com/changelog/v1.7.7)[![AnythingLLM Desktop Changelog v1.7.6](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.7.6→](https://docs.useanything.com/changelog/v1.7.6)[![AnythingLLM Desktop Changelog v1.7.5](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.7.5→](https://docs.useanything.com/changelog/v1.7.5)[![AnythingLLM Desktop Changelog v1.7.4](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.7.4→](https://docs.useanything.com/changelog/v1.7.4)[![AnythingLLM Desktop Changelog v1.7.3](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.7.3→](https://docs.useanything.com/changelog/v1.7.3)[![AnythingLLM Desktop Changelog v1.7.2](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.7.2→](https://docs.useanything.com/changelog/v1.7.2)[![AnythingLLM Desktop Changelog v1.7.1](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.7.1→](https://docs.useanything.com/changelog/v1.7.1)[![AnythingLLM Desktop Changelog v1.7.0](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.7.0→](https://docs.useanything.com/changelog/v1.7.0)[![AnythingLLM Desktop Changelog v1.6.11](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.6.11→](https://docs.useanything.com/changelog/v1.6.11)[![AnythingLLM Desktop Changelog v1.6.10](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.6.10→](https://docs.useanything.com/changelog/v1.6.10)[![AnythingLLM Desktop Changelog v1.6.9](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.6.9→](https://docs.useanything.com/changelog/v1.6.9)[![AnythingLLM Desktop Changelog v1.6.8](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.6.8→](https://docs.useanything.com/changelog/v1.6.8)[![AnythingLLM Desktop Changelog v1.6.7](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.6.7→](https://docs.useanything.com/changelog/v1.6.7)[![AnythingLLM Desktop Changelog v1.6.6](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.6.6→](https://docs.useanything.com/changelog/v1.6.6)[![AnythingLLM Desktop Changelog v1.6.5](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.6.5→](https://docs.useanything.com/changelog/v1.6.5)[![AnythingLLM Desktop Changelog v1.6.4](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.6.4→](https://docs.useanything.com/changelog/v1.6.4)[![AnythingLLM Desktop Changelog v1.6.3](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.6.3→](https://docs.useanything.com/changelog/v1.6.3)[![AnythingLLM Desktop Changelog v1.6.2](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.6.2→](https://docs.useanything.com/changelog/v1.6.2)[![AnythingLLM Desktop Changelog v1.6.1](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.6.1→](https://docs.useanything.com/changelog/v1.6.1)[![AnythingLLM Desktop Changelog v1.6.0](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)Changelog v1.6.0→](https://docs.useanything.com/changelog/v1.6.0)

### v1.10.0

*AnythingLLM Desktop v.1.10.0 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.10.0

#### Major New Features:

##### Meeting Assistant is live!

The AnythingLLM Meeting Assistant is live! The meeting assistant is a tool that can help you with your meetings or just any recordings.

The Meeting Assistant is an on-device solution for meeting transcription, summarization, agentic follow-up actions with no limits or paywalls, and complete customization.

[Video](https://webassets.anythingllm.com/preview.mp4)

You can learn more about the meeting assistant [on its introduction page](https://docs.useanything.com/meeting-assistant/introduction#the-meeting-assistant-does-this-and-more).

##### AnythingLLM Mobile is live on Google Play!

AnythingLLM Mobile is [live on Google Play](https://play.google.com/store/apps/details?id=com.anythingllm)! You can now download the app from the Google Play Store and start using AnythingLLM on your Android phone.

[Embedded video/content](https://www.youtube.com/embed/6bfVvZwC0vk?si=tvtQmrYerKF9B7mQ)

#### Notable Improvements: 🚀

**Installer Optimization**  
Now, on Windows and MacOS we will not attempt to reinstall dependencies if they are already installed. This speeds up installation time significantly. We also made some improvements to the installer to
shrink the installer size even though we are still packing more features!

---

**Docker Model Runner**  
We now have first class support for running models via the [Docker Model Runner & MCP Toolkit](https://docs.docker.com/ai/model-runner/). If you have the latest Docker Desktop installed you can use Docker for models and MCP servers!

![AnythingLLM Docker Model Runner Preview](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.10.0%2Fdmr-preview.png&w=3840&q=100)

---

**Windows ARM64 Qualcomm NPU improvements**  
We have made some improvements to the Windows ARM64 Qualcomm NPU engine. You should now see faster tokens and model loading times.

#### Other Improvements

- Migrate Azure OpenAI to enable streaming via V1 endpoint
- Remove workspace creation onboarding page
- Refactor WorkspaceFileRow Comp (handlers)
- FoundryLocal Improvements
- Implement global error boundary format
- Cohere agent implementation
- Privacy policy page improvements
- Track model name on chat send so you can see what model was used to answer your question.
- Add auth token support to Ollama embedding
- Move AnythingLLM Mobile to live under tools
- Refactor local whisper to use custom FFMPEG class.

#### Bug Fixes

- Patch Pagination bug in paperless-nix
- Many dependency updates and patches
- Patch XLSX files not being uploaded correctly on drag-and-drop.
- Patch YT scraper
- Patch docker AWS cred issue

#### Pinned Download Links

**Revision 1.10.0:**

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.10.0/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.10.0/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.10.0/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.10.0/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.10.0/AnythingLLMDesktop.AppImage)
- Linux (ARM64) [Download](https://cdn.anythingllm.com/legacy/1.10.0/AnythingLLMDesktop-Arm64.AppImage)

### v1.11.0

*AnythingLLM Desktop v.1.11.0 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.11.0

#### AnythingLLM Desktop Assistant is live!

The AnythingLLM Desktop Assistant is live! The desktop assistant is a context-aware assistant that lives across your entire OS.

In a single keystroke, you can open the Desktop Assistant and start chatting, creating agents, and more with full context from any open applications as well as all other chat functionality in AnythingLLM.

[Video](https://webassets.anythingllm.com/anythingllm-assistant-desktop-promo.mp4)

You can learn more about the desktop assistant [on its introduction page](https://docs.useanything.com/desktop-assistant/introduction).

#### Onboarding Improvements

We have made some improvements to the onboarding process to make it more user-friendly and intuitive. Now, on a fresh install of AnythingLLM Desktop, we will suggest the best model for your hardware and system for the most optimal performance and experience.

By default, this will always be an on-device multi-modal model. You can still choose any other model or provider if you prefer. This does not impact your ability to customize what LLM provider and model you want in settings or per-workspace.

![AnythingLLM Desktop Assistant Onboarding](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.11.0%2Fonboarding.png&w=3840&q=100)

#### Other Improvements

- General UI improvements and fixes
- Ability to edit SQL connectors in SQL Agent skill builder
- [PrivateMode](https://privatemode.ai) LLM provider support
- [SambaNova](https://sambanova.ai) LLM provider support
- Support for Auth tokens for LM Studio provider (LLM and Embedder)
- Smarter automatic context window size detection for models that support it.

#### Bug Fixes

- General dependency updates and patches

#### Pinned Download Links

**Revision 1.11.0:**

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.11.0/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.11.0/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.11.0/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.11.0/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.11.0/AnythingLLMDesktop.AppImage)
- Linux (ARM64) [Download](https://cdn.anythingllm.com/legacy/1.11.0/AnythingLLMDesktop-Arm64.AppImage)

### v1.11.1

*AnythingLLM Desktop v.1.11.1 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.11.1

#### Homepage Redesign

The main AnythingLLM homepage has been completely redesigned to be more modern and user-friendly so you can instantly start chatting the second you open the app after onboarding.

![AnythingLLM Changelog v1.11.1](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.11.1%2Fhomepage.png&w=3840&q=100)

#### Native Tool Calling

> **Note:**
>
> Native tool calling is the best performance and experience for tool calling with your LLM provider and model. If you can enable it, you should.
>
> *this only applies to local LLM providers. It has no impact on cloud LLMs like OpenAI, Anthropic, or Azure.*

We have completely overhauled how `@agent` tool calling works. Now, we will leverage the new native tool calling abilities of your LLM provider and model.

**What this means for you:**

- You can now run complex, **multi-step** tool calls with your LLM provider and model.
- Your model will now continue to work until your final response is generated or determined to be complete.
- You will get 100x better responses from even small tool-calling models

We have implemented safeguards as well to prevent infinite loops with a maximum of 10 tool calls per response to prevent runaway tasks.

![AnythingLLM Native Tool Calling](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.11.1%2Fnative-tool-calling.png&w=3840&q=100)

##### Limitations

Most providers do not allow us to probe for if a model supports native tool calling.

The following local LLM providers will automatically support native tool calling if your model supports it:

- Default Built in LLM Provider (AnythingLLM Default)
- Ollama
- LM Studio

For others, you will need to set an ENV variable to enable native tool calling for supported providers.

- Generic OpenAI
- Groq
- AWS Bedrock
- Lemonade
- LiteLLM
- Local AI
- OpenRouter

This can be set via the [`PROVIDER_SUPPORTS_NATIVE_TOOL_CALLING`](https://docs.useanything.com/configuration#native-tool-calling-for-llm-providers) environment variable.

```
PROVIDER_SUPPORTS_NATIVE_TOOL_CALLING="bedrock,generic-openai,groq,lemonade,litellm,local-ai,openrouter"
```

#### Meeting Assistant Overhaul

We have completely overhauled the Meeting Assistant to make it smaller, faster, and more efficient across all devices and platforms. Featuring a full Rust rewrite of the core meeting transcription and processing pipeline
you should now see significant changes in the performance and bundle size of the Meeting Assistant.

##### Model & Engine Migration

This new engine is so small (97% smaller) that AnythingLLM will automatically delete the old engine to free up space on your system. The new engine is now built-into the application itself.

The new engine also now moves to a more efficient and flexible model runtime. This means **you will need to re-download the Parakeet model** on your next transcription. AnythingLLM will automatically remove the old model to free up space on your system.

#### Lemonade by AMD Integration

![AnythingLLM Lemonade by AMD Integration](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.11.1%2Flemonade.png&w=3840&q=100)

[Lemonade](https://lemonade-server.ai) by AMD is an [open-source](https://github.com/lemonade-sdk/lemonade) local model runtime that optimizes performance and efficiency for local models (LLM, ASR, TTS, Image Generation, etc.) for all types of hardware including AMD GPUs and NPUs.

We have added first class support so you can use your local models running via Lemonade within AnythingLLM for the best application experience on top of your local hardware.

#### Other Improvements

- New `system` theme support that will inherit the system theme for the UI.
- Lightmode sidebar UI updates.

#### Bug Fixes

- Fix light mode/vibrancy issue on MacOS where Meeting Assistant was not visible.
- Resolve issue where `codesign` would show bundle signature warning after first launch for MacOS.
- CMD+Arrow keys disabled on prompt focus to prevent chat history moving around.
- Gemini 400 error on tool calls
- Fix issue with Ollama strict num\_ctx type conversion error.
- Fix issue with GitLab infinite loop for some repositories.

#### Pinned Download Links

**Revision 1.11.1:**

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.11.1/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.11.1/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.11.1/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.11.1/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.11.1/AnythingLLMDesktop.AppImage)
- Linux (ARM64) [Download](https://cdn.anythingllm.com/legacy/1.11.1/AnythingLLMDesktop-Arm64.AppImage)

### v1.11.2

*AnythingLLM Desktop v.1.11.2 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.11.2

#### More UI Improvements

[Video](https://webassets.anythingllm.com/changelog-1.11.2-uiv2.mp4)

Now, in the main chat UI we added some much desired UI improvements and fixes.

- New prompt input
- Better Citations UI and reporting
- Metrics for Agent calls
- Report document and web-search citations during Agent calls!
- Ability to each toggle on/off Agent skills from the prompt
- Ability to select the provider and model for the workspace without leaving the page.

#### Install time improvements

On Windows x64 machines with GPUs, we will automatically detect your GPU vendor and download **only** the appropriate GPU support files for your hardware. This will greatly improve the install time of AnythingLLM on Windows machines with GPUs.

This dramatically decreases the install time of AnythingLLM on Windows machines with AMD GPUs since the supporting binaries are much smaller.

#### Other Improvements

- Agents now report metrics and citations from docs + websites used
- OpenRouter stream metrics are now accurate
- Native tool calling for Novita
- Removed Google SERP as a default web-search provider (Google killed it)
- Add long-timeout fetch to Ollama embedder
- Better addtoworkspace errors in API
- Remove `use_mlock` from Ollama for API compatibility
- Added document count indicators to workspace document picker
- Perplexity search SERP is now available as a web-search provider

#### Bug Fixes

- Show LMStudio error state in model picker
- More Confluence Wiki fixes
- Strip thinking outputs from copy message in chat window
- Meeting Assistant - auto-verify model files before transcription to prevent errors during transcription

#### Pinned Download Links

**Revision 1.11.2:**

| Operating System | Architecture | Download |
| --- | --- | --- |
| Mac | x64 | [Download](https://cdn.anythingllm.com/legacy/1.11.2/AnythingLLMDesktop.dmg) |
| Mac | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.11.2/AnythingLLMDesktop-Silicon.dmg) |
| Windows | x64 | [Download](https://cdn.anythingllm.com/legacy/1.11.2/AnythingLLMDesktop.exe) |
| Windows | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.11.2/AnythingLLMDesktop-Arm64.exe) |
| Linux | x64 | [Download](https://cdn.anythingllm.com/legacy/1.11.2/AnythingLLMDesktop.AppImage) |
| Linux | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.11.2/AnythingLLMDesktop-Arm64.AppImage) |

### v1.12.0

*AnythingLLM Desktop v.1.12.0 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.12.0

#### Notable Improvements

##### Automatic Mode for native tool calling

For [Select providers](https://docs.useanything.com/features/chat-modes#available-chat-modes) that support native tool calling, you no longer need to use `@agent` to use tools. You can now just use the tools directly in your prompt.

If your prompt input does not have the "@" symbol, your chats will automatically use tools as needed.

[Video](https://webassets.anythingllm.com/docs-agent-example.mov)

#### Intelligent Tool Selection

We have added a new feature called [Intelligent Tool Selection](https://docs.useanything.com/agent/intelligent-tool-selection). This feature allows you to load **unlimited** tools for your agent to use into context with better performance and save up to 80% on token usage every single chat.

![AnythingLLM Agent Settings Menu Icon Location](https://docs.useanything.com/_next/image?url=%2Fimages%2Fanythingllm-setup%2Fagent-configuration%2Fsettings-menu-icon-location.png&w=3840&q=100)

#### Filesystem Agent

We have added a new feature called [Filesystem Agent](https://docs.useanything.com/agent/usage/file-system-agent). This feature allows you to use the filesystem of your host machine to search for files and directories.

![AnythingLLM AI Agents File Search Agent Main Panel](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fai-agents%2Ffs-desktop-config.png&w=3840&q=100)

#### Document Generation Agent

We have added a new built-in agent for [Document Generation](https://docs.useanything.com/agent/usage/document-generation-agent). With document generation, you can generate text files, PDFs, Excel files, Docx, and even entire PowerPoint presentations.

[Video](https://webassets.anythingllm.com/docgen.mp4)

#### Telegram Bot

AnythingLLM Docker and Desktop now support a [Telegram bot](https://docs.useanything.com/channels/telegram) so you can connect to your AnythingLLM instance anywhere in the world.

**Supports**:

- Text chat (streaming & thinking)
- Image understanding
- Voice messages & Attachments
- Automatic mode and @agent support
- Workspace and thread selection
- Model selection
- Citations
- Any agent skill available in AnythingLLM

![Telegram bot analyzing an image](https://docs.useanything.com/_next/image?url=%2Fimages%2Fguides%2Fchannels%2Ftelegram%2Fimage-understanding.png&w=3840&q=100)

#### Other Improvements

- Creation agent skills now will "Ask for confirmation" before creating files or documents.
- Removed cost estimation from the embedder window
- Uploaded files in embed window are now auto-selected in the document picker.
- Added API Key support to Lemonade Provider
- Granualar tool managment for MCP sub-skills to prevent tool call bloat.

#### Bug Fixes

- Fixed bug where checking URLs did not check MIME type before attempting to fetch.
- Fixed bug with chat window UI performance.

#### Pinned Download Links

**Revision 1.12.0:**

| Operating System | Architecture | Download |
| --- | --- | --- |
| Mac | x64 | [Download](https://cdn.anythingllm.com/legacy/1.12.0/AnythingLLMDesktop.dmg) |
| Mac | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.12.0/AnythingLLMDesktop-Silicon.dmg) |
| Windows | x64 | [Download](https://cdn.anythingllm.com/legacy/1.12.0/AnythingLLMDesktop.exe) |
| Windows | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.12.0/AnythingLLMDesktop-Arm64.exe) |
| Linux | x64 | [Download](https://cdn.anythingllm.com/legacy/1.12.0/AnythingLLMDesktop.AppImage) |
| Linux | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.12.0/AnythingLLMDesktop-Arm64.AppImage) |

### v1.12.1

*AnythingLLM Desktop v.1.12.1 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.12.1

#### Notable Improvements

##### Streamed Document Embedding

Now, when you upload a document to the workspace the process per-document is now reported during embedding. This is a huge improvement in performance and user experience. During this process you can add and remove documents to the queue as well as even close and navigate away from the page without losing your progress.

![Document Embedding](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.12.1%2Fqueue-embedding.png&w=3840&q=100)

##### App integrations

There are now built in integrations for the following apps with minimal to zero setup required for Agent skills:

- [Gmail](https://docs.useanything.com/agent/usage/gmail-agent)
- [Outlook](https://docs.useanything.com/agent/usage/outlook-agent)
- [Google Calendar](https://docs.useanything.com/agent/usage/google-calendar-agent)
- Apple Notes (MacOS only)

#### Other Improvements

- Image Lightbox in main UI
- Enabled Korean, Chinese, & Japanese character support for PDF generation via custom mdpdf fork
- Better citations for app integrations
- DDG default web-search in agent skills
- Open documents in native application on machine when generated by Document Generation Agent
- Auto approve agent skill via ENV setting
- Ollama bumped to 0.20.7 (Qwen3.5 support, Gemma 4, etc)
- New Customization > Chat setting for `Unload model when closed` to unload the model when the user closes the chat window.
- Generic OpenAI Capability detection/ENV setting
- Update Lemonade to support 1.10.0 changes
- Catalan translations
- Name field added to API keys
- Chat ID reported in agent sessions so now you can regenerate chats, TTS, and more actions without page reloads.

#### Bug Fixes

- Fixed bug where UI would flicker during chat if prompt input was collapsed with "Show more"
- Fixed bug where Desktop Assistant UI area capture tool would clip the intended capture area.
- Suppress the Audio transcription feature for Telegram (for now)
- Fixed temperature bug for AWS Bedrock Claude 4.7
- Fixed bug where illegal characters were present on Windows files.
- Fixed bug where last call tool runs when Max stack is hit
- Confluence Wiki context path preservation when set
- Fix streaming issue for LLM instruction blocks (Anthropic)

#### Pinned Download Links

**Revision 1.12.1:**

| Operating System | Architecture | Download |
| --- | --- | --- |
| Mac | x64 | [Download](https://cdn.anythingllm.com/legacy/1.12.1/AnythingLLMDesktop.dmg) |
| Mac | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.12.1/AnythingLLMDesktop-Silicon.dmg) |
| Windows | x64 | [Download](https://cdn.anythingllm.com/legacy/1.12.1/AnythingLLMDesktop.exe) |
| Windows | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.12.1/AnythingLLMDesktop-Arm64.exe) |
| Linux | x64 | [Download](https://cdn.anythingllm.com/legacy/1.12.1/AnythingLLMDesktop.AppImage) |
| Linux | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.12.1/AnythingLLMDesktop-Arm64.AppImage) |

### v1.13.0

*AnythingLLM Desktop v.1.13.0 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.13.0

#### Notable Improvements

This release is focused on improving the agent experience and adding new features to the agent system as well as moving towards a more passive, personal, and **hybrid** AI experience.

##### Model Router: The World's First Hybrid AI Experience

No other platform offers what AnythingLLM is shipping today.

The Model Router is the first-ever user-defined intelligent routing system that seamlessly blends local and cloud AI into a single, unified experience that is entirely under your control. Until now, you had to choose: run everything locally, or send everything to the cloud. That tradeoff is over.

With Model Router, you define the rules. Every message you send is automatically analyzed and routed to the perfect model for that specific task, whether that's a lightweight local model for quick questions, a reasoning model for complex math, or your most powerful cloud model for nuanced legal analysis. All from the same chat. All invisible to the user. All defined by you.

**What makes this groundbreaking:**

- **True hybrid AI.** Mix and match local models (Ollama, LM Studio, etc.) with cloud providers (OpenAI, Anthropic, Google) in a single conversation. No manual switching. No compromises.
- **You're in complete control.** Create [calculated rules](https://docs.useanything.com/model-router/setup#calculated-rules) that trigger on keywords, token counts, time of day, or image attachments **instantaneously**. Or use [LLM-classified rules](https://docs.useanything.com/model-router/setup#llm-classified-rules) that understand intent in plain English.
- **Save money without sacrificing quality.** Route simple queries to cheap or local models. Reserve expensive API calls for the messages that actually need them.
- **Intelligent caching.** Our advanced sticky routing system keeps you on the same model during a conversation thread, so you're not bouncing between models on every message.

This is, we believe, a fundamental shift in how AI assistants work. For the first time, you get the privacy of local models, the power of cloud models, and the intelligence to know when to use each. And it's 100% open source.

[Learn how to set up your first router →](https://docs.useanything.com/model-router/setup)

![Chat showing routing notifications above each response](https://docs.useanything.com/_next/image?url=%2Fimages%2Fmodel-router%2Fchat-routed.png&w=3840&q=100)

##### Scheduled Jobs: Your AI That Works While You Don't

What if your AI assistant could work for you in the background, automatically, on a schedule you define, without you lifting a finger?

**Scheduled Jobs** turns AnythingLLM into an always-on AI workforce. Create recurring tasks that run themselves: morning briefings, weekly reports, data monitoring, research digests. Anything you'd normally ask an agent to do, but automated and hands-free.

**Why this changes everything:**

- **Set it and forget it.** Define a prompt, pick your tools, choose a schedule, and walk away. Your agent runs exactly when you need it: every morning at 8 AM, every Monday at noon, every hour on the hour.
- **No technical knowledge required.** Our visual Cron Builder lets you schedule jobs with simple dropdowns. No cryptic cron syntax, no command line, no code. Just point and click.
- **Full agent power, fully automated.** Scheduled jobs have access to the same tools as your regular chats: web search, document analysis, custom skills, MCP integrations, and more. If an agent can do it in a conversation, it can do it on a schedule.
- **Complete run history.** Every execution is logged with the agent's full reasoning, tool calls, generated files, and final response. Review past runs anytime, or continue where the agent left off in a new thread.
- **Push notifications.** Get alerted the moment a job finishes, even when AnythingLLM is in the background. Click to jump straight to results.

**This is yet another capability no other local-first AI app offers.** Enterprise tools charge thousands for this kind of automation. Cloud-only platforms require you to trust your data to third parties. AnythingLLM gives you scheduled AI agents that run entirely on your machine, with your data, under your control.

Wake up to a summary of overnight emails. Get weekly progress reports written automatically. Monitor websites for changes. The possibilities are endless, and it all happens while you focus on what matters.

[Learn how to create your first scheduled job →](https://docs.useanything.com/scheduled-jobs/getting-started)

![Scheduled Jobs Run Result](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.13.0%2Fscheduled-job.png&w=3840&q=100)

##### Automatic Memories & Personalization

AnythingLLM now supports automatic memory extraction and personalization so your AI assistant can remember what you've talked about and use that knowledge to personalize its responses.

AnythingLLM runs a background job to extract memories from your chats and store them in a memory bank. This memory bank is then used to personalize the responses of your AI assistant - you have full control over what is remembered and how it is used
you can even add custom memories manually to the memory bank.

There are two types of memories:

- Workspace memories: These are memories that are specific to the current workspace (like what you are working on, projects-specific information, etc.)
- Global memories: These are memories that are specific to the entire AnythingLLM instance (like your name, preferences, etc.)

Memories are injected into the system prompt of your AI assistant so it can use them to personalize its responses and are a welcome addition to your AI assistant's knowledge base.

[Learn how to enable and manage memories →](https://docs.useanything.com/features/memories)

![Memories sidebar showing the Personalization toggle, workspace and global tabs, and memory cards](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fmemories%2Fmemories-sidebar.png&w=3840&q=100)

##### Agent Surveys (special tool)

Agent Surveys is a special tool that allows your AI assistant to ask clarifying questions before proceeding. This is useful when you are working with a complex task and the agent needs more information to proceed.

This is off by default and must be enabled in the agent settings. Answers to the questions are saved alongside the chat message so the agent can use them in future turns.

[Learn how to enable and manage agent surveys →](https://docs.useanything.com/features/agent-surveys)

![AnythingLLM Multi-Choice Survey](https://docs.useanything.com/_next/image?url=%2Fimages%2Ffeatures%2Fagent-surveys%2Fmulti-choice.png&w=3840&q=100)

#### Other Improvements

- Better tools menu so you can now see and manage all your tools directly from the chat window.
- Baidu web search support
- Improvements in error handling and reporting for several providers.
- Fix Deepseek v4 reinject thoughts bug causing errors in chat
- UI tooltips improvements and UX
- Support for Reasoning from LMStudio/Lemonade
- We have renamed "Auto" to ["Agent"](https://docs.useanything.com/features/chat-modes#available-chat-modes) in the chat window so it is more clear (works the same way)
- MiniMax support
- Pull generated documents from API
- Security improvements

#### Bug Fixes

- Fixed issue where you would need to `/reset` the chat twice to clear the chat history.
- Fixed issue where TTS would include markdown tags in the spoken text.
- Fixed issue where "Auto speak" would not work on new message
- Community Hub clipping/layout on narrow screens improved
- Font fallback for Cyrillic characters
- Gemini Parallel tool calling bug fixed, also better Gemini error reporting

#### Pinned Download Links

**Revision 1.13.0:**

| Operating System | Architecture | Download |
| --- | --- | --- |
| Mac | x64 | [Download](https://cdn.anythingllm.com/legacy/1.13.0/AnythingLLMDesktop.dmg) |
| Mac | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.13.0/AnythingLLMDesktop-Silicon.dmg) |
| Windows | x64 | [Download](https://cdn.anythingllm.com/legacy/1.13.0/AnythingLLMDesktop.exe) |
| Windows | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.13.0/AnythingLLMDesktop-Arm64.exe) |
| Linux | x64 | [Download](https://cdn.anythingllm.com/legacy/1.13.0/AnythingLLMDesktop.AppImage) |
| Linux | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.13.0/AnythingLLMDesktop-Arm64.AppImage) |

### v1.14.0

*AnythingLLM Desktop v.1.14.0 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.14.0

#### Improvements

- Cerebres provider
- The default chat thread is now killed when you create a new thread. If you have chats on the default thread, it will be available still. New workspaces or workspaces with no chats on default will no longer show it.
- All model providers are now *opt-out* of tool calling by default. Everything will call tools by default unless you opt-out offering better performance for agents everywhere
- STT Support for Deepgram, GenericOAI, Lemonade, & OpenAI
- TTS Support for KokoroTTS
- Web-scraping now will convert to markdown for better parsing and chat followup tasks with minimal context bloat
- Summary tool was overhauled. Now it will so better summaries with transparency as well as ask before continuing for longer summaries
- Improvements to the GenericOAI provider
- 24hour system variable formats
- Better LaTex rendering support

#### Bug Fixes

- Context limit detection issue for agents: <https://github.com/Mintplex-Labs/anything-llm/pull/5716>
- SEARXNG double encoding: <https://github.com/Mintplex-Labs/anything-llm/pull/5723>
- Timeouts for all fetch requests <https://github.com/Mintplex-Labs/anything-llm/pull/5721>
- Escape illegal XML in word docs, etc <https://github.com/Mintplex-Labs/anything-llm/pull/5760>
- (Windows) On unisntall, checkbox to remove **all** AnythingLLM data is now present
- Tray Fixes when app starts in background or Desktop Assistant feature is toggled.

#### Pinned Download Links

**Revision 1.14.0:**

| Operating System | Architecture | Download |
| --- | --- | --- |
| Mac | x64 | [Download](https://cdn.anythingllm.com/legacy/1.14.0/AnythingLLMDesktop.dmg) |
| Mac | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.14.0/AnythingLLMDesktop-Silicon.dmg) |
| Windows | x64 | [Download](https://cdn.anythingllm.com/legacy/1.14.0/AnythingLLMDesktop.exe) |
| Windows | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.14.0/AnythingLLMDesktop-Arm64.exe) |
| Linux | x64 | [Download](https://cdn.anythingllm.com/legacy/1.14.0/AnythingLLMDesktop.AppImage) |
| Linux | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.14.0/AnythingLLMDesktop-Arm64.AppImage) |

### v1.14.1

*AnythingLLM Desktop v.1.14.1 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.14.1

#### Meeting Assistant Overhaul

We have overhauled a large portion of the Meeting Assistant to make it smaller, faster, and more efficient across all devices and platforms.

- Now supports Intel, AMD, and NVIDIA GPUs for a 92% smaller binary and 15% faster processing times.

  - If you already have the NVIDIA GPU binary installed, you can safely delete it if you want. It will still work and is backwards compatible.
- Support for Developer API for transcription on audio (POST: `/v1/transcription/transcribe`)
- Meeting Assistant context window overflow handling is much better now - so small models can summarize longer meetings.
- Introduction of [Basic Speaker Identification](https://docs.useanything.com/meeting-assistant/features#speaker-identification) for 60% better summarizes from any audio.
- Dual channel stero recordings for meetings now - leading to 80% better speaker identification in "Full Diarization" mode.

#### Improvements

- Linux AppImage now **91%** smaller in size and caches Ollama engine downloads for faster startup times.
- Meeting Assistant title fix on meetings post-summary now auto-updates in UI
- AgentFLow variable highlight so its clear what is and is not a valid variable
- "Copy chat link" in UI to quickly re-open a chat in the desktop app via deeplinking.
- Re-enabled audio and video uploads via chat UI - uses Tinyscribe engine now.
- Export Chat as (PDF, JSON, Markdown, etc) from chat UI.
- Desktop Assistant Setting - HD screenshots now available for screenshot capture area.
- Request approval internal function is now available for custom skills.

#### Bug Fixes

- Removed DPAIS and HuggingFace providers from AnythingLLM
- Fixed memory leak in embedder from it constantly reloading in server process
- Fixed text clearing bug when dragging and dropping files into the chat and text was already present in prompt.
- Massive performance improvements to the frontend UI for long running chats.
- Cohere SDK removed and ported to OpenAI SDK for compatibility.
- Desktop Assistant Capture Area not showing on windows multi-monitor setups.
- Strip thinking from fork thread name when forking a chat that had thoughts.
- Fix toast light mode always showing regardless of system theme.
- Mistral embedder encoding issue fixed.
- Better error messages for API
- Omit temp in Claude Bedrock for Claude 4.8
- Fixed event emitter leak in server process for web-scraping and summarize process

#### Pinned Download Links

**Revision 1.14.1:**

| Operating System | Architecture | Download |
| --- | --- | --- |
| Mac | x64 | [Download](https://cdn.anythingllm.com/legacy/1.14.1/AnythingLLMDesktop.dmg) |
| Mac | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.14.1/AnythingLLMDesktop-Silicon.dmg) |
| Windows | x64 | [Download](https://cdn.anythingllm.com/legacy/1.14.1/AnythingLLMDesktop.exe) |
| Windows | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.14.1/AnythingLLMDesktop-Arm64.exe) |
| Linux | x64 | [Download](https://cdn.anythingllm.com/legacy/1.14.1/AnythingLLMDesktop.AppImage) |
| Linux | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.14.1/AnythingLLMDesktop-Arm64.AppImage) |

### v1.14.2

*AnythingLLM Desktop v.1.14.2 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.14.2

#### Improvements

- Groq Speech-to-Text support (whisper models)
- Brave Search web-search provider
- FastCRW web-browsing support
- Workspace settings spacing and design layout changes
- Improved UI/UX for mass delete of threads - now only shows when hovering over the thread container instead of everytime you press CMD/CTRL
- Migrated AWS Bedrock provider to OpenAI SDK for compatibility and removed it's packages.

#### Bug Fixes

- User prompt edit not appearing in agent mode after message completion
- Omit temp in Claude for Anthropic for Claude 4.8
- Fix Ollama keepalive with auth header when using API key
- Fix logic in Embed allowlist (self-hosted only)
- Fix bug where file attachments were not being displayed in chat when used during agent chat as citations

#### Pinned Download Links

**Revision 1.14.2:**

| Operating System | Architecture | Download |
| --- | --- | --- |
| Mac | x64 | [Download](https://cdn.anythingllm.com/legacy/1.14.2/AnythingLLMDesktop.dmg) |
| Mac | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.14.2/AnythingLLMDesktop-Silicon.dmg) |
| Windows | x64 | [Download](https://cdn.anythingllm.com/legacy/1.14.2/AnythingLLMDesktop.exe) |
| Windows | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.14.2/AnythingLLMDesktop-Arm64.exe) |
| Linux | x64 | [Download](https://cdn.anythingllm.com/legacy/1.14.2/AnythingLLMDesktop.AppImage) |
| Linux | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.14.2/AnythingLLMDesktop-Arm64.AppImage) |

### v1.15.0

*AnythingLLM Desktop v.1.15.0 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.15.0

#### Introducing Magic Features

Magic Features bring AI to your entire computer — not just inside AnythingLLM. Dictation, text actions, and autocomplete that work in any app, fully on-device. Available on AnythingLLM Desktop only.

All Magic Features are free to use — no signup required. Pro removes the daily limits.

###### AnythingLLM Pro

Nothing about AnythingLLM is changing. Pro is purely additive — no existing features are affected, nothing is being locked away.

Every Pro feature will always have a free daily tier, no signup required.

You can read more about AnythingLLM Pro [here](https://docs.useanything.com/pro/overview).

#### Magic Echo

> A smarter voice-to-text dictation that works anywhere on your OS. Can replace tools like SuperWhisper or WhisprFlow entirely. Fully on-device.

Speak naturally and your words appear right where your cursor is — transcribed, cleaned up, and punctuated. Echo can see what's on your screen to make dictations smarter and more contextual.

Includes custom dictionary support, voice commands, and more.

[[Video](https://webassets.anythingllm.com/magic-feature-promos-desktop/MagicEcho-promo.mp4)

##### Magic Echo

Voice-to-text dictation that works anywhere on your OS.

Learn more →](https://docs.useanything.com/pro/magic-echo)

#### Magic Beacon

> Highlight text in any app and instantly act on it with AI.

Highlight any text on your screen and instantly act on it — summarize, translate, rewrite, research, or run a custom action. Beacon works in any app without switching windows.

It also has full access to your agent skills, MCPs, and tools — AnythingLLM's entire capability set, available anywhere your cursor is.

[[Video](https://webassets.anythingllm.com/magic-feature-promos-desktop/MagicBeacon-promo.mp4)

##### Magic Beacon

Highlight text in any app and instantly act on it with AI.

Learn more →](https://docs.useanything.com/pro/magic-beacon)

#### Magic Tab

> Grammarly across your entire computer - fully on-device.

As you type, Magic Tab suggests what comes next — in any app, aware of what you're working on so suggestions actually fit. Click into a text field and it'll suggest something before you've typed a single letter.

If you use Grammarly, Tab can replace it entirely — privately, on your device.

[[Video](https://webassets.anythingllm.com/magic-feature-promos-desktop/MagicTab-promo.mp4)

##### Magic Tab

Inline text completions as you type — press Tab to accept.

Learn more →](https://docs.useanything.com/pro/magic-tab)

#### Other Improvements

- Removed chat history cap for workspace settings.
- [Intelligent Tool Selection](https://docs.useanything.com/agent/intelligent-tool-selection) is now enabled by default
- Generic OpenAI Embedder Prefixing is now supported in UI

#### Bug Fixes

- Windows filepath in `/update-embeddings` API endpoint was not being properly parsed

#### Pinned Download Links

> A revision for Windows (1.15.0-r2) is linked below to hotfix a bug where beacon would expand
> indefinitely while dragging due to Windows DPI scaling.
>
> If you downloaded Windows and the app shows version 1.15.0, please download the revision 1.15.0-r2 for the fix.

**Revision 1.15.0:**

| Operating System | Architecture | Download |
| --- | --- | --- |
| Mac | x64 | [Download](https://cdn.anythingllm.com/legacy/1.15.0/AnythingLLMDesktop.dmg) |
| Mac | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.15.0/AnythingLLMDesktop-Silicon.dmg) |
| Windows | x64 | [Download](https://cdn.anythingllm.com/legacy/1.15.0/AnythingLLMDesktop-r2.exe) |
| Windows | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.15.0/AnythingLLMDesktop-Arm64-r2.exe) |
| Linux | x64 | [Download](https://cdn.anythingllm.com/legacy/1.15.0/AnythingLLMDesktop.AppImage) |
| Linux | ARM64 | [Download](https://cdn.anythingllm.com/legacy/1.15.0/AnythingLLMDesktop-Arm64.AppImage) |

### v1.6.0

*AnythingLLM Desktop v.1.6.0 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.6.0

![AnythingLLM Changelog v1.6.0](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### New Features:

- **Multimodal support** - You can now upload text and images into the
  chat and use them with image capable models.

> You **must** use a multi-modal model to chat with images. This model can be
> a local LLM or cloud-hosted model like GPT-4o.
>
>   
>
> We added `LLaVA-Llama3` as a model in our built-in LLM to make selection
> easier for those unfamiliar with multi-modal models.

- Drag-and-Drop files into the chat UI to automatically upload & embed at
  once.

> Images you drag-and-drop into a chat window are used for that specific chat.
> Document files **uploaded are embedded** into the workspace as you normally
> would and are available until un-embedded.

#### Fixes & Improvements:

- Bumped known models for Perplexity & TogetherAI
- Various small bugfixes

#### What's Next:

- Custom `@agent` skill builder
- More data connector integrations

### v1.6.1

*AnythingLLM Desktop v.1.6.1 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.6.1

![AnythingLLM Changelog v1.6.1](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### New Features:

- **PiperTTS** - 100+ High-quality multi-lingual locally running text-to-speech models :)
- Multiple `/slash` command expansions in prompt now supported
- MathJax/KaTeX/LaTeX support in responses

#### Fixes & Improvements:

- German and Portuguese translations
- Various small bugfixes

#### What's Next:

- Custom `@agent` skill builder
- More data connector integrations

### v1.6.10

*AnythingLLM Desktop v.1.6.10 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.6.10

![AnythingLLM Changelog v1.6.10](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### What's New:

- Added Support for a true dark and light mode UI
- Internal Ollama bumped to 0.4.2
- Added Undo/Redo to prompt input

#### Other Improvements:

- Fixed titlebar not being draggable on onboarding
- Updated VoyageAI model list
- Improved model list detection for LMStudio

#### Bug Fixes:

- Fixed performance issues with long-running message windows
- Fixed scrollbar UI toggle not showing
- Fixed Bing search sessions not working

#### What's Next:

- Community Hub for Agent skills, workspace sharing, and more. [Pull Request #2555](https://github.com/Mintplex-Labs/anything-llm/pull/2555)

### v1.6.11

*AnythingLLM Desktop v.1.6.11 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.6.11

![AnythingLLM Changelog v1.6.11](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### What's New:

- Internal Ollama bumped to 0.4.3
- Text size setting now changes font size in prompt input
- Added support for Mistral Embedding

#### Other Improvements:

- Bumped Gemini Models
- Bumped TogetherAI Models
- Added Vietnamese partial translation
- MaxConcurrentChunks Setting for Generic OpenAI Embedder is now configurable

#### Bug Fixes:

- Sidebar width changing when going between workspaces

#### What's Next:

- Community Hub for Agent skills, workspace sharing, and more. [Pull Request #2555](https://github.com/Mintplex-Labs/anything-llm/pull/2555)

### v1.6.2

*AnythingLLM Desktop v.1.6.2 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.6.2

![AnythingLLM Changelog v1.6.2](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### Fixes & Improvements:

*this was a hotfix patch to bump the internal ollama binaries to support tooling*

### v1.6.3

*AnythingLLM Desktop v.1.6.2 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.6.3

![AnythingLLM Changelog v1.6.3](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### New Features:

- **Speech to Text** - You can now chat to AnythingLLM with your device microphone. This uses a built-in whisper model that runs in AnythingLLM. Supports all multiple languages.

#### What's Next:

- Custom `@agent` skill builder
- More data connector integrations

### v1.6.4

*AnythingLLM Desktop v.1.6.4 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.6.4

![AnythingLLM Changelog v1.6.4](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### Fixes & Improvements:

- Slash Commands bug fix during editing
- Gemini `exp-flash` model bug fixed
- Added `.go` filetype
- Fix depth handling on bulk link scraper
- Host URL auto-detection for LocalAI
- Agent prompt window limit sizing corrected
- Markdown styling for images in chat window
- Pre-prompt filtering handler
- Hebrew Language Support

#### What's Next:

- Custom `@agent` skill builder/custom-plugins
- Chrome Extension support

### v1.6.5

*AnythingLLM Desktop v.1.6.5 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.6.5

![AnythingLLM Changelog v1.6.5](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)
> **Note:**
>
> **Hotfix Available** This version was patched in [1.6.6](https://docs.useanything.com/changelog/v1.6.6) -
> please use that version before submitting a bug on GitHub or Discord.

#### What's New:

- [**AnythingLLM Browser Extension:**](https://docs.useanything.com/browser-extension/install) Send and embed information from the web directly to AnythingLLM or embed directly into your workspaces for later!
- [**Custom Agent Skills:**](https://docs.useanything.com/agent/custom/introduction) Create fully custom agent skills to extend the capabilities of your `@agent` invocations.
- [Better logging](https://docs.useanything.com/debug) for debugging.
- You can now use `@agent` to run skills via the developer API.

**Potential Breaking Change:**

- By default, AnythingLLM will boot up on `localhost` and not `0.0.0.0` - which may be required if you are using the Desktop App developer API over LAN via private IP connection. You can change this in the system settings of the app.

#### Fixes & Improvements:

- Fixed bug on windows where dragging and dropping files would embed, but not show as embedded in the UI.
- Default profile picture are less ugly now.
- Model provider updates (Gemini, Perplexity, Voyage AI, etc)
- Milvus bug fix
- Escape key to close document uploader
- `SearchApi` agent web browsing support
- Removal of `@agent` popup for first time users.
- Removal of Fine-tuning alert from UI.

#### What's Next:

- Custom workspace icons and user avatars.
- Community Hub for sharing custom agent skills, workspaces, prompts, etc.

### v1.6.6

*AnythingLLM Desktop v.1.6.6 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.6.6

![AnythingLLM Changelog v1.6.6](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)
> **Tip:**
>
> **Hotfix** This version is a hotfix patch for [1.6.5](https://docs.useanything.com/changelog/v1.6.5) - see that
> version changelog for full changes in 1.6.6.

#### Hotfix patch

This version was a hotfix patch for a small bug with `@agents` on 1.6.5. If you are on 1.6.5, you should upgrade to this version before submitting a GitHub issue or asking the Discord.

### v1.6.7

*AnythingLLM Desktop v.1.6.7 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.6.7

![AnythingLLM Changelog v1.6.7](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### What's New:

- Added custom agent skill calling to `@agent` calls in the developer API.

#### Fixes & Improvements:

- Fixed bug where `@agent` web-search and sql-agent connections were not showing in UI once saved, but were saved.
- Fixed bug where UI would should 11Labs model selection was not saved, but was saved.
- Perplexity model selections updated to current.

### v1.6.8

*AnythingLLM Desktop v.1.6.8 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.6.8

![AnythingLLM Changelog v1.6.8](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### What's New:

- You can now paste text, pictures, and files into the prompt input when focused if the items are on your clipboard.
- Generic OpenAI TTS connector is live. Any OpenAI compatible tts service will work now!
- [Deepseek](https://deepseek.com) LLM connector is now supported
- [Apipie](https://apipie.com) LMM connector is now supported
- [Fireworks](https://fireworks.ai) LLM connector is now supported
- [XAI](https://x.ai) Grok `grok-beta` LLM connector is now supported
- [Tavily](https://tavily.com) SERP connector is now supported for agent `web-search` skill.
- O1 model support for OpenAI
- LiteLLM Agent support
- Workspace agent selection is no longer **required** to be set in the settings. It will auto-select the model and provider based on your workspace and then your system settings. You can still set it manually if you'd like.
- Bulk document removal from UI is now supported via checkbox selection on right panel.
- `Select all` is now supported in the directory component. Right-click on the directory panel to select/deselect all.
- Mistral multi-modal support
- Groq Image support (please use supported vision model.)

#### Improvements:

- XLSX file upload support
- Gitlab connector can now pull issues in addition to code.
- Chat windows now auto-scrolls with reasonable behavior
- Show scrollbar `Appearance` setting to show scrollbar on right of chat windows for some users
- Freeform model input for chat models selection is now supported for LLMs with no `/models` endpoint. (Azure, Bedrock, etc.)
- Voyage model embedders were bumped to the latest versions.
- Github repo loader `langchain` was bumped to the latest version.
- Attachments in Dev API are now supported for API chats.
- File fetch speed improvements for the file picker
- `UserID` is now a supported option param in requests to the `workspace thread` endpoints for API.

#### Bug Fixes:

- Fixed a bug where the chat window would not scroll when you had a lot of messages.
- The agent model preference was not being respected for Bedrock and LMStudio. It now is.
- Handle non-ascii characters in single and bulk link scraper URLs
- Handle Bedrock models that cannot use `system` prompts (Titan)
- File name truncation on file rows overflowing the UI on file picker
- `Dockerfile` and `Jenkinsfile` file upload support
- Patch 11Labs selection bug not persisting in UI, while still being selected in the backend
- Patch bug in web-search and sql connector not persisting in UI, while still being selected in the backend
- GitHub handle `/tree` or `/blob` URLs from breaking collector.

#### What's Next:

- Community Hub for Agent skills, workspace sharing, and more.
- True dark mode and light mode UI
- Bump in internal OLLAMA provider to latest version + pulling in any valid Ollama tag via our UI.

---

- *optional* - we may enable custom UI themes for AnythingLLM

### v1.6.9

*AnythingLLM Desktop v.1.6.9 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.6.9

![AnythingLLM Changelog v1.6.9](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### What's New:

##### AMD GPU Support + More

Our internal Ollama provider was bumped to the latest version (0.3.14) which includes support for AMD GPUs, as well as other improvements.

For Windows, we install the additional support files during the [installation process](https://docs.useanything.com/installation-desktop/windows) automatically.
For MacOS, there is nothing to do.

##### Import any Ollama Model Tag or Hugging Face Model

You can now import any Ollama model tag or Hugging Face model into AnythingLLM using the default Ollama provider. Simply enter the tag or URL and hit import.
This allows you to use models that are not explicitly listed in the UI.

Just paste in the `ollama run` command and hit import!

Pulling from [Ollama.com](https://ollama.com/library)
example: `ollama run mistral-nemo`

Pulling from [Hugging Face](https://huggingface.co/docs/hub/en/ollama)
example: `ollama run hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF`

![AnythingLLM Import Model](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.6.9%2Fimport.png&w=3840&q=100)

##### Computer Use (Anthropic AI)

AnythingLLM can now leverage the new Anthropic AI Computer Use models.

This is an [experimental feature](https://docs.anythingllm.com/beta-preview/active-features/computer-use) and must be explicitly enabled in your system settings.

![AnythingLLM Computer Use](https://docs.useanything.com/_next/image?url=%2Fimages%2Fbeta-preview%2Fcomputer-use%2Finvoke.png&w=3840&q=100)

##### Find-in-page support for workspace chat

You can now find specific text within the workspace chat window. Simply press `Ctrl+F` to open the finder input at the top-right of the chat window.

![AnythingLLM Find in Page](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.6.9%2Ffind-in-page.png&w=3840&q=100)

#### Other Improvements:

- Added [NovitaAI](https://novita.ai/) as a supported LLM Provider
- Improved document metadata for embedding/RAG results
- Added Session Token support for AWS BedRock inference
- Added API docs update
- Added API Limit/orderBy for `workspace/chats` endpoint
- Added support for INO filetype

#### Bug Fixes:

- Patch restriction where localhost address web scraping was blocked.
- Patch bad reference for Ephemeral agent invocation
- Fixed issue where files with non-latin characters were not being respected when uploaded via API

#### What's Next:

- Community Hub for Agent skills, workspace sharing, and more. [Pull Request #2555](https://github.com/Mintplex-Labs/anything-llm/pull/2555)
- True dark mode and light mode UI [Pull Request #2481](https://github.com/Mintplex-Labs/anything-llm/pull/2481)

### v1.7.0

*AnythingLLM Desktop v.1.7.0 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.7.0

![AnythingLLM Changelog v1.7.0](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### What's New:

- [AnythingLLM Community Hub is live!](https://hub.anythingllm.com/) & [integrated into AnythingLLM Desktop](https://docs.useanything.com/community-hub/about)

#### Bug Fixes:

- Fixed bug with undefined code blocks in light mode being invisible
- Fixed where creation of multiple workspaces in a row would not display the new workspace

### v1.7.1

*AnythingLLM Desktop v.1.7.1 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.7.1

![AnythingLLM Changelog v1.7.1](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### What's New:

- Token tracking metrics (time spent, tokens per second, etc.) on chats in workspace
- Fine-tuning flow support fully deprecated - to be replaced by local fine-tuning
- API improvements for workspace creation
- Add `GitLab` to watchable documents
- Add vector search API endpoint
- Ability to show/hide sidebar (cmd/ctrl + Shift + S)

#### Improvements:

- Gemini `/models` support
- Internal Ollama bumped to 0.5.4
- Deletion of current thread will not automatically re-route to default thread

#### Bug Fixes:

- User confirmation to reset all workspaces and clear document cache when changing embedding model or vector database - prevents accidental lockup of workspaces due to dimension mismatch
- Light mode table styles not showing headers

### v1.7.2

*AnythingLLM Desktop v.1.7.2 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.7.2

![AnythingLLM Changelog v1.7.2](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### What's New:

- Reranker added for workspace RAG (LanceDB only)
- Support attachmets via threadWorkspace API endpoints
- Added support for Gemini text embedder

###### Windows ARM64 - Snapdragon X Elite devices only

By default, on Windows ARM64 devices that have the Snapdragon X Elite chipset, AnythingLLM is now able to download and run LLMs on the built-in NPU. This is a huge efficiency boost for any workspace that uses RAG.

Additionally, the default embedder model is able to run on the NPU as well with a 30% performance increase in embedding documents.

[Embedded video/content](https://www.youtube.com/embed/iQvHtubnfcI?si=McTUvuPNCc_AtGIM)

#### Improvements:

- Migrate assets to our CDN for faster download speeds
- Update OpenAI responses to be proper second format
- Typo in SearXNG setup
- Voyage embedding models updated
- Api documentation upload endpoint fixed

#### Bug Fixes:

- Fixed “Javascript error” modal that showed for some users on start with no impact to app function (Windows x86 only)
- Scrollbar showing on some chats for no reason
- Fixed crash on audio file upload with low bitrate

### v1.7.3

*AnythingLLM Desktop v.1.7.3 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.7.3

![AnythingLLM Changelog v1.7.3](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### What's New:

![AnythingLLM Thinking UI](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.7.3%2Fthink.png&w=3840&q=100)![AnythingLLM Agent UI](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.7.3%2Fagent-ui.png&w=3840&q=100)

- Added new Agent logging output UI elements
- Added LLM `<thinking>` UI handlers for thinking chats and outputs
- Added ability to disable `default` agent skills

#### Improvements:

- Farsi translations
- Gemini model caching
- AzureOpenAI `o1` API verison support
- Caching of TogetherAI models
- Update NVIDIA NIM branding
- Bump perplexity models
- Improved LaTeX support for `$$` and `\[...\]` style equations

#### Bug Fixes:

- Fixed Officeparser tempfile location bug
- Adjustment to how `similarity_score` is calculated for RAG
- UI stop button bug invisible on light mode

### v1.7.4

*AnythingLLM Desktop v.1.7.4 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.7.4

![AnythingLLM Changelog v1.7.4](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### What's New:

![AnythingLLM Agent UI](https://docs.useanything.com/_next/image?url=%2Fimages%2Fagent-flows%2Fflow-example.png&w=3840&q=100)

- [Agent Flows](https://docs.useanything.com/agent-flows/overview) for easier agent skill creation (more blocks coming to desktop soon)
- Built in native OCR for scannedPDF and Images!

#### Improvements:

- QNN NPU model engine bumped for faster loading of models and inference.
- Include `reasoning_content` in Generic OpenAI connector
- Include reasonsing for Deepseek API
- Changed onboarding flow to be native language for system
- Tokenizer performance improvements for large documents
- `<thinking>` Inherit UI font size from UI for think
- Azure O1,O3 support and reasoning
- Enable `num_ctx` in ollama embdder to match dimensions
- Patch PPLX timeouts + inchat citations from PPLX
- Improved agent logging for web scraping
- Patch Gitlab sub-project pulling
- PAT on Confluence connector
- In chat citations for Perplexity API

#### Bug Fixes:

- Fixed bad upload UI loop on document loader
- Fixed light mode SQL connector `X` being invisible
- Fixed bad codeblock header size on Windows
- Fixed O3 model temperature being present in requests resulting in 403

#### Pinned Download Links

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.7.4/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.7.4/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.7.4/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.7.4/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.7.4/AnythingLLMDesktop.AppImage)

### v1.7.5

*AnythingLLM Desktop v.1.7.5 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.7.5

![AnythingLLM Changelog v1.7.5](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### What's New:

- Anthropic `/models` endpoint - no more static model list (finally!!!!)
- Add multi-lingual support for OCR module

#### Improvements:

- More localization in more parts of UI
- PPIO model provider
- New agent/thinking animation UI
- Added API to upload documents to folder
- Arabic translations
- L/R message layout configuration for chat UI
- Support markdown in custom messages
- Normalize default chat ordering in API
- Add endpoints to retrive documents by folder
- Ollama Auth token UI

#### Bug Fixes:

- Return default Deepseek models when API key is wrong or invalid
- Fix collector crash when transcription model 404

#### Pinned Download Links

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.7.5/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.7.5/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.7.5/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.7.5/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.7.5/AnythingLLMDesktop.AppImage)

### v1.7.6

*AnythingLLM Desktop v.1.7.6 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.7.6

![AnythingLLM Changelog v1.7.6](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### What's New:

##### Reorder workspaces

You can now reorder your workspaces by dragging and dropping them into your desired order.

##### Ollama 0.6.2

The internal version of Ollama has been updated to 0.6.2

*note:* There is a known issue with ollama 0.6.2 where `gemma3` does not work. We will patch this when it is fixed in Ollama.

##### Installer skip

*windows only*

We've added an option to skip instllation of the ollama libraries when installing AnythingLLM. This is useful if you plan to not use the internal ollama shipped with AnythingLLM and want to save disk space and time.

#### Improvements:

- Added Danish translations
- Documentation pinning UI improvements
- Remove folder endpoint was added to dev API

#### Bug Fixes:

- Fixed issue where clicking on gear icon on non-focused workspace on sidebar would open chat page and not it's settings page
- Fixed issue where `deepseek` thoughts in the UI were being cut off
- Fixed issue where `stop` button did not show in the UI when streaming responses
- ChromaDB integrations updated to work with latest chroma version
- Embedding OpenAI compatible endpoint updated to comply with expected OpenAiI response schema

#### Pinned Download Links

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.7.6/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.7.6/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.7.6/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.7.6/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.7.6/AnythingLLMDesktop.AppImage)

### v1.7.7

*AnythingLLM Desktop v.1.7.7 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.7.7

![AnythingLLM Changelog v1.7.7](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### Improvements:

- Bumped LanceDB to 0.15.0 for improved performance and memory usage

#### Bug Fixes:

- Resolved issue where internal LLM would hang when a chat was sent and then the user waited 10+ to send another message

#### Pinned Download Links

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.7.7/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.7.7/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.7.7/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.7.7/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.7.7/AnythingLLMDesktop.AppImage)

### v1.7.8

*AnythingLLM Desktop v.1.7.8 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.7.8

![AnythingLLM Changelog v1.7.8](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### Improvements:

- Introduced official [NVIDIA NIM support](https://docs.useanything.com/nvidia-nims/introduction) for Windows machines with RTX GPUs - [check system requirements](https://docs.useanything.com/nvidia-nims/system-requirements) to see if your GPU is supported
- [System Variable support](https://docs.useanything.com/features/system-prompt-variables) now supported in regular chat via the Workspace `System Prompt` input.
- Added support for `@agent` usage in slash commands.
- Added support for Slash commands in Developer API chat requests.
- Added support for [Agent Flow](https://docs.useanything.com/agent-flows/overview) execution via Developer API chat requests.

#### Bug Fixes:

- Resolved issue in UI where the frontend would crash on New Workspace creation if the user was on a workspace with multiple threads.
- Fixed bug in Developer API for workspace chat where attachments were not being persisted in the UI/Chat history.
- Fixed bug where you could set a slash command the same as a reserved system slash command.

#### Pinned Download Links

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.7.8/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.7.8/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.7.8/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.7.8/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.7.8/AnythingLLMDesktop.AppImage)

### v1.8.0

*AnythingLLM Desktop v.1.8.0 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.8.0

![AnythingLLM Changelog v1.8.0](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)

#### Improvements:

- [MCP Agent skills](https://docs.useanything.com/mcp-compatibility/overview) are now available in the AnythingLLM Desktop app
- We now have a fresh new landing page when on the main screen of the app!
- Several hundred UI updates for readability and consistency across the app
- Added Japanese translations
- Support for in-text citations in the openRouter provider when using Perplexity models
- Azure AI options and model map updated with new model context window configurations

#### Bug Fixes:

- Fixed a bug where the MSSQL connection string parser was not working
- Fixed a bug where the Agent Flow description was not being used in the agent runner
- Updated the time for Gemini model list to expire to 1 day
- Fixed a bug where a failed tool call for some providers could result in a loop of failed tool calls
- Fixed bug where using the https `.git` URL for a repo in the data connector would 404.

#### Pinned Download Links

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.0/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.8.0/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.8.0/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.8.0/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.0/AnythingLLMDesktop.AppImage)

### v1.8.1

*AnythingLLM Desktop v.1.8.1 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.8.1

![AnythingLLM Changelog v1.8.1](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2Fheader-image.png&w=3840&q=100)
> **Warning:**
>
> **Revision 1.8.1-r2 available:**
>
> - Fixed error with AzureOpenAI LLM integration
>
> *see bottom of this page for revision fixed download links*

#### New Features:

- Agent flow [Read](https://docs.useanything.com/agent-flows/blocks/read-file) and [Write](https://docs.useanything.com/agent-flows/blocks/write-file) file blocks for Desktop
- Added Text-to-Speech and Speech-to-Text auto-submit and autoplay settings
- DrupalWiki data connector

#### Improvements:

- Updated internal [Ollama to 0.6.7](https://github.com/ollama/ollama/releases/tag/v0.6.7)
- Deeplinks for connecting Hub to AnythingLLM Desktop
- Migrate Gemini API to Azure to common OpenAI SDK
- UI bugs, fixes, and improvements for light mode
- Translations for main page
- Allow custom headers on upload-link via `/upload-link` endpoint
- Fix Windows MCP server restart issues
- Extended MCP tool use to be included in backend API `/chat` endpoint calls
- API document upload auto-add to workspace(s)
- MCP SSE/Streamable support

#### Bug Fixes:

- Fix `404` on Ollama large GGUF imports
- KoboldCPP Max Tokens
- Fix empty thoughts from reasoning models from showing in chat

#### Pinned Download Links

**Revision 1.8.1-r2:**

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.1-r2/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.8.1-r2/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.8.1-r2/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.8.1-r2/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.1-r2/AnythingLLMDesktop.AppImage)

**Revision 1.8.1:**

> *This version was patched to fix the AzureOpenAI LLM integration error. Please use 1.8.1-r2 if you are experiencing issues*

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.1/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.8.1/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.8.1/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.8.1/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.1/AnythingLLMDesktop.AppImage)

### v1.8.2

*AnythingLLM Desktop v.1.8.2 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.8.2

#### New Features:

- You can now swap models in the chat window (Cmd/Ctrl + L while on a chat screen or click the "brain" icon in the prompt input)

![AnythingLLM Changelog v1.8.2](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.8.2%2Fmodel-selector.png&w=1200&q=100)

- System Prompt History version tracking

  ![AnythingLLM Changelog v1.8.2](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.8.2%2Fsystem-prompt.png&w=1200&q=100)
- PGVector support for your vector database
- Keyboard shortcuts (`cmd/ctrl + Shift + ?` to see all quick commands)

![AnythingLLM Changelog v1.8.2](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.8.2%2Fkeyboard-shortcuts.png&w=1200&q=100)

#### Improvements:

- Updated internal [Ollama to 0.9.0](https://github.com/ollama/ollama/releases/tag/v0.9.0)
- Various minor UI/UX improvements
- Dynamic context window pulling for cloud based LLMs
- When you create a new API key, it will now be added to the API key list without having to refresh the page
- Attachments UI loading and active state update
- UX improvement to disable sending messages when attaching documents is still processing
- Disable Spellcheck in chat window (available in chat settings)
- Improved file picker load times when loading large files (150MB+)
- Latvian language support
- You can now import Agent Flows from the [Community Hub](https://hub.anythingllm.com/list/agent-flows)

- **MCP Improvements**
- - MCP start/stop text
- - MCP ENV inheritance for desktop clients

- **Agent Flow improvements**
- - removed the `inputVar` requirement for LLM Instruction blocks (you can use any variable anywhere in any block now)
- - You can now enable `Direct Output` on any block in agent flows to avoid the LLM from interacting with the flow outputs when invoked
- - Added `PUT` and `PATCH` support for agent flow API blocks
- - You can now use [JSON object traversal](https://docs.useanything.com/agent-flows/blocks/default-blocks#json-object-traversal) in agent flow variables to access nested values in JSON like variables in flows

- **Citations UI/UX improvements**
- - Better rendering animation
- - New layout for citations line items and icons
- - Tooltip for semantic score fixed being under the citaiton modal when open.

#### Bug Fixes:

- Fixed Azure image attachment issues where images were not being attached to the chat
- OpenAI MaxChunkLength was not being respected for splitting text into chunks
- Fixed bug where agent sessions would not clear any attached files on prompt input
- Fixed UI bug where file directory tooltip was not wrapping text that was underscored and long
- Fixed bug where model map cache was not being refreshed or was `null` when stale resulting in incorrect context window sizes

#### Pinned Download Links

**Revision 1.8.2:**

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.2/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.8.2/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.8.2/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.8.2/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.2/AnythingLLMDesktop.AppImage)

### v1.8.3

*AnythingLLM Desktop v.1.8.3 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.8.3

#### Improvements:

- [Authenticated Web-Scraping](https://docs.useanything.com/features/browser-tool) - AnythingLLM agents, flows, and the document collector can now scrape websites that require authentication or are paywalled!
- Updated homepage checklist to include new "Connect to Community Hub" task
- You can now seamlessly push new Agent Flows, System Prompts, and Slash Commands to the Community Hub from the AnythingLLM Desktop app
- You can now disable streaming for the Generic OpenAI LLM provider
- Added more translations (German, Korean, Estonian, Polish)

#### Bug Fixes:

- Migrated CMD+H to Cmd+Shift+H for home shortcut (broken hide command on MacOS)
- Show Scrollbar toggle moved to `Chats` menu item
- Added a tooltip hint when you are in a chat and the model is set to `Query Only` and you get the default response
- Fixed broken YouTube transcript scraper
- Fixed Reranker Tokenizer race condition
- Fixed score reporting on Milvus, Zillz, and Pinecone

#### Pinned Download Links

**Revision 1.8.3:**

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.3/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.8.3/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.8.3/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.8.3/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.3/AnythingLLMDesktop.AppImage)

### v1.8.4

*AnythingLLM Desktop v.1.8.4 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.8.4

#### Improvements:

- Search for Workspaces and Threads in the sidebar
- Sticky codeblock header while scrolling for easy copy
- Obsidian connector for desktop is live
- SQL Preflight connection check **before** saving as agent skill item
- Encrypted MSSQL connection strings support

#### Bug Fixes:

- Fixed issue with false positive for AntiVirus softwares (mostly Bitdefender)
- Fixed Font size UI bug causing layout shift
- Fixed Max codeblock width as long strings would overflow the UI
- Fixed Youtube folder name bug where title had odd characters
- Added Legal/TOS link in sidebar
- Fixed chunk parser log
- Fixed BigInt Bug handler with some providers who return BigInts (?)

#### Pinned Download Links

**Revision 1.8.4:**

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.4/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.8.4/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.8.4/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.8.4/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.4/AnythingLLMDesktop.AppImage)

### v1.8.5

*AnythingLLM Desktop v.1.8.5 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.8.5

> **Warning:**
>
> We released a hotfix for this version. Please ensure you are on the **v1.8.5-r2** release instead.

#### File Chat Overhaul 🎉

[Video](https://docs.useanything.com/images/document-chat/upload-documents.mp4)

When we first launched AnythingLLM the average local model context window was around 2K tokens. Now that local models are very powerful with 16K+ context windows it is time we overhaul our file UX.

Now, in AnythingLLM Desktop chatting with files is a breeze. When available we will now use the **full** file content to answer your questions when your model's context window is appropriate.

If you upload a file that is too large to fit in the context window, we will ask you to embed the file instead (RAG). If you want to have a file only for RAG, you can do that too via the regular file upload window on the workspace.

Now you can have the best of both worlds. Read more about this change [here](https://docs.useanything.com/chatting-with-documents/introduction#rag-vs-attached-documents).

#### Improvements: 🚀

- Modal to clear embedding cache when you change the text splitter options so all files share the same splitting logic
- Moonshot AI LLM support
- The native embedder model can now easily be configured. Supports [`nomic-embed-text-v1`](https://huggingface.co/Xenova/nomic-embed-text-v1) and [`multilingual-e5-small`](https://huggingface.co/intfloat/multilingual-e5-small) now!
- PostgresSQL now supports non-public schemas for tables.
- STT now appends spoken text in input instead of replacing it.
- Mobile Sync support for [AnythingLLM Mobile Beta](https://docs.useanything.com/mobile/overview)
- More translations including new Romanian translation
- New Agent [EXA SERP provider](https://exa.ai)
- New Vector Database [Chroma Cloud DB support](https://trychroma.com)

#### Bug Fixes:

- Fixed YT and XLSX folder name bug where title had odd characters
- Fix multimodal chats for OpenAI Compatible API
- Fix issue where microphone tooltip was duplicated
- Fix issue with API chat export endpoint
- Fix issue with bedrock agents implied role

#### Pinned Download Links

**Revision 1.8.5-r2:**

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.5-r2/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.8.5-r2/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.8.5-r2/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.8.5-r2/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.8.5-r2/AnythingLLMDesktop.AppImage)

### v1.9.0

*AnythingLLM Desktop v.1.9.0 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.9.0

#### `@agent` Overhaul & streaming ⚡️️

[Video](https://docs.useanything.com/images/product/changelog/1.9.0/agent-streaming.mp4)

When anythingllm first launched, the word "agent" was not in the vocabulary of the LLM world. Agents are quickly becoming the standard for building AI applications and also
the core expierience for interacting with LLMs.

For too long, due to the complexity of building agents, spotty tool call support, models that **cant even use tools** and more nerd stuff we
often had to settle an experience that was not really fun to use since 99% of the time you were just looking at at loading spinners waiting for the response.

##### The new agent experience is now here

- Streams tool calls and responses in real time (all providers, all models, any hardware)
- Agents can now real-time download and ingest files from the web (eg: link to PDF, excel, csv). Anything you would use a document can be read in real time by the agent.

*Upcoming:*

- Agent real-time API calling without agent flows
- Agent image understanding
- Agent system prompt passthrough + user context awareness
- Realtime file searching cross-platform default skill

#### Microsoft Foundry Local 🤖

![Microsoft Foundry Local](https://docs.useanything.com/_next/image?url=%2Fimages%2Fproduct%2Fchangelog%2F1.9.0%2Ffoundry-local.png&w=2048&q=75)
> **Warning:**
>
> Microsoft Foundry Local is currently in beta preview for Windows and MacOS.

Are you using [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local)? We have you covered.

AnythingLLM Desktop now supports a deep integration with Microsoft Foundry Local.

This means you can now use AnythingLLM Desktop to chat with your data on your Microsoft Foundry Local device.

- AnythingLLM will automatically start Microsoft Foundry Local when you start AnythingLLM Desktop, if installed.
- AnythingLLM will automatically unload models for you to keep your system resources free.
- Can pull optimized models based on your system hardware (CPU, GPU, NPU, etc.)

*btw*, **Foundry Local is free** and runs on Apple Silicon, Windows (x64 & ARM64), and Linux (x64 & ARM64)! Its worth checking out if you are looking for a local LLM solution.

*currently the model selection in AnythingLLM only shows currently downloaded models. So pulling of models still needs to be done via `foundry cli`*

You can download the latest version of [Microsoft Foundry Local here](https://github.com/microsoft/Foundry-Local/releases).

#### Linux improvements & ARM64 support 🖥️

Linux ARM64 is quickly becoming the most popular architecture for Linux devices and even personal compute devices like the upcoming [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/), Framework desktops, and
even people who tinker around with ARM based Raspberry Pi devices.

Additionally, we overhauled our [Linux Installation guide](https://docs.useanything.com/installation-desktop/linux) to make it more user friendly and easier to install.

- Auto created the `apparmor` rule to allow the app to run without any additional configuration. (Ubuntu only)
- Auto created the `.desktop` file so the app can be launched from the desktop and pinned to the launcher. (GNOME based desktops only)

#### Linux x64 and ARM64 now ships with Ollama 🚀

Linux for a long time has been lacking a local LLM support. We are happy to announce that we have now shipped Ollama (0.11.4) with Linux.

This does increase the size of the Linux AppImage, but it is a small price to pay for local LLM support with zero setup or installation required.

Happy chatting!

#### Major Improvements: 🚀

- All models and providers now support agentic streaming
- Microsoft Foundry Local integration
- Ephemerally scrape any web-resource via agent or uploader

##### Other still cool, but not major improvements

- Workspace/Thread Tooltips
- Resize chat area on paste in main chat UI
- Web-scraper can now handle URLs with no protocol
- Generic OpenAI Embedder allow artificial delay
- Anthropic computer-use tool updated to newest model and tool version.
- Ollama and LMStudio automatic model context window size detection
- Render HTML live in chat responses
- Update how chats are rendered in chat history viewer
- Youtube transcript improvements for ASR
- Custom HTTP Response timeout for ollama
- New System Prompt variables (workspace.name, workspace.id)
- Generic OpenAI Embedder allow artificial delay
- Report sources in API responses on last chunk in stream via developer API
- Add user agent to Generic OpenAI requests
- Patch folder GET request response code for developer API
- CometAPI integration
- Portuguese translations
- Export JSON/JSONL with attachments from Workspace Chats viewer

#### Bug Fixes:

- Upgraded core Electron version
- Migrated OpenAI inteface to Responses API
- Fixed orphan docs bug with filenames that have spaces being pruned
- Update UI icons to be normalized in spacing under chat messages
- PGVector metadata sanitization to prevent bad byte in `jsonb` vector metadata field
- Fix Dell Pro AI Studio default URL

#### Deprecated Feature Notices:

- NVIDIA NIM is being **phased out** of AnythingLLM Desktop starting with v.1.9.0 and will be removed in the next version or patch.

#### Pinned Download Links

**Revision 1.9.0:**

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.9.0/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.9.0/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.9.0/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.9.0/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.9.0/AnythingLLMDesktop.AppImage)
- Linux (ARM64) [Download](https://cdn.anythingllm.com/legacy/1.9.0/AnythingLLMDesktop-Arm64.AppImage)

### v1.9.1

*AnythingLLM Desktop v.1.9.1 Changelog*

**Source:** https://docs.useanything.com/changelog/v1.9.1

#### Notable Improvements: 🚀

**Windows Installer Optimization**  
Fixed bug where installation time on Windows would take a very long time to complete. Installation time is now significantly faster.

**MCP Support Improvements**  
Refactored MCP support. Patches issues with MCPs not starting or not working correctly.

**Chat Input Persistence**  
Chat input now persistent when navigating between workspaces if not sent when navigating away.

**Realtime YouTube Scraping**
Realtime scraping of YouTube videos is now supported.

> Ask `@agent` to scrape a YouTube video and it will be used to answer your question.

#### Other Improvements

- Internal Ollama version bumped to [0.13.0](https://github.com/ollama/ollama/releases/tag/v0.13.0)
- Managed NVIDIA NIM has been removed from AnythingLLM Desktop.
- Dell Pro AI Studio model URL updated to new specification.
- Improved error handling for MCPs not starting or not working correctly.
- General language improvements and fixes.
- Keyboard navigation of slash command when showing slash command list.
- Paperless NGX data connector support
- Agent workspace system prompt can now use system variables for variable expansion.
- Use `eval_duration` from Ollama for accurate TPS calculations.
- Add SerpAPI web search as agent web-search provider
- Support AWS Bedrock API key connection method
- ZAI LLM provider support
- Anthropic prompt caching and config
- Ability to set global default prompt for new workspaces
- Add base64 document attachment support for chat API
- SSL bypass for local confluence
- GiteeAI LLM provider support
- OpenRouter Embedder support
- Ollama batch embedding support

#### Bug Fixes

- Fixed runtime issue with Ollama and LMStudio model caching causing model list to be empty or incorrect.
- Fixed bug where the MCP panel was not scrollable for certain models.
- Fix relevance score not showing for Astra, QDrant, Zilliz, and Weaviate citations
- EPub upload for certain file layouts were failing on upload - this is now fixed.
- Fixed bug where Gemini thinking output was not showing in chat or hanging the response.
- Fix infinite loop logic in GitLabLoader
- Add Svelte renderer to markdown output
- Disable Prisma CLI telemetry
- Patch Ollama broken thought output from chat template update
- Extend HTTP TTL on extension requests for timeout
- Fix undefined result in llm-instruction blocks
- Fix directOutput causing hanging response for agent flow calls when streaming
- Fixed Chroma cloud limitations on payload size for upsert of embeddings.

#### Pinned Download Links

**Revision 1.9.1:**

- Mac (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.9.1/AnythingLLMDesktop.dmg)
- Mac (Apple Silicon) [Download](https://cdn.anythingllm.com/legacy/1.9.1/AnythingLLMDesktop-Silicon.dmg)
- Windows [Download](https://cdn.anythingllm.com/legacy/1.9.1/AnythingLLMDesktop.exe)
- Windows (ARM) [Download](https://cdn.anythingllm.com/legacy/1.9.1/AnythingLLMDesktop-Arm64.exe)
- Linux (x86\_64) [Download](https://cdn.anythingllm.com/legacy/1.9.1/AnythingLLMDesktop.AppImage)
- Linux (ARM64) [Download](https://cdn.anythingllm.com/legacy/1.9.1/AnythingLLMDesktop-Arm64.AppImage)


---
