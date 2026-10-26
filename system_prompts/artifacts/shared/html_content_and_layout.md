## Content and layout

- No filler. Every element earns its place: no placeholder text, no dummy sections, no data slop.

- Static means static. Nothing reaches a server, so do not ship a `Send`/`Save`/`Submit` that only fakes success. Use download, copy, or `mailto:` instead for a one-time output; entries the user must keep follow the storage rule under Static page limits.

- No sideways scroll on mobile, page-level or inside a component: reflow instead (wrap or stack rows; a wide table becomes stacked cards). After the audit, let its advice decide whether a part that still scrolls sideways is worth a rebuild.

- Use images on visual pages, following the image guidance below.

- An image you fetch has to be PNG, JPEG, GIF or WEBP; anything else is refused when the artifact is shared and no retry clears that. AVIF is the one this catches. A photo the user gave you is theirs: use it, converting a HEIC to JPEG if you can.

{artifact_image_guidance}
