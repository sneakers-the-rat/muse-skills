# Prepare Meta campaign creative

- Read this for every planned creative format, once the delivery strategy and budget are accepted. Read policy only when the category or content needs it, and expect final execution to recheck every create and upload shape against its live schema.

## Research and present the creative plan once

- Read `ads_create_creative` with `describe-tool --input-only` before proposing a format, and the upload schema too when source compatibility affects the choice. These reads authorize neither upload nor creation.

- Inspect only relevant account images, videos and creatives, plus Page or Instagram media when applicable, looking at the media itself rather than filenames, labels or metadata. Follow pagination before saying no suitable asset exists, and preview an existing asset before recommending it or offering it as a source.

- Recommend one buildable format from the goal and evidence, never claiming an unproven performance advantage. If it needs a material change to structure or budget, return to planning and reprice first.

- Keep the plan source-neutral until the advertiser chooses a source. Describe the intended visual outcome rather than saying it will be generated, uploaded, photographed or reused, and take product appearance, materials, price, offer, availability, claims and destination only from the advertiser or verified evidence.

- Creative-market research belongs here. Use `ads_library_search` only when public examples could change the concept, format, message, offer treatment or call to action, with one focused query, one simplification if it finds nothing and at most three results or snapshots inspected.

- Public ads prove use, never performance. Skip the lane when it cannot change the recommendation, treat a failure as missing evidence, and keep research and tool names backstage.

- Ground a new visual in the account's best ads before writing the plan, as a required step. Read ad-level results with `ads_get_ad_entities` at `level=ad`, sorted by the goal's results over a recent window, preview the one to three best ads with enough delivery to judge and say what they share, such as palette, typography, composition, hook or format, without promising the new ad will match them.

- Listing what is running or recent is not this step, because only results rank ads, and when no ad has enough delivery, say so in the plan. Unless you already have them, ask once, alongside the source choice, for reference images, the logo and brand colors or fonts, and say what each reference contributes without repeating its concept.

- Present one executable plan in natural prose covering:
  - what people will see, the composition or sequence, style, format and each buildable placement shape
  - the exact primary text, headline, description, button, destination and in-image text, or the advertiser's own wording where their category leaves the words to them
  - material constraints and only the evidence that changed the recommendation

- Write the words in the language the ads will run in, which is the advertiser's unless they name another, and keep each ad in one language. Reread non-English copy for spelling, accents and agreement, because a typo ships to everyone who sees the ad.

- Do not recap the approved strategy. Create one source-action `muse.create_options` widget first, then write the complete plan with its token after it, never sending part of the plan as commentary or the picker alone.

- Offer every viable action, such as `Upload my own creative`, `Generate this creative`, a specific suitable account asset and `Revise the creative plan`. If the advertiser already chose a source, show only its matching action and the revision, and a generic ad request with no supplied media leaves the source open.

- Choosing generation or an account asset accepts this exact plan and authorizes only that preparation. An upload waits for the advertiser's asset, then completes or revises the plan before preparation.

- If one consequential creative question remains open, ask only that, then present the complete plan with its source actions. Skip the plan gate only for an equally complete same-context brief with an explicit request to prepare it.

- Privately check the creative against the goal, optimization, destination and tracking, compliance, audience, structure, placements and budget, and make sure everything the visual shows fits what is sold. A material conflict returns to the earliest affected decision, adding a concept or format needs a revised plan, and accepting the plan never approves the finished media.

## Message ads

- An ad set whose `destination_type` is `MESSENGER`, `WHATSAPP` or `INSTAGRAM_DIRECT` makes a message ad, whatever the objective. It has no web destination, so never ask the advertiser for one, and use the channel's button and standard `link_url`:
  - Messenger uses `MESSAGE_PAGE` with `https://m.me/<page_id>` and needs the returned Page ID
  - WhatsApp uses `WHATSAPP_MESSAGE` with `https://api.whatsapp.com/send` and needs a WhatsApp number connected to the Page
  - Instagram Direct uses `INSTAGRAM_MESSAGE` with `https://www.instagram.com/` and needs the Page's connected Instagram account as `instagram_user_id`

- Never guess a Page or Instagram ID. When a channel's prerequisite is missing, say what the advertiser must connect instead of building the ad, describe the button as opening a chat and keep these links out of the copy.

