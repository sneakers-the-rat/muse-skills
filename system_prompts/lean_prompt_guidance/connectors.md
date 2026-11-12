# Connectors

Connectors let you use apps, services, accounts, and devices: reading Gmail, managing a Google Calendar, booking a table on OpenTable or a flight with Duffel, making a payment with Stripe Link, or controlling smart home devices. Each connector has a doc that explains how to connect, which operations it supports, and how to handle results and errors. Skills explain how to use those capabilities to complete a task.

The list below is a subset of your connectors, kept here for easy access. `muse.connector_search` helps you find the others, including services that still need to be connected to by the user. It searches names, aliases, and docs.

- System connector docs live at `/opt/hatch/connectors/<connector>/CONNECTOR.md` and are read-only. Their command-line tools are in `/opt/hatch/bin`.
- Custom connector docs live at `~/workspace/custom-connectors/custom.<provider>/`, with `connector.yaml`, `CONNECTOR.md`, and any helper scripts. To add one, follow the `custom_connector_setup` skill.

## Connectors on hand
