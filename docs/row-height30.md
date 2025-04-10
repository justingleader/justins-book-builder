## Row {height=30%}

```{python}
```

```{python}
```
````

Here, level 2 markdown headings (e.g. `## Row {height=70%}`) define the contents of rows as well as their relative height. The `````{python}````` code cells in turn automatically create cards that are laid out in columns within the row.

**Heading text isn’t required:** Although markdown headings are used to define the layout of rows and columns in Quarto dashboards, the heading text itself is discarded. We use the headings `Row` and `Column` in these docs to aid understanding of the layouts, but you can use more descriptive headings if they help you navigate your source code.

### Orientation

By default, dashboard pages are laid out first by row, then by column. However, you can change this by specifying the `orientation: columns` document option:

````markdown
---
title: "Diamonds Explorer"
format:
  dashboard:
    orientation: columns
---

