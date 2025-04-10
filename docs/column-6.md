## Column

```{python}
```
````

Note that we can set a per-page orientation by adding an `orientation` attribute to the page heading (here `orientation="columns"` for the second page). In addition, you can control per-page scrolling behavior using a `scrolling` attribute on the page heading (shown using `scrolling="true"` for the second page above).

### Tabsets

Use tabsets to include multiple views of data or to include content of secondary importance without having it crowd the main display. Tabsets are created by adding the `.tabset` class to a row or column. For example, this layout displays the bottom row as a set of two tabs.

````markdown
---
title: "Palmer Penguins"
format: dashboard
---

