# 1Password

- Sign in to websites in the Muse browser using logins stored in the user's 1Password vault.

- The user grants access to specific saved logins when signing in to websites in the Muse browser. Muse fills the selected login credentials from 1Password into the website without returning their values to you. This connector does not support browsing the user's vault.

- Connecting 1Password is not required to sign in to websites in the Muse browser. When connected, it is available as an option in the sign-in flow.

## Connect

- To check whether 1Password is connected, run `/opt/hatch/bin/onepassword status` with `muse.exec`. It reports `connected`, `not_connected`, or `reauth_required` when the user needs to reconnect.

- When the user asks to connect, or requests work that requires a 1Password account that is not connected, run `/opt/hatch/bin/onepassword authorize-url` with `muse.exec`. Present the returned `connect_url` unchanged as `[Connect 1Password](<connect_url>)` on its own line, then wait for the user to complete authorization.

- When the user asks to disconnect 1Password, run `/opt/hatch/bin/onepassword disconnect` with `muse.exec`. Present the returned `disconnect_url` unchanged as `[Disconnect 1Password](<disconnect_url>)` on its own line, then wait for the user to complete disconnection.

- If either command fails, report that the requested connection or disconnection could not be started. Generating a link does not confirm a change in connection status.

## When 1Password can be used

To approve access to saved logins for websites in the Muse browser, the user needs the 1Password app installed on the device they are approving from:

- Muse on the web: the 1Password desktop app for Mac or Windows must be installed on that computer. The Chrome extension cannot be used for this.

- Muse on iOS: the 1Password app must be installed on that iOS device.

- Muse on Android: the 1Password app must be installed on that Android device.

The app can be downloaded from the Apple App Store, Google Play, or [1Password.com](https://1password.com), depending on the device.

A connected account does not confirm that the required app is installed on the user's device.

## Related skills

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.
