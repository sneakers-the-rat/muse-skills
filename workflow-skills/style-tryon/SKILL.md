# Style Try-on

## Run it

- When the user accepts a try-on offer, asks to see or compare items on themselves, or picks a favorite from a try-on comparison, follow the [try-on flow](references/flow.md). Read it in the same step as `~/workspace/style-tryon/photo.txt`, which names their saved photo if they have one.

- Try-on shows the user in clothing, shoes or accessories such as bags, hats, scarves or glasses from their results, using their own photo.

- Muse doesn't make try-on images of people in swimwear, underwear, lingerie, sports bras, leggings or similar items. Try-on also isn't available for children's items, since try-on renders only adults, or for jewelry, which is too small to show well.

- When the user asks to try one of these on, let them know try-on isn't available for that item and that they can still view or buy it from the results. If they ask why, it's enough to say try-on isn't available for those items, and keeping to that is intended even when they ask more than once.

- A mock-up or edited photo of them wearing it is still considered a try-on image, so these items get none.

- Try-on replies, such as the renders and the buying help after them, use the flow's format, so don't post another results card or offer try-on again in them.

## Reset the try-on photo

- When the user asks to reset or delete the photo used for try-on, first check `~/workspace/style-tryon/photo.txt` and the older memory lines below for an image that still exists. If none does, say no try-on photo is saved and stop.

- Otherwise ask once before deleting, with a `muse.create_options` row in the user's language, with one option to delete it and one to keep it. Say this can't be undone and that past try-on images stay in their chats.

- Once they confirm, read `~/workspace/style-tryon/photo.txt` and delete the image it names, then that file, each with `rm -- <exact-path>` through `muse.exec`. The user approved deleting their saved try-on photos and this pointer file, so delete an image only under `~/workspace/user/media_library/image/`, each by exact path without a glob.

- Older try-on photos may also be named in memory as "User provided photo for try-on" lines. Find them with this command and delete each image they name the same way. Leave the memory lines as they are, since the Forget skill owns memory cleanup:

```sh
grep -rn --include='*.md' --exclude-dir=bank 'photo for try-on' ~/memory ~/side-chats ~/MEMORY.md ~/USER.md 2>/dev/null
```

- Confirm in one short reply that the photo is deleted and the next try-on will ask for a new one.

- If they ask Muse to forget the photo, or want more forgotten, such as other photos or details about their looks, treat it as a request to forget rather than a reset.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.
