# Style try-on flow

## Rules

- Use catalog or browser search products only, not Marketplace listings.

- Try on wearable items only, such as clothing, outerwear, shoes, bags, hats, glasses, earrings and necklaces.

- Swimwear and lingerie aren't supported because the renders would be too revealing, and rings, bracelets and watches are too small to look right. If asked, say try-on isn't available for that item and point to it in the results.

- Renders use a photo of the user, not an inspiration or product photo showing someone else. If they look under 18, skip the render and say try-on is for adults.

- Take size and gender only from the Shopping skill's steps. Don't guess them from the photo or comment on the user's body or looks, since those remarks can be hurtful.

- A render is a preview, not a fit promise. The listing is the source of truth.

- Remember only where the photo is saved, nothing about the user's looks.

## 1. Find the user's photo

- Use the photo the user attaches for try-on, else the latest photo they sent for try-on earlier in this chat, else the latest saved one from `muse.memory_search` for "photo for try-on". Their social profile photos (including `~/workspace/profile-images/`) and media library aren't try-on sources, because the user didn't choose them for this.

- If none of these gives a photo, ask the user for a photo of themselves in good lighting, mentioning that a full-body photo works best, and wait. If they decline, show only the product.

- Check each newly sent photo with `muse.read` before using or saving it, and a saved photo before its first render in a chat. If it won't open, ask for another.

- If the photo isn't a real photo of only one person, ask for another.

- When a newly sent photo passes these checks, append just this line to today's `~/memory/YYYY-MM-DD.md` with `muse.write` in `mode="append"`:

```text
- User provided photo for try-on: workspace/user/media_library/image/<xx>/<hash>.jpg
```

- Write file paths starting with `workspace/`, without `sandbox://`, `~/` or `/home/hatch/`.

## 2. Choose products

- A single try-on uses the product the user named, else the first catalog product in the results, or the first product. Say which ("Here's the <marker> on you").

- Accepting the "a few on you" offer, or asking to compare items on themselves, means a comparison.

- For a comparison, use the products the user named. If they named none, pick up to 3 of the requested kind in results order, catalog first, skipping repeats of the same product.

## 3. Get each product photo

- Save it with the helper, passing every results file behind the shopping results.

- If the helper fails or the user declines the download, don't retry. Drop that product and say you couldn't load its photo, since a render needs the product photo. If none are left, offer another product.

- Check the photo with `muse.read`. If a model's face shows on a catalog product, save its other views with the helper, `muse.read` each in order, and use the first that shows the whole item with no face.

- If no view does, or it is a browser product, crop the face off unless the item is worn on the head, face or ears. Estimate the model's mouth as a whole-number percentage of the height from the top and crop there.

- Use the crop only if no eyes or nose show and the whole item is still visible. Otherwise use the original.

## 4. Render

- Call `media.generate_image` once per product, all at once, at most 3. Each call takes a `style_preset`, a short `product` label and two images, the user's photo then the product photo, with no text entry.

- Use `product_try_on_head_and_shoulders` for items worn on the head, face, ears or neck, and `product_try_on` for everything else.

- Build the label from the listing: the item's type plus any color, length or material it states, such as "long wool coat". The listing is reliable where the photo can mislead, and the label describes only the item.

- Leave out any render that failed or doesn't show the user, and don't retry. Briefly mention only failures the tool reports. If no renders are left, offer another product.

## 5. Show the results

- Call `shopping.resolve_results` once with the rendered products in render order, only for their markers. If a catalog results file is gone, rebuild it with the helper first.

- Reply with the images, with nothing between them. Then write one line naming the products by marker ("In order: <marker A> and <marker B>"). Keep it short.

- If the photo wasn't sent this turn, add "Using your photo from earlier. Send a new one to change it."

- If you showed one image, go straight to step 6 in the same reply.

- If you showed two or three, ask which they like best with a `muse.create_options` row, one option per product in gallery order. Use its exact name if 40 characters or fewer, else a 1 to 3 word name that tells it apart, in the user's language.

## 6. Help them buy

- Find their pick from a tapped option, a reply to an image, a position along your latest "In order" line or a description. If unclear, ask.

- Cover the pick in one short reply:
  - Size, skipped for one-size items. Use their given or saved size and check it is in stock, through the Shopping skill's variant steps or, for a browser product, the merchant's page via `browser.open`. If you don't know it, ask with a `muse.create_options` row of in-stock sizes and end the reply there, continuing after they pick.
  - Fit, from the listing's fit notes or size chart for their size. The render is a preview and can't show fit.
  - Price and stock in their size, and the return policy if stated.
  - A `muse.create_options` row of only these options: "Buy in size <size>" (or "Buy it" for one-size items), "Add to cart" only when the Shopping skill allows a cart for that product, and "Not yet". Buying follows the Shopping skill.

- If the user taps "Not yet", briefly ask what would help them decide, and say they can also just tell you.

- In that follow-up, add a `muse.create_options` row of "Find it cheaper" and "Help me decide".

## Helper commands

```sh
# Save the product photo
python3 /opt/muse/skills/style-tryon/scripts/product_image.py --product-id '<product_id>' --results '<results file>' [--results '<another results file>']
# Save up to three other views of a catalog product
python3 /opt/muse/skills/style-tryon/scripts/product_image.py --product-id '<product_id>' --results '<results file>' --alternates
# Crop a saved photo at the mouth line
python3 /opt/muse/skills/style-tryon/scripts/product_image.py --from-file '<saved path>' --crop-top-percent <mouth percent>
# Rebuild missing catalog results files (one --product-id per product)
python3 /opt/muse/skills/style-tryon/scripts/product_image.py --rebuild-results --product-id '<product_id>'
```
