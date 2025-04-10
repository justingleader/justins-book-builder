## Exploring the data

See @fig-bill-sizes for an exploration of bill sizes by species.
"""

# %%
#| label: fig-bill-sizes
#| fig-cap: Bill Sizes by Species

import matplotlib.pyplot as plt
import seaborn as sns

g = sns.FacetGrid(df, hue="species", height=3, aspect=3.5/1.5)
g.map(plt.scatter, "bill_length_mm", "bill_depth_mm").add_legend()
```

1.  Scripts rendered with Quarto must begin with a markdown cell containing the YAML header.
2.  A code cell.
3.  A markdown cell containing a multiline string (`"""`).
4.  Code cell options specified with `#|` comments.
5.  You can include blank lines within cells—cells continue until another cell is encountered.

##### Generating Markdown

Jupyter scripts are especially convenient when most of your document consists of code that dynamically generates markdown. You can write markdown from Python using functions in the `IPython.display` module. For example:

```python
# %%
#| echo: false
radius = 10
from IPython.display import Markdown
Markdown(f"The _radius_ of the circle is **{radius}**.")
```

Note that dynamically generated markdown will still be enclosed in the standard Quarto output divs. If you want to remove all of Quarto’s default output enclosures use the `output: asis` option. For example:

```python
# %%
#| echo: false
#| output: asis
radius = 10
from IPython.display import Markdown
Markdown(f"The _radius_ of the circle is **{radius}**.")
```

##### Raw Cells

You can include raw cells (e.g. HTML or LaTeX) within scripts using the `# %% [raw]` cell delimiter along with a `format` attribute, for example:

```python
# %% [raw] format="html"
"""
<iframe width="560" height="315" src="https://www.youtube.com/embed/lJIrF4YjHfQ?si=aP7PxA1Pz8IIoQUX"></iframe>
"""
```

#### Knitr

Script rendering for Knitr is based on the [`knitr::spin()`](https://bookdown.org/yihui/rmarkdown-cookbook/spin.html) feature and makes use of the same [syntax rules](https://bookdown.org/yihui/rmarkdown-cookbook/spin.html#syntax):

*   Markdown content is included on lines starting with a special `#'` comment.
*   Lines that don’t start with `#` are code. Code blocks are split when Markdown content occurs , e.g. use `#'` to create another code block.

There are also Quarto-specific additions:

*   The R script must start with YAML header block using the special `#'` comment.
*   You can add code cell options in the usual way with `#|` comments.

For example, here is an R script that includes both markdown and code cells (you can click on the numbers on the right for further details):

**script.R**
```r
#' ---
#' title: Palmer Penguins
#' author: Norah Jones
#' date: 3/12/23
#' format: html
#' ---

library(palmerpenguins)

#' ## Exploring the data
#' See @fig-bill-sizes for an exploration of bill sizes by species.

#| label: fig-bill-sizes
#| fig-cap: Bill Sizes by Species
#| warning: false

library(ggplot2)
ggplot(
  data = penguins,
  aes(
    x = bill_length_mm,
    y = bill_depth_mm,
    group = species)) +
  geom_point(
    aes(
      color = species,
      shape = species),
    size = 3,
    alpha = 0.8
  ) +
  labs(
    title = "Penguin bill dimensions",
    subtitle = "Bill length and depth for Adelie, Chinstrap and Gentoo Penguins at Palmer Station LTER",
    x = "Bill length (mm)",
    y = "Bill depth (mm)",
    color = "Penguin species",
    shape = "Penguin species"
  )
```

1.  Scripts rendered with Quarto must begin with a YAML header using `#'` comments.
2.  R code is the main content of the R script and is included without any delimitation.
3.  Preface Markdown content with the `#'` comment.
4.  Code cell options are specified with `#|` comments and apply to code below them.

### Render and Preview

You can render and preview notebook scripts just as you would a `.qmd` or `.ipynb` file. For example, the following commands are all valid:

```bash
quarto render script.py
quarto render script.jl
quarto render script.R

quarto preview script.py
quarto preview script.jl
quarto preview script.R
```

The script must begin with the appropriate [syntax](#syntax) for the YAML block to be rendered with Quarto. Based on the syntax detected Quarto will render with the Jupyter or Knitr engine.

The [Quarto VS Code Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) also implements support for rendering and previewing scripts.

### Scripts in Projects

Notebook scripts can also be included within [projects](https://quarto.org/docs/projects/quarto-projects.html) (e.g. websites, blogs, etc.). Scripts within projects are only rendered by Quarto when they start with the appropriate [syntax](#syntax).

If for some reason you need to ignore such a script, you can create an explict render list in `_quarto.yml` that excludes individual scripts as required, for example:

```yaml
project:
  type: website
  render:
    - "*.{qmd,R,py}"
    - "!utils.py"
```

Note that this technique is documented for the sake of completeness—in practice you should almost never need to do this since scripts rarely begin with a YAML block unless you are authoring them specifically for report rendering.

