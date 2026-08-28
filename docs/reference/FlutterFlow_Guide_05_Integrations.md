# FlutterFlow Documentation — Complete Guide (Part 5 of 7: Integrations: Auth, Firebase, Supabase, Payments, Maps, Search, Ads)

> **Note for NotebookLM:** This is one part of a multi-file Markdown export of the official FlutterFlow documentation, cleaned and reorganized for use as a NotebookLM source set to build a structured FlutterFlow learning plan. Import all parts together as separate sources in the same NotebookLM notebook.

- **Source:** https://docs.flutterflow.io (crawled via https://docs.flutterflow.io/llms-full.txt)
- **This file's page count:** 55
- **Total pages across the full guide (all 7 parts):** 369
- **Date generated:** 2026-07-18
- **Part:** 5 of 7 — Integrations: Auth, Firebase, Supabase, Payments, Maps, Search, Ads
- **Other parts in this guide:**
  - Part 1: Fundamentals, Account, CLI & Builder UI (`FlutterFlow_Guide_01_Fundamentals_and_Platform.md`)
  - Part 2: Core Concepts: UI Building, Actions, Animations, Navigation, Custom Code (`FlutterFlow_Guide_02_CoreConcepts.md`)
  - Part 3: Widgets Reference (`FlutterFlow_Guide_03_WidgetsReference.md`)
  - Part 4: Resources: Data, Backend Query, Forms, Functions & Projects (`FlutterFlow_Guide_04_ResourcesDataAndLogic.md`)
  - Part 6: Deployment, Testing, Marketplace & Exporting Code (`FlutterFlow_Guide_06_DeploymentTestingMarketplace.md`)
  - Part 7: Troubleshooting Guides (`FlutterFlow_Guide_07_Troubleshooting.md`)

## Table of Contents

**Integrations (Auth, Firebase, Supabase, APIs, Payments, etc.)**

