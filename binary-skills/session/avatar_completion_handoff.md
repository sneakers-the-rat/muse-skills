The selected avatar image is active. Instagram profile available: {instagram_profile_available}. Use avatar.get to check that its current image path matches {image_path}. If a different avatar is now active, do not announce or present this completed avatar.

### If instagram profile available is true
- Videos may still be generating; do not wait for them. After confirming this is still the current avatar, give the user the option to add a Muse banner to their profile. 
- This banner is a visual pill on the user's Instagram profile beneath their bio, showing their Muse avatar and name. Tapping it opens the Muse app if installed, or prompts the visitor to download it. It does not change the user's profile picture or bio. Adding the banner does not grant or change permissions for Muse or anyone else to read or access the user's Instagram profile, posts, or account. It does not give visitors access to the user's Muse and does not let them ask the user's Muse questions. Visitors only see the Muse avatar and name through the banner. Use these facts when explaining the banner or answering privacy questions.
- To give the user the option to add a Muse banner to their profile, speak in first person and invite the user: "Want to show off my new look? Add me as a banner on your Instagram profile". Use this wording in English, or its natural equivalent in the user's language. Refer to yourself as "me" and the avatar as "my new look", not by your name in third person. Call muse.create_options with exactly one accepting reply: {"options":["Let's do it"]} in English, or its natural equivalent in the user's language. The option's displayed text is also the exact user message sent when tapped. Include the returned embed_token unchanged in the same message as the invitation; plain text alone is not a complete offer. Do not use the avatar_share card, open a share sheet, attach avatar media, or add a separate readiness announcement.
- This handoff authorizes only the invitation, not a profile change. Wait for the user's acceptance; tapping "Let's do it" accepts this invitation. If they accept, read /opt/hatch/connectors/instagram/CONNECTOR.md to resolve their linked account and run instagram-cli profile-banner --account-id <user_own_fbid> --action add through the normal connector approval flow. If multiple accounts are linked and the intended account is unclear, ask which one. Recheck account availability before the write. If Instagram has been disconnected, do not update the profile or turn this offer into an account-linking upsell. Do not change the profile photo or bio. Confirm the banner was added only when the command returns success: true; otherwise explain that the update did not complete or could not be confirmed.

### If Instagram profile available is false
- Preserve the existing sharing flow: all required images and videos are published. After verifying the current avatar, call avatar.create_avatar_share_widget with the sharing-card fields. Set button_text to "Share avatar" and fallback_text to "You can share it with friends!" in the user's language. Write a short sharing invitation in title and subtitle in the user's language. Omit image_url. Send only the returned embed token in your final message. Do not send commentary, a readiness announcement, or other text. Do not attach avatar media. The client handles sharing when the user presses the button; do not open a share sheet or perform sharing yourself. Do not mention Instagram or offer to connect it.
idle_video_path{image_path}{instagram_profile_available}runtime_execinstagram profile banner invitation handed to agentavatar completion handoff acceptedconnector_call_reason/opt/hatch/bin/instagram-cliJARVIS_HOMEJARVIS_VAR_LIB_DIRavatar completion handoff armedJARVIS_STEFI_PROXY_SOCKworkspace/avatarsthe look's still has an unsupported formatactivationavatar: failed to record the Halloween costumeMy avatar is updated and active now. Briefly and naturally tell the user in first person that my avatar is updated. Don't reference option numbers, internal identifiers, or video/animation generation.clearenrichmentsender per jobavatar job task panickedavatar create: wardrobe unreadable; dressing the active avatarno widget presentation contextavatar create: bundled looks unreadable; generating costumesavatar create: avatar folder unavailable; generating costumesavatar create: bundled preview copy failed; generating costumeswitch_hatEdit the provided reference image: dress the same character in a full-body
witch Halloween costume. It wears a tall pointed witch hat with a wide brim
and a buckled band, a long flowing witch robe in deep black or midnight purple
that covers its body from neck to feet, and a short matching cape fastened at
the collar. A small broomstick rests beside it, or in its hand if it already
has hands. The whole costume is tailored to the character's own body shape and
size.

This is the same character in costume, not a new character. Keep its identity,
face and expression, species or object type, silhouette, body plan,
proportions, pose, and rendering style exactly as the reference image shows,
so it is instantly recognizable in the costume. Never add arms, hands, legs, a
face, or anatomy the reference image does not already have. For an animal, the
robe and cape drape over its natural body and legs, and the hat rests on its
head.

If the character is an inanimate object or an abstract shape rather than a
person, animal, or creature, do not dress it in clothing or give it a body.
Keep its whole shape, surface, and materials visible and unchanged, and make
the costume with props instead: a small pointed witch hat with a buckled band
resting on its top, and a little broomstick leaning beside it. The props are
sized to suit it and leave its shape uncovered.

If the reference character has no face, such as an object or an abstract
shape, it stays faceless: do not add eyes, a mouth, a nose, or any face to it,
and keep its front exactly as the reference image shows.

Keep its body plan and stance exactly as the reference image shows. Wings stay
wings, fins stay fins, paws stay paws, hooves stay hooves, and a tail stays a
tail. A four-legged animal stays on all four legs, an upright two-legged
character stays upright on two legs, and a character without limbs stays
without limbs. The costume adapts to the body; the body never changes to fit
the costume.

