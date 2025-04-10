## Dashboards: Interactivity with Observable JS

Source: [Dashboards with Observable JS – Quarto](https://quarto.org/docs/dashboards/interactivity/observable.html)

### Introduction

Quarto includes native support for [Observable JS](https://observablehq.com/@observablehq/observables-not-javascript), a set of enhancements to vanilla JavaScript created by [Mike Bostock](https://bost.ocks.org/mike/) (also the author of [D3](https://d3js.org/)). Observable JS is distinguished by its [reactive runtime](https://observablehq.com/@observablehq/how-observable-runs), which is especially well suited for interactive data exploration and analysis.

The creators of Observable JS (Observable, Inc.) run a hosted service at <https://observablehq.com/> where you can create and publish notebooks. Additionally, you can use Observable JS (“OJS”) in standalone documents and websites via its [core libraries](https://github.com/observablehq/runtime). Quarto uses these libraries along with a [compiler](https://github.com/observablehq/ojs-compiler) that is run at render time to enable the use of OJS within Quarto documents.

### Walkthrough

Quarto Dashboards are a great way to present interactive OJS visualizations. Below we’ll provide a complete example which will give you a high level view of the basics. If you want to learn more, please see the complete documentation on [Using OJS with Quarto](https://quarto.org/docs/interactive/ojs/).

This example covers many of the techniques you’ll use when creating dashboards with OJS, including reactive calculations and more advanced layout constructs like sidebars and tabsets. Here is the interactive document we’ll be building:

![OJS Dashboard Example](https://quarto.org/docs/dashboards/interactivity/images/observable-dashboard.png)

The source code for this dashboard is below. Note that we add the `//| output: false` option to the first cell: this is to designate the cell as having only intermediate computations (so it should not be turned into a card in the dashboard layout).

Click on the numbers on the far right for additional explanation of syntax and mechanics)

````markdown
---
title: "Palmer Penguins"
author: "Cobblepot Analytics"
format: dashboard
---

```{ojs}
//| output: false

data = FileAttachment("penguins.csv")
  .csv({ typed: true })

filtered = data.filter(function(penguin) {
  return bill_length_min < penguin.bill_length_mm &&
         islands.includes(penguin.island);
})
```

# {.sidebar}

![](images/penguins.png){width="80%"}

```{ojs}
viewof bill_length_min = Inputs.range(
  [32, 50],
  {value: 35, step: 1, label: "Bill length (min):"}
)

viewof islands = Inputs.checkbox(
  ["Torgersen", "Biscoe", "Dream"],
  { value: ["Torgersen", "Biscoe", "Dream"],
    label: "Islands:" }
)
```

# Plot

```{ojs}
Plot.rectY(filtered,
  Plot.binX(
    {y: "count"},
    {x: "body_mass_g", fill: "species", thresholds: 20}
  ))
  .plot({
    facet: {
      data: filtered,
      x: "sex",
      y: "species",
      marginRight: 80
    },
    marks: [
      Plot.frame(),
    ]
  }
)
```

# Data

```{ojs}
Inputs.table(filtered)
```
````

1.  We set `output: false` to indicate that this cell includes only intermediate calculations and should not have its contents printed.
2.  We read the raw penguins dataset from a CSV when the page loads.
3.  `filtered` is a value that is automatically recomputed when variables declared with `viewof` change (in this case `bill_length_min` and `islands`).
4.  Create global sidebars by adding the `.sidebar` class to a level 1 heading. Sidebars can include code cells as well as images, narrative, and links.
5.  Here we define our inputs using `viewof` so that the `filtered` dataset is automatically recomputed when they change.
6.  Level 1 headings (here `# Plots` and `# Data`) create pages within the dashboard.
7.  The plot is automatically redrawn whenever the `filtered` dataset changes.
8.  The tabular data display is automatically refreshed whenever the `filtered` dataset changes.

### Learning More

To learn more about using OJS with Quarto, see the following articles:

*   [Input](https://quarto.org/docs/dashboards/inputs.html) describes various ways to layout inputs (sidebars, input panels, attaching inputs directly to cards, etc.).
*   [Using OJS](https://quarto.org/docs/interactive/ojs/) provides an introduction and overview of other topics.
*   [OJS Libraries](https://quarto.org/docs/interactive/ojs/libraries.html) covers using standard libraries and external JavaScript libraries.
*   [OJS Data Sources](https://quarto.org/docs/interactive/ojs/data-sources.html) outlines the various ways to read and pre-process data.
*   [OJS Cells](https://quarto.org/docs/interactive/ojs/ojs-cells.html) goes into more depth on cell execution, output, and layout.
*   [OJS Code Reuse](https://quarto.org/docs/interactive/ojs/code-reuse.html) delves into ways to re-use OJS code across multiple documents.

