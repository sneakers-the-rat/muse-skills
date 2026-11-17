# Recovering a Call or Text

## Stored contacts find no one

- Search other paired devices only when the selected device's stored search is complete and its `count` is zero, never to settle a weak, ambiguous or numberless result. Find them with `device.list` and search each one's stored contacts:

```bash
/opt/hatch/bin/device-data contacts search --match-mode ranked --device FALLBACK_DEVICE_ID --query NAME
```

- Finish every search before choosing, and treat all results as one set under the main resolution rules. If any search is incomplete or the set does not settle one person and line, ask.

- Offer a single fallback match as one numbered option, say it came from another paired device, and use it only after the user confirms. The call or text still goes from the selected device, never from the fallback.

- When every stored search is complete and empty, read the selected device's description. Refresh it after a setup change or a requested retry as the main skill requires. If it advertises `contacts.search`, run that live search on the selected device only, never on a fallback.

- If every search is complete and found no one, and the selected device's search did not report `contacts_never_synced: true`, say the name wasn't found among the contacts shared with Muse and that nothing was sent, and ask for the number or the name the person is saved under. When the selected device's `platform` is `ios`, add that if they are saved on the iPhone, Meta AI may have access to only some contacts: in iPhone Settings, open Apps, then Meta AI, then Contacts, and choose Full Access. Do not say the person isn't on the phone, and skip the Phone setup.

## Contacts have not synced

- When "Calling and texting commands are unavailable" below applies, follow it instead. The missing command, not the contacts, is why it failed.

- Use this when the selected device's search reports `contacts_never_synced: true` and every stored and live search still found no one. The flag means no contacts are stored for that device. It does not show that the user skipped setup, so never say they did.

- If there was no fallback device, or every fallback also reported the flag, the name cannot be looked up. Say the phone contacts have not synced yet, without calling it a missing contact or asking for another spelling.

- If a fallback device without the flag was searched, say the name was not found on the user's other devices and ask whether it could be spelled differently. Do not offer setup from these results.

- Offer setup only when all completed searches found no matches and every searched device reports `contacts_never_synced: true`.

- Then give the setup steps briefly. In the Meta AI app, open Settings, then Apps, Communicate hands-free, then Phone, and check that it is connected with every permission it asks for, including contacts. When `contacts_platform` is `ios`, also open iPhone Settings, then Bluetooth, tap the glasses, and turn on Sync Contacts and Show Notifications.

- Keep the reply brief and easy to follow by ear, and do not call or text from these empty results.

## iPhone messaging is off

- Use this when a text fails with `device_error_code: map_not_connected`. Only an iPhone reports it. The iPhone has not given the glasses its Bluetooth messaging connection, so the message was not sent. This is an iPhone Bluetooth setting, so skip the contacts steps above and never say "MAP".

- Tell the user the message was not sent because their iPhone hasn't given the glasses its Bluetooth messaging connection. On the iPhone, they open Settings, then Bluetooth, tap the info icon next to the glasses and turn on Show Message Notifications. If that setting is missing or already on, turning Bluetooth off and back on in iPhone Settings usually restores the connection. Offer to send the message again once they have done that, and wait for them to ask.

- When they ask, run `device.describe` on the selected device again and send the same message once more if a compatible command is available. If it fails the same way, do not repeat a step they already tried, and suggest the Bluetooth restart if they have not done it.

- If they have already restarted Bluetooth, explain instead that an iPhone gives this connection to one device at a time, so a car, a headset or other glasses connected with messaging may be holding it. Ask them to disconnect or turn off that device, keep the reply brief, and send again only when asked.

## Android texting permission is off

- Use this when a text fails with `device_error_code: permission_denied` on glasses whose `platform` is `android`. The phone has not let the Meta AI app send texts, so nothing was sent.

- Say that, and give the steps on the phone: Settings, then Apps, then Meta AI, then Permissions, then SMS, and allow it. Skip the Phone setup and Bluetooth steps, and give no duplicate warning.

- Offer to send the message once they have allowed it, and wait for them to ask.

## The phone limited or could not send the text

- For `rate_limited`, nothing was sent, because the phone limits how many texts it sends to one person in a short time. Do not say earlier texts were sent. Ask them to wait a few minutes before trying again.

- For `no_service`, nothing was sent, because their phone had no cellular service or its radio was off. Ask them to check their signal and turn off airplane mode if it is on.

- For `attempt_failed`, nothing was sent, because their phone could not start sending it. Say their phone couldn't send the text, not the glasses or the other person's phone. The phone gives no cause, so don't guess one or give setup steps, and give no duplicate warning. Offer to try once more and wait for them to ask; they can also send it themselves from their phone.

- For `rate_limited` and `no_service`, offer to send it again once that is sorted, and wait for them to ask.

## Calling and texting commands are unavailable

- Use this when a requested call or text was not dispatched and a fresh `device.describe` of the selected device advertises neither calling nor texting commands. A timeout or a disconnected device does not establish that commands are unavailable, and absent commands alone do not establish why.

- Say that calling and texting are unavailable on the selected device, using its name, and that the requested action did not happen. Show where to check setup: Meta AI app, Settings, Apps, Communicate hands-free, Phone; connect it and allow access to calls, messages and contacts. For a text, when the wearable's `platform` is `ios`, also give iPhone Settings, then Bluetooth, the info icon next to the glasses, then Show Message Notifications. Give no Bluetooth steps for a call.

- Do not blame contacts, even when they have not synced, and do not ask for a number or another spelling to send it now.

- If the user requests another attempt, refresh the same device's description before deciding what to do. When a compatible command is now advertised, use it for that requested attempt. Do not switch to another device or a `phone.*` tool.

- If the fresh description still advertises neither command and setup instructions were already provided for that unresolved problem, state the current unavailability and that the action did not happen, then offer to review the steps. Do not repeat the steps or end with an invitation to try again or resend. This review-only response does not apply to a new `map_not_connected` failure.
