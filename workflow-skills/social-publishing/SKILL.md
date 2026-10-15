# Social Publishing

## Plan the content

- Identify the account or Page, the audience, the goal of the post and when it should go out. Work from the user's brief, brand voice and existing material.

- For a series or content calendar, set a cadence the user can sustain and vary formats and themes. Place each post at a date and time in the audience's timezone, around launches, holidays and local events in the audience's market.

- Keep claims supported. Quote a private message or another person publicly only with their permission, and use the platform's paid-partnership label when a post is sponsored.

## Create the media and copy

- Choose the format that suits the network and the goal, such as a short vertical video, a carousel, a single image or a text post. Explain the choice briefly when the user has not set one.

- Start from the user's own photos and videos. Generate images or video with `media.generate_image`, `media.generate_video` or a creative connector, and use another creator's work only with permission.

- Adapt each version to its destination. Check aspect ratio and crop, media order, caption length, hashtags, alt text and link behavior against the limits in each connector's docs.

- Confirm that each file is the final asset and that each link reaches the intended page.

## Get approval for the exact post

- Show the user the exact text and media for each destination, with the account, audience and publication time, before anything is published or scheduled. When the user supplied the exact text and media, the connector's own approval prompt is that check.

- Treat approval as covering only what the user saw. A changed caption, crop, media order, audience or destination needs fresh approval.

- Let delegated or scheduled work publish only the exact post the user approved. Prefer the platform's own scheduling when the connector supports it.

## Publish and verify

- Follow the connector's publishing sequence. An accepted upload is not a published post, so wait for media processing to finish and read the post back after publication.

- Never retry a publish command automatically. When a result is uncertain, look up the post or schedule first, because the first attempt may have published.

- Track each destination separately when posting to several networks, so recovering one failure cannot duplicate a post that already succeeded.

- Report a draft saved in the app, a scheduled post and a live post as different states. When editing a scheduled post, keep its identity and time unless the user asks to change them.

- Return each public link, or each scheduled time with its timezone, and name any destination that failed and why. Use [Social Content Performance](/opt/muse/skills/social-content-performance/SKILL.md) when the user later wants to know how the posts did.

## Available connectors

- [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) for personal text posts, comments and replies, and Page drafts, posts and scheduling.

- [Instagram](/opt/hatch/connectors/instagram/CONNECTOR.md) for feed posts, reels, carousels and stories.

- [Threads](/opt/hatch/connectors/threads/CONNECTOR.md) for text and media posts, carousels and replies.

- [Canva](/opt/hatch/connectors/canva/CONNECTOR.md) for designing post images and resizing a design for each network.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Facebook Internal](/opt/hatch/connectors/facebook_cli_internal/CONNECTOR.md) for personal photo and video posts, Group posts, Page posts with media and Page posting ideas.

- [Upload-Post](/opt/hatch/connectors/upload_post_mcp/CONNECTOR.md) for publishing and scheduling one post across several networks, including TikTok, LinkedIn and Pinterest.

- [Moltbook](/opt/hatch/connectors/moltbook/CONNECTOR.md) for posting as the user's agent on Moltbook, the social network for AI agents.

- [vidIQ](/opt/hatch/connectors/vidiq_mcp/CONNECTOR.md) for YouTube titles, thumbnails and scripts.

- [FLUX by Black Forest Labs](/opt/hatch/connectors/bfl_mcp/CONNECTOR.md) for generating and editing images.

- [Runway](/opt/hatch/connectors/runway_mcp/CONNECTOR.md) for generating and editing video, product marketing videos and localized ads.

- [HeyGen](/opt/hatch/connectors/heygen_mcp/CONNECTOR.md) for presenter and avatar videos and translated versions of a video.

- [Krea](/opt/hatch/connectors/krea_mcp/CONNECTOR.md) for generating images and video with a choice of models.

- [Magnific](/opt/hatch/connectors/magnific_mcp/CONNECTOR.md) for upscaling, resizing and cleaning up images, and for generating images and video.

## Websites

- Use these through `browser.spawn_task` for networks without a connector. Carry the exact approved text, media files and publication time into the task, have it publish only that version and return the live link or scheduled time.

- [LinkedIn](https://www.linkedin.com/) for personal posts and posts from company Pages the user administers.

- [YouTube Studio](https://studio.youtube.com/) for uploading and scheduling videos.

- [TikTok Studio](https://www.tiktok.com/tiktokstudio/) for uploading and scheduling TikTok videos.

- [Pinterest](https://www.pinterest.com/) for Pins and boards.

- [X](https://x.com/) for posts on X.

- Use the [Facebook](https://www.facebook.com/) site only for a personal photo or video post when Facebook Internal is not available, since the Facebook connector publishes personal posts as text only.

- Use the [Instagram](https://www.instagram.com/) site only to edit a caption or to delete or archive a post, which the Instagram connector cannot do.

## Alternatives for better results

- Post when the account's own audience is most active, using its insights rather than generic best times.

- Repurpose one strong asset across networks with a native edit for each, rather than posting identical copies everywhere.

- Change one thing at a time across posts, such as the opening line, the format or the posting time, so the results show what made the difference.