Exactly one standalone avatar image; square 1:1 framing; straight-on and
front-facing; the complete character and the whole costume centered and fully
visible with no cropping; a plain white background with no scene, surface, or
environment; no text, logos, watermarks, captions, or UI. Playful and
friendly, never scary or gory.
jack_o_lanternEdit the provided reference image: dress the same character in a full-body
pumpkin Halloween costume. On its head it wears a round orange pumpkin costume
hood, with a short green stem on top and a friendly cartoon pumpkin face (two
triangle eyes and a smiling grin) printed on the hood's upper front, above a
large round opening cut into the front. The character's own face fills that
opening and is fully visible: its own eyes, expression, and features,
unchanged, uncovered, and bright. Below, it wears a matching puffy orange
pumpkin costume with soft vertical ribs covering its body from neck to feet,
finished with a green leaf collar. The costume is tailored to the character's
own body shape and size.

This is the same character wearing a costume. Keep its identity, face, eyes
and expression, species or object type, silhouette, body plan, limbs,
proportions, pose, and rendering style exactly as the reference image shows,
so the costume clearly sits on this character. Render the costume in that same
rendering style. Keep exactly the arms, hands, legs, and anatomy the reference
image already has. For an animal, the pumpkin costume follows its natural body
and legs.

If the character is an inanimate object or an abstract shape rather than a
person, animal, or creature, do not dress it in clothing or give it a body.
Keep its whole shape, surface, and materials visible and unchanged, and make
the costume with props instead: a small orange pumpkin cap with a green stem
and leaf resting on its top, and a little pumpkin treat bucket with a friendly
printed face beside it. The props are sized to suit it and leave its shape
uncovered.

If the reference character has no face, such as an object or an abstract
shape, it stays faceless: do not add eyes, a mouth, a nose, or any face to it,
and keep its front exactly as the reference image shows.

Keep its body plan and stance exactly as the reference image shows. Wings stay
wings, fins stay fins, paws stay paws, hooves stay hooves, and a tail stays a
tail. A four-legged animal stays on all four legs, an upright two-legged
character stays upright on two legs, and a character without limbs stays
without limbs. The costume adapts to the body; the body never changes to fit
the costume.

Exactly one standalone avatar image; square 1:1 framing; straight-on and
front-facing; the complete character and the whole costume centered and fully
visible with no cropping; a plain white background with no scene, surface, or
environment; no text, logos, watermarks, captions, or UI. Cute, cheerful,
cartoon dress-up, like a friendly trick-or-treater.
ghost_sheetEdit the provided reference image: dress the same character in a full-body
classic homemade ghost Halloween costume, a soft plain white bedsheet draped
over its whole body from head to feet with two cut-out eye holes. The sheet
follows the character's own silhouette closely, so its overall shape, size,
and distinctive outline (ears, horns, handles, or other protruding features
showing as bumps under the cloth) stay recognizable. The character's own eyes
peek out through the holes. The bottom edge of the sheet falls in gentle
folds, with the character's feet, paws, or base just visible beneath it.

This is the same character in costume, not a new character. Keep its identity,
proportions, pose, and rendering style exactly as the reference image shows;
the sheet is the only change. Render the cloth in that same rendering style
with soft, believable folds. Never add arms, hands, legs, or anatomy the
reference image does not already have.

If the character is an inanimate object or an abstract shape rather than a
person, animal, or creature, do not dress it in clothing or give it a body.
Keep its whole shape, surface, and materials visible and unchanged, and make
the costume with props instead: a small white sheet-ghost cap draped just over
its top like a little hat, and a tiny plush sheet-ghost toy beside it. The
props are sized to suit it and leave its shape uncovered.

If the reference character has no face, such as an object or an abstract
shape, it stays faceless: do not add eyes, a mouth, a nose, or any face to it,
and keep its front exactly as the reference image shows.

Keep its body plan and stance exactly as the reference image shows. Wings stay
wings, fins stay fins, paws stay paws, hooves stay hooves, and a tail stays a
tail. A four-legged animal stays on all four legs, an upright two-legged
character stays upright on two legs, and a character without limbs stays
without limbs. The costume adapts to the body; the body never changes to fit
the costume.

Exactly one standalone avatar image; square 1:1 framing; straight-on and
front-facing; the complete character and the whole costume centered and fully
visible with no cropping; a plain white background with no scene, surface, or
environment, with the white sheet kept clearly readable against it through
soft shading; no text, logos, watermarks, captions, or UI. Playful and
friendly, never scary.
Edit the provided reference image: dress the same character in a full-body
bone-print Halloween costume. On its head it wears a big, rounded, bone-white
cartoon costume hood, soft and plush, shaped like a friendly cartoon head with
round eye shapes, a small heart-shaped nose, and a big smiling grin printed on
the hood's upper front, above a large round opening cut into the front. The
character's own face fills that opening and is fully visible: its own eyes,
expression, and features, unchanged and uncovered, with no face paint or
markings. Below, it wears a fitted black costume bodysuit covering its body
from neck to feet, printed with a simple, friendly bone-white pattern that
follows its own body (a ribcage shape on the chest and stripes along each limb
it already has). The costume is tailored to the character's own body shape and
size.

This is the same character wearing a costume. Keep its identity, face, eyes
and expression, species or object type, silhouette, body plan, limbs,
proportions, pose, and rendering style exactly as the reference image shows,
so the costume clearly sits on this character. Render the costume in that same
rendering style. Keep exactly the arms, hands, legs, and anatomy the reference
image already has. For an animal, the bodysuit follows its natural body and
legs.

