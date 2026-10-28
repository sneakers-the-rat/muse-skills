# Product shots

Only for photos of items, including items a person wears or holds to sell. If
  the subject is a person, a selfie or a pet or other animal, or the listing is
  for one, stop and help without this skill.

Label AI-edited photos in previews. Use `muse.create_options` in the user's language.
  In touch-up and photo-picking steps, a message with options or a picker
  asks nothing else.

Follow [Touch-ups](references/photo-touch-ups.md), or [Marketplace](references/marketplace-photos.md)
  for listings.

Finish choices first. Write a caption per photo and one for a carousel,
  using supplied facts. Hashtags and [other styles](references/other-styles.md)
  only on request.

Verify the linked Instagram account once, silently, following its connector
  steps and reusing an account result already in context. Offer linked
  Instagram, Facebook Page, [website files](references/website-pack.md) or
  "Not now". If Instagram is unlinked, say so in one line. Run Facebook Page
  commands only after the user picks Facebook. Follow connector steps.

With two or more photos, ask "Together" or "Separately".
  Preview photos and captions; confirm posts,
  drafts and changes. Never automatically change or repeat posts or listings.

Instagram: `post-feed`, white padding. Use the Facebook connector's
  `references/pages.md` for Page posts.

## Available connectors

- [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md)

- [Instagram](/opt/hatch/connectors/instagram/CONNECTOR.md)

- Find others with `muse.connector_search`.
