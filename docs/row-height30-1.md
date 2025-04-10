## Row {height=30%}

### Column {.tabset}

```{python}
#| title: Chart 2
```

```{python}
#| title: Chart 3
```

### Column

```{python}
```
````

Each cell within the tabset column becomes a tab, and we provide navigational titles for our tabs by adding a `title` option to the cell used to produce each tab.

You can also have tabs that contain only markdown. To do this use a `::: {.card}` div and include a `title` attribute for the tab:

```markdown
::: {.card title="My Title"}
Card text
:::
```

In the examples above, each tab included a single card. If you want tabs to contain multiple cards, introduce another level of headings below the tabset row or column. For example:

````markdown
---
title: "Palmer Penguins"
format: dashboard
---