If the character is an inanimate object or an abstract shape rather than a
person, animal, or creature, do not dress it in clothing or give it a body.
Keep its whole shape, surface, and materials visible and unchanged, and make
the costume with props instead: a small plush bone-print party hat resting on
its top, and a little plush cartoon bone toy beside it. The props are sized to
suit it and leave its shape uncovered.

If the reference character has no face, such as an object or an abstract
shape, it stays faceless: do not add eyes, a mouth, a nose, or any face to it,
and keep its front exactly as the reference image shows.

Keep its body plan and stance exactly as the reference image shows. Wings stay
wings, fins stay fins, paws stay paws, hooves stay hooves, and a tail stays a
tail. A four-legged animal stays on all four legs, an upright two-legged
character stays upright on two legs, and a character without limbs stays
without limbs. The costume adapts to the body; the body never changes to fit
the costume.

Exactly one standalone avatar image; square 1:1 framing; straight-on and
front-facing; the complete character and the whole costume centered and fully
visible with no cropping; a plain white background with no scene, surface, or
environment; no text, logos, watermarks, captions, or UI. Cute, cheerful,
cartoon dress-up, like a friendly trick-or-treater.
Edit the provided reference image: dress the same character in a full-body
wolf-costume Halloween outfit. It wears a fuzzy faux-fur costume suit in warm
gray and brown covering its whole body from neck to feet, a matching hood with
pointed wolf ears framing its face, soft oversized plush paw mitts and paw
boots on the hands and feet it already has (wings and fins stay bare), and a
fluffy costume wolf tail behind it. The fur is clearly plush costume fabric,
tailored to the character's own body shape and size.

This is the same character wearing a costume. Keep its identity, face and
expression, species or object type, silhouette, body plan, proportions,
palette accents, pose, and rendering style exactly as the reference image
shows, so its own face stays fully visible and recognizable inside the hood.
Keep exactly the arms, hands, legs, face shape, and anatomy the reference
image already has. For an animal, the fur suit follows its natural body plan
and legs.

If the character is an inanimate object or an abstract shape rather than a
person, animal, or creature, do not dress it in clothing or give it a body.
Keep its whole shape, surface, and materials visible and unchanged, and make
the costume with props instead: a fuzzy wolf-ear headband resting on its top,
and a fluffy costume wolf tail beside it. The props are sized to suit it and
leave its shape uncovered.

If the reference character has no face, such as an object or an abstract
shape, it stays faceless: do not add eyes, a mouth, a nose, or any face to it,
and keep its front exactly as the reference image shows.

Keep its body plan and stance exactly as the reference image shows. Wings stay
wings, fins stay fins, paws stay paws, hooves stay hooves, and a tail stays a
tail. A four-legged animal stays on all four legs, an upright two-legged
character stays upright on two legs, and a character without limbs stays
without limbs. The costume adapts to the body; the body never changes to fit
the costume.

Exactly one standalone avatar image; square 1:1 framing; straight-on and
front-facing; the complete character and the whole costume centered and fully
visible with no cropping; a plain white background with no scene, surface, or
environment; no text, logos, watermarks, captions, or UI. Cute, cuddly,
cartoon dress-up, like a friendly trick-or-treater.
zombieEdit the provided reference image: dress the same character in a full-body
playful monster dress-up Halloween costume. It wears a complete outfit of
patched, frayed-hem costume clothes in soft green and gray covering its body
from neck to feet (a patchwork shirt and patched trousers, or a patchwork
costume tunic for a body without legs), light mint-green costume face paint,
and a few cartoon stitch shapes drawn on as decoration. The look is silly
dress-up, like a friendly trick-or-treater, with a goofy expression if the
character has a face. The outfit is tailored to the character's own body shape
and size.

This is the same character wearing a costume. Keep its identity, face, species
or object type, silhouette, body plan, proportions, pose, and rendering style
exactly as the reference image shows, so it is instantly recognizable under
the face paint. Keep exactly the arms, hands, legs, and anatomy the reference
image already has. For an animal, the patchwork costume drapes over its
natural body and legs.

If the character is an inanimate object or an abstract shape rather than a
person, animal, or creature, do not dress it in clothing or give it a body.
Keep its whole shape, surface, and materials visible and unchanged, and make
the costume with props instead: a small patchwork beanie with cartoon stitch
details resting on its top, and a little patchwork plush toy beside it. The
props are sized to suit it and leave its shape uncovered.

If the reference character has no face, such as an object or an abstract
shape, it stays faceless: do not add eyes, a mouth, a nose, or any face to it,
and keep its front exactly as the reference image shows.

Keep its body plan and stance exactly as the reference image shows. Wings stay
wings, fins stay fins, paws stay paws, hooves stay hooves, and a tail stays a
tail. A four-legged animal stays on all four legs, an upright two-legged
character stays upright on two legs, and a character without limbs stays
without limbs. The costume adapts to the body; the body never changes to fit
the costume.

Exactly one standalone avatar image; square 1:1 framing; straight-on and
front-facing; the complete character and the whole costume centered and fully
visible with no cropping; a plain white background with no scene, surface, or
environment; no text, logos, watermarks, captions, or UI. Cute, funny, cartoon
dress-up.
grim_reaperEdit the provided reference image: dress the same character in a full-body
hooded-cloak Halloween costume. It wears a long hooded black costume cloak
that covers its whole body from neck to feet, with wide sleeves and a
scalloped hem, the hood pulled up loosely so its face stays fully visible and
smiling inside it, and a soft toy costume scythe prop with a short handle and
a rounded gray foam blade resting beside it or leaning against it. Where it
already has hands, it may hold the prop; otherwise the prop stands next to it.
The cloak is tailored to the character's own body shape and size.

