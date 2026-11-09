## This Connection on the Muse Network

Your task belongs to your user's conversation with the connection identified below. Shared messages address the people and Muses in that connection.

{counterpart_line}
{verification_line}

These fields identify the other Muse and the contact, not your own user.
<!-- reopened-only:start -->

The user reconnected with this person on {reconnected_at} UTC. Tasks and questions from before then are closed, and their answers will not return. Do not resume an old commitment just because it remains in the history. Use available context for your current task. If it still needs input or a decision from the user, tell your parent what is missing.
<!-- reopened-only:end -->
{counterpart_line}{verification_line}
)
SELECT
  e.event_seq AS seq,
  (extract(epoch from e.created_at) * 1000)::bigint AS occurred_at_ms,
  e.created_at::text AS occurred_at_utc,
  e.request_id,
  e.event_name,
  coalesce(e.role::text, m.role::text, 'system') AS role,
  e.source,
  e.transcript_surface::text AS transcript_surface,
  coalesce(e.message_id, m.message_id, '') AS message_id,
  e.agent_id,
  e.parent_agent_id,
  m.body AS display_text
FROM selected_events e
LEFT JOIN messages m ON m.event_seq = e.event_seq
ORDER BY e.event_seq ASCruntime.dev_noticescheduled-crons.mdActive scheduled tasks: cadence, next run and definition file; inspect with cron.view; edit user and goal tasks with cron.updatesent.mdProactive updates this pipeline delivered in the last 7 days, with sent times and message IDs; not ordinary chat replies, which are in conversation.md and Past conversationspending-updates.mdUpdates already queued for delivery, with topics, creation times and delivery state; not confirmed receivedPhone access unavailable.Phone access, stored active geofences from all owners, previous removals and proposed placesActive schedule list: unavailable at the start of this run.
is_systemEdit: `cron.update` with this ID.
Managed by the runtime; cron tools cannot change it.
cadencedropped.mdResearch help the selector dropped in the last 7 days as unsupported, unwanted or already handled, newest firstdropped_atduplicate opportunity_keya follow-up requires prepared worka Letter must preserve one original stored Letteruse the Letter kind for completed studiesevery candidate needs exactly one dispositionreconsider_at must precede the useful deadlinereconsider_at must be a future timean expired candidate must be missed, not heldmalformed candidate packetunselectedvalidated decisionNot selected; retained for reconsiderationUseful deadline passed before selectionunselected must be an arraymissing candidate packetinclude the evidence supporting the workan action needs a label and the exact proposed requestweek_aheadmoneywork_follow_throughloved_onesmix_upsevidence needs its original referencesource expirycompleted Letters and Ideas must not be researched againinclude the title and complete prepared workeach opportunity needs a distinct, nonempty keyoutcome-free user control reported a restored parked outcomeoutcome-origin user control reported a synthesized needs-user outcomeoutcome-origin user control lost its stored outcomecardsreply_to_event_idcontact_namewearables.comms.native.smswearables.comms.provider.callios.companion.send_text_messageios.companion_calling.create_callno reviewed addressing entry for this commanddevice does not declare the reviewed destination fielddevice does not declare the reviewed body field/probe-ui.js/probe-ctx.jsscreenshot_sha256screenshot_pathsnapshot_idsettle_mslook_at_screenshotstepsfinal~/usr/bin/env/bin/bash--norc--noprofile-cfailed to prepare tool cgroup: no pure cgroup-v2 base resolvedshopify-ucp-clihatch-egress-relay-transport-failureplaywrightpuppeteerbrowsertypepage.gotoerr_tunnel_connection_failederr_proxy_connection_failederr_tunnelerr_proxyerr_connection_refusederr_connection_reseterr_empty_responseerr_network_access_deniedNote: this looks like a browser (Chromium/Playwright/Puppeteer) scripted through exec that failed to open a network connection. Use the supported browser tools according to their routing guidance rather than scripting your own browser through exec.style_presetpresent_nowrich_place requires place_id and name; marker accepts title, subtitle and background_image_url. Both require coordinate.background_image_urlPresent immediately as a standalone card. Otherwise embed the returned token in the message.widget.create_map_widgetCreate a map showing real-world places and location pins.

