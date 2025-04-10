## Interactive Widgets: Jupyter Widgets

Source: [Jupyter Widgets – Quarto](https://quarto.org/docs/interactive/widgets/jupyter.html)

### Overview

[Jupyter Widgets](https://ipywidgets.readthedocs.io/en/stable/) enable you to use JavaScript visualization libraries like [Leaflet](https://ipyleaflet.readthedocs.io/en/latest/), [Plotly](https://plotly.com/python/getting-started/), and [threejs](https://github.com/jupyter-widgets/pythreejs) directly from Python.

If you are using the Jupyter engine with Quarto this is a great way to incorporate interactivity without learning JavaScript.

Note that while Quarto uses a Jupyter kernel during rendering, there is no Jupyter kernel once the site is published, so there is interactivity with JavaScript but not with Python.

### Leaflet Example

Including Jupyter Widgets within a Quarto document is as easy as including a plot. For example, here is how we embed a [Leaflet](https://ipyleaflet.readthedocs.io/en/latest/) map:

````markdown
```{python}
from ipyleaflet import Map, Marker, basemaps, basemap_to_tiles

m = Map(
  basemap=basemap_to_tiles(
    basemaps.NASAGIBS.ModisTerraTrueColorCR, "2017-04-08"
  ),
  center=(52.204793, 360.121558),
  zoom=4
)

m.add_layer(Marker(location=(52.204793, 360.121558)))

m
```
````

To learn about available Jupyter Widgets visit <https://jupyter.org/widgets>.

### Plotly

Plotly is an interactive graphics library that can also be used with the Jupyter engine. Here’s an example of using [Plotly](https://plotly.com/python/getting-started/):

````markdown
```{python}
import plotly.express as px
import plotly.io as pio

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length",
                 color="species",
                 marginal_y="violin", marginal_x="box",
                 trendline="ols", template="simple_white")
fig.show()
```
````

**Note:** If you are using Plotly within the VS Code Notebook Editor you will need to add a line of code to ensure that your plots can be seen both within VS Code and when rendered to HTML by Quarto. You can do this by configuring the Plotly [default renderer](https://plotly.com/python/renderers/) as follows:

````markdown
```{python}
import plotly.io as pio
pio.renderers.default = "plotly_mimetype+notebook_connected"
```
````

This workaround is required because when running within VS Code, Plotly chooses a default rendering that can’t be easily exported to HTML (for more background, see this [GitHub Issue](https://github.com/microsoft/vscode-jupyter/issues/8135) and related discussion). Note that this workaround is only required for the VS Code Notebook Editor (it is not required if you are using Jupyter Lab or if you are editing a plain-text `.qmd` file).