This is the same character wearing a costume. Keep its identity, face and
expression, species or object type, silhouette, body plan, proportions, pose,
and rendering style exactly as the reference image shows, so it is instantly
recognizable. Keep any face it has fully visible, and keep exactly the arms,
hands, legs, and anatomy the reference image already has. For an animal, the
cloak drapes over its natural body and legs.

If the character is an inanimate object or an abstract shape rather than a
person, animal, or creature, do not dress it in clothing or give it a body.
Keep its whole shape, surface, and materials visible and unchanged, and make
the costume with props instead: a small black costume hood resting on its top
like a cap, and a soft toy costume scythe prop with a rounded gray foam blade
leaning beside it. The props are sized to suit it and leave its shape
uncovered.

If the reference character has no face, such as an object or an abstract
shape, it stays faceless: do not add eyes, a mouth, a nose, or any face to it,
and keep its front exactly as the reference image shows.

Keep its body plan and stance exactly as the reference image shows. Wings stay
wings, fins stay fins, paws stay paws, hooves stay hooves, and a tail stays a
tail. A four-legged animal stays on all four legs, an upright two-legged
character stays upright on two legs, and a character without limbs stays
without limbs. The costume adapts to the body; the body never changes to fit
the costume.

Exactly one standalone avatar image; square 1:1 framing; straight-on and
front-facing; the complete character, the whole cloak, and the whole prop
centered and fully visible with no cropping; a plain white background with no
scene, surface, or environment; no text, logos, watermarks, captions, or UI.
Cute, cheerful, cartoon dress-up, like a friendly trick-or-treater.
devilEdit the provided reference image: dress the same character in a full-body
little devil Halloween costume. It wears a bright cherry-red costume jumpsuit
covering its whole body from neck to feet with a short red cape at the collar,
a costume headband with two small glossy red horns on top of its head or
topmost point, and a long red costume tail with a pointed arrowhead tip
curving out from behind it. Everything is clearly costume fabric and
accessories, tailored to the character's own body shape and size.

This is the same character in costume, not a new character. Keep its identity,
face and expression, species or object type, silhouette, body plan,
proportions, pose, and rendering style exactly as the reference image shows,
so it is instantly recognizable in the costume. Never add wings, arms, hands,
legs, or anatomy the reference image does not already have. For an animal, the
jumpsuit follows its natural body and legs, the horns sit on a headband, and
the tail attaches to the costume.

If the character is an inanimate object or an abstract shape rather than a
person, animal, or creature, do not dress it in clothing or give it a body.
Keep its whole shape, surface, and materials visible and unchanged, and make
the costume with props instead: a small headband with soft red costume horns
resting on its top, and a little toy red pitchfork prop leaning beside it. The
props are sized to suit it and leave its shape uncovered.

If the reference character has no face, such as an object or an abstract
shape, it stays faceless: do not add eyes, a mouth, a nose, or any face to it,
and keep its front exactly as the reference image shows.

Keep its body plan and stance exactly as the reference image shows. Wings stay
wings, fins stay fins, paws stay paws, hooves stay hooves, and a tail stays a
tail. A four-legged animal stays on all four legs, an upright two-legged
character stays upright on two legs, and a character without limbs stays
without limbs. The costume adapts to the body; the body never changes to fit
the costume.

Exactly one standalone avatar image; square 1:1 framing; straight-on and
front-facing; the complete character, both horns, and the whole tail centered
and fully visible with no cropping; a plain white background with no scene,
surface, or environment; no text, logos, watermarks, captions, or UI. Playful
and mischievous, never scary, sinister, or gory.
clownEdit the provided reference image: dress the same character in a full-body
cheerful circus-performer Halloween costume. It wears a baggy polka-dot
jumpsuit in bright primary colors covering its whole body from neck to feet,
with big pom-pom buttons and a wide ruffled collar, a round red foam costume
nose, a fluffy rainbow costume wig or a small striped party hat on its head or
topmost point, and oversized floppy shoes on the feet it already has. The
costume is tailored to the character's own body shape and size.

This is the same character wearing a costume. Keep its identity, face and
expression, species or object type, silhouette, body plan, proportions, pose,
and rendering style exactly as the reference image shows, so it is instantly
recognizable, with any face it has clear and uncovered. Keep exactly the arms,
hands, legs, and anatomy the reference image already has. For an animal, the
jumpsuit follows its natural body and legs and the foam nose sits on its own
nose or snout.

If the character is an inanimate object or an abstract shape rather than a
person, animal, or creature, do not dress it in clothing or give it a body.
Keep its whole shape, surface, and materials visible and unchanged, and make
the costume with props instead: a small striped party hat resting on its top,
and a few bright balloons and a juggling ball beside it. The props are sized
to suit it and leave its shape uncovered.

If the reference character has no face, such as an object or an abstract
shape, it stays faceless: do not add eyes, a mouth, a nose, or any face to it,
and keep its front exactly as the reference image shows.

Keep its body plan and stance exactly as the reference image shows. Wings stay
wings, fins stay fins, paws stay paws, hooves stay hooves, and a tail stays a
tail. A four-legged animal stays on all four legs, an upright two-legged
character stays upright on two legs, and a character without limbs stays
without limbs. The costume adapts to the body; the body never changes to fit
the costume.

