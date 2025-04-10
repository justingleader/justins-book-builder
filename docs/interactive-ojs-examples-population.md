## Interactive: OJS Examples Population

Source: [Population – Quarto](https://quarto.org/docs/interactive/ojs/examples/population.html)

This example demonstrates importing a notebook from ObervableHQ and replacing its data with data of our own (the code and data for this example were originally published [here](https://observablehq.com/@observablehq/inputs-table#cell-172)).

First we read from a local JSON file into `population`:

````markdown
```{ojs}
//| echo: false
//| output: none
population = FileAttachment("population.json").json()
```
````

Then we import from <https://observablehq.com/@d3/zoomable-sunburst> and specify that we’d like to use `population` instead of the data built in to the notebook:

````markdown
```{ojs}
//| echo: fenced
import { chart } with { population as data } from "@d3/zoomable-sunburst"
```
````

Finally, we display the chart:

````markdown
```{ojs}
//| echo: fenced
chart
```
````

