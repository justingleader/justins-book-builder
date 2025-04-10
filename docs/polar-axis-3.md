## Polar Axis

For a demonstration of a line plot on a polar axis, see @fig-polar.

```{python}
#| label: fig-polar
#| fig-cap: "A line plot on a polar axis"

import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
fig, ax = plt.subplots(
  subplot_kw = {'projection': 'polar'}
)
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()
```

Next, open a Terminal and switch to the directory containing `hello.qmd`.

Let’s start by rendering the document to a couple of formats.

```bash
quarto render hello.qmd --to html
quarto render hello.qmd --to docx
```

Note that the target file (in this case `hello.qmd`) should always be the very first command line argument.

When you render a `.qmd` file with Quarto, the executable code blocks are processed by Jupyter, and the resulting combination of code, markdown, and output is converted to plain markdown. Then, this markdown is processed by [Pandoc](https://pandoc.org/), which creates the finished format.

### Authoring

The `quarto render` command is used to create the final version of your document for distribution. However, during authoring you’ll use the `quarto preview` command. Try it now from the Terminal with `hello.qmd`.

```bash
quarto preview hello.qmd
```

This will render your document and then display it in a web browser.

You might want to position your editor and the browser preview side-by-side so you can see changes as you work.

To see live preview in action:

1.  Change the line of code that defines `theta` as follows:
    ```python
    theta = 4 * np.pi * r
    ```
2.  Save the file. The document is re-rendered, and the browser preview is updated.

This is the basic workflow for authoring with Quarto.

There are few different types of content in `hello.qmd`, let’s work a bit with each type.

#### YAML Options

At the top of the file there is a YAML block with document level options.

```yaml
---
title: "Quarto Basics"
format:
  html:
    code-fold: true
jupyter: python3
---
```

Try changing the `code-fold` option to `false`:

```yaml
format:
  html:
    code-fold: false
```

Then save the file. You’ll notice that the code is now shown above the plot, where previously it was hidden with a `Code` button that could be used to show it.

#### Markdown

Narrative content is written using markdown. Here we specify a heading and a cross-reference to the figure created in the code cell below.

```markdown
