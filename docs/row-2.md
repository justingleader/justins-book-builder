## Row

```{python}
```
```

#### Dynamic Content

You can use [inline expressions](https://quarto.org/docs/computations/inline-code.html) to make text content dynamic. For example, here we have a row with text content that makes use of Python expressions:

````markdown
::: {.card}
The sample size was `{python} sample`. The mean reported
rating was `{python} rating`.
:::
````

### Cell Output

The output of each computational cell within your notebook or source document will be contained within a [Card](https://quarto.org/docs/dashboards/layout.html#cards). Below we describe some special rules observed when creating cards.

#### Dynamic Titles

You can create a dynamic `title` by printing a `title=` expression as a cell’s first output (in contrast to including the `title` as a YAML cell option). For example:

**Python:**
````markdown
```{python}
from ipyleaflet import Map, basemaps, basemap_to_tiles
lat = 48
long = 350
print("title=", f"World Map at {lat}, {long}")
Map(basemap=basemap_to_tiles(basemaps.OpenStreetMap.Mapnik),
    center=(lat, long), zoom=2)
```
````

**R:**
````markdown
```{r}
library(leaflet)
lat <- 48
long <- 350
cat("title=", "World Map at", lat, long)
leaflet() |>
  addTiles() |>
  setView(long, lat, zoom = 2)
```
````

#### Excluded Cells

Cells that produce no output do not become cards (for example, cells used to import packages, load and filter data, etc). If a cell produces unexpected output that you want to exclude add the `output: false` option to the cell:

````markdown
```{python}
#| output: false
# (code that produces unexpected output)
```
````

#### Expression Printing

By default, all output from top level expressions is displayed within dashboards. This means that multiple plots can easily be generated from a cell. For example:

````markdown
```{python}
#| title: "Tipping Behavior"
px.box(df, x="sex", y="total_bill", color="smoker")
px.violin(df, x="sex", y="total_bill", color="smoker")
```
````

This behavior corresponds to the `"all"` setting for [Jupyter shell interactivity](https://quarto.org/docs/reference/formats/ipynb.html#ipynb-shell-interactivity). You can customize this behavior within Quarto using the `ipynb-shell-interactivity` option.

#### Card Layout

If a cell produces multiple outputs you can use cell layout options to organize their display. For example, here we modify the example to display plots side-by-side using the `layout-ncol` option:

````markdown
```{python}
#| title: "Tipping Behavior"
#| layout-ncol: 2
px.box(df, x="sex", y="total_bill", color="smoker")
px.violin(df, x="sex", y="total_bill", color="smoker")
```
````

See the article on [Figures](https://quarto.org/docs/authoring/figures.html#figure-panels) for additional documentation on custom layouts.

### Learning More

*   [Layout](https://quarto.org/docs/dashboards/layout.html) shows you how to control the navigation bar, and how to arrange your content across pages, rows, columns, tabsets, and cards.
*   [Inputs](https://quarto.org/docs/dashboards/inputs.html) demonstrates various ways to layout inputs for interactive dashboards (sidebars, toolbars, attaching inputs directly to cards, etc.)
*   [Examples](https://quarto.org/docs/gallery/#dashboards) provides a gallery of example dashboards you can use as inspiration for your own.
*   [Theming](https://quarto.org/docs/dashboards/theming.html) describes the various way to customize the fonts, colors, layout and other aspects of dashboard appearance.
*   [Parameters](https://quarto.org/docs/dashboards/parameters.html) explains how to create dashboard variants by defining parameters and providing distinct values for them on the command line.
*   [Deployment](https://quarto.org/docs/dashboards/deployment.html) covers how to deploy both static dashboards (which require only a web host, but not a server) and Shiny dashboards (which require a Shiny Server).
*   [Interactivity](https://quarto.org/docs/dashboards/interactivity/) explores the various ways to create interactive dashboards that enable more flexible data exploration.