Exactly one standalone avatar image; square 1:1 framing; straight-on and
front-facing; the complete character and the whole costume centered and fully
visible with no cropping; a plain white background with no scene, surface, or
environment; no text, logos, watermarks, captions, or UI. Happy, bright,
cartoon dress-up, like a friendly trick-or-treater.
mummyEdit the provided reference image: dress the same character in a full-body
mummy Halloween costume, like a homemade costume made from soft cream-white
cloth bandages or toilet paper. Overlapping strips wind snugly around its
whole body from the top of its head down to its feet, following its own shape,
with a few loose, playful ends fluttering free and slightly uneven wraps that
look handmade. Around its head the wrapping forms a hood that leaves a large
opening at the front, and the character's own face fills that opening and is
fully visible: its own eyes, expression, and features, unchanged and
uncovered, with no bandages, shadows, or markings across its face. The costume
is tailored to the character's own body shape and size. For an animal, the
strips wrap its natural body, legs, and tail, and leave its face and ears
showing.

This is the same character in costume, not a new character and not an actual
mummy. Keep its identity, face, eyes and expression, species or object type,
silhouette, body plan, limbs, proportions, pose, and rendering style exactly
as the reference image shows, so the costume clearly sits on this character.
Render the costume in that same rendering style. Never add arms, hands, legs,
or anatomy the reference image does not already have.

If the character is an inanimate object or an abstract shape rather than a
person, animal, or creature, do not dress it in clothing or give it a body.
Keep its whole shape, surface, and materials visible and unchanged, and make
the costume with props instead: a small soft wrap-cloth bow resting on its
top, and a little plush mummy toy beside it. The props are sized to suit it
and leave its shape uncovered.

If the reference character has no face, such as an object or an abstract
shape, it stays faceless: do not add eyes, a mouth, a nose, or any face to it,
and keep its front exactly as the reference image shows.

Keep its body plan and stance exactly as the reference image shows. Wings stay
wings, fins stay fins, paws stay paws, hooves stay hooves, and a tail stays a
tail. A four-legged animal stays on all four legs, an upright two-legged
character stays upright on two legs, and a character without limbs stays
without limbs. The costume adapts to the body; the body never changes to fit
the costume.

Exactly one standalone avatar image; square 1:1 framing; straight-on and
front-facing; the complete character and the whole costume centered and fully
visible with no cropping; a plain white background with no scene, surface, or
environment; no text, logos, watermarks, captions, or UI. Cozy, playful, and
friendly, never scary, creepy, gory, dirty, or decayed.
optionsinvalid_argsstate_loadavatar create: recent selections unreadable; offering a random costume setcould not load the latest avatar selection for compiler contextavatar create: reference upload did not yield a handle; attaching the file per candidateactive_avatarcompileavatar edit compiled no promptimage_editsuperseded_during_editskipped_activationexpected_active_stemcurrent_active_stemthe active avatar changed while the edit was generatingavatar selections are unavailablefreshness_checkpresentation_modeawaiting_userEdited avatar preview is ready. Present it and, once the user confirms, activate it with the avatar set action and this candidate_id. The avatar is not active until avatar set is called. The candidate carries the `path` of its image; read it with the read tool to see it before describing it.present_inlineinline_image_markdownpresetthat seasonal preset is not available right nowreference_inputdress in a costumeassets/avatar/reference/hatch.jpgimage_option_countrequested_option_countfailed_option_countAvatar options are ready, but none is active. Present every option and wait for a later user message to choose or confirm one. Do not activate an option in this turn. Each candidate carries the `path` of its image; you have not seen the images, so to answer what an option looks like, read its `path` with the read tool first.presentedavatar create: widget presentation failed; presenting inlinepartial_successavatar: theme color extraction failed, using defaultavatar: theme color task failed, using defaultavatar: could not tell whether an outfit is worn; keeping the baselook_already_wornunchangedI'm already wearing that look; nothing changed. Tell the user briefly in first person.customavatar get: failed to read the wardrobeavatar: active message id is not a submission id; enrichment runs unsupervisedavatar: no active runtime work for the turn; enrichment runs unsupervisedselectionmain_imageworkspace_copyavatar wardrobe: the new avatar could not be recorded as the baseimage_first_activationbase_image_id_presentavatar completion handoff could not be armedthe avatar wardrobe's base changed while keeping itavatar visual metadata was superseded or is not applicableavatar visual metadata is readyavatar visual metadata enrichment failed; dedicated maintenance will retryavatar visual metadata classifiedvisual_metadatadefault_lookavatar get: failed to classify the active avataravatar get: failed to load current avatar stateimage_variant_assetsaspect_ratio_video_variantsdarkmode_aspect_ratio_video_variantsclaimcandidate_id names an option that does not existselection_already_consumedThe active avatar changed before this candidate could be activated, so nothing was activated. Re-create or re-preview and try again.unknown candidate_idthe avatar wardrobe is unavailablebase_already_wornthis avatar's files were not kept, so it cannot be worn againwardrobe_wearMy avatar has changed back and is active now. Briefly and naturally tell the user in first person which look I'm wearing now. Don't reference internal identifiers or video/animation generation.avatar wardrobe: the default avatar could not be recorded as the basedefault_avatar_activationavatar repair withheld by local CVM admissionavatar repair: failed to kill subprocesses on cancelavatar repair was cancelledavatar_finalizeavatar: failed to start activity threadavatar: failed to update activity actionavatar: failed to finish activity threadavatar_compileraccount_hint must name the account to sign in with, without control characters.Browser services are unavailable.browser specialist control did not completeThe specialist control did not complete. Check browser.specialists before you try again.browser workflow is waiting or terminalbrowser call effects could not be readThis browser task is no longer active.task_state_unavailableBrowser control is held by another workflow or the user.seat_state_unavailableOnly the browser agent controls specialists.This browser operation is unavailable.services_unavailableBrowser durable state is unavailable.durable_state_unavailableBrowser submission is no longer active.native browser operation did not completeThe view this call cites is gone, so nothing was sent. Observe the tab again, then make this call again from that view.persistbrowser screenshot was not kept

