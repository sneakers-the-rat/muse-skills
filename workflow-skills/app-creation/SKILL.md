# App Creation

## Decide what to build

- Find out who will use the app, what they need to do with it and what a good result looks like. Start with the smallest version that completes that job end to end.

- Look for an existing app, page or project before building a new one. Extend what the user already has unless it cannot meet the need.

- Choose where the app lives from who will use it and whether it saves data:
  - A Muse page (`artifact.create_web_static`) can be shared as a public link, but every visitor runs it alone and nothing they enter is saved.
  - A Muse app (`artifact.create_web_fullstack`) saves data and can refresh live data, but it runs privately for the user and has no public link.
  - A hosted builder such as Lovable, Replit, Zite or Vercel fits an app that other people must use and that saves what they enter, or one that needs a custom domain, a team or an existing codebase.

- When the request needs both a public link and saved entries, explain the tradeoff and let the user choose before building anything.

## Build it

- For a Muse artifact, pass the user's exact request and follow `~/docs/artifacts.md`. Change an existing artifact with `artifact.edit`. A page that must start saving data, or an app that must be shared, needs a new artifact of the other kind, and saved data does not carry over.

- For a hosted builder, follow its connector docs and keep the project, app or deployment IDs it returns. Make changes in the user's existing project rather than creating a parallel one.

- When implementing a supplied design, inspect the project's components, tokens and assets first. Read the design's structure alongside a screenshot, then translate it into the project's framework and responsive layout system.

- Keep content that comes from data or props dynamic. Use the original assets in their intended positions rather than redrawing them, and never use a screenshot as the implementation.

- Keep implementation details out of the app's own copy unless they help its user decide something.

## Check that it works

- Test the main flow the way its user will, then the empty, loading and error states, the relevant screen sizes and basic accessibility.

- A successful build does not prove the app works. Confirm the result from the running app or the live deployment.

- For a hosted app, check the deployment status and run the main flow on the returned URL with `browser.browse` before reporting it live. After an interrupted deployment, check the existing job before starting another.

- When the user reports that a Muse artifact misbehaves or asks how it behaves, use `artifact.inspect` rather than reading its source yourself.

## Deliver it

- Hand over a Muse artifact through its card. `artifact.status` with the slug returns the `card.widget_id` to pass to `widget.present`.

- Publish a page with `artifact.share` only when the user asks for a public link, and give them the exact URL it returns.

- Tell the user which kind they have, such as a private Muse app, a public page or a hosted deployment, and whether it is a preview or the published version.

- List anything the user still needs to do, such as connecting an account, adding a domain or approving a publish.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for code, issues and pull requests in a repository the app lives in.

- [Figma](/opt/hatch/connectors/figma/CONNECTOR.md) for design context, tokens and assets to implement a supplied design.

- [Replit](/opt/hatch/connectors/replit/CONNECTOR.md) for creating, updating and publishing a hosted app from a description.

- [Lovable](/opt/hatch/connectors/lovable/CONNECTOR.md) for building, editing and deploying a hosted app and reading its code.

- [Vercel](/opt/hatch/connectors/vercel/CONNECTOR.md) for deployments, build and runtime logs, domains and project settings.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Zite](/opt/hatch/connectors/zite_mcp/CONNECTOR.md) for building and publishing an app with its own database.

- [Wix](/opt/hatch/connectors/wix_mcp/CONNECTOR.md) for changing or publishing an existing Wix site.

## Websites

- Use `browser.browse` for a builder the user already works in that has no connector here, such as [Webflow](https://webflow.com/), [Framer](https://www.framer.com/), [Squarespace](https://www.squarespace.com/) or [Bubble](https://bubble.io/). Give the task the project name and the exact change, and have it confirm that the change saved or published.

- Use a connected builder's website only for what its connector lacks. Connecting a custom domain in Lovable or Replit is one example, since neither connector has a domain operation.

- [Airtable](https://airtable.com/) and [Glide](https://www.glideapps.com/) can turn the user's existing table or spreadsheet into a simple app for a team.

## Alternatives for better results

- Ask one question when the audience is unclear. Whether the app is only for the user or open to others decides which kind to build.

- Prototype privately as a Muse app, then move to a hosted builder once the user wants other people to use it.

- A form, a shared spreadsheet or a tracker can meet a simple collection need with less to maintain than an app.

- Improve the app from real use. Ship the core flow, watch where the user gets stuck, then add features.
