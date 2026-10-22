## Visual Design

For major new features or sections, do quick design thinking:
- Moment: A specific person, in a specific context, doing a specific thing; the lens for design decisions
- Hero Element: the one element or layout pattern that anchors the experience; without a clear priority the design is just a template

If making visual changes:
- Tailwind CSS v4 works: `className="flex items-center gap-3 text-base"`
{space_template_edit_color_rules}
- Don't degrade mobile: no new horizontal scroll, broken safe-area protection, or primary actions out of thumb reach. Fix an obvious mobile bug in code you're already touching; don't expand scope to audit the rest.
- Check phone and desktop widths in audit

Images: keep the existing image strategy. Anything you add or repopulate follows the Images And Media rules.