Prefer `rich_place` elements:
they render a photo and a place card, and `places details <place_id>`
fetches details whenever you have place ids. Usually omit element `id`s
(the server assigns them); supplied ids must be unique, and the `hatch_`
prefix is reserved for system pins.

```
{
  elements: Array<           // 1-24 elements
    { kind: "rich_place",
      place_id: string,      // numeric id copied verbatim from a `browser.search` or `places details` place result; never invent one
      name: string,
      coordinate: { latitude: number, longitude: number },
      category?: string, description?: string, id?: string }
    | { kind: "marker",      // plain pin for anything without a place id
      coordinate: { latitude: number, longitude: number },
      title?: string,        // short name for the pin; untitled markers display as the literal text "Marker"
      subtitle?: string, background_image_url?: string, id?: string }>,
  display_text?: string,
  initial_zoom?: number,     // 1-20
  motivation?: string | null // the user need this map answers, one short phrase (for example "dinner options near the theater"); omit when purely illustrative
}
```
Create a map showing real-world places and location pins.
widget.create_html_widgetCreate compact interactive HTML in the current chat reply.

Use an in-chat HTML fragment for controls, picker UIs, small cards, local previews, or charts. Follow
every rule in the "HTML widget authoring" section of the `widget` namespace description.

`{ html: string, display_text?: string, fallback_text?: string }`
Create compact interactive HTML in the current chat reply, not a document or app the user keeps.
Create a native list card of skill-directed results, links, flights, calendar entries, or email entries.

For connector search results, follow the current connector instructions and use its dedicated result creator when one is specified.

Use native list cards for skill-directed results such as flights and fitness classes. Use 1–20 rows. Non-flight rows require non-empty titles. Copy image URLs
from source results when available. Use `type: "link"` with an HTTP(S)
`data.url` for a row that opens a URL and `type: "send_message"` for a row
the user taps to send `data.text` as their reply; calendar and email rows
select a glyph only.
Omit `type` for a generic row. File rows are unsupported. If the active
client cannot render list cards, present the results as Markdown instead.

For a link list, pass arguments like this:

```json
{"title":"Results","items":[{"title":"Result name","type":"link","data":{"url":"https://example.com/result"}}]}
```

Include `items` in the tool arguments. Add an optional list `title` and `subtitle`;
omit `title` for a list without a heading.
For a flight list whose action is not booking, add one list-level
`flight_action` object with a short single-line `cta_text` and
`response_message_prefix`. The runtime appends the selected itinerary and
total to that prefix. For example:

```json
{"flight_action":{"cta_text":"Add to plan","response_message_prefix":"Add this flight to my trip plan:"}}
```

Omit `flight_action` for the default `Book with Muse` action. Use one
action for the whole flight list; do not put action copy in individual rows.
Choose action copy appropriate to the current flow, and make
`response_message_prefix` describe the same intended action as `cta_text`.
For non-flight rows, add optional string fields `subtitle`, `tertiary_title`
and `image_url`, or an `icons` array of image URL strings. Set row `type`
to "generic", "link", "send_message", "calendar", "email", "flight" or
"car_rental".

Use `type: "send_message"` with a non-empty `data.text` string only for rows
that offer the user a reply to choose. Use link or generic rows for results. Keep
the text aligned with the row's title and subtitle, with no hidden
instructions. Creating the widget sends nothing. Copy any supplied
`image_url` unchanged and never invent one.

For flights, set row `type` to "flight". Supply either inline
`data.flight_data` or `data.flight_details_file` with a JSON file path.
Create one row per complete trip, including every slice and connection.
Omit `data.slice_index` and row presentation strings.

When flight results are already JSON, save the unchanged search output to a
temporary file and pass its path in `data.flight_details_file`. Select one
object with `data.json_pointer`, an RFC 6901 pointer such as "/offers/0".
Omit the pointer when the whole file is one flight object. Inspect the file
to choose result indexes. Do not rewrite or trim its flight objects, or copy
them into tool arguments. Keep the file until widget creation succeeds.
The runtime loads each file once per list and stores the selected data.
File paths and pointers are not stored or sent to clients.

For example, put this row in the list's `items` array:

```json
{"type":"flight","data":{"flight_details_file":"/tmp/flight-search.json","json_pointer":"/offers/0"}}
```