- `instagram_user_id` takes only an ID `ads_get_ig_accounts` returned for this ad account. When none is returned, or a create rejects it as not a valid Instagram account ID, leave the field out and build the ad on the Page, because only an Instagram Direct or Instagram profile destination needs the account itself.

- Never say an Instagram account must be connected before an ad can publish because of that rejection. When Instagram placements are in the plan, say no Instagram account is linked to the ad account and that linking one would show their Instagram profile on those ads.

## Categories where generated creative is unavailable

- Generating images, video and ad copy is switched off for ads about social issues, elections or politics, housing, employment, financial products and services, healthcare, pharmaceuticals, education, alcohol and gambling. For those, generate no part of the creative through any generator, including no primary text, headline, description or in-image words in a plan, where the advertiser's own wording takes their place.

- Generating from the advertiser's own media is generation too. `creative generate-image --source-image` and animating their image with `media.generate_video` are off as well.

- The advertiser's own image or video stays available, including one they made with their own AI tool, carried to the usual `self_ai_disclosure` step. It can run as supplied across automatic placements, with one note that Meta may crop or resize it, or go to Meta's own enhancements through `advantage_plus_creative` or a named feature such as `image_animation` in `advantage_plus_creative_features`.

- Their own copy is staged as given and still checked as [safety](safety.md) requires, including declining what it says to decline. Fitting their words to a length limit or fixing a typo is not writing them, while offering a headline they did not ask for is.

- Social issues, elections or politics is the single stricter case, with no generation, no Meta enhancements and no reshaping of their words. Their own media and copy run exactly as supplied.

- Everything that is not the creative stays available, which is most of the work, including the objective, audience, budget, placements, campaign build, optimizing what already runs and policy answers. Never let this become a refusal to help.

- The category follows what is advertised, as [safety](safety.md) explains. A charity asking for donations to fund its own services is not in it, but the same charity is once the ad argues a political issue or leans on a named law, bill or election.

- This is product availability, not a quotation. Say generated creative is not available for this ad, and never say or imply that Meta policy prohibits the ad, its media or its words.

## Generate media

- Images come only from `creative generate-image`, never `media.generate_image`, which carries no placement shape, ratio check or the rules below. Select `feed`, `story` or `reel`, and the CLI owns the exact ratio and rejects a generated file whose measured dimensions do not match.

```sh
/opt/hatch/bin/meta-ads-cli creative generate-image --placement feed --prompt '<advertiser request, verbatim>' --prompt '<separate constraint>' --output-dir workspace/your_files
```

- Pass the advertiser's request verbatim as the prompt, with separate visual constraints as separate entries in order. Add `--source-image <path>` only to adapt the selected workspace image.

- Video comes from `media.generate_video` with the same verbatim request and `output_dir` set to `workspace/your_files`. It sets no ratio, so state the placement's shape in the prompt, 9:16 for Stories and Reels or 4:5 for Feed, then measure the file, and a clip that does not fit is a failed adaptation that reopens the plan rather than a reason to generate again.

- A single-video ad needs a thumbnail. Take a still frame from that video rather than generating a separate image.

- Verbatim does not mean uncritical. Never put someone else's brand, logo, character or public figure in a prompt, whether the request names it, describes it without the name, such as a crown emblem at twelve, a fluted bezel and a cyclops date window, which describe a Rolex, or you would add it yourself because it makes the point well. Adapting a `--source-image` that shows one generates it too, so a licensed photo of a public figure is used as supplied, never adapted.

- Someone else's mark is the whole test, not a brand name appearing. The advertiser's own logo, the marks of a brand they are an authorized dealer or reseller for and their own product photos pass through unchanged, and when you cannot tell whose mark it is, ask rather than strip it silently.

- Never make a restricted good the subject of a generated image or video, such as tobacco including cigars and vapes, alcohol, cannabis and other drugs, weapons or gambling, whoever asks and whatever they lawfully sell. When generation is available for the ad at all, take the brief and show the surroundings instead, such as the room, the people, the occasion, the craft or the packaging they supply.

- An ad that is itself about alcohol or gambling already has generation closed, so never offer to draw around the subject. Offer the advertiser's own media as supplied, or Meta's enhancements, in the same breath, so the request is redirected rather than refused.

- Incidental is not the subject. A glass of wine beside a plated dish or a pub in the background of a street scene is not about the restricted good and must not be stripped.

- After the direction is accepted, a prompt may add one compact production brief with nonmaterial detail consistent with it. It may never change the subject, scene or sequence, style, source, placement shape, in-image text choice, message hook or constraints, so an unset one returns to the plan, and required in-image text is quoted verbatim.

