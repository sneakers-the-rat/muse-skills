Reassess the health classification before researching the draft. Treat the
current request as related to health when it needs specific medical advice:
advice or assessment about a particular person's or pet's symptoms, injury,
surgery, health condition, test results, readings, treatment decisions,
pregnancy, or breastfeeding. Include questions about whether to take, dose, or
combine medicines. Treat general medical explanations that concern no
particular person as unrelated to health. Include a report of immediate medical
danger even when the user asks only to record it.

Treat basic nutrition and general, well-known health advice like these as
unrelated to health:

- calorie counting
- macronutrient counting
- nutrition logs
- nutrition labels
- eating, hydration, and sleep habits
- basic fitness coaching

Treat one of these requests as related to health when it also needs specific
medical advice.

Resolve short follow-ups against the latest conversation topic. After a topic
change, use the new topic unless the current request explicitly returns to an
earlier one. Do not carry health relevance forward from an older topic.

If the current request is unrelated and the draft contains no specific medical
advice, call verifier.not_relevant immediately. The runtime returns the exact
original draft and skips the resolve phase. Continue verification if the draft
itself contains specific medical advice, even when it went off topic. Do not use
this tool for missing evidence or uncertainty about a medical answer.
