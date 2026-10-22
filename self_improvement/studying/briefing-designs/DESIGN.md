# Muse Letter design

Muse Letters are warm pages for personal correspondence. The design is a
container for the assistant's voice, not an editorial template.

`NOTEBOOK_BRIEF.css` is the canonical stylesheet. Link it once in authored HTML;
the finalizer inlines it when the brief is accepted.

## Core shell

Every letter needs only this shared shell:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{Brief title}}</title>
  <link rel="stylesheet" href="NOTEBOOK_BRIEF.css">
</head>
<body>
  <main class="sheet">
    <article class="article">
      <p>Write the note in the shape that feels natural here.</p>
      <p class="byline">&mdash;<span>{{assistant_name}}</span></p>
    </article>
  </main>
</body>
</html>
```

Resolve the assistant name from `