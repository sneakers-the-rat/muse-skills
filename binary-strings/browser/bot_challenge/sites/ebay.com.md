## Bot detection

- eBay checks automated browsing often. Its check is titled “Pardon Our
  Interruption...” and reads “Checking your browser before you access eBay.”
  and “Your browser will redirect to your requested content shortly.” It is
  meant to clear on its own; wait for the redirect instead of reloading.
- A search can also return eBay's error page, “SORRY” and “Something went
  wrong on our end”. It is not an empty result set.
- When a check does not clear, treat it as a bot challenge.
