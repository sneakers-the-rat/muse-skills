{space_template_static_color_rules}

- Reach for a map only when a place is central and seeing it helps the reader. When a page needs one, read `/opt/muse/assets/artifacts/references/maps.md` and build a real interactive map, or ship no map at all; never hand-author one (no SVG maps, drawn routes, or pins dropped on a photo).

- A chart's numbers are never invented. When a page plots data, read `/opt/muse/assets/artifacts/references/charts.md` first and build from it. Hand-author charts as SVG: a live page has no chart-rendering pipeline behind it.

- Audio and motion are invisible to the audit; verify them yourself. Resume the one `AudioContext` on a user tap, or iOS stays silent.
