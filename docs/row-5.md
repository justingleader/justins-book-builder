## Row

```{python}
```
````

#### Global Toolbar

If you have a dashboard with [multiple pages](https://quarto.org/docs/dashboards/layout.html#pages), you may want the toolbar to be global (i.e. visible across all pages). To do this, add the `.toolbar` class to a level 1 heading:

````markdown
---
title: "Toolbar"
format: dashboard
server: shiny
---

# {.toolbar}
Toolbar content

# Page 1

```{python}
```

# Page 2

```{python}
```
````

#### Inline Toolbar

While toolbars are often laid out at the page level (i.e. spanning the dashboard from left to right) you can actually include them anywhere within a layout. For example, here we have a toolbar that is within a column (rather than spanning all columns):

````markdown
---
title: "Palmer Penguins"
format:
  dashboard:
    orientation: columns
server: shiny
---

