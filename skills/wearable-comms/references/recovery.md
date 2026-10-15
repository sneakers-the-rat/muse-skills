# Recovering a Call or Text

## Stored contacts find no one

- Search other paired devices only when the selected device's stored search is complete and its `count` is zero, never to settle a weak, ambiguous or numberless result. Find them with `device.list` and search each one's stored contacts:

```bash
/opt/hatch/bin/device-data contacts search --match-mode ranked --device FALLBACK_DEVICE_ID --query NAME
```

- Finish every search before choosing, and treat all results as one set under the main resolution rules. If any search is incomplete or the set does not settle one person and line, ask.

- Offer a single fallback match as one numbered option, say it came from another paired device, and use it only after the user confirms. The call or text still goes from the selected device, never from the fallback.

- When every stored search is complete and empty, read the selected device's description, reusing one you already have. If it advertises `contacts.search`, run that live search on the selected device only, never on a fallback.

## Contacts have not synced

- Use this when the selected device's search reports `contacts_never_synced: true` and every stored and live search still found no one. The flag means no contacts are stored for that device. It does not show that the user skipped setup, so never say they did.

- If there was no fallback device, or every fallback also reported the flag, the name cannot be looked up. Say the phone contacts have not synced yet, without calling it a missing contact or asking for another spelling.

- If a fallback device without the flag was searched, say the name was not found on the user's other devices and ask whether it could be spelled differently.

- Then give the setup steps briefly. In the Meta AI app, open Settings, then Apps, Communicate hands-free, then Phone, and check that it is connected with every permission it asks for, including contacts. When `contacts_platform` is `ios`, also open iPhone Settings, then Bluetooth, tap the glasses, and turn on Sync Contacts and Show Notifications.

- Keep the reply brief and easy to follow by ear, and do not call or text from these empty results.

## iPhone messaging is off

- Use this when a text fails with `device_error_code: map_not_connected`. Only an iPhone reports it. The iPhone has not given the glasses its Bluetooth messaging connection, so the message was not sent. This is an iPhone Bluetooth setting, so skip the contacts steps above and never say "MAP".

- Tell the user the message was not sent. On the iPhone, they open Settings, then Bluetooth, tap the info icon next to the glasses and turn on Show Message Notifications. If that setting is missing or already on, turning Bluetooth off and back on in iPhone Settings usually restores the connection. Offer to send the message again once they have done that, and wait for them to ask.

- When they ask, send the same message once more. If it fails the same way, do not repeat a step they already tried, and suggest the Bluetooth restart if they have not done it.

- Otherwise explain that an iPhone gives this connection to one device at a time, so a car, a headset or other glasses connected with messaging may be holding it. Ask them to disconnect or turn off that device, keep the reply brief, and send again only when asked.
