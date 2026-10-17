# Product shots

- Offers edits for product shots. The item stays unchanged and not misrepresented, captions are real facts.
Show user previews of the images and tell which images are AI-edited.

## Workflow

- Before `facebook-cli marketplace listing create` with photos the user
supplied, follow
[Marketplace listing touch-ups](references/marketplace-photos.md).
- Offer choices with `muse.create_options` in the user's language.
- Before waiting for the user's pick or choice, mark any to-do items that
depend on it as blocked.

### 1. Style

- Offer style options: "Studio", "Lifestyle" or "Keep my
setting".
- Studio is a light-grey studio backdrop. Lifestyle is where the item is
normally used, with decor kept apart from it.
- For website photos offer these styles instead: "Store white", "Match my store"
or "Lifestyle".
- "Match my store" needs a screenshot of their product page
or one photo from their store link.

### 2. Polish

- Make one `media.generate_image` edit per photo,
`output_dir` `workspace/product-shots/` and `output_format` `jpg`.
- Include in each image prompt, "Keep the item exactly as it is: same angle, size, position,
shape, color, text, logos and wear. Do not add anything that touches it."
- "Store white" may center the item. "Match my store" passes the store photo as
a second image, for its background and lighting only.
- Compare each result with its original. If the item changed, something new
touches the item, or it moved when the style didn't call for that, use the
original instead, say so in one line.

### 3. Captions

- Add caption per photo and one for a carousel, using facts the user
gave or visible in the photo.
- Add hashtags if the user asks for it.

### 4. Share

- Sharing options: run `instagram-cli accounts` once, silently, share options
"Post on Instagram" if it found an account, "Post to my Facebook Page", "Get
files for my website" and "Not now". Inform the user if Instagram isn't linked.
- Wait until the
user picks Facebook before running `facebook-cli pages list`, since it can
show a consent card.
- With two or more photos, ask whether to post them "Together" (one carousel) or
"Separately".
- Try other styles: follow
[Product shots other styles](references/other-styles.md).

- **Instagram:** use `post-feed` from the instagram skill, pad with white
instead of cropping.
- **Facebook Page:** like the
  facebook_cli skill's `references/pages.md` describes.
- **Get files for my website:** follow [Product shots website
pack](references/website-pack.md).

## Available connectors

- [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md)
- [Instagram](/opt/hatch/connectors/instagram/CONNECTOR.md)
