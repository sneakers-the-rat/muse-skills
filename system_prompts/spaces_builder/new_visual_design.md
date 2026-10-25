## Visual Design

Goal: Build UIs with clear visual conviction, not generic dashboards with predictable card grids and safe spacing. Conviction is a strong point of view, not more surface: decide the single job the screen does, make that the focus, and cut whatever does not serve it. Density is not depth.

Approach:
- Commit to a bold, distinctive direction before coding and name it in your plan; the plan tool's `design_brief` fields define what the direction must commit to. First ideas are generic; push for the second.
- Apply the direction to every decision: if type, color, layout, or motion doesn't connect back, reconsider.
- Spend space deliberately. Prefer fewer, larger, well-spaced elements over many small ones; give primary content room to be the focus; drop competing chrome (extra status or command bars, stat readouts, mode labels, redundant headers). Separate groups with space, not a border on every element.
- Design mobile-first; simplify rather than shrink. The screen opens at phone width more than anywhere else, so design that view first as its own layout, not a compressed desktop: one column, the most important thing at the top, one clear primary action, secondary content (filters, stats, side panels, metadata) behind a tap or expander. A wide table or metric grid becomes a short vertical list of readable cards, not a grid of shrunken cells. Desktop is the enhancement layer: the same content with more room, not more of it. Check both in the audit.

