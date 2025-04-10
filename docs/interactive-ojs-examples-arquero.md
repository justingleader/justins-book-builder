## Interactive: OJS Examples Arquero

Source: [Arquero – Quarto](https://quarto.org/docs/interactive/ojs/examples/arquero.html)

Simple demonstration of [Arquero](https://github.com/uwdata/arquero) using Allison Horst’s [Palmer Penguins](https://allisonhorst.github.io/palmerpenguins/) dataset.

````markdown
```{ojs}
import { aq, op } from '@uwdata/arquero'

penguins = aq.loadCSV("palmer-penguins.csv")

penguins.view()
```
````

````markdown
```{ojs}
penguins
  .groupby('species')
  .filter(d => d.body_mass_g > 0)
  .rollup({
     count: op.count(),
     avg_mass: op.average('body_mass_g')
   })
  .view()
```
````

If you want to use inputs in an arquero query, you can use the `params` method of table. Below is a simple example of filtering a dataset by the values provided.

````markdown
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
````

````markdown
```{ojs}
penguins
  .params({ blm: bill_length_min, i: islands })
  .filter((d, $) => op.includes($.i, d.island) && d.bill_length_mm > $.blm)
  .view()
```
````

