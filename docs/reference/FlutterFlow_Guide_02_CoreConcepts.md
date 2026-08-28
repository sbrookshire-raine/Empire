# FlutterFlow Documentation — Complete Guide (Part 2 of 7: Core Concepts: UI Building, Actions, Animations, Navigation, Custom Code)

> **Note for NotebookLM:** This is one part of a multi-file Markdown export of the official FlutterFlow documentation, cleaned and reorganized for use as a NotebookLM source set to build a structured FlutterFlow learning plan. Import all parts together as separate sources in the same NotebookLM notebook.

- **Source:** https://docs.flutterflow.io (crawled via https://docs.flutterflow.io/llms-full.txt)
- **This file's page count:** 56
- **Total pages across the full guide (all 7 parts):** 369
- **Date generated:** 2026-07-18
- **Part:** 2 of 7 — Core Concepts: UI Building, Actions, Animations, Navigation, Custom Code
- **Other parts in this guide:**
  - Part 1: Fundamentals, Account, CLI & Builder UI (`FlutterFlow_Guide_01_Fundamentals_and_Platform.md`)
  - Part 3: Widgets Reference (`FlutterFlow_Guide_03_WidgetsReference.md`)
  - Part 4: Resources: Data, Backend Query, Forms, Functions & Projects (`FlutterFlow_Guide_04_ResourcesDataAndLogic.md`)
  - Part 5: Integrations: Auth, Firebase, Supabase, Payments, Maps, Search, Ads (`FlutterFlow_Guide_05_Integrations.md`)
  - Part 6: Deployment, Testing, Marketplace & Exporting Code (`FlutterFlow_Guide_06_DeploymentTestingMarketplace.md`)
  - Part 7: Troubleshooting Guides (`FlutterFlow_Guide_07_Troubleshooting.md`)

## Table of Contents

**Core Concepts (UI, Actions, Logic, Animations, Custom Code)**

- [Accessibility](#accessibility)
- [Integrating Native SDKs Using Method Channels](#integrating-native-sdks-using-method-channels)
- [Alert Dialog](#alert-dialog)
- [Dismiss Custom Dialog](#dismiss-custom-dialog)
- [Haptic Feedback](#haptic-feedback)
- [Animations](#animations)
- [Hero Animation](#hero-animation)
- [Implicit Animations](#implicit-animations)
- [Lottie Animation](#lottie-animation)
- [Page Transition Animations](#page-transition-animations)
- [Rive Animation](#rive-animation)
- [Shaders](#shaders)
- [Widget Animations](#widget-animations)
- [App Events Integrations](#app-events-integrations)
- [App Events](#app-events)
- [Component Catalog](#component-catalog)
- [Custom Code](#custom-code)
- [Cloud Functions](#cloud-functions)
- [Code File](#code-file)
- [Common Code Examples](#common-code-examples)
- [Configuration Files](#configuration-files)
- [Custom Actions](#custom-actions)
- [Custom Functions](#custom-functions)
- [Custom Widgets](#custom-widgets)
- [FlutterFlow Visual Studio Extension](#flutterflow-visual-studio-extension)
- [Design System](#design-system)
- [File Handling](#file-handling)
- [Clear or Delete Media](#clear-or-delete-media)
- [Displaying Media](#displaying-media)
- [Download File](#download-file)
- [Uploading Files](#uploading-files)
- [GenUI Chat](#genui-chat)
- [Building Layout](#building-layout)
- [ConditionalBuilder](#conditionalbuilder)
- [Flex](#flex)
- [Responsive Layout](#responsive-layout)
- [Wrap](#wrap)
- [Localization](#localization)
- [Bottom Sheet](#bottom-sheet)
- [Deep & Dynamic Linking](#deep-dynamic-linking)
- [Generate Current Page Link](#generate-current-page-link)
- [Launch URL [Action]](#launch-url-action)
- [Overview](#overview)
- [Page Navigation](#page-navigation)
- [PageView](#pageview)
- [Passing Data between Pages](#passing-data-between-pages)
- [Share [Action]](#share-action)
- [Overview](#overview-2)
- [TabBar](#tabbar)
- [WebView](#webview)
- [Notifications](#notifications)
- [OneSignal](#onesignal)
- [Push Notifications](#push-notifications)
- [State Management](#state-management)
- [Widget State](#widget-state)
- [Tools Configuration](#tools-configuration)

---

## Core Concepts (UI, Actions, Logic, Animations, Custom Code)

### Accessibility {#accessibility}

*Learn how to make your app accessible to everyone.*

**Source:** https://docs.flutterflow.io/concepts/accessibility

Accessibility is about making your app usable for everyone, including individuals with visual, auditory, cognitive, or motor impairments. Ensuring your app is accessible not only benefits users with disabilities but also improves the overall user experience and usability of the app for everyone.

Here are some examples of how accessibility can help users with disabilities:

* **Screen Readers for Visually Impaired Users**: Screen readers like **TalkBack** (Android) and **VoiceOver** (iOS) help visually impaired users navigate and understand the app by reading aloud on-screen content.
* **Large Touch Targets for Motor Impairments**: Large touch targets make it easier for users with motor impairments to interact with buttons and other UI elements.
* **Color Contrast for Visual Impairments**: High-contrast color schemes ensure text and interactive elements are easily readable for users with visual impairments.
* **Keyboard Navigation for Physical Impairments**: Users unable to use touchscreens can navigate the app effectively with keyboard controls.
* **Haptic Feedback**: Tactile responses help users with visual or motor impairments understand when interactions are successful.

In FlutterFlow, you can enhance the accessibility of your app by incorporating various accessibility features, such as semantic labels, keyboard navigation, haptic feedback, responsive fonts, and proper color contrast.

Here are some key accessibility features you can use:

#### Semantic Label

**Semantic Labels** enhance your app’s accessibility and SEO by providing meaningful context about widgets for screen readers and search engines. These descriptions are especially helpful for users relying on assistive technologies.

For example, in an e-commerce app, you can add a semantic label to an '*Add to Bag*' button with a message like '*Add the selected item to cart*', which helps users better understand the button's action.

To add a semantic label for any widget, select the widget, move to the properties panel (right side), tap the document icon inside the **Accessibility & Semantic Label** section, add the message, and click **Save**.

> **Tip:** You can also dynamically set semantic labels using variables or expressions. This allows the label to change based on the app context, so screen readers announce exactly what’s on the screen instead of generic terms like "image" or "button." For example, a product image can read out the product name (e.g., "Red Running Shoes" pulled from Firestore) instead of just saying "image."

##### Advanced Semantic Settings (Enterprise Only)

These settings help make your app more accessible by giving you better control over how screen readers interpret and describe your UI.

> **Info:** These settings are only available to **Enterprise** users.

Here’s what each option does:

* **Is Container**: Indicates the widget acts as a grouping for other semantic widgets.
* **Is Image**: Tells screen readers the widget represents an image.
* **Is Button**: Declares that the widget behaves like a button.
* **Is Header**: Identifies a widget as a heading for better navigation.
* **Explicit Child Nodes**: Forces semantics to include all child nodes, even if normally ignored.
* **Exclude Semantics**: Prevents screen readers from announcing this widget.
* **Is Live Region**: Tells assistive tech that the widget’s content may change dynamically and should be re-announced.
* **Hint Text**: Provides an additional hint for users (e.g., "Double tap to open").
* **Tooltip Text**: Provides descriptive text about the widget to screen readers, giving extra context beyond the primary label.
* **Ordinal Sort Key**: Controls the order in which widgets are accessed by screen readers.

> **Tip:** You can add a semantic label for every widget in your app that has an action trigger `OnTap` or `onLongPress`, by enabling the **Add Warning for Semantic Widgets**. By doing so, you'll get a warning if any widget has an action but doesn't have a semantic label added yet. You can click on the warning item to directly navigate to that widget.

![add-warning-for-semantic-widgets.avif](https://docs.flutterflow.io/assets/images/add-warning-for-semantic-widgets-5d0dc639482abc4bace4a41d4cd01da2.avif)

After you add semantic labels, enable **TalkBack** on Android or **VoiceOver** on iOS to test how screen readers interact with your app. These screen readers will help you verify that all UI elements are read clearly, descriptions are meaningful, and users can navigate logically without getting lost.

Learn more about [enabling screen reader on your device](https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility#screen-readers).

#### Semantic Announce \[Action]

The **Semantic Announce** action lets you notify screen reader users about important UI changes or provide contextual updates. It sends a request to the device’s accessibility service (TalkBack/VoiceOver) to speak the text out loud.

It significantly improves accessibility by allowing screen reader users to receive timely and meaningful feedback. This is especially helpful when visual feedback might be missed or unavailable.

possible use cases

* **Form Submission**: After a user submits a form, you can trigger a screen reader announcement like "Your form has been submitted successfully," giving immediate feedback without requiring visual cues.
* **Dynamic Content Updates**: When new content is added or changed on the screen—like loading new chat messages or refreshing a feed—you can announce messages like "3 new messages loaded" to ensure screen reader users are aware of the update.
* **Error or Validation Messages**: If a user enters invalid input, you can announce helpful validation feedback like "Please enter a valid email address".

The Semantic Announce action allows you to trigger screen reader announcements with the following settings:

* **Announcement Text**: The message you want the screen reader to speak aloud (e.g., "Item added to favorites").
* **Is Text Right to Left**: Set this to True for right-to-left languages like Arabic or Hebrew. It defaults to False, which is appropriate for left-to-right languages like English.

![semantic-announcement.avif](https://docs.flutterflow.io/assets/images/semantic-announcement-12a2c9ab81b23b565dca5b1d97b520e3.avif)

Best Practices

* Long announcements can overwhelm the user. Aim for a concise phrase like "Search complete — 3 results."
* Too many announcements can confuse or irritate the user. Only announce critical or timely changes that aren’t otherwise discoverable.
* Use the correct language direction of the message. If your app supports multiple locales, dynamic direction binding can help.
* Screen reader behavior can vary across Android (TalkBack) and iOS (VoiceOver). Test thoroughly on real hardware to confirm the experience.

#### Focus Configuration

**Focus Configuration** helps improve keyboard and remote-control navigation in your app—especially important for web, desktop, TV, and kiosk apps. It controls how users move through widgets using the `Tab` key or other navigation inputs (like arrow keys or D-pad on TV or remote).

You can control the Focus Configuration using the following properties:

* **Wrap in Focus Traversal Group**: It places a widget (and all its children) in a dedicated group so focus cycles within that region before moving on. For example, if you have a login form with two fields: Email and Password, enabling this option ensures that pressing `Tab` will cycle only between them (and not jump to unrelated parts of the screen).
* **Focus Traversal Order**: This sets the exact sequence in which widgets receive focus using numeric values (e.g., 1, 2, etc.). For example, In a sign‑up form, set `Name = 1`, `Email = 2`, and `Password = 3` so pressing `Tab` moves logically down the form rather than following the raw widget tree.
* **Show Border on Focus**: Enabling this toggle highlights the widget with a visible border when it receives focus, making navigation clearer. Once enabled, you can customize the border’s appearance using **Border Width**, **Border Color**, and **Border Radius** to match your design.

> **Warning:** While you can assign a value for the **Focus Traversal Order** of any widget, it won’t take effect unless you enable **Wrap in Focus Traversal Group** on the current widget or one of its parent widgets.

The **Focus Traversal Group** defines a context or scope for focus traversal, and **Focus Traversal Order** only applies within that group. Without it, there's no defined order for the traversal logic to follow.

#### Update Text Scaling Factor \[Action]

The **Update Text Scaling Factor** action in FlutterFlow allows you to dynamically adjust the text size across your app during runtime. This is particularly useful for improving accessibility by letting users control the size of the text without having to manually change system settings.

Imagine you have a "+" and "-" button on a page to help users adjust text size. When the user taps the "+" button, the text scaling factor increases by 1, making the text larger. Tapping the "-" button decreases the text scaling factor by 1, making the text smaller. Additionally, a Reset button can be provided to return the text scaling back to its default value.

> **Info:** This action works in conjunction with the [**Display Settings**](https://docs.flutterflow.io/resources/projects/settings/general-settings#display-settings) configured at the project level, such as **Min Text Scaling Factor** and **Max Text Scaling Factor**.

When configuring the Update Text Scaling Factor action, you can choose from three update types:

* **Set Value**: Directly assigns the text scaling factor to a specific value.
* **Increment/Decrement**: Adjusts the current scaling factor by a specified amount. A positive value increases scaling, and a negative value decreases it.
* **Reset**: Restores the text scaling factor to the project's default setting.

![text-scaling-action](https://docs.flutterflow.io/assets/images/text-scaling-action-8c7c4afe7cb0c3575599aecae82eb60e.avif)

#### Keyboard Navigation

You can use the [On Shortcut Press](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#on-shortcut-press-action-trigger) action trigger to bind keyboard shortcuts to specific actions. This makes it easier for users with disabilities to navigate your app, especially in web and desktop environments.

It enhances accessibility by allowing users to interact without relying solely on a mouse or touchscreen, making the experience more inclusive and efficient.

#### Haptic Feedback

Using [Haptic Feedback](https://docs.flutterflow.io/concepts/alerts/haptic-feedback), you can vibrate the user's device, which is particularly helpful for users with visual or cognitive impairments. It provides a tactile response to indicate that an action has been completed.

For example, vibrating the user's device when successfully submitting a form.

#### Responsive Fonts

When developing an app, it's important to consider the different platforms on which it will run. Text may appear smaller on devices with higher screen resolution, such as tablets, web, or desktops, which can negatively impact accessibility for users with visual impairments.

[Adding responsive text](https://docs.flutterflow.io/concepts/design-system#adding-responsive-text-styles) that adjusts font size based on the platform helps make content more readable, improving accessibility for users who need larger or more legible text.

#### Color Contrast

Use sufficient color contrast to make text and interactive elements readable for users with visual impairments or color blindness. This helps ensure that content is easily distinguishable, even for users with limited vision. Learn more about using various ways to [add colors](https://docs.flutterflow.io/concepts/design-system#colors) in your FlutterFlow app.

> **Tip:** You can use tools like [**WCAG Contrast Checker**](https://webaim.org/resources/contrastchecker/) to validate the color contrast ratio.

#### Best Practices

* Accessibility should be considered from the start of the design and development process, not added as an afterthought.

* While adding [semantic labels](https://docs.flutterflow.io/concepts/accessibility#semantic-label): * Avoid ambiguous labels like "Click here" or "Press this"; instead, use descriptive phrases such as "Submit form" or "Navigate to settings."
  * Instead of just showing an icon, add semantic labels like "Back button" or "Search button" to provide context for screen readers.

* Ensure that interactive widgets have a minimum touch target size of 48x48 logical pixels. This helps users with motor impairments easily interact with buttons, switches, and other components.

* Always test your app with screen readers enabled to verify that it behaves as expected.

* Don't use color as the only means to convey important information. Include text, icons, or patterns to supplement color, making the content accessible to colorblind users.

* Verify your app's UI under high contrast or larger text sizes to ensure it remains readable and usable.

* Use simple gestures like taps and double-taps instead of multi-finger swipes or long presses. Provide alternate ways to perform actions, such as using a button in addition to a swipe gesture.

* Perform usability tests with individuals with disabilities. Real user feedback is invaluable for identifying issues that might not be caught during standard testing.

---

### Integrating Native SDKs Using Method Channels {#integrating-native-sdks-using-method-channels}

*Learn how to integrate third-party native SDKs into your FlutterFlow project using Method Channels. This guide walks through setting up channels, writing native code, and connecting it back to FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/advanced/method-channels

Flutter lets you build one app that runs on mobile, web, desktop, and embedded experiences from a single codebase. You write your app logic in Dart once, which is then compiled natively for the target platform. This is a big advantage for teams that want to reduce duplication between Android and iOS apps while maintaining great performance and flexibility.

For native developers accustomed to Kotlin, Java, Swift, or Objective-C, Flutter provides access to platform-specific functionality. The bridge between Dart and native code is called a **MethodChannel**.

You can think of it as a two-way door: Dart can ask Android or iOS to run some code, and the platform can send results back. The two sides communicate using messages, rather than shared memory, which makes the system simple and secure.

With MethodChannels, you can:

* Call Android and iOS APIs that aren’t built into Flutter.
* Use advanced third‑party SDKs (e.g., barcode scanners, Bluetooth libraries, custom UI components).
* Perform operations that need native performance or device-specific access.
* Return data from the native side into Flutter with low latency.

**Why this matters for native engineers**

| What you need            | How MethodChannel helps                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------- |
| Reach every platform API | You can call any Android or iOS API from Flutter using familiar native code.                    |
| Keep the app smooth      | Messages are encoded in binary and handled asynchronously, so the UI remains responsive.        |
| Keep the key code native | You can keep performance-sensitive or secure logic in Kotlin/Swift while building UI in Dart.   |
| Bridge advanced SDKs     | Integrate with native libraries that do not have Flutter support, without waiting for a plugin. |

You’re not limited by what Flutter provides out of the box. MethodChannels lets you plug in your native knowledge exactly where needed, so you don’t lose years of platform experience when moving to Flutter.

#### What is a MethodChannel?

A **[MethodChannel](https://docs.flutter.dev/platform-integration/platform-channels)** or **Platform Channels** is Flutter’s core mechanism for integrating platform-specific functionality. It allows Dart code to send messages to, and receive responses from, the host platform’s native code - Android (written in Kotlin or Java) or iOS (written in Swift or Objective-C). This enables your Flutter app to access device features and third-party native libraries that are outside the scope of the Flutter framework or its plugin ecosystem. Here is an example of MethodChannel.

```
class _BatteryLevelScreenState extends State<BatteryLevelScreen> {

  // Define the MethodChannel with a unique name. This name must match the one used on the native side.
  static const platform = MethodChannel('com.example.battery');

  // Variable to hold the battery level.
  String _batteryLevel = 'Unknown battery level.';

  // Method to invoke the native method to get the battery level.
  Future<void> _getBatteryLevel() async {
    String batteryLevel;
    try {
      // Invoke the method on the native side.
      final int result = await platform.invokeMethod('getBatteryLevel');
      batteryLevel = 'Battery level at $result%.';
    } on PlatformException catch (e) {
      // Handle exception if the native code fails.
      batteryLevel = "Failed to get battery level: '${e.message}'.";
    }

    // Update the UI with the retrieved battery level.
    setState(() {
      _batteryLevel = batteryLevel;
    });
  }
```

MethodChannels operate over a named channel using a message-passing model. You define a unique **channel name**, such as `'com.example/device'`, and both the Flutter and native sides agree to use it. On the Dart side, you call a method using `invokeMethod()`, sending an optional payload. The platform side sets up a listener (known as a method call handler) that waits for these invocations, runs native logic, and returns a result.

This message flow is asynchronous and decoupled:

* Dart code doesn’t block while the native code runs; it returns a `Future` that resolves when the result is ready.
* Native code must explicitly return a result using either `success`, `error`, or `notImplemented`, ensuring consistent feedback.

##### Key Concepts

* **Channel Name**: A unique identifier string that both Flutter and native code must use. Example: `'com.example/platform'`. Naming collisions should be avoided by namespacing based on your app or organization.
* **Method Invocation**: Flutter calls `invokeMethod('methodName', arguments)`. The method name is a simple string. Arguments can be null or any value supported by Flutter’s `StandardMessageCodec` (bool, int, double, string, List, Map).
* **Method Handler**: Native code uses a handler (e.g., `setMethodCallHandler` on Android) to listen for calls and run logic when the specified method name is matched.
* **Result Callback**: The native handler must return a result via `result.success(...)`, `result.error(...)`, or `result.notImplemented()`. These responses are passed back to Dart, completing the `Future`.

##### Example Message Flow

![method-channels.avif](https://docs.flutterflow.io/assets/images/method-channels-ec81d7359e3e6892c652e1b5905c3bee.avif)

This design ensures clear separation between platform and UI logic, and it keeps the UI thread non-blocking for both Dart and native sides. It also makes the communication extensible—you can define as many methods as you need over a single channel or use multiple channels for modular organization.

##### When to Use a MethodChannel

MethodChannel is most appropriate when:

* You need to use Android/iOS APIs not available in Flutter or plugins (e.g., access to specific hardware sensors, native storage APIs).
* You need to integrate a proprietary or vendor SDK (e.g., analytics, payment, OCR) written for the platform.
* You need to launch a platform-native UI (e.g., a full-screen scanner or a native file picker).
* You’re bridging a legacy native feature into a Flutter app or gradually migrating a native app to Flutter.

##### What MethodChannels Are Not

* They are not **shared memory** - All data is copied through serialization, not shared by reference. Only standard types are supported (primitives, lists, maps, typed data). Large data transfers require full serialization/deserialization.
* They are **not synchronous** - Calls return Futures immediately without blocking. Results arrive asynchronously via the event loop. Platform errors surface as PlatformExceptions when the Future completes.
* They are **not opinionated** - You define the API contract (method names, arguments, types) on both sides. There's no compile-time validation across the boundary - mismatches fail at runtime. Document your contract and validate inputs since type safety isn't enforced.

By understanding these characteristics, you can create robust, maintainable bridges between Dart and native code. You can write minimal, purpose-driven native handlers and keep the rest of your app in Flutter, achieving both deep platform access and cross-platform speed.

#### Real-World Use Cases for MethodChannels

While Flutter plugins cover many common platform integrations, there are frequent scenarios where you require direct access to native SDKs or platform-specific APIs. MethodChannels offer a direct path for these integrations without waiting for third-party plugin support.

Ultimately, method channel integration is essentially plugin development - you're writing the same native bridge packaged for your app instead of as a public package. Once complete, it can be imported into FlutterFlow. The following examples show when building your own native integration is more practical than waiting for or wrestling with existing plugins. The following examples outline situations where MethodChannels are suitable.

##### Accessing Device Hardware Not Exposed by Plugins

**Example:** Retrieve mobile network signal strength, advanced battery metrics, or thermal status.

* Low-level APIs like Android's `TelephonyManager` or iOS's `CoreTelephony` are rarely exposed through Flutter plugins.
* These require direct permission management and native invocation.
* With MethodChannels, you can call only what you need, without waiting for a plugin update or writing one from scratch.

**Benefit:** Access hardware-level telemetry or diagnostics crucial for field-service apps, testing tools, or enterprise reporting.

##### Integrating Proprietary SDKs or Vendor Libraries

**Example:** Use a third-party identity verification SDK, document scanner, or encrypted storage SDK.

* Many vendors distribute Android/iOS SDKs only and have no Flutter wrappers.
* A minimal native wrapper and MethodChannel interface let you expose only the needed functionality.
* Native SDK updates remain decoupled from Flutter UI changes.

**Benefit:** Unlocks core business features (KYC, biometrics, payments) without dependency on plugin authors or external wrappers.

##### Embedding Native UI Views Temporarily

**Example:** Show a native PDF viewer, a camera UI from a vendor SDK, or an AR interface.

* `PlatformView` allows embedding native UI, but it requires more setup and introduces performance tradeoffs.
* If the native UI is temporary or full-screen, you can invoke it via MethodChannel and return control to Flutter afterward.

**Benefit:** Delivers platform-native experiences where needed while preserving Flutter’s rendering pipeline elsewhere.

##### Background Tasks and Event-Driven Native APIs

**Example:** Respond to geofencing events, push token refresh, or Bluetooth device state changes.

* These use cases originate in native services or background tasks.
* You can queue or debounce events on the native side and send them to Flutter via MethodChannel when the app is active.
* For continuous updates, use `EventChannel`, as MethodChannel is ideal for transactional or one-off data transfers.

**Benefit:** Achieves OS-level integration (e.g., location, power, Bluetooth) without polling or Dart-side complexity.

##### Secure Device Data Retrieval

**Example:** Fetch IMEI, MAC address, device fingerprint, or system identifiers.

* These APIs often require special entitlements and native-side permission prompts.
* Native logic can validate permissions, sanitize data, and decide what’s safe to return.

**Benefit:** Ensures security-sensitive operations remain native-controlled, supporting enterprise, regulated, or BYOD environments.

#### Implementing a MethodChannel

This section walks through the complete implementation of a MethodChannel, showing how to define the channel in Flutter (Dart), connect it to native platform code, and properly exchange messages, arguments, and results. For native developers used to Android or iOS, this breakdown will show how to bridge Dart and native code in a way that is robust, testable, and production-ready.

##### 1. Dart Side (Flutter)

In Flutter, you use the `MethodChannel` class from the `services` package to create a communication path. The Dart side always initiates the call, and the native side responds.

**Define and Use a Channel:**

```
import 'package:flutter/services.dart';
const platform = MethodChannel('com.example/device');
```

* The channel name `'com.example/device'` must match **exactly** with the one used on the native side.
* Channel names should follow a reverse-domain convention to avoid collisions.

**Sending a Method Call:**

```
Future<String> getBatteryLevel() async {
  try {
    final int result = await platform.invokeMethod('getBatteryLevel');
    return 'Battery level: $result%';
  } on PlatformException catch (e) {
    return 'Failed to get battery level: ${e.message}';
  }
}
```

* `invokeMethod` sends a string method name and optional arguments to native code.

* The result comes back asynchronously via a `Future`.

* Always wrap the call in a `try-catch` block to handle `PlatformException`, which may occur if: * The native method throws an error
  * The method is not implemented
  * Data serialization fails

**Notes:**

* You can pass arguments to `invokeMethod()` as the second parameter (e.g., a `Map<String, dynamic>`).
* The result can be any JSON-compatible Dart type: `int`, `String`, `bool`, `double`, `List`, or `Map`.

##### 2. Android Side (Kotlin)

The Android side handles Dart calls using a `MethodChannel` registered in `MainActivity`. This handler runs on the **main thread** by default, so long-running work should be offloaded to a background thread.

**Setting Up the Channel:**

```
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel
import android.os.BatteryManager
import android.content.Context
```

**Handling the Method Call:**

```
class MainActivity: FlutterActivity() {
  private val CHANNEL = "com.example/device"
  override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
    super.configureFlutterEngine(flutterEngine)
    MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL).setMethodCallHandler {
      call, result ->
      when (call.method) {
        "getBatteryLevel" -> {
          val batteryLevel = getBatteryLevel()
          if (batteryLevel != -1) {
            result.success(batteryLevel)
          } else {
            result.error("UNAVAILABLE", "Battery level not available.", null)
          }
        }
        else -> result.notImplemented()
      }
    }
  }
  private fun getBatteryLevel(): Int {
    val batteryManager = getSystemService(Context.BATTERY_SERVICE) as BatteryManager
    return batteryManager.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
  }
}
```

**Notes:**

* Always return a result using one of the following: * `result.success(data)` — returns data to Dart
  * `result.error(code, message, details)` — throws `PlatformException` in Dart
  * `result.notImplemented()` — throws `MissingPluginException` in Dart

* Do **not** call `result` multiple times. Flutter expects a one-time, one-result reply per method call.

* If your native call involves I/O, network, or anything that blocks, use a background thread:

```
    Thread(Runnable {
        val resultData = longRunningOperation()
        runOnUiThread {
            result.success(resultData)
        }
    }).start()
```

##### 3. iOS Side (Swift)

In iOS, the platform channel is handled via `FlutterMethodChannel` in `AppDelegate.swift`. Similar to Android, the method call handler runs on the **main thread** by default.

**Setting Up the Channel:**

```
import UIKit
import Flutter
@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let controller = window?.rootViewController as! FlutterViewController
    let batteryChannel = FlutterMethodChannel(name: "com.example/device",
    binaryMessenger: controller.binaryMessenger)
```

**Handling the Method Call:**

```
    batteryChannel.setMethodCallHandler { (call: FlutterMethodCall, result: @escaping FlutterResult) in
      if call.method == "getBatteryLevel" {
        UIDevice.current.isBatteryMonitoringEnabled = true
        let level = UIDevice.current.batteryLevel
        if level >= 0 {
          result(Int(level * 100))
        } else {
          result(FlutterError(code: "UNAVAILABLE",
                              message: "Battery level not available.",
                              details: nil))
        }
      } else {
        result(FlutterMethodNotImplemented)
      }
    }
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }
}
```

**Notes:**

* Always return exactly one response per method call.
* Use `FlutterError` to send detailed error info to Dart.
* If needed, use `DispatchQueue.global().async` to run long tasks in the background, then return via `DispatchQueue.main.async`.

##### Best Practices on MethodChannels

To implement **MethodChannels** successfully:

* **Use consistent channel and method names** between Dart and native code.
* **Use standard types** for data exchange (prefer `String`, `int`, `bool`, `List`, `Map`).
* **Always handle errors** clearly on both sides.
* **Offload long-running native logic** to background threads.
* **Keep the native side minimal and testable**, separating SDK logic from channel code where appropriate.

By following these steps and patterns, you’ll be able to bridge Flutter with native code cleanly—supporting deep platform integrations while maintaining a smooth UI and maintainable codebase.

#### Integrating MethodChannels in FlutterFlow

FlutterFlow is a visual development platform that generates complete Flutter applications. While it supports writing custom Dart code through **Custom Actions** and **Custom Functions**, it does not allow direct editing of platform-native code (Kotlin, Swift) through its web UI. This introduces some important considerations when integrating Flutter’s `MethodChannel` API for platform-specific functionality.

**Step 1: Create a Custom Flutter Plugin**

**1.1 Initialize the Plugin**

Use the Flutter CLI to create a new plugin:

```
flutter create --template=plugin --platforms=android,ios my_custom_plugin
```

This command sets up a plugin project with the necessary structure for both Android and iOS platforms.

**1.2 Implement Platform-Specific Code**

Within the generated plugin, navigate to the platform-specific directories (`android` and `ios`) to implement the desired functionality. For example, to retrieve the device's battery level:

* **Android (Kotlin):** Modify `MyCustomPlugin.kt` to access the battery information using Android's `BatteryManager`.
* **iOS (Swift):** Update `MyCustomPlugin.swift` to utilize `UIDevice` for battery level retrieval.

**1.3 Publish to GitHub**

After implementing and testing your plugin:

1. Initialize a Git repository in your plugin directory.
2. Commit your changes.
3. Push the repository to GitHub.

Ensure your `pubspec.yaml` is correctly configured, and consider tagging releases for versioning.

**Step 2: Add the Plugin as a Dependency in FlutterFlow**

To integrate your custom plugin into a FlutterFlow project:

1. Navigate to **Custom Code > Custom Actions** or **Custom Widgets** in FlutterFlow.

2. Create a new Custom Action or Widget.

3. In the **Settings** panel on the right, scroll to **Dependencies**.

4. Add your plugin using the Git URL:

   ```
     my_custom_plugin:  
       git:  
         url: https://github.com/yourusername/my_custom_plugin.git
   ```

5. In the code editor, import your plugin:

   ```
   import 'package:my_custom_plugin/my_custom_plugin.dart';`
   ```

6. Implement the desired functionality using the plugin's API.

For detailed guidance, refer to FlutterFlow's documentation on [using unpublished or private packages](https://docs.flutterflow.io/concepts/custom-code/#using-unpublished-or-private-packages).

**Step 3: Utilize the Plugin via Custom Actions in FlutterFlow**

With the plugin integrated, you can now create Custom Actions to leverage its functionality:

1. Define a new Custom Action in FlutterFlow.

2. In the code editor, implement the action using your plugin. For example:

   ```
     Future<int> getBatteryLevel() async { 
       final batteryLevel = await MyCustomPlugin.getBatteryLevel();  
       return batteryLevel;  
     }
   ```

3. Compile the custom code to ensure there are no errors.

4. Use this Custom Action within your FlutterFlow project's action flows, just like any built-in action.

This approach allows you to encapsulate complex logic within reusable actions, enhancing modularity and maintainability.

##### Managing Private Repositories

If your plugin repository is private, FlutterFlow needs access to it. As per FlutterFlow's documentation, you may need to provide authentication credentials or use SSH keys. Refer to the [FlutterFlow documentation](https://docs.flutterflow.io/concepts/custom-code#using-unpublished-or-private-packages) for detailed instructions on integrating private packages.

#### Common Pitfalls and Debugging

MethodChannels are powerful but require careful implementation. When the Dart and native sides are not aligned, or error handling is overlooked, it often leads to runtime issues or silent failures. This section outlines the most common problems developers face with MethodChannels, especially in projects generated by tools like FlutterFlow, and provides actionable solutions to help you debug effectively and write resilient platform-channel integrations.

##### MissingPluginException

**Symptom:** Flutter throws a `MissingPluginException`, typically saying the plugin or method is not implemented.

**What it means:** Flutter tried to invoke a method on the MethodChannel, but the native side did not recognize the channel or method name.

**Common causes:**

* Dart `MethodChannel` name does not match the native channel name.
* Native code handler (`setMethodCallHandler`) was never set up or was incorrectly placed.
* Custom native code was overwritten when re-downloading a FlutterFlow project without preserving changes.
* The method was invoked before the Flutter engine or the channel was fully initialized.
* Hot reload only updates Dart code, but not with native channel implementations.

**How to fix:**

* Confirm that the channel name is **identical** in Dart and native code (case-sensitive).
* On Android, ensure the channel is registered inside `configureFlutterEngine()`.
* On iOS, set up the `FlutterMethodChannel` inside `didFinishLaunchingWithOptions()`.
* Log the available channels/methods to confirm registration during app startup.
* Native channel implementations require a full restart because the platform-specific code must be recompiled and relinked.

##### Incorrect Argument or Result Types

**Symptom:** App crashes with type casting errors or returns `null` unexpectedly.

**What it means:** The data passed between Dart and native does not match expected formats.

**Common causes:**

* Dart sends an argument as a Map but native expects a String, or vice versa.
* Native code returns a platform object that can't be serialized by Flutter.
* The return value is not compatible with `StandardMessageCodec`.

**How to fix:**

* Only use standard types: `int`, `double`, `String`, `bool`, `List`, or `Map` with JSON-safe contents.
* On Dart side, specify the expected return type with generics: `invokeMethod<int>(...)`.
* On native side, validate input types before using them. Consider using try/catch or safe casting.
* Avoid sending complex objects like native SDK responses directly—convert to a simple dictionary or string.

##### No Response or App Hangs

**Symptom:** The Dart call to `invokeMethod()` never returns, or the UI freezes.

**What it means:** The native side didn’t complete the method call correctly, or a long-running task is blocking the UI thread.

**Common causes:**

* Native method handler fails to call `result.success`, `result.error`, or `result.notImplemented`.
* The method call handler throws an exception that prevents the response from being sent.
* Heavy logic (e.g., file I/O, network calls) is blocking the main thread.

**How to fix:**

* Always call one—and only one—of the result callbacks.
* Wrap native code in try/catch blocks to catch and report any exceptions.
* Offload slow operations to a background thread or coroutine (Kotlin) or dispatch queue (Swift).
* Use Dart timeouts or loading indicators to keep the UI responsive while waiting.

##### Calling `result` Multiple Times

**Symptom:** The app crashes with a runtime error like "Reply already submitted" or shows inconsistent results.

**What it means:** The native code responded more than once for the same method call.

**Common causes:**

* Both success and error branches are executed due to logic errors.
* Async operations or callbacks race to return multiple responses.
* A timeout, retry, or exception causes unintended second calls.

**How to fix:**

* Track whether a response has been sent using a flag (e.g., `var responded = false`).
* Use return statements or guards to prevent multiple result calls.
* Structure async callbacks carefully to ensure only one callback path runs.

##### Debugging Tips by Platform

**Flutter/Dart:**

* Use `print()` or `debugPrint()` to log method calls and results.
* Always wrap `invokeMethod` in `try/catch` and log exceptions.
* Add logs before and after `invokeMethod()` to verify flow.
* Use Flutter DevTools to inspect console logs and application state.

**Android (Kotlin/Java):**

* Use `Log.d("MethodChannel", "Received: ${call.method}")` inside the handler.
* Use `adb logcat | grep flutter` to filter platform logs.
* Ensure `configureFlutterEngine()` is actually called—older project setups may require manual configuration.
* Use breakpoints in Android Studio for step-by-step inspection.

**iOS (Swift/Objective-C):**

* Use `print()` or `NSLog()` to trace handler execution.
* Watch the Xcode console for startup logs or channel registration issues.
* Ensure you're calling `result(...)` correctly and only once.
* Check if the `AppDelegate` is properly casting `window?.rootViewController` to `FlutterViewController`.

By understanding and anticipating these pitfalls, developers can avoid common errors that derail Flutter-to-native communication. MethodChannels are extremely reliable when implemented correctly, and with structured debugging, most issues can be diagnosed and resolved quickly—even in FlutterFlow-generated apps where visibility into the build system may be limited.

#### Performance and Architecture Best Practices

Integrating native functionality through MethodChannels can bring significant value to your app - but only if it’s done with performance and maintainability in mind. Below are the five most important best practices engineers should apply in real-world production apps, along with deeper insights into why each one matters.

Important Context for FlutterFlow Users

FlutterFlow generates clean Dart code and supports Custom Actions for inserting Dart logic, but it does not currently support inline native (Kotlin/Swift) editing.

##### Don’t Block the Main Thread

* By default, all MethodChannel calls are handled on the **main UI thread**, which is also responsible for rendering the app.
* Native operations like database access, file I/O, Bluetooth scanning, or network requests **must** be moved off the main thread.
* Use background threads (e.g., `Executors` or `coroutines` on Android, `DispatchQueue.global()` on iOS) to perform long-running tasks.
* Return results on the main thread using `runOnUiThread` (Android) or `DispatchQueue.main.async` (iOS).

Blocking the UI thread for even a few milliseconds can cause dropped frames, janky animations, and a visibly unresponsive app, especially on mid-range devices.

> **Tip:** While UI interactions and workflows look smooth inside FlutterFlow, once you export and test the app on a real device, slow operations in Kotlin or Swift can still freeze the app. Always delegate those tasks to background threads before calling back into Dart.

##### Keep MethodChannel Code Minimal

* Your MethodChannel handler should act like a **controller**, not a service. It should delegate execution to well-structured, modular native components.
* This keeps the interface between Dart and native thin and easy to maintain.
* For example, `getBatteryLevel` in Kotlin should just delegate to `BatteryService().getLevel()`.
* This separation helps native teams evolve platform code independently of Flutter UI updates.

Clean separation of concerns leads to better test coverage, easier onboarding, and avoids hard-to-debug cross-layer bugs.

##### Use Only JSON-Compatible Data

* The Flutter engine uses `StandardMessageCodec` for MethodChannel communication.
* It supports only a limited set of Dart-native types: `int`, `double`, `bool`, `String`, `List`, `Map`, and `null`.
* Any native types (e.g., `Bitmap`, `Bundle`, `NSData`, `UIColor`) must be converted to a JSON-friendly structure first.
* If data is complex (e.g., a barcode result or device info), serialize it to a flat Map or a JSON string before sending it across.

Type mismatches across the bridge don’t fail at compile time—they crash at runtime. Keeping your types simple prevents hard-to-diagnose issues.

> **Tip:** When using Dart Custom Actions that invoke MethodChannels, ensure the return values can be used in FlutterFlow bindings. Only supported types (like `String` or `int`) can be stored in App State or used in conditions or widgets.

##### Validate and Sanitize Dart Inputs

* Treat incoming Dart method calls like external API requests. Assume they can be malformed.
* Use pattern matching (switch/case or `when`) to route and verify each method call.
* Validate presence and type of arguments before using them. For example:

```
val timeout = call.argument<Int>("timeout") ?: return result.error("INVALID", "Missing timeout", null)
```

* Defensive coding helps avoid unexpected behavior, native crashes, or incorrect hardware usage.

Dart developers might call your method incorrectly. Native code must fail safely and visibly.

> **Tip:** Custom Actions in FlutterFlow can include parameters from the UI, but if the parameter isn’t set or passed correctly in a workflow, the Dart code will still execute. Validate these inputs natively before use.

##### Log Clearly on Both Sides

* Add logging on both Dart and native layers for every MethodChannel call: * What method was called?
  * What were the arguments?
  * What was returned, and how long did it take?

* Use structured logs (`Log.d("MethodChannel", "method=... args=... result=...")` on Android, `NSLog` or `print()` on iOS).

* Align log timestamps across layers to help trace issues during debugging sessions.

When something goes wrong in production, good logs make the difference between a 10-minute fix and a multi-day investigation.

> **Tip:** Use `debugPrint()` inside Dart Custom Actions to log output alongside platform logs. In test builds, these logs help verify whether native results are arriving as expected.

#### Summary & Guidance

MethodChannels are a foundational tool for extending the power of your app beyond what plugins alone can provide. They allow direct access to platform-native APIs and SDKs, enabling teams to solve tough integration challenges and deliver production-grade features with full control.

But like any system boundary, MethodChannels require disciplined design. Misuse can lead to fragile bridges, performance bottlenecks, and increased maintenance overhead. When implemented thoughtfully, MethodChannels provide:

* A clean interface between Dart and native layers
* Strategic reuse of platform-optimized SDKs and APIs
* A clear path to ship advanced features without waiting on plugin ecosystems
* A sustainable integration model that scales with your team and product

Flutter will continue to evolve with innovative solutions for platform interoperability in the future through two key tools: FFIgen and JNIgen. FFIgen automates the creation of Objective-C and Swift API bindings, while JNIgen handles Java and Kotlin API connections, making native code integration more streamlined and maintainable across platforms.

---

### Alert Dialog {#alert-dialog}

*The action allows you to alert the user of important situations that require acknowledgment in the form of a pop-up or custom-designed dialog. With this feature, you can choose to display a pre-built pop-up or create a custom design that suits your specific requirements.*

**Source:** https://docs.flutterflow.io/concepts/alerts/alert-dialog

The action allows you to alert the user of important situations that require acknowledgment in the form of a pop-up or custom-designed dialog. With this feature, you can choose to display a pre-built pop-up or create a custom design that suits your specific requirements.

##### Types of Alert Dialog

We allow you to define two types of Alert Dialog Actions:

* **Informational Dialog:** To show some information the user should be aware of before interacting with the app. Contains only a single action button.
* **Confirm Dialog:** This dialog can contain two action buttons. It can trigger the subsequent action based on whether a user confirms the action. It can also be used before performing any non-revertable user action, for example, before deleting a user account.
* **Custom Dialog**: This is a fully customizable dialog that you can create using [components](https://docs.flutterflow.io/resources/ui/components).

##### Adding Informational Dialog \[Action]

Follow the steps below to add this type of action to any widget:

1. Select the **Widget** (e.g., Button) on which you want to add the action.
2. Select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.
3. Search and select the **Alert Dialog** (under *Alerts/Notifications*) action.
4. Set the **Alert Dialog Type** to **Informational Dialog**.
5. Provide the **Title** and **Message** for the dialog. Note: You can also set it from a variable; for example, a combined text with a value from a variable.
6. Also, enter a **Dismiss Text** that will be shown on the action button.

##### Adding Confirm Dialog \[Action]

Follow the steps below to add this type of action to any widget:

1. Select the **Widget** (e.g., Button) on which you want to define the action.

2. Select **Actions** from the Properties panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window. 1. Click on the **+ Add Action**.

   2. On the right side, search and select **Alert Dialog**.

   3. Set the **Alert Dialog Type** to **Confirm Dialog**.

   4. Provide the **Title** and **Message** for the dialog. Note: You can also set it from a variable; for example, a combined text with a value from a variable.

   5. Now, enter a **Dismiss Text** (shown on the action button that will cancel the Action) and a **Confirm Text** (shown on the action button that will trigger the Action that you will define in the next step).

   6. Now, click on the **+** button and select **Add Conditional**.

   7. On the right side (**Set Condition for Action**), set the **Source** to **Confirm Dialog Response**. 1. Under the **TRUE** section, add an action that will be triggered if a user gives confirmation.
      2. Under the **FALSE** section, add an action that will be triggered if a user cancels this dialog.

3. Click **Close**.

##### Adding Custom Dialog \[Action]

Before you add this action, ensure you [create a component](https://docs.flutterflow.io/resources/ui/components/creating-components) that you want to display as a custom dialog. Now follow the steps below to add this type of action to any widget:

1. Select the **Widget** (e.g., Button) on which you want to add the action.

2. Select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.

3. Search and select the **Alert Dialog** (under *Alerts/Notifications*) action.

4. Set the **Alert Dialog Type** to **Custom Dialog** and **Select Component**.

5. It is recommended to set the appropriate **Width** and **Height** for the custom dialog.

6. Optionally, you can set the **Background** and **Barrier Color** for this dialog.

   ![Setting background color and barrier color](https://docs.flutterflow.io/assets/images/custom-dialog-f68560d78150e1f20ecaed3aab6b928f.avif)

7. By default, this type of action blocks the following action (if any) from triggering while this action is in progress, meaning the dialog is present on the screen. However, in some cases, you might want to allow the next action (after this) to execute, for example, making an API call immediately after showing the custom loading dialog. To do so, enable **Non Blocking** option.

8. By default, **Non Dismissble** option closes the dialog when you click outside of it. To disable this behavior, enable this option.

9) By default, the custom dialog appears in the center of the screen. However, you can use the **Dialog Alignment** property to decide where to position the dialog on the screen.

   ![Align custom dialog](https://docs.flutterflow.io/assets/images/align-custom-dialog-f591108c3294aec8394816920e839921.avif)

10) To position the dialog around the widget that opened it, enable the **Align with the Target Widget**, and then align using the **Target Alignment** property. **Tip**: If dialog goes out of the screen, enable **Avoid Overflow**.

---

### Dismiss Custom Dialog {#dismiss-custom-dialog}

*With this action, you can easily close the custom dialog, providing a convenient way for users to dismiss it. This functionality is handy when you want to give users the option to close the dialog from any widget within it, like a close button.*

**Source:** https://docs.flutterflow.io/concepts/alerts/dismiss-custom-dialog

With this action, you can easily close the [custom dialog](https://docs.flutterflow.io/concepts/alerts/alert-dialog#adding-custom-dialog-action), providing a convenient way for users to dismiss it. This functionality is handy when you want to give users the option to close the dialog from any widget within it, like a close button.

#### Adding Dismiss Custom Dialog \[Action]

Follow the steps below to add this type of action to any widget:

1. Select the **Widget** (e.g., Button) on which you want to add the action.
2. Select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.
3. Search and select the **Dismiss Custom Dialog** (under *Alerts/Notifications*) action.
4. You can set a default value to be sent when the user closes the custom dialog. You can do so by enabling the **Has Value** option. For instance, if the dialog provides a list of colors and the user closes it without selecting any color, you can set a default color value of "Black" to be sent as the default selection.

![Adding Dismiss Custom Dialog action](https://docs.flutterflow.io/assets/images/adding-dismiss-custom-dialog-action-84538fcd13850dd52da4c5c24f4a1aac.png)

---

### Haptic Feedback {#haptic-feedback}

*Using this action, you can vibrate the user's device. Typically this is used to draw users' attention to the action they have performed. For example, vibrating the user's device on setting the alarm.*

**Source:** https://docs.flutterflow.io/concepts/alerts/haptic-feedback

Using this action, you can vibrate the user's device. Typically this is used to draw users' attention to the action they have performed. For example, vibrating the user's device on setting the alarm.

#### Types of Haptic Feedback

Depending on the action a user has performed (e.g., bookmark an item, on-off flashlight), you can set the different vibration intensity and duration types.

Here are the types of haptic feedback:

1. **Light**: This creates a very low-intensity vibration similar to pressing a virtual on-screen key.
2. **Medium**: This creates a medium-intensity vibration similar to pressing a key on a keyboard.
3. **Heavy**: This creates a high-intensity vibration similar to clicking an item.
4. **Selection Click**: This vibrates the device when selection changes through discrete values. Similar to changing hours and minutes on the clock app.
5. **Vibrate**: This creates a vibration for a short duration.

> **Warning:** * The *Light*, *Medium*, *Heavy*, and *Selection Click*, these types of haptic feedback only work on iOS version 10 and above.
* The *Selection Click* type only works on Android API levels 23 and above.

#### Adding Haptic Feedback \[Action]

Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to define the action.
2. Select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.
3. Search and select the **Haptic Feedback** (under *Alerts/Notifications*) action.
4. Set the **Feedback Type** among the **Light**, **Medium**, **Heavy**, **Selection Click**, and **Vibrate**.

---

### Animations {#animations}

*Learn the basics of animations in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/animations

Enhancing your app with animations significantly improves the user experience, making it more engaging and intuitive. In FlutterFlow, you have several options to add animations to your app:

* [**Widget Animations**](https://docs.flutterflow.io/concepts/animations/widget-animations): Add animation effects to an entire widget.
* [**Implicit Animations**](https://docs.flutterflow.io/concepts/animations/implicit): Animate changes in specific widget properties, such as the height of a Container.
* [**Hero Animations**](https://docs.flutterflow.io/concepts/animations/hero-animations): Animate a widget that transitions smoothly between screens, also known as shared element transitions.
* [**Page Transition Animations**](https://docs.flutterflow.io/concepts/animations/page-transition): Specify transitions between pages within your app.
* **Import Animations**: Import animations you've created using other tools such [lottiefiles](https://docs.flutterflow.io/concepts/animations/lottie-animation) and [Rive](https://docs.flutterflow.io/concepts/animations/rive-animation).
* [**Shaders**](https://docs.flutterflow.io/concepts/animations/shaders): Add GPU-powered visual effects like animated backgrounds, distortions, and interactive touch-based visuals to enhance your UI.

To learn more about animations in FlutterFlow, check out this video:

[YouTube video player](https://www.youtube.com/embed/-quxi_t0eWU?si=GdZBMFcuEZEyFplB)

---

### Hero Animation {#hero-animation}

*Learn how to add Hero Animations in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/animations/hero-animations

"Hero" is a widget that gracefully transitions from one screen to another. For instance, on a product listing page, clicking on a product's image triggers a smooth animation where the image flies to a new screen, revealing detailed information about the product.

#### Creating Hero Animation

Let's how to create hero animation with an example that looks like the one below:

![hero-animation-image-widget.gif](https://docs.flutterflow.io/assets/images/hero-animation-image-widget-5338d8ec61a3451fc894306e233fe913.gif)

> **Info:** Building Hero Animation requires you to have at least two pages that share the same image.

The steps to build such an example are as follows:

1. On the first page, select the image, head over to the properties panel, enable **Use Hero Animation**, and **Add Hero Tag**.

2. On the second page, select the image, head over to the properties panel, enable **Use Hero Animation**, and select the **Hero Tag** that you created on the first page component.

3. Add [navigation action](https://docs.flutterflow.io/concepts/navigation/page-navigation#navigate-to-action) from page 1 to page 2.

#### Hero Animation on Component

You can also add hero animation on a custom component. Let's see how to build an example that looks like the one below:

Before you begin,

* Make sure you have a component added to both the first and second pages.
* For a smoother and more appealing hero animation effect, ensure that the components on both pages have a somewhat similar appearance. This enhances the overall visual impact of the animation.

The steps to add hero animation on a component are as follows:

1. On the first page, select a component, head over to the properties panel, enable **Use Hero Animation**, and **Add Hero Tag**.

2. On the second page, select a component, head over to the properties panel, enable **Use Hero Animation**, and select the **Hero Tag** that you created on the first page component.

3. Add [navigation action](https://docs.flutterflow.io/concepts/navigation/page-navigation#navigate-to-action) from page 1 to page 2.

#### FAQs

Why is the Hero animation not working when navigating forward? Works only backward

This is because the image on the second page does not exist on the very first frame. Hero animation will only work when the image is loaded from an asset or from the network (*if the path is pre-specified*). If you're pulling the image from a Firestore document, it might not be ready in time for the animation to take place.

To fix this issue, you can avoid loading an image directly from Firestore. Instead, you can pass the image URL (which would have already been retrieved from the Firestore) from the previous page to the second page. And then use that URL to load the image.

See how to [pass data](https://docs.flutterflow.io/concepts/navigation/passing-data) from one page to another.

---

### Implicit Animations {#implicit-animations}

*Learn how to add implicit animations in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/animations/implicit

In Implicit Animation, the widget automatically animates to a new property's value when they are updated. For example, the container widget animates whenever you change its size and colors.

> **Info:** Implicit Animation is recommended only when you want to run the animation once (after the properties are changed).

Here are some examples of how it looks when you update the widget properties with and without Implicit Animation.

|               | Without Implicit Animation                                                                                         | With Implicit Animation                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| **Container** | ![Without Implicit Animation](https://docs.flutterflow.io/assets/images/without-implicit-animation-e6592770149d9db9e86d1e9b0b0d4d93.gif)      | ![With Implicit Animation](https://docs.flutterflow.io/assets/images/with-implicit-animation-124cc1e1c70135504c7be7675ad78ef9.gif)     |
| **Text**      | ![Without Implicit Animation](https://docs.flutterflow.io/assets/images/without-implicit-animation-text-b58f28715f01ad899d063ee8d1cbb9c9.gif) | ![Wit Implicit Animation](https://docs.flutterflow.io/assets/images/with-implicit-animation-text-6b252df96edd2f6806e62c49904fea2d.gif) |

Here's an example of how you add the Implicit Animation on Container widget:

---

### Lottie Animation {#lottie-animation}

*Learn how to add Lottie animation in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/animations/lottie-animation

The LottieAnimation widget allows you to display [Lottie files](https://lottiefiles.com/featured) from uploaded assets or the URL link. Lottie files are high quality (they do not pixelate), smaller than GIF, and easy to add to any platform.

For example, you could use the LottieAnimation widget to show a nicely animated loading indicator to provide a great user experience to the users.

#### Adding LottieAnimation

Showing Lottie files in a LottieAnimation widget comprises the following steps:

1. [Getting Lottie files](https://docs.flutterflow.io/concepts/animations/lottie-animation#1-getting-lottie-files)
2. [Adding LottieAnimation widget](https://docs.flutterflow.io/concepts/animations/lottie-animation#2-adding-lottieanimation-widget)
3. [Changing animation source](https://docs.flutterflow.io/concepts/animations/lottie-animation#3-changing-animation-source)

##### 1. Getting Lottie files

The LottieAnimation requires the Lottie file to be added to display the animation on the screen. You can get the Lottie files from its [official collection](https://lottiefiles.com/featured) in two ways.

###### 1.1 Downloading the Lottie JSON file

The Lottie JSON file is required when you want to play the animation from the file uploaded to your project.

To download the Lottie JSON file:

1. Open <https://lottiefiles.com/> and search for the required animation.
2. Select the animation you would like to add. This will open a new popup.
3. Click on the **Download** button and select **Lottie JSON**.

###### 1.2 Copying Lottie animation URL

The Lottie animation URL is required when you want to play the animation from the file hosted at <https://lottiefiles.com/>.

To copy the animation URL:

1. Open <https://lottiefiles.com/> and search for the required animation.
2. Select the animation you would like to add. This will open a new popup.
3. Find the **Lottie Animation URL** (bottom right of the playing animation) and copy it.

> **Info:** The Lottie animation URL is only visible when you are logged in.

##### 2. Adding LottieAnimation widget

To add LottieAnimation widget to your project:

1. Drag the **LottieAnimation** widget from the **Base Elements** tab (in the Widget Panel) or add it directly from the widget tree.
2. Move to the properties panel (on the right side of your screen) and scroll down to the **Lottie Animation** section.
3. Find the **Path** property and enter the **URL** (see how to get it [1.2](https://docs.flutterflow.io/concepts/animations/lottie-animation#12-copying-lottie-animation-url)) for the new Lottie file.
4. By default, the animation will play as soon as the page loads. To disable this and play animation on a button click or any other event, uncheck the **Auto Animate** checkbox.

##### 3. Changing animation source

By default, the widget's animation source is set to network. However, you can change this to use a Lottie file uploaded directly to your app.

Here's how you can change the animation source:

1. Select the **LottieAnimation** widget from the widget tree or the canvas area.
2. Move to the property panel (on the right side of your screen) and scroll down to the **Lottie Animation** section.
3. Find the **Animation Source** dropdown and select .
4. Now, find the **Asset Animation** property, click the **Upload LottieAnimation** button, select the Lottie file and upload it.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

##### Changing animation type

You can control how the animation is played, whether it should play only once, in a loop, or in a boomerang fashion (play back and forth).

To control the animation type:

1. Select the **LottieAnimation** widget from the widget tree or the canvas area.
2. Move to the property panel (on the right side of your screen) and scroll down to the **Lottie Animation** section.
3. Find the **Animation Type** dropdown and select among the **Once**, **Loop**, and **Boomerang**.

* Open
* Loop
* Bomerang

##### Change frame rate

By default, animations are played at the frame rate specified when they are exported from After Effects, usually at 10 or 30 FPS. Modern phones, however, can support higher refresh rates, such as 60 or 120 FPS. If you're not satisfied with how the animation looks at these default settings, you can adjust its frame rate to a smoother 60 FPS for better quality.

To do so, move to the **properties panel** > **Lottie Animation** > enter the value in the **Frame Rate** field.

##### Changing the box fit

Changing the Box Fit value allows you to control how the Lottie file animation should display inside the LottieAnimation widget. Various options under the Box Fit property help you scale (grow or shrink in size) the Lottie file animation inside the LottieAnimation widget.

To change the Box Fit value:

1. Select the **LottieAnimation** widget from the widget tree or the canvas area.
2. Move to the property panel (on the right side of your screen) and scroll down to the **Lottie Animation** section.
3. Find the **Box Fit** dropdown, try changing the value among the **Fill**, **Contain**, **Cover**, **Fit Width**, **Fit Height**, **None**, and **Scale Down**.

#### Start/pause animation on button press

You probably want to start or pause the animation when something happens in your app. For example, after saving the form, while data is loading, searching, etc. You can do this by triggering the Lottie Animation action.

##### Adding Lottie Animation \[Action]

Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Container, Button, etc.) on which you want to add the action.
2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.
3. Click on the **+ Add Action**.
4. On the right side, search and select **Lottie Animation**.
5. **Choose Lottie Animation** from the dropdown.
6. Enable **Allow Play/Pause** if you want to start and pause the animation while the animation is running. **Note**: You can only access this setting if the **Auto Animate** property of the LottieAnimation widget is unchecked. **Note** that this option is only available if you have set the [animation type](https://docs.flutterflow.io/concepts/animations/lottie-animation#changing-animation-type) to either Loop or Boomerang.

---

### Page Transition Animations {#page-transition-animations}

*Learn how to add page transition animations in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/animations/page-transition

The animation that plays while transitioning from one page of the app to another is known as a page transition. In FlutterFlow, you can customize this animation to enhance the user experience.

You can choose from any of the following transition animations:

> **Info:** Here, the transitions are recorded with the duration set to 1000ms to make the animation clearly visible. But inside the app, it's recommended to keep the duration between 200-400ms.

| Transition Type | Description                                                | Example                                                                                         |
| --------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Instant         | Transition with no animation, switching pages immediately. | ![Instant](https://docs.flutterflow.io/assets/images/instant-page-transitions-d5095a438999fcd33a1b56cac8ade15f.gif)        |
| Fade In         | Gradually fades the new page into view.                    | ![Fade In](https://docs.flutterflow.io/assets/images/fade-page-transitions-5be1eead82c6344067a70a9f457eb6fb.gif)           |
| Slide Up        | Slides the new page up from the bottom.                    | ![Slide Up](https://docs.flutterflow.io/assets/images/slide-up-page-transition-786f1cc3a74cbcc6d84f262442985430.gif)       |
| Slide Down      | Slides the new page down from the top.                     | ![Slide Down](https://docs.flutterflow.io/assets/images/slide-down-page-transition-3d3e86f4d15106129d0484cb9c7f8214.gif)   |
| Slide Left      | Slides the new page in from the right.                     | ![Slide Left](https://docs.flutterflow.io/assets/images/slide-left-page-transition-94ae7fb43d636201d54b16a38d6638cf.gif)   |
| Slide Right     | Slides the new page in from the left.                      | ![Slide Right](https://docs.flutterflow.io/assets/images/slide-right-page-transition-aee5a5a584ef005c7c434cefd4a4cd21.gif) |
| Scale           | Scales the new page in from a smaller size to full screen. | ![Scale](https://docs.flutterflow.io/assets/images/scale-page-transitions-e146d5c73ecde74e57c87c2cf7ecabb7.gif)            |

#### Animate single navigate transition

To set a transition animation for a single navigate action, first, ensure that you have added a [**Navigate To**](https://docs.flutterflow.io/concepts/navigation/page-navigation#navigate-to-action) action and then select an animation from the **Transition Type** dropdown. By default, the animations use 300 milliseconds as the duration for which it plays but you can change it by specifying a value inside the **Duration** (ms) field.

![single-navigate-transition-animation.avif](https://docs.flutterflow.io/assets/images/single-navigate-transition-animation-5d5b9d9bda8bb8177893dc3f32794c03.avif)

#### Change global navigate transition

To change the default transition animation of your entire app, follow the steps below:

---

### Rive Animation {#rive-animation}

*Learn how to add Rive animation in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/animations/rive-animation

[Rive](https://rive.app/) is a real-time interactive design and animation tool. Using the **RiveAnimation** widget you can easily import your Rive assets to FlutterFlow and use them inside your app.

#### Designing Animation

You can create an animation from scratch by using [Rive Editor](https://editor.rive.app/).

1. Click **+ New File**.
2. Specify the **Artboard dimensions** (Width and Height).
3. Click **Create**.

Use the Rive [design tools](https://help.rive.app/editor/fundamentals/shapes-and-paths) or import image files to start designing your animation. Once your design is ready you can use the [Timeline](https://help.rive.app/editor/animate-mode/timeline) and use keying to easily animate your design.

> **Info:** You should have at least one [**Artboard**](https://help.rive.app/editor/fundamentals/artboards) inside your Rive file but you can add an infinite amount of Artboards.

After you have completed designing your animation, you can either download it as an asset (having `.riv` extension) or you can share it with others by publishing it to the Rive community.

To download the Rive file, click the **Export icon** (top-left corner of the Rive toolbar), and select **Download -> For newest runtime**.

To publish the file to the community, click the **Export icon** (top-left corner of the Rive toolbar), and select **Publish to Community**. Give a **title** and **description** to your animation and click **Publish to Community**.

> **Warning:** For using a Rive animation file inside FlutterFlow, you should either download or publish the file to the community.

Instead of creating an animation from scratch, you can also use any Rive asset shared in the [Community](https://rive.app/community/).

#### Adding RiveAnimation widget

Follow the steps below to use a Rive animation:

1. Drag and drop the **RiveAnimation** widget onto the canvas.
2. Select the **Animation Source** as either ***Network*** or ***Asset***.
3. If you have selected ***Network***, enter the **Path** (download URL) \*\*\*\*of the animation. Get the path by navigating to the Rive animation published in the community, right-click on the **Download** button and copy the link address.
4. If you have selected ***Asset***,
5. Choose an **Artboard** from the dropdown list.
6. Select the **Animations** that you want to use (these are imported from the Rive asset). After selecting one or more animation(s), you can use the **Preview Animations** button to play it.
7. The **Animation Type** is selected as ***Once*** by default. If the selected animations contain a loop or boomerang, you will have an option to select ***Continuous***. On choosing this option, if the animation contains a loop it will play continuously.
8. By default, the **Auto Animate** checkbox remains checked, which means that the animation will play as soon as the page loads. But if you want to use an Action to trigger the animation, uncheck this.
9. Specify the **Width** and **Height** of the RiveAnimation widget, and select a **Box Fit** type.
10. (Optional) If you plan to use an Action to trigger the animation, you can give an appropriate **Name** to this *RiveAnimation* widget for it to be easily identifiable.

#### Control animation using action

To trigger a RiveAnimation to start playing using an Action, you can use the **Rive** **Animation Action**.

##### Adding Rive Animation \[Action]

Follow the steps below to define an action to start the animation:

1. Select the **widget** (eg., `Button`) on which you want to define the action.
2. Select **Actions** from the Properties Panel.
3. Click **+ Add Action** button.
4. Choose a gesture from the dropdown among **On Tap, On Double Tap,** or **On Long Press**.
5. Select the **Action Type** as ***Animation**.*
6. Set **Choose Animation Type** to ***Rive Animation***.
7. Under **Choose Rive Animation**, select the `RiveAnimation` widget (If you have given your `RiveAnimation` widget a name, that will be displayed here).

> **Info:** You should have the **Auto Animate** unchecked inside the properties of `RiveAnimation` widget to take advantage of this action.

---

### Shaders {#shaders}

*Learn how to add visual effects using Shaders in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/animations/shaders

Shaders let you add rich visual effects to your app, such as animated gradients, ripple distortions, dissolve transitions, and interactive touch effects. Instead of using static images or simple color backgrounds, shaders generate visuals in real time using the device’s graphics processor (GPU). This makes it possible to create smooth animations and procedural textures that feel dynamic and alive.

#### Shader Widgets

FlutterFlow provides two shader widgets, each designed for a different purpose. Choose the one that best matches how you want to apply the visual effect in your UI.

##### ShaderFill

The **ShaderFill** widget creates a standalone shader effect that fills a rectangular area. It does not contain any child widgets and works as its own visual element in the UI. This makes it ideal for decorative effects such as animated gradients, procedural textures, or dynamic backgrounds. You can control its size directly using the width and height properties.

For example, you can use the **ShaderFill** widget to create a visually engaging animated gradient background for an onboarding or welcome screen.

##### ShaderWrapper

The **ShaderWrapper** widget applies a shader effect on top of an existing widget. Instead of rendering a standalone visual, it wraps a child widget and modifies how it appears on screen. This is useful when you want to add effects like ripples, burn transitions, or dissolve animations to elements such as images, containers, or other UI components.

> **Info:** The **ShaderWrapper** widget automatically takes the size of the child widget it contains.

For example, instead of abruptly removing a UI element, wrap it with a **Shader Wrapper** to apply a visual effect that gradually fades or distorts it, helping users understand that it’s being removed.

> **Note:** Internally, it uses the [**material\_palette**](https://github.com/FlutterFlow/material_palette) package, developed by the FlutterFlow team, to power the shader-based visual effects.

#### Shader Mode

Every shader widget includes a **Shader Mode** setting that lets you choose how the shader is defined and applied. You can either use ready-made effects or bring your own custom shader.

* **Preset:** Select from a library of built-in shader effects. Each preset includes adjustable parameters such as colors, speed, intensity, and more, allowing you to easily customize the look and behavior directly from the properties panel.
* **Custom:** Upload your own `.frag` (fragment shader) file to create fully custom effects. You can define and control inputs using uniform values, which are exposed as sliders in FlutterFlow. Custom shaders appear as a checkerboard placeholder in the builder, but render with full visuals in Test or Run mode.

#### Preset

Presets are ready-to-use shader effects that you can quickly apply and customize without writing any code.

> **Tip:** You can explore and try out all available [**presets here**](https://flutterflow.github.io/material_palette/).

##### ShaderFill Preset

The following presets are available on the ShaderFill Widget:

###### Gradient Presets

Gradient presets combine color transitions with procedural noise to create rich, animated visuals. Each gradient type is available in both **linear** and **radial** variants, and all share a common set of customizable property groups for fine-tuning the look and motion via the properties panel.

| Gradient Type           | Description                                             | Example                                                                                 |
| ----------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Gritty Gradient**     | A rough, grainy gradient with a textured, stippled feel | ![gritty-gradient](https://docs.flutterflow.io/assets/images/gritty-gradient-14c58eb938728597cc1b26d3723c8b02.png) |
| **Perlin Gradient**     | Smooth, natural-looking noise blended into a gradient   | ![sf1](https://docs.flutterflow.io/assets/images/sf1-9fb7639b827d7a94f77a25d0ccf220c9.gif)                         |
| **Simplex Gradient**    | Similar to Perlin, but sharper and more structured      | ![sf2](https://docs.flutterflow.io/assets/images/sf2-966a7fc4582c95e032b5070be468e9f3.gif)                         |
| **FBM Gradient**        | Layered noise that creates soft, cloud-like detail      | ![sf3](https://docs.flutterflow.io/assets/images/sf3-bef67b165968a47d13a52289e95a04f8.gif)                         |
| **Turbulence Gradient** | A more chaotic, high-energy version of FBM              | ![sf4](https://docs.flutterflow.io/assets/images/sf4-d441c1c9bcf9d12e5f9a80da37383eff.gif)                         |
| **Voronoi Gradient**    | Distinct cell-like patterns based on geometric regions  | ![sf5](https://docs.flutterflow.io/assets/images/sf5-043116bd83cf98c7a7391b138b92c429.gif)                         |
| **Voronoise Gradient**  | A hybrid of cell structures and smooth noise            | ![sf6-6](https://docs.flutterflow.io/assets/images/sf6-6-8f9a2f584995cc69b038e31f2a336e76.png)                     |

###### Marble Smear Preset

A procedural marble texture that reacts to user input. When **Interactive** is enabled, users can drag or touch the surface to smear and distort the marble pattern in real time, creating a fluid, organic visual effect. This is ideal for playful backgrounds, creative demos, or experiences where you want users to directly interact with the visuals.

![marble-smear](https://docs.flutterflow.io/assets/images/marble-smear-58e759fbd05ec8a25a0f62a145c1e2ed.png)

##### ShaderWrapper Preset

The following presets are available on the ShaderWrapper Widget:

###### Ripple / Clickable Ripple

Creates a wave-like distortion on the child widget, similar to water ripples. The standard ripple animates continuously, while the clickable version triggers ripples from the user’s tap location, adding responsive visual feedback to interactions.

![sw1](https://docs.flutterflow.io/assets/images/sw1-86591ece0c3e2d5d8c3c12574f4b6f88.gif)

###### Burn / Radial Burn / Tappable Burn

A dramatic dissolve effect that makes the widget appear to burn away. It can progress in a direction, radiate from a center point, or originate from user taps, with glowing edges that resemble fire.

![sw11](https://docs.flutterflow.io/assets/images/sw11-4e9f73a298631ce32f6add6b5ebcc6bf.gif)

###### Smoke / Radial Smoke / Tappable Smoke

A softer version of the burn effect, where the widget fades away like drifting smoke. It supports directional, radial, and tap-based variations for smooth and subtle transitions.

![sw3](https://docs.flutterflow.io/assets/images/sw3-a45497d51d0969943029318403127c32.gif)

###### Pixel Dissolve / Radial Pixel Dissolve / Tappable Pixel Dissolve

Breaks the widget into pixel blocks that scatter and disappear. This effect works for directional, radial, or tap-based dissolves, making it ideal for stylized removal or transition animations.

![sw4](https://docs.flutterflow.io/assets/images/sw4-04badc7eec01957b703015c3d13b5ff8.gif)

###### Tappable Slurp

A playful distortion effect that pulls the widget toward tap points, like a whirlpool. Each interaction creates a dynamic suction effect, adding a fun and interactive feel to the UI.

#### Implicit Animated

When [**Implicit Animated**](https://docs.flutterflow.io/concepts/animations/implicit) is enabled, changes to shader parameters (such as colors or slider values) animate smoothly instead of updating instantly. This is especially helpful when parameters are driven by app state, allowing for seamless transitions like gradually shifting gradient colors or intensities.

#### Time Animation Behavior

Time Animation Behavior controls how a shader animates over time. It defines whether the animation runs automatically, is controlled manually, or follows a custom timeline.

##### Continuous (default)

The shader animates automatically in a smooth, endless loop with no setup required. This is ideal for ambient effects like animated backgrounds, gradients, or subtle motion that should always be running.

> **Tip:** You can have the **Time Animation Behavior** set to **Continuous** while the widget is [**Implicit Animated**](https://docs.flutterflow.io/concepts/animations/shaders#implicit-animated). This allows the animation to run continuously while still enabling you to control specific parameters when needed.

##### Implicit

You control the shader’s animation manually using a **Time** slider \[0–10]. This is useful when you want to connect the animation to app state or user interaction, such as syncing it with scroll position, triggering it through actions, or freezing the effect at a specific point in time.

##### Explicit

Provides full control over the animation timeline. You can define how the animation plays by configuring properties like duration, delay, easing curve, looping, and direction. This mode is useful for choreographed animations that need to start, stop, or respond to events using a **Shader Animation** action.

#### Interactive Mode

Some shader presets support touch and tap interactions, allowing users to directly influence the visual effect. When **Interactive** is enabled, users can tap or drag on the shader to trigger dynamic responses such as ripples, burn marks, distortions, or smearing effects, making the UI feel more engaging and responsive.

![st](https://docs.flutterflow.io/assets/images/st-b09341f4cb0600c7d72c019af3908752.gif)

**The following presets are Interactive:**

* **Fill:** Marble Smear (drag to smear)
* **Wrap:** Clickable Ripple, Tappable Burn, Tappable Smoke, Tappable Pixel Dissolve, Tappable Slurp

##### Persist Taps

Available for tappable wrap presets. When enabled, the effects created by taps remain visible even after the user lifts their finger. When disabled, the effects gradually fade away, creating a more temporary interaction.

##### Tap Animation

For interactive wrap presets, you can control how each tap effect animates. This is separate from the main time animation and lets you define properties like curve, duration, delay, and playback behavior for each interaction, giving you finer control over how tap responses feel.

#### Cache

The **Cache** option improves performance by storing the shader’s rendered output. When enabled, the shader is rendered once and reused until its parameters change. This is enabled by default for ShaderFill.

> **Tip:** Disable caching if your shader needs to update continuously, such as in animations or real-time interactive effects that change every frame.

#### Custom Shaders

Custom Shaders allow you to create fully custom visual effects by uploading your own `.frag` (fragment shader) file. This gives you complete control over how pixels are rendered.

Here’s how to add a custom shader:

1. Create a Flutter-compatible `.frag` (fragment shader) file. You can generate it using ChatGPT or Claude by describing the effect you want. You can also start from an [existing shader](https://github.com/FlutterFlow/material_palette/blob/main/lib/shaders/perlin_gradient.frag) and modify it. Example Prompt:

   ```
   Create a Flutter-compatible GLSL .frag shader for a soft animated onboarding background using Flutter runtime effect format. {describe your effect here} Return complete shader code and a downloadable .frag file.
   ```

2. Upload the `.frag` file using the **Shader Asset** picker in FlutterFlow.

3. After uploading, use **Add Uniform** to define input values for your shader. Each uniform is a slider value from 0 to 10.

In the builder, custom shaders appear as a checkerboard placeholder. To view the actual rendered effect, run or test your app.

##### Adding Uniforms

Uniforms are simply input parameters that you pass to a custom shader. In FlutterFlow, they appear as sliders in the UI, similar to how you adjust settings (like speed, colors, or intensity) in preset shaders.

###### Order is everything

Uniforms are not matched by name. They are passed strictly in the order they are declared in the shader. This means the first uniform you declare receives the first value from the UI, the second uniform receives the next values, and so on.

Example:

```
uniform float speed;   // 1st
uniform vec4 color;    // 2nd
```

In the UI, you must provide values in this exact sequence:

* Uniform 1 → `speed`
* Uniform 2 → `color` (since `vec4` = 4 float values)

![uniform](https://docs.flutterflow.io/assets/images/uniform-3138516513b9e782b90be69f028a5c08.avif)

> **Warning:** If the order does not match, the shader will receive incorrect values, which can result in broken visuals or unexpected behavior.

###### Everything becomes floats

When you have the following uniform in shader file:

```
uniform vec4 color;
```

FlutterFlow treats it as:

```
float r
float g
float b
float a
```

###### Default uniforms

Even if you don’t write them, FlutterFlow **always passes these first**:

```
uniform vec2 uSize;
uniform float uTime;
```

So your shader MUST assume these exist at the top. Meaning your file should start like:

```
uniform vec2 uSize;
uniform float uTime;

uniform float speed;
uniform vec4 color;
```

#### Use Shadertoy Shaders

[Shadertoy](https://www.shadertoy.com/) hosts thousands of community-made GLSL fragment shaders such as animated backgrounds, glowing effects, liquid simulations, and more. Flutter supports custom fragment shaders through its `FragmentProgram` API, but Shadertoy shaders can't be dropped in directly: they use a different entry point, different uniform names, and several built-ins that Flutter doesn't recognize.

The [Shadertoy to Flutter skill](https://github.com/FlutterFlow/shadertoy_to_flutter_skill) helps convert Shadertoy GLSL into Flutter-compatible `.frag` shaders. It rewrites the shader structure, maps Shadertoy uniforms to Flutter uniforms, handles texture/audio channels where possible, and produces a `.frag` file that can be uploaded into your FlutterFlow project.

**Step 1: Download Skill**

The skill teaches AI Agents how to convert Shadertoy shaders accurately and safely for Flutter. The skill used for this workflow is: **`shadertoy-to-flutter`**. Download it from the [GitHub repo](https://github.com/FlutterFlow/shadertoy_to_flutter_skill).

The skill contains the following files:

* `SKILL.md`: Main instruction file containing the shader conversion workflow and rules.
* `references/flutter_glsl_constraints.md`: Flutter GLSL limitations, unsupported features, uniform rules, and texture handling.
* `references/uniform_mapping.md`: Maps Shadertoy uniforms to Flutter equivalents (e.g. `iTime → uTime`).
* `references/templates.md`: Example fill/wrap shader templates and sample conversions.
* `references/noise_library.md`: Noise/hash helper functions for replacing Shadertoy noise textures.
* `scripts/package-skill.sh`: Packages the skill into a distributable zip file.

**Step 2: Install Skill**

You can use this skill with AI agents such as Claude, Codex, or another AI assistant that can read `SKILL.md` and follow its instructions.

**Install in Claude**

1. Open the **Claude Desktop app**.
2. Go to **Customize**. Select **Skills** from the left sidebar.
3. Click the **+** button at the top of the Skills panel. Choose **Upload a skill**.
4. Upload the Shadertoy skill as a .zip file or skill folder.

The uploaded skill must include:`SKILL.md`. It can also include supporting folders such as: `references/` and `scripts/`

**Install in Codex**

1. Open the **Codex Desktop app**.
2. In the message box, type: `/sk`
3. Select **Skill Installer** from the skill suggestions list.
4. Ask Codex to install the Shadertoy skill directly from GitHub:

```
Install this skill https://github.com/FlutterFlow/shadertoy_to_flutter_skill
```

Codex will run the Skill Installer and install the skill into your local Codex folder. After installation finishes, restart Codex.

**Step 3: Using Skill**

You can use the skill with either a Shadertoy URL or a local .glsl file.

**Option A: Convert a Shadertoy URL**

In the prompt, provide the Shadertoy URL and ask to convert into `.frag` file, for example:

```
[invoke shadertoy-to-flutter skill] convert this Shadertoy shader into a Flutter .frag file:
[shadertoy-url]
```

![convert-via-url.avif](https://docs.flutterflow.io/assets/images/convert-via-url-5e57bb85748151d9d67f8664a100b608.avif)

**Option B: Convert a Local .glsl File**

Open the Shadertoy shader you want to use, copy the shader code, and save it as a `.glsl` file. Then attach the file and use a prompt such as:

```
[invoke shadertoy-to-flutter skill] convert this file into a Flutter .frag file
```

> **Tip:** You can also paste the shader code directly into the prompt, for example:

```
Use the /shadertoy-to-flutter skill and convert this shader to a Flutter .frag file:

[paste shader code]
```

**Step 4: Upload .frag File to FlutterFlow Project**

Upload the `.frag` file generated in the previous step to the **Shader Asset** picker in FlutterFlow and run your app. If required, also [add Uniform](https://docs.flutterflow.io/concepts/animations/shaders#adding-uniforms) to define input values for your shader.

##### Best Practices

* Keep the generated .frag file unchanged unless you know GLSL well.
* Always check the uniform order before wiring values in FlutterFlow or Dart.
* Prefer fill shaders when possible because they are easier to use.
* Use wrap shaders only when the shader needs an image, scene, or app UI texture.
* Avoid adding extra uniforms unless you really need user control.

---

### Widget Animations {#widget-animations}

*Learn how to add widget animations in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/animations/widget-animations

Widget animations allow you to add animation effects at the widget level. To add an animation to a widget, you'll need to go to the property panel for the widget and select the animations tab.

![animation-properties.png](https://docs.flutterflow.io/assets/images/animations_overview-2-90c80022663c27f43c9eb79279fd7980.png)

Animation Overview

#### Animation effects & properties

FlutterFlow supports a variety of animation effects and properties for widget animations.

Most animations have core properties you can edit, like the `Duration`, which specifies how long the animation should run for, and the `Delay`, which specifies what delay the animation should have before it starts to run.

In addition, there are animation-specific properties that usually have both a start and end value, which are mentioned in the table below.

| Effect       | Description                                                                                                                                                                                                                   | Example                                                                                | Effect-Specific properties                                                                                                                                                                                                                                                                                                                |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Fade**     | Makes the widget gradually appear or disappear. It's widely used for smooth introductions of elements on the screen and to focus user attention by fading in or out content or UI elements.                                   | ![Alt text for your GIF](https://docs.flutterflow.io/assets/images/fade-74dce8bfb19c813981a82249c782d390.gif)     | `Opacity`: the starting or ending visibility of the widget, where 0 is fully transparent and 1 is fully visible                                                                                                                                                                                                                           |
| **Slide**    | Changes the widget's position on the screen. Typically used to introduce widget in a dynamic, visually engaging way, like sliding in menus, pages, or notifications. FlutterFlow supports both vertical and horizontal slide. | ![Alt text for your GIF](https://docs.flutterflow.io/assets/images/slide-ce4b66cbd168766f4786839abc936f8a.gif)    | `Position`: where 0 specifies the widget's current position, -100 specifies 100px to the left (horizontal) or down (vertical), and 100 specifies 100px to the right (horizontal) or up (vertical).; ; *To make the widget come and go off the screen, make the start and/or final position greater than the width of the device.* |
| **Scale**    | Changes the size of the widget. Often used to draw attention to UI components, like magnifying buttons on hover or animating dialog boxes to appear from a central point.                                                     | ![Alt text for your GIF](https://docs.flutterflow.io/assets/images/scale-1fcac2418d1530633f792113f21f7095.gif)    | `Scale`: the starting or ending multiple to scale the widget horizontally (X) or vertically (Y), where 1 represents the current size of the widget.                                                                                                                                                                                       |
| **Rotate**   | Turns the widget clockwise or anticlockwise. It's often used for simple effects like spinning a loading icon.                                                                                                                 | ![Alt text for your GIF](https://docs.flutterflow.io/assets/images/rotate-f295f7fff35fc0ff396d44f4a3321e54.gif)   | `Turns`: specifies the number of 360 degree rotations.                                                                                                                                                                                                                                                                                    |
| **Shake**    | Creates the shake effect on a widget. Often used to draw attention to an element or indicate an error, like when a user enters incorrect information in a form field.                                                         | ![Alt text for your GIF](https://docs.flutterflow.io/assets/images/shake-ed533b417c3500650ab1a974cee66660.gif)    | `Frequency`: Number of shakes per second; ; `Offset`: Shake distance, a higher value intensifies and a negative value shakes the opposite direction; ; `Rotation Angle`: Angle of the shake                                                                                                                               |
| **Blur**     | Creates a focus or un-focus effect on a widget                                                                                                                                                                                | ![Alt text for your GIF](https://docs.flutterflow.io/assets/images/blur-95946cd8bab69eab32988f2de676776e.gif)     | `Radius (X or Y)`: Size of the blur.; ; *To create an unfocus effect, `Final Radius` should be greater than `Initial Radius`. To create a focus effect, `Initial Radius` should be greater than `Final Radius`*.                                                                                                                  |
| **Saturate** | Used to enhance visual appeal by making colors more vibrant for focused content or creating a muted effect for background elements.                                                                                           | ![Alt text for your GIF](https://docs.flutterflow.io/assets/images/saturate-cfa9a65e2af5bfcf6dbabcc7aebc3816.gif) | `Strength`: 0 indicates fully desaturated, 100 represents normal saturation and >100 represents the percent saturation                                                                                                                                                                                                                    |
| **Tilt**     | Creates a transforming effect (3D perspective) on your widget. Typically used to add a subtle interactive element to UI components, like buttons or cards, indicating user interaction or focus.                              | ![Alt text for your GIF](https://docs.flutterflow.io/assets/images/tilt-be815bd2b18bc241870c8a16babee6ee.gif)     | `Tilt`: The angle at which the widget is viewed.                                                                                                                                                                                                                                                                                          |
| **Flip**     | Flip animation rotates an element around its horizontal or vertical axis, creating a mirror effect. It's often used for flipping cards in a UI to reveal hidden information.                                                  | ![Alt text for your GIF](https://docs.flutterflow.io/assets/images/flip-6a4be57f468f0bd7ea93258399327160.gif)     | `Flip`: The angle at which the widget is viewed.                                                                                                                                                                                                                                                                                          |
| **Shimmer**  | Creates a "shiny" effect moving across the screen, often used to signify that data or content is in the process of loading or being fetched.; ; **Note** that this animation doesn't run on the Test mode.            | ![Alt text for your GIF](https://docs.flutterflow.io/assets/images/shimmer-87e3ba79e5e0600d87c12d14317add7b.gif)  | `Color`: The color of the "shiny" line or gradient that sweeps of the widget. A common practice is to use a slightly lighter shade than the content.; ; `Angle`: Determines the direction of the shimmer effect across the content. 0 degrees for horizontal and 90 for vertical.                                                 |
| **Tint**     | Adds a color overlay effect to your content.                                                                                                                                                                                  | ![Alt text for your GIF](https://docs.flutterflow.io/assets/images/tint-d01264b6437187cfa1332ee13230308d.gif)     | `Color`: Color of the overlay.; ; `Strength`: Intensity of the tint.                                                                                                                                                                                                                                                              |

#### Animation curves

When applying an animation, you'll also be able to specify the curve. An animation curve is essentially a mathematical formula used to interpolate values over time. Changing the animation curve allows you to control the speed and style of the animation.

![Alt text for your GIF](https://docs.flutterflow.io/assets/images/animation_curves-0b845c61e6c51d21c95c697e777436aa.gif); ; FlutterFlow supports a variety of animation curves:

| Curve           | Description                                                                                                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Ease In**     | Starts the animation slowly and then accelerates towards the end. It's useful for creating an effect where the motion begins gently and speeds up.                                               |
| **Ease In Out** | Starts the animation slowly, accelerates in the middle, and then decelerates towards the end. It's ideal for creating smooth, natural-looking animations that don't have abrupt starts or stops. |
| **Ease Out**    | Begins the animation quickly and then slows down towards the end. It gives the effect of a rapid start that gently comes to a stop.                                                              |
| **Bounce**      | Adds a bouncing effect at the end of the animation. The animated object overshoots its final position and then bounces back, mimicking the physical behavior of a bouncing ball.                 |
| **Elastic**     | Creates an elastic effect where the animation overshoots its target value and oscillates before settling. It's useful for animations that need a springy, elastic feel.                          |
| **Linear**      | Progresses at a constant speed throughout the animation. It provides a uniform transition from start to end, with no acceleration or deceleration.                                               |

#### Animation on Page Load

There are many cases when you might want to trigger an animation when a page or (in the case of a delayed load) widget is loaded onto the screen.

Consider an eCommerce use case, where a backend query is used to retrieve a list of trending products. There may be some delay between when the page is first loaded and when the actual results are displayed. To improve the user experience we can add some animations to let users know when content is loading.

![A widget that first shows a container with a shimmer effect, then fades in a widget displaying the product details](https://docs.flutterflow.io/assets/images/shimmerAnimationFinal-dc5ef2f80204dce1c5a7102ca23f1a69.gif)

To create an experience like this, you need to add a shimmer animation to a widget, and display that widget conditionally (i.e. when the query is loading). Here's how you do it:

#### Animation on Action Trigger

Beyond triggering widget animations on load, you can trigger an animation to occur as part of an action. For example, say you want a like button to be animated when a user clicks it.

Here's how you do it:

> **Note:** You can give a name to the widget that you want to animate using the action, this will make it easier to find in the action menu.

#### Applying multiple animations

You can apply multiple animations to a single widget. By default, when you add multiple animations, they are executed in a series (one after another) creating staggered animation. However, you can define to run all animations at the same time.

##### Run multiple animations simultaneously

If you want to run multiple animations together for the same amount of time (e.g., slide and scale widget at the same time), enable the **Apply same duration & delay** while adding animation.

##### Create staggered animation

A staggered animation is multiple animations executed subsequently. Adding staggered animations can help you create a stunning visual effect.

To create staggered animation, ensure you **disable** the **Apply same duration & delay** option and keep adding animations. The delay property will be auto adjusted based on the duration of all previously added animations.

> **Tip:** For manually controlling the staggered animation, set the delay for your new animation based on the total duration of all previously added animations. For instance, if the first two animations each last 1000ms (1 second), the delay for the third animation should be 2000ms (2 seconds). This ensures the third animation begins only after the completion of the first two, each lasting 1 second.

Here's an example of creating a staggered animation:

#### Setting animation values from variables

You can set animation values dynamically using the variables of your app. This flexibility allows you to create more sophisticated animations. Let's see an example of creating a beautiful animation where a list of items is sliding in from left to right. Here's how it looks:

![Setting animation values from variables](https://docs.flutterflow.io/assets/images/set-animations-from-variable-b784248823cbf3da590d2ca5a5bb8922.gif)

If you notice carefully, the items appear in a staggered fashion. This can be achieved by setting the delay value of each item based on its position (index) in the list. Here's how exactly you do it:

Select the item in the list and add the Slide animation.

In the Delay property, open the variable menu and add a [inline function](https://docs.flutterflow.io/resources/functions/utility#inline-function-code-expressions) to calculate the delay value based on the item's index. For this example, we use the formula `[index] * 100`, where `index` represents the position of the item, and `100` is the delay in milliseconds. This means the first item will slide in after 100 ms, the second after 200 ms, and so on, creating a staggered animation effect.

---

### App Events Integrations {#app-events-integrations}

*Feed local app events into GenUI so the conversation can react to live app state and time-sensitive signals.*

**Source:** https://docs.flutterflow.io/concepts/app-event-integration

App Event Integration lets GenUI listen to FlutterFlow **LOCAL** app events and turn them into conversation context.

This is how GenUI becomes aware of things the user did not explicitly type:

* Cart changes
* Workflow completion
* Alerts
* Navigation context
* Device or sensor updates

GenUI automatically listens for matching local events and converts them into hidden context messages for the conversation.

#### Two Integration Modes

* **Context Injection**: Use `auto_respond: false` when the event should enrich future replies without interrupting the user immediately. In this mode, the event message is added to a pending queue, which is then flushed before the next user message is sent, allowing the model to use these queued messages as hidden context during the next inference.

* **Proactive Response**: Use `auto_respond: true` when the event should trigger an immediate GenUI response. In this mode, the event message is sent directly into the conversation as an InternalMessage, inference starts right away, and the model may respond with text, UI, both, or nothing visible depending on the prompt and context.

#### Message Construction

You can either enter a custom message directly in the **Message Template** field or bind it to a variable for dynamic content.

If the event includes payload data, GenUI automatically appends it. For example, entering “Your order status is:” and triggering the event which includes event data such as `pending` or `in transit` will result in messages such as “Your order status is pending.”

#### Pending Context Queue

For `auto_respond: false`, GenUI stores pending event messages in memory until the user sends the next message. The queue has a maximum size of 50, and if it overflows, the oldest messages are dropped first. Before the next user request is sent, these messages are injected directly into the conversation history as InternalMessages, allowing the model to use them as context without triggering additional model calls.

#### Best Practices

###### Use context injection for ambient state

For example:

* Updated cart contents
* Current page context
* Background sync results

These make future replies smarter without causing unsolicited responses.

###### Use proactive response for time-sensitive events

For example:

* Threshold alerts
* Task completion
* Failed jobs
* Incoming high-priority updates

These are the moments where an immediate assistant response is justified.

###### Keep event data structured

If an event carries payload data, use a stable, well-designed data type. The generated message ends up calling `toMap()`, so clearer payload structure produces clearer AI context.

###### Do not flood the queue

If a background signal can fire rapidly, consider batching it before triggering the event. The queue has a hard cap of 50 messages.

#### Examples

###### Cart awareness without interruption

Use a `CartUpdated` local event with `auto_respond: false`.

Each cart update quietly enriches the pending context so the next time the user asks, "What's in my cart?" the model already has the latest state.

###### Immediate alerting

Use a `TemperatureAlert` local event with `auto_respond: true`.

When the event fires, GenUI immediately triggers inference and the model can warn the user and render a supporting UI component if the catalog contains one.

---

### App Events {#app-events}

*Learn how to use App Events in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/app-events

**App Events** allow different parts of your app to communicate without being directly connected. Instead of tightly coupling pages and components together, you can trigger an event in one place and handle it somewhere else. This helps keep your app more modular, easier to maintain, and simpler to scale as new features are added.

In many apps, making `Page A` react to something that happened on `Page B` often requires passing data through navigation parameters, updating app state, or building complex callback chains. As your app grows, this approach can quickly become difficult to manage.

App Events provide a cleaner pattern. Any part of your app can broadcast a named event (optionally with data), and any other part of the app can listen for that event and respond accordingly. The sender and receiver do not need to know about each other, which keeps your architecture loosely coupled.

For example, imagine a user adds a product to the cart from a product detail sheet. Instead of manually updating every place that shows cart information, the app can trigger a **CartUpdated** event. The cart badge, mini cart, or product list page can listen for this event and refresh itself automatically. The component that added the item doesn’t need to know which parts of the app will update. It simply announces that the cart has changed.

![app-event.avif](https://docs.flutterflow.io/assets/images/app-event-56ecf95098e14853bdedb5dbe084ef8a.avif)

#### Key Concepts

##### Events

An **Event** is a named signal that indicates something happened in your app. For example:

* `Internet Connection Changed` : The device’s network connectivity status changed (e.g., went offline or came back online)
* `Cart Updated` : An item was added to or removed from the cart

You can also pass relevant details along with an event. For example, a `Cart Updated` event might include information about the specific product that was added or removed. This data can be defined using a **FlutterFlow [DataType](https://docs.flutterflow.io/resources/data-representation/data-types)** to ensure the event carries structured and consistent information.

##### Event Handlers

Event handlers define **what should happen when an event occurs**. When an event is triggered, the handler runs an **Action Block** that performs the required logic.

##### Global vs. Local Events

App Events can be scoped as **Global** or **Local**, which determines **where the event is handled and who can respond to it**. Global events are handled at the app level, while Local events are handled by specific pages or components that choose to listen for them. Choosing the right scope helps keep your app architecture clean and prevents unnecessary coupling between parts of the UI.

|                             | Global                                                                                      | Local                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Where it's handled**      | At the app level                                                                            | On specific pages or components that explicitly subscribe to the event                         |
| **Number of handlers**      | Exactly one (the assigned Action Block)                                                     | Many — any page or component can add a handler                                                 |
| **Subscription management** | Automatic — always active                                                                   | Manual — handlers are added and cancelled using actions                                        |
| **Best for**                | App-wide concerns such as analytics, logging, authentication state, or global notifications | Page or component reactions such as refreshing lists, updating widgets, or syncing UI elements |
| **Processing**              | Sequential queue (events processed one at a time)                                           | Broadcast stream (all subscribers notified immediately)                                        |

##### Actions

You can **trigger and respond to App Events** using the following actions:

* **Trigger App Event:** Fires an event. This action can be used anywhere actions are supported, such as on button taps, page load triggers, or inside action flows.
* **Add Local App Event Handler:** Starts listening for a local event on the current page or component and runs the assigned **Action Block** when the event is triggered.
* **Cancel Local App Event Handler:** Stops listening for a local event on the current page or component when you no longer want it to respond to that event.

#### Using App Events

Follow the steps below to use App Events in your app:

##### 1. Create an App Event

1. Open the **App Events** page from the left sidebar.

2. Click the **+** button to create a new event.

3. Enter a name of the event.

4. Configure the event settings: * **Description** *(optional):* Add a short explanation of when and why this event fires. This description appears as a comment in the generated Dart code.
   * **Scope:** Choose **Global** or **Local** depending on where the event should be handled.
   * **Include Event Data:** Enable this if the event needs to pass additional information when it fires.
   * **Data Type:** If event data is enabled, select the **DataType** that defines the structure of the event payload.
   * **Nullable:** Specify whether the event data can be `null`.

5. **If the scope is Global**, assign a handler **Action Block**. This Action Block runs automatically whenever the event is triggered. If the event includes data, the Action Block must have a parameter matching the event's Data Type.

##### 2. Trigger the Event

1. Open the **Action Flow Editor** on the widget or page where the event should be triggered.

2. Add a new action as **Trigger App Event** (under the **App Events** group).

3. Configure the action: * **Event to Trigger:** Select the app event you created.
   * **App Event Data:** If the event includes data, provide the values to pass with the event.
   * **Wait for Completion (Global events only):** If enabled (default), the event queue waits until the handler Action Block completes before processing the next queued event. Disable it for fire-and-forget behavior. This option is not shown for local events.
   * **Debug ID** *(optional):* Add a label to help identify this trigger during debugging.

##### 3. Handle the Event

###### For Global Events

No additional setup is required. The Action Block you created in [Step 1](https://docs.flutterflow.io/concepts/app-events#1-create-an-app-event) is called automatically whenever the event fires, from anywhere in the app.

###### For Local Events

1. On the page or component that should respond to the event, open the **Action Flow Editor** (commonly under **On Page Load** or **On Component Load**).

2. Add a new action as **Add Local App Event Handler**.

3. Configure the handler as per the following: * **Local App Event to Handle:** Select the event you want this page or component to listen for.
   * **Handler Action Block:** Choose the Action Block that should run when the event is triggered. If the event includes data, the Action Block must have a parameter matching the event's Data Type.

*(Optional)* If you want to stop listening later (for example, after a certain condition is met or a toggle is switched off), add a **Cancel Local App Event Handler** action and select the same event.

> **Tip:** Local event subscriptions are automatically cleaned up when the page or component is disposed (removed from the widget tree). You only need to manually cancel if you want to stop listening *before* the page closes.

#### Examples

Let’s look at a couple of examples to understand how **App Events** can be useful in real-world scenarios.

##### Internet Connectivity Status (Global Event)

Internet connectivity affects the **entire app**, not just a single page. Instead of handling connectivity changes separately on every screen, you can trigger a **global event** whenever the device goes offline or reconnects and handle the response from one centralized place.

When the app detects that the device has gone **offline** or come **back online**, the global event handler can react accordingly. For example, it can:

* Show a **“No Internet Connection”** banner or snackbar when the device goes offline
* Hide the banner when the connection is restored
* Pause or resume background sync or network-dependent actions

You can also include additional event data to provide more context about the connectivity state, such as:

* `isConnected` → `true` / `false`
* `connectionType` → `wifi` / `mobile` / `none`

![global-event.avif](https://docs.flutterflow.io/assets/images/global-event-1e6a594f6137c21bc3bd5f0dad1b4c2f.avif)

Here’s the complete setup:

1. Create a **DataType** called `ConnectivityStatus` with the following fields: * `isConnected` (Boolean)
   * `connectionType` (String) → `wifi`, `mobile`, or `none`

2. Create a **Global App Event** called `Internet Connection Changed` with the following configurations: * Scope: **Global**
   * Include Event Data: **On**
   * Data Type: `ConnectivityStatus`

3. Create an **Action Block** called `handleConnectivityChange` that: * Checks the `isConnected` value
   * Shows a **“No Internet Connection”** banner when `false`
   * Optionally displays the current `connectionType` when connected
   * Hides the banner when the connection is restored

4. **Trigger the event** whenever connectivity changes: * In a connectivity listener or custom action → **Trigger App Event**
   * Pass `isConnected: true` with `connectionType: wifi` or `mobile` when connected
   * Pass `isConnected: false` with `connectionType: none` when offline

The app responds consistently to connectivity changes from anywhere. All network status handling is centralized in a single Action Block, making the behavior easy to maintain and extend.

##### Multi-Tab Dashboard Sync (Local Event)

In many apps, a dashboard contains **multiple tabs showing related data**. When information is edited in one tab, the other tabs should update to reflect the latest state. Instead of directly wiring the tabs together, you can trigger a **local event** so that each tab can react independently.

When a change happens, the tabs listening for the event can react in different ways, such as:

* Refreshing backend queries to fetch the latest data
* Updating summary widgets or charts
* Reloading lists or tables displayed in other tabs

Because this is a **local event**, only the pages or components that subscribe to it will respond.

![local-event.avif](https://docs.flutterflow.io/assets/images/local-event-28abb7116637070ff0dec8f563c9303e.avif)

Here’s the complete setup:

1. Create a **Local App Event** called `Dashboard Data Changed` with the following configurations: * Scope: **Local**
   * Include Event Data: **Off**

2. On each **dashboard tab component** (typically on **On Component Load**): * Add **Add Local App Event Handler**
   * Set the App Event to `DashboardDataChanged`

3. Create an **Action Block** called `refreshDashboardTab` that: * Re-runs the backend queries used by the dashboard
   * Refreshes the UI components that depend on that data

4. On any **edit or save action** inside a tab: * Add **Trigger App Event**
   * Set the App Event to `DashboardDataChanged`

Once triggered, all tabs that are listening for the event refresh automatically.

#### How Event Processing Works

Understanding the event lifecycle helps you design reliable event-driven flows. Internally, when an App Event is triggered, it follows a predictable flow inside the app. The event is first placed in a queue and then processed in order. Based on its **scope** (Global or Local), the event is routed to the appropriate handler, which performs the defined actions.

![flow.avif](https://docs.flutterflow.io/assets/images/flow-ceddbd8c582d88da179d98bdc5de2b71.avif)

Here are a few things to remember:

* **Global events** are queued and processed sequentially. If multiple global events are triggered quickly, they run one after another, not in parallel.
* **Local events** are broadcast to all active subscribers immediately when triggered.
* **Wait for Completion** (Global events only, enabled by default) makes the event queue wait until the handler Action Block completes before processing the next event. Disable it for fire-and-forget behavior.
* **Global events** always run their assigned handler, no matter where the event is triggered.
* **Local event** handlers exist only while their page or component is active. When the page is disposed, the subscription is automatically removed.

#### Best Practices

##### When to Use Global vs. Local

**Use Global events when:**

* The reaction should happen **anywhere in the app**, regardless of which page is currently open (e.g., showing snackbars, handling auth state changes, logging events).
* The logic should be handled in **one centralized place**.
* The behavior is **app-wide** and should always run when the event is triggered.

**Use Local events when:**

* Only **specific pages or components** need to respond to the event.
* Different parts of the UI may need to **react differently** to the same event.
* The handler needs access to **page-level state or widget data**.

In short, **Global events are for app-wide reactions**, while **Local events are for page-specific behavior**.

##### Naming Conventions

Use clear, past-tense names that describe **what already happened**, not what should happen. This keeps event flows easy to read and understand.

Examples:

* `User Logged In` (not `Login`)
* `Cart Updated` (not `Update Cart`)
* `Payment Completed` (not `Process Payment`)

This makes action flows read naturally, for example, “When `Cart Updated` is triggered, refresh the product list.”

> **Info:** FlutterFlow automatically generates a camelCase identifier from this name behind the scenes, which is used internally in code. Examples:

* `User Logged In` → `userLoggedIn`
* `Cart Updated` → `cartUpdated`
* `Payment Completed` → `paymentCompleted`

##### Keep Handlers Focused

Each event handler (Action Block) should perform **one clear responsibility**. This keeps event flows easier to understand and maintain.

If multiple reactions are needed:

* Use a **Local event** and add separate handlers on different pages or components, or
* Use a **single Global handler** that runs a small sequence of related actions.

##### Avoid Event Chains

Avoid triggering many events from inside other event handlers. While this is technically possible, long chains of events can quickly become difficult to follow and debug.

If you find yourself chaining events frequently, consider **passing additional data through a single event** instead.

##### Use Debug IDs During Development

The **Debug ID** field in the **Trigger App Event** action lets you label where an event was triggered. This is especially helpful when the same event can be fired from multiple places in the app, making it easier to trace and debug event flows.

#### FAQs

Why do I see “No local app events available to handle”?

This message appears when adding an **Add Local App Event Handler** action if either:

* No App Events have been created with **Local** scope.
* A handler has already been added for all available local events on the current page or component.

**Fix:** Create a new App Event with **Local** scope, or check whether the event you want to handle already has a handler on this page or component.

Why do I see “No local app event handlers available to cancel”?

This message appears when adding a **Cancel Local App Event Handler** action if there are no active local event handlers on the current page or component.

**Fix:** You must first add a handler using **Add Local App Event Handler** before you can cancel it.

Why is my Global event handler not firing?

Check the following:

* The event scope is set to **Global**.
* A valid **Handler Action Block** is assigned in the event configuration.
* The **Action Block parameters** match the event’s data type (if the event includes data).

Why is my Local event handler not firing?

Verify the following:

* The **Add Local App Event Handler** action is being executed (for example, placed inside **On Page Load** or **On Component Load**).
* The event scope is set to **Local**, since global events will not appear in the local handler dropdown.
* The page or component listening for the event is still **active and mounted** (has not been navigated away from).

Why are events firing in an unexpected order?

App Events are processed sequentially through an event queue. If **Wait for Completion** is enabled (`true`), each event finishes handling before the next one starts.

If the order seems unexpected, check whether some triggers have **Wait for Completion** set to `false`, which allows subsequent events to start before the previous event finishes.

**Also note** that global events are processed sequentially through a queue, while local events are broadcast immediately to all active subscribers and do not go through the queue.

---

### Component Catalog {#component-catalog}

*Configure the FlutterFlow components that GenUI is allowed to render inside the chat surface.*

**Source:** https://docs.flutterflow.io/concepts/component-catalog

The **Component Catalog** is the list of FlutterFlow components that GenUI can render inline in the conversation. Without a catalog, GenUI can still chat and call tools, but it has no specific UI to render.

Internally, GenUI creates documentation for each catalog component. That documentation includes:

* Component name
* Component description
* Parameter names
* Parameter types
* Required or optional status
* Parameter descriptions

The model's render decisions are only as good as the naming and descriptions you provide.

#### Component Requirements

###### The component must be serializable at the API boundary

Catalog components cannot expose **action parameters**. GenUI only knows how to pass structured data into the component, not callbacks or arbitrary closures.

###### Parameters should use supported types

Supported parameter categories in the generated catalog pipeline include:

* `String`
* `int`
* `double`
* `bool`
* `Color`
* `DateTime`
* `TimestampRange`
* `LatLng`
* `GooglePlace`
* `JSON`
* `DataStruct`
* `Enum`
* media-path string types such as `ImagePath`, `VideoPath`, `AudioPath`, and `MediaPath`
* `List<T>` of supported item types

###### Required complex parameters need explicit defaults

If a catalog parameter is non-nullable and uses one of these complex types:

* `Color`
* `DateTime`
* `TimestampRange`
* `LatLng`
* `GooglePlace`
* `DataStruct`
* `JSON`

then you should either:

* set an explicit default value, or
* make the parameter optional

For instance, if your **EventCard** component has a required `eventDate: DateTime` parameter, you must either set a default value in the component editor or make the parameter optional. Without this, GenUI validation will reject the component.

GenUI validation enforces this because those types do not have a safe implicit fallback in generated constructor code.

#### Runtime Rules

###### One root component per surface

Each GenUI surface renders exactly one catalog component as its root. That root component can be a rich component tree internally, but the model cannot compose arbitrary parent wrappers like `Column`, `Container`, or other widgets that are not in the catalog.

###### The model can only use listed catalog components

If a component is not in the catalog, it does not exist from the model's perspective.

#### Best Practices

###### Use list-friendly components

Because a surface has one root component, a component that accepts `List<T>` is often the right shape for result sets:

* `TransactionList`
* `SearchResultsGrid`
* `CartItemsSummary`

###### Prefer focused components over screen-sized composites

Good catalog components are reusable units, such as:

* `ProductCard`
* `OrderSummary`
* `InvoicePreview`
* `ReviewSummary`
* `AppointmentConfirmation`

These give the model flexible building blocks. A large page-like component is harder to reuse and usually harder for the model to choose well.

###### Use consistent `DataStruct` across tools and components

If a tool returns `ProductStruct`, prefer catalog components that also accept `ProductStruct` or `List<ProductStruct>`. That keeps tool output and rendering input aligned and makes the tool-to-UI handoff more reliable.

###### Describe parameters like you are documenting an API

Good:

* `estimatedDeliveryDate`: "Expected arrival date in ISO 8601 format."
* `inventoryStatus`: "Availability state shown to the user, such as inStock or backOrdered."

Weak:

* `date`
* `status`

###### Keep component names specific

Use clear, descriptive names that reflect the component’s purpose.

Good:

* `OrderStatusCard`
* `SensorAlertSummary`
* `QuoteBreakdown`

Weak:

* `Card1`
* `Summary`
* `Details`

###### Avoid ambiguous overlap

If two components do roughly the same thing, the model has to guess. Either merge them, rename them more clearly, or narrow their intended use.

---

### Custom Code {#custom-code}

*Learn how to write and integrate custom code in your FlutterFlow app to add custom functionalities.*

**Source:** https://docs.flutterflow.io/concepts/custom-code

While FlutterFlow provides a wide range of pre-built components and functionalities, there may be times when you need to extend your app with custom logic or UI components that are not available out of the box. This is where writing custom code comes into play.

There are a few different ways to make custom code accessible in FlutterFlow:

* **[Custom Functions](https://docs.flutterflow.io/concepts/custom-code/custom-functions):** Custom Dart functions that can be used to set Widget or Action properties.
* **[Custom Actions](https://docs.flutterflow.io/concepts/custom-code/custom-actions):** Custom Dart functions that can be triggered by [Action Triggers](https://docs.flutterflow.io/resources/functions/action-triggers/) or used as nodes in an [Action Flow](https://docs.flutterflow.io/resources/functions/action-flow-editor#action-flow-editor). These are usually `async` functions and are able to import [custom package dependencies](https://docs.flutterflow.io/concepts/custom-code#adding-a-pubspec-dependency).
* **[Code File](https://docs.flutterflow.io/concepts/custom-code/code-file):** You can define custom classes, enums, and logic to manage your app’s data and behavior.
* **[Custom Widgets](https://docs.flutterflow.io/concepts/custom-code/custom-widgets):** Custom Flutter widgets that can also import [custom package dependencies](https://docs.flutterflow.io/concepts/custom-code#adding-a-pubspec-dependency) and be used in the same way as [Components](https://docs.flutterflow.io/resources/ui/components) throughout your project.
* **[Configuration Files](https://docs.flutterflow.io/concepts/custom-code/configuration-files):** You'll have the ability to edit native files for Android and iOS.

Why Write Custom Code?

* **Extend Functionality:** Add features that are not included in the standard FlutterFlow components.
* **Custom Integrations:** Integrate with third-party packages or APIs / databases that require specific handling.
* **Unique UI Elements:** Create unique user interface elements that require custom rendering or interactions.

#### Writing Custom Code

Custom Code lets you add app-specific logic, custom widget, and native configuration directly in FlutterFlow. You can keep functions, actions, widgets, and code files organized with the pages and components they support, so each feature's files are easier to find and manage.

> **Warning:** Instructions and visuals on this page show the new Custom Code layout. You can switch from from the classic Custom Code editor by clicking **Try New Layout** in the toolbar.

Switching to the new Custom Code layout is one-way for that project. After you switch, you cannot go back to the classic Custom Code editor for the same project. To safely try the new custom code layout first, create another branch, switch to that branch, and then click Try New Layout there.

There are two main ways to write custom code in FlutterFlow:

1. Using the [**In-App Code Editor**](https://docs.flutterflow.io/concepts/custom-code#using-the-in-app-code-editor)
2. Using the [**Visual Studio Code Extension**](https://docs.flutterflow.io/concepts/custom-code/vscode-extension)

##### Using the In-App Code Editor

You can use the In-App Code Editor to view and edit custom code directly in the FlutterFlow application.

![custom-code-common.avif](https://docs.flutterflow.io/assets/images/custom-code-common-fef32c326e8da841ae095b7003319aab.avif)

> **Tip:** To leverage the capabilities that go beyond our in-app code editor, you can click on the **VS Code icon** to open and edit your custom code directly in VS Code using the FlutterFlow [**VSCode extension**](https://docs.flutterflow.io/concepts/custom-code/vscode-extension).

![open-in-vscode](https://docs.flutterflow.io/assets/images/open-in-vscode-f5f99800d92ec16d1755c3eec08f1213.avif)

Using the In-App Code Editor on Desktop

Note that the desktop version of the In-App Code Editor is limited. We recommend using the Web editor or the **[VSCode Extension](https://docs.flutterflow.io/concepts/custom-code/vscode-extension)**.

##### Code Copilot

Code Copilot is an AI-assisted feature that helps you generate code snippets, functions, or entire blocks of code based on natural language descriptions of what you want to achieve. It simplifies the app-building process by allowing you to describe the functionality you need, such as 'calculate the total price of items in a cart', and then the Copilot generates the necessary code.

This can significantly speed up the building process and reduce the need for in-depth programming knowledge, making it especially useful for custom functions and actions.

Limitation

Your prompt must be at least 3 words and no more than 500 characters.

##### Compile Code

When you are done adding your code snippets, you can compile it to ensure there are no compilation errors and that your code can be transformed into something that can execute when your app is running.

To do so, click the **Compile Code** button.

![compile-errors.avif](https://docs.flutterflow.io/assets/images/compile-errors-28f35f69f11e403e11de0bd869a506a1.avif)

How to recognize compile time errors

To run your app, you must make sure **Custom Functions** are compiled.

Custom Widgets and Actions don't need to be compiled to export code or test your app. However, you won't be able to preview Custom Widgets in the builder until they are compiled. You'll see a project warning if you don't compile Custom Widgets or Actions.

Compiling Custom Functions should be pretty fast, but sometimes, compiling Custom Actions and Widgets takes a while.

##### Code Analyzer

The code analyzer is available in all your custom code snippets and ensures the quality and correctness of your custom code. It automatically checks your Dart code for errors and warnings, providing real-time feedback as you write.

![code-analyzer](https://docs.flutterflow.io/assets/images/code-analyzer-83e3365c67e75c84432d4a930bc4badc.avif)

When there is a compilation error, the code analyzer will stop running and display the errors caught by the compiler. Once fixed, save the code and restart the code analyzer to resume real-time analysis and receive feedback on updated code.

##### Automatic FlutterFlow Imports

When creating a new custom code snippet (Actions, Widgets, or Functions) in FlutterFlow, some fundamental imports will be automatically added for you. These imports cannot be modified by the developer. Custom Functions do not allow adding any custom imports, but you can add custom imports in Custom Actions and Widgets after the line **"Do not remove or modify the code above"**.

![automatic-imports.png](https://docs.flutterflow.io/assets/images/automatic-imports-138890e7d87bf374a4899f48d1e474b3.png)

##### Custom Code Settings

When you edit a custom code snippet in FlutterFlow, the Settings menu opens on the right. This menu may vary slightly depending on the type of custom code (Actions, Functions, or Widgets), but here, we’ll cover the common settings.

###### Generate Boilerplate Code

This setting allows you to generate boilerplate code, providing a structured starting point with essential code imports and a basic widget or function structure.

![copy-boilerplate-code.png](https://docs.flutterflow.io/assets/images/copy-boilerplate-code-01438f1964317e413b1636db9fb04d54.png)

After creating a new resource file, click the code icon on the Widget Settings menu to generate the boilerplate code. Then, click "Copy to Editor" to add the boilerplate to your resource file’s code editor, where you can further customize it.

###### References

The References helps you understand where your custom code is being used throughout the project. When enabled, FlutterFlow scans your app and displays all locations where a custom function, custom action, or custom widget is referenced.

> **Warning:** Enabling References may increase the loading time of the Custom Code editor because FlutterFlow needs to scan the project and map all usage locations.

![references](https://docs.flutterflow.io/assets/images/references-f4efba18bcebc583fbb533c8fde1de65.avif)

###### Exclude From Compilation

If, for some reason, your action or widget fails to compile but you still want to compile the rest of your code, you can enable this toggle. Doing so will exclude the problematic code from the compile process.

Scope

This option is only available for Custom Widgets and Custom Actions.

![action-settings.avif](https://docs.flutterflow.io/assets/images/action-settings-50233cae6608254af92f074442cad4b6.avif)

###### Include BuildContext

This setting determines whether to pass the BuildContext of the widget calling this custom action as an argument. This is useful for actions that need to interact with the widget tree or access context-specific data.

Scope

This option is only available for Custom Actions.

#### Input Arguments

When writing custom code in FlutterFlow, you can define input arguments to make your custom functions, widgets, or actions more dynamic and reusable. Input arguments allow you to pass data into your custom code, enabling it to perform different tasks based on the input provided. By using input arguments, you can create more flexible and powerful custom code that can adapt to various scenarios within your application.

Here's an example of an action that takes 2 arguments: `cartItems` that is a `List of ItemsStruct` and `productId` that is a String. ![action-arguments.png](https://docs.flutterflow.io/assets/images/action-arguments-a52dd335f09d0cc5de625bda9e1fe960.png)

Generated Code for custom data types

When you define a custom data type in FlutterFlow, the generated code will refer to the type as `<YourTypeName>Struct`. For example, if your custom data type is called `Items`, it will be referenced in the generated code as `ItemsStruct`.

##### Callback Action As Parameter

A callback action is an action passed as a parameter to a custom action or widget and triggered at some point in the future when a specific event occurs.

This is especially helpful when you want to trigger actions from within the custom action or custom widget logic and include them as part of the custom behavior. For example, if an error occurs inside the custom logic, you could trigger an action immediately to inform the user about the error, and then continue execution or end with a default value to return.

What are callbacks?

In programming, callbacks are functions passed to other functions to be called when a specific event occurs.

In the following example, we have a Custom Action that takes an `onError(searchKeyword)` callback action with an Action Parameter `searchKeyword`. This means that the custom action will provide this search keyword back to the callback action when it calls it.

![explain-callback-action.png](https://docs.flutterflow.io/assets/images/explain-callback-action-bc00cb56afb51a047c1fc2e950c1efca.png)

##### Add an Action to Callback Action

To provide a callback action to your main custom action, check out this quick guide where we provide a "**Show Snackbar**" action to `onError`, displaying a combined text using the search keyword.

#### Return Values

In FlutterFlow, custom code can not only take input arguments but also return values, back to the caller. Return values allow your custom functions, or actions to pass data back to the main application, enabling further processing or UI updates based on the results of the custom code.

Scope

Return Values are only enabled for Custom functions & Custom Actions. Custom Widgets **cannot** return a value at the moment.

Here's an example of an Action that returns a *nullable* integer.

![return-value-actions.png](https://docs.flutterflow.io/assets/images/return-value-actions-1b07a6e637fbbbb36ce6989a6a0d8c6a.png)

#### Description

You can add a [**Description**](https://docs.flutterflow.io/flutterflow-ui/resource-hierarchy#resource-description) note on Custom Functions and Custom Actions to briefly explain their purpose, usage, or important details. This helps clarify what the function or action is intended for, making your project more understandable and maintainable—especially in libraries and collaborative environments.

![adding-description.avif](https://docs.flutterflow.io/assets/images/adding-description-086493054f5d563189ec6faf02660ecf.avif)

You can view these descriptions as tooltips by hovering over the green note icon when selecting a Custom Function or Custom Action.

![description-note](https://docs.flutterflow.io/assets/images/description-note-c67c9c314192f68a70ea3dcc4f613bf7.avif)

> **Tip:** In the generated code, descriptions are added as comments before the function definition, and they also appear in the custom code editor.

![description-in-custom-code](https://docs.flutterflow.io/assets/images/description-in-custom-code-794f28d8e82c1262ae92fbc04913dcfb.avif)

#### Organize Custom Code

Pages, components, and custom code can be grouped together in the same user folders. This makes it easier to organize a feature in one place instead of keeping its UI and custom code separate.

For example, if you have a **Cart** folder that contains cart pages and components, you can drag a related custom function, such as `calculateCartTotals`, into the same folder. This keeps the page, component, and custom logic for that feature together in the widget tree.

#### Adding a Pubspec Dependency

[Pub.dev](https://pub.dev) is the official package repository for Dart and Flutter. It hosts a wide range of packages, libraries, and tools that developers can use to extend the functionality of their Dart and Flutter applications.

Flutter Favorite Packages

Flutter Favorite packages are a curated set of packages on pub.dev that have been recognized by the Flutter team and the community for their quality, popularity, and usefulness in Flutter development. These packages are marked with a "Flutter Favorite" badge, indicating that they meet a high standard of quality, reliability, and best practices.

You can explore the Flutter Favorite packages on **[pub.dev's Flutter Favorites page](https://pub.dev/packages?q=is%3Aflutter-favorite)**.

To add a pubspec dependency from pub.dev, go to **Settings and Integrations > Project Dependencies**, then open the **Custom Dependencies** tab. Click **Add Pub Dependency**, enter the **package name** and **version**, and click **Add** to include it in your project.

##### Choosing the correct package from pub.dev

You will find varieties of dependencies for a specific requirement, and choosing the best one can be challenging. This section helps you identify the right dependency by examining its score.

When you search for any dependency in *pub.dev*, you will get a list of dependencies. You can filter out the result based on which dependency is more inclined toward your needs. You can do so by opening and checking each dependency manually.

Once you have a handful of dependencies, consider the following factors while choosing the final one.

* **WEB**: It must support Web to run your app in our Run/Test Mode.
* **Likes**: This shows how many developers have liked a dependency.
* **Pub Points**: Tells the quality of the dependency (out of 130) based on code style, platform support, and maintainability.
* **Popularity**: This metric indicates how many apps use the package. A high popularity score (out of 100%) can suggest that the package is stable and trusted by many developers.
* **Documentation:** A well-documented package will save you time and reduce ambiguity. Check if the package has clear usage examples, a comprehensive README, and ideally API documentation.
* **Maintenance & Updates**: Check the last update date. A regularly updated package is more likely compatible with the latest Dart/Flutter versions and has fewer bugs.

![Dependency-score.png](https://docs.flutterflow.io/assets/images/Dependency-score-605001293cfa6b24bf4ce7073feea1d8.png)

When adding a pubspec dependency to your custom code in FlutterFlow, you’ll need two pieces of [information](https://docs.flutterflow.io/concepts/custom-code#setup-code): the Package name with its Version number and the Import statement.

##### Using Unpublished or Private Packages

FlutterFlow supports the use of unpublished packages, which allows you to integrate packages that are not yet available on **pub.dev**. This capability is particularly useful when working with custom, forked, or private packages hosted on public or private repositories. By leveraging this, you can enhance your app’s functionality with customized or proprietary libraries tailored to your specific needs.

Possible Use Cases

* **Using a Different Branch of a Package**: When you need to test or use features that are only available on a specific branch of a package.
* **Forked Version for Customizing Features**: When you need to fork a package to customize its functionality or fix issues that the original maintainer hasn’t addressed.
* **Private Packages for Internal Use**: Companies or enterprises may have internal Flutter libraries that they want to use in their FlutterFlow app but cannot publish publicly due to confidentiality or proprietary restrictions.

###### Add Packages from Public Repositories

For packages hosted on public repositories (e.g., GitHub), you can add them to your FlutterFlow project by specifying the repository URL in the following format.

```
  package_name:
    git:
      url: https://github.com/username/repository_name.git
```

You can also fine-tune the dependency by using additional parameters like `ref` and `path` in the given format. Here are some examples:

* **To use a specific branch** (e.g., `development`):

```
  package_name:
    git:
      url: https://github.com/username/repository_name.git
      ref: development
```

* **To use from a specific commit**:

```
dependencies:
  package_name:
    git:
      url: https://github.com/username/repository_name.git
      ref: a1b2c3d4
```

* **To use package located in a subdirectory of the repository**:

```
  package_name:
    git:
      url: https://github.com/username/repository_name.git
      path: packages/subpackage_name
```

Here’s exactly how you do it:

###### Add Packages from Private Repositories

For packages hosted in private repositories, you’ll need to authenticate access. This can be done using HTTPS with a personal access token.

For GitHub, you can go to your GitHub account’s settings and [generate a token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) with the necessary permissions and use it in the following format. You can also create and use a [fine-grained access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) that only has certain permissions.

```
package_name:
    git:
      url: https://<username>:<personal-access-token>@github.com/username/private_repo.git
```

Replace `<username>` with your GitHub username and `<personal-access-token>` with the generated token.

##### Setup Code

To configure your custom code with the package, copy and paste the following items from the package's pub.dev page:

1. **Copy Package Name & Version**

To use the dependency in your Custom Action or Custom Widget resource file, go to the package's pub.dev page and click the **Copy to Clipboard** icon next to the package name and version. Then, paste it into the **Pubspec Dependency** section (bottom right) of the FlutterFlow code editor.

![package-dependency-version-copy](https://docs.flutterflow.io/assets/images/package-dependency-version-copy-6caeb2d534461e682a1a8f8cf02d1e59.avif)

See **[example](https://docs.flutterflow.io/concepts/custom-code#add-pubspec-dependency-to-custom-code-example-guide)** for more information.

> **Warning:** The current dependency might depend on other dependencies to work. So make sure you also copy the name and version of all the additional dependencies to specify in the code

You can check if the current dependency has any additional dependencies inside the '*Dependencies'* section at the bottom right side.

![img\_1.png](https://docs.flutterflow.io/assets/images/img_1-9cf7d6b8156405f7205db311cbefb87d.png)

2. **Copying Import Statement**

An import statement specifies the location of the dependency's code. When creating a custom widget or action, add this statement at the end of the default import statements in the code editor.

Open the dependency page and select the **Installing** tab; under the **Import It** section, you'll find the import statement. To copy, click the **Copy to Clipboard** icon.

![copy-import-statement.png](https://docs.flutterflow.io/assets/images/copy-import-statement-3813e68c653aa5d19ffdd8c9d79d998f.png)

3. **Copy Example Code**

Example code is always available in the **Example** tab on the package’s pub.dev page. Copy any relevant snippets that demonstrate usage, and paste them into your custom widget or function file. You can then modify the code as needed to fit your project.

#### Add Pubspec Dependency to Custom Code: Example Guide

In this example, we are using the [**flutter\_rating\_bar**](https://pub.dev/packages/flutter_rating_bar) dependency to create a `ProductRatingBar` custom widget for our Product pages. See how we utilize the example code from pub.dev and add the customized widget in FlutterFlow:

> **Note:** This example demonstrates how to add a [**pub.dev**](https://pub.dev) package to a Custom Widget snippet, but you can follow the same process for adding a package to Custom Actions. For a deep dive, explore the detailed documentation on **[Custom Widgets](https://docs.flutterflow.io/concepts/custom-code/custom-widgets)** and [**Custom Actions**](https://docs.flutterflow.io/concepts/custom-code/custom-actions).

#### Manage Dependencies

You can manage dependencies directly from **Settings and Integrations > Project Dependencies** > **Custom Dependencies** tab.

If version conflicts occur, warnings will appear in both the **Custom Dependencies** tab and the **Custom Code** editor. You can also bump package versions directly from the list, making it easier to resolve issues and keep dependencies consistent.

---

### Cloud Functions {#cloud-functions}

*Learn how to use Cloud Functions in your FlutterFlow app for serverless backend functionality.*

**Source:** https://docs.flutterflow.io/concepts/custom-code/cloud-functions

Cloud Functions let you run backend code in response to events and API requests without managing your own servers. They are commonly used for tasks such as processing data, calling external APIs, sending notifications, running AI workflows, or securely handling secrets and business logic.

FlutterFlow supports both Firebase Cloud Functions and Supabase Edge Functions, allowing you to build scalable backend workflows.

#### Firebase Cloud Functions

[**Firebase Cloud Functions**](https://firebase.google.com/docs/functions) allow you to run server-side Node.js code triggered by Firebase services and HTTPS requests. For example, you can automatically send emails, process uploads, generate AI content, or react to database changes.

FlutterFlow includes built-in support for creating, editing, deploying, and triggering Firebase Cloud Functions directly from the platform.

> **Note:** Read up on some interesting use cases of [**Cloud Functions**](https://firebase.google.com/docs/functions/use-cases).

##### Adding Cloud Functions

Let's see how to add a *Cloud Function* by building an example that generates logos based on user prompts. Here's how it looks:

The Cloud Function takes input from a TextField widget and initiates an API call to an [image generation API](https://platform.openai.com/docs/api-reference/images/create). Once the image URL is retrieved, it's displayed within an Image widget.

Here are the step-by-step instructions to build such an example:

Before you Begin

* Make sure the project is on Blaze plan on Firebase.
* Completed all steps in the [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase).

**1. Add page state variables**

For this example, you'll need to set up two [Page State variables](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#creating-a-page-state):

1. **generatingImage (*****Type: Boolean*****)**: This is used to control the visibility of a loading indicator during the logo creation process. Its value is set to *True* before initiating the API call and switched to *False* once the logo generation is complete.
2. **logoImage (*****Type: ImagePath*****)**: This is used to hold the generated logo image. After a successful API call, the retrieved image URL is stored here, allowing the logo to be displayed in the Image widget.

![img\_6.png](https://docs.flutterflow.io/assets/images/img_6-970302e076fc0dddef916c3973759c72.png)

**2. Build a page**

Let's add a page that allows users to enter the prompt. To speed up, you can add a page from the template or use [AI Page Gen](https://docs.flutterflow.io/resources/ui/pages#generate-with-designer). Here is the page added using AI Page Gen, and after some modification, it looks the below:

Also, see how to [build a page layout](https://docs.flutterflow.io/concepts/layouts) if you want to build a page from scratch.

![img\_7.png](https://docs.flutterflow.io/assets/images/img_7-a82a145481ef54c0e8723db21c1d3519.png)

Few things to note here:

* We use the [**ConditionalBuilder**](https://docs.flutterflow.io/concepts/layouts/conditional-builder) widget to show/hide the loading indicator based on the *generatingImage* variable. **Tip**: The Else branch of this widget is nothing but a ProgressBar inside the Container with a [rotating loop animation](https://docs.flutterflow.io/concepts/animations/widget-animations).
* The Image widget uses the *logoImage* variable to display the logo.

**3. Create and deploy Cloud Function**

To create and deploy a *Cloud Function* :

1. Click on the **Cloud Functions** from the [**Navigation Menu**](https://docs.flutterflow.io/flutterflow-ui/builder#navigation-menu) (left side of your screen).
2. Click **+ Add**. This will add the default `newCloudFunction`.
3. Set the **Cloud Function Name**.

###### Boilerplate Settings

On the right side, you can configure the following Boilerplate Settings:

1. **Memory Allocation**: You can specify the amount of memory your function should have when it's executed based on its complexity and needs. This setting is crucial as it influences the function's performance and the cost of running it. More memory can enhance performance for intensive tasks but also increase costs.

2. **Timeout (s)**: This refers to the maximum amount of time, in seconds, that a function is allowed to run before it is automatically terminated. If your function takes longer to execute, increasing the timeout setting may be necessary. However, be aware that longer timeouts can incur higher costs since billing is based on execution time.

3. **Require Authentication**: Turn on this setting if you want users to be authenticated to execute this cloud function.

4. **Cloud Function Region**: This determines the geographical location of the servers where your functions are hosted and executed. Ideally, you should keep this same as your *Default GCP resource location* and the Cloud Function Region specified in the Firebase Advanced Settings.

![cf-region.avif](https://docs.flutterflow.io/assets/images/cf-region-a94ec06c45dee0ff21e5bf4875dc28f0.avif)

###### Configuring Input & Output

Your cloud function might need some data to process and return the result. You can do so by configuring the input and output.

1. To receive output from a Cloud Function, enable the **Return Value** and choose an appropriate Type for the output, like 'String' for text. For this example, set it to *ImagePath* to get the URL of the generated logo.

2. To input data: Click **+ Add parameters**. **Name** the parameter, select its **Type**, choose single or multiple items (**Is List** option), and uncheck **Nullable** if the value can be null. For this example, add a parameter 'prompt' with *Type* set to *String*.

3. When using [Custom Data Types](https://docs.flutterflow.io/resources/data-representation/custom-data-types), Cloud Function expects JSON, matching each field in the Data Type to a key-value pair in the JSON. If the Data Type is a list, the function expects a list of JSONs. For example, for a custom data type named 'Person' with fields 'Name' and 'Age,' the function should return:

```
       //JSON:
       { "Name": "John", "Age": 30 }
   	
       //Example Cloud Function Code:
       return {
         "name": person.name,
         "age": person.age
       };
```

For a list, the function should return:

```
        //JSON
         [ { "Name": "John", "Age": 30 }, { "Name": "Jane", "Age": 25 } ]
		 
        //Example Cloud Function Code:
        return filteredpersons.map(filteredpersons => {
          return {
            "name": filteredpersons.name,
            "age": filteredpersons.age
          };
        });
```

###### To deploy

1. Click the `[</>]` icon to view the boilerplate code; a popup will open with the updated code, and then click **`</> Copy to Editor`**. **Tip**: To see if you are able to deploy the cloud function (before adding your own code), proceed directly with steps 8 and 9.

2. Inside the code editor, add the cloud function code. **Tip**: You can copy the boilerplate code to [ChatGPT](https://chat.openai.com/) and ask it to write the desired code based on that.

3. Click **Save Cloud Function**.

4. Click **Deploy**.

Here's the code used for this example:

```
const functions = require('firebase-functions');
const admin = require('firebase-admin');
const https = require('https');

exports.logoMaker = functions.region('us-central1')
    .runWith({
        timeoutSeconds: 10,
        memory: '512MB'
    }).https.onCall((data, context) => {
        return new Promise((resolve, reject) => {
            const prompt = data.prompt;
            if (!prompt) {
                reject(new functions.https.HttpsError('invalid-argument', 'No prompt provided'));
                return;
            }

            const postData = JSON.stringify({
                model: "dall-e-3",
                prompt: prompt,
                n: 1,
                size: "1024x1024"
            });

            const options = {
                hostname: 'api.openai.com',
                port: 443,
                path: '/v1/images/generations',
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer YOUR-APIKEY`,
                    'Content-Length': postData.length
                }
            };

            const req = https.request(options, (res) => {
                let responseBody = '';

                res.on('data', (chunk) => {
                    responseBody += chunk;
                });

                res.on('end', () => {
                    try {
                        const responseJSON = JSON.parse(responseBody);
                        if (responseJSON.data && responseJSON.data.length > 0) {
                            // Retrieve the URL of the first image
                            const firstImageUrl = responseJSON.data[0].url;
                            resolve(firstImageUrl);
                        } else {
                            reject(new functions.https.HttpsError('not-found', 'No images found'));
                        }
                    } catch (error) {
                        reject(new functions.https.HttpsError('internal', 'Error processing response', error));
                    }
                });
            });

            req.on('error', (error) => {
                reject(new functions.https.HttpsError('internal', 'Error generating image', error));
            });

            req.write(postData);
            req.end();
        });
    });
```

Important

Always regenerate and use the updated boilerplate code or adjust your own code accordingly whenever there are changes in the code, boilerplate settings, or input/output parameters.

Optional: Add package

Your cloud function may require third-party packages to work. You can include any npm package (dependency) by listing it in the `package.json` file. This file not only manages the npm package dependencies for your functions but also holds project metadata, sets up scripts for tasks such as deployment and outlines the compatible Node.js versions.

To add a dependency, open the `package.json` file and specify your package in the `dependencies` section.

![img\_9.png](https://docs.flutterflow.io/assets/images/img_9-90023c8e1828a702463ab4b7a5aceced.png)

**4. Trigger Cloud Function**

The newly created *Cloud Function* will be available as an action when you are adding one. For this example, on click of a button, we'll first set the *generatingImage*to *True* and then trigger the **Cloud Function Action**.; **5. Optional: Use Cloud Function result**

To use the *Could Function* result, ensure you provide the *Action Output Variable Name* while adding the action, and then you can access it via the **Set from Variable menu > Action Outputs > \[Action Output Variable Name]**.

For this example, we'll use the result (i.e., generated logo image URL) and set it to *logoImage* variable. Here's how you do it:

##### Testing Cloud Functions

The Google Cloud console has built-in functionality to allow you to trigger a Cloud Function for testing. This means that after deploying Cloud Functions, you can test them without writing to Firestore (either from FlutterFlow or otherwise).

Here's how to test FlutterFlow's `sendUserPushNotificationsTrigger` function in the Google Cloud console:

1. Open your browser and navigate to the following URL: `https://console.cloud.google.com/functions/details/us-central1/sendUserPushNotificationsTrigger?env=gen1&project=<projectID>&tab=testing`; In here: * Replace `<projectID>` with your GCP or Firebase project.
   * If you want to test a different Cloud Function, update `sendUserPushNotificationsTrigger` with the relevant cloud function name.

2. Paste the following JSON into the `Configure Triggering Event` text area. * If you want to test a different Cloud Function, update `sendUserPushNotificationsTrigger` with the relevant cloud function name.

   ```
   {
       "value": {
           "name": "projects/<projectID>/databases/(default)/documents/sendUserPushNotificationsTrigger/<documentID>",
           "fields": {
               "scheduled_time": { "stringValue": "" },
               "initial_page_name": { "stringValue": "" },
               "notification_title": { "stringValue": "Your friends are missing you!" },
               "notification_text": { "stringValue": "Please come back to Nanochat" },
               "user_refs": { "stringValue": "users/VXu6EvFMl5M8KMXriYRvFEWTFHA2" }
           }
       }
   }
   ```

3. In the `name` property: * Replace `<projectID>` with your GCP or Firebase project.
   * Replace `<documentID>` with the ID of the document. This document must already exist in Firestore.
   * If you're testing another function than `sendUserPushNotificationsTrigger`, update `ff_user_push_notifications` with the collection where the document is written.

4. Update the values under the `fields` property for the message you want to send.; The `fields` in the example above are for FlutterFlow's built-in `sendUserPushNotificationsTrigger` function. If you're testing a different Cloud Function, you will need to update the `fields` for the code in *that* function.

5. Click the `TEST THE FUNCTION` button.

The Cloud Function will now run and gather the relevant entries from Google Cloud Logging.

##### FAQs

Why do cloud function deployments fail on newly created projects?

This issue occurs because the newly created Google Cloud Platform (GCP) project hasn't been fully configured with the necessary APIs and permissions. Follow the steps below to enable the required APIs and set proper permissions.

1. Open your browser and navigate to the following URL: `https://console.cloud.google.com/functions/list?referrer=search&hl=en&project=<projectID>` Replace `<projectID>` with your GCP or Firebase project ID.
2. Click on the **Create Function** button. GCP will prompt you to enable the necessary APIs: **Cloud Build** and **Cloud Functions**.
3. After clicking **Next**, you will be prompted to enable the **Cloud Run Admin API**. ![cloud-run-admin-api](https://docs.flutterflow.io/assets/images/cloud-run-admin-api-6289d1d79337a0f909d0e29e555335f6.png)
4. Now, you need to grant the default compute service account the appropriate permissions. In the next page, you will see the option to deploy an example cloud function like `helloHttp`. Deploy this function. You will be prompted to grant permissions to the default compute service account. The message will look like: `You need to grant the following roles to the build service account to deploy a function: roles/cloudbuild.builds.builder to <projectID>-compute@developer.gserviceaccount.com.`
5. Click **Grant** to provide the required permissions and deploy the example cloud function. Once deployed, you can delete this function if you wish.

With the required permissions granted, you should now be able to deploy cloud functions from FlutterFlow without any further issues.

I am getting Cloud Function Deployment Errors

![img\_10.png](https://docs.flutterflow.io/assets/images/img_10-56cfc3937708ca6bbbd99dad965068d1.png)

If you encounter deployment errors, it may be helpful to check out [this community post](https://community.flutterflow.io/discussions/post/how-to-fix-cloud-function-deployment-errors-all-solutions-discussion-wgfMLgpLrBlmnUI) for possible solutions and insights.

Why am I getting a CORS error when executing my Cloud Function?

The CORS error occurs because the **Access-Control-Allow-Origin** header is missing from the response, preventing your request from being completed. This issue can arise with new Cloud Functions, whether deployed through FlutterFlow or not.

Follow the steps below to fix the issue:

1. Open your Google Cloud Project's [**Cloud Functions List**](https://console.cloud.google.com/functions/list)
2. Select the function causing the issue.
3. Navigate to the **Permissions** tab.
4. Open the **VIEW BY ROLES** tab.
5. Ensure there's a row with `Cloud Functions Invoker` with principal set to `allUsers`. If it’s missing, click on the **Grant Access**, add `allUsers` with the `Cloud Functions Invoker` role.

![add-cf-invoker-role](https://docs.flutterflow.io/assets/images/add-cf-invoker-role-f06288f87aa8e929db35770df5aa1eb9.avif)

#### Supabase Edge Functions

[**Supabase Edge Functions**](https://supabase.com/docs/guides/functions) let you run secure backend logic using Deno and TypeScript directly on Supabase infrastructure. They are ideal for AI integrations, secure API wrappers, webhooks, payments, and server-side processing.

Unlike Firebase Cloud Functions, Supabase Edge Functions are tightly integrated with your Supabase project and run closer to users for lower latency.

Prerequisite

Before using Supabase Edge Functions, make sure your FlutterFlow project is connected to Supabase. See the [**Supabase Setup**](https://docs.flutterflow.io/integrations/supabase/setup#connect-with-supabase-oauth) guide.

##### Adding Edge Functions

Let's see how to add an Edge Function by building an example that generates an AI summary of product reviews.

The Edge Function takes a list of reviews as input, sends them to an AI model, and returns a JSON response containing a summary and overall sentiment. This example demonstrates a key benefit of Edge Functions: securely storing API key on the Supabase backend instead of exposing it inside the app.

Here's how it looks:

**1. Create and Deploy Edge Functions**

1. Open the **Cloud Functions** section from the Navigation Menu.

2. Click the **+** button and select **Supabase Edge Function**.

3. Give the Edge Function a name. In this example, we use `getAIReviewsSummary`.

4. Configure the function settings. In this example, the function accepts a list of reviews as input and returns a JSON response containing the AI-generated summary and sentiment.

   You can also configure additional settings:

   * **Verify JWT**: Verifies the JWT token from the request header. Disable this if you want to allow unauthenticated access.
   * **Enable CORS**: Automatically adds CORS headers and preflight request handling. Required when calling the Edge Function from web apps.
   * **Return Value**: Defines the response type returned by the function.
   * **Define Parameters**: Configure the request body parameters accepted by the function.

5. Click the code-generation button to generate and copy the boilerplate code into the editor. Copy the boilerplate code and use any AI assistant to generate the implementation for your specific use case. For example, you can ask the AI assistant to complete the function for generating AI-powered review summaries using the Anthropic API. Review the generated implementation and verify it matches your expected logic and response format.

6. Paste the generated code back into the Edge Function editor.

7. Click **Save Edge Function**.

8. Once saved, click **Deploy**.

9. FlutterFlow will show a deployment dialog listing the available Supabase Edge Functions for deployment.

10. Click **Deploy** for the selected Edge Function to deploy it to your connected Supabase project.

Optional - Add Package

You can also add external Deno, npm, or JSR packages using the `Dependencies (deno.json)` tab if your Edge Function requires additional libraries or SDKs.

For example, to add the `lodash` npm package:

```
{
  "imports": {
    "lodash": "npm:lodash@4.17.21"
  }
}
```

You can then use it inside your Edge Function:

```
import _ from "lodash"
```

![add-packge-edge-function](data:image/avif;base64,AAAAIGZ0eXBhdmlmAAAAAGF2aWZtaWYxbWlhZk1BMUIAAADybWV0YQAAAAAAAAAoaGRscgAAAAAAAAAAcGljdAAAAAAAAAAAAAAAAGxpYmF2aWYAAAAADnBpdG0AAAAAAAEAAAAeaWxvYwAAAABEAAABAAEAAAABAAABGgAAFl0AAAAoaWluZgAAAAAAAQAAABppbmZlAgAAAAABAABhdjAxQ29sb3IAAAAAamlwcnAAAABLaXBjbwAAABRpc3BlAAAAAAAAAiYAAADMAAAAEHBpeGkAAAAAAwgICAAAAAxhdjFDgQAMAAAAABNjb2xybmNseAACAAIABoAAAAAXaXBtYQAAAAAAAAABAAEEAQKDBAAAFmVtZGF0EgAKChgl4ly2CBAQNCAyzCxMBALcg8lrGb6vlm3okOXopdaMxkgQ22X5aA5gKYlfBsxqAFi2NXeY2fbdv76lodLjDLMIvH+JA2b5/I3MUKETHaw1mxeCClwZE/ksGln3ANO+hItKnjs/HO9M8yUp5Cl+KJARL0hzczhtLk0V1pxjwGjhUiGgZIPh9cy7Q3cap7F2LI9Vj1jJK+/GWoOJj5mun881MHzl29fqA7DS6ckRZdOviIaWTa5b8rpnUjRe5kNn2wHs2IhoqgdSLZRPRqlbNlXbl8n3M4OSD6UHMEh5ZdWQuQOjGjBLktsQ/r6YJwFrpLC45gCpE8F6ErnHULs+siS3DZ+6MJxlnNGkj+ZGdjEDu5o+lK00Z3yS/Fa3TYHAPf3oDDnQjcprUdDF2qmwxa+b30KCvveSFdbRSosn2KuQiBlyWRXx0mStXAS4mWVltSAWD1BfHUsmvGigWoMnd/kIaKBMjz8u0QCusZx8jxxBk4meF0LUSbrehCQ1RnLOOqh+FaaETzV7yTzDzYX6esODppQ87kqPBGR91E+aB1ttyDBrvTaKEw56Z16ahq7DdvZpPsCUPP56njRTkDVz5IfM9l4IT2RGdJrY2Af8iX1JO8OGECP/981gTYPwHBxAqFHMzPxVOlWXmcWVEtj9ks7ONtgCf6JkWSeF2HmrZBX8qICxsldp+Wu56ZYFpmzgWR9w8xtCmlvnu5R0GjyShmrXwM6NCM2HmrwuQ7UgJhwHKQmyBKiBpPqPf1csJz+bumlQqj1NCVQxhxJuryM/eef7YkkHS+/FeRBj9NudHPthon+vFF4fd1W6KcN2EtsRuoAtRxNcuUIqgP64nIt3HLhQ2o4aLCM03U44k0cAzIvkh1Aj9HW6eAlyLkcMGUKNWFgKyyFWbY93iOjYmhWJxPR16FfpZ5mGDXhCiXCrKmlmY9dHJFuWd6hi8odxVJTj7LXRoQkEvYAE/+D237wkIlntTjQ1PTpioELt0WjKWh+ZZ17jKD2rksoZ5D204FNPyP+pxa29i8NIS71saJe+a8ZN7cL8MPTx4ps+dVtA8X7jCn6VnkxNVB1Ond/9jPHwzskg5W6RoEUy3FGgmbKVZ/7CLgTCbh9eW4Bx83bBHxFtRdodbCVF2WGCzGLVmCpys0p6uXdgZDiXCTc+/Dp71iOZaIyHWhXUv4WQ+bk7jTIShuDVP2NuQiwXxXOMjY+MflMEWqFEgEc1hwbL3IFUqveDk83Andw58i1v+lxsI3jct7QDChTPdKanB5Ki9paV5DBN6/ENkyWgF234BG1f5COAz7LoQHtKr47CDPgo+5gYyZVrmEVNueXF0PaXH49qTW5V8w0kPhRD0LK8FIqbTJ+I/2oi67P+NibmodWVX+/kITBSn+hGD+2qXxsWtVzHlrqsClDRi+ycSsdAjF5MRvl9xweW6e0aPRoQDxr4L4bbRhpeEu7P2Bl5cSqwkqiZgG3RJPsaaC1Ys3QfOGBTruVaxEiOlCzgNfEuRffBE7jbPVLtMa01zIoN0T5mEbotWJXg7KZ379/B+3wrlrr1gT4Cqw5LfM1TuWZKrRtiNs7iekrlzyv4e9rmKjL8XKGayi8bDU5orTt9NTJ56LHL2Btw7kwitaBLR21hcpp6c8W3BmuDe79udgMUHfjAIScO0ngn998ZTMl/xe/pm2bKuj/36WXfWyoq6aGHwHcKSakDKhhEiCGnTjVzjEYJjV4fXG0HsHeuzsdLj9Jfhz//MSNOfTPwPgyZTeQ7QhYj9DyEsUmnAczTfhykBfkYLwueENalgjwWNK1huaRoFJimZYQFEi3ANoDVV3P8zU3ZwI+l+ixbNABdckKd5ZUBC6XbG67HxHKIj+8UU4CM5O5loxAgJgA3KuC4tz+atHTlpce1uB3kILjmvg9Hue3SJMaelovvyM1wj9BIFy/eKmGZCBztkw0T0InuPt+CDvRvMdc+sHiAERQ4aqMervdW5D/Dpfc3hX+eKrxqpqeribpNbDWnvqlAQ7yqaxdsCvI88IPQ7sMWpWD49rCUTbE+43Wd+9JcchLxTVJgq/WhLusmz/xqBxU3y48d3fggjipS/QDsnqMBZbxcO+QFz0LWww60uMimH1gCaaZ/rXQ8v/RwGOSo/tMIE2/dMBjfA8eYVI1rAQ2kiLt8lmHh+aQTuK4/k3CY7uVAzTI1rZKl8zx+qOWmALSPdvcXQJ7UBMUatm/wjlpbW09gY2cET5EpgfmLhn6sU02ck4UrpoPh1TGgMBOhJm61FYfjSv0zrAK46Dznd2q8cLadlKDrYOjhjA1rJs0WWW5tWA42tGoYOB8tXGY/sH0GaBJKQf/yaQRdgwQSDTFekSNp14eEvUAUEwalC44aiMP3CAOpEfWzr+Z6UywBVgK6r5YMnJVnSFNOAq97t7rtP+DUo4fIApxuHI98rGrfKnxA37G1iEZtGzVM2oWnSa88PQWwFmSwhXBoYrSU4HypXegXoYNmsfm6xtkoG1iNQvPaUgNYwf45CmXYFPNNwLNtHFKCITmOHvit0CanFRi2+yUZTSP5okhd5aXjPCh489OpIMFORxkFSpdl7jcJKhTZoyZP5PED+HdOKo0AUma+kpcC/QX8cU2mnl37xC4sKP1QG+Ecp/k3i3dvRrU5kCIHwTMqaRJ11s1TD3v+TsRKOAJ8UU9CG+ZUtKYaHcG6zs8ViVfpVsBLyuyFlmMcxy9Vlrkuo+NBDTlPkoPGBEOsUbmtzBzZWS4B37Ai3xWR/ULH+AENIt6GCcrCWjhac/osXRvhELfqIKNL78PDHufWshtoM8ggle8sQ17Ng9ZJXWv6D64i2Vf0zb3lq2nihWjbC6R/oWin7ieI57VS9PVoimkZ8ZA5uFHThIDlT7oxkVnsXhkJhSKzYHUR0PcdocKekscyY5Vpv553djOl+7l39Zzhn6rF8crOjcz49HwFbMUYAA2PAGRMW8Ar3uFl4ZF6X8hy/LZm5DXqlpMIs8nstxdyJgDswz8Szgt2PcT6NH0wtSCb+1q0qTqRxeo0gtqnG2J7hJU/g9mCBwv1Pn8y9mKNTB9olJ5wd2JGc6/WIN5GdpHwIuO3Ip7ZzTpnYCrJzQzQkuiipMoLSFQLbH+7xPRcymdBr8gfEFy8k4rPBS7NpBlPqXxhpKs9ilqK5eEw7W/3c9LZxaKwAq5o98QaGihVQ/718MaiCMQn3JVZWNf/asSO+9CVuDoU6og9jbR+KJdGpCiMom3mQB5xpBP4i7xqpjrMsMJguw4Vr6Q70Te8tS/+a5ka/KzECgcZHKFqbaUhfuS5gXgxYWDUBWJc19VVoGJc9Za/2+LzQE7cUv3QOyknb5KKDBgJjKZCA2UY+ZCbiyw1CAhtliOvVC+Vpxj2y84kcO668f8sHEcMD7wxE/j7Oy0YpK1p62neiIoof7S26cRG9uT8eVNpxSTfAlEVmG2n8zwXcZSn/ryzZjwUrSf5cWHmILw+PhEkLtjDB8OGhOAn6zYzH7X5vKTHdBokxSA0ePcucVlstW5/y1fzN7UN4vsL30OIx6iVLnEk9DgoCUkje2CIMxq1QsSvRtk6DssG1XaKXav7f7y2RhHhweLAQMbbvCaUH6rF/2tt9N+zc6NKib7MNrFewDOFOz8jz14C3GZjoCPaNd+XOhldapUBiD3452bgd+qQlKvMTNEVwkUngEjhjhCCT7I43TAgV8Xn5J/ssurppQ5bK9wtYtSYouyIhUsOqPqKL5Rz6bAvTzWWyWuCNvQdKJR8bfGfKYAfdX3Fu2MKdk/1GZvOVCGqtW2P5c31fb2zWYxZkwT/WynV4Fl4goY9x1FpRCXmPtJXFWmOrxXXyxru4feIocVjLZ2BuvJylAp+k0oAD80b+QNmMb5ozNxnM3VWbaZ1xz71ToeZDAwQ4dY7lfZ2wTPhVvzHG2RYYda4lXma+Leo/Pz4uflQo7UPHe2tf253PSuCBKo7StFnU2UgHNAS8yGqG/XE2NPCWL3tEtZAPxN+MXbCzQEEiGoLH0gPCs2fqO34tPIfFou15HiFJKur8M88tunvP0c0uzbDQZbnHp+2OeaiE1sMKZbvYg/SNj8h+VQZ7ikaNfgHT0i6HwMoIgLI9UrQ379kK2EVFujMDJmypLH762vBTBW18wl5JQWW2T0bMo0/n/45RRS4ADMSZoZh+JE3oZRJGdh7cuE2NJbHrP5pjYzG2HAuZjvn0I4gCP/9oT2+JievnPgVbQmVCT2bU1EJdmOmiUHOx4uv/aUHwi52GmoPe3G2+HGCM1mIygapR7c+LWrZ5glkL3cyr9iAD0x8lUjLyhHPmWqzi873q15kiq4UQSxXB9Rz78Qrc4kRk9AJHfm5Sp271aoVek9saRtZtqEcX19h+Sd8ly+1NEp2K3uZiVQGGi0uEa6HCgu8Axufb/z3M0yY/yZG3aO1ut3kFAQH3pik/kdBJE1vw83vAO/SEeNCI+1LbK/i6JXDKk8WSbAEczV+AkCRS1anlIIHV73v5zeAgKNVjDf5xa+lX0k9KpnRJqytVoCKT1Bdgil46tbr9gNym/XAxJ54kGB4rnFnHYckI6EQexdw3Z1V1I9d9j9zmWxLhdqa7BTFooyqhw3+FUowiw75+HhzpRFd/GyO6EkleWnTPLINvY6n3Ibrx+XC5DjDKhUAdK15psS8uJXExb7RX8LHaagOiTJ2HQmo3ffiSBaqLzDsLUhZDYS0t3R2Y8g+yty6yZo78tMhyPO7Dlgd0T/6xTiA589kKrUMb5xyWsfCBfMomTjNQomNOqkfX1S1hVqDGEL/FHKJLohqEGstj0t1Dew3aofiuE4GTK0QUGJAmklUHnpamOz7bmRCDStFcTSrRrAmpDUewy1biz3Lapxdz2dYRvZ9FKtoHAha8dRGLEDwIVTV7uV/lIE+bgNNuwJFCReLaiUIuWELIlC8lYMYCZeal2w5PE7TBSsv/fQuw0A7/EHef6/kh9p0rkln4/f66yATSvVVE33pBdVaAMrKw3M1CD8v1tJY6Lo84u2LldCaxorcTHucmK68XDgMN8TLDmKopEYBP/TbtRuJSckog+CNUMSEqRsVo67iuMhLZS7kXBVLcfaARnCvrIGWN/U5TlUR6w0d/LEMjeQNWRI4K/5Newe53lpjIOP2nEhDTvipWhlUcPLJFuQ8RFo0LUFf+njwkDQO8W25njyPoAz4tYEBtts8l1+kmGNHXIqney3cNkFipxZiZKqZWMvY0lmtRXGS+UsMrmOtDd8Hr0AD2yDr5sc8kdE4rz85+AjDw443XSmnq8/BQWzMjFIkRoXk02Meqbbws3hMoX58AKicvYheZdvoBCOuKiH0L4UqQZLPo16b5qiMIZGIK5MTyttVu6V3gqujIpD3JkMe4LV29IIdLFIPuMaMpQiE69LMOiTkb2qmCN+jpaIoJwjr5IVbomABCPs1loNchvwwRozpUqSP7CrSOICeTZxVY3tRBi/IBCmD5TLRQIII8P3CR7oMrk+Bm5u9s7H//UVv8dbD267wKQ1i4zvUK4h1vbP7pY3TBG7bArkX9DjpyqHMUSjKwM2kbx5cvXozykUAwXR6Ssc9urRdauqn/Lkw1Kp4lMXKv3giOJDQ58v1SzleOfqG/bnWEhHEb2k/OTyxkig9cPDh6XuoKl8YmN2/drt5/eWQ+qhMfM/X+t6ssBoBCsMkeymLco8qmwOEJYL2+5mJs6MY0l9G6vL0TwqEqkAZzB+oFW/cxp1xQAK7f0smcSPw+uY6BpBl60HEgM+xDX0/46oxRr2L5nx/0bCrYI2slTw9w73jdy8wCxRGw7Q+VuBfCB2f/mS/L8LhlMZOpzJw7+sOtpzd4OEN9RZ1eTD2Q7D1DK+Ev+ydGrXZPggSs9AlW5TeAqyQnFFTGCi76EIRamMUe1w1mK6XNjeEdV9/tfSAFoKvBWMlKoJMD8tbh7SjMgDtt7EgfBKymniZCY0dG1yMJC/JyzYtDyASejMIFD/c+EChAetoaCmVX6Ghy1j65KqFPntt4Qj7PSBWPUuTQCYLZ4UEzI+AnBRy3iSJo8cYzbsJrkGkWo1rgaWwddIFLeNUF2hsP/gykCKr2pCz88jAthRwmzbqGU7luNzlz5SXzv/TwOCOa4XV6NPBrs+t9c9HxIzAjjwz+HUf9NEwYhlAejnErYkqXD4v0vWialOWaMcIdYUDPPt5SN/n/2jNPHEBni9xJBp91yFKG/0if8wWu9knNQ5XCSeC9+M6pLY65dY+T911x4VR/1cdIjXad2pCuf/BgseiwWblfN97lKLRVQjgOkE+J7Ps/gzqW5kJsuE2+Rc+7Acny6MjVmqXvtZBhaCsWZzG06AHT2YH4qChCeVrau5X+IQhBf1mdM4TR3X5WNgRj3c8vEIev84RkPPdhRGC2Q2xqwwkF9ttvCBNl9dAKeG3TVWgtQLBghfZzd1drykNcT0w8LWW7Tg8VF9nxFI2jZ9z9nIhtsTyY664W+tpB0XGdgDdVslUbwQ+rlhPitP7f8Vr6KPXwJWzdkR1CPwVDFqgU3AuapriGmO06hwG65zEu2u5Pz0/ASOvKPHGbFpdJFHQjrzU2dMioHLuTHByhRLBnFwAxpU07Z8Dw/Klm2dd6eR1PsySz6DEePe9vVQ+w3g3gs1LeEQ4AAz3avh3FaT6pO3e9FCkXAO7r7S3qI7Fey74Z7GFm79mE1xCJSsURMybscCXsXb/fCI21NCs7cx6NTjcXBN4SpJsbAeL+0PH/TJVye9ueE/qL2sYCkITH/s2CYK9hbxdaUFqKPKOBYcxPDi+4r47fXz3cGs49aApXI7m9F/xlofQA8v8lk1lgDRxjDHAbA8kITqD0jG18RU0k/rYs2+PAji6H3XCz0zer27FH0bmz1kLG70W17zSzHgz/QQEsfj7k5ZJe/8jK5dv9eKW6h3d59PA5G74I9paT+ChnFhl+GbCZaAqn6rKViT4OPXfbecPSzeQEmNFNV8hjptxb8EVAgeuU3UTI1LJ+BLK1RKwoSYEUvUCFRgOicnFbQZahZHMdOaLjcOSJjxCw6IPaHFS12SWkHJOLRKYqZcg94DcXoUZkswX6E+zfWKhswkB7TgUO3vPZxmDIsrw2GDQSUoVBy8GrIOj4CIablc4muykjensSahKdxmSEK6oUEO+oMwmIdHfiqK00dOXYI5zZy0bjlWMH3sG00INef/QUsR+CWXWET6PR+5gB82IkJZSQ3KwAZboMQVm/ipeI7QHQ3YYxzbYO4155yxMk/GAah4rGFYFTVvy1pZbTnNvt1ZNGF1ItFIF5GFtIXKavZCYarLZz2ZFY9pp1pnkURwQiXrYUf6PcOCBfBdl6iMLKU/opDr/cFcLEY1sxD6EE+XyL7L6tRBGB361pNNOFR8ZxNeyYg+F9DNEm2AktQZWmCQcqGSIaJ6lX746gGtK9dDpVuUzkWNHHnNBGGQwVSqqnh6ZoUxZPzjChYSISQFrxOBp2LTCF/UElzF0u/kr14rPrVXwPm4E611AqhdxGbY9is4NR/VCA6nKHbMJv+KJH7+JoWj1dTnLEOc1oq4gQMyHjP2PbLaeVRAb7cucQCYJgpkkUSpY2aGtvWBVRO4gbXTssP77f1baTLlOSF2aM1IX3kHIwqsncA==)

**2. Handling Secrets**

When your Edge Function needs credentials, API keys, or tokens, do not hardcode them in the function code. Store them as Supabase Edge Function secrets so they remain encrypted and are not exposed in your app or repository.

To add a secret, open your Supabase project, go to **Edge Functions > Secrets**, enter the secret name and value, then click **Save**. For example, you can add an any API key as:

```
ANTHROPIC_KEY=your-api-key
```

Then reference it inside your Edge Function using `Deno.env.get()`:

```
const apiKey = Deno.env.get("ANTHROPIC_KEY")

if (!apiKey) {
  return new Response("Missing ANTHROPIC_KEY", {
    status: 500,
    headers: { ...corsHeaders, "Content-Type": "text/plain" },
  })
}
```

![edge-functions-handle-secrets.avif](https://docs.flutterflow.io/assets/images/edge-functions-handle-secrets-e43cc17dc005248fcc90a730698971e8.avif)

This keeps sensitive values on the Supabase backend while allowing your function to securely use them at runtime.

**3. Trigger Edge Functions and Use Result**

Once the Edge Function is deployed, you can trigger it from an action in your app.

For example, on a button tap or page load, add the **Edge Function** action and select the function you created. Pass the required input parameters, such as the list of reviews.

![trigger-edge-function](https://docs.flutterflow.io/assets/images/trigger-edge-function-07ee10274b9bb6cebace4c8584e60e7e.avif)

If the function returns a value, provide an **Action Output Variable Name** while configuring the action. You can then use the returned data from:

**Set from Variable > Action Outputs > \[Action Output Variable Name]**

For this example, you can use the returned JSON values, such as `summary` and `sentiment`, to update page state variables or display the AI-generated review summary directly in your UI.

![use-edge-function-result](https://docs.flutterflow.io/assets/images/use-edge-function-result-89af9a939949c872bda0df3eca8c2716.avif)

---

### Code File {#code-file}

*Learn how to create and use custom classes and enums in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/custom-code/code-file

FlutterFlow allows you to add your own custom Dart files with [classes](https://dart.dev/language/classes) and [enums](https://dart.dev/language/enums). This means you can create reusable building blocks to manage your app’s data and logic more easily. Using custom classes, you can create custom data types, use their properties in the UI, call methods in action flows, and much more.

#### Key Use Cases

* **Custom Models**: Define your own data models, such as `UserProfile`, `Product`, or `Order`, and use them throughout your app.
* **Business Logic**: Add reusable utility methods like tax calculations, formatting, or conditional evaluations.
* **Reusable Enums**: Define enums and use them in UI conditions and dropdowns.

Limitations

* **No Generics:** Classes with generic types (e.g., `class ApiResponse<T> {}`) are currently not supported.
* **No Function-Typed Parameters:** Methods or fields that have function types as parameters or fields are ignored (e.g., void Function(int) onTap).
* **No Extensions:** Dart Extensions (e.g., `extension StringX on String { … }`) are not supported yet.

#### Create Custom Class

To add a custom class, go to the **Custom Code** from the left navigation menu, click **plus (+)** button, and select **Code File**. Set the name of the file, add your code, and hit the **Save** button. Now, you must **validate** your code in the editor to catch basic syntax errors. If there are no errors, click the **Parse** button. FlutterFlow will scan your code and automatically detect supported classes and enums.

Here’s an example of adding a `Review` custom class:

Here's the code snippet of the `Review` custom class:

```
class Review {
  String id;
  String productId;
  String userId;
  String userName;
  String comment;
  double rating; // out of 5
  ReviewStatus reviewStatus;
  DateTime date;
  int helpfulCount = 0;

  Review(
    this.id,
    this.productId,
    this.userId,
    this.userName,
    this.comment,
    this.rating,
    this.reviewStatus,
    this.date,
  );

  // Method: Get a short version of the comment
  String shortComment() {
    if (comment.length <= 50) return comment;
    return comment.substring(0, 47) + "...";
  }

  // Method: Get formatted date as string (e.g., "2024-05-22")
  String formattedDate() {
    return "${date.year}-${_twoDigits(date.month)}-${_twoDigits(date.day)}";
  }

  String _twoDigits(int n) {
    return n >= 10 ? "$n" : "0$n";
  }

  // Method: Check if review is positive (4 stars or more)
  bool isPositive() {
    return rating >= 4.0;
  }

  // Method: Check if review is recent (within last 30 days)
  bool isRecent() {
    final now = DateTime.now();
    return now.difference(date).inDays <= 30;
  }

  // Method: Mark this review as helpful
  void markHelpful() {
    helpfulCount += 1;
  }
}
```

> **Tip:** You can also include import statements and access generated classes within your custom class files. For more details, [**see the examples**](https://docs.flutterflow.io/concepts/custom-code/common-examples) on how to access generated classes.

#### Create Custom Class Instance

You need to create an instance of a class so you can work with actual data and use the class’s properties and methods in your app. Here’s a simple explanation:

* A **class** is like a blueprint or template. For example, the `Review` class describes what a review is, but doesn’t hold any real review information itself.

* An **instance** (or “object”) is a real, usable item made from that blueprint. See the code snippet below:

  ```
  Review review1 = Review(
    'r001',
    'p123',
    'u456',
    'Alex Morgan',
    'Great quality T-shirt!',
    4.5,
    DateTime(2025, 5, 22),
    3,
    ReviewStatus.approved,
  );
  ```

* In FlutterFlow, you will store the instance of the custom class in the [state variables](https://docs.flutterflow.io/concepts/state-management#state-variables) of your app, page, or component.

* You can create multiple instances of the same class, reusing the same structure multiple times, each with different review data.

When you create an instance of a class, you can:

* Store actual review details.
* Access and update the fields (e.g., `review1.rating` or `review1.comment`).
* Call methods that do something with that data (e.g., `review1.markHelpful()` or `review1.shortComment()`).

To create an instance of a custom class, first you need to [create a state variable](https://docs.flutterflow.io/concepts/state-management#creating-state-variables) (of type Custom Class) that will hold the instance. Then, to create and add the instance to the state variable, open the **Set from Variable** dialog and select **Create Custom Class Instance**. Choose the class you want to use, then select the class name from the **Constructor** dropdown. After that, set values for each of the required fields.

#### Using Custom Class

Once the custom class is added successfully, you can access its fields and methods in the Variable Dialog, call its methods in the Action Flow Editor, assign instances to state variables, pass them to page or component parameters, and use enum values in dropdowns or conditionals.

##### Custom Class as Data Type

You can select your custom class as a Type for variables, state, or parameters, just like a [Custom Data Type](https://docs.flutterflow.io/resources/data-representation/custom-data-types).

![custom-class-as-data-type.avif](https://docs.flutterflow.io/assets/images/custom-class-as-data-type-ae8e906e74a17fc8e9cbaff4f9e296e7.avif)

##### Access Fields and Methods

You can use custom class fields to display values directly in the UI, and call its methods in variable dialogs to return a result.

![access-fields-methods.avif](https://docs.flutterflow.io/assets/images/access-fields-methods-080e4deaf0c376847b91845fb82c62ae.avif)

##### Set Field \[Action]

Use the **Set Field** action to update a specific property of a custom class instance. For example, you can set `review.comment = 'Great fit and quality!'` when a user updates the review, allowing the UI to reflect the new comment instantly.

##### Call Method \[Action]

Use the **Call Method** action to invoke a method defined in your custom class. For instance, if your `Comment` class has a `markHelpful()` method, you can trigger it when a user taps a “Helpful” button to record the interaction.

#### Using Static Members

Sometimes, you may want to define fields and methods that are shared across your app. In such cases, `static` fields and methods are ideal. Because they're tied to the class rather than an instance, static members are accessible globally, for example, utilities for formatting, calculations, or global configuration.

This approach is typically used for **stateless utility classes** where shared functionality is needed across the app. For example, look at the class below:

```
class Utils {
  static int square(int x) => x * x;
}
```

The `Utils` class contains a static method `square` that returns the square of a number without needing to create an object of the class.

Here are couple more examples to understand it better:

* This `StringFormatter` class below provides reusable static methods to capitalize text, convert it to lowercase, or format it in snake\_case.

  ```
  class StringFormatter {
    static String lastFormatted = '';
    static int formatCount = 0;
    
    static String capitalize(String input) =>
        input[0].toUpperCase() + input.substring(1);

    static String toLowerCase(String input) => input.toLowerCase();

    static String toSnakeCase(String input) =>
        input.replaceAll(' ', '_').toLowerCase();
  }
  ```

* The `MathHelper` class offers handy static methods to calculate tax, apply discounts, find percentages, and round off numbers.

  ```
  class MathHelper {
    static double calculateTax(double amount) => amount * 0.18;

    static double applyDiscount(double amount, double discountPercent) =>
        amount - (amount * discountPercent / 100);

    static double calculatePercentage(double part, double total) =>
        (part / total) * 100;

    static int roundOff(double value) => value.round();
  }
  ```

> **Tip:** You can mix both **static** and **instance** members in a single class. Static members are shared across all instances, while instance members hold data specific to each object. For example, look at the class below:

```
class Review {
  static List<String> flaggedWords = ['bad', 'spam', 'fake'];
  
  String id;
  String userId;
  String comment;
  int helpfulCount = 0;

  Review(
    this.id,
    this.userId,
    this.comment
  );

  static bool isCommentAppropriate(String input) {
    return !flaggedWords.any((word) => input.toLowerCase().contains(word));
  }
  
  void markHelpful() {
    helpfulCount += 1;
  }
}
```

* `flaggedWords` is a static list used across all reviews.
* `isCommentAppropriate()` is a static method that can be used without creating a `Review` instance, useful for validating comments before saving them.

> **Warning:** Using static members are powerful, but they should be used carefully. Overusing static methods can lead to less flexible code and potential issues, especially when the logic requires access to state or needs to evolve over time. Stick to static methods only when the logic is truly independent and doesn’t rely on instance-specific data.

##### Access Static Fields and Methods

You can access the static class data and methods directly via the ****Set from Variable**** menu.

![static-class-methods.avif](https://docs.flutterflow.io/assets/images/static-class-methods-d338fb2df9b78de2bf5c63a570edf8ce.avif)

##### Set Static Field \[Action]

Use the **Set Static Field** action to update a static field on a custom class. For example, if you have a class `MathHelper` with a static field `amount`, you can set it using an input value when a user enters a price. This allows you to store that value globally and use it across different calculations.

##### Call Static Method \[Action]

Use the **Call Static Method** action to run a static method of your class. For instance, you can call `MathHelper.calculateTax(amount)` to compute tax on a given amount during a checkout action, without needing to create an instance of the class.

#### Custom Enums

Similar to how you add a custom class, you can also add Custom Enums in your app. [Enums](https://docs.flutterflow.io/resources/data-representation/enums) are a great way to define a fixed set of values, such as user roles, order statuses, or content types. Once parsed, these enums become available throughout your app and can be used in dropdowns, conditionals, and UI bindings.

For example, you could define an enum called `ReviewStatus` with values like `pending`, `approved`, and `rejected`. Here's the code snippet for it:

```
enum ReviewStatus {
  pending,
  approved,
  rejected,
}
```

![custom-enums.avif](https://docs.flutterflow.io/assets/images/custom-enums-ddb46d1db418b8cc6c52f3a58b86d75d.avif)

You can access the custom enums from **Set from Variable** menu > **Custom Enum** section. You’ll see your Dart file listed by name. Select the enum you want to use, such as `ReviewStatus`, and then choose the specific value you want to assign.

#### Tips & Best Practices

* Keep your custom class files modular and focused; ideally one class per file for better organization and reusability.
* Avoid advanced Dart features that are not supported by FlutterFlow’s parser, such as generics or function-typed fields.
* Re-parse your code after making changes to ensure FlutterFlow updates the parsed structure correctly.
* Document your code with comments to make your custom classes easier to understand and maintain over time.

#### FAQs

Can I add Custom Classes (Code Files) in a Library Project?

Yes, you can. When a Library Project is imported, any custom code files you’ve defined will be parsed, and the resulting classes will be available for use in the consuming project.

---

### Common Code Examples {#common-code-examples}

*Learn about the common custom code examples and use it directly in your project.*

**Source:** https://docs.flutterflow.io/concepts/custom-code/common-examples

The custom code feature in FlutterFlow allows you to extend functionality by accessing generated classes and modifying global variables like App States and FlutterFlow themes. This guide covers common scenarios where you can leverage custom code to enhance your project by working directly with data models and other resources within your code.

Disclaimer

Custom Functions cannot import new files or packages outside of the default dedicated imports. Therefore, most of the suggestions below that involve adding a new import will not work in Custom Functions due to this restriction. However, they will work for Custom Widgets and Custom Actions.

For example, a new [**Custom Function**](https://docs.flutterflow.io/concepts/custom-code/custom-functions) typically includes the following packages and files. Your custom function code changes should use only these packages & files:

```
import 'dart:convert';
import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:intl/intl.dart';
import 'package:timeago/timeago.dart' as timeago;
import 'lat_lng.dart';
import 'place.dart';
import 'uploaded_file.dart';
import '/backend/backend.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import '/backend/schema/structs/index.dart';
import '/backend/schema/enums/enums.dart';
import '/auth/firebase_auth/auth_util.dart';
```

##### Access FlutterFlow Generated Classes

FlutterFlow generates a complete Flutter codebase for you as you build apps in its platform. Part of this code includes custom classes that are designed to streamline common tasks and encapsulate reusable properties or logic.

For example:

* **Button Widgets:** FlutterFlow provides custom button classes like `FFButton` that come with built-in styling and behaviors.
* **Google Places:** The `FFPlace` class encapsulates properties of a Google Place, such as name, address, and coordinates.
* **File Uploads:** The `FFUploadedFile` class represents files uploaded to your app, encapsulating properties like the file name, bytes, and URL.

What is a Class?

In programming, a class is a blueprint for creating objects. It defines properties (data) and methods (functions) that belong to objects of that type.

For example,

* A `Car` class might have properties like `color` and `speed` and methods like `drive()` and `stop()`.
* In FlutterFlow, a class like `FFPlace` might have properties like `address` and `latLng`, and methods to manipulate or retrieve these values.

These custom FlutterFlow classes in the generated code are mostly prefixed with `FF<ClassName>` or `FlutterFlow<ClassName>`. If you need to access these classes in your custom code, simply type "FF" or "FlutterFlow" in the code editor to locate them quick.

![suggestions-dropdown.png](https://docs.flutterflow.io/assets/images/suggestions-dropdown-7cdcb2e99a811ac6ad11b2e94aae4cf1.png)

##### Leveraging Components in Custom Widget

Static Components vs Dynamic

Use this approach only when the component is a fixed element that does not change across different use cases. If the child component needs to change based on user choices, pass it directly [**as a parameter**](https://docs.flutterflow.io/concepts/custom-code/custom-widgets#creating-a-new-custom-widget).

In a **[Custom Widget](https://docs.flutterflow.io/concepts/custom-code/custom-widgets)**, you can integrate a previously built **[FlutterFlow Component](https://docs.flutterflow.io/resources/ui/components)** directly, saving you from recreating child content in code. For example, if you’re building a Custom Widget to display custom dialog boxes or bottom sheets using a package from [pub.dev](https://pub.dev/), you can simply return an existing Component created on the canvas, rather than coding a new one from scratch.

Imports

When referencing a Component class in your code, FlutterFlow will automatically add the necessary import statement.

![return-widget-custom-code.png](https://docs.flutterflow.io/assets/images/return-widget-custom-code-6c3678bc441c99b54929ff3c4028580e.png)

##### Get FlutterFlow Theme in Custom Widget

When building custom widgets, you often need to style parts of the widget, such as setting colors. Instead of using hardcoded color values, you can directly access the **FlutterFlow Theme**. This theme provides consistent styling across your app and reflects colors set by you or your project developer.

To access theme colors in your custom widget, use the `FlutterFlowTheme.of(context)` method. This allows you to retrieve any theme property, such as the default `primary`, `primaryBackground`, or other custom-created colors, as well as text styles like `bodyLarge` or `bodyMedium`, ensuring that your custom widget aligns with the app’s overall theme.

Here’s an example of how to use the primary color from FlutterFlow Theme in a custom widget:

Imports

Ensure you import `import '../flutter_flow/flutter_flow_theme.dart';` when accessing `FlutterFlowTheme` in your custom widgets.

```
class CustomButton extends StatefulWidget {
  final String label;

  CustomButton({required this.label});

  @override
  _CustomButtonState createState() => _CustomButtonState();
}

class _CustomButtonState extends State<CustomButton> {
  bool isPressed = false;

  void toggleButton() {
    setState(() {
      isPressed = !isPressed;
    });
  }

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      style: ElevatedButton.styleFrom(
        backgroundColor: isPressed
            ? FlutterFlowTheme.of(context).primary // Primary color when pressed
            : FlutterFlowTheme.of(context).secondaryBackground, // Default color
        foregroundColor: FlutterFlowTheme.of(context).secondaryText, // Text color
      ),
      onPressed: toggleButton,
      child: Text(
        widget.label,
        style: FlutterFlowTheme.of(context).bodyText1, // Themed text style
      ),
    );
  }
}
```

##### Modifying AppState from Custom Code

In FlutterFlow, you can access or update AppState directly from the Action Flow Editor. However, certain scenarios may require you to access or modify AppState within custom code for more control over the operation flow. The `FFAppState` class also provides additional helper functions to modify AppState values. Let’s look at some examples:

Imports

Ensure you import `import '../../flutter_flow/flutter_flow_util.dart';` when accessing `FFAppState` in custom code resources.

* **Get AppState value in Custom Code**

```

Future getCartItems() async {
  // Retrieve the current cart items from AppState
  final currentCartItems = FFAppState().cartItems;
  print('Current Cart Items: $currentCartItems');
}
```

* **Updating AppState Values in Custom Code**

```
Future enableDarkMode() async {
  // Enable dark mode in AppState
  FFAppState().update(() {
    FFAppState().enableDarkMode = true;
  });
  print('Dark mode enabled');
}
```

* **Modifying a List in AppState Using Helper Functions**

The `FFAppState` class offers a variety of helper functions to easily manage list variables in AppState. For a detailed overview of this generated class, check out **[this guide](https://docs.flutterflow.io/generated-code/ff-app-state#managing-appstatelist)**. Here are some examples of how to use these helper functions to modify an AppState list variable:

```
Future addLocation(LatLng value) async {
  // Add a new location to the LatLng list
  FFAppState().addToLatLngList(value);
}

Future removeLocation(LatLng value) async {
  // Remove a specific location from the LatLng list
  FFAppState().removeFromLatLngList(value);
}

Future removeLocationAtIndex(int index) async {
  // Remove a location at a specific index from the LatLng list
  FFAppState().removeAtIndexFromLatLngList(index);
}

Future updateLocationAtIndex(int index, LatLng Function(LatLng) updateFn) async {
  // Update a location at a specific index in the LatLng list
  FFAppState().updateLatLngListAtIndex(index, updateFn);
}

Future insertLocationAtIndex(int index, LatLng value) async {
  // Insert a new location at a specific index in the LatLng list
  FFAppState().insertAtIndexInLatLngList(index, value);
}
```

##### Leverage Custom Data Types

When you create a custom data type in FlutterFlow, it **[generates a corresponding `<Name>Struct` class](https://docs.flutterflow.io/generated-code/custom-data-types)**. In FlutterFlow's custom code, you can create new instances of such data types, pass instances back into an action, or manipulate and retrieve information from existing objects. Here are some examples to help illustrate working with an example `ProductStruct` class.

###### Example 1: Creating a new Instance of `ProductStruct`

To create a new `ProductStruct` instance, initialize it with the required properties:

```
// Create a new instance of ProductStruct
final newProduct = ProductStruct(
    productId: '123',
    name: 'Example Product',
    description: 'A sample product description.',
    category: 'Electronics',
    subCategory: 'Mobile Phones',
    price: PriceStruct(amount: 299.99, currency: 'USD'),
    sizes: ['Small', 'Medium', 'Large'],
    colors: [ColorsStruct(colorName: 'Red', colorHex: '#FF0000')],
    images: [ImagesStruct(thumbnail: 'https://example.com/image.jpg')],
    stockStatus: StockStatusStruct(xs: 0, small: 2),
    reviews: [ReviewsStruct(rating: 4, comment: 'Great product!')],
);
```

###### Example 2: Get Properties of an Existing `ProductStruct` object

If you have an existing `ProductStruct` object (e.g., retrieved from a list of products), you can access its properties or return specific values back to the calling Action.

Let's assume you have an Action that calls a Custom Action to retrieve a field value from the provided `ProductStruct` object.

* **Returning a Single Field from ProductStruct**

This function retrieves and returns the product's name. The return type is `String?` to account for the possibility of a null value.

```
// Function to return the product name from a ProductStruct instance
String? getProductName(ProductStruct product) {
    // Get and return the product name
    return product.name;
}
```

* **Checking if a Field Exists in a `ProductStruct` Object** This function determines whether the `ProductStruct` object contains a non-null value for a specific field, such as `description`. It returns `true` if the field exists and is not null, and `false` otherwise.

```
// Function to check if the description field exists in a ProductStruct instance
bool hasDescription(ProductStruct product) {
    // Return true if the description is not null, false otherwise
    return product.description != null;
}
```

* **Returning a List of Review Comments from ProductStruct**

This function retrieves a list of review comments from the reviews field in the `ProductStruct`. The return type is `List<String>` as it returns a list of comments (or an empty list if there are no reviews).

```
// Function to return a list of review comments from a ProductStruct instance
List<String> getProductReviewComments(ProductStruct product) {
  // Check if reviews are present and return a list of review comments
  return product.reviews?.map((review) => review.comment ?? '').toList() ?? [];
}
```

###### Example 3: Modifying Properties of an Existing `ProductStruct` Object

You can also modify the properties of an existing `ProductStruct` object. This can be helpful if you want to update a field before saving the data back to Firebase or passing it into an action.

* **Simple Property Modification** In this example, we’ll modify a single property, like `productName`, of an existing `ProductStruct` object. This example is straightforward and demonstrates how to update a basic field in the object.

```
// Function to update the product name of a ProductStruct instance
Future updateProductName(ProductStruct product, String newProductName) {
  // Update the product name with the new value
  product.productName = newProductName;
}
```

* **Complex Property Modification - Nested Object Update** In this more complex example, we’ll modify a nested property within the `ProductStruct`, such as updating the price (which itself is a `PriceStruct` object). This shows how to update a property that itself contains multiple fields.

```
// Function to update the price of a ProductStruct instance
Future updateProductPrice(ProductStruct product, double newAmount, String currency) {
// Check if price is not null
    if (product.price != null) {
        // Update only the amount field
        product.price!.amount = newAmount;
    } else {
        // If price is null, optionally initialize it if needed
        product.price = PriceStruct(
            amount: newAmount,
            currency: currency,
    );
    }
}
```

* **Complex Property Modification - Updating a List Property** In this example, we’ll add new items to a list property, like adding new review comments to the `reviews` list in `ProductStruct`. This example shows how to work with a list of nested objects.

```
Future addNewReviews(ProductStruct product) {
  product.reviews ??= []; // Initialize the reviews list if it's null
  product.reviews!.addAll([
    ReviewStruct(rating: 5, comment: 'Excellent product!'),
    ReviewStruct(rating: 4, comment: 'Good quality, but a bit expensive.'),
    ReviewStruct(rating: 3, comment: 'Satisfactory, meets expectations.'),
  ]);
}
```

or if the new list of reviews is being provided to the Custom Action, then:

```
Future addDynamicReviews(ProductStruct product, List<ReviewStruct> newReviews) {
  product.reviews ??= []; // Initialize the reviews list if it's null
  product.reviews!.addAll(newReviews); // Add the new reviews
}
```

##### Using Firebase Auth Variables in Custom Code

When using Firebase Authentication for your app, FlutterFlow provides access to key authentication data, such as `currentUserDisplayName`, `currentUserUid`, and more. These variables can be used in your Custom Actions to build additional features that require such common data from authenticated users.

For example, you can check if a user’s email is verified before proceeding with certain actions:

```
if (currentUserEmailVerified) {
  // Perform action for verified users
}
```

Or, if you need to create a directory path that includes the user’s unique ID:

```
String directoryPath = '/users/' + currentUserUid + '/files';
```

Here’s a list of other Firebase Auth variables that can be referenced in Custom Code:

* `currentUserEmail` – The email address of the current user.

* `currentUserUid` – The unique ID of the current user.

* `currentUserDisplayName` – The display name set by the user.

* `currentUserPhoto` – The profile photo URL of the current user.

* `currentPhoneNumber` – The user’s phone number, if available.

* `currentJwtToken` – The current user’s JWT token for secure requests.

* `currentUserEmailVerified` – Boolean indicating if the user’s email is verified.

* These variables make it easy to integrate Firebase Auth data into custom functionality, enhancing the user experience.

##### Get Dev Environment Values in Custom Code

Similar to `FFAppState`, FlutterFlow generates a singleton `FFDevEnvironmentValues` class in your FlutterFlow generated codebase, if you are using **[Dev Environments](https://docs.flutterflow.io/testing/dev-environments)**. This class can also be accessed from custom code if needed. It is generated based on the environment selected by the user at the time of code generation.

To access any Dev Environment values in custom code, simply use:

```
Future getWebhookId() async {
  // Add your function code here!
  return FFDevEnvironmentValues().webhookId;
}
```

##### Access Library Components in Custom Code

When using a library dependency in your project, you can also access its components, such as Library App State, Library Values, and Library Widgets, in the user project's custom code. Here are a few examples:

###### Get Library Values

Similar to `FFAppState` or `FFDevEnvironmentValues` class, FlutterFlow generates a singleton `FFLibraryValues` class for library projects, which provides direct access to **[Library Values](https://docs.flutterflow.io/resources/projects/libraries#library-values)**.

To access Library Values directly in custom code:

```
Future getSchema(StateStruct? syncStatus) async {
  print(FFLibraryValues().schema);
}
```

###### Get Library Custom Code

When you add a library dependency to your FlutterFlow project, FlutterFlow automatically includes necessary imports, allowing you to utilize custom code resources from the library project in your user project's custom code files.

For example, if you have a library with project ID `library_hybw3o`, FlutterFlow will add the following import to your project:

```
import 'package:library_hybw3o/flutter_flow/custom_functions.dart' as library_hybw3o_functions;
```

Now, let's use the library’s custom functions in the user project's custom function:

```
int getRandomIndex(List<int> indexList) {
    final item = library_hybw3o_functions.getRandomItem(); // Library's custom function
    // get Random Index
    final randomNumber = math.Random();
    return ...
}
```

###### Manually Add Library Imports

If the library import doesn’t appear in your project automatically, you can manually add it and assign a custom alias. For example, to import a library’s custom actions into your project’s Custom Widget resource, add the import yourself as shown below:

For example, let's import the library's custom actions into the user project's Custom Widget resource.

If the import is not already available, you can add it manually as follows:

```
// Custom import
import 'package:library_hybw3o/custom_code/actions/index.dart' as library_hybw3o_actions; // Assigning a custom alias to the import

// Example Widget code
class CustomDialog extends StatefulWidget {
  const CustomDialog({
    super.key,
    this.width,
    this.height,
  });

  final double? width;
  final double? height;

  @override
  State<CustomDialog> createState() => _CustomDialogState();
}

class _CustomDialogState extends State<CustomDialog> {
    @override
    void initState() {
        library_hybw3o_actions.getSchema(StateStruct()); // calling library custom action
        super.initState();
    }
    @override
        Widget build(BuildContext context) {
            return Container(height: 50, width: 50);
    }
}
```

---

### Configuration Files {#configuration-files}

*Learn how to modify platform-specific files for Android and iOS to extend your app's capabilities.*

**Source:** https://docs.flutterflow.io/concepts/custom-code/configuration-files

FlutterFlow allows you to modify configuration files for your app, and platform-specific files, without leaving the FlutterFlow interface.

In some cases, you’ll need to tweak the configuration files that FlutterFlow generates. This is usually required when integrating third-party packages such as analytics, ad networks, and payment solutions.

Here are the key configuration files you can edit:

* [**`AndroidManifest.xml`**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#androidmanifestxml-android) – Configures app permissions, metadata, and intent filters for Android.
* [**`build.gradle`**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#buildgradle-android) – Defines Android specific build configurations such as compile SDK version, dependencies, build types, and signing configurations.
* [**ProGuard files**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#proguard-file-android) – Used for code shrinking and obfuscation in Android builds.
* [**`Info.plist`**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#infoplist-ios)– Manages iOS app settings, including permissions and configurations.
* [**`Entitlements.plist`**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#entitlementsplist-ios) – Defines iOS app privileges such as push notifications and Apple Pay.
* [**`AppDelegate.swift`**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#appdelegateswift-ios) – Manages iOS app launch behavior and runtime configuration. It registers Flutter plugins, initializes services like Firebase, and handles app lifecycle events and deep linking.
* [**`main.dart`**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#maindart-flutter) – The entry point of your Flutter app, where you can modify app-level logic.

> **Warning:** While editing configuration files can unlock advanced functionality, it comes with risks. A small mistake (e.g., a missing XML tag or a wrong key) can cause your app to fail compilation or crash at runtime. Incorrect changes might lead to App Store/Play Store rejections. So, it’s important to note your changes and thoroughly test your app after each edit.

In short, edit native code only when necessary, and do so carefully.

#### Editing Files

FlutterFlow provides two main ways to modify native files: [**Add Individual Snippets**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#option-1-add-individual-snippets) and [**Manual Edit Mode**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#option-2-manual-edit-mode).

##### Option 1: Add Individual Snippets

**Snippets** are small pieces of code that you can inject into the native files at predefined locations. Instead of opening the whole file to edit, you provide just the fragment you want to add, and FlutterFlow merges it into the file in the correct place. This is safer and easier for small additions such as a permission line or a meta-data tag.

###### Snippet Placement for Android

Let’s see how to add a snippet for the `AndroidManifest.xml` file, where you can add the following tags:

* **Activity Tags:** Inserts XML code inside the `MainActivity` block. This is typically used to add child XML elements within the MainActivity, such as `<intent-filter>` or `<meta-data>` to control aspects such as deep linking, theme application, or launch mode.
* **Application Tags**: Used to inject properties or attributes directly on the `<application>` tag itself. For example, you can use this to set values such as `android:icon`, `android:label`, `android:allowBackup`.
* **App Component Tags**: Inserts complete XML components inside the `<application>...</application>` block. Use this to add additional activities, services, broadcast receivers, or content providers that your app depends on.

To add a snippet to your `AndroidManifest.xml`, navigate to **Custom Code** from the left navigation menu, select **Configuration Files**, then choose `AndroidManifest.xml`. Click the **plus (+)** button next to the tag where you want to insert the snippet. Provide a name (this will be included as a comment in the file) and paste your snippet code.

###### Snippet Placement for iOS

For iOS, let’s see how to add a snippet for the `Info.plist` and `Entitlements.plist` files. There’s no nested application/activity structure like on Android. Instead, both files are dictionaries of key-value pairs. When you add a snippet, it’s placed directly under the root `<dict>` element of these plist files.

To add a snippet to native iOS files, navigate to **Custom Code** (from the left-side menu) > **Configuration Files**, and select the desired file. Click the **plus** (+) button, provide a descriptive name (which will appear as a comment in the file), and paste your snippet code.

> **Tip:** * Snippet insertion isn't available for `main.dart`. Instead, you can directly modify the file using [**Manual Edit Mode**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#option-2-manual-edit-mode).
* You can also use your Development [**Environment Values**](https://docs.flutterflow.io/testing/dev-environments#environment-values) and [**Library Values**](https://docs.flutterflow.io/resources/projects/libraries#library-values) inside snippets. For more details, refer to the [**Include Variables in Native Code**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#include-variables-in-native-code) section.

##### Option 2: Manual Edit Mode

For more complex changes, you can enable **Manual Edit Mode**, which unlocks the entire file for free-form editing. This is like opening the raw file in a text editor directly within FlutterFlow. **Note that** the manual mode is powerful but should be used carefully.

To manually edit native files, navigate to **Custom Code** (from the left-side menu) > **Configuration Files**, select the file you want to edit, and click the **lock** button to unlock it. You can now freely modify the file.

> **Warning:** Once unlocked, the file stays in manual editing mode until you lock it again. Re-locking it will reset the file to a version generated by FlutterFlow, which will overwrite any manual changes you've made.

> **Tip:** * Don’t remove FlutterFlow’s existing entries unless you are sure. It’s safer to only add or modify necessary lines and leave the rest as is.
* Use Manual Edit Mode for bulk or complex edits that the snippet can’t easily do, such as reordering tags, removing something, or pasting in a large chunk of config. Always verify that the app still builds and runs after such edits.
* You can also use your Development [**Environment Values**](https://docs.flutterflow.io/testing/dev-environments#environment-values) and [**Library Values**](https://docs.flutterflow.io/resources/projects/libraries#library-values) inside snippets. For more details, refer to the [**Include Variables in Native Code**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#include-variables-in-native-code) section.

#### Include Variables in Native Code

When editing native files in FlutterFlow, you may need to include dynamic values, such as API keys, app configurations, or environment-specific settings. Instead of hardcoding these values directly in **`AndroidManifest.xml`**, **`Info.plist`**, or other native files, you can use FlutterFlow [**Environment Values**](https://docs.flutterflow.io/testing/dev-environments#environment-values) and [**Library Values**](https://docs.flutterflow.io/resources/projects/libraries#library-values) to keep your app flexible and secure.

To include a variable in a configuration file, start by creating a **file-level variable** and assigning it a value from either your **Environment Values** or **Library Values**. Then, reference this variable using a placeholder format (e.g., `{{apiToken}}`) within the configuration file. These placeholders in native files are automatically replaced with their actual values during the code generation process.

Here’s exactly how you do it:

> **Tip:** * You can also directly insert a variable placeholder (e.g., `{{variableName}}`) into the code using a snippet or manual edit mode and FlutterFlow automatically creates the corresponding file-level variable.
* You can use the file level variable across different snippets within the same file.

Here are some examples that utilize variables in native code:

**Example 1: Using API Keys in `AndroidManifest.xml`**

Let’s say you are integrating the Mapbox package in your FlutterFlow app, and it requires an API Key in the form of a token inside the `AndroidManifest.xml` file. Instead of hardcoding the token, you can use a variable like this:

```
<meta-data
    android:name="com.mapbox.token"
    android:value="{{MAPBOX_ACCESS_TOKEN}}"/>
```

Here, `{{MAPBOX_ACCESS_TOKEN}}` is a file level variable that holds the Environment Value.

**Example 2: Configuring `Info.plist` for iOS**

For iOS apps, you might need to configure App Transport Security (ATS) to allow non-HTTPS connections. Instead of manually setting `NSAllowsArbitraryLoads` to `true`, you can use a variable:

```
<key>NSAllowsArbitraryLoads</key>
<{{ALLOW_HTTP_TRAFFIC}}/>
```

If `ALLOW_HTTP_TRAFFIC` is set to `true` in FlutterFlow’s Environment Value, the app will allow HTTP connections.

**Example 3: Using Library Values**

If you are building a [FlutterFlow Library](https://docs.flutterflow.io/resources/projects/libraries) and need to include public API keys in native code, you can use [Library Values](https://docs.flutterflow.io/resources/projects/libraries#library-values) as placeholders. This ensures that when someone installs your library, they can define their own values.

For example, if your library integrates with a public weather API that requires an API key (such as Open-Meteo or WeatherAPI for general use), it’s best not to add the key directly in the manifest file. Instead, create a file-level variable and assign it a Library Value.

```
<application>
    <meta-data 
        android:name="com.google.android.geo.API_KEY" 
        android:value="{{WEATHER_API_KEY}}" />
</application>
```

The library user will define their own API key under Library Values when importing your library. At build time, FlutterFlow replaces `{{WEATHER_API_KEY}}` with the user-defined key.

#### Editable Files

FlutterFlow allows editing several key native files. Below, we cover each file’s role, why you might need to edit it, and examples of real-world use cases.

##### `AndroidManifest.xml` (Android)

`AndroidManifest.xml` is the master configuration file for your Android app. It is located in the root directory of the app's `android/app/src/main` folder and declares essential app information to the Android OS and Google Play. This includes your app’s package name, components (activities, services, receivers), and the permissions it needs.

It defines hardware and software features the app depends on, such as Bluetooth, GPS, or sensors. The manifest manages intents and filters, determining how the app responds to system events and deep linking. It also includes metadata and configuration for SDKs and libraries, such as API keys or feature flags.

In short, the manifest is like an app’s identity card and permission sheet for Android.

Here are some scenarios where you may need to modify the `AndroidManifest.xml` file:

**Example 1: Declaring App Components (Activities, Services, Receivers)**

For including additional screens (activities), background processes (services), or listeners (broadcast receivers), you must declare them in `AndroidManifest.xml`.

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.app">

    <application
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name">

        <!-- Add your activity here -->
        <activity android:name=".NewScreenActivity" />
        
    </application>

</manifest>
```

This registers `NewScreenActivity` so the system knows it exists.

**Example 2: Requesting Permissions**

If your app requires access to restricted resources such as wake locks (to keep the device awake) or audio recording, you must declare the necessary permissions in `AndroidManifest.xml` by [manually editing](https://docs.flutterflow.io/concepts/custom-code/configuration-files#option-2-manual-edit-mode) the file. **Tip:** You can also add custom permissions directly through the [**Permission Settings**](https://docs.flutterflow.io/resources/projects/settings/project-setup#adding-custom-permission) in FlutterFlow.

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="com.example.yourappname">

    <!-- Permissions -->
    <uses-permission android:name="android.permission.WAKE_LOCK"/>
    <uses-permission android:name="android.permission.RECORD_AUDIO"/>

    <application
        android:label=""
        tools:replace="android:label"
        android:icon="@mipmap/ic_launcher"
        android:requestLegacyExternalStorage="true">

        <activity android:name=".NewScreenActivity"/>

    </application>
</manifest>
```

Without these, the app cannot keep the device awake or record audio.

**Example 3: Adding Metadata for SDKs and Libraries**

Many third-party packages (Google Maps, Firebase, AdMob, etc.) require `<meta-data>` tag in `AndroidManifest.xml` to pass configuration values. For example, the [**Mapbox Flutter**](https://pub.dev/packages/mapbox_flutter) plugin requires adding your Mapbox access token as a metadata entry for initialization. A real example: to initialize Mapbox, you’d add:

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.app">

    <application
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name">

        <!-- Your snippet goes here -->
        <meta-data
            android:name="com.example.MAPS_API_KEY"
            android:value="YOUR_API_KEY" />

    </application>
</manifest>
```

**Example 4: Restricting the App to Specific Devices**

You can specify device hardware requirements (e.g., GPS, camera, touchscreen) to ensure the app only installs on compatible devices.

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.app">

    <!-- Your snippet goes here -->
    <uses-feature android:name="android.hardware.camera" />

    <application
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name">
        
        <!-- other components -->

    </application>

</manifest>
```

This prevents installation on devices without a camera.

**Example 5: Enabling Cleartext Traffic**

If your app needs to communicate over HTTP (unencrypted) for testing or legacy reasons, you might need to add `android:usesCleartextTraffic="true"` in the `<application>` tag. This is to relax network security for HTTP URLs.

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.app">

    <application
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:usesCleartextTraffic="true"> <!-- Add this line -->

        <!-- Other components -->

    </application>

</manifest>
```

> **Tip:** You can modify the `AndroidManifest.xml` file by either [**adding a snippet**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#snippet-placement-for-android) or [**editing it manually**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#option-2-manual-edit-mode).

##### `build.gradle` (Android)

The `build.gradle` file is the main Gradle build script for your Android app module. It resides in the `android/app/` directory and controls how your Android app is compiled, packaged, and built. This file defines critical configuration such as:

* SDK versions (`compileSdkVersion`, `minSdkVersion`, `targetSdkVersion`)
* Dependencies for third-party libraries
* Build types (like debug vs. release)
* Signing configurations for release builds
* Kotlin and Flutter settings
* MultiDex and ProGuard rules
* Android packaging options

In short, the `build.gradle` file acts as the blueprint for how your Android app is built and prepared for distribution.

**Example 1: Changing SDK Versions**

To set which Android SDK your app compiles with, update the following section in `build.gradle`:

```
android {
    compileSdkVersion 33

    defaultConfig {
        applicationId "com.example.myapp"
        minSdkVersion 21
        targetSdkVersion 33
        versionCode 1
        versionName "1.0"
    }
}
```

Use this when you want to upgrade to a newer Android API level or need compatibility with certain libraries.

**Example 2: Adding Third-Party Libraries**

To use Android-specific libraries (such as Play Services or Jetpack), add them in the `dependencies` section:

```
dependencies {
    implementation 'com.google.android.gms:play-services-maps:18.1.0'
    implementation 'androidx.work:work-runtime:2.7.1'
}
```

Use this when integrating services like Google Maps, Firebase Messaging, or WorkManager.

**Example 3: Adding ProGuard Rules for Release Build**

If your app uses ProGuard (code shrinking/obfuscation), you can define custom rules or reference a rules file:

```
android {
    buildTypes {
        release {
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}
```

Use this to reduce APK size and protect code in production.

**Example 4: Enabling MultiDex for Large Apps**

If your app exceeds the 64K method limit (common when using many dependencies), enable MultiDex support:

```
defaultConfig {
    ...
    multiDexEnabled true
}
```

Use this when your build fails with `Too many methods` errors or when integrating large libraries like Firebase.

> **Tip:** You can modify the `build.gradle` file by either [**adding a snippet**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#snippet-placement-for-ios) or [**editing it manually**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#option-2-manual-edit-mode).

##### ProGuard File (Android)

The **ProGuard file (`proguard-rules.pro`)** is a configuration file used in Android projects to optimize, shrink, and obfuscate the app’s code. It helps reduce APK or AAB size, improves performance, and protects the app’s code from reverse engineering by making it difficult to decompile.

The ProGuard files allow you to specify rules to keep certain classes or methods (prevent them from being removed or renamed), or to tweak the obfuscation behavior. Located in the **`android/app/proguard-rules.pro`** directory of an Android project, the ProGuard rules are applied when code shrinking is enabled in a release build.

Here are some scenarios where you may need to modify the ProGuard file:

**Example 1: Preventing Issues with Third-Party Libraries**

ProGuard can obfuscate critical libraries, breaking their functionality. To prevent this, you need to keep specific classes used by the library.

```

#### Firebase
-keep class com.google.firebase.** { *; }

### Custom Actions {#custom-actions}

*Learn how to create and use custom actions in your FlutterFlow app to enhance functionality.*

**Source:** https://docs.flutterflow.io/concepts/custom-code/custom-actions

Custom Actions in FlutterFlow differ from custom functions in that they always return a `Future`. This makes them particularly useful for complex operations that may take time to complete, such as querying a database or calling a function that returns results after a delay. Additionally, Custom Actions are beneficial when you want to add a third-party dependency from `pub.dev`, allowing you to extend the capabilities of your application with external packages.

What is a Future?

Futures in **Flutter** represent an asynchronous operation that will return a value or an error at some point in the future. `Future<T>` indicates that the future will eventually provide a value of type `T`. So if your return value is a `String`, then the Custom Action will return a `Future<String>`, and the `String` return value will be output at some point in the future.

#### Key Use Cases

* **Database Queries:** Perform complex queries to retrieve or update data in a database.
* **API Calls:** Make asynchronous HTTP requests to external APIs and handle the responses.
* **File Operations:** Manage file reading or writing operations that require time to complete.
* **Third-Party Integrations:** Incorporate external packages and dependencies to enhance functionality, such as an external analytics package.

#### Using a Custom Action

Once your Action code is finalized, saved, and compiled, you can start using this action as a part of your Action flow.

In the following example, we have a Custom Action called `executeSearch` that takes an argument `searchItem` that is the search string from the search **TextField** of an ecommerce app's `HomePage`.

#### Using the Custom Action Result

In our previous example, we enabled the **Return Value** of the Custom Action to return a `List<Product>` when the search keyword is valid. With this change the code will change from

```
Future executeSearch(String searchItem) async {
  // Add your function code here!
}
```

to

```
Future<List<ProductStruct>> executeSearch(String searchItem) async {
// Add your function code here!
}
```

Let's modify our Action Flow now so we can use the custom action result values within our Action Flow.

LOOKING for other CUSTOM action properties?

To learn more about Custom Action settings, such as the [**Exclude From Compilation toggle**](https://docs.flutterflow.io/concepts/custom-code#exclude-from-compilation), [**Include Build Context toggle**](https://docs.flutterflow.io/concepts/custom-code#include-buildcontext), and other properties like [**Callback Actions**](https://docs.flutterflow.io/concepts/custom-code#callback-action-as-parameter), [**Pubspec Dependencies**](https://docs.flutterflow.io/concepts/custom-code#adding-a-pubspec-dependency), please check out this [**comprehensive guide**](https://docs.flutterflow.io/concepts/custom-code).

---

### Custom Functions {#custom-functions}

*Learn how to create and use custom functions in your FlutterFlow app to add custom functionalities.*

**Source:** https://docs.flutterflow.io/concepts/custom-code/custom-functions

Custom Functions in FlutterFlow allow you to perform simple Dart calculations and logic. These functions are ideal for tasks that require immediate results, such as data transformations, mathematical calculations, or simple logic operations. **Custom Functions** enable you to encapsulate reusable logic, making your code more organized and maintainable. Let's see some common examples:

**To calculate discount given price and discount rate:**

```
double calculateDiscount(double price, double discountRate) {
    return price - (price * discountRate / 100);
}
```

**To capitalize a String input:**

```
String capitalize(String input) {
    return input.isNotEmpty ? '${input[0].toUpperCase()}${input.substring(1)}' : '';
}
```

**To convert Celsius to Fahrenheit**

```
double celsiusToFahrenheit(double celsius) {
    return (celsius * 9/5) + 32;
}
```

#### Key Use Cases

* **Data Transformation:** Convert or manipulate data before displaying it in the UI.
* **Mathematical Calculations:** Perform complex calculations directly within your app.
* **String Manipulation:** Format or parse strings based on specific requirements.
* **Conditional Logic:** Implement logic that determines output based on given inputs.

#### Test Functions

Custom Functions are typically straightforward input-output expressions designed to perform specific tasks. It is highly recommended to test your Custom Functions before integrating them into your project. Testing the Custom Function code ensures that it works as expected with various inputs, helping you catch potential issues early. Overall, it boosts your confidence in shipping your app to production, knowing that your logic is reliable and robust.

LOOKING for other CUSTOM Function properties?

To learn more about Custom Function properties such as [**Input Arguments**](https://docs.flutterflow.io/concepts/custom-code#input-arguments) and **[Return Values](https://docs.flutterflow.io/concepts/custom-code#return-values)**, please check out this [**comprehensive guide**](https://docs.flutterflow.io/concepts/custom-code).

#### FAQs

I can't add imports!

You can't have imports in a custom function. To be able to add imports, consider using a Custom Action.

Getting error: The function 'FFAppState' isn't defined.

You can't use the app state variable (i.e., `FFAppState().variablename`) directly in your custom function code. Instead, you can pass the app state variable as a parameter and then use it in your code.

#### Utility Functions Library

Instead of building everything from scratch, explore our **[Utility Functions Library](https://marketplace.flutterflow.io/item/ZVBmWMGpXe6vqnASRHDA)** — packed with 50+ helpful functions for everyday tasks like formatting text, manipulating dates, validating input, and more. Easily plug them into your custom logic to save time and reduce errors.

---

### Custom Widgets {#custom-widgets}

*Learn how to create and use custom widgets in your FlutterFlow app to enhance its user interface.*

**Source:** https://docs.flutterflow.io/concepts/custom-code/custom-widgets

Custom Widgets allow you to create unique and reusable UI components that extend beyond the standard widget offerings in FlutterFlow. By leveraging Custom Widgets, you can achieve a higher level of customization and control over your app's user interface.

In most cases, you can create a reusable component with the basic widget set available in FlutterFlow. However, when you want to include a UI package from [**pub.dev**](https://pub.dev), **Custom Widgets** are the better choice.

#### Key Use Cases

* **Unique UI Elements:** Create complex UI components that are not available in the default FlutterFlow widget set.

* **Third-Party Integrations:** Integrate external UI packages from pub.dev to enhance the functionality and appearance of your app.

#### Creating a New Custom Widget

To create a new custom widget, add a new Custom Code snippet and follow the quick guide below. In this example, we will create a `ProductRatingBar` widget that uses a pub.dev dependency to display the rating bar UI. It will also take a callback action to provide the rating value back to the caller.

Widget Builder as Parameter

You can also leverage [**Widget Builders**](https://docs.flutterflow.io/resources/ui/components/widget-builder) that allow you to pass in widgets to be used within the custom widget tree. This is especially useful when you want to dynamically substitute content for some part of a custom widget - like displaying an item in a custom widget popup.

##### Properties: Width & Height

For custom widgets, it is mandatory to specify both width and height. These properties are required to size the custom widget appropriately. Without setting these dimensions, the custom widget will not render correctly within your application.

#### Add Dependency to Custom Widgets

In this example, we are using the [**flutter\_rating\_bar**](https://pub.dev/packages/flutter_rating_bar) dependency to create a `ProductRatingBar` widget for our Product pages. See how we utilize the example code from pub.dev and add the customized widget in FlutterFlow:

Choosing a Pubspec Dependency

For a comprehensive guide on navigating external packages using pub.dev, evaluating packages, and making the best choices for your app, [**follow the guide**](https://docs.flutterflow.io/concepts/custom-code#adding-a-pubspec-dependency).

#### Using a Custom Widget

To add a custom widget to your page, you can drag and drop it from the Widget Palette's Components section or through the Widget Tree section. Here is a demo:

##### Providing the Callback Actions

Since we created the `onRating` callback action in our custom widget, we must provide an action when setting the widget in page. In this example, we set the `ratingValue` to the page state variable `userRating`.

#### Preview Widget

FlutterFlow also allows you to view your custom widget once it is successfully compiled.

![preview-custom-widget.avif](https://docs.flutterflow.io/assets/images/preview-custom-widget-14775d4bdaa999a2cdd0a91d2592e70f.avif)

LOOKING for other CUSTOM action properties?

To learn more about Custom Widget settings, such as the [**Exclude From Compilation toggle**](https://docs.flutterflow.io/concepts/custom-code#exclude-from-compilation), and other properties like [**Callback Actions**](https://docs.flutterflow.io/concepts/custom-code#callback-action-as-parameter), [**Pub Dependencies**](https://docs.flutterflow.io/concepts/custom-code#adding-a-pubspec-dependency), please check out this [**comprehensive guide**](https://docs.flutterflow.io/concepts/custom-code).

---

### FlutterFlow Visual Studio Extension {#flutterflow-visual-studio-extension}

*Learn how to leverage the Visual Studio Code Extension to write custom code.*

**Source:** https://docs.flutterflow.io/concepts/custom-code/vscode-extension

The **Visual Studio Code (VSCode) extension** allows you to work with your FlutterFlow project’s custom code directly in [Visual Studio Code](https://code.visualstudio.com/) (a local code editor). This extension facilitates easy editing, pushing, and pulling of custom code changes between FlutterFlow and your local development environment.

While you can edit custom code inside FlutterFlow's in-app code editor, editing the code in Visual Studio Code may be preferable for a few reasons:

1. **Access to the Entire Codebase**: When writing custom code in Visual Studio Code, you'll have full access to your app's entire codebase, making it easier to reference component widget classes, custom data types, enums, and more.

2. **Real-time Autocomplete and Error Detection**: Working on a local machine typically provides more reliable access to real-time error detection and autocomplete features within the code editor, which can make your development process more efficient.

3. **Leverage Flutter & Dart Tooling**: Using Visual Studio Code allows you to take advantage of existing Flutter and Dart tools, making it easier to develop and refactor your custom code.

4. **Leverage the AI Ecosystem**: Additionally, you can easily utilize AI tools available in the Visual Studio ecosystem, such as Copilot.

> **Info:** The VS Code extension is only available on the Growth plan and higher. Check out our [**pricing**](https://www.flutterflow.io/pricing) section.

#### Installation

To fully leverage the Flutter, Dart, and AI tools in Visual Studio Code while editing your FlutterFlow custom code files, you can install the **FlutterFlow: Custom Code Editor** extension. Here are a few easy methods to set it up.

##### Install from Marketplace

You can install the FlutterFlow extension from the [Visual Studio Code marketplace](https://marketplace.visualstudio.com/items?itemName=FlutterFlow.flutterflow-custom-code-editor\&ssr=false#overview) site.

To install the extension directly from Visual Studio Code, open the editor, click on the **Extensions** icon (or press `Ctrl + Shift + X` / `Cmd + Shift + X`), search for "**FlutterFlow: Custom Code Editor**," and click **Install** to add the extension to your workspace.

##### Add API Keys

To use the extension, you must set your **API key** in the editor's **Extension Settings**. You can generate an API key from the [FlutterFlow account page](https://app.flutterflow.io/account) and then add it to the extension settings page in Visual Studio Code. Here’s exactly how you do it:

> **Tip:** You can configure optional settings such as specifying the **Project ID** and **Branch** to pull and update code from. Additionally, you can set a **Download Location** to determine the initial directory where the code will be downloaded.

##### Downloading Code

The first step in editing custom code for your FlutterFlow project is to download its code. To download the code for your project, use the Visual Studio Code command palette (`cmd` + `shift` + `p` or `ctrl` + `shift` + `p`).

In the command palette, you can use the `FlutterFlow: Download Code` command.

This command will prompt you for three pieces of information:

* **Project ID**: This is the Project ID, or unique identifier, for your FlutterFlow project. You can find the Project ID by hovering over the Project Name in the top left corner inside the FlutterFlow builder.
* **Branch Name:** The name of the FlutterFlow project branch you want to work on. You can leave this blank to work on the main branch.
* **Download Location:** A file picker will be presented for you to choose where to download your project code, the code will be downloaded to `thisdirectory`/`projectID`.

##### Initializing a Code Editing Session

After the code has been downloaded, you will need to initiate a **Code Editing** session using the extension. When a Code Editing session has been initiated, you’ll be able to pull and push code from Visual Studio Code to FlutterFlow.

![extension-overview.png](https://docs.flutterflow.io/assets/images/extension-overview-4b40b34eeb52ddca5cde6f841672c3b1.png)

To start a Code Editing session, run the command `FlutterFlow: Start Code Editing Session` from the Visual Studio Code Command Palette. This command will also automatically run `flutter pub get`.

![start-code-edit-session](https://docs.flutterflow.io/assets/images/start-code-edit-session-d3935aed9630b1f8d37de438187e6885.png)

Editing Flutter & Dart Files

It’s recommended that you install the [**Flutter & Dart Extensions**](https://docs.flutter.dev/tools/vs-code) which will make it easier to edit Flutter and Dart code.

#### Editing Custom Code

After successfully [installing](https://docs.flutterflow.io/concepts/custom-code/vscode-extension#installation) the Visual Studio Code extension and [downloading the code](https://docs.flutterflow.io/concepts/custom-code/vscode-extension#downloading-code), you can [initialize your session](https://docs.flutterflow.io/concepts/custom-code/vscode-extension#initializing-a-code-editing-session) to start adding or editing custom code.

Currently, the following resources are available for customization:

* **Custom Actions**
* **Custom Widgets**
* **Custom Functions**
* **Package Dependencies** in `pubspec.yaml`

##### Testing Changes Locally

When working with custom code, it's important to test your implementations. We recommend integrating your Custom Function, Action, or Widget directly within your FlutterFlow project—for example, by adding the Custom Widget to a FlutterFlow Page.

You can then choose to test your app from FlutterFlow, using a [Test Mode session](https://docs.flutterflow.io/testing/run-your-app/#test-mode) or [Local Run](https://docs.flutterflow.io/testing/local-run), or run your app locally from Visual Studio Code.

Before testing from FlutterFlow, ensure you’ve [pushed your changes](https://docs.flutterflow.io/concepts/custom-code/vscode-extension#push-changes-to-flutterflow).

To run your project from Visual Studio Code, make sure the Flutter extension is installed. Once set up, you can simply click the Run (play) button. For further details, refer to [Flutter’s official documentation](https://docs.flutter.dev/tools/vs-code#running-and-debugging).

##### Push Changes to FlutterFlow

To make your custom code available in FlutterFlow, you need to push your changes.

When you push changes, all the files you've edited in Visual Studio Code will be updated in FlutterFlow.

You can see which files have been changed in the **FF: Modified Files section** of the Explorer. This section updates whenever you save a file, showing what has been added, removed, or changed.

![see-modified-files.png](https://docs.flutterflow.io/assets/images/see-modified-files-e757b1b1addfaa784e09bb0bfe13b165.png)

To push changes click the `Push to FlutterFlow` status bar icon, or run the `FlutterFlow: Push to FlutterFlow` command in the command palette.

![push.png](https://docs.flutterflow.io/assets/images/push-9d5f3bd9f958610077043871896911dc.png)

> **Warning:** This action can’t be undone. Make sure you don’t overwrite any changes in FlutterFlow that you want to keep.

To avoid this, pull the latest changes from FlutterFlow before editing in Visual Studio Code, and push your updates once you're done.

##### Pull Latest Changes from FlutterFlow

Before editing any custom files, it's important to pull the latest changes from FlutterFlow into your local repository. This ensures you have the most up-to-date components, app state variables, and custom data types/enums that you might need to reference in your custom code.

To pull the latest changes, click the `Pull Latest` icon in the lower status bar, or run the `FlutterFlow: Pull Latest Changes` command.

![pull.png](https://docs.flutterflow.io/assets/images/pull-e10f259ab4ecab254938ff5b84bfee72.png)

> **Warning:** Pulling changes will also overwrite any local modifications made in the code editor.

#### Updating Files

The VSCode Extension allows you to update **custom code resources**, including entire files or specific Dart/Flutter functions.

For Custom Actions and Custom Widgets, there’s a one-to-one relationship between each action/widget and its corresponding file. If you create a new file in the `lib/custom_code/actions` or `lib/custom_code/widgets` directory, it will automatically add a new action or widget to your FlutterFlow project.

For Custom Functions, all functions are contained within a single file: `lib/flutter_flow/custom_functions.dart`. You can add, edit, or delete custom functions directly within this file.

For Package Dependencies, you can [add new dependencies](https://docs.flutterflow.io/concepts/custom-code/vscode-extension#adding-new-dependencies) in the `pubspec.yaml` file, but you cannot modify the existing ones. When you add a new dependency, it will appear in **Settings and Integrations > Project Dependencies > Custom Code Dependencies** section.

![custom-code-dependencies](https://docs.flutterflow.io/assets/images/custom-code-dependencies-fbaf0813d74afe6e76c14ecfc1093e83.png)

##### Renaming Files

To rename Custom Actions or Custom Widget, use the Visual Studio Code rename symbol functionality. Simply, right-click the name of a Custom Action or Widget and select **Rename Symbol**, then type the new name.

If you change the name without doing this, you’ll need to update the name in the file where the Widget or Action is defined, as well as the index file that exports the Widget (`lib/custom_code/widgets/index.dart`) or Action (`lib/custom_code/actions/index.dart`).

##### Creating New Resource

To add a new Custom Action or Widget, create a new Dart file in the `lib/custom_code/widgets` or `lib/custom_code/actions` directory and the boilerplate should appear within the new file.

To add a new Custom Function, simply create a new Dart function in the `lib/flutter_flow/custom_functions.dart` file. We do not have automatic support for Custom Function boilerplate code in Visual Studio Code at this time.

##### Deleting Files

To delete a Custom Action or Widget, delete the associated file.

##### Adding New Dependencies

You can add custom [pub.dev](https://pub.dev/) package dependencies with the `Dart: Add Dependency` command from the Visual Studio Code command palette. This will update the `pubspec.yaml` file.

#### Using Flutter Version Management (FVM)

If you want to manage Flutter versions with [**Flutter Version Management (FVM)**](https://fvm.app/), you need to install it and add it to your system’s PATH. Follow these steps to get started:

##### Install FVM

To install **FVM**, run the following command in your terminal. This installs FVM globally using Dart’s package manager.

```
dart pub global activate fvm
```

##### Add FVM to Your System’s PATH

After installation, you need to add the directory containing FVM’s executables to your **PATH variable** so that it can be accessed globally.

###### For macOS & Linux

1. Open the Terminal and run the following command. It adds the `~/.pub-cache/bin` directory to your system's `PATH` permanently by updating your `~/.zshrc` file. This ensures that the FVM installed in `~/.pub-cache/bin` is accessible from anywhere in the terminal.

   ```
   echo 'export PATH="$PATH":"$HOME/.pub-cache/bin"' >> ~/.zshrc  # For Zsh
   echo 'export PATH="$PATH":"$HOME/.pub-cache/bin"' >> ~/.bashrc # For Bash
   ```

2. Restart your terminal or run `source ~/.zshrc` (or `source ~/.bashrc`) to apply the changes.

###### For Windows

1. Locate the **FVM executable path**, typically:

   ```
   C:\Users\YourUsername\AppData\Local\Pub\Cache\bin
   ```

2. Add this path to your **System’s PATH variable**:

   1. Open **System Properties** → **Advanced system settings**.
   2. Click **Environment Variables**.
   3. Under **System variables**, select **Path** → **Edit**.
   4. Click **New** and add the above path.
   5. Click **OK** and restart your terminal.

##### Verify the Installation

To check if FVM is correctly installed and accessible, run:

```
fvm --version
```

If this command prints the installed version of FVM, it means FVM is successfully installed and added to PATH.

##### Configure FVM in Your Flutter Project

Once FVM is installed, navigate to your Flutter project folder and set up FVM:

```
cd your-flutterflow-project
fvm init
fvm install <flutter_version>
fvm use <flutter_version>
```

*(Replace `<flutter_version>` with the required Flutter version.)*

#### FAQs

How do I download code from the Beta or Enterprise version of FlutterFlow?

If you're using a different version of FlutterFlow, such as *Beta* or *Enterprise*, you can override the URL by modifying the **Extension Settings > settings.json** file.

For example:

* For the **Beta** version, set the `flutterflow.urlOverride` value to `https://api-beta.flutterflow.io/v1`.
* For the **Enterprise** version, set the `flutterflow.urlOverride` value to `https://api-enterprise-[region].flutterflow.io/v1` (replace \[region] with your specific region).

---

### Design System {#design-system}

*Discover how to create a consistent UI/UX across your app with a design system in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/design-system

A design system is a guideline to create a consistent UI/UX across the app. A design system includes colors, typography, fonts, icons, app assets, a nav bar, an app bar, and pre-designed UI components such as buttons and text widgets.

This is especially helpful when you are working in a team of builders and designers in a large company. Let's say you have an app with several different features and pages, each with its unique design. However, you notice that you are starting to create inconsistencies in the design across different pages, such as using different colors, fonts, and layouts.

To solve this issue, you can create a design system outlining common design guidelines. Then, the team members can use this design system, which ensures the design remains consistent.

[Sharing a Project with a User](https://www.youtube.com/embed/moP9VtkoyjY)

#### Adding Design System

You can add a design system from the [Library](https://docs.flutterflow.io/resources/projects/libraries) dependencies added to your project. A library can serve as a central repository for your design assets, components, and styles—effectively becoming a Design Library for your application(s).

possible use cases

* **Enterprise Applications:** Large organizations can develop a centralized design system as a library to ensure all internal applications maintain a cohesive look and feel, enhancing brand identity and user experience.
* **Startup MVPs:** Startups can expedite the development of Minimum Viable Products (MVPs) by leveraging a pre-built design system library like [**shadcn**](https://marketplace.flutterflow.io/item/cNlm0zWW1Nfq11cFXBmp), allowing them to focus on functionality and user validation.
* **Cross-Platform Consistency:** Teams aiming to deploy apps across multiple platforms (iOS, Android, Web) can use a popular platform based design system library to ensure uniformity in design, reducing the effort required for platform-specific adjustments.

To add a design system from a library, start by creating the design system in a new FlutterFlow project and [publishing it as a library](https://docs.flutterflow.io/resources/projects/libraries#publishing-a-library). Next, [import](https://docs.flutterflow.io/resources/projects/libraries#importing-a-library) that library into the project where you want to use the design system. Then, navigate to **Theme Settings > Design System** and click **No Design System Selected**. From the dropdown that appears, **Select a library** you’ve just imported to apply its design system to your project.

#### Import Figma Theme

You can bring your Figma design system directly into your FlutterFlow project. This streamlines the design-to-development process by automatically importing colors and typography from your Figma file, helping you maintain visual consistency and reduce manual effort.

To import a Figma theme into your FlutterFlow project, go to **Theme Settings > Design System** and click **Connect To Figma**. Authenticate your account and grant access to Figma. Once connected, paste your Figma file URL to fetch the theme.

You’ll see a list of all imported colors; start mapping them to your project colors. You can filter these colors by whether they’re mapped or unmapped, and you also have the option to bulk delete any imported colors. After that, you can customize your project typography using the imported text styles.

> **Info:** All imported colors are accessible anytime under **Colors > Custom Colors**.

[Sharing a Project with a User](https://demo.arcade.software/84lqVC1ZDkq7EFFnCusm?embed\&show_copy_link=true)

If you prefer watching a video tutorial, here is the guide for you:

[Sharing a Project with a User](https://www.youtube.com/embed/kWvWa5PSWhw)

***

#### Loading Indicators

To customize the **Loading Indicators** used in the app, you can make changes in this section. You have the option to specify the **Indicator Type**, **Color**, and **Radius**, and the preview of the changes will be displayed below.

[Sharing a Project with a User](https://demo.arcade.software/6OiSlYPiCEY1p3fg0kpG?embed\&show_copy_link=true)

> **Tip:** Avoid mis-sized loading indicators or components, which lead to jumping layouts. Ensure loading components match the size and position of the content they replace.

If you prefer watching a video tutorial, here is the guide for you:

[Sharing a Project with a User](https://www.youtube.com/embed/3sG-O1lkv0M)

***

#### Scrollbar Theme

From here, you can customize the appearance of the scrollbar that shows up on scrollable elements like ListView, GridView, StaggeredView, Row, and Column.

> **Note:** The scrollbar currently shows up by default only on platforms where Flutter natively supports it, such as web and desktop environments.

You can modify its color, adjust its thickness, give it a rounded border, and more. In the 'Preview' section, you'll also be able to see the immediate visual effect of your changes.

Here are all the properties you can customize:

1. **Thumb Color:** This changes the color of the draggable portion of the scrollbar, often called the "thumb".

   ![thumb-color](https://docs.flutterflow.io/assets/images/thumb-color-bfd24701e544df03230cdec7f59dc6c2.avif)

2. **Thickness:** This increases width (in a vertical scrollbar) or height (in a horizontal scrollbar).

   ![thickness](https://docs.flutterflow.io/assets/images/thickness-e92ffc854e7214cf4e6fd84c946acb2b.avif)

3. **Border Radius:** This sets the curvature of the scrollbar's corners. By adjusting the border-radius, you can give the scrollbar a more rounded appearance (higher values) or a more squared appearance (lower values).

   ![border-radius](https://docs.flutterflow.io/assets/images/border-radius-2c41be300659fafb6f852df4df63de3a.avif)

4. **Min Thumb Length:** This refers to the smallest size that the draggable portion (thumb) of a scrollbar can be. This ensures that users can always see and interact with the thumb, even when the content is very long.

   ![min-thumb-length](https://docs.flutterflow.io/assets/images/min-thumb-length-7c35793294a21ba25b9092cadc1c6010.avif)

5. **Main Axis Margin:** This refers to the space or gap along the primary direction of the scrollbar. For instance, in a vertically scrolling list, it refers to the top and bottom spacing, and in a horizontally scrolling list, it refers to the left and right spacing.

   ![main-axis-margin](https://docs.flutterflow.io/assets/images/main-axis-margin-a8bb16785cca8391f53b0d75a7186802.avif)

6. **Cross Axis Margin:** This refers to the space or gap along the cross direction of the scrollbar. For instance, in a vertically scrolling list, it refers to the left and right spacing, and in a horizontally scrolling list, it refers to the top and bottom spacing.

   ![cross-axis-margin](https://docs.flutterflow.io/assets/images/cross-axis-margin-53328bce34a6c1272ee4b41bcd5771dc.avif)

7. **Thumb Always Visible:** This determines whether the draggable "thumb" element of the scrollbar constantly remains visible or fades out when not in use. When enabled, you can also specify whether to show the track as well with custom color and border color.

8. **Interactive**: Using this property, you can set different colors for different states of the thumb, including when it's hovered over or being dragged.

   ![interactive](https://docs.flutterflow.io/assets/images/interactive-0737de8ab3ff2050e4cfb129b96d39b8.gif)

***

#### Pull to Refresh Style

From here, you can customize the appearance of the pull to refresh (i.e., the loading circle).

You can modify its color, background color, and stroke width. In the 'Preview' section, you'll also be able to see the immediate visual effect of your changes.

[Sharing a Project with a User](https://demo.arcade.software/KHdvetH4Eg46TfDmZQUJ?embed\&show_copy_link=true)

#### Colors

This section allows you to customize the colors of your app, giving you control over the visual appearance of your application. From here, you can configure colors for both light and dark themes. Additionally, you can preview existing theme colors, import colors from Coolors, and even extract colors from images.

##### Add or replace color

By default, we add 16 predefined colors for light and dark themes. However, you might want to add a new color or replace the existing color to align better with your brand identity.

To add a new color:

1. Click **Add Color** button.
2. The new color will be added as **Custom Color.** Click on it and enter the [Hex color value](https://www.w3schools.com/colors/colors_hexadecimal.asp).
3. You can also edit the name of the custom color.
4. Click **Use Color**.

To update an existing color in a light and dark mode theme, click on the color and enter the hex color value.

##### Explore Project Colors

We allow you to browse through the commonly used colors in your app and some pre-defined color schemes that might align with your app branding.

To do so:

1. Click on the **Explore Project Colors**.
2. **Select page** you want to preview.
3. To find common colors, scroll down and click **Find Common Colors**. This will list out all the colors being used in the app. Use the 'done' and 'cancel' icons to accept or reject colors.
4. To explore the pre-defined color schemes, switch to the **Explore** tab, scroll through all the schemes, and tick to see the preview.
5. Click the 'refresh' button to get back to the original theme.
6. To proceed further, click **Save Changes**.

##### Import from Coolors

Importing colors from [Coolors](https://coolors.co/) website is a quick and easy way to add your preferred color scheme to your app. Coolors offers a vast library of color palettes that you can import with just a few clicks, saving you time and effort in creating your own custom color palette.

To import from Coolors:

1. Go to the [coolors.co](https://coolors.co/palettes/trending), identify the palette you would like to add, click on the **options menu** (three dots), and then click on the **Export palette**.
2. Now, select the **Code**, and then copy the contents below the `/* Object */` section.
3. Open your project, and navigate to **Theme Settings > Colors**.
4. Click on the **Import from Coolors** button. This will open a new popup window.
5. Paste the copied content and then click **Import**. New colors will be displayed under the **Custom Colors** section.

##### Extract from Image

This feature provides an easy way to create visually striking themes by utilizing the colors present in an image. You can generate a color palette that harmonizes perfectly with the colors in the image, resulting in stunning designs that capture the essence of your image.

To extract and use color from the image:

1. Navigate to **Theme Settings > Colors**.
2. Click the **Extract from Image** button and select the image.
3. A pop-up will appear that displays the extracted color from the image. To proceed further, click **Extract & Continue**.
4. In the next step, click on any color to see and select the extracted color.
5. Click **Done**.

##### AI Generated Theme Colors

With 'AI Gen Theme,' simply describe the desired color theme for your app, such as 'Tiger in the Jungle' or 'Kids bedtime story,' and watch as a comprehensive color scheme tailored to your needs magically appears.

##### Video guide

If you prefer watching a video tutorial, here's the one for you:

#### Typography & Icons

This section puts you in complete control of your app's text styling. With options to add responsive and custom fonts, you can ensure your app looks unique and consistent across all screen sizes. Moreover, you can also add custom icons to your app, allowing you to create unique and visually appealing user interfaces.

##### Define Text Styles (Typography/Fonts)

To change the font family at the project level, open the **Theme Settings** (from the navigation menu) **> Typography & Icons**, click on the button below the **Primary Font Family** or **Secondary Font Family,** and search and select the new font.

> **Info:** The *Primary Font Family* is the font that you will use the most throughout your app. The *Secondary Font Family* is the font that you will use to serve slight variation or contrast to the primary font.

You can customize the following properties of each text style:

* **Font Size** - Use this to specify the size of the text.
* **Letter Spacing** - Use this to set the space between characters.
* **Italic** - Checkbox for enabling *Italic* font style.
* **Font Weight** Choose the font weight among *Thin, Extra Light, Light, Normal, Medium, Semi Bold, Bold, Extra Bold & Black*.
* **Color** - Set the color of the text using either the color picker or by specifying a Hex value.
* **Font Family** - You can change the Font Family for any style from here. Click here to set the font family from [*Google Fonts*](https://fonts.google.com/) or choose from the uploaded Custom Fonts. You can also choose whether this style is a *Primary* or *Secondary Font Family*.

You can also create fully custom text styles to match your design needs, going beyond the default styles like Display, Headline, or Title. Simply click the **+ Add Custom Text Style** button, a new text style will be added at the bottom, then edit the style name and customize the style properties.

![typography](https://docs.flutterflow.io/assets/images/typography-94af7225f1856e4d9f5de6f0ede5d83a.avif)

PLANS

Custom Text Styles are available on the **Business** plan and higher. Check our [**pricing plans**](https://flutterflow.io/pricing).

###### Adding responsive text styles

When developing a mobile app, it's important to consider the different platforms on which it will run. You might notice that the text looks smaller on platforms with higher screen resolution, such as tablets, web, or desktops. This can impact the user experience and make your app difficult to read. To solve this issue, you can add responsive text that adjusts the font size based on the platform.

See how the texts are displayed with and without responsive font style:

* With responsive Text
* Without responsive text

![with-responsive-text](https://docs.flutterflow.io/assets/images/with-responsive-text-e92f3ca8860018d5c26a5adf95ede1cf.avif)

![without-responsive-text](https://docs.flutterflow.io/assets/images/without-responsive-text-58150c933c57c50652d32bed6fbb01cf.avif)

You can add the responsive style by following the instructions below:

1. Open the **Theme Settings** (from navigation menu) **> Typography & Icons**.
2. Click on the **Make Responsive** button.
3. Now, all the styles are available under the three tabs. *Mobile*, *Tablet*, and *Desktop*. Modify each style under the different platform tabs that you are supporting.
4. Run the app and see how the texts are displayed by changing the platform.

##### Custom Fonts

Adding Custom Fonts to your app makes it stand out from others. This section allows you to upload your own fonts. You can upload the custom font files of types `.ttf`, `.otf`, and `.woff.` Once the font is uploaded, you can use it directly from the widget or add it to the text style section to create a general theme.

> **Info:** Before you upload the Custom Fonts, make sure you have permission to use the font in your application.

To add the *Custom Fonts*:

1. Open the **Theme Settings** (from navigation menu) **> Typography & Icons**.
2. Scroll down to the **Custom Fonts** section.
3. Click on the **+ Add Font** button.
4. Enter the **Font Family Name** and click the **Upload File(s)** button.
5. Select and upload your font.
6. Click **Add Font**. The newly added font will be displayed.
7. To use a custom font directly in a widget, move to the property panel, click on the already applied font family, select the **Custom Fonts** tab, and then choose the font.
8. To use a custom font for a common text style, open the Text Styles section, click on the already applied font family, select the **Custom Fonts** tab, and then choose the font.

If you prefer watching a video tutorial, here's the one for you:

##### Custom Icons

Custom icons help reinforce your brand identity and add a unique touch to your app. Before uploading icons to FlutterFlow, you’ll first need to generate them using an icon font generator like [FlutterIcon](https://www.fluttericon.com/) or [IcoMoon](https://icomoon.io/).

We’ve also built our **[own SVG to Custom Icon Generator](https://icons.flutterflow.app)** to make the process even easier — feel free to use that instead.

> **Info:** Make sure you have the proper rights or licenses to use the icons in your application.

**Steps to Generate and Add Custom Icons**

1. Head over to the [IcoMoon](https://icomoon.io/app/#/select).
2. Import your custom icon (.svg) or select from the free icons set.
3. Select the **Generate Font** tab.
4. Click on the Settings button (gear icon) beside the download text on the bottom right side.
5. Enable **Generate Dart class for Flutter**.
6. Click on the **Download** button and then extract the downloaded file.

7) Open your FlutterFlow project, navigate to the **Theme Settings** (from navigation menu) **> Typography & Icons**.
8) Scroll down to the **Custom Icons** section.
9) Click on the **+ Add Icons** button.
10) Click on the **Upload Icon File** button.
11) Select and upload `.ttf` file under the downloaded folder > fonts.
12) Now click on the **Upload Icon Info** button.
13) Select and upload the `filename.dart` under the downloaded folder (besides the fonts folder).
14) Click **Add Icons**.

###### Use the Custom Icon

To use a custom icon, add the **Icon** widget, move to the properties panel, and scroll down to the **Icon** section. Click on the already selected icon, select the **Custom Icons** tab, and then select your icon.

If you prefer watching a video tutorial, here is the guide for you:

#### Theme Widgets

Creating a theme for widgets ensures that your app looks consistent and has a cohesive design. The Theme widgets can be reused, making it easy to update the styles of your app. If you decide to change any property of the widget, such as color scheme or fonts, you can update the theme widget instead of going through every widget individually. This can save a lot of time and effort, especially in larger projects.

For example, creating theme widgets for different types of buttons such as 'primary\_button', 'secondary\_button', and 'tertiary\_button' with specific attributes like width, color, icon, border radius, and padding. Then, these widgets can be directly added to a page or applied to an existing widget.

##### Adding theme widgets

To add a theme widget to your app, you must create it and then use it on your page by dragging it from the Widget Palette or applying it to the existing widget.

Here's how you do it:

1. Open the **Theme Settings** (from the navigation menu) > **Theme Widgets**.
2. Click **Create Widget** button.
3. Enter the **Theme Widget Name** and then select the widget.
4. Create a theme for the widget using its properties available on the right side and then click **Save**.

5) You can also make any widget a theme widget by right-clicking and selecting **Save as Theme Style Widget**.

6. Now, you can add this widget directly from the widget tree or Widget Palette.

7) To apply this widget styling to an existing widget, select the widget, move the **Properties Panel > Widget Styling >** click **Theme Style Unset >** select the theme widget.

> **Warning:** After applying theme widget styling, any previously set properties will be overridden except the properties with *Set from Variable*. However, you are free to modify the existing widget properties as you like.

##### Video guide

If you prefer watching a video tutorial, here's the one for you:

#### FAQs

How is the theme widget different from creating a template and component?

The Theme Widget allows you to customize the visual appearance of a single widget, whereas templates consist of multiple widgets that create a unique UI layout with a specific purpose. On the other hand, components are fully-featured custom widgets that combine multiple widgets and actions to complete a task.

---

### File Handling {#file-handling}

*Learn how to handle media files in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/file-handling

FlutterFlow makes it easy to manage, upload, download, and display files within your app. It supports a variety of file types, including images, videos, and documents, and integrates seamlessly with popular storage solutions. Using built-in widgets and actions, you can effectively manage your app's media. This guide covers the following key aspects of file handling in FlutterFlow.

* **Media Assets**: Upload any assets you want to use in your app from the Navigation Menu > Media Assets. This also shows the media assets of the Team.
* [**Uploading Files**](https://docs.flutterflow.io/concepts/file-handling/uploading-files): Upload and save different file types, including images, audio, videos, and PDFs to cloud storage.
* [**Displaying Media**](https://docs.flutterflow.io/concepts/file-handling/displaying-media): Fetch files from cloud storage or external URLs and display them in your app.
* [**Download Files**](https://docs.flutterflow.io/concepts/file-handling/download-file): Allow users to download files directly to their devices.
* [**Clear or Delete Media**](https://docs.flutterflow.io/concepts/file-handling/clear-delete-media): Allow users to delete uploaded files from their devices and cloud storage.

Also see

* **Stream Media with Mux**: [**Integrate Mux's broadcasting**](https://docs.flutterflow.io/integrations/mux) services in FlutterFlow by using the MuxBroadcast widget for live streaming.
* **Request Permissions**: [**Request user permissions**](https://docs.flutterflow.io/resources/projects/settings/project-setup#request-permission-action) when implementing custom widgets or actions that access personal information, such as capturing photos or selecting images, especially if no built-in permission mechanism is available.

---

### Clear or Delete Media {#clear-or-delete-media}

*Learn how to add clear and delete file actions into your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/file-handling/clear-delete-media

The **Clear** and **Delete** **Media** actions provide essential functionalities for managing media files efficiently.

#### Clear Uploaded Data \[Action]

When users upload media files, these files are first stored in a local state variable, i.e., *Uploaded File URL* for immediate access and display. This action is helpful when you want to offer users a straightforward method to remove any uploaded media, such as images or recordings.

> **Info:** For this action to work, the [**Upload or Save Media**](https://docs.flutterflow.io/concepts/file-handling/uploading-files#upload-or-save-media-action) action must already be added to the actions workflow.

#### Delete Data \[Action]

The **Delete Data** action permanently removes uploaded media—such as images, videos, and PDF files—from external storage platforms like [Firebase Storage](https://firebase.google.com/docs/storage) and [Supabase Storage](https://supabase.com/storage).

Inside the **URL** section, provide a valid media URL. This must be either the direct **Uploaded File URL** or a variable that holds the URL.

> **Tip:** Always prompt users for confirmation before deleting media files to prevent accidental loss of data.

---

### Displaying Media {#displaying-media}

*Learn how to display media in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/file-handling/displaying-media

Displaying media efficiently is crucial for enhancing user experience in your FlutterFlow app. Whether you're working with images, audio, video, or PDFs, FlutterFlow provides flexible options for integrating and managing media. This guide covers how to set media sources, customize playback settings, and implement best practices like lazy loading, caching, and BlurHash to optimize performance.

#### Media Types

To display media on widgets, navigate to the **Properties Panel** and specify the media source under the **\[Media] Type** option (e.g., ImageType, AudioType, VideoType). Here are the available options:

##### Network

Enter the URL of the media directly into the **Path** input field. This is for media hosted online.

![dm-network-path.avif](https://docs.flutterflow.io/assets/images/dm-network-path-b78e3f6052ed5884abf91f49e0ba4c1f.avif)

If your media is uploaded to Firebase or Supabase, click **Set from Variable** on the **Path** input field, and select **Source** as **Widget State > Uploaded File URL**.

![dm-uploaded-file.avif](https://docs.flutterflow.io/assets/images/dm-uploaded-file-17833124a8c84bf658089bedabff8bcb.avif)

For media uploaded via an API, choose **Source** as **Action Outputs > \[Action Output Variable Name] (API Response)**. Ensure that the API response contains the URL of the uploaded file. Learn how to extract the URL using [JSON path](https://docs.flutterflow.io/resources/backend-logic/rest-api#json-path).

![dm-api.avif](https://docs.flutterflow.io/assets/images/dm-api-266ac1624c53096b9476c369636e9f15.avif)

> **Info:** To handle scenarios where media takes time to load or fails to load, you can set a placeholder. Click **Set from Variable** on the **Path** field and specify a placeholder URL under the **Default Value** property.

##### Asset

You can also display media files uploaded to your **Assets**. Assets are resources such as images, videos, documents, fonts, and other files that you include locally in your project. To upload assets, click on **Media Assets** in the left-side navigation menu and add files directly from your device. Alternatively, you can directly upload and display files when configuring media widgets by clicking the upload icon.

> **Tip:** For more details on how assets are stored in your project, see the directory [**Assets**](https://docs.flutterflow.io/generated-code/project-structure#assets) in the generated code.

![select-from-assets](https://docs.flutterflow.io/assets/images/select-from-assets-28f9446ec024836e64cb61fab0d1d70a.avif)

##### Uploaded File

You can also access media files within your app that are stored temporarily in your application. For example, if you'd like to preview an image before sending it to cloud storage, you can do so by setting the source to **Widget State -> Uploaded Local File**.

![dm-local-upload.avif](https://docs.flutterflow.io/assets/images/dm-local-upload-382c03139589aff098665200c4febdc2.avif)

#### AudioPlayer

The **AudioPlayer** widget allows you to integrate audio playback into your apps. You can play audio from both uploaded assets and external URLs. Refer to the [**Displaying Media**](https://docs.flutterflow.io/concepts/file-handling/displaying-media#media-types) section for more details on accessing media.

Generated Code

The AudioPlayer widget in FlutterFlow uses the [**assets\_audio\_player**](https://pub.dev/packages/assets_audio_player) package for audio playback.

**Customization Options**

* **Title:** Specify the audio title in the **Title** property. You can set this directly or bind it to a variable, such as an app state variable, API response, or Firestore document.

* **Pause on Forward Navigation:** By default, the audio stops when navigating to another page.

* **Play in Background:** Define how the audio behaves when the app moves to the background: * **Enabled:** The audio continues to play.
  * **Disabled, restore on foreground:** The audio pauses and resumes when the app becomes active again.
  * **Disabled, pause:** The audio stops immediately when the app goes into the background.

* **Colors:**

  * **Background Color:** Customize the background using the **Fill Color** property.
  * **Playback Button Color:** Adjust the colors of the play and pause buttons.
  * **Active/Inactive Track Color:** Change the progress bar color that indicates the current playback position.

* **Elevation:** Use the **Elevation** property to modify the shadow beneath the audio tile. A higher value increases the shadow size, while setting it to 0 removes the shadow.

* **Text Styling:**

  * **Title Text:** Personalize the title’s font, size, and color in the **Title Text Style** section.
  * **Playback Duration Text:** Adjust the style of the playback duration text in the **Playback Duration Text Style** section.

#### Audio Recording

You can implement audio recording functionality using the **Start Audio Recording** and **Stop Audio Recording** actions.

> **Warning:** Currently, audio recording is not supported in **Run** or **Test** modes due to certain limitations.

##### Start Audio Recording \[Action]

This action starts the recording. It also provides a name to the recording, which you can use later to stop the recording using the [Stop Audio Recording](https://docs.flutterflow.io/concepts/file-handling/displaying-media#stop-audio-recording-action) *action.*

Before adding this action, ensure you [request microphone permission](https://docs.flutterflow.io/resources/projects/settings/project-setup#request-permission-action). Within the **TRUE** block of the permission condition check, add the **Start Audio Recording** action. By default, the **Name** field value is a randomly generated string. You can change it to a more descriptive name for easier identification.

> **Tip:** After starting recording, you might want to update the state variables to reflect changes on the UI. For instance, you can enable/disable buttons or start recording animations to provide a visual cue of the ongoing process. This step allows you to enhance the user experience and provide real-time feedback during the recording.

![start-audio-recording.avif](https://docs.flutterflow.io/assets/images/start-audio-recording-061566456f74b9bcd7abc36d2d21fb1f.avif)

##### Stop Audio Recording \[Action]

If you have multiple audio recording actions, all the Recorder object names (either auto-generated by FlutterFlow or manually set by the user) are listed under the Recorder Name dropdown. Choose the recorder object you want to stop, and it will stop the ongoing recording.

To capture and play the recorded audio, make sure to specify the *Action Output Variable Name*, which can be used with the audio player.

Here’s how you can setup this action:

1. When you add this action, choose the **Recorder Name** from the dropdown. This will be the name you provided in the Start Audio Recording action.

2. Specify the **Action Output Variable Name**. This will store the actual audio recording, which you can use with any audio player. It stores recording in an **Audio Path** data type.

3. If you want to upload the audio recording to Firebase or Supabase, you can use the [Upload file](https://docs.flutterflow.io/concepts/file-handling/uploading-files#upload-or-save-media-action) action. When you add this action: 1. Set the **Upload Type** to the preferred one.
   2. Set **File Type** to **Uploaded File** because the *Stop Audio Recording* action internally stores recorded audio bytes (inside widget state).
   3. Set the **File to Upload** to **Widget State > Recorded File**.

4. For uploading via API, *you don't need to add the Upload file action*. Just directly add the [**API call**](https://docs.flutterflow.io/resources/backend-logic/rest-api) and select the API that will upload the file to your server. **Note** that the request body for this API must be in *Multipart* format. You can pass the audio recording via **Widget State > Recorded File** in the API variable. See how to [configure an API for the multipart request body](https://docs.flutterflow.io/resources/backend-logic/rest-api#multipart-format).

> **Tip:** * After stopping the recording, you might want to update the state variables to reflect changes on the UI. For instance, you can enable/disable buttons or stop recording animations.
* It's always a good idea to have a fail-safe mechanism to ensure recordings are properly stopped, even if the user forgets to do so manually. For example, you can use the [**On Dispose**](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#on-dispose-action-trigger) action trigger to stop recording when a user closes the app without manually stopping it.

##### Playing audio recording

After you have stopped the recording, you can simply provide the *Action Output Variable Name* to the [Audio Player](https://docs.flutterflow.io/concepts/file-handling/displaying-media#audioplayer) widget to start playing the recorded audio.

#### Play or Stop Sound

The **Play Sound** and **Stop Sound** actions offer flexibility for enhancing the user experience with audio effects or background sounds.

##### Play Sound \[Action]

The **Play Sound Action** allows you to play a sound that notifies users about the action they have taken—for example, playing a sound after refreshing a list or sending a message.

> **Tip:** It is advisable to use this action only for short audio. To play the more extended audio, consider adding the [**AudioPlayer**](https://docs.flutterflow.io/concepts/file-handling/displaying-media#audioplayer) widget.

By default, this action is assigned a random **Name** to be stopped later using the [Stop Sound](https://docs.flutterflow.io/concepts/file-handling/displaying-media#stop-sound-action) action. You can adjust the volume using the **Volume** slider (0.0 = mute, 1.0 = full volume). The action is non-blocking by default, allowing subsequent actions to trigger immediately. To wait until playback finishes before proceeding, enable the **Await Playback** option.

Use cases

* **Feedback Sounds:** Play sounds for button clicks, form submissions, or error alerts to improve user interaction and feedback.
* **Notifications:** Play sound alerts for reminders, messages, or task completion.
* **Gamification:** Enhance gaming experiences with sound effects for achievements, levels, or interactions.

##### Stop Sound \[Action]

You can stop a sound that is currently playing, which was started by the [Play Sound](https://docs.flutterflow.io/concepts/file-handling/displaying-media#play-sound-action) action. For example, If your app is playing any sound effects, you may need to stop them when the app is paused or stopped.

> **Info:** This action is enabled only when you have added a [**Play Sound**](https://docs.flutterflow.io/concepts/file-handling/displaying-media#play-sound-action) action on a page.

#### VideoPlayer

The **VideoPlayer** widget is used to show a video from uploaded assets or the URL link. The VideoPlayer widget can play various video formats such as MP4, MOV, WAV, MPEG, and JPEG motion photos. Refer to the [**Displaying Media**](https://docs.flutterflow.io/concepts/file-handling/displaying-media#media-types) section for more details on accessing media.

Generated Code

The VideoPlayer uses the [**video\_player**](https://pub.dev/packages/video_player) package for reliable video playback across different platforms.

**Customization Options**

The **VideoPlayer** widget includes several options to align with your app's design and functionality:

* **Aspect Ratio:** Set the desired aspect ratio (e.g., 1.7 for a 16:9 ratio) to ensure the video displays correctly.
* **AutoPlay:** Enable this option to automatically start playing the video when the page loads.
* **Loop Video:** Choose whether the video should replay automatically after it ends.
* **Show Controls:** Display playback controls, including play/pause buttons and the seek bar.
* **Allow Full Screen:** Enable users to expand the video to full-screen mode.
* **Playback Speed Menu:** Let users adjust the video playback speed.
* **Load on Page Load:** When enabled, the video will preload when the page loads, reducing buffering time when the user starts playback.
* **Pause on Forward Navigation:** If enabled, the video will pause automatically when the user navigates away from the page.

#### YoutubePlayer

The **YouTubePlayer** widget in FlutterFlow allows you to integrate and play YouTube videos within your app. It offers customizable playback options and an intuitive interface for enhancing the user experience.

Generated Code

The YoutubePlayer uses a custom version of the [**youtube\_player\_iframe**](https://pub.dev/packages/youtube_player_iframe) package, hosted on FlutterFlow's GitHub repository.

**Customization Options**

* **Loop Video:** When enabled, the video will automatically replay after it finishes.
* **Mute Video:** Starts the video in a muted state.
* **Show Controls:** Displays playback controls such as play/pause, volume, subtitles, and fullscreen options.
* **Show Full Screen Control:** This specifically displays the fullscreen toggle button among the controls.
* **Pause on Forward Navigation:** Automatically pauses the video when the user navigates away from the page.
* **Strict Related Videos:** Ensures that related videos shown at the end of playback come from the same channel as the currently played video.

#### PdfViewer

In FlutterFlow, the **PdfViewer** widget enables you to display PDF files within your app, supporting both network URLs and locally uploaded assets. Refer to the [**Displaying Media**](https://docs.flutterflow.io/concepts/file-handling/displaying-media#media-types) section for more details.

Generated Code

The PdfViewer in FlutterFlow uses the [**pdfx**](https://pub.dev/packages/pdfx) package for rendering PDFs.

**Customization Options**

* **Horizontal Scroll:** By default, the PdfViewer allows vertical scrolling through pages. Enable this option to allow horizontal scrolling.
* **Use Proxy:** By default, FlutterFlow routes PDF fetching through a proxy in **Run Mode** and **Test Mode** to avoid CORS (Cross-Origin Resource Sharing) issues. **Switch this off** if you do not want the PDF request to be routed through the proxy.
* **Use Custom Proxy URL:** If you need a specific proxy, enable this option and provide your own proxy URL instead of using FlutterFlow’s default proxy.

#### Web Access for PDFs and Other Files

Some types of files require additional configuration to be accessed on the web. In particular, the PDF Viewer requires network-hosted files (such as uploaded PDFs) to allow Cross-Origin Resource Sharing (CORS). For a deeper understanding of Cross-Origin Resource Sharing (CORS), you can refer to this guide.

The key takeaway is that to allow users to upload and view PDFs using Firebase Storage, follow the steps below.

You'll need to run a few commands to enable CORS for your Firebase project. No programming experience is required, but if you're comfortable with Firebase, you can refer to the official guide here: [Firebase CORS Configuration](https://firebase.google.com/docs/storage/web/download-files#cors_configuration).

**Step 1: Find Your Firebase Project ID**

You can find the Firebase project ID from **FlutterFlow > Settings and Integrations > Firebase**. Copy your **Firebase** **Project ID**.

![copy-firebase-project-id.avif](https://docs.flutterflow.io/assets/images/copy-firebase-project-id-8d7691404188fe706b09cf96b1a0c471.avif)

**Step 2: Open Cloud Shell in Google Cloud Console**

1. Go to the following link, replacing **FIREBASE\_PROJECT\_ID** with your actual project ID:

```
https://console.cloud.google.com/home/dashboard?cloudshell=true&project=FIREBASE_PROJECT_ID
```

1. If prompted, click **Continue**.
2. You should see a terminal at the bottom of the screen. If your project ID is not displayed in yellow, click the **down arrow** (🔽) next to the project name and select the correct Firebase project.

![cloud-shell](https://docs.flutterflow.io/assets/images/cloud-shell-2cfa3917b0d0c7a1d67f607c32776a87.avif)

**Step 3: Run the CORS Configuration Command**

1. Click on the **Cloud Shell terminal** (the black screen).
2. Copy and paste the following command and replace `<your-cloud-storage-bucket>` with your actual storage bucket. To locate your Firebase Storage bucket name, navigate to Firebase Console > Storage > at top left side, you'll see your bucket's URL, which typically follows the format `your-project-id.appspot.com`.

```
touch cors.json && \
echo '[{"origin": ["*"], "method": ["GET"], "maxAgeSeconds": 3600}]' > cors.json && \
gsutil cors set cors.json gs://<your-cloud-storage-bucket>
```

![storage-bucket.avif](https://docs.flutterflow.io/assets/images/storage-bucket-2a38c52febd3dfc98c9b5ef68b90a86d.avif)

3. Press **Enter** (or **Return**) to execute the command.
4. If prompted, click **Authorize** to allow Cloud Shell to access your Firebase project.
5. Once the command executes successfully, you should see a confirmation message.

![cors-3](https://docs.flutterflow.io/assets/images/cors-3-59c800255b68c5e2f05da6b7ec2e748b.png)

#### BlurHash

In FlutterFlow, **BlurHash** is a technique used to enhance the user experience by displaying visually appealing placeholders while images are loading. Instead of showing empty spaces or generic loading indicators, BlurHash generates a blurred preview that resembles the actual image, providing users with a smoother and more engaging experience.

![blurhash.avif](https://docs.flutterflow.io/assets/images/blurhash-0048ec5ea8985f9d4315c0af8f6003bb.avif)

Here are the steps to generate and use the BlurHash:

1. When using the [**Upload/Save Media**](https://docs.flutterflow.io/concepts/file-handling/uploading-files#upload-or-save-media-action) action to upload images, you can enable the **Include Blur Hash** option. This setting automatically generates a BlurHash string for the uploaded image.

![enable-blurhash.avif](https://docs.flutterflow.io/assets/images/enable-blurhash-5eaf03e450524845bce4c0ee4d7a8d6b.avif)

1. After generating the BlurHash, it's advisable to store it alongside the image URL in your database (e.g., Firestore). The generated BlurHash is accessible via the **Widget State > Uploaded Local File > Media Blur Hash**. This approach ensures that both the image URL and its corresponding BlurHash are readily accessible when needed.

![save-blurhash.avif](https://docs.flutterflow.io/assets/images/save-blurhash-0a1b9edfce912604c4e320cffbd80525.avif)

1. To utilize the BlurHash as a placeholder, in the Image widget's properties, enable the **Use Blur Hash** option and then set the **Blur Hash String** value from a variable.

![use-blurhash.avif](https://docs.flutterflow.io/assets/images/use-blurhash-5eb017934e37e5f292dc0e0693ca198a.avif)

#### Best Practices

* Enable [infinite scrolling](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#adding-infinite-scroll) (lazy loading) in list views to load additional content as users scroll, rather than loading all data at once.
* Leverage FlutterFlow's built-in cache manager, which automatically handles image caching.
* Implement [local caching](https://docs.flutterflow.io/resources/backend-query#backend-query-caching) to store frequently accessed data on the device, reducing the need for repeated network requests.
* Reduce the number of network calls by fetching only necessary data and utilizing caching strategies.
* Ensure that database queries are efficient and retrieve only the data required for display.
* Use [BlurHash](https://docs.flutterflow.io/concepts/file-handling/displaying-media#blurhash) to display a blurred preview of images while they load, enhancing the user experience.
* Display loading indicators to inform users that data is being fetched, improving perceived performance.

---

### Download File {#download-file}

*Learn how to add download file action into your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/file-handling/download-file

The **Download File** action allows you to enable users to download or save files locally on their devices.

File Download Location

* **Windows, macOS, Linux, and Web**: Files are saved in the **Downloads** folder by default.
* **iOS**: Files are downloaded in the **Application Documents Directory**.
* **Android**: Files are saved in the application's directory at `Android/data/your.package.name/files/your_file.extension`.

#### Download File \[Action]

To add a Download File action, select the **Widget** (e.g., button or any interactive widget) where you want users to initiate the file download and set the **Source** to one of the following.

* **From URL**: Use this option for downloading files that are accessible through a direct link and specify the URL of the file that should be downloaded.
* **From File (Bytes)**: Use this option when the file is uploaded to the device using the [Local Upload (Widget State)](https://docs.flutterflow.io/concepts/file-handling/uploading-files#local-upload-widget-state). You can access the file via ***Widget State > Uploaded Local File***.

Optionally, you can specify a **Filename** to be used when the file is downloaded.

![file-download-action](https://docs.flutterflow.io/assets/images/file-download-action-d1fa481c006877dbdc588f6d3f713918.avif)

---

### Uploading Files {#uploading-files}

*Learn how to upload media in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/file-handling/uploading-files

Uploading files is an essential feature for many apps, enabling users to share images, videos, documents, and more. FlutterFlow offers flexible actions to handle file uploads, whether you’re using Firebase, Supabase, or your own backend server. You can customize the upload process to suit your app’s needs, such as resizing media, setting quality, or temporarily storing files locally before uploading.

This guide covers the available upload methods, configuration options, and workflows, including how to save media locally and upload it via an API.

#### Types of Media Uploads

FlutterFlow provides three methods for uploading media files, each catering to different needs:

##### Firebase

Media files can be uploaded directly to **Firebase Storage**, a reliable cloud-based solution. Once the upload is complete, you can use the **Widget State > Uploaded File URL** to preview the media or store the file URL for later use.

![upload-type-firebase.avif](https://docs.flutterflow.io/assets/images/upload-type-firebase-456f096ed9a757798c5a1213e90035b5.avif)

##### Supabase

You can upload media to a **Supabase bucket** at a specified location. After the upload, the file's URL is accessible via **Widget State > Uploaded File URL**, enabling you to preview the media or save the URL for later use in your app.

![upload-type-supabase.avif](https://docs.flutterflow.io/assets/images/upload-type-supabase-dd59212b4c2981e164125df7f5353a1e.avif)

##### Local Upload (Widget State)

This method initially stores your media on the device, making it accessible via **Widget State > Uploaded Local File**. You can preview, edit, or process the file before uploading it to a cloud storage.

![upload-type-local-and-api.avif](https://docs.flutterflow.io/assets/images/upload-type-local-and-api-141c3fa9b729007f50dfb7a245a6b140.avif)

#### Upload or Save Media \[Action]

This action allows you to upload a photo or video to your app. You can choose to store the file on [Firebase](https://docs.flutterflow.io/concepts/file-handling/uploading-files#firebase), [Supabase](https://docs.flutterflow.io/concepts/file-handling/uploading-files#supabase) storage, or your own server using an API. Once uploaded, you can access the file through its generated URL. This URL can be used to display the content immediately or store it in a database for future retrieval.

Prerequisites for Firebase

1. **Firebase** should be connected to your project. Follow the instructions on [**this page**](https://docs.flutterflow.io/integrations/database/cloud-firestore/getting-started) for integrating Firebase with FlutterFlow.
2. **Firebase Authentication** must be properly configured. Check out [**this page**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) for setting up authentication.
3. **Firebase Storage** must be set up and properly configured. It takes just a second! Follow the instructions on [**this page**](https://docs.flutterflow.io/integrations/firebase-storage/storage-rules).
4. At least one **Firebase Collection** should be configured for the project so that you can store the generated URL.

Prerequisites for Supabase

1. Make sure to [**integrate Supabase**](https://docs.flutterflow.io/integrations/supabase/setup) into your app.
2. [**Create a storage bucket**](https://supabase.com/docs/guides/storage/quickstart#create-a-bucket) in Supabase. By default, the **Public bucket** option is disabled, meaning uploaded media is not accessible by anyone without authentication. If needed, you can enable the Public bucket option, but this is not recommended for sensitive content.

![supabase-storage-bucket.png](https://docs.flutterflow.io/assets/images/supabase-storage-bucket-7c69ea6354974d2fa3a080cf97b48106.png)

3. Apply additional [**security rules**](https://supabase.com/docs/guides/storage/quickstart#add-security-rules) which determine who can access the bucket. **Tip**: If you are uploading to a folder structure like this '*pics/uploads*,' here is how you can add a policy that allows only authenticated users to upload their profile picture.

To create an upload media workflow, add the **Upload/Save Media** action to the widget (e.g., a button or any interactive element) where you want users to initiate the file upload. Next, set the [**Upload Type**](https://docs.flutterflow.io/concepts/file-handling/uploading-files#types-of-media-uploads). In the **Media Type/Source** section, specify the type of media to upload: photo, video, or both. Then, use the **Media Source** dropdown to choose the source of the media:

* **Camera**: Directly capture media using the device's camera.
* **Gallery**: Select existing media from the device's gallery.
* **Either Camera or Gallery**: Allows users to choose the source via a bottom sheet, letting them select either the camera or the gallery as the media source.

Once the media is uploaded, see how to display it on a widget in the [next section](https://docs.flutterflow.io/concepts/file-handling/displaying-media).

> **Info:** When you set **Upload Type** to:

* **Firebase**: You must [**deploy the storage rules**](https://docs.flutterflow.io/integrations/firebase-storage/storage-rules).
* **Supabase**: Provide the **Bucket Name** and set the **Uploaded Folder Path** (e.g., pics/uploaded). This is the path where the media will be uploaded.

The Upload Media action offers various settings to control how media files are uploaded, resized, and processed in your app. Below is a breakdown of all the available properties.

![configure-upload-media-action.avif](https://docs.flutterflow.io/assets/images/configure-upload-media-action-2c7983d290d8de71a3b58c526b9fd093.avif)

* **Max Width** and **Max Height**: If you are uploading a photo, you can set a maximum width and height using these properties. This resizes the image while maintaining its original aspect ratio.
* **Image Quality**: Control the image quality by adjusting the slider or entering a value between 0 and 100, where 100 retains the original quality.
* **Include Media Dimensions**: Enable this option to retrieve the dimensions (width and height) of the uploaded media. Keep in mind that this operation is resource-intensive, so enable it only if necessary.
* **Include Blur Hash**: Automatically generates a BlurHash for the uploaded image, allowing you to display a blurred placeholder while the full image loads. For more information, refer to the [BlurHash](https://docs.flutterflow.io/concepts/file-handling/displaying-media#blurhash) section.
* **Source Picker Style**: Customize the appearance of the bottom sheet UI that appears when selecting a media source (e.g., Camera or Gallery).
* **Allow Multiple Images**: Enable this option to allow users to select multiple images. Note that this requires the **Media Source** to be set to **Gallery**. Once multiple images are uploaded, you can access their URLs via **Set from Variable menu > Widget State > Uploaded File URLs (`List<String>`)**.
* **Show Snackbar**: Enable this option to notify users about the upload progress with a snackbar message.

Check out our YouTube video for a detailed explanation of the **Upload or Save Media \[Action]** in FlutterFlow.

##### Store Media for Upload

You can also save the media file temporarily on the device before uploading it to cloud storage by setting the **Upload Type** to [**Local Upload**](https://docs.flutterflow.io/concepts/file-handling/uploading-files#local-upload-widget-state). This saves the file in Bytes, allowing you to preview, edit, or process it before finalizing the upload.

Once the file is uploaded to the device, you can do the following:

* **Preview or Validate the Media**: Show the user an in-app preview before they decide whether to finalize or discard the upload.

* **Editing Before Submission**: In social media apps, users upload photos for posts or stories. The app temporarily saves the image on the device while users edit or apply filters, and then uploads the final image to cloud storage.

* **Perform Data Operations**: In document scanning apps, users capture images of documents, which are temporarily stored on the device. The app accesses the file bytes to apply OCR (Optical Character Recognition), enhance contrast, or convert the image to PDF before uploading the final processed file to cloud storage.

* **Offline Functionality**: Store the media locally and defer uploading until the user regains internet access.

* **Upload to Server**: When you want to store the file externally, you can then make an API call (e.g., multipart form data) to transfer the local file. Be sure to retrieve and save the resulting file URL in your database if you plan to display it later.

Here are some examples of uploading a file to a device and using it in different scenarios:

**Example 1: Upload to Your Backend Server via API**

First, set the **Upload/Save Media** action with the **Local Upload (Widget State)** upload type. Then, add the next action as an **API call** and select the API that will upload the file to your server. After the API call is complete, ensure your server returns the uploaded file's URL. Use this URL to save in the database or [display the uploaded image](https://docs.flutterflow.io/concepts/file-handling/displaying-media).

> **Info:** The request body for the API must be in *Multipart* format. See how to [**configure an API for the multipart request body**](https://docs.flutterflow.io/resources/backend-logic/rest-api#multipart-format).

**Example 2: Compress Image Using Custom Action**

First, configure the **Upload/Save Media** action with the **Local Upload (Widget State)** upload type. This temporarily saves the media file on the device.

Next, create and add a [**Custom Action**](https://docs.flutterflow.io/concepts/custom-code/custom-actions) (e.g., `compressImageAction`) that takes the locally stored file as input and compresses it using its **bytes** data. Ensure the custom action processes the image and returns a compressed file. Once compressed, the file can then be uploaded to cloud storage using another **Upload/Save Media** action.

![compress-image](https://docs.flutterflow.io/assets/images/compress-image-ad8fa8677df4048a3189d92bf99fa084.avif)

**Example 3: Upload to Firebase or Supabase**

First, configure the **Upload/Save Media** action with the **Local Upload (Widget State)** upload type. Once the file is modified or processed, add another **Upload/Save Media** action to the widget that confirms the final upload. Set the **Upload Type** to **Firebase** or **Supabase**, choose **File Type** as the **Uploaded File**, and select **File to Upload** from **Widget State > Uploaded Local File**.

![local-upload-to-firebase-supabase](https://docs.flutterflow.io/assets/images/local-upload-to-firebase-supabase-2fb33a0122e06e4a4477a4d482c7a47b.avif)

#### Upload or Save File \[Action]

You can upload any type of file to your app, such as PDFs, MP3s, and more. The process for uploading files is almost similar to the [Upload or Save Media Action](https://docs.flutterflow.io/concepts/file-handling/uploading-files#upload-or-save-media-action).

Web access for PDF files

If you plan to support the web version of your app or test the PDF upload feature in **Run Mode**, you’ll need to complete additional configuration steps required for certain file types (e.g., PDFs). Learn how to [**enable web access**](https://docs.flutterflow.io/concepts/file-handling/displaying-media#web-access-for-pdfs-and-other-files).

---

### GenUI Chat {#genui-chat}

*Add a conversational AI surface to your FlutterFlow app that can render catalog components, call action blocks as tools, and react to local app events.*

**Source:** https://docs.flutterflow.io/concepts/genui-chat

Usually, applications follow a fixed model: developers design screens, define navigation, and hard-code interactions. Users are limited to these predefined flows, and anything outside those paths simply isn’t supported.

With GenUI, your app provides agent-driven experiences. Instead of relying on rigid flows, an AI agent can assemble user journeys dynamically in real time. Developers no longer need to predict every scenario. Instead, they define the building blocks and the AI orchestrates them into meaningful, context-aware experiences for the user.

This represents a fundamental shift, from building fixed applications to building flexible capabilities that an agent can compose on demand. Think of it as building the components, and AI decides when to use them.

**Traditional App:** The user clicks 'View Order' → navigates to `OrderDetailPage` → sees order info + tracking + items list. The flow is fixed, and every interaction must be pre-built.

**With GenUI:** Build `OrderSummaryCard`, `TrackingStatusCard`, `OrderItemsList` as separate components. Build `getOrderDetails` as a tool. The AI decides what to show based on what the user asks.

For example, a user asks, “Show my recent orders.” Instead of responding with text, the agent renders **order card components** with details like items, price, and delivery status. The user then asks, “Where is my latest order?” Now, instead of showing another block of text, the agent switches to a **map component** to display the live delivery location. This demonstrates how the agent dynamically selects the most relevant UI component based on the user’s intent.

![personal-shopper.avif](https://docs.flutterflow.io/assets/images/personal-shopper-b9e7ccff90193aeb9638a5b8da227793.avif)

GenUI is not a chatbot

GenUI may look like a chat interface, but it is fundamentally different from traditional chatbots. Instead of responding with text messages, the AI renders real UI components, such as cards, lists, forms, and maps—directly in the interface. Users don’t just read responses; they interact with fully functional UI.

This means GenUI is not about conversations, it’s about dynamically composing application experiences using your actual app components.

> **Note:** This doesn’t replace traditional UI. Navigation, dashboards, and structured flows still play an important role. GenUI introduces a **new layer** — dynamic, adaptive, and conversational — that handles the long tail of use cases traditional interfaces can’t efficiently cover.

#### GenUI Is Built on A2UI

GenUI is FlutterFlow's implementation of [**A2UI (Agent-to-UI)**](https://a2ui.org/). An [**open project by Google**](https://github.com/google/A2UI) that defines a declarative UI protocol for agent-driven interfaces. A2UI allows AI agents to generate rich, interactive UIs that render natively across platforms (web, mobile, desktop) without executing arbitrary code.

#### Three Pillars of GenUI

GenUI introduces three core pillars that work together to transform your app into an agent-driven experience:

**1. Component Catalog:** Instead of replying with plain text, the AI uses your FlutterFlow components, such as product cards, booking tiles, or dashboards, to present information directly in the interface. Users don’t read the text; they interact with real UI.

**2. Tools:** Your existing FlutterFlow action blocks become capabilities the AI can use. Whether it’s fetching data, calling APIs, submitting forms, or triggering workflows, the AI can execute these actions and use the results instantly. It moves beyond conversation and starts performing real tasks inside your app.

**3. App Event Integration:** Your app’s events provide real-time context to the AI. Things like user actions, state changes, or backend updates can trigger responses. With auto-response enabled, the AI doesn’t wait for input; it proactively reacts and updates the experience as things happen.

![three-pillars.avif](https://docs.flutterflow.io/assets/images/three-pillars-e833097b98c4cf315e6622864d5d66a1.avif)

#### Adding GenUI

Let’s walk through how to add a GenUI Chat by building a simple product lookup assistant. Follow the steps below:

1. Make sure you’ve completed the [Firebase integration](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase), including the [initial setup](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) and configuration files.

2. Go to **Firebase Console > AI Logic** and enable it. GenUI is powered by **Google Gemini** via [**Firebase AI Logic**](https://firebase.google.com/products/firebase-ai-logic) and uses a **usage-based pricing model**. You can get started on the **Spark (free)** plan for testing and low usage, but for production or higher usage, you’ll need to upgrade to the **Blaze (pay-as-you-go)** plan, where costs depend on AI requests and token usage.

   tip

   We recommend monitoring your usage in the Firebase Console, setting up budget alerts to avoid unexpected charges, and upgrading to Blaze before moving to production.

3. In your FlutterFlow project, create a **`ProductListCard`** component, which displays product details such as the image, name, and description. This component accepts a parameter of Data Type **`Product`**.

4. Create an Action Block named **`getProductDetails`**, which retrieves the details of a single product and returns it as a **`Product`** data type.

5. Place the **GenUI Chat** widget on a page or component like any other FlutterFlow widget.

6. Go to the Properties panel and define domain instructions to guide how the assistant behaves and communicates in your app. These instructions help the AI understand your app’s context, tone, and what it should prioritize. If left empty, it defaults to a generic assistant that builds UI in response to user requests.

   **Example System Prompt:** `You are a helpful AI shopping assistant for an e-commerce app. Help users discover products, compare options, track orders, and complete purchases.`

7. Select the components that the AI is allowed to render in responses. For this example, select the `ProductListCard` component created in step 3. To learn how to configure components for GenUI, refer to the [Component Catalog](https://docs.flutterflow.io/concepts/component-catalog) documentation.

8. If needed, add the [Action Blocks](https://docs.flutterflow.io/resources/functions/action-blocks) that the AI can call. For this example, select the action block named `getProductDetails`, created in step 4. Note that only Action Blocks that return a value can be added. To learn how to configure them for GenUI, refer to the [Tools Configuration](https://docs.flutterflow.io/concepts/tools) documentation.

9. If needed, choose Local [App Events](https://docs.flutterflow.io/concepts/app-events) to connect to the conversation. To learn how to configure app events for GenUI, refer to the [App Events Integrations](https://docs.flutterflow.io/concepts/app-event-integration) documentation.

##### Customization

You can fully customize the chat interface using the following options available in the Properties panel:

* **Layout & container:** Background, border radius, padding, message spacing, and max message width
* **Header:** Visibility, title, background color, and text color
* **Avatars:** Visibility, size, and image sources for both user and AI
* **Message bubbles:** Background colors, text colors, and border radii for user and AI messages
* **Input field:** Placeholder text, background, border radius, and padding
* **Send button:** Icon and background styling
* **Welcome state:** Visibility, title, and subtitle shown when the chat is empty
* **Scrolling behavior:** Auto-scroll to new messages and animation duration
* **Thinking/status message:** Text displayed while the AI is generating a response

**Default Behavior:**

* Header is shown by default
* Avatars are enabled by default
* Auto-scroll is enabled
* Input placeholder defaults to “Type a message…”
* Thinking message defaults to “Thinking…”
* Welcome state is shown when there are no messages

#### Examples

###### 1. Customer Support Agent

**Traditional Approach:** Build a help center with FAQ pages, a ticket form, and a chatbot that matches keywords to canned responses.

**GenUI Approach:**

* **Catalog Components:** TicketStatusCard, FAQArticle, EscalationForm, SatisfactionSurvey, AgentContactCard
* **Tools:** `lookupTicket(ticketId)`, `searchKnowledgeBase(query)`, `createTicket(details)`, `getCustomerHistory(customerId)`
* **App Events:** `NewTicketUpdateEvent` (auto-respond) when a support ticket is updated in the backend, the AI proactively informs the user

A user opens the support chat. They describe their issue in natural language. The AI searches the knowledge base using the tool, finds a relevant article, and renders it as a FAQ Article component. If that does not resolve the issue, the AI creates a ticket using `createTicket`, shows the TicketStatusCard with the new ticket ID, and says it will notify them of updates. Later, when the support team updates the ticket, a `NewTicketUpdateEvent` fires, and the AI proactively shows the updated TicketStatusCard with the resolution.

The developer did not build a "ticket lookup flow" or a "knowledge base search screen." They built components and tools. The AI composed the journey.

###### 2. E-Commerce Personal Shopper

**Traditional Approach:** Build product listing pages, filters, a search bar, a comparison tool, a cart, and a checkout flow.

**GenUI Approach:**

* **Catalog Components:** ProductCard, ComparisonTable, PriceHistoryChart, ReviewSummary, CartSummary, PromoCodeBanner
* **Tools:** `searchProducts(query,filters)`, `getProductDetails(productId)`, `getReviews(productId)`, `addToCart(productId,quantity)`, `applyPromoCode(code)`, `getPriceHistory(productId)`
* **App Events:** `CartUpdatedEvent` (context injection) keeps the AI aware of what is already in the cart; `FlashSaleEvent` (auto-respond) alerts the user about time-sensitive deals

A user says, "I need a gift for my dad who likes woodworking and coffee." The AI searches products, shows a curated set of ProductCards, and when the user shows interest in a specific item, pulls up the ReviewSummary and PriceHistoryChart. The AI knows what is in the cart (via CartUpdatedEvent context) and can suggest complementary items. When a flash sale starts on a relevant product, the AI proactively shows the PromoCodeBanner.

No search results page. No filter sidebar. No "compare" button. The AI built a personalized shopping experience from the components and tools available to it.

#### Current Limitations

Here are some important limitations and considerations to keep in mind:

* The only supported backend today is **Firebase AI Logic**.
* App event listeners currently work only with **LOCAL** app events.
* Catalog components cannot expose action parameters.
* Avatar images must be valid network URLs (local asset paths are not supported).
* Each rendered surface supports only a single catalog component as its root.

#### Best Practices

###### Describe Everything

The AI reads your component and parameter descriptions to decide what to render and what values to provide. The quality of your descriptions directly impacts the quality of the AI's responses.

* Name components clearly: `ProductCard` not `Card1`
* Name parameters descriptively: `estimatedDeliveryDate` not `date`
* Add descriptions to parameters: "The product's price in USD" not just "price"
* Add descriptions to action blocks: "Searches the product catalog and returns matching items with prices and availability" not just "search"

The AI is only as smart as the vocabulary you give it.

###### Design for Composition

Components and tools work best when they are designed to be composed:

* **Retrieval Tool + Display Component:** `getOrderDetails()` returns an `OrderStruct` -> `OrderStatusCard` accepts an `OrderStruct` as a parameter. The AI calls the tool and passes the result to the component.
* **Granular Over Monolithic:** A `ProductCard`, `ReviewSummary`, and `PriceChart` give the AI three options. A single `ProductDetailPage` component gives the AI one.
* **Consistent Data Types:** Use the same DataStruct across related tools and components. If `searchProducts` returns `ProductStruct`, make `ProductCard` accept `ProductStruct`.

###### Use Events for Temporal Awareness

App events give the AI a sense of time and change. Without them, the AI only knows what the user tells it. With them, the AI knows what is happening.

* Use **auto\_respond: false** for continuous state awareness, such as user navigation, preference changes, background data updates.
* Use **auto\_respond: true** for time-sensitive signals, such as alerts, completions, threshold breaches, incoming messages.

###### Write System Prompts Like Onboarding Documents

The system prompt is the AI's job description. Write it like you are onboarding a new team member:

* What is their role?
* What domain should they know about?
* What should they prioritize?
* What should they never do?
* What tone should they use?
* What business rules must they follow?

A great system prompt makes the difference between a useful assistant and a generic chatbot.

#### Behind the Scenes

GenUI is powered by [**Firebase AI Logic**](https://firebase.google.com/products/firebase-ai-logic) (Google Gemini) as its LLM backend. At a high level, the system works as:

**Your configuration → code generation → runtime widget powered by Firebase AI Logic and the [GenUI](https://pub.dev/packages/genui) package**.

You define components, tools, and events in FlutterFlow, and GenUI automatically generates the necessary code and runtime behavior to render dynamic UI experiences.

#### FAQS

The widget builds but the AI only sends text

Check the catalog first. If no component fits the request, text is the expected fallback. Also, confirm that your system prompt and component descriptions make it clear when each component should be used.

I can't add a component to the catalog

The most common causes are:

* The component has an action parameter.
* A required complex parameter is missing a default value.
* The component was deleted or renamed after being configured.

I can't add an Action Block as a tool

The Action Block must return a value, and every parameter, plus the return type, must be supported by the tool serializer.

My event listener is not firing

Make sure the following are correctly set:

* The event is LOCAL scope.
* The right event is being triggered at runtime.
* `auto_respond` is set the way you expect.

Why does a component fail validation?

Common reasons include:

* It has an action parameter.
* It is configured twice in the same catalog.
* A required complex parameter is missing a default value.
* The configured component no longer exists.

Why is the model choosing the wrong component?

Usually one of these is true:

* The names are too generic.
* Parameter descriptions are weak.
* Multiple catalog components overlap too much in purpose.
* The system prompt does not explain how the assistant should prioritize them.

Can the model render multiple items?

Yes, but the reliable pattern is to use a single catalog component that accepts a list rather than expecting the model to assemble multiple independent sibling components on its own.

Why is the model not calling a tool?

Usually, the issue is not codegen. It is tool discoverability:

* The name is vague
* The description is weak
* The system prompt does not make it clear when the tool should be used
* The model already has enough context to answer without calling it

What happens when a tool fails?

The generated tool code catches the exception, clears the loading state, and sends an error payload back to the model. The UI should remain stable, and the model can decide how to explain or recover.

Why can't I select my event?

The event must be **LOCAL** scope and must still exist in the project or dependency where it was defined.

Why didn't the assistant respond immediately?

Check the following:

* whether `auto_respond` is actually `true`
* whether the event is being triggered
* whether the system prompt tells the model to react visibly

Note: Even with immediate inference, not every event will result in a visible response.

Why does the assistant only react on the next user message?

That is the expected behavior for `auto_respond: false`. The listener queues hidden context instead of triggering a separate inference call.

Can one GenUI widget listen to the same event twice?

No. Duplicate listeners for the same event on the same widget are rejected during validation.

Do conversations persist across app restarts?

No. Conversations do not persist across app restarts. If a user closes and reopens the app, the chat history is reset.

Can I choose the Gemini model or adjust parameters like temperature?

GenUI uses Firebase AI Logic, which manages the underlying Gemini model and its configuration. At the moment, you cannot directly select specific model variants or adjust parameters like temperature or top\_p. The system is designed to provide a simplified, managed experience without requiring manual tuning.

What happens when Firebase AI Logic quota or rate limits are exceeded?

If you exceed Firebase AI Logic or Gemini free-tier limits, requests will fail with a 429 quota-exceeded error. This typically means you’ve hit limits such as requests per minute or free-tier usage caps. In some cases, the error will include a retry time, after which you can try again. While the Spark plan works for testing, it is subject to strict free-tier limits, so for higher usage or production apps, you should expect to upgrade to a paid plan and monitor usage closely

---

### Building Layout {#building-layout}

*Learn how to build layout in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/layouts

In FlutterFlow, you build a page layout using Widgets. **Widgets**, such as [Text](https://docs.flutterflow.io/resources/ui/widgets/text), [Buttons](https://docs.flutterflow.io/resources/ui/widgets/button), [Images](https://docs.flutterflow.io/resources/ui/widgets/image), and [Icons](https://docs.flutterflow.io/resources/ui/widgets/icons), are visible on the screen. Others, like [Containers](https://docs.flutterflow.io/resources/ui/widgets/container), Rows, Columns, and Stacks, are not directly visible but help arrange and position the visible elements on the page.

These widgets are categorized into four main types: [Layout Elements](https://docs.flutterflow.io/tags/layout-elements), [Base Elements](https://docs.flutterflow.io/tags/base-elements), [Page Elements](https://docs.flutterflow.io/resources/ui/pages/scaffold), and [Form Elements](https://docs.flutterflow.io/tags/form-elements). To build a page, you combine different widgets from these categories to get the desired look and feel of your app.

#### Understanding Layout Concept

One of the most common layout patterns is to arrange widgets either **vertically** or **horizontally**. To display widgets in a vertical layout, use the **Column** widget. For a horizontal layout, use the **Row** widget. If you need to place one widget on top of another, use the **Stack** widget.

> **Info:** **Composing widgets** is a fundamental aspect of creating layouts in FlutterFlow. It involves combining different widgets to form a cohesive and functional user interface. Understanding how to effectively compose widgets allows you to design complex layouts and create intuitive, user-friendly apps. Learn more about composing widgets [**here**](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/rows-column-stack).

#### Building Layouts: Exercise

Let's walk through an exercise to build the following layout:

![build-layout-page.avif](https://docs.flutterflow.io/assets/images/build-layout-page-708a22947554f59924e51a2e876092f7.avif)

The steps to build the given layout are as follows:

1. [Sketch the layout](https://docs.flutterflow.io/concepts/layouts#1-sketch-the-layout)
2. [Add Image section](https://docs.flutterflow.io/concepts/layouts#2-add-image-section)
3. [Add info section](https://docs.flutterflow.io/concepts/layouts#3-add-info-section)
4. [Add reviews section](https://docs.flutterflow.io/concepts/layouts#4-add-reviews-section)

###### 1. Sketch the layout

When you are just starting out with building apps, this step is very crucial. Before you actually start adding widgets to the page, sketch a picture of how the main layout will be broken into smaller parts.

Breaking down the given layout into sections looks like this:

![breaking-main-layout-2.png](https://docs.flutterflow.io/assets/images/breaking-main-layout-2-cd4430869a74e015f6e0021330903d14.avif)

Next, identify the widgets that can replace those sections, such as Column, Row, and Stack. Once you have a clear idea of which widgets to use, you can begin adding them.

In the figure above, the main section is replaced with the Column widget and is divided into smaller sections. The next step is to look carefully at these smaller sections and, if required, divide them into further small sections and replace them with the appropriate widget. You can repeat this process until you achieve the desired level of granularity.

Splitting the smaller section further looks like this:

![divide-smaller-section-2.png](https://docs.flutterflow.io/assets/images/divide-smaller-section-2-b2b0ea71f1867fc5686d49de5168e1d1.avif)

> **Info:** A page can only have one parent widget. i.e., you can't have two containers (at the same level) inside the HomePage. For that, you can wrap the two containers inside the Column widget, which makes the Column widget a single parent.

![column-as-single-parent.avif](https://docs.flutterflow.io/assets/images/column-as-single-parent-308c0170df84f473826850c93ffa0e64.avif)

###### 2. Add Image section

The top section includes the Image and IconButton widgets. To place the IconButton on top of the Image, wrap them inside a Stack widget. Here's how you do it:

###### 3. Add info section

The info section consists of a few Text widgets inside the Column.

###### 4. Add reviews section

The review section consists of multiple different widgets. First, add a Column to separate the reviewer's information (image and name) from the actual review text. Next, display the reviewer's information inside a Row widget using the CircleImage and Text widgets. Here’s exactly how you do it:

#### Common Layout Widgets

Apart from Row, Column, and Stack widgets, there are some other widgets that are widely used for building the page layout. Here are some of them:

* [Container](https://docs.flutterflow.io/resources/ui/widgets/container)
* [Card](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/card)
* [ListView](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid)
* [GridView](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid)
* [TabBar](https://docs.flutterflow.io/concepts/navigation/tabbar)
* [PageView](https://docs.flutterflow.io/concepts/navigation/pageview)
* [Form](https://docs.flutterflow.io/resources/forms)

#### Video guides

To learn more about building layout, watch our videos:

---

### ConditionalBuilder {#conditionalbuilder}

*Learn how to display different widgets based on certain conditions in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/layouts/conditional-builder

The `ConditionalBuilder` widget allows you to dynamically display different widgets based on certain conditions (either [single](https://docs.flutterflow.io/resources/functions/conditional-logic#single-condition) or [multiple](https://docs.flutterflow.io/resources/functions/conditional-logic#multiple-conditions-andor)). Using this widget, you can define different conditions, each associated with a specific widget to be displayed when that condition is true. It's like having a switch that shows different things depending on what's happening in your app.

For example, displaying different charts based on user roles. For team members, an individual progress chart can be shown. Team leads can view the overall progress of the entire team, while project managers can see over project progress chart. Just like the below:

![conditional-builder-widget-demo.png](https://docs.flutterflow.io/assets/images/conditional-builder-widget-demo-183b8ff6c3c63a19d3e8bd8be6880b31.png)

#### Adding ConditionalBuilder widget

To add the `ConditionalBuilder` widget to your app:

1. Add the **ConditionalBuilder** widget (from the **Base Elements**) to where you want to display dynamic widgets.

2. Move to the **Properties Panel** **>** **Conditional Builder Properties,** andUnder the **First Condition**, provide the **IF** [condition](https://docs.flutterflow.io/resources/functions/conditional-logic) by clicking on **UNSET**.

3. Now, besides the **THEN**, click **Empty**. This will automatically select the **IF** widget in the widget tree. Inside that, add a widget that you want to display if this condition is true.

4. To add one more condition-based widget, click on the "+" button, add a condition for the **ELSE IF** section, and add a widget inside the **Else If** widget in the widget tree.

5. If none of the conditions are satisfied, add a default widget to display inside the **Else** widget.

6. Use the **Show In UI Builder** option to see that particular widget in the [canvas area](https://docs.flutterflow.io/flutterflow-ui/canvas). You can see only one widget at a time.

---

### Flex {#flex}

*Learn how to add the Flex widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/layouts/flex

The **Flex** widget can be used as an alternative to **Row** and **Column**. It allows you to dynamically set the layout axis (horizontal or vertical) based on specific conditions or logic. This is especially useful for creative responsive layouts - where child elements should be horizontal when the screen is wide, and vertical when the screen is narrow.

![flex.png](https://docs.flutterflow.io/assets/images/flex-aaafa4fc69ce98d225fc76b00662819c.png)

#### Adding Flex Widget

To use the Flex widget, add it from the **Layout Elements** section of the **Widget Palette**, then add child widgets inside it. From the properties panel, set a condition for the **Is Horizontal** property. When this condition evaluates to `True`, the items will be laid out horizontally.

Consider an ecommerce app where recent orders are displayed vertically on mobile devices and switch to a horizontal layout on larger screens to make better use of the available space.

Here's another example of using a Flex widget on a create account page to dynamically align the signup fields based on screen size.

Best Practices

* If you only need a simple vertical or horizontal arrangement, consider using [**Row**](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/rows-column-stack) or [**Column**](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/rows-column-stack).
* For very large numbers of children, consider using [**ListView**](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#listview-widget) or [**GridView**](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#gridview-widget) instead of **Flex**, as they offer better performance for scrolling large lists of items.
* When the content exceeds the screen limit, you can enable scrolling to make the content accessible. However, if you want to avoid scrolling altogether and still fit all the content on the screen, consider using a [**Wrap**](https://docs.flutterflow.io/concepts/layouts/wrap) widget.

#### Customization

When **Is Horizontal** property is disabled, the Flex widget behaves like a Column, and when enabled, it acts as a Row. Settings like [main axis alignment](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/rows-column-stack#main-axis), [cross axis alignment](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/rows-column-stack#cross-axis), [scrollability](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/rows-column-stack#scrollability), and [spacing](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/rows-column-stack#spacing) work the same way they do for the Column and Row widgets.

---

### Responsive Layout {#responsive-layout}

*Learn how to create responsive layout in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/layouts/responsive

FlutterFlow is great at creating applications adaptable to a wide range of screen sizes, devices, and platforms. Ensuring that our screens maintain their aesthetic appeal across all these variations is crucial. Below, we outline various methods to enhance the responsiveness of your UI screens.

**Note:** Please check out the examples in the order they're given, as they use the same example. Jumping to sections might make things confusing.

##### Global Properties

Let's start by demonstrating how screen width and height values change when you switch between devices in Test Mode.

First, create a new project. In the Home Page, under a Column parent, add two Text widgets. Label one "Screen Width" and the other "Screen Height."

![screen-width-height.avif](https://docs.flutterflow.io/assets/images/screen-width-height-15b30c03124d32fadf7ae728754cac87.avif)

Next, we'll display the changing values alongside these titles. For each Text widget, set its value to a variable. Select *Combine Text* from the options. Your first Text value should be either "Screen Width: " or "Screen Height: ".

Then, add another Text value that will show the corresponding value. This second Text value is also set from a variable. Choose 'Global Properties,' and then select either 'Screen Width' or 'Screen Height' from the list. These options hold the current screen width/height values. Repeat this process for both Text widgets.

![setting-global-properties.avif](https://docs.flutterflow.io/assets/images/setting-global-properties-4f4375303e692ebdaf2ca886062b95ee.avif)

Now, when you switch to Test Mode and try out different devices, you'll see the screen width and height values update accordingly.

* Running app on Test Mode for desktop device sizes
* Running app on Test Mode for mobile device sizes

![running-app-on-test-mode-for-desktop-device-sizes.avif](https://docs.flutterflow.io/assets/images/running-app-on-test-mode-for-desktop-device-sizes-a33815a0c05375fd8501943ab6d49d17.avif)

![running-app-on-test-mode-for-mobile-device-sizes.avif](https://docs.flutterflow.io/assets/images/running-app-on-test-mode-for-mobile-device-sizes-52410bce4805003848c8de270648d02a.avif)

This is to show you that these screen values are always accessible as global properties. You can use them to design your UI logic effectively.

#### Expanded & Flex

Let's explore a fundamental method to make columns and rows adapt to different screen widths and heights. While designing a Row or Column, it's important to avoid assigning fixed sizes to the children, unless specifically required by the design.

Take, for instance, the navigation bar we're creating for our web version. It includes the page name, several navigation icons, and a search bar. Notice how the search bar adjusts its length based on the available width. This adaptability is achieved because the widths of the children are set relative to the available space in the horizontal section.

![web-version-of-our-shopping-app-example.gif](https://docs.flutterflow.io/assets/images/web-version-of-our-shopping-app-example-aa9a2440bf6f2a5e6b5b3e8b0ba3922f.gif)

To design the same navbar, create the following widget hierarchy:

```
- Container (named as webHeader)
       - Row
             - Row
             - TextField (named as searchBar)
             - IconButton
```

The second Row is further broken down into the following:

```
- Row 2
    - Text (named as pageName)
    - Row 3 (named as navIcons)
        - IconButton
        - IconButton
        - IconButton
```

![row-breakdown.avif](https://docs.flutterflow.io/assets/images/row-breakdown-0865c1248a5728409c0b62b9c483791b.avif)

As you can see, the search bar currently occupies the maximum available space. However, we want both `Row 2` and the `searchBar` to share the space equally. To achieve this, simply adjust the Widget properties.

For `Row 2`, set its Expansion property to *Flexible* (the middle icon) and assign a Flex value of 1. Repeat the same steps for the `searchBar`. This change ensures they are allocated space in a 1:1 ratio, based on what's available. After this adjustment, you'll notice that the remaining space, following the placement of the *search IconButton* on the right, is evenly divided between `Row 2` and the `searchBar`.

![test-expansion.avif](https://docs.flutterflow.io/assets/images/test-expansion-22ad3f38b0413b27af8917f838f7fbdc.avif)

We encourage you to test with different web dimensions and sizes to see how well this adapts.

Depending on your design needs, there are various approaches to managing space. Let's consider a different scenario: What if we want the searchBar to always occupy 40% of the screen width, with `Row 2` taking up the remaining space after placing the `searchBar` and `search IconButton`?

To do this, first set the `searchBar`'s width to 40% and its expansion to *Default* (the first icon).

![set-searchbar.png](https://docs.flutterflow.io/assets/images/set-searchbar-b7c349fa3407021706be9ba91ff8923b.png)

Next, adjust the `Row 2` widget's Expansion setting to *Expanded* (the third icon). With these settings, you'll see that `Row 2` now occupies all the space left over after allocating 40% to the `searchBar` and placing the `search IconButton`.

Note: We've added some padding and enhanced the UI of the `searchBar` to improve its appearance.

![enhanced-searchbar.avif](https://docs.flutterflow.io/assets/images/enhanced-searchbar-677c41baa49322699a4dad3e56c5e75b.avif)

You can also go ahead and improve the spacing between the `pageName` and `navIcons` by adjusting the MainAxisAlignment to *Space Between* (represented by the last icon).

Feel free to try this out with different screen sizes to see how it effectively adapts to the available space.

#### Wrap method

Another effective method to enhance the responsiveness of a row or column containing multiple items is through the use of the Wrap widget.

Let's consider a scenario with a Row of category cards.

![row-of-cards.avif](https://docs.flutterflow.io/assets/images/row-of-cards-e4e6d2a4cb846148878d7bbe80c99643.avif)

You might observe that when the screen size is adjusted to resemble mobile dimensions, the cards begin to get cut off at the edges.

![row-card-resize.gif](https://docs.flutterflow.io/assets/images/row-card-resize-c2acaeb8d8830a78f3662c0d9f63e380.gif)

To resolve this issue, simply replace the parent Row widget with a Wrap widget.

Make sure to set the Wrap Direction to 'Horizontal' in the Wrap properties. You'll then see that the previously overflowing cards neatly move to the next line, as illustrated in the example.

![row-card-resize.gif](https://docs.flutterflow.io/assets/images/row-card-resize-2-f65d7398b92533417391457ad854c746.gif)

The Wrap widget efficiently manages layout for varying screen sizes by automatically adjusting its children into multiple rows or columns. It prevents overflow and ensures a clean, responsive design, especially useful for adapting content like category cards from desktop to mobile views.

#### Responsive Breakpoints

Moving on to more complex layout scenarios, where the UI significantly differs between mobile and web platforms, it's important to first understand breakpoints.

**Breakpoints** in responsive design are like thresholds for different screen sizes. They act as specific points where the layout of a user interface meets a certain screen size requirement and then changes to accommodate it. When the screen size crosses one of these thresholds, the layout adjusts.

FlutterFlow has default breakpoints for different screen sizes, but you can also adjust these to better suit your app's design needs.

##### Customize Responsive Breakpoints

Go to your Theme Settings > Design System and find the Breakpoints section with default values already set. You can go ahead and customize it if needed.

![custom-responsive-breakpoints.avif](https://docs.flutterflow.io/assets/images/custom-responsive-breakpoints-74e45bbcc5192146f1511644cc2b9789.avif)

The following sections will also rely heavily on *Responsive Visibility,* so let's proceed.

#### Visibility of Nav Bar & App Bar

In many designs, the App Bar and Nav Bar are typically included in mobile or mobile + tablet screens, and often omitted in desktop formats. FlutterFlow makes it easy to enable or disable the Nav Bar and App Bar.

Just go to App Settings, select Nav Bar & App Bar, and toggle the 'Show Nav Bar' option. Upon enabling it, you'll see additional settings. Icons for mobile, tablet, tablet (landscape), and desktop let you choose where the Nav Bar should appear.

Generally, it's advisable to enable it only for mobile, or mobile and tablet. Let's follow these steps to configure it for our app.

![appbar-navbar-visibility.webp](https://docs.flutterflow.io/assets/images/appbar-navbar-visibility-824b7f96fe1dd292089af2f2b7dc4e85.webp)

Now, when testing directly in our editor, observe how the navbar appears only for mobile and tablet screen sizes. This same approach can be applied to the App bar as well.

![appbar-navbar-visibility-resize.gif](https://docs.flutterflow.io/assets/images/appbar-navbar-visibility-resize-2aad6b0af11e814a4f0dbbf3ac048507.gif)

#### Responsive Visibility

In our previous examples, we improved many aspects, but some responsive issues still remained. For instance, our NavBar displayed the same navigation icons on both top header and bottom navbar. Additionally, when the screen width was reduced to mimic mobile dimensions, the header elements became cramped and difficult to interact with.

To address this, we can leverage FlutterFlow's Responsive Visibility feature to implement distinct AppBar and SearchBar designs for mobile, while maintaining the current design for web.

Imagine we've created a new widget, `mobileAppBar` , and added it to our layout. This widget cleverly separates the categories header and search bar vertically and includes a back navigation button. The goal is to activate this mobile-friendly layout for mobile and tablet screens, while preserving the 'webHeader' for tablet (landscape) and desktop views.

![responsive-visibility.avif](https://docs.flutterflow.io/assets/images/responsive-visibility-748f5a277989829f4c2427b745a218c8.avif)

To implement this, we can go to its widget properties and toggle the device icons as shown in the following demo.

And now you have a more responsive screen for this shopping app use case that looks good in both mobile and desktop formats.

With these adjustments, your shopping app now boasts a highly responsive screen that seamlessly adapts to both mobile and desktop formats. This ensures an optimal user experience across all devices, maintaining both functionality and aesthetic appeal.

#### Responsive Value

**Responsive Values** allow you to define different property values, such as widths, heights, font sizes, or padding, for different device sizes (mobile, tablet, desktop, and wide). At runtime, your app evaluates the screen width and automatically applies the appropriate value based on your configurations.

possible use cases

* **Adaptive Layouts**: Automatically adjust element sizes to deliver a consistent UI across devices.
* **Better Readability**: Increase font size on larger screens to improve legibility.
* **Improved Spacing**: Use different padding or margins on tablets and desktops to optimize content flow.

To set a responsive value, select a widget and choose a property that supports responsiveness. Click **Set from Variable > Responsive Value**, then enter different values for each screen size:

* Mobile (below `Breakpoint Small`)
* Tablet (below `Breakpoint Medium`)
* Desktop (below `Breakpoint Large`)
* Wide (above `Breakpoint Large`)

As you preview on different devices, the property will automatically adjust based on the selected screen size.

Customizing Breakpoints

You can adjust the default screen size breakpoints (mobile, tablet, desktop, wide) in FlutterFlow’s Theme Settings. See how to [**Customize Breakpoints**](https://docs.flutterflow.io/concepts/layouts/responsive#customize-responsive-breakpoints).

---

### Wrap {#wrap}

*Learn how to add the Wrap widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/layouts/wrap

The Wrap widget is similar to Row and Column as it shows its children one after another. If there is not enough space to show your item, the Wrap widget will automatically place it in a new row or column.

#### Adding Wrap widget

Here's an example of how you can use a Wrap widget in your project:

1. First, drag the [**Container**](https://docs.flutterflow.io/resources/ui/widgets/container) widget from the **Layout Elements** tab (in the Widget Panel) or add it directly from the widget tree and set its **width** to **infinity** and **height** to **200**.

2. Add the **Wrap** widget from the **Layout Elements** tab inside the Container.

3. Add the **Button** widget inside the Wrap widget.

4. Copy-Paste and add a few more Button widgets.

![add-wrap-widget.gif](https://docs.flutterflow.io/assets/images/add-wrap-widget-22e05ab20c3829a655e8b53114fe0050.gif)

See how the Button that won't fit in the remaining space is placed in the next line.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

##### Changing Direction

In the example above you saw that the items are added in the horizontal direction, which is a default axis for adding items.

To change the direction in which the items are added:

1. Select the **Wrap** from the widget tree or from the canvas area.
2. Move to the Property Editor and scroll down to the **Wrap Properties** section.
3. Spot the **Direction** dropdown, change it to **Vertical**.

The Horizontal Direction makes the Wrap widget work like a Row while the Vertical Direction makes the Wrap widget work like a Column.

![wrap-change-direction.gif](https://docs.flutterflow.io/assets/images/wrap-change-direction-ee904fc260c4adb4ffd0d05cad584d74.gif)

##### Adding Space Between Items

To add space between items:

1. Select the **Wrap** from the widget tree or from the canvas area.

2. Move to the Property Editor and scroll down to the **Wrap Properties** section.

3. In the **Spacing** input box, enter the value as 10. If the **Direction** is set to **Horizontal**, Wrap will insert the empty space of 10px vertically between the items. and If the **Direction** is set to **Vertical**, Wrap will insert the empty space of 10px horizontally between the items.

4. In the **Run** **Spacing** input box, enter the value as 15. If the **Direction** is set to **Horizontal**, Wrap will insert the empty space of 15px horizontally between the items. and If the **Direction** is set to **Vertical**, Wrap will insert the empty space of 15px vertically between the items.

![wrap-space-between-items.gif](https://docs.flutterflow.io/assets/images/wrap-space-between-items-3bbbf369615a39c1581569b2711c0f6a.gif)

##### Adjust Alignment

The default Main Axis for a Wrap Widget is the horizontal axis, so adjusting this will change how the child widgets are horizontally distributed in the Wrap widget.

To change the Alignment:

1. Select the **Wrap** from the widget tree or from the canvas area.

2. Move to the Property Editor and scroll down to **Alignment**.

3. Select from the options displayed including **Start**, **Center**, **End**, **Space** **evenly**, **Space** **between**, and **Space** **around**.

![wrap-adjust-alignment.gif](https://docs.flutterflow.io/assets/images/wrap-adjust-alignment-a902a53a8ddb0577580119dbd7c7a464.gif)

##### Adjust Run Alignment

The default Run Axis for a Wrap Widget is the vertical axis, so adjusting this will change how the child widgets are vertically distributed in the Wrap widget.

To change the Run Alignment:

1. Select the **Wrap** from the widget tree or from the canvas area.

2. Move to the Property Editor and scroll down to **Run Alignment**.

3. Select from the options displayed including **Start**, **Center**, **End**, **Space** **evenly**, **Space** **between**, and **Space** **around**.

![wrap-run-alignment.gif](https://docs.flutterflow.io/assets/images/wrap-run-alignment-c25ae3830a53093f5fd8384926c94de7.gif)

##### Adding Items From Bottom

By default, the new items are always added from top to bottom direction. In a very rare case, you may need to change this behavior.

To add items from the bottom to top:

1. Select the **Wrap** from the widget tree or from the canvas area.

2. Move to the Property Editor and scroll down to **Vertical Direction**.

3. Set the Dropdown value to **Up**.

4. Try adding items.

![wrap-add-items-from-bottom.gif](https://docs.flutterflow.io/assets/images/wrap-add-items-from-bottom-69bccc1a469b5e87a62343c4db9742ad.gif)

##### Clipping The Items

If you add several items to the Wrap widget that exceed the size of the patent widget, the Wrap widget will continue to display the overflowing items. However, you can choose to hide the overflowing items using the Clip Behaviour property:

To clip the overflowing items:

1. Select the **Wrap** from the widget tree or from the canvas area.

2. Move to the Property Editor and scroll down to **Clip Behaviour**.

3. Change it to **Clip Content**.

![wrap-clip-items.gif](https://docs.flutterflow.io/assets/images/wrap-clip-items-28e043558d15d6cca365f7aaeea92c68.gif)

***

#### Video guide

If you prefer watching a video tutorial, here's the one for you:

---

### Localization {#localization}

*Learn how to make your app work for different languages.*

**Source:** https://docs.flutterflow.io/concepts/localization

**Localization** (often abbreviated as **l10n**) is the process of making your app work for different languages, regions, and cultures. It involves translating the app's text, adapting date and number formats, and adjusting other elements to meet the cultural expectations of a particular locale.

Difference Between Internationalization and Localization

* [**Internationalization (i18n)**](https://docs.flutter.dev/ui/accessibility-and-internationalization/internationalization): This is the process of setting up your app in such a way that it can easily adapt to various languages and regions without requiring engineering changes. **Note that FlutterFlow handles most of the internationalization for you, so the only thing you need to take care of is localization.**
* **Localization (l10n)**: This is the process of translating the content of your app and adapting it for a specific locale or culture. It involves providing translations for user-visible strings, formatting dates, times, and numbers, and adapting content to meet cultural norms.

In a nutshell, internationalization is about making your app to support multiple languages, while localization is the actual process of translating the content and adapting it to specific locales.

#### Add Multi Language Support

FlutterFlow enables you to translate all text in your app at once using Google Translate or to manually adjust translations as needed. Additionally, you can localize predefined messages, such as permission prompts, authentication snackbars, and other in-app notifications.

Adding multi-language support is essential for making your app accessible to a wider audience. For instance, if your app provides exercise instructions only in English, non-English speakers may find it hard to understand and might choose a different app, even if it’s less effective, simply because it’s available in their language. Implementing a multi-language feature helps your app succeed globally by offering a user-friendly experience for diverse audiences.

To add multi-language support in FlutterFlow, navigate to **Settings and Integrations** > **Languages**, add the languages to support, set a primary language as a fallback, and optionally choose a display language. Then, use **Translate All** for automatic translations and adjust them if needed. Finally, verify translations on different pages by changing the language dropdown in the canvas.

> **Warning:** Changing the primary language after translating all of your text will clear the existing translations for other languages.

#### LanguageSelector Widget

The **LanguageSelector** widget in FlutterFlow allows users to switch to their preferred language in real-time without needing to restart the app. It displays the currently selected language and, when interacted with, presents a list of all available languages for easy selection.

It's particularly useful on onboarding screens or within settings menus to allow users to customize their language preferences.

##### LanguageSelector Properties

You can customize the appearance using the various properties available under the Properties Panel.

![language-selector-properties.avif](https://docs.flutterflow.io/assets/images/language-selector-properties-6e3a8952b1f093573c65fe53125ed6cb.avif)

> **Tip:** By default, the **LanguageSelector** widget does not persist the user's language choice across app sessions. To retain the selected language, enable the **Persist Selection** option under Language Settings.

#### Set App Language Manually \[Action]

Sometimes, you might prefer not to use the default [LanguageSelector widget](https://docs.flutterflow.io/concepts/localization#languageselector-widget) and instead implement a custom widget for language switching. For example, you could create a custom language selection screen that appears when the app first launches.

You can use the **Set App Language** action to let users choose their preferred language from the available options.

> **Info:** Note that this action affects only the app's language and does not modify the device's system language.

![set-app-lang-action.png](https://docs.flutterflow.io/assets/images/set-app-lang-action-d2cd5297fb8801e5739b7a87862b0614.png)

#### Managing Translation

There are two ways you can manage the app text translation:

**Inside Language Settings**

The Language Settings page lists all of your app's text, grouped by page, making it easy to manage translations in bulk.

To manually add or update a translation, make changes directly in the language column and mark the text as **Fixed**. Marking it as **Fixed** will prevent auto translate from overriding your custom translations during the bulk translation process.

To use Google Translate for new or existing text, click **Translate Page.**

![manage-translation-in-language-settings.avif](https://docs.flutterflow.io/assets/images/manage-translation-in-language-settings-c4fbd83ee771d8c104776bf8f537edf4.avif)

**Inside Properties Panel**

You can also add or update translations for individual text directly inside the properties panel. To do so, select the widget (e.g., Text, TextField, etc.), go to the properties panel, and click on the Globe icon. This will open a new panel.

* To manually add or update a translation, make changes directly in the box under the language name.
* To auto-translate for all languages, click on **Google Translate**.

![manage-translation-in-properties-panel.avif](https://docs.flutterflow.io/assets/images/manage-translation-in-properties-panel-068d129b671bcca4e8c18d198cea4785.avif)

#### Translating Predefined Messages

FlutterFlow allows you to manage the translation for the following types of predefined messages.

* **iOS Permission Messages**: iOS permission messages are the prompts shown to iOS users when your app requests access to device features, such as the camera or photo library.
* **Preset In-App Messages**: These are built-in messages that FlutterFlow displays for specific actions, such as authentication and file upload actions.

To add translations for predefined messages, navigate to **Settings and Integrations** > **Project Setup** > **Languages**. Scroll down to the **Translation** section and select the category containing the message you wish to translate.

Start by entering your message in the base language. Then, either use the **Translate Message** button for automatic translation or manually add your translations and mark them as **Fixed** to prevent them from being overridden by auto-translate.

> **Info:** Permission messages are displayed based on the features included in your app. For instance, Camera and Photo Library permission messages appear when a page contains a button with the **Upload Photo/Video action**.

#### Accessing Language-Specific Data

When building a multi-language app, you may need data like the current language code or language-specific text.

In FlutterFlow, you can retrieve the following types of language-related data:

* **Current Language Code**: This provides the ISO language code for the current app language (e.g., en, de, fr).
* **Language-Dependent Text**: Allows you to specify different values for each language. For instance, you might want to display a country flag or name based on the current app language.

These options are accessible through **Set from Variable > Internationalization**.

![retrieve-lang-data.png](https://docs.flutterflow.io/assets/images/retrieve-lang-data-2eef5ceefd42854023441907287fb4f1.png)

#### Localizing Dates

To ensure your app displays dates in formats familiar to users from different regions, you can use the predefined **DateTime Format Options** while displaying dates.

For example, in the United States, dates follow a **month, day, year** format (e.g., 12/31/2023), whereas in India, they use a **day, month, year** format (e.g., 31/12/2023). To accommodate these regional differences, set the format option to `yMd`, a locale-aware format that automatically adjusts date representation based on the user's locale.

![localize-dates.avif](https://docs.flutterflow.io/assets/images/localize-dates-c521dbf44268a20cec711f682e08779d.avif)

> **Tip:** Here are a few more locale-aware formatting options you can use:

* **`yMMMd`** – Formats the date with an abbreviated month and day, e.g., `Dec 31, 2023` (US) or `31 Dec 2023` (India).
* **`jm`** – Displays time with minutes, e.g., `5:30 PM` (US) or `17:30` (Europe).

For custom locale-specific date formats, you can also [**create your own patterns**](https://docs.flutterflow.io/resources/data-representation/global-properties#custom-formatting).

#### Localizing Numbers

Different regions use different symbols for decimal and thousand separators. For example, the U.S. uses a period for decimals and a comma for thousands, while many European countries use the opposite.

To localize the numbers, set the [**Number Format Options**](https://docs.flutterflow.io/resources/ui/widgets/text#formatting-numbers) to **Decimal** and then set the **Decimal Type** to **Automatic**.

![localize-numbers.avif](https://docs.flutterflow.io/assets/images/localize-numbers-4f0c4f5d020f9b74b44201477b9f5b59.avif)

#### Localizing Currency

Currency symbols and their placement vary by locale. For example, in the U.S., the dollar sign appears before the amount (`$1,000.00`), whereas in countries like France, the currency symbol is placed after the amount (e.g., `1 000,50 €`).

To handle this behavior, enable the **Display as Currency** option under Number Format settings and leave the **Currency Symbol** field empty to automatically adjust based on the user’s locale.

![localize-currency.avif](https://docs.flutterflow.io/assets/images/localize-currency-04a7d016aed333db6a0bed72beb35887.avif)

#### Testing

Localization testing is crucial to ensure that all elements work properly across different languages and locales. Here are a few ways to test localization:

* **Change Device Locale**: Test your app by changing the device locale to verify translations and layout adjustments.
* **Use Emulators**: Use Android or iOS emulators to simulate different locales and ensure everything is displaying correctly.
* **Long Texts**: Verify that long translations do not overflow or cause UI issues.
* **Manual Testing**: Manually verify the accuracy of translations, date formats, number formats, etc.

---

### Bottom Sheet {#bottom-sheet}

*A Bottom Sheet is an alternative to a menu or a dialog. It opens from bottom to top and can be dismissed by swiping it from top to bottom. When it opens, it prevents the user from interacting with the rest of the app.*

**Source:** https://docs.flutterflow.io/concepts/navigation/bottom-sheet

A Bottom Sheet is an alternative to a menu or a dialog. It opens from bottom to top and can be dismissed by swiping it from top to bottom. When it opens, it prevents the user from interacting with the rest of the app.

You can use the bottom sheet when you want to perform a small action without creating a separate screen.

#### Types of Bottom Sheet action

Below are the types of Bottom Sheet actions:

1. **Show**: This opens the bottom sheet.
2. **Dismiss**: This closes the bottom sheet.

#### Opening Bottom Sheet

Follow the steps below to add an action that opens the bottom sheet:

1. First, create a bottom sheet [component](https://docs.flutterflow.io/resources/ui/components).

> **Tip:** You can also create one from the 'BottomSheet' [**templates**](https://docs.flutterflow.io/resources/ui/components/creating-components#creating-component-from-template).

2. Select the **Widget** (e.g., Button) from where you want to open the bottom sheet.

3. Select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.

4. Search and select the **Bottom Sheet** (under *Widget/UI Interactions*) action.

5. To open the bottom sheet, select **Show**.

6. **Select Component** as the component you created for the bottom sheet.

7. (Optional) set the **Height** value. You should set the height if you want the bottom sheet to appear only up to some portion of the screen.

8. You can set the **Background** and **Barrier Color** for the bottom sheet.

   ![Set Background and Barrier color](https://docs.flutterflow.io/assets/images/bottom-sheet-background-color-98450a3773ec892d19d8483d7c20002b.png)

9. You can also [pass parameters](https://docs.flutterflow.io/resources/ui/components/creating-components#creating-a-component-parameter) to a bottom sheet component.

10. By default, this type of action blocks the following action (if any) from triggering while this action is in progress. (i.e., meaning the bottom sheet is present on the screen). However, in some cases, you might want to allow the next action (after this) to execute, for example, making an API call immediately after showing the bottom sheet. To do so, enable **Non Blocking** option.

11. By default, **Non Dismissble** option closes the bottom sheet when you click outside of it. To disable this behavior, enable this option.

12. With **Enable Drag** option, you can open and close the bottom sheet using a swipe gesture.

13. Optional: If you are returning any value from the bottom sheet, provide the **Action Output Variable Name**. The result will be stored in this variable.

#### Closing Bottom Sheet

Follow the steps below to add an action that closes the bottom sheet:

1. Select the **Widget** (e.g., Button, ListTile, Container) on which you want to add the action.

2. Select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.

3. Search and select the **Bottom Sheet** (under *Widget/UI Interactions*) action.

4. To close the bottom sheet, select **Dismiss**.

5. If you want to return a value from the current bottom sheet, enable the **Has Value** toggle and pass the value by setting its *Data Type* and *Value Source*. 1. If you enable the *Has Value* option, you must come back to the action that opens this bottom sheet and provide the **Action Output Variable Name**. This will be used to retrieve the value from the bottom sheet.
   2. Now you can use the *Action Output Variable Name* to get the data.

Here is an example of returning the selected user name back to the page.

---

### Deep & Dynamic Linking {#deep-dynamic-linking}

*Learn how to implement deep and dynamic linking in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking

Support for Dynamic Links

On August 25th, 2025, Firebase Dynamic Links will be shut down. Read more about the [**announcement here**](https://firebase.google.com/support/dynamic-links-faq). It's recommended to start exploring alternative solutions like [**Branch.io**](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#branch-deeplinking-library) for link management and deep linking.

Adding deep and dynamic linking allows you to share a special type of link that takes the user right inside the specific page of your app. You can also send the custom data with a link to load the page content based on the data.

For example, you could share an interesting social media post with your friends, and they can directly access its content without manually searching the post inside the app. It just works like any website link would work.

The figure below illustrates how it works:

![img.png](https://docs.flutterflow.io/assets/images/img-16416344289e75695c203df1f638b767.png)

Deep and Dynamic link flow

When you click on the link, first, it checks if the app is installed. If not, the link opens the Playstore or Appstore (based on your device) to install the app. After installing, if the page requires authentication, you'll see a login page. After successful login, you can access the content shared with you.

The best thing to note here is that even if the app has a different flow for accessing the page content (e.g., Home Page -> All Posts -> Single Post), you can bypass the flow and directly open a specific page (e.g., Single Post).

#### Deep Link

The deep link allows you to create a URL that will open a specific page in your app. For the deep links to work, you must have the app installed on your device.

##### URL Scheme (structure)

The deep link consists of three parts. It begins with the scheme followed by the host and page name, such as `designersapp://designersapp.com/profile`.

![img\_1.png](https://docs.flutterflow.io/assets/images/img_1-e9bcc7b4c7a527a117dd98d2e4e33f33.png)

If the page name is not provided (i.e. `designersapp://mydesignersapp.com/)`It will open the app's landing page.

![img\_2.png](https://docs.flutterflow.io/assets/images/img_2-67ea88901a2b863a7c95e0e5858a017c.png)

##### Adding Deep Link

Let's build an example of sharing and opening a profile page using the deep link. The example looks like the below:

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/deep-link-example.gif?alt=media\&token=d6f40d74-f510-4f49-8026-9ccc87896ff4)

Sharing and opening a deep link

The steps to add the deep link are as follows:

1. [Set URL scheme](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#1-set-url-scheme)
2. [Setting page URL](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#2-setting-page-url)
3. [Sharing deep link](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#3-sharing-deep-link)
4. [Testing deep link](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#4-testing-deep-link)

###### 1. Set URL scheme

In this step, You will set the URL scheme. To do that:

1. Navigate to **Settings & Integrations > General > App Details.**

2. If you want to add deep linking on multiple pages and all of them require users to log in, turn on the **Pages Requires Authentication by Default**.

3. In **URL scheme** fields, by default we add the values based on your project name. To change it, enter the **scheme** **name** (before "://") and **hostname** (after "://").

4. If you want users to navigate back to the home page instead of closing the app when they press the back button from a deep link page, enable the **Pages Are Subroutes of Root Page** option.

![img\_3.png](https://docs.flutterflow.io/assets/images/img_3-efe840e2cf4de2fb903743d38cf7ebe5.png)

> **Tip:** We recommend enabling this option to increase user engagement with your app.

###### 2. Setting page URL

The page URL points to the specific page in your app, which is used on the Web and for deep linking on mobile.

To set the page URL:

1. Select the page that you would like to open via a deep link.

2. Move the **properties panel** on the right and open the **Route Settings** section.

3. By default, the Route is the current page name. Edit this if you want a different name in the page URL.

4. By default, the page does not require authentication when it opens via the deep link. However, checkmark the **Requires Authentication** if your app works only after login.

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/set-page-url.gif?alt=media\&token=4ec81b75-a5b0-4130-8e3c-dda9aacd1c84)

Setting page URL

###### 3. Sharing deep link

You can share the deep link of the current page by adding the [share action](https://docs.flutterflow.io/concepts/navigation/share-action).

To share the deep link of the current page:

1. Select the page that you would like to open via a deep link.

2. From that page, select any widget (e.g. share button) from the widget tree or the canvas area.

3. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action flow Editor** in a new popup window.

   1. Click on the **+ Add Action**.
   2. On the right side, search and select the **Share** action.
   3. Set the **Value Source** to **From Variable**.
   4. Set the **Source** to **Global Properties**.
   5. Set the **Available Options** to **Link To Current Page** and click **Close**.

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/sharing-deep-link.gif?alt=media\&token=05521a84-43e4-4c21-869c-5ecdcd1e34c6)

Sharing deep link

###### 4. Testing deep link

Deep links can not be tested in Run Mode. Instead, you will need to test the deep links on a real device/emulator.

Before you test the deep link, you need to get it first. The easiest way to get it is to run the app on a device/emulator, click on the share button and then copy the deep link.

Now, you can test the deep link in two ways:

Using CLI tools

If you have Android Studio with the SDK platform tools installed, you can run the following command in the terminal and replace it with your deep link.

Copy

```
adb shell am start -a android.intent.action.VIEW \
    -c android.intent.category.BROWSABLE \
    -d "designersapp://designersapp.com/profile"
```

Using Firefox mobile browser

You can also test the deep link in a Firefox mobile browser. To do so, open the browser, paste the URL in the search bar, open the options menu and click on the **Open in app**.

Here is how you do it:

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/deep-link-example.gif?alt=media\&token=d6f40d74-f510-4f49-8026-9ccc87896ff4)

Using Firefox mobile browser to open the deep link

#### Dynamic Links with Firebase Dynamic Links \[Deprecated]

The dynamic link opens a specific page in your app. Unlike the deep link, the dynamic link survives the app install. That means if the user has not installed the app, they can be taken to the respective store to install the app. After the app is installed, users can be taken straight to the intended app page.

For the dynamic link to work, you need to enable the [deep link](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#adding-deep-link). You can think of a dynamic link as the additional benefit of the deep link.

> **Note:** FlutterFlow uses [**Firebase Dynamic Link**](https://firebase.google.com/docs/dynamic-links) (a product from Firebase) to create dynamic links.

Let’s walk through an example of sharing and opening a profile page using a dynamic link. The example will look like this:

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/deep-link-example.gif?alt=media\&token=d6f40d74-f510-4f49-8026-9ccc87896ff4)

Dynamic link example

The steps to add the dynamic link are as follows:

1. [Setting up a domain](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#1-setting-up-a-domain)
2. [iOS setup](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#2-ios-setup)
3. [Set URL scheme](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#3-set-url-scheme)
4. [Setting page URL](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#4-setting-page-url)
5. [Sharing dynamic link](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#5-sharing-dynamic-link)
6. [Testing dynamic link](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#6-testing-dynamic-link)

##### 1. Setting up a domain

The dynamic link requires a domain name that will be used as the URL prefix in the link.

To set up the domain name, follow the steps below:

1. Open the [Firebase console](https://console.firebase.google.com/), and click on \*\*Dynamic Link \*\* (on the left side menu).

2. Click on the **Get Started** button. This will open a popup.

3. Enter the domain name. If you don't own a domain, you can select the free **Google Provided Domain** that ends with a **page.link**. To set up your own domain, follow the guide [here](https://firebase.google.com/docs/dynamic-links/custom-domains).

4. If you chose Google Provided Domain, you could **Finish** the setup.

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/set-up-domain.gif?alt=media\&token=219b0780-3632-478b-918c-05fba91508a3)>

Setting up a domain for the dynamic link

##### 2. iOS setup

You must complete additional configuration for the dynamic link to work on the iOS devices.

Setting up iOS includes:

###### 2.1 Add App Store and Team ID to the Firebase project

To add the App Store and Team ID to the Firebase project:

1. Open the [Firebase console](https://console.firebase.google.com/), and click on **Project Overview** (on the left side menu).

2. Select the iOS project and click on the Settings (gear) icon inside.

3. Scroll down to see your selected iOS project.

4. Find the **App Store ID** field, click on the edit icon (pencil icon), enter the ID, and click \* *Save*\*. To know where is your App Store ID, click on the question mark icon beside the label.

5. Similarly, find the **Team ID** field, click on the edit icon (pencil icon), enter the ID, and click **Save**. To know where is your Team ID, click on the question mark icon beside the label.

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/add-app-store-team-id.gif?alt=media\&token=116cb42a-9bc6-4af5-a9d6-cc5a8a5906f7)

Adding App Store and Team ID to the Firebase project

###### 2.2 Adding Associated Domain capability to App Store

To add the Associated Domain capability on App Store:

1. Open the [Apple Developer homepage](https://developer.apple.com/account) and select \* *Certificates, IDs & Profiles*\*.

2. Select **Identifiers** (far left menu) and then click on your app identifier.

3. Checkmark the **Associated Domains** and click **Save**.

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/add-capability.gif?alt=media\&token=90315580-9480-40d4-a85b-1957c6d759e2)

Adding Associated Domain capability to App Store

##### 3. Set URL scheme

In this step, You will set the URL scheme. To do that:

1. Navigate to **Settings & Integrations > General > App Details.**

2. If you want to add deep linking on multiple pages and all of them require users to log in, turn on the **Pages Requires Authentication by Default**.

3. Also, turn on the **Use Firebase Dynamic Links**.

4. In **URL scheme** fields, by default, we add the values based on your project name. To change it, enter the **scheme** **name** (before `://`) and **hostname** (after `://`).

5. If you want users to navigate back to the home page instead of closing the app when they press the back button from a deep link page, enable the **Pages Are Subroutes of Root Page** option. \* *Tip*\*: we recommend enabling this option to increase user engagement with your app.

![img\_4.png](https://docs.flutterflow.io/assets/images/img_4-982d4b2527f6ec15aef536da88b9733a.png)

##### 4. Setting page URL

The page URL points to the specific page in your app, which is used on the Web and for deep linking on mobile.

To set the page URL:

1. Select the page that you would like to open via a dynamic link.

2. Move the **properties panel** on the right and open the **Route Settings** section.

3. By default, the Route is the current page name. Edit this if you want a different name in the page URL.

4. By default, the page does not require authentication when it opens via the dynamic link. However, checkmark the **Requires Authentication** if your app works only after login.

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/set-page-url-dynamic-link.gif?alt=media\&token=537674be-d58e-431f-940d-59afda3089d6)

Setting page URL

##### 5. Sharing dynamic link

You can share the dynamic link of the current page by adding the [\*\*Generate Current Page Link \*\*](https://docs.flutterflow.io/concepts/navigation/generate-current-page-link) action and then sharing it using the [**Share Action**](https://docs.flutterflow.io/concepts/navigation/share-action).

To share the dynamic link of the page:

1. Select the page that you would like to open via a deep link.

2. Select any widget (e.g., share button) from the widget tree or the canvas area.

3. First, add the action to [Generate Current Page Link](https://docs.flutterflow.io/concepts/navigation/generate-current-page-link#defining-generate-current-page-link-action).

4. Now chain the next action to share the dynamic link.

5. To do that, click on the **+** button at the bottom of the box and select **Add Action**.

6. On the right side, search and select the **Share** action.

7. Set the **Value Source** to **From Variable**.

8. Set the **Source** to **Widget State**.

9. Set the **Available Options** to the **Current Page Link** and click **Close**.

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/sharing-dynamic-link.gif?alt=media\&token=f9caa24f-efbf-47f2-af9c-ee1172de5863)

Sharing dynamic link

##### 6. Testing dynamic link

Dynamic links can not be tested in Run Mode. Instead, you will need to test the links on a real device/emulator.

Before you test the dynamic link, you need to get it first. The easiest way is to run the app on a device/emulator. Click on the share button and then copy the dynamic link.

Now you can test the link in a Firefox mobile browser. To do so, open the browser and paste the URL into the search bar.

Here is how you do it:

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/dynamic-link-demo-testing.gif?alt=media\&token=5b218ef8-198d-4941-be12-640e9babb3e4)

Testing Dynamic Link

#### Passing Data with a Link

In most cases, you might want to pass custom data with a link. For example, you send the product page link with a discount code and share the profile page with its profile ID. Passing custom data with the link can be used to retrieve the information required to display on the page.

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/pasing-data.gif?alt=media\&token=2fc5c267-fc68-4f4f-aa39-41597a5b5e48)

Passing profile id in the link

To pass custom data with the link, you need to have the following:

1. Make sure you have a parameter defined on a page you want to pass in a dynamic link.

![img\_5.png](https://docs.flutterflow.io/assets/images/img_5-0f8209160033e995ee2a0e3a6fcc4434.png)

Adding parameter on page

2. In the **Route Settings**, include a parameter as part of the route by prefixing it with a colon (**:**) for example, `profilePage/:profileId`.

![img\_6.png](https://docs.flutterflow.io/assets/images/img_6-d13a06bd905292dea8a8211cb0d81484.png)

Including a parameter in the route

That's all you need to pass custom data with a **Deep Link** or **Dynamic Link**.

#### Deep Links with Branch.io

Since **Firebase Dynamic Links** have been deprecated and can no longer be used for new Firebase projects, we can integrate a powerful alternative: **[Branch.io](https://branch.io/)** — a cross-platform solution for deep linking and deferred linking.

With Branch, we can support robust deep linking inside FlutterFlow apps without writing a backend from scratch.

##### Branch.io Configuration

Start by setting up your project in the [Branch Dashboard](https://dashboard.branch.io). Once you’ve created a project:

**1. Note down your Branch Key**

Once you create a project, the first thing you’ll need to do is note down your **Branch Key**.

This key uniquely identifies your app and will be required later when setting up your FlutterFlow configuration.

**2. Set up Redirect Links**

In the Branch dashboard, you’ll find settings to define fallback URLs — these determine where users are sent if your app isn’t installed. Typically, you would redirect users to the App Store, Play Store, or a custom landing page.

Setting up redirects is important because it ensures that your links don't break and that users always have a seamless experience, even if they need to install the app first.

**3. Create a Smart Link**

After setting up your project and redirects, you can create a new Smart Link from the **Quick Links** tab in the Branch dashboard. Here you’ll be able to set a link title, alias, add analytics tags, and customize the social media preview (such as the image, title, and description).

Once saved, Branch will generate a Smart Link that’s ready to use across your campaigns and app flows.

Here's a short demo:

##### FlutterFlow Configuration Setup

To make **Branch Smart Links** work in your FlutterFlow app, you’ll need to update the native configuration files via the **Custom Code** tab in your project.

1. First, create environment variables for:

   * `branchHostUrl` (e.g., `brnch4.app.link`)
   * `branchKey` (your Branch key, use it for production and optionally `branchKeyTest` for dev environments. You can toggle modes through Branch dashboard and also through FlutterFlow environment toggling).

2. Then navigate to, FlutterFlow > Custom Code

**🔧 Android Setup**

1. Create two variables in `AndroidManifest.xml` file named `branchKey` and `branchHostUrl` and bind them to the environment variables we earlier created.

2. Add an `intent-filter` block to your **Main Activity** through the **Activity Tags** hook:

```
<intent-filter android:autoVerify="true">
  <action android:name="android.intent.action.VIEW"/>
  <category android:name="android.intent.category.DEFAULT"/>
  <category android:name="android.intent.category.BROWSABLE"/>
  <data android:scheme="https" android:host="{{branchHostUrl}}"/>
</intent-filter>
```

3. Add an **App Component** block for meta-data:

```
<meta-data android:name="io.branch.sdk.BranchKey" android:value="{{branchKey}}"/>
<meta-data android:name="io.branch.sdk.TestMode" android:value="false"/>
```

**🍎 iOS Setup**

1. In `Info.plist`, add a new variable called `branchKey` and bind it to the environment variable.

2. In `Info.plist`, add the following code snippet.

```
<key>branch_key</key>
<string>{{branchKey}}</string>
```

3. In `Runner.entitlements`, add a new variable called `branchHostUrl` and bind it to the environment variable.

4. In `Runner.entitlements`, add the following code snippet.

```
<key>com.apple.developer.associated-domains</key>
<array>
  <string>applinks:{{branchHostUrl}}</string>
</array>
```

Branch automatically hosts and serves the `apple-app-site-association` file needed for Universal Links. You don’t need to manually upload it to your domain.

**FlutterFlow Routing Setup**

FlutterFlow also defines a Custom URI Scheme (like `myapp://`) by default. Even if you're using Branch for web-based Smart Links, it’s a good idea to keep this in sync.

1. Go to: Settings & Integrations > App Settings > App Details

2. Scroll to **Routing & Deep Linking** section.

3. Under Custom URI Scheme, match the URI host/domain to what’s defined in your Branch dashboard (e.g., `brnch4://` or `dreambrush://`).

![custom-uri.png](https://docs.flutterflow.io/assets/images/custom-uri-20835b4d1c0d276769203e5441f65618.png)

Even if your links mainly use `https://`, FlutterFlow's routing engine may still use the custom URI internally. Keeping this field consistent prevents confusion or route mismatches.

You're now ready to use Branch Smart Links in a FlutterFlow app with seamless deferred deep linking, App/Universal Link verification, and environment-based configuration.

##### Integrate Flutter Branch SDK

To integrate Branch with your FlutterFlow app, you'll use the [`flutter_branch_sdk`](https://pub.dev/packages/flutter_branch_sdk) Dart package. This will allow your app to listen to Branch links and respond accordingly.

1. Go to your **FlutterFlow project > Settings and Integrations > Pubspec Dependencies** tab, and add the following dependency.

```
flutter_branch_sdk: ^5.0.1
```

Make sure to use the latest version available from [pub.dev](https://pub.dev/packages/flutter_branch_sdk)

2. Create a Custom Action to initialize the Branch SDK. This ensures the Branch session is set up when your app starts.

```
import 'package:flutter_branch_sdk/flutter_branch_sdk.dart';

Future initBranch() async {
  // Add your function code here!
  await FlutterBranchSdk.init();
}
```

Call this action inside the **Final Actions** of your `main.dart`.

3. Create another custom action to listen for Branch link clicks and optionally route the user:

```

// Automatic FlutterFlow imports
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/custom_code/actions/index.dart'; // Imports other custom actions
import '/flutter_flow/custom_functions.dart'; // Imports custom functions
import 'package:flutter/material.dart';
// Begin custom action code
// DO NOT REMOVE OR MODIFY THE CODE ABOVE!

import 'dart:async';
import 'package:flutter_branch_sdk/flutter_branch_sdk.dart';
import 'package:flutter/services.dart';

StreamSubscription<Map>? _branchSubscription; // stream subscription that listens for branch links
final Set<String> _handledBranchLinks = {};

Future handleBranchDeeplink(Future Function(dynamic data) onLinkOpened) async {
   // Add your function code here!

   if (_branchSubscription != null) return; // If already listening, ignore link

   _branchSubscription = FlutterBranchSdk.listSession().listen(
           (data) async {
      final clicked = data['+clicked_branch_link'] == true;
      if (!clicked) return;

      final uniqueId = data['~referring_link'] ?? data['deeplink_path'] ?? '';

      if (_handledBranchLinks.contains(uniqueId)) return;
      _handledBranchLinks.add(uniqueId);

      await onLinkOpened(Map<String, dynamic>.from(data)); // call action defined by user & pass the link data.
   },
   onError: (error) {
      if (error is PlatformException) {
         print('[Branch] PlatformException: ${error.code} - ${error.message}');
      } else {
         print('[Branch] Unknown error: $error');
      }
   },
);
}
```

You can pass custom key-value pairs like `"page": "paywall"` or `"navigation_type": "bottom_sheet"` when creating the Branch link, and retrieve them here to decide which screen to navigate to in FlutterFlow.

Be sure to test both fresh installs (deferred deep links) and existing app sessions to confirm that your actions run as expected.

> **Tip:** For a complete walkthrough, check out the tutorial video:

[YouTube video player](https://www.youtube.com/embed/nEBot6-zhfY?si=y-flWx8zoGH8mgjM)

#### Branch Deeplinking Library

If you’d prefer not to integrate Branch.io from scratch, we have introduced the **Branch Deep Linking Library** that you can import from the Marketplace completely free.

This library sets up everything you need for routing users into your app using Branch’s smart links — with native configuration, link handling, and deep link helpers already wired in.

##### Install Library

You can install the [Branch Deeplinking Library from the Marketplace](https://marketplace.flutterflow.io/item/oAco1HzQHxtOVE1ssTcC). Refer to the [Add Library Item](https://docs.flutterflow.io/marketplace/adding-purchasing-item#add-library-item) instructions to see how to add it to your account.

##### Branch Setup

You’ll need three values from your Branch dashboard:

* **Branch Key**: Your production or test key from the Branch dashboard.

* **Custom Link Domain**: Your primary Branch link domain (e.g., yourapp.app.link). This is used to generate and handle smart links.

* **Alternate Link Domain**: An additional Branch domain (e.g., yourapp-alternate.app.link) that points to the same link data and behavior. This is recommended for ensuring better deliverability across platforms and channels, and must be included in your platform configuration.

We recommend storing these values in Environment Variables so you can:

* Manage them per environment (e.g., dev vs prod Branch keys).
* Easily assign them to the library’s configuration when adding it to a project.

**Adding Library Values**

When you add the **Branch Deep Linking Library** to your project (ensure you are on +0.0.7 and above), it will prompt you to provide four values:

* `branchApiKey`
* `branchLinkDomain`
* `branchAlternateLinkDomain`
* `isTestMode`

Use the environment variables you created to populate these values.

> **Info:** `isTestMode` should be set to false when running your app in production.

Here’s a quick demo to show how to configure those values inside your library panel.

###### Initialize the Branch SDK

Open your `main.dart` file in FlutterFlow and add the `initBranch` custom action under the **Final Actions** section. This ensures the **Branch SDK** is initialized when your app launches.

##### Handle Branch Deeplink \[Custom Action]

To receive and act on deep link data, go to your **Entry Page** or **Logged-In Page** and add the `handleBranchDeeplink` action as the first action in the page flow.

This `handleBranchDeeplink` action listens for incoming Branch Deeplinks and handles routing logic. This action should be added to your **Entry Page** or **Logged-In Page** under the **onPageLoad** trigger. It initializes a stream listener that waits for Branch links to be opened (either deferred or direct). Ensure this is the first action of your **on Page Load** action trigger.

**`onLinkOpened` Action Callback**

When a link is received, the `onLinkOpened` callback is triggered with the [**link data**](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#linkdata-action-parameter), allowing you to perform custom navigation or logic. You can perform your navigation logic in this action callback.

###### `linkData` Action Parameter

The `handleBranchDeeplink` action receives a `linkData` object that contains all the metadata sent with the link. The `linkData` parameter is a Map containing useful information from the Branch link.

In the Dreambrush app example, we get the following link data:

```
{
   "$og_title": "Check out my Ai Image on DreamBrush!",
   "$publicly_indexable": true,
   "imageId": "QiC94EaGNoonEKzln07A",
   "~creation_source": 4,
   "$og_description": "This image was created with DreamBrush app. You can check it out here.",
   "+click_timestamp": 1750099254,
   "$match_duration": 100000,
   "~feature": "Ai Image Creation",
   "$tags[0]": "generation",
   "+match_guaranteed": true,
   "$alias": "",
   "$canonical_identifier": "/imageDetails/QiC94EaGNoonEKzln07A",
   "+clicked_branch_link": true,
   "~id": "1461141612502859827",
   "+is_first_session": false,
   "~campaign": "Image Generation",
   "~referring_link": "https://dreambrush.app.link/DZ9liDTc6Tb",
   "~channel": "Share"
}
```

Link Structure

Your link data might not look *exactly* like the example shown above. However, it will follow a **similar structure** with comparable keys and values.

Some of the important keys we should know about:

* **`$canonical_identifier`:** The original route path used when the link was generated (e.g., `/imageDetails/:id`). You can explicitly set this value when creating a link through the **[Generate Link](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#generate-link-custom-action)** action. If you don’t set it, Branch will infer it based on the link's destination or content metadata.

* **`~referring_link`:** The full Branch URL that was clicked.

* **`$og_title`:** This is the headline that will appear in the link preview. This is set by the user through the **[Generate Link](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#generate-link-custom-action)** action.

* **`$og_description`:** This is the description text shown below the title in the link preview. This is set by the user through the **[Generate Link](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#generate-link-custom-action)** action.

* **`~channel`**, **`~feature`**, **`~campaign`** and **`$tags[0]`** are part of Branch’s user-defined analytics and attribution metadata. These fields are explicitly set by users when creating a link (e.g., via the **[Generate Link](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#generate-link-custom-action)** action), and they help organize and analyze your link performance across platforms and campaigns.

* **`page`:** This is a suggested custom key that can be set by the user when generating the link. It typically defines the target page or screen the app should navigate to when the link is opened (e.g., "paywall", "productPage", "onboardingStep2"). While not a reserved Branch key, it's a commonly used naming convention for handling deep links and routing logic within the app.

* Any other custom parameters added during link creation (e.g., `productId`, `referrer`, etc.). Ensure the key and value are both `String`.

This lets you write flexible, conditional navigation logic based on what was shared. For example, in the following example, we can even show a bottom sheet based on the page value.

Use the link data from this callback to:

* Navigate to a page.
* Show a bottom sheet.
* Load content from Firestore using a referenced ID.

###### Using Global Context to Navigate

In certain app structures, especially when the home page is removed from the navigation stack early, standard navigation using the local context may fail. To ensure deep linking and routing continue to work reliably in these scenarios, you can override the local context with the global navigator context.

This approach ensures that navigation logic is not tied to the widget hierarchy at the time of execution, making it more robust and flexible.

See a **[detailed example](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#dreambrush-example)** using the DreamBrush app.

Testing Deeplinks

It’s recommended to test deep links on a **physical device**, as link verification (especially for Universal Links or App Links) may not consistently work on emulators or simulators. We recommend using **[Local Run](https://docs.flutterflow.io/testing/local-run)** to run your apps on physical devices.

##### Generate Link \[Custom Action]

The `generateLink` action allows you to create a custom Branch Smart Link directly from your FlutterFlow app.

This is especially useful when you want to let users:

* Share app content (like a post, product, or image).
* Invite others with referral codes.
* Trigger deep links that take recipients to specific app screens.

The action accepts the following parameters:

* **`canonicalIdentifier`** – A unique path for the content (e.g., `/imageDetails/:id`). This becomes the key reference used when routing the user back into the app.

* **`title`** – The link's title (used in social previews or analytics).

* **`description`** – (Optional) A short description of the content.

* **`metadata`** – A dynamic map of custom parameters to include with the link (e.g., page: "imageDetails", imageRef: "abc123", etc.)

* **`linkProperties`** – A dynamic map for configuring how the link behaves (e.g., set the `feature`, `channel`, `campaign`, or `stage` for analytics).

JSON maps

Due to a limitation, if you plan to leave map-type variables (like `metadata` or `linkProperties`) empty, you must still pass them as **empty maps**, not `null`.; Ensure all keys and values are **plain strings**, avoid nested JSON or non-string types.; Incorrect structure may cause the Link Generation action to fail silently.

##### Branch Helper Functions

These functions help you safely work with deep link data, extract values, and conditionally navigate based on link metadata.

* **`isTargetingPage(linkData, targetPage)`** - Checks whether the page value in the link data matches a specific screen name. The `page` parameter is set by the user when generating the link from Branch dashboard or FlutterFlow. For example, if the target page value in your deep link is "paywall", you can use this function to check for this value and navigate accordingly.

* **`getCanonicalIdentifierFromLink(linkData)`**: Helper function that returns the canonical path (e.g., `/imageDetails/abc123`) that was originally attached to the smart link. Useful for extracting the base route or content reference associated with the shared link.

* **`getReferringLinkFromLink(linkData)`**: Helper function that retrieves the full Branch smart link URL from the data (typically under the `~referring_link` key). Useful for tracking, analytics, or verifying the source of the link.

* **`getLastPathSegmentFromMap(linkData, key)`**: Extracts the last path segment (e.g., `abc123`) from a URI stored inside a link data field (e.g., `/imageDetails/abc123`). This is especially useful when your deep link contains a structured path, like `/imageDetails/abc123` and you want to retrieve just the ID (`abc123`).

* **`getLinkValue(linkData, key)`**: Safely retrieves any single value from the link data Map. Returns null if not found. (e.g., retrieving `showPromo` attribute value from the `linkData`).

> **Warning:** If you're trying to retrieve default Branch keys like `~channel` or `$canonical_identifier`, make sure to include the special character (e.g., `~` or `$`) as part of the key string.

* **`createLinkProperties(...)`**: Returns a Branch Link Properties map used when generating a smart link. You can define values like: feature, campaign, stage, channel, alias or tags or custom fallback URLs. Useful for organizing and tracking generated links for marketing or referrals.

##### DreamBrush Example

In the DreamBrush app, we can use `generateLink` after a user finishes generating an image. The link could include:

* **canonicalIdentifier**: Current Page Route that is `/imageDetails/:imageRef`.
* **page**: Target page name `imageDetails`.
* **title**: "Check out my AI image!"

This link can then be shared via WhatsApp, email, or social media — and when clicked, it brings the recipient directly to that content inside the app.

Here's a quick example of generating a Branch link from a page that uses a **Firebase Document ID** as a route parameter.

Now in your `handleBranchDeeplink` action callback, add the additional logic to handle such custom links:

To demonstrate how to use the global context for navigation, add a new **Execute Custom Code** Action just before the **Navigate To** Action, and insert the following code.

```
final context = appNavigatorKey.currentContext!;
```

This ensures that the navigation logic uses the global navigator context, which is essential if your app structure removes the home page early in the lifecycle. In such cases, relying on a local context may cause deep linking to fail—using a global context guarantees that navigation still works reliably.

Paid Plans

Note: The **Execute Custom Code** Action is available only on the [**paid plans**](https://www.flutterflow.io/pricing).

##### FAQs

Why isn't my deep link working when I navigate to another page from the home page?

This often happens because the Home Page gets removed from the navigation stack, especially when **Allow Navigate Back** is disabled in the **Navigate To** Action.

Since the deep link handler is typically defined on the Home Page, it gets disposed once the page is removed, causing deep links to stop working when triggered later.

✅ Preferred Solution: **Use Global Context for Navigation**

Instead of relying on the Home Page's presence to handle deep links, configure your navigation logic to use the global navigator context. This ensures navigation will work even if the Home Page has been removed from the stack.

You can do this by adding an **Execute Custom Code** Action before the **Navigate To** Action.

See the **[complete example](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#using-global-context-to-navigate)**.

✅ Alternative (but limited) Solution: **Keep the Home Page in Stack**

If you're not using global context, you can prevent this issue by keeping the Home Page in memory:

Enable "Allow Navigate Back" on any navigation actions from your Home Page, even if the navigation isn't triggered from deep links directly.

This keeps the Home Page alive so it can continue listening for deep link events.

Why is my Branch link generation failing?

This often happens because one or more of the inputs passed to the action (like `metadata` or `linkProperties` or `customParams` when using `createLinkProperties` helper function) contains invalid JSON formatting.

Branch expects these values to be passed as a map of plain `String` key-value pairs, not as nested JSON, objects, or dynamic types.

Ensure both **Key and Value's expected type** is `String` and `String` and try again.

Why isn’t deep linking working when testing from a simulator?

Deep linking, especially Universal Links and deferred deep linking may not work reliably on iOS or Android simulators/emulators due to platform limitations.

Simulator Limitations:

* **iOS:** Simulators cannot verify Universal Links properly (no App Store, limited AASA domain support).

* **Android:** Some versions fail to auto-verify App Links or handle deferred deep links without Play Services.

✅ Recommended:

Always test deep linking on a physical device for accurate behavior.

---

### Generate Current Page Link {#generate-current-page-link}

*Learn how to generate the current page link in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/concepts/navigation/generate-current-page-link

Using this action, you can generate the dynamic link for the current page.

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/dynamic-link-demo.gif?alt=media\&token=f6aee025-782a-45b9-baa6-3d357ca30cec)

Sharing and opening a dynamic link

Prerequisites

Before adding this action, ensure you have performed all the steps to [**add the dynamic link**](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#deep-links-with-branchio).

#### Defining Generate Current Page Link action

Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.

1. Select the **Widget** (e.g. share button) on which you want to define the action.

2. Select **Actions** from the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) (the right menu), and click **Open**. This will open an **Action flow Editor** in a new popup window.

   1. Click on the **+ Add Action**.
   2. On the right side, search and select the **Generate Current Page Link** action and click **Close**.

![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/adding-share-action.gif?alt=media\&token=b94f6e86-1c1f-4a19-ad0b-b83cc66fc08f)

Adding Generate Current Page Link action

---

### Launch URL [Action] {#launch-url-action}

*Learn how to use the Launch URL Action in FlutterFlow to open URLs with supporting apps.*

**Source:** https://docs.flutterflow.io/concepts/navigation/launch-url

The Launch URL Action lets you specify a URL that will be opened using an app supporting it. If there is more than one app that can handle the specified URL, the user will be presented with a dialog from where one of the apps can be selected.

#### Adding Launch URL Action

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Container, Button, etc.) on which you want to add the action.
2. Select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.
3. Click on the **+ Add Action**.
4. On the right side, search and select the **Launch URL** (under widget/UI Interactions) action.
5. In the *URL Value Type* property, select either **Specify URL** (to add the URL as a String) or **From Variable** (to use the value stored in a String variable).
6. If using **Specify URL**, enter the URL that you want to use in the **URL** field. For example, you can enter "[https://flutter.dev](https://flutter.dev/)" to open the Flutter webpage.
7. If using **From Variable**, select the **Source** from which to fetch the URL value. You can also specify a **Default Value** that will be used when the variable value is not set (i.e. null).

![launch-url.avif](https://docs.flutterflow.io/assets/images/launch-url-d7c613a47c466132a877ded81754a642.avif)

***

#### URL schemes

A URL scheme is a way to define how different types of links, such as webpages, phone numbers, SMS messages, and emails, should be handled by an app or browser. The following are some common URL schemes that can be handled by an external app present on the user's device.

##### Open a webpage

This URL scheme for loading up a webpage can be defined in this format:

###### Scheme

`http:<webpage URL link>`

`https:<webpage URL link>`

###### Example

`https://flutter.dev`

![webpage.gif](https://docs.flutterflow.io/assets/images/webpage-e77c8217ba0e3808009841e02573d1ea.gif)

##### Use a phone number

This URL scheme helps to handle phone numbers inside your app. Using this, you can easily initiate a phone call to the provided phone number from the user's device.

###### Scheme

`tel:<phone-number>`

###### Example

`tel:2125551212`

![phone.gif](https://docs.flutterflow.io/assets/images/phone-0d973c2de6a23a5c6f6797c80608194d.gif)

##### Compose a text message

This URL scheme lets you redirect users from your app to compose and send an SMS message to a specified phone number.

###### Scheme

`sms:<phone_number>`

###### Example

`sms:2125551212`

![text-message.gif](https://docs.flutterflow.io/assets/images/text-message-da7b8687d93f06c971fecff069d70cbd.gif)

##### Create an email

This URL scheme helps you to launch an email app on the user's device. It allows you to pass the *email to*, *subject*, and *body* to the app so that you have these fields prefilled with details as the email app is opened.

###### Scheme

`mailto:<email_address>?subject=<subject>&body=<body>`

###### Example

`mailto:name@example.org?subject=Welcome%20to%20FlutterFlow&body=Hey%20there`

This will pass the following details to the email app:

***mailto:*** <name@example.org>, ***subject:*** Welcome to FlutterFlow, ***body:*** Hey there

![ceate-email.gif](https://docs.flutterflow.io/assets/images/ceate-email-3b1a5a099752899687f96c37882c340d.gif)

---

### Overview {#overview}

*Learn how to add navigation in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/navigation/overview

Navigation in FlutterFlow is a crucial aspect of app development, enabling users to move between different pages or screens. This is achieved through a system of routing, where each page is assigned a unique route identifier. Understanding how navigation works and what happens to the navigation stack under the hood can help you create a seamless user experience.

#### What are Routes?

Routes are essentially the paths that define different screens or pages within the app. Each route is associated with a specific screen and has a unique identifier that allows the app to recognize and navigate to it. For example, a route could point to the home screen, a product details page, or a user profile page.

| Page            | Route            |
| --------------- | ---------------- |
| Home            | /home            |
| Product Details | /product-details |
| Cart            | /cart            |

#### Navigation Stack Logic

The **navigation stack** is a data structure that keeps track of the routes as they are pushed and popped off the stack. It follows the Last In, First Out (LIFO) principle, meaning the last screen that was navigated to is the first one to be navigated away from when the user presses the back button.

Here’s how the navigation stack logic works in FlutterFlow:

##### 1. Pushing a Route

When you navigate to a new screen, that route is pushed onto the top of the stack.

For example, if you are on the home screen and navigate to the profile screen, the profile screen route is pushed onto the stack.

![pushroute.avif](https://docs.flutterflow.io/assets/images/pushroute-cc5b83d167d62aa624456a276a131eff.avif)

##### 2. Popping a Route

When you navigate back, the topmost route is popped off the stack, and the previous screen becomes visible.

For example, if you are on the profile screen and press the back button, the profile screen route is popped off, revealing the home screen.

![poproute.avif](https://docs.flutterflow.io/assets/images/poproute-9da2a09d047959456e62dda3b2b3c9c9.avif)

##### 3. Replacing a Route

Sometimes, you might want to replace the current route with a new one without adding to the stack. This is useful for actions like logging in, where you don’t want users to navigate back to the login screen after they have logged in.

For example, after a successful login, replace the login screen route with the home screen route.

![replaceroute.avif](https://docs.flutterflow.io/assets/images/replaceroute-a31973716265cb977d00fc85c50fd311.avif)

#### Navigation Actions

In FlutterFlow, there are three main navigation actions you can use to navigate between different screens in your app. Here are they:

1. [Navigate To (Push a Route)](https://docs.flutterflow.io/concepts/navigation/overview#1-navigate-to-push-a-route)
2. [Navigate Back (Pop a Route)](https://docs.flutterflow.io/concepts/navigation/overview#2-navigate-back-pop-a-route)
3. [Replace Route](https://docs.flutterflow.io/concepts/navigation/overview#3-replace-route)

##### 1. Navigate To (Push a Route)

This action involves navigating to a new screen by pushing a new route onto the navigation stack.

**What Happens Under the Hood:**

* When you push a route, a new screen is placed on top of the current stack. This means the previous screen is still in the stack but is not visible to the user.
* The new screen becomes the active screen that the user interacts with.

> **Info:** Learn more about adding this action in the [**page navigation guide**](https://docs.flutterflow.io/concepts/navigation/page-navigation#navigate-to-action).

##### 2. Navigate Back (Pop a Route)

This action involves navigating back to the previous screen by popping the current route off the navigation stack.

**What Happens Under the Hood:**

* When you pop a route, the current screen is removed from the stack, and the previous screen becomes active again.
* This action effectively reverses the last push operation.

> **Info:** Learn more about adding this action in the [**page navigation guide**](https://docs.flutterflow.io/concepts/navigation/page-navigation#navigate-back-action).

##### 3. Replace Route

This action involves replacing the current route with a new route. Unlike pushing a route, replacing a route does not add to the stack but swaps the current route with the new one.

**What Happens Under the Hood:**

* The current screen is removed from the stack, and the new screen is added in its place.

> **Info:** * This is useful when you want to prevent the user from navigating back to the previous screen.
* This action is essentially the **Navigate To** action with the **Replace Route** option enabled. Learn more about adding this action in the [**page navigation guide**](https://docs.flutterflow.io/concepts/navigation/page-navigation#navigate-to-action).

---

### Page Navigation {#page-navigation}

*Learn how to navigate between pages in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/navigation/page-navigation

Page Navigation in FlutterFlow is handled through routing, where each page is identified by a unique route. Navigation can be programmed to happen on events like button clicks, leading to actions such as pushing a new route (opening a new page) or popping a route (returning to a previous page). FlutterFlow simplifies the routing process, allowing you to visually design the navigation flow of your app.

Let's see how to do that in FlutterFlow:

[Navigate](https://demo.arcade.software/EwmbXvNO5SvWtQdQyTBK?embed\&show_copy_link=true)

##### Navigate To \[Action]

The Navigate To Action allows you to set the next page and modify other navigation-related properties:

| Action Property Name      | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Allow Back Navigation** | Toggle    | Toggle this to prevent the user from navigating back to this page after moving to the next page                                                                                                                                                                                                                                                                                                 |
| **Replace Route**         | Toggle    | Use this option to replace the current page in the navigation stack. For example, if a user navigates from Page A to Page B and then to Page C, pressing the back button on Page C would normally return to Page B. However, if **Replace Route** is enabled on Page B, the route changes to Page A -> Page C; therefore, pressing the back button on Page C will take the user back to Page A. |
| **Transition Type**       | Drop Down | This allows you to specify an animation that will be applied while navigating away from a screen. Options include **Default, Instant, Fade In, Slide Up, Slide Down, Slide Left, Slide Right,** and **Scale**.                                                                                                                                                                                  |
| **Transition Duration**   | Double    | Set the duration of the transition animation in milliseconds                                                                                                                                                                                                                                                                                                                                    |
| **Page Parameters**       |           | Use this to send data to the next page during navigation.                                                                                                                                                                                                                                                                                                                                       |

Note

**Allow Back Navigation** does not affect the Android back button. To disable the Android back button, set **Disable Android Back Button** property on the destination page.

![Nav.png](https://docs.flutterflow.io/assets/images/Nav-d529f8e9c3602314f487d0cf3a6ab17d.png)

Properties of a Navigate To Action

##### Navigate Back \[Action]

In the next page you are navigating to, ensure that you add a 'Navigate Back' action to the AppBar or wherever you want users to navigate from. Let's add a ' Navigate Back' action to our subsequent page, from which we navigated in the previous section:

---

### PageView {#pageview}

*Learn how to use the PageView widget for creating swipeable pages, perfect for creating onboarding screens or multi-step forms.*

**Source:** https://docs.flutterflow.io/concepts/navigation/pageview

The PageView widget is used to create swipeable pages. In page view, you can add multiple child widgets, each of which is considered a page and can be scrolled horizontally or vertically.

The PageView is useful when you have a collection of pages that you want to display one at a time, especially if you want the user to be able to swipe between them, such as in an onboarding screen, an app that shows a short video by swiping up or down just like Instagram, TikTok, Youtube shorts, etc.

![PageViewDemo](https://docs.flutterflow.io/assets/images/PageViewDemo-8515173fd8c7f97e54d5d4fef3983cf7.avif)

#### Adding PageView widget

To add the PageView widget to your app:

1. Add the **PageView** widget from the **Layout Elements** tab.
2. By default, it adds three pages and shows the first one in the canvas. In the widget tree, it is represented as **PageView Page**. To see another page in the canvas, move to the **Properties Panel >** set the **Active Page** to the page you want to see.
3. To add a new page, move to the **Properties Panel > Active Page >** click **+ Add Page**.
4. To delete any page, select the **PageView Page** (which you want to delete) from the widget tree or the canvas area and press the **Delete** key on the keyboard.
5. By default, PageView Page contains an [Image](https://docs.flutterflow.io/resources/ui/widgets/image) widget; however, you can customize it as per your requirement. For example, if you want to use the PageView widget to create an onboarding experience, you could wrap (`⌘` + B) the default image widget inside the Stack widget and then add some more widgets.

#### Adding infinite scroll

The PageView widget is an incredibly versatile widget that can be utilized in a variety of situations to create interactive applications. For example, you might want to use it in an app that involves reading books, magazines, or similar content to mimic the experience of flipping through pages.

In such situations, you might consider adding an infinite scroll on this widget, which automatically loads the new pages as you swipe.

We have already covered how to [add infinite scroll on ListView](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#adding-infinite-scroll) widget, which will give you an overall idea of how to add infinite scroll on the PageView widget as well.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

##### Changing the scroll direction

By default, the PageView comes with a horizontal scroll for the pages. To change the scroll direction to vertical, move to the **Properties Panel > Page View Properties >** set the **Axis** to **Vertical**.

##### Enable/disable swipe to scroll

This widget allows you to change the page using a swipe gesture as well as clicking on the indicator (3 dots at the bottom indicate which page is being viewed). You can change this behavior and only allow changing the page on click of the indicator.

To do so, move to the **Properties Panel > Page View Properties >** disable **Allow swipe scrolling**.

##### Update page on swipe

Sometimes you might want to rebuild the page on which the PageView widget is contained. i.e., rebuilding the outside of the page view widget. You might want to load data or show/hide UI elements based on the page currently being displayed. For example, you could display a floating action button only on a certain page or show/hide certain widgets based on the page index.

To do so, move to the **Properties Panel > Page View Properties >** turn on the **Update Page on Swipe**.

Here's an example of displaying the current page index on a page that contains the PageView widget.

##### Trigger action on swipe

You might want to trigger an action when the page is swiped in the PageView widget. For example, you might want to load data for a specific page only when the user swipes to it instead of loading all the data upfront.

To trigger action on swipe:

1. Select the widget from the widget tree or canvas area.
2. Select **Actions** from the Properties Panel (the right menu), and click **+ Add Action**.
3. You will notice that the **Type of Action** (aka callback) is already set to **On Page Swipe**. That means actions added under this will be called whenever the page is swiped.
4. Now, you can add any action here.

Here is an example showing the [snackbar](https://docs.flutterflow.io/resources/ui/pages/scaffold#snackbar) message whenever the page is swiped to the second page.

##### Setting initial page index

You might want to display a specific page as soon as it is loaded. To do so, move to the **Properties Panel > Page View Properties >** enter the **Initial Page Index** value. Please **note** that the page index starts from 0. So, if you want to set page 1, you should enter 0. If you want to set page 2, you should enter 1, and so on.

![setting-initial-page-index.png](https://docs.flutterflow.io/assets/images/setting-initial-page-index-0e4bce1a95e33b2bef3bc25dacd1c5b7.png)

##### Set margin

Margin adds a space between the PageView content and its border. To change the margin, select the **PageView** widget, move to the **Properties Panel > Page View Properties >** find the **Margin** property, and change the values.

##### Customize the indicator

The Indicator helps you identify which page is currently being viewed. You can change the appearance of the Indicator using the various properties available under the *Indicator Properties* section.

To customize the indicator:

1. Select the **PageView** widget, and move to the **Properties Panel > Indicator Properties**.

2. To change the indicator position, 1. Find the **Horizontal Alignment** property and adjust the value by using the slider or entering a value. A value of -1 will place the Indicator all the way to the left, while a value of 1 will place the Indicator all the way to the right.
   2. Similarly, you can also change the indicator position vertically using the **Vertical Alignment** property. A value of -1 will place the Indicator all the way to the top, while a value of 1 will place the Indicator all the way to the bottom.

3. To add padding around the indicator, find the **Padding** property and enter the values in L (Left), T (Top), R (Right), and B (Bottom) properties to get the desired result.

4. To change the active and inactive color, use the **Active Color** and **Inactive Color** properties to change the color.

5. To change the indicator dot size, use the **Dot Width** and **Dot height** properties.

6. To change the size of an active dot, you can use the **Expansion Factor** property. For example, if you enter 2, the active dot size will be twice its normal size.

> **Info:** The width of the active dot is calculated by multiplying the value of the **Dot Width** property with the value of the **Expansion Factor** property. That means if the Dot Width is set to 40 and *Expansion Factor* is set to 2, then the width of the Active dot will be 80.

1. To add space between the indicator dots, use the **Spacing** property.
2. To adjust the rounded corner of indicator dots, use the **Border Radius** property.
3. To show only the border, enable the **Outline** toggle.
4. If you want to hide the indicators, disable the **Show Indicator** toggle.

##### Scroll PageView on button press

If you use the PageView widget to create the onboarding experience, you may probably want to allow users to scroll the pages on button press (e.g., next, previous, and skip buttons) in addition to the swipe to scroll. You can do so by adding the PageView and then defining the Control Page View action on the Tap of a Button widget.

Here's an example of scrolling PageView on button press:

1. First, [add the PageView](https://docs.flutterflow.io/concepts/navigation/pageview#adding-pageview-widget) widget.
2. [Customize the PageView](https://docs.flutterflow.io/concepts/navigation/pageview#customizing) widget and add buttons to go to the previous and next pages.
3. Now select any button and define the [Control Page View action](https://docs.flutterflow.io/concepts/navigation/pageview#control-page-view-action).

#### Control Page View \[Action]

By using this action, you can gain more control over the scrolling behavior of the PageView widget. For instance, you can enable your users to move to the next or previous page with a single tap of a button or to quickly jump to a specific page index based on their preferences.

##### Types of page view action

These are the types of actions you can add to the pageview.

* **Previous**: Scroll to the previous page in the pageview.
* **Next**: Scroll to the next page in the pageview.
* **First**: Scroll to the first page in the pageview.
* **Last**: Scroll to the last page in the pageview.
* **Jump to**: Scroll to a specific page in the pageview. Please note that the page index starts from 0. So, if you want to jump to page 1, you should enter 0. If you want to jump to page 2, you should enter 1, and so on.

##### Adding Control Page View action

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Container, Button, etc.) on which you want to add the action.
2. Select **Actions** from the properties panel (the right menu), If it's the first action, click **+ Add Action** button. Otherwise, click the "**+**" button below the previous action tile (inside *Action Flow Editor*) and select **Add Action**.
3. Search and select the **Control Page View** (under *Widget/UI Interactions*) action.
4. Set the **Page View to Control** to the **name** of the page view added to your page.
5. Select the [**Page View Action Type**](https://docs.flutterflow.io/concepts/navigation/pageview#types-of-page-view-action).

#### Video guide

If you prefer watching a video tutorial, here's the one for you:

---

### Passing Data between Pages {#passing-data-between-pages}

*Learn how to pass data between pages in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/navigation/passing-data

As you build your app, you'll often encounter the need to pass through or transfer data from one page to another. For instance, when a user taps on a product item, you may want to send product data to the next page to display its details.

#### Page parameters

This process of passing data between pages is accomplished using **Parameters**. When navigating from one page to another, you can send parameters to configure the destination page based on the data from the current page. This is useful for tasks like passing a user ID to a profile page or specific details to a detailed view page.

To create a page parameter, follow the steps:

[Create Page Parameters](https://demo.arcade.software/oZV2X0pKNYO61p1jhY22?embed\&show_copy_link=true)

When a page parameter is set to Required, it indicates that this parameter is mandatory when navigating to this page. Users must provide this value; otherwise, FlutterFlow will throw errors. However, if you are creating an optional parameter, please ensure this option is unchecked.

Additionally, you can specify a default value in the Default Parameter Value field to safeguard against incoming values that are empty or null. This step is optional.

![Page-Params.png](https://docs.flutterflow.io/assets/images/Page-Params-da3dd75f70356ff8b7bb002e2c199dd4.png)

If you have created a **Required** Page Parameter and there is a Navigation Action already set on your previous page, FlutterFlow will throw errors because this required parameter has not yet been sent from the previous page. Let's fix that:

[Send Page Parameters](https://demo.arcade.software/kp34JJipEW24hz0u5RsW?embed\&show_copy_link=true)

> **Info:** Passing data can only be tested in **Run** and **Test** Mode (it can not be tested in Preview Mode).

#### When to use Page Parameters?

Page parameters are used to pass essential data between pages that is not persisted in the app’s global state but is necessary for specific functionalities or displays on the subsequent page. Here’s a breakdown of typical uses:

* **Contextual Data:** Information that defines the context of the new page, such as identifiers for items or entities that the page must display. This could include identifiers for transactions, specific products, or user profiles that were selected on the previous page.

* **Configuration Options:** Settings or options chosen by the user that affect how the next page functions or appears. For example, filter or sort preferences selected on a list page that need to be applied on a subsequent results page.

* **Operational Parameters:** Values needed for calculations or logic on the next page that are generated through user activities on the current page. These could be values like quantities, dates, or configuration details necessary to perform operations or initiate processes on the next page.

Page parameters are thus essential for maintaining a seamless user experience, enabling the new page to function as intended based on the specific needs and inputs from a previous interaction.

#### Allowed Data Types

You can pass any supported data from one page to another via *page parameter(s)*. You can think of a *page parameter* as a variable that holds the value being passed from one page to another.

> **Info:** If you are using Firestore Database, most of the time, you would pass the *Document* (an actual record inside the Firestore collection) and *Document Reference (points to actual document)* between the pages.

***

#### Video guide

If you prefer watching a video tutorial, here's the one for you:

---

### Share [Action] {#share-action}

*Learn how to use the Share Action in your FlutterFlow app to share content.*

**Source:** https://docs.flutterflow.io/concepts/navigation/share-action

The **Share Action** enables users to send text or URLs from your app using the native sharing capabilities of their device. This functionality allows users to share information through various applications installed on their devices, such as email, messaging apps, or social media platforms.

> **Warning:** It's important to note that the Share Action is designed for mobile platforms and is not supported in FlutterFlow's Run Mode or Preview Mode. To test this functionality, you need to [**run your app on an iOS or Android device or emulator**](https://docs.flutterflow.io/testing/local-run).

![share-action](https://docs.flutterflow.io/assets/images/share-action-b45517e6222a39ef2d068a4d3c2744cc.avif)

---

### Overview {#overview-2}

*Learn how to add Special Page Navigations in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/navigation/special-page-navigations

FlutterFlow provides special navigation widgets like Tab Bar, NavBar, and PageView for advanced navigation scenarios:

* **Tab Bar**: Used for navigating between different sections of your app with tabs, ideal for organizing content into categories. Learn more [here](https://docs.flutterflow.io/concepts/navigation/tabbar).
* **NavBar**: A bottom navigation bar that helps users switch between major sections of your app seamlessly. Learn more [here](https://docs.flutterflow.io/resources/ui/pages/scaffold#nav-bar).
* **PageView**: Allows for swipeable pages, perfect for creating onboarding screens or multi-step forms. Learn more [here](https://docs.flutterflow.io/concepts/navigation/pageview).

---

### TabBar {#tabbar}

*Learn how to use the TabBar widget in FlutterFlow to create a horizontal row of tabs for navigating different content views in your app.*

**Source:** https://docs.flutterflow.io/concepts/navigation/tabbar

The TabBar widget displays a horizontal row of tabs, allowing users to switch between different content views by tapping on the tabs. Each tab typically represents a different section or category of content.

It can be used in various types of apps, such as news apps with different categories, e-commerce apps with product categories, or social media apps with different sections like feeds, notifications, and messages.

![TabBarDemo.avif](https://docs.flutterflow.io/assets/images/TabBarDemo-d5bf1d3b69572bef578ea1da432a07b1.avif)

#### Adding TabBar widget

To add the TabBar widget to your app:

1. Add the **TabBar** widget from the **Layout Elements** tab.

2. By default, it adds three tabs to the page and shows the first one in the canvas. In the widget tree, it is represented as **Tab** and **TabBar Page**. To see another tab in the canvas, select the **TabBar** widget, move to the **Properties Panel,** and \*\*\*\*set the **Active Tab** to the one you want to see.

3. To customize the Tab: 1. Select the **Tab >** Move to **Properties Panel**.
   2. Use the **Text** property to change the label of the Tab.
   3. You can also [add Icon](https://docs.flutterflow.io/resources/ui/widgets/icons), align it horizontally, and set its margin. **Tip**: To only display Icon, remove the Text value.

4. Inside the **TabBar Page**, you can replace the existing **Text** widget with any widget of your choice.

5. To add a new tab, move to the **Properties Panel > Active Page >** click **+ Add Page**.

> **Tip:** * If you want to adjust the height of a TabBar Page, wrap a TabBar widget inside a container and then set the container’s height.
* You can find the currently selected tab index from *set from variable menu > widget state > TabBar Current Index*.

#### Change tab in response to widget action

If you want to change the tab selection in response to a widget action, such as a button click, you can do so by adding the [Control Tab Bar](https://docs.flutterflow.io/concepts/navigation/tabbar#control-tab-bar-action) action.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

##### Customizing label

To customize the tab label:

1. Select the **TabBar** widget > move to the **Properties Panel > Label Properties**.
2. To set different colors when the tab is selected and unselected, use the **Selected Color** and **Unselected Color** properties.
3. To add some space around the label, use the **Label Padding** property.
4. Use the **Label Style** property to change its [styling](https://docs.flutterflow.io/resources/ui/widgets/text#common-text-styling-properties). You can also set the label styling for the unselected tab text by enabling the **Custom Unselected Label Style**.

##### Customizing tab

By default, the tab in the TabBar widget is displayed with an indicator style, which includes a line under the tab to indicate the currently viewed page. However, you have the flexibility to change the tab's styling to achieve different visual effects. Instead of the indicator style, you can customize the tab to appear as a row of buttons or a toggle button, depending on your design requirements and preferences.

To change the tab styling:

1. Select the **TabBar** widget > move to the **Properties Panel > Tab Properties**.

2. Choose the **Tab Bar Style** from **Indicator**, **Button** and **Toggle Button**.

3. When the style is set to **Indicator**, you can set the indicator **Color** and **Weight** (thickness).

   ![customizing-indicator-style.png](https://docs.flutterflow.io/assets/images/customizing-indicator-style-b7a47fa5c321f45886a3d56f30de3d4b.png)

4. When the style is set to **Button**, you have the following options to customize:

   1. To set the tab background color for selected and unselected states, use the **Fill Color** and **Idle** **Fill Color,** respectively.
   2. To set the border color for selected and unselected states, use the **Border Color** and **Idle Border Color,** respectively. Also, make sure to set the **Border Width** to see the border.
   3. To adjust the rounded corner of each tab, use the **Border Radius** property.
   4. You can also set the **Elevation** and **Button Margin** properties for all tabs.

   ![customizing-button-TabBar-style.png](https://docs.flutterflow.io/assets/images/customizing-button-TabBar-style-f1f73cb838dc1c4108e5c896afee3728.png)

5. When the style is set to **Toggle** **Button**, you have the following options to customize:

   1. To set the tab background color for selected and unselected states, use the **Fill Color** and **Idle** **Fill Color,** respectively.

   2. To set a border around all tabs, use the **Border Color** and **Border Width** properties.

   3. To add a divider between the tabs, use the **Div** **Border Color** and **Border Width** properties.

   4. You can also set the **Elevation** and **Button Margin** properties for all tabs.

      ![customizing-toggle-button-TabBar-style.gif](https://docs.flutterflow.io/assets/images/customizing-toggle-button-TabBar-style-07fbd2de26b3f0c8650363011009897b.gif)

##### Setting initial tab index

You might want to display a specific tab as selected as soon as the TabBar is loaded. To do so, move to the **Properties Panel > General Properties >** enter the **Initial Tab Index** value. Please **note** that the tab index starts from 0. So, if you want to set tab 1, you should enter 0. If you want to set tab 2, you should enter 1, and so on.

![tab-index.webp](https://docs.flutterflow.io/assets/images/tab-index-00877bde5779f8893f72fc07f031352a.webp)

![setting-initial-tab-index .gif](https://docs.flutterflow.io/assets/images/setting-initial-tab-index-6852460a76701225d98cfde9a9aa6cc2.gif)

##### Change the tab bar position

Sometimes you might want to change the default tab bar position, i.e., from top to bottom. You can do so by navigating to **Properties Panel > General Properties >** changing the **Tab Bar Position** value.

![change-the-tab-bar-position.gif](https://docs.flutterflow.io/assets/images/change-the-tab-bar-position-943b2d2684eb747fac67e63083316fcc.gif)

##### Making TabBar Scrollable

When you have a large number of tabs, they may not all fit on the screen. To address this, you can make the tabs scrollable, allowing the user to scroll horizontally to view all the tabs.

To make a TabBar scrollable, select the TabBar widget > move to the **Properties Panel > General Properties >** enable the **Tab Bar Scrollable** option.

> **Info:** If there are fewer tabs, you can control the alignment using the **Tab Bar Horizontal Alignment** property. However, for fewer tabs, you may not need to make them scrollable, but the option is available if required.

##### Set margin

Margin adds a space between the TabBar and its border. To change the margin, select the **TabBar** widget, move to the **Properties Panel > General Properties >** find the **Tab Bar** **Margin** property, and change the values.

![set-margin .gif](https://docs.flutterflow.io/assets/images/set-margin-f67175f0b39524cb5cf59d3b6cf1cf48.gif)

##### Disable swipe to switch tab

By default, you can switch to another tab by swiping and clicking on the tab. In case you want to disable the swiping behavior, you can do so by navigating to **Properties Panel > General Properties >** disabling the **Allow Swiping to Switch Tabs**.

##### Keeping tab state alive

By default, when you switch to a different tab, the state of the previous tab is lost and gets rebuilt when you switch back to it. However, in certain scenarios, you may want to maintain the state of each tab to preserve user input, scroll positions, data from an API call, or any other relevant data. This is called keeping the tab state alive.

To keep the tab state alive, select the **TabBar** widget **> Properties Panel > General Properties>** enable **Keep Tab State Alive**.

#### Control Tab Bar \[Action]

By using this action, you can gain more control over the tab-switching behavior of the TabBar widget. For instance, you can enable users to move to the next or previous tab with a single tap of a button or to quickly jump to a specific tab based on their preferences.

##### Types of action

These are the types of actions you can add to the TabBar.

* **Previous**: Switch to the previous tab in the TabBar.
* **Next**: Switch to the next tab in the TabBar.
* **First**: Switch to the first tab in the TabBar.
* **Last**: Switch to the last tab in the TabBar.
* **Jump to**: Switch to a specific tab in the TabBar. Please **note** that the tab index starts from 0. So, if you want to jump to tab 1, you should enter 0. If you want to jump to tab 2, you should enter 1, and so on.

##### Adding Control Tab Bar action

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Container, Button, etc.) on which you want to add the action.
2. Select **Actions** from the properties panel (the right menu), If it's the first action, click **+ Add Action** button. Otherwise, click the "**+**" button below the previous action tile (inside *Action Flow Editor*) and select **Add Action**.
3. Search and select the **Control Tab Bar** (under *Widget/UI Interactions*) action.
4. Set the **Tab Bar to Control** to the **name** of the tab bar added to your page.
5. Select the [action type](https://docs.flutterflow.io/concepts/navigation/tabbar#types-of-action).

#### Video guide

If you prefer watching a video tutorial, here's the one for you:

---

### WebView {#webview}

*Learn how to use the WebView widget in FlutterFlow to display website content directly within your app.*

**Source:** https://docs.flutterflow.io/concepts/navigation/webview

The WebView widget lets you display the website content right inside your app. It's useful in a case where you don't want your users to leave your app to view the web page.

#### Adding WebView widget

To add the WebView widget to your app:

1. Add the **WebView** widget from the **Base Elements** tab.
2. Head over to Properties Panel, adjust the **Width** and **Height**, and then enter the Webview URL.(e.g., <https://flutterflow.io/,https://en.wikipedia.org/wiki/Main_Page>).
3. Certain web pages may have restrictions that prevent them from being viewed within the WebView, such as popular websites like [Unsplash](https://unsplash.com/) or [Facebook](https://www.facebook.com/). However, you can override these restrictions by enabling the **Bypass Domain Restrictions** option.
4. You can also **Force Allow Vertical** and **Horizontal Scrolling** if needed.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

##### Load content from HTML

Sometimes, you might choose to construct your own HTML with the desired styling and structure and then load that HTML into a WebView. For example, display a privacy policy page with a slight variation using modified HTML content (which might be different than the one hosted on your site).

To do so, enable the **Load content from HTML** and then enter your **Webview HTML Content**.

---

### Notifications {#notifications}

*Learn how to add notifications in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/notifications

**Notifications** are alerts or messages that appear on a user's device outside the normal UI flow of an app. They can inform the user of time-sensitive or high-priority messages, events, or actions that require attention. Notifications may appear as banners, alerts, pop-ups, or lock-screen notifications, depending on user preferences and platform design guidelines.

Notifications enhance your app by increasing user engagement and delivering critical information in real time. Whether it’s an urgent alert or a gentle nudge, these timely messages:

* **Prompt User Action**: Remind users to perform tasks or revisit the app, ensuring higher retention and conversion.
* **Foster Engagement**: Encourage ongoing interaction through updates, promotions, or new content notifications.
* **Deliver Value**: Provide relevant insights—such as location-specific alerts or personalized reminders—at the right moment.

#### Types of Notifications

Generally, notifications can be divided into two main categories: **Local Notifications** and **Push (remote) Notifications**.

**Local Notifications** are scheduled directly on the device and do not require a server component. They are commonly used for time-based reminders or location-based triggers, such as a daily workout reminder at 7:00 AM. To implement local notifications in FlutterFlow, you can integrate the [flutter\_local\_notifications](https://pub.dev/packages/flutter_local_notifications) package using [custom actions](https://docs.flutterflow.io/concepts/custom-code/custom-actions).

**[Push Notifications](https://docs.flutterflow.io/concepts/notifications/push-notifications)**, on the other hand, are delivered from a remote server through a platform-specific push notification service. They are primarily used for real-time updates, such as chat messages, social media alerts, or news updates. In FlutterFlow, [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) (FCM) is used to handle push notifications, enabling seamless communication between your app and users.

---

### OneSignal {#onesignal}

*Integrating OneSignal lets you send emails and SMS (text messages) to your users. This can help you*

**Source:** https://docs.flutterflow.io/concepts/notifications/one-signal

Integrating OneSignal lets you send emails and SMS (text messages) to your users. This can help you get more engagement, make more sales, and keep users coming back. After you set up OneSignal, you'll be able to easily add users to or remove them from OneSignal's subscription list.

![img.png](https://docs.flutterflow.io/assets/images/os-img-f9a915fcc8fd97f76cf0e8b93194261b.png)

Prerequisites

* Before you begin, make sure the project is on **Blaze plan** on Firebase.
* [**Create an Account**](https://dashboard.onesignal.com/signup) on OneSignal

#### Initial Setup

Here's a detailed, step-by-step guide to help you integrate OneSignal:

##### Setup in OneSignal

1. To get started, you need an app created on OneSignal. You can create one from the [dashboard](https://dashboard.onesignal.com/apps).

![img\_1.png](https://docs.flutterflow.io/assets/images/os-img_1-7252718c2ea36679e6d21ba6376567fc.png)

1. After creating your app, activate the services you need, like SMS and Email. Go to your app settings by clicking **App > Settings > Platforms** and then select **Activate** for the services you want to use.

   * If you're planning to use SMS, you'll need a [Twilio](https://twilio.com/) account and then follow the steps from the official [SMS Quickstart documentation](https://documentation.onesignal.com/docs/twilio-setup#step-2-twilio-account-setup).

   ![](https://firebasestorage.googleapis.com/v0/b/ecommerceflow-docs/o/activate-SMS-service.gif?alt=media\&token=b655cf4b-0c4c-4e0a-99bb-be8cebc85997)

   SMS Configuration

   * For sending emails, configure your settings as per the guidelines provided in the OneSignal [documentation](https://documentation.onesignal.com/docs/email-quickstart).

##### Setup in FlutterFlow

To enable OneSignal in FlutterFlow:

1. Navigate to **Settings and Integrations** > **Integrations** > **OneSignal**.

2. Switch on the **Enable OneSignal** toggle.

3. Gather your credentials:

   * **App ID**: Find this in your OneSignal dashboard under **Settings > Keys & IDs > OneSignal App ID**.
   * **API Key**: Located in the same section as the App ID, under **Rest API Key**.
   * **User Key**: Go to your user profile icon, then **Account & API Keys > User Auth Key**.
   * Click **Deploy**.

4) Now, at appropriate event in your app, you can [add an action](https://docs.flutterflow.io/concepts/notifications/one-signal#adding-onesignal-action) that adds the user to the OneSignal's subscription.

5) To test SMS functionality, follow the continuation of the instructions in the [SMS documentation](https://documentation.onesignal.com/docs/sending-sms-messages#sending-sms-notifications-from-dashboard).

6) To try out sending Emails, continue with instructions from [here](https://documentation.onesignal.com/docs/sending-email#sending-email-notifications-from-dashboard).

#### Types of OneSignal action

There are two main actions you can utilize in OneSignal:

* **Add**: This lets you add users with their details like Email Address, Phone Number, and Tags.
* **Dismiss**: Use this to remove a user from the subscription list.

##### Adding OneSignal action

To add a OneSignal action, such as adding a user, follow these steps:

1. Select the **Widget** (e.g., Button, etc.) on which you want to add the action.

2. Select **Actions** from the Properties Panel (the right menu).

3. Search and select the **OneSignal** (under Integration) action.

4. Select the [Type](https://docs.flutterflow.io/concepts/notifications/one-signal#types-of-onesignal-action) of the action.

5. To add a user, enable the subscription options you want. You can set the value directly or use a variable. Remember, phone numbers should be in the [E.164 format](https://documentation.onesignal.com/docs/sms-faq#what-is-the-e164-format).

6. Optionally, add Tags for more personalized messaging. For example, you could tag users based on their spending amount to target them with specific emails or SMS messages about their purchases.

You can find out if the user was successfuly added to the subscription by navigating to **OneSignal dashboard > App > Audience > Subscriptions**.

![img\_2.png](https://docs.flutterflow.io/assets/images/os-img_2-38c9b00550e4ec0a49a984f30c841cca.png)

OneSignal for Supabase Users

Currently, our OneSignal integration supports only Firebase authentication. If you want to use [**Supabase authentication**](https://docs.flutterflow.io/integrations/authentication/supabase/initial-setup), you may need to use [**custom code**](https://docs.flutterflow.io/concepts/custom-code) to notify your users.

---

### Push Notifications {#push-notifications}

*Push Notifications let you deliver time-sensitive, real-time messages to users even when the app isn’t active. These notifications rely on Firebase Cloud Messaging (FCM) behind the scenes, which routes messages to both Android and iOS devices. When integrated correctly, you can use push notifications to:*

**Source:** https://docs.flutterflow.io/concepts/notifications/push-notifications

**Push Notifications** let you deliver time-sensitive, real-time messages to users even when the app isn’t active. These notifications rely on [**Firebase Cloud Messaging (FCM)**](https://firebase.google.com/docs/cloud-messaging) behind the scenes, which routes messages to both Android and iOS devices. When integrated correctly, you can use push notifications to:

* Send alerts for new content (e.g., chat messages, and updates).
* Re-engage users with timely reminders or offers.
* Provide relevant information (e.g., order status, location-based alerts).

Push notifications involve several key components working together to deliver messages to users' devices. In FlutterFlow, you can construct and send notification payloads—such as title, message body, and additional data like image—to a push service, Firebase Cloud Messaging (FCM). FCM receives notifications and routes them to the appropriate devices.

Each device is identified by a unique **Device Token/Registration Token** generated by the FCM to target specific devices. The user's device receives these notifications and handles the payload by displaying messages or navigating the user to specific screens.

#### Push Notifications Setup

You can add and send push notifications manually or trigger them based on user actions within the app. Here are the steps in detail:

General Prerequisites

Before you begin, ensure that you:

* Complete all the steps in [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase). Note that, while setting up, make sure to follow step number 5 and 8 carefully from [**Allow FlutterFlow to Access Your Project**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#allow-flutterflow-to-access-your-project) section to properly add the **Cloud Functions Admin** role to **<firebase@flutterflow.io>** user.
* Upgrade your Firebase project to the [**Blaze plan**](https://firebase.google.com/pricing) to enable [**Cloud Functions**](https://firebase.google.com/docs/functions), which are required specifically for FlutterFlow’s push notification setup, such as retrieving the FCM token and sending notifications trigger from FlutterFlow.

iOS Prerequisites

To send push notifications to iOS devices, you must:

* Have an active [**Apple ID**](https://appleid.apple.com/account?appId=632\&returnUrl=https%3A//developer.apple.com/account/).
* Enroll in the [**Apple Developer Program**](https://developer.apple.com/programs/enroll/) (a paid membership is required). For more details, visit the [**Apple Developer Program**](https://developer.apple.com/programs/).

##### Enabling Push Notification

> **Warning:** **Please note, push notifications will not work in these scenarios:**

* Push notifications will not work on an iOS simulator. To test you will need to use a real device.
* Push notifications will not be delivered to users who are logged out of your app. To send push notifications to users who are not logged in, consider implementing [**Anonymous Firebase Login**](https://docs.flutterflow.io/integrations/authentication/firebase/anonymous-login) within your app
* Push notifications will not work if you have the app open on your device.

To enable push notifications:

1. Navigate to the **Settings and Integrations > Push Notifications** and **Enable Push Notifications**.

2. Now, click on the **Deploy** button. This will create and deploy the *Cloud Functions* in your Firebase project that are necessary for push notifications to work.

3. Optionally, you can enable **Allow Scheduling** to send push notifications at a later time. Once enabled, you can select **Scheduler Granularity**, which determines how precisely the notifications will be sent. You can choose the granularity based on how time-sensitive your notifications are; For example: * If you need the notification to be sent at an **exact time** (e.g., 11:37 AM), choose **"1 minute"**.
   * If a slight delay is acceptable, you can select **"15 minutes"** or **"1 hour"**, meaning the notification will be sent within that timeframe.
   * **Higher precision (e.g., 1-minute intervals) requires more computing resources**, which may **slightly increase costs** (up to $0.50 per month).
   * **Lower precision (e.g., 1-hour intervals) is more cost-effective**, as it reduces the frequency of function execution (around $0.05 per month).

Upgrading to Blaze Plan

If you encounter deployment errors instructing you to contact support, it could be because you recently upgraded your Firebase project to the **Blaze plan**. After upgrading, Firebase may take approximately **10-15 minutes** to propagate the changes. If you receive this error, wait **10-15 minutes** and then try deploying again.

![img.png](https://docs.flutterflow.io/assets/images/enable-push-notification-75d9cd132af0f04b1b31f832849cb38a.avif)

> **Info:** By default, the **Automatically Prompt Users for Permission** option is enabled, meaning your app will automatically prompt users requesting for permission to receive push notifications when the app is started. However, this may be disruptive to your user sign-in flow.

If you disable it, you can control when the permission is requested. To do so, you will need to manually [**Request Permission**](https://docs.flutterflow.io/resources/projects/settings/project-setup#request-permission-action) at the appropriate point in your app. **It is recommended to keep this option always enabled**.

##### Configuring iOS App

To receive the push notifications in an iOS app, you need to perform the following additional steps.

###### Step 1: Creating a Key

Apple requires developers to create a key for the push notifications inside the *Apple Developer Console* to verify the push notification's sender.

To create an APNs key in your Apple Developer account, go to the [**Keys**](https://developer.apple.com/account/resources/authkeys/list) section and click the **(+)** button. Enter a **Key Name**, select **Apple Push Notifications service (APNs)**, and click **Configure**. Choose the appropriate **Environment** (Sandbox, Production, or both) and set any [**Key Restriction**](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns#Team-scoped-keys) as needed. Once configured, click **Save**, then **Continue** and **Register**. Finally, download and securely store the key file, as it will be required for integration with your Firebase project.

> **Tip:** After testing push notifications in the development environment, it's advisable to create a new key specifically for production use and upload it to your Firebase project.

###### Step 2: Add APNs Key to Firebase Project

To add the **APNs** key to your Firebase project, navigate to your **Firebase Project Dashboard > Project Settings** and select the **Cloud Messaging** tab. Scroll down to the **Apple app configuration** section and locate the **APNs Authentication Key**.

Click **Upload** and select your APNs auth key file (that you downloaded in the [previous step](https://docs.flutterflow.io/concepts/notifications/push-notifications#step-1-creating-a-key)). Enter the **Key ID**, which can be found inside the key entry in [Keys](https://developer.apple.com/account/resources/authkeys/list). Finally, enter the **Team ID**, available in the [**Apple Developer Account**](https://developer.apple.com/account) inside the **Membership details** section.

#### Send Push Notifications

To send push notifications, go to **FlutterFlow** > **Settings and Integrations** > **Push Notifications**, then open the **Manually Trigger Notifications** section. Enter the notification details and click **Send Notification**. A confirmation popup will appear—type **"Send Notification"** and click **Send Notification** again to deliver your message.

To send push notifications, you need to provide the following details:

* **Notification Title:** Enter the title of the notification.

* **Notification Text:** Provide the message content for the notification.

* **Notification Image (Optional):** Upload an image to be displayed with the notification.

* **Target Audience** **(Optional):** Choose whether to send notifications to **iOS**, **Android** users, or **All** users regardless of their device type.

* **Deliver With Sound** **(Optional):** Enable this option if you want the notification to play a sound.

* **Batch Notifications** **(Optional):** Toggle this setting if you want to send the notification in batches. Enable this only when you have over 10K users.

* **Scheduled Time (Optional):** Choose the specific date and time for the notification to be sent. This option is available only when the **Allow Scheduling** option is enabled, and the selected date and time follow your timezone.

* **User References (Optional):** Send push notifications to a specific user or a few users. Enter the user document reference (from the 'users' collection in Firestore) into the *User References* in this format: `/users/user_id`.

  tip

  You can easily copy and paste the document reference directly from the [**Firestore Data Manager**](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-content-manager) in FlutterFlow.

  ![pn-with-data-2](https://docs.flutterflow.io/assets/images/pn-with-data-2-38ba3bb21ddf877d8c9bbf8ae2547113.avif)

* **Initial Page (Optional):** Choose the page the app should open when the user taps the notification.

#### Push Notifications with Data

Sometimes, you might want to include additional data with your push notifications, which can then be used to display more detailed information on the page when it is opened through a push notification.

For instance, consider a news app that sends push notifications for breaking news. When the user taps the notification, the additional data like the article’s title, summary, and image can be displayed on the news page.

> **Warning:** Currently, we only support sending *Firestore DocumentReferences* as data.

To send a push notification with data, you need a page that accepts a parameter of type **DocumentReference**. Start by building the notification, and set the **Initial Page** to the one that accepts the parameter. In the **Parameter Data** section, copy-paste the document reference from Firestore. Finally, click **Send Notification** to deliver the push notification with the specified data.

> **Tip:** On the page that receives the DocumentReference, you can fetch additional details of the item using the [**Backend Query**](https://docs.flutterflow.io/resources/backend-query/document-from-reference).

![pn-with-data.avif](https://docs.flutterflow.io/assets/images/pn-with-data-78bba6fa30b96c152057792dfbbec77d.avif)

#### Trigger Push Notification \[Action]

You may want to send a push notification when a specific event occurs in your app. For example, notifying a user when they receive a new message, when an appointment is booked, or when there is a price change.

You can send the push notification when such an event occurs by adding the **Trigger Push Notification** action.

In this action, you can decide who should receive the push notification by setting the **Audience** to either **Single Recipient** or **Multiple Recipients**.

* **Single Recipient:** Sends a notification to one specific user. For example, notifying the **group creator** when a new member joins.
* **Multiple Recipients:** Sends a notification to multiple users. For example, notifying **all group members** when someone joins the group.

> **Tip:** * You must provide the document reference of the user who should receive the notification.
* You can set other notification details as per your requirements.

![trigger push notifications](https://docs.flutterflow.io/assets/images/trigger-pn-38ef8379e58d26e2b910534153ff7b10.avif)

#### Testing Push Notifications Cloud Function

You can also test the Push Notifications Cloud Function directly from the Google Cloud console, without needing to trigger from FlutterFlow. This is especially useful for debugging purposes. For step-by-step instructions, including an example and how to structure the request, refer to the [Testing Cloud Functions in Google Cloud Console](https://docs.flutterflow.io/concepts/custom-code/cloud-functions#testing-cloud-functions) section.

#### Update App Badge Count (iOS only) \[Action]

The **Update App Badge Count** action lets you manually display a numeric badge on your **iOS app icon**. This badge typically indicates pending tasks or updates, such as unread messages, notifications, or reminders.

Platform Support

In Android, badges automatically appear on app icons with push notifications. We would like to add this functionality for iOS. However, we are blocked by [**this**](https://github.com/firebase/flutterfire/issues/9563) issue. Therefore, it is important to note that this action **does not automatically set the badge count** when receiving a push notification in iOS—rather, it must be triggered manually while your app is running.

![badge-count](https://docs.flutterflow.io/assets/images/badge-count-950c23375ca20d6239ec2246c78fb86e.avif)

possible use cases

* In a **messaging app**, you might manually increment the badge count each time a new chat message arrives while the user has the app open or decrease it as they read the messages.
* In an **email app**, you could manually update the badge count each time a new email arrives while the user is actively using the app and decrease it as emails are opened or marked as read.
* In a **calendar app**, you might set the badge count to reflect the number of upcoming events for the day, incrementing or decrementing it based on the user's interactions or changes in their schedule.

To implement, simply enter the number of **Badge Count** the app should display on the home screen icon.

![set-app-badge-count-ios](https://docs.flutterflow.io/assets/images/set-app-badge-count-ios-41c8bb9a7140b280051345356d6cdfbf.avif)

#### FAQs

Push notifications not working; Getting cloud function error: PERMISSION\_DENIED: Missing or insufficient permissions

If you encounter an error with push notifications, specifically a cloud function failure due to permission issues, it might be related to your Google Cloud organization's settings. Organizations can disable automatic IAM grants for default service accounts, leading to this error.

To fix this issue, manually grant the Editor role to the default service account used by your project. You can do this by visiting the GCP IAM page and assigning the Editor role to the following service account:

* For App Engine (Gen 1): `{firebase-project-id}@appspot.gserviceaccount.com`
* For Compute Engine (Gen 2): `{project-number}-compute@developer.gserviceaccount.com`

![pn-faq-img-1](https://docs.flutterflow.io/assets/images/pn-faq-img-1-c3cee31c4aaf730b44f2ec4c635c6682.png)

Also, ensure that these principals (emails) and their roles are present in the permissions tabs in *App Engine Default service account*, *Default compute service account*, and *firebase-adminsdk*. You can do this by visiting the GCP Service Accounts page, clicking on each service account email, and granting access to these principals in the permissions tab.

Below is a sample image for App Engine Default service account. ![pn-faq-img-2](https://docs.flutterflow.io/assets/images/pn-faq-img-2-6c76aedc7a87b21690b34f727945ed18.png)

---

### State Management {#state-management}

*An overview of state management & state variables in FlutterFlow.*

**Source:** https://docs.flutterflow.io/concepts/state-management

State management is a crucial concept focused on maintaining and controlling the **state** of an application. Simply put, it involves monitoring the changes within your app and updating the user interface to reflect these changes.

The UI (user interface) displays information based on state variables. When these state variables change, the UI updates to reflect the changes.

#### State Variables

In FlutterFlow, there are a few types of state variables that you can create:

![app stage overview](https://docs.flutterflow.io/assets/images/state_management_overview-fcd8004bf3a66a6cdbc87536a335b637.png)

App State is shared across multiple pages in the application. Component State is specific to a component. Page State is shared across widgets on the page.

* State variables are themselves [**variables**](https://docs.flutterflow.io/resources/data-representation#variable) - meaning they have a *name* and a *data type*.
* They also have an initial value that is set when you create the variable.
* Once you create a state variable, it's value can be used to change the configuration of widget properties - like any other variable.
* You can update the value of state variables using the **[Update State Variable](https://docs.flutterflow.io/concepts/state-management#updating-state-variables)** action.

##### Creating State Variables

* To create an **App State variable**, refer to this **[guide](https://docs.flutterflow.io/resources/data-representation/app-state#create-app-state-variable)**.
* To create a **Page State variable**, refer to this [**guide**](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#creating-a-page-state).
* To create a **Component State variable**, refer to this [**guide**](https://docs.flutterflow.io/resources/ui/components/component-lifecycle#creating-a-component-state).

Note: Users cannot create **widget state variables**. These are automatically exposed by FlutterFlow when a Form widget is used.

##### Updating State Variables

* To update an **App State variable**, refer to this **[guide](https://docs.flutterflow.io/resources/data-representation/app-state#update-app-state-action)**.
* Refer to the [**Page Lifecycle**](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle) guide to learn about updating **[Page State variables](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#update-page-state-action)**.
* Refer to the [**Component Lifecycle**](https://docs.flutterflow.io/resources/ui/components/component-lifecycle) guide to learn about updating **[Component State variables](https://docs.flutterflow.io/resources/ui/components/component-lifecycle#update-component-state-action)**.

Learn from video

You can learn more about state management from this video:

[YouTube video player](https://www.youtube.com/embed/jD6L4xjYjJA?si=-RjniUB-K0ZsMoB1)

#### Rebuild \[Action]

The **Rebuild** action allows you to refresh a page or a component’s UI. This is especially useful when data changes dynamically; for example, after an API call, a database update, a custom action, or a class method modifies the internal state, and you want the latest data or UI state to be reflected instantly.

The Rebuild action provides different update types depending on where it is used:

* **Rebuild Page:** When on a page, you will see the **Rebuild Current Page** option, which refreshes the entire page’s UI.
* **Rebuild Component:** When on a component, you will see the **Rebuild Current Component** option, which refreshes only that specific component. * **Rebuild Containing Page:** When on a component, you will see this option as well, which refreshes the entire page that contains the component. For example, if you have a **"Confirm"** button inside a dialog component that updates an order’s status, selecting this action will refresh the parent page to instantly show the updated order list.

![rebuild](https://docs.flutterflow.io/assets/images/rebuild-51b6826a3452f3174ff2b8e615f78627.avif)

---

### Widget State {#widget-state}

*Widget state refers to the data or information that a widget holds, which can change over time and affect the widget's appearance or behavior. In FlutterFlow, the state is particularly important for form widgets, such as text fields, checkboxes, and radio buttons, as it allows these widgets to respond to user interactions.*

**Source:** https://docs.flutterflow.io/concepts/state-management/widget-state

**Widget state** refers to the data or information that a widget holds, which can change over time and affect the widget's appearance or behavior. In FlutterFlow, the state is particularly important for form widgets, such as text fields, checkboxes, and radio buttons, as it allows these widgets to respond to user interactions.

Additionally, **Widget Focus State** refers to the state that indicates whether a widget, such as a text field, currently has focus or not. When a widget has focus, it is ready to receive user input, and its appearance typically changes to indicate this (e.g., a text field with a blinking cursor).

**Key Points:**

* **Dynamic Data:** Represents values that change over time (e.g., user input in a text field).
* **Automatic Management:** FlutterFlow handles the state, so developers do not need to write explicit state management code.
* **Reactive Updates:** Changes in the state automatically update the widget's display.

![widget-state.png](https://docs.flutterflow.io/assets/images/widget-state-39a918ddf281ee26e78cda1368918400.png)

#### Managing Widget States

FlutterFlow simplifies state management by providing built-in support for handling widget states. This means developers do not need to manually create or manage the state of form widgets. Instead, FlutterFlow automatically manages the state for these widgets, ensuring a seamless and intuitive experience.

Some examples of widget states exposed by FlutterFlow:

* **Text Fields:** The state of text fields is automatically managed, including the input text and validation states.
* **Checkboxes:** The state of checkboxes is managed, indicating whether they are checked or unchecked.
* **Radio Buttons:** The state of radio buttons is managed to reflect the selected option.

In the following example, we find widget state and widget focus state of a TextField being exposed by FlutterFlow on the page it was created and available as an option in the variable menu.

![using-widget-state.png](https://docs.flutterflow.io/assets/images/using-widget-state-12d396c12118d4cfb1607a772829fef1.png)

Scope

**Widget states** are mostly available for access on the page or component where they were created. However, when you add a component to a page, the widget states exposed in the component will also be available in its parent page.

For instance, consider a component with two `TextFields` – one for the username and another for the password. This component could be utilized in both sign-in and sign-up pages. In such cases, you need to be able to retrieve the values from each TextField as if they were added directly to the page.

You can access the widget state of a component's widgets on your page, just as you would for other widgets. Simply navigate to the **Set Variable menu > Widget State > \[component\_name] > \[your\_widget]**.

FlutterFlow allows you to update the state of these widgets through actions exposed by the platform. For example, if you want to clear a TextField when the Send button is clicked on a form-like page, then in the Actions Flow, you can find relevant actions such as **Clear TextField**. This enables dynamic interaction and state management directly within the visual development environment.

![managing-widget-state.png](https://docs.flutterflow.io/assets/images/managing-widget-state-4c54f8309e04934c13235f8d65a5117c.png)

#### Action Triggers for Form Widgets

FlutterFlow allows you to bind action triggers to widget states, such as calling an API on focus change of a textfield or changing the appearance of a button when a checkbox is checked.

**Most common Action Triggers exposed by form widgets:**

* **On Focus Change:** Triggered when a widget, such as a text field, gains or loses focus. For example, showing additional tips or validation messages when the user starts typing in a text field.

* **On Submit:** Triggered when a form or text field is submitted. For example, validating input and submitting data when the user presses the enter key or clicks a submit button.

* **On Change:** Triggered when the value of a widget changes. For example, real-time validation or updating state as the user types in a text field or changes a selection in a dropdown.

* **On Completed:** Triggered when a specific input is completed, such as entering a pincode. For example, automatically moving to the next step in a process after a complete and valid pincode is entered.

* **On Selected:** Triggered when an option is selected in widgets like choice chips, checkboxes, radio buttons, or sliders. For example, updating the UI or performing actions based on the selected option.

These triggers allow developers to create interactive and responsive applications by defining specific actions that occur in response to user interactions with form widgets.

![action-triggers-widget-state.png](https://docs.flutterflow.io/assets/images/action-triggers-widget-state-06bf4658efc13383380f0a863b4d8b31.png)

---

### Tools Configuration {#tools-configuration}

*Expose Action Blocks to GenUI so the model can fetch data, run workflows, and use real results in its responses.*

**Source:** https://docs.flutterflow.io/concepts/tools

In GenUI, **Tools** are Action Blocks that the model can call during a conversation. A tool is appropriate when the model needs fresh data or needs to perform work before it can answer.

Common uses:

* Query APIs or databases
* Run calculations
* Fetch records by ID
* Transform structured data
* Trigger a workflow that still returns a useful result

> **Warning:** If the Action Block does not return anything, it cannot be used as a GenUI tool.

For each tool, GenUI includes:

* Function name
* Description
* Parameters
* Required or optional status
* Parameter descriptions
* Return type
* Return description

That means the Action Block name and description matter. They are part of the tool-selection signal the model sees.

> **Note:** If a tool throws an exception, the error is caught and sent back to the model as a structured error payload. The UI remains stable and the model can explain the failure or suggest alternatives.

#### Tool Requirements

###### The Action Block must return a value

Tools are designed around request/response semantics. No return value means nothing meaningful can be sent back to the model.

###### Parameter and return types must be supported

Supported tool types include:

* `String`
* `int`
* `double`
* `bool`
* `Color`
* `DateTime`
* `TimestampRange`
* `LatLng`
* `GooglePlace`
* `JSON`
* `DataStruct`
* `Enum`
* media-path string types such as `ImagePath`, `VideoPath`, `AudioPath`, and `MediaPath`
* list forms of the same supported types

Unsupported types are rejected during validation.

###### Duplicate tools are not allowed on the same widget

Configuring the same Action Block twice on one GenUI widget is treated as an error.

#### Loading Messages

Each tool can define its own loading message in the widget configuration.

* If set, that message is shown while the tool runs.
* If omitted, the generated tool uses `Processing...`.

This is separate from the widget-level thinking message, which defaults to `Thinking...` and is shown before the tool call starts.

#### Serialization Rules

The generated code serializes common FlutterFlow data types into model-friendly JSON:

* **Color**: CSS color string. e.g., `Color(0xFF4CAF50)` → `"#4CAF50"`
* **DateTime**: ISO 8601 string. e.g., `DateTime(2024, 3, 15)` → `"2024-03-15T00:00:00.000"`
* **TimestampRange**: start|end milliseconds string. e.g., `TimestampRange(1700000000000, 1700086400000)` → `"1700000000000|1700086400000"`
* **LatLng**: serialized string form. e.g., `LatLng(37.7749, -122.4194)` → `"37.7749,-122.4194"`
* **GooglePlace**: serialized place payload (JSON object with place details)
* **DataStruct**: converted using `toMap()`. e.g., `Product(name: "Shoes", price: 99)` → `{ "name": "Shoes", "price": 99 }`
* **Enum**: serialized enum string. e.g., `OrderStatus.delivered` → `"delivered"`

#### Best Practices

###### Keep tools focused

Prefer small, specific tools:

* `getOrderDetails`
* `searchProducts`
* `getWeatherForLocation`
* `calculateQuote`

over broad tools like:

* `handleRequest`
* `fetchData`
* `processWorkflow`

###### Write descriptions for model behavior, not just for humans

Good:

`Retrieves the current order status, tracking number, and ETA for a given order ID.`

Weak:

`Looks up an order.`

###### Return structured data when possible

If the output can be represented as Custom Data Type `DataStruct`, do that instead of flattening everything into strings. Structured output is easier for the model to feed into catalog components.

###### Match tool output to catalog input

Reliable GenUI setups usually follow this shape:

* A tool returns `OrderStruct`
* A catalog component accepts `OrderStruct`

That gives the model a clean path from retrieval to rendering.

#### Common Examples

###### Data lookup

`getOrderDetails(orderId: String) -> OrderStruct`

The model calls the tool, gets a structured order result, and renders an order summary component.

###### Search

`searchProducts(query: String, maxPrice: double?) -> List<ProductStruct>`

The model calls the tool and then renders a list-style catalog component using the returned products.

###### Calculation

`calculateMonthlyPayment(amount: double, rate: double, termMonths: int) -> PaymentQuoteStruct`

The model uses the result to explain the output and optionally render a quote component.

---

