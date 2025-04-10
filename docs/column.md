## Column

```{python}
#| title: Population
px.area(df, x="year", y="pop", color="continent",
        line_group="country")
```

```{python}
#| title: Life Expectancy
px.line(df, x="year", y="lifeExp", color="continent",
        line_group="country")
```

::: {.card}
Gapminder combines data from multiple sources into
unique coherent time-series that can’t be found
elsewhere. Learn more about the Gampminder dataset at
<https://www.gapminder.org/data/>.
:::
````

Note that if you are authoring using a Jupyter Notebook then markdown cells automatically become `.card` divs (i.e. they don’t need the explicit `:::` div enclosure).

#### Content within Cells

To include content alongside the ouptut of a cell, just enclose the both the cell and the content in a `.card` div. For example:

````markdown
::: {.card title="Life Expectancy"}

```{python}
px.line(df, x="year", y="lifeExp", color="continent",
        line_group="country")
```

Gapminder combines data from multiple sources into
unique coherent time-series that can’t be found
elsewhere. Learn more about the Gampminder dataset at
<https://www.gapminder.org/data/>.
:::
````

#### Leading Content

Content that is included at the very top of a dashboard (and not explicitly within a `.content` div) is considered leading content, and will be included as is with no card styling (e.g. with no border). For example:

```markdown
---
title: "My Dashboard"
format: dashboard
---

This content will appear above all of the other rows/columns, with no border.

