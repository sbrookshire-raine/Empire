# FlutterFlow Documentation — Complete Guide (Part 3 of 7: Widgets Reference)

> **Note for NotebookLM:** This is one part of a multi-file Markdown export of the official FlutterFlow documentation, cleaned and reorganized for use as a NotebookLM source set to build a structured FlutterFlow learning plan. Import all parts together as separate sources in the same NotebookLM notebook.

- **Source:** https://docs.flutterflow.io (crawled via https://docs.flutterflow.io/llms-full.txt)
- **This file's page count:** 56
- **Total pages across the full guide (all 7 parts):** 369
- **Date generated:** 2026-07-18
- **Part:** 3 of 7 — Widgets Reference
- **Other parts in this guide:**
  - Part 1: Fundamentals, Account, CLI & Builder UI (`FlutterFlow_Guide_01_Fundamentals_and_Platform.md`)
  - Part 2: Core Concepts: UI Building, Actions, Animations, Navigation, Custom Code (`FlutterFlow_Guide_02_CoreConcepts.md`)
  - Part 4: Resources: Data, Backend Query, Forms, Functions & Projects (`FlutterFlow_Guide_04_ResourcesDataAndLogic.md`)
  - Part 5: Integrations: Auth, Firebase, Supabase, Payments, Maps, Search, Ads (`FlutterFlow_Guide_05_Integrations.md`)
  - Part 6: Deployment, Testing, Marketplace & Exporting Code (`FlutterFlow_Guide_06_DeploymentTestingMarketplace.md`)
  - Part 7: Troubleshooting Guides (`FlutterFlow_Guide_07_Troubleshooting.md`)

## Table of Contents

**Resources (Widgets, Data, Backend Query, Functions, Projects)**

