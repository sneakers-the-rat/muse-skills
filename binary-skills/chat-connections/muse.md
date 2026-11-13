- On web: there is a Download option on Library items, and a public share link available from an artifact's Share dialog. There is no share-to-message action on web.
- {{ARTIFACT_SHARE_MENU_ITEM}} in a page or app's menu gives its link.
No share-message action on web. Sharing an artifact means creating a public link from the artifact's Share dialog. Put the content in chat or an artifact, then point the user to their own share option.
{{ARTIFACT_SHARE_MENU_ITEM}}, in a page or app's menu, creates its link; `~/docs/artifacts.md` explains who can open it. Put the content in chat or an artifact, then point the user to their own share option.
{{ARTIFACT_SHARING_GUIDANCE}}ShareInviteShare link{{ARTIFACT_SHARE_MENU_ITEM}}Share link in the space's menu publishes a page or app as a public copy.
The copy starts with the space's data, then keeps its own. Platform
locations are in `~/docs/client-surfaces.md`.

- The copy updates only when the user taps Sync updates. Data never syncs.
- To publish, sync, or take a link down, open Share link with `ui.navigate`
  target `space.share` if `ui.list` shows it; the user decides there. Otherwise,
  tell them where it is. It's the only way to get a link
  others can open: an uploaded or exported page downloads as a file instead of
  opening.
Publishing gives a page or app a public share link. Invite is in its menu;
platform locations are in `~/docs/client-surfaces.md`.

- Shared pages and apps usually publish later successful builds.
  `artifact.unshare` takes a link down.
- To publish or change sharing, open Invite with `ui.navigate` target
  `space.share` if `ui.list` shows it; the user decides there. Otherwise,
  tell them where Invite is. Invite is the only way to get a link
  others can open: an uploaded or exported page downloads as a file instead of
  opening.
{{ARTIFACT_PUBLISHING}}browser_bot_challenge_guidesagent_to_agentconnection_researchartifact_icon_generationavatar_wardrobeserendipitynavigationcvm_media_generationphone_self_teststripe_link_balanceproactivity_source_readproactivity_legacy_toolsproactivity_legacy_source_readproactivity_delightfulnessproactivity_coordinator_v1proactivity_media_generationproactivity_trackingshare_ideas_skillsmb_product_shots_skillvoice_designvoice_modevoice_optionsvoice_spoken_previewbuiltin_artifactsartifact_versionsmuse_promo_codebrowser_open_live_checksbrowser_choicewelcome_to_muse_tutorialmuse_townshopping_collectionsstateful_artifact_sharingartifact_view_referencepreapprovalpoppy_conversationswhatsapp_group_creationlive config snapshot refreshedlive config refresh failed; retaining last snapshotanimalinternal_wakeheld bootstrap input lock was poisoned; recovering 