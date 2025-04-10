## Row

```{python}
#| content: valuebox
#| title: "Articles per day"
#| icon: pencil
#| color: primary

dict(
  value = articles
)
```

```{python}
#| content: valuebox
#| title: "Comments per day"

dict(
  icon = "chat",
  color = "primary",
  value = comments
)
```

```{r}
#| content: valuebox
#| title: "Spam per day"

list(
  icon = "trash",
  color = "danger",
  value = spam
)
```
````

You can choose between specifying value box options within YAML or within a `dict()` or `list()` (for Python and R, respectively) printed by the cell. The latter syntax is handy when you want the `icon` or `color` to be dynamic based on the value.

#### Icon and Color

The `icon` used in value boxes can be any of the 2,000 available [bootstrap icons](https://icons.getbootstrap.com/).

The `color` can be any CSS color value, however there are some color aliases that are tuned specifically for dashboards that you might consider using by default:

| Color Alias | Default Theme Color(s) |
| :---------- | :--------------------- |
| `primary`   | Blue                   |
| `secondary` | Gray                   |
| `success`   | Green                  |
| `info`      | Bright Blue            |
| `warning`   | Yellow/Orange          |
| `danger`    | Red                    |
| `light`     | Light Gray             |
| `dark`      | Black                  |

You can override these defaults by specifying [value box Sass variables](https://quarto.org/docs/dashboards/theming.html#value-boxes) in a custom theme.

While the aliases apply to all [themes](https://quarto.org/docs/dashboards/theming.html), the colors they correspond to vary.

#### Shiny

In a Shiny interactive dashboard you can have value boxes that update dynamically based on the state of the application. The details on how to do this are language-specific:

*   **Python:** Use the `ui.value_box()` function within a function decorated with `@render.ui`. For example:
    ````markdown
    ```{python}
    from shiny.express import render, ui
    @render.ui
    def value():
      return ui.value_box("Value", input.value())
    ```
    ````
*   **R:** Use the `bslib::value_box()` function along with an optional icon drawn from the `bsicons` package. For example:
    ````markdown
    ```{r}
    library(bslib)
    library(bsicons)
    value_box(
      title = "Value",
      value = textOutput("valuetext"),
      showcase = bs_icon("music-note-beamed")
    )
    ```
    ````

#### Markdown Syntax

You can also create value boxes using plain markdown, in which case you’ll typically include the value via an inline expression. For example:

````markdown