The screenshot of this view could not be kept, so it is missing from this result.browser specialist stop was not settledbrowser task is no longer runningruntime.browser_controlbrowser_invocation_idbrowser_workflow_resultbrowser workflow could not completeThe specialist stopped without a verified result, and its recorded actions may still need checking. Call the same specialist again, or report the blocker in `browser.report`. Do not do its protected work with ordinary browser actions or another tool, and do not repeat an uncertain purchase.
browser invocation replay changed inputthe specialist's tab is no longer openbrowser task has no plannerruntime.todo_snapshottodo snapshot after compaction skipped: stored snapshot unreadabletodo snapshot after compaction skipped: snapshot load failedtodo snapshot after compaction failed to recordThis subtask stopped during a restart and did not report a result. Its work may be partly or fully done: check what it already produced before redoing anything, then redo or redelegate only what is actually missing.Closed during restart recovery without reporting a result.failed to persist terminal state for closed checkpointed subagentfailed to persist terminal status for closed checkpointed agentclosed Spaces builder checkpoint has no parent identityclosed Spaces builder checkpoint has no storage rootfailed to load closed Spaces builder generationfailed to delete runtime restart checkpoint for closed agentpartial_recovery_descriptormissing_conversationinvalid_structural_owner_identityrecovery_identity_mismatchinvalid_recovery_descriptorinvalid_durable_owner_identityinvalid_inherited_execution_authorityproject context prompt loader task failed; omitting project contextproject context prompt loader timed out; omitting project context
DELETE FROM search_documents
WHERE owner_table = 'runtime.events'
  AND owner_key = $1
DELETE FROM resources WHERE event_seq = $1INSERT INTO resources (event_seq, ordinal, resource_kind, resource_key, label, mime_type, size_bytes, metadata_json) VALUES /__hatch/chat_context_jsonstring/__hatch/display_text_updated_at_msnumberSELECT field_path, scalar_type, scalar_value, text_value FROM event_payload_fields WHERE event_seq = $1 FOR UPDATEDELETE FROM event_payload_fields WHERE event_seq = $1 AND field_path = ANY($2::text[])INSERT INTO event_payload_fields (event_seq, field_path, scalar_type, scalar_value, text_value) VALUES  ON CONFLICT (event_seq, field_path) DO UPDATE SET scalar_type = excluded.scalar_type, scalar_value = excluded.scalar_value, text_value = excluded.text_valueruntime.search_documents.search_text
INSERT INTO search_documents (owner_table, owner_key, search_text, language, search_vector)
VALUES ('runtime.events', $1, $2, 'simple', to_tsvector('simple', $3))
ON CONFLICT (owner_table, owner_key) DO UPDATE SET
  search_text = excluded.search_text,
  language = excluded.language,
  search_vector = excluded.search_vector,
  updated_at = now()
WHERE search_documents.search_text IS DISTINCT FROM excluded.search_text
   OR search_documents.language IS DISTINCT FROM excluded.language

SELECT coalesce(f.text_value, f.scalar_value)
FROM event_payload_fields f
WHERE f.event_seq = $1
  AND f.field_path = '/__hatch/chat_context_json'
LIMIT 1

SELECT
  e.event_name,
  e.transcript_surface::text AS transcript_surface,
  e.visibility::text AS visibility,
  COALESCE(e.role::text, m.role::text, 'system') AS role,
  e.source
FROM events e
LEFT JOIN messages m
  ON m.event_seq = e.event_seq
WHERE e.event_seq = $1

UPDATE widgets
SET state_bundle_json = $2,
    state_version = $3,
    state_updated_at_ms = $4,
    updated_at_ms = $4
WHERE widget_id = $1
  AND state_version = $5
RETURNING state_version

SELECT state_bundle_json, state_version
FROM widgets
WHERE widget_id = $1
state_bundle_jsonwidget state bundle must be a JSON objectstate_version
INSERT INTO context_items (
  agent_id, seq, item_kind, text_content, role, call_id, tool_name, success,
  message_source, created_at, item_json,
  data_fbids, data_message_ids, data_thread_ids, data_expires_at
)
VALUES ($1, $2, $3::agent.context_item_kind, $4, $5::runtime.message_role,
        $6, $7, $8, $9, to_timestamp($10::double precision), $11,
        $12::bigint[], $13::text[], $14::text[], $15::timestamptz)
RETURNING context_item_id

INSERT INTO context_items (
  agent_id, seq, item_kind, text_content, role, call_id, tool_name, success,
  message_source, created_at, item_json,
  data_fbids, data_message_ids, data_thread_ids, data_expires_at
)
VALUES ($1, $2, $3::agent.context_item_kind, $4, $5::runtime.message_role,
        $6, $7, $8, $9, to_timestamp($10::double precision), $11,
        $12::bigint[], $13::text[], $14::text[], $15::timestamptz)
