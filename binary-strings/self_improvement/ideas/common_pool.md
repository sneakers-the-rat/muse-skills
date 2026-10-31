## General version

Every card in this section is written for a specific user. We also want a general version, which applies to a broader audience as well. You should judge whether the idea still makes sense without the specific user info, and then write a general version of it.

## Judging

A personalized card stands for a specific need of a user, it can be about the user’s specific instance, like order, account, place or date.

We should consider the need and the instance together.

First, whether the need is applicable to a broader audience? If so, judge whether we should keep the instance. If the need + instance applies to a broader audience as well, like a trip to a popular destination like Japan, then keep the detailed instance. If the need is broad applicable, but the instance itself is only applicable to a small part of users or the instance is directly from user’s history or highly derived from the user’s own data, then we should replace the instance with a broader category. Also, we should treat the different instances in the card as a combination, if the combination itself is not common or directly derived from the user's own info, then we should consider to rewrite them.

If the need is niche, only for a very small part of users, or the need doesn’t make sense without the specific instance, then the idea is ineligible for a general version. Also, we should avoid cards reading like advice for sensitive topis like health and finance.

## Writing

Rewrite the idea card for broader audience.

- When the detailed instance needs to be replaced, replace it with a category it belongs to.
- Make sure to remove all the PII info in the card
- Don’t assume anything about the user. “You/your” is applicable when it’s a general “you” that apply to a broad audience. Avoid any specific you/your that assumes the user’s life stage or condition, like your wife, your 40s, your dog and etc.
- Respect the rules here first when there’s conflict with style guide. Other additional rules in style guide still valid.

For the fields:

- Title: 6-10 words, 60 characters max. Make it attractive to give the real outcome or hook first, better start with a verb. Use the second person tone or write it as a command.
- Summary: 1-2 short sentences, more detailed description of the card.
- Prompt: the sentences what will be sent to assistant by the user themselves, use first person tone. 1-2 short sentences.
- Instructions: the markdown plan that the assistant will follow to execute, 400 words max. Write from the card’s build plan, items and execution contract. Try to keep it aligned with the personalized version, but remove all the detailed PII info from the user. Anything the assistant needs to know, let it directly ask the user. If the assistant needs any permission like sending, posting, or spending, let it ask the user first before doing it.

## Filing

Write the output to pool field. If it’s eligible, mark eligible as true and fill all the fields. If it’s ineligible, fill the reason.

Don’t make any change to the personalized idea.
,TimeDelta::hours out of boundsmemorytravelalignmentskill_improvementwindow_sincewindow_untilidle_gatedgoals bookkeeping has a composite cursor without a last-run timestampgoals bookkeeping has a last-run timestamp without a composite 