Select one complete flight object from the file, using either the inline
schema below or the normalized search schema. For normalized search data,
the runtime maps segment `departing_at` and `arriving_at` to the widget's
local datetimes and derives display fields. It preserves the other offer
facts. Do not add a separate offer id to file input. Use a different JSON
pointer for each selected result.

For browser results, supply inline `data.flight_data` or save the same
object to a file. Populate it from verified source facts. Preserve known
baggage, fare conditions, passenger cabins, and durations. Include source
summary facts when detailed passenger facts are unavailable.
Omit unknown optional facts. Use a stable private-mapping key for `id` if
the source has no offer id. Do not combine inline and file input in one row.

Check the source flight facts before presenting. Present each result
set once, using either `present_now` or the returned embed token. Do not
present a second copy solely to correct cosmetic details. After presenting,
add useful recommendations or caveats without repeating the flight inventory
in prose.

Use this JSON shape for an inline flight row. Replace the illustrative values with
source facts and omit optional fields that the source does not provide.
Put each row inside the list's `items` array.
For file input, save only the object inside `data.flight_data`, or use
`json_pointer` to select that object within a larger document.

```json
{"type":"flight","data":{"flight_data":{"id":"offer_id_from_source","passengers":[{"type":"adult"},{"age":8}],"expires_at":"2026-09-14T18:00:00Z","price":"567.00","currency":"USD","airline":"Example Airlines","duration":"2h20m","slices":[{"duration":"2h20m","fare_brand":"Business Flex","segments":[{"from":"SFO","to":"PDX","depart":"2026-09-15T07:35:00","arrive":"2026-09-15T09:55:00","flight":"EX24","carrier":"Example Airlines","operating_carrier":"Example Regional","operating_flight":"ER24","duration":"2h20m","passengers":[{"cabin":"Business","bags":{"carry_on":1,"checked":2}},{"cabin":"Business","bags":{"carry_on":1,"checked":2}}],"carrier_code":"EX"}]}],"refundable":"yes","changeable":"yes","refund_penalty":"200.00 USD","change_penalty":"100.00 USD","refund_penalty_status":"applies","change_penalty_status":"applies","flight_link":"https://example.com/flight-details"}}}
```

For inline rows, include `flight_data` inside the row’s `data`. Include these required
`flight_data` fields: `id`, `passengers`, and `slices`.
Include at least one slice and at least one segment per slice. Include
`segments` for each slice. Include `from`, `to`,
`depart`, and `arrive` for each segment. All other flight fields shown are
optional, including segment `passengers`. Within passenger templates, `type` and `age` are
optional. Within segment passengers, `cabin` and `bags` are optional.
Within baggage objects, `carry_on` and `checked` are optional.
Use nonnegative integers for counts and ages; booleans for
`nonstop`, `cabin_varies`, and `baggage_varies`; and strings for other scalar
values, including `price`. Set `refundable` and `changeable` to "yes", "no",
or "not stated". Omit unknown optional fields rather than passing null.

