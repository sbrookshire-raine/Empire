# FlutterFlow Documentation — Complete Guide (Part 6 of 7: Deployment, Testing, Marketplace & Exporting Code)

> **Note for NotebookLM:** This is one part of a multi-file Markdown export of the official FlutterFlow documentation, cleaned and reorganized for use as a NotebookLM source set to build a structured FlutterFlow learning plan. Import all parts together as separate sources in the same NotebookLM notebook.

- **Source:** https://docs.flutterflow.io (crawled via https://docs.flutterflow.io/llms-full.txt)
- **This file's page count:** 23
- **Total pages across the full guide (all 7 parts):** 369
- **Date generated:** 2026-07-18
- **Part:** 6 of 7 — Deployment, Testing, Marketplace & Exporting Code
- **Other parts in this guide:**
  - Part 1: Fundamentals, Account, CLI & Builder UI (`FlutterFlow_Guide_01_Fundamentals_and_Platform.md`)
  - Part 2: Core Concepts: UI Building, Actions, Animations, Navigation, Custom Code (`FlutterFlow_Guide_02_CoreConcepts.md`)
  - Part 3: Widgets Reference (`FlutterFlow_Guide_03_WidgetsReference.md`)
  - Part 4: Resources: Data, Backend Query, Forms, Functions & Projects (`FlutterFlow_Guide_04_ResourcesDataAndLogic.md`)
  - Part 5: Integrations: Auth, Firebase, Supabase, Payments, Maps, Search, Ads (`FlutterFlow_Guide_05_Integrations.md`)
  - Part 7: Troubleshooting Guides (`FlutterFlow_Guide_07_Troubleshooting.md`)

## Table of Contents

**Deployment**

