# Touch-ups

Ask if photos are missing. Load `widget` first. Edit uploaded photos one at a
  time, in upload order: show each photo's versions together in one picker and
  wait for the user to choose before starting the next. For Marketplace, edit
  the cover and any later photos the user wants touched up, and leave the rest
  as they are. Copy originals, with their extensions, into fresh photo folders
  (`workspace/product-shots/` or `workspace/marketplace/`) and save edits as new
  files.

Use `media.generate_image`: originals, their folder as `output_dir`,
  `jpg` as `output_format`. Include in each image prompt, "Keep the item
  exactly as it is: same angle, shape, color, text, logos and wear. Do not add
  anything that touches it." For every style except Close-up, also ask to keep
  the item's size and position unless the user asked for a change or the chosen
  style allows it. Studio: light grey. Lifestyle: everyday setting. Touched-up:
  clear surrounding mess, soft daylight. Close-up: clear surrounding mess, soft
  daylight, and frame the item more tightly with about 20% margin.

Before offering any generated version, compare it with its original: angle,
  shape, color, text, logos, parts and wear must match; nothing new may touch
  the item. Reject edits that fail these checks or change framing or position
  unless asked or allowed by the chosen style. Close-up may frame the item more
  tightly, at the same angle. Explain any rejection in one line; use the
  fallback below.

When a generation fails or an edit is rejected, make one grey-to-white backup
  for that photo within the remaining call budget, and check it by the same
  rules. If the backup fails or is rejected, use the original. Four attempts
  including failed calls and backups, until user or scheduler input.

Requested styles replace defaults. Keep website styles consistent.
  Store white allows centering. For Match my store, ask for a product-page
  screenshot or get one photo from their store link. Use it as a second image
  for background and light only, never its item, logo or text.

Show versions in the same reply using `widget.create_image_picker_widget`,
  with `multi_select` on so the user can pick several images. Use each
  version's returned `local_path` as its picker path; don't copy or rename
  edits. Name styles in order. For the default styles, fill all four slots:
  replace dropped versions with the backup, then the original, then square and
  portrait framings of the original saved as new files, without
  `media.generate_image`. Keep every part with 20% margin; pad instead of
  cropping when the item doesn't fit. For chosen or requested styles, show only
  those, replacing a rejected one with the backup or original.
  [Pick](picking-photos.md); don't retry.

If the user asked for one style, show that version on its own rather than in
  the picker.
  Offer to keep it or see more styles, and say which style it is. If the user
  keeps the current edit, that's their pick. If they want more, open the
  picker with the first three default styles you haven't shown, in order, and
  the original last. If you showed the original, end with the next fallback
  instead.