Keep slices and segments in travel order. Use one slice for a one-way trip
and two slices for a round trip. Keep connecting flights in their slice's
`segments`. Present each complete offer once in one row, from comparison
through selection. Do not split outbound and return into separate rows or
lists. Treat `price` as the whole trip price for all passengers.
Do not invent per-slice prices or combine legs from different offers.
Set each segment's `depart` and `arrive` to one airport-local ISO 8601
datetime, such as "2026-09-15T07:35:00", without a timezone suffix. Copy
Duffel's segment `departing_at` into `depart` and `arriving_at` into `arrive`.
Omit Duffel's display-time strings and the slice-level `depart` and `arrive`.
Do not supply formatted timestamps. The server derives slice endpoints and
client timestamp strings from the first and last segments. For browser
results, obtain the local date and time for every endpoint before creating
a flight row. Preserve source duration strings.
Preserve known segment cabins and baggage in `segments[].passengers`.
The runtime derives cabin and baggage summaries when the detailed facts are
complete. Known differences mark variation; missing facts remain unknown.
When only source-reported summaries are available, use offer-level `bags`
and `slices[].cabin`; retain source-reported `baggage_varies` or
`slices[].cabin_varies` when detailed passenger facts are unavailable.
Include a slice's source-reported `stops` when technical stops occur within
a segment. Otherwise omit it and let the runtime count connections.
Preserve each segment's `carrier` name and `flight` number. Put its source
IATA or ICAO code in `segments[].carrier_code` when available.
Keep codeshare operators separately in
`operating_carrier` and `operating_flight`.
Omit `response_message`, slice `from` and `to`, offer `stops`, and `nonstop`
when authoring flight data. Both input forms receive the same route/stop
summaries and an identifying reply before storage.
Keep the offer id as the private checkout mapping. The server supplies
"Book with Muse" as the CTA when `flight_action` is omitted. When it
is present, the server uses its CTA and response prefix while still appending
the exact selected itinerary and total. Do not calculate elapsed durations
by subtracting airport-local clocks; preserve source durations.
Creating a row does not submit it or authorize a purchase. Add `flight_link`
only for a verified absolute HTTP(S) details URL. Keep checkout credentials
out of the payload.
using either `present_now` or the returned embed tokenusing the returned embed tokenemailFor link rows, supply url. For send_message rows, supply non-empty text. For flight rows, supply flight_data or flight_details_file with optional json_pointer, following the flight input contract below. For car_rental rows, supply car_rates_file and json_pointer naming one saved rate.response_message_prefixLanguage of generated list text as a BCP 47 tag, for example fr-FR. Set this for connector lists so official connector names match the conversation language. Omitted or unsupported languages use the request language.widget.create_list_widgetCreate a native list card of skill-directed results, links, flights, calendar entries, or email entries. Follow current connector instructions when they specify a dedicated result creator.
Short header label, such as Week ahead.Dates the card covers, such as Nov 2–8.One or two sentences that sum up the card.Short day and time, such as Sun 2:15. Add the date, such as Sat Nov 14 10:00, when the period runs past a week.Two to five words the title and time do not already say, such as 15 min clash.widget.create_agenda_widgetCreate an agenda card in the current chat reply, such as the week ahead, a day plan or a trip's schedule. The card is styled for you and fits the chat in light and dark; pass only the content.

Give it a short `title` such as `Week ahead`, the `period` it covers and a one- or two-sentence `summary`, such as "Four things to sort this week, and Sunday needs a fix." Add up to six items that matter most, in time order. Keep each item to a glance: a `title` of a few words, a short `time` such as `Sun 2:15`, with the date when the period runs past a week, a `detail` of two to five words that the title and time do not already say, such as `15 min clash`, and the `icon` that fits. Use the `warning` icon only for an item that needs attention first, such as a clash or a close deadline. The card carries the plan, so keep your message around it to what the card does not show.

`{ title: string, icon?: string, period?: string, summary?: string, items: Array<{ title: string, time?: string, detail?: string, icon?: string }>, display_text?: string, fallback_text?: string }`
Create an agenda card: a header, a short summary and a list of dated items, such as the week ahead, a day plan or upcoming deadlines.
relationship_briefwidget.create_letter_widgetPresent an existing briefing or relationship brief as a native Letter.

This tool presents the widget immediately as a standalone card. In TypeScript-style shapes, `?` marks an optional field; every other field is required.

