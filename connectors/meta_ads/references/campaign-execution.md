# Create the paused campaign

This stage creates the campaign after the advertiser approves the [preview](campaign-preview.md). It turns the approved decisions into exact create arguments, then creates everything paused.

## Prepare the arguments

- The live schemas of `ads_create_campaign`, `ads_create_ad_set`, `ads_create_creative` and `ads_create_ad` decide the arguments, plus `ads_creative_upload_media` when there's new media. Every argument comes from the schema and an approved decision: a field the schema doesn't list isn't supported, optional fields stay out unless they carry an approved setting, and names and values are copied exactly. The schema is learned by reading it, not by trying a write.

- If the schema needs a value the advertiser didn't give and no read returned, that decision goes back to them, with a new preview.

- The budget sits at one level, campaign or ad set, in the account's own currency. Housing, employment and financial ad sets include `targeting_as_signal: 0`. The server creates campaigns, ad sets and ads paused, so no status field is added.

- When a schema has `advertiser_request`, it gets the advertiser's full current wording.

## Message ads

An ad set with a Messenger, WhatsApp or Instagram Direct destination makes a message ad, whatever the objective. Its creative has no website link; the button opens a chat:

- Messenger: button `MESSAGE_PAGE`, link `https://fb.com/messenger_doc/`.

- WhatsApp: button `WHATSAPP_MESSAGE`, link `https://api.whatsapp.com/send`. It needs a WhatsApp number connected to the Page.

- Instagram Direct: button `INSTAGRAM_MESSAGE`, link `https://www.instagram.com/`, with the Page's Instagram account as `instagram_user_id`.

`instagram_user_id` takes only an account `ads_get_ig_accounts` returned for this ad account. If none comes back, or the create rejects it, the field is left out and the ad runs on the Page. Only an Instagram Direct or Instagram profile destination needs the account itself. When a channel's requirement is missing, tell the advertiser what to connect.

## Create the campaign

- Only the approved arguments run, in this order:
  - You should upload each approved new image or video with `ads_creative_upload_media` before creating the campaign.
  - Call `ads_create_campaign` once and keep its campaign ID.
  - Call `ads_create_ad_set` once per ad set with that ID, and `ads_create_creative` once per creative, using the `image_hash` or `video_id` the upload returned. Only calls that don't depend on each other run in parallel.
  - Call `ads_create_ad` once per ad, after its ad set and creative exist.
- Approved media is passed like this: a generated image as its returned `media_handle`, or its `local_path` as `file` when no handle came back; a generated video as its `local_path` as `file`, with a still frame as its thumbnail; another asset as its known `media_handle`; otherwise a local `file`, downloading a web link first. An existing account image hash or ready video ID is used directly.

- Creation worked when every campaign, ad set and ad returns its ID with status `PAUSED`, and every creative returns its ID. Those results are the check, so a clean create isn't read back. A child's status isn't assumed from its parent.

- An `ACTIVE` result means stop: pause it with an update, check the state and report it, and create nothing under it.

- If a successful result is missing its ID or status, read that object once with the live read tool. If it's missing or isn't paused, there's no success card or publish option.

- If an argument or decision changes after approval, stop, update only what's affected, reprice if needed and show a new preview.

- After a verified success, continue with [handoff](campaign-handoff.md).

## Recover from failures

- After a failure, check the account's current state before any other write. Report only objects you've confirmed, with their status, and the first stage that didn't finish. Uploaded media counts as existing even when no campaign, ad set, creative or ad was created, so say "No Ads objects were created", not "nothing was created".

- Describe the failure as returned, without guessing at a cause. Say "everything validated" or "the last step" only when every step behind it finished.

- Some rejections name something only the advertiser can fix, such as no payment method or unaccepted Lead Ads terms. You tell them what it is and where to fix it, as [write operations](writes.md) describes. When they say it's fixed, you read the account or Page again before you retry.

- Retries follow [write operations](writes.md#retry-and-verify).
