## Row {height=40%}

```{python}
#| title: Population
px.area(
  df, x="year", y="pop",
  color="continent", line_group="country"
)
```

```{python}
#| title: Life Expectancy
px.line(
  df, x="year", y="lifeExp",
  color="continent", line_group="country"
)
```
````

1.  The document options define the `title` and `author` for the navigation bar as well as specifying the use of the `dashboard` format.
2.  Rows and columns are defined using headings. In this example we define two rows and specify their relative sizes using the `height` option.
3.  Computational cells become cards that live within rows or columns. Cards can have an optional title (which here we specify using the `title` option).
4.  The second row includes two computational cells, which are automatically split into two side by side cards.

### Getting Started

#### Step 1: Install Quarto

Dashboards are a feature in the Quarto v1.4. Before you get started, make sure you install the [latest release](https://quarto.org/docs/download/) version of Quarto.

#### Step 2: Learn the Basics

Start by learning how to lay out your dashboard and populate it with content:

*   [Dashboard Layout](https://quarto.org/docs/dashboards/layout.html) shows you how to control the navigation bar, and how to arrange your content across pages, rows, columns, tabsets, and cards.
*   [Data Display](https://quarto.org/docs/dashboards/data-display.html) shows you how to display data in your dashboard as plots, tables, value boxes, and text.

#### Step 3: Explore Further

Once you’ve mastered the basics, check out these additional articles to learn more.

*   [Examples](https://quarto.org/docs/gallery/#dashboards) provides a gallery of example dashboards you can use as inspiration for your own.
*   [Inputs](https://quarto.org/docs/dashboards/inputs.html) demonstrates various ways to layout inputs for interactive dashboards (sidebars, toolbars, attaching inputs directly to cards, etc.)
*   [Theming](https://quarto.org/docs/dashboards/theming.html) describes the various way to customize the fonts, colors, layout and other aspects of dashboard appearance.
*   [Parameters](https://quarto.org/docs/dashboards/parameters.html) explains how to create dashboard variants by defining parameters and providing distinct values for them on the command line.
*   [Deployment](https://quarto.org/docs/dashboards/deployment.html) covers how to deploy both static dashboards (which require only a web host, but not a server) and Shiny dashboards (which require a Shiny Server).
*   [Interactivity](https://quarto.org/docs/dashboards/interactivity/) explores the various ways to create interactive dashboards that enable more flexible data exploration.