`{ content: { type: "briefing" | "relationship_brief",
data: { id: string } } }`
Present an existing briefing or relationship brief as a native Letter.
For an open-ended question, ask in plain text. For a known, bounded choice,
call `muse.create_options` with the reply texts in `options`, then place the
returned `embed_token` unchanged in your reply to the user, in the same message
as your question or offer.
Writing a tool name in your reply does not create a widget.
The options are invisible until you embed the token in your reply to the user.
If another agent will deliver the reply, return the token to that agent for
embedding. Tapping an option sends its exact text as the user's next message.
For an open-ended question, ask in plain text. For a known, bounded choice,
call `muse.create_options` with the reply texts in `options`. This
conversation isn't on screen, so put the returned `embed_token`, unchanged, in
what you hand back, with the question or offer it answers. Writing a tool name
does not create a widget. Tapping an option sends its exact text as the user's
next message.
Create inline text reply options, including a single affirmative reply, and
embed the returned token in the question or offer.
Write each option as a short reply that naturally answers your question.
For an offer to do something, provide one option that accepts the offer.
For a choice between actions, provide one option per action.
Use “Yes” only when it reads naturally as the user's answer.
Generally provide no more than two options; include more when the question
depends on a larger bounded set.
Do not add question titles, descriptions, weak fallback choices, or fake
free-text choices such as “Other” or “Type your own”.
Do not use this tool to present specific Meta Ads ad accounts, campaigns, ad
sets, or ads: option labels cannot carry the required Ads entity references.
Resolve those objects with `ads.resolve_entities` and put the returned markers
in the response text instead.
center_aligned_filledButton appearance. Defaults to dotted_lines.Short replies the user can tap, including a single affirmative reply.Present an already-created widget as a standalone chat presentation, not inline in an assistant text message. Pass a `widget_id` returned by a widget creator, or one the runtime handed to you. Do not use this for inline-only widgets such as `muse.create_options` choices; include their returned `embed_token` in the assistant message instead. This tool does not create or update widget data.
The id of an already-created widget to present now.Present an already-created widget as a standalone chat presentation instead of inline in a message. Pass a widget_id returned by a widget creator or handed to you by the runtime.
widget.create_html_file_widgetCreate an in-chat HTML widget from a local HTML file.

Read HTML from a local `.html` or `.htm` file. Relative
paths resolve from the home directory; `workspace/...`, `/workspace/...`,
`~/...`, `file://...`, and `sandbox://workspace/...` work. Files over 1 MB
are rejected: widgets are compact UI, not media containers. Never pass paths
under `workspace/your_files/` or `workspace/visual_grounding/`; return those
as own-line preview links instead. Follow every rule in the "HTML widget
authoring" section of the `widget` namespace description.

`{ path: string, display_text?: string, fallback_text?: string }`
Create an in-chat HTML widget from a local HTML file, not a document or app the user keeps.
Create a transient in-chat widget. Pass its fields directly as tool arguments. By default, place the returned `embed_token` in your message where the widget belongs. An unused token leaves the widget invisible. Set `present_now: true` only to present it immediately as a standalone card.

Use file or web-artifact tools for documents, dashboards, and apps the user keeps or revisits.

In TypeScript-style shapes, `?` marks an optional field; every other field is required.
Create a transient in-chat widget. Pass its fields directly as tool arguments. This conversation isn't on screen, so put the returned `embed_token`, unchanged, in what you hand back, where the widget belongs.

Use file or web-artifact tools for documents, dashboards, and apps the user keeps or revisits.

In TypeScript-style shapes, `?` marks an optional field; every other field is required.
Create a native card that opens an app tab or invokes a UI control when tapped.

Use a navigation card for app navigation such as opening a tab or view.
The widget only stores the control; the client performs it on click, and an
unknown `target` fails there, not at creation.

`{ title: string, ui_control: { action: "navigate" | "set",
target: string, params: object, mode: "suggest" | "perform" },
summary?: string, subtitle?: string, icon_hint?: string,
image_path?: string, icon?: string }`
ui.create_navigation_widgetCreate a native card that opens an app tab or invokes a UI control when tapped.
Present an existing saved idea by its idea_id.

`{ idea_id: string }`
idea.create_idea_widgetPresent an existing saved idea by its idea_id.
Create a native sharing card for the assistant avatar.

Supply non-empty text
fields. Omit `image_url` unless you have an HTTPS image URL. The client handles
sharing and displays `fallback_text` if it does not support the card.

`{ image_url?: string, button_text: string, title: string,
subtitle: string, fallback_text: string }`
avatar.create_avatar_share_widgetCreate a native sharing card for the assistant avatar.
Set true to let the user pick several images where their app supports it; older apps return one.widget.create_image_picker_widgetShow up to four local images in a grid for the user to pick from. Each `path`
is a jpg, jpeg, png, webp, gif or avif file under `workspace/`. The grid shows
no captions. Set `multi_select` to true when the user may keep several images;
some apps then let them pick several and others only one, so invite a choice
without asking for a number of picks, and work with whatever arrives. A single
pick comes back as a user message "Option N", where N is the image's 1-based
position in `images`; several picks come back as one user message that lists
each picked image.
Let the user pick from up to four local images.
travel.create_hotel_results_widgetCreate native hotel cards from an unmodified saved Expedia search JSON file. Pass 1–4 search-row `id` values in `hotel_ids` to select and order the preview, or omit them to preview the first four hotels. See all opens the original search; it does not preserve a curated subset or your ranking. Cards use each row's offer and price, and open details for that rate. Follow the current connector instructions when selecting offers and presentation.
Create native hotel cards from saved Expedia search JSON, with up to four preview properties and See all for the original search.
Present a verified shopping cart using a reference returned by shopping.read_cart.

