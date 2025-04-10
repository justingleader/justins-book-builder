## Interactive: OJS Cells

Source: [OJS Cells – Quarto](https://quarto.org/docs/interactive/ojs/ojs-cells.html)

OJS code cells `{ojs}` behave a bit differently than cells in traditional notebooks, and have many options available to control their display and layout.

### Cell Execution

A critical difference between OJS cell execution and traditional notebooks is that in OJS cells do not need to be defined in any particular order.

Because execution is fully reactive, the runtime will automatically execute cells in the correct order based on how they reference each other. This is more akin to a spreadsheet than a traditional notebook with linear cell execution.

For example, in this cell we reference a variable that is not yet defined (it’s defined immediately below):

````markdown
```{ojs}
x + 5
```
````

````markdown
```{ojs}
x = 10
```
````

This code works because the Observable runtime automatically determines the correct order of execution for the cells.

### Cell Output

By default, OJS cells show their full source code and output within rendered documents. Depending on the type of document you are creating you might want to change this behavior either globally or for individual cells.

#### Code Visibility

The `echo` option controls whether cells display their source code. To prevent display of code for an entire document, set the `echo: false` option in YAML metadata:

```yaml
---
title: "My Document"
execute:
  echo: false
---
```

You can also specify this option on a per-cell basis. For example:

````markdown
```{ojs}
//| echo: false
data = FileAttachment("palmer-penguins.csv").csv({ typed: true })
```
````

#### Output Visibility

OJS cell output is also displayed by default. You can change this at a global or (more likely) per-cell level using the `output` option. For example, here we disable output for a cell:

````markdown
```{ojs}
//| output: false
data
```
````

Note that cells which only carry assignments do not print their output by default. For example, this assignment won’t print anything:

````markdown
```{ojs}
//| echo: fenced
dummy1 = "aHiddenAssignment"
```
````

If you want to print even the results of assignments, you can specify the `output: all` option. For example:

````markdown
```{ojs}
//| echo: fenced
//| output: all
dummy2 = [{key: 1, value: [1, 2, [3, 4], dummy1]}]
```
````

If you click the inspector you’ll see it expand to reveal the data as JSON.

#### Code Display

We talked about showing and hiding source code above, but what about controlling exactly how it’s displayed?

There are options available for customizing the appearance of code blocks (highlighting, background, border, etc.) as well as how horizontal overflow is handled. See the article on [HTML Code Blocks](https://quarto.org/docs/output-formats/html-code.html) for all of the details.

One option we wanted to specifically highlight here is code folding, which enables you to collapse code but still provide an option for users to view it. This is especially handy for custom JavaScript visualizations as they often span dozens of lines of code.

Add the `code-fold: true` option to a code cell to enable code folding (you can also enable this globally). For example, click the “Code” button to show the code block (note the `code-fold: true` option is specified)

````markdown
```{ojs}
//| code-fold: true

pdata = FileAttachment("palmer-penguins.csv").csv({typed: true})

Plot.plot({
  facet: {
    data: pdata,
    x: "sex",
    y: "species",
    marginRight: 80
  },
  marks: [
    Plot.frame(),
    Plot.rectY(pdata,
      Plot.binX({y: "count"}, {x: "body_mass_g", thresholds: 20, fill: "species"})
    ),
    Plot.tickX(pdata,
      Plot.groupZ({x: "median"}, {x: "body_mass_g",
         z: d => d.sex + d.species,
         stroke: "#333",
         strokeWidth: 2 })
    )
  ]
})
```
````

### Cell Layout

There are additional `panel` and `layout` options which you can add to OJS cells to customize how their output is presented. Here’s a version of some of the previous examples we’ve used presented with a sidebar and tabset:

![OJS with Sidebar and Tabset Layout](https://quarto.org/docs/interactive/ojs/images/layout-example.png)

We created this layout by first adding the `panel: sidebar` option to the cell with our inputs:

````markdown
```{ojs}
//| panel: sidebar

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

We then added a tabset (div of class `.panel-tabset`) with `Plot` and `Data` tabs (headings within the div define the tabs):

````markdown
::: {.panel-tabset}

