# Touch-ups

Ask if photos are missing. Product shots: edit in upload order; show each
  photo's picker and wait for the user's choice before editing the next.
  Marketplace: edit only the initial cover; leave other photos and later uploads
  unedited. Copy originals with extensions into fresh photo folders:
  `workspace/product-shots/` or `workspace/marketplace/`. Never overwrite.

Use `media.generate_image`: originals, their folder as `output_dir`,
  `jpg` as `output_format`. Include in each image prompt, "Keep the item
  exactly as it is: same angle, size, position, shape, color, text, logos and
  wear. Do not add anything that touches it." Studio: light grey. Lifestyle:
  everyday setting. Touched-up: clear surrounding mess, soft daylight.

Before offering any generated version, compare it with its original: shape,
  color, text, logos, parts and wear must match; nothing new may touch the item.
  Reject edits that fail these checks or change framing or position unless asked
  or allowed by the chosen style. Explain any rejection in one line; use the
  fallback below.

Locally crop Close-up from the Touched-up file, or the original if that edit
  was dropped, without `media.generate_image`. Keep every part with 20% margin.
  Only when a generation fails or an edit is rejected, make at most one
  grey-to-white backup for that photo within the remaining call budget, and
  check it by the same rules. If the backup fails or is rejected, use the
  original. Four attempts including failed calls and backups, until user or
  scheduler input.

Requested styles replace defaults. Keep website styles consistent.
  Store white allows centering. For Match my store, ask for a product-page
  screenshot or get one photo from their store link. Use it as a second image
  for background and light only, never its item, logo or text.

Load `widget`; show versions through `widget.create_image_picker_widget` that
  turn, with `multi_select` on so the user can keep several. Use each
  version's returned `local_path` as its picker path; don't copy or rename
  edits. Name styles in order. For the default styles, fill all four slots:
  replace dropped versions with the backup, then the original, then square and
  portrait framings of the original saved as new files, without
  `media.generate_image`. Keep every part with 20% margin; pad instead of
  cropping when the item doesn't fit. For chosen or requested styles, show only
  those, replacing a rejected one with the backup or original.
  [Pick](picking-photos.md); don't retry.