- [Apple App Store Deployment](#apple-app-store-deployment)
- [Deploy for Development Environments](#deploy-for-development-environments)
- [Deploy from GitHub](#deploy-from-github)
- [Google Play Store Deployment](#google-play-store-deployment)
- [Pre-checks Before Publishing](#pre-checks-before-publishing)
- [Web Publishing](#web-publishing)

**Exporting Code**

- [Push to GitHub Repo](#push-to-github-repo)

**Marketplace**

- [Adding & Purchasing Items](#adding-purchasing-items)
- [Creators Hub](#creators-hub)
- [Copyright (DMCA) Process](#copyright-dmca-process)
- [Creator FAQs](#creator-faqs)
- [Legal Guidelines for Creators](#legal-guidelines-for-creators)
- [Navigating External Licenses](#navigating-external-licenses)
- [FlutterFlow Marketplace Review Dispute Guidelines](#flutterflow-marketplace-review-dispute-guidelines)
- [Item Submission Criteria](#item-submission-criteria)
- [Submitting Item for Review](#submitting-item-for-review)
- [Refund Policy](#refund-policy)
- [Submitting Feedback for Items](#submitting-feedback-for-items)

**Testing**

- [Automated Tests](#automated-tests)
- [Development Environments](#development-environments)
- [Local Run](#local-run)
- [Run your App](#run-your-app)
- [Test Pilot](#test-pilot)

---

## Deployment

### Apple App Store Deployment {#apple-app-store-deployment}

*Learn how to seamlessly deploy your apps to the Apple App Store using FlutterFlow.*

**Source:** https://docs.flutterflow.io/deployment/apple-app-store-deployment

FlutterFlow allows you to deploy your apps directly to the App Store from within the platform. This guide covers all the necessary prerequisites, a step-by-step deployment process, and common troubleshooting tips.

Prerequisites

* Create an [**Apple account**](https://appleid.apple.com/account?appId=632\&returnUrl=https%3A//developer.apple.com/account/).
* [**Purchase an Apple Developer membership**](https://developer.apple.com/programs/enroll/). Learn more about the program and enrollment process [here](https://developer.apple.com/programs/).
* Set an App Launcher Icon for your app under **Settings & Integrations > General > App Assets**. **Note**: The launcher icon cannot be transparent or contain an alpha channel.
* It's recommended to test your app on a real device before deployment. Follow [**these instructions**](https://docs.flutterflow.io/testing/local-run) to test your app locally.

#### Deploy to App Store

The App Store deployment involves the following steps:

##### 1. Create a Bundle Identifier

A **Bundle Identifier (ID)** is a **unique string** that identifies your app within the Apple ecosystem, typically formatted in reverse domain name notation like `com.example.myapp`.

To create a Bundle ID, visit the [**Certificates, IDs & Profiles**](https://developer.apple.com/account/resources/identifiers/list) page, add a new **App ID**, and provide these details:

1. **Bundle ID:** Copy the **Package Name** from FlutterFlow.
2. **Description:** Add a brief description of your app.
3. **Capabilities:** Select the necessary app capabilities. Ensure you select **Push Notifications** if your app uses them, and **Sign In with Apple** if your app includes that feature.

##### 2. Add New App

[App Store Connect](https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-homepage) is the platform used for submitting apps, managing app metadata, and much more. To add a new app, open the [App Store Connect](https://appstoreconnect.apple.com/) and then follow the official steps outlined [here](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app).

##### 3. Add Apple App ID to FlutterFlow

An App ID is used by Apple to identify your app and associate it with your development team.

To add your App ID to FlutterFlow, go to **[App Store Connect](https://appstoreconnect.apple.com/) > My Apps**, copy your **Apple ID** from **App Information**, and paste it into the **App ID** field in **FlutterFlow > Settings & Integrations > Mobile Deployment > App Store**.

##### 4. Generate API key and add to FlutterFlow

To generate your API Key, go to [**App Store Connect**](https://appstoreconnect.apple.com/) > **Users and Access** > **Integrations > [Team Keys](https://appstoreconnect.apple.com/access/integrations/api)**. If you haven't added a key before, you will see a **Request Access** button. For further details, watch a [demo](https://youtu.be/L2BpgVog4so?si=yS9r_PBeORgd6Uhp\&t=240) here.

Generate a new API key by selecting **Add (+)**, entering a name, and assigning the **App Manager** role. Once the key is generated, download it and upload it to **FlutterFlow** under **Settings & Integrations > App Settings > Mobile Deployment > App Store > Private Key**.

##### 5. Add issuer ID to FlutterFlow

Copy the **Issuer ID** from [**App Store Connect**](https://appstoreconnect.apple.com/) by navigating to **Users and Access** > **Integrations > [Team Keys](https://appstoreconnect.apple.com/access/integrations/api)**, and then paste it into the **Issuer ID** field under **App Store settings** in FlutterFlow.

##### 6. Add Key ID to FlutterFlow

Return to **[App Store Connect](https://appstoreconnect.apple.com/) >** **Users and Access** > **Integrations > [Team Keys](https://appstoreconnect.apple.com/access/integrations/api).** Find the row for the API Key you generated [here](https://docs.flutterflow.io/deployment/apple-app-store-deployment#4-generate-api-key-and-add-to-flutterflow), select **Copy Key ID,** and then paste it into the **Key ID** field under **App Store settings** in FlutterFlow.

##### 7. Deploy

To deploy your app from FlutterFlow, go to **Settings & Integrations > App Settings > Mobile Deployment > App Store** and click **Deploy To App Store**. Once deployed, you will receive an email from App Store Connect that a new build has been added to your app.

![deploy-to-appstore.avif](https://docs.flutterflow.io/assets/images/deploy-to-appstore-5aa199888f377af25dcdcfb05c5c4102.avif)

> **Info:** * Every time you deploy, we'll auto increment the **Build Number** (i.e., version code in Android) to ensure that each release is identifiable. If needed, you can update the *App Version* and *Build Number* yourself.
* If another deployment is already in progress, deploying a new build will cancel the previous one.
* It may take a few minutes for the request to process. Once completed, the status will be updated to **Submitted**.

> **Tip:** If you prefer to manage your deployment process outside of FlutterFlow, such as integrating with your own CI/CD pipeline, or if you want more control over versioning and custom code management directly on GitHub. You also have the option to [**Deploy apps from your GitHub repository**](https://docs.flutterflow.io/deployment/deploy-from-github).

##### 8. Submit your app for App Store approval

From [**App Store Connect**](https://appstoreconnect.apple.com/), select **My Apps** and choose your app. Select **Prepare for Submission**, add the app assets and metadata, and then click **Add for Review**.

![add-for-review.avif](https://docs.flutterflow.io/assets/images/add-for-review-e313a116a9022d701e69edc01833f304.avif)

Your app will now be reviewed by Apple. For additional information on Apple's review guidelines, please see [this link](https://developer.apple.com/app-store/review/guidelines/).

***

#### Video guide

Watch this video if you prefer watching a video tutorial.

[Sharing a Project with a User](https://www.youtube.com/embed/4GFMsYep_S0)

***

#### FAQs

Invalid App Store Icon. The App Store Icon in the asset catalog in 'Runner.app' can't be transparent nor contain an alpha channel.

You need to update your App Launcher Icon (under Settings & Integrations --> General) with an image that isn't transparent and/or doesn't contain an alpha channel.

After submitting my iOS app to the App Store, I am getting an 'ITMS-91053: Missing API declaration' issue. What should I do?

Apple requires that apps using certain APIs have a Privacy Manifest file that declares the [**reason for using the API**](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api). Apple will begin requiring this file for App Store approval on May 1, 2024.

Most packages that FlutterFlow uses already have a Privacy Manifest created by the package author or FlutterFlow team. However, there may be some cases where packages don't have the necessary privacy manifest needed.

Similarly, if you have written custom code that calls these APIs directly or uses a package that calls the APIs, you must ensure that your app has the required manifest file.

Here are the steps you can take to resolve this issue:

1. See if the custom package you use is listed [here](https://developer.apple.com/support/third-party-SDK-requirements/); ensure to use the latest version if you are using any of these.

2. If unsure which package is using protected APIs, you may be able to use a tool like [this](https://github.com/crasowas/app_store_required_privacy_manifest_analyser) to identify them. Once identified, update to the latest versions, as the package author may have addressed compliance issues. 1. To verify, look into the package's changelog or source code for a `PrivacyInfo.privacy` file, which indicates compliance (examples [here](https://github.com/fluttercommunity/plus_plugins/blob/main/packages/share_plus/share_plus/ios/PrivacyInfo.xcprivacy) and [here](https://github.com/flutter/packages/blob/main/packages/url_launcher/url_launcher_ios/ios/Resources/PrivacyInfo.xcprivacy)).
   2. If the current package hasn’t resolved the issue, consider using an alternative package that complies, or contact the package's maintainer for a fix.

3. If you have written a custom iOS code that is accessing the APIs: 1. In FlutterFlow, navigate to **Settings & Integrations > App Settings > Privacy Manifest Configuration**.
   2. Activate the necessary API reasons and select the appropriate reasons from the dropdown. A detailed explanation of each API reason can be found [here](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api).

![privacy-manifest-configuration](https://docs.flutterflow.io/assets/images/privacy-manifest-configuration-519c68fd856e18c19a57e7c2e76147ab.avif)

---

### Deploy for Development Environments {#deploy-for-development-environments}

*Learn how to deploy your apps for development environments.*

**Source:** https://docs.flutterflow.io/deployment/deploy-for-environments

FlutterFlow provides flexibility in configuring deployment settings for different [environments](https://docs.flutterflow.io/testing/dev-environments), allowing you to manage your app builds for both mobile and web apps.

With deployment settings tailored to each environment, you can test, isolate app functionality, and optimize for various use cases without impacting production builds.

#### Mobile Deployment

You can configure and publish environment-specific builds of your app for both iOS and Android platforms, allowing each build to coexist and function independently for different environments.

To set up deployment for different environments, go to **Settings & Integrations > App Settings > Mobile Deployment**, and select the desired environment from the **Current Environment** dropdown on the right side.

Now, to submit an environment-specific build to the App Store and Play Store, you must have unique package names representing each environment. To set this up, go to **Settings & Integrations > General > App Details > Package Name**, select the **Current Environment** from the dropdown (on the right), and specify the package name for that environment. This ensures that when you switch environments, the package name changes and you can submit separate builds to the App Store and Play Store.

For example, in an ecommerce app, you can set package names such as `io.flutterflow.ecommerceflow.dev` for the development environment and `io.flutterflow.ecommerceflow.staging` for the staging environment.

Once this setup is complete, you can deploy to [App Store](https://docs.flutterflow.io/deployment/apple-app-store-deployment) and [Play Store](https://docs.flutterflow.io/deployment/google-playstore-deployment) as usual.

For iOS

* You can publish your apps as unlisted on the App Store to allow different builds without public exposure.
* You must configure provisioning profiles, certificates, and App IDs unique to each environment to ensure secure and streamlined publishing.

#### Web Deployment

Web deployment in FlutterFlow provides you with the ability to configure the entire web deployment for each environment, including custom URLs, page titles, metadata, and deployment history.

To set up deployment for different environments, navigate to **Settings & Integrations > App Settings > Web Deployment**, and select the desired environment from the **Current Environment** dropdown on the right side. Then, set a new **Site URL** for the selected environment and [publish](https://docs.flutterflow.io/deployment/web-publishing) your app as usual.

![deploy-web-app-for-environments.avif](https://docs.flutterflow.io/assets/images/deploy-web-app-for-environments-65e46cce24b61a07d205e9e703aa5b87.avif)

---

### Deploy from GitHub {#deploy-from-github}

*Learn how to deploy your apps directly from GitHub branch.*

**Source:** https://docs.flutterflow.io/deployment/deploy-from-github

If your FlutterFlow project is connected to a GitHub repository, the generated code can be pushed to GitHub, giving you full control over your project’s code. Then, you can deploy your app directly from the same repository, rather than deploying through FlutterFlow.

Deploying from GitHub is particularly beneficial when:

* You have written custom code that cannot be managed directly in FlutterFlow, such as features that require advanced Flutter functionality.
* You want to manage the source code in an external GitHub repository for better version control.
* You want to automate the process of deploying your app directly from GitHub to the Play Store or App Store after modifying the code.
* You want to deploy from a specific branch of your GitHub repository.

#### Steps to Deploy

To deploy from a GitHub repository:

1. If you haven't already added your project to the GitHub repository, follow the instructions provided [here](https://docs.flutterflow.io/exporting/push-to-github#connect-a-github-repo).
2. In FlutterFlow, go to **Settings & Integrations > App Settings > Mobile Deployment.**
3. Locate the **Deployment Source** section and click the arrow icon on the right to expand it.
4. Turn on the toggle for **Use GitHub repo: \[your repo URL]**.
5. Enter the branch name of your repository that contains the code you want to deploy. Ensure the branch name is correct.
6. Click the **Deploy to App Store** or **Deploy to Play Store** button, depending on your desired platform for deployment.

![deploy-from-github](https://docs.flutterflow.io/assets/images/deploy-from-github-9e0534ff4e93223c90e2332a4c195c6f.png)

important

When deploying from your GitHub branch, you will need to manage the app versioning manually. This is done through the `pubspec.yaml` file. For example, to set the version to **1.1.0** and the build number to **2**, you can use the format: `version: 1.1.0+2`.

![update-version.avif](https://docs.flutterflow.io/assets/images/update-version-02789a60b90d0089cf1b990c1d858a68.avif)

#### FAQs

I am having an issue while Deploying from a GitHub branch. Error: *You uploaded an APK or Android App Bundle that was signed in debug mode. You need to sign your APK or Android App Bundle in release mode.*

If you are experiencing problems deploying or uploading to the Google Play Store from a Github branch, check to make sure your `build.gradle` file is correct.

1. Open your `android/app/build.gradle` file.

2. Ensure your file has these lines of code:

   ```
   def keystoreProperties = new Properties()
   def keystorePropertiesFile = rootProject.file('key.properties')
   if (keystorePropertiesFile.exists()) {
       keystoreProperties.load(new FileInputStream(keystorePropertiesFile))
   }
   signingConfigs {
       release {
           keyAlias keystoreProperties['keyAlias']
           keyPassword keystoreProperties['keyPassword']
           storeFile keystoreProperties['storeFile'] ? file(keystoreProperties['storeFile']) : null
           storePassword keystoreProperties['storePassword']
       }
   }
   ```

3. Newer Flutterflow code will automatically have these lines added. If yours doesn't, you can push it to your `flutterflow` branch on GitHub and merge in the changes or add them like so:

   ![deploy-github-issue](https://docs.flutterflow.io/assets/images/deploy-github-issue-3dec70eb9ae21fab4f205ab76c8fedc1.avif)

4. Lastly, change `debug` (shown in the red box above) to `release` before deploying.

---

### Google Play Store Deployment {#google-play-store-deployment}

*Learn how to seamlessly deploy your apps to the Google Play Store using FlutterFlow.*

**Source:** https://docs.flutterflow.io/deployment/google-playstore-deployment

FlutterFlow allows you to seamlessly deploy your apps directly to the Google Play Store, all from within the builder. This guide provides comprehensive instructions on prerequisites, step-by-step process for deployment, advanced settings, and troubleshooting common issues.

Prerequisites

1. Register for a [**Google Play Developer account**](https://play.google.com/console/u/0/signup).
2. [**Test your application**](https://docs.flutterflow.io/testing/local-run) on a real device.
3. Confirm the [**app details**](https://docs.flutterflow.io/resources/projects/settings/general-settings#app-details). Especially the package name, which can't be changed after your app is deployed.
4. Set an [**App Launcher Icon**](https://docs.flutterflow.io/resources/projects/settings/general-settings#launcher-icon). The App Launcher icon can't be transparent or contain an alpha channel.

#### Deploy to Google Play Store

Deploying to Google Play Store comprises of the following steps:

1. [Creating an app on Google Play Store](https://docs.flutterflow.io/deployment/google-playstore-deployment#1-creating-an-app-on-google-play-store)
2. [Set up your app](https://docs.flutterflow.io/deployment/google-playstore-deployment#2-set-up-your-app)
3. [Adding service account credentials](https://docs.flutterflow.io/deployment/google-playstore-deployment#3-adding-service-account-credentials)
4. [Deploy to Google Play Store](https://docs.flutterflow.io/deployment/google-playstore-deployment#4-deploy-to-google-play-store)

##### 1. Creating an app on Google Play Store

Follow the steps below to create an app on Google Play Store:

1. Open the [Google Play Console](https://play.google.com/console).
2. Click on the **Create app** button at the top right side of your screen.
3. Enter the **App name**, select the app type, and choose whether the app is **Free** or **Paid**.
4. Accept the **Declarations**.
5. Click **Create app** at the bottom.

[Sharing a Project with a User](https://www.loom.com/embed/f7060474fd3741cbbff64e885751d1ed?sid=75eb6e5e-7bcf-4ed8-9480-42bfc46ef622)

##### 2. Set up your app

To successfully deploy the app, you must fill in all the app details required by the Google Play Store.

To proceed, navigate to the **Set up your app** section within the newly created app. Expand the **View tasks** section. Then, click on each task and fill in the necessary app information.

![setup-your-app](https://docs.flutterflow.io/assets/images/setup-your-app-5e3b2b145f130052273944cdbfc5b97d.avif)

##### 3. Adding service account credentials

Adding Service Account Credentials to FlutterFlow helps you publish your apps on Google Play.

###### 3.1 Creating a Service Account

To create the Service Account, you can follow the instructions from [here](https://developers.google.com/android-publisher/getting_started). To help you get started quickly, here are the exact steps you need to follow:

1. If you haven't set up Firebase in your app, you'll need to [create a Google Cloud Project](https://developers.google.com/android-publisher/getting_started#creating).

2. Then, head over to the [Google Play Developer API page](https://console.developers.google.com/apis/api/androidpublisher.googleapis.com/) in Google Cloud Console and click **Enable**.

   ![enable-play-api](https://docs.flutterflow.io/assets/images/enable-play-api-58a30239911273105a4d83c27e046b2f.avif)

3. In Google Cloud Console, go to [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts), click + **CREATE SERVICE ACCOUNT,** and follow the steps as per in the visual below.

[Sharing a Project with a User](https://www.loom.com/embed/221b44ff1f21449191ad400c368c98c1?sid=1d157ef4-8255-45f9-b313-b19c94fc4323)

4. On the right side of the newly created service account, click the action menu (three dots) icon and select **Manage keys**. Then, click **ADD Key > Create new key > select JSON > CREATE**. Keep the downloaded file at a safe place.

   [Sharing a Project with a User](https://www.loom.com/embed/ddacc773f607466dacda84d2bc5a65d3?sid=99860215-0e37-412d-bfb3-5f04791a7c11)

5) Now, return to the Google Play Console and follow the steps below: 1. Go to the [Users & Permissions](https://play.google.com/console/users-and-permissions) page.

   2. Click **Invite new users**.

   3. Put the email address for your service account in the email address field and grant the necessary rights to perform actions: * "Edit and delete draft apps"
      * "Release to production..."
      * "Release apps to testing tracks"
      * "Manage testing tracks and edit tester lists"

   4. Click **Invite user**.

[Sharing a Project with a User](https://www.loom.com/embed/c0df78e3c850419787559a399ca5eebd?sid=429452db-f87d-46af-8d80-c6d64d400dc6)

###### 3.2 Uploading service account credentials to FlutterFlow

To upload the service account credentials on FlutterFlow:

1. Return to FlutterFlow, navigate to **Settings & Integrations > App Settings >** **Mobile** **Deployment,** and scroll down to the **Google Play Store** section.
2. Under the **Service Account Credentials**, Click on **Upload Credentials** and select the downloaded credential, i.e., the `.json` file in the previous step no.4.

[Sharing a Project with a User](https://www.loom.com/embed/a59cb331fc6944af97249dd6aec378bc?sid=62fd1920-4994-45e3-abba-e84f75a8f705)

##### 4. Deploy to Google Play Store

To enable FlutterFlow to deploy your app to the Google Play Store on your behalf for the first time, you have to download the [`.AAB`](https://chat.openai.com/share/6f5714c1-eb13-428b-b9ee-9772f2810284) file from FlutterFlow and upload it to the [Internal Testing](https://play.google.com/console/about/internal-testing/) Track on the Google Play Store.

Once the Internal Testing track is ready (with `.AAB` file), FlutterFlow can handle the subsequent releases.

###### 4.1 Getting the AAB (App Bundle) file

To get the AAB file:

1. Set the **Google Play Track** to **Internal** and hit **Deloy to Play Store**.
2. Wait for a couple of minutes and then click **Check Build Status**. If you don't see the **AAB APK** options yet, wait for some time.
3. Click on the **AAB** to download the `.aab` file.

> **Info:** You need to perform this step only for fresh deployment (i.e., first-time setup).

[Sharing a Project with a User](https://www.loom.com/embed/2c432b6bc4ba41d0bf7ec0db3912a0bd?sid=7f8df4ca-107a-4e82-aa34-06194c188ed9)

###### 4.2 Creating a testing track

> **Info:** While you can certainly release your app directly to the Production Track, it's advisable to first release it within your team using the Internal Testing Track.

Inside the [Google Play Console](https://play.google.com/console), create a testing track as per in the steps below:

[Sharing a Project with a User](https://www.loom.com/embed/01500472234942f78af65b48d1f6eacf?sid=fb31285c-b957-4011-ad0a-8285b7c553b8)

###### 4.3 Deploy

You can now deploy directly from FlutterFlow or from your GitHub repository.

> **Info:** * Every time you deploy, we'll auto increment the **Build Number** (i.e., version code in Android) to ensure that each release is identifiable. If needed, you can update the *App Version* and *Build Number* yourself.
* We'll [**auto-generate**](https://developer.android.com/studio/publish/app-signing#generate-key) and [**sign**](https://developer.android.com/studio/publish/app-signing#sign_release) your app for the release with the Keystore (i.e., upload key). If you wish to download the keystore, click the orange key button.

Ensure the **Google Play Track** is set to **Internal** and hit the **Deloy to Play Store** again. On successful deployment, you will see the status as 'finished'.

![deploy-flutterflow](https://docs.flutterflow.io/assets/images/deploy-flutterflow-cf0c6a4c693f61019a33c88d9766fd35.avif)

> **Tip:** If you prefer to manage your deployment process outside of FlutterFlow, such as integrating with your own CI/CD pipeline, or if you want more control over versioning and custom code management directly on GitHub. You also have the option to [**Deploy apps from your GitHub repository**](https://docs.flutterflow.io/deployment/deploy-from-github).

###### 4.4 Verify deployment

To verify that the app is deployed to Play Console:

1. Open the **Internal testing** in [Google Play Console](https://play.google.com/console).
2. Under the **Releases** section, find your release and click on the **Show Summary** button.
3. See the **Version Codes** number is increased.

![verify-deployment](https://docs.flutterflow.io/assets/images/verify-deployment-1fd5e667065c7ab8011980cadaec5aa2.avif)

###### 4.5 Deploy to production

To deploy your app to production:

1. Inside the **Internal testing** in [Google Play Console](https://play.google.com/console).
2. Under the **Releases** section, find and click on the **Promote Release** dropdown.
3. Select the **Production**. This will create the Production track and you can continue to release your app from there onwards.
4. Next time onwards in FlutterFlow, you can publish directly to the Production track by setting the **Google Play Track** to **Production**.

* Google Play Console: Promote to production
* FlutterFlow: Set Google Play Track to Production

![play-console-deploy-prod](https://docs.flutterflow.io/assets/images/play-console-deploy-prod-3cadf567d429b6586aa9a04b5bd74208.avif)

![play-console-deploy-prod](https://docs.flutterflow.io/assets/images/ff-deploy-prod-393c02301c78bd8fcee7a5aff9fa9325.avif)

***

#### Advanced Settings

##### Upload Keystore

If you've previously deployed an app to the Play Store using your own keystore file, you must enable this option. Once enabled, proceed to **Upload Keystore** file and provide the **Keystore Alias**.

![upload-keystore](data:image/avif;base64,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)

##### Changes not sent for review

If you face an error that says '*Changes cannot be sent for review automatically*', enable this option and retry deployment.

##### Submit as draft

While deploying, if your app is still in draft mode, meaning it is not available on the Play Store yet, you may encounter an error message stating, 'Only releases with the status draft may be created on a draft app.'

To resolve this, enable this option, and you'll see that the release will be created as a draft. You'll then need to manually roll out the app.

***

#### Video guide

Watch this video if you prefer watching a video tutorial.

[Sharing a Project with a User](https://www.youtube.com/embed/kLfcAzAHA6o)

---

### Pre-checks Before Publishing {#pre-checks-before-publishing}

*Ensure your app is ready for launch with this detailed guide on essential pre-publishing checks.*

**Source:** https://docs.flutterflow.io/deployment/pre-checks-before-publishing

This page outlines the important steps and checks to be made before publishing your app. These steps are crucial to ensure that your app works as expected, meets platform guidelines, and to gather preliminary feedback.

Here’s a comprehensive list of these prechecks:

1. **Functionality Testing**: Test the app manually across devices. You can also implement integration tests using FlutterFlow’s [**Automated Tests**](https://docs.flutterflow.io/testing/automated-tests) framework to cover various scenarios.

2. **Get Feedback**: Run your app in Run Mode to generate a shareable link to the session. You can share these links to gather feedback from users and testers, providing valuable insights and potential areas of improvement before the public release.

3. **Optimizations & Enhancements**: Improve performance by implementing [optimization and enhancement](https://docs.flutterflow.io/flutterflow-ui/toolbar#project-suggestions) suggestions. Ensure that images are properly sized, consider using higher compression for assets, and remove unused assets and custom widgets. These will help improve your app's speed and size.

4. **User Interface:** Check UI consistency across different screen sizes and resolutions using the [Canvas Size](https://docs.flutterflow.io/flutterflow-ui/canvas) option.

5. **Accessibility Checks**: Add semantic labels to make the app more accessible to users with disabilities by providing meaningful descriptions.

6. **Security Measures**: Make sure all data handling practices comply with legal standards, including GDPR if applicable. Use HTTPS for all network connections and ensure that sensitive data is encrypted.

7. **Compliance with Store Guidelines**: Review the submission guidelines for [Apple’s App Store](https://developer.apple.com/app-store/review/guidelines/) and [Google Play Store](https://play.google/developer-content-policy/). Check for any specific requirements such as app metadata, privacy policies, and minimum functionality.

8. **Localization and Internationalization**: If your app targets users in multiple countries, consider [adding multi-language](https://docs.flutterflow.io/concepts/localization) support.

9. **License and Third-Party Attributions**: Adhere to licenses and include necessary attributions for third-party libraries and assets.

10. **Prepare Marketing Assets**: Prepare all the necessary marketing assets, such as screenshots, app icons, and promotional text. You can easily [generate screenshots](https://docs.flutterflow.io/deployment/pre-checks-before-publishing#generate-screenshots) right within FlutterFlow.

***

#### Generate Screenshots

Alongside crafting beautiful apps, you can also generate screenshots for your mobile app right within the builder. Screenshots are captured in all the recommended device sizes required for publishing to the App Store and Play Store.

> **Info:** If pages are rendered using a **WebView** widget, the generated screenshots will appear blank.

Let's explore how to generate screenshots for your app:

[Sharing a Project with a User](https://demo.arcade.software/PgdOhHS8UBVdVTrem2Fy?embed\&show_copy_link=true)

---

### Web Publishing {#web-publishing}

*Discover how to effortlessly publish your applications on the web with FlutterFlow. This guide covers everything from enabling web support to deploying your app and adding custom domains.*

**Source:** https://docs.flutterflow.io/deployment/web-publishing

FlutterFlow supports web publishing, allowing you to build and publish web applications in addition to your mobile apps. This guide provides details on how to use FlutterFlow for web publishing. From enabling web support and making design adjustments to deploying your app and adding custom domains.

> **Info:** * You can ship your existing mobile app as a web app with little or no change to the current setup.
* We offer free hosting and custom subdomains for all users.
* We've rebuilt some of the components to work better on the web.

#### Publish to Web

Publishing to the Web comprises of the following steps:

1. [Enabling web support](https://docs.flutterflow.io/deployment/web-publishing#1-enabling-web-support)
2. [Make design adjustments (optional)](https://docs.flutterflow.io/deployment/web-publishing#2-make-design-adjustments-optional)
3. [Resolving errors](https://docs.flutterflow.io/deployment/web-publishing#3-resolving-web-compatibility-warnings)
4. [Adding general information](https://docs.flutterflow.io/deployment/web-publishing#4-adding-general-information)
5. [Deploy](https://docs.flutterflow.io/deployment/web-publishing#5-deploy)
6. [View live web app](https://docs.flutterflow.io/deployment/web-publishing#6-view-live-web-app)

##### 1. Enabling web support

By default, FlutterFlow allows you to run your app on *Android* and *iOS* without any additional effort. But, to run and deploy your app on the *Web*, you need to add platform support for the Web.

To add platform support, navigate to the **Setting and Integrations > Project Setup > Platform >** turn on the **Web** toggle.

![enable-web](https://docs.flutterflow.io/assets/images/enable-web-643a2696a52194f7129f78a65175e7dc.avif)

> **Info:** Enabling web support automatically enables [**deep linking**](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking) for your project. This helps in creating URLs for every page of your app.

###### Advanced Web Settings

1. **Use CanvasKit**: Enabling this option can provide high-quality graphics and text rendering on web platforms.

2. **CORS Proxy for Images (Optional)**: When using CanvasKit, some images can be blocked from loading if the server is not configured to allow loading them from other websites. This happens because Flutter web uses WebGL for rendering, which requires access to raw image data and is subject to browser security restrictions called [Cross-Origin Resource Sharing (CORS)](https://docs.flutter.dev/platform-integration/web/web-images#cross-origin-resource-sharing-cors).

   Choose the appropriate option based on where your images are hosted:

   * **None**: If you are only loading images from your Firebase Storage, select this option and configure Firebase Storage for web access. FlutterFlow automatically excludes Firebase Storage images from CORS proxy requirements.

   * **Deploy with Firebase**: If images are hosted on external servers (not Firebase Storage) *but you use Firebase for your app*, choose this option. FlutterFlow will automatically deploy a regional CORS proxy function to your Firebase project for optimal performance. Simply click the **Deploy** button that appears below this option.

   * **Custom Proxy URL**: If you're not using Firebase or prefer to manage your own CORS proxy, specify your custom proxy URL here. If you don't have one, you can create one using services like [cors-anywhere](https://github.com/Rob--W/cors-anywhere) or CloudFlare Workers.

   warning

   **Performance Note**: Using a CORS proxy adds a network hop for external images, which may slightly increase loading times. For best performance, host images on Firebase Storage or a CORS-enabled CDN when possible.

3. **Import Emoji Library**: Importing the Emoji library is necessary if your app may use emojis anywhere in any text widget. However, this will increase the size of your app on web.

4. **Use Wasm (Beta)**: Enabling this option will build your app using Flutter’s **Wasm (WebAssembly) web renderer**. For more details, see the [Flutter Documentation on Wasm](https://docs.flutter.dev/platform-integration/web/wasm).

   warning

   * This feature is currently in *Beta*, so it should be used with caution.
   * Wasm is not supported in *Test Mode*.

###### Troubleshooting CORS Issues

If you're experiencing image loading issues on web:

1. **Check browser console**: Look for CORS-related error messages
2. **Verify image sources**: Ensure external image servers allow cross-origin requests
3. **Test proxy configuration**: Verify your custom proxy URL is accessible and functioning
4. **Firebase Storage setup**: Confirm Firebase Storage rules allow public read access for web

##### 2. Make design adjustments (optional)

If you're creating a web-only application, setting the canvas size to desktop and building pages accordingly can work well. However, if you plan to target both mobile and web users, some design adjustments may be necessary to ensure that the UI is optimized for both platforms.

You can create separate widgets for different platforms and control their visibility using [Responsive Visibility](https://docs.flutterflow.io/concepts/layouts/responsive#responsive-visibility).

##### 3. Resolving web compatibility warnings

If you have previously built a mobile app and have recently enabled web support, you may encounter warnings regarding web compatibility. Due to the distinct nature of mobile and web platforms, some of the widgets and actions in FlutterFlow, including [AdMob](https://docs.flutterflow.io/integrations/ads/admob), [RevenueCat](https://docs.flutterflow.io/integrations/payments/revenuecat), [Share](https://docs.flutterflow.io/concepts/navigation/share-action) action, and [Launch Map](https://docs.flutterflow.io/deployment/web-publishing) action, or your custom widgets may not function as expected because they are not yet supported on the web.

Any known *Web Support* Issues will be displayed as a **Platform Support Warning**. This won't stop you from deploying your app to the web, but it can result in poor user experience and unexpected app behavior.

![platform-warnings](https://docs.flutterflow.io/assets/images/platform-warnings-ab76fa005365e723233d93bc4bb2337b.avif)

In such a situation, you can try to find a replacement package on [pub.dev](https://pub.dev/) (considering it meets your requirements and has a good score).

> **Warning:** **Important**: Make sure to double-check any *pub.dev* packages you are using have *Web* Support.

![web-support](https://docs.flutterflow.io/assets/images/web-support-09e3ea561fe01d5c695f7288e073cf8c.avif)

##### 4. Adding general information

In this step, you must provide general information about your web app by following the steps below:

1. Navigate to the **Setting and Integrations >** **App Settings >** **Web Deployment**.

![web-pub-general-settings](https://docs.flutterflow.io/assets/images/web-pub-general-settings-66306bc810313d0b7ff879d85786f4e4.avif)

Inside the **General Information** section, enter the following details:

* **Site URL**: You can define the *Site URL* by adding the subdomain, for example, *mywebapp.flutterflow\.app*. You can only change the subdomain, i.e., the part before *flutterflow\.app*.

  warning

  * You can remove or change the existing subdomain by simply entering the new one and hitting the publish button. Note that when you change your subdomain, it only takes effect the next time you deploy.
  * Old addresses can stop working anytime and be given to another user.
  * There is a limit on the number of subdomains you can register per user. *Paying users can register up to 20 subdomains*. You will receive an in-app warning if you are approaching the limit.

* **SEO Title**: This appears in social sharing previews and search results.

* **Site Description**: A text that you would like to appear in the social sharing preview card and search results.

* **Page Title**: This appears in the browsers tab for all pages of your app.

* **Favicon**: An icon that typically appears before the web app name inside the browser's tab. To change it, click on the **Upload Favicon +** and upload the icon. You can generate it for free from [here](https://favicon.io/).

* **Status Bar Color**: This is to change the status bar color when viewed on the Safari browser on iOS and installed as a PWA on mobile devices.

* **Social Share Image URL**: The image from this URL will be displayed inside the social share preview card (e.g., OpenGraph and Twitter card).

* **Individual Page Titles**: Enabling this will display the current page name in the browser tab. If you do so, ensure you provide the **Page Title** under **Page > Properties Panel > Route Settings**.

* **Show Watermark**: By default, a button with 'Built in FlutterFlow' text appears as a watermark at the bottom right side of your page. To remove, disable the **Show watermark** toggle.

* **Allow Showcasing**: If enabled, we may feature your project on our website.

* **Allows Search Engine Indexing**: This is to let people discover your site via search engines.

* **Enabling PWA**: Enabling this can provide an app-like experience right in the browser. PWA app can be installed on the device, supports offline functionality, sends push notifications, and can be accessed without the need to go through an app store.

* **Use CanvasKit**: Enabling this can provide high-quality graphics and text rendering on web platforms. CanvasKit can be used as an alternative to the default HTML renderer when higher graphical fidelity is needed in Flutter web apps.

* **Use Original Engine Initialization**: This uses original Flutter web engine initialization, which sometimes helps in better loading time in the deployed web app.

> **Info:** Tip: Only users on the paid plans can remove the FlutterFlow watermark.

##### 5. Deploy

When you are ready to deploy, click **Publish.** This will take approximately 2-3 minutes.

![publish-button](https://docs.flutterflow.io/assets/images/publish-button-69cee7cd9d757ee661957d2b9ca6c0f9.avif)

By default, you will publish to a subdomain based on your project id. These default subdomain addresses do not count toward the subdomain quota, and you can deploy as many projects as you'd like. The URL would look like this: `your-project-id-1234.flutterflow.app`

You can also modify the address by specifying a custom subdomain address, in the **Settings > Web Publishing** tab's **Site URL** field, as long as it's available. You can have up to **2** custom subdomain URLs on the Free plan, up to **20** on any of our Paid plans, and **unlimited** custom subdomain URLs on the Enterprise plan.

> **Info:** Once it is published, you can make any changes live to your users by clicking the **Publish** button again.

If you try to publish to a domain that is already taken, you will receive a warning like ‘*Error reserving subdomain: Subdomain `your-domain-name` is already used by another project.*’ To overcome this, enter a different subdomain inside the **Site URL** and select **Publish** again.

> **Info:** In case you want to unroll your web app, hit the **Unpublish** button at the bottom.

##### 6. View live web app

To view the live version of your app, click the **eye icon** next to the 'Publish' button.

![view-published-site.avif](https://docs.flutterflow.io/assets/images/view-published-site-fb67b90e4b5a97af7a7c101aeea1061d.avif)

***

#### Adding custom domain

Adding a custom domain to your web app can give it a more professional look and feel and make it easier for your users to remember and find. FlutterFlow allows you to connect your own domain name to your web app and have it up and running in no time. This feature is perfect for those wanting to establish a strong online presence and increase brand awareness.

Important

* All our paid plans include one free custom domain, with the option to purchase more if needed.
* A single custom domain slot can be linked to only one domain or subdomain.
* You can connect only one domain to a project, which can be either a root domain (like 'myapp.com') or a subdomain (such as 'beta.myapp.com'). That means if you connect a root domain, none of the subdomains under it will connected to the project. This leads to the rule of '*One project => One domain OR subdomain'*.

To add a custom domain:

1. Enter your **Custom Domain URL**. Ensure you only enter the domain name (without www) and extension (e.g.,*mywebapp.com* and not *[www.mywebapp.com](http://www.mywebapp.com)*).

2. Now, you must set up the DNS. To do so: 1. Visit the website from where you bought the domain.
   2. Open the DNS manager and create the records as per displayed in UI. **Note** that there should not be other A or AAA records after adding this. Here are quick links on how to do this on popular domain-selling websites. 1) [Godaddy](https://in.godaddy.com/help/add-an-a-record-19238) 2) [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/319/2237/how-can-i-set-up-an-a-address-record-for-my-domain/) 3) [Google Domains](https://support.google.com/a/answer/2579934?hl=en). Here's an example of how it looks in Godaddy. ![custom-domain-listing.avif](https://docs.flutterflow.io/assets/images/custom-domain-listing-15b4939f2bd6b275d07c417ec1a89ff1.avif)
   3. Click **Connect**.
   4. Once the domain is connected, hit the **Publish** button again. ![connect-custom-domain.avif](https://docs.flutterflow.io/assets/images/connect-custom-domain-7e79a9bf73bf3f1f372ca67e5c0706da.avif)

***

#### Add custom headers

If you are familiar with HTML, you may set any additional headers (e.g., [style](https://www.w3schools.com/tags/tag_style.asp) and [script](https://www.w3schools.com/tags/tag_script.asp)) that you would like to be used in your published web app. For example, adding inline or external javascript. This will appear inside the head tag of your published app.

> **Warning:** These headers are used directly in the `index.html` of your site, so malformed headers may cause unexpected behavior (just as directly editing `index.html` would).

To add a custom header, enter your tag inside the *Custom Headers* input box and publish the web app again.

> **Info:** You can verify the added custom header by opening the inspect element window (**Command+Option+i** on **Mac** or **F12** on **PC**) and finding your tag inside the head tag.

![custom-header.avif](https://docs.flutterflow.io/assets/images/custom-header-530514e7514209099851f8a6c95f6777.avif)

***

#### Changing Firebase dynamic link

If you do web deployment and utilize Firebase dynamic links in your app, it's recommended that you update your Firebase Dynamic Links URL scheme. This adjustment is necessary to ensure shared links open correctly on the web. By doing so, your dynamic links will function properly for users across all platforms.

![update-firebase-dynamic-link.avif](https://docs.flutterflow.io/assets/images/update-firebase-dynamic-link-4237c8bcd04bc639c96bcc9368428f0d.avif)

***

#### Adding subdomain as Authorized domain (Firebase)

If you are using *Firebase Authentication*, you must add your custom subdomain as an authorized domain in the [Firebase console](https://console.firebase.google.com/). Otherwise, social and phone sign-in will not work.

To enable your subdomain as an authorized domain:

[Sharing a Project with a User](https://demo.arcade.software/lT8TyH1hZARTobmthlwI?embed\&show_copy_link=true)

***

#### See deployment history

Deployment history is essential for maintaining transparency, accountability, and a clear understanding of how a web application has evolved over time. Each deployment entry in the history includes a timestamp indicating when the deployment occurred.

It also display the status of each deployment (e.g., successful, failed). This helps in quickly identifying whether a deployment was completed without issues.

Click **View Full History** to review the previous successful version.

![view-deploy-history.avif](https://docs.flutterflow.io/assets/images/view-deploy-history-f47685e0faae99366d95363c2472065d.avif)

---

---

## Exporting Code

### Push to GitHub Repo {#push-to-github-repo}

*Learn how to connect your FlutterFlow project to a GitHub repository and manage custom code.*

**Source:** https://docs.flutterflow.io/exporting/push-to-github

This guide provides instructions on how to connect your FlutterFlow project to a GitHub repository and manage custom code.

#### Connect a GitHub repo

In this section, we'll learn how to connect your FlutterFlow project to a GitHub repository. This includes creating a new repository, installing the FlutterFlow GitHub App, and pushing your code to the repository.

Here’s how you do it:

1. First, go to your GitHub account and create a new repository.

[Sharing a Project with a User](https://demo.arcade.software/UhBD10h3wufXyozCBFhK?embed\&show_copy_link=true)

2. Once the repository is created, install the [FlutterFlow GitHub App](https://github.com/apps/flutterflow-github-app) in your GitHub account.

[Sharing a Project with a User](https://demo.arcade.software/bxvvWOrBV7RFzfa2lEDP?embed\&show_copy_link=true)

3. You can now push your code to the repository.

[Sharing a Project with a User](https://demo.arcade.software/f6L33Z7nNg7QNKeWQMWg?embed\&show_copy_link=true)

> **Tip:** * FlutterFlow always pushes changes to a branch named `flutterflow`. Avoid making direct changes to this branch, as your changes will be overwritten by the next push from FlutterFlow.
* If you need to modify the code, make changes in a separate branch. Learn more about managing custom code.

#### Manage Custom Code on GitHub

Writing custom code allows you to add features that are not supported by FlutterFlow's current functionality. This section outlines how you can manage custom code using GitHub to prevent FlutterFlow from overriding it.

![manage-custom-code](https://docs.flutterflow.io/assets/images/manage-custom-code-b95630fd004549dd5a784f05337c1c79.avif)

The diagram illustrates the flow or process of managing code in GitHub. This process allows you to leverage all the features from FlutterFlow and deploy your app with a custom code.

Here's a step-by-step explanation:

##### 1. Connect FlutterFlow to GitHub

First, set up the connection between your FlutterFlow project and GitHub repository. [Follow these steps](https://docs.flutterflow.io/exporting/push-to-github#connect-a-github-repo) if you haven’t already done so.

##### 2. Establish a custom code branch

After pushing your FlutterFlow code to GitHub, it lands in the `flutterflow` branch. To safeguard your custom modifications from being overwritten by future pushes, create a `develop` branch.

1. Navigate to your GitHub repository.
2. Switch from `main` to `flutterflow` in the branch dropdown.
3. In the branch creation field, enter `develop` and create the branch from `flutterflow`.

##### 3. Add custom code

Once your `develop` branch is ready, [clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to your local machine. Open the project in your IDE, switch to the `develop` branch, and add your custom code.

After making changes, commit and push them back to the `develop` branch.

##### 4. Merge changes from FlutterFlow

To integrate the latest updates of your FlutterFlow project into your custom code:

1. Create a pull request on GitHub from `flutterflow` to `develop`.
2. Review and merge the changes, resolving any conflicts if necessary.

##### 5. Final testing and deployment

After testing the changes in `develop`:

1. Merge `develop` into `main` via a new pull request on GitHub.
2. Once reviewed and merged, deploy your application from the `main` branch using FlutterFlow’s deployment features.

> **Tip:** Also, see how you can download the code using [**FlutterFlow CLI**](https://docs.flutterflow.io/flutterflow-cli) and [**Local Run**](https://docs.flutterflow.io/testing/local-run).

---

---

## Marketplace

### Adding & Purchasing Items {#adding-purchasing-items}

*Learn how to add and purchase FlutterFlow marketplace items.*

**Source:** https://docs.flutterflow.io/marketplace/adding-purchasing-item

The **FlutterFlow Marketplace** lets you add new features to your app in just a few clicks. It includes ready-made components, templates, and libraries built by other users. These items can help you add things that are not yet available in FlutterFlow or would take more time to build from scratch.

To add a Marketplace item, go to your FlutterFlow dashboard and click **Marketplace**, or visit [marketplace.flutterflow.io](https://marketplace.flutterflow.io/) directly. Click on any item to view its details.

* For **free items**, click **+ Clone for Free**, then choose the project you want to add it to.
* For **paid items**, click **Buy Now** and complete the purchase.

Once added, the item will be available in your selected project for immediate use.

* Free Item
* Paid Item

![free-item](https://docs.flutterflow.io/assets/images/free-item-723adc39b8cba522e58a59b89a0cffb0.avif)

![paid-item](https://docs.flutterflow.io/assets/images/paid-item-1eb671388d39c50fbe09110f71035c44.avif)

#### Add Library Item

To install a library item from the Marketplace, search for the library, open its details page, and click **+ Add for Free**. This adds the library to your FlutterFlow account, meaning you can reuse it in any of your projects.

To add it to a specific project, go to **Settings > Project Dependencies**, click **Add Library**, and search for your library.

![branch-library-install](https://docs.flutterflow.io/assets/images/branch-library-install-c634fb2710a175e9f5cca5a7a7a738b9.png)

---

### Creators Hub {#creators-hub}

*This section is designed to provide you with all the necessary information to contribute effectively and responsibly to Marketplace.*

**Source:** https://docs.flutterflow.io/marketplace/creators-hub

Welcome to the FlutterFlow Marketplace Creators' Hub! This section is designed to provide you with all the necessary information to contribute effectively and responsibly to Marketplace. Whether you are submitting your first item or looking to understand the legal nuances, you'll find detailed guidelines and helpful tips here.

##### Submitting an Item for Review

* Understand the [criteria](https://docs.flutterflow.io/marketplace/creators-hub/submission-criteria) we apply to items submitted to Marketplace.
* Learn how to prepare and [submit](https://docs.flutterflow.io/marketplace/creators-hub/submit-item-for-review) your items to the Marketplace with our step-by-step guide.

##### Legal Guidelines for Creators

A user-friendly [guide](https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators) outlining what content can and cannot be published on our Marketplace.

We've also compiled information on dealing with [external licenses](https://docs.flutterflow.io/marketplace/creators-hub/navigating-external-licenses), including excerpts from popular third-party marketplaces that restrict the creation of templates on platforms like FlutterFlow Marketplace.

Finally, we have a detailed guide on how we handle [DMCA takedown notices](https://docs.flutterflow.io/marketplace/creators-hub/copyright-dmca-process). This is crucial for understanding how to manage copyright issues and ensure compliance.

##### Creator FAQs

[Find answers](https://docs.flutterflow.io/marketplace/creators-hub/creator-faqs) to common questions from fellow creators.

---

### Copyright (DMCA) Process {#copyright-dmca-process}

*Understand the copyright (DMCA) process on FlutterFlow Marketplace.*

**Source:** https://docs.flutterflow.io/marketplace/creators-hub/copyright-dmca-process

> **Danger:** This guide is meant for creators of items on FlutterFlow Marketplace. If you want to provide feedback on an item published in FlutterFlow Marketplace, please follow the relevant instructions at [**Submitting Feedback for Items**](https://docs.flutterflow.io/marketplace/submit-feedback).

As a valued creator on the FlutterFlow Marketplace, it's important to understand the process that unfolds when an item you've submitted receives an infringement report. Our approach distinguishes between two main types of allegations: DMCA infringement claims and other types of infringement allegations.

##### DMCA Infringement Claims

The [DMCA (Digital Millennium Copyright Act)](https://en.wikipedia.org/wiki/Digital_Millennium_Copyright_Act) is a US copyright law that provides a mechanism for copyright owners to request the removal of content they believe infringes on their copyright. Here's how we handle these specific claims:

1. **Immediate Action**: If an infringement report is classified as a DMCA claim and the reporter provides adequate proof of ownership or authorized representation, we are legally required to act quickly. In such cases, the reported item is immediately removed from FlutterFlow Marketplace.
2. **Notification Email**: Upon removal, you will receive an email notification outlining the details of the claim and the steps you can take if you believe the item was wrongly removed.
3. **(Optional) Counter-Notice**: If you choose to submit a counter-notice, we will provide guidance on the process. Please email <marketplace-legal@flutterflow.io> with any relevant details.

##### Other Infringement Allegations

For other infringement reports, specifically those filed by individuals who are neither the copyright owner nor their authorized representatives, we follow a different process:

1. **Credibility Review:** Our team will first assess the credibility of the report. We will engage with the reporter to gather additional information if the initial claim lacks sufficient detail. If we determine the claim appears credible, we will then proceed to notify you the creator. 1. *Evidence of Prior Publication:* In cases where an infringement allegation is supported by a URL linking to similar content that was clearly published prior to the date of submission on FlutterFlow Marketplace, this URL will be considered sufficient preliminary evidence to establish the credibility of the claim.
2. **48 Hours Notice:** When we receive a non-DMCA allegation that is deemed credible after our initial review, we will notify you and provide a 48-hour period for you to respond to the claim. This window allows you to present any counter-evidence or resolve the issue by modifying or removing the item yourself.
3. **Review of Evidence**: If you provide evidence or make changes that address the report's concerns, we will review this new information before making a final decision on the item's status in Marketplace.
4. **Resolution**: If, after reviewing the evidence, the claim is found to be credible, or if no response is received within the 48-hour window, we will proceed with removing the item from Marketplace and inform you of the action taken.

---

### Creator FAQs {#creator-faqs}

*Learn about creator's FAQs in FlutterFlow Marketplace.*

**Source:** https://docs.flutterflow.io/marketplace/creators-hub/creator-faqs

#### ⚖️ Intellectual Property and Legal Concerns

##### Why might my item be removed from Marketplace?

Your item might be removed from the Marketplace under several circumstances, mainly related to legal and quality standards. Here are the specific reasons:

* **DMCA Takedown Notices:** If we receive a DMCA takedown notice claiming that your item infringes on someone else's copyright, we are legally required to remove the item immediately. We will notify you of the takedown, and you will have the opportunity to respond or counter-claim according to the legal processes set out by the DMCA. Please see [Copyright (DMCA) Process](https://docs.flutterflow.io/marketplace/creators-hub/copyright-dmca-process) for details.
* **Other IP Violations:** If your item is found to violate IP laws outside of a formal DMCA complaint—i.e. if filed by someone other than the original author or their representative—we will inform you of the specific violation. You will be given a chance to provide proof of licensing or to correct the issue within **48 hours**. If satisfactory proof or corrections are not provided, the item may be removed to comply with legal standards. Please see [Copyright (DMCA) Process](https://docs.flutterflow.io/marketplace/creators-hub/copyright-dmca-process) for details.
* **Violation of Marketplace Policies:** Aside from copyright issues, if your item violates other Marketplace policies, such as those related to quality, accuracy, or ethical standards, you will be notified of the specific issues. We will provide you with details about the violation and, depending on the severity, you may be asked to modify the item or it might be removed. Please see [Marketplace Item Submission Guidelines](https://flutterflow.io/flutterflow-marketplace-item-submission-guidelines) for more details.
* **Critical Item Reports:** If we receive reports from users or other creators that critically challenge the legality or appropriateness of your item (e.g., reports of plagiarism, false advertising, or severe quality issues), these will be thoroughly investigated. Based on the findings, and in accordance with our commitment to maintaining a trustworthy and high-quality Marketplace, your item might be subject to removal. We will communicate with you throughout this process, offering details of the report and an opportunity to respond.

##### Will I be notified if my item is removed from Marketplace?

Yes, in all cases, you will be notified if your item is removed from FlutterFlow Marketplace.

##### Can I list my item on other marketplaces?

No. You cannot sell FlutterFlow projects on other marketplaces. Please see the non-circumvention clause in our [Marketplace Terms of Service](https://flutterflow.io/tos-marketplace).

This policy helps ensure that all interactions with FlutterFlow templates are safe, compliant, and effectively managed for our users.

##### What licenses are granted to users of my item?

When users purchase or add items from the FlutterFlow Marketplace, they are granted use under specific licenses:

* **Free items** are generally covered under the **MIT License (Open Source License)**, which allows extensive freedom to use, modify, and redistribute the content.
* **Paid items** are usually governed by **Single Use License.**

Please refer to the specific restrictions and conditions outlined in our [Marketplace Terms of Service](https://flutterflow.io/tos-marketplace) for each license type.

##### What if someone copies my template code or design?

Please reach out to <marketplace-legal@flutterflow.io> for next steps.

#### 🚨 Reporting Process

##### What happens if someone reports my item?

> **Info:** We will always notify you if your item is removed from Marketplace.

If the reporter is the original author and files a DMCA notice, the item will be removed immediately as required by law. You will be notified and have the opportunity to submit counter-evidence. Please see [Copyright (DMCA) Process](https://docs.flutterflow.io/marketplace/creators-hub/copyright-dmca-process) for details.

For other reports, we will notify you **48 hours** before taking any action. During this time, you may submit counter-evidence or clarify the situation.

##### If my item is reported, what details will you share with me?

When your item is reported, our goal is to maintain transparency while respecting privacy and legal constraints. Here’s what we will share with you:

* **Report Type:** We will inform you about the specific nature of the complaint, such as whether it’s a copyright or quality issue.
* **Relevant Details:** We will provide any non-confidential details submitted within the report that you need to understand the complaint and to formulate your response.
* **Deadlines:** We will inform you of any deadlines by which you need to respond or take corrective action to avoid having your item removed from Marketplace.

Please note that we will not share the identity of the reporter.

##### If my item is reported, what details will you share with the original reporter?

When a report is filed, we ensure that the process is fair and respects the privacy of all parties involved. Here’s what we will share with the original reporter:

* **Confirmation of Report:** We will acknowledge receipt of their report and confirm that we are taking it seriously.
* **Contact Email:** We will provide your Marketplace Creator official email as specified in your [public profile](https://marketplace.flutterflow.io/profile).

##### What if I see low-quality items on the Marketplace? How can I report an item?

We strive to maintain a high standard, but some items may not meet these expectations. If you encounter an item on the Marketplace that appears to violate our policies, please submit feedback using one of the channels described on [this page](https://docs.flutterflow.io/marketplace/submit-feedback):

#### 📦 Item Submission and Review

##### What is the criteria for getting my item approved for Marketplace?

Please see our [Item Submission Criteria](https://docs.flutterflow.io/marketplace/creators-hub/submission-criteria).

##### What happens if my item is rejected?

If your item is not approved, it will be returned to draft status, allowing you to make the required edits. We will provide you with detailed feedback via email, specifying the criteria it did not meet. You can see more details about our criteria and suggested actions [here](https://docs.flutterflow.io/marketplace/creators-hub/submission-criteria). You can then make the necessary adjustments and resubmit it for review.

##### When will my template be reviewed?

We have significantly improved our review wait time recently! ⚡

We aim to review your template within 7 days. However, depending on the volume of submissions or the complexity of your submission, the review process can take up to 30 days (20 business days).

#### 🖐️ Other Questions?

If your question is not covered here, please **first review the other documentation pages** within the Marketplace section. If you are still facing issues, please reach out to the appropriate channel:

* For legal issues, please email <marketplace-legal@flutterflow.io>
* For other issues, please email <marketplace@flutterflow.io>

---

### Legal Guidelines for Creators {#legal-guidelines-for-creators}

*Understand the legal guidlines for creating marketplace items.*

**Source:** https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators

As part of our creative community, your contributions are invaluable in helping others build amazing apps. To ensure a smooth experience for everyone and to adhere to legal requirements, we've outlined what types of content you can publish on Marketplace. This guide is designed to be user-friendly and straightforward, focusing on the legal aspects of your submissions. For a more detailed view of our policies, please review the [Marketplace Terms of Service](https://flutterflow.io/tos-marketplace).

##### What You Can Submit

* **✅ Original Creations:** Your template should be your original work or properly licensed work that you have the right to distribute. Whether it’s a unique design layout, a functional module, or an innovative app solution, if you created it, we're excited to see it!
* **✅ API Wrappers**: If you've developed a wrapper for public APIs (like AWS or SendGrid), you're welcome to submit it! Ensure your wrapper adds value through simplification, integration, or enhancement of the original API functionalities.
* **✅ Educational Templates**: Educational or demonstrative templates that mimic functionalities of popular apps (like a "social photo app clone") are great for learning and are welcome, provided they do not use any trademarked names, logos, or proprietary UI elements from the actual apps.

##### What to Avoid in Your Submissions

* **❌ Designs from External Marketplaces:** Please refrain from submitting designs or templates that you've acquired from other marketplaces. Typically, these items are licensed, not sold, and come with restrictions that prohibit their redistribution on our platform. For guidance on navigating external licenses and understanding your rights, please review [Navigating External Licenses](https://docs.flutterflow.io/marketplace/creators-hub/navigating-external-licenses).
* **❌ Proprietary Code or Data**: Do not include any proprietary code, data, or APIs that you do not have explicit rights to use and redistribute. This includes direct copies of proprietary software or use of internal SDKs not intended for public distribution.
* **❌ Trademarked Material Without Permission**: Avoid using trademarked names, logos, or branding elements in your templates unless you have obtained explicit permission from the trademark owner. This includes mimicking the UI of a proprietary app exactly.
* **❌ Misleading Content**: Ensure your template does not mislead users into thinking it's officially affiliated with or endorsed by any brand or service it might resemble, especially in educational or demonstrative templates.

##### Best Practices for Template Submission

* **✍️ Clear Attribution**: If your template includes third-party open-source components, ensure you comply with their licenses by properly attributing the original creators and including any required license texts or notices. Also see [Open Source Licenses](https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators#open-source-licenses).
* **💎 Use Generic Elements**: For educational or demonstrative templates, use generic names and design elements to avoid trademark issues while still providing valuable learning experiences.
* **⚖️ Include Disclaimers**: When necessary, include disclaimers clarifying the purpose of your template, especially if it's for educational use, to avoid any potential confusion about its unofficial status.
* **📣 Stay Informed**: Licenses and legal requirements can change, so it's crucial to stay informed about the legal aspects of the components and APIs you use in your templates.

#### Licenses: What's Allowed?

##### Open Source Licenses

Embracing open-source is part of our ethos, but not all licenses are created equal, especially in a commercial setting like ours. Here's a quick rundown of what fits on Marketplace:

* **✅ Permissive Licenses**: Licenses such as MIT, BSD, and Apache 2.0 are generally fine because they allow commercial use and modification with minimal restrictions. Just make sure to give proper credit and include the original license text as required.
* **🤔 Copyleft Licenses (Caution!)**: Licenses like GPL (General Public License) can be tricky. They often require derivative works to be distributed under the same license, affecting how your template can be used. If you're considering using GPL-licensed code, please review the specific terms carefully or consult with legal advice to ensure compliance.
* **❌ No Unlicensed Code**: Ensure all open-source code used in your templates is properly licensed. Using unlicensed code or failing to comply with open-source license requirements can lead to legal headaches for you and for us.

##### Licenses from Other Marketplaces

We understand that inspiration can come from lots of different sources, including other marketplaces. However, it's important to respect legal and ethical standards, especially with the reuse of design elements and templates purchased elsewhere. Here’s what you should know:

* **🤝 Ownership and Licensing**: When you purchase a design or template from other marketplaces, you're typically acquiring a license to use that item, not owning it outright. These licenses often come with significant restrictions, particularly around redistribution and creating derivative works meant for resale. It’s best to carefully review the license terms for each item and marketplace you use. See [Navigating External Licenses](https://docs.flutterflow.io/marketplace/creators-hub/navigating-external-licenses) for some examples.

* **⚠️ End Products and Redistribution**: Most marketplace licenses restrict the use of their items as part of an “end product” that is not meant for redistribution or resale. For example, using a downloaded Figma design to create a template that you then sell on FlutterFlow Marketplace may violate the original marketplace's license terms, even under extended licenses. When in doubt, ask the original content provider. Obtaining explicit permission or clarification can prevent future disputes and legal challenges.

* **Clarifications and Examples**: * **❌ Likely Prohibited**: Using a UI design purchased from another marketplace to create a FlutterFlow template that you intend to distribute or sell.
  * **✅ Allowed**: Creating a template inspired by design principles or trends you've observed, without directly copying or adapting a purchased item.
  * **✅ Allowed**: Implementing a UI design with the explicit written permission from the author and owner of that design.

For more details and examples, please review:

[Navigating External Licenses](https://docs.flutterflow.io/marketplace/creators-hub/navigating-external-licenses)

#### Item Reports and Complaints

At FlutterFlow, we're committed to maintaining a respectful and legally compliant community. We understand that there may be instances where content on FlutterFlow Marketplace may infringe on your rights or violate our policies. To address these concerns, we've established a straightforward process for filing complaints, including DMCA requests and other legal concerns.

##### Reporting an Item

We encourage our community members to resolve disputes amicably whenever possible. For details on contacting creators, reporting items, rating items, and filing a DMCA notice, please visit the following page.

[Submitting Feedback for Items](https://docs.flutterflow.io/marketplace/submit-feedback)

##### Responding to Item Reports

When you receive a report about an item you've listed on FlutterFlow Marketplace, it's important to respond promptly and thoughtfully. We've put together a breakdown of our process for responding to DMCA and other infringements here:

[Copyright (DMCA) Process](https://docs.flutterflow.io/marketplace/creators-hub/copyright-dmca-process)

Our goal is to foster a creative, respectful, and lawful environment for all users. By following these steps, you help us achieve this goal and ensure FlutterFlow remains a platform where innovation thrives within the bounds of respect and legality.

For further assistance or questions, please contact <marketplace-legal@flutterflow.io>.

---

### Navigating External Licenses {#navigating-external-licenses}

*Understand the key concepts that will assist you in creating unique and compliant content for FlutterFlow Marketplace.*

**Source:** https://docs.flutterflow.io/marketplace/creators-hub/navigating-external-licenses

We know navigating the world of licenses and copyright rules can be a bit daunting, so we’ve put together this guide to help simplify things for you. Here, we’ll cover some of the most common licensing terms you’ll encounter and explain key concepts that will assist you in creating unique and compliant content for FlutterFlow Marketplace.

Keep in mind that while we aim to highlight the most prominent licenses, it’s crucial to always check the most recent and applicable license terms for any assets you plan to use. If you’re ever unsure, please consult the relevant content provider or original author.

##### Key Terms

**"Derivative Work"**

The term **Derivative Work** refers to any new creation that incorporates a copyrighted asset in a form that is still closely related to the original. Most licenses, especially in digital marketplaces, prohibit using assets to create derivative works that are then sold as standalone products or used as base templates in a marketplace. This means you cannot take a design template, make minor adjustments, and resell it as your own template. The creation of derivative works generally requires significant transformation of the original asset, ensuring the final product is distinct enough to not merely be a slight variation of the original.

**"End Product"**

Some licenses may permit “unlimited end products”. However, it's important to understand that this typically refers to the ability to create multiple final projects using the original asset as long as each project remains within the terms set out by the original license. An **End Product** is a final, functional, and complete creation that is built from the initial resources but is substantially different from them. In the context of app development, an end product is typically the final app delivered to users, *not an app template* intended for further development or resale.

##### License Examples

As seen from the licensing terms of platforms like UI8, Envato, Creative Market, and Canva, there are clear restrictions against using their items directly or in slightly modified forms as base materials for creating new FlutterFlow Marketplace items. This practice could violate copyright laws and the specific licensing agreements set by these platforms.

* UI8
* Envato
* Creative Market
* Canva

**License Terms:** <https://ui8.net/licensing>

**Relevant Products:** [All Access Pass](https://ui8.net/products/all-access-pass) (Basic, Elite, and Lifetime)

**Excerpt** *(as of April 22, 2024)*

> \[You cannot] make a theme, template or derivative work of any product to sell on any marketplace.

**hi** **Legal Contact:** <legal@ui8.net>

***

**Result:** ❌ Not allowed to use in creating FlutterFlow Marketplace template

**License Terms:** <https://elements.envato.com/license-terms> and <https://codecanyon.net/licenses/terms/extended>

**Relevant Products:** [Envato Elements subscription](https://elements.envato.com/pricing)

Also, individual items sold on:

* CodeCanyon: <https://codecanyon.net/>
* ThemeForest: <https://themeforest.net/>
* VideoHive: <https://videohive.net/>
* AudioJungle: <https://audiojungle.net/>
* GraphicRiver: <https://graphicriver.net/>
* PhotoDune: <https://photodune.net/>
* 3DOcean: <https://3docean.net/>

**Excerpts** *(as of April 22, 2024)*

> You can’t re-distribute the Item as stock, in a tool or template, or with source files. You can’t do this with an Item either on its own or bundled with other items, and even if you modify the Item. You can’t re-distribute or make available the Item as-is or with superficial modifications.

> You can’t use the Item in any application allowing an end user to customise a digital or physical product to their specific needs, such as an “on demand”, “made to order” or “build it yourself” application. You can use the Item in this way only if you purchase a separate license for each final product incorporating the Item that is created using the application.

**Legal Contact:** <legal@envato.com>

***

**Result:** ❌ Not allowed to use in creating FlutterFlow Marketplace template

**License Terms:** <https://creativemarket.com/licenses/terms/general#extended-commercial>

**Relevant Products:** [Membership](https://creativemarket.com/membership) with Extended Commercial License

**Excerpt** *(as of April 22, 2024)*

> Resale or Sub-Licensing of the Licensed Asset or any modification of it in a way that is directly competitive with the original Licensed Asset is strictly prohibited (e.g., as a stock asset or template).

**Legal Contact:** <ip@creativemarket.com>

***

**Result:** ❌ Not allowed to use in creating FlutterFlow Marketplace template

**License Terms:** <https://www.canva.com/policies/content-license-agreement/>

**Relevant Products:** [Canva Pro](https://www.canva.com/pro/) (with Pro Content license)

**Excerpt** *(as of April 22, 2024)*

> Unless it’s a template created for use on Canva, you can’t use Pro content in templates of any nature.

**Legal Contact:** <legal@canva.com>

***

**Result:** ❌ Not allowed to use in creating FlutterFlow Marketplace template

##### Securing Explicit Permissions

In situations where standard licensing does not meet the specific needs of your project or where the terms seem restrictive, **obtaining explicit permission from the original content creators can be a viable solution.** This allows for flexibility and ensures that your use of the assets is legally sound.

We encourage reaching out directly to copyright holders whenever you are considering uses that are not clearly allowed under the standard license terms. Documenting such permissions in writing is essential to avoid any future misunderstandings or legal disputes.

---

### FlutterFlow Marketplace Review Dispute Guidelines {#flutterflow-marketplace-review-dispute-guidelines}

*Learn about FlutterFlow Marketplace review dispute process and when reviews may be removed or modified.*

**Source:** https://docs.flutterflow.io/marketplace/creators-hub/review-dispute-guidelines

At FlutterFlow Marketplace, we believe in transparent and honest feedback. Reviews are an essential part of helping buyers make informed decisions and helping creators improve their work.

However, not all reviews are created equal. Sometimes feedback is based on misunderstandings, irrelevant factors, or issues unrelated to the quality of the item itself. This guideline outlines when and how we handle review disputes.

##### Criteria for Removing a Review

We may remove a review if it meets **one or more** of the following criteria:

* **Spam or Abuse:** The review contains offensive language, harassment, or unrelated spam content.
* **Misuse of the Review System:** The review is about unrelated topics (e.g., FlutterFlow features, pricing, unrelated bugs).
* **Critical Misunderstanding:** The review is based on a clear misunderstanding of the item's purpose or scope, despite the listing being accurate and transparent.
* **Irrelevant to the Current Version:** The review references issues that have since been resolved, and the creator has updated the item significantly.

> **Note:** We may remove outdated reviews in cases where leaving them would misrepresent the current product.

##### Reviews That Meet Our Standards

We **will not remove** a review just because it is negative if it:

* Represents a real user experience
* Critiques the item's quality, usability, documentation, or performance in good faith
* Highlights friction that future buyers may encounter, even if subjective

##### How to Dispute a Review

If you believe a review on your item qualifies for removal:

1. **Contact Us:** Email <marketplace@flutterflow.io>.

2. **Include:**

   * A link to the item and review
   * A short explanation of why you believe it qualifies for removal

Decision

Our team will review each case individually and respond within **10 business days**. Please note we are actively working on better creator tools to allow creators to reply directly to reviews.

---

### Item Submission Criteria {#item-submission-criteria}

*Learn about marketplace item submission criteria.*

**Source:** https://docs.flutterflow.io/marketplace/creators-hub/submission-criteria

#### Item Submission Standards

Below, you'll find the criteria our Submission Review Team uses to review items submitted to FlutterFlow Marketplace.

##### 1. Originality and Ownership

###### 1.1 Project Ownership

* **Criteria:** You must own the rights to the project you submit.

* **Why it Matters:** Only the original creator has the right to share and potentially sell their work. This ensures fairness, prevents unauthorized distribution, and protects intellectual property.

* **What To Do:**

  * **If you're the sole creator:** Great! Make sure you're submitting the project from your own FlutterFlow account.
  * **If you're collaborating:** The project owner should be the one to submit it to Marketplace. Discuss this with your collaborators beforehand.
  * **If you've acquired a project:** Ensure the original creator has officially [transferred ownership](https://docs.flutterflow.io/resources/projects/collaboration#transferring-project) rights to you. This may involve legal documentation, so it's important to handle it properly.

###### 1.2 Significant Edits Made

* **Criteria:** Projects must demonstrate a substantial amount of original work and editing.

* **Why It Matters:** The Marketplace thrives on innovation and creativity. Minor cosmetic tweaks to existing projects don't offer the same value as fundamentally unique creations or heavily modified versions showcasing your distinct design and development skills.

* **What To Do:**

  * **Highlight your modifications:** Clearly demonstrate the unique components, functionalities, or design choices you've implemented.
  * **Go beyond superficial changes:** If your modifications are primarily visual (e.g., color swaps, logo replacements), consider adding more substantive improvements.

###### 1.3 Not Based on an Existing Marketplace Item

* **Criteria:** Projects must not be direct derivatives of existing Marketplace items.

* **Why It Matters:** Originality is key! Duplicating existing offerings diminishes the diversity and value of Marketplace. We want to empower users with a wide range of unique choices.

* **What To Do:**

  * **Draw inspiration, don't duplicate:** While you can certainly learn from existing projects, aim to differentiate yours significantly.
  * **Add your own flavor:** Infuse your unique style, features, or functionalities to make the project distinctively yours.

###### 1.4 Not Based on a Sample App

* **Criteria:** Submissions should not be minimally modified versions of FlutterFlow's provided sample apps.

* **Why It Matters:** Sample apps are fantastic learning tools, but Marketplace items should showcase a higher level of complexity and original thought.

* **What To Do:**

  * **Use sample apps as a foundation:** Treat them as a starting point. Experiment, expand, and transform them into something new.
  * **Demonstrate advanced skills:** Go beyond basic layouts and features; integrate custom code, complex animations, or add helpful API calls.

###### 1.5 Original Project Content

* **Criteria:** All project content—text, images, designs—must be original or appropriately licensed for commercial use. Please see [Legal Guidelines for Creators](https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators) and [Navigating External Licenses](https://docs.flutterflow.io/marketplace/creators-hub/navigating-external-licenses) for more info.

* **Why It Matters:** Using copyrighted material without permission can lead to legal issues and undermines the professional nature of Marketplace.

* **What To Do:**

  * **Create your own assets:** This is the best way to ensure originality.
  * **Use royalty-free resources and properly licensed code:** Several websites offer high-quality, free-to-use assets. See also our guidance on [Open Source Licenses](https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators#open-source-licenses).
  * **Purchase commercial licenses:** If you choose to use paid assets, secure the appropriate license for commercial distribution. This can be really tricky, so please review [Licenses from Other Marketplaces](https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators#open-source-licenses) and [Navigating External Licenses](https://docs.flutterflow.io/marketplace/creators-hub/navigating-external-licenses).

###### 1.6 No Library Dependencies (Libraries Only)

* **Criteria:** Libraries cannot depend on other libraries.
* **Why It Matters:** Dependencies between libraries create complexity in permissions management and version control, potentially leading to compatibility issues or broken functionality.
* **What To Do:**
  * **Build Self-Contained:** Ensure your library contains all necessary functionality without requiring other libraries (from Marketplace or personal libraries).

> **Info:** When you publish a free item to Marketplace, you agree to license it under the [MIT License](https://opensource.org/licenses/MIT), which grants users perpetual rights to use, modify, and distribute the project. Paid items are subject to the license terms specified in our [Marketplace Terms of Service](https://www.flutterflow.io/tos-marketplace).

While creators may remove their items from Marketplace at any time, this does not affect the rights of users who obtained the item while it was published - they retain their license rights according to the terms that were in effect when they acquired the item.

Please review our [Legal Guidelines for Creators](https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators) for more details about licensing and intellectual property rights.

##### 2. Metadata

Clear, engaging, and accurate metadata helps users discover and understand the value of your project.

###### 2.1 Submission in English

* **Criteria:** All item metadata (title, description, tags, etc.) must be in English.
* **Why it Matters:** To ensure a broad understanding among our global community, all Marketplace items must be in English.
* **What To Do:** Use clear, concise English throughout your submission. If English isn't your first language, consider using FlutterFlow's automatic [translation](https://docs.flutterflow.io/concepts/localization) feature.

###### 2.2 Professional Title

* **Criteria:** Your project title should be clear, concise, and free of grammatical errors.

* **Why it Matters:** A strong title grabs attention and communicates the essence of your project at a glance.

* **What To Do:**

  * **Keep it brief and impactful:** Aim for a title that's easy to remember and accurately reflects the core purpose of your project.
  * **Use relevant keywords:** This helps users find your project when searching on Marketplace.
  * **Proofread carefully:** Typos and grammatical errors create a negative first impression.

###### 2.3 Unique Title

* **Criteria:** Your title should be distinct from other items in Marketplace.

* **Why it Matters:** A unique title helps your project stand out and prevents confusion among users.

* **What To Do:**

  * **Research existing titles:** Before settling on a title, do a quick search to make sure it isn't already in use.
  * **Get creative with wording:** If you find similar titles, brainstorm alternative phrases or keywords that accurately describe your project's unique selling points.

###### 2.4 Professional Description

* **Criteria:** Your project description should be well-written, engaging, and free of grammatical errors.

* **Why it Matters:** The description provides users with a deeper understanding of your project's features, benefits, and intended use cases.

* **What To Do:**

  * **Start with a strong opening:** Capture attention from the start and clearly state what your project does.
  * **Highlight key features:** Use bullet points or formatting to make it easy to scan for important information.
  * **Focus on benefits:** Explain *why* someone would want to use your item – what problems does it solve or what opportunities does it unlock?
  * **Proofread meticulously:** Errors in grammar and spelling can make your project seem unprofessional.

> **Warning:** While tools like ChatGPT can assist in drafting content, they often generate generic text that might not fully capture the unique aspects of your project or could sound overly promotional and insincere. Always personalize and proofread AI-generated content to ensure it aligns with your item's features and capabilities.

###### 2.5 Accurate Description

* **Criteria:** The description should accurately reflect the project's functionality and avoid exaggerating its capabilities.

* **Why it Matters:** Misleading descriptions lead to negative user experiences. Transparency builds trust within Marketplace.

* **What To Do:**

  * **Be truthful and transparent:** Clearly state what your project can and cannot do.
  * **Avoid hype and jargon:** Focus on clear, concise language that everyone can understand. Do not overpromise.

###### 2.6 Third-Party Service Information

* **Criteria:** If your project relies on any external services or APIs, you must disclose this information in the description.

* **Why it Matters:** Transparency about potential additional costs or dependencies ensures users have all the information needed to make an informed decision before purchasing or cloning an item.

* **What To Do:**

  * **List all external services:** Include the name of the service, its purpose within your project, and whether it requires a paid subscription or API key.
  * **Provide links (if applicable):** Direct users to relevant documentation or pricing pages for the third-party service.

###### 2.7 Professional Instructions

* **Criteria:** Instructions and documentation should be clear, easy to follow, and written in a professional tone.

* **Why it Matters:** Well-written instructions ensure a smooth setup and implementation experience for users, increasing customer satisfaction.

* **What To Do:**

  * **Assume no prior knowledge:** Write for someone who's completely new to your project and FlutterFlow.
  * **Use numbered steps:** Break down complex processes into manageable, actionable steps.
  * **Include video links:** Use the documentation URL to point users to a visual video walkthrough. Alternatively, point users to a Google Doc or similar written documentation for your item.
  * **Test your instructions:** Have someone else follow your instructions to identify any points of confusion.

###### 2.8 Accurate Tags

* **Criteria:** Use relevant tags that accurately describe your project's category, features, and functionality.

* **Why it Matters:** Tags play a crucial role in helping users discover your project through Marketplace search.

* **What To Do:**

  * **Think like a user:** What keywords would someone use to search for a project like yours?
  * **Use a mix of broad and specific tags:** For example, use general tags like "e-commerce" or "social media" along with more specific ones like "shopping cart" or "user authentication".
  * **Don't use irrelevant tags:** This only makes it harder for users to find what they're looking for.

###### 2.9 High-Quality Images

* **Criteria:** Images should be visually appealing, high-resolution, and representative of the project's design and functionality. Cover images should be at least 1200 x 800 pixels and in 1.5 aspect ratio.

* **Why it Matters:** Images are the first thing users see – make a great visual impression!

* **What To Do:**

  * **Showcase key screens and features:** Select images that highlight the most visually impressive and important aspects of your project.
  * **Use high-resolution images:** Avoid blurry or pixelated images.
  * **Maintain a consistent style:** Use similar image dimensions and visual treatments to create a cohesive look.

> **Tip:** Use FlutterFlow's [**screenshot generator**](https://docs.flutterflow.io/deployment/pre-checks-before-publishing#generate-screenshots) along with services like [**Shots.so**](https://shots.so/) to create beautiful cover images.

###### 2.10 Image Representativeness

* **Criteria:** Images must accurately reflect the actual content and functionality of your project.

* **Why it Matters:** Misleading images create a negative experience for users and erode trust in Marketplace.

* **What To Do:**

  * **Use genuine screenshots or recordings:** Avoid showcasing designs or features that are not actually present in your project.
  * **Use abstract images sparingly:** While a certain level of abstraction or illustration can be effective for concepts that are hard to capture with screenshots, they should be used judiciously. Prefer to showcase actual product screenshots in your gallery images.

###### 2.11 No FlutterFlow Logo in Images

* **Criteria:** Do not include the FlutterFlow logo in your cover photos.
* **Why it Matters:** Using the FlutterFlow logo might suggest an official endorsement or the appearance of an official template, neither of which may be accurate. Additionally, including the logo is redundant, as all items are exclusively offered through the FlutterFlow Marketplace.
* **What To Do:** Remove any references to the FlutterFlow logo in your images.

##### 3. Aesthetics & Design

First impressions matter! We're looking for projects that go beyond basic functionality and demonstrate a strong understanding of visual design principles.

###### 3.1 Design Standard

* **Criteria:** Projects should adhere to high standards of visual design, incorporating principles of usability, accessibility, and aesthetics.

* **Why it Matters:** A well-designed app is not just visually appealing; it's intuitive, easy to navigate, and provides a positive user experience.

* **What To Do:**

  * **Prioritize usability:** Make sure your design choices support, rather than hinder, the core functionality of your app.
  * **Consider visual hierarchy:** Guide the user's eye with clear visual cues – size, color, contrast, and spacing can all be used effectively.
  * **Maintain consistency:** Aim to use a theme colors and typography throughout your project, as well as consistent padding, list spacing, border radii, and navigation elements.
  * **Test with real users:** Get feedback from others to identify any areas of your design that are confusing or frustrating to use.

###### 3.2 Screen Size Compatibility (Responsiveness)

* **Criteria:** Projects should be designed to adapt seamlessly to various screen sizes.

* **Why it Matters:** Users expect Flutter apps to scale appropriately across a wide range of devices, from small smartphones to large desktop monitors. A responsive design ensures a positive user experience across the board.

* **What To Do:**

  * **Follow responsive design best practices:** Use `Wrap`, Responsive Visibility, and Flex features to ensure your app can scale across devices. Read more about building responsively in [Responsive Layouts: 101](https://docs.flutterflow.io/concepts/layouts/responsive).
  * **Test on different devices:** Use FlutterFlow's different virtual devices in Test and Run Modes to test your project on a variety of screen sizes. Experiment with the canvas size in the builder to check how your designs scale.

##### 4. Test Experience

A seamless and positive test experience is crucial for users to evaluate your FlutterFlow item before purchasing or cloning. This section focuses on ensuring your submission is functional, accessible, and easy to explore.

###### 4.1 Functional Run Mode Link

* **Criteria:** The provided Run Mode link must be active and correctly load a working demo of your project. For mobile-only features or utility libraries that cannot be demonstrated in Run Mode's web environment, you must provide alternative demonstration methods.

* **Why it Matters:** The Run Mode link is the primary way users can interact with your project before purchasing. A broken, inaccessible, or non-demonstrative link creates a significant barrier to understanding the item's value.

* **What To Do:**

  * **For Standard Web-Compatible Items:**

    * Double-check your link before submitting to confirm it showcases the experience you want potential buyers to have.
    * Test the link multiple times to ensure consistent functionality.

  * **For Mobile-Only Features:**

    * Create a dedicated demonstration page in your project that explains the mobile-only functionality.
    * Include screenshots, videos, or mockups showing how the feature works on mobile devices.
    * Clearly indicate which features are mobile-only and why they cannot be demonstrated in Run Mode.
    * Optionally, provide a published FlutterFlow web deploy link that can be used instead of the Run Mode URL.

  * **For Utility Libraries (e.g., Analytics, Background Services):**

    * Create a demonstration page that explains the library's functionality.
    * Show configuration options and expected outcomes.
    * Include visual aids like flowcharts or diagrams to explain the library's operation.
    * Provide example code or configuration snippets.
    * Consider adding debug/test outputs that demonstrate the library is working.

  * **Documentation:**

    * Regardless of the type of item, ensure your documentation clearly explains how to implement and test the functionality in a real mobile environment.
    * Include troubleshooting guides and common implementation scenarios.

> **Tip:** For items that cannot be fully demonstrated in Run Mode, focus on creating a clear, informative demonstration page that helps users understand the value and implementation of your item. Visual aids, clear explanations, and comprehensive documentation are key to helping users make informed decisions.

###### 4.2 User Sign-In (Anonymous Auth)

* **Criteria:** Users should be able to explore the core functionality of your item *without* being required to create an account or log in.

* **Why It Matters:** Requiring upfront authentication creates friction for users who simply want to try before they buy. Additionally, forcing users to provide personal information could cause privacy issues. Anonymous authentication allows for immediate exploration.

* **What To Do:**

  * **Provide pre-filled demo credentials:** If your demo relies heavily on user-specific data, consider creating a demo account with pre-populated sample data accessible to guest users. Pre-fill the username and password on the sign in screen so that users can easily begin exploring your item.
  * **Implement anonymous authentication:** FlutterFlow supports easy integration with Firebase for [anonymous sign-in](https://docs.flutterflow.io/integrations/authentication/firebase/anonymous-login). This allows users to access your project's demo mode without creating an account.
  * **Remove authentication:** Another option is to remove the need for any authentication altogether. This will enable users to start exploring your item immediately without any barriers.

###### 4.3 Accessible Navigation

* **Criteria:** All pages and sections within your project should be easily navigable and accessible.

* **Why it Matters:** A confusing or broken navigation flow creates a frustrating user experience. Users should be able to intuitively explore all aspects of your project.

* **What To Do:**

  * **Configure the Initial Page Properly**: In Settings > App Details, the 'Entry Page' determines the starting point for Run Mode links and the initial page users will see when they enter your app. Make sure this is set to the most logical and welcoming page to ensure a smooth user entry and navigation experience.
  * **Review your project's [Storyboard](https://docs.flutterflow.io/flutterflow-ui/storyboard) view:** This view displays the navigation across various pages and can help highlight any gaps. Please note that any page which is not accessible will not be shown.
  * **Test navigation thoroughly:** Click through *every* button, link, and menu item in Run Mode to make sure they lead to the correct destinations.

###### 4.4 Functional Template

* **Criteria:** All core features and functionalities within your project must be working correctly.

* **Why it Matters:** Broken features or functionalities lead to a negative user experience and give the impression of a rushed or incomplete project.

* **What To Do:**

  * **Rigorous testing is essential:** Test *every* aspect of your project – from button clicks and form submissions to API calls and animations.
  * **Emulate real-world scenarios:** Don't just test with ideal data or happy paths. Introduce potential edge cases or user errors to see how your project handles them.
  * **Get fresh eyes on it:** Ask someone unfamiliar with your project to test it and provide feedback.

##### 5. Build Quality

Building a solid app template goes beyond surface-level design. It's about creating a robust, efficient, and user-friendly project that can scale and makes efficient use of components. This section focuses on technical excellence and attention to detail.

###### 5.1 Error-Free Functionality

* **Criteria:** Projects should be free of runtime errors, crashes, and unexpected behaviors.

* **Why it Matters:** Errors and crashes create a frustrating user experience and can damage the reputation of your project.

* **What To Do:**

  * **Review project errors and optimizations:** Do not submit projects with any errors, and attempt to address most optimization suggestions in the top bar.
  * **Use FlutterFlow's debugging tools:** Take advantage of FlutterFlow's built-in debugging panel to identify and resolve issues.
  * **Handle nulls and errors gracefully:** Add default values for variables in case their value is ever `null`. Implement conditionals in action chains to respond appropriately to API errors or other cases when something goes wrong.

###### 5.2 No Pixel Overflow

* **Criteria:** Ensure your UI elements are positioned and sized correctly to avoid content overflowing its container, leading to visual glitches / cut off content.

* **Why It Matters:** Pixel overflows are a sign of UI inconsistencies that can negatively impact the user experience, especially on different screen sizes. Pixel overflow issues can occur in Test Mode when there's a hardcoded pixel value and not enough space on the screen to render that exact value.

* **What To Do:**

  * **Preview pixel overflows:** Toggle the pixel overflow icon in the top-right of the canvas to see if there are any overflow issues.
  * **Leverage FlutterFlow's layout tools:** Use Expanded and Flex values to help prevent layout issues. Make `Columns` or `Rows` scrollable to prevent overflows. Use auto-sizing text or text clipping where it makes sense. Remove hard-coded width and height where it makes sense.
  * **Test on different screen sizes:** Resize the canvas while building to preview any potential issues.

###### 5.3 Error-Free Custom Code

* **Criteria:** Any custom code integrated into your project (using Custom Functions, Actions, and Widgets) must be free of syntax errors, logical errors, and potential security vulnerabilities.

* **Why it Matters:** Errors in custom code can lead to app instability, crashes, or even security risks.

* **What To Do:**

  * **Write clean, well-documented code:** This makes it easier to debug and maintain your project.
  * **Test custom code thoroughly:** Isolate and test your custom code units (functions, actions) to ensure they work as expected.
  * **Use FlutterFlow's code validation:** Pay close attention to any warnings or errors highlighted by FlutterFlow's built-in code validation.

###### 5.4 Coherent & Relevant Custom Code

* **Criteria:** Custom code should be purposefully integrated and enhance your project's functionality in a meaningful way. Avoid unnecessary or redundant code. Avoid including unused or irrelevant custom code.

* **Why it Matters:** While custom code offers flexibility, excessive or poorly integrated code can make your project harder to understand, maintain, and update in the future.

* **What To Do:**

  * **Plan your custom code strategically:** Determine if FlutterFlow's built-in features can achieve the desired functionality before resorting to custom code.
  * **Comment your code effectively:** Explain the purpose and logic behind your custom code to improve readability and maintainability.
  * **Keep it modular:** Break down complex logic into smaller, reusable functions or actions. Prefer code blocks when a Custom Function is relatively short and will only be used once.

###### 5.5 Testable Custom Code in Run Mode

* **Criteria:** Ensure that the functionality implemented using custom code is accessible and verifiable within the Run Mode demo.

* **Why It Matters:** Users should be able to experience the full impact of your custom code item within the Run Mode environment.

* **What To Do:**

  * **Add a page that uses your custom code:** This page should ideally expose the ideal use case of your custom code or perhaps allow users to set and control parameter values in Run Mode.
  * **Provide clear instructions:** If special steps are required for users to test certain custom code functionalities in Run Mode, explain these instructions clearly within your project description or documentation.

###### 5.6 Proper Firestore Rules (If Applicable)

* **Criteria:** If your project utilizes Firestore as a database, ensure your Firestore Security Rules are correctly configured in Settings to protect user data and prevent unauthorized access.

* **Why it Matters:** Improperly configured Firestore Rules can expose sensitive user data or create security vulnerabilities within users' apps.

* **What To Do:**

  * **Implement Firestore Security Rules:** Familiarize yourself with how FlutterFlow exposes [Firestore rules](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-rules) and make the necessary modifications in your base project.
  * **Test your rules thoroughly:** Create test accounts and attempt add, update, and delete operations on your data across different authentication states to verify your rules are working as intended.

###### 5.7 Spelling and Grammar

* **Criteria:** Maintain a professional tone with correct spelling and grammar throughout your project's UI text, descriptions, and documentation.
* **Why it Matters:** Even small typos can detract from your project's credibility and create a negative user experience.
* **What To Do:**
  * **Proofread, proofread, proofread:** Carefully review all text elements within your project. Ask a friend or colleague to review your text for errors.

###### 5.8 User-Friendly Template

* **Criteria:** Your template should empower users to build upon it easily and intuitively, regardless of their FlutterFlow expertise.

* **Why It Matters:** A user-friendly template increases its value and appeal. When users can quickly understand and customize your template, they're more likely to choose it, leading to greater success for your Marketplace item.

* **What To Do:**

  * **Embrace reusable components:** Design your template with modularity in mind. Create reusable components that users can easily modify for their use case.
  * **Clear and concise naming conventions:** Use descriptive names for widgets, variables, and functions to make your template's structure understandable at a glance.
  * **Logical organization:** Structure your template's layout in a clear and logical manner, grouping related elements and using comments to guide users.
  * **Documentation is key:** Provide clear and comprehensive documentation that guides users on how to use and customize your template effectively. Include explanations of key features, customization options, and potential use cases.
  * **Test with diverse users:** Get feedback from users with varying levels of FlutterFlow experience. This helps identify potential pain points or areas where your template could be more user-friendly.

###### 5.9 Appropriate State Management

* **Criteria:** Implement state management effectively to ensure data is updated and reflected correctly across your application.

* **Why it Matters:** Proper state management is crucial for building responsive and dynamic Flutter apps. It helps prevent data inconsistencies, improves performance, and makes your code easier to maintain.

* **What To Do:**

  * **Choose the right state management scope:** FlutterFlow supports (1) [App State](https://docs.flutterflow.io/resources/data-representation/app-state) (2) [Page State](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#page-state) and (3) [Component State](https://docs.flutterflow.io/resources/ui/components/component-lifecycle#creating-a-component-state) variables. Familiarize yourself with these options and scope any state variables to where they are needed. For instance, do not use App State to control the value of a checkbox within a component.
  * **Rebuild efficiently:** Ensure changes to state rebuild only the necessary scope for efficiency.

###### 5.10 Organized Widget Tree

* **Criteria:** Maintain a well-structured and organized widget tree within your FlutterFlow project.

* **Why It Matters:** A clean and organized widget tree makes your project more understandable, maintainable, and less prone to errors. It also makes it easier for others to collaborate on your project.

* **What To Do:**

  * **Use descriptive names for widgets and variables:** Make your code self-documenting by using clear and meaningful names for major nodes.
  * **Avoid deeply nested widgets:** If your widget tree becomes too deeply nested (>10 levels), consider breaking it down into smaller, reusable [components](https://docs.flutterflow.io/resources/ui/components).

###### 5.11 Follow FlutterFlow Best Practices

* **Criteria:** Adhere to recommended best practices and guidelines for building apps with FlutterFlow.
* **Why It Matters:** Following best practices can help you avoid common pitfalls, improve the performance of your app, and ensure your project is compatible with future updates to FlutterFlow.
* **What To Do:**
  * **Stay up-to-date:** Keep an eye on FlutterFlow's official documentation, blog posts, and community forums for the latest tips, tricks, and best practices.

> **Info:** Stay tuned for an upcoming "style guide" we're publishing that goes into deeper detail about best practices for building in FlutterFlow.

###### 5.12 Limit Static Images

* **Criteria**: Minimize the use of large, unoptimized static images within your project to prevent app bloat and ensure that your template accurately represents the functionality of your app.

* **Why It Matters**: Overusing large static images not only increases the download size and slows down performance, particularly on slower networks, but also risks misleading users. For example, using an image of a map or a credit card form, rather than building these elements, can give the false impression that your app includes functionalities that are merely visual mockups. This can disappoint users when they discover these components are non-interactive.

* **What To Do**: * **Build Functional Components**: Wherever possible, replace static images with functional elements built using FlutterFlow. This ensures your app remains scalable and interactive, providing a genuine user experience across all device sizes and orientations.
  * **Use optimized images**: Reduce image file size using online compression tools, which maintain quality while decreasing load times.
  * **Leverage caching**: Implement image caching for network images to minimize repeated downloads of the same images, which enhances performance.

###### 5.13 Limit Custom Code (When Possible)

* **Criteria:** While custom code is powerful, strive to achieve as much functionality as possible using FlutterFlow's visual builder and built-in features.
* **Why It Matters:** Over-reliance on custom code can make your project less maintainable, less user-friendly, and potentially more prone to errors.
* **What To Do:**
  * **Explore FlutterFlow's capabilities:** Familiarize yourself with FlutterFlow's extensive library of pre-built widgets, actions, and integrations to see if they can fulfill your requirements before resorting to custom code.

###### 5.14 Efficient Component Use & Avoiding Duplication

* **Criteria:** Projects should demonstrate efficient use of FlutterFlow's components. Avoid unnecessary duplication of pages, widgets, or actions. Strive to create reusable components and implement action blocks in a scalable and maintainable way.

* **Why it Matters:** Duplicating large sections of code or entire pages with only minor changes bloats the project size, reduces maintainability, and can mislead users about the project's complexity and value.

* **What To Do:**

  * **Leverage Components:** Create reusable components for elements that repeat throughout your project (e.g., product cards, list items, headers, footers).
  * **Utilize Parameters:** Pass data and customize component instances using parameters instead of duplicating and hardcoding values.
  * **Review for Redundancies:** Before submitting, carefully examine your project for any unnecessarily duplicated pages, widgets, or action chains that could be consolidated or streamlined.

###### 5.15 Library Values Implementation (Libraries Only)

* **Criteria:** Libraries must use [Library Values](https://docs.flutterflow.io/resources/projects/libraries) for sensitive keys and customizable elements that users need to configure.

* **Why It Matters:** Library Values allow users to safely provide their own API keys and customize critical configuration without modifying the library's core functionality. This improves security and makes libraries more flexible and reusable.

* **What To Do:**

  * **Identify Configurable Elements:** Review your library for any API keys, endpoints, or other values that users should be able to customize.
  * **Create Library Values:** Set up Library Values for these configurable elements in Settings > App Settings > Publish as Library.
  * **Document Requirements:** Clearly explain in your item description if any Library Values are required for your library to function correctly.
  * **Test Configuration:** Verify that your library functions correctly when Library Values are changed by users.

###### 5.16 Automated Tests (Strongly Recommended)

* **Criteria:** Projects should include automated tests that verify core functionality and key user workflows. While not required for approval, this is strongly recommended for libraries and will positively impact visibility.

* **Why It Matters:** Automated tests help ensure reliability, catch regressions, and demonstrate your commitment to quality. They also improve your item's visibility.

* **What To Do:**

  * **Add Integration Tests:** Use FlutterFlow's [automated testing](https://docs.flutterflow.io/testing/automated-tests) features to verify your item's core functionality.

  * **Test Key Workflows:** Focus on testing critical user paths and features that users will rely on.

  * **For Libraries:** Since libraries are often used as building blocks in larger applications, thorough testing is particularly important to: * Verify that Library Values are properly implemented
    * Ensure core functionality works across different configurations
    * Demonstrate expected behavior to potential users
    * Catch issues before they affect downstream applications

##### 6. Value (Paid Items)

A successful Marketplace item goes beyond just a functional app—it provides real value to users.

###### 6.1 High Value Proposition

* **Criteria:** Items should offer a compelling value proposition that justifies their price.

* **Why It Matters:** Users are looking for solutions that save them time, effort, or resources, or that provide a unique experience they can't easily find elsewhere.

* **What To Do:**

  * **Define Your Unique Value**: Identify and articulate what sets your project apart from others. Ensure it solves a specific problem in a way that is not readily available in Marketplace.

  * **Tag Appropriately**: Accurately categorize your item—whether it's a full app, UI kit, or library—to set the right expectations for potential users.

  * **Justify Your Pricing**: Make sure the pricing of your item reflects its true value and stands in fair comparison to similar offerings. Ensure it offers enough depth and uniqueness to warrant the minimum price point.

  * **For Paid Libraries**: Libraries should excel in at least one of these areas: * 🧘 Simplifying technical complexity (ease)
    * ⚡️ Enabling quick and seamless integrations (speed)
    * 🎛️ Offering diverse reusable components and features (quantity)
    * 🛠️ Providing robust, reliable functionality (quality)
    * 🙋‍♂️ Addressing specific, high-demand use cases with thoughtful solutions (relevance)

##### 7. Legal & Security

Building trust in the FlutterFlow Marketplace requires respecting legal boundaries and safeguarding user information. This section covers essential considerations to ensure your project adheres to ethical and legal standards.

###### 7.1 Free of Inappropriate Content

* **Criteria:** Projects must not contain any offensive, discriminatory, or illegal content. This includes, but is not limited to: * Hate speech or discrimination
  * Sexually explicit material or pornography
  * Content that promotes violence, illegal activities, or harm to others

* **Why it Matters:** Maintaining a safe and inclusive community is paramount. Inappropriate content violates the [FlutterFlow Terms of Service](https://flutterflow.io/tos) and may have legal ramifications.

* **What To Do:**

  * **Review your content carefully:** Ensure all text, images, and other assets align with community standards and legal guidelines.
  * **Err on the side of caution:** When in doubt, it's best to avoid potentially controversial content.

###### 7.2 Free of Copyrighted Material

* **Criteria:** Projects must not include any unauthorized use of copyrighted material, such as: * Images, illustrations, or graphics
  * Music or sound effects
  * Code snippets or libraries — see our docs on [Open Source Licenses](https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators#open-source-licenses) for details

* **Why it Matters:** Using copyrighted material without permission is a legal infringement and can result in serious legal consequences, including [DMCA takedown](https://docs.flutterflow.io/marketplace/creators-hub/copyright-dmca-process).

* **What To Do:** Please review our [Legal Guidelines for Creators](https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators) and [Navigating External Licenses](https://docs.flutterflow.io/marketplace/creators-hub/navigating-external-licenses) for more details.

###### 7.3 Free of Trademarked Material

* **Criteria:** Items must not misuse or infringe upon registered trademarks, including: * Brand names
  * Logos
  * Slogans

* **Why it Matters:** Trademark infringement can lead to legal disputes and damage the reputation of FlutterFlow Marketplace. Please see our [Legal Guidelines for Creators](https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators) for more details.

* **What To Do:** Please review our [Legal Guidelines for Creators](https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators) for more details.

###### 7.4 Free of Confidential Data

* **Criteria:** Projects should not expose any sensitive or confidential information, including: * API keys
  * User credentials
  * Personal data (e.g., names, addresses, financial information)

* **Why it Matters:** Exposing confidential data can compromise the security of your project and put users at risk.

* **What To Do:**

  * **Follow [API Key Best Practices](https://docs.flutterflow.io/best-practices/secure-api-keys):** Add restrictions, delete unnecessary API keys, and regularly rotate your keys to ensure keys are secured.
  * **Require users to provide their own API keys:** Use ephemeral, user-provided API keys in calls rather than hardcoding your own keys directly into code.
  * **Scrub your project before submission:** Double-check your project files and codebase to ensure no confidential information is accidentally included.

#### Common Rejection Reasons

To help streamline your submission process, here are some of the most frequent reasons projects are flagged:

* [**Lack of Anonymous Authentication**](https://docs.flutterflow.io/marketplace/creators-hub/submission-criteria#42-user-sign-in-anonymous-auth): Make it easy for users to test your project without requiring logins.
* [**Unclear Usage Instructions**](https://docs.flutterflow.io/marketplace/creators-hub/submission-criteria#27-professional-instructions): Provide detailed, step-by-step guidance on how to use and customize your template.
* [**Image Issues**](https://docs.flutterflow.io/marketplace/creators-hub/submission-criteria#29-high-quality-images): Ensure images are high-resolution, sized appropriately, and don't include the FlutterFlow logo.
* [**Poor Widget Tree Organization**](https://docs.flutterflow.io/marketplace/creators-hub/submission-criteria#510-organized-widget-tree): Utilize components and naming effectively to create a clean, well-structured project.
* [**Use of Copyrighted Assets**](https://docs.flutterflow.io/marketplace/creators-hub/submission-criteria#72-free-of-copyrighted-material): Only include assets that you have created or have the legal right to use commercially.
* [**Library Dependencies**](https://docs.flutterflow.io/marketplace/creators-hub/submission-criteria#515-library-values-implementation-libraries-only): Libraries cannot currently depend on other libraries from Marketplace.

We're excited to see the amazing FlutterFlow projects you bring to Marketplace! By following these guidelines, you'll help us maintain a high-quality platform that benefits the entire FlutterFlow community. **Let's build something incredible together!** 🚀

---

### Submitting Item for Review {#submitting-item-for-review}

*Learn how to submit an item to the FlutterFlow Marketplace.*

**Source:** https://docs.flutterflow.io/marketplace/creators-hub/submit-item-for-review

All items submitted to the Marketplace are subject to a comprehensive review process prior to publication. While we have recently significantly improved review times, please note that the review period can take up to 30 days depending on the complexity and volume of submissions.

Important: Review Submission Policies

Please review our [**Submission Guidelines**](https://docs.flutterflow.io/marketplace/creators-hub/submission-criteria) and our [**Marketplace Terms of Service**](https://flutterflow.io/tos-marketplace) before submitting your item. It may also be helpful to review our [**Legal Guidelines for Creators**](https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators), which explain your legal responsibility in plain language.

#### How to Submit an Item

An item can be an entire project (in the case of Temlate Apps or Libraries), a page or a component (in the case of Template Page & Components) or a Custom Function, Action or Widget (in the case of Custom Code).

##### 1. Set your project as a Marketplace project

Marketplace items should belong to projects that are specifically made to publish Marketplace items (i.e., they should not be inside of a production project).

In order to submit an item, it must be inside of a project that has been Set For Marketplace. A project that is set for Marketplace can not be deployed.

To set a project for Marketplace:

1. Prerequisite: please enroll as a Marketplace creator first by setting up a profile in [Marketplace](https://marketplace.flutterflow.io/profile). You can optionally also apply to become a paid creator, which allows you to monetize your items.
2. Select the [**Share Icon**](https://docs.flutterflow.io/flutterflow-ui/toolbar#share-project) from the Toolbar (top right side of the screen). Please note that you must be the project owner to see this icon and to submit an item.
3. Select **Create New Item > Set For Marketplace > Yes**

> **Tip:** You can also clone an existing project and then set it as a Marketplace Project.

##### 2. Fill out the submission form

Below is an overview of what is needed to create your Marketplace item:

> **Tip:** If you aren't ready to submit your item, select **Save As Draft** to continue editing your submission at a later time.

###### Cover Photo

The cover photo should be **1200x800 pixels** and help the users understand the purpose of the item. GIFs are allowed but should not be distracting, focus solely on the use and/or usability of the template, and be highly optimized to ensure a smooth load on the platform. Please do not include the FlutterFlow logo in your cover image.

###### Gallery Photos (optional)

Include up to 4 additional photos that showcase your item's features. GIFs are allowed but should not be distracting, focus solely on the use and/or usability of the template, and be highly optimized to ensure a smooth load on the platform.

Each should be should be **1200x800 pixels**.

###### Name

The item name should be professional, unique, and help the users understand the purpose of the item. Please use correct grammar and capitalization.

###### Description

The description should provide an overview of the key features, helping users determine if the item aligns with their requirements.

If the item includes any third-party paid services or pub.dev packages/dependencies, those should also be mentioned in the description. Please use correct grammar and capitalization.

###### Usage Instructions

Provide clear and concise instructions on how to implement and utilize your item within FlutterFlow. Include any necessary steps, code snippets, or configurations required to get started. If your item depends on any third party services or pub.dev packages/dependencies, please provide full details of these including showing users where to find relevant API keys or more information. Please use correct grammar and capitalization.

###### Marketplace Item Type

Four types of items can be submitted:

* Libraries
* Template Apps
* Template Page or Components
* Custom Code

- Libraries
- Template App
- Page or Component
- Custom Code

Libraries allow you to share resources like API endpoints, UI components, custom data types, custom code, action blocks and more with complete version control.

To submit a Library to the Marketplace, first publish your project as a Library. Note that there are some limitations on Library projects - most notably there is currently no support for Firebase or Pages.

For more details, see the [documentation on Libraries](https://docs.flutterflow.io/resources/projects/libraries).

> **Note:** *Libraries* can be monetized. The minimum price for Libraries is $50.

Template apps contain multiple screens. There are 2 sub-types:

* **Full App:** an app with authentication, complete navigation, multiple pages/flows, database schema, complete action trees, etc.
* **UI Kit**: purely design-based templates and layouts

> **Note:** *Template Apps* can be monetized. The minimum price for Full Apps is $400 while the minimum for UI Kits is $50.

Pages or Components are assembled modules that can be used within FlutterFlow. There are 2 sub-types:

* **Page:** a single page in a FlutterFlow project
* **Component:** a reusable UI element that can be integrated into any part of your application

> **Warning:** *Pages and Components* cannot be monetized at this time.

Custom Code is Dart code that can be used within FlutterFlow projects. There are 3 sub-types:

* **Custom Functions:** synchronous functions that do not have external dependencies.
* **Custom Actions:** synchronous or asynchronous functions that may have external dependencies. If your action contains dependencies, please review our guide on [Open Source Licenses](https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators).
* **Custom Widgets:** user-defined Dart widgets that extend the capabilities of the standard FlutterFlow widget collection. If your widget contains dependencies, please review our guide on [Open Source Licenses](https://docs.flutterflow.io/marketplace/creators-hub/legal-guidelines-for-creators).

*Please note that each custom code item needs to be submitted separately.*

> **Warning:** *Custom Code* cannot be monetized at this time.

###### Template Tags (optional)

Template tags help users sort and filter items. If the tags listed don't match your item, enter your desired search terms under *Keywords*.

###### Supported Platforms

You can submit Marketplace items for Android, iOS, and Web (or all three!). Please make sure to test on all supported platforms to ensure the item works without issues or errors.

###### Run Mode URL

A Run Mode link of your Marketplace allows users to better understand how your item looks and works.

> **Info:** If your Run Mode link includes authentication functionality, please add a demo login button that uses [**Anonymous sign-in**](https://docs.flutterflow.io/integrations/authentication/firebase/anonymous-login) or pre-fill demo credentials in the email and password inputs.

###### Documentation URL

If there are complex installation or usage instructions, we highly recommend creating a documentation link for your Marketplace item. This can be written (e.g., Notion Doc, Google Doc) or video (e.g., YouTube, Loom).

##### 3. Submit your item for review

Once the Marketplace item submission form is complete, you can submit it for review. To submit a Marketplace item for review:

1. Fill out the items in the Marketplace Item Submission Form
2. Select **Submit For Approval**

Your item will be shown in your [Dashboard](https://marketplace.flutterflow.io/dashboard) under **Created Items** as "Pending Approval":

![Item in \&quot;Pending Approval\&quot;](https://docs.flutterflow.io/assets/images/image-29405d90490c33329a3a9f9ed007ae4e.avif)

##### 4. Edit an approved item

> **Info:** At this time, it is not possible to edit an approved Marketplace Item. We are working to add this functionality soon.

---

### Refund Policy {#refund-policy}

*Learn more about the refund policy of FlutterFlow marketplace.*

**Source:** https://docs.flutterflow.io/marketplace/refund-policy

> **Note:** Please note that this policy does not override the local laws concerning refunds in your country, which remain applicable where necessary.

At FlutterFlow, we're committed to ensuring that Marketplace offers high-quality templates that meet the diverse needs of our users. We understand the importance of finding the right tools to accelerate your app development, and we strive to ensure our Marketplace reflects the high standards you expect.

#### No-Refund Policy

Due to the digital nature of Marketplace items, which include access to code, design, and layout, we maintain a **no-refund policy**. This policy is clearly outlined during the purchase process near the "Buy Now" button. Each template is designed for single use, and once purchased, the buyer gains immediate access to all its contents, making returns infeasible.

#### Exceptional Circumstances

While our policy is to not offer refunds, we are committed to the satisfaction of our customers. If you encounter any of the following issues, you may be eligible for refund consideration:

1. **Major Defects:** All the items are thoroughly tested before being published, but unexpected errors may occur. Such issues must be submitted for verification. If any deficiency is confirmed, we will reach out to the item creator to address the issue and may issue a refund if we fail to address the defect within a reasonable time frame.
2. **Purchased with Incorrect Account:** If you purchased an item with a different account than you intended and have not yet used the item, we can help transfer the item to the correct account.

If you believe an item qualifies, please contact us directly by emailing <marketplace@flutterflow.io>. Each request will be considered on a case-by-case basis, and in exceptional circumstances, we may issue a refund. Such cases are handled manually and may take 5-10 days to process.

#### Feedback and Resolution

Your feedback is vital in helping us improve the quality of the offerings on our Marketplace. If the template didn’t meet your expectations, please consider:

* **Providing Feedback:** You can [rate the item](https://docs.flutterflow.io/marketplace/submit-feedback#rate-an-item) in your Marketplace dashboard, which helps us maintain quality standards and assists other users in making informed decisions.
* **Contacting the Creator:** [Reach out directly](https://docs.flutterflow.io/marketplace/submit-feedback#contact-the-item-creator) to the item creator to express any dissatisfaction.
* **Reporting Issues:** If you believe the item violates our standards or policies, please [report it](https://docs.flutterflow.io/marketplace/submit-feedback#report-an-item). We take these concerns seriously and investigate every report.

---

### Submitting Feedback for Items {#submitting-feedback-for-items}

*Learn more about the submitting feedback on FlutterFlow marketplace items.*

**Source:** https://docs.flutterflow.io/marketplace/submit-feedback

At FlutterFlow Marketplace, your feedback is crucial to improving the quality and reliability of the items available. There are three main ways to submit feedback:

#### Contact the Item Creator

For direct feedback or questions, we recommend contacting the item creator. This is great for providing constructive feedback or for support with minor item issues:

**Via Item Detail Page:**

1. Navigate to the item's detail page on Marketplace.
2. Click the **Contact the creator** button. This action will launch a new email draft with the creator's official email address pre-filled.

**Via Creator's Profile:**

1. Navigate to the creator's profile on Marketplace.
2. Click the **Contact** button. This action will copy the creator's official email address to your clipboard.
3. Send an Email to the copied email address.

#### Rate an Item

You can rate items you have used, which helps other users make informed decisions:

**Via Item Detail Page:**

1. Navigate to the item's detail page on Marketplace.
2. Navigate to the **Reviews** tab.
3. Click **Add a review**.
4. Select a star rating from 1 to 5, where 5 is the highest.
5. Optionally, add a comment to your rating. Please keep your feedback respectful and honest.

**Via Dashboard:**

1. Go to the **Usage History** tab of your [dashboard](https://marketplace.flutterflow.io/dashboard).
2. Find the item you want to rate and click on the stars next to it.
3. Select a star rating from 1 to 5, where 5 is the highest.
4. Optionally, add a comment to your rating. Please keep your feedback respectful and honest.

#### Report an Item

If you encounter any issues with an item that may require our attention, such as copyright or trademark infringements, or severe quality issues, you can report it. Reports are submitted anonymously and will alert both the creator and our Marketplace team.

1. Navigate to the item's detail page in Marketplace.
2. Click **Report this item** button.
3. Choose a report type and clearly describe the issue, including external URLs if necessary.
4. Click **Submit**

> **Tip:** If you are the original author or copyright holder of content that has been uploaded to the FlutterFlow Marketplace without your permission, you can file DMCA takedown request following the instructions in [**FlutterFlow's Terms of Service**](https://flutterflow.io/tos).

#### Review Disputes

If you're a creator and believe a review on your item was submitted inappropriately, you can learn about our review dispute process in our [Review Dispute Guidelines](https://docs.flutterflow.io/marketplace/creators-hub/review-dispute-guidelines). This covers when reviews may be removed and how to submit a dispute.

---

---

## Testing

### Automated Tests {#automated-tests}

*Discover how to effectively utilize automated testing in FlutterFlow to ensure your app performs as intended.*

**Source:** https://docs.flutterflow.io/testing/automated-tests

Automated Tests allow you to test the behavior and appearance of your app to ensure all features are working as expected. It’s essentially like testing a real application without human intervention.

Internally, when you write tests, FlutterFlow generates code for the [Flutter integration testing framework](https://docs.flutter.dev/testing/integration-tests), which you can download and test locally or through services like [Firebase Test Lab](https://firebase.google.com/docs/test-lab).

Legacy testing

Automated Tests are now considered a legacy testing option in FlutterFlow. For new testing workflows, we recommend using [**Test Pilot**](https://docs.flutterflow.io/testing/test-pilot), which lets you create and run AI-powered QA tests using natural-language instructions.

Pricing Details

* **Free and Basic plans:** Automated testing is not available.
* **Growth plan:** Includes **1 test per project**.
* **Business plan:** Allows **up to 3 tests per project**.
* **Enterprise plan:** Supports **unlimited automated tests**.

#### Basics

Before you add and run any tests, it's crucial to understand the workflow. When creating a test, you essentially map out a series of steps that dictate how the test will engage with the app. Each step can serve a distinct purpose and can be categorized as:

##### Step Type

1. [Interact with Widget](https://docs.flutterflow.io/testing/automated-tests#1-interact-with-widget)
2. [Wait to Load (Pump & Settle)](https://docs.flutterflow.io/testing/automated-tests#2-wait-to-load-pump--settle)
3. [Expect Result](https://docs.flutterflow.io/testing/automated-tests#3-expect-result)

###### 1. Interact with Widget

This step simulates user interactions with your app, such as tapping on a button or entering text into a field. When you add this step, you can specify what kind of [action type](https://docs.flutterflow.io/testing/automated-tests#action-type) you would like to simulate and on [which widget](https://docs.flutterflow.io/testing/automated-tests#selection-method).

##### Action Type

* **Tap**: Acts like a single tap or click.
* **Double Tap**: Imitates tapping twice quickly.
* **Long Press:** Imitates pressing and holding for a moment.
* **Enter** **Text**: Input the exact text you want to simulate entering.
* **Scroll Until Visible**: When this is selected, you can specify the **Delta** 'number of pixels' you want to repeatedly scroll until the widget is visible. If you have more than one scrollable widget, select which one you want to scroll using the **Scrollable** property.

###### 2. Wait to Load (Pump & Settle):

After an interaction, your test might need to pause momentarily, allowing the app to process the interaction, load something, or update its state. This is where the 'Wait to Load' mechanism comes into play, ensuring the app has had enough time to reflect any changes.

When this is selected, you have options to adjust:

* **Duration**: How long do you want to wait? The default value is 100ms.
* **Timeouts**: Maximum amount of time to wait, after which the test will fail.

Best practices

* Start your test with this step for about 3 seconds (i.e., 3000ms).
* After every "Interact with Widget" step, it's usually wise to add another "Wait to Load".

###### 3. Expect Result

After performing an action in your app, it's important to verify that the result matches your expectations. This is the verification step where you confirm that the app behaves as expected after the interaction. Here, you confirm whether a particular widget is present on the screen.

When this is selected, you have to [locate a widget](https://docs.flutterflow.io/testing/automated-tests#selection-method) that you want to verify and set what you expect to find using any of the below options:

* **Find Nothing:** Ensures that the specified widget is not present on the screen.
* **Finds Num Widgets:** Expect a certain number of widgets to be present.
* **Finds One Widget:** Confirms that exactly one widget is present.
* **Finds Widgets:** Expect multiple widgets to be found.
* **Is Enabled**: Verifies that the widget is not only visible but also functional.
* **Is Disabled**: Verifies that the widget is in a disabled state, meaning it is inactive and will not respond to user interactions.
* **Has State**: Confirms that a widget is in a specific state, such as *True* or *False*. For example, verify whether a checkbox is checked.

##### Selection Method

This is the method by which you locate the widget you want to select or verify. FlutterFlow offers the following ways to identify widgets:

* **Select from UI Builder:** Use the UI Builder's interface to visually select the widget you want to verify.
* **Find By ValueKey:** Locates the widget by its unique ValueKey. **Tip**: To add a ValueKey to a widget, use the 'Value Key' property located under the 'Testing' section on the widget properties panel.
* **Find By Type:** Search for a widget based on its type, like `Text` or `Button`.
* **Find By Semantics Label:** Useful for locating widgets that have a specific semantics label.
* **Find By Text:** Locate a widget that displays specific text.
* **Find By Descendent:** Search for a widget that has a specific child or ancestor.

#### Add Tests

Let's see how to add tests with an example that will ensure that users can add and remove items from their favorites list.

Here are the step-by-step instructions on adding tests:

1. Create a test to verify if the page is visible on the screen.

[Sharing a Project with a User](https://demo.arcade.software/RjJPy7zOBCu1QAVi8h0p?embed\&show_copy_link=true)

2. Next, find and simulate on tap event on the favorite button with the 'ValueKey' as the product id. **Important**: By using the 'ValueKey', we precisely target the favorite button for a specific product. Without this specificity, the test will encounter multiple favorite buttons and become uncertain about which one to tap, leading to a failed test.

[Sharing a Project with a User](https://demo.arcade.software/GF5My9t7gjEGfSEdgSXR?embed\&show_copy_link=true)

3. Similarly, you can now duplicate the test and make changes for the 'RemoveFromFavorites' test. **Tip**: While doing so, ensure that in the last step (i.e., **Expect Result**), you set the **Expectations** to **Finds Nothing**. This ensures that the removed item is not visible on the favorites list.

![remove-from-favorites](https://docs.flutterflow.io/assets/images/remove-from-favorites-40571fef2eabad43eb41466b20bbfdb9.avif)

#### Run Tests

You can run tests on local devices or use the services like [Firebase Test Lab](https://firebase.google.com/docs/test-lab).

To run the tests locally:

1. [Download the project code](https://docs.flutterflow.io/flutterflow-cli/exporting).
2. Go to `your_project/integration_test/test.dart`.
3. To run a specific test, click the play button next to it. To execute all tests at once, double-click the play button next to `void main`.
4. Alternatively, you can use the terminal and enter the command: `flutter test integration_test/test.dart`."

> **Info:** To run the tests on Firebase Test Lab, you can follow the instructions [**here**](https://docs.flutter.dev/testing/integration-tests#test-using-the-firebase-test-lab).

---

### Development Environments {#development-environments}

*Learn how to create and leverage development environments in FlutterFlow.*

**Source:** https://docs.flutterflow.io/testing/dev-environments

Development Environments in FlutterFlow allow you to set up multiple environments for your apps, such as `Development`, `Staging`, and `Production`. For each environment, you can create environment-specific values and databases. This allows you to easily point to different backends depending on where you are in your development lifecycle.

> **Note:** By default, every FlutterFlow project starts with a `Production` environment.

When to Use Dev vs. Staging Environments

* **Dev Environment**: Use for testing and developing new features without affecting production data.
* **Staging Environment**: Use to simulate the production environment before launching, and is isolated from the actual production data.

*This is a common best practice, but you can create custom environments with different names for your own workflow.*

##### Create and Switch Development Environments

You can create and switch environments in the **Dev Environments** page in **App Settings**. You can always see the current environment that is selected by looking in the top left hand corner of the project.

[Creating and Switching Development Environments](https://demo.arcade.software/yR8P5pFPOKtuQ0jFSOJ7?embed\&show_copy_link=true)

The selected environment is used to generate the proper app code when you run, test, deploy or export your app. The only things that change between environment are the [Firebase Project](https://docs.flutterflow.io/testing/dev-environments#configuring-firebase-or-supabase-for-each-environment) or variables that are tied to [Environment Values](https://docs.flutterflow.io/testing/dev-environments#environment-values)

##### Environment Values

Environment Values can be used to dynamically change parts of your app's code based on the environment that is being used.

For example, in an e-commerce app, you might define an `apiUrl` Environment Value that points to different API URLs for Development, Staging, and Production. This allows you to test new features without affecting the live production environment, where real customer orders are processed.

###### Use Environment Value

Let's see an example of creating and using `apiUrl`:

[Creating and Using Environment Values](https://demo.arcade.software/bAVpkNAanVDlBTyeRwJy?embed\&show_copy_link=true)

Generated Code

When you switch to an environment, FlutterFlow generates code specific to that environment, for any of the following interactions:

* Test / Run mode sessions
* Local Run
* Code export
* Deployment

You may also encounter different project errors depending on the selected environment.

In the generated code, FlutterFlow creates two files:

* `environment.json` – Stores the environment values defined by the user in FlutterFlow.
* `FFDevEnvironmentValues` class – A singleton class that holds a single instance of the `FFDevEnvironmentValues` object. It includes initialization logic and getters for accessing these environment values. They can also be referenced in your custom code resources. See **[Common Custom Code Examples](https://docs.flutterflow.io/concepts/custom-code/common-examples#get-dev-environment-values-in-custom-code)**.

###### Private Environment Values

You can mark environment values as private when they contain sensitive information that should not be exposed in the client-side code.

> **Warning:** Private environment values are not included in the compiled application code and are never exposed to end users. However, if a private environment value is used in a private API call that runs through a generated cloud function, the value may appear in the cloud function’s code. When exporting or pushing your project to GitHub, you must review and manage these cloud function files—for example, excluding them with `.gitignore` if they contain sensitive information.

Currently, the only way to use a private environment value is as a variable in a private API call. Since private API calls are routed through a Cloud Function, the variable value remains hidden from any client-side requests made by the app.

Generated Code

For private environment values, the generated code does not include these values in the `environment.json` file, and no getter logic is created in the `FFDevEnvironmentValues` class.

##### Configuring Firebase or Supabase for each Environment

A single FlutterFlow project can have **multiple environments**, each mapped to its **own Firebase or Supabase project**. This ensures that environments like `Development`, `Staging`, and `Production` remain independent, giving you better control over your app's data and behavior throughout different stages of development.

![flutterflow-environment](https://docs.flutterflow.io/assets/images/flutterflow-environment-update-ebd402503ef403cb632e068bfe98d81f.avif)

You must complete the Firebase or Supabase setup for an environment before you can test your app using that environment. However, this doesn't stop you from continuing to run and test your app in other environments. Just switch back to Production, and you can keep testing while finishing the setup for the new environment.

###### Configuring Firebase

If your project uses Firebase, you'll need to create a separate Firebase project in the Firebase Console for each environment. Then, you can change the selected environment in the Firebase settings page (see below), and follow the steps to [**manually configure the Firebase project**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#connect-an-existing-firebase-project-manually) for each one.

![firebase-dev-env-config.png](https://docs.flutterflow.io/assets/images/firebase-dev-env-config-e6341ee4a2459cbd8b1dd84cea224c07.png)

Additionally, you must manually set up [**Firestore rules**](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-rules) and [**collections**](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-collections) for the new environment.

> **Info:** The data that you add to Firebase through the Content Manager is specific to the Firebase project, and environment, that you have selected.

###### Configuring Supabase

If your project uses Supabase, you'll need to [**set up a new Supabase project**](https://docs.flutterflow.io/integrations/supabase/setup) for each environment.

Create environment-specific values like `SupabaseAPIURL` and `SupabaseAnonKey`, and then configure the Supabase properties to point to these newly created values. Below is an example of how it would look like.

> **Note:** It's recommended that you keep schemas consistent between the different Supabase environments. It's also recommended that you **Get Schema** from the Production environment and build from there.

##### FAQ

How can you push code from one environment to another?

It’s important to note that the **Development Environments** feature in FlutterFlow is primarily designed to configure different backends for testing

If you are building new features, you should consider using [**Branching**](https://docs.flutterflow.io/collaboration/branching). You can develop and test new features on a new branch by selecting a development environment. Once tested, you can merge the branch into `main` and switch to the `Production` Environment to go live.

Are you using Flutter flavors under the hood?

No, FlutterFlow does not use Flutter flavors. Instead, it generates code based on the environment selected in FlutterFlow. The environment-specific code is generated and applied for the following actions:

* Test / Run mode sessions
* Local Run
* Code export
* Deployment

How to deploy apps for different environments?

You can configure deployment settings for each environment using the dropdown interface on the deployment page. For mobile, set a new package name, and for web, set a new site URL. Once done, deploy your app as usual. See how to do it in [**detail here**](https://docs.flutterflow.io/deployment/deploy-for-environments).

---

### Local Run {#local-run}

*Local Run downloads the code locally and gives you the option to use Flutter's Hot Reload to see your changes instantly on a device.*

**Source:** https://docs.flutterflow.io/testing/local-run

You can test your app on a real device using the Local Run feature, which is available in the FlutterFlow Desktop App. Local Run automatically tracks changes in your FlutterFlow project, downloads the code locally, and gives you the option to use Flutter's Hot Reload or Hot Restart to see your changes instantly on a device.

**Prerequisites**

Testing on mobile devices requires downloading code, for which you must be on [**paid plans**](https://flutterflow.io/pricing).

##### iOS Setup

For iOS app testing on a device or simulator, you need a Mac with Xcode. Follow [**these instructions**](https://docs.flutter.dev/get-started/install/macos/mobile-ios?tab=download#configure-ios-development) to set up your Mac, which includes [**setting up your device for testing**](https://docs.flutter.dev/get-started/install/macos/mobile-ios?tab=download#configure-your-target-ios-device).

##### Android Setup

For Android app testing on a device or emulator, configure your machine ([**Windows**](https://docs.flutter.dev/get-started/install/windows/mobile?tab=virtual), [**Mac**](https://docs.flutter.dev/get-started/install/macos/mobile-android?tab=virtual), [**Linux**](https://docs.flutter.dev/get-started/install/linux#android-setup)) by following [**these instructions**](https://docs.flutter.dev/get-started/install/macos/mobile-android?tab=virtual#configure-android-development), which include [**setting up your device for testing**](https://docs.flutter.dev/get-started/install/macos/mobile-android?tab=virtual#configure-your-target-android-device).

#### Using Local Run

Here are the steps to use local run:

1. Download the [desktop](https://flutterflow.io/desktop) app and open your project.
2. In the [Toolbar](https://docs.flutterflow.io/flutterflow-ui/toolbar), click on the **dropdown** next to the *Test Mode* button and click **Setup Local Run**. This will open the setup wizard.

![setup-local-run](https://docs.flutterflow.io/assets/images/setup-local-run-ccd7811b7cb820f9f949185b93e1ca53.avif)

3. To run the app locally, you'll need the Flutter SDK. Click the **Download** button to download it. **Note** that for iOS, ensure you have *Xcode* and *CocoaPods* installed, select the checkmark, and then click **Download**.

![download-flutter-sdk](https://docs.flutterflow.io/assets/images/download-flutter-sdk-5dcbdc286c65082b012c91321e36e39f.avif)

4. Once it's ready to use, click the **Continue** button. This will run the **`Flutter Doctor`** command to check your environment for any issues that might prevent you from running the applications. It performs a series of checks to verify that the necessary tools and dependencies are correctly installed and configured on your system.

![doctor-output](https://docs.flutterflow.io/assets/images/doctor-output-da2d64e4465ae9aefe070cea216c5f32.avif)

5. Optional: You can set up your preferred IDE to open the project code directly from the local run. To do this, select your IDE, **Select Path**, and click **Save**. This feature is useful for debugging and understanding your project code. For this step, ensure you have setup [Flutter SDK](https://docs.flutterflow.io/testing/local-run#2-setup-flutter-sdk) and [IDE](https://docs.flutterflow.io/testing/local-run#3-installing-ide-and-plugins).

> **Info:** * The local run uses its own isolated Flutter SDK to ensure consistency and compatibility. The SDK is stored separately from any existing Flutter installations on your system and is automatically used to run your app and open projects in VS Code. For other IDEs like Android Studio, you need to set the SDK path to FlutterFlow's version manually.
* **Please note** that any changes made in the IDE will not sync with the FlutterFlow project and will be overwritten when you hot reload or restart the app.
* The path is the location of the IDE on your computer. On macOS, it's typically in "Applications," and on Windows, it's usually in "Program Files."
* Also, see how to [**access the project code**](https://docs.flutterflow.io/testing/local-run#access-project-code).

![config-IDE](https://docs.flutterflow.io/assets/images/config-IDE-3cd6d998b47f2e689b71921d080a1806.avif)

6. In the **Code Export** section, you can configure how Local Run exports and updates your FlutterFlow project code.

   * **Experimental Speed Up**: Uses an optimized export pipeline to significantly reduce export times. When enabled, Local Run can also work offline for faster iteration. If you experience export-related issues, you can disable this option.

   * **Format Exported Code**: Controls whether the exported code should be automatically formatted. Disabling formatting improves export speed, which helps during rapid iteration. However, if you plan to inspect or modify the generated code, it’s recommended to keep this enabled.

   * **Enable Debug Logging**: Includes logging support in the exported app. Keeping this enabled allows you to use the FlutterFlow Debug Panel inside DevTools for debugging and inspection.

   * **Auto Hot Reload**: Automatically triggers a hot reload whenever changes are made in FlutterFlow. This removes the need to manually trigger hot reload after every update.

   * **Auto Hot Restart**: Automatically performs a full app restart when changes require more than a hot reload, such as new dependencies or state model updates. This is disabled by default because full restarts are slower than hot reloads.

   ![local-run-code-export](https://docs.flutterflow.io/assets/images/local-run-code-export-6b12621e787e585534fcd0ba8f76b6a6.avif)

7. From the test menu, click on the **Get Devices** button. This will list devices connected to your system. You can add or remove devices from the list by clicking on the **+** and **-** buttons, respectively. Once you've finalized your selection, simply click on the **Test** button to see your app running on selected devices. **Tip**: In the Mac OS desktop app, you can directly open the simulator by clicking on the **Launch iOS Simulator** text. To test app on a real device, see how to [setup a physical device](https://docs.flutterflow.io/testing/local-run#setup-physical-device).

[Sharing a Project with a User](https://demo.arcade.software/PdTDtCPA6dmY2N4ziJ1A?embed\&show_copy_link=true)

8. After you make a change in your app, open the test menu to access options like **hot reload**, **hot restart**, and **stopping** your app. You'll notice that the test mode button has now changed to the **Hot Reload** button, which you can click anytime to instantly see your changes reflected on your device.

**Hot Reload** updates UI instantly without losing its state, while **Hot Restart** recompiles and reloads the entire app, resetting its state. For more info, you can visit [Flutter's Hot Reload documentation](https://docs.flutter.dev/tools/hot-reload).

![run-controls](https://docs.flutterflow.io/assets/images/run-controls-af8bd39b1b2838b4f99b6d9c8e2caa41.avif)

#### Setup Physical Device

Testing your app on physical devices is essential to ensure it performs as expected in real-world scenarios. To set up a physical device, first, launch the project in **Android Studio** or **Xcode**, depending on the platform you are targeting. You can easily access these options by clicking on the **code icon** in the **Local Run** menu.

![access-project-code.avif](https://docs.flutterflow.io/assets/images/access-project-code-b77d440078de6a10c3cf93798c5eb5f5.avif)

##### Setup Android Device

To setup Android physical device, first enable Developer Options and USB Debugging in your Android device. Navigate to **Settings > About phone**, tap **Build number** seven times to activate Developer Options, then go to **Settings > System > Developer options** and enable **USB debugging**.

Connect your device to your computer via USB, authorizing the connection if prompted. Verify the setup by running `flutter devices` in Android Studio’s terminal; your device should appear in the list of connected devices.

> **Info:** For more detailed guidance, refer to the [**Android Flutter documentation**](https://docs.flutter.dev/get-started/install/macos/mobile-android#configure-your-target-android-device).

##### Setup iOS Device

To setup iOS physical device, you must configure your **Apple Developer account** and set up **code signing** in Xcode. First, add your **Apple ID** by opening **Xcode > Preferences > Accounts**, clicking **"+"**, selecting **Apple ID**, and signing in.

Next, assign your project to a development team. Open your project in Xcode, select the **Runner** project, go to **Signing & Capabilities**, and choose your **Apple Developer team** in the **Team** dropdown. If your team is not listed, ensure that your Apple ID has been properly added to Xcode.

Finally, configure code signing to allow your app to run on a real device. Ensure **"Automatically manage signing"** is enabled. Xcode will attempt to create and download a **provisioning profile** for your project. If issues arise, you may need to manually create a provisioning profile in the **Apple Developer Certificates, Identifiers & Profiles** section. Once created, download and double-click the provisioning profile to install it in Xcode.

> **Info:** For more detailed guidance, refer to the [**iOS Flutter documentation**](https://docs.flutter.dev/get-started/install/macos/mobile-ios#configure-your-target-ios-device).

#### Access Device Logs in Local Run

Device logs provide a way to access and view the logs generated by your app while it's running on a device or simulator. They are invaluable for understanding the inner workings of your app. If something isn't functioning as expected, the device logs can reveal the reasons behind it.

To access the device logs, first run your app using the local run. Then, open the test menu and click on **Logs** icon. This will display a floating window with detailed logs of the app while it's running.

![access-device-logs](https://docs.flutterflow.io/assets/images/access-device-logs-2-409187df261c87da7bcf5c2122b13008.avif)

##### Console Input

The console input in local run is particularly useful for performing hot reload and hot restart directly from the device logs. To initiate a hot reload, press `r` followed by `Enter`, and for a hot restart, press `R` followed by `Enter`. Additionally, any terminal commands commonly used with Flutter while running an app should work with the console input.

[Sharing a Project with a User](https://demo.arcade.software/fraMoCbFDhzunNgBN852?embed\&show_copy_link=true)

##### Checking Errors

Any errors displayed in the red box on your screen are also recorded in the Device logs, where you can find detailed information about the app's state and the events leading up to the issue.

#### Reconfigure Local Run Setup

If you need to update the Flutter SDK version, run Flutter Doctor, or start the simulator again, simply open the test menu and click **Configure**.

![reconfigure-local-run.avif](https://docs.flutterflow.io/assets/images/reconfigure-local-run-2-73aba54c54ec4217e046f342cd5a0491.avif)

#### Access Project Code

To access the project code, open the test menu and ensure the project is not running. Click on the **code icon**, and you'll be presented with options to either open the project folder, project in your preferred IDE or directly launch the project in Xcode (for macOS users).

![access-project-code.avif](https://docs.flutterflow.io/assets/images/access-project-code-b77d440078de6a10c3cf93798c5eb5f5.avif)

#### Manually Download Code and Run

There may be certain situations where you, as a developer, may prefer not to have local runs overwrite any changes that have been made in the code. In such cases, you can manually download the code onto your local system and then make any modifications as needed.

Here’s how you do it:

1. [Download code](https://docs.flutterflow.io/testing/local-run#1-download-code)
2. [Setup Flutter SDK](https://docs.flutterflow.io/testing/local-run#2-setup-flutter-sdk)
3. [Installing IDE and Plugins](https://docs.flutterflow.io/testing/local-run#3-installing-ide-and-plugins)
4. [Running app on device](https://docs.flutterflow.io/testing/local-run#4-running-app-on-device)

##### 1. Download Code

> **Warning:** * Project code download is available only on the paid plans.
* Make sure to address any project issues before downloading the code.

To download your app code, you have two options:

* Use the [FlutterFlow CLI](https://docs.flutterflow.io/flutterflow-cli/exporting). (Recommended)
* Alternatively, from the **Toolbar**, click on the **Developer Menu** > **Download Code**. This will download the *.zip* file. Extract the *.zip* file to view the contents of the project.

##### 2. Setup Flutter SDK

You can download the latest Flutter SDK from [here](https://docs.flutter.dev/get-started/install). However, we recommend using the Flutter SDK downloaded by the [local run](https://docs.flutterflow.io/testing/local-run#using-local-run), whether you have already downloaded the Flutter SDK or not. This approach ensures compatibility with FlutterFlow projects and helps you avoid issues arising from version differences.

To do this, copy the Flutter SDK path (click 'this path' button) from the local run and [add it to your system path](https://docs.flutterflow.io/testing/local-run#troubleshooting).

![setup-flutter-SDK](https://docs.flutterflow.io/assets/images/setup-flutter-SDK-57c8c80b82e6d2998cc36b930153bc01.avif)

If you prefer to use your existing Flutter SDK, you can follow the steps below to avoid any versioning issues:

1. Take note of your FlutterFlow project version.

![check-flutter-version.avif](https://docs.flutterflow.io/assets/images/check-flutter-version-2-ae7065141a80cc79c9eec976e7dfc296.avif)

1. Check your current Flutter SDK version by entering the following command in the terminal. `flutter --version`

2. If that is different from what FlutterFlow uses, you may need to switch to the supported version.

3. To install a specific version of Flutter, use the following command: 1. To **downgrade** flutter version:

      ```
      flutter downgrade <version_number>
      ```

   2. To **upgrade** flutter version:

      ```
      flutter upgrade --force <version_number>
      ``` Replace `<version_number>` with the version supported by FlutterFlow.

##### 3. Installing IDE and Plugins

You can choose to install either [Visual Studio Code](https://code.visualstudio.com/) or [Android Studio](https://developer.android.com/studio) as the IDE for your project. With either IDE, you also need the official Flutter and Dart plugins that provide you with code completion, syntax highlighting, widget editing assistance, run & debug support, and more.

* To install Visual Code with Flutter and Dart plugins, check out [this link](https://flutter.dev/docs/get-started/editor?tab=vscode).
* To install Android Studio with Flutter and Dart plugins, check out [this link](https://flutter.dev/docs/get-started/editor?tab=androidstudio).

##### 4. Running App on Device

You can choose to run your app on a real device or an emulator.

> **Tip:** To test app on a real device, see how to [**setup a physical device**](https://docs.flutterflow.io/testing/local-run#setup-physical-device).

To run your app on a device:

1. First open the downloaded project in your preferred IDE.

2. For **VS Code**: 1. Go to the "View" menu -> select "Terminal" from the dropdown.
   2. Run the command `flutter pub get`.
   3. Now, enter the command `flutter run`. VS Code will build and run your app. You'll see the output in the terminal, and the app should launch in the selected emulator or physical device.

3. For **Android Studio**: 1. Open the terminal within Android Studio by clicking **"View" -> "Tool Windows" -> "Terminal"**.
   2. Run the command `flutter pub get`.
   3. Click the green "Run" button (a right-facing triangle) located in the top toolbar. Choose the target device (emulator or physical device) where you want to run the app. Android Studio will build and run your app. You'll see the output in the "Run" panel at the bottom, and the app should launch in the selected emulator or device.

> **Info:** * If your device is not listed in the **Flutter Device Selection** dropdown, make sure you have properly completed the Android and iOS setup.
* If you encounter a version compatibility issue with Flutter, you can resolve it by upgrading to the latest version. Simply execute the `flutter upgrade` command in your terminal. To verify your current Flutter version, use the `flutter --version` command.

#### Run on Desktop

Running your app on a Desktop involves:

1. **Adding platforms**: Navigate to **Setting and Integrations** from the Navigation Menu > **Project Setup** > **Platforms** and enable your desired platform.
2. **Make design adjustments (optional)**: If you plan to target both mobile and desktop users, some design adjustments may be necessary to ensure that the UI is optimized for both platforms. You can create separate widgets for different platforms and control their visibility using [Responsive Visibility](https://docs.flutterflow.io/concepts/layouts/responsive#responsive-visibility).
3. **Run the app on a desktop**: Use the Local Run feature in the FlutterFlow Desktop app or manually download and run the code, choosing your target device (e.g., macOS) before running.

#### Video Guide

If you prefer watching a video tutorial, here's the one for you:

[Local Run | New Feature Tutorial](https://www.youtube.com/embed/k9NpYncXC_U)

***

#### Troubleshooting

Command not found: flutter (add Flutter to system's path)

If you downloaded Flutter via local run, it might not be added to your system's path. You'll need to get the Flutter SDK directory and add it to your path manually.

* For Mac
* For Windows

1. From the [local run](https://docs.flutterflow.io/testing/local-run#using-local-run) wizard, open the **Configure IDE** step and click on **this path** to get the Flutter SDK path. ![get path](https://docs.flutterflow.io/assets/images/get-path-5180adef7967b16994e39ff537e3fb09.avif)

2. Open the Terminal and run the following command to open your `.zshrc` file (or `.bash_profile` if you're using Bash):

   ```
   open -e ~/.zshrc
   ```

3. Add path at the end of the file. It should look something like this:

   ```
   export PATH="$PATH:$HOME/Library/Application Support/io.flutterflow.prod.mac/flutter/bin"
   ```

4. Save and close the file.

5. Run the following command to apply the changes:

   ```
   source ~/.zshrc
   ```

6. Restart your terminal and try running the `flutter` command again.

1) From the [local run](https://docs.flutterflow.io/testing/local-run#using-local-run) wizard, open the **Configure IDE** step and click on **this path** to get the Flutter SDK path. ![get path](https://docs.flutterflow.io/assets/images/get-path-5180adef7967b16994e39ff537e3fb09.avif)
2) Right-click on the Start menu and select "System".
3) Click on "Advanced system settings" and then "Environment Variables".
4) Under "System variables", find the "Path" variable and click "Edit".
5) Click "New" and add the path to your Flutter SDK.
6) Click "OK" to save your changes.
7) Restart your command prompt and try running the `flutter` command again.

Device not showing in the list

If you don't see your device in the list after refreshing, follow these steps:

1. Ensure you have added Flutter to your path.

2. Open the Terminal and run the following command:

   ```
   flutter devices
   ```

   This will list all connected devices that the Local Run recognizes.

3. If you still don't see your device, try restarting it.

   1. **For iOS**: Open Xcode, go to the "Window" menu, select "Devices and Simulators," choose your simulator, and click "Restart."

   2. **For Android**: Open the Android Studio > Device Manager, choose your emulator, and click the "Play" button.

   3. You can also restart the emulator directly from the command line using Flutter:

      ```
      flutter emulators --launch <emulator_id>
      ```

      **Note** that replace `<emulator_id>` with the ID of your emulator. You can find the ID by running `flutter emulators`.

4. Try running `flutter devices` again.

Xcode warning "Runner.xcworkspace modified"

If you encounter a warning from Xcode stating:

> "The file 'Runner.xcworkspace' has been modified by another application."

This warning can usually be safely ignored. It typically occurs when multiple tools or processes (such as FlutterFlow local run and Xcode) modify the project files simultaneously. Here's what you can do:

1. **Save Your Work**: Ensure that you've saved any changes you've made in Xcode.
2. **Close and Reopen**: Close the warning prompt and, if necessary, close and reopen Xcode to refresh the project files.
3. **Clean the Build**: If the warning persists, try cleaning the build folder in Xcode by going to "Product" > "Clean Build Folder."
4. **Flutter Clean**: You can also run `flutter clean` in your terminal to clean the build cache for your project, which can sometimes resolve issues related to outdated or conflicting files.

***

#### FAQs

Can I export the project as a Flutter Module?

Yes, you can export your project as a Flutter module. Here's how:

1. Activate the FlutterFlow CLI by entering `dart pub global activate flutterflow_cli` in your terminal.
2. Use the command below to export your project and substitute `<project id>`, `<output folder>`, and `<token>` with your specific project details:

```
flutterflow export-code --project <project id> --dest <output folder> --include-assets --token <token> --as-module
```

If you wish to exclude assets from the export, use `--no-include-assets` in your command. This will export the project code without the assets.

For example: `flutterflow export-code --project your_project_id --dest path_to_output_folder --no-include-assets --token your_token --as-module`

You can then follow the instructions for [Android](https://docs.flutter.dev/add-to-app/android/project-setup) and [iOS](https://docs.flutter.dev/add-to-app/ios/project-setup) to add the module to your main app.

---

### Run your App {#run-your-app}

*Discover the essentials of running and testing your FlutterFlow app with this comprehensive guide.*

**Source:** https://docs.flutterflow.io/testing/run-your-app

Running and testing your app is a crucial part of the app development process. This page provides a comprehensive guide on how to run and test your FlutterFlow app. It covers various modes of testing, including [Preview](https://docs.flutterflow.io/testing/run-your-app#preview-mode), [Test](https://docs.flutterflow.io/testing/run-your-app#test-mode), [Run](https://docs.flutterflow.io/testing/run-your-app#run-mode), and [Local Run](https://docs.flutterflow.io/testing/run-your-app#local-run) modes, with detailed steps and indications of when to use each mode.

> **Info:** You can access various modes of running your app from the [**Toolbar**](https://docs.flutterflow.io/flutterflow-ui/toolbar).

![run your app](https://docs.flutterflow.io/assets/images/run-your-app-61003863bd89e585f73f68fc26c93b83.avif)

#### Preview Mode

You can use the Preview Mode to quickly try out your app on a virtual device without waiting for it to build. This is helpful primarily for navigation and animations. You can also preview your app in the Dark/Light mode and visualize it on various mobile, tablet, and desktop devices.

##### When to use Preview Mode

The primary benefit of **Preview Mode** is that it allows your app to load instantly, making it ideal for UI testing. However, most business logic is not included in this mode. As a result, this mode is used less frequently than other testing modes, which provide a more comprehensive evaluation of the app's functionality.

Preview Mode Limitations

* Actions may not trigger or work properly.
* FontAwesome icons jump around when mouse hovers over certain material widgets.
* Firestore data is not loaded from Firebase.
* Firebase auth flow can't be tested. We always allow log in.
* API Calls can't be run or tested here.
* Refresh if animation actions are not working.
* Refresh if Clear TextFields actions are not working.
* RevenueCat data is not loaded.
* Paywall actions execute as if the entitlement is active.
* Hero Animation may not work on dynamically generated widgets.
* Dropdown disabling does not work in Preview Mode.
* Tooltip does not work for some screen sizes in Preview Mode.

#### Test Mode

The **Test Mode** runs a web version of your FlutterFlow app and uses Flutter's Hot Reload feature, which lets you immediately see any changes made to code in an emulator or on-device. Running your app in Test Mode helps you experiment, test UIs, and fix bugs faster.

To run your app in Test Mode:

1. Select **Test Mode** from the left-side menu. The test environment will launch and be ready to use within a few minutes.
2. Once Test Mode is running, make changes in the FlutterFlow builder, such as updating colors, layouts, or widgets.
3. In Test Mode, **Sync changes automatically** is enabled by default, so changes made in FlutterFlow are automatically synced to the running app.
4. If you disable auto-sync, click **Hot Reload** or press `Cmd/Ctrl + J` whenever you want to manually sync and preview the latest changes.
5. Use **Hot Restart** when changes require a full restart, such as dependency updates or certain state model changes.

> **Note:** **For users on a paid plan**, Test Mode sessions do not expire and can remain active indefinitely until manually stopped.

**For users on the Free plan**, Test Mode sessions expire after 20 minutes. Once a session expires, you can start a new one by clicking the **New Session** button.

![new-session](https://docs.flutterflow.io/assets/images/new-session-586a87a3ac25f5881e09126311c15b86.avif)

##### Floating Window

A Floating Window displays the running app on top of the builder, allowing you to design and test at the same time without switching between tabs.

The Floating Window makes iteration much faster because you can immediately see the impact of your changes while working in the builder. It makes it easier to fine-tune layouts, styling, and interactions.

To open the Floating Window, start a Test Mode session and click the **Floating Window** icon in the Test Mode toolbar. A movable preview of your app will appear over the builder, allowing you to keep the live app and editor visible at the same time. You can drag the window anywhere on the screen and resize it as needed while continuing to edit your app.

##### Inspect Mode

Inspect Mode helps you quickly locate widgets in the FlutterFlow builder while testing your app. This is especially useful when working with large pages or deeply nested layouts. Instead of manually searching through the Widget Tree to find a specific button, image, text, or container, you can simply click it in the running app and jump directly to its location in the builder.

To use Inspect Mode, click the **Inspect Mode** icon in the Test Mode toolbar. Once enabled, select any widget in the running app preview. FlutterFlow will automatically navigate to and highlight the corresponding widget in the builder, allowing you to inspect or edit it immediately.

When you're finished, click the Inspect Mode icon again to exit inspection mode and continue interacting with the app normally.

##### Test Mode on Mobile

You can open the current Test Mode session directly on a physical mobile device. This allows you to test your app on actual hardware and verify touch interactions, layouts, scrolling behavior, and overall user experience.

To open the session on your phone, click the **QR Code** icon in the Test Mode toolbar. FlutterFlow will generate a QR code and a unique session link. Scan the QR code using your phone's camera or open the generated link on your mobile device. The app will load the same active Test Mode session that is running in your browser.

> **Warning:** The generated link is tied to the current Test Mode session and will stop working when the session ends.

![test-mode-in-phone](https://docs.flutterflow.io/assets/images/test-mode-in-phone-2c85818cfd1323b0164376ca0ffc0c19.avif)

##### Debug info

Test mode also includes a **Debug Info** panel, which provides a real-time view of all variables with their current values. It includes search and filter options, allowing you to find variables based on type or nullability. This is particularly useful for developers who need to track the state of the app and diagnose issues efficiently.

![deubg-info](https://docs.flutterflow.io/assets/images/deubg-info-f3da771189b805d1e3c99110a4dbccbd.avif)

Test Mode Limitations

**Test Mode** has certain limitations because some packages are not supported on the web and because of the way FlutterFlow configures your project to run in the cloud.

* If you see a grey "broken" screen with a sad face, it may be a DNS server issue with your network provider. We recommend using CloudFlare's 1.1.1.1 DNS server. [**Click here**](https://developers.cloudflare.com/1.1.1.1/setup/) to see instructions.
* Lottie animation may not load if you provide a variable path.
* Cookies need to be enabled for Test Mode to function properly. They are only used for functional purposes.
* If you see a progress bar where the phone outline should be that lasts longer than 15 seconds, try refreshing the page.
* The device screen can not be wider than the page's width.
* Copy to Clipboard Action is not supported in Test Mode. Use [**Run Mode**](https://docs.flutterflow.io/testing/run-your-app#run-mode) to avoid this issue.
* Widgets with Shimmer or Tint animation might not appear properly.
* Assets used within Custom Code might not appear properly.
* Audio Recording actions do not work in Test Mode; use web publishing in Settings to test recording audio or test it on emulator via Local Run.

#### Run Mode

You can test a fully functional version of your app using the **Run Mode**, including live data. It will build the app, which typically requires around 2-4 minutes - but can be longer for larger projects. You can then interact with your app through your web browser. This is a web version of the app, identical to the version that is run on *Test Mode*.

To run the app in Run Mode, click on the **dropdown** next to the Test Mode button and click the play button or press **Cmd/Ctrl + E** (keyboard shortcut). This will run your app in a new browser window.

##### When to use Run Mode

The main benefit of Run Mode is the ability to share a running app within your team via a link. Please note that, **Run Mode links are not public**; they are only accessible to project members. Even if the project is made public (allowing others to view and clone the project), the visibility of Run Mode links remains restricted to project members.

All Run Mode sessions will persist and can be accessed from the dropdown menu next to the lightning bolt icon in the upper right of the FlutterFlow builder.

![run-project-versions](https://docs.flutterflow.io/assets/images/run-project-versions-4a8611a8a0971f33edc403b661e723e8.avif)

Run Mode Limitations

Run Mode does not support Hot Reloading, so any changes you make to your app will not be reflected in the Run Mode. In order to see the changes, you would have to create another Run Mode.

#### Local Run

Local Run downloads the code locally and gives you the option to use [Flutter's Hot Reload](https://docs.flutter.dev/tools/hot-reload) or Hot Restart to see your changes instantly on a device. See how to setup Local Run [here](https://docs.flutterflow.io/testing/local-run).

> **Info:** Please note that Local Run is currently available only on the [**Paid Plans**](https://flutterflow.io/pricing).

#### FAQ

I don't see the new Test Mode option in the left sidebar. If the new Test Mode option is not visible in the left sidebar, open the test menu and enable the **Use new test mode** option. Once enabled, the new Test Mode option will appear in the navigation menu.

---

### Test Pilot {#test-pilot}

*Learn how to create and run AI-powered QA tests for your FlutterFlow app using Test Pilot.*

**Source:** https://docs.flutterflow.io/testing/test-pilot

Test Pilot in FlutterFlow allows you to run AI-powered tests for your app. Instead of building step-by-step integration tests manually, you create natural-language tests, group related tests together, and ask Test Pilot to interact with your app like a QA tester.

This is useful when you want to validate important user journeys before publishing or sharing a new build. For example, you can ask Test Pilot to sign in with test credentials, add an item to a cart, open the profile page, or confirm that a checkout flow lands on the expected success screen.

At a high level, Test Pilot creates a web build snapshot of your project, launches the app in a browser-based QA environment, and uses an AI agent to follow each test's instructions. After the run completes, you can review pass or fail status, per-test summaries, screenshots, playback, actions taken, and credit usage.

#### Create Test

To get started, first create a **Test Group**. Use test groups to organize related tests, such as authentication, checkout, profile settings, or onboarding.

After you create or select a test group, add tests that describe the exact journey Test Pilot should perform. Each test has:

* **Test Name**: The label shown in the test group and run results.
* **Entry Page**: Optional initial route for the test. Use **App default** when the app should start from its default entry page.
* **Enabled or Disabled state**: A toggle to enable or disable a test. Only enabled tests are included when the group runs.
* **Instructions**: Natural-language steps for the AI agent to follow.
* **Expected Outcome**: Optional success criteria that Test Pilot should verify after completing the instructions.
* **Restart before test**: Optional behavior that starts the app fresh before that test. This is **turned off by default, so tests are executed sequentially** one by one and can continue from the state left by the previous test. Turn it on when a test should start from a clean app state and not depend on earlier tests.

Write instructions the way you would brief a QA teammate. Mention the screen, the UI element, the action to take, and the expected result.

For example, a login test might use:

* **Instructions**: `Wait for the screen to load, then enter $email and $password into the text fields and click the continue button.`
* **Expected Outcome**: `The app should land on the home page.`

> **Tip:** `$email` and `$password` are [**Test Parameters**](https://docs.flutterflow.io/testing/test-pilot#test-parameters). After you create a parameter, you can reference it directly in test instructions by adding `$` before the parameter name.

Here's how to create tests:

##### Test Parameters

Test Parameters let you store reusable values that Test Pilot can substitute into test instructions. This is especially helpful for credentials, environment-specific values, or other data that you do not want to type into every test.

Test Parameters are managed per [FlutterFlow Environment](https://docs.flutterflow.io/testing/dev-environments). Use the **Environment** dropdown to switch between environments, then add the parameter values for the selected environment.

Each parameter includes:

* **Name**: The variable name used in instructions.
* **Value**: The value Test Pilot substitutes when running the test.
* **Description**: A clear note describing what the value is used for.
* **Encryption toggle**: Marks sensitive values so they are encrypted.

To use a parameter, create it from **Test Parameters**, then reference it in instructions with a dollar sign, such as `$email` or `$password`.

> **Caution:** For login tests, use a separate test account instead of a real user account. Secret parameters help hide sensitive values, but you should avoid using production credentials in Test Pilot runs.

#### Run Test

To run a test group, select the test group you want to run, click **Run Test Group**, choose the run configuration, and then click **Run Tests**.

Run configuration options include:

* **Device Sizes**: Uses the current canvas size by default. You can add predefined devices or custom width and height values. The run dialog supports up to 3 selected devices.
* **Brightness**: Choose light or dark mode. Dark mode is available only when dark mode is enabled in the project design system.

> **Info:** Before starting a run, make sure the selected group has at least one enabled test, the project has no blocking errors, the selected environment is valid, and no other Test Pilot run is active for the same project or group.

#### Review Test Results

The **Run History** section shows the previous and active Test Pilot runs for the selected group. Click **View Results** to open the run details page. From there, you can review every test in the run and inspect the AI agent's explanation for each result.

Each test result can include:

* **View Test Playback**: Opens a step-by-step playback of the agent's interaction with the app. When you open Test Playback, you can use **Previous** and **Next** to move through each step, select a screenshot from the thumbnail strip, and review the agent's reasoning for that step. The playback side panel includes:

  * **Goal**: What the agent was trying to do in the selected step.
  * **Observation**: What the agent saw on the screen.
  * **Actions**: The action taken in that step and whether it succeeded.
  * **Config**: Displays the test run duration, screen size, and options to show or hide the device frame and overlay. It also includes a **View JSON** option to inspect the raw step data.

* **Screenshots**: Captured screens from the run. Use these to quickly see what the agent saw at key moments.

* **Actions Taken**: The actions the agent performed while executing the test, including clicks, text entry, key presses, completion steps, and whether each action succeeded.

* **Open Snapshot**: Opens the build snapshot used for the run.

#### Best Practices

* Keep each test focused on one user journey, such as login, checkout, or opening profile settings.
* Start instructions with any setup the agent needs, such as waiting for the screen to load.
* Use clear UI descriptions, such as "click the profile icon on the top left side" instead of "click the icon."
* Add an expected outcome when the result matters, such as "the app should land on the home page."
* Store separate parameter values for each environment.
* Review screenshots, playback, and actions taken when a test fails, because the summary may point to a build, startup, UI, or instruction issue.
* Turn on **Restart before test** when a test should start from a clean app state. Leave it off when tests are intentionally designed to run sequentially.

#### Test Pilot Credits

Test Pilot uses Test Pilot credits. Each project gets **5 free credits**, which equals **5 single-test runs**. After the free credits are used, runs use credits from an assigned Test Pilot Credits Pass.

A Test Pilot Credits Pass is a paid add-on. Passes start at **$5/month for 100 credits**. One credit represents one single test being run.

Credit usage is based on the number of tests, devices, and brightness modes included in the run. For example, if a test run includes **3 tests**, runs on **2 devices**, and uses both **light and dark mode**, it uses `3 * 2 * 2 = 12` credits.

Before you start a run, FlutterFlow shows how many credits the run will use. This lets you review the cost of running the selected test group before you click **Run Tests**.

Pricing:

* **USD**: `$5/month` per pass unit. Each unit grants `100` credits per reset cycle. You can buy multiple units. For example, `10` units cost `$50/month` and grants `1000` credits.
* **INR**: The same pricing applies.
* **Regional discounts**: None.
* **Annual discount**: Approximately 25%.

Pass types:

* **Personal pass**: Purchased from Account billing and assignable to one personal project owned by that user.
* **Team pass**: Purchased from Teams billing and assignable to one project belonging to the same team.

Pass assignment is permanent. You cannot manually clear, update or transfer the pass while the project still exists. If the assigned project is deleted, the pass becomes unassigned. If a project changes owner or team scope and the assigned pass no longer matches that scope, the pass should be unassigned automatically. For example, if a team project with an assigned team pass is moved to become a personal project, the team pass will be unassigned.

Deleting or canceling a purchased pass is a billing action. Like other subscriptions and add-ons, when you delete a Test Pilot pass, you can continue to use it until the end of your current billing cycle.

#### FAQs

Why can't I run tests?

Check that the project has available Test Pilot credits or free runs, at least one enabled test, editor access, no active Test Pilot run, a valid environment, and no blocking project errors.

Why do I see 0 credits?

This can happen when no Test Pilot Credits Pass is assigned to the project, the assigned pass has used all credits for the cycle, the assigned pass no longer matches the project scope, or credit status failed to load.

Why can't I assign my pass?

A pass may already be assigned, the project may already have a pass, the pass may not match the project scope, or you may not have the required billing permissions. Personal passes can only be assigned to matching personal projects, and team passes can only be assigned to matching team projects.

Can support move my pass?

Pass assignment is intended to be permanent. Contact support if you suspect a data issue, such as a stale assignment after a project was deleted or moved.

How many free credits do projects get?

Each project gets 5 free Test Pilot credits. Since 1 credit equals 1 single test run, this gives each project 5 free tests. After those credits are used, the project needs an assigned Test Pilot Credits Pass.

Why doesn't my pass have a regional discount?

Test Pilot Credits Passes do not use regional discounts. The billing page shows the price that applies to your account.

Do I get free credits if I have an educational account?

Educational accounts get 5 free tests per project, and are able to purchase Test Pilot passes for further credits.

---

