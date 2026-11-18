- Device-target wiring: the host picks the device in the URL fragment. If it's missing, add this script at the top of `<head>`, exactly as written:

  ```html
  <script id="hatch-space-target">
    (() => {
      const params = new URLSearchParams(location.hash.slice(1));
      const root = document.documentElement;
      if (params.get("hatch_target") === "tv") root.dataset.hatchTarget = "tv";
      const widget = params.get("hatch_view") === "widget";
      root.dataset.hatchView = widget ? "widget" : "app";
      if (widget) {
        root.dataset.hatchWidget = params.get("hatch_widget") || "default";
        root.dataset.hatchInstance = params.get("hatch_instance") || "";
        const sizes = ["small", "medium", "large", "watch", "watch_round"];
        root.dataset.hatchSize = sizes.includes(params.get("hatch_size")) ? params.get("hatch_size") : "small";
        const style = document.createElement("style");
        style.textContent = 'html[data-hatch-view="widget"], html[data-hatch-view="widget"] body { background: transparent; }';
        document.head.prepend(style);
      }
    })();
  </script>
  ```

  It sets `data-hatch-target`, `data-hatch-view`, `data-hatch-widget`, `data-hatch-instance`, and `data-hatch-size` on `<html>`, and makes a widget's page transparent by default; a later rule with the same selector overrides it. Style targets with selectors such as `html[data-hatch-target="tv"]` and `html[data-hatch-view="widget"]`; the phone and desktop page stays as it is. A widget is its own `<section>`, shown instead of the app, and declaring `widgets` is the one other `space.json` edit allowed.
