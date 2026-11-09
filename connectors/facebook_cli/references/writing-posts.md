# Writing Facebook posts

- These commands are useful for publishing text updates<!-- facebook-profile-media-only:start --> and photo/video posts<!-- facebook-profile-media-only:end --> to the user's own Facebook profile<!-- facebook-group-posts-only:start --> or to a Group they can post in<!-- facebook-group-posts-only:end -->. A native approval shows the exact post, audience and sharing destinations so the user can confirm who will see it.

- If the conversation already shows the user manages a Page and they didn't say where to post, ask whether the post<!-- facebook-profile-media-only:start --> or Reel<!-- facebook-profile-media-only:end --> should go to their personal profile or to a Page they manage.

## Publish a post

```sh
/opt/hatch/bin/facebook-cli post create --message 'Exact post text'
<!-- facebook-group-posts-only:start -->
/opt/hatch/bin/facebook-cli post create --group-id '<numeric id from groups search>' --message 'Exact post text'
<!-- facebook-group-posts-only:end -->
<!-- facebook-profile-media-only:start -->
/opt/hatch/bin/facebook-cli post create \
  --message 'Exact post text' \
  --file '<path to photo or video>' \
  --file '<path to another photo or video>' \
  --media-caption '1=<caption for the first file>' \
  --media-caption '2=<caption for the second file>'
<!-- facebook-profile-media-only:end -->
```

- Audience and sharing for a profile post follow the user's current Facebook defaults<!-- facebook-group-posts-only:start -->, and a post without `--group-id` goes to the profile<!-- facebook-group-posts-only:end -->. The approval displays those choices for confirmation.

<!-- facebook-group-posts-only:start -->
- With `--group-id`, the post goes to that Group, and the Group decides who sees it. Leave out `--privacy` and the sharing flags, because `post create` rejects them for a Group post. If more than one Group in the `groups search` results matches what the user described, ask which one to post to.
<!-- facebook-group-posts-only:end -->

- Drafting or revising post content does not publish the post. Preserve the user’s final post content unless they ask you to edit it.

<!-- facebook-profile-media-only:start -->

- A Reel is a post with one video and no other media. `--message` is its caption.

- PNG, JPEG and MP4 attachments are supported.

- On a confidential VM, a video can be at most 100 MB, and a larger one is refused before approval. Ask the user for a shorter or smaller file.

- If the user shares an unsupported attachment, explain which formats work and ask how they'd like to proceed. Convert a file only when the user clearly asks for that, since approval to post the original file is not a request to convert it.

- `post create` both stages the media for publishing and publishes the attachment.

- A post may have an overall caption, as well as individual captions for each media attachment.

- A single photo or video shares the post text, so omit `--media-caption` or use identical text. A media-only post omits `--message`.

- Pass each photo or video file with `--file`, in post order. Number `--media-caption` in that same order, starting at 1.

<!-- facebook-profile-media-only:end -->

## Change a profile post's audience or sharing

- If a different audience is requested, read the available choices and pass a returned ID or exact name with `--privacy`:

```sh
/opt/hatch/bin/facebook-cli post audiences
/opt/hatch/bin/facebook-cli post create \
  --message 'Exact post text' \
  --privacy '<returned audience ID or exact name>'
```

- Only me, Friends, and Public are supported when returned. Custom audiences and per-person inclusions/exclusions are currently unavailable. Sharing settings and destination eligibility are available through:

```sh
/opt/hatch/bin/facebook-cli post crossposting
/opt/hatch/bin/facebook-cli post crossposting --privacy '<returned audience ID or exact name>'
```

- Omit audience and sharing flags to use Facebook defaults. The command resolves and displays them.

- `auto_share` describes the account setting. `eligible` describes whether this post can use that destination.

- For a requested sharing change, include `--share-to-story`, `--share-to-instagram` or `--share-to-threads` with `on` or `off` in the creation command. These choices apply to that post, leaving account settings unchanged.

- If `post create` rejects the audience or a sharing destination, nothing was posted. Tell the user, run `post audiences` again to show the current choices, and ask which one to use. A rejected audience fails again under any ID or spelling.

- Do not select a different audience or destination without the user's prompting.

- After a denied approval, say nothing was posted and stop. Do not suggest another destination.

## Confirm the outcome

- A receipt with `post_id` and either no `state` or `state: published` confirms publication. An empty read after a confirmed receipt does not justify posting again.

<!-- facebook-group-posts-only:start -->
- `state: pending_approval` means the post is in the Group's admin approval queue and appears in the Group only after an admin approves it. The post already exists, so posting again would create a duplicate.
<!-- facebook-group-posts-only:end -->

- Show any returned `post_url` as a clickable link.

<!-- facebook-profile-media-only:start -->
- `state: processing` means Facebook accepted a video post and returned a `story_id` while processing continues. Read it with `facebook-cli post read --story-id '<returned story_id>'`. If a returned link is available, surface it to the user.
<!-- facebook-profile-media-only:end -->

- A timeout, interrupted response, or unknown outcome may mean the post was created. Another write should not be attempted without the user’s request. Use [Reading posts](/opt/hatch/connectors/facebook_cli/references/reading-posts.md) to reconcile the attempt. If readback cannot confirm the outcome, report it as unconfirmed and ask the user to check Facebook before another attempt.

- Report that nothing was posted only when approval was denied or the service explicitly confirms rejection. Otherwise, treat an uncertain outcome as unconfirmed.

## Related actions

- [Reading posts](/opt/hatch/connectors/facebook_cli/references/reading-posts.md) for inspecting a published update.

- [Page publishing](/opt/hatch/connectors/facebook_cli/references/pages-publishing.md) for publishing as a Page.

<!-- facebook-group-posts-only:start -->
- [Groups](/opt/hatch/connectors/facebook_cli/references/groups.md) for finding a Group and its `id`.
<!-- facebook-group-posts-only:end -->
