## Row {.flow}
```

### Scrolling

By default, dashboard content fills all available space in the page. You can alternatively specify the `scrolling: true` option to layout content using its natural height and scroll to accommodate page overflow. For example:

````markdown
---
title: "Scrolling"
format:
  dashboard:
    scrolling: true
---

```{python}
```

```{python}
```

```{python}
```
````

Because of its ability to scroll this layout could easily accommodate many more charts. While this is useful, you might also consider [Pages](#pages) and [Tabsets](#tabsets) (described in the next two sections) as alternate ways to present content within layouts that fill their page.

### Pages

The layout examples above demonstrated only single-page dashboards. To introduce multiple pages, use level 1 headings above the level 2 headings used to define rows and columns. The text of the level 1 headings will be used to link to the pages in the navigation bar. For example, here is a dashboard that splits content across two pages:

````markdown
---
title: "Palmer Penguins"
format: dashboard
---

# Bills

```{python}
```

# Flippers {orientation="columns" scrolling="true"}

