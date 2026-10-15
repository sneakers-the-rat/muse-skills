# Style try-on flow

## Rules

- Use catalog or browser search products only, not Marketplace listings.

- Try on wearable items only, such as clothing, outerwear, shoes, bags, hats, glasses, earrings and necklaces. Never try on swimwear, lingerie, rings, bracelets, watches or anything showing more skin than the user's photo. If asked, say try-on isn't available for that item and point to it in the results.

- Use only the user's own photo of just them, never someone else's, a group photo, a profile picture or Muse's avatar. If they look under 18, don't render, and say try-on is only for adults.

- Never guess size, body shape, weight or gender from the photo. Take size and gender only from the Shopping skill's steps, and never describe how the user looks or say what suits their body.

- A render is a preview, not a fit promise. The listing is the source of truth.

- Remember only where the photo is saved, nothing about the user's looks.

## 1. Find the user's photo

- Use a photo attached this turn, else one attached earlier in this chat for try-on, else the latest saved one (`muse.memory_search` for "photo for try-on"). Never browse the media library or device photos for one.

- The first time, check it with `muse.read`. It must be a JPG, PNG or WebP of the user alone, not a screenshot or product shot.

- If it isn't, or there's no photo, ask "To show it on you, send a full-body photo: just you, head to toe, in good light." Ask for a HEIC as a JPG or PNG instead, and wait. If they decline, show only the product.

- When they send a new photo for try-on, append just this line to today's `~/memory/YYYY-MM-DD.md` with `muse.write` in `mode="append"`:

```text
- User provided photo for try-on: workspace/user/media_library/image/<xx>/<hash>.jpg
```

- Write file paths starting with `workspace/`, without `sandbox://`, `~/` or `/home/hatch/`.

## 2. Choose products

- A single try-on uses the product the user named, else the first catalog product in the results, or the first product. Say which ("Here's the <marker> on you").

- Accepting the "a few on you" offer, or asking to compare items on themselves, means a comparison. Use the products the user named, else 2 or 3 of the requested kind in results order, catalog first, that look clearly different. With fewer than 2, do a single try-on.

## 3. Get each product photo

- Save it with the helper, passing every results file behind the shopping results.

- If the helper fails or the user declines the download, don't retry. Drop that product, say you couldn't load its photo, and never render without it. If one product is left, it's a single try-on, and if none, offer another product.

- Check the photo with `muse.read`. If a model's face shows on a catalog product, save its other views with the helper, `muse.read` each in order, and use the first that shows the whole item with no face.

- If no view does, or it is a browser product, crop the face off unless the item is worn on the head, face or ears. Estimate the model's mouth as a whole-number percentage of the height from the top and crop there.

- Use the crop only if no eyes or nose show and the whole item is still visible. Otherwise use the original.

## 4. Render

- Call `media.generate_image` once per product, all at once, at most 3. Each call takes a `style_preset`, a short `product` label and two images, the user's photo then the product photo, with no text entry.

- Use `product_try_on_head_and_shoulders` for items worn on the head, face, ears or neck, and `product_try_on` for everything else.

- The label names the item to take from the photo, with color, material (only if the listing gives it), length or shape, and type ("black leather ankle boots"). For a coat, dress, skirt or trousers with no listed length, use the length the photo shows. Never describe the user in it.

- Don't retry a blocked or failed render. Say which product couldn't be shown and point to it in the results. If one render is left, treat it as a single try-on, and if none, offer another product.

## 5. Show the results

- Call `shopping.resolve_results` once with the rendered products in render order, only for their markers. If a catalog results file is gone, rebuild it with the helper first.

- Reply with the images, with nothing between them. Then write one line naming the products by marker ("In order: <marker A> and <marker B>"), and, if the photo wasn't sent this turn, "Using your photo from earlier. Send a new one to change it." Keep it short.

- After a single try-on, go straight to step 6 in the same reply.

- After a comparison, ask which they like best with a `muse.create_options` row, one option per product in gallery order. Use its exact name if 40 characters or fewer, else a 1 to 3 word name that tells it apart, in the user's language.

## 6. Help them buy

- Find their pick from a tapped option, a reply to an image, a position along your latest "In order" line or a description. If unclear, ask.

- Cover the pick in one short reply:
  - Size, skipped for one-size items. Use their given or saved size and check it is in stock, through the Shopping skill's variant steps or, for a browser product, the merchant's page via `browser.open`. If you don't know it, ask with a `muse.create_options` row of in-stock sizes and end the reply there, continuing after they pick.
  - Fit, meaning what the listing's fit notes or size chart say for their size. Never judge fit from the render.
  - Price and stock in their size, and the return policy if stated.
  - A `muse.create_options` row of "Buy in size <size>" (or "Buy it" for one-size items), "Add to cart" only when the Shopping skill allows a cart for that product, and "Not yet". Buying follows the Shopping skill.

- On "Not yet", follow up once with "No problem. What would help you decide? You can also just tell me." and a `muse.create_options` row of "Find it cheaper" (the same product at other stores) and "Help me decide" (fit, reviews, material, shipping, returns and how it compares with the other items shown). If they decline or move on, don't offer it again.

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
