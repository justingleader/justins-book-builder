## Dashboards: Data Display

Source: [Dashboard Data Display – Quarto](https://quarto.org/docs/dashboards/data-display.html)

Dashboards are compositions of components used to provide navigation and present data. Below we’ll cover presenting data using plots, tables, and value boxes, as well how to include narrative content within dashboards.

### Plots

Plots are by far the most common content type displayed in dashboards. Both interactive JavaScript-based plots (e.g. [Altair](https://altair-viz.github.io/) and [Plotly](https://plotly.com/python/)) and standard raster based plots (e.g. [Matplotlib](https://matplotlib.org/) or [ggplot2](https://ggplot2.tidyverse.org/)) are supported.

Below we provide some language specific tips and techniques for including plots within dashboards.

#### Python

*   **plotly:** [Plotly](https://plotly.com/python/) is a popular Python package for JavaScript based plots, and works very well in dashboard layouts. Plotly is also noteworthy because it includes many interactive features while still not requiring a server. For example, this plot supports an animated display of values changing over time:
    ````markdown
    ```{python}
    #| title: GDP and Life Expectancy

    import plotly.express as px
    df = px.data.gapminder()
    px.scatter(
      df, x="gdpPercap", y="lifeExp",
      animation_frame="year", animation_group="country",
      size="pop", color="continent", hover_name="country",
      facet_col="continent", log_x=True, size_max=45,
      range_x=[100,100000], range_y=[25,90]
    )
    ```
    ````
*   **altair:** [Altair](https://altair-viz.github.io/) is a declarative statistical visualization library for Python based on Vega and Vega-Lite. Altair plots are JavaScript based so automatically resize themselves to fit their container within dashboards.
    ````markdown
    ```{python}
    #| title: Iowa Electricity

    import altair as alt
    from vega_datasets import data

    source = data.iowa_electricity()

    alt.Chart(source).mark_area(opacity=0.3).encode(
      x="year:T",
      y=alt.Y("net_generation:Q").stack(None),
      color="source:N"
    )
    ```
    ````
*   **matplotlib:** If you are using traditional plotting libraries within static dashboards, you’ll need to pay a bit more attention to getting the size of plots right for the layout they’ll be viewed in. Note that this is not a concern for plots in interactive Shiny dashboards since all plot types are resized dynamically by Shiny.

    If you are using [Matplotlib](https://matplotlib.org/) (or libraries built on it like [Seaborn](https://seaborn.pydata.org/)) then you can set plot sizes using the `figure.figsize` global option (or alternatively per-figure if that’s more convenient):
    ````markdown
    ```{python}
    import matplotlib.pyplot as plt
    plt.rcParams['figure.figsize'] = (12, 3)
    ```
    ````
    In the case that your plots are laid out at a wider aspect ratio, setting this option can make a huge difference in terms of using available space. For example, the top plot in the stack below uses the default figure size of 8 x 5 and the bottom one uses the 12 x 3 ratio specified above:
    ![Matplotlib Plot Sizing](https://quarto.org/docs/dashboards/images/matplotlib-sizing.png)

    Note that the need to explicitly size plots is confined to traditional plotting libraries—if you use Plotly or another JavaScript based plotting system plots will automatically resize to fill their container.

#### R

*   **htmlwidgets:** The [htmlwidgets](https://www.htmlwidgets.org/) framework provides high-level R bindings for JavaScript data visualization libraries. Some popular htmlwidgets include [Plotly](https://plotly.com/r/), [Leaflet](https://rstudio.github.io/leaflet/), and [dygraphs](https://rstudio.github.io/dygraphs/).

    You can use htmlwidgets just like you use normal R plots. For example, here is how we embed a Leaflet map:
    ````markdown
    ```{r}
    library(leaflet)
    leaflet() %>%
      addTiles() %>%
      addMarkers(lng=174.768, lat=-36.852,
                 popup="The birthplace of R")
    ```
    ````
    There are dozens of packages on CRAN that provide htmlwidgets. You can find example uses of several of the more popular htmlwidgets in the htmlwidgets [showcase](https://gallery.htmlwidgets.org/) and browse all available widgets in the [gallery](https://gallery.htmlwidgets.org/).
*   **R Graphics:** You can use any chart created with standard R raster graphics (base, lattice, grid, etc.) within dashboards. When using standard R graphics with static dashboards, you’ll need to pay a bit more attention to getting the size of plots right for the layout they’ll be viewed in. Note that this is not a concern for plots in interactive Shiny dashboards since all plot types are resized dynamically by Shiny.

    The key to good sizing behavior in static dashboards is to define knitr `fig-width` and `fig-height` options that enable the plots to fit into their layout container as closely as possible.

    Here’s an example of a layout that includes 3 charts from R base graphics:
    ````markdown
    ## Row {height="65%"}

    ```{r}
    #| fig-width: 10
    #| fig-height: 8
    plot(cars)
    ```

    ## Row {height="35%"}

    ```{r}
    #| fig-width: 5
    #| fig-height: 4
    plot(pressure)
    ```

    ```{r}
    #| fig-width: 5
    #| fig-height: 4
    plot(airmiles)
    ```
    ````
    We’ve specified an explicit `fig-height` and `fig-width` for each plot so that their rendered size fits their layout container as closely as possible. Note that the ideal values for these dimensions typically need to be determined by experimentation.

**Tip:** For static dashboards, there are pros and cons to using JavaScript-based plots. While JavaScript-based plots handle resizing to fill their container better than static plots, they also embed the underlying data directly in the published page (one copy of the dataset per plot), which can lead to slower load times. For interactive Shiny dashboards, all plot types are sized dynamically, so resizing behavior is not a concern as it is with static dashboards.

### Tables

You can include data tables within dashboards in one of two ways:

1.  As a simple tabular display.
2.  As an interactive widget that includes sorting and filtering.

Below we provide some language specific tips and techniques for including tables within dashboards.

#### Python

There are many Python packages available for producing tabular output. We’ll cover two of the more popular libraries (itables and tabulate) below.

*   **itables:** The Python [itables](https://mwouts.github.io/itables/) package supports creating interactive data tables from Pandas and Polars DataFrames that you can sort and filter.

    Use the `show()` method from `itables` to display an interactive table:
    ````markdown
    ```{python}
    from itables import show
    show(penguins)
    ```
    ````
    **Options:** Note that a few `itables` options are set automatically within dashboards to ensure that they display well in cards of varying sizes. The option defaults are:
    ```python
    from itables import options
    options.dom = 'fiBrtlp'
    options.maxBytes = 1024*1024
    options.language = dict(info = "Showing _TOTAL_ entries")
    options.classes = "display nowrap compact"
    options.paging = False
    options.searching = True
    options.ordering = True
    options.info = True
    options.lengthChange = False
    options.autoWidth = False
    options.responsive = True
    options.keys = True
    options.buttons = []
    ```
    You can specify alternate options as you like to override these defaults. Options can be specified in the call to `show()` or globally as illustrated above. Here’s an example of specifying an option with `show()`:
    ```python
    show(penguins, searching = False, ordering = False)
    ```
    You can find the reference for all of the DataTables options here: <https://datatables.net/reference/option/>. All base options are available, as well as the options for the following extensions (which are automatically included by Quarto):
    *   <https://datatables.net/extensions/buttons/>
    *   <https://datatables.net/extensions/keytable/>
    *   <https://datatables.net/extensions/responsive/>
    For example, to enable the copy and export (excel/pdf) buttons in a call to `show()`:
    ```python
    show(penguins, buttons = ['copy', 'excel', 'pdf'])
    ```
    Or alternatively, to enable these buttons for all tables:
    ```python
    from itables import options
    options.buttons = ['copy', 'excel', 'pdf']
    ```
    **Downsampling:** When a table is displayed, the table data is embedded in the dashboard output. To prevent dashboards from being too heavy to load for larger datasets, itables will display only a subset of the table—one that fits into `maxBytes` (1024kb by default).
    If you wish, you can increase the value of `maxBytes` or even deactivate the limit (with `maxBytes=0`). For example, to set a limit of 200kb:
    ````markdown
    ```{python}
    show(penguins, maxBytes = 200*1024)
    ```
    ````
*   **tabulate:** The Python [tabulate](https://github.com/astanin/python-tabulate) package supports creating markdown tables from Pandas data frames, NumPy arrays, and many other data types. You can generate a markdown table from any Pandas data frame via the `to_markdown()` method (being sure to wrap it as `Markdown` output using IPython):
    ````markdown
    ```{python}
    import pandas as pd
    from IPython.display import Markdown

    penguins = pd.read_csv("penguins.csv")
    Markdown(penguins.to_markdown(index=False))
    ```
    ````
    Note that the `index = False` parameter supresses the display of the row index. Here is a card containing output from `tabulate`:
    ![Tabulate Table Example](https://quarto.org/docs/dashboards/images/tabulate-table.png)

    You can also import `tabulate` directly and pass in the object to print directly:
    ````markdown
    ```{python}
    from tabulate import tabulate
    Markdown(
      tabulate(penguins, showindex=False,
               headers=penguins.columns)
    )
    ```
    ````

#### R

There are many R packages available for producing tabular output. We’ll cover two of the more popular approaches (kable and DT) below.

*   **kable:** Simple markdown tables are ideal for smaller numbers of records (i.e. 20-250 rows). Use the `knitr::kable()` function to output markdown tables:
    ````markdown
    ```{r}
    knitr::kable(mtcars)
    ```
    ````
    Simple markdown tables in dashboards automatically fill their container (scrolling horizontally and vertically as required).
*   **DT:** The [`DT`](https://rstudio.github.io/DT/) package (an interface to the DataTables JavaScript library) can display R matrices or data frames as interactive HTML tables that support filtering, pagination, and sorting.

    To include a DataTable you use the `DT::datatable` function:
    ````markdown
    ```{r}
    library(DT)
    datatable(mtcars)
    ```
    ````
    **Options:** Note that a few `DT` options are set automatically within dashboards to ensure that they display well in cards of varying sizes. The option defaults are:
    ```r
    options(
      DT.options = list(
        bPaginate = FALSE,
        dom = "ifrt",
        language = list(info = "Showing _TOTAL_ entries")
      ))
    ```
    You can specify alternate options as you like to override these defaults.

### Value Boxes

Value boxes are a great way to prominently display simple values within a dashboard. For example, here is a dashboard row with three value boxes:

![Value Box Example](https://quarto.org/docs/dashboards/images/value-boxes.png)

Here is the code you might use to create these value boxes. Note that we use a mix of Python and R cells in this example to illustrate the syntax for each language. Note also that we assume the variables `articles`, `comments`, and `spam` are computed previously within the document.

````markdown
