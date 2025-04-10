## Column

```{python}
```

```{python}
```
````

Here’s how a sidebar would appear (note there is a button in the top right that enables the user to optionally close the sidebar):

![Sidebar Example](https://quarto.org/docs/dashboards/images/sidebar-example.png)

#### Global Sidebar

If you have a dashboard with [multiple pages](https://quarto.org/docs/dashboards/layout.html#pages), you may want the sidebar to be global (i.e. visible across all pages). To do this, add the `.sidebar` class to a level 1 heading:

````markdown
---
title: "Sidebar"
format: dashboard
---

# {.sidebar}
Sidebar content

# Plots

```{python}
```

# Data

```{python}
```
````

#### Inline Sidebar

While sidebars are often laid out at the page level (i.e. spanning the dashboard from top to bottom) you can actually include them anywhere within a layout. For example, here we have a sidebar that is within a row (rather than spanning all rows):

````markdown
---
title: "Palmer Penguins"
format: dashboard
server: shiny
---

