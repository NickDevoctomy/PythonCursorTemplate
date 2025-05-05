# NiceGUI Reference

This document is a living reference for using [NiceGUI](https://nicegui.io/) in this project. As new features, patterns, or best practices are discovered, they will be added here. Please refer to this document for guidance and examples.

---

## General Notes
- NiceGUI is a Python framework for building web-based user interfaces with a simple, Pythonic API.
- UI elements are created using the `ui` module, e.g., `ui.button()`, `ui.textarea()`, `ui.column()`, etc.
- The UI is reactive and can be updated dynamically in response to user actions or backend events.
- You can use both NiceGUI's built-in components and raw HTML/CSS for custom layouts.

## Creating UI Elements
- Use `ui.button('Label', on_click=callback)` to create a button.
- Use `ui.textarea(placeholder='Type here...')` for a multi-line text input.
- Use `ui.column()` and `ui.row()` for layout.
- Use `ui.html('<div>...</div>')` to insert raw HTML, but note that this is static and not ideal for dynamic content.
- Use `ui.element('div')` to create a dynamic container you can add children to later.

## Updating the UI
- To update a UI element, you can clear its contents with `.clear()` and add new children.
- For dynamic lists (like chat messages), prefer using `ui.element('div')` as a container and add children dynamically, rather than recreating the container each time.
- `ui.update()` can be used to force a UI refresh, but is rarely needed if using NiceGUI's reactive patterns.

## Dark Mode
- Use `ui.dark_mode(True)` or `ui.dark_mode(False)` to toggle dark mode.
- NiceGUI automatically applies dark/light theme classes to the body and built-in components.
- Custom CSS can be used to further style elements for dark mode.

## Tabs and Panels
- Use `ui.tabs()` and `ui.tab_panels()` to create tabbed interfaces.
- Each tab and panel is created with `ui.tab('Label')` and `ui.tab_panel(tab)`.

---

# Advanced Usage & Best Practices

## Code Organization & Modularization
- **Componentization:** For large apps, split your UI into logical components (e.g., header, sidebar, main content) and place each in its own module or class.
- **Subclassing:** You can subclass NiceGUI elements (e.g., `class MyHeader(ui.header): ...`) to encapsulate logic, styling, and event handling.
- **Context Managers:** Use context managers (`with my_component(): ...`) to keep your main UI code clean and readable.
- **Event Handling:** For complex event handling between components, connect the "pipes" after assembling the UI, or use shared state objects.
- **See also:** [Modularization Example](https://github.com/zauberzeug/nicegui/tree/main/examples/modularization)

## Async & Performance
- **Async-first:** NiceGUI is async-first. Always use `async def` for event handlers and long-running tasks.
- **IO-bound work:** Use async libraries (e.g., `aiofiles`, `httpx`).
- **CPU-bound work:** Use `run.cpu_bound` for heavy computation.
- **Avoid blocking:** Never block the main thread; otherwise, UI updates and interactions will lag or freeze.
- **Per-user pages:** Use `@ui.page` for per-user pages to avoid global state issues in multi-user apps.

## State Management
- **Persistent/session state:** Use `app.storage.user`, `app.storage.general`, and `app.storage.browser`.
- **Per-user state:** Prefer `@ui.page` and `app.storage.user` or `app.storage.browser` for user-specific data.
- **Avoid global state:** Don't use global variables for user-specific data in multi-user deployments.

## Styling
- **Quasar & Tailwind:** NiceGUI uses Quasar (Vue3) and supports Tailwind CSS. You can use both, but be aware of color/class name differences.
- **Colors:** For custom colors, use Quasar color names for best compatibility.
- **Custom styling:** Use `.classes()` and `.style()` for custom styling, and `.props()` for Quasar-specific properties.

## Dynamic Content & Refreshing
- **Dynamic lists:** Use `ui.element('div')` or `ui.column()` and update with `.clear()` and child elements.
- **Refreshable sections:** Use `ui.refreshable` for sections that need to be fully re-rendered on demand.
- **Binding:** Use `.bind()` for automatic updates of individual UI elements when a value changes.

## Debugging & Hot Reload
- **Double execution:** If using `ui.run(reload=True)`, your code runs twice (main process and reload subprocess).
- **Main guard:** Use `if __name__ == '__mp_main__':` to guard code that should only run in the reload subprocess.
- **Production:** For production, use `ui.run(reload=False)`.

## Deployment & Scaling
- **Sticky sessions:** For multi-process deployments (e.g., with a load balancer), use sticky sessions and avoid global state.
- **Shared state:** Use Redis or a database for shared state across processes if needed.

## Community & Support
- **Discussions:** The [NiceGUI GitHub Discussions](https://github.com/zauberzeug/nicegui/discussions) and [Discord](https://discord.gg/2wP6F2k4) are active for help and sharing patterns.
- **Underlying tech:** Many issues can be solved by consulting FastAPI, Vue3, or Quasar documentation, as NiceGUI builds on these.

---

**Note:**
This document is continuously updated as new features, patterns, and best practices are discovered. If you encounter a new pattern or solution, please add it here! 