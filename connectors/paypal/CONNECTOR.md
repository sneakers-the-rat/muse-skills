# PayPal

- Connect PayPal from Settings, Wallet. Complete sign-in using the PayPal authorization link.

- Use `/opt/hatch/bin/paypal auth status` to read the saved connection state. To reconnect, disconnect PayPal in Settings and connect it again.

- Use `/opt/hatch/bin/paypal wallet user-info` for a live PayPal account lookup. It returns the connected account's available identity, name, email, and address fields.

- Use `/opt/hatch/bin/paypal auth inspect` to verify the connection with PayPal. A missing local connection reports `disconnected`. A rejected token reports `reauth_required`; a network failure is an error, not evidence that the account is disconnected.

- Use `/opt/hatch/bin/paypal auth disconnect` to get the connector disconnect confirmation link. After the user confirms in Settings, Muse attempts to revoke PayPal consent and removes the local connection even if PayPal's revocation fails. Report remote revocation as successful only when confirmed. If browser cleanup is pending, report that status and retry disconnect to finish it.

## Related skills

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.