- [Components](#components)
- [Action Parameters (Callbacks)](#action-parameters-callbacks)
- [Child Widget](#child-widget)
- [Component Actions & Lifecycle](#component-actions-lifecycle)
- [Components](#components-2)
- [Using Components](#using-components)
- [Widget Builder Parameters](#widget-builder-parameters)
- [UI Building Blocks](#ui-building-blocks)
- [Introduction to Pages](#introduction-to-pages)
- [Page Lifecycle](#page-lifecycle)
- [Properties Panel](#properties-panel)
- [Page Elements](#page-elements)
- [Introduction to Widgets](#introduction-to-widgets)
- [Basic Widgets](#basic-widgets)
- [AspectRatio](#aspectratio)
- [Badge](#badge)
- [Barcode](#barcode)
- [Blur](#blur)
- [Calendar](#calendar)
- [Card](#card)
- [Carousel](#carousel)
- [Bar Chart](#bar-chart)
- [Chart](#chart)
- [Line Chart](#line-chart)
- [Pie Chart](#pie-chart)
- [CountController](#countcontroller)
- [CreditCardForm](#creditcardform)
- [DataTable (Paginated)](#datatable-paginated)
- [Dividers](#dividers)
- [Draggable + DragTarget](#draggable-dragtarget)
- [Expandable](#expandable)
- [FlippableCard](#flippablecard)
- [Markdown](#markdown)
- [MediaDisplay](#mediadisplay)
- [MouseRegion](#mouseregion)
- [PinCode](#pincode)
- [ProgressBar](#progressbar)
- [RatingBar](#ratingbar)
- [Signature](#signature)
- [Slider](#slider)
- [Spacer](#spacer)
- [StickyHeader](#stickyheader)
- [SwipeableStack](#swipeablestack)
- [Tooltip](#tooltip)
- [Transform](#transform)
- [Button](#button)
- [Composing Widgets](#composing-widgets)
- [Generate Dynamic Children](#generate-dynamic-children)
- [Lists & Grids](#lists-grids)
- [Rows, Column & Stack](#rows-column-stack)
- [Container](#container)
- [Icons](#icons)
- [Image](#image)
- [Properties Panel](#properties-panel-2)
- [Text](#text)
- [Common Widget Properties](#common-widget-properties)

---

## Resources (Widgets, Data, Backend Query, Functions, Projects)

### Components {#components}

*Components in FlutterFlow are reusable widgets. You design a widget once and can reuse it throughout your app*

**Source:** https://docs.flutterflow.io/resources/ui/components

Components in FlutterFlow are reusable widgets. You design a widget once and can reuse it throughout your app to save time, ensure consistency, and make it easier to maintain.

When you add a component to a [**Page**](https://docs.flutterflow.io/resources/ui/pages), it becomes part of that page's **[Widget Tree](https://docs.flutterflow.io/resources/ui/widgets#widget-tree)**. This allows the component to interact with other widgets, inherit properties, and respond to state changes as part of the page's structure.

Components help in several ways:

* **Consistency:** Components provide a consistent look and behavior, reducing the likelihood of discrepancies that can occur when the same UI elements are created multiple times.

* **Centralized Updates:** By creating a component once and reusing it across different parts of your app, you ensure that any design or functionality changes are made in one place. When that component is updated, all instances of that component across the app automatically reflect those changes. This significantly reduces the effort required to maintain and update the app.

  Classes vs. Instances

  Learn more about **[Classes and their Instances](https://docs.flutterflow.io/resources/ui/overview)** and what they mean in FlutterFlow.

* **Error Reduction:** Since components reduce design duplication, the risk of errors decreases. Fixing an issue in a component means it is fixed everywhere, leading to fewer bugs and inconsistencies.

* **Scalability:** As your app grows, maintaining a DRY codebase through components makes it easier to scale. Adding new features or modifying existing ones becomes more straightforward and less prone to introducing errors.

  DRY PRINCIPLE

  The **DRY (Don't Repeat Yourself)** principle is a software development concept that emphasizes the importance of reducing repetition within code and design.

Leveraging components effectively helps you build a consistent, efficient, and maintainable app.

#### Common Use Cases

Components can be used in various scenarios to accelerate your app development process. Here are some common use cases:

* Design a **standard button once** and reuse it across multiple screens to maintain a cohesive look.

* Use components for **card designs** frequently used in your app, such as product cards, user profiles, or news articles.

* **Standardize input forms** for tasks like user registration, login, or feedback collection, to ensure a consistent user experience.

* Design **pop-up messages or dialogs** that match the overall theme of your app, enhancing visual consistency.

* Build interactive elements such as **custom sliders, ratings, or progress bars**, and use them across various parts of your app.

* Design sections of a screen that are frequently repeated, such as testimonials, image galleries, or feature highlights, and reuse them to maintain a cohesive layout.

Here's an example of commonly used components in the [EcommerceFlow demo](https://bit.ly/ff-docs-demo-v2) app.

![custom-components-demo-list.png](https://docs.flutterflow.io/assets/images/custom-components-demo-list-fd33ff85bc0fec2925c8a7ffba8c15d4.png)

Some of the custom components from the Ecommerce Demo App

---

### Action Parameters (Callbacks) {#action-parameters-callbacks}

*Learn how to add action parameters or callbacks to custom components.*

**Source:** https://docs.flutterflow.io/resources/ui/components/callbacks

In FlutterFlow, callbacks are a way to pass down actions from parent entities (like pages or other components) to child entities (such as custom widgets or components). This allows the parent to define specific behaviors that the child entity should execute when certain events occur.

Callbacks enable dynamic and interactive behavior in child components, allowing them to perform actions defined by the parent, such as navigation, data updates, or displaying dialogs.

For example, if you have an *image upload component*, the parent can define what should happen after an image is successfully uploaded. Using callbacks, the *image upload component* can execute a parent-defined action, such as:

* Resize and compress the image to reduce storage size.
* Update the user's database record with the new image URL.
* Refresh the UI to display the updated profile picture.

This makes the *image upload component* reusable, as it doesn't need to know the specifics of what should happen after upload. Instead, the parent controls the behavior by passing the appropriate actions via a callback.

![action-parameters-callbacks](https://docs.flutterflow.io/assets/images/action-parameters-callbacks-93f5b42a0ea8dc2d5bf5f7ccacd430c6.avif)

Benefits of Using Callbacks in FlutterFlow

* **Modularity:** Separate the logic of what happens when an event occurs from the child component, making your component more modular and reusable.
* **Reusability:** Use the same child component in different contexts with different behaviors, simply by passing different callbacks.

#### Adding Callbacks

Let’s continue with our previous example (*image upload component*) and see how to add callbacks to it:

##### Creating a Callback Parameter

To create a component that will execute a callback, you must create a component with a parameter with the **Action** type. You can create an action parameter called `uploadAction`, which represents the action that will be executed after the image is uploaded.

When you create an action parameter, you can also specify parameters that will be passed into the action. For this example, the action will likely need to know the uploaded image URL to process it further. So, you can specify an action parameter called `uploadedURL`.

Now, the page or component that uses this button can use this parameter in its own action flow. An example of this is shown below.

##### Executing a Callback

You can execute the action passed into the component by using the **Execute Callback** action within the component's action flows.

For example, you can execute the above callback after the image is successfully uploaded and pass the uploaded image URL into the callback.

##### Passing an Action to a Component

When you add a component to the widget tree of a page or another component, you can define values for its parameters, including action parameters.

For instance, when you add an *image upload component*, you can specify the action flows that should run when the callback is triggered. For this example, we simply update the profile picture.

> **Info:** You can access the value passed to the callback by navigating to the **Set Variable** menu > **Callback Parameters**.

Now that we have an *image upload component* with action parameters set up, it can be reused across different pages or contexts, because it relies on the parent to define the after-upload logic. For example, the same component can be used to upload an image while posting reviews for a product, eliminating the need to create a separate component for this functionality.

![component-action-parameters.avif](https://docs.flutterflow.io/assets/images/component-action-parameters-4af70e2016eac391b7ad452ec33669b5.avif)

#### More Examples

Let's look at a few more examples of action parameters (callbacks) in real-world scenarios.

##### Example 1: Dynamic Dialog Component

Let’s take another example of a reusable dialog component that uses callbacks to handle context-specific actions like confirming a deletion, logging out, or saving data. In one context, "Yes" deletes an item. In another, it logs out a user.

The specific logic for each action is defined by the parent component or page using the dialog. The dialog itself does not need to know what should happen—it simply executes the callback passed to it when users click the "Yes" button.

![dialog-component-action-parameters.avif](https://docs.flutterflow.io/assets/images/dialog-component-action-parameters-c5a8e657eb4d1524754afd2dcad0d02a.avif)

##### Example 2: Custom Navigation Bar in Super App

Using action parameters to build a custom navigation bar in a super app is an excellent way to create a dynamic, reusable, and modular navigation solution. A **super app** typically hosts multiple mini-apps or features, each requiring specific navigation logic. Action parameters allow you to define navigation behavior dynamically, depending on the active context, making it perfect for this scenario.

Here, the navigation bar doesn’t require hardcoded routes. Instead, the navigation logic can be customized for each mini-app, allowing the navigation bar to remain focused solely on its UI role.

For example, in an **ecommerce mini-app**, the home button navigates to the product listing page, while the main (middle) button opens the shopping cart. In contrast, in a **cab booking mini-app**, the home button navigates to the dashboard, and the main (middle) button opens the quick booking page.

![navigation-bar-action-parameters.avif](https://docs.flutterflow.io/assets/images/navigation-bar-action-parameters-3e8f6b8fa1a943ec9121ba2126f91386.avif)

---

### Child Widget {#child-widget}

*Learn how to use Child Widget to add flexible, customizable content inside components.*

**Source:** https://docs.flutterflow.io/resources/ui/components/child-widget

Child Widget allows you to create reusable components while keeping part of the layout flexible. Instead of building multiple variations of the same component, you define a fixed structure and leave a specific area open for customization.

* Its position is fixed within the component layout.
* It accepts any widget, such as text, buttons, images, custom widgets, and components.
* Each component instance can contain different content.
* The overall structure of the component remains consistent

This allows you to reuse the same component while adapting its content as needed.

![child-widgets.avif](https://docs.flutterflow.io/assets/images/child-widgets-9dc2d6e4e3b18a124a96dad258399b38.avif)

Common use cases

* Dashboard cards with different content (charts, stats, lists)
* Settings rows with different controls (toggle, dropdown, button)
* Empty state sections with different actions
* Feature or onboarding cards with varying content

#### Using Child Widget

Let’s see how to use the Child Widget by building a simple example of displaying different controls in a settings row.

1. In your Component, add a new parameter and give it a clear name (e.g., `childWidget`).
2. Set the parameter **Type** to **Child Widget**.
3. In the component layout, add a **Child Widget placeholder** where you want dynamic content to appear.
4. Go to the component instance (the place where you add this component), locate the Child Widget area, and add any widget to it.

##### Child Widget vs Widget Builder Parameter

Both options let you insert custom UI into a component, but they are designed for different workflows. One focuses on visual flexibility, while the other focuses on structured and scalable component design.

**Child Widget**: A Child Widget allows you to drag and drop any widget directly into a component instance. It does not require setup from the component creator and is handled entirely in the visual editor. Each instance can have different content, making it ideal for quick, flexible customization.

[**Widget Builder Parameter**](https://docs.flutterflow.io/resources/ui/components/widget-builder): A Widget Builder Parameter is defined by the component creator and lets you pass UI into a component as a parameter. It works like a function input, providing a more structured and controlled way to customize components, especially for reusable and scalable designs.

##### Best Practices

* Place the Child Widget in a predictable area of the layout, such as a trailing section, content block, or action area. Avoid placing it in positions that affect the overall structure (e.g., between tightly coupled layout elements).
* Keep the role of the Child Widget clear. It should represent a specific purpose, such as "action area" or "content area", not a random insertion point.
* Avoid adding too many Child Widget placeholders in a single component, as it can make the component harder to understand and use.
* Test the component with different widget types (small, large, interactive) to ensure the layout remains stable across variations.

##### Limitations

* The Child Widget position is fixed inside the component. You cannot move or reposition it differently for each instance.
* It does not enforce any structure on what is inserted, so inconsistent widgets across instances can lead to inconsistent UI if not carefully designed.
* It is not ideal for highly dynamic, repeated layouts such as product lists or grids, where content is driven entirely by data.
* It relies on manual placement per instance, which can be less efficient for larger or system-driven designs.

---

### Component Actions & Lifecycle {#component-actions-lifecycle}

*In FlutterFlow, understanding the component lifecycle is crucial for managing state and optimizing your*

**Source:** https://docs.flutterflow.io/resources/ui/components/component-lifecycle

In FlutterFlow, understanding the component lifecycle is crucial for managing state and optimizing your app's performance.

Let's delve into the key moments in the lifecycle of a **Component**:

* **Creation**: Component instances are created dynamically when they are used within a page or another component. This means that component instances are created as needed, which helps manage resources efficiently and avoid unnecessary overhead.

* **Initialization:** Actions defined in the `On Initialization` **Action Trigger** are executed during this phase. For instance, you can initialize local state variables with initial values, or start component animations in this phase. At this stage, component state variables with their default values (if any) are also created. These variables hold data specific to the component, such as form inputs or toggle states, and are essential for managing the component’s internal state.

* **Updating:** While in use, the component can receive updated parameters from its parent when the parent rebuilds itself, allowing the component to adjust its behavior and appearance accordingly. When updating state variables inside a component, you can choose to rebuild only the component itself or the entire page containing the given component. This dynamic updating is crucial for maintaining a responsive and interactive user experience.

* **Disposal:** When the component is no longer needed, such as when a user navigates away from the page or the component is explicitly removed, it is destroyed.

In FlutterFlow, most of these lifecycle stages are handled internally by FlutterFlow's architecture. However, FlutterFlow exposes some lifecycle methods so that you, as a developer, can decide what additional configurations to load upon initialization and when to re-render the UI based on interactions.

Let's look at them in the following sections:

#### Initialization Action Triggers

During the initialization of a **Component**, FlutterFlow exposes the `On Initialization` **Action Trigger** that assists you in loading resources or initializing data when the Component is loaded in a Page or a Component.

What are Action Triggers?

**Action Triggers** serve as event listeners or handlers that respond to specific events or user interactions within an application. FlutterFlow provides developers with a way to define logic that responds to various events, such as button clicks, page loads, form submissions, or data changes. To learn more, see the [**Action Flow Editor**](https://docs.flutterflow.io/resources/functions/action-flow-editor) section.

As you open the Action Flow Editor for your Component, you can see the `On Initialization` **Action Trigger** exposed for your **Component**.

##### On Initialization \[Action Trigger]

The `On Initialization` action trigger in FlutterFlow allows you to define actions that should occur when a component loads or is initialized, such as setting up necessary data, state variables, or other initialization tasks.

If the component stops being shown in the UI and then becomes visible again, the actions under the **On Initialization** action trigger will run again so any setup tasks are re-executed. For dynamically generated components, such as those in a ListView with a query, each instance will trigger the actions under `On Initialization` action trigger when it is created.

##### On Shortcut Press \[Action Trigger]

Your component can also respond to certain keypress events. For more details on setting this up, see [this section on keyboard shortcuts](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#on-shortcut-press-action-trigger).

##### On Dispose \[Action Trigger]

The **On Dispose** action trigger for components allows you to define actions that execute when the page containing the component is navigated away or removed from memory. It is particularly useful for stopping ongoing operations.

Imagine a scenario where a [periodic action](https://docs.flutterflow.io/resources/time-based-logic/periodic-action), such as fetching live weather updates, is started in a component when it is loaded (i.e., [On Initialization](https://docs.flutterflow.io/resources/ui/components/component-lifecycle#on-initialization-action-trigger)). The action runs periodically, providing real-time data updates as long as the component is active. However, when the page containing the component is navigated away, you need to stop the periodic action to conserve resources and prevent unnecessary processing. By using the **On Dispose** action trigger, you can safely stop the periodic updates and clean up any associated resources.

> **Info:** The **On Dispose** action trigger always runs before the [**parent page’s On Dispose**](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#on-dispose-action-trigger). This ensures that the component cleans up its resources first, allowing the parent to finalize its disposal without dependencies on the child.

#### Component State

STATE VARIABLES

A state variable holds information or data about your UI at any given moment. To learn more about **states and state management, [refer to this guide.](https://docs.flutterflow.io/concepts/state-management)**

**Component state** refers to the information that a component tracks about its current condition or the data it manages internally. This can include data such as whether a button is enabled, the value of a slider, or the entries in a dynamically updated list. Component state variables are only accessible within the current component's scope.

This type of variable is particularly useful for storing data that affects how the component behaves or appears, such as toggling UI elements, keeping track of user choices within the component, or caching data pertinent to the component's functionality.

For example:

* In a custom drop-down menu component, you might use a component state variable to keep track of which item is currently selected.
* In a toggle switch component, you could use a component state variable to store the on/off state based on user interaction. This approach ensures that the state of the component is maintained as it interacts with the user or other parts of the application.

When a component state variable changes, the component can be re-rendered with the updated values, displaying the latest state of the component with these updates.

##### Creating a Component State

To create a new **Component State variable** in your component, follow these steps:

[Create Component State](https://demo.arcade.software/nEmCDqupF7YHUTi4hKvW?embed\&show_copy_link=true)

When creating Component State, the following properties are included:

* **Is List:** This property determines whether the variable can hold multiple values of the same data type (like a list or array) or just a single value.

* **Initial Field Value:** This property sets the default value for the variable when it is first created. It's like setting the starting point or the value that the variable begins with before anything else happens.

* **Nullable:** This property determines whether the variable can have a null value. When "**Nullable**" is set to true, it means the variable can be empty or have a null value. This is useful when dealing with optional data or scenarios where the absence of a value is valid.

Now, apply these concepts to the `isFavourite` variable in the context of the above example:

* For the `isFavourite` variable, it is a single value (boolean), so **Is List** would be set to false.

* Set the **Initial Field Value** to **false**, indicating that the item is not favorited by default.

* Set the **Nullable** property to false, as the variable should always have a boolean value (true or false) and never be null.

> **Note:** You can set the **Data Type** of your Component State variable to primitive data types such as **String, Integer, Boolean,** or **Double**, or complex built-in data types such as **Enum, Custom Data Type,** or **Document**. To learn more about the available data types, refer to the [**Data Representation section**](https://docs.flutterflow.io/resources/data-representation).

##### Get Component State Value

In the following example, we demonstrate how to toggle the heart icon from an outlined to a filled icon based on the `isFavourite` state variable. We introduce a `Conditional Builder` widget that allows us to show a widget tree based on **If/Else If/Else** conditions. The goal is to visually indicate whether a product has been favorited by the user.

Follow these steps:

[Get Component State](https://demo.arcade.software/Y96decdgYWVll3SP9Jk8?embed\&show_copy_link=true)

##### Update Component State \[Action]

**Component state** values can only be updated via actions. Whenever you want to update the component state, add an **Update Component State** action from the Action Flow Editor of the component.

In the following demo, we open the Action Flow Editor on the parent widget `Conditional Builder` and call the **Update Component State** action to toggle the value of `isFavourite`.

[Get Component State](https://demo.arcade.software/4tEsyMFyCxEP1tWQcPVh?embed\&show_copy_link=true)

###### Rebuild on Update

When updating your component state in FlutterFlow, you'll often come across the **Update Type** property in your action properties. Here's what it means:

* **Rebuild Containing Page:** This option triggers a re-rendering of the page containing this component.

* **Rebuild Current Component:** This option triggers a re-rendering of the current component only.

* **No Rebuild:** Choose this option when you need to update the state value without immediately reflecting the changes in the UI.

> **Tip:** If you want to rebuild a component without updating any state variables, use the [**Rebuild**](https://docs.flutterflow.io/concepts/state-management#rebuild-action) state action.

Expensive Rebuilds

Too many rebuilds can impact performance because rebuilding the widget tree frequently consumes resources and may lead to decreased responsiveness and increased battery usage. Therefore, it's essential to consider the trade-offs and use rebuilds judiciously to maintain optimal app performance.

To learn more about what happens behind the scenes, refer to the [**Generated Code: Components**](https://docs.flutterflow.io/generated-code/component-model) section.

---

### Components {#components-2}

*Components are reusable widgets you create to meet the specific needs of your app. This approach ensures consistency, saves*

**Source:** https://docs.flutterflow.io/resources/ui/components/creating-components

Components are reusable widgets you create to meet the specific needs of your app. This approach ensures consistency, saves time, and simplifies maintenance across your project.

#### Creating a Component from Scratch

To create a component from scratch, click the **Add Button** in the **Page Selector** or **Widget Tree** tab. Then choose **Add Component > Create Blank Component**.

[Create Component From Scratch](https://demo.arcade.software/shoUH86rXsdpAxtlCOKq?embed\&show_copy_link=true)

#### Convert to a Component

If you have already built a complex widget in your page, you can convert that entire widget into a component and reuse it throughout your app.

To convert a complex widget into a reusable component, right-click on the root widget that contains the entire widget tree you want to convert, then select **Convert to Component.**

[Convert into a component](https://demo.arcade.software/if0fCrWpn6wVDdcGbW0E?embed\&show_copy_link=true)

#### Creating Component from Template

FlutterFlow offers multiple popular templates for components across various use cases that you can apply to your project in seconds, saving time.

[Create from template](https://demo.arcade.software/z4aoeN7TK0Zxp6EseLuD?embed\&show_copy_link=true)

#### Generate with Designer

You can quickly create a component with [FlutterFlow Designer](https://designer.flutterflow.io/) by describing what you want in natural language. Designer uses your description along with your project context, to build the component with relevant widgets.

[Generate with Designer](https://demo.arcade.software/VAsk3ElbFb9ehAV2e94k?embed\&show_copy_link=true)

#### Import from Figma Frame

You can quickly turn your Figma designs into functional FlutterFlow components using **Import from Figma**. Provide a Figma Frame URL, and FlutterFlow AI will analyze the design and generate a UI layout that closely matches your mockup.

To get started, first [connect your Figma account](https://docs.flutterflow.io/concepts/design-system#import-figma-theme). Then, when creating a new component, select **Import from Figma** from the available options. Paste the Figma Frame URL and click **Import**.

FlutterFlow will display a preview of the selected frame. Review the preview, then click **Generate** to create the component. Once completed, the component will appear in the **AI Generation History**, where you can preview and add it to your project.

> **Warning:** Currently, FlutterFlow doesn't support importing SVG elements from Figma frames. However, you can manually add the SVGs directly to your project [**assets**](https://docs.flutterflow.io/generated-code/project-structure#assets) after generation is complete, or replace them in Figma with supported image formats like PNG or JPEG.

[Import from Figma](https://demo.arcade.software/V4kUtFFezchW03HIeqyY?embed\&show_copy_link=true)

#### Component Properties Panel

When you select a component from the widget tree, the Properties panel opens on the right side of the interface. Use it to configure and manage the various aspects of your components.

Here’s what you can typically find and modify in this panel:

![components-configurations.png](https://docs.flutterflow.io/assets/images/components-configurations-92b76049a4a278d21dfad82454a6f149.png)

#### Component Parameters

Component parameters are values that a component receives from its parent entity, such as a page or another component. These parameters allow the component to be dynamic and adaptable based on the context in which it is used. By using parameters, you can customize components for different scenarios without altering the base design or functionality.

##### Creating a Component Parameter

To create a component parameter, go to the root widget in the component's widget tree.

[Adding a Parameter](https://demo.arcade.software/chgEkWJpUFAIUzoB0LuG?embed\&show_copy_link=true)

##### Bind the Parameter

Once you have created a component parameter, you can link data from the parent entity to your component.

Here's a small example of how we can bind the parameters created in `ProfileListItem` to their respective widgets and action triggers.

[Bind Parameters in Components](https://demo.arcade.software/ixR32sxe5W97bEaS1hTt?embed\&show_copy_link=true)

Aside from standard data types used throughout FlutterFlow, you can also create parameters of the following types:

* **Action (callback)**: This allows you to pass actions into the component. The component can then invoke the action, usually referred to as a callback, in its own action flows. Callbacks are often used to handle events, like updating a parent's state when a button has been pressed. [You can learn more about how to use callbacks here.](https://docs.flutterflow.io/resources/ui/components/callbacks)

* **Widget Builders**: Widget builders allows you to pass in widgets to be used within the component's widget tree. This is especially useful when you want to dynamically substitute content for part of a component, such as displaying an item in a custom dropdown, or creating a component for some consistent layout. [You can learn more about how to use Widget Builders here.](https://docs.flutterflow.io/resources/ui/components/widget-builder)

##### Actions

This tab allows you to define and manage interactions or events triggered by user actions. For example, you can configure a button to navigate to another page or execute a callback action from the page using the current component.

Adding an action to a component element is exactly the same experience as adding actions to any page element. Here's a quick overview:

![component-actions.png](https://docs.flutterflow.io/assets/images/component-actions-bd0cc8a019bc88f5efc73a08e46b7f6f.png)

For component actions, you can establish specific behaviors or functions that are triggered by certain events related to the component's lifecycle, such as **On Initialization**.

> **Info:** To learn more about component lifecycle and adding **On Initialization** action to your component [**refer here.**](https://docs.flutterflow.io/resources/ui/components/component-lifecycle)

##### State Management

Components can have their own internal state variables that track information like form inputs, toggles, or other user interactions. Components can update their state in response to user actions (e.g., clicking a button) or external events (e.g., receiving new data from an API).

Effective state management ensures that components dynamically update their UI to reflect changes in state, providing a responsive user experience.

> **Info:** Learn how to **[Create a State variable](https://docs.flutterflow.io/resources/ui/components/component-lifecycle#creating-a-component-state)** for your components and how to **[Update them](https://docs.flutterflow.io/resources/ui/components/component-lifecycle#update-component-state-action)**.

---

### Using Components {#using-components}

*Components in FlutterFlow can be added to the widget tree of a page or another component. They help streamline*

**Source:** https://docs.flutterflow.io/resources/ui/components/using-components

Components in FlutterFlow can be added to the widget tree of a page or another component. They help streamline development by allowing you to reuse design and functionality throughout your app. Components can accept parameters, making them adaptable to specific contexts. Additionally, you can use [callbacks](https://docs.flutterflow.io/resources/ui/components/callbacks) to pass actions from parent entities to child components, enabling dynamic and interactive behavior. You can also use [widget builders](https://docs.flutterflow.io/resources/ui/components/widget-builder) to substitute dynamic content into the component's widget tree.

To learn more about creating components, see [Creating a Component](https://docs.flutterflow.io/resources/ui/components/creating-components).

#### Add a Component to a Widget Tree

To add a component to the widget tree of a page or another component, choose the parent entity where you want to add the new component. Next, you can find the component in the Widget Palette, under the **Components** section.

[Add component to Page](https://demo.arcade.software/EBpdB2PtNGPGzKh7O2eQ?embed\&show_copy_link=true)

##### Specify Parameter Values

In FlutterFlow, each component instance can receive unique values from its parent entity. When you add a component to the widget tree, you can set the parameter values by clicking on the instance of the component and going to the **Properties panel**.

[Pass Down Values](https://demo.arcade.software/t4r4TKLGrRvdthCZYdvm?embed\&show_copy_link=true)

#### Setting a Unique Key

When you use a component in a dynamically generated list, you can set a unique key. For example, imagine a dynamic list where items change frequently, such as a to-do list where tasks are added and removed. Think of it as giving each task a unique ID number. This is important for a few reasons:

* **Tracking Changes:** The **Unique Key** helps the app recognize which tasks are new, completed, or removed, ensuring accurate updates.

* **Efficiency:** With unique IDs, the app updates only the tasks that have changed instead of the entire list, improving performance.

* **Retaining Details:** When you modify a task and move away from it, the **Unique Key** ensures the changes are remembered and displayed correctly when you return.

> **Tip:** If it's a list of documents, the unique key might be the document ID.

![component-unique-id.avif](https://docs.flutterflow.io/assets/images/component-unique-id-03e509dec30fb19e7da5eed06d683939.avif)

#### Recursive Components

You can create a recursive component, which means the component can include an instance of itself within its own widget tree. This is especially useful for nested content.

For example, in social media applications or forums, comments can have replies, and each reply can have further replies. A recursive component can display this nested structure effectively.

![recursive-comp.png](https://docs.flutterflow.io/assets/images/recursive-comp-13c03bf3a4f9d465909348ae5e025ad1.png)

---

### Widget Builder Parameters {#widget-builder-parameters}

*Sometimes, you want to create a component that offers some consistent design, while also allowing for customization. This is where passing widget builders as parameters becomes valuable.*

**Source:** https://docs.flutterflow.io/resources/ui/components/widget-builder

Sometimes, you want to create a component that offers some consistent design, while also allowing for customization. This is where passing widget builders as parameters becomes valuable.

Widget builder parameters allow component authors to substitute dynamic content within the widget tree of the component. This means that when someone uses the component, they can dynamically pass in pieces of UI to be used within the component.

For example, consider a custom dropdown component. While the overall structure of the dropdown remains the same, you might need to change the style or content of the dropdown items based on different use cases. By passing the dropdown item widget as a parameter, you can reuse the dropdown's appearance and behavior without creating new components for each variation.

Possible use cases

* **Custom Cards**: Imagine you need to display product cards in an e-commerce app. You can build a reusable card component with parameters for the image, header, content, and call-to-action button. This card can be reused across multiple pages but with different content.
* **Dynamic Forms**: Build a form component where different fields (TextFields, Dropdowns, or Checkboxes) are passed in as parameters. This allows you to reuse the same form structure but adapt to various input fields.
* **Modular Layouts**: Create a consistent layout structure with areas like headers and footers that remain the same while passing in different body content as parameters to adapt to different pages.

Let’s see an example from an ecommerce app. On the shipping address page, you may want to maintain a consistent design for the various input fields (where the user can specify their name, email, etc.). However, you may want to allow customization for different inputs - for example, you want to use a `TextField` to allow the user to type their name, and a `DropDown` to allow the user to select their country.

![widget-builder-as-parameter-example.avif](https://docs.flutterflow.io/assets/images/widget-builder-as-parameter-example-1bf822ec372b4fbb9f3305d6c7d0932d.avif)

#### Creating Widget Builders as Parameters

To create a component with a widget builder as a parameter, use the steps outlined below.

##### Create a Parameter of Type Widget Builder

Create a new component and add the base widgets that will be unchanged. Next, define a parameter and set its type to **Widget Builder**. To pass data from the current component to the widget builder, you can specify a parameter for the widget builder.

##### Add the Widget Builder to the Widget Tree

Add the widget builder placeholder to the desired spot in the component’s widget tree where the dynamic element should appear. Widget builders appear in the **Components** section of the **Widget Palette** when adding a widget to the widget tree.

##### Pass Parameters to the Widget Builder

Sometimes, you need to pass data from the component to the widget builder. For example, on the shipping address page, you might want the hint text in an input field to change depending on some configuration. In this case, you can pass the hint as a parameter into the widget builder. Here’s how you do it:

###### Preview the Widget Builder Using Different Components

You can select different components to use as a preview while building the component that has a widget builder parameter.

To select a component to use in the preview, select the Widget Builder, then go to the **Widget Builder UI Properties** section of the **Properties panel**.

![preview-component.png](https://docs.flutterflow.io/assets/images/preview-component-7f90a152b97333c3d433330463decaa5.png)

#### Using Components with Widget Builders as Parameters

When you use a component that has a widget builder parameter, you can pass [components](https://docs.flutterflow.io/resources/ui/components) to customize the content according to your needs.

In this example, we create two additional components for `TextField` and `Dropdown` — and pass them as widget builders.

---

### UI Building Blocks {#ui-building-blocks}

*When designing user interfaces in FlutterFlow, understanding the fundamental building*

**Source:** https://docs.flutterflow.io/resources/ui/overview

When designing user interfaces in FlutterFlow, understanding the fundamental building blocks—ranging from atomic to more complex structures—is crucial. The way UI is structured in FlutterFlow closely resembles the concept of **Atomic Design**, a methodology that segments UI into distinct levels of complexity.

In **Atomic Design**, we start with the smallest, indivisible components known as "atoms"—these are your basic building blocks. From there, we combine these atoms to form "molecules," which then come together to create "organisms" or larger functional units. By applying this hierarchical structure to FlutterFlow, we streamline the UI development process, making it both efficient and manageable.

Now, let’s explore how this structured approach plays out in FlutterFlow, from the simplest elements to the creation of full-fledged interfaces:

* **Atoms**

  * These are the fundamental building blocks that serve as the foundational elements of the UI.
  * **Example:** `TextField`, `Button`, `Icon`.

* **Molecules**

  * These are groups of atoms bonded together and are the smallest fundamental units of a compound. These form the basic building blocks of pages but can often be used on their own.
  * **Example:** `EmailSignInField` (which could include an `TextField` atom and an `Icon` atom).

* **Organisms**

  * These are groups of molecules joined together to form a relatively complex, distinct section of an interface.
  * Example: `LoginComponent` (which could include the `EmailSignInField` molecule, another similar `PasswordSignInField` molecule, and a `SubmitButton` atom).

* **Pages**

  * Pages are complete screens and represent the final visible output that users interact with. They are composed of smaller units that work together to provide a full experience, including all the necessary functionality and design elements.
  * **Example**: `SignInPage`

Now let's apply the above concepts to what we see in FlutterFlow as we create our first [project](https://docs.flutterflow.io/resources/projects).

#### Pages

In FlutterFlow projects, a **Page** is essentially a new section or feature of your app that combines various UI elements to form a complete screen in the app. When you create a new project in FlutterFlow, an empty page called `HomePage` is the first thing you see on your canvas.

How you define your pages defines the flow of the app and user experience for the user. For example, in our [**E-commerce Demo app**](https://bit.ly/ff-docs-demo-v2), after login, the user lands on `ProductListPage` which has a NavigationBar at the bottom that takes the user to different Pages in the app such as `ProfilePage`, etc.

> **Info:** Learn more about creating a new [**Page**](https://docs.flutterflow.io/resources/ui/pages) and using its [**Page Elements**](https://docs.flutterflow.io/resources/ui/pages/scaffold) like AppBar, Drawer, etc.

#### Widgets

A Page usually contains a combination of widgets and components. ![everything-widget.png](https://docs.flutterflow.io/assets/images/everything-widget-e85b2e0546ad6daf4a5eb16ccff5dac3.png)

Let's talk about widgets first, which are the atomic elements or building blocks of the UI structure in FlutterFlow.

Each widget can be thought of as an atom or a molecule, depending on its complexity and its parent-child relationship. For example, an atomic widget (such as `TextField`) cannot hold a child element, but molecular widgets (such as `Column` or `Row`) can.

> **Info:** Learn more about the [**basic widgets**](https://docs.flutterflow.io/resources/ui/widgets) and how to [**compose widgets**](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/rows-column-stack) to build more complex UI.

#### Components

In the idea of atomic design, components in FlutterFlow are similar to "organisms." These organisms are made up of simpler parts called *atoms* and *molecules*, or simply widgets, which together form useful and reusable parts of the user interface.

These components are designed to be reusable, meaning they can be utilized across different screens and projects to provide consistent functionality and aesthetics without the need to recreate them from scratch everytime.

> **Info:** Learn more about [**components**](https://docs.flutterflow.io/resources/ui/components) and [**how to use them**](https://docs.flutterflow.io/resources/ui/components/using-components) in pages.

#### Classes vs Instances

When you add a UI element to your page, you are utilizing widget **classes** and creating **instances** of them.

For example, `Icon` is a **widget class**. When you use it in different parts of your application, you're creating an **instance** of the `Icon` widget class and providing different values to it for each use.

Think of classes as templates that outline the structure and features of something you want to create multiple times. For instance, in our demo app [EcommerceFlow](https://bit.ly/ff-docs-demo-v2), we have a reusable component called `ProductListCard` with specific characteristics such as image, product information text, and actions it should perform when clicked. Here, we've essentially created a **class**.

When you place this `ProductListCard` in different Pages of your app, each one you add is an `instance`. For example, in the `ProductListPage`, we have created an **instance** called `topSellingProductCard` for use in the Top Selling section. Similarly, in the `CategoryProductListPage`, we've created an **instance** called `categoryProductCard`.

![Class-Instance.png](https://docs.flutterflow.io/assets/images/Class-Instance-92597e040b9cfb524243eb8631e8a6d1.png)

You can customize each **instance** of your component to perform different actions or to fit different parts of your app, but they all start from the template you created (**the class**). This means you only need to design the `ProductListCard` once and then can reuse and adapt it as needed, simplifying your app development process and ensuring consistency across your project.

---

### Introduction to Pages {#introduction-to-pages}

*In FlutterFlow, a Page represents a single screen in your app. Under-the-hood pages use a Scaffold, a foundational widget from Flutter that provides a structured layout for a screen within your app. The Scaffold offers essential elements like the AppBar and Body, allowing you to easily build screens.*

**Source:** https://docs.flutterflow.io/resources/ui/pages

In FlutterFlow, a **Page** represents a single screen in your app. Under-the-hood pages use a **Scaffold**, a [foundational widget from Flutter](https://api.flutter.dev/flutter/material/Scaffold-class.html) that provides a structured layout for a screen within your app. The Scaffold offers essential elements like the AppBar and Body, allowing you to easily build screens.

Pages are composed of various UI elements, or widgets. Widgets are added to a page when they are added to the page's **Widget Tree**.

Widget Tree

The **Widget Tree** is a structural representation of how widgets are organized within a Page. To learn more, check out the [**Widget Overview**](https://docs.flutterflow.io/resources/ui/widgets#widget-tree) documentation.

In FlutterFlow, pages are automatically configured to handle [routing](https://docs.flutterflow.io/resources/ui/pages/properties#route-settings). Additionally, pages can have [input parameters](https://docs.flutterflow.io/resources/ui/pages/properties#page-parameters) and [state variables](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#page-state).

> **Info:** For more details on how to use Scaffold and the various Page Elements in FlutterFlow, see the dedicated **[Page Elements](https://docs.flutterflow.io/resources/ui/pages/scaffold)** guide.

#### Creating a Page

In FlutterFlow, you can craft a page tailored to your needs and design preferences. Whether you're starting from scratch, using a template, or leveraging AI tools, there are several pathways to achieve the desired functionality and aesthetic of your desired Page.

Generated Code

When you create a page in FlutterFlow, a `Widget` class and a corresponding `Model` class are automatically generated. You can view these in the Code Viewer. To explore the details of the generated `Model` class, take a closer [**look at the code**](https://docs.flutterflow.io/generated-code/page-model).

FlutterFlow allows you to easily create new pages from the **Page Selector** tab in the **Navigation Menu**.

![create-new-page.avif](https://docs.flutterflow.io/assets/images/create-new-page-a5d5b49373456a2bf75da5365f3fbd77.avif)

##### Create Empty Page

When creating your page in FlutterFlow, one option is to start with an empty page, providing you with a blank canvas. This approach allows you to build your UI from the ground up by composing widgets and components together according to your specific design vision and functional requirements.

To create an empty FlutterFlow Page from scratch, follow these steps:

##### Create Page from Template

FlutterFlow simplifies the process of page creation by offering a variety of popular template use cases. These templates provide a basic structure for your pages, which you can quickly customize with your own styling, widgets, and text.

To utilize a template from FlutterFlow, follow these steps:

[Create a page from a popular template](https://demo.arcade.software/JBhxcBBPb7r1Yk6YwehS?embed\&show_copy_link=true)

##### Generate with Designer

You can quickly create a page with [FlutterFlow Designer](https://designer.flutterflow.io/) by describing what you want in natural language. Designer uses your description along with your project context, to build the page with relevant widgets. This is especially helpful when you're starting from scratch or prototyping ideas rapidly.

[Generate with Designer](https://demo.arcade.software/oRmGZOkvdnM844VZfHLq?embed\&show_copy_link=true)

##### Import from Figma Frame

You can quickly turn your Figma designs into functional FlutterFlow pages using **Import from Figma**. Simply provide a Figma Frame URL, and FlutterFlow AI will analyze the design and generate a UI layout that closely matches your mockup.

To get started, first [connect your Figma account](https://docs.flutterflow.io/concepts/design-system#import-figma-theme). Then, when creating a new page, select **Import from Figma** from the available options. Paste the Figma Frame URL and click **Import**.

FlutterFlow will display a preview of the selected frame. Review the preview, then click **Generate** to create the page. Once completed, the page will appear in the **AI Generation History**, where you can preview and add it to your project.

> **Warning:** Currently, FlutterFlow doesn't support importing SVG elements from Figma frames. However, you can manually add the SVGs directly to your project [**assets**](https://docs.flutterflow.io/generated-code/project-structure#assets) after generation is complete, or replace them in Figma with supported image formats like PNG or JPEG.

---

### Page Lifecycle {#page-lifecycle}

*In FlutterFlow and Flutter, understanding the page lifecycle, or the stages a page goes*

**Source:** https://docs.flutterflow.io/resources/ui/pages/page-lifecycle

In FlutterFlow and Flutter, understanding the page lifecycle, or the stages a page goes through from creation to disposal, is essential for managing resources and data effectively.

Let's delve into the key moments in the lifecycle of a **Page**:

* **Initialization**: This is the first phase where the page is set up. Here, the initial data is loaded. This might involve setting up the necessary state or defaults for the page.
* **Rendering**: Here, the page is actually drawn or rendered on the screen. This includes setting up the layout, styles, and any interactive elements. The user can now see the page in its initial [state](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#page-state).
* **Updating:** After rendering, the page becomes interactive and can respond to user inputs such as clicks, typing, or other gestures. It may re-render parts of the page or the entire page to reflect changes from user interaction or new data.
* **Disposal**: When the page is no longer needed, or the user navigates away, this phase is triggered. This is where resources related to the page are released from memory.

In FlutterFlow, most of these lifecycle phases are handled internally by FlutterFlow's architecture. However, FlutterFlow exposes some lifecycle methods so that you, as a developer, can decide what additional configurations to load upon initialization and when to re-render the UI based on interactions.

#### Page-Level Action Triggers

There are several **[Action Triggers](https://docs.flutterflow.io/resources/functions/action-flow-editor#action-triggers)** that are accessible at the root level of a page.

What are Action Triggers?

**Action Triggers** serve as event listeners or handlers that respond to specific events or user interactions within an application. FlutterFlow provides developers with a way to define logic that responds to various events, such as button clicks, page loads, form submissions, or data changes. To learn more, see the **[Action Flow Editor](https://docs.flutterflow.io/resources/functions/action-flow-editor)** section.

As you open the [Action Flow Editor](https://docs.flutterflow.io/resources/functions/action-flow-editor) for your Page, you can see the following Action Triggers exposed for your Page.

![actions-triggers.png](https://docs.flutterflow.io/assets/images/actions-triggers-e7a59d7f7e2da33c600e2286251c6dee.png)

##### On Page Load \[Action Trigger]

This allows you to set actions when the page loads or initializes. It enables developers to perform tasks or execute logic at specific points in the page lifecycle, such as fetching data from an API, initializing variables, or updating UI elements.

Possible use cases

* **Initializing Data:** You can use the **On Page Load** action trigger to initiate API calls, database queries, or read from local storage, setting up the data that the page needs to display. This ensures that all necessary data is ready and available by the time the user sees the page.

* **Setting State:** If your page depends on certain state conditions (like toggles, selections, or input fields), you can set these states appropriately as the page loads.

* **Running Animations:** Start animations that welcome users or draw attention to certain UI elements on the page.

To add an action to **On Page Load** action trigger, follow the steps:

[app.flutterflow.io/authentication](https://demo.arcade.software/ii0otHqkoRtPY66n4c2y?embed\&show_copy_link=true)

Generated Code

When you add actions to the **on Page Load** action trigger, they are executed within a `SchedulerBinding.instance.addPostFrameCallback((_)` method. This ensures that the actions run after the widget tree is fully built. For more details, refer to the [**Page: Generated Code**](https://docs.flutterflow.io/generated-code/page-model#onpageload-action-generated-code) document.

##### On Phone Shake \[Action Trigger]

Actions added under this trigger run when the user shakes their phone. This is useful when you want to perform certain tasks or trigger specific actions in response to a phone shake gesture.

Possible use cases

* **Randomizing content:** Shake the phone to generate a random number, display a random quote, or change the background image.
* **Refreshing data:** Shake the phone to trigger a data refresh, such as fetching the latest news articles or updating a live feed.
* **Resetting the app state:** Shake the phone to reset the app state, clear form fields, or return to the app's home screen.

##### On Shortcut Press \[Action Trigger]

This action trigger lets you bind keyboard shortcuts to actions. This is incredibly helpful for improving accessibility and enhancing user experience, especially in web and desktop apps.

Possible use cases

* **Create New Issues in Project Management Apps:** In project management apps like Linear, users can press `C` to quickly open a form for creating a new issue or task.
* **Form Submission:** Users can press a key combination (e.g., `Ctrl + Enter`) to submit a form.
* **Navigating Between Pages:** Use shortcuts like `Ctrl + Right Arrow` to navigate between pages without using the mouse.

important

* When a keyboard shortcut is created at the page level, it won't trigger if a TextField is in focus, and you also won't be able to type the shortcut key into the TextField.
* When a keyboard shortcut is created at the component level, it also won't trigger if a TextField is in focus, but you'll still be able to type the shortcut key into the TextField.
* **To avoid conflicts, use shortcuts that users are unlikely to type, such as Command + S, instead of a single key like 'S'.**
* There's currently a known issue with Flutter's autofocus functionality. If a TextField inside a component has autofocus enabled, and the component has a keyboard shortcut, the TextField will not autofocus as expected.

Implementing keyboard shortcuts is a straightforward process in FlutterFlow. You can define as many shortcuts as you want, each mapped to specific actions that will trigger when the corresponding key combination is pressed. Let's see an example of an eCommerce web app where users can quickly access the cart page by pressing the `C` key.

To create a shortcut, use the **On Shortcut Press** action trigger, then enter the keys your app should listen for.

Keyboard Shortcuts & Text Fields

When implementing keyboard shortcuts on a page or component with a text field, you may need to ensure the text field ignores those shortcuts.

For instance, if you have a shortcut assigned to the letter "C" and a user tries to type "C" in the text field, you likely want the input to capture the keypress without triggering the shortcut.

To handle this, you can enable the option on the `TextField` widget to bypass keyboard shortcuts. However, it's generally better to assign more unique combinations, like Cmd + C, which are less likely to conflict with normal typing in a text field.

##### On Dispose \[Action Trigger]

The **On Dispose** action trigger allows you to define actions that execute when a page is navigated away from or removed from memory. It is particularly useful for stopping ongoing operations.

Imagine a scenario where [audio recording](https://docs.flutterflow.io/concepts/file-handling/displaying-media#audio-recording) is started when the page loads using the [On Page Load](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#on-page-load-action-trigger) action trigger. The recording process runs as long as the user remains on the page. However, when the user navigates away, you need to stop the recording to save resources and ensure the recorded audio is finalized. By using the **On Dispose** action trigger, you can safely stop the recording and save the file.

Additionally, if you are using a third-party package that relies on persistent connections or listeners, you can leverage [Custom Actions](https://docs.flutterflow.io/concepts/custom-code/custom-actions) with the On Dispose action trigger to close streams or cancel subscriptions.

Possible Use Cases

* **Cleaning Up Resources:** Use this action trigger to cancel timers, close database connections, or unsubscribe from streams to prevent memory leaks and unnecessary processing. * For example, real-time applications, such as stock trading platforms, rely on WebSocket connections to fetch live updates. A homepage displaying a live ticker of stock prices would require opening the WebSocket connection on page load and closing it when **On Dispose** runs. Without an On Dispose trigger, the WebSocket connection could remain open unnecessarily, leading to wasted resources and app instability.
* **Finalizing Database Transactions**: Commit or roll back database transactions if the user leaves the page before completing the process.
* **Logging or Analytics:** Track user behavior or log events (e.g., page exit or time spent on a page) to monitor user engagement and improve the application experience.

![page-on-dispose.avif](https://docs.flutterflow.io/assets/images/page-on-dispose-8025fe786790802aac8cd697c25dabfa.avif)

#### Page State

State Variables

A state variable holds information or data about your UI at any given moment. To learn more about **states and state management, [refer to this guide](https://docs.flutterflow.io/concepts/state-management)**

**Page state** refers to the information that a page tracks about its current condition or the data it displays. This can include things like which tabs are active, the contents of a form, or any user interactions. Managing state is crucial for dynamic pages that interact with user inputs or load varying data. Page State variables are only accessible within the given Page scope.

This type of variable can be useful for storing data that needs to be shared between different widgets on the page, such as form data, a search query, and filtering or sorting options.

For example,

* In a multistep form, you might use a **Page State** variable to store the current step number or the user's input for each step.
* Or, on a search results page, you could use a **Page State** variable to store the search query entered by the user and the current filtering and sorting options applied to the results.

This allows you to maintain the state of the page as the user interacts with different widgets and components.

When a **Page State** variable changes, you can choose to re-render the page with the updated values, and it will display a new version of the page with these updates.

##### Creating a Page State

To create a new Page State variable on your page, follow the steps:

[Create Page State](https://demo.arcade.software/Qhg62nqMjhg8973XPQhb?embed\&show_copy_link=true)

While creating a Page State, the following properties are included:

* **Is List:** This property determines whether the variable can hold multiple values of the same data type (like a list or array) or just a single value.

* **Initial Field Value:** This property sets the default value for the variable when it is first created. It's like setting the starting point or the value that the variable begins with before anything else happens.

* **Nullable:** This property determines whether the variable can have a null value. When "**Nullable**" is set to true, it means the variable can be empty or have a null value. This is useful when dealing with optional data or scenarios where the absence of a value is valid.

Now, let's apply these concepts to the `searchString` variable in the context of the above example:

* Since `searchString` is used to store a single search query entered by the user in the search bar, "**Is List**" is set to false, therefore it can hold only one value at a time.

* The default value for `searchString` is set to an empty string (""). This ensures that when the homepage loads, the search bar is initially empty, allowing users to enter their search query.

* Since entering a search query is optional and the search bar can be left empty, "**Nullable**" is set to true. This allows the `searchString` variable to be null until the user enters a search query, indicating that no search has been performed yet.

> **Note:** You can set the Data Type of your Page State variable to primitive data types such as **String, Integer, Boolean,** or **Double**, or complex built-in data types such as **Enum, Custom Data Type,** or **Document**. To learn more about the available data types, refer to the [**Data Representation Section.**](https://docs.flutterflow.io/resources/data-representation)

##### Get Page State value

You can access the **Page State** value anywhere on the current page. Any widget can hold the current value of a Page State variable, either to display it in the UI or for transactional logic.

You can set the source value of the widget wherever you see the following icon. This icon indicates that you can link the widget's value to a variable.

![Page-State.png](https://docs.flutterflow.io/assets/images/page-state-5f4d542a831409759613be0d2b79a1cf.png)

##### Update Page State \[Action]

Page State values can only be updated via **Actions**. Whenever you want to update the page state, such as through a button click, user interaction, or form update, add an **Update Page State** action.

[Update Page State](https://demo.arcade.software/ezZO22YHQDqTHeg0uQ8Q?embed\&show_copy_link=true)

###### Rebuild on Update

When updating page state in FlutterFlow, you'll often come across the **Update Type** property in your Action properties. Here's what it means:

**Rebuild Current Page:** This option triggers a re-rendering of the page, ensuring that any changes to the state are reflected in the user interface (UI).

**No Rebuild:** Choose this option when you need to update the state without immediately reflecting the changes in the UI.

> **Tip:** If you want to rebuild a page without updating any state variables, use the [**Rebuild**](https://docs.flutterflow.io/concepts/state-management#rebuild-action) state action.

Expensive Rebuilds

Too many rebuilds can impact performance because rebuilding the widget tree frequently consumes resources and may lead to decreased responsiveness and increased battery usage. Therefore, it's essential to consider the trade-offs and use rebuilds judiciously to maintain optimal app performance.

To learn more about what happens behind the scenes, refer to the [Generated Page](https://docs.flutterflow.io/generated-code/page-model) section.

---

### Properties Panel {#properties-panel}

*In FlutterFlow, the Properties panel on the right helps you set up and manage your pages. It opens when you select the root element in the Widget Tree (on the left).*

**Source:** https://docs.flutterflow.io/resources/ui/pages/properties

In FlutterFlow, the Properties panel on the right helps you set up and manage your pages. It opens when you select the root element in the [Widget Tree](https://docs.flutterflow.io/resources/ui/widgets#widget-tree) (on the left).

The panel is organized into sections, each focusing on different settings to customize your pages.

Here’s what you can typically find and modify in this panel: ![page-properties-panel.png](https://docs.flutterflow.io/assets/images/page-properties-panel-290d268c5c4a072b2ed59dd7dfbe23b2.png)

##### Page Parameters

This section lets you define and manage parameters that your page can receive from other pages in the app. Parameters are essentially variables that hold values that can be passed between pages. For example, you might pass a user ID from a list page to a detail page to display specific information about that user.

LEARN MORE

Learn more about passing data between pages [**here**](https://docs.flutterflow.io/concepts/navigation/passing-data).

##### Route Settings

In FlutterFlow, Route Settings are essential for defining how pages within your application are accessed and interacted with. These settings allow you to customize the URL paths for web and mobile deep linking, set meaningful Page Names as unique identifiers, integrate dynamic parameters into your routes, and set access restrictions based on user authentication.

![route-settings-configs.png](https://docs.flutterflow.io/assets/images/route-settings-configs-4f679eabdb838bc859ca009c4a24ff21.png)

**Skip On Page Load When Inactive**

Ensures that actions are bypassed if the Entry Page or Logged In Page is detected as inactive. This is designed specifically for entry points in the app to prevent unnecessary operations when the page is not fully active, optimizing performance and avoiding redundant executions.

Generated Code

When this option is enabled, the following code is added to your page’s `initState`:

```
if (RootPageContext.isInactiveRootPage(context)) {
       return;
    }
      // On Page Load Actions added after this
```

**Requires Authentication**

When the "Requires Authentication" option is enabled for a page, it ensures that only users who are logged in can access that page. This setting is particularly useful for protecting sensitive or personalized content, as it prevents unauthorized users from viewing or interacting with the page.

Generated Code

When the Route object is created for this Page, setting `requireAuth: true` ensures that only authenticated users can access this page. If "Requires Authentication" is checked, the app will automatically enforce authentication checks before navigating to this page. This is automatically enabled for **Logged In Page**.

```
FFRoute(
    name: 'promotionPage',
    path: '/promotionPage',
    requireAuth: true, 
    builder: (context, params) => PromotionPageWidget(),
  )
```

LEARN MORE

Learn more about Routing [**here**](https://docs.flutterflow.io/concepts/navigation/overview).

#### Advanced Configurations

For more advanced customization and functionality within your FlutterFlow projects, the **Properties Panel** offers various configuration settings. These settings allow for modifying appearance, greater interactivity, dynamic data handling, and more tailored user experiences.

Here's an overview of these additional configurations:

* [Page Properties](https://docs.flutterflow.io/resources/ui/pages/properties#page-scaffold-properties)
* [Actions](https://docs.flutterflow.io/resources/ui/pages/properties#actions)
* [Backend Query](https://docs.flutterflow.io/resources/ui/pages/properties#backend-query)
* [State Management](https://docs.flutterflow.io/resources/ui/pages/properties#state-management)

![advanced-configs.png](https://docs.flutterflow.io/assets/images/advanced-configs-5b53cb0e973f1bde7ae667ca3542f9ba.png)

##### Page (Scaffold) Properties

This section lets you set the fundamental aspects of a page’s layout and behavior, including:

* **Background Color:** This property allows you to set a background color for the entire page. You can choose a color that fits the theme and design of your app.

* **Safe Area:** When this toggle is enabled, the page content will be automatically adjusted so it does not overlap with the system status bar, navigation bar, and other critical device UI elements. This ensures that all elements of the page are visible and accessible on different devices.

* **Hide Keyboard on Tap:** Enabling this option makes the keyboard retract when the user taps anywhere outside the keyboard area on the screen. This is particularly useful for improving user experience by preventing the keyboard from obscuring content.

* **Disable Android Back Button:** When enabled, this toggle prevents the Android back button from affecting the navigation on this particular page. This can be useful in scenarios where you don't want users to navigate back to the previous screen easily, such as in a login or payment screen.

##### Actions

This section allows you to define and manage interactions or events triggered by user actions. For example, you can configure a button to navigate to another page, submit form data, or call an API. Actions are crucial for creating interactive and functional apps.

For Scaffold (Page) actions, you can establish specific behaviors or functions that are triggered by certain events related to the page's lifecycle, such as [**On Page Load**](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#on-page-load-action-trigger) or [**On Phone Shake**](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#on-phone-shake-action-trigger).

LEARN MORE

To learn about the page lifecycle and other methods exposed by FlutterFlow, [**refer to this resource**](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle).

##### Backend Query

Here, you can configure the page to fetch data from a backend source or database. This is typically done through API calls or direct database queries. Setting up a backend query allows the page to display dynamic content, such as user profiles, product lists, or any other data your app needs to retrieve from a server.

LEARN MORE

To learn more about how to connect to a backend source, refer to our [**Database section**](https://docs.flutterflow.io/resources/backend-query)

##### State Management

State management configurations are essential for maintaining the state or status of a page across user interactions or app sessions. This can include tracking user inputs, remembering user choices, or preserving the app's state during navigation between pages.

LEARN MORE

Learn how to create and **[manage the update lifecycle](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle)** of Page State variables.

---

### Page Elements {#page-elements}

*Page elements in FlutterFlow are the key elements that define the structure and functionality of each page in your app. Understanding these elements is crucial for building intuitive and effective user interfaces. From navigational elements like the AppBar and Drawer to interactive components like Floating Action Buttons (FABs), each element plays a specific role in shaping the user experience.*

**Source:** https://docs.flutterflow.io/resources/ui/pages/scaffold

Page elements in FlutterFlow are the key elements that define the structure and functionality of each page in your app. Understanding these elements is crucial for building intuitive and effective user interfaces. From navigational elements like the **AppBar** and Drawer to interactive components like **Floating Action Buttons (FABs)**, each element plays a specific role in shaping the user experience.

Here's how the `Scaffold` contributes to page design in FlutterFlow:

* **[AppBar](https://docs.flutterflow.io/resources/ui/pages/scaffold#appbar)**: Scaffold allows you to easily include an `AppBar` at the top of the page, which can house the title, navigation controls, and other actions.

* **[Floating Action Button (FAB)](https://docs.flutterflow.io/resources/ui/pages/scaffold#floating-action-button-fab)**: An action button that is commonly used for primary actions on the screen, like adding a new contact or composing a message.

* **[Drawer & End-Drawer](https://docs.flutterflow.io/resources/ui/pages/scaffold#drawers)**: A slide-out menu for app navigation, accessible from the `AppBar` or by swiping from the side.

* **Body:** The main content area where you place the widgets for the page.

PLEASE NOTE

In FlutterFlow, you won't find a section explicitly labeled as "Body". For example, in the `ProfileSettingsPage`, the `Column` serves as the root of the widget tree for the body, with the rest of the child widgets assembled underneath.

![scaffold-elements.png](https://docs.flutterflow.io/assets/images/scaffold-elements-91f1c9529e6bb438dd460b27b59dafa5.png)

#### AppBar

**AppBar** is a widget that displays a toolbar at the top of the screen, typically used for branding, navigation, and actions related to the current screen. It supports a title and icons, and offers customization with a variety of styles and functionalities.

The AppBar is divided into the following sections:

* **Leading:** Typically holds a **menu** or **back icon** that provides navigation control. By default, if there is a [**drawer**](https://docs.flutterflow.io/resources/ui/pages/scaffold#drawers) or [**page navigation**](https://docs.flutterflow.io/concepts/navigation/page-navigation) with ["Allow Back Navigation" enabled](https://docs.flutterflow.io/concepts/navigation/page-navigation#navigate-to-action), a specific icon (such as a menu or back arrow) is displayed. However, you can override this with another [**Icon widget**](https://docs.flutterflow.io/resources/ui/widgets/icons) if desired, allowing for more tailored navigation options.
* **Title:** Primarily serves to indicate the content of the active screen or to display the name of the application, aiding users in recognizing their context within the app. This section can also be customized with different widgets for a more tailored visual representation.
* **Actions:** Hosts icon buttons for various operations like search, share, and more, situated on the right end.

##### Add an AppBar

[Add AppBar](https://demo.arcade.software/Gviwe4k9svWyMBr6NLCP?embed\&show_copy_link=true)

##### Enable Default Button

The "Show Default Button" toggle in the **AppBar** Properties Panel controls whether the default leading icon (usually a back arrow or a menu icon) appears when the user can [navigate back](https://docs.flutterflow.io/concepts/navigation/page-navigation) or when a [Drawer](https://docs.flutterflow.io/resources/ui/pages/scaffold#drawers) is present on the page.

However, it's important to note that this default icon won't appear in the FlutterFlow canvas during the design stage. It only becomes visible when the app is running, and the conditions for showing the button are met.

If you wish to replace the default icon with another icon in the leading space, follow the [guide on adding an AppBar](https://docs.flutterflow.io/resources/ui/pages/scaffold#add-an-appbar).

Generated Code

In the generated code, when this toggle is enabled, [`automaticallyImplyLeading`](https://api.flutter.dev/flutter/material/AppBar/automaticallyImplyLeading.html) property in the **AppBar** widget is set to `true`. This means that the appropriate default button will be displayed if back navigation is enabled or Drawer is detected when you run the app.

#### Floating Action Button (FAB)

A **Floating Action Button (FAB)** is a distinctive circular button that hovers over content, commonly used for a primary action within an app, like adding a new item or composing a message.

##### Extended Property

This variant of the `FAB` includes both an icon and a label, making it larger than the standard circular `FAB`. It is useful when you want the action button to convey more information than just the icon can provide, such as text explaining the action ("Add Task", "Create Post", etc.).

**Use cases**

The **extended** `FAB` is particularly beneficial in applications where the action needs clear and immediate recognition from the user, which cannot be fully achieved by an icon alone. It is also useful in interfaces where there is ample space to accommodate a longer button without cluttering the UI.

![fab-comparison.png](https://docs.flutterflow.io/assets/images/fab-comparison-3b65acd5c5d7265223da2b2e9094fb1d.png)

##### Adding a Floating Action Button to your Page

[Add FAB](https://demo.arcade.software/TfHpfAQYIc5iaALgbK2O?embed\&show_copy_link=true)

#### Drawers

**Drawer** is a slide-out menu that can emerge from either side of the screen, typically used for app navigation or placing additional options. It allows users to switch between different sections of an app without cluttering the main interface.

##### Add a Drawer to your Page

[Scaffold - Add Drawer](https://demo.arcade.software/jTl8VlxxDxmhyms7YEVS?embed\&show_copy_link=true)

##### End-Drawer

Using a similar approach, you can also add an End Drawer to your page.

##### Drawer \[Action]

Using this action, you can open and close the drawers with a tap of a button. For example, opening the drawer from a widget placed outside the Appbar and closing it from the widget placed inside the drawer.

###### Types of drawer actions

There are three types of actions you can add to the drawer.

* **Open Drawer**: Opens the regular drawer.
* **Open End Drawer**: Opens the end drawer.
* **Close Drawers**: Closes all the open drawers.

#### Nav Bar

The NavBar (or Navigation Bar) allows you to quickly navigate between pages of your app. It is displayed at the bottom of the screen for convenient access. The items inside the NavBar are represented by an icon, optional text, or both.

You can display up to three or five primary or top-level pages (pages that can be accessed from anywhere in your app) inside the NavBar.

From the NavBar settings page, you can add the NavBar and make modifications such as changing the display style, reordering icons, customizing its appearance, and more.

##### Enable Nav Bar in settings

By default, the NavBar is disabled for any project created in FlutterFlow. Before you can add pages to the NavBar, you need to enable it from the FlutterFlow settings. Navigate to **Setting and Integrations > General > NavBar & AppBar** and enable Nav Bar.

> **Caution:** Initially, your NavBar will not have any pages in it. You'll see a message instructing you to add at least two pages. Before proceeding, make sure to create at least two pages. If you need help with adding a new page, you can find [**more information here**](https://docs.flutterflow.io/resources/ui/pages#creating-a-page).

![nav-bar.png](https://docs.flutterflow.io/assets/images/nav-bar-3e95a622b810f966bed49041ddfd96b3.png)

**Responsive Visibility:** To ensure that your NavBar is visible only on certain screen sizes, you can toggle the device icons based on your design preference.

##### Add Pages to your Nav Bar

Once enabled, you need to select the pages you want to appear in the navigation bar and then add them. Here's how you can do it:

[Nav Bar Add Pages](https://demo.arcade.software/ShQiuWlUfEbCT29G6nyJ?embed\&show_copy_link=true)

###### Nav Bar Properties (Property Panel)

* **Label:** This label will be displayed on the Nav Bar.
* **Nav Bar Icon:** This icon represents the page in the Nav Bar. You can also choose its **size**.

> **Info:** The NavBar will only appear on the canvas if you have added at least two pages to it.

###### Reordering Nav Bar Items

To reorder the Nav Bar items:

* Navigate to the **Setting and Integrations > General > NavBar & AppBar > Nav Bar**.

* Under the **Re-Order Page Icons**, identify the page that you want to reorder, click on the hamburger icon (icon with three lines ) beside it and drag it in an upward or downward direction.

##### Modifying NavBar Style

When you enable the NavBar, it initially adopts the Flutter Default Nav Bar style. However, if you need more customization options, you can set the Nav Bar Style dropdown to one of the following:

###### Flutter Default Nav Bar

This is the standard material style NavBar. You have the option to show or hide labels for both selected and unselected items.

![nav-bar-default.png](https://docs.flutterflow.io/assets/images/nav-bar-default-60c4b4df61a1a36ab816fd9e384e1fad.png)

**Styling Properties**

| Property                     | Type        | Description                                                                                |
| ---------------------------- | ----------- | ------------------------------------------------------------------------------------------ |
| **Show Labels (Selected)**   | Toggle      | Allows you to enable or disable the display of labels for selected items in the `NavBar`.  |
| **Show Labels (Unselected)** | Toggle      | Allows you to enable or disable the display of labels for unselected items in the `NavBar` |
| **NavBar Color**             | Color Wheel | Sets the background color of the `NavBar`                                                  |
| **Selected Icon Color**      | Color Wheel | Specifies the color of the icons when they are selected.                                   |
| **Unselected Icon Color**    | Color Wheel | Specifies the color of the icons when they are not selected.                               |

###### Google Nav Bar

This modern Google-style NavBar features a subtle animation that reveals the item label (page name) but only displays the label for the selected item.

![nav-bar-google.png](https://docs.flutterflow.io/assets/images/nav-bar-google-335c7e5919226da7956c5f7235554cc4.png)

**Styling Properties**

* **Nav Bar Color:** Sets the background color of the NavBar.
* **Selected Icon & Text Color:** Changes the color of the icon and text when an item is selected.
* **Unselected Icon & Text Color:** Sets the color for icons and text when an item is not selected.
* **Selected Background Color**: Alters the background color of the selected item.
* **Show Unselected Border**: Toggles the visibility of a border around unselected items
* **Border Width:** Specifies the width of the border around the NavBar item buttons.
* **Border Radius:** Determines the corner roundness of the NavBar item buttons.
* **Border Color:** Alters the color of the borders around NavBar item buttons.
* **Nav Button Padding:** Adjusts the padding inside each nav button.
* **Nav Button Margin:** Controls the margin around each nav button.
* **Nav Button Alignment:** Allows customization of how nav buttons align within the NavBar. Options include center, space-between, etc., are given.
* **Gap Between Icon and Text:** Specifies the spacing between the icon and text within nav buttons.
* **Animation Duration (ms):** Defines how long animations take when switching between items.
* **Haptic Feedback:** A toggle that enables or disables haptic feedback when interacting with NavBar items, enhancing the tactile experience.

###### Floating Nav Bar

This NavBar style appears as a floating element above the pages and shows labels for all items present in the NavBar.

![nav-bar-floating.png](https://docs.flutterflow.io/assets/images/nav-bar-floating-3d935739e7a9ff390c894e9e2dd54a42.png)

**Styling Properties**

* **Nav Bar Color:** Sets the background color of the NavBar.
* **Selected Icon & Text Color:** Specifies the color of the icon and text when an item is selected.
* **Unselected Icon & Text Color:** Defines the color for the icons and text when they are not selected.
* **Selected Background Color:** Alters the background color of the selected item.
* **Width:** Controls the width of the NavBar.
* **Border Radius:** Determines the roundness of the NavBar's corners.
* **Elevation:** Adjusts the shadow or elevation effect beneath the NavBar, which helps give the NavBar a floating appearance above other content.
* **Button Border Radius:** Specifies the radius for the borders of each button within the NavBar.
* **Nav Button Margin:** Sets the margin around each nav button
* **Nav Button Padding:** Controls the padding inside each nav button.

[YouTube video player](https://www.youtube.com/embed/Qhe8X5ykK54)

#### SnackBar

**SnackBar** is a temporary, lightweight notification that briefly appears at the bottom of the screen to provide feedback about an operation.

##### When to Use Snackbar?

Here are some common uses of a SnackBar in an app:

* **User Feedback:** Notifies users about the success or failure of actions like submitting a form or uploading a file.
* **Undo Actions:** Provides a quick option to undo a recently completed action, such as deleting an email or removing an item from a list.
* **Informational Alerts:** Displays brief messages about changes or updates, such as synchronization status or network issues, without requiring user interaction.
* **Confirmation Messages:** Confirms the completion of tasks that don't need immediate attention, like saving settings or adding a calendar event.

##### To show a SnackBar message

[Show a snackbar](https://demo.arcade.software/wSnox6aBYylpdh2qx1JJ?embed\&show_copy_link=true)

##### Show SnackBar \[Action]

Material Design allows you to add an interactive element to the SnackBar notification, allowing users to respond directly from the snack message.

###### Add Action Property

Typically, a SnackBar can include a single action button. This button is used to offer users an immediate option to interact with the snack message.

Common uses include undoing an action that the snack message refers to (like undoing a deletion), retrying a failed task (like reconnecting to a network), or any other quick recovery or response tasks.

* **Customization:** The action within a SnackBar is customizable. You can define the button's label, appearance, and the function it executes when pressed. This allows the SnackBar to not only inform users but also engage them in meaningful ways to enhance the user experience.

* **Timeouts and Visibility:** The presence of an action can affect the duration the SnackBar is displayed. By default, a SnackBar may auto-dismiss after a few seconds, but if an action button is present, users might need more time to read the message and respond, thus you might consider adjusting the display duration accordingly.

![snackbar-action-props.png](https://docs.flutterflow.io/assets/images/snackbar-action-props-deaac181811c45b593c1d699d548946d.png)

Adding actions to SnackBars helps make them not just informative but also interactive, facilitating a more dynamic user interaction model where feedback and actions are closely linked.

![snackbar.png](https://docs.flutterflow.io/assets/images/snackbar-8d480ecbcad24ca94d4199fce66a182a.png)

##### Hide SnackBar \[Action]

Managing multiple SnackBar instances efficiently is crucial because showing them all at once can overwhelm the user interface and confuse the user. To address this, Flutter apps use a queuing system for `SnackBars`:

**Snackbar Queue:** When multiple SnackBars are triggered in succession, they are queued to be displayed one after the other rather than all at once. Each `SnackBar` waits for the previous one to disappear before the next one shows up.

**Hiding Previous Snackbar:** If you want to immediately replace a currently displayed SnackBar with a new one without waiting for it to auto-dismiss, you can use the **Hide Snackbar** action in FlutterFlow.

The action has the following hide scope:

* **Current Only:** This option hides only the currently displayed snackbar.
* **All (Current and Queue):** This option hides the current snackbar as well as any snackbar in the queue.

This can be useful in scenarios where an immediate update to the user feedback is necessary, such as correcting a message or providing new information. By using these methods, you can control the flow of information via SnackBars, ensuring that user feedback is timely, relevant, and not overwhelming.

---

### Introduction to Widgets {#introduction-to-widgets}

*Introduction to Widgets*

**Source:** https://docs.flutterflow.io/resources/ui/widgets

Widgets are the building blocks of your app's user interface in FlutterFlow. Each widget represents a fundamental UI element that contributes to the overall layout and functionality of your app. In FlutterFlow, you create your app's UI by combining basic widgets like **Text, Button** and **Container** with more complex, multi-child widgets like **Rows, Column, Lists**.

Understanding the parent-child relationship between widgets is crucial, as it forms the foundation of the [**Widget Tree**](https://docs.flutterflow.io/resources/ui/widgets#widget-tree), which defines the structure and hierarchy of your app's UI.

#### Types of Widgets in FlutterFlow

* **Built-in Widgets**: You can choose from a variety of built-in widgets in FlutterFlow. These are discussed throughout this section.

* **[Components](https://docs.flutterflow.io/resources/ui/components/creating-components)**: You can also build your own reusable widgets, or Components by assembling multiple widgets using FlutterFlow’s drag-and-drop interface.

* **[Custom Widgets](https://docs.flutterflow.io/concepts/custom-code/custom-widgets)**: For scenarios where more complex functionalities are required, FlutterFlow allows you to develop your own Custom Widgets using code.

* **[Theme Widgets](https://docs.flutterflow.io/concepts/design-system#theme-widgets)**: Themed widgets can be reused across your app, making it easy to update styles universally. If you decide to change any properties, such as color schemes or fonts, you can update the theme widget instead of modifying each widget individually.

#### Widget Tree

The Widget Tree is a structural representation of how widgets—ranging from [atomic elements](https://docs.flutterflow.io/resources/ui/overview) like Text and Button to more [complex molecules and organisms](https://docs.flutterflow.io/resources/ui/overview)—organized within a Page. It outlines the parent-child relationships that define the layout and functionality of your UI. This hierarchy is similar to the concept of atomic design, where atoms and molecules combine to form more complex structures, ultimately creating a cohesive interface.

WIDGET TREE BREAKDOWN

![tree.png](https://docs.flutterflow.io/assets/images/tree-dd5fad754dcf04fe9f4067413e137386.png)

The above diagram illustrates a widget tree for an `ExamplePage`. The page is structured using a hierarchy of widgets that define its layout and functionality.

* **ExamplePage**: The root of the widget tree, representing the entire Page. * **Column**: Directly under the root, this widget organizes its child widgets vertically. It is the main layout widget for this Page. * **Container**: A molecular widget that contains another widget, providing padding, margins, borders, or color to its child. * **Text**: An atomic widget, this displays a string of text within the `Container`.
    * **Row**: A molecular widget that arranges its children horizontally. It contains multiple `Icon` widgets. * **Icon**: These are atomic widgets, each representing an `Icon` image. They are repeated here twice under the `Row`.
    * **Image**: An atomic widget placed directly under the `Column`, used here to display an image.
    * **Button:** An atomic widget also under the `Column`, used for user interaction.

Each widget in this tree plays a specific role in constructing the user interface, from basic elements like `Text` and `Image` to layout structures like `Row`s and `Column`s that organize these elements.

Here's how this widget tree would be represented in FlutterFlow: ![widget-tree-new.png](https://docs.flutterflow.io/assets/images/widget-tree-new-083629745aefd437e890ea2f81086844.png)

Understanding the widget tree is crucial for developers using FlutterFlow because it helps visualize the composition of the application's interface. It shows how individual widgets (atoms) combine and nest within each other to form more complex widgets (molecules and organisms) and ultimately complete pages.

##### Widget categories

In FlutterFlow, we have the following categories of widgets:

* [Layout Elements](https://docs.flutterflow.io/resources/ui/widgets#layout-elements)
* [Base Elements](https://docs.flutterflow.io/resources/ui/widgets#base-elements)
* [Page Elements](https://docs.flutterflow.io/resources/ui/widgets#page-elements)
* [Form Elements](https://docs.flutterflow.io/resources/ui/widgets#form-elements)

###### Layout Elements

These widgets help organize the structure and layout of your app. They determine how other widgets are arranged and displayed on the screen.

Common layout elements include:

| Widget        | Description                                                                                                               | Example                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Row**       | Arrange its child widgets horizontally                                                                                    | ![](https://docs.flutterflow.io/img/widgets/row-example.png)   |
| **Column**    | Organizes its child widgets vertically.                                                                                   | ![](https://docs.flutterflow.io/img/widgets/col-example-1.png) |
| **Stack**     | Layers its child widgets on top of each other, allowing for overlapping elements.                                         | ![](https://docs.flutterflow.io/img/widgets/stack-example.png) |
| **Container** | Provides a box model for a single child widget, with optional padding, margins, borders, box shadow and background color. | ![](https://docs.flutterflow.io/img/widgets/cont-example.png)  |

Find the entire list on this [**index page**](https://docs.flutterflow.io/tags/layout-elements).

###### Base Elements

Base elements are the fundamental building blocks for creating the visual and interactive components of your app.

Examples include:

| Widget                                        | Description                                                                                                                            | Example                              |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **[Text](https://docs.flutterflow.io/resources/ui/widgets/text)**     | Displays a string of text and allows you to customize fonts, sizes, and styles.                                                        | ![](https://docs.flutterflow.io/img/widgets/text-example.png)   |
| [**Image**](https://docs.flutterflow.io/resources/ui/widgets/image)   | Displays image.                                                                                                                        | ![](https://docs.flutterflow.io/img/widgets/img-example.png)    |
| [**Icon**](https://docs.flutterflow.io/resources/ui/widgets/icons)    | Displays icon.                                                                                                                         | ![](https://docs.flutterflow.io/img/widgets/icon-example.png)   |
| [**Button**](https://docs.flutterflow.io/resources/ui/widgets/button) | A widget meant to trigger actions and take users to another flow in the app. It can be styled with different colors, borders, and text | ![](https://docs.flutterflow.io/img/widgets/button-example.png) |

Find the entire list on this [**index page**](https://docs.flutterflow.io/tags/base-elements).

###### Page Elements

In FlutterFlow, the **Page Elements** category consists of widgets like **[AppBar](https://docs.flutterflow.io/resources/ui/pages/scaffold#appbar)**, **[Floating Action Button (FAB)](https://docs.flutterflow.io/resources/ui/pages/scaffold#floating-action-button-fab)**, **[Drawer](https://docs.flutterflow.io/resources/ui/pages/scaffold#drawers)**, and **[End Drawer](https://docs.flutterflow.io/resources/ui/pages/scaffold#end-drawer)**, which are essential for structuring pages and facilitating navigation throughout the app.

> **Info:** Learn more about **[Page Elements](https://docs.flutterflow.io/resources/ui/pages/scaffold)** such as **AppBar**, **Snackbar**, **Drawers** etc and how to use them in FlutterFlow.

###### Form Elements

Form elements are widgets specifically used for creating forms where users can enter data. These are crucial for tasks like user registration, login, and data entry.

Examples include:

| Widget           | Description                                                       | Example                                            |
| ---------------- | ----------------------------------------------------------------- | -------------------------------------------------- |
| **Text Field**   | Allows users to enter text.                                       | ![Textfield Example](https://docs.flutterflow.io/img/widgets/txtfield-ex.png) |
| **Radio Button** | Allows users to select one option from a set.                     | ![Radio Button Example](https://docs.flutterflow.io/img/widgets/radio-ex.png) |
| **Dropdown**     | Provides a menu with multiple options where users can select one. | ![Dropdown Example](https://docs.flutterflow.io/img/widgets/dropdwn-ex.png)   |

Find the entire list on this [**index page**](https://docs.flutterflow.io/tags/form-elements).

Each category in FlutterFlow serves distinct purposes, helping you design both the appearance and functionality of your app more efficiently.

---

### Basic Widgets {#basic-widgets}

*FlutterFlow offers a range of basic widgets that are the building blocks of a Page or Component. In this guide, we'll cover five fundamental widgets: Container, Text, Icon, Button, and Image. Understanding these widgets is crucial for building any FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/basic-widgets

FlutterFlow offers a range of basic widgets that are the building blocks of a Page or Component. In this guide, we'll cover five fundamental widgets: **Container**, **Text, Icon, Button,** and **Image**. Understanding these widgets is crucial for building any FlutterFlow app.

![basic-widgets.png](https://docs.flutterflow.io/assets/images/basic-widgets-a4c8ea362895b6f1a4472cbc0ad025ca.png)

Some basic widgets include:

* **[Container](https://docs.flutterflow.io/resources/ui/widgets/container)**: The **Container** widget is one of the most commonly used widgets in FlutterFlow. It allows you to create a rectangular or circular box that is allowed to have one single child - any other basic or advanced widget, and you can style it with various properties such as padding, margins, borders, and colors, etc.

* **[Text](https://docs.flutterflow.io/resources/ui/widgets/text)**: The **Text** widget is used to display a string of text with single style. It’s a basic yet powerful widget that allows you to customize text appearance, alignment, and behavior.

* **[Icon](https://docs.flutterflow.io/resources/ui/widgets/icons)**: The **Icon** widget is used to display an icon from the Material Icons, Font Awesome or your own custom icons set. Icons are essential for building user-friendly interfaces, providing visual cues to users.

* **[Button](https://docs.flutterflow.io/resources/ui/widgets/button)**: In FlutterFlow, **Button** widgets are specialized interactive elements that come with built-in visual feedback and default hover properties.

* **[Image](https://docs.flutterflow.io/resources/ui/widgets/image)**: The **Image** widget is used to display images in your app. FlutterFlow supports various sources for images, including assets, network URLs, and uploaded files.

---

### AspectRatio {#aspectratio}

*Learn how to add an AspectRatio widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/aspect-ratio

The `AspectRatio` widget lets you maintain a consistent width-to-height ratio for its child widget. Instead of setting fixed pixel dimensions, you define a ratio, and the widget calculates the height automatically based on the available width. This keeps your UI proportionally consistent across all screen sizes without manual math.

Use it whenever a child widget needs to maintain a predictable shape, regardless of the device — media thumbnails, video players, hero images, or uniform card layouts.

In the widget tree, AspectRatio sits as a wrapper around a single child widget, typically an `Image` or `Video player`. The structure looks like this:

```
Container
    └── AspectRatio
        └── Image
```

AspectRatio controls the bounding box. Whatever child you place inside fills that box.

#### Configuring the Ratio

Select the AspectRatio widget to open its properties panel. Under **Aspect Ratio**, you'll find a **Ratio** dropdown.

##### Preset Ratios

The **Aspect Ratio** widget ships with seven presets covering the most common layout needs:

| Preset | Decimal | Best For                                        |
| ------ | ------- | ----------------------------------------------- |
| 1:1    | 1.0     | Profile pictures, avatars, square thumbnails    |
| 4:3    | 1.333   | Standard photos, product images                 |
| 3:2    | 1.5     | Photography, editorial cards                    |
| 16:9   | 1.778   | Video players, YouTube thumbnails, hero banners |
| 9:16   | 0.563   | Vertical video (Reels, Shorts, Stories)         |
| 3:4    | 0.75    | Portrait photos, book covers                    |
| 2:3    | 0.667   | Posters, portrait cards                         |

##### Custom Value

If none of the presets fit your design, select **Custom** from the dropdown. A **Value** field appears where you enter the ratio as a decimal number.

The formula is simple: divide width by height.

* A 5:4 ratio → enter `1.25`
* A 21:9 ultra-wide ratio → enter `2.333`
* A 4:5 Instagram portrait → enter `0.8`

###### Dynamic Ratio with Variable Binding

The **Value** field supports variable binding. This lets you drive the ratio dynamically at runtime.

**Example use case:** You're building a media feed that shows both landscape videos and portrait photos. Store the ratio as an `double` field in your data model and bind the AspectRatio's value to it. When the feed loads, each card adopts the correct shape automatically — no hardcoded layouts needed.

#### Constraint Warning

When AspectRatio is placed inside a parent that provides tight constraints in both dimensions, meaning the parent has already fixed both the width and height, the widget displays a warning.

**What it means:** AspectRatio works by taking the available width and calculating height from the ratio. If the parent has locked the height too, there is no room for AspectRatio to do its job. The ratio is ignored, and the child simply fills the parent's fixed dimensions.

**Common triggers:**

* Nesting it inside a `Container` that has both a fixed width and fixed height set
* Placing AspectRatio inside a `Row` without wrapping it in an `Expanded` or `SizedBox`
* Putting it inside a `Column` with `MainAxisSize` set in a way that squeezes available space

**How to fix it:**

* Remove the fixed height from the parent `Container` and let AspectRatio drive the height.
* If inside a `Row`, wrap AspectRatio in an `Expanded` widget so it receives unconstrained width first.

---

### Badge {#badge}

*The Badget widget indicates the number of items that need your attention. Typically it's a medium-sized dot that floats over other widgets such as IconButton.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/badge

The Badget widget indicates the number of items that need your attention. Typically it's a medium-sized dot that floats over other widgets such as IconButton.

For example, You could use the badge widget to show the number of unread notifications and items in your shopping cart.

![img\_3.png](https://docs.flutterflow.io/assets/images/img_3-cb5b5453c62028011d19f823b3e07cd9.png)

#### Adding Badge widget

Here's an example of how you can add the Badge widget to your project:

1. First, drag the **Badge** widget from the Base Elements tab and carefully drop it into the Actions section of the AppBar.
2. Now, add the **IconButton** widget inside the **Badge** widget. Customize the Icon and its color as per your requirement.
3. Select the **Badge** widget, move to the properties panel, and set the **top** side padding to 5 and **right** side padding to 15.

#### Customizing

You can customize the appearance and behavior of the badge widget using the various properties available under the **Properties Panel**.

##### Setting badge text

You can set the badge text that appears inside the badge. Usually, it's a numeric value.

To set the badge text:

1. Select the **Badge** widget from the widget or the canvas area.
2. Move to the properties panel (on the right side of your screen), and scroll down to the **Badge Properties** section.
3. Find the **Text** property and enter a value. You would probably set this value from the variable or field from the backend database, such as the API response variable and Firestore document field. To do so, click on the **Set from Variable**.

##### Styling badge text

To change the badge text style:

1. Select the **Badge** widget from the widget or the canvas area.
2. Move to the properties panel (on the right side of your screen), and scroll down to the **Badge Properties** section.
3. Find the **Theme Text Style** property and change the style as per instructions [here](https://docs.flutterflow.io/resources/ui/widgets/text).

##### Show/hide badge

You might want to hide the badge widget initially and only show it when some items need the user's attention—for example, showing the notification badge only when there are new/unread notifications.

To show/hide the badge widget:

1. Select the **Badge** widget from the widget or the canvas area.
2. Move to the properties panel (on the right side of your screen), and scroll down to the **Badge Properties** section.
3. Find the **Show Badge** property and check/uncheck to show/hide the badge. Most probably, you would set this value from the variable such as the app state variable and variable from API response. To do so, click on the **Set from Variable**.

##### Changing badge color

To change the badge color:

1. Select the **Badge** widget from the widget or the canvas area.
2. Move to the properties panel (on the right side of your screen), and scroll down to the **Badge Properties** section.
3. Find the Badge Color property, click on the box next to the already selected color, select the color, and then click **Use Color** or click on an already selected colorand enter a Hex Code directly. You can also choose the color by clicking the **Palette** and **Simple** button.

##### Changing elevation

To change the elevation (depth or Z-axis) of the badge:

1. Select the **Badge** widget from the widget or the canvas area.

2. Move to the properties panel (on the right side of your screen), and scroll down to the **Badge Properties** section.

3. Find the **Elevation** input box and enter the value to see the drop shadow effect below the badge. The Higher value sets the bigger size of the shadow, and the 0 value removes the shadow.

##### Changing badge position

By default, the badge is displayed on the top right side of its child widget. You can change its position and bring it to the left side.

To change the badge position:

1. Select the **Badge** widget from the widget or the canvas area.
2. Move to the properties panel (on the right side of your screen), and scroll down to the **Badge Properties** section.
3. Find the **Position (Start or End)** property and click on the icons to change the position.

##### Allow animating badge

By default, the badge widget animates whenever the value is changed.

To allow/disallows animating badge:

1. Select the **Badge** widget from the widget or the canvas area.

2. Move to the properties panel (on the right side of your screen), and scroll down to the **Badge Properties** section.

3. Find the **Animate** toggle, and then turn it on or off.

---

### Barcode {#barcode}

*The Barcode widget is used to embed the information inside the series of lines and patterns. The data inside the barcode can be easily retried with a scanner machine, an app like Google Lens (Android), Apple Camera (iOS), or your own app created using FlutterFlow.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/barcode

The Barcode widget is used to embed the information inside the series of lines and patterns. The data inside the barcode can be easily retried with a scanner machine, an app like [Google Lens](https://lens.google/) (Android), [Apple Camera](https://support.apple.com/en-in/HT208843) (iOS), or your [own app](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/barcode#scan-barcode--qr-code-action) created using FlutterFlow.

It is typically used to retrieve product information quickly and accurately. For example, you could track the inventory/books (e.g., price, description, location, etc.), share website/app URL, quick onboarding process, and so on.

![img\_4.png](https://docs.flutterflow.io/assets/images/img_4-2b518112d20901711080da59327256da.png)

#### Adding Barcode widget

To add a Barcode widget to your app:

1. First, click on the **+ Add Widget**, drag the **Barcode** widget from the **Base Elements** tab, or add it directly from the widget tree.

2. By default, the barcode is displayed in a linear fashion called **1D Barcode**. (i.e., a series of lines and space of various widths). To display the barcode in a matrix form, such as QR-Code, move to the properties panel and set the **Barcode Dimensions** to the **2D Barcode**.

3. Now, you'll need to figure out the type of information you want to embed and select the **Barcode Type**. The barcode type options are available based on the *Barcode Dimensions* you selected in the previous step. For example, to label the retail products (i.e., 12 digits numeric only number), you can set it to *UPC-A* or *UPC-E*, and to embed the URL, you can set it to the *QR-Code*. If you are unsure which type to choose, [here](https://packagex.io/blog/barcode-types) is a guide to help.

4. Finally, you can provide the data/information into the **Barcode Value** property. You can also click **Set from Variable** to set it based on the value from the app state, your backend, or any other source.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the **Properties Panel**.

##### Changing size

To change the size of the barcode widget, select the **Barcode** widget, move to the properties panel, find the **Width** and **Height** property and enter the values.

##### Changing color

To change barcode colors, select the **Barcode** widget, move to the properties panel, and [change the colors](https://docs.flutterflow.io/resources/ui/widgets/widget-commonalities#change-color) for the following properties:

* **Foreground Color**: This sets the line or pattern color.
* **Background Color**: This sets the background color behind the line or pattern.

##### Show barcode text

You can also display the actual data below the barcode by enabling the **Show Text** property.

Note

This option is only available when using the *1D Barcode*.

#### Scan Barcode / QR code \[Action]

Using this Action, you open a barcode or QR code interface and scan a code using the device camera.

Follow the steps below to define a Scan Action to any widget.

1. Select **Actions** from the Properties panel (the right menu)
2. Click **+ Add Action** button
3. Choose a gesture from the dropdown among ***On Tap**, **On Double Tap**, or* **On Long Press**
4. Select the **Action Type** as ***Scan Barcode/QR code**.*
5. If you check the **Barcode Mode** checkbox then the UI will look like a barcode scanner. Otherwise, the UI will be like a QR code scanner.
6. **Cancel button text** would be ***Cancel*** by default, but you can specify any other text if you want.
7. In the **Output Variable Name** field, you can specify the name of the variable where the scanned text would be saved and then you can access it via the **Set from Variable menu > Action Outputs > \[Action Output Variable Name]**.

---

### Blur {#blur}

*Learn how to add Blur widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/blur

The Blur widget is used to blur its child or parent widget. You can use this widget to create the [Frosted glass](https://en.wikipedia.org/wiki/Frosted_glass) effect, typically seen in iOS.

#### Adding Blur widget

Here's an example of how you can add the Blur widget to your project:

1. First, drag the **Blur** widget from the **Base Elements** tab (in the Widget Panel) or add it directly from the widget tree.
2. Now, add the **Image** widget inside the **Blur** widget. Customize the Image as per your requirement.

#### Adding blur effect to the parent widget

By default, the Blur widget adds the blur effect on the child. For example, if you add the image widget as a child of the Blur widget, you will see the effect on the image. But sometimes, you might want to create the blur effect on the parent widget of the Blur widget.

> **Tip:** Adding a blur effect on the parent helps create the **Frosted Glass effect**.

![Frosted glass effect examples](https://docs.flutterflow.io/assets/images/frosted-glass-example-7270737045c7d3a75686b5d246c97fb6.png)

Here is how you can create the first example:

1. First, add the **Container** widget. Move to the properties panel, set its **width** to **Inifinity** and **height** to **200**. Also, set its **Background Image**.
2. Inside the Container, add the **Blur** widget.
3. Now, add the **Text** widget inside the blur widget and bring it to the center by changing its alignment.
4. Finally, select the **Blur** widget from the widget tree or the canvas area. Move to the properties panel, scroll down to the **Blur Properties** section, and **turn on** the **Backdrop** toggle. This toggle decides whether to add a blur effect on the parent or child widget. If enabled, it will blur the parent widget, while disabling it will cast the blur effect on its child.

Here are the steps to create the second example:

1. First, add the **Container** widget. Move to the properties panel, set its **width** to **Inifinity** and **height** to **200**. Also, set its **Background Image**.
2. Add the **Column** widget (inside the Container) and set its **Main Axis Alignment** to **end**.
3. Add the **Blur** widget (inside the Column).
4. Add the **Container** widget (inside the Blur) and set its **width** to **infinity** and **height** to **50**. Also, make the container's background around 40% transparent by selecting the **Fill Color** and bringing the second slider to the left.
5. Add the **Text** widget (inside the Container) and bring it to the center by changing its alignment.
6. Finally, select the **Blur** widget from the widget tree or the canvas area. Move to the properties panel, scroll down to the **Blur Properties** section and **turn on** the **Backdrop** toggle. This toggle decides whether to add a blur effect on the parent or child widget. If enabled, it will blur the parent widget, while disabling it will cast the blur effect on its child.

#### Customization

You can customize the behavior of this widget using the various properties available under the properties panel.

##### Changing blur strength

The blur strength is the blurriness added to the widget. This widget adds blur strength by utilizing the Sigma X and Sigma Y property. Sigma X sets the blur strength in the horizontal direction, while Sigma Y sets the blur strength in the vertical direction. The higher Sigma X and Y values increase the blurriness, whereas setting them to 0 completely removes the blurriness.

To change the blur strength:

1. Select the **Blur** widget from the widget tree or the canvas area.
2. Move to the properties panel (on the right side of your screen), and scroll down to the **Blur Properties** section.
3. Change the values in the **Sigma X** and **Sigma Y** input boxes.

##### Show or hide blur effect

To show or hide the blur effect:

1. Select the **Blur** widget from the widget tree or the canvas area.
2. Move to the properties panel (on the right side of your screen), and scroll down to the **Blur Properties** section.
3. **Check**/**Uncheck** the **Should Apply Blur** property to show/hide the blur effect. You can also set this value from a variable such as the App State variable, API response variable, or Firestore document by clicking on the **Set from Variable**.

---

### Calendar {#calendar}

*Learn how to add Calendar widget in your FlutterFlow project.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/calendar

The Calendar widget shows days in a month and a week. You can use the Calendar widget to filter the event list by date. For example, showing appointments on a specific date.

#### Adding Calendar to your project

To add the Calendar widget to your project:

1. Drag the **Calendar** widget from the **Base Elements** tab (in the Widget Panel) or add it directly from the widget tree.
2. On running the app, the calendar widget shows today's date by default. To set a different date, follow the instructions as below.
3. Move to the Properties Panel and scroll down to the **Calendar** section.
4. Find the **Initial Date** property, click **Unset,** and set the date from the variable (app state, API, etc.).

#### Show/save the selected date

When you select/change any date on the calendar, you can display it on the page or save it in a variable/Field (as Timestamp datatype) for later access.

Let's build an example of showing the selected date in a Text widget that looks like the one below:

The steps to show the selected date in the Text widget are as follows:

##### 1. Create an app state variable

Changing the date on the calendar widget emits the selected date in a variable called *calendarSelectedDay*. You can't use this value directly in the Text widget because the Text widget can only accept String values. Hence it would help if you created an app state variable that will store the *calendarSelectedDay* value and then display the selected date in a Text widget (using Date Format Options).

To create the app state variable, please find the instructions [here](https://docs.flutterflow.io/resources/data-representation/app-state#create-app-state-variable).

It should look something like this:

![app-state-variable-calendar.avif](https://docs.flutterflow.io/assets/images/app-state-variable-calendar-defc3da58615929db3ea58265d5d8e26.avif)

##### 2. Saving selected date in app state variable

To save the selected date in an app state variable, you can utilize the ***On Date Selected*** event and then add actions to update the app state variable:

Here are the steps in detail:

1. Select the **Calendar** widget from the widget tree or canvas area.

2. Select **Actions** from the Properties panel (the right menu), and click **Open**. This will open an **Action flow Editor** in a new popup window. 1. Click on the **+ Add Action**.

   2. On the right side, search and select the [**Update App State**](https://docs.flutterflow.io/resources/data-representation/app-state#update-app-state-action) action.

   3. Set the **Select field to update** to the App State variable **name**.

   4. Choose the **Select Update Type** to **Set Value**.

   5. Set the **Value Source** to **From Variable**.

   6. Set the **Source** to **Widget State**.

   7. Set the **Available Options** to the **calendarSelectedDay**.

   8. If there is a multiple date selection (date range selection), you can choose which date to pick up. You can choose to set the start or end date by setting the **Range Part** to **Start** or **End**. For a single date selection (which is by default), the start and end date would be the same.

##### 3. Showing date in Text widget from an app state variable

To show the selected date in the Text widget:

1. Select the **Text**, move to the properties panel, and click **Set from Variable**.
2. Select **Source** as **App State** and **Available Options** to the App State Variable **name**.
3. (Optional) Set the **Timestamp Format** to display the date in a specific format.
4. (Optional) Set the default value if you wish to.
5. Click **Confirm**.

#### Using a calendar to filter the list

You might need to use the calendar widget to filter the list of events (appointments, meetings, tickets, etc.). You can do so by applying the filter on the backend query and passing the selected date as a parameter.

Let's build an example that shows the Todos list (from the Firestore collection) based on date. Here's how it looks:

The steps to use the calendar to filter the list are as follows:

##### 1. Prepare data

Before you use the calendar to filter the list, you need to have a list of items with at least one field that holds the date. This date will be used to match against the date selected from the calendar. Skip if you already have data in such a format.

You can create a Firestore collection with a date field like the one below:

![calendar-prepare-data.avif](https://docs.flutterflow.io/assets/images/calendar-prepare-data-9d7b9823e8105bcf236c8ea82005ce28.avif)

##### 2. Building UI

Your UI must include at least two calendars and ListView widgets. Here's how you add it:

1. Add the **Calendar** widget. To provide a better user experience, you can switch to the week view.
2. Add the **ListView** and show the data from the Firestore collection.

##### 3. Apply date filter on backend query

Finally, you can add a filter on the existing backend query or a new one and provide the selected date from the calendar.

To apply filter by date:

1. Select **ListView** from the widget tree or the canvas area.
2. Click on the **Backend Query** tab (on the right side of your screen).
3. Query a collection. Skip if you have already done so.
4. Scroll down and click on the **+ Filter** button at the bottom
5. Find the **Field Name**, click on the Unset, and select the field on which you would like to apply the filter.
6. Find the **Relation** dropdown, click on the **Unset** and choose the relation as **Equal To**.
7. Set the **Value Source** to **From Variable**.
8. Set the **Source** to **Widget State**.
9. Set the **Available Options** to the **calendarSelectedDay**.
10. If there is a multiple date selection (date range selection), you can choose which date to pick up. You can choose to include the start or end date by setting the **Range Part** to **Start** or **End**. For a single date selection (by default), the start and end date would be the same.
11. Click **Confirm**.
12. After this, you can display the actual data in UI elements.

#### Customizing calendar

The Properties Panel can be used to customize the appearance and behavior of your widget.

##### Changing icon color

You can change the color of the icons displayed on the top right side of the calendar. to do that:

1. Select **Calendar** from the widget tree or the canvas area.
2. Move to the Properties panel and scroll down to the **Calendar** section.
3. Find the **Icon Colors** property, click on the box next to **Unset**, select the color, and then click **Use Color** or click on **Unset** and enter a Hex Code directly. You can also choose the color by clicking the Palette and Simple button.

##### Separate title and icons

By default, the calendar title (displaying the current month-year) and the icon for changing the month are positioned on the same row. If you wish to place them in separate rows, navigate to the **Properties Panel > Calendar >** and **enable the Two-row Header** option.

##### Changing row height

Changing the row height allows you to adjust the calendar height as per your design.

To change the row height:

1. Select **Calendar** from the widget tree or the canvas area.
2. Move to the Properties panel and scroll down to the **Calendar** section.
3. Find the **Row Height** property and enter the value.

---

### Card {#card}

*The Card widget is used to represent some related information in a box with rounded corners and a slight shadow for a 3D effect. For example, you can use a Card widget to show a Business card, restaurant information, movie details, etc.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/card

The [Card](https://api.flutter.dev/flutter/material/Card-class.html) widget is used to represent some related information in a box with rounded corners and a slight shadow for a 3D effect. For example, you can use a Card widget to show a Business card, restaurant information, movie details, etc.

The Card widget is often used with a List to display the item information for a specific record.

![img.png](https://docs.flutterflow.io/assets/images/img-fe542d54ca6413fb02dc2ef49a03ef09.png)

#### Adding Card Widget

Here's an example of how you can use a Card widget in your project:

1. Open the [Widget Palette](https://docs.flutterflow.io/flutterflow-ui/widget-palette) and locate the **Card** widget under the **Layout Elements** tab. You can drag it into your desired location or add it directly from the widget tree or canvas area.
2. Start with adding a `Row` or `Column` widget inside the Card and build the UI as per your requirements.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the Properties Panel.

##### Styling the Card

Styling helps you customize a widget that matches your design. The Card widget allows you to customize the background color, elevation, and rounded corners.

Here's how you stylize the Card widget:

1. Select the **Card** widget and move to the **Properties Panel > Card Properties**.
2. To change the background color, [modify the Color](https://docs.flutterflow.io/resources/ui/widgets/widget-commonalities#change-color) property.
3. To change the elevation (depth or Z-axis), enter the value in the **Elevation** property.
4. To create the rounded border, use the **Border Radius** property. For uniform curvature on all sides, use the **Uniform Radius** option by sliding the adjustment bar or inputting your preferred value directly.

---

### Carousel {#carousel}

*Learn how to add Carousel widget in your FlutterFlow project.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/carousel

The Carousel widget, often called an image slider, is a popular design element used to display a series of images or content in a horizontal or sometimes vertical format. The primary purpose of a carousel slider is to showcase multiple pieces of information, such as images, product features, news articles, or testimonials, within limited screen space.

#### Adding Carousel widget

To add the Carousel widget to your app:

1. Add the **Carousel** widget from the **Layout Elements** tab.
2. By default, it adds four slides and shows the first one in the canvas. In the widget tree, it is represented as **Carousel Page**. To see another slide in the canvas, move to the **Properties Panel >** set the **Active Page** to the slide you want to see.
3. To add a new slide, move to the **Properties Panel > Active Page >** click **+ Add Page**.
4. To delete any slide, select the **Carousel Page** from the widget tree or the canvas area and press the **Delete** key on the keyboard.
5. By default, Carousel Page contains an Image widget; however, you can customize it as per your requirements.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

##### Changing the scroll direction

By default, the Carousel comes with a horizontal scroll for the slides. To change the scroll direction to vertical, move to the **Properties Panel > Carousel Properties >** set the **Axis** to **Vertical**.

##### Trigger action on slide chang

You might want to trigger an action when the slide is swiped. For example, If your carousel has an auto-play feature, you can listen for slide change events to pause or resume auto-play. You could also have a custom indicator below the Carousel and have it synchronize with the current slide to provide users with clear feedback about their position within the carousel.

To trigger action on page or slide change:

1. Select the widget from the widget tree or canvas area.
2. Select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.
3. You will notice that the **Type of Action** (aka callback) is already set to **On Page Change**. That means actions added under this will be called whenever the slide is swiped.
4. Now you can add any action here.

Here is an example showing the snackbar message whenever the slide is swiped.

##### Setting initial page index

You might want to display a specific slide as soon as it is loaded. To do so, move to the **Properties Panel > Carousel Properties >** enter the **Initial Page Index** value. Please **note** that the slide index starts from 0. So, if you want to set slide 1, you should enter 0. If you want to set slide 2, you should enter 1, and so on.

![set-initial-index](https://docs.flutterflow.io/assets/images/set-initial-index-f1c89cccdedfe9ca381f411e549502f5.png)

##### Loop carousel contents

By default, the content of the carousel loops continuously. To stop this behavior, move to the **properties panel > Carousel Properties >** disable **Loop carousel contents**.

##### Wrap items in a center widget

If you want all items in a center position, move to the **properties panel > Carousel Properties >** enable **Wrap items in Center Widget**.

![wrap-items-in-center-widget](https://docs.flutterflow.io/assets/images/wrap-items-in-center-widget-c49c2c41d38f8fde5e18b1922ffe9c11.png)

##### Changing Viewport and Shrink factor

You can use the **Viewport Fraction** to change the size of a single item, i.e., the item in the center. The **Shrink Factor** lets you adjust the size of other items, i.e., items that are not in focus. Both the properties accept the value between 0 and 1. where 1 is full size, and 0.5 is half of the actual size.

##### Enabling autoplay

When autoplay is enabled, the carousel will automatically transition from one slide to the next at regular intervals, determined by the following options:

* **Duration**: The amount of time (in milliseconds) that it takes to transition from the current slide to the next.
* **Delay**: The amount of time (in milliseconds) that the item remains in the center before moving to the next one.

##### Change slide on button press

You might want to allow users to change the slide on button press (e.g., next, previous, and skip buttons) in addition to the swipe. You can do so by adding the **Control Carousel** action on the Tap of a Button widget.

Here's how you do it:

1. First, [add the Carousel](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/carousel#adding-carousel-widget) widget.
2. Add buttons to go to the previous and next pages.
3. Now select any button and define the [Control Carousel](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/carousel#control-carousel-action) action.

***

#### Control Carousel \[Action]

By using this action, you can gain more control over the scrolling behavior of the Carousel widget. For instance, you can enable your users to move to the next or previous slide with a single tap of a button.

##### Types of action

These are the types of actions you can add on the Carousel widget.

* **Previous**: Scroll to the previous slide.
* **Next**: Scroll to the next slide.
* **First**: Scroll to the first slide.
* **Last**: Scroll to the last slide.
* **Jump to**: Scroll to a specific slide in the Carousel widget. Please note that the slide index starts from 0. So, if you want to jump to slide 1, you should enter 0. If you want to jump to slide 2, you should enter 1, and so on.

---

### Bar Chart {#bar-chart}

*Learn how to add Bar Chart widget in your FlutterFlow project.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/bar-chart

The Bar Chart shows the rectangular bars on a graph whose height varies as per its numeric value and has equal width. This can be used to display categorical information.

For example, you could use the Bar chart to display each year's income and expense value together.

#### Adding bar chart

Adding a chart comprises of following steps:

1. [Preparing data](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/bar-chart#1-preparing-data)
2. [Adding bar chart widget](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/bar-chart#2-adding-bar-chart-widget)

##### 1. Preparing data

Before adding the chart widget, you need to prepare the data in the format that the chart widget accepts. The bar chart widget requires label values (runs horizontally from left to right) and Y coordinate values (runs vertically from bottom to top). Together these values (labels and Y coordinate) are used to draw bars on a chart. You can store and retrieve these values in the following ways:

1. [Firestore Documents](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/bar-chart#11-firestore-documents)
2. [Numbers Lists](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/bar-chart#12-numbers-lists)

###### 1.1 Firestore Documents

If you use Firebase as the backend, you can create a collection and add the list of documents. Each document entry can be used to draw bars on the chart. Hence you must add at least two fields (one with DataType String and another with DataType Double) in a document that will act as the labels, and the Y coordinates value to draw a bar.

The figure below illustrates the sample collection that draws the two bars (income and expense) for each year.

![bar-collection-to-document.avif](https://docs.flutterflow.io/assets/images/bar-collection-to-document-d00625c51027b8e8a06a6edb1023390f.avif)

> **Warning:** The above collection schema is used for simplification. You are free to have your own schema that works best for you.

Here's how the data is used to draw bars on a chart:

![firestore-data.avif](https://docs.flutterflow.io/assets/images/firestore-data-d5adcaee1b95538e3c6a04aa5c2523e6.avif)

###### 1.2 Numbers Lists

The bar chart widget can draw a bar using a list of labels and numbers. You need at least two separate lists with DataType String and Double. One list stores a list of labels to be displayed on the X-axis, whereas the other stores a list of values on the Y-axis. The chart widget uses both variables to draw the bar.

> **Info:** The variable can be an app state variable or the action output variable of an API call.

The figure below illustrates the sample app state variables that draw the two bars (income and expense) for each year.

![app-state-variable.avif](https://docs.flutterflow.io/assets/images/app-state-variable-c1ba443e4de61ab35664680f5bd7900b.avif)

> **Warning:** A number of values in the Y-axis variable should match the number of labels in the X-axis variable.

Here's how the number list is used to draw bars on a chart:

![app-state-variable-2.avif](https://docs.flutterflow.io/assets/images/app-state-variable-2-4d34ce331379057fe557b186e42b310d.avif)

To create the app state variable, please find the instructions [here](https://docs.flutterflow.io/resources/data-representation/app-state#create-app-state-variable).

##### 2. Adding bar chart widget

To add the bar chart widget to your project:

1. Drag the **Chart** widget from the **Base Elements** tab (in the Widget Panel) or add it directly from the widget tree.

2. Move to the property panel and set the **Chart Type** to **Bar**.

3. For the Bar Chart, a single **Chart Data** is a **Bar** drawn on the chart. The bar is drawn by providing the data to this. To show the first bar, open the **Chart Data 1** section, and set the **Data Source** to [Firestore Documents](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/bar-chart#11-firestore-documents) or [Numbers List](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/bar-chart#12-numbers-lists).

4. If you select **Firestore Documents**: 1. Make sure you have access to a list of documents. The list of documents can be retrieved by querying a collection at any top-level widget, such as the **Page** or **Column** widget. You can also query a collection on the Chart widget itself. To query collection on a page: 1. Select the **page** and then click on the **Backend Query** tab (on the right side of your screen).
      2. Set the **Query Type** to **Query Collection**.
      3. Scroll down to find the **Collection** dropdown and set it to your collection.
      4. Set the **Query Type** to **List of Documents**.
      5. To order the labels, you can perform Ordering on a query.
      6. Click **Save**.

   2. Set the Source to the **collection\_name Documents > Documents (List/)** and click **Confirm** (e.g. *transactions Documents > Documents (List/)*).

   3. Set the **Bar Labels Field,** whose values will be used as labels, and lay out horizontally from left to right (e.g., day, week, month, year).

   4. Set the **Bar Values Field,** whose values will be used to draw bars on a chart. This will draw bars for the first chart data (e.g., income data).

5. If you select **Numbers Lists**: 1. Under the **Bar Labels**, click on the **UNSET** and set it to a variable whose values will be used as labels and lay out horizontally from left to right (e.g., day, week, month, year).
   2. Further options are displayed as per the selected source. For example, if you choose **App State**, The **Available Option** field is displayed that allows you to select the actual variable.
   3. Under the **Bar Values**, click on the **UNSET** and set it to a variable whose values will be used to draw bars on a chart. This will draw bars for the first chart data (e.g., income data).

6. Click **Add Data** to show bars for multiple categories (e.g., income and expense). The bars for each new category are displayed next to the previous one. **Note**: When you click **Add Data**, you can only set **Bar Values Field** since the **Bar Labels Field** is already provided in the first **Chart Data**.

7. Scroll down to the **Chart Properties** section and adjust the **Width** and **Height** properties.

* Using Firestore Documents
* Using Numbers Lists

#### Customizing bars

You can customize the look and feel of bars to match your design.

##### Customize bar for an individual chart data

You can customize the bar for each specific chart data to help users easily identify the information.

To customize the bar for each chart data:

1. Select the **Chart** widget from the widget tree or the canvas area.
2. Move to the properties panel, and open the **Chart Data** > **Bar Properties**.
3. To change the **Bar Color**, click on the box next to the already selected color, select any dark/light color, and then click **Use Color** or click on an already selected color and enter a Hex Code directly.
4. To add a border around the bar, enter the **Border Width** value and change its **Border Color**.

##### Customize all bars

To customize all bars together:

1. To change the bar width, scroll down the **Bar Styling properties > Bar Width** and enter the value.
2. To add space between two bars or two bars category (if you have multiple chart data), enter the value in the **Group Spacing** property.
3. If you have multiple chart data and want to add space between two adjacent bars, you can enter a value in the **Bar Spacing** property.
4. To combine multiple chart data and display it as a single bar, enable the **Stack Bars**.
5. To change how the bars should be distributed horizontal direction, choose from the **Main Axis Alignment** options.

#### Customizing chart

You can [customize the chart](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/chart#customizing-chart) to match your design by changing the background color, setting axis bounds, showing grids, displaying borders, and more.

---

### Chart {#chart}

*Learn how to add Chart widget in your FlutterFlow project.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/chart

The chart widget is used to represent the information in a graphical format. You can use it to display complex information in an easily understandable format.

#### Types of chart

You can add the following types of charts:

1. [Line Chart](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/line-chart)
2. [Bar Chart](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/bar-chart)
3. [Pie Chart](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/pie-chart)

#### Customizing chart

Using *Chart* Properties (inside the properties panel), you can customize the appearance and behavior of the widget.

> **Info:** The following instructions will have a similar effect on the Bar chart.

##### Showing legend

Legend helps users identify the data drawn over the chart. It's a small box that shows the chart data name/text next to its color (a color used to draw a line or bar).

![legend.webp](https://docs.flutterflow.io/assets/images/legend-21e11cdd278ca1c7777961e548dfebcc.webp)

To show legend:

1. Select the **Chart** widget from the widget tree or the canvas area.
2. Move to the properties panel and open **Chart Data 1**.
3. Enter the **Legend** name. This will be displayed as the name of the line or bar.
4. If you have multiple chart data (e.g., Chart Data 1, Chart Data 2, and so on), set the legend for them as well.
5. Scroll down to **Chart Properties** and enable the **Show Legend** property.

##### Customizing legend box

You can change the appearance of the legend box by following the instructions below:

1. First, [enable the legend](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/chart#showing-legend).
2. Scroll down to the **Legend Properties** section.
3. To change the dimension of the legend box, enter the **Width** and **Height** values.
4. The legend box typically appears over the chart on the bottom right side. To change its position, use the **Horizontal** and **Vertical** **Alignment** slider.
5. To change the background color, find the **Background Color** property and click on the box next to **Unset**, select the color, then click **Use Color** or click on **Unset** and enter a Hex Code directly.
6. To customize the border, use the **Border Color**, **Border Width,** and **Border Radius**.
7. To add space between legend text and its box border, adjust **Padding** property.

##### Customizing legend text and indicator

To customize the legend text and indicator:

1. First, [enable the legend](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/chart#showing-legend).
2. To style the legend text, scroll down to the **Legend Properties** > **Legend Text Properties** and change the style as per [here](https://docs.flutterflow.io/resources/ui/widgets/text#common-text-styling-properties).
3. To add space between the indicator and the text, adjust the **Text Padding** property.
4. You can change the indicator size by entering a value inside the **Indicator Size** property.
5. To create rounded corners around the indicator, you can use the **Indicator Border Radius** property.

##### Changing background color

The default background color for the chart widget is white. To change the background color:

1. Select the **Chart** widget from the widget tree or the canvas area.
2. Move to the properties panel, and scroll down to the **Chart Properties** section.
3. Find the **Background Color** property, click on the box next to **Unset**, select any dark/light color, and then click **Use Color** or click on **Unset** and enter a Hex Code directly. You can also choose the color by clicking on the Palette and Simple buttons.

##### Set axis bounds

Axis Bounds specify limits on the axis. You can set the minimum and maximum limits on the X and Y axes.

You can set four types of bounds on a chart:

1. **Min X** (only applicable in Line Chart): Specifies a number at which the X-axis should start.
2. **Min Y**: Specifies a number at which the Y-axis should start.
3. **Max X** (only applicable in Line Chart): Specifies a number at which the X-axis should end.
4. **Max Y**: Specifies a number at which the Y-axis should end.

> **Info:** If you don't specify the axis bounds, the start and end numbers for the X and Y axis are set as per the min and max of the actual data.

To set the axis bounds:

1. Select the **Chart** widget from the widget tree or the canvas area.
2. Move to the properties panel, and scroll down to the **Chart Properties** section.
3. Find the **Axis Bounds** section and enter the **Min X**, **Min Y**, **Max X**, and **Max Y** values.

* Chart without axis bounds
* Chart with axis bounds

![chart-without-axis-bound.png](https://docs.flutterflow.io/assets/images/chart-without-axis-bound-8d6081e86da1e26e8adac134dfea2a4a.png)

The line chart with bounds set to **Min X:0 ,Min Y:0, Max X:7 and Max Y:100** looks like this:

![chart-with-axis-bound.avif](https://docs.flutterflow.io/assets/images/chart-with-axis-bound-fa38946dc2d501e275ed529634a91f12.avif)

##### Showing grid

To display the grid on the chart background:

1. Select the **Chart** widget from the widget tree or the canvas area.
2. Move to the properties panel, and scroll down to the **Chart Properties** section.
3. Find the **Show Grid** toggle and **enable** it.

##### Showing border

To display a border around the chart:

1. Select the **Chart** widget from the widget tree or the canvas area.
2. Move to the properties panel, and scroll down to the **Chart Properties** section.
3. Find the **Show Border** toggle and **enable** it.
4. Find the **Border Color** property, click on the box next to **Black**, select the color, and then click **Use Color** or click on **Black** and enter a Hex Code directly.
5. Now, find the **Border Width** property below and enter the value. (e.g. 2,5,10)

##### Showing tooltip

Sometimes it becomes difficult to identify the exact Y value. To overcome this, you can enable the tooltip. Enabling the tooltip will display the Y value when you interact with the chart. You can also add background color to the tooltip.

To enable tooltip:

1. Select the **Chart** widget from the widget tree or the canvas area.
2. Move to the properties panel, and scroll down to the **Chart Properties** section.
3. Find the **Show Border** toggle and **enable** it.
4. To change the background color, find the **Tooltip Background Color** property, click on the box next to **Unset**, select any dark/light color, and then click **Use Color** or click on **Unset** and enter a Hex Code directly.

##### Customizing X axis (Show name, number, and labels)

You can customize the X axis to display names and numbers on it.

##### Displaying name on X-Axis

To show the name on the axis, such as day, week, and month:

1. Select the **Chart** widget from the widget tree or the canvas area.
2. Move to the properties panel, and scroll down to the **Chart Properties** section.
3. Scroll down to the **X Axis Properties** and enter the value in the **Text** input box. You can also set the name from a variable by clicking on the **Set from Variable text**.
4. You can also customize the appearance of the name text.

##### Displaying numbers or labels on the X axis

Displaying numbers or labels on the axis helps you quickly understand the graph.

**For Line Chart**

If you have set the [Axis bounds](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/chart#set-axis-bounds), the start and end numbers are displayed as per the value set in **Min X** and **Max X**. Otherwise, they are shown as per the min and max values of the actual data. You can also specify the intervals between the numbers.

To display numbers on the X-axis:

1. Select the **Chart** widget, head over to the properties panel, and scroll down to the **Chart Properties** section.
2. Scroll down to the **X Axis Properties** and enable the **Show Label** option.
3. When it comes to displaying numbers, it's usually acceptable to show up to two digits as is. However, if the number exceeds that limit, it's recommended to set the **Label Format Type** to **Number** and configure the appropriate **Number Format Options**.
4. Enter the value in the **Label Interval** input box.
5. You can also customize the appearance of the numbers.

* Displaying numbers on the X axis
* Displaying numbers (with formatting) on the X axis

> **Info:** For the bar chart, you can only display labels on X-axis.

##### Customizing Y axis (Show name and numbers)

You can customize the Y axis to display names and numbers on it.

##### Displaying name on Y-axis

To show the name on the axis, such as progress, number of users, and sales:

1. Select the **Chart** widget from the widget tree or the canvas area.
2. Move to the properties panel, and scroll down to the **Chart Properties** section.
3. Scroll down to the **Y-Axis Properties** and enter the value in the **Text** input box. You can also set the name from a variable by clicking on the **Set from Variable text**.
4. You can also customize the appearance of the name text.

##### Displaying numbers on the Y axis

Just like X-axis, If you have set the [Axis bounds](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/chart#set-axis-bounds), the start and end numbers are displayed as per the value set in **Min Y** and **Max Y**. Otherwise, they are shown as per the min and max value of the actual data. You can also specify the intervals between the numbers.

To display numbers on the Y axis:

1. Select the **Chart** widget, head over to the properties panel, and scroll down to the **Chart Properties** section.
2. Scroll down to the **Y Axis Properties** and enable the **Show Label** option.
3. When it comes to displaying numbers, it's usually acceptable to show up to two digits as is. However, if the number exceeds that limit, it's recommended to set the **Label Format Type** to **Number** and configure the appropriate **Number Format Options**.
4. Enter the value in the **Label Interval** input box.
5. You can also customize the appearance of the numbers.

* Displaying numbers on the Y axis
* Displaying numbers (with formatting) on the Y axis

---

### Line Chart {#line-chart}

*Learn how to add Line Chart widget in your FlutterFlow project.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/line-chart

The Line Chart connects the data points on a graph with a line. This is typically used to display information that evolves over time.

For example, you could use this widget to show progress over some time. This will plot the progress value on a chart that becomes easily digestible for the users instead of just showing numbers in a tabular format.

#### Adding line chart

Adding a chart comprises of following steps:

1. [Preparing Data](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/line-chart#1-preparing-data)
2. [Adding Chart widget](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/line-chart#2-adding-chart-widget)

##### 1. Preparing Data

Before adding the chart widget, you need to prepare the data in the format that the chart widget accepts. The line chart widget requires an X coordinate (runs horizontally from left to right) and a Y coordinate (runs vertically from bottom to top) value. Together these values (x,y) are used to mark a point in the chart. You can store and retrieve these values in the following ways:

1. [Firestore Documents](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/line-chart#11-firestore-documents)
2. [Numbers Lists](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/line-chart#12-numbers-lists)

###### 1.1 Firestore Documents

If you use Firebase as the backend, you can create a collection and add the list of documents. Each document entry is used to plot a single point on the chart. Hence you must add at least two fields (with DataType Integer or Double) in a document that acts as the X and Y coordinates to plot the point.

The figure below illustrates the sample collection that will draw a single line on the chart:

![collection-to-document.avif](https://docs.flutterflow.io/assets/images/collection-to-document-48ad2e91983c8635ce6a1a030f46df6a.avif)

> **Warning:** The above collection schema is used for simplification. You are free to have your own schema that works best for you.

Here's how the data is used to mark a point in a chart:

![firestore-data-to-chart.avif](https://docs.flutterflow.io/assets/images/firestore-data-to-chart-07e36e7338130cd653b6eed0628b42e5.avif)

###### 1.2 Numbers Lists

The chart widget can plot a point using a list of numbers. You must create at least two separate lists with DataType Integer or Double. One list stores all X-axis values, whereas the other stores a list of all Y-axis values. The chart widget uses both variables to create pair of (x,y), which are then used to mark a point in the chart.

> **Info:** The variable can be an app state variable or the action output variable of an API call.

> **Warning:** You must have at least two variables to draw a single line.

The figure below illustrates what the app state variables should look like:

![app-state-variables.avif](https://docs.flutterflow.io/assets/images/app-state-variables-d36db8be8677f9c3e9700215bbd341d2.avif)

Here's how the number list is used to mark a point in a chart:

![numbers-to-chart.avif](https://docs.flutterflow.io/assets/images/numbers-to-chart-15ec524e67beb7f6c6393230d8f4cc04.avif)

To create the app state variable, please find the instructions [here](https://docs.flutterflow.io/resources/data-representation/app-state#create-app-state-variable).

##### 2. Adding Chart widget

To add the chart widget to your project:

1. Drag the **Chart** widget from the **Base Elements** tab (in the Widget Panel) or add it directly from the widget tree. **Note**: The Line Chart is the default chart type.

2. Move to the property panel and scroll down to the **Chart Data** section.

3. For the Line Chart, **Chart Data** is a **line** drawn on the chart. The line is drawn by providing data to this. To show the first line, open the **Chart Data 1** section, and set the **Data Source** to [Firestore Documents](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/line-chart#11-firestore-documents) or [Number List](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/line-chart#12-numbers-lists).

4. If you select **Firestore Documents**: 1. Make sure you have access to a list of documents. The list of documents can be retrieved by querying a collection at any top-level widget, such as **Page** or **Column** widget. You can also query a collection on the Chart widget itself. To query collection on a page: 1. Select the **page** and then click on the **Backend Query** tab (on the right side of your screen).
      2. Set the **Query Type** to **Query Collection**.
      3. Scroll down to find the **Collection** dropdown and set it to your collection.
      4. Set the **Query Type** to **List of Documents**.
      5. Click **Save**.

   2. Set the Source to the **collection\_name Documents > Documents (List\<collection\_name>)** and click **Confirm** (e.g. *progress Documents > Documents (List\<progress>)*).

   3. Set the **X Value Field,** whose values will lay out horizontally from left to right (e.g., day, week, month).

   4. Set the **Y Value Field,** whose values will lay out vertically from bottom to top (e.g., progress, number of users, sales).

5. If you select **Numbers Lists**: * Under the **X Data**, click on the **UNSET** and set it to a variable whose values will lay horizontally from left to right (e.g., day, week, month).
   * Further options are displayed as per the selected Source. For example, if you choose **App State**, The **Available Option** field is displayed that allows you to select the actual variable.
   * Under the **Y Data**, click on the **UNSET** and set it to a variable whose values will lay out vertically from bottom to top (e.g., progress, number of users, sales).

6. Click **Add Data** to show multiple lines on a chart. Each new line is stacked on top of the previous line.

7. Scroll down to the **Chart Properties** section and adjust the **Width** and **Height** properties.

* Using Firestore Documents
* Using Numbers Lists

#### Customizing line

You can customize the look and feel of each line drawn on a chart widget to match your design. The Line Properties (inside the Chart Data) section is used the customize the line.

To customize the line:

1. Select the **Chart** widget from the widget tree or the canvas area.
2. Move to the properties panel, open the **Chart Data** section and then open the **Line Properties** section.
3. To change the **Line Color**, click on the box next to the already selected color, select any dark/light color, and then click **Use Color** or click on an already selected color and enter a Hex Code directly.
4. To change the thickness of the line, change the value in the **Line Thickness** input box.
5. By default, all the data points are connected with a smooth curve line; to disable this, simply **turn off** the **Curved Lines** property. This will draw a straight line between two points. 1. If you keep this property enabled, you may notice that for some data points the curve goes beyond/above the actual value. To prevent this, you can **enable** the **Prevent curve from overshooting**.
6. To see the point at the exact location on the chart, you can turn on the **Show Dots** property.
7. To fill the area below the line with a custom color, turn on the **Fill Below Line** property and set the **Fill Color** by clicking on the box next to **Unset**, select any dark/light color, and then click **Use Color** or click on **Unset** and enter a Hex Code directly.

#### Customizing chart

You can [customize the chart](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/chart#customizing-chart) to match your design such as changing the background color, setting axis bounds, show grids, displaying borders, and more.

---

### Pie Chart {#pie-chart}

*Learn how to add Pie Chart widget in your FlutterFlow project.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/pie-chart

The Pie Chart divides the circle (aka Donut) into slices/sections representing different categories. Each section shows the size of the data. It is typically used to display how a total amount is distributed between sections.

For example, you could use the Pie Chart to show which animal dominates the pet world.

#### Adding pie chart

Adding a pie chart comprises of the following steps:

1. [Preparing data](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/pie-chart#1-preparing-data)
2. [Adding pie chart widget](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/pie-chart#2-adding-pie-chart-widget)

##### 1. Preparing data

Before adding the chart widget, you need to prepare the data in the format that the chart widget accepts. The pie chart widget requires labels and section values. Together these values are used to draw slices on a chart. You can store and retrieve these values in the following ways:

1. [Firestore Documents](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/pie-chart#11-firestore-documents)
2. [Numbers Lists](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/pie-chart#12-numbers-lists)
3. [Single Value](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/pie-chart#13-single-value)

###### 1.1 Firestore Documents

If you use Firebase as the backend, you can create a collection and add the list of documents. Each document entry can be used to draw sections on the chart. Hence you must add at least two fields (one with DataType String and another with DataType Integer or Double) in a document. The field with String DataType will be used as labels, whereas the field with Integer or Double DataType will be used as section values.

The figure below illustrates the sample collection that draws three sections on the pie chart.

![pie-collection-document.avif](https://docs.flutterflow.io/assets/images/pie-collection-document-b527fe46d6e4adfee4e144c96206def9.avif)

> **Warning:** The above collection schema is used for simplification. You are free to have your own schema that works best for you.

Here's how the data is used to draw sections on a pie chart:

![pie-firestored-data.avif](https://docs.flutterflow.io/assets/images/pie-firestored-data-77f4b01376f3946949fa7cef7c716f72.avif)

###### 1.2 Numbers Lists

The pie chart widget can draw sections using a list of labels and numbers. You need at least two different lists with DataType String and Integer or Double. One list stores a list of labels, whereas the other stores a list of section values.

> **Info:** The variable can be an app state variable or the action output variable of an API call.

The figure below illustrates the sample app state variables that draw three sections on the pie chart.

![pie-app-state-variable.avif](https://docs.flutterflow.io/assets/images/pie-app-state-variable-f8fbd7bb5de5988c355a569ab20d847a.avif)

> **Warning:** The number of section values should match the number of labels.

Here's how the number list is used to draw sections on a chart:

![pie-app-state-variable-2.avif](https://docs.flutterflow.io/assets/images/pie-app-state-variable-2-4f157cb01320088e4cbf59af5127cc6b.avif)

To create the app state variable, please find the instructions [here](https://docs.flutterflow.io/resources/data-representation/app-state#create-app-state-variable).

###### 1.3 Single Value

When you have a fixed number of labels (aka static labels, which won't change over time), you can use this option. This option allows you to define labels and their section value from a variable.

> **Info:** The variable can be an app state variable or the action output variable of an API call.

Here's how the three separate app state variables are used to draw sections on a chart:

![pie-single-value.avif](https://docs.flutterflow.io/assets/images/pie-single-value-5319c32f46c024aa5dd2b764fc502a5c.avif)

##### 2. Adding pie chart widget

To add the pie chart widget to your project:

1. Drag the **Chart** widget from the **Base Elements** tab (in the Widget Panel) or add it directly from the widget tree.

2. Move to the property panel and set the **Chart Type** to **Pie**.

3. For the Pie Chart, a single **Chart Data** is a **Section** drawn on the chart. The section is drawn by providing the data to this. Open the **Chart Data 1** section, and set the **Data Source** among the [Firestore Documents](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/pie-chart#11-firestore-documents), [Numbers List](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/pie-chart#12-numbers-lists), and [Single Value](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/pie-chart#13-single-value).

4. If you select **Firestore Documents**: 1. Make sure you have access to a list of documents. The list of documents can be retrieved by querying a collection at any top-level widget, such as the **Page** or **Column** widget. You can also query a collection on the Chart widget itself. To query collection on a page: 1. Select the **page** and then click on the **Backend Query** tab (on the right side of your screen).
      2. Set the **Query Type** to **Query Collection**.
      3. Scroll down to find the **Collection** dropdown and set it to your collection.
      4. Set the **Query Type** to **List of Documents**.
      5. Click **Save**.

   2. Under the **Data**, click on the **UNSET** and set the source to the **collection\_name Documents > Documents (List/)** and click **Confirm** (e.g., *pets Documents > Documents (List/)*).

   3. Set the **Legend Labels Field,** whose values will be used as labels.

   4. Set the **Section Values Field,** whose values will be used to draw sections on a chart.

   5. To set the section color, scroll down to **Pie Chart Properties > Pie Chart Color** and click on **Add Color**. **Note**: Make sure the number of colors you have must be equal to or greater than the number of labels. Otherwise, all sections would have the same colors.

5. If you select **Numbers Lists**: 1. Under the **Legend Labels**, click on the **UNSET** and set it to a variable whose values will be used as labels.
   2. Further options are displayed as per the selected source. For example, if you choose **App State**, The **Available Option** field is displayed allowing you to select the actual variable.
   3. Under **Section Values**, click on the **UNSET** and set it to a variable whose values will be used to draw sections on a chart.
   4. To set the section color, scroll down to **Pie Chart Properties > Pie Chart Color** and click on **Add Color**. **Note**: Make sure the number of colors you have must be equal to or greater than the number of labels. Otherwise, all sections would have the same colors.

6. If you select **Single Value**: 1. Under **Section Value**, click on the **UNSET** and set it to a variable whose value will be used to draw the first section.
   2. Further options are displayed as per the selected source. For example, if you choose **App State**, The **Available Option** field is displayed allowing you to select the actual variable.
   3. Click **Add Data** to show multiple sections (e.g., Dogs, Cats, Birds). **Note**: This option is only available when using Single Value.

7. Scroll down to the **Chart Properties** section and adjust the **Width** and **Height** properties.

* Using Firestore Documents
* Using Numbers Lists
* Using Single Value

#### Customizing section

You can customize the look and feel of each section to match your design by following the instructions below:

1. Select the **Chart** widget from the widget tree or the canvas area.
2. Move to the properties panel, and open the **Chart Data** > **Pie Chart Properties**.
3. To change the size of the circle, enter the value in the **Pie Chart Radius** property.
4. To add a border around the section, enter the **Border Width** value and change its **Border Color**.
5. To create an inner circle (hole) inside the main circle(Donut), enter the size into the **Donut Hole Radius** property. 1. To change the **Donus Hole Color**, click on the box next to the already selected color, select any dark/light color, and then click **Use Color** or click on an already selected color enter a Hex Code directly.
6. To display the section value or its percentage, set the **Section Lable Type** to **Value** or **Percent** respectively.

#### Showing legend

Legend helps users identify the data drawn over the chart. It's a small box that shows the chart data name/text (label) next to its color (a color used to draw a section).

To show and customize the legend follow the instructions [here](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/chart#customizing-chart).

---

### CountController {#countcontroller}

*Learn how to add CountController in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/count-controller

The CountController widget is used to increment and decrement the count or number.

You could use the CountController widget to set the quantity of any product when buying in an e-commerce app.

Widget State

Before diving into form widgets, check out our guide on [**Widget States**](https://docs.flutterflow.io/concepts/state-management/widget-state) to efficiently manage the state and behavior of your form elements.

#### Adding CountController to your project

Here's an example of how you can use a CountController widget in your project:

1. First, drag the **CountController** widget from the **Form Elements** tab (in the Widget Panel) or add it directly from the widget tree.
2. Move to the properties panel (in the right) and scroll down to the **Count Controller Properties**.
3. The number on CountController appears as soon as it is loaded, called the Initial Count, 0 by default. To change this initial count, enter the value in the **Initial Count** input box. You can also set this value dynamically by having it **Set from Variable**. This can be used to display the default quantity of a product in an E-commerce app.
4. The Step Size property sets the value by which the count should be increased or decreased. The default value is 1. To change this, enter the value in the **Step Size** input box.
5. To allow users to set the valid count or quantity, you can limit the CountController range (min and max count) by specifying the value in the **Minimum** and **Maximum** input boxes.

#### Trigger action on count change

Let's see how to trigger an action when the count changes on this widget. This is helpful when you want to update the latest count in your backend (make API call, create/update Firestore document) as the count changes.

To do so:

1. Select **CountController**, select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.
2. You will notice that the **Type of Action** (aka callback) is already set to **On Count Changed**. That means actions added under this will be called whenever the count changes.
3. Now you can add any action here.

Here is an example of updating the count in an [app state variable](https://docs.flutterflow.io/resources/data-representation/app-state).

#### Customizing CountController

The Properties Panel can be used to customize the appearance and behavior of your widget.

##### Customizing icon

To customize the decrement icon:

1. Select the **CountController** widget from the widget tree or the canvas area.
2. Move to the properties panel, and find the **Style Properties** section.
3. To change the icon, click on the already selected icon and then search and select the new icon.
4. To change the icon size, enter the value in the **Icon Size** property.
5. To change the icon color, find the **Icon Color** property, click on the box next to the selected color, select the color, and click **Use Color** or click on **Unset** and enter a Hex Code directly.

---

### CreditCardForm {#creditcardform}

*Learn how to add CreditCardForm in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/credit-card-form

The CreditCardForm widget allows users to enter their credit card details such as card number, expiry date, and CVV.

Widget State

Before diving into form widgets, check out our guide on [**Widget States**](https://docs.flutterflow.io/concepts/state-management/widget-state) to efficiently manage the state and behavior of your form elements.

#### Adding CreditCardForm widget

Here's an example of how you can add the CreditCardForm widget to your project:

1. First, drag the **CreditCardForm** widget from the **Form Elements** tab (in the Widget Panel) or add it directly from the widget tree.
2. When you type in, the card number gets obscured (number becomes •, i.e., dot). To disable this feature and allows users to see the full number, move to the properties panel, find the **Obscure Card Number** toggle and turn it off.

#### Customizing

You can customize the behavior and appearance of this widget using the various properties available under the properties panel.

##### Obscuring CVV

By default, the CVV number is visible when you type in. It's essential that you obscure (number becomes •, i.e. dot) it.

To obscure the CVV:

1. Select the **CreditCardForm** widget from the widget tree or the canvas area.
2. Move to the properties panel, find the **Obscure CVV** toggle and turn it on.

##### Adding background color

To change the background color of the fields:

1. Select **CreditCardForm** from the widget tree or the canvas area.
2. Move to the Properties panel and scroll down to the **Input Decoration Properties** section.
3. Find the **Fill** toggle and turn it on.
4. Now find the **Fill Color** property, click on the box next to **Unset**, select the color, and then click **Use Color** or click on **Unset** and enter a Hex Code directly. You can also choose the color by clicking on the Palette and Simple buttons.

##### Customizing border

To customize the border around the credit card fields:

1. Select **CreditCardForm** from the widget tree or the canvas area.

2. Move to the Properties panel and scroll down to the **Input Decoration Properties** section.

3. Select from the **Input Border Type** dropdown. 1. Choose **Outline** to place a border around the entire field.
   2. Choose **Underline** to place a border only on the bottom of the field.
   3. Choose **None** to eradicate the border.

4. Scroll down a bit to find the **Border Color** property, click on the box next to the already selected color, select the color, and then click **Use Color** or click on an already selected color and enter a Hex Code directly. You can also choose the color by clicking on the Palette and Simple buttons.

5. Find the **Border Width** property below, and enter the desired value.

6. Now, Enter the **Border Radius** property and enter the value as 50. By default, the value 50 will be set for all corners, which are TL (Top left), TR (top right), BL (bottom left), and BR (bottom right). Click on the lock icon to change each corner separately.

##### Add content padding

Content padding adds space between the field text and the border.

To add the content padding:

1. Select **CreditCardForm** from the widget tree or the canvas area.
2. Move to the Properties panel (on the right side of your screen) and scroll down to the **Input Decoration Properties** section.
3. Find the **Content Padding** property and enter the values for L(left), T(top), R(right), and B(bottom) input boxes.

##### Reducing field height

You might want to reduce the field height to match your design. Using the dense property, you can reduce the field height to a predefined size.

To reduce the field height:

1. Select **CreditCardForm** from the widget tree or the canvas area.
2. Move to the Properties panel (on the right side of your screen) and scroll down to the **Input Decoration Properties** section.
3. Find the **Dense** toggle and turn it on.

---

### DataTable (Paginated) {#datatable-paginated}

*Learn how to add DataTable widget in your FlutterFlow project.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/datatable

The DataTable is a widget used to display data in a table format. It organizes information into rows and columns, similar to a spreadsheet, making it easier to read and understand large amounts of data.

For example, you could use it to display a list of employees in a company, with each row representing an individual employee and the columns showing the employee's name, age, department, and salary.

Additionally, this widget supports pagination, which can handle large datasets by displaying them in manageable chunks.

![paginated-data-table-fi](https://docs.flutterflow.io/assets/images/paginated-data-table-fi-5210ba954854e542064291691155495e.avif)

#### Adding DataTable widget

Let's see how to add a DataTable widget by building an example that shows a list of all employees in a company. Here's how it looks:

The steps to add DataTable and display the employees' details are:

1. Open the [Widget Palette](https://docs.flutterflow.io/flutterflow-ui/widget-palette) and locate the **DataTable** widget under the **Layout Elements** tab. You can drag it into your desired location or add it directly from the widget tree or canvas area.

2. It adds two types of predefined widgets: 1. **DataTableHeader**: This refers to the top row of the table, which displays the names of the columns. To change its text, click on the **DataTableHeader > Text** widget, move to the properties panel and give it a name.
   2. **DataTableCell**: This displays the actual data. By default, it comes with the Text widget. However, you can replace it with any other widget based on your requirements. ![data-table-header](https://docs.flutterflow.io/assets/images/data-table-header-5386eefbd8baa55687bfd6095b2ac4f1.avif)

3. By default, it shows three columns. To show more, select the **DataTable** widget, move to the **properties panel > Paginated Data Table Properties >** enter the **Number of Columns** you want.

4. For the demonstration purpose, let's display data from Firestore: 1. First, ensure you have created a collection.
   2. *It's **important to note** that, unlike other widgets, you cannot directly have a backend query on the DataTable widget. Because if you do so, you won't have access to the query result (list of employees) for further use, such as sorting and searching. Hence, getting the backend query result on a parent widget and then using that result to populate DataTable is advisable.*
   3. For this example, on page load, we'll add a Query Collection action and save the result in a page state variable.
   4. On the **DataTable** widget, generate dynamic children using the page state variable (which holds a list of employees).
   5. Display data in the **DataTableCell > Text**.

#### Sorting

The way sorting works in a DataTable is as follows: first, you mark the column to sort. Then, whenever a user clicks on a header, you receive an *OnSortChanged* callback with two properties: `Sorted Column Index` and `Is Ascending`. You consume both properties in a custom function to write a sorting logic.

* **`Sorted Column Index`** specifies the column by which the data should be sorted (0 for first column, 1 for the second column and so on).
* **`Is Ascending`** determines the sort direction (true for ascending order, false for descending order).

> **Info:** **Remember**, sorting is not performed automatically by the DataTable widget. It provides you the flexibility to implement your own sorting logic through a Custom Function.

Let's extend the previous example and see how you can enable sorting on columns. Here's how it looks:

To enable sorting:

1. Select the **DataTableHeader**, move to the **Properties Panel**, and turn on the **Sortable** toggle. Apply this to each column you want to sort
2. Select the DataTable widget, select **Actions** from the Properties panel, and open **Action Flow Editor**.
3. Select the **On Sort Changed**. Actions added under this will be triggered whenever the user clicks on any column header that has sorting enabled.
4. For this example, we update the same page state variable (that populates the DataTable) with the sorted data using the following custom function.

```
List<EmployeesRecord> sortMyData(
  List<EmployeesRecord> listToSort,
  bool isAsc,
  int sortColumIndex,
) {
  /// MODIFY CODE ONLY BELOW THIS LINE

  // Sort by 'name' for 0, 'age' for 1, 'position' for 2 in code.
  switch (sortColumIndex) {
    case 0:
      listToSort.sort((a, b) => a.name.compareTo(b.name));
      break;
    case 1:
      listToSort.sort((a, b) => a.age.compareTo(b.age));
      break;
    case 2:
      listToSort.sort((a, b) => a.position.compareTo(b.position));
      break;
    default:
      break;
  }
  if (!isAsc) {
    listToSort = listToSort.reversed.toList();
  }
  return listToSort;

  /// MODIFY CODE ONLY ABOVE THIS LINE
}
```

#### Searching

You can add search functionality to the DataTable widget using our Simple Search feature. However, for this specific widget, instead of using a [Conditional Builder](https://docs.flutterflow.io/concepts/layouts/conditional-builder) widget, you can directly utilize the [Conditional Value](https://docs.flutterflow.io/resources/functions/conditional-logic#conditional-value-ifthenelse) to determine which result to display based on the `IsShowFullList` variable.

![searching-through-table](https://docs.flutterflow.io/assets/images/searching-through-table-7eaa66ef377e289c012db89a9600069d.avif)

#### Selecting rows

You might want to allow users to select one or more of its rows for tasks like editing, deleting, or performing specific actions on the selected data. For example, preparing a list of promoted employees from the main employee listing.

To achieve this, create a page state variable to store the selected list. Upon button click, update this variable with the chosen selections from the DataTable. **Note that** the DataTable provides a list of selected row indices; you'll need a [custom function](https://docs.flutterflow.io/concepts/custom-code/cloud-functions) to retrieve the actual rows corresponding to these indices.

Here are the exact steps:

1. First, create a [page state](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#creating-a-page-state) variable that will hold the list of selected rows.
2. Select the **DataTable**, move to the **Properties Panel > Paginated Data Table Properties >** turn on the **Selectable** toggle.
3. On button click, [update the page state](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#update-page-state-action) variable with the selected rows. While adding this action, use the following custom function to retrieve the selected items based on the indices. You can get the list of selected rows indices via **Widget State > DataTable Selected Rows**.
4. Optionally, you could pass this variable to a new page to display the selection.

Custom function:

```
List<EmployeesRecord> findPromotedEmps(
  List<EmployeesRecord> allEmps,
  List<int> selecteEmpsIndex,
) {
  // MODIFY CODE ONLY BELOW THIS LINE
  // return allEmps based on selecteEmpsIndex
  List<EmployeesRecord> promotedEmps = [];
  for (int i = 0; i < selecteEmpsIndex.length; i++) {
    int index = selecteEmpsIndex[i];
    if (index >= 0 && index < allEmps.length) {
      EmployeesRecord emp = allEmps[index];
      promotedEmps.add(emp);
    }
  }
  return promotedEmps;
  /// MODIFY CODE ONLY ABOVE THIS LINE
 }
```

#### Get notified on page changed

You might want to get a callback whenever a user taps on the next page of the DataTable. For example, to make an API call to retrieve the data for the next page.

To do so:

1. Select the **DataTable** widget.
2. Select **Actions** from the Properties panel and open **Action Flow Editor**.
3. Select **On Page Changed**. This callback gives you the **Current Row Index**, which is the index of the first row of a new page. For example, if you have 25 items (0-24) on the current page, the **Current Row Index** value will be 25. This is helpful in APIs that fetch a fixed set of data by specifying a starting position ([offset](https://developer.box.com/guides/api-calls/pagination/offset-based/)).
4. Now, add an action to call the paginated API (that returns the result in chunks). See [how to add the paginated API](https://docs.flutterflow.io/resources/backend-logic/rest-api#query-parameters) call by adding query parameters. For this example, we use this API: <https://reqres.in/api/users?per_page=7&page=1>. **Note**: this API uses page-based rather than offset-based pagination, requiring manual adjustment of the page variable.
5. On the success of the API call, you can add an action to append the new data in the current list. For this, you can add the following custom function to add new results to existing data.

```
List<UserStruct> addAlldatatoList(
  List<UserStruct> currentUsersList,
  List<UserStruct> newUsersList,
) {
  /// MODIFY CODE ONLY BELOW THIS LINE

  // add all newUsersList to currentUsersList
  currentUsersList.addAll(newUsersList);
  return currentUsersList;

  /// MODIFY CODE ONLY ABOVE THIS LINE
}
```

#### Get notified on rows per page changed

Sometimes, you might want to get a callback when a user changes the number of rows to display on a page. This is helpful for dynamically adjusting data fetch requests based on user preferences.

This is how you do it:

1. Select the **DataTable** widget.
2. Select **Actions** from the **Properties panel** and open **Action Flow Editor**.
3. Select **On Rows Per Page Changed**. Any actions added under this will be triggered when the number of displayed rows is changed.
4. Now, you can add any action here.

![get-notified-on-row-changed-per-page](https://docs.flutterflow.io/assets/images/get-notified-on-row-changed-per-page-68dbbe36c595912ea9c093d9a8f999d9.avif)

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

##### Configure paginated DataTable

To configure the paginated DataTable, move to the **Properties Panel > Paginated Data Table Properties** and then:

* To hide the pagination, turn on the **Hide Paginator** toggle.
* To display buttons to navigate to the first and last page of the DataTable, turn on the **Show First And Last Buttons**.
* To have a normal DataTable without pagination, turn off the **Paginated** toggle.

> **Info:** Typically, setting the size explicitly isn't necessary for a DataTable, as it's designed to showcase large datasets and should utilize all available space. However, to enable horizontal scrolling in the DataTable (when content exceeds screen width), you must specify the **Min Width**.

##### Adjust row and column spacing

To modify the row and column spacing, move to the **Properties Panel > Layout Properties** and then tweak the following properties:

* **Header Row Height**: This changes the height of the header.
* **Data Row Height**: This changes the height of all the rows.
* **Column Spacing**: This changes the distance between columns.

##### Customize DataTable color

To modify the DataTable color, navigate to the **Properties Panel > Style Properties**, where you can set colors for various elements:

* **Header Row Color**: This changes the background color of the header row.
* **Row Color**: This sets the background color for all rows.
* **Alternate Row Color**: This allows for a different background color for alternate rows.
* **Sort Icon Color**: This alters the color of the sort icon used in sortable columns.

##### Adjust border radius

To add the rounded corner to the DataTable, navigate to the **Properties Panel > Style Properties > Border Radius** and then:

1. Enter values for TL (Top left), TR (top right), BL (bottom left), and BR (bottom right).
2. To apply the same radius on all sides, switch to the **Uniform Radius** option. You can then adjust the radius by either moving the slider or entering the desired value directly.

![adjust-row-border](https://docs.flutterflow.io/assets/images/adjust-row-border-36196b67df9ddebc447abe1159bb5fec.avif)

##### Add dividers

To add horizontal and vertical dividers inside the DataTable, navigate to the **Properties Panel > Style Properties >** turn on the **Horizontal** and **Vertical Dividers**.

After enabling, you can also change its **Color** and **Thickness**.

![add-dividers](https://docs.flutterflow.io/assets/images/add-dividers-44a337a79fddd01973f65573ada53ef2.avif)

##### Customize checkbox colors

When rows are selectable, you can customize the appearance of the checkbox by adjusting the following color properties:

* **Selected Fill Color**: Sets the background color of the checkbox when it is selected.
* **Unselected Fill Color**: Sets the background color of the checkbox when it is not selected.
* **Unselected Border Color**: Changes the border color of the checkbox when it is not selected.
* **Selected Border Color**: Changes the border color of the checkbox when it is selected.
* **Check Color**: Alters the color of the checkbox mark itself when selected, providing visual feedback to users about their selection status.

---

### Dividers {#dividers}

*Add a thin horizontal or vertical line, with padding on either side. Customize the color, width*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/dividers

Add a thin horizontal or vertical line, with padding on either side. Customize the color, width or height, and style of the divider from the Properties Panel.

#### Divider Properties

Here are the properties in detail:

![divider.png](https://docs.flutterflow.io/assets/images/divider-7b4c775b67dbc4c100dbe304e2900405.png)

Divider (Horizontal) Properties

![v-divider.png](https://docs.flutterflow.io/assets/images/v-divider-1494face8c703ce035468b4a8d3bf78c.png)

Vertical Divider Properties

* **Line Style**: This property determines the visual pattern of the divider line. Options typically include:

  * **Solid**: A continuous line.
  * **Dotted**: A series of dots.
  * **Dashed**: A series of dashes.
  * **Dashdotted:** A combination of dashes and dots.

* **Color**: Defines the color of the divider line. This can be set using predefined theme colors or custom values to match or contrast with the application's design scheme.

* **Thickness**: Specifies the thickness of the divider line, influencing its visual prominence. Thicker lines are more noticeable and can be used to make a bold statement, while thinner lines are subtler.

* **Width**: This property sets the horizontal length of the divider. It can be specified in absolute terms (e.g., pixels).

* **Height**: For vertical dividers, this property sets the vertical length. Like width, it can also be defined in pixels.

* **Indent and End-Indent**: These properties control the spacing from the edges of the container to the start and end points of the divider line, respectively. Indents can be used to fine-tune the placement of the divider within a layout, helping to achieve a balanced or desired aesthetic effect.

---

### Draggable + DragTarget {#draggable-dragtarget}

*The Draggable widget is used to make a widget that can be dragged and dropped to a different location within the app. It allows users to interact with the app by moving an item using touch gestures or a mouse. The DragTarget widget is used in conjunction with the Draggable widget to specify where a dragged item can be dropped. It creates a region that can accept the data carried by the Draggable widget.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/draggable

The Draggable widget is used to make a widget that can be dragged and dropped to a different location within the app. It allows users to interact with the app by moving an item using touch gestures or a mouse. The DragTarget widget is used in conjunction with the Draggable widget to specify where a dragged item can be dropped. It creates a region that can accept the data carried by the Draggable widget.

When an item is dragged over a DragTarget, the DragTarget has the opportunity to determine whether it can accept the item. If it accepts, it can then trigger actions such as updating the app's state to reflect the change.

For example, in a shopping cart app, you could use these widgets together to allow users to add items to their cart by dragging and dropping them onto a cart icon.

#### Adding Draggable and DragTarget Widgets

Let's see how to add a drag-and-drop functionality by building an example that allows users to put only plants on the shelf. Here's how it looks:

The steps to build such an example are as follows:

##### 1. Create page state variable

In this example, we have two images of a shelf: one with empty space for one plant and another with all plants on the shelf. To control which image to show based on whether the correct item is dropped on the shelf, we need a [page state variable](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#page-state). Therefore, [create a page state variable](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#creating-a-page-state) named `isShelfFull` with the datatype *Boolean* and set its default value to *False*.

![img\_1.png](https://docs.flutterflow.io/assets/images/img_1-f80cacf0889a64d442e5907793c4005c.png)

Control image display based on page state variable

##### 2. Add Draggable widgets

Let's add the draggable widgets and specify the data for each widget. This data will later be used to determine if the correct item is being dropped on the shelf. For instance, you can assign a unique identifier or a type attribute (e.g., plant, spoon, toy) to each draggable widget.

> **Note:** As we proceed in this section, you'll learn how this information is crucial for the DragTarget widget to evaluate whether the item being dropped matches the expected type for the shelf.

In this example, the draggable items are a plant, a spoon, and a football. Let's see how to add them:

1. Inside the **Row** widget, add **Draggable** widgets directly from the widget tree or canvas area.
2. Inside the **Draggable** widget, you can add any widget as a child widget. For this example, we use the **Image** widget.
3. To add data to draggable widgets, select the **Draggable widget > Properties Panel > Draggable Properties >** specify the **Type** of the data and its **Value**.

> **Info:** The Draggable widget also provides you with various drag events (as [**Action Triggers**](https://docs.flutterflow.io/resources/functions/action-triggers)) that you might want to use to customize the drag experience. These include:

* **On Drag Started**: Gets triggered when the user initiates a drag operation.
* **On Drag Update**: Gets triggered when the drag is currently in progress, allowing you to track its movement or update other UI elements accordingly.
* **On Drag Completed**: Gets triggered when the user successfully drags and drops the widget into [**DragTarget**](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/draggable#3-add-dragtarget-widget) widget.
* **On Drag Cancelled**: Gets triggered when the drag operation is aborted, such as when the user releases the widget outside a **DragTarget** or the DragTarget rejects the widget.
* **On Drag End**: Gets triggered when the drag operation finishes, regardless of whether it was completed or cancelled.

##### 3. Add DragTarget widget

The DragTarget widget in this example allows users to drop items onto the shelf. We utilize the Stack widget to layer the DragTarget widget over the shelf image. Moreover, the display of the shelf image is controlled by the [ConditionalBuilder](https://docs.flutterflow.io/concepts/layouts/conditional-builder) widget, which uses the `isShelfFull` variable to determine which image to show. This widget arrangement ensures that the shelf image updates dynamically based on whether the shelf is full or not.

Let's see how to add DragTarget widget:

1. Open the [Widget Palette](https://docs.flutterflow.io/flutterflow-ui/widget-palette) and locate the **DragTarget** widget under the **Base Elements** tab. You can drag it into your desired location or add it directly from the widget tree.
2. Inside the **DragTarget** widget, add a [**Container**](https://docs.flutterflow.io/resources/ui/widgets/container) widget, preferably of the same size as the image, and set its background color to transparent. This will serve as the drop zone for draggable items.
3. Now, you need to specify the type of data this target will receive. To do so select the **DragTarget widget > Properties Panel > Draggable Properties >** specify the **Type** of the data. This is crucial for ensuring that only the correct items can be dropped on the target.

##### 4. Get notified on drag events

The DragTarget widget provides you with the various drag events (aka callbacks) which are essential in building drag and drop functionalities.

Here are they:

* **On Drag Accept:** Actions under this are triggered when the data is dropped over the DragTarget.
* **On Drag Enter:** Actions under this are triggered when the data is being dragged over DragTarget.
* **On Drag Exit:** Actions under this are triggered when a draggable item that was previously over the DragTarget leaves its area. For example, In the shopping app, if the user decides not to drop the item into the cart and moves it away, this event callback can be used to remove the highlight from the shopping cart.

> **Tip:** You can use On Drag Accept or On Drag Enter to determine if DragTarget can receive the data and accordingly update the app state.

It's crucial to think about the user experience you wish to create. For instance, if you aim to trigger an action as soon as an item enters the drop area, utilize On Drag Enter along with On Drag Exit. Conversely, if your action should occur only after the item has been dropped, then On Drag Accept, paired with On Drag Exit, is your go-to option.

Let's see how to add drag events for this example:

1. Select **DragTarget** widget, select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.

2. To ensure that only a plant item is being dropped:

   1. Select the **On Drag Accept** and select **+ Add Conditional Action**.
   2. From the **set variable** menu, select **Drag Target > Dragged Data**. This captures the data of the draggable item that we added in [step 2](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/draggable#2-add-draggable-widgets).
   3. Check if the captured data matches the expected item, i.e., plant.
   4. In the **TRUE** branch, you can add a [snackbar message](https://docs.flutterflow.io/resources/ui/pages/scaffold#snackbar) and [update](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#page-state) the `isShelfFull` variable to True. This will create an effect like the user has actually dragged and dropped the item onto the shelf.

3) Now, select the **On Drag Exit** andadd an action to [update](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#page-state) the `isShelfFull` variable to False. This ensures that if the user decides not to drop the item and moves it away, the shelf image reverts to the empty one.

![img\_2.png](https://docs.flutterflow.io/assets/images/img_2-c110529846ac9814ffd79fbdfffc630f.png)

---

### Expandable {#expandable}

*An Expandable widget is a user interface component used to show or hide content dynamically. It consists of a header that can be tapped to reveal or collapse additional content. This functionality is particularly useful in interfaces where space is at a premium, such as in mobile applications or complex forms, enabling users to access information on demand without overwhelming the screen with too much content all at once.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/expandable

An Expandable widget is a user interface component used to show or hide content dynamically. It consists of a header that can be tapped to reveal or collapse additional content. This functionality is particularly useful in interfaces where space is at a premium, such as in mobile applications or complex forms, enabling users to access information on demand without overwhelming the screen with too much content all at once.

**Default Widget Tree for Expandable Widget**

When you add an **Expandable** widget, the default widget tree typically includes:

* **Header:** The visible part of the widget when it is both collapsed and expanded. This usually contains a label or icon indicating what the expandable content relates to.
* **Collapsed View:** The default state showing minimal content or summarization.
* **Expanded View:** Contains more detailed information or additional controls that are visible when the widget is expanded.

![expandable-widget-tree.avif](https://docs.flutterflow.io/assets/images/expandable-widget-tree-7f0f06e1450e64f33575ea6e218275cf.avif)

#### Expandable Widget Properties

* **Icon Properties:** For Icon Properties, check out the **[Icon](https://docs.flutterflow.io/resources/ui/widgets/icons)** guide.

* **Expandable Properties:**

  * **Active View:** Specifies whether the widget is currently in the collapsed or expanded state.
  * **Initially Expanded:** Determines if the widget should be expanded by default when the view is first loaded.
  * **Tap Header to Toggle:** Allows the user to expand or collapse the content by tapping the header.
  * **Tap Body to Expand/Collapse:** Defines whether tapping on the body of the expanded content can toggle its state.

* **Style Properties:**

  * **Width & Height:** Dimensions of the widget, which can be set to infinity to take full width or height.
  * **Background Color:** The color behind the expandable content.
  * **Header Alignment:** Aligns the header content such as left, center, or right.

##### Practical Use of Expanded

This setup allows for a highly customizable Expandable widget, making it suitable for FAQs, forms, lists, or other content that benefits from a clean, compact initial appearance with options for more detailed information. The ability to fine-tune how and where icons appear, along with the behavior of the widget's expandability, gives developers significant control over user experience and interface design.

---

### FlippableCard {#flippablecard}

*Learn how to add Flippable Card widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/flippable-card

The FlippableCard widget provides the visual interaction called 'Flip card animation'. Initially, it shows the front side of the card, and when you tap on it, it shows the back side.

You could use this widget to show and hide details of an item (e.g., credit card, online course card, coupon card, etc.)

#### Adding FlippableCard widget

To add the FlippableCard widget:

1. First, click on the **+ Add Widget** and drag the **FlippableCard** widget from the **Layout Elements** tab or add it directly from the widget tree.
2. Select the **Card Front** from the widget tree and customize or replace the **Container** with the widget of your choice. For example, replacing it with a **Credit Card** widget (under the Templates > Card Views).
3. To edit the back side of the card, select the **FlippableCard**, move to the properties panel, scroll down to the **Flippable Card Propertie**s and enable the **Edit Back of Card**.
4. Now select the **Card Back** from the widget tree and customize or replace the **Container** with the widget of your choice. For example, again, add the Credit Card widget and customize it to show the details.

#### Customizing

You can customize the appearance of this widget using the various properties available under the properties panel.

##### Changing flip direction

By default, this widget flips the card in the horizontal direction (i.e., from left to right and right to left).

To change the flip direction:

1. Select the **FlippableCard** widget from the widget tree or canvas area.
2. Move to the properties panel, and scroll down to the **Flippable Card Properties** section.
3. Find the **Flip Direction** dropdown and change it to **Horizontal** or **Vertical**.

##### Changing flip animation duration

When you tap on this widget, the flip animation completes in 400ms (milliseconds). You can change this duration if you wish to make it a little faster or slower.

To change the flip animation duration:

1. Select the **FlippableCard** widget from the widget tree or canvas area.
2. Move to the properties panel, and scroll down to the **Flippable Card Properties** section.
3. Find the **Flip Animation Duration** property and change the value. Note: The value should be in milliseconds (e.g., 1000ms = 1 second).

##### Disable flip on tap

By default, the card flips when you tap on it. To disable this behavior, move to the **properties panel > Flippable Card Properties** > disable **Flip on Tap** toggle.

---

### Markdown {#markdown}

*The Markdown widget is used to input and display text using Markdown syntax. It allows you to format text easily, without the complexity of a full-fledged WYSIWYG (What You See Is What You Get) editor or the need to write HTML code.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/markdown

The Markdown widget is used to input and display text using [Markdown syntax](https://www.markdownguide.org/basic-syntax/). It allows you to format text easily, without the complexity of a full-fledged WYSIWYG (What You See Is What You Get) editor or the need to write HTML code.

You could use this widget in various applications like note-taking apps, forums, and blogging platforms. They are particularly popular in technical and coding communities for their ease of formatting code snippets and descriptions.

![img.png](https://docs.flutterflow.io/assets/images/img-fe542d54ca6413fb02dc2ef49a03ef09.png)

#### Adding Markdown widget

To add a Markdown widget:

1. Open the [Widget Palette](https://docs.flutterflow.io/flutterflow-ui/widget-palette) and locate the **Markdown** widget under the **Base Elements** tab. You can either drag it into your desired location or add it directly from the widget tree.
2. To display the markdown content, move to the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) and enter the text inside the **Data** section.
3. Optionally, you have the choice to make your Markdown content selectable. This can be adjusted using the **Selectable** property.

---

### MediaDisplay {#mediadisplay}

*Learn how to add MediaDisplay widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/media-display

The **MediaDisplay** widget in FlutterFlow automatically detects the type of media fetched from a URL and adjusts the widget accordingly. For instance, if the URL returns an image, the widget will behave as an Image widget.

This versatility allows you to easily present various types of media within your app. For example, it can be integrated into scrollable widgets like [ListView](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#listview-widget) for displaying activity feeds or [GridView](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#gridview-widget) for presenting photos and videos together.

#### Adding MediaDisplay widget

Let's build an example of using the MediaDisplay widget inside the ListView and display the photos and videos from the Firestore database.

The steps to add and use the MediaDisplay are as follows:

1. Add the **MediaDisplay** widget from the **Base Elements** tab and drop it inside the **ListView**.

2) Create a collection and add data with some image and video URLs.
3) Query a collection to get a list of documents from the Firestore collection and show them in the ListView.
4) To display media inside the widget, move to the properties panel > **Media Path** > Set from Variable menu. Select the source as **\[collection\_name] Document** and select the field that holds the URL path from the **Available Options** list.

#### Customizing

You can customize the appearance and behavior of the widget using the various properties available under the properties panel.

##### Customizing Image

To customize the widget when image is displayed, refer [here](https://docs.flutterflow.io/resources/ui/widgets/image#common-image-properties).

##### Customizing Video

To customize the widget when video is displayed, refer [here](https://docs.flutterflow.io/concepts/file-handling/displaying-media#videoplayer).

---

### MouseRegion {#mouseregion}

*The MouseRegion widget lets you know whenever the mouse pointer enters or exits from a widget. You could use it to build a user experience (UX), such as animating buttons when a user hovers over them and revealing or hiding menu items when a user hovers over the menu icon.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/mouse-region

The `MouseRegion` widget lets you know whenever the mouse pointer enters or exits from a widget. You could use it to build a user experience (UX), such as animating buttons when a user hovers over them and revealing or hiding menu items when a user hovers over the menu icon.

On this page, you will learn how to [add the MouseRegion widget](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/mouse-region#adding-mouseregion-widget), use it to [show/hide elements](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/mouse-region#showhide-elements-using-mouseregion), and [customize](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/mouse-region#customizing) it.

#### Adding MouseRegion widget

Here are the step-by-step instructions to build such an example:

1. First, click on the **+ Add Widget** and drag the **MouseRegion** widget from the **Base Elements** tab or add it directly from the widget tree.
2. Add a [**Button**](https://docs.flutterflow.io/resources/ui/widgets/button) (inside MouseRegion) with [**On Action Trigger**](https://docs.flutterflow.io/concepts/animations/widget-animations#animation-on-action-trigger) animation.
3. Select the **MouseRegion** widget, select **Actions** from the Properties Panel (the right menu), and click **Open**. This will open an **Action flow Editor** in a new popup window.
4. Select the **On Mouse Enter** tab. Actions added under this will be triggered whenever the mouse enters the MouseRegion widget. 1. Add the [Widget Animation](https://docs.flutterflow.io/concepts/animations/widget-animations) action to start the animation on a Button.
5. Select the **On Mouse Exit** tab. Actions added under this will be triggered whenever the mouse leaves the MouseRegion widget. 1. Add the [Widget Animation](https://docs.flutterflow.io/concepts/animations/widget-animations) action to stop the animation on a Button.

#### Show/hide elements using MouseRegion

Using the callbacks provided by the MouseRgion widget, you can show or hide a widget. The idea is to update the *App State* variable when the mouse pointer enters or exits the widget. And then use the same app state variable to add *Conditional Visibility* on a widget.

Let's see how to build the following example:

Here are the step-by-step instructions:

1. First, add the Stack **>** **Container** **> MouseRegion >** **IconButton** to display the menu icon.
2. Add the **Container > MouseRegion >** **Column** (with some menu items/options) inside the same Stack widget.

Note

Note that we wrapped the menu icon and its options inside the MouseRegion widget. In the next step, we will add the same actions for both MouseRegion widgets so that the menu options stay visible as long as you hover over them.

![img\_9.png](https://docs.flutterflow.io/assets/images/img_9-8b6a979e7ead3b7291192c7f05eb1a2a.png)

3. Create a boolean [App State variable](https://docs.flutterflow.io/resources/data-representation/app-state) and use it to [add conditional visibility](https://docs.flutterflow.io/resources/ui/widgets/widget-commonalities#conditional) on menu options.
4. On both MouseRegion widgets, add an [update app state variable](https://docs.flutterflow.io/resources/data-representation/app-state#update-app-state-action) action to set **True** when the mouse enters and **False** when the mouse exit.

Use app state variable and MouseRegion to show/hide a widget

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the **Properties Panel**.

##### Customize mouse cursor

When a mouse enters the widget, its cursor will change to the appropriate one by default. However, you can also set it to a custom one if you wish to.

To customize the mouse cursor, select the **MouseRegion** widget, move to the properties panel, find the **Mouse Cursor** dropdown select the one you think fits best.

---

### PinCode {#pincode}

*Learn how to add the PinCode widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/pincode

The PinCode widget allows you to enter the PIN or OTP. You could use this widget to verify the user identity or a transaction before making payments in fintech apps.

Widget State

Before diving into form widgets, check out our guide on [**Widget States**](https://docs.flutterflow.io/concepts/state-management/widget-state) to efficiently manage the state and behavior of your form elements.

#### Adding PinCode widget

To add a PinCode widget:

1. Open the [Widget Palette](https://docs.flutterflow.io/flutterflow-ui/widget-palette) and locate the **PinCode** widget under the **Base Elements** tab. You can drag it into your desired location or add it directly from the widget tree or canvas area.
2. To increase the pin length (number of values users can enter), move to the properties panel, see the **Pin Length** property, and enter the value. **Note**: You can only set this value up to 8.
3. If you are using this widget to get a secret PIN from users, you can obscure it with a special character. To do so, enable the **Obscure Text** toggle and select the **Obscuring Character** among the \*,-,?, and •.
4. You can also enable/disable the **Hint Text** toggle and select the **Hint Character** displayed when you haven't entered anything.

#### Trigger Action On Completed

Let's see how to trigger an action when you are done entering the value in this widget. This is helpful when you want to compare the entered value with the one stored in your backend.

To do so:

1. Select the **PinCode** widget, select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.
2. Set the **Type of Action** (aka callback) to **On Completed**. That means actions added under this will be called after the user has entered all PIN field values.
3. Now you can add any action here.

Here is an example of displaying a snackbar message that shows the entered value in the PinCode widget.

#### Trigger Action On Change

You may want to trigger an action whenever users enter or delete the value in each field of this widget. For instance, you can check the validity of the entered digit as soon as the user types it in and show a message that it is not valid. To do this, [add an action using the trigger](https://docs.flutterflow.io/resources/forms/form-triggers#on-change) that responds to changes in this widget.

#### Trigger Action On Focus Change

You may want to trigger an action when the user taps into or exits the Pincode field. For example, you can run a validation check once the user finishes entering the code and moves focus away from the field. To do this, [add an action using the trigger](https://docs.flutterflow.io/resources/forms/form-triggers#on-focus-change) that responds to focus changes in this widget.

#### Validation

You can validate the Pincode widget to see if a user has entered any value. To do so, wrap the Pincode widget inside the [**Form**](https://docs.flutterflow.io/resources/forms/form-validation#adding-form-widget) widget, In the *Form* widget, enter the error message you want to display and then trigger the [**Validate Form**](https://docs.flutterflow.io/resources/forms/form-validation#3-adding-validate-action) action. This will display an error message when a user tries to submit the form without a pincode value.

You can also adjust the height to the error text from **Properties Panel > Error text height**.

![Set error text height](https://docs.flutterflow.io/assets/images/set-error-text-height-33fb804125c167aebbf767935c094286.png)

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

##### Changing keyboard type

When the keyboard opens by default, you can enter only numbers. But you might want to allow users to enter both letters and numbers. To do so, select the **PinCode** widget, move to the **Properties Panel** **> PinCode Properties >** set the **Keyboard Type** to the **Visible Password**.

![Keyboard Type](https://docs.flutterflow.io/assets/images/keyboard-type-5cfaa2613a7498d4a87b7703e1897bbc.webp)

![Keyboard type: Visible Password](https://docs.flutterflow.io/assets/images/keyboard-type-visible-password-aa5bfba910b56312073b4646db7b61a9.png)

##### Using PinCode for secret pin

To make a *PinCode* a secret pin field, move to the **Properties Panel > Pin Code Properties >** enable the **Obscure Text**. Now, when you enter a value, it will be obscured with the star (\*). You can change this symbol using the **Obscuring Character** dropdown.

##### Setting hint character

A hint character refers to a special character or symbol that is displayed in each input field of the PinCode Widget to give users a visual clue about the expected input format. Hint characters are often used in combination with the actual input characters to guide users when entering a PIN or password.

To set the hint text, move to the **Properties Panel > Pin Code Properties > enable the Hint Text > set the Hint Character**.

##### Auto focus

When enabled, it mimics the tap event and immediately shows the keyboard. This makes *PinCode* widget ready to receive input from users without having to click on it. In case, you want to disable this behaviour, move to the **Properties Panel** **> Pin Code Properties >** disable the **Auto Focus** property.

##### Auto Fill

When this is enabled, it can read and auto fill the code from your messages app.

![Auto Fill enabled](https://docs.flutterflow.io/assets/images/auto-fill-enabled-7c3e5da02c15b11362b97970d64f3f22.png)

##### Aligning pin code fields

By default, all the pin fields are aligned to *Space Evenly*. Meaning there will be equal space between each pin field.

The following options help you align the pin code fields:

* **Start**: Place pin code fields as close to the beginning as possible.
* **Center**: Place pin code fields as close to the middle as possible.
* **End**: Place pin code fields as close to the end as possible.
* **Space Evenly**: Evenly space pin code fields.
* **Space Around**: Place the free space evenly between the pin code fields with some extra space at the beginning and end.
* **Space Between**: Place the free space evenly between the pin code fields. To configure the space between and around the pin fields, select the **PinCode** widget, move to the properties panel, find the **Pin Code Alignment** property and select among the above options.

##### Changing pin field shape and size

To change the pin field shape and size:

1. Select the **PinCode** widget, move to the properties panel, find the **Pin Field Shape** property, and here you can set the shape to **Box**, **Circle**, and **Underline**.
2. To change the height and width, enter the value in **Field Height**, and **Field Width** boxes.
3. To create a rounded border when the shape is set to *Box*, use the **Border Radius** and **Border Width** properties.

##### Change colors

You can change colors for the different states of the pin fields. To do so:

1. Select the **PinCode** widget, move to the properties panel, and change the colors for the following properties: * **Active Color**: This sets the border color when the value is entered.
   * **Inactive Color**: This sets the border color when there is no value.
   * **Selected Color**: This sets the border color when the cursor is inside the pin field and the user is about to enter the value.

2. To change the background color instead of only the border color, **Enable Active Fill**.

##### Customizing cursor

You can show/hide the cursor using the **Show Cursor** toggle and change the color using the **Cursor Color** property.

Clear pin code value

See how to [**reset the pin code value**](https://docs.flutterflow.io/resources/forms/reset-form-field).

---

### ProgressBar {#progressbar}

*Learn how to add ProgressBar widget in your FlutterFlow project.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/progressbar

The ProgressBar widget is used to represent the progress of any task. You can use the ProgressBar widget to build a UI that shows the downloading or uploading of files, sales this week, hours spent, overall score, etc.

#### Adding ProgressBar

Here's how you can add the ProgressBar widget to your project:

1. Add the **ProgressBar** widget by dragging it from the **Base Elements** tab or directly from the widget tree and align it in the center.

2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Progress Bar Properties** section.

3. Find the **Progress Bar Shape** dropdown and set it to either **Circular** or **Linear**. * **Circular**: The ProgressBar is displayed in a Circle shape. This is the default shape set to the ProgressBar.
   * **Linear**: The ProgressBar is displayed in a rectangular shape and laid out horizontally on the screen.

4. To set the progress, find the **Progress Value** input box and enter the value between 0 and 1.0. For example, a value of 0.3 will fill 30% of the portion on the ProgressBar.

5. To change the progress text (displayed in the center), scroll down to the **Text** section, find the Text property, and enter the value.

#### Customizing circular progress bar

The Properties Panel can be used to customize the appearance and behavior of the Circular Progress Bar.

##### Changing size

You may want to change the default size of the Circular ProgressBar to match your design. You can do so using the *Diameter* property.

To change the size of the Circular progress bar:

1. Select **ProgressBar** from the widget tree or the canvas area.

2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Progress Bar Properties** section.

3. Find the **Diameter** property. Now, there are two ways to change the size: * To set to an **exact size,** select **PX** and enter the desired values.
   * To set the size as a **% of the screen size**, select **%** and enter the desired value.

##### Changing thickness

Changing the thickness property allows you to change the size of the progress bar belt.

1. Select **ProgressBar** from the widget tree or the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Progress Bar Properties** section.
3. Find the **Thickness** property and enter the value.

##### Changing start angle

By default, the progress bar starts filling the progress from the top-center position (i.e., 0 degree). However, you can set it to start the progress bar from a specific angle using the *Start Angle* property.

To change the start angle:

1. Select **ProgressBar** from the widget tree or the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Progress Bar Properties** section.
3. Find the **Start Angle (degree)** property and enter the value in degree. For example, entering a value of 90 fills the progress bar from the right. Whereas the value of 180 fills the progress bar from the bottom.

#### Customizing linear progress bar

The Properties Panel can be used to customize the appearance and behavior of the Linear Progress Bar.

##### Changing size

You can change the default size using the *Width* property.

To change the size of the Linear Progress Bar:

1. Select **ProgressBar** from the widget tree or the canvas area.

2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Progress Bar Properties** section.

3. Find the **Width** property. Now, there are two ways to change the size: * To set to an **exact size,** select **PX** and enter the desired values.
   * To set the size as a **% of the screen size**, select **%** and enter the desired value.

##### Changing thickness

Changing the thickness property allows you to change the height of the progress bar.

1. Select **ProgressBar** from the widget tree or the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Progress Bar Properties** section.
3. Find the **Thickness** property and enter the value.

##### Changing end radius

By default, the progress bar appears in a rectangular shape. However, you can make it rounded rectangular using the *End Radius* property.

To change the end radius:

1. Select **ProgressBar** from the widget tree or the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Progress Bar Properties** section.
3. Find the **End Radius** property and enter the value.

---

### RatingBar {#ratingbar}

*Learn how to add RatingBar in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/ratingbar

The RatingBar widget is used to show a rating or collect ratings from users (this is an interactive RatingBar). For example, you can use the RatingBar widget inside an e-commerce app to show ratings for a product.

#### Adding a RatingBar to Your Project

Here's an example of how you can use the RatingBar widget in your project:

1. First, drag the **Column** widget from the **Layout Elements** tab (in the Widget Panel) or add it directly from the widget tree. Set its **Cross Axis Alignment** to **Start**.
2. Now add one **Image** widget inside the column and set its **Width** property to **inf** and **Height** property to 200.
3. Add a **Text** widget (Inside the Column). Change the **name** to **Item Name** and the **Theme Style** to **Title 1.** Set the **Left Padding** to 10.
4. Add another **Text** widget. Change the **name** to **Item Description** and the **Theme Style** to **Subtitle 2.** Set the **Left Padding** to 10.
5. Finally, add the **RatingBar** widget from the **Form Elements** tab or add it directly from the widget tree.

##### Collectings Ratings from Users (Interactive RatingBar)

To collect ratings from users:

1. Select **RatingBar** from the widget tree or from the canvas area.
2. Move to the Property Editor and scroll down to the **Rating Bar Properties** section.
3. Find the **Interactive** property and checkmark it (click on it).

##### Setting The Rating Value

The Rating can be set by inputting an amount or set from a variable. This is only for a RatingBar that is not interactive.

To manually set the Rating value for the RatingBar:

1. Select **RatingBar** from the widget tree or from the canvas area.
2. Move to the Property Editor and scroll down to the **Rating Bar Properties** section.
3. Find the **Rating** property and change the default value.

> **Info:** You can also enter the value in decimal such as 1.5. When a decimal is used, a portion of the icon will be colored.

##### Customize the Icon

Here's an example of how you can customize the icons appearing in the RatingBar:

1. Select **RatingBar** from the widget tree or from the canvas area.
2. Move to the Property Editor and scroll down to the **Rating Bar Properties** section.
3. Find the **Icon Count** property and change the value to 10.
4. Set the **Icon Size** property to 30.
5. Find the **Icon Selector** property below, Click on the **Start Rounded** button, then search and select the icon name with **FontAwesome.smile**.

##### Changing the Rated/Unrated Color

To change the rated and unrated color (color for icons that are not filled in) for the RatingBar:

1. Select **RatingBar** from the widget tree or from the canvas area.
2. Move to the Property Editor and scroll down to the **Rating Bar Properties** section.
3. Now, find the **Rated Color** property, Click on the box next to **Secondary**, select the color, and then click **Use Selected Color** or click on **Secondary** and enter a Hex Code directly. You can also choose the color by clicking on the Palette and Simple button.
4. Similarly, set the **Unrated** **Color** as well.

##### Add Padding between Icons

To add padding between icons:

1. Select **RatingBar** from the widget tree or from the canvas area.
2. Move to the Property Editor and scroll down to the **Rating Bar Properties** section.
3. Find the **Icon Padding** property and enter the values.

> **Info:** Use the Lock button to change the Left, Top, Right and Bottom padding all at the same time. Unlocking will allow you to modify each value separately.

##### Changing the Axis

In a very rare case, you may want to make all icons (inside the RatingBar) appear vertically. This can be done using the Axis property.

To change the Axis:

1. Select **RatingBar** from the widget tree or from the canvas area.
2. Move to the Property Editor and scroll down to the **Rating Bar Properties** section.
3. Find the **Axis** dropdown and change it to **Vertical**.

---

### Signature {#signature}

*Learn how to add Signature widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/signature

The signature widget allows you to capture a signature. This widget tracks your finger or mouse pointer on a screen and draws the line accordingly on a signature pad.

You can use this widget to get the user consent on an agreement or contract in digital form.

#### Adding Signature widget

Here's an example of how you can add the Signature widget to your project:

1. First, drag the **Signature** widget from the **Form Elements** tab (in the Widget Panel) or add it directly from the widget tree.
2. Move to the properties panel, scroll down to the **Signature** section and adjust the **width** and **height** of the widget.

#### Saving signature to Firestore document

You might be using the Firestore database to store your app data in the collection-document model. Let's see how you can save the signature into the Firestore document.

The drawn signature is first uploaded and stored as an image into the [Firebase Storage](https://firebase.google.com/docs/storage) using the *Upload Signature* action. This returns the uploaded URL, which can be stored inside the Firestore document for later access.

Prerequisites

Ensure you incorporate all the mentioned prerequisites.

* Be familiar with [**Structuring the Firebase Database**](https://docs.flutterflow.io/integrations/database/cloud-firestore/getting-started#structuring-the-database).
* Complete all steps in the [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) section for your project.
* [**Firebase Authentication**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) must be properly configured.
* [**Firebase Storage**](https://docs.flutterflow.io/integrations/firebase-storage/storage-rules) rules must be deployed.

Saving signature to Firestore document comprises the following steps:

##### 1. Create Image Path field

Create a Firestore Collection with the schema that contains a field with an Image Path data type. ![image-path-field](https://docs.flutterflow.io/assets/images/image-path-field-0b5a207a3ecbad66e7606284bace3a46.avif)

##### 2. Upload signature \[Action]

Using this action, you can upload the drawn signature to [Firebase Storage](https://firebase.google.com/docs/storage). This action returns the Uploaded URL, which you can use to show its content or store in a database to access it later.

Follow the steps below to define the Action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to define the action.

2. Select **Actions** from the Properties panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window. 1. Click on the **+ Add Action**.
   2. On the right side, search and select **Upload Signature**.
   3. Set the **Signature to Upload** to the name of the signature widget. (i.e., Signature by default).

3. Click **Close**.

##### 3. Passing signature image URL into document field

The *Upload Signature* action (added in the previous step) returns the URL of the signature image. You can use it to pass into the document field by adding the action that creates or updates the document, such as [Create Document](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-actions#create-document-action) or [Update Document](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-actions#update-document-action).

Here are the steps in detail:

1. Select the **Widget** (e.g., Button) on which you want to add the action.

2. Select **Actions** from the Properties panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window. 1. Select the already added **Upload Signature Action**, click on the **+** button at the bottom of the box and select **Add Action**.

   2. On the right side, search and select **Create Document** or **Update Document**.

   3. If you select **Create Document**. 1. Set the **Collection** to your collection name (e.g., todo).

   4. If you select **Update Document**, set the document reference to update. 1. If you have access to the document, set the **Source** to the **actual document** and **Available Options** to **reference**.

   5. Under the **Set Fields** section, click on the **+ Field** button.

   6. Click on the Field name until you see the fields that store the slider value. 1. Set the **Value Source** to **From Variable**.
      2. Click on the **UNSET** (this will open a popup on the left side).
      3. Select the **Widget State** and then select **Uploaded Signature URL**.

   7. **Close** the action flow editor.

#### Clear signature \[Action]

You can allow users to delete the signature if they make a mistake or want to get the perfect signature. You can do this by adding the *Clear Signature* action.

Follow the steps below to define the Action to any widget.

1. Select the **Widget** (e.g., IconButton with canceling or delete icon) on which you want to define the action.

2. Select **Actions** from the Properties panel (the right menu), and click **+ Add Action**. 1. Search and select **Clear Signatures**.
   2. Select the **Signature Fields** from the list below. This helps when you have multiple signature widgets on a page and want to clear only selected one(s).

3. Click **Close**.

#### Customization

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

##### Customizing pen

To change the pen color and stroke width:

1. Select the **Signature** widget from the widget tree or the canvas area.
2. Move to the properties panel, and scroll down to the **Signature** section.
3. Find the **Pen Color** property and click on the box next to the already selected color, select the color, then click **Use Color** or click on an already selected color and enter a Hex Code directly.
4. Find the **Pen Stroke Width** property and enter the value. The higher value increases the thickness of the stroke.

---

### Slider {#slider}

*Learn how to add Slider in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/slider

The Slider widget is used to select a single value from a range of values. You define the min and max value for the slider, and users can choose the value between the specified range by dragging the slider thumb (sliding circle).

For example, you can use the **Slider** widget to allow users to set the volume, set the donation amount, etc.

Widget State

Before diving into form widgets, check out our guide on [**Widget States**](https://docs.flutterflow.io/concepts/state-management/widget-state) to efficiently manage the state and behavior of your form elements.

#### Adding Slider

Let's build an example of using the Slider widget and retrieve its value in a Text widget.

The steps to build the example are as follows:

1. First, add the **Slider** widget from the **Form Elements** tab or add it directly from the widget tree.

2. Now, add the **Text** widget to display the slider value.

3. Keep the **Text** widget selected, Move to the properties panel, and click on the **Set from Variable**. This will open a new panel. 1. Set **Source** to **Widget State**.
   2. Set the **Available Options** to **Slider**. If you add multiple sliders, the names would be like Slider1, Slider2, and so on.
   3. Set the **Number Format Option** if you wish to.
   4. Click **Confirm**.

#### Trigger Action on Change

See how to [trigger an action when a selection changes](https://docs.flutterflow.io/resources/forms/form-triggers#on-selected) on this widget.

#### Setting initial value

Sometimes you might want to display the slider with the default value. For example, showing the volume slider with the audible volume value. You can do so by setting the initial value for the Slider.

#### Customization

You can customize the appearance and behavior of the widget using the various properties available under the properties panel.

##### Setting platform type

You can set the platform type to *Adaptive or Android* for this widget. Selecting the Adaptive type will display the widget in its native style. That means the widget will show iOS-style rendering when running on iOS devices and Android-style rendering when running on Android devices.

To set the platform type:

1. Select the **Slider** widget from the widget tree or the canvas area.
2. Move to the properties panel and open the **Platform** section.
3. Set the **Platform Type** among the **Android** or **Adaptive**.

##### Defining slider range

You can define the slider range by setting the min and max values.

To set the min and max values:

1. Select the **Slider** widget from the widget tree or the canvas area.
2. Move to the properties panel and scroll down to the **Slider Properties** section.
3. Find the **Min** property and enter the value. This will be the start value of the range.
4. Find the **Max** property and enter the value. This will be the end value of the range.

##### Setting step size

By default, you can move and stop the slider thumb at any place on the slider track. To make the slider thumb stop at a specific interval, you can set the step size value.

> **Info:** If the range is not evenly divisible by the step size, the slider thumb will stop at the closest value in the range.

To set the step size:

1. Select the **Slider** widget from the widget tree or the canvas area.
2. Move to the properties panel and scroll down to the **Slider Properties** section.
3. Find the **Step Size** property and enter the value.

##### Changing color

To change the slider colors:

1. Select the **Slider** widget from the widget tree or the canvas area.
2. Move to the properties panel and scroll down to the **Slider Properties** section.
3. To change the active color, find the **Active Color** property, click on the box next to the already selected color, select the color, and then click **Use Color** or click on an already selected color and enter a Hex Code directly. You can also choose the color by clicking the **Palette** and **Simple** button.
4. To change the inactive color, find the **Inactive Color** property, click on the box next to the already selected color, select the color, and then click **Use Color** or click on an already selected color and enter a Hex Code directly. You can also choose the color by clicking the **Palette** and **Simple** button.

##### Showing slider value

You can show the slider value while moving the slider thumb on the track. The value appears as a tooltip above the slider thumb.

To show the slider value:

1. Select the **Slider** widget from the widget tree or the canvas area.
2. Move to the properties panel and scroll down to the **Slider Properties** section.
3. Find the **Show Value** property and turn on the toggle.

---

### Spacer {#spacer}

*The Spacer widget is used to insert a flexible empty*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/spacer

The [Spacer widget](https://www.youtube.com/watch?v=7FJgd7QN1zI) is used to insert a flexible empty space between the children of the Column and Row widget.

![img.png](https://docs.flutterflow.io/assets/images/spacer-0a2253d3f9f18a42a86c74ea3d76474c.png)

If you want even space between your child widgets, you can add space by setting the **Main Axis Alignment** to **Space Around**, **Space Evenly,** and **Space Between.** If you want a more customized space between your child widgets (example below), you should use the Spacer Widget.

> **Info:** The Spacer widget takes all of the available space so the Spacer Widget will have no effect on a Column or Row where the **Main Axis Alignment** is set to **Space Around**, **Space Evenly,** and **Space Between.**

To use the Spacer widget, add it between the children of your Row or Column wherever you like, and set the flex value to a positive whole number. By default, it is set to 1.

![spacer-widget.png](https://docs.flutterflow.io/assets/images/spacer-widget-457ac9a558b9e8844c4cb3e46122937a.png)

Spacer Example

In the example above, we have added two Spacer widgets between the Row children. One is set to 3, therefore taking up three times more space than the other Spacer widget, which is set to 1.

---

### StickyHeader {#stickyheader}

*The StickyHeader widget is a special type of widget that allows the top part of a scrollable list to "stick" or remain visible at the top of a viewport while the rest of the content can be scrolled. As users scroll down, the sticky header remains fixed at the top, providing consistent context or navigation cues.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/sticky-header

The StickyHeader widget is a special type of widget that allows the top part of a scrollable list to "stick" or remain visible at the top of a viewport while the rest of the content can be scrolled. As users scroll down, the sticky header remains fixed at the top, providing consistent context or navigation cues.

For instance, In data-heavy applications where users scroll through large data tables, sticky headers ensure that the column titles are always visible, enhancing usability and readability.

StickyHeader widget in action

The StickyHeader widget consists of two primary sections: the *StickyHeader Header* and the *StickyHeader Content*.

* **StickyHeader Header**: This section contains the widget that remains fixed at the top while scrolling. It is typically used to display headers, titles, or important information that should stay visible at all times.
* **StickyHeader Content**: This section contains the scrollable widget, such as ListView or GridView, that holds the main content. It allows users to scroll through the content while the header remains in place.

Please note

For the StickyHeader widget to work, you must add it inside the scrollable widget, such as Column and ListView, and make them the **Primary** scrollable widget. **Note**: When you add it inside the Column, make sure you make the column **scrollable**. This enables the desired behavior of the header to stick at the top while the content scrolls.

![img\_1.png](https://docs.flutterflow.io/assets/images/img_1-f80cacf0889a64d442e5907793c4005c.png)

StickyHeader sections

#### Adding StickyHeader widget

Let's see how you can use the StickyHeader widget as a replacement for the **AppBar** by building an example that contains a search bar as a sticky header.

Here's how it looks:

Using a search bar as a sticky header widget

Here are the steps to build such an example:

1. First, ensure you have a Column widget on a page. if not, add it. Also, make the Column widget **scrollable** and **Primary**.
2. Add the **StickyHeader** widget from the **Base Elements** tab.
3. Inside the **StickyHeader Header**, add a widget that you want to stay at the top when scrolling. For this example, it's the search bar.
4. Inside the **StickyHeader Content**, add the **ListView > Container** widgets to display a list of users.
5. Query and display a list of users in a ListView.

#### Another example

When displaying a long list with categorized sections, such as a contacts list with alphabetical sections (A, B, C...), you can use the `StickyHeader` widget to keep the section headers (e.g., letters) visible as users scroll through the contact list.

The aim is to generate StickyHeader widgets corresponding to each letter. Inside each StickyHeader, display contacts matching its starting letter. By dynamically generating StickyHeader widgets per letter, we can provide a structured view with grouped contacts.

Here's how it looks when completed:

Contact list page using StickyHeader widget

Here are the steps to build such an example:

1. Prepare a list of letters starting from A-Z. You can use the `AppState` variable for this.

![img\_2.png](https://docs.flutterflow.io/assets/images/img_2-c110529846ac9814ffd79fbdfffc630f.png)

2. Prepare a list of contacts.

![img\_3.png](https://docs.flutterflow.io/assets/images/img_3-cb5b5453c62028011d19f823b3e07cd9.png)

3. Add the **ListView > StickyHeader** widgets.

   1. In ListView, generate dynamic children from a variable that holds the letters.
   2. Inside the `StickyHeader` section, add a widget to display the current letter.

4) Now, inside the *StickyHeader* *Content* section, add the **ListView** with a **Container** inside to display the list of matching contacts.

   1. On this ListView, generate dynamic children from a variable that holds all the contacts. But while doing so, filter the list and extract only matching contacts using [Inline Function](https://docs.flutterflow.io/resources/functions/utility#inline-function-code-expressions).
   2. Now you can display the contact's details, such as name, inside the UI.

---

### SwipeableStack {#swipeablestack}

*Learn how to add SwipeableStack widget in your FlutterFlow project.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/swipeable-stack

The SwipeableStack is a widget designed to stack cards or content layers that users can swipe in any direction. It is commonly used in dating apps like Tinder for profile browsing.

#### Adding SwipeableStack widget

To add a Stack widget:

1. Open the [Widget Palette](https://docs.flutterflow.io/flutterflow-ui/widget-palette) and locate the **SwipeableStack** widget under the **Layout Elements** tab. You can drag it into your desired location or add it directly from the widget tree or canvas area.
2. By default, it adds four cards and is represented as **SwipeableStack Page**. To see another page in the canvas, move to the **Properties Panel >** set the **Active Page** to the card you want to see.
3. To add a new card, move to the **Properties Panel > Active Page >** click **+ Add Page**.
4. To delete any card, select the **SwipeableStack Page** (which you want to delete) from the widget tree or the canvas area and press the **Delete** key on the keyboard.
5. By default, SwipeableStack Page contains an Image widget; however, you can customize it as per your requirement. For example, if you want to create a Tinder like user experience, you could wrap (`⌘` + B) the default image widget inside the Stack widget and then add some more widgets.

#### Swipe card on the button press

You might want to allow users to swipe the cards with a button press—for instance, swiping a card left through an 'unlike' or 'reject' button, and right with a 'like' or 'accept' button.

Here's how you can swipe the card with a button press:

1. First add the [SwipeableStackwidget](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/swipeable-stack#adding-swipeablestack-widget).
2. Add a couple of buttons inside.
3. Now, [add the Control SwipeableStack action](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/swipeable-stack#control-swipeable-stack-action).

#### Get notified on swipe

You might want to get a callback when the child widget (e.g., card) gets swiped and then add further actions. For example, updating the item (like or unlike flag) in the backend based on the swipe type (left or right).

Here is how you can get a callback when the child widgets get swiped:

1. Select the **SwipeableStack** widget.
2. Select **Actions** from the Properties panel and open **Action Flow Editor**.
3. Select the swipe type (among the **OnWidgetSwipe, OnLeftSwipe, OnRightSwipe, OnUpSwipe, On Down Swipe**) on which you would like to get a callback. If the swipe direction is not important to you, select **On Widget Swipe**.
4. Now you can add any action that will be triggered upon receiving the selected callback—for example, showing the Snackbar message on swipe.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

##### Loop cards

To loop the cards in SwipeableStack, move to the **Properties Panel > SwipeableStack Properties >** turn on the **Loop** toggle.

![loopcard](https://docs.flutterflow.io/assets/images/loopcard-c521cf860905090a85c97a048b081aa5.avif)

##### Allowed Swipe Direction

You can control the directions in which users can swipe cards by adjusting the **Allowed Swipe Direction** property. It enables you to customize how users interact with the SwipeableStack, letting you limit swipes to certain directions or enable swiping in any direction.

To do so, navigate to the **Properties Panel > SwipeableStack Properties > Allowed Swipe Direction**, and select one of the following options:

* **All**: Users can swipe in all directions.
* **Left**: Swipe only to the left.
* **Right**: Swipe only to the right.
* **Down**: Swipe only downward.
* **Up**: Swipe only upward.
* **Vertical**: Swipe up or down.
* **Horizontal**: Swipe left or right.

For example, in Tinder-like Swipeable Cards layout, you can set the **Allowed Swipe Direction** to **Horizontal**, enabling users to swipe left to "dislike" and right to "like" a profile.

![allowed-swipe-direction.png](https://docs.flutterflow.io/assets/images/allowed-swipe-direction-fa49e6decdd522be89636cc3116b25cf.png)

##### Customize card display count and scale

You can adjust how many cards are visible in the stack at one time and how they are scaled. This customization enhances the UX by letting you create a more engaging and visually appealing card stack, where the depth and hierarchy of cards can be easily perceived by users.

To do so, move to the **Properties Panel > SwipeableStack Properties >** enter the value in **Card Display Count** and **Next Card Scale**. For *Next Card Scale,* experiment with values ranging from 0.9 to 0.99 to achieve the desired visual effect.

##### Change swipe threshold

A "threshold" typically refers to the sensitivity of swipe gestures. It determines how much a user needs to swipe a card for it to be considered a complete swipe action. It accepts value between 0 and 1; the threshold set closer to 1 requires the user to swipe or drag the card further across the screen to trigger a swipe action.

To do so, move to the **Properties Panel > SwipeableStack Properties >** enter the value in **Swipe Threshold** property.

##### Set card swiping angle

You can control the tilt or rotation effect of cards as they are swiped. The *Max Angle* property allows you to set the maximum rotation angle a card can reach during a swipe gesture.

To do so, move to the **Properties Panel > SwipeableStack Properties >** enter the value (0-360) in **Max Angle** property.

##### Change back card offset

You can control how the subsequent cards are visually offset relative to the top card, creating a layered effect. This enhances the visual depth and appeal of the card stack within the app.

To change the offset of the back cards move to the **Properties Panel > SwipeableStack Properties > Back Card Offset >** enter the values in **Horizontal** and **Vertical** boxes.

***

#### Control Swipeable Stack \[Action]

Using this action, you can swipe the widgets inside the SwipeableStack widget. For example, swiping the card left or right with the tap of a button.

##### Types of card swipe

There are the following types of card swipes you can add:

* **Trigger Left Swipe**: Moves the current card from right to left.
* **Trigger Right Swipe**: Moves the current card from left to right.
* **Trigger Up Swipe**: Moves the current card upwards from bottom to top.
* **Trigger Down Swipe**: Moves the current card downwards from top to bottom.

---

### Tooltip {#tooltip}

*The Tooltip widget provides additional information or visual cues of a widget in a small popup box. It appears when the user taps or long-presses the widget or hovers over it. It's typically used to provide an explanation about the function of a widget.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/tooltip

The Tooltip widget provides additional information or visual cues of a widget in a small popup box. It appears when the user taps or long-presses the widget or hovers over it. It's typically used to provide an explanation about the function of a widget.

> **Info:** It is not frequently used on touch devices where tapping or long-pressing can initiate other actions. But they can be incredibly useful in the desktop environment where hover functionality is available.

![tooltip.png](https://docs.flutterflow.io/assets/images/tooltip-0ef2d763bc6f64243f713d5c1c530220.png)

#### Adding Tooltip widget

To add the *Tooltip* widget to your app:

1. Identify the widget you want to provide a description for and right-click on it. Select **Wrap Widget** and then select **Tooltip** widget.
2. Now select the **Tooltip** widget, move to the **Properties Panel > Message > Text**, and enter the message you want to display.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the Properties Panel.

##### Component as Tooltip

Sometimes, you may want to display more than just text in a tooltip—such as images, icons, buttons, or other custom components. For example, in an e-commerce app, a tooltip could show a detailed breakdown of customer reviews when users hover over the overall rating.

To achieve this, simply set the **Tooltip Type** to **Component** and select the custom component you'd like to display.

To display dynamic content in tooltips, you can create a wrapper component that accepts a [**WidgetBuilder**](https://docs.flutterflow.io/resources/ui/components/widget-builder) as a parameter and use this component within the tooltip.

Here’s exactly how you do it:

##### Change trigger mode

On touch devices, the *Tooltip* opens on tap. To make it open on long press instead, use the **Trigger Mode** property.

##### Show Tooltip on Focus

The **Show Tooltip on Focus** toggle controls whether the tooltip is displayed when the child widget receives keyboard focus. This is particularly useful for improving accessibility and keyboard navigation, as it ensures users see helpful information when they tab through form fields, interactive elements or any important information.

![tooltip-on-focus](https://docs.flutterflow.io/assets/images/tooltip-on-focus-1e2b4249df8108342df62a4ea8d69523.avif)

##### Change tooltip alignment

By default, the *Tooltip* appears below the target widget. You can change this setting using the **Preferred Direction** property. This allows you to open the Tooltip **Above**, **Left,** and **Right** directions in addition to the **Below**.

##### Customize tail size

To change the tail's size, you can use the **Tail Width** and **Tail Length** properties.

##### Changing background color

You can change the Tooltip's background color using the **Background Color** property.

![tooltip-bckgrnd.png](https://docs.flutterflow.io/assets/images/tooltip-bckgrnd-2b518112d20901711080da59327256da.png)

##### Set tooltip offset

By setting the tooltip offset, you can adjust the space between the tooltip and the target widget. To do so, move to the **Properties Panel >** set the **Offset** value.

![tooltip-offset.png](https://docs.flutterflow.io/assets/images/tooltip-offset-529df1e8b721d43198f546967572f525.png)

##### Customize border radius

To change the rounded corner of the Tooltip widget, move to the **Properties Panel >** set the **Border Radius** property.

![radius.png](https://docs.flutterflow.io/assets/images/radius-e3cc8f869e0ad07b580e37adc4592767.png)

##### Elevate tooltip

To add a shadow or to create a sense of depth on this widget, you can use the **Elevation** property. It allows a widget to stand out, making it appear like it's floating above the surface of the UI, ultimately making the tooltip more noticeable.

![elevate-tooltip.png](https://docs.flutterflow.io/assets/images/elevate-tooltip-3fffcfff953b0324ad25a7c1259ba90a.png) toolt

##### Set internal padding

In case you want to add some space around the tooltip message, navigate to the **Properties Panel >** set the **Padding** property.

![internal-padding.png](https://docs.flutterflow.io/assets/images/internal-padding-2a4ac4b4e9f7886f70bb660b07701921.png)

##### Change wait duration

The wait duration specifies the amount of time that the Tooltip widget waits before it displays. To change this setting, move to the **Properties Panel >** set the **Wait Duration** value.

##### Change show duration

The show duration specifies the duration for which the Tooltip widget continues to be displayed on the screen, even after the user has navigated away from it. As a best practice, it's often recommended to set this value to zero. This ensures that the tooltip disappears instantly once the user navigates away.

To change the default duration, move to the **Properties Panel >** set the **Show Duration** value.

---

### Transform {#transform}

*The Transform widget applies graphic transformations such as skew (or tilt), rotate, scale, and translate (or slide) to its child widget. You could use this widget in combination with animations to build visually engaging apps.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/transform

The `Transform` widget applies graphic transformations such as skew (or tilt), rotate, scale, and translate (or slide) to its child widget. You could use this widget in combination with animations to build visually engaging apps.

![transform.png](https://docs.flutterflow.io/assets/images/transform-aabf5d89972f979388a475a22f597383.png)

#### Adding Transform widget

To add a Transform widget to your app:

1. First, click on the **+ Add Widget**, drag the **Transform** widget from the **Base Elements** tab, or add it directly from the widget tree.

2. Add a child widget inside the Transform widget that you want to transform.

3. By default, the transformation applied to a child widget is the **Skew** transformation. This type of transformation allows you to tilt the child widget, i.e., top and bottom or the left and right sides no longer remain to be parallel. To add/customize tilt to the child widget:

   1. Select the **Transform** widget and move to the properties panel.
   2. To add tilt in the horizontal direction, find the **Skew X** property and use the slider or directly enter the value into the box. The positive value will move the top side to the left and the bottom side to the right.
   3. To add tilt in the vertical direction, use the **Skew Y** property. The positive value will move the left side in an upward direction and the right side in a downward direction.
   4. The negative value will move the sides in the opposite direction.

4. Optional: To change the position of the origin (a center of the transform widget), you can use the **Transform Orgin and Alignment** options.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel).

##### Changing transform type

To change the transform type, select the **Transform** widget, move to the properties panel, find the **Transform Type** dropdown and choose the desired one.

* For **Scale** type, use the **Scale X** property to increase or decrease the size in the horizontal direction. Use the **Scale Y** property to change the size in the vertical direction. For example, If you enter 0.5, it will make the widget half the size, whereas value two will make the widget twice its size.

- For **Rotate** type, use the **Rotate (degree)** property to turn the widget. The value must be in degrees (i.e., 0 to 360). By default, the widget rotates in a clockwise direction. To turn the widget anticlockwise, enter the negative value.

* For **Translate** type: * Set the **Translate X** property to slide the widget in horizontal direction. The positive value will move the widget in the right direction, whereas the negative value will move in the left direction.
  * Set the **Translate Y** property to slide the widget in the vertical direction. The positive value will move the widget in a downward direction, whereas the negative value will move in an upward direction.

---

### Button {#button}

*The Button widget is a fundamental component in user interface design, utilized extensively across web and mobile applications. It serves as a primary means of user interaction, allowing users to execute actions or commands within an application. Buttons are essential for:*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/button

The Button widget is a fundamental component in user interface design, utilized extensively across web and mobile applications. It serves as a primary means of user interaction, allowing users to execute actions or commands within an application. Buttons are essential for:

* **Initiating Actions:** Whether it's submitting a form, opening a new page, or performing any operational task, buttons trigger these functionalities.

* **User Feedback:** Buttons often change visually in response to user actions—like hover effects, changes in color on click, or disabled states—providing immediate visual feedback that confirms an action has been recognized.

* **Navigational Purposes:** Buttons can guide users through a site or application, such as moving to the next page of a form or returning to the home page.

* **Enhancing User Experience:** Well-designed buttons are crucial for creating a smooth and intuitive user experience. They are designed to be easily recognizable and accessible, facilitating a seamless interaction by clearly communicating their function.

When you add a Button widget to your Page or Component and select it, the Properties Panel on the right displays various properties and functionalities:

Some significant properties are illustrated below:

##### Button Default Styling Settings

Define the initial appearance of your button, including its size, color, border, and padding. These settings determine how the button looks under default conditions.

![button.png](https://docs.flutterflow.io/assets/images/button-1fe4d0fc73df7d0734e49fd89437a0d2.png)

##### Button Disabled & Hover Settings

Customize how your button appears when disabled or when a user hovers over it. These settings allow you to alter the button's color, border, and elevation to indicate its state visually.

![button-disabled.png](https://docs.flutterflow.io/assets/images/button-disabled-799361e254ccd5c50136ed53437068f4.png)

Additionally, you can define the style of the text inside the Button and, if enabled, the style of the Icon within the Button.

---

### Composing Widgets {#composing-widgets}

*In FlutterFlow, creating a complex user interface often involves combining simpler widgets into more intricate layouts. While atomic widgets like Text, Button, Image, and Icon form the building blocks of your UI, you’ll use molecular widgets like Row, Column, and Stack to arrange these atomic widgets into a structured layout.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/composing-widgets

In FlutterFlow, creating a complex user interface often involves combining simpler widgets into more intricate layouts. While atomic widgets like **Text, Button, Image**, and **Icon** form the building blocks of your UI, you’ll use molecular widgets like **Row**, **Column**, and **Stack** to arrange these atomic widgets into a structured layout.

As you grow more comfortable with these, you can advance to using **Lists** and **Grids** for even more dynamic and complex compositions.

#### Molecular Widgets: Row, Column, and Stack

To start composing more sophisticated interfaces, FlutterFlow provides essential molecular widgets like **Row, Column**, and **Stack**. These widgets allow you to control the arrangement of atomic widgets within your app.

* **Row:** This widget aligns its children horizontally in a single line, from left to right. It's useful for creating layouts where elements need to be placed side by side, such as icons with labels or buttons in a toolbar.

* **Column:** This widget aligns its children vertically, from top to bottom. It's perfect for creating lists of items or laying out sections of a page vertically.

* **Stack:** This widget allows for overlapping widgets by placing them on top of each other. It’s ideal for creating layered effects, like placing text over an image or adding a badge to an icon.

![row-col-stack.png](https://docs.flutterflow.io/assets/images/row-col-stack-43692a7d10f09d07ddb08295cc2b1055.png)

> **Info:** Learn more about how to compose widgets with **[Row, Column & Stack](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/rows-column-stack)**.

#### Advanced Composition: Lists & Grids

As you become more familiar with using molecular widgets like **Row**, **Column**, and **Stack**, you can begin working with **Lists** and **Grids**. These widgets are specifically designed to handle large sets of data or dynamic content, making them essential for more complex layouts.

* **Lists:** While a `Column` is useful for stacking a few items vertically, a `ListView` is designed to handle potentially infinite items by allowing the content to scroll. This makes it ideal for things like a chat app, news feed, or any list that can grow beyond the screen size. One of the key advantages of using a ListView is also its built-in support for **lazy loading**.

Lazy Loading

Lazy loading means that the `ListView` only builds and renders the items that are currently visible on the screen. As the user scrolls, `ListView` dynamically loads additional items just in time. This significantly improves performance, especially when dealing with long lists of data, by conserving memory and processing resources.

* **Grids:** A GridView organizes items into a two-dimensional grid. It's perfect for displaying items like photos, products, or any other type of content that benefits from being presented in a grid format, making it visually appealing and easy to navigate.

List & Grids

Learn about the advanced properties of **[Lists & Grids](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid)**.

---

### Generate Dynamic Children {#generate-dynamic-children}

*Widgets capable of handling multiple child widgets have an additional functionality called*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/generate-dynamic-children

Widgets capable of handling multiple child widgets have an additional functionality called Generate Dynamic Children that helps you generate multiple child widgets from a `List` variable.

This is particularly useful when you are retrieving data from an API call, Firebase Query, or a State variable that holds a List of items.

Some of the widgets that can handle multiple children include **[Column, Row, Stack](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/rows-column-stack), [ListView, GridView](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid),** and **[PageView](https://docs.flutterflow.io/concepts/navigation/pageview)**.

In the following example, we will use an `AppState` called `categoryList` that holds a List of Product Categories and set the variable to the categoryList widget that is a ListView.

> **Note:** In the demo app, we have predefined custom `DataTypes`. One such DataType is "**Category**," which includes the fields `categoryImg` and `categoryName`. In our App State, **categoryList** is a `List<Category>` that holds multiple Category objects. We use this list variable as the value source for our `ListView` widget.

The value is stored in a variable (in this example, `allCategoriesList`) and can be used to populate any scrollable view. In our example, we populate the `ListView` widget, which creates multiple instances, each holding a Column with a circular Container and Text.

What are Instances?

Learn about **[Instances](https://docs.flutterflow.io/resources/ui/overview#classes-vs-instances)** and how it compares with **Classes** in this [**document**](https://docs.flutterflow.io/resources/ui/overview#classes-vs-instances).

To make changes, you need to **modify only the first child** and set the variable sources to the first child widgets. These changes will be applied to all children widgets in the `ListView`. The number of children will match the length of the List variable unless you have set a limit in the **Max Items** option under the **Generating Dynamic Children** tab.

Let's see a quick demo to set the variable source of the first child widgets:

---

### Lists & Grids {#lists-grids}

*In FlutterFlow, ListView and GridView are versatile widgets designed for displaying lists and grids*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid

In FlutterFlow, `ListView` and `GridView` are versatile widgets designed for displaying lists and grids of elements, respectively. Both are highly customizable and optimized for dynamic content displays, making them essential for any app that requires scrolling through a collection of items such as images, text, or interactive elements.

#### ListView Widget

ListView is a scrollable list of widgets arranged linearly. It is ideal for scenarios where items need to be displayed one after another, either **vertically or horizontally**.

It is particularly useful for long lists that need to be efficient; only the items visible on the screen are rendered, enhancing performance for lists with a large number of elements.

You can customize the ListView properties and functionalities, some are as follows:

##### Axis

Axis sets the orientation of the ListView. You can select either "Vertical" or "Horizontal" depending on whether you want the list to scroll vertically or horizontally.

![listview-axis.png](https://docs.flutterflow.io/assets/images/listview-axis-9b98370a7ac7fe23dc7df200f0a8c10c.png)

##### Spacing

* **Items Spacing:** This defines the space between individual items in the ListView. You can specify the spacing in pixels.

Items Spacing vs Padding

Prefer “Items Spacing” set on the parent row or column instead of padding on individual elements. This ensures consistency, especially on non-dynamically generated lists.

* **Apply to Start & End:** When enabled, the item spacing will also be applied to the start and the end of the ListView, adding a margin at the beginning and end of the list. This effectively adds padding at the start and end of the layout in addition to between the items.

* **Start Spacing and End Spacing:** These properties allow you to set additional spacing at the start and end of the ListView, respectively. This can be used to create padding around the list items that is separate from the spacing between the items.

##### Advanced Functionalities

* **Shrink Wrap:** When this property is enabled, the ListView will size itself to the total size of its children, meaning it won’t take more space than necessary. This is useful for lists that do not need to be scrollable because they fit within their constraints.

* **Primary:** If set to true, the ListView will act as the primary scrolling view in the context. This usually affects how the view interacts with other scrolling views and whether it stretches to fill the viewport. [**See more info here**](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#primary-property).

* **Reverse:** In lists, when the reverse property is enabled, it reverses the order in which items appear in the ListView. For a vertical list, this means starting from the bottom and for a horizontal list, starting from the right.

![listview-reverse.png](https://docs.flutterflow.io/assets/images/listview-reverse-87c139dec023d5c05aec91c5c21e0735.png)

##### Reorderable List

Whether to allow reordering of items in the list. On Web or Desktop this will add drag handles, but on mobile the reorder is triggerred by long pressing an item.

Note

This will not automatically persist the order of items in the list, but instead lets you define an action under **"On Reorder**" action trigger to make any necessary changes yourself.

CONTENTs of a Reorderable List

**Reorderable ListView** must have dynamic children otherwise enabling this will throw an error.

Here's a quick tutorial to set up your Reorderable ListView:

###### Using App State variable

1. First, create an app state variable with a few items of type String and display them on the ListView widget.

2. Then, select the ListView, head over to the **Properties Panel > ListView Properties**, and enable the **Reorderable** property.

3. Select Actions from the properties panel (the right menu), and open the **Action Flow Editor.**

4. You'll see an **On Reorder** action trigger. Actions under this are triggered when a user completes repositioning an item in the UI. But, we also need to update the item position in the actual list as well. To do so, we can create a custom action that will modify the item index in the list.

   1. Create a custom action with three arguments that accept the actual list, old index, and new index. Tip: You'll get the old and new index from Set Variable menu > Reorderable ListView.
   2. Here's the custom code with explanation

```
// Define a function called reorderItems that returns a Future of a list of strings.
// It takes in a list of strings, an old index, and a new index as parameters.
Future<List<String>> reorderItems(
List<String> list,
int oldIndex,
int newIndex,
) async {
// If the item is being moved to a position further down the list
// (i.e., to a higher index), decrement the newIndex by 1.
// This adjustment is needed because removing an item from its original
// position will shift the indices of all subsequent items.
if (oldIndex < newIndex) {
newIndex -= 1;
}

// Remove the item from its original position in the list and store
// it in the 'item' variable.
final item = list.removeAt(oldIndex);

// Insert the removed item into its new position in the list.
list.insert(newIndex, item);

// Return the modified list.
return list;
}
```

5. The custom action returns the modified list, which you can use to update the actual list using the update app state variable action.

###### Reordering Items in a Firebase Query

If you want to reorder the list items retrieved via Firebase query collection, the steps are almost similar except for the following changes.

Caution

Reordering items in a Firebase query is only suited for smaller lists. For larger datasets, this method can be inefficient and might lead to performance issues. Additionally, frequent writes and updates to Firebase can increase costs significantly.

1. Create 'order' field in the collection.
2. Query collection order by 'order' field.
3. Ensure that the Infinite scroll is disabled.
4. Replace the custom action code with the below one:

```
Future reorderFirebaseItems(
  List<PlaylistRecord> list,
  int oldIndex,
  int newIndex,
) async {
  // If the item is being moved down the list, we adjust the newIndex.
  if (oldIndex < newIndex) {
    newIndex -= 1;
  }

  // Remove the item from its current position in the list.
  final PlaylistRecord item = list.removeAt(oldIndex);
  
  // Insert the item into its new position.
  list.insert(newIndex, item);

  // Create a batch to combine multiple Firestore operations into one.
  final batch = FirebaseFirestore.instance.batch();

  // Iterate through the list and update the order field for each document in Firestore.
  for (int i = 0; i < list.length; i++) {
    final PlaylistRecord doc = list[i];
    // Update the 'order' field of the document with its new index. 
    // This assumes that you have an 'order' field in Firestore where you store the order of the items.
    batch.update(doc.reference, {
      'order': i
    }); 
  }

  // Commit all the batched operations to Firestore.
  return await batch.commit();
}
```

#### ListTile widget

The `ListTile` widget is a versatile component designed for displaying rows in a list, commonly used for menus, drawers, and lists where each row consists of multiple elements aligned horizontally. `ListTile` is particularly useful when you need a standardized row layout that includes elements a main title, a subtitle, and interactive icons at the start or end of the row. It saves time compared to constructing custom row layouts from scratch while ensuring visual consistency.

When to Use ListTile Over Custom Components

ListTile should be used when you require a simple, effective layout with standard elements and interactions. It is ideal for:

* Lists where items have a uniform structure.
* Quick assembly of functional interfaces without needing complex customization.
* Scenarios requiring integrated touch feedback and accessibility features which ListTile provides by default.

You can customize the Title (Text), Subtitle (Text) and Icon properties from the Properties Panel

![list-tile.png](https://docs.flutterflow.io/assets/images/list-tile-20d6ffe0e8f7e0dbcc14be9a912a365d.png)

> **Info:** To learn about how to customize the Text widgets in this component, refer the [**Text widget**](https://docs.flutterflow.io/resources/ui/widgets/text).

##### Convert into SlidableListTile

The ListTile in FlutterFlow offers an additional functionality—it can easily be transformed into a slidable version. This enhanced ListTile allows you to embed actions that users can access by sliding the tile to the left, adding a layer of interactivity and utility to the standard list item.

Here's how you can enable the Slidable functionality of a ListTile and modify the properties of the Actions:

#### GridView Widget

GridView provides a two-dimensional array of children. It is the widget of choice when you need to display items in a grid pattern, like a photo gallery or a board game layout.

Like [ListView](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#listview-widget), GridView only renders the visible items, making it efficient for displaying large collections of elements. GridView supports multiple configurations for column count, spacing, aspect ratio, and scroll directions, offering robust customization options for diverse layout needs.

![gridview.png](https://docs.flutterflow.io/assets/images/gridview-4dd3fbd31bc4dba1a1cca05e4992c86d.png)

Here's a quick demo to show how to add a GridView widget and modify its properties:

##### Staggered View

Grid View vs Staggered View

**GridView** and **StaggeredView** are similar widgets in FlutterFlow, with the main difference being the layout and sizing of their children. GridView arranges its children in a fixed-size grid, while StaggeredView allows for variable-sized children, creating a more flexible and dynamic layout. StaggeredView is ideal for layouts with items of varying sizes. For example, it can be used to create a layout similar to the Pinterest app.

![staggeredView](https://docs.flutterflow.io/assets/images/staggeredView-bda380985a09f3a676211368bdb80f0c.png)

##### Advanced Functionalities

* **Shrink Wrap:** By default, the GridView widget takes up all the available space in its main axis. That means if the Axis property is set to Vertical, GridView will occupy all vertical space on the screen. Similarly, if the Axis is set to Horizontal, then GridView will reserve all the horizontal space.

* **Primary:** When set, this indicates whether the GridView is the primary scrollable widget in the layout. A primary GridView handles the scroll interactions, usually necessary when there's only one scrolling view in the viewport. [**See more info here**](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#primary-property).

Video Tutorial

If you prefer watching a video tutorial, here's the one for you:

#### Adding infinite scroll

The infinite scroll automatically loads the new items as you scroll down the list. It works by showing only a limited number of items (e.g., 15, 25) at first and loads subsequent items before the user reaches the end of the list. At the end of the list, a circular progress bar is visible as the new items are loaded.

![Infinite scroll behind the scene](https://docs.flutterflow.io/assets/images/infinite-scroll-behind-scene-fa69e91aa71918d1aa8713d475819c50.avif)

Adding infinite scroll helps you improve the user experience by reducing the initial waiting time (as without infinite scroll, it would take more time to load the long list) and loading new items only when required.

The infinite scroll can be added to the list of items retrieved from two sources:

* [Infinite scroll on a list from the Firestore collection](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#infinite-scroll-on-a-list-from-the-firestore-collection)
* [Infinite scroll on a list from API call](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#infinite-scroll-on-a-list-from-api-call)

##### Infinite scroll on a list from the Firestore collection

In FlutterFlow, you can directly enable the infinite scroll on a list of items received from the Firestore collection.

To enable the infinite scroll:

1. [Query a collection](https://docs.flutterflow.io/resources/backend-query/query-collection) on a ListView (skip if you have already done so).
2. Select the ListView, move to the properties panel and, select the **Backend Query** section.
3. Scroll down the already added query and **turn on** the **Enable Infinite Scroll**.
4. On enabling the infinite scroll, the **Listen For Changes** property also gets enabled. That means the list automatically updates if changes are made to the item. This is done to keep all the items up to date on the screen. However, it does not update the list if any new item is added or deleted. In rare cases, you would need to disable this feature. To do so, turn off this property.
5. In infinite scroll, the items are loaded in chunks called pages. The number of items to load on a single page is determined by the **Page Size** property. By default, the value is set to 25 (i.e., load 25 items per page). The ListView loads the first page as soon as it is visible on the screen, and the subsequent pages (with the number of items defined in the Page Size property) are loaded as you scroll down the screen. You can adjust this value according to your design and requirements.
6. Click **Save**.

##### Infinite scroll on a list from API call

To add an infinite scroll on the API call, you must have an endpoint that supports pagination with at least one query parameter that accepts a page number like page, offset, etc.

###### Pagination Variables

When you add the paginated API call in the builder and enable the infinite scroll, we provide you the following pagination variables that you can pass to your API variables. These will be available inside the **Set Variable** menu.

![Pagination Variables](https://docs.flutterflow.io/assets/images/pagination-variable-74b3bf4532bd715de1bc806ab48a6a57.png)

1. **Next Page Index**: You can pass this variable for the query parameter that accepts the page number. The default value is 0 and keeps increasing by one as you scroll down the list until it reaches the end.
2. **#(Number of) Loaded Items**: This equals the number of items returned by the paginated API call.
3. **Last Response**: This is useful if you want to get anything from the last response that might help you retrieve the next set of data.

> **Tip:** When passing the *Number of Loaded Items* for query parameters like *limit*, *per\_page*, *size,* etc., use a *Specific Value,* such as 15,20.

Adding infinite scroll includes:

1. [Add paginated API call](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#1-add-paginated-api-call)
2. [Passing pagination variable in API call query](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#2-passing-pagination-variable-in-api-call-query)

###### 1. Add paginated API call

The paginated API is the API that returns the result in chunks. Most of the paginated API requires you to add the query parameters to know how many items to retrieve and from where to start.

For example, this API call <https://reqres.in/api/users?per_page=20&page=1> requires `per_page` parameter that specifies 20 items to load per page, and `page` parameter tells to start from the first page. This is called page-based pagination.

See [how to add the paginated API](https://docs.flutterflow.io/resources/backend-logic/rest-api#passing-query-parameters) call by adding query parameters.

###### 2. Passing pagination variable in API call query

This step includes adding the ListView -> ListTile widget and querying the paginated API call.

1. First, query and show data from API calls.
2. While querying the API call, pass the query parameter value from the pagination variable.

#### Primary property

When this property is true and even if the content inside the scrollable widget, such as ListView, or GridView, doesn't overflow the visible area, the user can still attempt to scroll it. The content might move slightly and then bounce back, especially noticeable on iOS with the bounce effect.

> **Tip:** In situations where you have multiple scrollable widgets nested within each other, only one should typically be set as primary.

In most cases, the outermost scrollable widget (usually the one that takes up the most space or the full screen) is set as primary, while inner scrollables are not. For example, when you have a widget structure like this Column > ListView, you should keep the Column as primary and ListView as non-primary.

![img\_2.png](https://docs.flutterflow.io/assets/images/img_2-c110529846ac9814ffd79fbdfffc630f.png)

#### Pull to Refresh on ListView or GridView

If you've enabled the Single Time Query for a Backend Query in a scrollable widget, it won't refresh the list when items are updated in the backend. To address this, add a pull-to-refresh feature.

This user interface pattern allows users to manually refresh content by pulling down the content area, such as a list. When pulled down sufficiently and released, the app will refresh, fetching the latest data or updates.

To enable pull to refresh:

1. Select your scrollable widget, such as `ListView`, `GridView`, or `StaggeredView`.
2. Move to the properties panel and select the **Backend Query**.
3. Open the already added query (e.g., Query collection or API call) and make sure the **Single Time Query** is enabled.
4. Switch on the **Enable Pull to Refresh** toggle. This will automatically add the **Refresh Database Request** action on a pull to refresh gesture.

#### Scroll To \[Action]

Using this action, you scroll the scrollable widget to the beginning or end.

> **Info:** Before adding this action, make sure you have a scrollable widget, such as a **ListView, StaggeredView**, or **GridView**, with enough items to enable scrolling.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., FloatingActionButton) on which you want to add the action.
2. Select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.
3. Search and select the **Scroll To** (under *Widget/UI Interactions*) action.
4. Set the **Scrollable Widget to Control** to the **name** of the scrollable widget (e.g., ListView) added to your page.
5. Set the **Scroll To** either **Beginning** (to scroll to the start) or **End** (to scroll to the end) of the list.
6. Specify the **Duration** in milliseconds (i.e., 1000ms = 1 second). This determines how long the scroll animation will take to complete. **Tip:** If you expect the list to be extensive, consider setting a shorter duration.

---

### Rows, Column & Stack {#rows-column-stack}

*In Flutter, Rows, Columns, and Stacks are fundamental layout widgets that*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/rows-column-stack

In Flutter, `Rows`, `Columns`, and `Stacks` are fundamental layout widgets that help you structure the UI by organizing other widgets in different visual arrangements. Here's how each one works:

* **Row**: A `Row` arranges its child widgets in a horizontal line. This is useful when you want to place elements side by side across the screen.

* **Column**: A `Column` organizes its child widgets vertically, stacking them from top to bottom. This is ideal for placing elements that need to appear in a vertical sequence, such as a list of messages in a chat app or entries in a form.

* **Stack**: A `Stack` layers its child widgets on top of each other, allowing for overlapping elements. In a `Stack`, widgets can be positioned absolutely relative to the edges of the `Stack`, giving you control over the exact location of each element.

Each of these widgets serves different purposes and choosing between them depends on how you need to arrange your UI components:

![row-col-stack.png](https://docs.flutterflow.io/assets/images/row-col-stack-43692a7d10f09d07ddb08295cc2b1055.png)

Minimum Layout Nesting

Use the minimum amount of rows/columns necessary to achieve your layout to avoid unnecessary complexity. No page or component should nest more than 10 levels deep. Reaching this limit likely signals the need for **[converting a part of the widget tree into components](https://docs.flutterflow.io/resources/ui/components/creating-components#convert-to-a-component)**.

#### Common Property: Alignment

##### Main Axis

The main axis is the primary direction in which child widgets are laid out in a `Row` or `Column`.

**Row:** The main axis runs **horizontally**. Child widgets are arranged from left to right.

FlutterFlow allows you to set Row's Main Axis property to the following types:

![row-main-axis.png](https://docs.flutterflow.io/assets/images/row-main-axis-51a849d58cd39f3daaf64557e0845bcb.png)

Row's Main Axis property has the following types: Start, End, Center, SpaceEvenly, SpaceAround, SpaceBetween

**Column:** The main axis runs **vertically**. Child widgets are laid out from top to bottom.

FlutterFlow allows you to set Column's Main Axis property to the following types:

![column-main-axis.png](https://docs.flutterflow.io/assets/images/column-main-axis-cd42d005444cf97750bc8e10eba404aa.png)

Column's Main Axis property has the following types: Start, End, Center, SpaceEvenly, SpaceAround, SpaceBetween

Manipulating the main axis allows you to control how widgets are spaced and how they should expand or align in relation to each other along this primary direction.

##### Cross Axis

The cross axis is **perpendicular to the main axis** and controls the alignment and spacing of widgets across this secondary direction. It has the following types: Start, Center, End.

**Row:** The cross axis runs **vertically**. It determines how child widgets are aligned from top to bottom within the row.

![row-cross.png](https://docs.flutterflow.io/assets/images/row-cross-9645c4fc85c933db44b7be3eca57c44b.png)

Cross Axis types for Row. Main Axis of Row is set to Center.

**Column:** The cross axis runs **horizontally**. It controls how child widgets align from left to right within the column.

![column-cross.png](https://docs.flutterflow.io/assets/images/column-cross-b398b7ef4db1839e86e06f7c581e8c0b.png)

Cross Axis types for Column. Main Axis of Column is set to Center

##### Stack Alignment

For `Stacks`, the concept of main and cross axes is less applicable because widgets are aligned relative to the entire area of the `Stack`. In FlutterFlow you can control the `Stack` children's alignment using the `Stack` property called *Default Child Alignment* which positions the children using `X` and `Y` coordinates.

![stack-align.png](https://docs.flutterflow.io/assets/images/stack-align-691158330abdc58c1e7f1b408fccd82b.png)

Understanding these axes and their properties is essential for effectively designing layouts that behave as expected on different screen sizes and orientations, ensuring a robust and flexible UI.

#### Expansion & Flex (for Row & Column)

When widgets are placed inside a Row or Column in a layout, they gain access to an additional property called **Expansion** & **Flex**. This property controls how a widget behaves in terms of taking up available space within its parent Row or Column.

###### Expanded

The Expansion properties are as follows:

* **Default:** Make the widget NOT fill space along the main axis (horizontal for Row, vertical for Column), therefore taking the minimum space required by its contents.

* **Flexible:** Allow the widget to take up to the available space along the main axis (horizontal for Row, vertical for Column). You can think of this as giving it a "Max Width" equal to the amount of available space. The widget can take up less space if it is smaller, but otherwise will be constrained to the available width.

  Understanding Layouts

  Flexible will be **disabled** if the child widget is in a Row with unbounded width or Column with unbounded height.

* **Expanded:** Make the widget fill the space along the main axis (horizontal for Row, vertical for Column).

Using Expanded & Flexible in an Example

![expanded.png](https://docs.flutterflow.io/assets/images/expanded-eda87a69753adc7cf7fb3649c71c4105.png)

1. **Default Behavior:** Here, you see two child widgets displayed next to each other, each occupying only the necessary space to show its content without any expansion.

2. **Expanded Widget Usage:** The first child widget (highlighted in red) is wrapped with an **Expanded** widget. This causes it to take up all the remaining space in the container after accounting for the space required by the other widgets. Here, the first child stretches to fill all the extra space, pushing the other widgets to the side or shrinking them to their minimum size.

3. **All Expanded Widgets:** In this example, all child widgets are set to **Expanded**. This configuration divides the container's space equally among all child widgets, regardless of their intrinsic size. Each widget stretches to fill an equal portion of the container.

4. **All Flexible Widgets:** In the last example, each child widget is wrapped with a **Flexible** widget. This allows the widgets to expand to fill the available space but unlike **Expanded**, they can also shrink below their allocated space if necessary, based on the flex factors and the minimum space required by each widget. If all have the same flex factor, they will divide the space equally but are able to shrink if the content size demands less space.

Let's understand Flexible concept with another example:

Flexible Concept

![flexible.png](https://docs.flutterflow.io/assets/images/flexible-5eeaab35dab266c5eb63c3af8b47162d.png)

* In the left image, Child 2 (in purple) and Child 3 (in green) retain their intrinsic sizes due to **default settings**, causing their content to appear cut off when the container's width is limited. They cannot adapt to smaller spaces, leading to potential content clipping. This highlights the limitations of default settings in confined spaces where dynamic resizing would improve content visibility.

* In contrast, the right image uses the **Flexible widget** for Child 2 and Child 3, allowing them to adjust dynamically to the container's width constraints. Instead of sticking to their original sizes, these widgets can shrink or expand, making the layout responsive and ensuring content remains visible and well-aligned, regardless of screen size changes. This adaptability is crucial for maintaining accessibility and visual coherence in diverse display environments.

###### Flex

Additionally, you can utilize Flex factors to determine the flexibility of a widget within its parent container. A Flex factor is an integer assigned to a child widget, indicating its proportional size compared to other children in the same parent. The space a child occupies is determined by its Flex factor in relation to the total Flex factors of all siblings in the layout.

Default Behavior

If no flex factor is provided, the child will not expand to fill extra space in the parent container. It will occupy only the space required for its content unless styled otherwise.

When you assign a flex factor, the widget can expand to fill any available space in the parent container. For instance, in a Row or Column, if one widget has a flex factor of 1 and another has a flex factor of 2, the second widget will take up twice as much space as the first.

Flex Example

![flex.png](https://docs.flutterflow.io/assets/images/flex-686dc14f7db4be8620279b395f21bb97.png)

* Child 2 (purple) with a higher Flex factor (8) consistently occupies a larger portion of space, showing how a higher number increases the space allocation relative to other widgets.

* Child 3 (green) has varying Flex factors (1 and 4), illustrating how increasing the Flex factor allows the widget to occupy more space, albeit still less than Child 2 due to its lower Flex factor.

Find a video tutorial about Expanded & Flexible:

#### Scrollability

Scrollability for **Row or Column** widgets in FlutterFlow determines whether the content within these layouts can extend beyond the visible boundaries of the screen or container, enabling horizontal or vertical scrolling:

* **Allow Scrolling:** When enabled, this allows the content to exceed the device or parent container’s screen limits, making the overflow content accessible through scrolling.

* **Do Not Allow Scrolling:** If disabled, the content that exceeds the boundaries of the screen or its parent container will not be accessible through scrolling. This setting forces the content to fit within the available visible space, hiding overflow content or potentially causing layout issues.

Generated Code

In the generated Flutter code, enabling scrollability simply involves wrapping the Row or Column in a `SingleChildScrollView()`. This widget adjusts its child's size and position based on the incoming constraints and the scrolling movement, effectively managing overflow by introducing scrollable behavior.

#### Spacing

* **Items Spacing:** This field sets the space between each child widget within the Row or Column. You can specify a static numerical value that determines the pixel spacing between adjacent children or set it from a variable.

Items Spacing vs Padding

Prefer “Items Spacing” set on the parent row or column instead of padding on individual elements. This ensures consistency, especially on non-dynamically generated lists.

* **Apply to Start & End:** When toggled on, this applies the specified item spacing to the beginning and the end of the Row or Column. This effectively adds padding at the start and end of the layout in addition to between the items.

* **Start Spacing and End Spacing:** These properties allow for additional specific spacing at the start and end of the Row or Column, respectively. This is useful for fine-tuning the layout to ensure content is visually balanced within the container or to provide clear margins.

---

### Container {#container}

*A Container is a highly versatile widget that functions much like a multi-purpose box in your app's*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/container

A Container is a highly versatile widget that functions much like a multi-purpose box in your app's interface. It is primarily used to decorate, position, and arrange child widgets—smaller components within your app. Containers are useful for dividing the screen into smaller, logical parts, and styling or positioning these parts effectively.

For instance, you can use a Container to assign a background color, shape, or specific size to elements like text or buttons. Think of it as placing an item inside a box and then customizing the appearance and placement of that box within the screen layout.

#### Container Properties

The Container properties can be adjusted to customize the appearance and layout of a Container widget. Here's a brief explanation of each:

![container-props.png](https://docs.flutterflow.io/assets/images/container-props-b14a355ea5884fb8ea6cccce91b24908.png)

##### Limiting Size

Sometimes, you don't set the height and width of the container explicitly and allow it to be the size of its child widget. If you do so, you may find layout issues where widgets may become too large or too small on different devices, leading to a poor user experience. To overcome this, you can limit the size of the container by specifying the Min W, Min H, Max W, and Max H.

For example, in a responsive design, you might want a button to grow with the screen size but not exceed a certain width. By setting these properties, you can ensure the button is at least a certain size for usability but doesn't become too large on bigger screens.

* **Min W (Minimum Width) & Min H (Minimum Height):** These set the minimum dimensions the Container can shrink to, in pixels or percentage.

* **Max W (Maximum Width) & Max H (Maximum Height):** These set the maximum dimensions the Container can expand to, in pixels or percentage.

##### Clip Content

Determines whether the content inside the Container should be clipped if it exceeds the boundaries of the Container. When enabled, anything outside the Container's bounds will not be visible.

#### Box Shadow Properties

The Box Shadow properties allow you to add and customize a shadow effect for your Container widget. Here's a brief explanation of each property:

* **Shadow Color:** The color of the shadow, typically specified in a hex format including an alpha value for transparency, like `#33000000.` You can select from Theme Colors, use a color picker, or input a hex code.

* **Blur:** Determines the blur radius of the shadow. A higher value produces a more diffused shadow, while a lower value makes the shadow sharper and more defined.

* **Spread:** Controls the **spread radius of the shadow**. **Increasing** this value will **expand** the area that the shadow covers, making it appear larger.

* **Offset X & Offset Y:** These properties set the horizontal (X) and vertical (Y) displacement of the shadow relative to the widget. **Offset X** shifts the shadow horizontally, and **Offset Y** moves it vertically. Positive values move the shadow right and down, respectively, while negative values move it left and up.

Here's a quick demo to show the box shadow property in Container:

#### Gradient Properties

The Gradient properties allow you to create and customize a gradient effect for a Container widget. Here's an overview of each property:

* **Angle (Degrees):** Sets the orientation of the gradient by specifying the angle in degrees. An angle of **0 degrees** creates a **horizontal** gradient, and **90 degrees** would make it **vertical**.

* **Colors**: These are the colors used in the gradient. You can set these colors using Theme Colors, a color picker, or hex codes. Two color values are added by default.

* **Add Color:** This option allows you to add additional colors to the gradient, further customizing the effect by adjusting their transition points and choosing from Theme Colors, a color picker, or hex codes.

* **Transition Point:** These values determine where each color starts transitioning within the gradient. Transition points are set as a fraction of the total gradient distance:

![gradient-cont.png](https://docs.flutterflow.io/assets/images/gradient-cont-0e1fe8041e4c52c057d37f52b40b072d.png)

In the above example,

* The Transition Point for Color 1 is set at 0, meaning it starts at the very beginning of the gradient.
* The Transition Point for Color 2 is 0.5, indicating that this color starts transitioning at the halfway point.
* The Transition Point for Color 3 is 1, which places the start of this color's transition at the end of the gradient.

#### Background Image Properties

The Background Image properties provide options for setting up an image as the background of a Container widget.

> **Info:** For a detailed guide on configuring **common Image properties**, please refer to the relevant section [**here**](https://docs.flutterflow.io/resources/ui/widgets/image#common-image-properties).

#### Child Properties

* **Child Alignment:** This allows you to specify the alignment of child widgets within the Container. The grid indicates possible positions (center, top, bottom, left, right, and etc), and you can adjust the alignment precisely using the X and Y values, which shift the child widget horizontally and vertically within the Container.

#### Implicit Animated

This property enables the use of implicit animations for changes in the Container’s properties (like size or color). This makes transitions between property changes smoother and visually appealing.

Here's an example of Container's width and color changing without the use of Implicit Animation.

Now we enable **Implicit Animation** for this Container and see the difference:

The properties of Implicit Animation are as follows:

* **Animation Curve:** Specifies how the animation progresses over time. The options are Ease In, Ease in Out, Ease Out, Bounce, Linear, Elastic.

* **Duration (ms):** Sets the duration of the animation in milliseconds. A shorter duration makes the animation faster, while a longer duration slows it down.

#### Safe Area

This toggle ensures that the Container and its contents are positioned within the safe area of the device’s screen, avoiding obscured areas like notches or rounded corners. This is particularly useful for ensuring good visibility and interactivity across different devices.

To enable the safe area, navigate to the properties panel and turn on the Safe Area toggle.

![safe-area.png](https://docs.flutterflow.io/assets/images/safe-area-f1ada35c9f8ace795a889f0e27999a84.png)

Watch the video tutorial

If you prefer watching a video tutorial, here is the guide for you:

[Containers](https://www.youtube.com/embed/EQgUvPEMd2E)

---

### Icons {#icons}

*Icons are integral elements in user interfaces, providing visual cues that enhance user interaction and aesthetic appeal. They communicate action, represent functionality, and improve navigation efficiency within applications.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/icons

Icons are integral elements in user interfaces, providing visual cues that enhance user interaction and aesthetic appeal. They communicate action, represent functionality, and improve navigation efficiency within applications.

![icon.png](https://docs.flutterflow.io/assets/images/icon-7d7bad4d005740306b979eabaab82ac2.png)

#### Types of Icon widgets

FlutterFlow allows a bunch of widgets and components:

* **Icon Widget**: The **Icon** widget in FlutterFlow is used for displaying symbols from a variety of available icon packs like Material Icons. It's straightforward to use, allowing for quick integration of visual symbols into your app.

* **Icon Button Widget**: The **IconButton** widget combines the functionality of an icon with the capabilities of a button, making it a clickable icon. It's commonly used for actions like opening a menu, submitting a form, or any other interactive task.

* **Toggle Icon Widget**: The **ToggleIcon** widget offers a specific functionality where the icon toggles between two states based on a boolean condition. This widget is ideal for "favorite" or "like" buttons, where the icon state changes to represent an active or inactive state. The ToggleIcon reacts to user taps, changing its appearance and also allowing for callback functionality to handle the state change.

#### Common Icon Properties

Upon selecting the Icon, you can modify properties such as **Icon color** and **Icon size** from the Properties Panel on the right. Additionally, you can set the Icon value by selecting from a vast catalog of **Material Icons** and **FontAwesome** Icons provided by FlutterFlow.

Custom Icons

You can also upload your own licensed Custom Icons. Check out [**this video**](https://youtu.be/rlGkbnhP75g) to learn more.

#### Icon Button Properties

The Properties Panel for your IconButton allows you to modify the Icon Properties, Button Styling, Disabled state, and Hovered state properties. It also lets you determine if you want a loading indicator when the icon button is clicked.

To get a quick demo of the styling changes, check this out:

#### Toggle Icon Properties

ToggleIcon is a special component created for you that lets you add a toggle on and toggle off icon, and define a State variable that determines the state of the Toggle icon. The properties are straightforward and include the following:

![toggle.png](https://docs.flutterflow.io/assets/images/toggle-68199f1a71fa7398fa0dbf1febb71a11.png)

##### On Toggle \[Action]

By default, FlutterFlow handles the toggling of the State variable from true to false and vice versa when the button is clicked. However, you can also add another action under the On Toggle action trigger to perform extra tasks.

---

### Image {#image}

*Images are a fundamental part of modern user interfaces, enhancing visual appeal and user*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/image

Images are a fundamental part of modern user interfaces, enhancing visual appeal and user engagement. In app design, images can provide context, support content, and guide user interactions. Different types of image widgets cater to various design requirements, ensuring flexibility and aesthetic integration across platforms.

* **Image Widget**: The Image Widget is a versatile component used to display images from a variety of sources, including local assets and the internet. It's essential for adding visual elements to your applications, such as logos, icons, and photographs.

* **CircleImage Widget**: The CircleImage Widget specifically caters to scenarios where you need to display images in a circular format, commonly used for profile pictures or branding elements.

The properties for the Image widget provide various customization options, from sizing and fitting to advanced animations.

#### Common Image Properties

* **Width & Height:** Specify the dimensions of the image. Values can be in pixels (px) or as a percentage (%) of the parent container's size, allowing for responsive design.

  * In case of `CircleImage` widget, you can define the **diameter** of the widget instead.

* **Border Radius:** Adjusts how rounded the corners of the image are. You can define border radius for TL (Top left), TR (top right), BL (bottom left), and BR (bottom right) separately or for all corners together. A higher value results in more rounded corners.

  CIRCLEIMAGE

  This option is not available for `CircleImage` widget since it is circular in shape.

##### Image Type

Specifies the source of the image. Options include:

* **Network:** Enter the URL of the image in the Path input field. This is used for images hosted online.

  * **Cached:** Determines whether the image should be cached for performance optimization. When toggled on, it stores the image locally to speed up load times on subsequent views.

    * When cached is enabled for `Image` widget & `CircleImage` widget, you can also define the **Fade in/out duration** (when blur hash is not enabled). This setting is not available for Background Image of Container.

* **Asset:** Click the Upload Image + button to upload an image from your computer or select from previously uploaded assets. When this option is selected, you can enable the **Set Dark Mode** toggle to specify a separate background image for dark mode environments, enhancing the visual experience under different lighting conditions.

* **Uploaded File:** Selecting this option allows for dynamic handling of image data within your app, accommodating images that users upload during app usage. This makes it suitable for applications requiring user-specific or user-generated content. Set this to use **Widget State > Uploaded File** to manage the image as part of the app's state.

##### Box Fit

Determines how this widget should take up the available space. The options are:

![image-boxfit.png](https://docs.flutterflow.io/assets/images/image-boxfit-74c8424b34088f4d083e1b7bc4483797.png)

Example of a horizontal & vertical image in different BoxFit options

* **Fill:** Scale the image to completely fill the container, which might distort the image.
* **Contain:** Scale the image to fit within the container without distorting it, which might leave some empty space.
* **Cover:** Scale the image to completely cover the container without distorting it, potentially cropping some parts of the image.
* **Fit Width:** Scale the image to fit the width of the container, possibly leaving empty space vertically.
* **Fit Height:** Scale the image to fit the height of the container, possibly leaving empty space horizontally.
* **None:** No scaling or adjustment, showing the image in its original size.
* **Scale Down:** Center the widget and scale it down until it fits within the available space.

##### Image Alignment

Controls the alignment of the image within the container. This grid allows you to position the image precisely within the container, with options to align it to the center, top, bottom, left, right, and combinations of these.

* **X & Y:** Adjusts the fine positioning of the background image along the X (horizontal) and Y (vertical) axes. This is useful for making precise adjustments to the image placement.

#### Advanced Image Functionalities

* **Show Error Image on Failure:** When enabled, displays an error image if the main image fails to load. This helps maintain a good user experience even when image retrieval issues occur.

* **Use Blur Hash:** When enabled, displays a blurred placeholder image while the main image is loading, based on a hash value representing the original image. This can enhance the perceived performance of image loading.

* **Make Expandable:** When enabled, the image can be expanded, usually to a larger view or a full-screen mode, upon user interaction.

* **Use Hero Animation:** Enables a hero animation effect when transitioning between screens. This can make the image appear to "fly" between screens for a smoother visual transition.

---

### Properties Panel {#properties-panel-2}

*In FlutterFlow, the Properties Panel on the right helps you configure and manage your widgets. It opens when you click on a widget or component in the Widget Tree.*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/properties

In FlutterFlow, the Properties Panel on the right helps you configure and manage your widgets. It opens when you click on a widget or [component](https://docs.flutterflow.io/resources/ui/components) in the [**Widget Tree**](https://docs.flutterflow.io/resources/ui/widgets#widget-tree).

Here's a quick demo showing how to add a widget to the canvas, which opens the widget properties panel on the right, allowing you to update the widget's properties:

The panel is divided into sections, each focusing on settings specific to the selected widget. The available options may vary depending on the widget type, with additional advanced configurations available for further customization.

![advanced-configs-widgets.png](https://docs.flutterflow.io/assets/images/advanced-configs-widgets-4fcf0fbd6b6c7ed7551a6df8262671bb.png)

##### Widget name

When you select any widget, its name appears on the properties panel. The default name for any widget is its type. For example, if you select the Container widget, the name appears as '**Container**'. However, you can use the edit icon on the right to change its name.

![widget-properties.png](https://docs.flutterflow.io/assets/images/widget-properties-5052050595add7f5def91601388644b3.png)

#### Actions

This section allows you to define and manage interactions or events triggered by user actions. For example, you can configure a button to navigate to another page, submit form data, or call an API. Actions are crucial for creating interactive and functional apps.

In the case of widgets, you can add user interactions on action triggers such as **On Tap** or **On Long Press**. The availability of these actions may vary depending on the widget.

Actions differ according to the widget selected; on some widgets, you can't apply any actions.

#### Backend Query

Here, you can configure the page to fetch data from a backend source or database. This is typically done through API calls or direct database queries. Setting up a backend query allows the widget to display dynamic content, such as user profiles, product lists, or any other data your app needs to retrieve from a server.

#### Generate Dynamic Children

Widgets capable of handling multiple child widgets have an additional tab called **Generate Dynamic Children**. This feature helps you generate multiple child widgets from a list variable.

This is particularly useful when you are retrieving data from an API call.

Some of the widgets that can handle multiple children include **Column, Row, Stack, ListView, GridView, and PageView**.

> **Info:** To learn more about [**Generating Dynamic Children**](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/generate-dynamic-children), refer here.

#### Animations

You can apply animations to a widget to enhance the visual appeal and user experience. Animations can be used to draw attention to important elements, provide feedback on user interactions, or create visually engaging transitions between states.

> **Info:** Learn more about adding **[animations](https://docs.flutterflow.io/concepts/animations)** here

#### Documentation and Semantic Labels

**Documentation** helps developers understand the purpose and function of a widget within the app, making maintenance and future updates easier.

**Semantic labels** are crucial for accessibility, allowing screen readers to accurately describe the widget's function to users with visual impairments.

---

### Text {#text}

*Text is a fundamental element in any user interface, used to convey information and interact*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/text

Text is a fundamental element in any user interface, used to convey information and interact with users. In app development, effectively presenting text can significantly enhance the user experience, making information accessible and interactions intuitive. Two common widgets used for displaying text in FlutterFlow are the Text widget and the RichText widget. Each serves a distinct purpose and offers different capabilities for integrating text into an application.

#### Text Widget

The Text widget is used to display a piece of text on the screen. It's one of the most commonly used widgets in app development.

![text-example.png](https://docs.flutterflow.io/assets/images/text-example-5dbb41a06e4e1625e516f25bc8b51682.png)

For example, in this screen, the Text widget is used to present different pieces of information clearly and effectively. The Text widgets display the product name, "Men's Harrington Jacket," its price, "$148," and a detailed description of the product. These Text widgets are styled differently to emphasize specific pieces of information.

The Text widget can be found under the **Base Elements** tab in the **Widget Palette**. You can either drag it to your desired location on the screen or insert it directly via the widget tree.

Once the Text widget is selected, the Properties Panel on the right side becomes active, allowing you to customize the styling of your Text widget. Here, you can adjust various attributes such as font size, color, alignment, and more to tailor the appearance to fit your design needs.

#### RichText Widget

The **RichText** widget offers more elaborate formatting capabilities compared to the basic Text widget. It allows for the mixing of multiple styles within a single text sequence, enabling the creation of stylized textual content.

This widget uses a tree of **TextSpan** objects to define the rich formatting options, including different fonts, sizes, and colors for various parts of the text. RichText is particularly useful for text-heavy applications that need inline styling and linking, like in a formatted article or a document viewer.

The RichText widget can be found under the **Base Elements** tab in the **Widget Palette**. You can either drag it to your desired location on the screen or insert it directly via the widget tree.

![richtext-eg.png](https://docs.flutterflow.io/assets/images/richtext-eg-fb12340204efef65ec066cab09b82894.png)

When the RichText widget is added to your widget tree, FlutterFlow automatically creates two RichTextSpan child objects. You can modify the text value and styling of each object to create multiple styles within your paragraph.

To modify the RichTextSpan objects, see the quick demo below:

#### Common Text Styling Properties

![text-props.png](https://docs.flutterflow.io/assets/images/text-props-6a4106562a78bb5e4db8d8c6fef14e1b.png)

> **Tip:** For consistency, we recommend defining your Typography and custom text styles from **Theme Settings > Typography & Icons** before creating any screens.

Few things to note:

* **Line Height:** Sets the height of the text (e.g. a value of 1.5 would make the line height 50% larger than the font size.

* **Text Align:** Define how text is positioned within a container, typically as left-aligned, right-aligned, centered, or justified

#### Advanced Properties for Text Widget

* **Max Lines:** This property specifies the maximum number of lines that the text can occupy. If the content exceeds the set number of lines, it will be truncated or end with an ellipsis, depending on the configuration. This is useful for maintaining a clean and consistent layout where text space is limited.

- **Auto Size**

  The `Auto Size` option allows the `Text` widget to automatically reduce its font size to fit within its parent widget. This ensures that the text remains legible without overflowing its container, making it especially handy for responsive designs where the display may vary across different devices.

  * **Configure Parent Widget Dimensions**

    To enable `Auto Size`, the `Text` widget must be inside a widget that has both defined width and height. Without these constraints, the font size cannot be adjusted automatically.

    1. Select the `Text` widget.

    2. Check its parent widget.

    3. Ensure both width and height are explicitly defined.

       warning

       Without defined dimensions, the `Auto Size` feature may not behave as expected.

  * **Behavior Scenarios**

    The following examples illustrate how `Auto Size` behaves under different container configurations:

    * Container with width set to `infinity` and height set to `100px`, `Auto Size` disabled. The text may overflow beyond the container.

    * Container with width set to `infinity` and height set to `100px`, `Auto Size` enabled. The font size adjusts to fit the defined height.

    * Container with width set to `30%` and no height defined, `Auto Size` enabled. The feature has no visible effect due to missing height constraint.

    * Container with width set to `70%` and height set to `50px`, `Auto Size` enabled. The text is resized to the minimum allowed font size to remain within the container.

      ![](https://docs.flutterflow.io/assets/images/20250430121459696014-760e4e8b93b65d720b5f8c3af1d34a4d.png)

> **Tip:** Use `Auto Size` with percentage-based dimensions for better responsiveness. For example, set the container width to `30%` and enable `Auto Size` to allow the text size to adjust as the screen size changes.

> **Note:** The `Auto Size` feature has a minimum font size threshold. If the container becomes too small, text may clip or overflow when resizing is no longer possible.

##### Setting Text Overflow replacement

You may want to limit the number of characters shown inside the Text widget and replace the extra characters with the ellipsis or completely hide them.

Important

This option is only available if the value is set from the variable.

To set the text overflow replacement:

1. Select the **Text** widget, navigate to the **Properties Panel > Text Properties >** enter the value for **Max character** to limit the number of characters.

2. Set the **Text Overflow Replacement** to either **Clip/Cutoff** or **Ellipsis (...)**

![text-overflow.png](https://docs.flutterflow.io/assets/images/text-overflow-acb011560d030927aadf17f5993feb5f.png)

##### Adding Gradient color

Conditional Properties

Note that enabling the Gradient option disables AutoSize and setting Max Lines for your Text.

Adding a gradient color to the text gives it a modern look and feel. You can either use our ready-made templates or create it from scratch.

Here's how you do it:

1. Select the **Text** widget, navigate to the **Properties Panel > Text Properties >** enable the **Gradient** toggle.

2. To add your own colors:

   1. Select the **Type** among the **Linear** and **Radial**. The *Linear* distributes the colors horizontally, whereas the *Radial* circularly spreads the color.

   2. If you choose *Linear*, specify the **Direction,** and for *Radial*, specify the **Radius**.

   3. Add/Remove or customize the existing colors.

> **Info:** You can also add gradient colors from a preset template as shown in the video demo.

#### Formatting numbers

You may want to format large numbers for better readability. Displaying a number like 2,354,000 or 4,356,634,444 instead of 2354000 or 4356634444 enhances the user experience.

For instance, it's clearer to show the population as 1,200,000 rather than 1200000 and currency values like $2K or $5M instead of $2000 or $5000000.

##### Types of formatting

Below are the types of formatting that we support:

* **Decimal**: Shows numbers in decimal format (e.g., 1,200,000 and 1.200.000).
* **Percent**: Shows numbers in percentage format (e.g., 28%, 99.99%).
* **Scientific**: Shows numbers in scientific format (e.g., 1e3, 1E6).
* **Compact**: Shows numbers in compact format (e.g., 2.1K, 2.3M, 5B).
* **Compact Long**: Shows numbers in compact long format (e.g., 2.1 thousand, 2.3 million, 5 billion).
* **Custom**: If the given formatting options do not fit your requirement, you can use specify a custom format.

##### Format a number

Use the instructions below to format a number:

1. Select the **Text** widget, move to the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) > **Set from Variable >** display the value from a variable of type **Integer** or **Double**. (e.g., **App State > App State Variable Name**).

2. After selecting a variable, set the **Available Options** to **Number Format** and **Number Format Options** to the required [type](https://docs.flutterflow.io/resources/ui/widgets/text#types-of-formatting).

   1. If you choose **Decimal**, you must set the **Decimal Type** as well. The decimal values can be shown in two ways, i.e., 1,200 (with a comma) and 1.200 (with a period).

      1. Select **Automatic** to show decimal value based on the user's country.

      2. Select **Period for Decimal** to show decimal value with a period (e.g., 1.200).

      3. Select **Comma for Decimal** to show decimal value with a comma (e.g., 1,200).

   2. If you choose **Custom**:

      1. Find the **Custom Format** box, and enter your format. For example, entering `###,###.###` will convert the number 123456.789 into 123,456.789, and 000.00 will convert the number 12.786 into 012.79.

      2. In the **Locale** input box, enter the locale in which you want to display the number. (If you leave this property empty, the locale is automatically set as per the user's location). Learn more about how to format a number [here](https://pub.dev/documentation/intl/latest/intl/NumberFormat-class.html).

3. To display this number as currency, enable the **Display as Currency** toggle and specify the **Currency Symbol**.

4. Click **Confirm**.

---

### Common Widget Properties {#common-widget-properties}

*Learn how to control common widget properties in FlutterFlow*

**Source:** https://docs.flutterflow.io/resources/ui/widgets/widget-commonalities

When working with widgets in FlutterFlow, you'll encounter properties and features that are common across multiple widget types. Below is a detailed overview of such properties.

#### Visibility

Visibility settings in FlutterFlow allow you to dynamically control when and how widgets appear in your app.

##### Conditional

**Conditional** visibility allows you to control the display of UI elements (widgets) based on specific conditions or criteria. It helps you create dynamic, personalized experiences by showing or hiding certain content.

For example, you could display specific features or actions only to users with particular roles, such as showing admin controls exclusively to administrators.

> **Info:** The **Show in UI Builder** toggle only affects visibility within the design canvas, giving you a quick preview of how the layout will adjust when this widget is shown or hidden.

![conditional-visibility.avif](https://docs.flutterflow.io/assets/images/conditional-visibility-23ea7b86289e9551c4468ed2b5a872d0.avif)

##### Responsive

The **Responsive visibility** property allows you to show or hide widgets based on device screen size, such as mobile, tablet, or desktop. By toggling each icon, you can show or hide the widget according to your design needs.

For example, you might create two separate navigation menus:

* **Desktop Menu**: A wider, left-aligned menu only visible on large screens by enabling the desktop icon and disabling all other screen size icons.
* **Mobile Menu**: A compact drawer menu only visible on smaller screens by enabling the phone icon and disabling all other screen size icons.

![responsive-visibility.avif](https://docs.flutterflow.io/assets/images/responsive-visibility-af9fb868f82411dafd2dcf3cf3485c90.avif)

##### Opacity

The **Opacity** property controls how transparent or visible a widget appears. It accepts a value between 0 and 1, where 0 means fully transparent, 1 is fully opaque, and 0.5 results in semi-transparency.

This property enables a wide range of creative UI effects, such as translucent buttons, overlay highlights, or smooth theme transitions.

When **Animated Opacity** is enabled, any changes to the opacity value are smoothly animated based on the specified duration and curve, enhancing visual appeal and user experience.

![Opacity.avif](https://docs.flutterflow.io/assets/images/Opacity-ef06ded87e55f159dad15135fdb2aa96.avif)

#### Padding

**Padding** is the space added inside a widget, between its content and its border (or edge). It ensures the content doesn't touch the borders, creating visual breathing room and contributing to a cleaner, more responsive layout across different screen sizes.

To set padding, select the widget, go to the **Padding & Alignment** > **Padding** section in the **Properties Panel**, and enter the values in **pixels (px)**, which represent logical pixels.

You can choose from two options:

* **Uniform Padding**: Apply the same value to all four sides.
* **Independent Padding**: Set different padding values for top, bottom, left, and right.

If you prefer watching a video tutorial, here is the guide for you:

#### Alignment

**Alignment** determines how a widget is positioned within its parent container. It helps you control where your widget appears—left, right, center, top, bottom, or any point in between.

To set alignment, select the widget and go to the **Padding & Alignment** > **Alignment** section in the **Properties Panel**. You'll see a 3×3 grid representing all nine positions:

* Top Left
* Top Center
* Top Right
* Center Left
* Center (Default)
* Center Right
* Bottom Left
* Bottom Center
* Bottom Right

Simply click the dot representing where you'd like the widget to be positioned. Alternatively, you can input a specific value (between -1 to 1) for the precise horizontal and vertical alignment.

* **X (Horizontal Alignment)** controls the widget’s position along the horizontal axis within its parent. A value of `-1` aligns it to the left, `0` centers it, and `1` aligns it to the right.
* **Y (Vertical Alignment)** controls the widget’s position along the vertical axis. A value of `-1` places it at the top, `0` centers it vertically, and `1` places it at the bottom.

> **Info:** Values beyond this range will push the widget outside the visible screen area.

#### Add Testing Value Key

A **Value Key** is used to uniquely identify widgets during [**Automated Testing**](https://docs.flutterflow.io/testing/automated-tests) in FlutterFlow. For example, on a Create Account page, you might use descriptive keys like `signupFirstNameField`, `signupEmailField`, `signupPasswordField`, and `signupSubmitButton`. This helps testing tools reliably locate and interact with the correct widgets. For more details, refer to the [complete guide here](https://docs.flutterflow.io/testing/automated-tests).

![test-value-keys.avif](https://docs.flutterflow.io/assets/images/test-value-keys-e38ee305c4a9fb82b6145cb18cd7697c.avif)

#### Set Width & Height

To adjust a widget's size, click on the widget you wish to resize and navigate to the right-side Properties Panel. There, you can set the size in the following ways:

* **PX (Pixels):** Enter a fixed size in pixels for a consistent dimension.
* **% (Percentage):** Set the size relative to the screen or parent container.
* **∞ (Infinity):** Make the widget expand to fill the available width or height.

You can also drag the handle bars on the right and bottom sides of a selected widget to resize. The measurements appear while resizing to show the current pixel values.

![use-handle-bars-to-resize.avif](https://docs.flutterflow.io/assets/images/use-handle-bars-to-resize-eb13939a7ac53272a5d6fa13aec92187.avif)

Responsive Width & Height

You can also use a **Responsive Value** to apply different width or height values based on screen size. To set it up, open the **Set from Variable** menu and select **Responsive Value**. Then, assign specific size values for each screen size category, such as mobile (Screen Width < Breakpoint Small), tablet (Screen Width < Breakpoint Medium), and desktop (Screen Width < Breakpoint Large).

#### Use Keyboard to Adjust Property Values

You can quickly increase or decrease the property value using your keyboard's up and down arrow keys. This allows for precise control without needing to type in new values each time.

> **Tip:** Hold down the **Shift** key while pressing the arrow keys to change the value by 10 units at a time.

#### Change Color

To change the color, navigate to a widget property that allows you to set a color, and then click on the currently selected color. This opens the **Color Picker**, where you have multiple ways to set the desired color:

* **Custom Color**: Use the gradient area to select any shade and fine-tune it using: * The **hue slider** (rainbow bar) to adjust the base color.
  * The **transparency slider** (checkered bar) to control opacity (alpha value).

* **Use RGB or HEX**: Manually input a **HEX code** (e.g., `#A489F5`) or set the **RGB values** directly for precise color control. The **Alpha (A)** value defines transparency (e.g., 100% = fully opaque).

* **Theme Colors**: Below the picker, you’ll find a list of your app’s predefined **Theme Colors** like Primary, Secondary, and Background. Using theme colors ensures design consistency across your app and makes global updates easier.

* **Set from Variable**: You can also dynamically assign a color based on your app logic. For example, changing the background color based on the selected item or theme.

> **Tip:** You can also assign a color using a **String variable** that contains a **CSS-style color value** (e.g., `"#FF5733"`, `"rgba(255, 87, 51, 1)"`, or `"red"`). This is especially useful when colors are stored in a database or returned from an API. Make sure the string format follows valid CSS color syntax, as FlutterFlow uses the [**`from_css_color`**](https://pub.dev/packages/from_css_color) package under the hood to parse these values.

This allows you to dynamically theme parts of your app based on user preferences or remote configurations.

![color-from-string.avif](https://docs.flutterflow.io/assets/images/color-from-string-d25dcbcd05a58f64d8dd0bbf5b5add9f.avif)

#### Copy Variable

If you’ve created a complex variable value (e.g., using Conditional Logic) and want to reuse the same logic elsewhere, you can easily do so by copying the variable.

To copy and paste a variable, open the **Set from Variable** menu, click the **three dots**, and select **Copy Variable**. Then go to the target location, open the same menu, click **Paste Variable**, and confirm.

#### Bulk Edits Properties

You can easily modify the properties of multiple widgets at once. For example, if you want to change the background color of several buttons from blue to green, there's no need to edit each one individually. Simply select all the buttons and update their fill color in one go.

To do this, hold down the **Shift** key and click on each widget you want to edit. Once selected, their shared properties will appear in the **Properties Panel**, where you can apply changes.

#### Use Images from Unsplash

You can easily display high-quality images directly from [Unsplash](https://unsplash.com/) using the Properties Panel. Just click the **search icon**, type in your desired keyword, and select an image from the results.

> **Tip:** You can also choose the image size (i.e., Small, Regular, or Full) before adding it, depending on your layout.

#### UI Builder Display Value

For widgets like `Text` and `RichText`, if the content is set from a variable, you can add a placeholder value that appears only in the FlutterFlow builder. This placeholder helps you visualize how the text will look on the canvas, but it won’t appear in the live app, it's replaced by the actual variable at runtime.

This is especially helpful for previewing layout, spacing, and alignment without removing or disrupting your variable bindings.

![ui-builder-display-value.avif](https://docs.flutterflow.io/assets/images/ui-builder-display-value-1efc84d1dd78a1725f8ff7e132a509be.avif)

#### Adding Border

You can add a border to any widget using the following properties:

* **Border Color**: Choose a color manually or bind it to a variable. You can select from your theme colors (like `Primary`) or use the color picker.

* **Border Width**: Set the thickness of the border in pixels.

* **Border Radius**: Adjust how rounded the corners should be using the options below: * **Independent Radius**: Set different radius values for top, bottom, left, and right.
  * **Uniform Radius**: Apply the same value to all four sides. The slider and numeric input allow you to have precise control.

* **Button Padding**: Controls the space inside the widget (between the content and the border).

> **Tip:** Use consistent border and padding styles for buttons, cards, and containers to maintain a clean and cohesive UI.

---

