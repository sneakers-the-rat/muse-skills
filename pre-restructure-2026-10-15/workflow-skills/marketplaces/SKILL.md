# Marketplaces

## Value the item and choose a market

- Establish whether the user wants to buy, sell or value an item, and keep its exact model, condition, included parts, location, budget and whether it will be shipped or collected.

- Value an item from recent sold listings, not asking prices, and compare it with the new price and refurbished offers. Use [Shopping](/opt/muse/skills/shopping/SKILL.md) when a new item or a retailer offer might suit the user better.

- Choose the market where the item will change hands. Local marketplaces suit bulky items and cash-on-collection, while a marketplace with checkout and buyer protection suits small or valuable items that ship.

- Use [Event Tickets](/opt/muse/skills/event-tickets/SKILL.md) for tickets, because transfer rules and admission guarantees differ from ordinary goods.

## Buy safely

- Check that the photos, title and description agree, read the seller's history and ratings, and ask about anything missing before committing. A price far below similar listings is a warning sign.

- Inspect the item before paying. Test electronics, check that a phone is not locked or reported lost, and for a vehicle check its history report and paperwork.

- Pay through the marketplace's checkout or another method with buyer protection where one is offered. Avoid wire transfers, gift cards, crypto and instant bank transfers to strangers, and never send a deposit to hold an item nobody has seen.

- Stop and check the facts when someone asks to move off the platform, to pay a different person or to accept a changed description.

- Never share a verification code that a buyer or seller sends or asks for, because it can hand over the user's account.

## Sell safely

- Use the user's own photos and describe the condition, defects and included parts accurately. Keep the home address out of a public listing and give a general area instead.

- Price from sold listings and show the platform's fees and the likely net proceeds before proposing a price.

- Hand the item over only after payment has cleared. Treat overpayments, refund requests, payment screenshots and emails claiming a payment as signs of a scam, and ship only with tracking to the address in the platform's order.

- Keep a draft separate from a published listing and an enquiry separate from a binding offer. Some listing commands publish as soon as every field is present, so read the connector's behavior and obtain the required approval.

## Meet and complete the handover

- Suggest a busy, well-lit public place in daylight, such as a police station's safe-exchange spot, and let the user bring someone along. Keep to the times and places the user approves.

- Get the user's approval for each message that commits them to a price, a hold, a meetup or a payment arrangement. Use [Messaging Other People](/opt/muse/skills/messaging/SKILL.md) for the conversation itself.

- Do not report payment, dispatch or collection until the marketplace or payment record confirms it. After an uncertain offer, payment or publication, check its status before trying again.

## Available connectors

- [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) for Marketplace search, listing details, seller ratings and the user's own listings.

- [Messenger](/opt/hatch/connectors/messenger_read/CONNECTOR.md) for contacting a Marketplace seller and continuing that conversation.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- Search and transact on these sites with `browser.spawn_task`, giving the exact item, condition, price range and the city or postcode where it will change hands. Have the task return each listing's price, condition, location, seller rating and payment or shipping terms.

- [eBay](https://www.ebay.com/) for new and used goods that ship, sold-listing prices and its Money Back Guarantee.

- [Craigslist](https://www.craigslist.org/) for local listings in North American cities, without built-in payment protection, and [Kijiji](https://www.kijiji.ca/) in Canada.

- [Gumtree](https://www.gumtree.com/) in the UK and [Gumtree Australia](https://www.gumtree.com.au/) for local listings.

- [Leboncoin](https://www.leboncoin.fr/) in France, [Kleinanzeigen](https://www.kleinanzeigen.de/) in Germany, [Mercari Japan](https://jp.mercari.com/) in Japan and [Mercado Libre](https://www.mercadolibre.com.mx/) in Mexico and Latin America. Check each site's account, payment and delivery requirements rather than assuming cross-border access.

## Alternatives for better results

- Compare a specialist resale site, a trade-in offer or a local dealer when authentication, warranty or convenience matter more than the last bit of price.

- Watch for a better listing when the user can wait, instead of settling for a weak match.
