# Marketplace listing touch-ups

When the user added photos for a listing, run these steps before `facebook-cli
marketplace listing create`.

## 1. Offer

Before creating the listing, even if the user asked to publish right away,
offer to touch up their photo: "Touch up photos" or "Save as-is". The
approval card is for creating the listing not whether they want touch-ups.

## 2. Make four versions

- Make a new folder under `workspace/marketplace/`.
- Copy the best photo in as the original, keep its extension, note its parts and
marks.
- Use the folder's paths for `output_dir`, `--photo` and the picker.
- Make each edit as in `SKILL.md` step 2.

- **Studio** and **Lifestyle:** as defined in `SKILL.md` step 1.
- **Touched-up:** remove mess and relight to soft daylight.
- **Close-up:** crop of Touched-up (or original if Touched-up was dropped) item
and its parts with 20% margin.

- If there's a failure, replace it with a
single backup on a grey-to-white gradient instead of
the original, and tell the user in one line what was dropped and why.
- If the user asks for any other edit instead, only make that edit.

## 3. Choose a cover

- Pick up to four distinct images: keep the versions in selection order, then
the backup, then the original if a slot is still empty.
- In the same turn as the edits, load the `widget` namespace and make one
`widget.create_image_picker_widget` call with their paths.
- Offer the user to choose a cover along with an option to keep their original
photo.
- Let the user pick as in [Picking photos](picking-photos.md). Attach the
picks cover first, then any other item photos.

## 4. Share

- Once the listing is created and facebook_cli's confirmation and buyer-message
steps are done, ask if the user wants to share the photos to Instagram, their
Facebook Page or their website too ("Yes" or "No thanks").
- On "Yes", continue at step 3 (Captions) of `SKILL.md` with the listing's
photos in order and skip "Try other styles".
- If the listing is live, add a caption line "Available on Facebook
Marketplace: <product URL>".
