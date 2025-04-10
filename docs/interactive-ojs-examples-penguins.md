## Interactive: OJS Examples Penguins

Source: [Penguins – Quarto](https://quarto.org/docs/interactive/ojs/examples/penguins.html)

A simple example based on Allison Horst’s [Palmer Penguins](https://allisonhorst.github.io/palmerpenguins/) dataset. Here we look at how penguin body mass varies across both sex and species (use the provided inputs to filter the dataset by bill length and island):

````markdown
::: {.panel-input}
```{ojs}
//| layout-ncol: 2
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

::: {.panel-tabset}

