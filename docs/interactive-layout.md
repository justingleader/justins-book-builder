## Interactive: Layout

Source: [Component Layout – Quarto](https://quarto.org/docs/interactive/layout.html)

### Overview

When you introduce interactive components into a document you’ll want to be sure to lay them out in a fashion that optimizes for readability and navigation.

There are of course a wide variety of ways you can incorporate interactivity spanning from visualizations embedded within a longer-form article all the way up to a more application/dashboard style layout. We’ll cover both of these layout scenarios below.

We’ll use examples from both [Observable JS](https://quarto.org/docs/interactive/ojs/) and [Shiny](https://quarto.org/docs/interactive/shiny/) interactive documents—if you aren’t familiar with the code/syntax used for a given example just focus on the enclosing layout markup rather than the application code.

### Input Panel

If you have several inputs, you may want to group them inside an input panel (code block with option `panel: input` or div with class `.panel-input`). For example:

![Input Panel Example](https://quarto.org/docs/interactive/images/input-panel.png)

The inputs are grouped in a panel and laid out in three columns by adding the `panel: input` and `layout-ncol: 3` options to the OJS code cell:

````markdown
```{ojs}
//| panel: input
//| layout-ncol: 3

viewof ch = checkbox({
  title: "Passport color:",
  options: [
    { value: "red", label: "Red" },
    { value: "green", label: "Green" },
    { value: "blue", label: "Blue" },
    { value: "black", label: "Black" }
  ],
  value: ["red", "green", "blue", "black"],
  submit: false
})

viewof type = radio({
  title: "Representation:",
  options: [
    { label: 'Passports', value: 'p' },
    { label: 'Circles', value: 'c' }
  ],
  value: 'p'
})

viewof k = slider({
  title: "Symbol size:",
  min: 1, max: 10, value: 3, step: 1
})
```
````

### Tabset Panel

If you want to allow users to toggle between multiple visualizations, use a tabset (div with class `.panel-tabset`). Include a heading (e.g. `##`) for each tab in the tabset.

For example, here are a plot and data each presented in their own tab:

![Tabset Panel Example](https://quarto.org/docs/interactive/images/tabset-panel.png)

Here is the markdown and code used to create the tabset:

````markdown
::: {.panel-tabset}