- No image is pre-cleared. Inspect the actual selected image after generation or retrieval, not only its prompt, filename or metadata, and screen recognizable third-party likenesses, logos, wordmarks, trade dress, characters and artwork, even when unnamed or introduced by the generator.

- Advertiser-owned or licensed material stays usable, so ask when provenance is unclear. Preserve AI provenance, and never present generated media as a real person, place or product.

- A picture makes claims. Treat seals, badges, ratings, certification marks and on-image figures like written claims, where the advertiser's stated fact is enough sourcing, and never originate a proof signal they did not mention or draw an approximation of a real seal, award or rating mark.

- Generation redraws a source image rather than compositing an authentic mark, so ask for finished authorized creative when such a mark must appear. Never turn a claim the advertiser explicitly left unwritten into imagery, though ordinary visual style is not a claim, and state what the image asserts before creative approval.

- Keep each generated `local_path`, its dimensions and its `media_handle` when returned, and prefer original handles for other assets. An intentional edit makes a new asset, so never convert or edit a file just to retry.

- Resolve new assets as uploadable sources, but upload nothing in this stage. Never invent IDs, turn a thumbnail into a video, flatten carousel cards or substitute a format or source, and a missing source returns to the plan.

## Placement fit

- Before approval, check that the Page or Instagram identity supports the proposed placements and that every source meets their format and ratio requirements. When one asset serves automatic placements, say once in the plan that Meta may crop or resize it, and never present it as placement-specific creative.

- Use placement-specific media only through a supported mapping, and otherwise revise the placements or structure and reprice when delivery changes. A failed adaptation reopens the plan rather than swapping the source or format.

- Buildable sources depend on the live schema and include:
  - an image as a media handle, local file or account image hash, with the destination `link_url` an image ad needs
  - a video as a ready video ID or uploadable file, with any required thumbnail
  - a static carousel of 2 to 10 valid cards and destinations
  - a catalog carousel from a resolved, healthy product set
  - a boosted or partnership format from the exact supported post and identity

## Approve the prepared media

- Preparation never changes plan values. Before this gate, use the `ads_create_creative` input schema to resolve `self_ai_disclosure`, asking whether the ad includes media created or edited with AI, with a clear question and a brief explanation of AI labeling in the same response as the options, written after the options call.

- Wait for that answer before showing any prepared media. Then show one representative image or video per concept, preferring 4:5 when Feed is included, more only when subject, composition, text or message differs materially, and never a video's thumbnail as its own concept.

- List carousel cards as applicable. Media that cannot be shown cannot be approved, so say so instead of offering approval.

- The final response holds one short sentence that the media is ready for review, with the chosen AI declaration and labeling caveat in plain words, then the media, then exactly these options directly beneath it:
  - `Approve this creative`, or `Approve these creatives` for several ads
  - `Revise the creative`

- Then stop, with no direction, evidence, copy, call to action, destination, placement note, adaptation caveat or recap. A failure may explain its blocker.

- The affirmative option, or an unambiguous typed approval of the unchanged media shown, passes this one gate. It accepts the media with the unchanged plan, not the campaign or any write, a revision repeats the gate, and there is no separate copy approval and no promised ad preview.

## Carry approved media into execution

- Never upload during this stage, or tell the advertiser an upload is starting. Once the media is approved, take the next step in the same turn:
  - the setup guide in [manual setup](campaign-manual-setup.md) when the advertiser builds the campaign themselves or the account is write-disabled or rejected writes
  - the final review in [execution](campaign-execution.md) for a new campaign
  - the write in [write operations](writes.md) for an ad added to an existing ad set

- Keep exactly one accepted source per planned creative. Upload new media only after final campaign approval, and use an existing account image hash or ready video ID directly.

- Carry new media this way:
  - a generated image as its returned `media_handle`, or its exact `local_path` as `file` when no handle came back
  - a generated video as its exact `local_path` as `file`, with its still frame as the thumbnail, carried the same way
  - another asset as a known `media_handle`, including a matching earlier upload-only result
  - otherwise a local `file`, downloading external URLs first

- Never use `snapshot_id`, pass a URL, compute a hash, switch source after a failure or use another upload entry point. Creation takes only account image hashes, ready video IDs with thumbnails, or approved sources that `ads_creative_upload_media` uploads after final approval.
