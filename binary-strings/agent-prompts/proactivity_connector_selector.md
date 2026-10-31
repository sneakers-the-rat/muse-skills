# Starter tasks for the connector_followup_items_variant QE. Each group lists
# the three tasks its connectors offer after a connection. A recurring task
# sets its schedule up on tap. After a task's result, the main agent asks one
# next-step question whose options are the next steps it writes from that
# result, guided by next_steps, followed by the task's fixed followups, such as
# a schedule. A note adds task-specific guidance for the main agent. Each arm
# says how the main agent shows the tasks, and choice says how it handles the
# one the user picks.
groups:
  - providers: [google_calendar, microsoft_calendar]
    items:
      - title: Send me my day every morning
        subtitle: Today's schedule now, then a recap each morning
        icon: morning-brief
        message: Show me my schedule for today, then send it to me every morning
        recurring: true
        next_steps: a step about a specific event you showed, or changing what time the recap arrives
        note: If it is already evening for the user or today has no events left, also show tomorrow's schedule. Set the recap for about 7am in the user's time zone unless they asked for another time. If the calendar has nothing left today and nothing tomorrow, say that in one sentence and offer adding an event and finding plans in their email as your next steps. Write into the recap job that on a day with nothing scheduled, it sends one short line asking whether to add plans, with "Add an event" and "Find plans in my email" as buttons, rather than a line that only says the day is clear.
      - title: Get me ready for what's next
        subtitle: What to bring, when to leave, or what to know
        icon: backpack
        message: Get me ready for my next event with what I need for it, like what to bring, when to leave, or what to know going in
        next_steps: a step that names that event and something it needs
        note: If nothing is coming up on the calendar, say that in one sentence and offer adding an event and finding plans in their email as your next steps.
        followups:
          - option: Get me ready before each event
            does: schedule one morning job that sets up that day's heads-ups before each event, rather than a job that keeps checking the calendar
      - title: Add plans from my email
        subtitle: Invites, school emails, and plans your calendar missed
        icon: email
        message: Find plans in my email that aren't on my calendar yet, like invites, school or club events, and appointments. Add them and tell me what you added
        next_steps: a step about a specific plan you added or found
        followups:
          - option: Do this every evening
            does: schedule an evening job that adds new plans from email and, only when it added something, messages the user what it added
        note: Add the events right away and let the normal calendar permission decide whether to ask first. If no email account is connected, offer the email connection right away.
  - providers: [google_drive]
    items:
      - title: Sum up my key docs
        subtitle: A short summary of the docs you use most
        icon: star
        message: Find the Google Drive docs I open most and tell me in a line or two what each one is about
        next_steps: a step about one specific doc you summarized, such as going deeper into it or acting on something in it
        followups:
          - option: Alert me to edits
            does: schedule a daily check that messages only when someone else edited one of these docs, saying who changed what
        note: Pick the docs the user has opened most recently, not the ones edited most recently. If Google Docs is not connected, name the docs, then offer the Google Docs connection right away so you can summarize them once it's connected.
      - title: See what's using my storage
        subtitle: How full your storage is and your biggest files
        icon: cloud-data
        message: Show me how full my Google storage is and which Drive files take up the most space
        next_steps: a way to free space based on what takes the most, such as specific large Drive files, or large email attachments when Gmail uses the most
        followups:
          - option: Alert me when nearly full
            does: schedule a weekly check that messages only when storage is more than 90% full
        note: Google storage is shared by Drive, Gmail and Photos, so say how much each one uses. Delete nothing unless the user names the files or taps an option that names them.
      - title: Tidy up my Drive
        subtitle: Duplicates, untitled files, and empty folders
        icon: broom
        message: Find the clutter in my Google Drive, like duplicate files, untitled docs, and empty folders, and show me what could go
        followups:
          - option: Move them to trash
            does: move everything you listed to the trash, say how many went, and say they can be restored from the trash for 30 days
          - option: Let me pick
            does: ask which of the listed files to trash, then trash only those
          - option: Check every month
            does: schedule a monthly check that lists new clutter, trashes nothing on its own, and delivers the list with "Move them to trash" and "Let me pick" as buttons
        note: Trash nothing until the user picks an option or names files, and do not delete anything permanently. Leave out files that other people own or that are shared with others. When more than 20 items could go, say in the result exactly how many items "Move them to trash" will move. Count each extra copy, untitled doc, and empty folder as one item.
  - providers: [google_docs]
    items:
      - title: Sum up my key docs
        subtitle: A short summary of the docs you use most
        icon: star
        message: Find the Google Drive docs I open most and tell me in a line or two what each one is about
        next_steps: a step about one specific doc you summarized, such as going deeper into it or acting on something in it
        followups:
          - option: Alert me to edits
            does: schedule a daily check that messages only when someone else edited one of these docs, saying who changed what
        note: Pick the docs the user has opened most recently, not the ones edited most recently.
      - title: Polish one of my docs
        subtitle: Fixes for typos, wording, and unclear spots
        icon: edit
        message: Help me polish one of my Google Docs
        followups:
          - option: Make the fixes
            does: apply the changes you showed most recently to the doc, either the fixes or the shorter version, and say what changed
          - option: Make it shorter
            does: show a tighter version of the doc that keeps its meaning, and end with the same question and options
        note: First ask which doc, with the user's three most recently edited docs that they own as options. Then show fixes for typos, wording, and unclear spots in the doc they pick. Change nothing until the user picks "Make the fixes".
      - title: Make slides from one of my docs
        subtitle: A short deck from a doc you pick
        icon: presentation
        message: Make a short slide deck from one of my Google Docs
        next_steps: a change to the deck based on its content, such as a section to expand or cut
        followups:
          - option: Save to Google Slides
            does: save the deck as Google Slides and give the user the link, offering the Google Slides or Google Drive connection first if neither is connected
        note: First ask which doc, with the user's three most recently edited docs as options. Then build the deck from the doc they pick.
  - providers: [messenger_companion]
    items:
      - title: Catch me up on my chats
        subtitle: I'll sum up what you missed in your chats
        icon: conversation
        message: Catch me up on my Messenger chats
        next_steps: a step about a specific chat, such as replying to someone who is waiting on the user
        followups:
          - option: Catch me up every evening
            does: set up an evening catch-up through the normal scheduling flow
      - title: Help me reply to my chats
        subtitle: I'll draft replies to whoever's waiting on you
        icon: chat-sparkles
        message: Draft replies to the Messenger chats I haven't answered for me to approve
        followups:
          - option: Send them
            does: send the drafts exactly as shown
          - option: Redraft
            does: rewrite every draft in a clearly different style, such as shorter and more casual or closer to how the user usually writes to that person, show them again, and end with the same question and options
          - option: Remind me later
            does: set a one-time reminder for this evening, or for tomorrow morning if it is already evening for the user, that checks whether the chats moved on, updates the drafts if needed, and delivers them with "Send them" and "Redraft" as buttons
        note: Ask "Want me to send these?" as the question, and mention that the user can also tell you what to change.
      - title: See my month in chats
        subtitle: Your top friends, most-shared reels, and best moments
        icon: party-popper
        message: Show me my month in Messenger chats, with my top friends, the reels we shared most, and a few highlights
        next_steps: a step about a specific friend or reel from the recap
        followups:
          - option: Show me last month
            does: make the same recap for the previous calendar month
          - option: Send this every month
            does: set up a monthly recap through the normal scheduling flow
  - providers: [instagram_messages]
    items:
      - title: Catch me up on my DMs
        subtitle: I'll sum up what you missed in your DMs
        icon: chat-bubble
        message: Catch me up on my Instagram DMs
        next_steps: a step about a specific DM, such as replying to someone who is waiting on the user
        followups:
          - option: Remind me tomorrow
            does: set a one-time reminder for tomorrow morning to catch up on Instagram DMs again
      - title: Help me reply to my DMs
        subtitle: I'll draft replies to whoever's waiting on you
        icon: email-draft
        message: Draft replies to the Instagram DMs I haven't answered for me to approve
        followups:
          - option: Send them
            does: send the drafts exactly as shown
          - option: Redraft
            does: rewrite every draft in a clearly different style, such as shorter and more casual or closer to how the user usually writes to that person, show them again, and end with the same question and options
          - option: Remind me later
            does: set a one-time reminder for this evening, or for tomorrow morning if it is already evening for the user, that checks whether the chats moved on, updates the drafts if needed, and delivers them with "Send them" and "Redraft" as buttons
        note: Ask "Want me to send these?" as the question, and mention that the user can also tell you what to change.
      - title: See my month in DMs
        subtitle: Your top friends, most-shared reels, and best moments
        icon: confetti
        message: Show me my month in Instagram DMs, with my top friends, the reels we shared most, and a few highlights
        next_steps: a step about a specific friend or reel from the recap
        followups:
          - option: Show me last month
            does: make the same recap for the previous calendar month
          - option: Send this every month
            does: set up a monthly recap through the normal scheduling flow
  - providers: [plaid]
    items:
      - title: Find my subscriptions
        subtitle: I'll list your recurring charges and what they cost
        icon: receipt
        message: Find all my subscriptions and recurring charges, including ones that started recently, and tell me what each one costs
        next_steps: a step about a specific subscription, such as cancelling one the user may not use
        followups:
          - option: Check every week
            does: schedule a weekly check that messages only when a new subscription or a price increase shows up
      - title: Send me a weekly spending check-in
        subtitle: This week's spending now, then every Sunday
        icon: chart-up
        message: Show me where my money went this week and flag anything unusual, then send me a spending check-in every Sunday
        recurring: true
        next_steps: a step about a specific category or charge from this week, or changing which day the check-in arrives
      - title: Show me what's coming due
        subtitle: I'll list upcoming card and loan payments
        icon: credit-card
        message: Show me my upcoming card and loan payments and when each one is due
        next_steps: a step that names one specific payment and its due date
        followups:
          - option: Remind me before each payment
            does: schedule one job that reminds the user a few days before each card and loan payment you listed is due
  - providers: [spotify]
    items:
      - title: Make me a playlist of new finds
        subtitle: Fresh songs like the ones you love, saved to Spotify
        icon: headphones
        message: Make me a Spotify playlist of new songs like the ones in my library that I haven't saved yet
        next_steps: a change that names a specific artist or song in the playlist
        followups:
          - option: Add new finds every Friday
            does: schedule a Friday job that adds a fresh batch of new finds to this same playlist
      - title: Tell me when my artists tour
        subtitle: Shows near you now, then new ones every week
        icon: ticket
        message: Find upcoming shows near me from the artists I play most on Spotify, then check every week and tell me when they announce new shows or presales near me
        recurring: true
        next_steps: a step about a specific show near the user, such as its presale, getting tickets, or adding it to the calendar
        note: If the user's city isn't known, ask for it before searching, and list only shows near them. If no shows are near them yet, say so, leave out ticket steps, and still set up the weekly check. Have the weekly check message the user only when it finds a new show or presale near them.
      - title: Tell me what my music says about me
        subtitle: Your taste in a nutshell, from your library
        icon: music-note
        message: Look at my Spotify library and tell me what my music taste says about me
        next_steps: a step about a specific artist or genre from the summary