- [AdMob](#admob)
- [AI Agents](#ai-agents)
- [Authentication Methods Overview](#authentication-methods-overview)
- [Overview](#overview)
- [Custom Authentication](#custom-authentication)
- [Anonymous Login](#anonymous-login)
- [Apple Login](#apple-login)
- [Common Auth Actions](#common-auth-actions)
- [Email Login using Firebase](#email-login-using-firebase)
- [Facebook Login](#facebook-login)
- [GitHub Login](#github-login)
- [Google Login](#google-login)
- [Enabling Firebase Auth in FlutterFlow](#enabling-firebase-auth-in-flutterflow)
- [JWT Token Authentication](#jwt-token-authentication)
- [Phone Login](#phone-login)
- [Authentication: Generated Code](#authentication-generated-code)
- [Apple Login](#apple-login-2)
- [Authentication Actions](#authentication-actions)
- [Email Authentication](#email-authentication)
- [Google Login](#google-login-2)
- [Initial Setup](#initial-setup)
- [Tokens: Types and Lifespans](#tokens-types-and-lifespans)
- [Creating Collections](#creating-collections)
- [Creating Subcollections](#creating-subcollections)
- [Firestore Actions](#firestore-actions)
- [Firestore Content Manager](#firestore-content-manager)
- [Firestore Rules](#firestore-rules)
- [Cloud Firestore](#cloud-firestore)
- [Refresh Database Request [Action]](#refresh-database-request-action)
- [SQLite](#sqlite)
- [Supabase Database Actions](#supabase-database-actions)
- [Import from FF Designer](#import-from-ff-designer)
- [Firebase Storage Library](#firebase-storage-library)
- [Storage Rules](#storage-rules)
- [App Check](#app-check)
- [Connect to Firebase](#connect-to-firebase)
- [Firebase Crashlytics](#firebase-crashlytics)
- [Performance Monitoring](#performance-monitoring)
- [Remote Config](#remote-config)
- [Gemini](#gemini)
- [Google Analytics](#google-analytics)
- [Maps & Places APIs](#maps-places-apis)
- [Google Maps Widget](#google-maps-widget)
- [Move Map Center [Action]](#move-map-center-action)
- [Place Picker Widget](#place-picker-widget)
- [Static Map Widget](#static-map-widget)
- [Launch Map](#launch-map)
- [Mux Livestream](#mux-livestream)
- [Braintree](#braintree)
- [RazorPay](#razorpay)
- [RevenueCat](#revenuecat)
- [Stripe](#stripe)
- [Algolia](#algolia)
- [Simple Search](#simple-search)
- [Supabase Setup](#supabase-setup)

---

## Integrations (Auth, Firebase, Supabase, APIs, Payments, etc.)

### AdMob {#admob}

*Learn how to add AdMob in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/ads/admob

Adding ads to your FlutterFlow project can be a powerful way to monetize your app. FlutterFlow supports the integration of popular advertising platforms like [Google AdMob](https://admob.google.com/home/), making it easy for you to add [Banner](https://developers.google.com/admob/android/banner) and [Interstitial](https://developers.google.com/admob/android/interstitial) ads to your projects. This guide provides a step-by-step walkthrough for integrating ads within your FlutterFlow project.

#### Setup AdMob

Setting up an AdMob involves creating AdMob apps for both Android and iOS, obtaining the app keys, and configuring some optional settings.

##### 1. Creating AdMob app

Visit the AdMob homepage and [sign up](https://admob.google.com/home/) using your Google account. Once logged in, create an Android and iOS app with the necessary details, such as platform and app name.

> **Info:** You should create two AdMob apps to display ads in both Android and iOS versions.

##### 2. Adding keys to FlutterFlow

You must add the App keys to your FlutterFlow project that will allow your app to communicate with the AdMob server.

To do so, get the app key from the AdMob App Settings, navigate to **Settings and Integrations** in FlutterFlow, and add the Android and iOS app keys under **AdMob** integration settings.

##### 3. Configure optional settings

Below are some AdMob settings (under **Settings and Integrations** menu) that you might need to configure based on your app and target audience.

![admob-settings](https://docs.flutterflow.io/assets/images/admob-settings-78d7d353740075c5d389a7af51222ae3.avif)

* **Show Test Ads**: Test ads are placeholders provided by AdMob that simulate real ads. To enable test ads during development, enable this option. This allows you to click on ads without charging Google advertisers and prevents your account from being flagged for invalid activity. Once your app is ready for production, you can disable this setting to serve real ads.

* **Show GDPR Consent Dialog at App Launch**: To display the GDPR consent dialog for users in the European Union (EU), enable this option. **Note that** the dialog will only appear if the user is from the EU and you created a [European regulations message](https://support.google.com/admob/answer/10113207).

* **Child-Directed Settings**: To indicate that your content is directed towards children, enable this option. This will ensure that Google treats your content as child-directed when making ad requests.

* **Users Under the Age of Consent**: This setting allows you to comply with privacy regulations for users in the European Economic Area (EEA) who are under the age of consent. It ensures that ad requests are appropriately handled, limiting data collection and targeting to meet legal requirements. This is important to protect user privacy and to avoid penalties for non-compliance.

* **Ad Content Filtering**: To filter the type of ads displayed, select the appropriate content rating. AdMob will ensure that ads returned for these requests have a content rating at or below the level selected.

  These are the levels you can set:

  * **G (General Audience)**: Suitable for all audiences, with no adult content or explicit themes.
  * **PG (Parental Guidance)**: Ads may contain mild content, suitable for children with parental supervision.
  * **T (Teen)**: Ads with content appropriate for teenagers; may include some mature topics.
  * **MA (Mature Audience)**: Ads intended for adults, which may include strong themes or explicit content.

Once the setup is completed, you can start to display [AdBanner](https://docs.flutterflow.io/integrations/ads/admob#adbanner) or [Interstitial ads](https://docs.flutterflow.io/integrations/ads/admob#interstitial-ad) in your app.

#### AdBanner

The **AdBanner** widget displays advertisement banners within your app. It can feature text, images, and rich media, including video ads.

Here's an example for AdBanner widget with a test ad: ![adbanner-widget-with-test-ad](https://docs.flutterflow.io/assets/images/adbanner-widget-with-test-ad-3e70c55ef47b3ef473610ead643a2be6.avif)

To display an **AdBanner** from AdMob, follow these steps:

##### Adding AdBanner widget

First, add the **AdBanner** widget from the **Base Elements**. Next, create a new Banner Ad unit in AdMob, then copy and paste its **unit ID** into FlutterFlow. The Ad unit ID is a unique identifier assigned to each ad created in AdMob.

> **Info:** By default, ad banners are set to a dimension of 100 (width) x 50 (height).

> **Tip:** While building your app, clicking on too many ads may cause your AdMob account to be flagged for invalid activity. To avoid this, it's recommended to enable **Test Ads** during development.

##### Testing AdBanner

Ads cannot be tested in Test or Run Mode. They can only be tested on a real device or emulator. To do this, you can use [Local run](https://docs.flutterflow.io/testing/local-run) or [download the code](https://docs.flutterflow.io/flutterflow-cli/exporting) and run it in your IDE.

#### Interstitial Ad

An **Interstitial Ad** is a type of full-screen ad that appears at natural transitions or pauses in an app, such as when switching between pages. Unlike banner ads, which stay on-screen while users interact with the app, interstitial ads are shown at key moments and are designed to be closed before the user can continue. They typically support multiple formats, including:

* **Image ads**
* **Video ads**
* **Rich media (interactive ads)**

To display an interstitial ad in FlutterFlow, you need to use the **Load Interstitial Ad** and **Show Interstitial Ad** actions together. Here's how it works:

![interstitial\_ad\_flow](https://docs.flutterflow.io/assets/images/interstitial_ad_flow-37b9a4643342b96a27d51145de51744a.png)

First, load the ad using the **Load Interstitial Ad** action, then display it with the **Show Interstitial Ad** action. Once the ad is shown, users can choose to either interact with it or dismiss it. After the ad is dismissed, it cannot be displayed again, so you'll need to load a new ad. The newly loaded ad will then be ready for display the next time you trigger the **Show Interstitial Ad** action.

> **Warning:** ***Allow sufficient time between calling Load Interstitial Ad and Show Interstitial Ad to ensure the ad has fully loaded.*** Since loading may take some time, it's recommended to load the ad well in advance to avoid display issues. For example, if you want to show an ad when a widget is tapped, you should load the ad as soon as the page loads. If the ad isn’t loaded in time, it won’t be displayed.

Let's see an example displaying the interstitial ad when you navigate to the next page:

![interstitial-ad-flow-2](https://docs.flutterflow.io/assets/images/interstitial-ad-flow-2-8f38970216bede167890e5f3434036c9.avif)

On the first page, trigger the **Load Interstitial Ad** action as soon as the page loads. Then, on a widget tap, add the **Show Interstitial Ad** action. The result of whether the ad is dismissed will be stored in the `interstitialAdSuccess` variable. If this value is true (the ad was dismissed), you can load a new ad and proceed to navigate to the next page.

Here are the step-by-step instructions:

##### Getting Ad Unit ID

The Ad Unit ID is the unique identifier given to every ad on Admob. You can get this by creating a new Interstitial ad unit from your Admob account. You’ll need this ID when loading the ad.

To get the ad unit ID, go to the AdMob dashboard, select your app under **Apps**, and create an **Interstitial** ad unit by following the steps under **Ad units**. Once created, copy the ad unit ID, and repeat the process for the iOS version if needed.

##### Loading Ad on Page Load

Always load the ad in advance before you intend to display it. This ensures the ad has enough time to fully load its content, whether it's an image or video, before being shown. The best place to do it is the **On Page Load**.

To load the ad when the page loads, select the page, add the **On Page Load** action trigger, and set the action to **Load Interstitial Ad**. Enter the iOS and Android **Ad Unit ID**s you obtained in [step 1](https://docs.flutterflow.io/integrations/ads/admob#getting-ad-unit-id).

> **Tip:** While building your app, clicking on too many ads may cause your AdMob account to be flagged for invalid activity. To avoid this, it's recommended to enable **Test Ads** during development.

##### Display Interstitial Ad

Now, you can display the ad using the **Show Interstitial Ad** action. This action returns `interstitialAdSuccess` (as an action output variable), which can be used to check if the user has dismissed the ad. If the ad is dismissed, load a new one and then proceed to navigate to the next page.

#### Best Practices

To maximize the effectiveness of AdMob ads in your app while maintaining a positive user experience and complying with AdMob policies, follow these overall best practices:

* **Use Test Ads During Development**: Always enable Test Ads during development to avoid invalid traffic and protect your AdMob account from being flagged or banned.
* **Comply with AdMob Policies**: Adhere strictly to AdMob’s guidelines regarding ad placement, frequency, and user interaction. This includes avoiding accidental clicks and ensuring that ads are not too intrusive. Learn more about [AdMob Policies & Restrictions](https://support.google.com/admob/answer/6128543?hl=en).
* **Respect User Privacy**: Follow data privacy regulations (e.g., GDPR, CCPA) and give users control over their ad preferences by integrating privacy options. Learn more about [AdMob Privacy & Consent](https://support.google.com/admob/answer/7676680?hl=en)

##### AdBanner Best Practices

* **Strategic Placement**: Position AdBanner widgets in non-intrusive areas of the app, such as at the bottom or top of the screen, so they don’t interfere with the user’s interaction with the app’s core content. Learn more about [Banner Ad Placement Guide](https://support.google.com/admob/answer/6128877?hl=en).
* **Avoid Clickbait**: Make sure the banner ad does not blend too much with the app content. Users should easily differentiate between the ad and the app’s content to avoid accidental clicks.

##### Interstitial Ad Best Practices

* **Loading Ads in Advance**: Interstitial ads should be loaded before they are needed, typically in the background, to avoid delays when it’s time to display the ad.
* **Displaying at the Right Time**: Ensure ads are shown at natural transition points. Showing ads in the middle of an activity can disrupt the user experience.
* **Monitoring Frequency**: Overuse of interstitial ads can lead to a negative user experience. It's recommended to show them sparingly and at appropriate times.
* **Test Before Production**: Use test ads during development to ensure that your implementation is correct and that you don’t accidentally trigger invalid ad interactions, which could lead to an AdMob account suspension.

---

### AI Agents {#ai-agents}

*Learn how to add AI Agents for chat, image generation, video generation, text-to-speech, and speech-to-text in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/ai-agents

AI Agents in FlutterFlow enable you to integrate AI-powered chat, image generation, video generation, text-to-speech, and speech-to-text directly into your app. An AI Agent is a configurable AI service that you define in FlutterFlow and then call from your app actions.

You can build agents powered by providers such as **OpenAI**, **Google**, **Anthropic**, and **ElevenLabs**. Depending on the agent kind, you can create a conversational assistant, convert text into speech, transcribe audio into text, generate images from prompts, or generate video using the latest supported models.

Here are some examples of AI Agents:

* **AI Stylist:** In an e-commerce fashion app, an AI agent analyzes photos of clothing items users upload from their wardrobes and provides styling tips based on color combinations, styles, seasons, and individual preferences.
* **Smart Recipe Assistant:** An AI agent in a cooking app that suggests recipes based on ingredients users have, dietary restrictions, or meal preferences, and offers interactive cooking guidance.
* **Marketing Image Generator:** An image generation agent that creates product thumbnails, social posts, or campaign visuals from a prompt.
* **Language Learning App:** A text-to-speech agent reads practice sentences aloud so learners can hear pronunciation in a natural voice.
* **Meeting Notes App:** A speech-to-text agent transcribes uploaded meeting recordings or voice notes into searchable text.
* **Social Media Campaign Builder:** A video generation agent creates short promotional clips from prompts for product launches, announcements, or ads.

Prerequisite

Before you begin setting up AI Agents, make sure you:

1. Complete all the steps in [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase). Note that, while setting up, make sure to follow step number 5 and 8 carefully from [**Allow FlutterFlow to Access Your Project**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#allow-flutterflow-to-access-your-project) section to properly add the **Cloud Functions Admin** role to **<firebase@flutterflow.io>** user.
2. Upgrade your Firebase project to the [**Blaze Plan**](https://firebase.google.com/pricing), as we rely on [**Firebase Cloud Functions**](https://firebase.google.com/docs/functions) to handle AI-related communication securely.
3. Get an API key for the provider you want to use, such as [**OpenAI**](https://platform.openai.com/api-keys), [**Anthropic**](https://platform.claude.com/settings/keys), [**Google AI Studio**](https://aistudio.google.com/app/apikey), or [**ElevenLabs**](https://elevenlabs.io/docs/api-reference/authentication).

#### Create AI Agent

To create an AI agent, select the **Agents** tab from the left-side navigation menu, then click the **(+)** button. Provide a descriptive **Agent Name** (e.g., "ShoppingAssistant") and click **Create**.

> **Info:** You can create one AI Agent on the Basic plan and unlimited AI Agents on the Growth plan and higher.

After creating the agent, start with the common agent settings:

* **Agent Kind**: Select what the agent should do. Supported kinds include **Chat**, **Image Generation**, **Text-to-Speech**, **Speech-to-Text**, and **Video Generation**.
* **Internal Description**: Add a short note describing what the agent is for. This is for your own reference and is not sent to the AI model.

> **Note:** The selected agent kind determines which model settings and app actions are available. For example, a **Chat** agent is used with the **Send Message** action, while an **Image Generation** agent is used with the **Generate Image** action.

#### Chat

Use a **Chat** agent when your app needs a conversational assistant that can respond to users with text, markdown, or structured JSON. Chat agents are useful for support bots, tutors, product recommenders, content assistants, and agents that analyze user-provided text, images, PDFs, audio, or video.

The chat settings are as follows:

**System Message**

Defines the AI’s role and how it should behave when responding to users. For instance, “You are an AI fashion stylist…” tells the agent to respond like a professional stylist, focusing on outfits, colors, and suggested combinations.

**Preloaded Messages**

Preloaded messages allow you to set predefined interactions between the AI and users. It is useful for training the agent with example responses to ensure it understands the expected format of answers.

* **Role**: Specifies whether the message is from the **User** or the **Assistant**.

* **Message**: The actual text input that either the user or assistant might send.

* **Example:**

  * **Role = User:** "What outfit suits my medium skin tone for a sunny day?"
  * **Role = Assistant:** "For your medium skin tone on a sunny day, a pastel-colored top with white chinos would look fantastic! Consider adding sunglasses and comfortable footwear."

> **Tip:** It is always recommended to include at least one sample conversation with both a user message and an assistant response.

**Model Settings**

* **Provider**: Allows you to select the AI vendor for this agent. Supported chat providers include **OpenAI**, **Google**, and **Anthropic**. * **OpenAI & Anthropic**: If you choose OpenAI or Anthropic, FlutterFlow will create a [Cloud Function](https://firebase.google.com/docs/functions) in Firebase to relay requests to the AI API securely. Hence, your Firebase project must be on a [Blaze](https://firebase.google.com/pricing) plan (paid) to deploy the necessary cloud function. **Note that** the deployed cloud function will only be accessible to authenticated users.

  * **Google**: When selecting Google as your provider for chat agents, you need to enable the following in your Firebase project. * [**Firebase Authentication**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup): This ensures secure interactions between users and your AI agents.
    * [**Vertex AI**](https://firebase.google.com/docs/vertex-ai): Vertex AI is Google's comprehensive AI platform used to manage and deploy machine learning models. FlutterFlow internally uses the [`firebase_vertexai`](https://pub.dev/packages/firebase_vertexai) package to integrate Google's AI models within your Firebase-connected project.

* **Model**: Choose from the list of available models for the given provider. Models differ in capabilities, supported parameters, and cost structure.

* **API Key:** Enter your provider’s API key when the selected provider or model requires one. FlutterFlow securely stores this key within the deployed cloud function to ensure it remains hidden from end-users and network requests.

**Request Options**

Define the types of inputs users can send to the AI agent. You can enable one or more of the following options:

* **Text**: Allows users to send written messages, questions, or prompts.
* **Image**: Enables users to upload photos for the AI to analyze visual content, such as objects, styles, or scenes.
* **PDF** (Anthropic and Google Agent only): Lets users submit PDF documents, allowing the AI to extract and interpret information from files like resumes, reports, or forms.
* **Audio** (Google Agent only): Supports voice input, enabling users to record or upload audio clips for transcription, sentiment analysis, or voice-based commands.
* **Video** (Google Agent only): Allows users to submit video files, enabling the AI to analyze visual elements.

Selecting multiple input types makes it easier for users to clearly communicate what they need. Instead of relying only on text descriptions, users can combine inputs. For instance, in an AI Stylist agent, enabling both Text and Image allows users to either describe their outfits in words or upload clothing photos for personalized analysis.

**Response Options**

Defines the type of output you want from the agent. You can select from the following options:

* **Text**: Returns plain text responses.
* **Markdown**: Allows richer formatting (headings, lists, links) if you display content as markdown. For example, an FAQ chatbot can use formatted bullet points, bold text, or italic text to highlight key information.
* **JSON**: Returns structured data, which can be parsed programmatically. For example, a restaurant finder app might need structured data, e.g., `{ name: 'Pizza Palace', distance: '2.4 miles' }` to display a dynamic map.

**Model Parameters**

Here, you can fine-tune how the agent generates responses.

* **Temperature**: Controls how creative or random the AI’s responses can be on a scale of 0 to 1. A lower value (e.g., 0.1) makes responses more factual and consistent. A higher value (e.g., 1.0) makes responses more creative and varied (e.g., brainstorming ideas).
* **Max Tokens**: Limits the total number of tokens used, including both the user's request and the agent's response. Adjusting this helps manage costs and ensures concise interactions.
* **Top P**: Another technique for controlling the variety of words the AI considers. Typically kept at default unless you want fine-tuned sampling control.

For example, in a **Blog-Writing Assistant**, you might set a moderate to high temperature for creative phrasing and a high max tokens limit for detailed paragraphs. Conversely, a **Financial Chatbot** would benefit from a lower temperature to deliver consistent, accurate, and stable responses without unnecessary creativity.

##### Send Message \[Action]

The **Send Message** action allows your app to pass user input (such as text or images) to a selected AI Agent and receive a response based on its system instructions, preloaded messages, and model settings. For example, you can add this action when a user taps a “Send” button after typing in a text field. The AI Agent can then reply based on its system instructions, preloaded messages, and model settings.

You can configure the following options for this action:

* **Select Agent**: Here, you select the specific AI Agent you previously configured.
* **Conversation ID**: The Conversation ID is a unique identifier you assign to maintain context and continuity across multiple interactions within the same conversation. Using a consistent ID (e.g., `user123_AIStylist_202503181200`) allows the AI to remember past interactions and keep conversations coherent and contextual.
* **Text Input**: This is where you specify the user's message or input text that the AI agent will process. Typically, this input comes from a widget state (e.g., TextField).
* **Image Input**: If your agent supports image processing, you can provide an image.
* **Audio Input**: If your agent supports audio processing, you can pass audio files.
* **Video Input**: If your agent can analyze video content, provide a video file.

> **Info:** * You can send media files either from [**network URL**](https://docs.flutterflow.io/concepts/file-handling/displaying-media#network) or a [**local device**](https://docs.flutterflow.io/concepts/file-handling/displaying-media#uploaded-file) storage.
* For non-Google agents, we only support network URLs for now. To pass media files from your device, [**upload it first to cloud storage**](https://docs.flutterflow.io/concepts/file-handling/uploading-files#upload-or-save-media-action) and then provide its generated URL.

- **Action Output Variable Name**: This field stores the AI agent's response to let you display the response to users or process it further.

![ai-agent-send-message-action.avif](https://docs.flutterflow.io/assets/images/ai-agent-send-message-action-6da8af9808becbc25e86f651e78cbf36.avif)

##### Clear Chat History \[Action]

The **Clear Chat History** action allows you to clear the remembered context for a Chat agent. It takes the **Conversation ID** and stops referencing the existing thread ID when you next send a message.

![ai-agent-reset-action.avif](https://docs.flutterflow.io/assets/images/ai-agent-reset-action-8cce58c7726c2cb53e5ce5db6adcbdea.avif)

#### Text-to-Speech

Use a **Text-to-Speech** agent when your app needs to convert text into spoken audio. This is useful for reading messages aloud, generating narration, creating voiceovers, or helping users hear content in a selected voice.

Text-to-speech settings include:

* **Provider**: The text-to-speech provider, such as ElevenLabs.
* **Model**: The speech generation model, such as Eleven Flash v2.5.
* **API Key**: The provider API key used by the deployed agent function.
* **Voice ID**: The default voice used to generate speech. Actions can override this per call.
* **Output Format**: The audio output format, such as MP3.
* **Stability**: Controls how consistent the voice output should be.
* **Similarity Boost**: Controls how closely the generated speech should match the selected voice.
* **Speed**: Controls the speaking speed.

![AI Agent text-to-speech settings](https://docs.flutterflow.io/assets/images/ai-agent-tts-15504ccad9953eed64be954eaf9bd4db.avif)

##### Generate Speech \[Action]

The **Generate Speech** action allows your app to send text to a Text-to-Speech agent and receive generated audio. You can configure the following options for this action:

* **Select TTS Agent**: Select the Text-to-Speech agent you previously configured.
* **Text Input**: The text to convert into speech.
* **Voice ID Override (optional)**: Optionally override the agent's default voice ID for this call.
* **Action Output Variable Name**: Stores the generated speech result so you can play it or use it in later actions.

![AI Agent generate speech action](https://docs.flutterflow.io/assets/images/ai-agent-tts-action-61ebd60b29bdc583d9daea5c3d63ee5b.avif)

#### Speech-to-Text

Use a **Speech-to-Text** agent when your app needs to convert audio into text. This is useful for transcribing voice notes, meeting recordings, support messages, uploaded audio files, or audio from a URL.

Speech-to-text settings include:

* **Provider**: The transcription provider, such as ElevenLabs.
* **Model**: The transcription model, such as Scribe v2.
* **API Key**: The provider API key used by the deployed agent function.

![AI Agent speech-to-text settings](https://docs.flutterflow.io/assets/images/ai-agent-stt-d3e0ac06cd0860241d9ec9e9170e99aa.avif)

##### Transcribe Audio \[Action]

The **Transcribe Audio** action allows your app to send audio to a Speech-to-Text agent and receive the transcribed text. You can configure the following options for this action:

* **Select STT Agent**: Select the Speech-to-Text agent you previously configured.
* **Audio Source**: Choose where the audio comes from. Supported sources include **Audio URL** and **Uploaded Audio File**.
* **Language Code (optional)**: Provide a language code, such as `en`, to guide transcription.
* **Action Output Variable Name**: Stores the transcribed text so you can display it or use it in later actions.

![AI Agent transcribe audio action](https://docs.flutterflow.io/assets/images/ai-agent-stt-action-cf19eac005869f09005de4169fe54f6c.avif)

#### Image Generation

Use an **Image Generation** agent when your app needs to create images from a text prompt. This is useful for generating product thumbnails, profile artwork, backgrounds, campaign visuals, or other app-specific images.

You can configure image generation with supported providers such as **Google** or **OpenAI**, choose the model, add the API key, and set a default image size.

Image settings include:

* **Provider**: The provider used to generate images, such as Google or OpenAI.
* **Model**: The image generation model, such as Gemini image models or GPT Image models.
* **API Key**: The provider API key used by the deployed agent function.
* **Image Size**: The default image size for Generate Image calls. Actions can override this per call.

![AI Agent image generation settings](https://docs.flutterflow.io/assets/images/ai-agent-image-gen-467092e7d216240586d252a2bb8d9262.avif)

##### Generate Image \[Action]

The **Generate Image** action allows your app to send a prompt to an Image Generation agent and receive a generated image. You can configure the following options for this action:

* **Select Image Generation Agent**: Select the Image Generation agent you previously configured.
* **Prompt**: The text prompt that describes the image to generate.
* **Size Override**: Optionally override the agent's default image size for this call. You can select **Use Agent Default** or choose a supported size such as **Square (1024 x 1024)**, **Portrait (1024 x 1536)**, or **Landscape (1536 x 1024)**.
* **Action Output Variable Name**: Stores the generated image result so you can display it or use it in later actions.

![AI Agent generate image action](https://docs.flutterflow.io/assets/images/ai-agent-image-gen-action-ac750333f6ba958387b3344a18c3c3de.avif)

#### Video Generation

Use a **Video Generation** agent when your app needs to generate video from a text prompt. This is useful for creating short clips, campaign visuals, animated concepts, visual storyboards, or social media assets.

Video generation settings include:

* **Provider**: The video generation provider, such as Google.
* **Model**: The video generation model, such as Veo 3.1.
* **API Key**: The provider API key used by the deployed agent function.
* **Aspect Ratio**: The default video aspect ratio for Generate Video calls. Actions can override this per call.
* **Duration**: The target video duration.

![AI Agent video generation settings](https://docs.flutterflow.io/assets/images/ai-agent-video-gen-8b8cdeb1a67fcb3be18b72776bc28612.avif)

> **Info:** Video generation can take 30 seconds to several minutes. The cloud function keeps the connection open while the provider job runs.

##### Generate Video \[Action]

The **Generate Video** action allows your app to send a prompt to a Video Generation agent and receive a generated video. You can configure the following options for this action:

* **Select Video Generation Agent**: Select the Video Generation agent you previously configured.
* **Prompt**: The text prompt that describes the video to generate.
* **Aspect Ratio Override**: Optionally override the agent's default aspect ratio for this call. You can select **Use Agent Default** or choose a supported aspect ratio such as **Landscape (16:9)**, **Portrait (9:16)**, or **Square (1:1)**.
* **Action Output Variable Name**: Stores the generated video result so you can display it or use it in later actions.

![AI Agent generate video action](https://docs.flutterflow.io/assets/images/ai-agent-video-gen-action-3d97b3cfcebd8f28675e578436697c0d.avif)

#### Deployment Settings

Here, you can fine-tune how your AI Agent is executed. These settings help balance performance, security, and cost for your use case.

* **Require Authentication**: By default, this is set to ON to restrict access to only authenticated Firebase users. When set to OFF, anyone can call your agent, which may pose a security risk.
* **Timeout (seconds)**: Defines how long the agent function can run before being terminated. For example, a value of `60` allows the function up to 60 seconds to complete. Increase if your agent performs long-running operations or processes complex logic.
* **Memory**: Allocates memory for your agent. Higher memory improves performance for heavy workloads but may cost more. For example, choose `256MB` for standard tasks or `512MB+` for agents handling large data or complex logic.
* **Min Instances**: The number of instances kept warm and ready at all times. Set to `0` to minimize costs. For example, setting `Min Instances` > 0 can improve response speed by avoiding cold starts, but this incurs additional cost. Set to `0` for development or low-traffic environments.
* **Max Instances**: The maximum number of instances that can run simultaneously. Helps scale under load and avoid throttling. For example, setting `Max Instances = 10` limits concurrency to 10 requests.

Once configured, click the **Publish** button to make it live.

For non-Google Agents

After you successfully deploy the agent, changes to its configuration, such as modifying the system message, model, or temperature, require you to redeploy the agent. For Google chat agents, the configuration is stored on the client side, so redeployment isn't necessary.

---

### Authentication Methods Overview {#authentication-methods-overview}

*Authentication enables users to create accounts and log into your app, establishing a secure,*

**Source:** https://docs.flutterflow.io/integrations/authentication-methods

Authentication enables users to create accounts and log into your app, establishing a secure, verified connection. In the dynamic world of applications, users can authenticate using various methods, including **Email Login**, **OAuth**, and **phone authentication**, among others.

While each method has its unique features and advantages, they all share a common goal: enhancing security and verifying the identity of users to provide a safe and personalized user experience.

#### Email Login Authentication

The Email Login method involves users registering with an email address and password.

Security in this approach is enhanced through **Email Verification**, where a link or code is sent to the user's email to confirm ownership. This step prevents unauthorized account creation and ensures that the user can recover their account and receive important communications.

![email-login.png](https://docs.flutterflow.io/assets/images/email-login-3b784eac7a0f93e27a53e54d7bdb9bdb.png)

#### OAuth (Open Authorization)

**OAuth** is a popular authentication protocol that enables users to authorize one application to interact with another on their behalf without revealing their password. This method is commonly used to allow applications to access service features or user information from other services, such as logging into a third-party app using Google or Facebook credentials.

By using OAuth, the user's login credentials stay secure with the original service provider, and only specific permissions are granted to third-party apps via access tokens. This approach minimizes the risk of exposing sensitive user data and streamlines the login process across various platforms.

#### Phone Authentication

Another method is phone authentication, where a user's phone number is used as a form of identity verification. Upon registering or logging in, the user receives a text message with a verification code that must be entered to proceed. This method leverages the security of mobile networks and the uniqueness of phone numbers to ensure that the person attempting access is the legitimate owner of the account.

![phone-login.png](https://docs.flutterflow.io/assets/images/phone-login-2eb5b670e54ed779af7155996897dc7b.png)

#### Anonymous Authentication

Anonymous Authentication allows users to interact with your application without signing in with permanent credentials, by creating temporary anonymous accounts. This method is beneficial for users who want to test services before committing to creating an account. If a user decides to sign up later, their anonymous account can be upgraded to a regular account, preserving their data and interactions.

Each anonymous session is typically isolated, with strict permissions to prevent access to sensitive features or user data. When upgrading to a full account, secure practices are used to link the anonymous data to the new authenticated profile, ensuring that no data leakage or unauthorized access occurs during the transition.

Each authentication method aims to balance user convenience with high security, ensuring that personal and sensitive data remains protected while providing a seamless user experience.

![anon-user.png](https://docs.flutterflow.io/assets/images/anon-user-14e3fb5dbb8951bf1fbb1c8e7ad29b20.png)

---

### Overview {#overview}

*Learn about integrating various authentication services like Firebase, Supabase, and Custom Authentication in FlutterFlow.*

**Source:** https://docs.flutterflow.io/integrations/authentication-types

FlutterFlow provides native support for a variety of Authentication Services, including **Firebase**, **Supabase**, and **Custom Authentication** options. To integrate these services into your app, simply navigate to 'App Settings,' select 'Authentication,' and then choose your preferred service. From there, you can set up initial pages for both entry and logged-in states. Follow any additional steps as necessary to complete the setup.

#### Firebase Authentication

In FlutterFlow, you can seamlessly connect with **Firebase** and utilize the available authentication methods.

Firebase Authentication integrates tightly with other Firebase services, leveraging industry standards like OAuth 2.0 and OpenID Connect. This makes it highly adaptable for use with your custom backend, ensuring a secure and scalable solution.

> **Info:** Learn how to enable [**Firebase Authentication**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) and integrate popular auth providers in your FlutterFlow app.

#### Supabase Authentication

In FlutterFlow, you can also integrate Supabase to manage authentication efficiently.

Supabase provides a powerful and flexible authentication solution, similar to Firebase but with some unique advantages like support for PostgreSQL.

> **Info:** Discover how to set up [**Supabase Authentication**](https://docs.flutterflow.io/integrations/authentication/supabase/initial-setup) and link it with available auth providers within your FlutterFlow app.

#### Custom Authentication

In FlutterFlow, you have the flexibility to implement custom authentication solutions tailored to your specific needs. This allows for a highly personalized approach to security, enabling you to design and integrate authentication mechanisms that perfectly fit the unique requirements of your application. Whether you need to work with legacy systems or have specific security protocols, custom authentication provides the necessary control.

> **Info:** Explore how to implement [custom authentication](https://docs.flutterflow.io/integrations/authentication/custom-authentication) strategies in your FlutterFlow app, ensuring your authentication flow aligns with your business requirements.

---

### Custom Authentication {#custom-authentication}

*Learn how to add custom authentication in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/custom-authentication

Custom authentication allows you to manage auth-related data (login details) while utilizing your own backend to authenticate users.

concepts

Understanding the concept of [**Token**](https://docs.flutterflow.io/integrations/authentication/tokens) is essential for grasping how secure access and user verification work in an application.

#### Adding custom authentication

Let's see how to add custom authentication by building an example that looks like this:

The steps to add custom authentication are as follows:

1. [Enabling custom authentication](https://docs.flutterflow.io/integrations/authentication/custom-authentication#1-enabling-custom-authentication)
2. [Building pages](https://docs.flutterflow.io/integrations/authentication/custom-authentication#2-building-pages)
3. [Authenticate users](https://docs.flutterflow.io/integrations/authentication/custom-authentication#3-authenticate-users)
4. [Save auth data](https://docs.flutterflow.io/integrations/authentication/custom-authentication#4-save-auth-data)
5. [Access auth data](https://docs.flutterflow.io/integrations/authentication/custom-authentication#5-access-auth-data)
6. [Update auth data](https://docs.flutterflow.io/integrations/authentication/custom-authentication#6-update-auth-data)
7. [Logout](https://docs.flutterflow.io/integrations/authentication/custom-authentication#7-logout)

##### 1. Enabling custom authentication

To enable custom authentication in FlutterFlow:

1. Open **Setting and Integrations** () **>** **App Settings > Authentication**.

2. Turn on the **Enable Authentication** toggle and set **Authentication Type** to **Custom**.

3. To ensure that your users are directed to the appropriate pages based on their login status, you must set the initial pages.

4. By default, the **Persist Auth Sessions** option is enabled, which means users remain logged in until they actively log out. With this option enabled, your app will automatically open to the homepage whenever it's restarted.

5. After successful authentication, your backend typically sends login details like an authentication token, a refresh token, and user details. To keep the user logged in within your app, you must store this data. You can achieve this by enabling **Associate User Data Type** and setting **User Data Type** to the [Custom Data Type](https://docs.flutterflow.io/resources/data-representation/custom-data-types). **Note** that the structure of your Custom Data Type should closely resemble the structure of a successful authentication's JSON response. At the very least, it should include critical fields like the authentication token.

##### 2. Building pages

Let's add a page that allows users to create accounts and log in. To speed up, you can add a page from the template. Here is the page added from the templates, and after some modification, it looks the below:

Also, see how to [build a page layout](https://docs.flutterflow.io/concepts/layouts) in case you want to build a page from scratch.

![auth-2-template.avif](https://docs.flutterflow.io/assets/images/auth-2-template-99e25264064ae6a07dac7abe7788f881.avif)

##### 3. Authenticate users

On each page, on click of a button, you can add appropriate authentication related [API calls](https://docs.flutterflow.io/resources/backend-logic/rest-api). For this example, we use [this](https://dummyjson.com/docs/auth).

##### 4. Save auth data

After successful authentication, you can save the auth related data using the 'Log in' action. Here's how you do it:

1. Inside the **TRUE** branch of the [previous API call](https://docs.flutterflow.io/integrations/authentication/custom-authentication#3-authenticate-users), add the **Log in** (under *Backend/Database > Custom Authentication*) action.

2. Under the **User Auth Properties**, you can set values for **Authentication Token**, **Refresh Token**, **Token Expiry Time**, and **User UID**. **Note that for the 'Persist Auth Sessions' option to work, you must set the Authentication Token**.

3. **Set User Data** to store the result of the previous API call (i.e., auth details) in a Custom Data Type. See how to get the [JSON into Data Type](https://docs.flutterflow.io/resources/backend-logic/rest-api#json-to-data-type).

##### 5. Access auth data

To access the auth data after a user logs in, open the **set from variable** menu **> Authenticated User >** choose **from Auth Properties** or **User Data Fields**.

##### 6. Update auth data

You may want to update the auth data in situations like updating the access token with the new one after it has expired. You can do so using the **Update Authenticated User** action.

Here's exactly how you do it:

1. Once you get the 401 status code, i.e., unauthorized user error, ensure to make an API call to renew the access token.

2. On getting the new access token, add a new action named **Update Authenticated User**.

3. Under the **User Auth Properties**, you can update a value for the **Authentication Token** with a new access token.

![update-auth-data.avif](https://docs.flutterflow.io/assets/images/update-auth-data-454adf49f58fd1bf0ee90a499bdcccee.avif)

##### 7. Logout

You can logout a user by adding the **Log Out** action.

![logout.avif](https://docs.flutterflow.io/assets/images/logout-2c596eacb8601f332f9a25c382850528.avif)

---

### Anonymous Login {#anonymous-login}

*Learn how to implement anonymous login in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/firebase/anonymous-login

Prerequisites

Before getting started with this section:

* Complete [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase)
* Complete [**Initial Setup**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) required for authentication.
* Learn more about the concepts of [**Anonymous Authentication**](https://docs.flutterflow.io/integrations/authentication-methods#anonymous-authentication)

#### Enable Anonymous Authentication in Firebase

To enable Anonymous authentication, first go to your Firebase console and enable the authentication provider:

#### Add Anonymous Login Action

1. On the button designated for anonymous authentication, add a new Action.

2. Search for and select the **Log In** action (located under Backend/Database > Firebase Authentication).

3. Set the Auth Provider to **Anonymous**.

4. Enable the **Create User Document** toggle and set the Collection to *users*. This action will create an entry for the user in the database without any details upon successful login.

> **Info:** To let users log out of your app, you can use the [**Logout**](https://docs.flutterflow.io/integrations/authentication/firebase/auth-actions#logout-action) action.

---

### Apple Login {#apple-login}

*Learn how to add Apple login in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/firebase/apple

Apple Sign-In allows users to authenticate using their Apple Accounts.

Support

Apple sign-in functionality is only supported for iOS.

Prerequisites

Before getting started with this section:

1. Complete [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase).
2. Complete [**Initial setup**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) required for authentication.
3. Created an [**Apple account**](https://appleid.apple.com/account?appId=632\&returnUrl=https%3A//developer.apple.com/account/).
4. [**Purchased an Apple Developer membership**](https://developer.apple.com/programs/enroll/). Read more about the [**Apple Developer Program**](https://developer.apple.com/programs/) and how to sign up.
5. Apple sign-In can not be tested in Run Mode. You will need to test it on a real device or emulator. Try with Local Run!

#### Adding Apple sign-in

Adding Apple sign-in comprises of the following steps:

1. [Configure email communication](https://docs.flutterflow.io/integrations/authentication/firebase/apple#1-configure-email-communication)
2. [Enable Apple sign-in in your App ID](https://docs.flutterflow.io/integrations/authentication/firebase/apple#2-enable-apple-sign-in-in-your-app-id)
3. [Enabling Apple sign-in in Firebase](https://docs.flutterflow.io/integrations/authentication/firebase/apple#3-enabling-apple-sign-in-in-firebase)
4. [Add an Apple sign-in button](https://docs.flutterflow.io/integrations/authentication/firebase/apple#4-add-an-apple-sign-in-button)
5. [Add login action](https://docs.flutterflow.io/integrations/authentication/firebase/apple#5-add-login-action)
6. [Adding logout action](https://docs.flutterflow.io/integrations/authentication/firebase/apple#6-adding-logout-action)
7. [Preparing to test the app](https://docs.flutterflow.io/integrations/authentication/firebase/apple#7-preparing-to-test-the-app)
8. [Verify user creation](https://docs.flutterflow.io/integrations/authentication/firebase/apple#8-verify-user-creation)

##### 1. Configure email communication

"Apple sign-in" is a privacy-focused authentication system. One of its notable features is the ability to hide a user's real email address when signing up for apps and services. When users choose to hide their email, you get one random email address that forwards to the user's actual Apple ID email. This helps users keep their real email addresses private.

![User opting to hide the email address](https://docs.flutterflow.io/assets/images/opt-to-hide-email-9ce8755a705492a463894be5e304fef7.png)

So, in order to contact such users, you must register email sources that your organization will use for communication.

> **Info:** Also, If you use any of the Firebase Authentication features that send emails to users, including email link sign-in, email address verification, etc., you must add `noreply@YOUR_FIREBASE_PROJECT_ID.firebaseapp.com` as well.

To register email sources:

1. From your Apple developer account, open the [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources/certificates/list) page and select [services](https://developer.apple.com/account/resources/services/list).
2. Under the 'Sign in with Apple for Email Communication,' click on the **Configure** button.
3. Click on the **(+)** button on the right side of **Email Sources**.
4. Enter the email in the **Email Addresses** section and click **Next**.
5. Now click on **Register** and then the **Done** button.

##### 2. Enable Apple sign-in in your App ID

Here's how you do it:

1. From your *Apple developer account*, open the [Identifiers](https://developer.apple.com/account/resources/identifiers/list) section.
2. Open the identifier with your existing APP ID.
3. Select **Sign In with Apple** from the list.
4. Click **Save**.

##### 3. Enabling Apple sign-in in Firebase

To enable Apple authentication in the Firebase:

1. Open the [Firebase console](https://console.firebase.google.com/) and click on **Authentication**.
2. Click on the **Get started** button (this may not be visible if you have already set up other forms of Authentication).
3. Select the **Sign-in method** tab.
4. Click on **Apple** (Under the 'Additional Providers' section). If you have already added any other provider, click on the **Add new provider** and then click on **Apple**.
5. Find the **Apple** switch and enable it.
6. Click on the **Save** button.

##### 4. Add an Apple sign-in button

To allow users to authenticate, you need a login page with a button. You can create your own or use the one from the widget template or page template.

Here's how you can add the Apple sign-in button from our page template:

##### 5. Add login action

When you click the Apple sign-in button, it will trigger the 'Log In' action, prompting users to provide their Apple ID credentials.

To add login action:

1. Select the widget (e.g., Button) on which you want to add the action.
2. Select **Actions** from the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) (the right menu) and select **Add Action**.
3. Search and select the **Log in** (under *Backend/Database > Firebase Authentication*) action.
4. Set **Auth Provider** to **Apple**.
5. Tick the **Create User Document** and set the **Collection** to **users**. After successful login, this will insert the user's email address into the 'users' collection. If a user already exists, it won't add details again.

##### 6. Adding logout action

To let users log out of your app, you can use the [Logout](https://docs.flutterflow.io/integrations/authentication/firebase/auth-actions#logout-action) action.

##### 7. Preparing to test the app

For testing your app on a real device, you must configure the project in Xcode. This includes adding a team to your project and setting an appropriate signing certificate.

Here's how you configure your project in Xcode:

1. From the Local Run, [open your project in Xcode](https://docs.flutterflow.io/testing/local-run#access-project-code).

> **Tip:** If you are using Android Studio, right-click on the **ios** folder, find **Flutter,** and then click on the **Open iOS module in Xcode**.

2. In Xcode, click on **Runner** (left side menu) and then select the **Signing and Capabilities** tab.
3. We recommend choosing the **Automatically manage signing** option. This will auto-create the profiles, app ID, and certificates required to build and run your app. If you don't, you'll have to [manually create a 'provisioning profile'](https://blog.codemagic.io/distributing-native-ios-sdk-with-flutter-module-using-codemagic/) and then add it in the Xcode.
4. Under the **Signing** section, find the **Team** dropdown and select your team.
5. Use [Local Run](https://docs.flutterflow.io/testing/local-run) to test the app on a real device.

##### 8. Verify user creation

Run and test your app. To confirm the successful integration of Apple authentication and the creation of users, navigate to your **Firebase project > Authentication > Users** and check the user entries.

---

### Common Auth Actions {#common-auth-actions}

*Learn how to add Firebase Authentication actions in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/firebase/auth-actions

Here's a list of common authentication actions:

#### Logout \[Action]

This action enables users to securely log out of their account and clear their session data from the app, which ensures that their account remains safe and secure.

Follow the steps below to add this action:

1. Select the widget (e.g., Button) on which you want to add the action.
2. Select **Actions** from the properties panel (the right menu), If it's the first action, click **+ Add Action** button. Otherwise, click the "**+**" button below the previous action tile (inside *Action Flow Editor*) and select **Add Action**.
3. Search and select the **Logout** (under *Backend/Database > Firebase Authentication*) action.

![logout](https://docs.flutterflow.io/assets/images/logout-action-83a4b4ad85e39bbdfd4f272f230f599f.png)

#### Reset Password

With Firebase Authentication, there are two ways you can allow users to reset their password in your FlutterFlow app:

##### In-App Password Change

This option allows users to change their password while they are logged into the app. This is useful when a user is authenticated but wants to update their password for security reasons.

To implement this, create a new page in your app, such as a **ChangePassword** page. This page should include two **TextFields** for the user to enter a new password and confirm it, along with a button (e.g., **Update Password**) to submit.

On the button's click, add the **Update Password** action (under *Backend/Database > Firebase Authentication*) and bind the **Password Field** and **Confirm Password Field** to their respective input widgets.

![firebase-update-password.avif](https://docs.flutterflow.io/assets/images/firebase-update-password-adcf2e4b82e68e4bc9a690bf398281e9.avif)

> **Info:** By default, the **Navigate Automatically** option is enabled. This means that after the password is successfully updated, the user will be redirected to the **Logged In Page** specified in your [**Initial Page**](https://docs.flutterflow.io/resources/projects/settings/general-settings#initial-page) settings.

##### Reset Password Link

This allows users who are logged out to reset their password. It sends a password reset link to the user's email address. When clicked, the user is directed to a Firebase-hosted webpage where they can set a new password.

To set this up, create a page in your app, such as a **ForgotPassword** page. This page should include a **TextField** for the user to enter their email address and a button (e.g., **Send Reset Link**) to submit the request.

On the button's click, add the **Send Reset Password Email** action (under *Backend/Database > Firebase Authentication*) and set the **Email Field** dropdown to the widget that takes user’s email. This action will send a password reset link to the provided email address.

![firebase-send-reset-link.avif](https://docs.flutterflow.io/assets/images/firebase-send-reset-link-017287b02614912f3a5e9e3d90e33e8d.avif)

#### Update Email \[Action]

This action allows users to change their registered email address linked to their user profile, thus ensuring their account details are up-to-date.

This is helpful in scenarios where a user may have changed their primary email address or entered an incorrect one during initial registration. Also, if users lose access to their original email or forget their login credentials, being able to update their email addresses can assist in resetting passwords or recovering account access.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Container, Button, etc.) on which you want to add the action.
2. Select **Actions** from the properties panel (the right menu), If it's the first action, click **+ Add Action** button. Otherwise, click the "**+**" button below the previous action tile (inside *Action Flow Editor*) and select **Add Action**.
3. Search and select the **Update Email** (under *Backend/Database > Firebase Authentication*) action.
4. As a best practice, it's also recommended to send the email verification link to the new email (using the [e-mail verification](https://docs.flutterflow.io/integrations/authentication/firebase/email-login#send-email-verification-link-action) action) followed by this action.

![adding-update-email-action](https://docs.flutterflow.io/assets/images/adding-update-email-action-fd7c5ad244258b04db50c45d4e8a50a4.avif)

#### Delete User \[Action]

Using this action, you can delete the user account created using the [Firebase authentication](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup). Additionally, you can also set up to delete all data associated with that user.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Container, Button, etc.) on which you want to add the action.

2. Select **Actions** from the properties panel (the right menu), If it's the first action, click **+ Add Action** button. Otherwise, click the "**+**" button below the previous action tile (inside *Action Flow Editor*) and select **Add Action**.

3. Search and select the **Delete User** (under *Backend/Database > Firebase Authentication*) action.

4. As a best practice, it's also recommended to log out the user (using the [logout](https://docs.flutterflow.io/integrations/authentication/firebase/auth-actions) action) following this action.

   ![adding-delete-action](https://docs.flutterflow.io/assets/images/adding-delete-action-caeaca8b26c96db25760f62310cfb042.avif)

5. To delete all records and data associated with that user's account:

   1. Navigate to the **Firestore** (from the Navigation Menu) > switch to **Firestore Settings** > **Firestore Rules**.
   2. Identify the collection from which you want to delete the user's data and ensure the **Delete** rule is set to **Tagged Users**. This will open the 'Tag Users' popup; here you can select the field that contains the document reference. See how to [setup a rule](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-rules).
   3. Tick the checkbox.
   4. See the **Delete User References** section and click on **Preview** to verify the generated rule.
   5. Click the **Deploy** button.

#### FAQs

While adding Delete User \[Action], I can't see or select field in 'Tag Users' popup

If you can't see or select the field containing the user reference, ensure that you have enabled the 'Create User Document' option in the **Create Account** action. Enabling this option ensures that the 'users' collection is properly set up and its reference can be accessed in the 'Tag Users' popup.

---

### Email Login using Firebase {#email-login-using-firebase}

*Learn how to add Email Login in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/firebase/email-login

Prerequisites

Before getting started with this section:

* Complete [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase)
* Complete [**Initial Setup**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup)

#### Enable Email Login Provider in Firebase

1. Open the Firebase Console and click on **Authentication**
2. Click on the Get started button (this may not be visible if you have already set up other forms of Authentication).
3. Select the **Sign-in** method tab.
4. Click on Email/Password (Under the 'Native providers' section). If you have already added any other provider, click on Add new provider and then click on Email/Password.
5. Find the Email/Password switch and enable it.
6. Click on the Save button.

#### Add a Login Screen with Email/Password Fields

In FlutterFlow, you can utilize the Page Templates feature to create a new authentication page that includes both a "Create Account" component and a "Log In" component.

This setup aligns with Firebase's authentication process, which requires users to first create an account using their email and then allows them to sign in using the email ID they registered with.

#### Create Account Action

The Create Account action is the entry point for new users in any application. It's about establishing a user's credentials and granting them access for the first time. This action involves collecting necessary information such as email, password, and potentially other user-specific details like name or phone number.

The primary goal is to register and store new user data securely in your backend or authentication service (like Firebase). This process typically includes steps like validating the data format (e.g., email format), checking for unique usernames or email addresses etc.

To enable this in FlutterFlow, follow these steps:

1. Create a page using Page Templates or from scratch, and add fields such as Email, Password, and Confirm Password. Based on your requirements, you may add additional fields.

2. Add a "Create Account" or "Sign Up" button and attach an action to it.

3. Search for and select the **Create Account** action under **Backend/Database > Firebase Authentication**.

4. Set the **Auth Provider to Email**.

5. Configure the fields to retrieve values from variables, which are usually found under Widget State > Field Name.

6. The **Create User document** is enabled by default. This means a user document will be created in the 'users' collection after the user is authenticated, if it does not already exist with details like email and UID. * To create a user document in a different collection, adjust the **Created Document > Collection** dropdown to the desired collection.
   * If additional details such as name, age, and birthday are needed at signup, click on the **+ Add Field** and set its value. Make sure these fields are already created in the 'users' collection.

![create-account-action.png](https://docs.flutterflow.io/assets/images/create-account-action-f8867c7b7b34ca3a6767314b5d86415c.png)

#### Send Email Verification Link \[Action]

> **Info:** To understand why email verification is required when authenticating with an email and password, refer to [**Authentication Methods**](https://docs.flutterflow.io/integrations/authentication-methods)

1. Add a new action immediately after the **Create Account** action.

2. Search for and select the **Send Email Verification Link** (located under **Backend/Database > Firebase Authentication**) action. The user's email is automatically retrieved from Firebase Authentication, and a verification link is sent to the user for confirmation.

[Send Email Verification Link](https://demo.arcade.software/3aDUDdUKXWmpBPiTO5oe?embed\&show_copy_link=true)

The user should receive an email verification link in their inbox. Upon successful verification, they will see a success message.

#### Log In \[Action]

The **Log In** action, on the other hand, is for users who already have an account. It involves verifying the credentials provided by a returning user against stored data to grant access to the system. This action is crucial for maintaining secure access control as it ensures that the entity attempting to gain access is indeed who they claim to be. The process usually requires users to provide their registered email and password, which are then checked for correctness through your authentication system.

To enable this in FlutterFlow, follow these steps:

1. Create another Log In page using Page Templates or from scratch, and add fields such as Email, Password.

2. Add a "Log In" button and attach an action to it.

3. Search for and select the **Log In** action under **Backend/Database > Firebase Authentication**.

4. Configure the fields to retrieve values from variables, which are usually found under Widget State > Field Name.

![login-action.png](https://docs.flutterflow.io/assets/images/login-action-a2b64c94132eea7dee3cfaa7eee87893.png)

> **Info:** To let users log out of your app, you can use the [**Logout**](https://docs.flutterflow.io/integrations/authentication/firebase/auth-actions#logout-action) action.

##### Verify user created in Firebase Dashboard

To verify that you have successfully added the email authentication and that users are being created, you can head over to your **Firebase project > Authentication > Users** and verify the user entries.

---

### Facebook Login {#facebook-login}

*Learn how to add Facebook login in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/firebase/facebook

Facebook login allows users to authenticate using their Facebook Accounts.

Prerequisites

Before getting started with this section:

* Complete [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase)
* Complete [**Initial Setup**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup)

#### Adding Facebook sign-in

Adding Facebook sign-in comprises the following steps:

1. [Create app on Facebook](https://docs.flutterflow.io/integrations/authentication/firebase/facebook#1-create-app-on-facebook)
2. [Configure app on Facebook](https://docs.flutterflow.io/integrations/authentication/firebase/facebook#2-configure-app-on-facebook)
3. [Add email permission](https://docs.flutterflow.io/integrations/authentication/firebase/facebook#3-add-email-permission)
4. [Enabling Facebook authentication in Firebase](https://docs.flutterflow.io/integrations/authentication/firebase/facebook#4-enabling-facebook-authentication-in-firebase)
5. [Enabling Facebook authentication in FlutterFlow](https://docs.flutterflow.io/integrations/authentication/firebase/facebook#5-enabling-facebook-authentication-in-flutterflow)
6. [Add a Facebook sign-in button](https://docs.flutterflow.io/integrations/authentication/firebase/facebook#6-add-a-facebook-sign-in-button)
7. [Add login action](https://docs.flutterflow.io/integrations/authentication/firebase/facebook#7-add-login-action)
8. [Add logout action](https://docs.flutterflow.io/integrations/authentication/firebase/facebook#8-add-logout-action)
9. [Prepare to test the app](https://docs.flutterflow.io/integrations/authentication/firebase/facebook#9-prepare-to-test-the-app)
10. [Verify user creation](https://docs.flutterflow.io/integrations/authentication/firebase/facebook#10-verify-user-creation)

##### 1. Create app on Facebook

When you create an app on the [Facebook Developer Console](https://developers.facebook.com/), you are given a unique *App ID* and *App secret*, ensuring secure communication between your app and Facebook's servers. Additionally, it lets you define required permissions and user data access and also restricts login origins for enhanced security.

Here's is how you create app on Facebook:

##### 2. Configure app on Facebook

Now, you must add and configure platforms that will support Facebook authentication - For example, Android and iOS.

To do so follow the steps below:

* Configure Android App
* Configure iOS App

##### 3. Add email permission

When users log in using third-party providers (like Google or Facebook), fetching their email addresses reduces the steps they need to take during sign-up. For Facebook sign-in, to access a user's email, you must add email permission in Firebase developer console.

Here's how you do it:

##### 4. Enabling Facebook authentication in Firebase

Here's how you enable Facebook auth in Firebase:

##### 5. Enabling Facebook authentication in FlutterFlow

To enable the Facebook authentication in FlutterFlow, follow the steps below:

##### 6. Add a Facebook sign-in button

To allow users to authenticate, you need a login page with a button. You can create your own or use the one from the widget template or page template.

##### 7. Add login action

When you click the sign-in button, it will trigger the 'Log In' action, prompting users to provide their Facebook credentials.

> **Info:** Switch on the **Create User Document** and set the **Collection** to **users**. After successful login, this will insert the user's email address into the 'users' collection. If a user already exists, it won't add details again.

##### 8. Add logout action

To let users log out of your app, you can use the [Logout](https://docs.flutterflow.io/integrations/authentication/firebase/auth-actions#logout-action) action.

##### 9. Prepare to test the app

Facebook Sign-In functionality does not work in Run or Test Mode. You can test your app on a real device or emulator using FlutterFlow’s Local Run. Follow the [Local Run documentation](https://docs.flutterflow.io/testing/local-run) and see [how to set up a physical device](https://docs.flutterflow.io/testing/local-run#setup-physical-device) to start testing.

##### 10. Verify user creation

To confirm the successful integration and the creation of users, navigate to your **Firebase project > Authentication > Users** and check the user entries.

---

### GitHub Login {#github-login}

*Learn how to add GitHub authentication in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/firebase/github

The GitHub auth provides a convenient way for users to authenticate and log in to your application using their GitHub accounts.

![github-demo.gif](https://docs.flutterflow.io/assets/images/github-demo-41380054c31b666044e4811ef9c1ffad.gif)

Prerequisites

Before getting started with this section:

* Complete [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase).
* Complete [**Initial setup**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) required for authentication.

#### Adding GitHub auth

Adding GitHub auth comprises of following steps:

1. [Enabling GitHub authentication in Firebase](https://docs.flutterflow.io/integrations/authentication/firebase/github#1-enabling-github-authentication-in-firebase)
2. [Adding GitHub login action](https://docs.flutterflow.io/integrations/authentication/firebase/github#2-adding-github-login-action)

##### 1. Enabling GitHub Authentication in Firebase

To enable GitHub authentication in the Firebase:

1. Open the [Firebase console](https://console.firebase.google.com/), Click on **Authentication** ( in the left side menu).

2. Select the **Sign-in method** tab, and select **GitHub**. If you have already added another provider, click on the **Add new provider**, select **GitHub**, and **Enable** it.

3. To get the **Client ID** and **Client Secret**, [register your app](https://github.com/settings/applications/new) as a developer application on GitHub, and while doing so, paste the authorization callback URL to your GitHub app configuration.

4. Click **Save**.

5) To test the app in Run Mode, add our domain to **Authorized domains**.

![adding-authorized-domain-2.png](https://docs.flutterflow.io/assets/images/adding-authorized-domain-2-ffe3326be53615349de80ceabb861d10.png)

##### 2. Adding GitHub Login Action

Follow the steps below to add GitHub login action:

1. Select the widget (e.g., Button) on which you want to add the action.

2. Select **Actions** from the properties panel (the right menu), If it's the first action, click **+ Add Action** button. Otherwise, click the "**+**" button below the previous action tile (inside *Action Flow Editor*) and select **Add Action**.

3. Search and select the **Login** (under *Backend/Database > Firebase Authentication*) action.

4. Set **Auth Provider** to **GitHub**.

![adding-github-login-action.png](https://docs.flutterflow.io/assets/images/adding-github-login-action-3b533ba2182aeb6b1ef822f4c605aa3c.png)

> **Info:** To let users log out of your app, you can use the [**Logout**](https://docs.flutterflow.io/integrations/authentication/firebase/auth-actions#logout-action) action.

---

### Google Login {#google-login}

*Learn how to add Google OAuth login in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/firebase/google-oauth-login

Google Sign-In allows users to authenticate using their Google Accounts.

Prerequisites

Before getting started with this section:

* Complete [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase)
* Complete [**Initial Setup**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup)
* Added **SHA-1 key** and regenerated **Config Keys**.

#### Enable Google Sign-in Provider in Firebase

Open the **Firebase Console**, click on **Authentication** and then follow the steps below to enable Google Sign in for your Firebase project.

#### Add a Login Screen with Google Login Action

##### Create a Login Screen

To allow users to authenticate, you need a Login or Sign-in Page with a button. You can create your own or use the one from page templates.

##### Add Login Action

1. On your Google Login button, select **Actions** from the properties panel (the right menu) and select **Add Action**.
2. Search and select the Log In (under **Backend/Database > Firebase Authentication**) action.
3. Set **Auth Provider** to **Google**.
4. Enable **Create User Document** and set the **Collection** to **users**. After successful login, this will insert the user's details, such as email, name, and photo, into the *users* collection. **Note** that, if a user exists already, it won't add the details again.

If you haven’t already, see how to [create *users* collection](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup#creating-the-users-collection).

> **Tip:** To let users log out of your app, you can use the [**Logout**](https://docs.flutterflow.io/integrations/authentication/firebase/auth-actions#logout-action) action.

#### Test Google Login

##### Running on Device

To test during development, you can run your app locally using FlutterFlow’s Local Run. Follow the [Local Run documentation](https://docs.flutterflow.io/testing/local-run) and see [how to set up a physical device](https://docs.flutterflow.io/testing/local-run#setup-physical-device) to start testing.

##### Running on Test Mode/Run Mode

1. To test Google sign-in in Test or Run mode, you must add the authorized domain in the Firebase console and Google cloud console.

   * **For Test mode**, you can open the browser console, try logging in, and get the domain from the browser console. It should look like `ff-debug-service-frontend-ygxkweukma-uc.a.run.app`. For *Pro* users, the above URL will also include `-pro`, such as `ff-debug-service-frontend-pro-ygxkweukma-uc.a.run.app`.

   * **For Run mode**, you can simply use 'app.flutterflow\.io'.

2. To add in Firebase console:

   1. Open the Firebase console and click on Authentication and select the Setting tab.

   2. Select **Authorized domains** from the left side menu.

   3. Click **Add domain**.

3. To add in Google cloud console:

   1. Head over to your [Project Credentials](https://console.cloud.google.com/apis/credentials?project=_) page.

   2. Ensure you are on the correct project. In our case, we are using the [EcommerceFlow demo project](https://bit.ly/ff-docs-demo-v2), it will be different for you.

   ![credential-page.png](https://docs.flutterflow.io/assets/images/credential-page-06a701a56039dabdf631d49eb9a63a87.png)

   3. Under the '**OAuth 2.0 Client IDs**', select '**Web client** (auto created by Google Service)'.

   4. Under the '**Authorized JavaScript origins**', click ADD URI and add both the URL.

   5. Similarly, under the '**Authorized redirect URIs**', click ADD URI, add both the URL and append '/\_\_/auth/handler' at the end.

4) If you don't see the Web client created yet, you can create new one by clicking **+ CREATE CREDENTIALS**, selecting OAuth client ID and then select Application type to Web application.

![add-app.gif](https://docs.flutterflow.io/assets/images/add-app-495cc4d69983deb104c266378e8402a1.gif)

##### Verify user created in Firebase Dashboard

To confirm the successful integration of Google authentication and the creation of users, navigate to your **Firebase project > Authentication > Users** and check the entries.

![verify-google-auth-users.png](https://docs.flutterflow.io/assets/images/verify-google-auth-users-1b112d385f9937e80e9bb28c3ce22893.png)

> **Info:** To ensure that your Android release will authenticate to Google, make sure to use Google Play Console's SHA keys - see how to [**Get SHA keys for release mode**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup#getting-sha-keys-for-release-mode).

---

### Enabling Firebase Auth in FlutterFlow {#enabling-firebase-auth-in-flutterflow}

*Learn how to perform the initial setup for Firebase authentication in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup

Skip if...

You have already enabled authentication while creating a [**new project with Firebase setup.**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase)

To enable authentication in FlutterFlow:

1. Open your FlutterFlow project where you are planning to use Firebase Authentication.
2. Open **Setting and Integrations > App Settings > Authentication**.
3. Turn on the Enable Authentication toggle and select **Authentication Type** to **Firebase**.
4. To ensure that your users are directed to the appropriate pages based on their login status, you must set the **Initial Page**.

![enable-auth-fr.png](https://docs.flutterflow.io/assets/images/enable-auth-fr-ae82ed0ec3ad5d152c5fbb0c1d1a2852.png)

##### Setting Initial Pages for Authentication

You can specify your app's **Entry Page** and **Logged In Page** from this section.

* **Entry Page** : This page will be displayed if the user is not logged in. This is typically used to display the onboarding flow or to provide the login/sign-up page.

* **Logged In Page**: This page will be displayed if the user is already logged in to your app. Users are automatically navigated to the page you specify here on a successful sign-in attempt.

#### Creating the 'users' collection

Prerequisities

To allow FlutterFlow to create user documents during authentication steps, it is important to enable Firestore Access in Firebase. Follow this section to enable it first.

The 'users' collection stores the information for authenticated users.

Skip if...

You have already enabled 'Create User Collection' while creating a new project with [Firebase Setup](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase).

1. Click on the Firestore tab from the [**Navigation Menu**](https://docs.flutterflow.io/flutterflow-ui/builder#navigation-menu).
2. Click on the **+ Create Collection** button. If you have any other collection already added, you can click on the Plus button.
3. Enter a collection\_name (this can be anything, but we recommend 'users') and click on Create button.
4. If you enter 'users' a popup will open which asks you to populate this collection with default fields. You can click Yes, and we will add all the fields.

Follow the quicklink to see the steps

Add Default Fields if skipped previously

1. Click on the Settings icon in the Firestore tab.
2. Find the **Users Collection** switch and enable it.
3. Find the **Collection** dropdown below, click on the **Unset**, and select the name of the collection you just created.
4. Now switch to the **Collection** tab. Now you should see all the default fields.

To store and collect additional information or modify the default fields list, see how to add fields.

WARNING

You do not need to create a password field. This is handled internally by Firebase.

#### Setup for Google or Phone sign-in setup for Android Apps

OPTIONAL

If you aren't planning to use **Google** or **Phone Sign-In**, you can skip these steps.

##### Generate the SHA-1 key

An SHA-1 key (aka the 'Secure Hash Algorithm') is required if you want to use Google Sign-in and Phone Sign-in. To learn more about the SHA-1 key, see this [link](https://developers.google.com/android/guides/client-auth).

Release Guidelines

While releasing the app, make sure to [**get the key from Play Console**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup#getting-sha-keys-for-release-mode).

1. Open a terminal window:

* **Mac**: Use the Launchpad or press (⌘ + Spacebar) for Spotlight search, type 'Terminal', and open it.

* **Windows**: Click the Windows icon, navigate to the 'Windows System' folder, and open 'Command Prompt' either by clicking or right-clicking it.

2. Copy the following command (based on your operating system) and select Enter.

Windows

`keytool -list -v -keystore C:\Users\leon\.android\debug.keystore -alias androiddebugkey`

If you get the following error while trying the above command:

`ERROR:'keytool' is not recognized as an internal or external command`

You might not have JAVA installed on your machine. [Here](https://codewithandrea.com/articles/keytool-command-not-found-how-to-fix-windows-macos/) is the helpful link to install JAVA and remove the above issue.

Mac/Linux

`keytool -list -v -alias androiddebugkey -keystore ~/.android/debug.keystore`

3. After being prompted for the key password, type 'android' and press 'Enter'. Note: For security reasons, you won't see the password as you type it.
4. Copy the SHA1 key.

###### Add the SHA-1 key in the Firebase Console

1. Open the **Firebase console > Project Overview > Project Settings** and scroll down to Your App section.
2. Select your Android App from the left side menu.
3. Find the SHA certificate fingerprints section and click on the Add fingerprint.
4. Enter the copied SHA-1 into the input box and click on Save.

###### Getting SHA keys for release mode

If you're releasing your app to the Play Store, you must add the SHA certificate fingerprints from the Play Console.

To get the keys for the release app, navigate to **Play Store Console > Your project > Release Setup > App Signing** and copy the **SHA-1** and **SHA-256** keys.

![release-sha1-key](https://docs.flutterflow.io/assets/images/release-sha1-key-1cfa5eacd6051da6c81cc863811a8c7c.avif)

##### Regenerate config files

After adding the SHA-1 key you must re-generate the config files in FlutterFlow.

To regenerate the config files:

1. Return to FlutterFlow. From the Navigation Menu, select **Settings & Integrations > Project Setup > Firebase**.
2. Click on the Regenerate Config Files.

![regerenate](https://docs.flutterflow.io/assets/images/regerenate-7b29b05d9cfb34aaa2f3b3800999eb91.png)

---

### JWT Token Authentication {#jwt-token-authentication}

*Learn how to implement JWT authentication in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/firebase/jwt-auth

[JWT](https://jwt.io/introduction) token sign-in allows you to log in and use the Firebase services such as Firebase Database and push notifications using the account created on your own server/backend.

![JWT-login-flow.avif](https://docs.flutterflow.io/assets/images/JWT-login-flow-261eda3f9f9786766286293886e3609b.avif)

In JWT token authentication, you send login credentials, like email and password, to your server through an API endpoint. The server then creates a user account, generates a custom JWT token, and returns it to your app. This JWT token allows you to log in to Firebase and access its services.

> **Info:** You can learn more about Firebase and JWT tokens [**here**](https://firebase.google.com/docs/auth/admin/create-custom-tokens).

#### Adding JWT token authentication

Let's build an example that uses a JWT token to log into the app. Here's how it looks when completed:

![JET-token-authentication.gif](https://docs.flutterflow.io/assets/images/JET-token-authentication-f2de1605e4785a73127e0454ab1a4d27.gif)

Prerequisites

Before getting started with this section:

* Complete [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase).
* Complete [**Initial setup**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) required for authentication.

Adding JWT token authentication comprises the following steps:

1. [Add login API](https://docs.flutterflow.io/integrations/authentication/firebase/jwt-auth#1-add-login-api)
2. [Adding login page](https://docs.flutterflow.io/integrations/authentication/firebase/jwt-auth#2-adding-login-page)
3. [Add login action](https://docs.flutterflow.io/integrations/authentication/firebase/jwt-auth#3-add-login-action)
4. [Adding logout action](https://docs.flutterflow.io/integrations/authentication/firebase/jwt-auth#4-adding-logout-action)
5. [Verify user creation](https://docs.flutterflow.io/integrations/authentication/firebase/jwt-auth#5-verify-user-creation)

##### 1. Add login API

You must [create an API](https://docs.flutterflow.io/resources/backend-logic/create-test-api) endpoint on your server that accepts email/username and password. If the credentials are valid, it generates the JWT token and passes it back in response.

At your server, you can generate the JWT token either using the [Firebase Admin SDK](https://firebase.google.com/docs/auth/admin/create-custom-tokens#create_custom_tokens_using_the_firebase_admin_sdk) or a [third-party JWT library](https://firebase.google.com/docs/auth/admin/create-custom-tokens#create_custom_tokens_using_a_third-party_jwt_library). You can find the detailed instructions [here](https://firebase.google.com/docs/auth/admin/create-custom-tokens).

> **Info:** Alternatively, you can integrate Supabase authentication into your app and use the JWT token generated after [**account creation**](https://docs.flutterflow.io/integrations/authentication/supabase/auth-actions#log-in-action).

The API endpoint should be similar to the following (Tip: Expand and see the '200 OK' section):

###### Login API to be created on your server

`POST` `/login`

##### Request Body

| Name       | Type   | Description |
| ---------- | ------ | ----------- |
| email\*    | String |             |
| password\* | String |             |

##### 200: OK

```
{
    "user": {
        "id": 1,
        "role_id": 1,
        "name": "james",
        "email": "james@yopmail.com"
    },
    "token_type": "Bearer",
    "expires_in": 3600,
    "jwt_token": "eyJraWQiOiItSE5TUmtwMWdXcG9QcC1wWVBmU1U4UW1fdng4Q0VwdzRSdTZTQU9WLThRIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULi1PaG5EdWREUG9qWklsZjMtVDRVWHlTWW5ERElHQ3dYTUdQcXk1c1JUbjAub2FydGh3ZmxpbzhZOVZJbHc0eDYiLCJpc3MiOiJodHRwczovL2Rldi00NTc5MzEub2t0YS5jb20vb2F1dGgyL2F1c2hkNGM5NVF0RkhzZld0NHg2IiwiYXVkIjoiYXBpIiwiaWF0IjoxNjU5MDAyOTQ5LCJleHAiOjE2NTkwMDY1NDksImNpZCI6IjBvYWhkaGprdXRhR2NJSzJNNHg2IiwidWlkIjoiMDB1aGVuaDFwVkRNZzJ1ZXg0eDYiLCJzY3AiOlsib2ZmbGluZV9hY2Nlc3MiXSwiYXV0aF90aW1lIjoxNjU5MDAyOTQ5LCJzdWIiOiJhcGktdXNlcjRAaXd0Lm5ldCJ9.g2TyTQECo-HCSjn58Fmazki8DBCtCq2hkG6OGQOJgr0JUq3uHgj8ulojoBI5ckv3e3TcVGFg1x9KknSwgiZo0LxRpbAdbF27hfF8truExjEv7hGKoV_oAOaiD56be5K-HjYkp6j-b5S6gXe4N10T1NtovLI7L6MZvmqCL_26qzXni5hNkCjgRm8Rd6GnJwbjDLpV3snp51bVNYNqhoAhOPBqjmOErFQvO2Wmfkj8DuVXzsvRqm_xfb8-7Oosx5oGVMVR3liXW5NZsRWes4TXXwsEou3qCyVy5fAhzm7rKjIk1zWv9vm0IOWMFwHHYTgEc_LTYWMovWtkuBx4ia546Q",
    "refresh_token": "dlIOQHHAmweyOrVkDlpNYpi1XM-DwX5Cgx70LoKIbTI"
}
```

> **Warning:** In most cases, you would make the app content available right after creating a new account. Hence, you should also generate and return the JWT token on the success of create account API and use it to login into the Firebase.

> **Info:** If you want to try the JWT token authentication without creating an API endpoint right now, you can [**generate the JWT token locally**](https://docs.flutterflow.io/integrations/authentication/firebase/jwt-auth#create-a-jwt-token-locally) for testing.

##### 2. Adding login page

Let's add a sign-in page from the templates and choose the **Authenticate Solo Alt** from under the **Auth** tab. Tip: After adding, remove the other social sign-in buttons.

![login-page.avif](https://docs.flutterflow.io/assets/images/login-page-31990c9ba390dc2395477fa4ac808aa0.avif)

##### 3. Add login action

The login process involves two steps. First, you trigger an API call to your server. Upon successful call completion, you'll use the returned JWT token in the JWT Token action.

Here are the step by step instructions:

1. Select the **Widget** (e.g., Sign In) on which you want to define the action.

2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.

3. Add the login api and provide the **Action Output Variable Name**. If the call succeeds, this will be used to retrieve the token.

4. Inside the **TRUE** section, click on the **+** button and select **Add Action**.

5. On the right side, search and select the **Log in** (under Firebase Authentication) action.

6. Set the **Auth Provider** to **JWT token**.

7. Now, you must provide the actual JWT token. To set the token from an API response:

   1. Click on the **UNSET** and select the **Action Outputs -> Action Output Variable Name** (that you specified in the API call section.)
   2. Set the **API Response Options** to **JSON Body** and **Available Options** to **JSON Path**.
   3. Enter the **JSON Path** to locate the token in API response, such as `$.token,` and click **Confirm**.

8. (Optional) add the [snackbar action](https://docs.flutterflow.io/resources/ui/pages/scaffold#show-snackbar-action) to display the success message.

9. (Optional) Inside the **False** section, add the snackbar action to display the failure message.

##### 4. Adding logout action

To let users log out of your app, you can use the [Logout](https://docs.flutterflow.io/integrations/authentication/firebase/auth-actions#logout-action) action.

##### 5. Verify user creation

To confirm the successful integration and the creation of users, navigate to your **Firebase project > Authentication > Users** and check the user entries. Tip: Notice the 'userid' (originally created by your server) is added inside the **User UID** column.

#### Create a JWT token locally

Sometimes you might want to build and test the JWT authentication before the login or create account API is ready. You can achieve this by creating the JWT token locally and passing it inside the [login action](https://docs.flutterflow.io/integrations/authentication/firebase/jwt-auth#3-add-login-action).

> **Warning:** Use this method only for testing purposes. Ideally, you should be doing this on the server side.

Below are steps to create a JWT token locally using Node.js:

1. In the Firebase dashboard of your project, navigate to the far left menu. Select **Project Settings( )** -> **Service accounts**.

2. Select **Generate new private key**. This will open a new popup. Again, click **Generate key** and save the `.json` file in some folder. You will need it while generating the token.

3. Now, download and Install [node.js](https://nodejs.org/en/download/).

4. Open a terminal at the folder where you have saved the `.json` file and enter this command: `npm install firebase-admin`. This will install Firebase Admin SDK inside the folder.

5. In the same folder, create an `index.js` file and add the below content.

```
const admin = require('firebase-admin');
const ServiceAccount = require('./[YOUR_SERVICE_ACCOUNT_JSON_FILE_NAME].json');
admin.initializeApp({
	credential: admin.credential.cert(ServiceAccount)
});

const uid= 'userid1'; // This user id will be stored in Firebase.

admin.auth().createCustomToken(uid)
  .then((customToken) => {
    console.log(customToken);
  })
  .catch((error) => {
    console.log('Error creating custom token:', error);
  });
```

1. To run this `index.js` file inside the terminal (at the same location where this file is located), hit this command: `node index.js`. This will print the JWT token in the console.

2. Copy this JWT token, return to FlutterFlow, and save it in the **app state variable** (String Datatype).

3. Open the JWT token action, click on **UNSET** (or a variable if you have already set it), and select the **App State -> variableName** (that holds the JWT token).

#### Accessing Firebase Database

Once you log in via the JWT token, the *Authenticated User* object is available. This object contains the fields (i.e., logged-in user's data), especially **User Reference (users ref),** that you may need to provide while adding or retrieving Firestore documents.

Here's an example of how you can use the *Authenticated User* object to filter the to-do items based on the user who created it.

![access-firebase-database.avif](https://docs.flutterflow.io/assets/images/access-firebase-database-e3ec523d4100cb53d23d2452081eef3a.avif)

#### Sending push notifications

Once you log in via the JWT token, the *Authenticated User* object is available. This object contains the fields (i.e., logged-in user's data), especially **User Reference (users ref),** that you may need to provide while adding or retrieving Firestore documents.

When such user reference is stored inside the Firestore documents, you can use them inside the **Single** or **Multiple Recipient** while defining the **Audience** inside the [Trigger Push Notification](https://docs.flutterflow.io/concepts/notifications/push-notifications#trigger-push-notification-action) action, as shown in the image below:

![send-push-notification-to-users-created-via-JWT-token.png](https://docs.flutterflow.io/assets/images/send-push-notification-to-users-created-via-JWT-token-ff46f39bfb7debb4b20811e130d309a4.png)

To learn more about how to use user references for sending push notifications, please check the [push notification](https://docs.flutterflow.io/concepts/notifications/push-notifications) section.

---

### Phone Login {#phone-login}

*Learn how to add phone login in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/firebase/phone

Phone login allows a user to sign in by sending an SMS message to the user's phone. The user login in using a one-time code contained in the SMS message.

Prerequisites

Before getting started with this section:

1. Complete [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase).
2. Complete [**Initial setup**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) required for authentication.

#### Adding Phone sign-in

Adding Phone sign-in comprises the following steps:

1. [Setting up phone sign-in](https://docs.flutterflow.io/integrations/authentication/firebase/phone#1-setting-up-phone-sign-in)
2. [Enabling phone authentication in Firebase](https://docs.flutterflow.io/integrations/authentication/firebase/phone#2-enabling-phone-authentication-in-firebase)
3. [Building phone number page](https://docs.flutterflow.io/integrations/authentication/firebase/phone#3-building-phone-number-page)
4. [Building verify code page](https://docs.flutterflow.io/integrations/authentication/firebase/phone#4-building-verify-code-page)
5. [Adding phone sign-in action](https://docs.flutterflow.io/integrations/authentication/firebase/phone#5-adding-phone-sign-in-action)
6. [Adding verify code action](https://docs.flutterflow.io/integrations/authentication/firebase/phone#6-adding-verify-code-action)
7. [Adding logout action](https://docs.flutterflow.io/integrations/authentication/firebase/phone#7-adding-logout-action)
8. [Testing phone sign-in](https://docs.flutterflow.io/integrations/authentication/firebase/phone#8-testing-phone-sign-in)
9. [Verify user creation](https://docs.flutterflow.io/integrations/authentication/firebase/phone#9-verify-user-creation)

##### 1. Setting up phone sign-in

To use phone sign-in, you must [get the SHA-1 key](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup#generate-the-sha-1-key) and [regenerate the configuration files](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup#regenerate-config-files). You can find the detailed instructions [here](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup). **Note** that this step is often missed, so ensure you must complete this step before you proceed further.

##### 2. Enabling phone authentication in Firebase

To enable authentication in the Firebase:

1. Open the [Firebase console](https://console.firebase.google.com/) and click on **Authentication**.

2. Click on the **Get started** button (this may not be visible if you have already set up other forms of Authentication).

3. Select the **Sign-in method** tab.

4. Click on **Phone** (Under the 'Native Providers' section). If you have already added any other provider, click on the **Add new provider** and then click on **Phone**.

5. Find the **Phone** switch and enable it.

6. Click on the **Save** button.

##### 3. Building phone number page

To allow users to authenticate using their phone number, you need to create a page to accept the user's phone number. We provide a collection of ready-to-use templates. You can use one of our templates or create a page from scratch.

Here is the page added from the templates, and after some modification, it looks the below:

##### 4. Building verify code page

You need to create another page to verify the SMS code. Here's how you build the verify code page using templates.

##### 5. Adding phone sign-in action

On click the 'sign-in' or 'send code' button, you will add the 'Phone Sign In' action, which redirects users to a page where they can enter the code received on their phone.

To add this action:

1. Select the widget (e.g., Button) on which you want to add the action.

2. Select **Actions** from the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) (the right menu) and select **Add Action**.

3. Search and select the **Phone Sign In** (under *Backend/Database > Firebase Authentication*) action.

4. Now provide the **Phone Number** via **Widget State > TextField** (that accepts the phone number).

5. Now, **Select Page** that you created to verify code.

##### 6. Adding verify code action

On click of the 'Verify Code' button, you will add the 'Verify SMS Code' action, which opens the home page if the action is successful.

1. Select the widget (e.g., Button) on which you want to add the action.

2. Select **Actions** from the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) (the right menu) and select **Add Action**.

3. Search and select the **Verify SMS Code** (under *Backend/Database > Firebase Authentication*) action.

4. Now provide the **SMS Code** via **Widget State > TextField** (that accepts the code).

##### 7. Adding logout action

To let users log out of your app, you can use the [Logout](https://docs.flutterflow.io/integrations/authentication/firebase/auth-actions#logout-action) action.

##### 8. Testing phone sign-in

###### 8.1 Test on Run or Test mode

To test phone sign-in in *Test* or *Run* mode, you must add the authorized domain in the Firebase console.

Here's how you add the authorized domain:

1. For **Test mode**, you can open the browser console, try logging in, and get the domain from the browser console, and for **Run mode**, you can simply use '*app.flutterflow\.io*.'
2. Now open the [Firebase console](https://console.firebase.google.com/) and click on **Authentication**.
3. Select the **Setting** tab.
4. Select **Authorized domains** from the left side menu.
5. Click **Add domain**.

Here's how it should look:

![adding-authorized-domain](https://docs.flutterflow.io/assets/images/adding-authorized-domain-44d8bcb1a06fe163b52139709e7bbacf.png)

###### 8.2 Test on a real device

Phone Sign In ***does not*** work in an Android emulator. You can only test it on a real device.

To test on a real device, add the SHA-256 key in the Firebase console and enable the 'Google Play Integrity API' in Google Cloud.

> **Info:** Skip if you find the below steps already completed by our automated Firebase integration.

1. Get the SHA-256 key/fingerprint, add it to your Firebase project, and then regenerate the Firebase config files in FlutterFlow. **Note**: The instructions are similar to generating the SHA-1 key and are explained [here](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup#generate-the-sha-1-key). You will find the SHA-256 key in the terminal just below the SHA-1 key. This is required for the Firebase to verify that the sign-in request is coming from a legitimate device.

> **Warning:** While releasing the app, make sure to [**get the key from the Play Console**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup#getting-sha-keys-for-release-mode).

![SHA-256 key](https://docs.flutterflow.io/assets/images/sha-256-key-5cdec65c7cedca46e5b2c6759f268cf1.png)

1. Open the [Google Developers Console](https://console.developers.google.com/) (Make sure your project is selected in the dropdown at the top), Click on the **Library** menu on the left, search for the **Google Play Integrity API,** and enable it.
2. Now, you can test your app on a real device using FlutterFlow’s Local Run. Follow the [Local Run documentation](https://docs.flutterflow.io/testing/local-run) and see [how to set up a physical device](https://docs.flutterflow.io/testing/local-run#setup-physical-device) to start testing.

##### 9. Verify user creation

To confirm the successful integration and the creation of users, navigate to your **Firebase project > Authentication > Users** and check the user entries.

#### FAQs

How do I test with dummy numbers?

To try phone sign-in without any limitations, you can add some fictitious numbers to the Firebase console.

To add the fictitious number:

1. Open the [Firebase console](https://console.firebase.google.com/) and click on **Authentication**.
2. Select the **Sign-in method** tab.
3. Click on the **Phone** (Under the Sign-in providers section).
4. Scroll down, find the **Phone numbers for testing** menu, and click on it.
5. Enter any dummy phone number (Make sure it looks unreal).
6. Enter the verification code that you would use on the verify code page.
7. Click on **add**.

Getting this error: "The given sign-in provider is disabled for this Firebase project. Enable it in the Firebase console, under the sign-in method tab of the Auth Section."

1. First, ensure you have clicked the "Save" button while [Enabling phone authentication in Firebase](https://docs.flutterflow.io/integrations/authentication/firebase/phone#2-enabling-phone-authentication-in-firebase).

![Enabling phone authentication in Firebase](https://docs.flutterflow.io/assets/images/adding-authorized-domain-44d8bcb1a06fe163b52139709e7bbacf.png)

1. If this is already enabled, head over to **Settings > SMS region policy >** select **Allow > Select regions** you want to support and click **Save**.

![SMS region](https://docs.flutterflow.io/assets/images/sms-region-5f476d85776e01b56251b53af01a767e.webp)

---

### Authentication: Generated Code {#authentication-generated-code}

*Learn about the generated code behind enabling authentication in FlutterFlow.*

**Source:** https://docs.flutterflow.io/integrations/authentication/generated-code

In FlutterFlow, enabling Authentication is a very simple task. You can check the documentation for the same here but ideally it is just enabling Authentication in Settings, choose your Authentication Type and adding an Action to your desired Auth button. But behind the scenes, a lot of code generation happens to enable this function for you, lets go through it one by one.

We will first discuss the base authentication architecture and then discuss the code changes when we choose custom authentication vs Firebase/Supabase auth.

#### File structure

When we enable Authentication in the Settings dashboard, it creates the following folders in our file structure to manage custom authentication.

```
lib/
    auth/
         custom_auth/
              auth_util.dart
              custom_auth_manager.dart
              custom_auth_user_provider.dart
```

Similarly, when we enable say Firebase authentication, the following files and folders are generated for you.

```
lib/
    auth/
         firebase_auth/
              auth_util.dart
              email_auth.dart (along with other providers)
              firebase_auth_manager.dart
              firebase_user_provider.dart
         auth_manager.dart
         base_auth_user_provider.dart
```

> **Info:** This documentation is exclusively focused on the generated code for Custom Authentication. For instructions on integrating custom authentication into your FlutterFlow app, please refer here.

### Apple Login {#apple-login-2}

*Learn how to integrate Apple Login of Supabase Auth into your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/supabase/apple

Adding Apple Sign-In with Supabase offers a convenient, secure, and privacy-friendly way for users to sign up or log in to your app using their Apple ID.

This guide will walk you through the steps necessary to integrate Apple login with Supabase, including configuring the necessary keys and settings in both Supabase and the Apple Developer Console.

Prerequisites

Before adding Apple Sign-In to your FlutterFlow project, make sure you have:

1. Completed all steps in the [**Supabase setup**](https://docs.flutterflow.io/integrations/supabase/setup)
2. Completed [**Initial setup**](https://docs.flutterflow.io/integrations/authentication/supabase/initial-setup) required for authentication.
3. Created an [**Apple account**](https://account.apple.com/account).
4. An active [**Apple Developer Account**](https://developer.apple.com/programs/enroll/). Read more about the [**Apple Developer Program**](https://developer.apple.com/programs/) and how to sign up.

Adding Apple sign-in comprises of the following steps:

#### Set Up in Apple Developer Console

To set up Apple Sign-In, you need to configure a few settings in your Apple Developer Console. This includes setting up email communication to manage user privacy and enabling the Apple Sign-In capability for your App ID.

##### Configure Email Communication

"Apple sign-in" is a privacy-focused authentication system. One of its notable features is the ability to hide a user's real email address when signing up for apps and services. When users choose to hide their email, you get one random email address that forwards to the user's actual Apple ID email. This helps users keep their real email addresses private.

![hide-apple-email.avif](https://docs.flutterflow.io/assets/images/hide-apple-email-4797a25c79fdfa22556f73f4aaf20d91.avif)

So, in order to contact such users, you must register email sources that your organization will use for communication.

To register email sources, open the [**Services**](https://developer.apple.com/account/resources/services/list) (under [**Certificates, Identifiers & Profiles**](https://developer.apple.com/account/resources/certificates/list)) section in your Apple developer account, configure **Sign in with Apple for Email Communication**, add the email source, and complete the registration process.

##### Enable Apple Sign-In Capability in your App ID

To enable Apple sign-in for your app, open the [**Identifiers**](https://developer.apple.com/account/resources/identifiers/list) section in your Apple developer account, select your existing **App ID**, enable **Sign In with Apple**, and click **Save**.

> **Tip:** If you haven't created an App ID yet, follow the instructions provided by Apple to [**register an App ID**](https://developer.apple.com/help/account/manage-identifiers/register-an-app-id/).

#### Configure Apple Auth in Supabase

To enable and configure Apple authentication in your Supabase project, open the [Supabase dashboard](https://supabase.com/dashboard/project/_/auth/providers), select your project, enable **Sign in with Apple** under the **Apple** section, enter the **Client ID** and **Secret Key**, and click **Save**.

> **Tip:** To obtain the secret key, use the tool provided under [**Configuration section**](https://supabase.com/docs/guides/auth/social-login/auth-apple?queryGroups=platform\&platform=flutter#flutter-configuration-web).

![get-secret-key.avif](https://docs.flutterflow.io/assets/images/get-secret-key-2f2a50880520c81cecf2784e729c7493.avif)

#### Enable Apple Auth in FlutterFlow

To enable Supabase Apple authentication in FlutterFlow, go to **Settings and Integrations** > **Supabase** > **Supabase Authentication**, and toggle on **Enable Apple Authentication**.

![enable-apple-auth-flutterflow.avif](https://docs.flutterflow.io/assets/images/enable-apple-auth-flutterflow-1746e0bf61acaaef283ec81baaf789bb.avif)

#### Create Account \[Action]

Now, proceed to add an account creation flow, which consists of the following two actions:

1. **Create Account Action**: Add the **Create Account** action (under Supabase Authentication). This will create an account in Supabase and add the user details to **Supabase Dashboard > Authentication > Users**.
2. [**Insert Row Action**](https://docs.flutterflow.io/integrations/database/supabase/database-actions#insert-row-action): The previous action does not automatically create an entry in the public "users" table you created [here](https://docs.flutterflow.io/integrations/authentication/supabase/initial-setup#1-creating-a-users-table). To do this, add a **Supabase Insert Row** action, to log the user's details, such as their email.

![create-account.avif](https://docs.flutterflow.io/assets/images/create-account-2fc4d2bda51572603955b581ef39054f.avif)

#### Login \[Action]

To enable user login, add the **Log In** action (under Supabase Authentication). When users click on the sign-in button, they will be prompted to log in with their Apple credentials.

![login.avif](https://docs.flutterflow.io/assets/images/login-c58aab763a4eb1ce27d983109cc300d9.avif)

#### Logout \[Action]

To let users log out of your app, you can use [this](https://docs.flutterflow.io/integrations/authentication/supabase/auth-actions#log-out-action) action.

#### Prepare to Test

To test your app on a real device, you must configure the project in Xcode. This includes adding a team to your project and setting an appropriate signing certificate.

Here's how you configure your project in Xcode:

1. From the Local Run, [open your project in Xcode](https://docs.flutterflow.io/testing/local-run#access-project-code).

> **Tip:** If you are using Android Studio, right-click on the **ios** folder, find **Flutter,** and then click on the **Open iOS module in Xcode**.

2. In Xcode, click on **Runner** (left side menu) and then select the **Signing and Capabilities** tab.
3. We recommend choosing the **Automatically manage signing** option. This will auto-create the profiles, app ID, and certificates required to build and run your app. If you don't, you'll have to [manually create a 'provisioning profile'](https://blog.codemagic.io/distributing-native-ios-sdk-with-flutter-module-using-codemagic/) and then add it in the Xcode.
4. Under the **Signing** section, find the **Team** dropdown and select your team.
5. Now use [Local Run](https://docs.flutterflow.io/testing/local-run) to test the app on a real device.

#### Verify User Creation

To verify that you have successfully added the Apple authentication, you can come over to your **Supabase project > Authentication > Users** and verify the user entries. Also, verify entries in your public `users` table.

![user-entries-in-supabase-auth](https://docs.flutterflow.io/assets/images/user-entries-in-supabase-auth-37198d7578c002efde7b523278ed7e3b.avif)

---

### Authentication Actions {#authentication-actions}

*Learn how to add Supabase Authentication actions in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/supabase/auth-actions

Currently FlutterFlow supports the following Actions for Supabase Authentication:

#### Log in \[Action]

This action provides users with multiple login options to access their accounts.

Follow the steps below to add Email Login action:

1. Select the widget(e.g., Button) on which you want to add the action.
2. Select **Actions** from the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) (the right menu) and click + **Add Action**.
3. Search and select the **Log in** (under *Backend/Database > Supabase Authentication*) action.
4. Set **Auth Provider** to **Email**.
5. Set the **Email Field** dropdown to the widget name that accepts email (e.g., *TextFieldEmail*).
6. Set the **Password Field** dropdown to the widget name that accepts a password (e.g., *TextFieldPassword*).

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/supabase-login-action.gif?alt=media\&token=a4aa0271-50b9-450f-b1e0-69860f0e66b3)

#### Create Account \[Action]

By using this action, you can provide your users with the flexibility to create their accounts in different ways, according to their preferences.

> **Note:** As of now, we support creating accounts with Email/Password, Google and Apple auth providers.

Follow the steps below to add email signup action:

1. Select the widget(e.g., Button) on which you want to add the action.

2. Select **Actions** from the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) (the right menu), **Open** the **Action Flow Editor,** and click + **Add Action**.

3. Search and select the **Create Account** (under *Backend/Database > Supabase Authentication*) action.

4. Set **Auth Provider** to **Email**.

5. Set the **Email** **Field** dropdown to the widget name that accepts email (e.g., *TextFieldEmail*).

6. Set the **Password Field** dropdown to the widget name that accepts a password (e.g., *TextFieldPassword*).

7. Similarly, If you have a confirm password field in your UI, set the **Confirm Password Field** to the appropriate one.

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/create-account-action.gif?alt=media\&token=372a8285-bd24-4279-b141-4a02085168c0)

#### Log out \[Action]

This action enables users to securely log out of their account and clear their session data from the app, which ensures that their account remains safe and secure.

Follow the steps below to add this action:

1. Select the widget (e.g., Button) on which you want to add the action.

2. Select **Actions** from the Properties Panel (the right menu), If it's the first action, click **+ Add Action** button. Otherwise, click the "**+**" button below the previous action tile (inside **Action Flow Editor**) and select **Add Action**.

3. Search and select the **Log Out** (under **Backend/Database > Supabase Authentication**) action.

![img\_6.png](https://docs.flutterflow.io/assets/images/img_6-d59b94e106d404251a6053eb1e1ba61b.png)

#### Send Reset Password Email \[Action]

This action allows users to reset their password by sending a reset link to their registered email address.

Prerequisites

To build the reset password functionality, you need to create the following two pages in your app:

1. **ForgotPassword Page**: This page allows users to enter their email address and request a password reset link.
2. **UpdatePassword Page**: This page allows users to set a new password after clicking on the reset link.

Here’s how you can add the Supabase reset password feature to your app:

1. On the **ForgotPassword Page**, add the **Send Reset Password Email** action and set the **Email Field** dropdown to the widget that accepts the user's email address. This action will send the reset password link to the provided email.
2. The reset link sent to the user will open the **UpdatePassword Page**. On that page, add the **Update Password** action and set the **Password Field** and **Confirm Password Field** to the respective input widgets.
3. Copy the route name of the **UpdatePassword Page** and paste it into the **Supabase Dashboard > Authentication > Email Templates > Reset Password > Source**. After **`"{{ .ConfirmationURL}}"`** add **`"/[here]"`** only if you're not using a [custom redirect URL](https://docs.flutterflow.io/integrations/authentication/supabase/auth-actions#use-custom-redirect-urls). If using a custom redirect URL, the confirmation URL will redirect directly to your specified path.
4. [Deploy your app to the web](https://docs.flutterflow.io/deployment/web-publishing).
5. Copy the URL of your deployed project and paste it into the **Supabase Dashboard > Authentication > URL Configuration > Site URL**.

> **Tip:** **For mobile**, you must set the **deep link URL** as the Site URL. To find this, navigate to **FlutterFlow > Settings & Integrations > App Details > Routing & Deep Linking**, open the **URL Scheme** tooltip, and copy the URL.

![mobile-deeplink.avif](https://docs.flutterflow.io/assets/images/mobile-deeplink-6d0ca0a2b81a9f9f8e817e8992f66d80.avif)

##### Use Custom Redirect URLs

Instead of relying on the default `{{ .ConfirmationURL }}` path, you could optionally configure a **custom redirect URL** in Supabase. This option allows you to bypass the default setup and send users directly to a custom page in your app for resetting their password.

To configure a custom redirect URL:

1. When adding the **Send Reset Password Email** action in FlutterFlow, enter the **Redirect To** URL. For example `http://my-site.com/resetPassword`.
2. Whitelist this custom URL by navigating to **Supabase Dashboard > Authentication > URL Configuration > Redirect URL**, and click **Add URL** to include it.
3. Update the reset password template. Go to **Supabase Dashboard > Authentication > Email Templates > Reset Password > Source** and ensure only `{{ .ConfirmationURL }}` is present in the template (remove any appended route names).

#### Delete User

At present, we do not support deleting Supabase user action. However, you can refer to this community video for guidance on how to do so.

[YouTube video player](https://www.youtube.com/embed/PNBvc35CDAk)

---

### Email Authentication {#email-authentication}

*Learn how to integrate Email Login of Supabase Auth into your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/supabase/email

Supabase email authentication is a secure and easy way to allow users to sign up and log in to your application using their email and password.

Prerequisites

Before getting started with this section, ensure you have,

1. Completed all steps in the [**Supabase setup**](https://docs.flutterflow.io/integrations/supabase/setup)
2. Completed [**Initial setup**](https://docs.flutterflow.io/integrations/authentication/supabase/initial-setup) required for authentication.

#### Adding Email Authentication

Let's see how to add a Supabase email authentication by building an example that looks like this:

The steps to add Supabase email authentication are as follows:

##### Configure Email Authentication in Supabase

Due to some Supabase auth behavior, you need to disable the email verification on the Supabase side. However, you can still add the email verification logic on your own in your app if you wish to.

Here's how you disable email verification on the Supabase side:

1. In your Supabase project, navigate to **Authentication > Provider**.
2. Open the **Email** section and disable the **Confirm email** and **Secure email change**.

![img\_2.png](https://docs.flutterflow.io/assets/images/img_2-c7a194a0116b8eb06cc80e5ab6bea181.png)

Disable email verification on the Supabase side

##### Building pages

Let's add a page that allows users to create accounts and log in. To speed up, you can add a page from the [template](https://docs.flutterflow.io/resources/ui/pages#create-page-from-template). Here is the page added from the templates, and after some modification, it looks the below:

Also, see how to build a page layout in case you want to build a page from scratch.

![img\_3.png](https://docs.flutterflow.io/assets/images/img_3-dd11fde15d52a4400a5f9616c6588301.png)

##### Adding Create Account \[Action]

Now, you can proceed to add an account creation flow, which basically consists of three actions in the following order:

1. Supabase [Create Account Action](https://docs.flutterflow.io/integrations/authentication/supabase/auth-actions#create-account-action)
2. Supabase [Insert row action](https://docs.flutterflow.io/integrations/database/supabase/database-actions#insert-row-action)
3. [Navigate](https://docs.flutterflow.io/concepts/navigation/overview) action

The first one creates an account in Supabase and adds an email and password in the "auth.users" table (i.e., *Protected schemas > schema auth*). However, this action does not create an entry in the "users" table you created [here](https://docs.flutterflow.io/integrations/authentication/supabase/initial-setup#1-creating-a-users-table). To do so, you need to add another action called Supabase *insert row* action with the user's details, such as email and profile\_pic. Once the entry has been created, you can navigate to the home page using the navigate action.

Here's how it looks:

##### Adding Log In \[Action]

To allow users to log in with their credentials, you can use the [**Log In**](https://docs.flutterflow.io/integrations/authentication/supabase/auth-actions#log-in-action) action.

##### Adding Logout \[Action]

To let users log out of your app, you can use the [**Log Out**](https://docs.flutterflow.io/integrations/authentication/supabase/auth-actions#log-out-action) action.

##### Verify user creation

To verify that you have successfully added the email authentication, you can come over to your Supabase project > Table Editor > select the "users" table and verify the user entries.

![img\_5.png](https://docs.flutterflow.io/assets/images/img_5-b6c2a02e968b3063223f358f527a92da.png)

##### What's next?

Now that you have successfully added the Supabase email authentication in your app, you can access the logged-in user's details, such as email, user id, phone number, email verified, and JWT token via the **Set Variable menu > Authenticated User**.

Here's an example of filtering the to-do list based on the logged-in user using the **Set Variable menu > Authenticated User > User ID** property.

---

### Google Login {#google-login-2}

*Learn how to integrate Google Login of Supabase Auth into your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/supabase/google

Google Authentication with Supabase offers a secure and convenient method for users to sign up and log in to your app using their Google accounts.

Prerequisites

Before getting started with this section, ensure you have,

1. Completed all steps in the [**Supabase setup**](https://docs.flutterflow.io/integrations/supabase/setup)
2. Completed [**Initial setup**](https://docs.flutterflow.io/integrations/authentication/supabase/initial-setup) required for authentication.

#### Adding Google authentication

Let's see how to add a Supabase Google authentication by building an example that looks like this:

The steps to add Supabase Google authentication are as follows:

##### 1. Create and configure Google Cloud project

To begin adding Google auth, you must first have an active [Google Cloud Platform](https://cloud.google.com/) account. You'll need to either set up a new project or use an existing one within this account.

Here's how you do it:

1. If you haven't already, create a new project in [Google Cloud Console](https://console.cloud.google.com/).

2) If you haven't already, configure the [OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent). This helps Google display a consent screen to the user, including a summary of your project and its policies and the requested scopes of access.

3. Now, you must create credentials so that your app can access Google data. To do so: 1. Head over to [credentials page](https://console.cloud.google.com/apis/credentials), click **+ CREATE CREDENTIALS** and select **OAuth client ID**.
   2. Set **Application type** to **Web Application**.
   3. Below, under the **Authorized redirect URIs**, click **+ ADD URI**. To get this URI, open your **Supbase project > Authentication > Providers**. Open the **Google** section, copy the **Callback URL**, and paste it here.
   4. Click **CREATE**.
   5. Copy the **Client ID** and **Client secret**; you'll need this in the next step.

4) For *Android*, you'll need to create a new credential with the **Application Type** set to **Android**. While creating, you'll need to provide the package name and [SHA-1 key](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup#generate-the-sha-1-key). **Note** that after your app goes live, you must replace the SHA-1 key with the [key from the Play Console](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup#getting-sha-keys-for-release-mode).

5. Similarly, create credential for *iOS* platform as well. **Note** that after your app goes live, you must specify the *App Store* and *Team ID*.

##### 2. Configure Google auth in Supabase

This step involes enabling Google login and providing the client IDs and secret in Supabase. Here's how you do it:

1. Head over to [Supabase project dashboard](https://supabase.com/dashboard/) **> Authentication > Providers**.
2. Open the **Google** section and turn on the **Enable Sign in with Google**.
3. Paste the **Client ID** and **Client secret** from the **Web** credential.
4. Paste the **Authorized Client IDs** from the **Android** credential.
5. Turn on the **Skip nonce checks** to support **iOS** platform.

6) Now, you must specify the redirect URL in [Supabase project dashboard](https://supabase.com/dashboard/) **> Authentication > URL Configuration**. It is the URL to which a user is sent after successful authentication. Here's how you do it for both web and mobile.

##### 3. Enable Google auth in FlutterFlow

To enable Supabase Google auth in FlutterFlow:

1. In FlutterFlow, navigate to the **Setting and Integrations** **>** **App Settings > Authentication**.
2. Open the **Supabase Authentication** section and turn on the **Enable Google Authentication** toggle.
3. Paste the **iOS** and **Web Client ID** obtained in step 1.

##### 4. Add a Google sign-in button

To allow users to authenticate, you need a login page with a button. You can create your own or use the one from the widget template or page template.

Here's how you can add the Google sign-in button from our page template:

##### 5. Adding create account action

Now, you can proceed to add an account creation flow, which basically consists of two actions in the following order:

1. Supabase create account action. Here's how you add it: 1. Select the widget (e.g., Button) on which you want to add the action.
   2. Select **Actions** from the Properties panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.
   3. Click on the **+ Add Action**.
   4. Search and select the **Log in** (under *Backend/Database > Supabase Authentication*) action.
   5. Set **Auth Provider** to **Google**.

2. Supabase [insert row action](https://docs.flutterflow.io/integrations/database/supabase/database-actions#insert-row-action)

The first one creates an account in Supabase and adds the user details at *Supabase Dashboard > Authentication > Users*. However, this action does not create an entry in the "users" table you created [here](https://docs.flutterflow.io/integrations/authentication/supabase/initial-setup#1-creating-a-users-table). To do so, you need to add another action called Supabase *insert row* action with the user's details, such as email.

##### 6. Adding login action

When you click the Google sign-in button, it will trigger the 'Log In' action, prompting a Google sign-in popup for users to input their credentials.

To add login action:

1. Select the widget (e.g., Button) on which you want to add the action.
2. Select **Actions** from the properties panel (the right menu) and select **Add Action**.
3. Search and select the **Log in** (under *Backend/Database > Supabase Authentication*) action.
4. Set **Auth Provider** to **Google**.

![Adding login action](https://docs.flutterflow.io/assets/images/adding-login-action-a46c475b4cd576832776c52a3c962132.avif)

##### 7. Adding logout action

To let users log out of your app, you can use [this](https://docs.flutterflow.io/integrations/authentication/supabase/auth-actions#log-out-action) action.

##### 8. Preparing to test the app

Currently, testing the Supabase Google login feature isn't possible in Run or Test modes due to certain restrictions. But, for web platform testing, you can publish your app with a subdomain using our [web publishing](https://docs.flutterflow.io/deployment/web-publishing) feature.

You can test your app on a real device or emulator using FlutterFlow’s Local Run. Follow the [Local Run documentation](https://docs.flutterflow.io/testing/local-run) and see [how to set up a physical device](https://docs.flutterflow.io/testing/local-run#setup-physical-device) to start testing.

##### 9. Verify user creation

To verify that you have successfully added the Google authentication, you can come over to your Supabase project > Authentication > Users and verify the user entries.

![Verify user creation](https://docs.flutterflow.io/assets/images/verify-user-creation-8226603473539212d9a93c67818fc86d.avif)

---

### Initial Setup {#initial-setup}

*Learn how to perform the initial setup for Supabase Authentication in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/authentication/supabase/initial-setup

To use authentication, you will need to complete the following initial setup:

1. [Creating a "users" table](https://docs.flutterflow.io/integrations/authentication/supabase/initial-setup#1-creating-a-users-table)
2. [Enabling authentication in FlutterFlow](https://docs.flutterflow.io/integrations/authentication/supabase/initial-setup#2-enabling-authentication-in-flutterflow)

Prerequisites

Before you begin, make sure you have completed the [**Supabase Setup**](https://docs.flutterflow.io/integrations/supabase/setup).

##### 1. Creating a "users" table

To use Supabase authentication, you'll need to create a table to store your users' data, such as their name, email, and profile picture.

Also, it's recommended to create a [foreign key relationship](https://supabase.com/docs/guides/database/tables#joining-tables-with-foreign-keys) from the `id` column of your "users" table to the `id` column of the "users" table in auth (protected) schema, i.e., `auth.users.id` with `on delete cascade`. This ensures that when a user is deleted from the "auth.users" table, their corresponding data in your "users" table will also be removed.

Here's how you do it:

> **Note:** The "users" table in auth (protected) schema is a private table that Supabase uses to store auth-related sensitive information such as email, encrypted pass, and confirmation token. ![img.png](https://docs.flutterflow.io/assets/images/img-b181589c7111a788900a2fa263eafee3.png)

##### 2. Enabling authentication in FlutterFlow

To enable authentication in FlutterFlow:

1. Open your FlutterFlow project.

2. Navigate to the Setting and Integrations () from the Navigation Menu > App Settings > Authentication.

3. Turn on the **Enable Authentication** toggle and select **Authentication Type** to **Supabase**.

4. To ensure that your users are directed to the appropriate pages based on their login status, you must set the [initial pages](https://docs.flutterflow.io/resources/projects/settings/general-settings#initial-page).

![img\_1.png](https://docs.flutterflow.io/assets/images/img_1-b7c8f0344e87b684233866df3d4144e5.png)

---

### Tokens: Types and Lifespans {#tokens-types-and-lifespans}

*Learn about the types and lifespans of tokens in custom authentication.*

**Source:** https://docs.flutterflow.io/integrations/authentication/tokens

The most crucial component of our generated authentication system is the `CustomAuthManager` class. It is responsible for managing authentication session attributes such as the `authenticationToken`, `refreshToken`, `tokenExpiration`, and user-specific attributes like `uid` and `userData`.

This class provides essential functionalities including: `signIn()`: Handles user sign-in processes.

`signOut()`: Manages user sign-out actions.

`updateAuthUserData()`: Updates authentication and user data.

`persistAuthData()`: Persists authentication data across sessions for persistent login capabilities.

In addition to the `CustomAuthManager`, we have another important file in our authentication framework: `custom_auth_user_provider.dart.`

This file defines a class, `<ProjectName>AuthUser`, to encapsulate the state of an authenticated user. It leverages BehaviorSubject from the [rxdart](https://pub.dev/packages/rxdart) package to manage a stream of the user object, enabling real-time updates to the user's authentication state. This stream is initially set with a user object that indicates a logged-out state. Subsequent authentication actions will update this stream, enabling real-time adjustments to any part of the application that depends on the user's authentication status.

Building on our authentication framework, the `custom_auth_manager.dart` file brings in the currentUser variable, an instance of the `<ProjectName>AuthUser` class. This global reference allows for quick and centralized access to the currently signed-in user's information, enabling access to their authentication state across the application.

The `loggedIn` property further simplifies verifying if a user is logged in by checking the currentUser's status.

#### Auth Manager Initialization

Then, we have the auth\_util file, which contains a singleton instance of `CustomAuthManager`

```
final _authManager = CustomAuthManager();
CustomAuthManager get authManager => _authManager;
```

The `authManager.initialize()` is called in `main()` before runApp is executed.

The `initialize()` method creates an instance of SharedPreferences, preparing it for `authToken`, `refreshToken`, etc, and also handles the logic for token expiration, including the automatic logout when these tokens expire.

> **Info:** Also note that this initialization occurs only because the 'Persist Auth Sessions' option has been enabled in the Custom Authentication Settings.

![Alt text for the image](https://docs.flutterflow.io/img/persist-auth-session.png)

This file also offers easy-to-use getters for essential information such as the user's ID, login token, and other data. This setup simplifies the process of accessing and managing login details throughout your app.

#### Log in Implementation

When the Log In action is activated by tapping a button, we initiate a series of operations behind the scenes to ensure a smooth login process.

Upon calling the signIn method, it triggers the `_updateCurrentUser` method from `CustomAuthManager` internally.

This method receives various parameters such as `authenticationToken`, `refreshToken`, `tokenExpiration`, `authUid`, and `userData`, updating the CustomAuthManager class's properties with these details. Consequently, this stores the current session's authentication and user information effectively.

> **Info:** To learn more about the concepts of Authentication Token, Refresh Token, and Token Expiry Time, please refer the [Concepts](https://docs.flutterflow.io/integrations/authentication/tokens) doc.

A new user object, marked as logged in (`loggedIn` set to true), along with the provided `authUid` and `userData`, is then added to the user object stream mentioned earlier. This update informs all the stream's subscribers about the changed user state, signaling that the user has successfully logged in.

Additionally, the `persistAuthData` method is invoked to save the updated authentication details (tokens, expiration, user ID, etc.) for future sessions.

After signing in, `context.goNamedAuth('AuthPage', context.mounted);` is called that navigates the user to the Logged In Page specified in FlutterFlow's Authentication Settings.

---

### Creating Collections {#creating-collections}

*Learn how to create collections in Firestore for your FlutterFlow app, including organizing documents within collections.*

**Source:** https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-collections

A collection is a group of documents. For example, you could have a 'users\*'\* collection that contains a list of documents, each representing a single user.

![img\_20.png](https://docs.flutterflow.io/assets/images/img_20-f99f4388b62b57262c21368ac5281a0c.png)

User collection document model

Getting Started: Things to Know First

* Get to know how to [**structure the Firebase Database**](https://docs.flutterflow.io/integrations/database/cloud-firestore/getting-started#structuring-the-database).
* Ensure you've gone through and completed every step in the [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) for your project.

#### Creating a collection

Here are the steps to create a collection:

1. Click on the **Firestore** from the Navigation Menu (left side of your screen).

2. Click on the **(+)** Plus sign button.

3. A popup will appear, Enter the collection name and click **Create** Button.

4. Next, [define the collection schema](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-collections#define-schema-creating-fields) (create Fields) and [add some data](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-actions#create-document-action) to the collection.

> **Info:** A collection will only appear on [**Firebase Console**](https://console.firebase.google.com/u/0/) if it contains at least one document.

##### Define Schema (Creating Fields)

A document represents a single item or entity, such as a user, post, animal, etc. To add data inside the document, you must define the document schema by creating Fields. Creating Fields helps you know what kind of data a document can contain.

Although you can add more fields later on, it's always a good idea to add fields from the start.

> **Caution:** Field names cannot be changed, so ensure that you have used the correct Field names.

To define the schema (create fields) for the document:

1. Select your collection from the list on the left side.

2. If you haven't added any fields yet:

   1. You can choose from the template collections that have common fields needed in most applications. This will auto-add all the fields.
   2. Click on **Start from scratch** to define your own schema.
   3. Or, use [AI Gen Schema](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-collections#create-schema-using-ai-gen).

3. To add a new field, start typing its name (e.g., title, description, date, etc.) and choose the suitable **Data Type**.

4. While choosing the Data Type, you can set if it will be a list or not using **Is List?** toggle.

   1. You can keep it disabled for storing only a single value. For example, fields such as title, description, price, etc., can have only one value. You can't have multiple titles for a single post.
   2. You can enable it to store multiple values of the same data type. For example, to store the list of accessory names for the field accessories.

5. Click on the **Done** icon.

> **Tip:** You can also use *Tab* and *Enter* keys to navigate quickly while creating fields.

##### Create schema using AI Gen

With **AI Gen Schema**, you can automatically generate a schema for your Firebase collection from a simple prompt.

To get better results...

...you can try optimizing your prompt. i.e., make it more descriptive.

Example prompts:

* Generate a collection for books, their reviews, and their purchase history.
* Create a database schema for music albums, their ratings, and sales records.
* Generate a collection for video games, their user reviews, and purchase history.
* Create a collection for art exhibits, visitor reviews, and ticket bookings.
* Generate a collection for online courses, student feedback, and enrollment records.

***

> **Note:** To learn more about custom data types within FlutterFlow, [check this doc](https://docs.flutterflow.io/resources/data-representation/data-types#built-in-data-types)

---

### Creating Subcollections {#creating-subcollections}

*Learn how to create subcollections in Firestore for your FlutterFlow app, including organizing documents within subcollections.*

**Source:** https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-subcollections

[Collections](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-collections) that are created inside the document are called subcollections. For example, you could have a 'comments' subcollection inside the 'posts' collection to store a post's comments.

Subcollection is best when you have several queries/filters or search on a collection based on the other collection. For example, loading or searching the comments of a specific post. (i.e., show all comments of a post with more likes.)

Feature Completion

At this time, FlutterFlow supports one level of nesting (e.g., collection -> subcollection). Second-level nesting is not currently supported ( e.g., collection -> subcollection 1 -> subcollection 2.)

![img\_21.png](https://docs.flutterflow.io/assets/images/img_21-eb0073a7794e33e857bb128f3b57d8f4.png)

Getting Started: Things to Know First

* Get to know how to [**structure the Firebase Database**](https://docs.flutterflow.io/integrations/database/cloud-firestore/getting-started#structuring-the-database).
* Ensure you've gone through and completed every step in the [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) for your project.

#### Working with subcollections

In this section, you'll learn to work with subcollections by building an example that allows you to see all messages and post a new message in a chat room (example below).

Here are a few tips on how subcollections work in FlutterFlow:

* You can create a subcollection document under an existing reference if there is a subcollection defined.
* You can either specify the reference to query a subcollection (UserA -> favorites) or can do a “collectionGroup” query across all subcollections (all Users -> Favorites) by not specifying the reference.

Before we begin, we need to identify the collections and define the database structure. So looking at the requirements, it's very clear that we'll need two collections. One for storing chat room details and another for storing its messages. And we need to display the messages only for a specific chat room. So, having the message collection as a subcollection of the chat rooms seems to be a good option.

Here's what the database structure looks like:

![img\_22.png](https://docs.flutterflow.io/assets/images/img_22-9f9568a94eb866b20899d864891eab8e.png)

Building the chat room example comprises the following steps:

1. [Creating a collection](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-subcollections#1-creating-a-collection)
2. [Creating a subcollection](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-subcollections#2-creating-a-subcollection)
3. [Add data to the collection](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-subcollections#3-add-data-to-the-collection)
4. [Building chat room listing page](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-subcollections#4-building-chat-room-listing-page)
5. [Building messages page](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-subcollections#5-building-messages-page)

##### 1. Creating a collection

[**Create the collection**](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-collections) called *chat\_rooms*. This will be used to hold the chat room details. While defining the schema for *chat\_rooms* collection, add the fields to display its name, i.e., *chat\_room\_name.*

![img\_23.png](https://docs.flutterflow.io/assets/images/img_23-0ab98eb05f49d1d28f073680489f1c7f.png)

##### 2. Creating a subcollection

To create the subcollection:

1. Click on the **Firestore** from the Navigation Menu (left side of your screen).

2. Click on the **(+)** Plus sign button.

3. A popup will appear; enter the collection name as '*messages.'*

4. **Turn on** the **Is Subcollection** toggle.

5. The dropdown list with existing collections will appear. Click on the **Unset** and select the parent collection, *chat\_rooms* in this case.

6. Click **Create** Button.

7. Next, [define the document schema](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-collections#define-schema-creating-fields). While defining the schema for the 'messages' subcollection, add the fields such as *message* (to store the message body) and *from* (to store the sender name).

##### 3. Add data to the collection

Add some default chat room details using [Firestore Content Manager](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-content-manager).

##### 4. Building chat room listing page

The first page shows the chat room listing, and when you tap, it opens the new page and shows all messages.

The steps to build the chat room page are as follows:

1. Query the **chat\_rooms** collection and display the chat room names in a ListTile (inside ListView).

2. Add the **[Navigate To](https://docs.flutterflow.io/concepts/navigation/overview#navigation-actions)** action **on Tap** of the **ListTile** and open the messages page. **Note**: While navigating, pass the chat room record to the next page. Learn how to [pass data to the next page](https://docs.flutterflow.io/concepts/navigation/passing-data). .

##### 5. Building messages page

The next page shows all the messages and allows you to send messages in the chat room.

The steps to build the chat room page are as follows:

1. Use the **ListView**, **ListTile**, **TextField**, and **Button** widgets to design a page that looks like the below:

![img\_24.png](https://docs.flutterflow.io/assets/images/img_24-ca68c3f4b34738abbe7ff5dda39534c5.png)

2. On the ListView, query a subcollection as you would query any other collection; except for the subcollection, you must provide its parent collection reference (i.e., chat\_rooms reference in this case). This way, you'll only see messages from that specific chat room.

3) On tap of 'Send' button, add the [create document](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-actions#create-document-action) action for `messages` collection and provide current `chat_rooms` reference. Also, provide the message to add via **From Variable > Widget State > \[TextFieldName]**.

---

### Firestore Actions {#firestore-actions}

*Learn about Firestore actions in your FlutterFlow app, including how to perform various database operations.*

**Source:** https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-actions

The Firestore action allows you to create, update, or delete a record from a Firestore Collection.

Prerequisites

* Get to know how to [**structure the Firebase Database**](https://docs.flutterflow.io/integrations/database/cloud-firestore/getting-started#structuring-the-database).
* Ensure you've gone through and completed every step in the [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) for your project.
* Created a [**collection**](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-collections)

#### Types of Firestore Database Actions

Following are the types of Firestore database action:

1. [**Create Document**](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-actions#create-document-action)**:** Creates a new record inside the specified Firestore Collection.
2. [**Read Document**](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-actions#read-document-action): Fetches document data using a reference.
3. [**Update Document**](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-actions#update-document-action)**:** Updates the specified field value of the existing document.
4. [**Delete Document**](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-actions#delete-document-action)**:** Deletes records inside the specified Firestore Collection.
5. [**Query Collection**](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-actions#query-collection-action): Retrieves record(s) from the Firstore collection.

##### Create Document \[Action]

Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to add the action.

2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.

3. Click on **+ Add Action**.

4. On the right side, search and select the **Firestore** > **Create Document** action.

5. Set the **Collection** to your collection name.

6. Under the **Set Fields** section, click on the **+ Add Field** button.

7. Open the *Field* to pass its value from a widget: * Set the **Value Source** to **From Variable**.
   * Click on **UNSET** and select **Widget State > Name** of the TextField.

8. Similarly, add the field for the other UI elements.

9. By default, documents are added with an auto-generated ID. However, if you prefer to use your own ID for the document, you can enable the **Custom ID** toggle.

##### Read Document \[Action]

There are some scenarios where you may want to fetch document data in response to a widget action. For example, fetching the user's profile details like name, profile picture, and bio to display them on click of a button.

Here are some more use cases where you may find this action helpful:

* Fetching additional user details for a post or comment.
* Retrieve product details, price, and availability for order IDs in a user's cart.
* Get details for cities referenced within a country document in a travel app.

Let's see how to add this action with an example that fetches and displays the details of users who've reviewed a travel destination. Here's how it looks:

Here's how collections are setup:

![img\_25.png](https://docs.flutterflow.io/assets/images/img_25-ac2455b536426cfbb3d2072fcf942d70.png)

Follow the steps below to define this action to any widget:

1. Select the **Widget** (e.g., Button) on which you want to add the action.
2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.
3. Click on **+ Add Action**.
4. On the right side, search and select the **Firestore** > **Read Document** action.
5. Now, **Select Reference to Read** data from.
6. Provide the **Action Output Variable Name**. This will be used to store the document data.

7) Now, you can use the *Action Output Variable Name* provided in the previous step to fetch the details. For example, to display data on Text widget, select the **Text widget > Properties Panel > Text > Set Variable menu > ***\[action\_output\_variable\_name]*** > select the field** you want to display.

##### Update Document \[Action]

Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to add the action.

2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.

3. Click on **+ Add Action**.

4. On the right side, search and select the **Firestore** > **Update Document** action.

5. In order to update a specific document within a Firebase collection, you need to specify the reference to that document. The reference acts as a pointer to the exact document you want to update.

6. Under the **Set Fields** section, click on the **+ Add Field** button.

7. Open the *Field* to pass its value from a widget:

   1. Set the **Value Source** to **From Variable**.
   2. Click on **UNSET** and select **Widget State > Name** of the TextField.

8. Similarly, add the field for the other UI elements.

##### Delete Document \[Action]

Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to add the action.
2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.
3. Click on **+ Add Action**.
4. On the right side, search and select the **Firestore** > **Delete Document** action.
5. In order to delete a specific document within a Firebase collection, you need to specify the reference to that document. The reference acts as a pointer to the exact document you want to delete.

##### Query Collection \[Action]

There are certain scenarios where you may want to query a collection manually. For example, you might want to only fetch data in response to a specific user action, such as clicking a button or submitting a form.

Additionally, If your app fetches different data under different conditions, you might find it more convenient to manually call queries. For example, fetching different tasks for admin and team members.

To manually query a collection, follow the steps below to define this action to any widget:

1. Select the **Widget** (e.g., Button) on which you want to define the action.

2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.

3. Click on **+ Add Action**.

4. On the right side, search and select the **Firestore** > **Query Collection** action.

5. Choose the **Collection** you want to query.

6. Choose the **Query Type** among the following:

   * **List of Documents:** Use this option when you need to query an entire list of documents from a collection. This is useful for retrieving multiple documents that can be ordered or filtered by specific criteria, such as a keyword.
   * **Single Document:** Select this when you want to fetch a specific single document from a collection, typically identified by its unique ID.
   * **Count:** Choose this option to determine the number of documents that meet certain criteria without retrieving the documents themselves. This is useful for getting quick insights or summaries, like the total number of entries that match a filter.

7. You can also [Filter](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-actions#filtering-a-collection-query) and [Order](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-actions#ordering-a-collection-query) the query result.

8. Provide the **Action Output Variable Name**. This will be used to store the query result.

9) Now, you can use the *Action Output Variable Name* provided in the previous step to generate children from a variable on **ListView**.
10) Finally, you can display data in a **Text** widget. To do so, select the **Text widget > Properties Panel > Text > Set from Variable menu** **> \[children\_from\_variable\_name] item > select the field** you want to display.

###### Filtering a Collection Query

Sometimes, you might need to filter a list based on a condition. For example, you might want to show only incomplete Todo items on the main listing.

To add a filter when querying a collection:

* In the Action properties of **Query Collection Action**, scroll down and click on the **+ Filter** button at the bottom
* Find the **Field Name**, click on the Unset, and select a field on which you would like to apply the filter.
* Find the **Relation** dropdown, click on the **Unset**, and choose the relation among the list.
* Find the **Value** property and set it to an appropriate value and click **Confirm**.

> **Info:** * Select a filter relation that aligns with your specific needs. For instance, if you wish to display only incomplete todos, you can create a field named 'isDone,' set the relation to 'Equal To,' and define the value as 'False.'
* Another example would be to showcase users older than 30; in this case, you'd create a 'Age' field, set the relation to 'Greater Than,' and specify the value as 30.
* You can combine multiple filters using **AND** or **OR** operators to create more advanced filtering logic. This enables you to refine your data query to match specific conditions.

###### Ordering a Collection Query

You might want to show your list based on a specific order. For example, you could show a Todo list in order of due date.

To specify the order when querying a collection:

* In the Action properties of **Query Collection Action**, scroll down and click on the **+ Order By** button at the bottom
* Find the **Field Name**, click on the **Unset**, and select the field which you would like to choose for ordering.
* Find **Order** dropdown, click on the Unset, and choose the order either Increasing or Decreasing and click **Confirm**.

> **Info:** Choose the order based on your requirements. For instance, if you want to display Todo items sorted by their due dates, simply set the **Field Name** to date and the **Order** to Increasing.

> **Warning:** If you apply both filtering and ordering while querying a collection, an index is necessary otherwise FlutterFlow will throw an error. [**Learn how to avoid the errors.**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#adding-indexes)

#### Enabling Firestore Batch Write

When working with databases, you often need to create, update, or delete data. Typically, you would send individual requests to the database for each operation, which requires multiple round trips to the server. This can be time-consuming and inefficient.

By enabling Firestore batch write, you can group multiple operations and send them to the database as a single request. With this, either all the operations within the batch will succeed or none of them will be applied. This guarantees data consistency, so you don't end up with a partially updated state if something goes wrong during the process.

> **Tip:** * You can learn more about [**Firestore Batch Write**](https://firebase.google.com/docs/firestore/manage-data/transactions#batched-writes).
* If you are a newbie, we recommend watching [**this video**](https://youtu.be/dOVSr0OsAoU) first.

Suppose you have an e-commerce application, and after a successful order, you need to update the product inventory count and create a new document in the 'orders' collection. Using a batch write, you can combine these operations and execute them together to ensure data consistency.

To enable Firestore batch write, you must have multiple Firestore any combination of actions; inside the action editor, at the top right side, enable **Batch Firestore Writes**.

![img\_26.png](https://docs.flutterflow.io/assets/images/img_26-7e206b723fb16f08a5900b43e0de2fc5.png)

Enabling Firestore Batch Write

#### Trigger action on data change

Sometimes, you might want to trigger an action whenever the data changes inside the collection. For instance, In a news app, you might want to notify users when new news is available, like this:

To do so:

1. Ensure you have added a **Query Collection** or **Document from Reference** on a widget with **Single Time Query** disabled.
2. Now, on the widget with **Query Collection** or **Document from Reference**, open the **Action Flow Editor** and set **On Data Change** as the [Action Trigger](https://docs.flutterflow.io/resources/functions/action-triggers). This ensures that any actions you add will be triggered whenever the data is updated, added, or deleted.
3. You can now [add any action](https://docs.flutterflow.io/resources/functions/action-flow-editor#adding-an-action-example) you want to perform, such as showing a notification, refreshing the UI, or fetching related data.

> **Info:** If you are using this trigger on a ListView, make sure to **disable** the **Infinite Scroll**.

---

### Firestore Content Manager {#firestore-content-manager}

*Learn how to use the Firestore Content Manager in your FlutterFlow app to manage Firestore data efficiently.*

**Source:** https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-content-manager

The Firestore Content Manager provides an easy way to visually create, edit, and add documents to your [**Firestore database**](https://docs.flutterflow.io/integrations/database/cloud-firestore/getting-started).

> **Info:** Subcollections are not supported in Content Manager at this time.

Prerequisites

Before getting started with this section, ensure you:

1. Become familiar with [**Structuring the Firebase Database**](https://docs.flutterflow.io/integrations/database/cloud-firestore/getting-started#structuring-the-database).
2. Completed all steps in the [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase).
3. Create a [**Collection**](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-collections).
4. [**Defined the Fields**](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-collections#define-schema-creating-fields) for the collection. Only fields defined in your Firebase schema are shown in the Firebase Content Manager.

#### Adding Document

Before you add a new document to the collection, make sure you have some Fields added. For instance, the 'exam\_result' collection with basic fields looks like this:

![img\_12.png](https://docs.flutterflow.io/assets/images/img_12-97c5c5ba66602e35e36bf86d8b9995f8.png)

'exam\_result' collection

To add a document:

1. Head to the **Firestore** (left side Navigation Menu) and click **Manage Content**. This will open up a new browser window.
2. Select the **Collection** to which you want to add a document and then select + **Add Document.** A popup will appear.
3. Enter the information for the record and click **Add Document**.

> **Caution:** If you get this error "**Could not create an account as <firebase@flutterflow.io> to your Firebase project**", just enable the '[**Email Sign-In**](https://docs.flutterflow.io/integrations/authentication/firebase/email-login)' in your Firebase project.

![img\_13.png](https://docs.flutterflow.io/assets/images/img_13-252de78599d465db3bb3b5ca1d49aa86.png)

##### Upload CSV file for bulk addition

You might want to migrate your data from somewhere else to the collection of your current project. Adding an extensive list of records one by one is an incredibly time-consuming process. If you can get or already have data in a CSV (comma-separated values) file, we allow uploading the CSV file, and your data will be loaded into the collection in just a few steps.

> **Info:** To successfully upload the data:

* Ensure you have header rows in your CSV file. The header should contain the exact name of the fields you have in your collection.
* If you are uploading lat-long data, make sure you format it like (lat, lng) or \[lat,lng].
* Dates must be in a format like YYYY-MM-DD HH:MM :SS , where hours should be in 24hrs format (e.g., 2022-11-07 13:05:32).

To better understand, here is the sample places collection and CSV file:

![img\_14.png](https://docs.flutterflow.io/assets/images/img_14-1e462d868d3005b30aec2e5572e00be7.png)

***places.csv***

```
name,location,last_updated
Central,"(40.76835069123224, -73.97203144014624)",2022-11-07 13:05:32
Museum,"(40.8217031079394, -73.9256367137398)",2022-11-09 16:12:02
Zoo,"(40.85452267684994, -73.8774290321384)",2022-11-04 03:05:54
```

Here's how you upload the CSV file:

1. Select the **Collection** and click the **Upload CSV** button (see top right side). A popup will open.
2. Click **Select File** and upload your CSV file.
3. Now, you can choose the **Separator Type** and enter the **Number of Rows to Upload**. If you leave this empty, all records will be imported.
4. Click **Upload CSV** button.
5. Once the file is uploaded, you'll see the preview of data with field name and its data type.
6. Click **Validate & Import**. If everything looks good, this will import the data and you can **Finish and Close**. If there is any issue with data type mismatch or formatting issue, you'll see a message like this:

![img\_15.png](https://docs.flutterflow.io/assets/images/img_15-7583d2accfff425dc4bf8a3f2d8ab94d.png)

Formatting issue

If your CSV file contains additional fields, you'll go through a quick *field import process* that will add the new fields with their data in your collection.

***

#### Adding Advanced Fields

You might want to add some advanced fields to store data, such as a Document Reference, DateTime, LatLng, and Multiple Items.

Let's see how to add them using Firestore Content Manager.

##### Document Reference

To store the document reference, make sure you have a Field with **Data Type** set to **Doc/Record Reference** and **Reference Type** set to your **Collection**.

The field looks like this:

![img\_16.png](https://docs.flutterflow.io/assets/images/img_16-7b20d6bc8df9015f970c3e4e2aeef656.png)

To add a document reference:

1. First, select the **Collection** from which you want to get a document reference.

2. Click on the **id** of the record to **copy** the document reference.

3. Now, select the **Collection** you would like to add a document to and then select + **Add Document.** A popup will appear. 1. Find the **Field** that accepts document reference and **paste** it
   2. Click **Add Document**.

##### Date Time

To store the DateTime, make sure you have a Field with **Data Type** set to **Timestamp**.

The field looks like this:

![img\_17.png](https://docs.flutterflow.io/assets/images/img_17-e8c831e2fba6ac377bbcf720adb80ae5.png)

To add a Date Time:

Select the **Collection** you would like to add a document to and then select + **Add Document.** A popup will appear.

1. Find the **Field** that accepts DateTime.
2. Click on it, choose the **Date,** and then click **OK**.
3. Now, select **Time** and click **OK**.
4. Click **Add Document**.

> **Note:** To modify the given Date Time, click on the Date Time Field again to open the Date Picker dialog.

##### Lat Lng

To store the Latitude and Longitude of any place, make sure you have a Field with **Data Type** set to **Lat Lng**.

The field looks like this:

![img\_18.png](https://docs.flutterflow.io/assets/images/img_18-d9aa8af378581bbeb0fb5b94368adb9e.png)

To add a Lat Lng for any place:

Select the **Collection** you would like to add a document to and then select + **Add Document.** A popup will appear.

1. Find the **Field** that accepts LatLng. There are two ways you can add LatLng. * Directly add LatLng value for any place.
   * Click on the icon to find the place and get the LatLng.

2. Click **Add Document**.

##### Multiple Items

To store the multiple items of the same data type, For example, a list of Fruit names, make sure you have a Field with **Data Type** set and **Field Type** set to **List**.

The field looks like this:

![img\_19.png](https://docs.flutterflow.io/assets/images/img_19-0e3e23776ec20189dd46edf05eca64f2.png)

To add data to List Field:

1. Select the **Collection** you would like to add a document to and then select + **Add Document.** A popup will appear.

   2. Find the **Field** that accepts a list and click on it.
   3. Click on the **+ Add Item** and enter the value.
   4. Similarly, add more items.
   5. Click **Add Document**.

##### Custom DataType (aka Firestore Map)

To add data to a custom data type field:

Select the **Collection** you would like to add a document to and then select + **Add Document**.A popup will appear.

1. Find the **Field** that accepts a custom data type.
2. Select **Tap to Set Fields (Unset)** or **Tap to Edit Fields** (based on whether you are creating or updating the document). This will open a new popup.
3. Enter the values for the fields of the custom data type.
4. Select **Save Data**.
5. Click **Add Document**.

***

#### Updating Document

To update a document:

1. Select the **pencil icon** in the row of the Document you want to update\*\*.\*\* You can also open the record by long-pressing any field in the Document (excluding the ID).
2. A popup will appear. Update the document as needed and then select **Update Document.**
3. You will now see the updated information displayed in your collection.

***

Other Tips & Tricks

* Clicking on the ID field will copy the \*reference\* to a record. This is a helpful feature when you need to reference a user while you are creating a document.
* Clicking on assets will open the asset URL.

***

#### FAQ

Getting 'Error updating Firestore Security Rules...'

To fix this issue, you must [**deploy the Firestore Rules**](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-rules#deploy).

Getting the error "Could not create an account as <firebase@flutterflow.io> to your Firebase project.

If you encounter such an issue, you just need to enable the [**Email Sign-In**](https://docs.flutterflow.io/integrations/authentication/firebase/email-login) in your Firebase project.

---

### Firestore Rules {#firestore-rules}

*Learn how to deploy Firestore rules in your FlutterFlow app to manage data access and security.*

**Source:** https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-rules

Firestore security rules are essential in safeguarding your Firebase data from potential malicious users. These rules not only enhance security but also give you control over data access within your application. With Firestore rules, you can enforce restrictions, ensuring that only authorized users can interact with specific data.

For instance, you can configure Firestore rules to permit appointment creation only for authenticated users, such as those who have signed in via Email, Google Sign-in, or other authenticated methods.

> **Tip:** If you are brand new to Firestore rules, check out this overview about [**Getting Started With Firestore Rules**](https://firebase.google.com/docs/firestore/security/get-started).

#### Creating Firestore Rules

There are two ways you can set the Firestore Rules:

1. [Using FlutterFlow Firestore setting](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-rules#1-using-flutterflow-firestore-settings)
2. [Using Firestore Database Console](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-rules#2-using-firestore-database-console)

##### 1. Using FlutterFlow Firestore Settings

To set up basic rules, you can use the *Firestore Setting* available right inside FlutterFlow.

###### Overview of Firestore Rules inside of FlutterFlow

You can control the following operations that can be performed on a document:

* **Create:** Allow users to create a new document inside the collection.
* **Read:** Allow users to read documents inside the collection.
* **Write:** Allow users to update a document of a collection.
* **Delete:** Allow users to delete a document of a collection.

![img\_3.png](https://docs.flutterflow.io/assets/images/img_3-d37f2952bba1f6a6e4703b836f2ed6de.png)

Default Rules

We provide various levels of access control that allow you to define user permissions for data access:

* **Everyone**: This grants access to all users, whether authenticated or unauthenticated, allowing them to create, read, write, and delete documents.

* **Authenticated Users**: Access is limited to authenticated users only, such as those who have signed in through Email, Google Sign-in, etc. Any user logged into the app can now create, read, write, and delete documents.

* **Tagged Users**: Allow users to read/update/delete a document if they are tagged in that document. For example, say there is a "posts" collection with a `created_by` field representing the user who created the post. Then the "Tagged User" rule can be set on the `created_by` field to only allow accessing (read/update/delete) the post if the logged-in user is the one who created it.

![img\_4.png](https://docs.flutterflow.io/assets/images/img_4-f33dd4a3f82494821ec3d9f33f715b3b.png)

* **Users Collection**: Allow users whose authentication id is the same as the id of a document. Tip: This option is only applicable to a 'users' collection.
* **No One**: No one is allowed to create/read/write/delete a document.

Note

For 'Tagged Users,' the document must contain a field that can either be a reference to the user or a string with the user id.

###### Default rules applied to new collections

When you create a new collection inside the [Firestore Content Manager](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-content-manager), below are the default rules applied to the collection:

* **Create -> Everyone**: All users can create a document.
* **Read -> Everyone**: All users can read documents.
* **Write -> No One**: No one can update a document.
* **Delete -> No One**: No one can delete a document.

![img\_5.png](https://docs.flutterflow.io/assets/images/img_5-ee72ce8c6324bb4bfe724e501a717e5e.png)

Default Rules

The default rule is suitable while you are getting started, but before the app goes live, please think about limiting access to any collections that potentially include the user's private information. To help you with that, we mark it as 'Has Private Data'. This will show you a warning to update the rule and restrict access.

For example, a newly created 'notes' collection allows everyone to read all notes by default. In reality, only the user who created it should be able to read it. But because we have marked it as '**Has Private Data**' it will show a warning like the one below, and you can modify the rules that allow only a user to read notes who created it.

![img\_6.png](https://docs.flutterflow.io/assets/images/img_6-c019fedd01873bec231fb5140062f695.png)

Firestore Warning

If you want more control over a specific collection, you can remove the FlutterFlow generated rule by checking the **Exclude** option. And then, you can set up advanced or custom security rules using the Firestore Database console.

> **Info:** To bring the rules into effect, you must deploy them. Click the **Deploy** button from here, and you will see the deployed rules at **Firebase Console > Firebase Database > Rules.**

When a user is deleted from your app, you might want to delete all records and data associated with that user as well. To do so, first set the 'Tagged Users' for the delete rule, and then check the () option.

###### Example: How to use Firestore Rules?

Let's take an example to set up the rules on a *todos* collection for the following requirements:

* Only authenticated users should be able to create a Todo item.
* All users (authenticated/unauthenticated) can see all the Todo items.
* Only a user who created the Todo item can update it.
* No one can delete a Todo item.

To set up the Firestore Rules for the above requirements:

1. Inside the **Firestore Rules** section, set the **Create** to **Authenticated Users**.
2. Set the **Read** to **Everyone**.
3. Set the **Write** to **Tagged Users**. This will open a popup named **Tag Users**. 2. Inside the dropdown, click on **Unset** and select the field that contains either user reference or user id. 5. Click **Save Changes**.
4. Set the **Delete** to **No One**.
5. Now you can [deploy](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-rules#deploy) the rules.

> **Caution:** The rules set in the above examples are for simplification purposes. You should carefully understand your requirements and set the rules accordingly.

##### 2. Using Firestore Database Console

To set up more advanced or custom rules you can use the Firebase Cloud Firestore Console.

Let's take an example to set up the rules on a *todos* collection for the following requirements:

* To create a Todo item, a user must be authenticated and verified via email or phone, and it must be a valid Todo item.
* All users (authenticated/unauthenticated) can see all the Todo items.
* Only a user who created the Todo item can update it with valid Todo details.
* Only a user who created the Todo item can delete it.

To set up the Firestore Rules for the above requirements:

1. Open the Firebase console of your project, and click on the **Firestore Database** in the left side menu.
2. Select the **Rules** tab.
3. Paste the following code and click on **Publish**.

```
rules_version = '2';

service cloud.firestore {
  match /databases/{database}/documents {
    
    // 1.
    function isSignedIn() {
      return request.auth != null;
    }
    
    // 2.
    function verified() {
      return request.auth.token.email_verified || request.auth.token.phone_number;
    }
    
    // 3.
    function isValidItem() {
      return request.resource.data.name.size() > 0 ;
    }
  
    match /todos/{document} {
      // 4.
      allow create: if isSignedIn() && verified() && isValidItem();
      // 5.
      allow read: if true;
      // 6.
      allow write: if isValidItem() && resource.data.created_by == /databases/$(database)/documents/users/$(request.auth.uid);
      // 7.
      allow delete: if resource.data.created_by == /databases/$(database)/documents/users/$(request.auth.uid);
    }

    match /users/{document} {
      allow create: if request.auth.uid == document;
      allow read: if true;
      allow write: if request.auth.uid == document;
      allow delete: if false;
    }

    match /{document=**} {
      allow read, write: if
          request.time < timestamp.date(2022, 3, 4);
    }
  }
}
```

Here’s a quick rundown of what’s going on in the code above:

1. **isSignedIn()**: This checks whether a user is authenticated.
2. **verified()**: This checks whether the user is verified via email or phone.
3. **isValidItem()**: This checks whether the Todo item is not empty.
4. **create**: Allow to create a Todo item only if a user is authenticated, verified, and created a valid Todo item.
5. **read**: Allow all users to see all Todo items.
6. **write**: Allow to update a Todo item with valid details to a user who created it.
7. **delete**: Allow to delete a Todo item to a user who created it.

#### Deploy

To deploy the Firestore Rules, simply hit the **Deploy** button.

Before you finally deploy the new rules, a popup asks you to review your changes. Here, you can check the difference between the before and after versions of the Firestone Rules and then click **Deploy Now**.

> **Caution:** * You must deploy rules every time you make a change.
* Before publishing your app, ensure you remove default Firestore rules, such as 'allow read, write: if request.time < timestamp.date(2024, 5, 31);' and exit Test mode.

![img\_7.png](https://docs.flutterflow.io/assets/images/img_7-4144c7e2f496368e69e93a72ba51232a.png)

#### Reverting to previous rules

You can go back to the previous rule state with Firebase Cloud Firestore Console:

1. Open the Firebase console of your project, and click on the **Firestore Database** in the left side menu.
2. Select the **Rules** tab.
3. Select and copy the previous rule from the left-side menu.
4. Select the current rule from the left side menu and paste the previous rule.
5. Click on **Publish**.

Learn More

Learn more about [**creating custom Firestore Rules**](https://fireship.io/snippets/firestore-rules-recipes/).

#### FAQs

Getting an error, "cloud resource location is not set," "It looks like you haven't used Cloud Firestore in this project before" or a red alert while deploying rules.

**Error-1**

![img\_8.png](https://docs.flutterflow.io/assets/images/img_8-7fe4c5fe4e410c57b16c0be27e9317e9.png)

**Error-2**

![img\_9.png](https://docs.flutterflow.io/assets/images/img_9-f9906f201f4bb7c03f4b000e3e997a37.png)

If you encounter such issues, the 'Default GCP resource location" is probably not set in your Firebase project. To fix this issue:

1. First, ensure that you have [**configured the Cloud Firestore**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#enable-firestore-for-database-access)
2. And then, head over to the second link (from the error) and set the GCP resource location.

![img\_10.png](https://docs.flutterflow.io/assets/images/img_10-acdc9f00cd36548d0ee86e3dbd5bf3d5.png)

Highlighted Link

![img\_11.png](https://docs.flutterflow.io/assets/images/img_11-c9169a52d249792339aea6654fc71d6f.png)

Set the link to Firebase Console > General Settings > Default GCP Resource Location

---

### Cloud Firestore {#cloud-firestore}

*Learn how to get started with Cloud Firestore in your FlutterFlow app to manage your app's data.*

**Source:** https://docs.flutterflow.io/integrations/database/cloud-firestore/getting-started

[Firestore Database](https://firebase.google.com/docs/firestore) is a product from Google's [Firebase](https://firebase.google.com/). It's a flexible, scalable, NoSQL cloud database. It allows you to store your app data and uses real-time listeners to keep the data in sync.

Let's understand the Firestore database (Cloud Firestore, a NoSQL Database) in more detail.

#### What is a NoSQL Database

The NoSQL database is a schema-less database. That means the data is NOT stored in the table format. You actually don't have any restrictions on how you store your data. The Firestore database uses the collection-document model to store the data.

Key terms to remember:

* **Collection:** A collection is simply a set of 'documents.'
* **Document:** A document is a record that contains the 'fields.'
* **Fields:** The key-value pairs inside the document are called 'fields.' e.g., name, place, age, etc.

To better understand, see the figure below:

![img.png](https://docs.flutterflow.io/assets/images/img-f99f4388b62b57262c21368ac5281a0c.png)

Collection document model

Every user's information is kept in a unique document. Multiple of these documents come together to form a collection. The beauty of this system is that not all documents within a collection need to have identical fields. So, if you decide to add a new field (e.g., DOB, image) to a new document, there's no need to go back and add it to older ones.

***

#### Structuring the Database

To see how to structure the database, consider an example that allows users to comment on a post.

With FlutterFlow, you can structure the database in the following ways:

* [Top-level collections](https://docs.flutterflow.io/integrations/database/cloud-firestore/getting-started#top-level-collections)
* [Subcollections within documents](https://docs.flutterflow.io/integrations/database/cloud-firestore/getting-started#subcollections-within-documents)

##### Top-level collections

In Top-level collections, multiple collections are created at the root level of your database.

For example, you create collections such as 'comments' and 'posts' at the root level. Comments for all the posts are stored in a single top-level collection. To know which comment belongs to which post, you include additional reference fields that distinctly identify each post within this structure.

![img\_1.png](https://docs.flutterflow.io/assets/images/img_1-7304390dcb8f4f7d5971a1ed1d6c13f1.png)

Top-level collection

Pro Tip

Use top-level collections when you often search or filter within one collection without depending on another. For instance, if you want to see all comments, regardless of their related post (i.e., showing comments with the most likes).

##### Subcollections within documents

Collections are created inside the document. Such a collection is called subcollection.

For example, you create the top-level collection, such as posts, and then create a 'comments' collection (as a subcollection) inside the 'posts' collection. The advantage? You don't need extra tags or reference fields to know which post a comment belongs to; it's already grouped right there.

![img\_2.png](https://docs.flutterflow.io/assets/images/img_2-5a73a7fd54b5b0550b9fe0617341145c.png)

Subcollections

Pro Tip

Subcollection is best when you have several queries or filters or search on a collection that is based on the other collection. For example, loading or searching the comments of a specific post (i.e., show all comments of a specific post that have more likes.)

> **Info:** You can secure the data using the [**Firestore Rules**](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-rules).

***

Learn more

[**MongoDB**](https://www.mongodb.com/), [**Cassandra**](https://cassandra.apache.org/_/index.html), and [**ElasticSearch**](https://www.elastic.co/) are the other No-SQL database solutions that exist in the market.

If you are a visual learner, you can check out the video:

#### Manage Databases

You can also create multiple Firestore databases within a single Firebase project. This is especially useful for enterprise use cases, for example, when managing region-based databases or supporting multiple clients with isolated data stores.

Additionally, you can use multiple databases to simulate different environments such as development, staging, and production. **However, note that** this setup is not directly related to the [Development Environments](https://docs.flutterflow.io/testing/dev-environments) in FlutterFlow, which operates independently of Firebase's multi-database configuration. This means that you’ll need to manually switch Firestore Database ID when switching Development Environments.

To create a new database, go to the **Firebase Console > Firestore Database** section. Click the button next to the default database, i.e, **Add database**. Choose a region and configure your security rules. Once the new database is created, you can switch between databases using the dropdown.

Next, copy the new **Database ID** and navigate to **FlutterFlow > Settings and Integrations > Firebase > Advanced Settings**. Paste the ID into the **Firestore Database ID** input field. Finally, regenerate the config file. Your app will now use the newly created database.

---

### Refresh Database Request [Action] {#refresh-database-request-action}

*Learn how to use the Refresh DB Request action in your FlutterFlow app to refresh your database content.*

**Source:** https://docs.flutterflow.io/integrations/database/refresh-db-request

Using this action, you can see the updated values of an item inside the scrollable widgets such as ListView, GridView, StaggeredView, Row, and Column.

Prerequisites

If you are querying data via a Backend Query, ensure you have enabled the **Single Time Query** in the Backend Query properties (Query Collection or API Call) on any scrollable widget.

Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to define the action.

2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action flow Editor** in a new popup window.

3. Click on the **+ Add Action**.

4. On the right side, search and select the **Refresh Database Request** (under *Backend/Database*) action.

   1. From the dropdown, select the widget (e.g., ListView, GridView, etc.) on which you have added the backend query.

   2. By default, the **Wait for Result** option is enabled. That means the subsequent action(s) will only trigger after this action is finished. If any subsequent action is not dependent on this action or you want to trigger them regardless of the completion of this action, you can turn off this option.

   3. When the **Wait for Result** is enabled, you can specify the **Min Wait Time** and **Max Wait Time** in ms (e.g., 1000ms = 1 second).

      * **Min Wait Time**: Time before triggering the following action(s) or refreshing the UI.

      * **Max Wait Time**: Time after which the subsequent action(s) will trigger regardless of the completion of this action.

5. Click **Close**.

---

### SQLite {#sqlite}

*Learn how to quickly get started with SQLite in your FlutterFlow app for local data storage.*

**Source:** https://docs.flutterflow.io/integrations/database/sqlite

SQLite is a compact, efficient database management system. Unlike conventional databases that require a server, SQLite is serverless and embeds directly into applications.

It's perfect for mobile apps where resources are limited, and a full-fledged database server is impractical. For example, it's ideal for a mobile app that needs to store data locally, such as a personal finance tracker or a health record app, especially when offline functionality is required.

> **Caution:** Currently, we don't support SQLite on Web-based apps.

Let's understand how you can utilize SQLite in your app with an example. An app where users can add, update, and delete Notes. Here's how it looks when completed:

Here are the steps to build such an example:

1. [Enable SQLite](https://docs.flutterflow.io/integrations/database/sqlite#1-enable-sqlite)
2. [Database configuration](https://docs.flutterflow.io/integrations/database/sqlite#2-database-configuration)
3. [Add SQL queries](https://docs.flutterflow.io/integrations/database/sqlite#3-add-sql-queries)
4. [Display all notes](https://docs.flutterflow.io/integrations/database/sqlite#4-display-all-notes)
5. [Add note](https://docs.flutterflow.io/integrations/database/sqlite#5-add-note)
6. [Update note](https://docs.flutterflow.io/integrations/database/sqlite#6-update-note)
7. [Delete note](https://docs.flutterflow.io/integrations/database/sqlite#7-delete-note)

#### 1. Enable SQLite

To enable SQLite in FlutterFlow, navigate to Settings and Integrations > Integrations > SQLite > switch on the **Enable SQLite** toggle.

![img.png](https://docs.flutterflow.io/assets/images/img-69f9c51c511fba175c15e7c8ca5c2e0d.png)

#### 2. Database configuration

In the database configuration step, you'll need to upload your SQLite database file and assign a name to it. This process is crucial for initializing the database when your app launches.

If you don't yet have an SQLite database, you can easily create one using tools like [sqlitebrowser](https://sqlitebrowser.org/). Simply download [sqlitebrowser](https://sqlitebrowser.org/dl/), create a new database, set up your tables, and optionally add some data. After preparing your database, upload the file to FlutterFlow to integrate it with your app.

For this example, we'll create a "Notes" table with `ID`, `Title`, `Details`, `DueDate`, and `IsCompleted` as columns.

> **Warning:** It is advisable to avoid using any SQL reserved keywords such as `type` and `data` as column names to prevent potential build errors or unexpected behavior. SQLite reserves certain words for its SQL syntax, and using these as identifiers without proper handling may cause issues. For a comprehensive list of reserved keywords, refer to the [**SQL reserved words**](https://en.wikipedia.org/wiki/List_of_SQL_reserved_words).

Here's how you can create and configure the database:

Important to note

SQLite does not have dedicated date-time or boolean data types. For storing date-time values like `DueDate`, we use the integer data type and represent the date-time as a [**UNIX timestamp**](https://www.unixtimestamp.com/). Similarly, for boolean values, such as checking if a note is completed, SQLite uses integers where `0` represents `false` (or not completed) and `1` represents `true` (or completed).

#### 3. Add SQL queries

SQL queries are statements used to interact with a database. We allow you to add queries in two different sections:

###### 1. Read Queries

This includes statements that retrieve data from the database but do not modify anything. Some common examples:

* `SELECT * FROM customers;` - retrieve all rows and columns.
* `SELECT name, city FROM customers;` - retrieve specific columns.
* `SELECT * FROM customers WHERE city = 'New York';` - retrieve rows that match a condition.

###### 2. Update Queries

This includes statements that modify the database, such as:

* `INSERT INTO customers (name, address, city) VALUES ('John', '555 Main St', 'New York')` - add new rows.
* `UPDATE customers SET address = '123 Main Street' WHERE name = 'John'` - update existing rows.
* `DELETE FROM customers WHERE city = 'Chicago'` - delete rows that match a condition.

In general, to add any query, you need to provide a name, the query statement, and variables that are used to pass values from your app to queries. For *Read Queries*, you have to define the output columns as well. This will help you display the row data in the UI by selecting the column name.

> **Tip:** * To use variables, simply use the syntax `${variableName}`. For example: `SELECT \* FROM Notes WHERE id = ${noteId}`
* When passing string or text data in queries, enclose variables in single quotes, like `${title}`, to signify them as strings. ![img\_1.png](https://docs.flutterflow.io/assets/images/img_1-f3fb3ba48d21061a2b7784fd6091e621.png)

Below are the queries that we'll require for this example:

###### 1. GetAllNotes

This will retrieve all notes from the database.

```
Select * from Notes
```

###### 2. AddNote

This will add a new note to the database.

```
INSERT INTO Notes (Title, Details, DueDate, IsCompleted) VALUES ('${title}', '${details}', ${dueDate}, 0);
```

###### 3. UpdateNote

This will update the existing note based on the note ID.

```
UPDATE Notes
SET 
    Title = '${title}',
    Details = '${details}',
    DueDate = ${dueDate},
    IsCompleted = ${isCompleted}
WHERE ID = ${id};
```

###### 4. DeleteNote

This will delete the note based on the note ID.

```
DELETE FROM Notes WHERE ID = ${id};
```

#### 4. Display all notes

To show a list of notes, you can use the **ListView** > **Container** widgets to design a page that looks like the following:

![img\_2.png](https://docs.flutterflow.io/assets/images/img_2-d8caf311fc98a1220bc08f26b9d65fa4.png)

Now, on the ListView widget, add a SQLite backend query as per the following instructions:

##### Add a SQLite Query:

Go to your project page and follow the steps below to define an SQLite query:

* Select the widget (or page) on which to apply the query.
* Select **Backend Query** from the Properties Panel (the right menu).
* Click **Add Query** and set the Query Type to **SQLite Query**.
* Select the **Query Name**. (Only Read Queries will be displayed here.) and click **Confirm**.

Once you have the SQLite query defined, you can use the data retrieved from the query to display on widgets present inside. Follow the steps below:

* Select the widget (e.g., Text) on which you want to display the data.

* From the Properties Panel, open the Set from Variable menu > select \[your query name] Row > select the column data that you want display here and click **Confirm**.

> **Info:** In our example, the due date is stored as a Unix timestamp, which isn't user-friendly for display purposes. Therefore, we've included a custom function in the [example project](https://app.flutterflow.io/project/note-taking-app-zto2ua) that converts this timestamp into a human-readable date format.

#### 5. Add note

You can add a new note in the database using the SQLite query Action with the type set to **Update Query** and Query Name to [AddNote](https://docs.flutterflow.io/integrations/database/sqlite#2-addnote).

Here's how you do it:

#### 6. Update note

For updating note values, like marking a note as completed or modifying other fields, utilize the SQLite Query Action and set the type to **Update Query**. Here, set the Query Name to [Update Note](https://docs.flutterflow.io/integrations/database/sqlite#3-updatenote).

Here's how you do it:

> **Info:** * In this example, we are updating the note on a bottom sheet component. To provide a better user experience, we initially display the current values of the note, ensuring that users have a clear idea of what they are going to edit. To display the note values in bottom sheet, we [pass](https://docs.flutterflow.io/concepts/navigation/passing-data) the current note with **Type** set to **SQLite Row**.

![img\_3.png](https://docs.flutterflow.io/assets/images/img_3-bfc44730b7360439ac421a992f0d2c12.png)

* When updating a date value, we also verify if the date has been modified. If there's no change, we simply pass back the same value we received.

#### 7. Delete note

You can delete an existing note from the database using the [SQLite query action](https://docs.flutterflow.io/resources/backend-query/sqlite-query) with the type set to *Update Query* and Query Name to **Delete Note**.

Pro Tip

To refresh the page, simply add an [**Update App State Action**](https://docs.flutterflow.io/resources/data-representation/app-state) Action with the Update Type set to 'Rebuild Current Page'.

Here's how you do it:

Example project

Check out the complete [**example project**](https://app.flutterflow.io/project/note-taking-app-zto2ua) for reference.

#### FAQs

Can SQLite handle complex data structures compared to App State Variables?

Yes, SQLite can handle complex data structures much more effectively. It allows for structured data storage, complex queries, sorting, and filtering, which are challenging to implement with app state variables.

Is SQLite a good choice for apps that require offline functionality?

Absolutely. SQLite stores data locally, making it an excellent choice for apps that need to operate offline. Users can access and manipulate data without needing an internet connection.

Will using SQLite affect my app's performance compared to using App State Variables?

SQLite is designed to be lightweight and efficient, so it generally won't negatively impact your app's performance. In fact, for larger data sets, it's more efficient than storing data in app state variables.

How does SQLite ensure data security and integrity?

SQLite maintains data integrity and supports transactional operations. This means it ensures the database state remains consistent even in cases of unexpected interruptions, like app crashes or power failures.

---

### Supabase Database Actions {#supabase-database-actions}

*Learn about Supabase Database actions in your FlutterFlow app, including how to perform various database operations.*

**Source:** https://docs.flutterflow.io/integrations/database/supabase/database-actions

The Supabase Database Actions allow you to **Insert, Update**, or **Delete a Row** from a Supabase table.

Note that beyond actions, you can also setup [**Backend Queries**](https://docs.flutterflow.io/resources/backend-query) for Supabase. This includes realtime streaming queries.

Prerequisites

Before getting started with this section, ensure you have,

1. Completed all steps in the [**Supabase setup**](https://docs.flutterflow.io/integrations/supabase/setup)
2. Ensure you have a table created for adding, updating, and deleting data.

#### Types of Supabase Database Actions

Following are the types of actions you can perform on a Supabase table.

* [**Insert Row**](https://docs.flutterflow.io/integrations/database/supabase/database-actions#insert-row-action): Adds a new row in a table.
* [**Update Row**](https://docs.flutterflow.io/integrations/database/supabase/database-actions#update-row-action)**:** Updates a row with the specified values.
* [**Delete Row**](https://docs.flutterflow.io/integrations/database/supabase/database-actions#delete-row-action)**:** Deletes a row from a table.
* [**Query Rows**](https://docs.flutterflow.io/integrations/database/supabase/database-actions#query-rows-action): Retrieves rows from a table based on specific criteria or conditions.

##### Insert Row \[Action]

1. Select the **Widget** (e.g., Button) on which you want to define the action.

2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.

   1. Click on **+ Add Action**.

   2. On the right side, search and select the **Supabase** > **Insert Row** action.

   3. Set the **Table** to your table name (e.g., assignments).

   4. Under the **Set Fields** section, click on the **+ Add Field** button.

   5. Click on the Field name.

      1. Scroll down to find the **Value Source** dropdown and change it to **From Variable**.
      2. Click on **UNSET** and select **Widget State > Name** of the TextField.

   6. Similarly, add the field for the other UI elements.

Pro Tip

While adding this action, you can leave the **id** (if marked as *Primary*) and **created\_at** (if default value is `now()`) fields. Supabase will automatically add values for these fields.

##### Update Row \[Action]

1. Select the **Widget** (e.g., Button) on which you want to define the action.

2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.

   1. Click on **+ Add Action**.

   2. On the right side, search and select the **Supabase** > **Update Row** action.

   3. Set the **Table** to your table name (e.g., assignments).

   4. Optional: If you want to get the rows after the update is finished, enable the **Return Matching Rows** option.

   5. Now, you must set the row you want to update. Usually, this is done by finding a row in a table that matches the current row ID. To do so, click **+ Add Filter** button inside the **Matching Rows** section.

      1. Set the **Field Name** to the field that contains the IDs. Typically, this is the **id** column.
      2. Set the **Relation** to **Equal To** because you want to find a row with the exact id.
      3. Into the **Value Source**, you can select the **From Variable** and provide the id of the row for which you just updated values in the UI.

   6. Under the **Set Fields** section, click on the **+ Add Field** button.

   7. Click on the Field Name.

      1. Scroll down to find the **Value Source** dropdown and change it to **From Variable**.
      2. Click on **UNSET** and select **Widget State > Name** of the TextField.

   8. Similarly, add the field for the other UI elements.

How to & Tips

If you have a flow like this, *HomePage* -> *AssignmentDetailsPage* -> *UpdateAssignmentPage*, you can enable the **Replace Route** option (see point no. 5 [here](https://docs.flutterflow.io/concepts/navigation/page-navigation#navigate-to-action)) when you navigate from *AssignmentDetailsPage* to *UpdateAssignmentPage*. And then chain the [Navigate Back](https://docs.flutterflow.io/concepts/navigation/page-navigation#navigate-back-action) action after the update action. This will directly open the *HomePage* after the row is updated.

##### Delete Row \[Action]

Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to define the action.

2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.

   1. Click on **+ Add Action**.

   2. On the right side, search and select the **Supabase** -> **Delete Row** action.

   3. Set the **Table** to your table name (e.g., assignments).

   4. Optional: If you want to know which rows were deleted from a table, enable the **Return Matching Rows** option.

   5. Now, you must set the row you want to delete. Usually, this is done by finding a row in a table that matches the current row ID. To do so, click **+ Add Filter** button inside the **Matching Rows** section.

      1. Set the **Field Name** to the field that contains the IDs. Typically, this is the **id** column.
      2. Set the **Relation** to **Equal To** because you want to find a row with the exact id.
      3. Into the **Value Source**, you can select the **From Variable** and provide the id of the row you want to delete.

> **Tip:** You can chain the [**Refresh Database Request**](https://docs.flutterflow.io/integrations/database/refresh-db-request) action after this action to remove the deleted items from the list.

##### Query Rows \[Action]

There are certain scenarios where you may want to query a Supabase table manually. For example, you might want to only fetch data in response to a specific user action, such as clicking on a button.

Additionally, if your app fetches different data under different conditions, you might find it more convenient to manually call queries. For example, you might fetch different tasks for admin and team members.

To manually query a Supabase table, follow the steps below to define this action to any widget:

1. Select the **Widget** (e.g., Button) on which you want to define the action.

2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.

3. Click on **+ Add Action**.

4. On the right side, search and select the **Supabase** > **Query Rows** action.

5. Select the **Table** you want to query.

6. You can also [Filter](https://docs.flutterflow.io/integrations/database/supabase/database-actions#filtering-table-data) and [Order](https://docs.flutterflow.io/integrations/database/supabase/database-actions#ordering-table-data) the query results.

7. Provide the **Action Output Variable Name**. This will be used to store the query result.

8) Now, you can use the **Action Output Variable Name** provided in the previous step to generate children from a variable on **ListView**.
9) Finally, you can display data in a **Text** widget. To do so, select the **Text widget > Properties Panel > Text > Set from Variable menu > ***\[children\_from\_variable\_name]*** item > Get Row Field > select the row field** you want to display.

###### Filtering table data

Sometimes you might want to filter a list based on a condition. For example, showing only completed assignments. You can do so by adding the Filter while you query a Supabase table.

Let's see how to filter the Supabase table to display only desired items:

* In your **Action properties** of Query Rows action, scroll down and click on the **+ Add Filter** button at the bottom.

* Find the **Field Name**, click on the Unset, and select a column on which you would like to apply the filter.

* Find the **Relation** dropdown, click on the Unset, and choose the relation amongst the list.

* Find the **Value** property and set it to an appropriate value and click Confirm.

> **Tip:** You could choose a filter relation based on your requirements. For example:

* **Equal To**: To show only completed assignments, set the **Field Name** to the column that holds the completion status (e.g., **is\_done**), set the **Relation** to **Equal To**, and set the **Value** to **True**.

* **Greater Than**: To show only users older than 30, set the **Field Name** to the **age** column, set the **Relation** to **Greater Than**, and set the **Value** to 30.

* **Like**: For filtering addresses with zip codes starting with '35,' set the **Field Name** to the **zip\_code** column, set the **Relation** to **LIKE**, and set the **Value** to **35%**. In the value field, you use the following wildcards to perform flexible pattern matching to filter your data effectively. * **Percent (`%`) Wildcard**: Represents zero, one, or multiple characters. * Example: `'A%'` matches any string starting with `'A'` (e.g., `'Apple'`, `'Apex'`).
    * Example: `'%A%'` matches any string containing `'A'` (e.g., `'Canada'`, `'Australia'`).

  * **Underscore (`_`) Wildcard**: Represents a single character. * Example: `'A_'` matches any two-character string starting with `'A'` (e.g., `'An'`, `'At'`).
    * Example: `'A__'` matches any three-character string starting with `'A'` (e.g., `'Ant'`, `'Art'`).

> **Info:** You can combine multiple filters using **AND** or **OR** operators to create more advanced filtering logic. This enables you to refine your data query to match specific conditions.

###### Ordering table data

You might want to show a list from the Supabase table in a specific order. For example, showing assignments in order of the due date.

To specify the order:

* In your **Action properties** of Query Rows action, scroll down and click on the **+ Add Order** button at the bottom.
* Set the **Table Field Name** to the column you would like to choose for ordering.
* Find **Order** dropdown, click on the Unset and choose the order either **Increasing** or **Decreasing** and click **Confirm**.

> **Tip:** You could choose the order based on your requirements. For example, to show assignments in order of due date, set Table Field Name to due\_date and Order to Increasing.

> **Info:** Additional Note: Currently, you can only add "and" conditions to Supabase query filters. If you want to add an "or" filter like "status == 5 or status == 8", you can consider logic to apply "status in (5,8)" or any other logic. Fully customizable using API calls or custom actions.

#### Trigger Action On Data Change

Sometimes, you may want to trigger an action whenever data changes in a Supabase table. For instance, in an ecommerce app, you might want to notify users on the orders page when the status of their order is updated.

To respond to data changes in a Supabase table:

1. Ensure you have added a **Supabase Query** to a widget (e.g., a ListView) with **Single Time Query** disabled to enable real-time updates.
2. On the widget with the **Supabase Query**, open the **Action Flow Editor** and set **On Data Change** as the [Action Trigger](https://docs.flutterflow.io/resources/functions/action-triggers). This ensures that any actions you add will be triggered whenever the data is updated, added, or deleted.
3. You can now [add any action](https://docs.flutterflow.io/resources/functions/action-flow-editor#adding-an-action-example) you want to perform, such as showing a notification, refreshing the UI, or fetching related data.

> **Info:** If you are using this trigger on a ListView, make sure to **disable** the **Infinite Scroll**.

#### Offline Support for Supabase Apps

If you need offline capabilities in your Supabase-powered app, consider using the **[PowerSync Library](https://marketplace.flutterflow.io/item/dm1cuOwYzDv6yQL2QOFb)** built by the **[PowerSync](https://www.powersync.com/)** team. It's designed specifically to enable seamless offline-first experiences by syncing your Supabase data locally and keeping it up to date when the device reconnects.

---

### Import from FF Designer {#import-from-ff-designer}

*Learn how to export screens from FF Designer and import them into FlutterFlow.*

**Source:** https://docs.flutterflow.io/integrations/designer/import-from-ff-designer

You can quickly bring your generated designs from [FF Designer](https://designer.flutterflow.io/) into FlutterFlow to continue building with real widgets, actions, and logic. This allows you to transform visual storyboards into fully functional app screens without recreating layouts manually.

###### Step 1: Export from FF Designer

1. Open the top-left **FF Designer** menu.
2. Choose **Export to FlutterFlow**.
3. This copies the selected frames (or entire storyboard) to your clipboard.

> **Tip:** You can also use the shortcut **Cmd + C** to copy frames directly for faster export.

###### Step 2: Import into FlutterFlow

1. Open your FlutterFlow project.
2. Navigate to the page where you want to paste the design.
3. Select any widget from the widget tree.
4. Paste the copied design.

FlutterFlow will recreate the layout structure using real widgets, preserving hierarchy, spacing, and styling.

To import a single component, copy the component’s root element and paste it into your widget tree.

---

### Firebase Storage Library {#firebase-storage-library}

*The Firebase Storage Library provides access to the files in Cloud Storage through the Firebase SDK beyond what FlutterFlow's built-in support provides.*

**Source:** https://docs.flutterflow.io/integrations/firebase-storage/storage-library

The [Firebase Storage Library](https://marketplace.flutterflow.io/item/Ec3NWw8sxqJ1tbriOIEE) provides access to the files in Cloud Storage through the Firebase SDK beyond what [FlutterFlow's built-in support](https://docs.flutterflow.io/concepts/file-handling) provides.

#### Instructions

To start using this library:

1. [Import the library](https://docs.flutterflow.io/resources/projects/libraries#importing-a-library) into your existing FlutterFlow project.
2. [Connect your FlutterFlow project to Firebase](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) (if you haven't done so already). The library will default to using the default bucket of your associated Firebase project. You can override this behavior by passing an explicit bucket URL to any of the actions.
3. [Use the Custom Actions](https://docs.flutterflow.io/concepts/custom-code/custom-actions#using-a-custom-action) and Custom Functions in your Action Flows.

##### Custom actions

* `uploadFileToBucket` - Upload a file to any path in any bucket that you have write access to.

  * **Parameters:**

    * The `bucketName` (`String?`) to upload the file to. If you leave this empty, it uses the default bucket of the associated Firebase project.
    * The `fullPath` (`String?`) where the file will be written to inside the bucket. If this is specified, the `prefix` parameter is ignored.
    * The `uploadedFile` (`FFUploadedFile`) that is to be uploaded to Cloud Storage. This is the action output of a previous `Store media for upload` action.
    * The `prefix` (folder/directory) (`String?`) where the file will be uploaded to. If `fullPath` is not specified, the action uses this parameter and the `name` of the `uploadedFile` to determine the full path where it writes the file.

  * **Action result:**
    * If successful, the action result is a `fileObject` containing the full path of the uploaded file.

* `listAllFilesInBucket` - List all files in any bucket that you have read access to.

  * **Parameters:**

    * The `bucketName` (`String?`) to list the files from. If you leave this empty, it uses the default bucket of the associated Firebase project.
    * The `listType` (`StorageListType?`) of the items to list (files, directories, both). If left empty, the action will list both files and prefixes (folders/directories).
    * The `prefix` (`String?`) is the `/` separated path from which to list files. If left empty, the action will list the items in the root of the storage bucket.

  * **Action result:**
    * If successful, the action results in a `List` of `fileObject` elements.

* `downloadFile` - Download the data for a file that you have read access to. This downloads the actual data into your application code. If you instead want a public URL to the data, use `getDownloadUrl` instead.

  * **Parameters:**

    * The `bucketName` (`String?`) to download the file from. If you leave this empty, it uses the default bucket of the associated Firebase project.
    * The `fullPath` (`String`) of the file whose data will be read from the bucket.

  * **Action result:**
    * If successful, the action result is an `FFUploadedFile` with the data of the file that was read from the bucket.

* `getDownloadUrl` - Get the download URL for a file in a bucket that you have read access to. This URL then provides public, read-only access to the file

  * **Parameters:**

    * The `bucketName` (`String?`) that contains the file. If you leave this empty, it uses the default bucket of the associated Firebase project.
    * The `fullPath` (`String`) of the file for which to get the download URL.

  * **Action result:**
    * If successful, the action result is a HTTP URL that allows public access to the file.

* `getMetadataForFile` - Get the metadata for a file in any bucket that you have read access to

  * **Parameters:**

    * The `bucketName` (`String?`) that contains the file. If you leave this empty, it uses the default bucket of the associated Firebase project.
    * The `fullPath` (`String`) of the file for which to get the download URL.

  * A**ction result:**
    * If successful, the action result is a `FullMetadata` with all the metadata and custom metadata of the file.

* `updateMetadataForFile` - Update the metadata for a file in any bucket that you have write access to

  * **Parameters:**

    * The `bucketName` (`String?`) that contains the file. If you leave this empty, it uses the default bucket of the associated Firebase project.
    * The `fullPath` (`String`) of the file for which to get the download URL.
    * The `metadata` (`SettableMetadata`) to write to the Cloud Storage bucket for the file. If any value is left out or empty in the metadata, it is left unmodified in Cloud Storage.

  * **Action result:**
    * If successful, the action result is a `FullMetadata` with all the metadata and custom metadata of the file after the update.

* `getPathFromUrl` - Get the path for a file based on its (https\:// or gs\://) URL. This is a synchronous call, as it doesn't require any call to the server.

  * **Parameters**
    * The `Url` to parse.
  * **Action result:**
    * The action result is a `fileObject` derived from the URL.

* `deleteFileFromBucket` - Deletes a file from any bucket you have write access to.

  * **Parameters:**

    * The `bucketName` (`String?`) that contains the file. If you leave this empty, it uses the default bucket of the associated Firebase project.
    * The `fullPath` (`String`) of the file to delete from the bucket.

  * **Action result:**
    * If the action succeeds the file has been deleted. There is no additional information.

##### Enums

* `StorageListType` is an enumeration of the types of items that the `listAllFilesInBucket` action can return. Values: * `files`: List only the files in the specified path.
  * `prefixes`: List only the prefixes in the specified path. You might more commonly refer to these as folders or directories, but since Cloud Storage doesn't actually have support for folders/directories, it uses `/` characters in the file names to emulate those and calls them prefixes.
  * `filesAndPrefixes`: List both files and prefixes in the specified path.

##### Data Types

* `fileObject` - the metadata for a file or prefix (folder/directory) in Cloud Storage. It has the following fields:

  * `fullPath` (`String`) - The full path of the file/prefix inside the storage bucket. The value does not start with a leading `/`.
  * `isPrefix` (`Boolean`) - Indicates whether the object is a file (`false`) or prefix (folder/directory) (`true`).

* `FullMetadata` - the full metadata of an item in a storage bucket as returned by `getMetadataForFile`, modelled after the [`FullMetadata` class in the Firebase SDK for Cloud Storage](https://pub.dev/documentation/firebase_storage/latest/firebase_storage/FullMetadata-class.html).

* `SettableMetadata` - the settable metadata of an item in a storage bucket, as passed to a call to `updateMetadataForFile`, modelled after the [`SettableMetadata` class in the Firebase SDK for Cloud Storage](https://pub.dev/documentation/firebase_storage/latest/firebase_storage/SettableMetadata-class.html).

* `KeyValuePair` - A `String`/`String` key/value pair as used for the `customMetadata` in the `FullMetadata` and `SettableMetadata` data types.

---

### Storage Rules {#storage-rules}

*Learn how to deploy storage rules in your FlutterFlow app to manage and secure your Firebase storage.*

**Source:** https://docs.flutterflow.io/integrations/firebase-storage/storage-rules

Like [Firestore security rules](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-rules), Firebase Storage security rules control who can access files uploaded by your users in your application.

For example, by setting the storage rules, you can allow only authenticated users (e.g., via Email, Google Sign-in, etc.) to upload or send images.

For beginners

If you are new to storage rules, you may want to check out this overview about [**Getting Started With Storage Rules**](https://firebase.google.com/docs/storage/security).

#### Deploying storage rules

To deploy the storage rules:

1. First, make sure Firebase Storage is enabled or configured in your project by visiting the [Firebase console](https://console.firebase.google.com/u/0/) and viewing the **Storage** tab.

2. Return to FlutterFlow, navigate to **Settings & Integrations > Project Setup > Firebase**.

3. Scroll down to the **Firebase Storage** section.

4. To set the storage rules outside of the FlutterFlow (i.e., from the Firebase Console), enable the **Manage Outside of FlutterFlow**.

5. To only allow accessing the images, videos, files, etc., to the users who uploaded it, enable **Make Users Uploads Private**.

6. Click the **Deploy** button.

7. A pop-up will open. Click **Yes** to continue and click **Deploy Now**.

Learn more

Learn more about Firebase Storage Rules [here](https://firebase.google.com/docs/storage/security).

---

### App Check {#app-check}

*Learn how to integrate Firebase App Check in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/firebase/app-check

[Firebase App Check](https://firebase.google.com/docs/app-check) is a new security feature for protecting the backend services of apps. It blocks traffic that comes from sources other than the registered app, ensuring that usage costs are not incurred for illegitimate usage.

App Check works by using attestation services, which already exist for iOS, Android, and the web. The feature can protect three different types of backends, including Firebase backends like Cloud Firestore, Google API services like Cloud Run, and API endpoints of your own server.

#### **Adding Firebase App Check**

To add *Firebase App Check* to your app:

1. Navigate to the [Firebase Console](https://console.firebase.google.com/u/0/) > Build > App Check page.

2. If this is the first time, click the **Get started** button.

   ![Get started with App Check](https://docs.flutterflow.io/assets/images/get-started-e563b36a10af3562962ca8f78d842f5f.avif)

3. Now, you'll see the list of apps you have added to this Firebase project. To register attestation service(s), select the project, click **Register,** and then select attestation service.

   1. For Android, you can select [Play Integrity](https://developer.android.com/google/play/integrity?authuser=1) and then follow step number 2 and 3 from [here](https://firebase.google.com/docs/app-check/android/play-integrity-provider?authuser=2#project-setup).
   2. For iOS, you can choose from [Device Check](https://developer.apple.com/documentation/devicecheck) or [App Attest](https://developer.apple.com/documentation/devicecheck/establishing_your_app_s_integrity) and then follow step number 2 and 3 from [here](https://firebase.google.com/docs/app-check/ios/devicecheck-provider?authuser=2).
   3. For the Web, select [reCAPTCHA v3](https://developers.google.com/recaptcha) or [reCAPTCHA Enterprise](https://cloud.google.com/recaptcha-enterprise) and then follow steps 2 and 3 from [here](https://firebase.google.com/docs/app-check/web/recaptcha-enterprise-provider?authuser=2#project-setup). **Note**: To run the app in Run/Test mode, you must register the **Web** version of the app as well.

* Android
* iOS
* Web

4. Ensure that enabling Firebase App Check [won't disrupt your existing legitimate users](https://firebase.google.com/docs/app-check/monitor-metrics?authuser=2).
5. Now, you can select the service you want to secure. Switch to the **APIs** tab, select the service, and click **Enforce** button. A popup may open, telling you that once enabled, it will deny all requests that do not have *App Check* token. Click **Enforce** again if you are ok. **Note** that it might take up to 15 minutes to start the enforcement.

6) Navigate back to FlutterFlow and open **Settings and Integrations > Project Setup > Firebase >** scroll down and expand **App Check** section **>** switch on **Enable App Check** toggle.

7) You can fill out the optional details such as **reCAPTCHA Site Key** (you should have it while performing step 3.3) and [**Run/Test Mode Debug Token**](https://firebase.google.com/docs/app-check/flutter/debug-provider). To get the debug token, follow the steps below: 1. Navigate to the [Firebase Console](https://console.firebase.google.com/u/0/) > Build > App Check > Apps.
   2. Open the app for which you want to generate the debug token.
   3. Click three dots icon (i.e., overflow menu icon) and select **Manage debug token**.
   4. Click **Add debug token**.
   5. Give it a **Name** and click **Generate token**.
   6. Copy the generated token and paste it in FlutterFlow's designated field.
   7. Click **Save**.

5. You might want to see if it works on a real device or an emulator. To run on a real device, you can set the **Android Provider** to **Play Integrity** and to run on an emulator, set it to **Debug,** and then try checking it by downloading the APK. 1. If it doesn't work for *Play Integrity*, ensure you have enabled the Play Integrity API. See how to do it in step 2 [here](https://firebase.google.com/docs/app-check/android/play-integrity-provider?authuser=1\&hl=en#project-setup).
   2. If it doesn't work for *Debug*, you can try [downloading the code](https://docs.flutterflow.io/flutterflow-cli/exporting), following the instructions [here](https://firebase.google.com/docs/app-check/flutter/debug-provider#android), and running it locally.

> **Tip:** To add the App Check on the app with the non-Firebase (i.e., your self-hosted) backend, follow the instructions [**here**](https://firebase.google.com/docs/app-check/flutter/custom-resource).

---

### Connect to Firebase {#connect-to-firebase}

*Learn how to integrate Firebase with your FlutterFlow app to add user authentication, cloud storage, real-time databases, and more.*

**Source:** https://docs.flutterflow.io/integrations/firebase/connect-to-firebase

Firebase integration in FlutterFlow provides an effortless way to enhance your apps with powerful features such as user authentication, cloud storage, real-time databases, and more. This setup guide will walk you through integrating Firebase with FlutterFlow, empowering you to easily create feature-rich, scalable applications.

#### Create a new Firebase project from FlutterFlow

FlutterFlow allows you to automatically create a Firebase project directly from the builder using a quick three-step process.

###### Step 1: Set Up Your Project

Go to **Settings & Integrations > Project Setup > Firebase** in FlutterFlow to get started.

###### Step 2: Select Your Region

Hit **+ Create Project**. You’ll see a popup where you can confirm your project's name and choose the Firebase region that best serves your users.

###### Step 3: Connect Your Google Account

Choose **Create** or **Sign in with Google** to link your Firebase account. If asked, you must grant the access requested from 'flutterflow\.io' to be able to create and configure the Firebase project on your behalf. Here, you can **Select all** and click **Continue**.

![Alt text](https://docs.flutterflow.io/img/firebase/warning-firebase.png)

Once initiated, FlutterFlow will handle the rest of the project creation in the background.

Here's a quick walkthrough:

[Shopping App - FlutterFlow](https://demo.arcade.software/C4Db1hkZU3Dyqd5VmY99?embed\&show_copy_link=true)

As soon as the process is completed, you will see the following view in your Firebase Settings dashboard.

![Firebase Project Created](https://docs.flutterflow.io/img/firebase/firebase-created-managed.png)

###### Enable Firebase Authentication

If you want to use the Firebase Authentication in your app or the Firebase Content Manager, you must enable the authentication in the Firebase console and enable the 'Email/Password' sign-in.

###### Enable Firebase Storage

If you plan to use Firebase storage in your app, click on the Enable Storage on Firebase and enable it on Firebase console.

###### Download Firebase Config files

The configuration files are necessary when connecting to Firebase. It contains various settings and keys that enable your project to communicate with Firebase services. To generate those files, click on Auto Generate Config Files and then click Generate Files.

#### Connect an existing Firebase project manually

If you already have a Firebase project and want to connect it to your current FlutterFlow project, go to **Settings & Integrations > Project Setup > Firebase** and click on the Firebase Setup Wizard. A pop-up dialog will appear. Follow these steps:

###### Setup Firebase

In the dialog, scroll down to **Setup Firebase**, check that option, and click **Next Step**. The second page of the dialog will open. Before filling in more information, you need to allow FlutterFlow to access your Firebase project. The following section will guide you through this process.

###### Allow FlutterFlow to Access Your Project

1. Go to the Firebase console of your existing project, navigate to the far left menu, and select **Project Settings -> Users and Permissions**.

2. Select **Add Member** from the top right.

3. Add **<firebase@flutterflow.io>** as an "**Editor**" for your project and select **Done**. Then press **Add Member**. ![firebase-add-member.png](https://docs.flutterflow.io/assets/images/firebase-add-member-c9dc098f376dda9328e0070f1f3b0f69.png)

4. On the same page (i.e., Users and Permissions), select **Advanced Permission Settings** (small blue text below the table). This will open the Google Cloud console in a new browser window.

![Steps 2, 3 and 4](https://docs.flutterflow.io/img/firebase/project-settings.png)

5. Find the row containing *<firebase@flutterflow.io>* and select **Edit principal** (pencil on the far right of the row).

![In the Google Cloud console page](https://docs.flutterflow.io/img/firebase/firebase-principal.png)

6. Select **+ Add Another Role.**

7. Under **Select A Role**, search for **Service Account User** (you may need to scroll to find this). Select **Service Account User**.

![On choosing Select A Role and searching for Service Account User](https://docs.flutterflow.io/img/firebase/service-account-user.png)

8. Select **+ Add Another Role** again. Under **Select A Role**, search for **Cloud Functions Admin**. Select **Cloud Functions Admin**.

> **Info:** Note: The option to add Cloud Functions Admin may only show up if you are on a Firebase Blaze plan. In addition, you may need to [enable cloud functions](https://console.cloud.google.com/marketplace/product/google/cloudfunctions.googleapis.com) first. Cloud Functions Admin permissions are required for several FlutterFlow features (e.g., Push Notifications). Adding this Cloud Functions Admin is optional, but not doing so will prevent you from using any functions that require Cloud Functions.

###### Connect and autogenerate files

1. From the Firebase dashboard of your project, navigate to the far left menu and select **Project Settings**.

2. Under Your Project, find the **Project ID**, right-click it, and copy.

3. Return to FlutterFlow, enter your Firebase Project ID in the dialog, and click Connect. A green checkmark will appear once the connection is successful.

4. Under Config Files, choose **Generate Config Files** and then select **Generate Files**.

> **Info:** Do not close or refresh the page while the files are being generated.

#### Connect to Firebase on Creating a New FlutterFlow Project

If you know you'll be integrating Firebase as you create your project, you can do the following:

###### Step 1: Create a new project and enable Firebase

First, create a new project, and while doing so, keep the Setup Firebase option enabled and click Next Step.

![Alt text](https://docs.flutterflow.io/img/firebase/create-project-enable-firebase.png)

###### Step 2: Connect to Firebase

If you'd like FlutterFlow to create a Firebase project for you, click **"+ Create Project"** and follow the [related steps](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#create-a-new-firebase-project-from-flutterflow). Alternatively, if you wish to connect an existing Firebase project manually, please follow the [manual steps here](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#connect-an-existing-firebase-project-manually).

###### Step 3: Enable Authentication

Turn on the Enable Authentication to allow users to log into your app using various sign-in methods, including email and password, social media providers, and even phone number.

**Note:** this step only enables authentication. You will need to complete an additional setup to implement authentication logic later.

![Enable Authentication During Project Creation](https://docs.flutterflow.io/img/firebase/enable-auth-option.png)

#### Enable Firestore for Database Access

If you plan to use Firestore Database as your backend, follow these additional steps to enable Firestore. This will allow you to create collections and add documents directly from FlutterFlow.

To configure Firestore Database:

1. From the Firebase dashboard of your project, navigate to the far left menu. Under Build, select Firestore Database and then select Create Database (marked in yellow in the screenshot).

![Alt text](https://docs.flutterflow.io/img/firebase/firebase-db-enable.png)

2. Next, you will need to set your **Firebase security rules**. To get started quickly, you can select Start in test mode and select Next.

![Alt text](https://docs.flutterflow.io/img/firebase/firebase-security.png)

> **Info:** We recommend updating your Firebase security rules before deploying your app. Please see [this link](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-rules) for additional information on Firestore security rules.

3. Next, you will need to choose the location where your Firestore data will be stored. From the dropdown, select a location and then select Enable. Please see this link for additional information on Firebase locations.

![Alt text](https://docs.flutterflow.io/img/firebase/firebase-location.png)

On completion, you land at the panel view of Cloud Firestore and can start creating collections and documents right away!

##### Adding Indexes

Deploying indexes is necessary to perform certain queries in your Firestore database. Firestore automatically adds indexes for the most basic queries. However, when you apply both filtering and ordering while querying a collection, an index is necessary, and a warning will be generated to add it.

We create indexes for you. The only thing you need to do is deploy them to your Firestore database.

Here are the steps to deploy indexes.

* Click on the Firestore from the Navigation Menu (left side of your screen).
* Switch to the **Settings** tab.
* Scroll down to the **Firestore Indexes** section and click on **Deploy**.

Please note

If you add a filtering/ordering on the query or change the existing filtering/ordering settings, you should deploy the Firestore Indexes again.

#### Enable Billing

If you want to deploy [Cloud Functions](https://firebase.google.com/products/functions) (e.g., Braintree payments, Push Notifications) or use [Firebase Cloud Storage](https://firebase.google.com/products/storage), you will need to enable billing for your Firebase project. Please follow these steps to enable billing:

1. From the Firebase dashboard of your project, navigate to the far left menu. Under Build, select **Functions** and then select **Upgrade project**.

2. Select **Purchase**. If this is your first time enabling billing, you will be taken to a new page to provide your payment information. Otherwise, you can set a project budget. Please see [this link](https://firebase.google.com/pricing) for additional information on Firebase pricing.

![Alt text](https://docs.flutterflow.io/img/firebase/billing.png)

---

### Firebase Crashlytics {#firebase-crashlytics}

*Learn how to integrate Firebase Crashlytics in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/firebase/crashlytics

[Firebase Crashlytics](https://firebase.google.com/products/crashlytics) is a crash-reporting tool that helps you catch errors. It enables you to troubleshoot the issue by logging the details, such as the exact line number that caused the error, device name, OS version, and time when the crash happened.

To enable Firebase Crashlytics, navigate to **Settings and Integrations** > **Project Setup** > **Firebase** > Expand the **Crashlytics** section and **Enable Crashlytics**.

Firebase Crashlytics only supports catching errors on mobile platforms (Android and iOS).

You can see all the logged errors/crashes inside the Crashlytics dashboard of your [Firebase console](https://console.firebase.google.com/). There, you'll see the list of crashes (with the page name and line number that caused the issue), and you can filter it by their state, signal, device type, and OS.

![Crashlytics dashboard](https://docs.flutterflow.io/assets/images/crashlytics-dashboard-2d40f05759331f5b6b4b39142a44ec4f.avif)

1. Click on the issue name to see its details.
2. To test the crash on your app, [download the app](https://docs.flutterflow.io/flutterflow-cli/exporting), add a code that throws an error, and run it on a mobile device or emulator with an active internet connection.

![Test crash](https://docs.flutterflow.io/assets/images/test-crash-b03b9e0d185ce6ce1c38646edc09447b.avif)

---

### Performance Monitoring {#performance-monitoring}

*Learn how to integrate Firebase Performance Monitoring in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/firebase/performance-monitoring

[Firebase Performance Monitoring](https://firebase.google.com/docs/perf-mon) is a tool that *automatically* collects performance data from your app and provides insights through the Firebase console. It can monitor both network requests and specific parts of your code.

Enabling performance monitoring is beneficial for:

* **Identify Bottlenecks**: Discover where your app's performance is lagging.
* **Improve User Experience**: Slow or unresponsive apps lead to a poor user experience.
* **Data-Driven Decisions**: Make optimization decisions based on real performance data.
* **Monitor Network Calls**: See how long network requests take, helping identify slow APIs or network issues.

To enable performance monitoring, navigate to Settings and Integrations > Project Setup > Firebase > Open the Performance Monitoring section and Enable Performance Monitoring toggle.

---

### Remote Config {#remote-config}

*Learn how to integrate Firebase Remote Config in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/firebase/remote-config

[Firebase remote config](https://firebase.google.com/docs/remote-config) allows you to control your app's behavior and appearance without pushing an app update. For example, you could use it to change or show/hide certain elements of your app, such as a promo banner and Santa hat, or use it as a feature flag (payments, food delivery) with no need to publish an app update.

![Using Firebase Remote Config to show/hide a feature](https://docs.flutterflow.io/assets/images/show-hide-fi-2c2cc22236d36e12d343efc5e727a8f5.avif)

When you enable the Remote Config, you must specify the parameter in our builder (called 'in-app defaults') and inside the Remote Config dashboard of your [Firebase console](https://console.firebase.google.com/). When the app starts, it fetches config values from the Firebase console, and for any reason, if it fails, your app will use the in-app defaults.

> **Warning:** The app will try to fetch values every time it starts. However, due to the minimum fetch interval of 1 hour (set by default), the values won't be fetched more than once in 1 hour.

#### Using Firebase Remote Config

Follow the steps below to use the Remote Config:

##### 1. Enable Remote Config

To enable Remote Config, navigate to **Settings and Integrations** > **Project Setup** > **Firebase** > Expand the **Remote Config** section and **Enable Remote Config**.

![Enabling Remote Config](https://docs.flutterflow.io/assets/images/remote-config-d8b616f9817002cfc3f28ac542a0e971.avif)

##### 2. Add parameter in Firebase Console

You will be able to dynamically control your app using the parameters created in the Firebase Console of your project.

To create the parameter:

1. Navigate to the [Firebase Console](https://console.firebase.google.com/u/0/) > Enagage > Remote Config\*\* page.
2. If this is the first time, click **Create configuration** button.
3. Click **Add parameter**. This will open the **Create parameter** section on the right side.
4. Enter the **Parameter name** (e.g., *show\_promo\_banner*, *primary\_color*, etc.).
5. Set the **Data type** among the *String*, *Number*, *Boolean*, and *JSON*.
6. Set the **Default value**.
7. If you enable the **Use in-app default** toggle, any change made to this parameter from here won't be reflected in your app. Instead, your app will use values from the parameters defined in our builder (see how to create it in the [next step](https://docs.flutterflow.io/integrations/firebase/remote-config#3-add-parameter-in-flutterflow)).
8. Click **Save**.
9. Click **Publish Changes** to make this parameter immediately available to your app.

##### 3. Add parameter in FlutterFlow

Parameters added to your FlutterFlow project are called in-app defaults. To add them:

1. Navigate to **Settings and Integrations** > **Integrations** > **Firebase Remote Config**.
2. Click **+ Add Parameter**. A pop will open.
3. Enter the parameter **name**, select the **Data Type**, set its **Default Value**, and click **Create Parameter**. **Note**: The parameter name must match the name given in the [previous step](https://docs.flutterflow.io/integrations/firebase/remote-config#2-add-parameter-in-firebase-console).

##### 4. Use parameter

Now you can access the newly created parameter from the **Set from Variable > Firebase Remote Config**.

Here's an example of using the remote config parameter to set the [conditional visibility](https://docs.flutterflow.io/resources/ui/widgets/widget-commonalities#conditional) for the social login feature.

Here's another example that changes the app's background using the color value from the Remote Config parameter.

---

### Gemini {#gemini}

*Learn how to get started with the Gemini action in your FlutterFlow app to generate text, process text-and-image inputs, and count tokens.*

**Source:** https://docs.flutterflow.io/integrations/gemini

With the Gemini action, you can generate text, process text-and-image inputs, and effortlessly count tokens.

Deprecation Notice

The Gemini action will eventually be deprecated. We recommend transitioning to the newer and more powerful [**AI Agent**](https://docs.flutterflow.io/integrations/ai-agents) actions.

#### Setup

Integrating [Gemini AI](https://gemini.google.com/app) into FlutterFlow unlocks Google's advanced AI capabilities right within your app. Follow this guide to integrate Gemini AI:

1. Visit [**Google AI Studio**.](https://aistudio.google.com/) and click on **Get API Key** > **Create API key**. You can create an API key within a new Google Cloud project by selecting *Create API key in new project*, or choose an existing Google Cloud project.

2. Once the API key is generated, copy it.

> **Tip:** To secure your API keys, refer to the Best Practices guide: [Secure API Keys](https://docs.flutterflow.io/best-practices/secure-api-keys)

1. Go back to FlutterFlow and navigate to **Settings and Integrations > Integrations > Gemini**.

2. Toggle on the **Enable Gemini** option and paste the copied **API key** into the designated field.

3. Now, you can add [Gemini actions](https://docs.flutterflow.io/integrations/gemini#gemini-action) at appropriate events within your app.

With these steps, you’re all set to enhance your FlutterFlow app with powerful AI features.

#### Gemini \[Action]

To add a Gemini Action, follow these steps:

1. Select the **Widget** (e.g., Container, Button, etc.) on which you want to add the action.

2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window. Click on the **+ Add Action**.

3. On the right side, search and select the **Gemini** (under *Integrations*) action.

4. Set the [**Action Type**](https://docs.flutterflow.io/integrations/gemini#types-of-gemini-action). **Note** that If you set this type to *Text from Image*, you must provide the image as well.

5. Provide the **Text prompt** that will be used to generate the result from the Gemini AI model. For this example, we use this prompt: `When users upload a photo, you analyze the food in the photo and tell if it is healthy to eat`.

6. Provide the **Action Output Variable Name** where the result of the generation will be stored. Later, you can access this variable from anywhere on the page.

[YouTube video player](https://www.loom.com/embed/8b57fff59e3f496b84eb719f0a41bc85)

#### Types of Gemini action

Following are the types of Gemini actions you can add:

##### Generate Text

This action allows you to create natural language text based on the text prompts you provide.

**Example**:

* **Input**: *Text prompt* - "Write a brief summary of the benefits of exercise."
* **Output**: *Action Output Variable Name* - "Exercise can improve mental health, increase lifespan, enhance physical fitness, and reduce the risk of chronic diseases."

##### Count Tokens

With this action, you can analyze the number of tokens in a given text prompt. This is particularly useful for applications that need to monitor or restrict the length of text inputs, ensuring that content stays within desired limits or quotas.

A token can be a word, but it can also be a part of a word or even punctuation. The division of text into tokens depends on the tokenization algorithm being used. For Gemini models, a token is equivalent to about 4 characters. 100 tokens are about 60-80 English words.

**Example**:

* **Input**: *Text prompt* - "Gemini is fun!"
* **Output**: *Action Output Variable Name* - 5

##### Text from Image

This action enables your app to analyze images and generate descriptive text about them. It can interpret the content of an image, such as identifying objects, scenery, or activities, and then provide a textual description.

**Example**:

* **Input**: *Text prompt* - "Identify the object in the image?"

* **Input**: *Image Type* - There are two ways you can provide an image.

  * **Image Network URL**: You can provide the URL of the image hosted on the internet. If you upload an image to **Firebase** or **Supabase**, you can provide the image via ***Widget State > Uploaded File URL***\*.\*
  * **Uploaded Image File**: You can also provide an image file directly [from your device](https://docs.flutterflow.io/integrations/gemini) via ***Widget State > Uploaded Local File***\*.\*

* **Output**: *Action Output Variable Name* - "This is a pipe organ. It is a large musical instrument that is used in churches, concert halls, and other large buildings. The sound of a pipe organ is very powerful and can be used to create a wide variety of music."

---

### Google Analytics {#google-analytics}

*Learn how to setup Google Analytics in FluterFlow*

**Source:** https://docs.flutterflow.io/integrations/google-analytics

Integrating Google Analytics into your FlutterFlow project enables you to monitor user interactions, track app performance, and gain valuable insights to enhance user experience. Here's a comprehensive guide on setting up and utilizing Google Analytics within FlutterFlow.

> **Tip:** Google Analytics is integrated into Firebase. This means you must [**set up Firebase**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) to enable analytics tracking and log events from your FlutterFlow app.

#### Enable Google Analytics in Firebase

To enable Google Analytics in Firebase, open the [Firebase Console](https://console.firebase.google.com/) and select your project. From the left-side menu, navigate to **Analytics > Dashboard** and click **Enable Google Analytics**. Choose an existing Google Analytics account or create a new one, then **Finish** the setup.

#### Enable Google Analytics in FlutterFlow

To begin collecting analytics data, navigate to **Settings and Integrations > Integrations > Google Analytics** within your FlutterFlow project and toggle on the **Enable Google Analytics** option.

Once enabled, you can set the [Predefined Events](https://docs.flutterflow.io/integrations/google-analytics#predefined-events). You can selectively toggle these options to log specific user interactions automatically.

![enable-google-analytics](https://docs.flutterflow.io/assets/images/enable-google-analytics-5d5b07e4f1dee8359e314b1148ef398c.avif)

##### Predefined Events

You can enable automatic logging for the following events:

* **On Page Load**: Logs an event when a user opens a page, recorded with the Firebase-recommended name `screen_view`. The actual screen name is accessible within the `screen_name` parameter.
* **On Action Start**: Captures events when users interact with widgets that trigger actions. Events are logged in the format `{WIDGET_NAME}_{TRIGGER_TYPE}`. For instance, if a user taps a button that navigates to another page, the event is logged as `Button_navigate_to`.
* **On Each Individual Action**: This logs an event for every individual action or action chain for a given widget. It will be logged as `{WIDGET_NAME}_{TRIGGER_TYPE}` For example, when the user taps on a button and adds the *Upload Media* action followed by the *Update App State* action, the event will be logged as `Button_upload_media` and `Button_update_local_state`.
* **On Authentication**: Logs events for authentication-related actions such as sign-up, login, logout, password reset, or account deletion. Events are logged using the action type, e.g., `sign_up` or `login`.

> **Tip:** To easily identify widgets in the analytics dashboard, consider giving them recognizable names, such as `BuyButton` instead of just `Button`.

#### Google Analytics Event \[Action]

In addition to predefined events, you can track specific user actions relevant to your app’s goals. This action allows you to log custom events and record additional information through parameters.

For example, in an e-commerce app, you might log product purchases with parameters such as `product_category: electronics` to track item categories and `user_role: premium` vs. `user_role: guest` to differentiate user types.

To log a custom event, add the **Google Analytics Event** action and enter a clear, descriptive **Event Name**. You can add parameters for extra context by clicking **+ Add Parameter** and providing **Key**-**Value** pairs (e.g., `product_category` as the Key and `electronics` as the Value).

![google-analytics-action](https://docs.flutterflow.io/assets/images/google-analytics-action-be22e990c2948c5b13eb97c716ff0b22.avif)

#### Viewing Analytics Data

To see all tracked events, both automatic and custom, open the [Firebase Console](https://console.firebase.google.com/) and select your project. From the left-side menu, navigate to **Analytics > Dashboard** to access detailed event reports.

Use this data to gain insights into app screens, which funnels convert best, and where churn or drop-offs occur. In the long run, these metrics help you make data-driven improvements that enhance the user experience and maximize the impact of your FlutterFlow app.

#### FAQs

Why don’t I see any Analytics data yet?

Event data may not appear instantly, which can be frustrating during development. Firebase may take up to **24 hours** to display event data in the main dashboards. Ensure your device has internet access and you’ve used the app at least once since enabling Analytics.

---

### Maps & Places APIs {#maps-places-apis}

*Learn how to generate and use Maps keys for Google Maps integration in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/google-maps/generate-maps-keys

FlutterFlow natively supports **Google Maps**, providing a seamless and efficient way to embed interactive maps into your FlutterFlow apps. It also supports **Places API** that returns formatted location data and imagery about establishments, geographic locations, or prominent points of interest.

#### Add Maps APIs

To enable **Google Maps** in your project, please follow the steps:

##### Get API Keys

To start working with **Google Maps APIs**, you need to enable the **Maps API** from the [Google Cloud Console](https://console.cloud.google.com/).

1. As you land on the Cloud console, make sure you are in the correct Google Cloud project. Then, from the right menu, click on [**Library**](https://console.cloud.google.com/apis/library) and search for **Maps**.

2. You may receive a prompt from Google Cloud to add a billing account. Please add a billing account to continue.

3. You will see options such as the **Maps SDK for iOS, Maps SDK for Android**, and the **Maps Javascript API**. Select the platform you wish to support and then click **Enable**. If you are running on Run Mode, ensure that your Maps Javascript API is enabled.

> **Warning:** To secure your API keys, refer to the [**Best Practices guide: Secure API Keys**](https://docs.flutterflow.io/best-practices/secure-api-keys)

* Click on the Credentials menu from the left panel.

* Find the key for the platform you need, and copy the key.

##### Add keys to FlutterFlow

Now add the API keys platform wise to FlutterFlow Settings page

![g-maps-settings.png](https://docs.flutterflow.io/assets/images/g-maps-settings-fb9c10318d1871f824e906ac5929daa4.png)

##### Create a new Key if not available

If you don't find the Android key (auto created by Firebase) or iOS key (auto created by Firebase) in the Google developer console, here are the steps to create one:

* On your Cloud console, click the **Credentials** menu on the left.

* Click on the **+ Create Credentials** at the top.

* Click on the **API Key** to create a new key for the Android app. Similarly, create one for iOS and Web.

#### Add Places APIs

You can [enable the **Places API**](https://console.cloud.google.com/apis/library/places-backend.googleapis.com) from your Google Cloud Console — make sure you are in the correct Google Cloud project. **Please note** that the current [PlacePicker widget](https://docs.flutterflow.io/integrations/google-maps/place-picker-widget) uses the legacy Places API. We plan to update the PlacePicker widget soon to support the new API. In the meantime, ensure that the legacy Places API is enabled for full functionality.

![places-api.png](https://docs.flutterflow.io/assets/images/places-api-75e9526626afcffa8bd5266aa4b37992.png)

---

### Google Maps Widget {#google-maps-widget}

*Learn how to add and configure the Google Maps widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/google-maps/google-maps-widget

The **Google Maps** widget enables the integration of interactive maps into your app, offering users valuable geographical insights. For instance, in a food delivery app, this widget could display the locations of restaurants. It offers a range of customization options, allowing you to tailor the display with various map types and markers to suit your specific needs.

Feature Completion

As we continuously enhance our platform, please note that while our integration is robust, it is not yet feature-complete. We encourage you to review the available APIs and features detailed below to ensure they meet your app development needs before integration.

![google-maps-widget.png](https://docs.flutterflow.io/assets/images/google-maps-widget-36f25b917240de88b6192e5a0fe57418.png)

Prerequisite

Ensure you have added the [**Google Map API keys**](https://docs.flutterflow.io/integrations/google-maps/generate-maps-keys#get-api-keys) before adding the Google Maps widget to your project

#### Add Google Map widget

1. Open the Widget Palette and locate the **Google Map** widget under the **Base Elements** tab. You can drag it to your desired location or add it directly from the widget tree or canvas area.

2. By default, the map displays a random location. To set a specific location, go to the **Properties Panel > Initial Location**.

3. Enter the latitude and longitude values in the **Lat and Lng** fields to specify the location. To use the user's current location, set a variable through the **Set Variable menu > Global Properties > Current Device Location**.

4. To change the map type, go to the **Properties Panel > Map Type** and select one of the following options:

   * **Roadmap:** Displays the default road map view.
   * **Terrain:** Shows a physical map based on terrain information.
   * **Hybrid:** Combines normal and satellite views.
   * **Satellite:** Displays satellite images from Google Earth.

5. To customize the visual appearance of your map, navigate to the **Properties Panel > Map Style**.

6. To set the **initial zoom level** of the map, go to the **Properties Panel > Initial Zoom** of Map and enter the desired value. Note that a higher value will zoom in on the map while a lower value will zoom out.

> **Tip:** If you don't see your current location while testing, make sure you have enabled location permission in your browser.

![location-browser.png](https://docs.flutterflow.io/assets/images/location-browser-e5f61c7357f9afa44240d26841e467aa.png)

#### Markers

A marker is an icon that appears over the map, indicating a location. To add markers:

* Select the **Google Map** widget, move to the **Properties Panel > Num Markers** and select whether you want to show **Single** or **Multiple** markers.

##### Set Markers from Firebase

* Set the Marker Type to **Document** if the data is on Firestore Collection

* In case of Documents, create a collection and query it on any widget (must be a parent of GoogleMap) or page.

* In Marker Document, set the source of markers as shown in the following video.

##### Set Markers from List of LatLng

If you choose **LatLng**, you must provide a source that contains a list of locations as Data Type (LatLng) (e.g., App State > \[variable\_name] (List of **LatLng**)).

##### Changing Marker Color

To change the marker color, move to the Properties Panel > Google Map > set the Marker Color dropdown value to the color you like:

![marker-color.png](https://docs.flutterflow.io/assets/images/marker-color-06977322341a142ddc3bbe1f5b90b2d9.png)

##### Set Marker Image

Custom marker images can enhance your map interface by making it more intuitive and visually engaging, while also aligning with your app's branding. To set an image as a marker:

* Move to the **Properties Panel > Google Map > set the Marker Icon to Image**.

* Select the type of image you want to set:

  * For an image hosted online, set the Image Type to **Network** and specify the image URL in the Path field.
  * To provide an image from your system, set the Image Type to **Asset** and upload the image.

##### Centering map on marker tap

To center a map on a marker tap, move to the **Properties Panel > Google Map > enable the Centering Map on Marker Tap toggle**.

#### On Marker Tap \[Action Trigger]

Sometimes, you might want to receive a callback when a user taps on a marker. This can be useful for dynamically displaying additional information about the location, opening a detailed view, or initiating other actions based on the selected marker.

Here’s how you do it:

* Select the **Google Map** widget.
* From the Properties Panel, select **Actions** and open the **Action Flow Editor**.
* Under the action trigger **On Marker Tap**, add any actions here.

![marker-tap.png](https://docs.flutterflow.io/assets/images/marker-tap-4a87b7d9ec158938bef841037f291923.png)

#### Advanced Customizations

You can customize the appearance and behavior of this widget using the various properties available in the properties panel.

##### Allow Interacting With the Map

By default, the map interaction feature is enabled, allowing users to drag, zoom in, and zoom out on the map. However, you can disable the **Allow Zooming the Map** and **Show Zoom Buttons** on the Map options if you wish to restrict the zoom functionality.

To access these settings, navigate to the **Properties Panel > Google Map > Allows Interacting with the Map**.

###### Map Takes Gesture Preference

When this is turned on, any gestures, such as zooming or dragging, will only affect the map, not the rest of the page. This is helpful if your map is inside a scrollable page, so users can interact with the map without accidentally scrolling the whole page.

> **Info:** This setting is only available if **Allow Interacting** and **Allow Zooming** are turned on.

* Map Takes Gesture Preference (Disabled)
* Map Takes Gesture Preference (Enabled)

##### Show User Location

When enabled, a blue dot appears on the map to indicate the user's current location. If the map is moved, users can re-center their location by clicking the button at the top right side.

To enable this option, navigate to the **Properties Panel > Google Map > enable the Show User Location toggle**.

> **Note:** When you enable this option, make sure to set the **Initial Location to Global Properties > Current Device Location**.

##### Showing Compass

While exploring the map, users may rotate the map (which can make it difficult to trace the route). Enabling compass will allow users to bring the map to its original direction.

To enable the compass, navigate to the **Properties Panel > Google Map > enable the Show Compass toggle**.

##### Enabling map toolbar

The Toolbar, located at the bottom right of the map, becomes visible when a user selects a marker. It offers quick access to either a map view or directions in the Google Maps mobile app.

To enable the toolbar, navigate to the **Properties Panel > Google Map > enable the Show Map Toolbar toggle**.

##### Showing Traffic on Map

Showing traffic on the map allows user to know the flow of traffic on the roads and helps them decide on a better route.

To show live traffic on a map, navigate to the Properties Panel > Google Map > enable the Show Traffic on Map toggle.

#### FAQ

Why Google Maps custom markers are not working in run mode or test mode?

Due to a recent update, Google Maps custom markers won't work in Run or Test mode unless CanvasKit is enabled. This is expected behavior. To use custom markers effectively, enable CanvasKit from [**Advanced Web Settings**](https://docs.flutterflow.io/resources/projects/settings/project-setup#advanced-web-settings).

---

### Move Map Center [Action] {#move-map-center-action}

*Learn how to use the Move Map Center action in your FlutterFlow app to adjust the center of the Google Map.*

**Source:** https://docs.flutterflow.io/integrations/google-maps/move-map-center-action

This action allows you to center the map on a specified location, such as setting the pickup and drop-off points. You can define the location either by directly inputting the latitude and longitude values or by using a variable.

Prerequisites

* To implement this feature, add a Google Maps widget to your page or component. [**Learn how.**](https://docs.flutterflow.io/integrations/google-maps/google-maps-widget)
* If you wish to enable users to select locations from a dropdown using FlutterFlow's PlacePicker widget, you can also integrate the Place Picker widget into your map view. [**Learn more here**](https://docs.flutterflow.io/integrations/google-maps/place-picker-widget).

Assuming you've set up the Place Picker widget on your Google Maps widget view, let's add a button that triggers the action to move the map center, so the map centers on the newly selected location.

In our example, we've added an IconButton with a location pin icon. For the button's OnTap action trigger, we'll add the Move Map Center action and set the LatLng to the LatLng of the Place Picker's selected place. You must check if the PlacePicker value (or the variable holding your new LatLng) is set before calling the Move Map Center action.

![move-map.png](https://docs.flutterflow.io/assets/images/move-map-365ef164a672a6e3878a06126998459f.png)

---

### Place Picker Widget {#place-picker-widget}

*Learn how to add and configure the Place Picker widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/google-maps/place-picker-widget

The `PlacePicker` widget is designed to retrieve information about places, such as establishments (e.g., buildings, parks, museums) and geographic features (e.g., roads, lakes, mountains). It provides details like name, address, city, state, country, zip code, and latitude-longitude coordinates.

This widget is particularly useful in applications like cab booking services. For instance, it can be used to capture the exact location and full address of a destination, displaying this information on a page or integrating it into a Google Map.

Visually, the PlacePicker appears as a button. When tapped, it enables you to search for a place by typing its name, and displaying a dropdown list of matching locations. Once a place is selected, its name is displayed on the button, and additional details are accessible through the placePickerValue variable from Widget State.

Here's an example from the Demo app:

[Place Picker Widget](https://demo.arcade.software/EQ4xhHBgjMp4wbm3aTin?embed\&show_copy_link=true)

Prerequisites

* The Place Picker **requires a Google Maps API key**. See how to [**create and add API keys**](https://docs.flutterflow.io/integrations/google-maps/generate-maps-keys#add-maps-apis) to FlutterFlow.
* Ensure you have enabled the [**Places API**](https://docs.flutterflow.io/integrations/google-maps/generate-maps-keys#add-places-apis) from Cloud console.
* Enable **Google Maps Platform Billing** via your Cloud console. Please note: Failing to enable the Google Maps Platform Billing will not show any place in an autocomplete list.

#### Add Place Picker widget

To add the PlacePicker widget to your project:

[Add Place Picker widget](https://demo.arcade.software/uWaLSOHPZctjnGik03Pu?embed\&show_copy_link=true)

By default, the `Place Picker` widget features an icon and the text "Select Location" on the button. You can modify the styling and properties of these elements from the Properties Panel on the right.

If you retain the Text widget, the text will update to the name of the selected location when a user makes a selection. Both the icon and text are optional; adjust them according to your design requirements.

![place-picker-properties.png](https://docs.flutterflow.io/assets/images/place-picker-properties-40c1481618f4452598a0fc7b9fd9aefa.png)

The widget properties of Place Picker widget

#### Use PlacePicker Values

The selected place’s details are stored in a `GooglePlace` custom data type provided by FlutterFlow. You can access this via **Widget State > placePickerValue**, which includes fields like name, address, latitude/longitude (LatLng), city, state, country, and ZIP code. These values can be used to display content in Text widgets or perform conditional logic based on the selected location.

[Use PlacePicker widget state](https://demo.arcade.software/oje0Gsbf9IJh7M0pb6Tv?embed\&show_copy_link=true)

---

### Static Map Widget {#static-map-widget}

*Learn how to add and configure the StaticMap (Mapbox) widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/mapbox/staticmap-widget

The StaticMap widget shows an image of the map from the [mapbox](https://www.mapbox.com/). This widget is a good choice when you want to display a location on a map without interactivity or controls such as zoom-in, zoom-out, and map scrolling.

> **Tip:** To display a map with interactivity or controls, use the [**GoogleMaps**](https://docs.flutterflow.io/integrations/google-maps/google-maps-widget) widget.

#### Adding StaticMap widget

Here's an example of how you can add the StaticMap widget to your project:

1. First, drag the **StaticMap** widget from the **Base Elements** tab (in the Widget Panel) or add it directly from the widget tree.
2. You'll need the Mapbox API key to render the map image. Get the API key by creating the [Mapbox account](https://account.mapbox.com/auth/signup/) and then return to FlutterFlow, move to the properties panel, scroll down to the Static Map section and enter the key into the **Mapbox API Key** input box.
3. To display your location on the map, enter the **Latitude** and **Longitude** values inside the **Lat** and **Lng** input boxes.

> **Tip:** To get the lat long values for any location, open to Google Map, right-click on any place and click on the first item from the list. It should look like this `19.080045795863743`, `72.8794235725136`.

#### Customization

You can customize the appearance and behavior of the widget using the various properties available under the [properties panel](https://docs.flutterflow.io/flutterflow-ui/builder#navigation-menu).

##### Changing the map style

Changing the map style allows you to change the overall theme and type of the map, such as Light, Dark, Street, and Satellite.

To change the map style:

1. Select **StaticMap** from the widget tree or the canvas area.
2. Move to the properties panel and scroll down to the **Static Map** section.
3. Find the **Map Style** property and choose among the *Light*, *Dark*, *Outdoor*, *Street*, *Satellite*, and *Detailed* *Satellite*.

##### Set zoom, tilt, and rotation

You can define the zoom level, adjust the map tilting and rotate the map as per your requirement.

To set the zoom, tilt, and rotation value for the map:

1. Select **StaticMap** from the widget tree or the canvas area.
2. Move to the properties panel and scroll down to the **Static Map** section.
3. Find the **Map Zoom** property and set the value that is good enough to highlight the place. The value starts from 0 (which is a full zoom-out). To zoom in, set the higher value.
4. Find the **Map Tilt** property and enter the value to display the map in the sloping position.
5. Find the **Map Rotation** property and enter the value to rotate the map.

##### Customizing marker

By default, the marker is invisible on the map. You can make it visible by setting the marker color. You can also change the marker icon/image from the URL link.

To customize the marker:

1. Select **StaticMap** from the widget tree or the canvas area.
2. Move to the properties panel and scroll down to the **Static Map** section.
3. To show the marker, find the **Map Marker Color** property, click on the box next to **Unset**, select the color, and then click **Use Color** or click on **Unset** and enter a Hex Code directly.
4. To display the custom marker image/icon, enter the URL into the **Map Marker URL** input box.

This widget does not resize the marker image from the URL link. Make sure you provide the image with the appropriate size.

##### Caching map image

Enabling the cache will store the map image and display it when the internet is unavailable.

To cache the map image:

1. Select **StaticMap** from the widget tree or the canvas area.
2. Move to the properties panel and scroll down to the **Static Map Image** section.
3. Find the **Cache** toggle and turn it on.

##### Changing the box fit

Changing the box fit value allows you to control how the map should display inside the StaticMap widget. Various options under the Box Fit property help you scale (grow or shrink in size) the map image.

To change the box fit value:

1. Select the **StaticMap** from the widget tree or the canvas area.
2. Move to the properties panel (on the right side of your screen) and scroll down to the **Static Map Image** section.
3. Find the **Box Fit** dropdown, and try changing it to the other values.

---

### Launch Map {#launch-map}

*Learn how to open Map app installed on your device from your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/maps/launch-map

Using this action, you can open the Map app installed on your device. For example, you could add this action on an event page to let users know more about the place inside the map apps like Google Maps, Apple Maps, and Waze app.

You can specify the Lat Long details or full address of any place to access the additional information such as directions, call details, timings, photos, street view, reviews, and more.

#### Types of Map apps

This action lets you specify the type of map app to open. If it's not installed, the default map app of the platform will be used. For example, opening the Google Maps on iOS devices. If not installed, it will open the default Apple Maps app.

You can launch the following types of maps apps:

1. **System Default**: Opens the default map app. That is opening Google Maps on Android devices and Apple Maps on iOS devices.
2. **Google Maps**: Google's default map app on Android devices.
3. **Apple Maps**: The default map app on iOS devices from Apple.
4. [**Waze**](https://play.google.com/store/apps/details?id=com.waze): App that tells you about real-time traffic, police, crashes, and more.

##### Adding Launch Map \[Action]

Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.

1. Select the **Widget** (e.g. Location icon, Address text) on which you want to define the action.

2. Select **Actions** from the Properties panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window. 1. Click on the **+ Add Action**.

   2. On the right side, search and select the **Launch Map** action.

   3. Set the **Preferred Map Type** among the **System Default**, **Google Maps**, **Apple Maps,** and **Waze**.

   4. To open the map app using lat long: 1. Set the **Place Type** to **Location**.
      2. Inside the **Location** section, enter the values in the **Latitude** and **Longitude** input boxes. You can also specify these values from a variable, such as an app state variable or a variable from an API response by clicking on the **Set from Variable**.
      3. (Optional) To set the place name (which will be displayed when the map app is opened), Inside the **Title** section, enter the place name in the **Value** input box. To set it from the variable, click on the **Set from Variable**.

   5. To open the map app using address: 1. Set the **Place Type** to **Address**.
      2. Inside the **Address** section, enter the address into the **Value** input box. You can also specify the address from a variable, such as an app state variable, or a variable from an API response by clicking on the **Set from Variable**.
      3. (Optional) To set the place name (which will be displayed when the map app is opened), Inside the **Title** section, enter the place name in the **Value** input box. To set it from the variable, click on the **Set from Variable**.

   6. Click **Close**.

---

### Mux Livestream {#mux-livestream}

*Learn how to get started with MuxBroadcast in your FlutterFlow app for live video broadcasting.*

**Source:** https://docs.flutterflow.io/integrations/mux

Mux Livestream allows you to integrate live video streaming capabilities directly into your FlutterFlow app. It leverages Mux’s powerful streaming API, providing real-time broadcasting features. For a deeper understanding, check out [how live streaming works](https://blog.flutterflow.io/flutter-mux-live-streaming/#how-does-live-streaming-work).

Possible use cases

* **Live Events**: Stream conferences, workshops, or meetups.
* **Educational Apps**: Conduct live classes, webinars, or tutorials.
* **Social Platforms**: Allow users to broadcast and share real-time video content.
* **Customer Support**: Provide interactive support sessions via live video streaming.

#### Setting Up Mux Integration

To get started, go to **Settings and Integrations > Integrations > Mux Livestream** in FlutterFlow and enable **Mux Broadcast**.

Then, create a Mux account and go to **Settings > API Access Tokens**. Click **Generate new token**, choose an environment (Development or Production), check **Mux Video** with **Write** access, name the token, and generate it. Copy the **Access Token ID** and **Secret Key**, paste them into FlutterFlow, and click **Deploy**.

#### Adding MuxBroadcast Widget

To create a live stream, start by adding the **MuxBroadcast** widget to your page. Navigate to the page where you want the livestream to appear, then drag and drop the widget onto the canvas. After placing it, configure its properties using the options available in the right-side panel.

The MuxBroadcast widget comes with three key properties to control the live stream:

* **Show Streaming View**: By default, this option is disabled, meaning the widget only displays the starting interface (camera preview and "Start Stream" button). Enabling this option shows the live streaming UI on the canvas during design time, which helps with layout and styling previews.
* **Broadcast Latency**: Choose between **Standard**, **Reduced**, and **Low** latency modes. Lower latency provides faster interaction but may reduce video quality or reliability depending on the network.
* **Broadcast Audio Channel**: Select **Stereo** or **Mono** audio. Stereo provides richer sound with left and right audio separation, while Mono offers broader device compatibility and lower bandwidth usage.

![muxbroadcast-widget.avif](https://docs.flutterflow.io/assets/images/muxbroadcast-widget-3d31a0be6518f23e2e7223a7423f3958.avif)

You can also customize the **MuxBroadcast** widget to match your app's design using various styling properties. These include:

* **Start Button Style, Text, and Icon:** Adjust the appearance, label, and icon of the broadcast start button.
* **Stop Button:** Customize how the stop button looks.
* **Flip Camera Button:** Modify the button used to switch between front and rear cameras.
* **Live Text Style:** Change the appearance of the "LIVE" text.
* **Live Container & Icon:** Style the container and icon shown during live broadcast.
* **Duration Text Style:** Customize how the elapsed time is displayed.
* **Duration Container:** Style the container holding the duration display.

#### Start and Stop Livestream

You can manage livestreaming using the built-in action triggers available on the **MuxBroadcast** widget: **On Broadcast Start** and **On Broadcast Stop**. These allow you to trigger workflows when a stream begins or ends.

![streaming-action-triggers.avif](https://docs.flutterflow.io/assets/images/streaming-action-triggers-3d8c36d44f47d2fdaa3d3ce14328339e.avif)

##### On Broadcast Start \[Action Trigger]

The actions under this trigger execute when the user clicks the **Start Stream** button. From here, you can access the livestream URL via **Widget State → Mux Playback URL** and perform tasks such as creating a new database record to indicate the livestream has started.

![on-broadcast-start.avif](https://docs.flutterflow.io/assets/images/on-broadcast-start-ec4c0c129b2882a81e72ad3510da627c.avif)

##### On Broadcast Stop \[Action Trigger]

The actions under this trigger execute when the user stops the stream. You can use this trigger to update your database, such as setting a livestream's `is_live` status to `false`, saving the end time, or navigating away from the stream page.

![on-broadcast-stop.avif](https://docs.flutterflow.io/assets/images/on-broadcast-stop-98af6c37211b1d75ce3f3c711cc9f6f9.avif)

#### View Livestream

When a livestream is active, you can access the broadcast instantly via the **Mux Playback URL** provided by the **MuxBroadcast** widget. If the livestream has already ended, additional steps are required to retrieve the archived playback URL and enable playback of the recorded session.

##### Viewing Active Livestream

Once your livestream is active, viewers can watch it in real-time using the **Mux Playback URL**. This URL can be passed to a dedicated page (for example, **ViewBroadcast**) to stream the live session.

To display the livestream:

1. Navigate to your desired list or overview page where livestreams are listed.
2. When a viewer taps on a live broadcast card (e.g., from a `ListView`), navigate to the **ViewBroadcast** page and pass the **Mux Playback URL** as a page parameter.
3. Inside the **ViewBroadcast** page, the **Mux Playback URL** can then be used in a [**VideoPlayer**](https://docs.flutterflow.io/concepts/file-handling/displaying-media#videoplayer) widget to stream the live video.

##### Viewing Past Livestream

When a livestream ends, its original **Mux Playback URL** becomes invalid. To replay an ended session, you need to fetch the archived asset's playback URL that was automatically created during the livestream.

To achieve this, you will need to retrieve the live stream ID from its playback ID, then get the associated asset's playback ID from the livestream's recent assets.

> **Tip:** You'll need to write a [**custom code expression**](https://docs.flutterflow.io/resources/functions/utility#custom-code-expression) or [**custom function**](https://docs.flutterflow.io/concepts/custom-code/custom-functions) to extract the playback ID from the current Mux Playback URL (e.g., from `https://stream.mux.com/iSHXmiVyFshIPgeZf2F78OrvOGnEQd02Api00ipWRwWaQ.m3u8` extract `iSHXmiVyFshIPgeZf2F78OrvOGnEQd02Api00ipWRwWaQ`, which is a playback ID of a livestream) and then reconstruct the new playback URL using the asset's playback ID in the same format.

![get-past-stream-id.avif](https://docs.flutterflow.io/assets/images/get-past-stream-id-7539757ca9f9fc760aeb0afdfc0e4858.avif)

The flow involves using three Mux APIs in sequence:

* [**GET /video/v1/playback-ids/`{PLAYBACK_ID}`**](https://www.mux.com/docs/api-reference/video/playback-id/get-asset-or-livestream-id): Gives the livestream ID from the livestream playback ID.
* [**GET /video/v1/live-streams/`{LIVE_STREAM_ID}`**](https://www.mux.com/docs/api-reference/video/live-streams/get-live-stream): Retrieves the livestream details including `recent_asset_ids` array. Extract the Asset ID from this api response.
* [**GET /video/v1/assets/`{ASSET_ID}`**](https://www.mux.com/docs/api-reference/video/assets/get-asset): Fetches the asset details to get its playback ID from the `playback_ids` array.

Now, use conditional logic to check the livestream status and pass the appropriate playback URL. For example, if the broadcast is live, use the current livestream playback URL directly. If the livestream has ended, call the APIs in sequence to get the asset's playback ID and construct the archived stream's playback URL.

---

### Braintree {#braintree}

*Learn how to integrate Braintree payments in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/payments/braintree

You can accept payments in your app using [Braintree](https://developer.paypal.com/braintree/docs/start/overview) (a service provided by PayPal) integration. This will also allow your users to pay directly using a credit card or using a service like PayPal, Google Pay, or Apple Pay

Prerequisites

Before starting to set up payments, make sure you have:

* Completed all the steps of [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) for your project.
* Upgraded your Firebase project to [**Blaze Plan**](https://firebase.google.com/pricing).
* Enabled [**Firebase Authentication**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) for your project.

> **Info:** FlutterFlow uses [**Firebase Cloud Functions**](https://firebase.google.com/docs/functions) to process a transaction using the selected service (Braintree/PayPal).

#### Braintree Integration

Integrating the Braintree in your app comprises the following steps:

##### 1. Setup payments integration

Payments can be set up on FlutterFlow using Braintree.

You should always test your payment processing using a Sandboxed environment, before deploying them to a production environment.

Follow the steps below to set up using Braintree:

1. Go to [Braintree Website](https://www.braintreepayments.com/).
2. **Sign up** for getting access to the Sandboxed environment. You might receive an email with the additional steps for completing the sign-up process. If you already have a Braintree account just **Log In**.
3. Navigate to the **Braintree Settings** page of your FlutterFlow project by going to the **Settings and Integrations** > **In App Purchases & Subscriptions** > **Braintree**.
4. On this page, **Enable Braintree/PayPal** using the toggle.
5. Under the **Credentials (Sandbox)** section, you need to enter the **Merchant ID**, **Tokenization** **Key**, **Public Key** & **Private Key** of the Braintree account.
6. To get the required credentials, navigate to your Braintree account **Home** page.
7. Click the **gear icon** (top-right corner), select **Business**. From this page, you'll get the **Merchant ID**.
8. Now, go to the **API** page. Here, you'll get the **Public Key** & **Private Key**.
9. To generate a **Tokenization Key**, go to the **API** page, and click **Generate New Tokenization Key**. Copy the Key and enter it in the respective field of FlutterFlow.

Finally, click **Deploy** to upload the Cloud Functions required for processing a payment using Braintree:

##### 2. Enable Google Pay or Apple Pay (Optional)

Completing the payment integration by following the above steps will allow you to accept payments using a credit card or a PayPal account. Additionally, you can accept payments using Google Pay or Apple Pay.

To accept payments using Google Pay or Apple Pay, you'll need to enter the respective **Merchant ID** of the Google/Apple account in the *Braintree Settings* page > *Credentials (Sandbox)* section.

1. To know how to find the Google Pay Merchant ID, navigate to [this page](https://support.google.com/paymentscenter/answer/7163092).
2. Steps for configuring Apple Pay and getting access to the Apple Merchant ID are [here](https://help.apple.com/developer-account/#/devb2e62b839).

##### 3. Trigger payment action

In order to initiate a payment, you have to use the *Braintree Payment Action*. Follow the steps below to add this action to any widget:

1. Select the **widget** on which you want to apply the Action.
2. Select **Actions** from the Properties panel (right menu).
3. Click **+ Add Action** button.
4. Choose a gesture from the dropdown among ***On Tap**, **On Double Tap**, or* **On Long Press**.
5. Select the **Action Type** as ***Braintree Payment***.
6. Enter the **Amount** either by defining a ***Specific Value*** or ***From Variable***.
7. Under **Payment Method**, you can select ***Credit Card***, ***PayPal***, or ***Drop-In***. The *Drop-In* option lets users choose which payment method to use. If you want to use the *Credit Card* option follow the steps [here](https://docs.flutterflow.io/integrations/payments/braintree#using-credit-card).
8. If you have chosen the **Drop-In** option, select the **Allowed Payment Types**. Using Google Pay or Apple Pay will require you to have their respective Merchant ID defined during the Payment Setup process.
9. Enter the **Currency Code** and you can define the optional parameters like **Tax Rate Percentage** and **Shipping Cost**. Enabling Apple Pay requires you to specify the **Country Code** in the respective field.

> **Warning:** Make sure the user is authenticated before triggering the Braintree Payment Action, otherwise, it will result in an error. You can follow the steps on [**this page**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) to set up Authentication.

###### Using Credit Card

If you want to keep only the Credit Card option on your checkout page, you'll need to add the **CreditCardFrom** widget to the page. Follow the steps below:

1. Select the **Payment Method** as ***Credit Card***.
2. Drag and drop the [**CreditCardFrom**](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/credit-card-form) widget onto the canvas.
3. You can modify the design of the form widget as per your app's needs.
4. Again select the **checkout button** to complete defining the Action.
5. Enter the **Currency Code** and you can define the optional attributes like **Tax Rate Percentage** and **Shipping Cost**.

##### 4. Testing

Braintree payments work on real Android devices or in emulators, and App Store purchases only work on real iOS devices. [This document](https://docs.flutterflow.io/testing/local-run) has instructions on how to run your app on an Android or iOS device.

> **Info:** The Braintree Payments cannot be tested in Preview Mode, Test Mode, or Run Mode.

To test your app before deployment:

1. Download and run your project as described [here](https://docs.flutterflow.io/testing/local-run).
2. To test the purchase, you can use any of these [basic test card numbers](https://stripe.com/docs/testing#cards).

##### 5. Releasing to production

Before you release the app to production, complete the following steps:

1. Create the Braintree Account (Not sandbox) and get the production credentials.
2. Add the **production credentials** in the FlutterFlow *Braintree Settings* page > *Credentials (Production)* section.
3. Turn on the **Is Production** toggle present on that page.
4. Deploy the new Firebase Cloud Functions with the production credentials by clicking on the **Deploy** button.

Now, you are ready to build and distribute your app with payments to production.

---

### RazorPay {#razorpay}

*Learn how to integrate Razorpay in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/payments/razorpay

[Razorpay](https://razorpay.com/) is a leading online payment gateway widely used by businesses in India to accept and process digital payments securely.

It provides a platform for merchants and businesses to integrate payment solutions into their websites and mobile apps. It allows customers to make online payments using various payment methods such as credit cards, debit cards, net banking, UPI (Unified Payments Interface), and digital wallets.

> **Warning:** Currently, publishing to the web with Razorpay enabled is restricted due to some regulations.

Prerequisites

Before starting to set up payments, make sure you have,

1. Complete [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) for your project.
2. Enabled [**Firebase Authentication**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) for your project.
3. Upgraded your Firebase project to [**Blaze Plan**](https://firebase.google.com/pricing). We use [**Firebase Cloud Functions**](https://firebase.google.com/docs/functions) to process a transaction.

#### Razorpay Integration

Integrating Razorpay in your app comprises the following steps:

1. [Setup Razorpay](https://docs.flutterflow.io/integrations/payments/razorpay#1-setup-razorpay)
2. [Trigger Razorpay payment](https://docs.flutterflow.io/integrations/payments/razorpay#2-trigger-razorpay-payment-action)
3. [Testing](https://docs.flutterflow.io/integrations/payments/razorpay#3-testing)
4. [Releasing to production](https://docs.flutterflow.io/integrations/payments/razorpay#4-releasing-to-production)

##### 1. Setup Razorpay

Setting up the Razorpay payments includes creating an account, enabling test mode, acquiring the keys from your Razorpay account, and adding them to your project.

> **Warning:** You should always try out payments in a test mode before releasing them to your production application. Hence, the instructions below will guide you on how to get the test keys.

Here are the steps:

1. Create a new Razorpay account from [here](https://dashboard.razorpay.com/signup). If you already have an account, [log in](https://dashboard.razorpay.com/signin).
2. Once you are logged in, turn on the **Test Mode**. Test mode helps you simulate the payments without involving real money transactions.

![Enabling test mode](https://docs.flutterflow.io/assets/images/enable-test-mode-63e84f711a6ce23e85cbd75de80ff2c0.avif)

3. From the left side menu, select **Account & Settings** > Under **Website and app settings** section, select **API keys**.
4. If you're asked to add a website link but your app isn't published yet, you can temporarily publish it to a subdomain using our [web publishing](https://docs.flutterflow.io/deployment/web-publishing) feature. Later, you can update this to your actual domain in both FlutterFlow and Razorpay.

![add-website-link](https://docs.flutterflow.io/assets/images/add-website-link-30819ee6335b8d13c0f6bc7aab70594a.avif)

5. Click **Generate Test Key** and copy the **Key Id** and **Key Secret**. To regenerate, click on **Regenerate Test Key** and choose how you want to deactivate the old key.

![Generate Test Key](https://docs.flutterflow.io/assets/images/generate-test-key-5421c844acd62e810d8a7be508ac4cb4.webp)

6. Return to the FlutterFlow project, navigate to **Settings and Integrations** > **In App Purchases & Subscriptions** > **Razorpay**. Use the toggle to **Enable Razorpay Payments**.
7. Under **Test Credentials**, paste the **Key ID** and **Key Secret** obtained in the previous step.
8. Set your **Business Name**.
9. Click the **Deploy** button.

![deploy](https://docs.flutterflow.io/assets/images/deploy-453f7e6cbf49e55ada68eed897e46030.png)

##### 2. Trigger Razorpay payment \[Action]

To initiate a payment using Razorpay, you must use the **Razorpay Payment** action. This action lets users process a payment inside your app using credit cards, debit cards, net banking, UPI (Unified Payments Interface), and digital wallets via Razorpay.

Follow the steps below to add this action:

1. Select the widget (e.g., checkout button) on which you want to add the action.

2. Select **Actions** from the Properties panel (the right menu), and click Open. This will open an **Action Flow Editor** in a new popup window. Click on the **+ Add Action**.

3. Search and select the **Razorpay Payment** (under *Integrations*) action.

4. Enter or use a variable for specifying the total amount under the **Amount** section. **Note** that the value should be specified in the currency's smallest unit. * For example, *$24.99* should be passed as *2499* (as a round-off integer; otherwise, it would be automatically rounded); similarly, for an amount of ₹120.00, 12000 should be passed.
   * Most probably, you'll specify this value from a variable. If you do so, you might need this [inline function](https://docs.flutterflow.io/resources/functions/utility#inline-function-code-expressions) to convert the total amount in the required format: `amount.toStringAsFixed(2).replaceAll(".", "");`

5. Enter the **Currency Code** to be used for the amount, for example, *INR*, *USD*, *EUR*, or *BRL*. Make sure you enter a valid currency code; otherwise, the transaction won't go through. Download the complete [list of supported currencies](https://razorpay.com/docs/build/browser/assets/images/international-currency-list.xlsx).

![Specifying amount and country code manually](https://docs.flutterflow.io/assets/images/specify-amount-and-code-manually-d3b5f57866da6b052eb72fd5706fa61d.avif)

6. With this action, you can also add some optional fields, such as **Receipt Number**, **Description**, **User Name**, **User Email**, **User Contact**, and **Timeout** (time for which the checkout dialog should remain active. By default, it is 180 seconds).

7) You can also customize the color scheme for the payment sheet using properties such as **Dialog Color, Barrier Color,** **Text Color**, **Processing Color**, **Success Color**, **Error Color,** and more.

![Customizing Razorpay payment sheet](https://docs.flutterflow.io/assets/images/customize-payment-sheet-b2c3a55da1a85dbc4cd3d088f7e65949.avif)

8. Enter an **Action** **Output Variable Name** where the payment ID would be stored on a successful transaction.

9. Now you must check if the payment was successful. You can do so by adding the [conditional action](https://docs.flutterflow.io/resources/functions/conditional-logic#conditional-actions). To do so, click the "**+**" button below the previous action tile and select **Add Conditional**.

10. On the right side (**Set Condition for Action**), 1. Select **UNSET** > **Condition** > **Single Condition**.
    2. **First Value** > **Action** **Output Variable Name**.
    3. Set the operator to **Is Set and Not Empty**.

11. Under the **TRUE** section, add an action that will be triggered if the payment is successful.

12. Under the **FALSE** section, add an action that will be triggered if payment is failed.

> **Warning:** Ensure the user is authenticated before triggering this action; otherwise, it will result in an error. You can follow the steps on [**this page**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) to set up Firebase Authentication.

##### 3. Testing

You can test Razorpay payments on Run mode, Test mode, an emulator/Simulator, or a physical device.

To test payments in Test or Run mode:

1. In your FlutterFlow project, navigate to **Settings and Integrations** > **In App Purchases & Subscriptions** > **Razorpay**.
2. Make sure the **Is Production** is disabled.
3. Make sure you have entered the correct **Test Credentials**.
4. Run your app in [Test mode](https://docs.flutterflow.io/testing/run-your-app#test-mode).
5. To test the purchase, you can try any method from [here](https://razorpay.com/docs/payments/payments/test-card-upi-details/#test-card-for-international-payments).

##### 4. Releasing to production

Once you are done testing your Razorpay integration and you are ready to go **live**, follow the steps below:

1. Complete **KYC** (or the [Activation Form](https://dashboard.razorpay.com/app/activation?ref=blog.flutterflow.io)) to access the Razorpay Live API.
2. Log into the [Razorpay Dashboard](https://dashboard.razorpay.com/?ref=blog.flutterflow.io#/access/signin) and switch to **Live Mode** on the menu.
3. From the left side menu, select **Account & Settings** > Under **Website and app settings** section, select **API keys**.
4. Click **Generate Live Key** and copy the **Key Id** and **Key Secret**. To regenerate, click on **Regenerate Live Key** and choose how you want to deactivate the old key.
5. Return to the FlutterFlow project, navigate to **Settings and Integrations** > **In App Purchases & Subscriptions** > **Razorpay**. Turn on the **Is Production**.
6. Under **Production Credentials**, paste the **Key ID** and **Key Secret** obtained in the previous step.
7. Click the **Deploy** button.
8. [Test](https://docs.flutterflow.io/testing/run-your-app#test-mode) your app.

---

### RevenueCat {#revenuecat}

*Learn how to integrate RevenueCat payments in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/payments/revenuecat

[RevenueCat](https://www.revenuecat.com/) simplifies implementing in-app purchases and subscriptions by handling all purchase validation operations.

Pub.Dev package and Limitations

The [**underlying package for RevenueCat**](https://pub.dev/packages/purchases_flutter) does not support web. Any functionality related to in-app purchases or subscriptions managed through RevenueCat will not be available on web platforms.

#### Setup RevenueCat

To set up the RevenueCat, follow these steps carefully:

1. Sign up for a new RevenueCat account [here](https://app.revenuecat.com/).

2. [Create a project](https://www.revenuecat.com/docs/getting-started/quickstart#%EF%B8%8F-create-a-project), [add your app](https://www.revenuecat.com/docs/getting-started/quickstart#%EF%B8%8F-add-an-app--platform), and ensure that you [add service credentials](https://www.revenuecat.com/docs/getting-started/quickstart#%EF%B8%8F-service-credentials) to help RevenueCat communicate with the app stores on your behalf.

3. [Create subscriptions](https://www.revenuecat.com/docs/getting-started/quickstart#%EF%B8%8F-store-setup) in the respective stores.

   1. While creating subscriptions in Google Play Console, if you see a message saying '***Your app doesn't have any in-app products yet**'* like in this picture, follow the steps below:

   ![error-while-creating-sub-in-play-console.avif](https://docs.flutterflow.io/assets/images/error-while-creating-sub-in-play-console-602d9fd2b8458217070b1dc3ad49b334.avif)

   1. Return to FlutterFlow and navigate to **Settings & Integrations >** **In App Purchases & Subscriptions >** **RevenueCat**.

   2. Switch on the **Enable RevenueCat**. For now, just enter any random string as your API Key (eg. `testkey`). We’ll update this later.

   3. Now, from the toolbar menu, click **Download APK**

   4. In the Play Console, create a [Closed testing](https://play.google.com/console/about/closed-testing/) track and create a new release.

   5. Upload your **App Bundle** or **APK**, enter the release name, and create the release.

   6. Open the **Subscriptions** tab again. It should let you manage subscriptions now.

4. [Create Products and Entitlements in RevenueCat](https://www.revenuecat.com/docs/getting-started/quickstart#%EF%B8%8F-configure-products-and-entitlements-in-revenuecat).

##### Enable RevenueCat in FlutterFlow

To enable RevenueCat in FlutterFlow, follow the steps below:

#### Displaying Subscription Details in Your App

To show in-app purchase and subscription information — such as pricing, product name, and description — within your app’s UI, you'll need to fetch these details from RevenueCat using the appropriate API or method.

Here is an example of retrieving monthly subscription details:

#### RevenueCat Actions

To manage in-app purchases and subscriptions inside your FlutterFlow app, you have to use the RevenueCat Actions. Below are the types of RevenueCat actions:

* **Paywall**
* **Purchase**
* **Restore Purchases**

##### Paywall \[Action]

This action checks whether a user has purchased an item. If not, you can open the Paywall (asking to buy an item or purchase a subscription).

Follow the steps below to see if a user is subscribed and take action accordingly.

##### Purchase \[Action]

This action allows you to purchase the item. Here’s how you add it:

##### Restore Purchases \[Action]

Using this action, you can allow users to re-activate the subscription they have already paid for. This is helpful when a user has reinstalled the app or logged in to a new device.

> **Info:** * A good practice is to allow users to manually restore the purchase by showing a button or text (maybe on a paywall/settings page).
* If you provide this option, please check [**How RevenueCat should respond to restore behavior**](https://www.revenuecat.com/docs/restoring-purchases#restore-behavior).

![adding-restore-purchase-action.avif](https://docs.flutterflow.io/assets/images/adding-restore-purchase-action-59390e74c4e0be5f07c417cfa440c923.avif)

Adding action to restore purchase

#### Testing Subscriptions

You can test your subscriptions using sandbox environments, which simulate real store behavior without incurring costs. Check out the full **[Sandbox Testing Guide](https://www.revenuecat.com/docs/test-and-launch/sandbox)** for more details.

Before going live, make sure to review **[RevenueCat’s Launch Checklist](https://docs.revenuecat.com/docs/launch-checklist)** to ensure everything is properly set up for production.

#### FAQs

I don't see offerings or products

If you're testing in the sandbox and the products are not retrieved from Apple/Google, it's likely a configuration issue. To resolve this, ensure the following:

1. The product identifier set in RevenueCat matches exactly with the store.
2. You're testing on a physical device and not a simulator.
3. The bundle ID in Xcode \[iOS] or package name \[Google] matches what's in App Store Connect or Google Play Developer console.

For iOS only, ensure that products are in the 'Ready To Submit' or 'Approved' state, you've signed your 'Paid Applications Agreement', and you're not using a StoreKit Configuration file.

For Google only, ensure that the subscription product is in the Active state, your app is published on a closed track, and you've added a tester.

See more details [here](https://community.revenuecat.com/sdks-51/why-are-offerings-or-products-empty-124).

#### Looking for other options?

If you're looking for other tools to manage in-app subscriptions, [**Adapty**](https://adapty.io/) is a solid alternative to RevenueCat — it offers advanced analytics, paywall A/B testing, and seamless integration with iOS and Android apps. You can explore the [**Adapty Library on our Marketplace**](https://marketplace.flutterflow.io/item/Mf1oFJcqngHzERZSPNA8) — it's actively maintained by the Adapty team and always kept up to date.

---

### Stripe {#stripe}

*Learn how to integrate Stripe in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/payments/stripe

Stripe helps integrate payment processing into your FlutterFlow app. Using this payment service, you can easily sell products directly inside your application and manage transactions easily.

While using Stripe as the payment provider, users can buy products using credit cards, Apple Pay, or Google Pay.

Prerequisites

Before starting to set up payments, make sure you:

1. Complete [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) for your project.
2. Enable [**Firebase Authentication**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) for your project.
3. Upgrade your Firebase project to [**Blaze Plan**](https://firebase.google.com/pricing). We use [**Firebase Cloud Functions**](https://firebase.google.com/docs/functions) to process a transaction.

#### Stripe Integration

Integrating the Stripe Payments in your app comprises the following steps:

1. [Setup Stripe payment](https://docs.flutterflow.io/integrations/payments/stripe#1-setup-stripe-payment)
2. [Apple Pay setup (optional)](https://docs.flutterflow.io/integrations/payments/stripe#2-apple-pay-setup-optional)
3. [Trigger Stripe payment](https://docs.flutterflow.io/integrations/payments/stripe#3-trigger-stripe-payment-action)
4. [Testing](https://docs.flutterflow.io/integrations/payments/stripe#4-testing)
5. [Releasing to production](https://docs.flutterflow.io/integrations/payments/stripe#5-releasing-to-production)

##### 1. Setup Stripe Payment

Setting up the Stripe payment includes acquiring the keys from your Stripe account and adding them to FlutterFlow.

> **Warning:** You should always try out payments in test mode before releasing them to your production app. Hence, the instructions below will guide you on how to get the test keys.

Follow the steps below to set up payment using Stripe:

1. Create a new **Stripe account** from [here](https://dashboard.stripe.com/register). If you already have an account, [login](https://dashboard.stripe.com/login).

2. From the dashboard page, click **Developers**.

3. Enable **Test Mode** (top right side of your screen).

4. Switch to the **API keys** tab.

5. Return to the FlutterFlow project and navigate to **Settings and Integrations** > **In App Purchases & Subscriptions** > **Stripe**. Use the toggle to **Enable Stripe Payments**.

6. Copy the **Publishable Key** and **Secret Key** from the Stripe API keys page and paste them into the respective fields inside FlutterFlow. If you are using Stripe in test mode, make sure you paste them inside the **Test Credentials** section.

7. Under the **Additional Settings**, you need to specify the following: 1. **Merchant Display Name** (*Required*): Enter a name for the merchant (you) that the user will see while performing the payment.
   2. **Merchant Country Code** (*Required*): Enter your country code. This must be the 2 digit ISO country code, such as US, IN, and AU.
   3. **Apple Merchant ID** (*Optional*): You need to enter this if you want to accept payments through Apple Pay as well. The instructions for using Apple Pay are in [this section](https://docs.flutterflow.io/integrations/payments/stripe#2-apple-pay-setup-optional).

8. Click **Deploy**.

This would deploy the Stripe payment service as a Firebase Cloud Function. Now, you are ready to trigger payments inside your app.

##### 2. Apple Pay Setup (optional)

Setting up Apple Pay comprises the following steps:

1. [Creating Apple Merchant ID](https://docs.flutterflow.io/integrations/payments/stripe#21-creating-apple-merchant-id)
2. [Uploading Payment Certificate in Stripe](https://docs.flutterflow.io/integrations/payments/stripe#22-uploading-payment-certificate-in-stripe)
3. [Adding Apple Merchant ID in FlutterFlow](https://docs.flutterflow.io/integrations/payments/stripe#23-adding-apple-merchant-id-in-flutterflow)

###### 2.1 Creating Apple Merchant ID

To create Apple Merchant ID:

1. Go to Apple's Developer Center and select [**Certificates, Identifiers & Profiles**](http://developer.apple.com/account).
2. Under **Identifiers**, select ***Merchant IDs***.
3. Click the **Add button** (+) in the upper-right corner.
4. Enter a **Description** and specify an **Identifier**. The identifier is usually defined in the format `merchant` followed by the *Package Name* of your app (you'll find it inside the ***Settings and Integrations*** page of FlutterFlow), for example, `merchant.com.domainname.appname`.
5. Click **Continue**.
6. Review the settings, and click **Register**.
7. Click **Done**.
8. Now, again under **Identifiers**, select ***Apps IDs***.
9. Select your app's identifier from the list.
10. Under **Capabilities**, check the ***Apple Pay Payment Processing*** option.
11. Click **Configure**.
12. Select the merchant account that you just created, and click **Continue**.
13. Click **Save** and then **Confirm** in the dialog.

###### 2.2 Uploading Payment Certificate in Stripe

To upload a payment certificate in Stripe:

1. First, go to the [**Settings**](https://dashboard.stripe.com/settings) page from your Stripe dashboard and select the **Payment methods** option.
2. Expand the **Apple Pay** tab under the **Wallets** section.
3. Click **Configure** to navigate to the [**Apple Pay settings**](https://dashboard.stripe.com/settings/payments/apple_pay) page.
4. Under **iOS certificates**, click **+ Add new application**.
5. This will download the **Certificate Signing Request (CSR)** file on your system and click **Continue**.
6. Select the **Merchant ID** with which you want to associate this certificate, and click **Create Certificate**.
7. Follow the instructions to **upload the CSR file** that you downloaded from Stripe.
8. To enable the certificate, click **Activate**. Then click **Download** to save it locally.
9. Go back to the Stripe page where the dialog box is displayed, and click **Continue**.
10. Upload the new certificate file.
11. Once uploaded, you should see the certificate listed under **iOS certificates**.

###### 2.3 Adding Apple Merchant ID in FlutterFlow

To add Apple Merchant ID in FlutterFlow:

1. Navigate to **Settings and Integrations** > **In App Purchases & Subscriptions** > **Stripe**.
2. Under the **Additional Settings**, enter your **Apple Merchant ID**.

![Adding Apple Merchant ID in FlutterFlow](https://docs.flutterflow.io/assets/images/adding-apple-merchant-id-d00eed09f3715d39b10df09e118fedde.png)

##### 3. Trigger Stripe Payment \[Action]

In order to initiate a payment using Stripe, you have to use the **Stripe Payment** action.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Container, Button, etc.) on which you want to add the action.
2. Select **Actions** from the Properties panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.
3. Click on the **+ Add Action**.
4. On the right side, search and select the **Stripe Payment** (under *Integrations*) action.
5. Enter or use a variable for specifying the total payment amount under the **Amount** section. The value should be specified in the currency's smallest unit. For example, *$24.99* should be passed as *2499* (as a round-off integer, otherwise it would be automatically rounded), whereas *¥1925* can be simply passed as *1925*. For more information check out [this page](https://stripe.com/docs/currencies#zero-decimal).
6. Enter the **Currency Code** to be used for the amount, for example, *USD*, *EUR*, *BRL*. Make sure you enter a valid currency code otherwise, the transaction won't go through.
7. Next, you need to specify the **Customer Email** (required) and **Customer Name** (optional) to be used for the transaction. You can either use a variable or enter the value for them. If you are using authentication, these two values can be retrieved from the ***Authenticated User**.*
8. Specify a **Description** of the purchase for both your and the user's record.
9. To enable **Google Pay** or **Apple Pay** as the payment method, turn on the respective toggle. To use Apple Pay, you have to set up a *Merchant ID* by following the steps [here](https://docs.flutterflow.io/integrations/payments/stripe#2-apple-pay-setup-optional).
10. Select the **Payment Sheet Theme** among ***System Default***, ***Light Theme***, or ***Dark Theme**.*
11. Specify the **Primary Button Color** and **Button Text Color** to be used on the payment dialog.
12. Enter an **Output Variable Name** where the payment ID would be stored on a successful transaction. Later, you can use this variable elsewhere inside the page or pass it to a different page of the app.

> **Warning:** Make sure the user is authenticated before triggering the Stripe Payment Action. Otherwise, it will result in an error.

##### 4. Testing

You can test Stripe payments on mobile and the Web before deployment. To do that:

1. Go to the FlutterFlow project and navigate to **Settings and Integrations** > **In App Purchases & Subscriptions** > **Stripe**.
2. Make sure the **Is Production** is disabled.
3. Make sure you have entered the correct **Test Credentials,** such as **Publishable Key** and **Secret Key**.
4. [Download](https://docs.flutterflow.io/flutterflow-cli/exporting) and [run](https://docs.flutterflow.io/testing/run-your-app) your project..
5. To test the purchase, you can use any of these [basic test card numbers](https://stripe.com/docs/testing#cards).

##### 5. Releasing to Production

Before you release the app to production, complete the following steps:

1. [Login](https://dashboard.stripe.com/login) to your Stripe account and navigate to the **Developers** page.
2. Disable the **Test Mode** (top right side of your screen).
3. Select **API keys** from the left menu and copy the **Publishable Key** and **Secret Key**.
4. Return to FlutterFlow; under the **Production Credentials** section, paste the **Publishable Key** and **Secret Key**.
5. To deploy the Android app, follow the [Google Play Store Deployment](https://docs.flutterflow.io/deployment/google-playstore-deployment) guide.
6. To deploy the iOS app, follow the [App Store Deployment](https://docs.flutterflow.io/deployment/apple-app-store-deployment) guide.

***

#### FAQs

I am getting "Error: Unknown error occurred"

When encountering the "Error: Unknown error occurred" message, consider these troubleshooting steps:

1. **Stripe Settings Adjustment**: In FlutterFlow's Stripe settings, verify the Merchant country code is a 3-digit code, like "USA" instead of "US". If needed, remove previously deployed functions in the Firebase console and redeploy them after updating the country code.
2. **User Authentication Requirement**: Stripe payments require an authenticated user session. Ensure you're attempting the Stripe action after a user has successfully logged in to the app.
3. **Cloud Functions Permissions**: Check that your cloud functions have the **Cloud Functions Invoker** permission set for **allUsers** in the Google Cloud console. To do this, go to the Cloud Console, directly search for the **initStripePayment** function, open the function, switch to the **Permissions** tab, and confirm the permissions status. This permission is typically assigned by default, but it's good practice to double-check.

![unknown-error-occured](https://docs.flutterflow.io/assets/images/unknown-error-occured-b03b43f1bf942dbbd98e2685f95a4ebd.avif)

---

### Algolia {#algolia}

*Learn how to implement algolia search functionality in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/integrations/search/algolia-search

[Algolia](https://www.algolia.com/) is a powerful search-as-a-service platform that provides lightning-fast and highly relevant search capabilities. Integrating Algolia into your FlutterFlow app allows you to implement real-time search functionality, making it easier for users to find relevant information within your app.

Prerequisites

* Algolia integration in FlutterFlow is tied exclusively to Firestore collections. This means you must [**setup Firebase**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) to sync data from Firestore into Algolia for searching.
* **Upgraded** your Firebase project to the [**Blaze Plan**](https://firebase.google.com/pricing) for the Algolia Firebase Extension to work.
* Have at least one **Firestore Collection** on which you want to perform the search queries.

#### Algolia integration

Follow the steps below to integrate Algolia in your FlutterFlow apps:

##### Setup Algolia

Setting up Algolia involves creating an application, defining an index, and generating an API key with the necessary permissions. Here are the steps in detail:

###### Step 1: Create an Algolia Application

Login to [Algolia](https://www.algolia.com/). If you don’t have an account, sign up for a free account [here](https://www.algolia.com/users/sign_up). During registration, fill in the required details and select a **data center region**. After signing up, you’ll be presented with an **import data screen**, but you can skip this for now (see button at the top right).

Next, name your application by navigating to **Settings > Applications** in the Algolia dashboard. By default, you should see an application called **"(unnamed application)"**. Click the three-dot button beside it, select **Rename**, enter a name for your application, and click **Save**.

###### Step 2: Create an Index

An **index** in Algolia is like a **database table** where your searchable data is stored. To create an index, go to the **Search** section in the left menu, then select **Index**. Click on **Create Index**, and **provide an exact name that corresponds to the Firestore collection** on which you intend to perform the search queries.

###### Step 3: Generate an API Key

To integrate Algolia, you need an **API key** with the correct permissions. In the Algolia dashboard, go to **Settings > API Keys > All API Keys**, then click **New API Key**. Under **Indices**, select the index you created in the previous step. In the **ACL (Access Control List)** field, include these permissions: `addObject`, `deleteObject`, `listIndexes`, `deleteIndex`, `editSettings`, and `settings`. Click **Create**, then copy the generated API Key and keep it handy—you’ll need it next to [configure Algolia Firebase Extension](https://docs.flutterflow.io/integrations/search/algolia-search#sync-firebase-data).

##### Sync Firebase Data

To sync your data from Firebase to Algolia, you must install [Algolia Firebase Extension](https://extensions.dev/extensions/algolia/firestore-algolia-search). It allows you to seamlessly connect **Cloud Firestore** with **Algolia**, ensuring that any updates, additions, or deletions in Firestore are instantly reflected in your search index.

Follow these steps to set up the official Firebase extension for Algolia search:

1. **Open Firebase Extensions:** Go to the [**Search Firestore with Algolia**](https://extensions.dev/extensions/algolia/firestore-algolia-search) extension page, then click **Install in Firebase Console**. Choose your project to proceed with the installation.

2. **Update Extension Instance ID (Optional)**: An extension instance ID uniquely identifies each installed instance of an extension within your Firebase project. This ID is used to manage the extension instance, including updating or uninstalling it.

3. **Review Billing and Usage:** A summary of billing details will appear. After reviewing, click **Next**.

4. **Review APIs Enabled and Resources Created:** This extension automatically creates some resources like Cloud Functions and APIs to interact with Algolia. Check the listed resources, then click **Next**.

5. **Review Access Granted to this Extension:** You'll be presented with a list of specific services and resources that the extension needs access to. Review the permissions, then click **Next**.

6. **Configure Extension:** During installation, you'll be prompted to provide the following details.

   * **Collection Path**: Specify the name of the Firestore collection you want to index for search.

   * **Indexable Fields (Optional)**: You can leave this blank to index all fields or manually list fields you want indexed.

   * **Force Data Sync (Optional)**: You can enable this to ensure that the extension performs an additional read operation from Firestore before processing and sending data to Algolia. It guarantees that the most recent and accurate data is indexed.

   * **Algolia Index Name**: The name of the index you created (in [step 2](https://docs.flutterflow.io/integrations/search/algolia-search#step-2-create-an-index)) in Algolia Setup.

   * **Algolia Application ID**: You can go to the Algolia dashboard page and check its URL, `https://www.algolia.com/apps/<applicationid>`. Copy the `application_id` and enter it in the field.

   * **Algolia API Key**: Paste the API key you created (in [step 3](https://docs.flutterflow.io/integrations/search/algolia-search#step-3-generate-an-api-key)) during the Algolia Setup and hit **Create Secret** button.

   * **Full Index Existing Documents**: Set this to **Yes** to import the existing data from the Firestore collection into the Algolia index.

   * **Cloud Functions Location**: Choose the region for deploying the Cloud Function.

7. **Install**: Click **Install extension** to finalize. Allow a few moments for the extension to install completely before proceeding to the next steps.

##### Choose Searchable Fields

To limit the fields used for searching in Algolia, you can specify which attributes should be indexed. From the **Algolia dashboard**, go to **Search > Index > Configuration** and click **+ Add a Searchable Attribute**. Enter the field name you want Algolia to use and repeat this step for additional fields.

Once done, click **Review and Save Settings**, then confirm by clicking **Save Settings** in the dialog. Algolia will now search only within the specified fields in your app.

##### Configure in FlutterFlow

To integrate **Algolia Search** into your FlutterFlow app, go to **Settings and Integrations > Algolia** and enable it. Enter the **Application ID**, which you can find in your Algolia dashboard URL (`https://www.algolia.com/apps/<applicationid>`). Next, copy the **Search API Key** from **Algolia Settings > API Keys** and paste it into FlutterFlow. Finally, under **Indexed Collections**, select the Firestore collections you want to make searchable.

Here’s exactly how you do it:

#### Using Algolia Search

You can use Algolia Search in your app using two methods:

* [**Algolia Search Action**](https://docs.flutterflow.io/integrations/search/algolia-search#algolia-search-action): This method is useful when the user enters a search term in a TextField and then interacts with a widget, such as tapping a button, to initiate the search.
* [**Backend Query**](https://docs.flutterflow.io/resources/backend-query/algolia-search-query): This approach automatically searches or refreshes search results as the user types in the TextField. It leverages the **Update Page On Text Change** property to dynamically update results.

##### Algolia Search \[Action]

To configure the **Algolia Search** action in FlutterFlow, begin by selecting the widget that will trigger the search, such as an **IconButton**. In the **Properties Panel**, navigate to the **Actions** tab and click on **+ Add Action**, choose the appropriate gesture, like **On Tap**. Search and select the **Algolia Search** action.

Next, configure the search parameters: for **Firebase Collection**, select the Firestore collection you intend to search; for **Search Term**, choose **From Variable** and select the TextField's value (e.g., **Widget State > \[Your TextField]**); and specify the optional **Max Results** to determine the number of search results.

Here’s an example of how you can add Algolia Search Action:

#### FAQs

Does Algolia work with other data sources like Supabase?

By default, FlutterFlow’s built-in Algolia integration only supports Firestore as the data source. If you need to use Algolia with another database—such as Supabase—you would have to manage that integration via [**custom code**](https://docs.flutterflow.io/concepts/custom-code). However, out of the box, FlutterFlow currently does not offer an Algolia search on databases beyond Firestore.

---

### Simple Search {#simple-search}

*Learn how to implement simple search functionality in your FlutterFlow app to search local data on a device.*

**Source:** https://docs.flutterflow.io/integrations/search/simple-search

The simple search allows you to search the data present locally on a device. For example, you could search from the list of strings (stored in a variable) and from the Firestore collection and documents already retrieved on the user's device (displayed on the screen).

When to use Simple Search vs Algolia

We advise using a simple search only for the smaller Firestore collection (with limited records). Otherwise, it can be slow and/or expensive. For a more extensive collection, consider using the [**Algolia search**](https://docs.flutterflow.io/integrations/search/algolia-search).

#### Types of Simple Search

There are three types of search you can add to the page:

* **Firestore collection**: To search from the Firestore collection.
* **Documents**: To search from the list of documents stored in a variable.
* **Strings**: To search from the list of strings stored in a variable such as app or page state variable.

#### Simple Search \[Action]

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to define the action.

2. Select **Actions** from the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.

   1. Click on the **+ Add Action**.

   2. On the right side, search and select the **Simple Search** action.

   3. Select the **Search Type** among the **Firestore Collection**, **Documents**, and **Strings**.

   4. If you select the **Firestore Collection**:

      1. Set the **Collection** to the one that you want to search from.
      2. **Select Searchable Fields** to the field that you want to perform the search on.

   5. If you select the **Documents**:

      1. Set the **Source** to the variable that holds the list of documents. For example, the result of the query at a top-level widget such as **Page** or **Column**
      2. **Select Searchable Fields** to the field that you want to perform the search on.

   6. If you select the **Strings**:

      1. Set the **Source** to the variable that holds the list of strings (e.g., app or page state variable).

   7. Inside the **Search Term** section, set **Widget State > TextField** (where users enter a search term).

---

### Supabase Setup {#supabase-setup}

*Learn how to set up Supabase in your FlutterFlow app for database and authentication functionalities.*

**Source:** https://docs.flutterflow.io/integrations/supabase/setup

You can either use [Supabase OAuth](https://docs.flutterflow.io/integrations/supabase/setup#connect-with-supabase-oauth) for a quick and secure setup or [connect using API Keys](https://docs.flutterflow.io/integrations/supabase/setup#connect-with-supabase-api-keys) for self-hosted setups.

#### Connect with Supabase OAuth

To connect with Supabase using the OAuth method, follow the steps below:

1. Open **Settings & Integrations** and go to the **Supabase** section.
2. Select the **Connect with Supabase OAuth** tab.
3. Click **Connect to Supabase** to start the connection flow.
4. Choose your Supabase organization and authorize access.
5. After authorization, either select an existing Supabase project or click **Create New Project** to make a new one.
6. If creating a new project, enter the project name and region, then click **Create**.
7. Copy and save the database password, since it will not be shown again.
8. Click **Done** to finish the setup.
9. Once connected, you can view and manage the Supabase project from the Supabase settings, switch projects, or open it in a new browser tab.

> **Tip:** After [**creating**](https://docs.flutterflow.io/integrations/supabase/setup#create-tables-in-supabase) or updating tables in your Supabase database, make sure to click **Get Schema** to refresh and sync the latest table structure in FlutterFlow.

#### Connect with Supabase API Keys

To connect using Supabase API Keys, you will manually link your Supabase project with FlutterFlow by providing the required credentials.

> **Warning:** Please note that this method is only intended for **self-hosted Supabase databases**.

1. First, create a project in Supabase from the Supabase dashboard.
2. In your Supabase project, navigate to [Project Settings > API](https://app.supabase.com/project/cwnjvtflygqlpxdpsujv/settings/api). Copy the **Project URL**.
3. Return to FlutterFlow, navigate to **Settings and Integrations > Integrations > Supabase**. Turn on the toggle (i.e., enable Supabase) and paste the **API URL**.
4. Similarly, from the Supabase [API section](https://app.supabase.com/project/cwnjvtflygqlpxdpsujv/settings/api), copy the **anon key** (under **Project API keys**) and paste it inside the **FlutterFlow > Settings and Integrations > Integrations > Supabase > Anon Key.**
5. Click on the **Get Schema** button. This will show the list of all tables with their schema (structure) created in Supabase.
6. (Optional) If you have defined an *Array* for any *Column Data Type* in Supabase, you must set its type here. To do so, tap the "**Click to set Array type**" and choose the right one.

> **Tip:** After [**creating**](https://docs.flutterflow.io/integrations/supabase/setup#create-tables-in-supabase) or updating tables in your Supabase database, make sure to click **Get Schema** to refresh and sync the latest table structure in FlutterFlow.

#### Create Tables in Supabase

If you haven't already, [create table(s)](https://supabase.com/docs/guides/database/tables#creating-tables). If you're just getting started, you can uncheck the **Enable Row Level Security (**[**RLS**](https://supabase.com/docs/guides/auth/row-level-security)**)** option to remove any restrictions on accessing the table data.

Note

It's important to note that while disabling Row Level Security (RLS) can be useful for testing and development purposes, **it's recommended that you re-enable RLS** and implement an access policy that aligns with your app's requirements before deploying your app.

Here's an example of creating an "assignments" table with a [foreign key relationship](https://supabase.com/docs/guides/database/tables#joining-tables-with-foreign-keys) from `created_by` column to `public.users.id` with `on delete cascade`. This ensures that if a user is deleted from the "public.users" table, any data related to that user stored in your "assignments" table will also be deleted.

> **Note:** To use Supabase authentication, you must [**create a "users" table**](https://docs.flutterflow.io/integrations/authentication/supabase/initial-setup#1-creating-a-users-table).

---

