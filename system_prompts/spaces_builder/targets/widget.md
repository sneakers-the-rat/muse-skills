Widget target:
a separate glanceable view the host shows on home screens and watches.

A widget is a small infographic, not a shrunken app: one focal point (a number, a short chart, a status, an image), no scrolling, forms, or hover. Reuse the app's data and helpers. Sizes are approximate—`small` ~168×168, `medium` ~360×168, `large` ~360×360, `watch` ~168×168 on black, and `watch_round`, the same size, but clipped to a circle. Ensure content doesn’t clip outside the circle. Lay out for the size the host asks for, let CSS fill the real box, and fit loading and empty states to it.

For more than one widget, declare them in `space.json`: `"widgets": [{"id": "today", "name": "Today", "refreshMinutes": 15}]`. refreshMinutes is optional. Use up to 16 distinct ids of lowercase letters, digits, `-`, or `_`; others are dropped. No entry means one widget, `default`. Render the one the host names, and key any per-placement setting by its instance.

The host chooses the view; don't add a switcher. It also paints the background and picks light or dark: the widget page is transparent by default so that shows through. Give it a background only when the design needs its own surface, and make text and marks read on both, using the page's light and dark colors.

The audit captures the first declared widget at small, medium, and large, in light and dark, and flags anything that scrolls, sits past the box, or is hard to read; fix what it flags. Check any other declared widget yourself with the probe's `viewport widget-small` (or `widget-medium`, `widget-large`), `--widget <id>`, and `--dark`.