arms:
  options: |
    ## Starter tasks
    Skip this section when you are continuing a pending task that needed this connection.
    Otherwise, after the one-sentence connection confirmation, add one short sentence on what you can now do with this connection, then offer these three starter tasks. They replace any instruction above to stop after the confirmation or to list example uses.
    If the user sent another message while you were preparing this reply, answer it too. Still give the confirmation and the starter tasks unless that message continues a task that needed this connection.
    Write the line "Want me to start on one of these?" translated into the response language. Then call muse.create_options with these options, translated into the response language and kept in this order:
    {titles_json}
    Wait for its result and place the returned embed_token right after the line. Do not list the tasks in text, and do not add other suggestions or another question. The one exception is a two-factor sentence asked for above, which goes after the embed. If muse.create_options fails, write the line followed by a Markdown list of the titles instead.
    Tapping an option sends its text as the user's message.
  widget: |
    ## Starter tasks
    Skip this section when you are continuing a pending task that needed this connection.
    Otherwise, after the one-sentence connection confirmation, offer these three starter tasks. They replace any instruction above to stop after the confirmation or to list example uses.
    If the user sent another message while you were preparing this reply, answer it too. Still give the confirmation and the starter tasks unless that message continues a task that needed this connection.
    Translate the line, titles, subtitles, and message text into the response language. Keep image URLs, tool names, and control fields unchanged.
    Before writing the response, load the widget tools with tool_search.load_tool_namespace. Then call widget.create_list_widget once with present_now false and language set to the response language as a BCP 47 tag, using these arguments with the visible text translated:
    {items_json}
    Keep the rows in this order. Copy each image_url unchanged. Do not add a list title.
    If the widget was created, write the confirmation and the line "Want me to start on one of these?" in one bubble. Then add <message_break/> and the returned embed_token alone. Do not repeat the rows in text, and do not add other suggestions or another question. The one exception is a two-factor sentence asked for above, which goes in its own bubble after the embed.
    If widget.create_list_widget reports that lists are unsupported or cannot create the widget, offer the tasks as option buttons instead. Write the same line, call muse.create_options with these options translated and kept in this order, and place the returned embed_token right after the line:
    {titles_json}
    Do not claim a list was shown. If muse.create_options also fails, write the line followed by a Markdown list of the titles.
    Tapping a row sends its data.text as the user's message, and tapping an option sends its text.
