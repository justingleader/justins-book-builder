## Interactive: OJS Examples Layout

Source: [Layout – Quarto](https://quarto.org/docs/interactive/ojs/examples/layout.html)

You can control the layout of OJS content in a number of ways.

### `page-layout: full`

This example uses `page-layout: full` to have its contents occupy the entire width of the page:

```yaml
---
title: "Layout"
format:
  html:
    page-layout: full
---
```

Enclose the inputs in a sidebar panel and the outputs in a tabset panel (click the “Code” button at top right to see the full source code):

````markdown
::: {.panel-sidebar}

```{ojs}
viewof bill_length_min = Inputs.range(
  [32, 50],
  {value: 35, step: 1, label: "Bill length (min):"}
)

viewof islands = Inputs.checkbox(
  ["Torgersen", "Biscoe", "Dream"],
  { value: ["Torgersen", "Biscoe"], label: "Islands:" }
)
```

:::

::: {.panel-tabset #penguins-tabset}

