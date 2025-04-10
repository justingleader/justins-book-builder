## Column {width=40%}

```{python}
```

::: {.card}
This text will be displayed within a card
:::

```{python}
```
````

To provide a title for a markdown card use the `title` attribute. For example:

```markdown
::: {.card title="My Title"}
This text will be displayed within a card
:::
```

Note that if you are authoring within a Jupyter Notebook then markdown cells automatically become `.card` divs.

For additional details on how cells and their content are mapped to cards (e.g. excluding cells, cells with multiple outputs, etc.), see [Cell Output](https://quarto.org/docs/dashboards/data-display.html#cell-output).

#### Display Options

By default, cards are displayed with no title and a small bit of padding around the edges. Here is a card that displays a [Leaflet](https://ipyleaflet.readthedocs.io/en/latest/) map:

![Card with Default Padding](https://quarto.org/docs/dashboards/images/card-default.png)

You can add a title to a card by including the `title` cell option. You can also customize the padding using the `padding` option. For example, here we add a title and remove the padding entirely:

````markdown
```{python}
#| title: "World Map"
#| padding: 0px

from ipyleaflet import Map, basemaps, basemap_to_tiles
Map(basemap=basemap_to_tiles(basemaps.OpenStreetMap.Mapnik),
    center=(48.204793, 350.121558), zoom=2)
```
````

You can create a dynamic `title` by printing a `title=` expression as a cell’s first output. For example:

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

#### Expanding Cards

By default, you can zoom in on the content of cards using the expand button in the bottom right:

![Card Expand Button](https://quarto.org/docs/dashboards/images/card-expand.png)

If you don’t want cards to be expandable you can specify `expandable: false` (either at the document level or for individual cards).

#### Card Fill Behavior

Quarto inspects card contents and generally choose a fill behavior that best matches the contents of the card (by default cards will fill their container, though in specific cases like simple markdown the card will choose a `flow` layout). You can explicit control the fill behavior of card using the `fill` attribute with the desired boolean value. For example `fill="false"` will cause the card’s height to match the size of the content (not filling).

### Learning More

*   [Data Display](https://quarto.org/docs/dashboards/data-display.html) shows you how to display data in your dashboard as plots, tables, value boxes, and text.
*   [Inputs](https://quarto.org/docs/dashboards/inputs.html) demonstrates various ways to layout inputs for interactive dashboards (sidebars, toolbars, attaching inputs directly to cards, etc.)
*   [Examples](https://quarto.org/docs/gallery/#dashboards) provides a gallery of example dashboards you can use as inspiration for your own.
*   [Theming](https://quarto.org/docs/dashboards/theming.html) describes the various way to customize the fonts, colors, layout and other aspects of dashboard appearance.
*   [Parameters](https://quarto.org/docs/dashboards/parameters.html) explains how to create dashboard variants by defining parameters and providing distinct values for them on the command line.
*   [Deployment](https://quarto.org/docs/dashboards/deployment.html) covers how to deploy both static dashboards (which require only a web host, but not a server) and Shiny dashboards (which require a Shiny Server).
*   [Interactivity](https://quarto.org/docs/dashboards/interactivity/) explores the various ways to create interactive dashboards that enable more flexible data exploration.

