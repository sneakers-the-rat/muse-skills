## General version

Every card in this section is written for a specific user. We also want a general version, which applies to a broader audience as well. You should judge whether the idea still makes sense without the specific user info, and then write a general version of it.

Note that the broader audience has no context about the card. They may meet it mid-scroll in a Facebook or Instagram feed, where the title is the only thing they see, and acting on it means opening or downloading an app. So the bar is not whether they can understand the card, but whether they would stop for it. The need has to be one that many people have often, or one that hurts enough to act on right away.

## Judging

A personalized card is built on a specific need of a user. It can be about the user's specific instance, like an order, an account, a place or a date.

We should consider the need and the instance together.

First, ask whether the need is applicable to a broader audience. Judge the need itself, not the life event it sits under. The parent event is often common while the need underneath it is rare. If the need is broadly applicable, judge whether we should keep the instance. If the need and the instance together apply to a broader audience as well, like a trip to a popular destination such as Japan, then keep the detailed instance. If the need is broadly applicable, but the instance itself is only applicable to a small share of users or the instance is directly from the user's history or highly derived from the user's own data, then we should look for another concrete anchor the card already has and keep that instead. A well-known brand, product, place, or event is a shared anchor even when it comes from the user's interests, so keep it. What gets replaced is what belongs to the user alone, like their own order, account, or schedule.

Also, we should treat the different instances in the card as a combination. If the combination itself is not common or is directly derived from the user's own info, then we should rewrite them.

Rewriting means three moves: swap the instance for a mainstream anchor the card already has, replace it with the plain category it belongs to, or drop the state the card assumes the user is in. After a category swap, check the result: the card still has to name what it acts on and what the user gets. If no move leaves anything concrete, mark the card ineligible instead of flattening it.

Ineligible cases:

- The need is niche, only for a very small share of users.
- The need doesn't make sense without the specific instance.
- The need is a one-off chore, or a problem that only exists in one moment, with no ongoing capability behind it worth selling, like confirming a checkout time or getting one device to pair.
- The card is a step in one person's specific story. A good card is one any reader can fill in from their own life. A card that depends on a particular person, deal, or case, on a small task, or on something already under way (stalled, postponed, cancelled, "that invoice") does not, like "Draft your bike rental reply with dates confirmed" or "Reopen a stalled hotel points case". When the need behind the step is big enough, offer the help from the start, before anything is under way.
- The card reads like advice on sensitive topics such as health or finance.
- Without the instance, the card becomes too general and abstract to feel meaningful or attractive. The giveaway is that you can't say what the card acts on, or what the user ends up with. Bad examples: "Catch early events with earlier reminders", "Find the true cheapest delivered price".

## Writing

Rewrite the idea card for a broader audience, who don't have any context about the card.

- Write the title, summary, and prompt in the same language as the personalized card, the way a native speaker of that language would say them rather than as a translation. Write the instructions in English.
- Make sure to remove all the PII in the card.
- If the card is about one occurrence of a need that recurs, sell the ongoing capability behind it instead, and let the instructions grow to cover that bigger promise.
- Don't assume anything about the user. "You/your" is applicable when it's a general "you" that applies to a broad audience. Avoid any specific you/your that assumes the user's life stage or condition, like your wife, your 40s, or your dog. Don't assume what they have already done or already own either.
- Name the capability that makes the card worth tapping. If a generic verb could open almost any card, it's hiding the point.
- Write the way the audience talks. Nothing that reads like a marketing line.
- Keep the tone easy, with no urgency that assumes the reader is about to act, like "today" or "your next phone". Timing many readers share works, like booking a trip before Christmas.
- Respect the rules here first when there's a conflict with the style guide. Other additional rules in the style guide are still valid.

For the fields:

- Title: 6 to 10 words, 60 characters max. It's the only part the user sees, so it has to land on its own.
  - Content: name the concrete thing the card acts on and what the reader gets out of it.
  - Wording: use plain, literal, everyday words that someone who never saw the personalized card understands on first read. Clear beats clever, with no filler or marketing lines.
  - Voice: if the title as a bare command would read like a to-do for the reader, write it as the assistant offering to do it, starting with "I can" or "Let me" in English, or the natural way to make that offer in the card's language. Otherwise, leave the assistant out and open with whatever carries the action and result best, such as a verb, a question, or the benefit.
- Summary: 1-2 short sentences, a more detailed description of the card.
- Prompt: the line the user sends to their assistant themselves, in first person. 1-2 short sentences.
- Instructions: the Markdown plan that the assistant will follow to execute, 400 words max. Write it from the card's build plan, items and execution contract. Try to keep it aligned with the personalized version, except where the general card promises the broader capability, then cover that instead. Remove the user's PII. Anything the assistant needs to know, let it directly ask the user. If the assistant needs any permission like sending, posting, or spending, let it ask the user first before doing it.
- Language: the lowercase two-letter ISO 639-1 code, with no region, of the language you wrote the title, summary, and prompt in.

## Filing

Write the output to the `pool` field. If it's eligible, mark `eligible` as true and fill in all the fields. If it's ineligible, mark `eligible` as false and fill in the reason.

Don't make any change to the personalized idea.
queue_claim_boot_id,TimeDelta::hours out of boundsmemorytravelalignmentideasskill_improvementwindow_sincewindow_untilidle_gatedgoals bookkeeping has a composite cursor without a last-run timestampgoals bookkeeping has a last-run timestamp without a composite cursor 