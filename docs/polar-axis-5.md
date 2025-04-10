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

Note that if you are following along be sure to install the required dependencies if you haven’t already:

| Platform   | Commands                                                     |
| :--------- | :----------------------------------------------------------- |
| Mac/Linux  | `python3 -m pip install jupyter matplotlib plotly`           |
| Windows    | `py -m pip install jupyter matplotlib plotly`                |

To render and preview, execute the `Quarto: Preview` command. You can alternatively use the <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>K</kbd> keyboard shortcut, or the `Preview` button (👁️) at the top right of the editor:

![VS Code Preview Button](https://quarto.org/docs/get-started/images/vscode-preview-button.png)

Note that on the Mac you should use <kbd>Cmd</kbd> rather than <kbd>Ctrl</kbd> as the prefix for all Quarto keyboard shortcuts.

**How it Works:** When you render a `.qmd` file with Quarto, the executable code blocks are processed by Jupyter, and the resulting combination of code, markdown, and output is converted to plain markdown. Then, this markdown is processed by [Pandoc](https://pandoc.org/), which creates the finished format.

### Authoring

Let’s try making a small change and then re-rendering:

1.  Change the line of code that defines `theta` as follows:
    ```python
    theta = 4 * np.pi * r
    ```
2.  Re-render the file (using `Quarto: Preview` or the <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>K</kbd> shortcut) The document is rendered, and the browser preview is updated.

This is the basic workflow for authoring with Quarto.

You do not need to save the file before rendering (as this happens automatically when you render). If you prefer, you can configure the Quarto extension to render whenever you save a document. See the documentation on [Render on Save](https://quarto.org/docs/tools/vscode.html#render-on-save) for additional details.

### Running Cells

You don’t need to fully render documents in order to iterate on code cells. You’ll notice that there is a `Run Cell` button above the code cell. Click that button to execute the cell (output is shown side by side in the Jupyter interactive console):

![VS Code Run Cell](https://quarto.org/docs/get-started/images/vscode-run-cell.png)

Execute the current cell with <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Enter</kbd>, the current line(s) with <kbd>Ctrl</kbd>+<kbd>Enter</kbd>, or previous cells with <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>P</kbd> (note that on the Mac you should use <kbd>Cmd</kbd> rather than <kbd>Ctrl</kbd> as the prefix for all Quarto keyboard shortcuts).

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

Then re-render the document (again, no need to save before rendering). You’ll notice that the code is now shown above the plot, where previously it was hidden with a `Code` button that could be used to show it.

#### Markdown

Narrative content is written using markdown. Here we specify a heading and a cross-reference to the figure created in the code cell below.

```markdown