ON CONFLICT (agent_id, seq) DO UPDATE SET
  item_kind = excluded.item_kind,
  text_content = excluded.text_content,
  role = excluded.role,
  call_id = excluded.call_id,
  tool_name = excluded.tool_name,
  success = excluded.success,
  message_source = COALESCE(excluded.message_source, context_items.message_source),
  created_at = excluded.created_at,
  item_json = excluded.item_json,
  data_fbids = excluded.data_fbids,
  data_message_ids = excluded.data_message_ids,
  data_thread_ids = excluded.data_thread_ids,
  data_expires_at = excluded.data_expires_at
RETURNING context_item_id

INSERT INTO context_items (
  agent_id, seq, item_kind, text_content, role, call_id, tool_name, success,
  message_source, created_at, item_json,
  data_fbids, data_message_ids, data_thread_ids, data_expires_at
) VALUES  RETURNING context_item_id, seq::agent.context_item_kind, ::runtime.message_role, , to_timestamp(::double precision), ::bigint[], ::text[], ::timestamptz)context_item_id
SELECT pg_advisory_xact_lock(hashtextextended(agent_id, $2))
FROM unnest($1::text[]) AS locked(agent_id)
ORDER BY agent_id

WITH inserted AS (
INSERT INTO chat.chats (
  chat_id,
  origin,
  lifecycle,
  status,
  thread_title,
  source_session_id,
  source_prompt_seq_upper_bound,
  source_message_id_boundary,
  created_at,
  updated_at
)
VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $12, $12)
RETURNING chat_id
)
INSERT INTO chat_private.bindings(chat_id, provider, conversation_key, delivery_target)
SELECT chat_id, $9, $10, $11 FROM inserted WHERE $9::text IS NOT NULL
persistent
INSERT INTO context_item_resume_projection (
  agent_id, seq, context_item_id, created_at, message_source
)
VALUES ($1, $2, $3, $4, $5)
ON CONFLICT (agent_id, seq) DO UPDATE SET
  context_item_id = excluded.context_item_id,
  created_at = excluded.created_at,
  message_source = COALESCE(excluded.message_source, context_item_resume_projection.message_source),
  updated_at = now()

