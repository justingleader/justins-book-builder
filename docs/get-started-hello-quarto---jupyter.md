## Get Started: Hello, Quarto - Jupyter

Source: [Tutorial: Hello, Quarto – Quarto](https://quarto.org/docs/get-started/hello/jupyter.html) (Content largely duplicated from Tools: JupyterLab section, tailored for beginners)

### Overview

In this tutorial we’ll show you how to use Jupyter Lab with Quarto. You’ll edit code and markdown in Jupyter Lab, just as you would with any notebook, and preview the rendered document in a web browser as you work.

Below is an overview of how this will look.

![Jupyter Lab and Quarto Preview Side-by-Side](https://quarto.org/docs/get-started/images/jupyterlab-preview.png)

The notebook on the left is *rendered* into the HTML version you see on the right. This is the basic model for Quarto publishing—take a source document (in this case a notebook) and render it to a variety of [output formats](https://quarto.org/docs/output-formats/all-formats.html), including HTML, PDF, MS Word, etc.

**Note:** Note that while this tutorial uses Python, using Julia (via the [`IJulia`](https://github.com/JuliaLang/IJulia.jl) kernel) is also well supported. See the article on [Using Julia](https://quarto.org/docs/computations/julia.html) for additional details.

### Rendering

We’ll start out by opening a notebook (`hello.ipynb`) in Jupyter Lab and rendering it to a couple of formats. If you want to follow along step-by-step in your own environment, download the notebook below.

[Download hello.ipynb](https://quarto.org/docs/get-started/hello/jupyter/hello.ipynb)

Then, create a new directory to work within, copy the notebook into this directory, and switch to this directory in a Terminal.

Next, execute these commands to install JupyterLab along with the packages used in the tutorial (`matplotlib` and `plotly`), and to open the tutorial notebook:

| Platform   | Commands                                                                       |
| :--------- | :----------------------------------------------------------------------------- |
| Mac/Linux  | `python3 -m pip install jupyter jupyterlab`<br>`python3 -m pip install matplotlib plotly`<br>`python3 -m jupyter lab hello.ipynb` |
| Windows    | `py -m pip install jupyter jupyterlab`<br>`py -m pip install matplotlib plotly`<br>`py -m jupyter lab hello.ipynb` |

Here is our notebook in Jupyter Lab.

![Hello Notebook in Jupyter Lab](https://quarto.org/docs/get-started/images/jupyterlab-notebook.png)

The notebook source:
```python
# %% [markdown]
# ---
# title: "Quarto Basics"
# format:
#   html:
#     code-fold: true
# jupyter: python3
# ---

# %% [markdown]
# ## Polar Axis
#
# For a demonstration of a line plot on a polar axis, see @fig-polar.

# %%
#| label: fig-polar
#| fig-cap: "A line plot on a polar axis"

import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
fig, ax = plt.subplots(
  subplot_kw = {'projection': 'polar'}
)
ax.plot(theta, r);
ax.set_rticks([0.5, 1, 1.5, 2]);
ax.grid(True);

plt.show()
```

Next, create a new Terminal within Jupyter Lab to use for Quarto commands.

![Jupyter Lab Terminal](https://quarto.org/docs/get-started/images/jupyterlab-terminal.png)

And finally, render the notebook to a couple of formats.

```bash
quarto render hello.ipynb --to html
quarto render hello.ipynb --to docx
```

Note that the target file (in this case `hello.ipynb`) should always be the very first command line argument.

When you render a Jupyter notebook with Quarto, the contents of the notebook (code, markdown, and outputs) are converted to plain markdown and then processed by [Pandoc](https://pandoc.org), which creates the finished format.

### Authoring

The `quarto render` command is used to create the final version of your document for distribution. However, during authoring you’ll use the `quarto preview` command. Try it now from the Terminal with `hello.ipynb`.

```bash
quarto preview hello.ipynb
```

This will render your document and then display it in a web browser.

![Quarto Preview in Browser](https://quarto.org/docs/get-started/images/quarto-preview.png)

You might want to position Jupyter Lab and the browser preview side-by-side so you can see changes as you work.

To see live preview in action:

1.  Change the line of code that defines `theta` as follows:
    ```python
    theta = 4 * np.pi * r
    ```
2.  Re-run the code cell to generate a new version of the plot.
3.  Save the notebook (the preview will update automatically).

This is the basic workflow for authoring with Quarto. Once you are comfortable with this, we also recommend installing the [Quarto JupyterLab Extension](https://quarto.org/docs/tools/jupyter-lab-extension.html) which provides additional tools for working with Quarto in JupyterLab.

There are few different types of cells in our notebook, let’s work a bit with each type.

#### YAML Options

You are likely already familiar with markdown and code cells, but there is a new type of cell (“Raw”) that is used for document-level YAML options.

![Raw Cell for YAML](https://quarto.org/docs/get-started/images/jupyterlab-raw-cell.png)

```yaml
---
title: "Quarto Basics"
format:
  html:
    code-fold: true
jupyter: python3
---
```

Try changing the `code-fold` option to `false`.

```yaml
format:
  html:
    code-fold: false
```

Then save the notebook. You’ll notice that the code is now shown above the plot, where previously it was hidden with a `Code` button that could be used to show it.

#### Markdown Cells

Markdown cells contain raw markdown that will be passed through to Quarto during rendering. You can use any valid Quarto [markdown syntax](https://quarto.org/docs/authoring/markdown-basics.html) in these cells. Here we specify a heading and a cross-reference to the figure created in the code cell below.

![Markdown Cell](https://quarto.org/docs/get-started/images/jupyterlab-markdown-cell.png)

```markdown
