## Dashboards

Source: [Quarto Dashboards – Quarto](https://quarto.org/docs/dashboards/index.html)

### Overview

Quarto Dashboards make it easy to create interactive dashboards using Python, R, Julia, and Observable:

*   Publish a group of related data visualizations as a dashboard. Use a wide variety of components including [Plotly](https://plotly.com/), [Leaflet](https://leafletjs.com/), [Jupyter Widgets](https://ipywidgets.readthedocs.io/en/latest/), [htmlwidgets](https://www.htmlwidgets.org/); static graphics (Matplotlib, Seaborn, ggplot2, etc.); tabular data; value boxes; and text annotations.
*   Flexible and easy to specify row and column-based [Layouts](https://quarto.org/docs/dashboards/layout.html). Components are intelligently re-sized to fill the browser and adapted for display on mobile devices.
*   Author using any notebook editor ([JupyterLab](https://quarto.org/docs/tools/jupyter-lab.html), etc.) or in plain text markdown with any text editor ([VS Code](https://quarto.org/docs/tools/vscode.html), [RStudio](https://quarto.org/docs/tools/rstudio.html), [Neovim](https://quarto.org/docs/tools/neovim.html), etc.)
*   Dashboards can be deployed as static web pages (no special server required) or you can optionally integrate a backend [Shiny Server](https://posit.co/products/open-source/shiny-server/) for enhanced interactivity.

### Examples

You can create highly customized layouts and use a wide variety of dashboard themes as illustrated in these examples (click to see them in more detail):

![Dashboard Example 1](https://quarto.org/docs/dashboards/images/thumbnail-penguins.png)
![Dashboard Example 2](https://quarto.org/docs/dashboards/images/thumbnail-retirement.png)
![Dashboard Example 3](https://quarto.org/docs/dashboards/images/thumbnail-flights.png)
![Dashboard Example 4](https://quarto.org/docs/dashboards/images/thumbnail-sales.png)

For live versions of these dashboards, source code, and additional examples see the [dashboard section of the gallery](https://quarto.org/docs/gallery/#dashboards).

### Walkthrough

Here we’ll walk through a simple example to illustrate the basics. Then, we’ll provide detailed instructions on how to get started with building your own dashboards.

This simple single-page Python dashboard uses interactive Plotly visualizations to explore development indicators in the [Gapminder](https://www.gapminder.org/data/) dataset. The dashboard includes two rows, the second of which includes two columns:

![Gapminder Dashboard Example](https://quarto.org/docs/dashboards/images/gapminder-dashboard.png)

Dashboards consist of several components:

*   **Navigation Bar** — Icon, title, and author along with links to sub-pages (if more than one page is defined).
*   **Pages, Rows, Columns, and Tabsets** — Pages, rows and columns are defined using markdown headings (with optional attributes to control height, width, etc.). Tabsets can be used to further divide content within a row or column.
*   **Cards, Sidebars, and Toolbars** — Cards are containers for plots, data display, and free form content. The content of cards typically maps to [cells](https://quarto.org/docs/dashboards/data-display.html#cell-output) in your notebook or source document. Sidebars and toolbars are used to present inputs within interactive dashboards.

Dashboards can be created either using Jupyter notebooks (`.ipynb`) or using plain text markdown (`.qmd`). Here is the code for the notebook version of the above example (click the image for a zoomed view):

[![Notebook Source Code](https://quarto.org/docs/dashboards/images/gapminder-notebook.png)](https://quarto.org/docs/dashboards/images/gapminder-notebook.png)

Here is the plain text `.qmd` version of the dashboard (click on the numbers on the far right for additional explanation of syntax and mechanics):

````markdown
---
title: "Development Indicators by Continent"
author: "Gapminder Analytics Group"
format: dashboard
---

```{python}
import plotly.express as px
df = px.data.gapminder()
```

