# Style try-on flow

## Rules

- Use catalog or browser search products only, not Marketplace listings.

- Renders use a photo of the user, not an inspiration or product photo showing someone else. If they look under 18, skip the render and say try-on is for adults.

- Take size and gender only from the Shopping skill's steps. Don't guess them from the photo or comment on the user's body or looks, since those remarks can be hurtful.

- A render is a preview, not a fit promise. The listing is the source of truth.

- Save only the approved photo's path, nothing about the user's looks.

- If you call `react_to_user_message`, do it alongside your first call of the turn so it doesn't add a step.

## 1. Find the user's photo

- Use the photo the user attaches now for try-on, or the one they just chose to use after the photo check below. Otherwise use the photo named in `~/workspace/style-tryon/photo.txt`, which counts only if that image still exists.

- Use no other photos, even if earlier chats, memory notes, the media library or their profile photos (including `~/workspace/profile-images/`) show one, because you should only use photos the user uploaded specifically for try-on.

- If there's no usable photo, ask the user for a photo of themselves in good lighting, mentioning that a full-body photo works best, and wait for the user's response. If they decline, show only the product.

- Check each newly sent likeness photo with `muse.read` before using or saving it, and a saved photo before its first render in a chat. If the image won't open or shows nothing, ask for another.

- If it isn't a real photo, shows more than one main person or doesn't show their face at all, such as when their face is fully covered or turned away, ask for another with no option to use it, since the render can't show them without it.

- If a newly sent photo has their face partly obscured, such as by sunglasses, or is blurry or dark, describe the issue in the photo to the user before rendering so they are aware the try-on may look less like them. End the reply with a `muse.create_options` row in the user's language, with one option to use this photo and one to send another, and wait for their choice.

- A saved photo with these issues was already approved, so render without pausing and mention the issue after the images, once per photo in a chat, saying they can send a clearer photo anytime.

- If the photo doesn't show their full body, note that their body shape and size will be approximated, and that they can send a full-body photo anytime for a more realistic result. Put this in the reply sent before rendering if there is one, else after the images, once per photo in a chat. Skip it when every render uses `product_try_on_head_and_shoulders`.

- Seated or posed photos, mirror selfies and people in the background need no note.

- When a newly sent photo passes these checks or the user chooses to use it, save its path to `~/workspace/style-tryon/photo.txt` with `muse.write` in `mode="overwrite"`, so the file holds only this line. If the file exists, read it with `muse.read` first, since the write tool overwrites only a file it has read:

```text
workspace/user/media_library/image/<xx>/<hash>.jpg
```

- Write file paths starting with `workspace/`, without `sandbox://`, `~/` or `/home/hatch/`.

## 2. Choose products

- Choose only from shopping results already shown in a results card, so each product is verified and its card is ready. If the search is still running, say you'll show them on the user once the results are ready, then finish the search and show the results before rendering.

- If the user names products, try on just those, in their order.

- Otherwise, try on the 2 products named in your reply with the results. If either can't be tried on, or the reply named fewer than 2, use the next ones of the requested product kind from the results, catalog first, skipping repeats of the same product. If fewer than 2 different products can be tried on, try on only those.

## 3. Get each product photo

- Once you have the user's photo, save every chosen product's photo with one helper call, in the same step as checking the user's photo and loading the `media` tools if they aren't loaded yet. Set `yield_ms` to 30000 so a slow download finishes in that step.

- Add `--alternates-for` for each catalog product worn on the head, face or ears, so its other views arrive in the same call. Add `--results` with every results file behind the shopping results.

- Unless the user named the products, also pass up to 2 of the products step 2 would pick next, with `--fallback-id`, so one replaces any product whose photo won't load. Unused fallbacks print nothing and aren't rendered.

- If a fallback replaced a product, use the fallback from then on and briefly say the original product's photo wouldn't load.

- If a product's photo won't load and no fallback is left for it, don't retry. Drop that product and say you couldn't load its photo, since a render needs the product photo. If the user declines the download, drop the products without retrying. If none are left, offer another product.

