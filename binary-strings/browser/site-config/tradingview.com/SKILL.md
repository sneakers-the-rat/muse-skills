# TradingView instructions

## Symbols and charts

- Search with “Search” (Ctrl+K) and check the symbol's exchange and instrument
  type; similar tickers can belong to different markets. Symbol pages sit at
  `/symbols/<EXCHANGE>-<SYMBOL>/`.
- Saved chart layouts open at `/chart/<layout>/`. Select the intended
  timeframe before reading the chart.
- Read exact numbers from visible values or data tables; a position on the
  chart is not an exact quote. “Market open · One update every 5 seconds”
  confirms the data is live.
- Chart controls can lack labels in the accessibility tree; read them from the
  screenshot `browser.observe` returns when they do. Observe again with `browser.observe` after opening a menu or
  changing a panel.

## Orders and alerts

- A watchlist, an alert, a paper trade and a live broker order have different
  effects. Saving a chart or symbol never places an order, and “All changes
  saved” refers only to the chart layout.

## Signing in

- Accounts created with Google have no TradingView password to fill; they sign
  in with Google.

## Bot detection

- TradingView occasionally shows a bot check. Treat any challenge page as a bot
  challenge.