choice: |
  These tasks are optional, and offering them starts no work. Wait for the user's choice or another request before acting. When the user picks one, handle it through the normal task flow and then follow its line below:
  {choices}
  Ask the next-step question once, translated, at the end of the reply that delivers the task's result. It is the reply's only question, including rhetorical ones like "Accurate?", so state anything else worth acting on, such as a conflict, without asking about it. Call muse.create_options with that task's options, translated into the response language, and offer at most three. Wait for its result and place the returned embed_token right after the question.
  Write each of your next steps as a short request in the user's voice. Base them on the result: name the specific person, event, file, or item a step acts on when the result gives you one, and use a general step when it is the most useful next move. Write each step so it can start as soon as it is tapped. Make each step different from the listed options.
  Treat a tapped option as the user's own request. The normal approval flow still applies to anything it sends, deletes, buys, or shares. Creating or showing the options is not consent. Set up a schedule only after the user picks its option or asks for it.
  If a task needs more from the user first, ask for it and ask the next-step question once the task is done. If the account's data is not ready yet because it was just connected, say in plain words that you'll send the result shortly, keep working on it in the background, and deliver the result and the next-step question as soon as it's ready. Do not end on a promise with no work still running. Skip the next-step question if the task fails. Set up every schedule through the normal scheduling flow. If a scheduled run will bring back a choice for the user, such as drafts to send or files to trash, write into the job that the delivered message ends with those choices as muse.create_options buttons. A recurring pick or a picked schedule option is the go-ahead, so do not ask again whether to schedule it.