WITH producer AS MATERIALIZED (
  SELECT target.id AS agent_id,
    CASE WHEN a.id IS NULL THEN NULL ELSE COALESCE(
-- Highest seq of an agent's rows that no public voice import reads, or NULL
-- when the import never reads any of them. Reads aliases `a` (the agent) and
-- `root` (its presentation root). exempt_non_producer_rows.sql repeats it.
CASE WHEN a.kind = 'root' AND a.depth = 0
          AND a.agent_type = 'realtime_voice' THEN CASE
    WHEN NOT pg_input_is_valid(a.spawn_metadata_json, 'jsonb') THEN -1
    WHEN root.id IS NULL
         OR a.spawn_metadata_json::jsonb #> '{realtime_voice,prompt_floor_seq}'
            IS DISTINCT FROM to_jsonb(COALESCE(root.prompt_floor_seq, -1))
        THEN NULL
    WHEN pg_input_is_valid(
        a.spawn_metadata_json::jsonb #>> '{realtime_voice,root_seed_context_seq}',
        'bigint'
    ) THEN GREATEST(
        (a.spawn_metadata_json::jsonb #>> '{realtime_voice,root_seed_context_seq}')::bigint,
        -1
    )
    ELSE -1
END END
    , 9223372036854775807) END AS exempt_through_seq
  FROM (SELECT ::text AS id) target
  LEFT JOIN agents a ON a.id = target.id
  LEFT JOIN agents root ON root.id = a.presentation_root_session_id AND root.id <> a.id
)
INSERT INTO context_item_resume_projection (
  agent_id, seq, context_item_id, created_at, message_source,
  client_context_json, client_context_projected, public_import_exempt
)
SELECT producer.agent_id, v.seq, v.context_item_id, v.created_at, v.message_source,
       v.client_context_json, v.client_context_projected,
       CASE WHEN v.seq <= producer.exempt_through_seq THEN TRUE END
FROM (VALUES ) AS v(seq, context_item_id, created_at, message_source, client_context_json,
          client_context_projected)
CROSS JOIN producer
ON CONFLICT (agent_id, seq) DO UPDATE SET
  context_item_id = excluded.context_item_id,
  created_at = excluded.created_at,
  message_source = COALESCE(excluded.message_source, context_item_resume_projection.message_source),
  client_context_json = COALESCE(
    excluded.client_context_json,
    context_item_resume_projection.client_context_json
  ),
  client_context_projected = COALESCE(
    context_item_resume_projection.client_context_projected,
    FALSE
  ) OR excluded.client_context_projected,
  public_import_exempt = COALESCE(
    context_item_resume_projection.public_import_exempt,
    excluded.public_import_exempt
  ),
  updated_at = now()
INSERT INTO context_item_resume_projection (
  agent_id, seq, context_item_id, created_at, message_source,
  client_context_json, reply_prefix, provenance_json,
  client_context_projected, reply_prefix_projected, provenance_projected,
  public_import_exempt
)
SELECT producer.agent_id, v.seq, v.context_item_id, v.created_at, v.message_source,
       v.client_context_json, v.reply_prefix, v.provenance_json,
       v.client_context_projected, v.reply_prefix_projected, v.provenance_projected,
       CASE WHEN v.seq <= producer.exempt_through_seq THEN TRUE END
FROM (VALUES ) AS v(seq, context_item_id, created_at, message_source, client_context_json,
          reply_prefix, provenance_json, client_context_projected, reply_prefix_projected,
          provenance_projected)
CROSS JOIN producer
ON CONFLICT (agent_id, seq) DO UPDATE SET
  context_item_id = excluded.context_item_id,
  created_at = excluded.created_at,
  message_source = COALESCE(excluded.message_source, context_item_resume_projection.message_source),
  client_context_json = excluded.client_context_json,
  reply_prefix = excluded.reply_prefix,
  provenance_json = excluded.provenance_json,
  client_context_projected = excluded.client_context_projected,
  reply_prefix_projected = excluded.reply_prefix_projected,
  provenance_projected = excluded.provenance_projected,
  public_import_exempt = COALESCE(
    context_item_resume_projection.public_import_exempt,
    excluded.public_import_exempt
  ),
  updated_at = now()

SELECT agent_id, parent_agent_id, event_name, source, role::text AS role,
       visibility::text AS visibility, request_id, root_request_id,
       parent_request_id, message_id, reply_to_message_id
FROM runtime.events
WHERE event_seq = $1

INSERT INTO context_item_resume_projection (
  agent_id, seq, message_source, client_context_json, reply_prefix, provenance_json,
  client_context_projected, reply_prefix_projected, provenance_projected
)
VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
ON CONFLICT (agent_id, seq) DO UPDATE SET
  message_source = COALESCE(context_item_resume_projection.message_source, excluded.message_source),
  client_context_json = excluded.client_context_json,
  reply_prefix = excluded.reply_prefix,
  provenance_json = excluded.provenance_json,
  client_context_projected = excluded.client_context_projected,
  reply_prefix_projected = excluded.reply_prefix_projected,
  provenance_projected = excluded.provenance_projected,
  updated_at = now()
SELECT pg_advisory_xact_lock_shared(hashtextextended($1, 0))agent.volatile_context_pins.lifecycleSELECT pg_advisory_xact_lock(hashtextextended($1, 0))
WITH owners AS MATERIALIZED (
    SELECT DISTINCT agent_id COLLATE "C" AS agent_id
    FROM unnest($1::text[]) AS input(agent_id)
)
SELECT pg_advisory_xact_lock(hashtextextended($2 || agent_id, 0))
FROM owners ORDER BY agent_id COLLATE "C"
agent.volatile_context_pins:SELECT agent_id FROM agent.agents WHERE agent_id = $1SELECT handoff_state_json -> $2::text AS state,
                (extract(epoch FROM clock_timestamp()) * 1000)::bigint AS now_ms
         FROM agent.subagent_spawns WHERE child_agent_id = $1 FOR UPDATEnow_msagent.subagent_spawns.handoff_state_jsonUPDATE agent.subagent_spawns
         SET handoff_state_json = jsonb_set(COALESCE(handoff_state_json, '{}'::jsonb),
                                           ARRAY[$2]::text[], $3::jsonb)
         WHERE child_agent_id = $1insert into chat_private.publication_turns (execution_id, chat_id, disposition, phase)
        select $1, $2, $3, $4 where pg_try_advisory_xact_lock_shared(hashtextextended($5, 0))
        on conflict(execution_id) do nothing returning trueselect chat_id, phase, disposition from chat_private.publication_turns
        where execution_id = $1 for updatechat_iddispositionphasepublication execution belongs to another chatcannot classify an active avatar without an active stemactive avatar uses a newer choreography profile versionrefusing to store an incomplete avatar choreography behavior planavatar choreography classification completedavatar-choreography-classifier-v8:avocrono-9bavatar choreography classification failed; using form-agnostic fallbackavatar choreography classification failed; retryingrefusing to publish invalid avatar visual metadataavatar visual metadata classificationavatar workspace gc: avatar state unreadableavatar state unreadableavatar workspace gc: wardrobe unreadablewardrobe unreadable
    select
        node_id,
        coalesce(display_name, node_id) as display_name,
        platform,
        enabled_permissions_json,
        commands_json,
        data_sources_json,
        version,
        device_family,
        model_id,
        metadata_json,
        is_wakeup_supported,
        delivery_app,
        invoke_protocol,
        coalesce(paired_at_text, created_at::text) as paired_at,
        coalesce(last_seen_at_text, last_seen_at::text, created_at::text) as last_seen_at,
        status,
        pairing_status
    from device.nodes
pairing_status <> 'revoked'SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite\_%' ESCAPE '\' AND name NOT LIKE '\_\_%' ESCAPE '\' ORDER BY namen_truncated_tables""app.dbrunprune-imports failedprune-imports runner returned a non-zero exitindex.htmlbuild-cvm-client.js--check-scripts--space-dirstatic script check report could not be parsedstatic script check produced no usable reportstatic script check could not be spawnedstatic script check timed outnode_modulesdeps-manifest.jsontemplate_sha256cp--reflink=auto--recursivecopy prebaked bun.lockpackage.jsonbunfig.toml.media-generationsquareicon prompt cannot be emptytranscode generated icon toicon subject must not be emptyHTTP_PROXYHTTPS_PROXYALL_PROXYhttp_proxyhttps_proxyall_proxylast_auditlast_buildneeds_input markerarchive superseded planwrite data plan drafturl_audit_baseline.bun-cacheinstallBUN_INSTALL_CACHE_DIRbun install failedfailed to install dependencieswrite templatebuild./server/src/actions.ts--target=bun--outfile=./server/dist/actions.jsbun build (server) failedfailed to bundle 