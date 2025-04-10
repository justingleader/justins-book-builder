## Interactive Widgets: htmlwidgets for R

Source: [htmlwidgets for R – Quarto](https://quarto.org/docs/interactive/widgets/htmlwidgets.html)

### Overview

The [htmlwidgets](https://www.htmlwidgets.org/) package enables you to use JavaScript visualization libraries like [Leaflet](https://rstudio.github.io/leaflet/), [Plotly](https://plotly.com/r/), [dygraphs](https://rstudio.github.io/dygraphs/), and [threejs](https://github.com/bwlewis/rthreejs) directly from R.

If you are using the Knitr engine with Quarto this is a great way to incorporate interactivity without learning JavaScript or requiring a Shiny Server to view your document.

### Usage

Including htmlwidgets within a Quarto document is as easy as including an R plot. For example, here is how we embed a [Leaflet](https://rstudio.github.io/leaflet/) map:

````markdown
```{r}
library(leaflet)
leaflet() %>%
  addTiles() %>%  # Add default OpenStreetMap map tiles
  addMarkers(lng=174.768, lat=-36.852,
             popup="The birthplace of R")
```
````

### Layout

You can also use [layout](https://quarto.org/docs/authoring/figures.html#figure-panels) options with htmlwidgets. For example, here we provide a custom `layout` to arrange three [dygraph](https://rstudio.github.io/dygraphs/) time series plots:

````markdown
```{r}
#| layout: [[1,1], [1]]

library(dygraphs)
dygraph(fdeaths, "Female Deaths")
dygraph(mdeaths, "Male Deaths")
dygraph(ldeaths, "All Deaths")
```
````

See the article on [Figures](https://quarto.org/docs/authoring/figures.html#figure-panels) for additional documentation on custom layouts.

To learn about available htmlwidgets see the [showcase page](https://gallery.htmlwidgets.org/) and the [htmlwidget gallery](https://gallery.htmlwidgets.org/index.html).