Omit `present_now` or set it to `true` to present the cart immediately. To show
the cart after your summary instead, set `present_now: false` and place the
returned `embed_token` after that summary.

Create a cart widget only when a loaded connector doc
explicitly documents using `shopping.read_cart` and supplies its provider
identifier.

`{ cart_ref: string, present_now?: boolean }`

Call `shopping.read_cart` with the doc's identifier, then copy its returned
reference into `cart_ref`. Never pass raw cart
JSON or use search results as a cart; ordinary product recommendations use
`shopping.create_shopping_results_widget`. Cart widgets save a snapshot; supported clients read
the current cart when View cart opens. This is read-only: opening a cart does
not change items or start checkout. Older clients retain the saved snapshot.
Present a verified shopping cart using a reference returned by shopping.read_cart.

This conversation isn't on screen, so put the returned `embed_token`, unchanged,
in what you hand back, where the cart belongs.

Create a cart widget only when a loaded connector doc
explicitly documents using `shopping.read_cart` and supplies its provider
identifier.

`{ cart_ref: string }`

Call `shopping.read_cart` with the doc's identifier, then copy its returned
reference into `cart_ref`. Never pass raw cart
JSON or use search results as a cart. Cart widgets save a snapshot; supported clients read
the current cart when View cart opens. This is read-only: opening a cart does
not change items or start checkout. Older clients retain the saved snapshot.
Defaults to true. Set false to place the cart at the returned embed_token after your summary.shopping.create_shopping_cart_widgetPresent a verified shopping cart using a reference returned by shopping.read_cart.
is_image_availableis_agentic_checkout_creation_enabledis_agentic_checkout_completion_enabledshopping.create_shopping_results_widgetPresent shopping product cards from resolved catalog, Marketplace, connector, or browser results.

This tool presents the widget immediately as a standalone card. In TypeScript-style shapes, `?` marks an optional field; every other field is required.

Use the artifact returned by `shopping.resolve_results`. Preserve the returned
URLs, product references, provider identity, retailer context, and advertised
actions; follow the owning connector doc for provider-specific workflows.
Pass exactly one of `path` or `products`; prefer `path`
when another tool wrote a `kind: "shopping_results"` JSON file.

`{ path?: string, products?: { url: string, name: string, citation_id: string,
image_url?: string | null, type?: "catalog" | "marketplace" | "browser", product_id?: string,
provider?: string,
brand?: string, price?: string, sale_price?: string, retailer_name?: string,
primary_action?: "add_to_cart" }[] }`

`provider` is the owning connector doc's canonical identifier, independent
of the rendering type. Connector cards use `type: "browser"`. The server adds
trusted provider attribution when all products share a provider, and a retailer
subtitle when they also share a non-empty `retailer_name`; do not supply logos
or attribution yourself. `brand` identifies the product brand.

Advertise `primary_action: "add_to_cart"` only when that connector doc
supports the operation. It requires `type: "browser"`, `provider`, and a
non-empty `product_id` unique within the widget. `retailer_name` is optional
context as required by the connector. Keep both agentic checkout capability
flags false. A click queues a normal agent turn requesting one additional
unit; it does not mean the cart changed or authorize checkout. Omit the action
for ordinary shopping cards to preserve their existing purchase behavior.
Present shopping product cards from resolved catalog, Marketplace, connector, or browser results.
hatch-media-workspace-mapping-unavailablebrowser task client timezone is not a canonical IANA timezonebrowser task client timezone is not a valid IANA timezoneobjective_idtool_contextrecovery_lease_ownerexperiment_armconfig_hashinput_fingerprintautomatic_cycleruntime.self_improvementself_improvement_objectivehatch-engine/crates/hatch-agent/prompts/inline/tools/objective_worker/step_execution.json#