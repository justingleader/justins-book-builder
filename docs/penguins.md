## Penguins

This example uses the **palmerpenguins** dataset and `ggplot2` to create a scatterplot of penguin bill length versus depth.

![Penguins plotting bill depth versus length](penguin-plot.png){#fig-scatterplot}

The code below creates the scatterplot:

```{r}
#| label: penguin-plot
#| fig-cap: Penguin bill dimensions
#| warning: false

ggplot(penguins, aes(x = bill_depth_mm, y = bill_length_mm, color = species)) +
  geom_point(na.rm = TRUE) +
  geom_smooth(method = "lm", na.rm = TRUE) +
  labs(
    title = "Bill depth and length",
    x = "Bill depth (mm)",
    y = "Bill length (mm)"
  )
```

@fig-scatterplot shows the relationship between bill length and depth for the Adelie, Chinstrap, and Gentoo penguins.
```

Quarto uses markdown syntax for text. If using the visual editor, you won’t need to learn much markdown syntax for authoring your document, as you can use the menus and shortcuts to add a heading, bold text, insert a table, etc. If using the source editor, you can achieve these with markdown expressions like `##`, `**bold**`, etc.

#### How it works

When you render a Quarto document, first [`knitr`](https://yihui.org/knitr/) executes all of the code chunks and creates a new markdown (.md) document, which includes the code and its output. The markdown file generated is then processed by [`pandoc`](https://pandoc.org/), which creates the finished format. The Render button encapsulates these actions and executes them in the right order for you.

### Next Up

You now know the basics of creating and authoring Quarto documents. The following tutorials explore Quarto in more depth:

*   [Tutorial: Computations](https://quarto.org/docs/get-started/computations/) — Learn how to tailor the behavior and output of executable code blocks.
*   [Tutorial: Authoring](https://quarto.org/docs/get-started/authoring/) — Learn more about output formats and technical writing features like citations, crossrefs, and advanced layout.

