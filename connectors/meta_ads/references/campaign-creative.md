# Prepare Meta campaign creative

This stage of campaign creation turns the accepted strategy into what people see in each ad: the image or video, the text, the headline and the button. First you write a creative plan. After the advertiser accepts it, you generate the media or take it from their files or account. The advertiser approves anything you made, and then the creative moves on as described below. Approving creative doesn't create or publish anything. You should read [creative generation](campaign-creative-generation.md) before you write ad text or generate or edit any media.

## Plan the creative

- The idea should fit the business and offer something new. It can build on what the account already runs and how those ads performed, or on one existing ad, saying what's different and why it's worth trying. Product details, prices, offers and claims come from the advertiser or a verified source. Other brands' public ads can inspire, but they don't prove anything works. The plan says what evidence it's based on, and says so when there's little to go on. Tools: `ads_get_creatives`, `ads_get_ad_entities`, `ads_library_search`.

- When the advertiser provides their own media, the plan can be short. Looking at it shows whether it presents the product and message clearly, whether any text is readable on a phone, and whether other media would work better. They can use it as it is, or have new media generated from it. Media already in the account: `ads_get_ad_images`, `ads_get_ad_videos`, `ads_get_ig_media`.

- The media fits where the ad runs: 4:5 for Feed, 9:16 for Stories and Reels. When one image or video runs in all placements, the plan says once that Meta may crop or resize it. Different media for different placements needs a supported setup. An existing post can be reused where that's supported. A message ad has no website link; its button opens a chat, so chat links stay out of the copy.

- The plan has to be buildable: the formats and media work with the current tools, and the Page, destination and tracking support them.

- Copy is in the advertiser's language unless they ask for another, one language per ad, and checked for mistakes. When generation isn't available, the copy is their own words, as [creative generation](campaign-creative-generation.md) explains. Claims, logos and people in the copy or media are checked as [safety](safety.md) explains.

- The plan should follow what the advertiser already set without repeating it. If they gave a complete brief and asked for it to be made, the brief is the plan. The plan ends with options to approve or revise it.

## Approve and hand off

- For every ad, whether you made the media or the advertiser supplied it, you should ask in its own message whether it includes media created or edited with AI, with a short note on how Meta labels AI content. The question comes before you show media you made, or before the advertiser's media moves on from this stage.

- The media review should be one short sentence saying the media is ready, then the media, then `Approve this creative` (or `Approve these creatives`) and `Tell me what to change`, with nothing after. If something failed, say what's blocking it.

- The review shows one image or video for each idea, in 4:5 when the ad runs in Feed. It shows more only when the subject, layout, text or message is really different. A video's thumbnail doesn't count as its own idea. Carousel cards are listed. Media that can't be shown can't be approved.

- Approved creative moves on in the same turn, with one source per ad and nothing uploaded yet. A new campaign goes to [preview](campaign-preview.md), where the advertiser approves the whole campaign. An ad added to an existing ad set goes to [write operations](writes.md). If the advertiser is building the campaign themselves, or the account can't be changed, it goes to [manual setup](campaign-manual-setup.md).
