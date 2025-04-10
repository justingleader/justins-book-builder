## Computations: Execution Options

Source: [Execution Options – Quarto](https://quarto.org/docs/computations/execution-options.html)

### Output Options

There are a wide variety of options available for customizing output from executed code. All of these options can be specified either globally (in the document front-matter) or per code-block. For example, here’s a modification of the Python example to specify that we don’t want to “echo” the code into the output document:

```yaml
---
title: "My Document"
execute:
  echo: false
jupyter: python3
---
```

Note that we can override this option on a per code-block basis. For example:

````markdown
```{python}
#| echo: true
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()
```
````

Code block options are included in a special comment at the top of the block (lines at the top prefaced with `#|` are considered options).

Options available for customizing output include:

| Option    | Description                                                                                                                                           |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `eval`    | Evaluate the code chunk (if `false`, just echos the code into the output).                                                                            |
| `echo`    | Include the source code in output                                                                                                                     |
| `output`  | Include the results of executing the code in the output (`true`, `false`, or `asis` to indicate that the output is raw markdown and should not have any of Quarto’s standard enclosing markdown). |
| `warning` | Include warnings in the output.                                                                                                                       |
| `error`   | Include errors in the output (note that this implies that errors executing code will not halt processing of the document).                              |
| `include` | Catch all for preventing any output (code or results) from being included (e.g. `include: false` suppresses all output from the code block).            |

Here’s a Knitr example with some of these additional options included:

````markdown
---
title: "Knitr Document"
execute:
  echo: false
---

```{r}
#| warning: false
library(ggplot2)
ggplot(airquality, aes(Temp, Ozone)) +
  geom_point() +
  geom_smooth(method = "loess", se = FALSE)
```

```{r}
summary(airquality)
```
````

**Tip:** When using the Knitr engine, you can also use any of the available native options (e.g. `collapse`, `tidy`, `comment`, etc.). See the [Knitr options documentation](https://yihui.org/knitr/options/) for additional details. You can include these native options in option comment blocks as shown above, or on the same line as the `{r}` as shown in the Knitr documentation.

**Tip:** The Knitr engine can also *conditionally* evaluate a code chunk using objects or expressions. See [Using R: Knitr Options](https://quarto.org/docs/computations/r.html#chunk-options).

### Figure Options

There are a number of ways to control the default width and height of figures generated from code. First, it’s important to know that Quarto sets a default width and height for figures appropriate to the target output format. Here are the defaults (expressed in inches):

| Format                      | Default Width | Default Height |
| :-------------------------- | :-----------: | :------------: |
| Default                     |      7        |       5        |
| HTML Slides                 |      9.5      |      6.5       |
| HTML Slides (reveal.js)     |      9        |       5        |
| PDF                         |      5.5      |      3.5       |
| PDF Slides (Beamer)         |      10       |       7        |
| PowerPoint                  |      7.5      |      5.5       |
| MS Word, ODT, RTF           |      5        |       4        |
| EPUB                        |      5        |       4        |
| Hugo                        |      8        |       5        |

These defaults were chosen to provide attractive well proportioned figures, but feel free to experiment to see whether you prefer another default size. You can change the default sizes using the `fig-width` and `fig-height` options. For example:

```yaml
---
title: "My Document"
format:
  html:
    fig-width: 8
    fig-height: 6
  pdf:
    fig-width: 7
    fig-height: 5
---
```

How do these sizes make their way into the engine-level defaults for generating figures? This differs by engine:

*   For the **Knitr** engine, these values become the default values for the `fig.width` and `fig.height` chunk options. You can override these default values via chunk level options.
*   For **Python**, these values are used to set the Matplotlib `figure.figsize` rcParam (you can of course manually override these defaults for any given plot).
*   For **Julia**, these values are used to initialize the default figure size for the `Plots.jl` GR backend.

If you are using another graphics library with Jupyter and want to utilize these values, you can read them from `QUARTO_FIG_WIDTH` and `QUARTO_FIG_HEIGHT` environment variables.

**Caution:** When using the Knitr engine, `fig-width` and `fig-height` are supported on a per-cell basis. But when using the Jupyter engine, these options only have an effect if specified at the document- or project-level metadata.

### Caption and Alt Text

You can specify the caption and alt text for figures generated from code using the `fig-cap` and `fig-alt` options. For example, here we add these options to a Python code cell that creates a plot:

````markdown
```{python}
#| fig-cap: "Polar axis plot"
#| fig-alt: "A line plot on a polar axis"

import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()
```
````

### Inline Code

Jupyter, Knitr and OJS all support executing inline code within markdown (e.g. to allow narrative to automatically use the most up to date computations). See [Inline Code](https://quarto.org/docs/computations/inline-code.html) for details.

### Raw Output

The `output: asis` option enables you to generate raw markdown output. When `output: asis` is specified none of Quarto’s standard enclosing divs will be included. For example, here we specify `output: asis` in order to generate a pair of headings:

**Jupyter:**
````markdown
```{python}
#| echo: false
#| output: asis
print("# Heading 1\n")
print("## Heading 2\n")
```
````

**Knitr:**
````markdown
```{r}
#| echo: false
#| output: asis
cat("# Heading 1\n")
cat("## Heading 2\n")
```
````

Which generates the following output:

# Heading 1