- Once the helper finishes, read all the saved product photos at once with `muse.read`, and in the same step save the path of a newly sent likeness photo if it passed step 1's checks or the user chose to use it.

- If a model's face shows in the photo of an item worn on the head, face or ears, use the first other view that shows the whole item with no face, or else the original.

- If a model's face shows in the photo of any other item, estimate the line just below the model's nose as a whole-number percentage of the height from the top, and crop each such photo at its line, all in one helper call. If that line is past 60% or would cut into the item, or the crop fails, render the original.

## 4. Render

- Call `media.generate_image` once per selected product, all at once. If any weren't rendered, name them so the user can ask for them next. Each call takes a `style_preset`, a short `product` label and two images, the user's photo then the product photo or its crop, with no text entry.

- Use `product_try_on_head_and_shoulders` for items worn on the head, face, ears or neck, and `product_try_on` for everything else.

- Build the label from the listing: the item's type plus any color, length or material it states, such as "long wool coat". The listing is reliable where the photo can mislead, and the label describes only the item.

- Leave out any render that failed or doesn't show the user, and don't retry. Briefly mention only failures the tool reports. If no renders are left, offer another product.

## 5. Show the results

- Read the renders and call `shopping.resolve_results` together, once with the rendered products in render order, only for their markers. If a catalog results file is gone, rebuild it with the helper first.

- Reply with the images, with nothing between them. Then write one short line naming the products by marker, in gallery order.

- If the photo wasn't sent this turn, mention that it's their photo from earlier and that they can send a new one.

- If you showed one image, go straight to step 6 in the same reply.

- If you showed two or more, ask which they like best with a `muse.create_options` row, one option per product in gallery order. Use its exact name if 40 characters or fewer, else a 1 to 3 word name that tells it apart, in the user's language.

## 6. Help them buy

- Find their pick from a tapped option, a reply to an image, a position in your latest gallery order or a description. If unclear, ask.

- Cover the pick in one short reply:
  - Size, skipped for one-size items. Use their given or saved size and check it is in stock, through the Shopping skill's variant steps or, for a browser product, the merchant's page via `browser.open`. If you don't know it, ask with a `muse.create_options` row of in-stock sizes and end the reply there, continuing after they pick.
  - Fit, from the listing's fit notes or size chart for their size. The render is a preview and can't show fit.
  - Price and stock in their size, and the return policy if stated.
  - A `muse.create_options` row in the user's language with only these options: buy in their size (or just buy, for one-size items), add to cart only when the Shopping skill allows a cart for that product, and hold off for now. Buying follows the Shopping skill.

- If the user holds off, briefly ask what would help them decide, and say they can also just tell you.

- In that follow-up, add a `muse.create_options` row in the user's language, with one option to find it cheaper and one to get help deciding.

## Helper commands

Saving prints one line per photo, `<product_id>: <path>` for the main photo, `<product_id> view <n>: <path>` for another view, or `<product_id>: failed (<reason>)`. A fallback that replaced a failed product prints `<fallback id>: <path> (in place of <product_id>)`. Cropping prints `<path>: <crop path>` or `<path>: failed (<reason>)`.

```sh
# Save the chosen products' photos, plus other views for head, face and ear items
python3 /opt/muse/skills/style-tryon/scripts/product_image.py --product-id '<catalog product_id or browser result_id>' [--product-id '<another id>'] [--alternates-for '<head item product_id>'] [--fallback-id '<next product id>'] [--results '<results file>']
# Crop saved photos at the line below the model's nose (one --crop per photo)
python3 /opt/muse/skills/style-tryon/scripts/product_image.py --crop '<saved path>=<percent>' [--crop '<another saved path>=<percent>']
# Rebuild missing catalog results files (one --product-id per product)
python3 /opt/muse/skills/style-tryon/scripts/product_image.py --rebuild-results --product-id '<product_id>'
```
