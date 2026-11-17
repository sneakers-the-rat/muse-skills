# Podcast language support

- Check the intended spoken language before writing a script, generating audio
  or scheduling generation. This applies to explicit language requests, the
  conversation's language when used for narration, existing scripts, and
  recurring episodes. If the intended narration language is unclear, ask.

- Check the language the user wants spoken, not just a supplied language code
  or the script's alphabet. Urdu written in Latin letters is still an Urdu
  narration request; labeling an Urdu script `hi` does not make it Hindi.
  Arabic support does not imply support for Urdu or Persian written in a
  related script. Do not reinterpret an explicit request as another language.

- This reference governs generated podcast audio. Live voice conversation has
  its own language capabilities; neither list establishes the other's support.
  Keep the explanation specific to podcast generation and follow the current
  conversation's response-language rules. A supported podcast language does
  not authorize speaking that language in a live call.

## Supported languages

The current podcast speech backend supports these 25 languages. Regional locale
forms such as `pt-BR` or `pt_BR` refer to the corresponding base language; they
are not additional languages. Use this table to check narration support.
When describing podcast language options, mention three to five naturally
and invite the user to choose. Give the full list only when explicitly asked
for all supported podcast languages.

| Language | Code |
|---|---|
| Arabic | `ar` |
| Bengali | `bn` |
| Chinese | `zh` |
| Dutch | `nl` |
| English | `en` |
| French | `fr` |
| German | `de` |
| Hebrew | `he` |
| Hindi | `hi` |
| Indonesian | `id` |
| Italian | `it` |
| Japanese | `ja` |
| Kannada | `kn` |
| Korean | `ko` |
| Malay | `ms` |
| Marathi | `mr` |
| Polish | `pl` |
| Portuguese | `pt` |
| Spanish | `es` |
| Tagalog | `tl` |
| Tamil | `ta` |
| Telugu | `te` |
| Thai | `th` |
| Turkish | `tr` |
| Vietnamese | `vi` |

## Unsupported language requests and failures

Urdu (`ur`), Persian/Farsi (`fa`), Russian (`ru`), Punjabi (`pa`), and Swahili
(`sw`) are examples of languages not currently supported. The supported list
above is the available output-language set, not just a list of examples.

When the requested narration language is unsupported:

- Briefly say that podcast generation in that language is not supported yet.
  Offer three to five supported languages from the table, choosing relevant
  alternatives from the conversation, and ask the user to choose. Give the
  full list only when explicitly requested. Use plain language; backend
  names, codes, and error-byte counts are not useful to them.

- Do not call generation, change the voice or engine, silently translate,
  create a recurring generation job, or schedule a retry. Do not promise that
  waiting will make the language work. A written script in the requested
  language can be offered as an alternative, without presenting it as audio.

- If generation was already attempted, explain the same limitation and stop
  this episode's retries. A tool message about empty/truncated audio, including
  a 26-byte response, may call it transient; that wording does not override a
  known unsupported narration language. Conversely, the byte count alone does
  not prove a language rejection for a supported-language script.

- Generate in a supported language only after the user chooses or has already
  authorized that language. Ordinary supported-language generation and its
  transient-failure retry policy still apply.

## Maintenance

- Checked 2026-10-23 against Shortwave/Kepler's
  `fbcode/realtimeai/cosmos/kepler/configs/_language_config.py`:
  `SUPPORTED_TTS_LANGUAGES` is the union of `M1_LANGS`, `M2_LANGS`, and `M3_LANGS`.
  `LID_DETECTABLE_LANGUAGES` is broader and is not a synthesis-support list.

- Recheck the backend allowlist when updating this reference. This is a
  capability list, not a guarantee of pronunciation quality for every voice.
