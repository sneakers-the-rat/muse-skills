# Home Control

## Identify the device

- Find the intended home, room and device and the state the user wants. Similar names can refer to different devices, so resolve any ambiguity before acting.

- Read the current state and the controls the device supports before changing it. A connected account does not prove the device is reachable.

- For devices paired with Muse, run `device.list`, read the advertised commands with `device.describe` and use only those with `device.invoke`. For Muse Home Link, read `~/docs/devices/home_link.md` and the integration guide it links. Never invent a control endpoint or command.

## Act and confirm

- Set an explicit state instead of toggling, especially when a retry is possible. Respect the user's limits and any safety condition that applies.

- After a timeout or an uncertain result, read the state before sending the command again. A queued or accepted request is not a confirmed physical change.

- Schedule a timed routine with `cron.add` in the user's timezone, and update an existing schedule instead of adding a duplicate. For an action when the user arrives or leaves, set a geofence on their phone through `device.invoke` with the `geofence.set` command.

- For camera questions, read the recorded events or saved images and show them. Past events and saved images are not live monitoring or proof that the home is safe now.

## Available connectors

- [Philips Hue](/opt/hatch/connectors/philips_hue/CONNECTOR.md) for Hue lights, rooms, zones and scenes, including brightness, color, color temperature and effects.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Arlo](/opt/hatch/connectors/arlo/CONNECTOR.md) for the latest image each Arlo camera saved.

- [Ring](/opt/hatch/connectors/ring/CONNECTOR.md) for event history, saved snapshots and recorded video from shared Ring devices.

## Alternatives for better results

- If the user runs Home Assistant, its API can control many brands of device through one custom connector instead of one per manufacturer.

- Point the user to the manufacturer's app for what these connectors cannot do, such as live camera view, arming a system or sounding a siren, and say which step is still theirs.

- When a device stays unreachable, explain the unfinished action and the physical control the user can use. Check whether an earlier command completed before trying another route.
