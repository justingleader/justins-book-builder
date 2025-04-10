## Authoring Cross-Reference Div Syntax

Source: [Cross-Reference Div Syntax – Quarto](https://quarto.org/docs/authoring/cross-references-divs.html)

### Overview

Cross-referenceable [figures](https://quarto.org/docs/authoring/cross-references.html#figures), [tables](https://quarto.org/docs/authoring/cross-references.html#tables) and [code listings](https://quarto.org/docs/authoring/cross-references.html#code-listings) are known as *float* cross-references. Floats can appear in the rendered document at locations other than where they are defined, i.e. they float, and usually have captions.

Along with compact syntax for the most common uses of cross-references, Quarto also provides a more general div syntax for declaring floats that can be cross-referenced. To declare a cross-referenceable float, place the content inside a fenced div with the reference identifier as an attribute. The last paragraph inside the fenced div will be treated as the caption. For example:

```markdown
::: {#fig-example}
CONTENT

Caption
:::
```

To be recognized as a cross-reference the identifier must begin with one of the built-in float reference types (Figures (`fig-`), Tables (`tbl-`) and Listings (`lst-`)), or be defined as a [custom float cross-reference](https://quarto.org/docs/authoring/cross-references-custom.html) type.

You can then refer to the element as usual with the `@` syntax, e.g. `@fig-example shows...`

The content can be any Quarto markdown. For example, Figure 1 is a markdown table treated like a figure:

```markdown
::: {#fig-table}
| A | B |
|---|---|
| C | D |

A table treated like a figure
:::
```

Result:

| A   | B   |
| :-- | :-- |
| C   | D   |

Figure 1: A table treated like a figure

Table 1 is an image treated like a table:

```markdown
::: {#tbl-table}
![](table.png)

An image treated like a table
:::
```

Result:

![An image treated like a table](table.png)

Table 1: An image treated like a table

Figure 2 is a code cell treated like a figure:

```markdown
::: {#fig-code}
```r
library(tidyverse)
starwars |>
  ggplot(aes(height, mass)) +
  geom_point()
```

A code cell treated like a figure.
:::
```

Result:

```r
library(tidyverse)
starwars |>
  ggplot(aes(height, mass)) +
  geom_point()
```

Figure 2: A code cell treated like a figure.

On this page, we illustrate common use cases for [Figures](#figures), [Tables](#tables) and [Code Listings](#listings) then some applications of the div syntax to:

*   [Cross-reference a video](#videos)
*   [Cross-reference a diagram](#diagrams)
*   [Produce subreferences to mixed content](#subreferences)
*   [Use computed values in a caption](#computed-captions)

### Figures

To create a cross-reference to a figure using div syntax, create a fenced div with an id starting with `fig-`, include the image followed by the caption inside the div:

```markdown
::: {#fig-elephant}
![](elephant.png)

An Elephant
:::
```

You can cross-reference a figure created by an executable code cell by including the code cell as the content:

````markdown
::: {#fig-line-plot}
```{python}
import matplotlib.pyplot as plt
plt.plot([1,23,2,4])
plt.show()
```

A line plot
:::
````

In the above example, you can reference the figure with `@fig-line-plot`, but not the code, which appears inline. If you would also like to be able to refer to the code, you can do so using code chunk options rather than the div syntax, see [Cross-References for Executable Code Blocks](https://quarto.org/docs/authoring/cross-references.html#computations-1) for details.

### Tables

To create a cross-reference to a table using div syntax, create a fenced div with an id starting with `tbl-`, include the table followed by the caption inside the div:

```markdown
::: {#tbl-letters}
| Col1 | Col2 | Col3 |
|------|------|------|
| A    | B    | C    |
| E    | F    | G    |
| A    | G    | G    |

My Caption
:::
```

If the table is produced by an executable code cell, put the cell inside the div as content, e.g:

````markdown
::: {#tbl-planets}
```{python}
from IPython.display import Markdown
from tabulate import tabulate
table = [["Sun","696,000",1.989e30],
         ["Earth","6,371",5.972e24],
         ["Moon","1,737",7.34e22],
         ["Mars","3,390",6.39e23]]
Markdown(tabulate(
  table,
  headers=["Astronomical object","R (km)", "mass (kg)"]
))
```

Astronomical object
:::
````

In the above example, you can reference the table with `@tbl-planets`, but not the code, which appears inline. If you would also like to be able to refer to the code, you can do so using code chunk options rather than the div syntax, see [Cross-References for Executable Code Blocks](https://quarto.org/docs/authoring/cross-references.html#computations-1) for details.

### Listings

To create a cross-reference to a code listing using div syntax, create a fenced div with an id starting with `lst-`, include the code cell followed by the caption inside the div:

````markdown
::: {#lst-customers}
```{.sql}
SELECT * FROM Customers
```

Customers Query
:::
````

This also works for executable code cells that produce no output:

````markdown
::: {#lst-assign}
```{r}
x <- 1
```

Assignment in R
:::
````

However, if any output is produced, it is assumed the output should be the content of the cross-reference, and the code is lifted out and placed inline. For example, the code cell here produces output:

````markdown
::: {#lst-assign-output}
```{r}
x <- 1
x
```

Assignment in R
:::

@lst-assign-output
````

When rendered the above results in output being the contents of the listing, with the code appearing before the listing:

```r
x <- 1
x
```

```
