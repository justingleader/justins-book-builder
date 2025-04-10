## Data

```{ojs}
Inputs.table(filtered)
```

:::
````

### Full Page Layout

By default Quarto documents center their content within the document viewport, and don’t exceed a maximum width of around 900 pixels. This behavior exists to optimize readability, but for an application layout you generally want to occupy the entire page.

To do this, add the `page-layout: custom` option. For example:

```yaml
format:
  html:
    page-layout: custom
```

Here’s an example of a Shiny application that occupies the full width of the browser:

![Full Page Layout Example](https://quarto.org/docs/interactive/images/full-page-layout.png)

You’ll also note that the inputs are contained within a sidebar—the next section describes how to create sidebars.

### Sidebar Panel

Sidebars are created using divs with class `.panel-sidebar`. You can do this using a markdown div container (as illustrated above for `.panel-input`), or, if the entire contents of your sidebar is created from a single code cell, by adding the `panel: sidebar` option to the cell.

Sidebar panels should always have an adjacent panel with class `.panel-fill` or `.panel-center` which they will be laid out next to. The former (`.panel-fill`) will fill all available space, the latter (`.panel-center`) will leave some horizontal margin around its content.

For example, here is the source code of the user-interface portion of the Shiny application displayed above:

````markdown
---
title: "Iris K-Means Clustering"
format:
  html:
    page-layout: custom
server: shiny
---

```{r}
#| panel: sidebar

vars <- setdiff(names(iris), "Species")
selectInput('xcol', 'X Variable', vars)
selectInput('ycol', 'Y Variable', vars, selected = vars[[2]])
numericInput('clusters', 'Cluster count', 3, min = 1, max = 9)
```

```{r}
#| panel: fill

plotOutput('plot1')
```
````

The `panel: fill` option is added to the plot output chunk. You can alternately use `panel: center` if you want to leave some horizontal margin around the contents of the panel.

Adding the `panel` option to a code chunk is shorthand for adding the CSS class to its containing div (i.e. it’s equivalent to surrounding the code chunk with a div with class e.g. `panel-fill`).

Here’s an example of using a sidebar with OJS inputs:

![Sidebar with OJS Inputs](https://quarto.org/docs/interactive/images/ojs-sidebar.png)

To do this you would use the following code:

````markdown
```{ojs}
//| panel: sidebar

viewof myage = {
  const myage = select({
    title: "Quelle classe d'âge voulez-vous cartographier ?",
    options: ages,
    value: "80etplus"
  });
  return myage;
}

viewof pctvax = slider({
  title: '<br/>Objectif de vaccination',
  description: '200% signifie 2 doses par personnes pour tout le monde',
  min: 50, max: 200, value: 200, step: 10, format: v => v + "%"
})

viewof overlay = radio({
  title: "Écarter les cercles",
  options: [{ label: 'Oui', value: 'Y' }, { label: 'Non', value: 'N' }],
  value: 'N'
})

viewof label = radio({
  title: "Numéros des départements",
  options: [{ label: 'Afficher', value: 'Y' }, { label: 'Masquer', value: 'N' }],
  value: 'N'
})
```

```{ojs}
//| panel: fill
(vaccine visualization code)
```
````

### Panel Layout

You can arrange multiple interactive components into a panel using the `layout` attribute of a containing div. For example, here we have a main visualization in the first row and two ancillary visualizations in the second row:

![Panel Layout Example](https://quarto.org/docs/interactive/images/panel-layout.png)

As described in the article on [Figures](https://quarto.org/docs/authoring/figures.html#custom-layouts), you can arrange panels of figures in very flexible fashion using the `layout` attribute. For the example above we enclosed the three visualizations in the following div:

```markdown
::: {layout="[ [1], [1,1] ]"}
(outputs)
:::
```

Note that you can apply the `layout` attribute to a div that is already a panel (e.g. `.panel-fill`) to specify layout for content adjacent to a sidebar. So the following markup is also valid:

```markdown
::: {.panel-sidebar}
(inputs)
:::

::: {.panel-fill layout="[ [1], [1,1] ]"}
(outputs)
:::
```

The `layout` attribute is an array of arrays, each of which defines a row of the layout. Above we indicate that we want the first row to encompass the first visualization, and then to split the next two equally over the second row.

The values in rows don’t need to add up to anything in particular (they are relative within each row), so we could have just as well have specified different relative widths for the second row if that was better suited to presenting our data:

```markdown
::: {layout="[ [1], [3,2] ]"}
(outputs)
:::
```

