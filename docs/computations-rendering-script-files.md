## Computations: Rendering Script Files

Source: [Rendering Script Files – Quarto](https://quarto.org/docs/computations/render-scripts.html)

### Overview

Quarto supports rendering script files (e.g. `.py`, `.jl`, or `.r`) that are specially formatted as notebooks. The specific syntax for the format is different for the Jupyter and Knitr engines. The Jupyter engine can render Python, Julia, and R (using the [`IRkernel`](https://github.com/IRkernel/IRkernel)) scripts, whereas the Knitr engine only renders R scripts.

On this page you can learn the [syntax](#syntax) for Jupyter and Knitr notebook scripts, how to [Render and Preview](#render-and-preview) notebook scripts as well as using notebook [Scripts in Projects](#scripts-in-projects).

### Syntax

The syntax for delineating YAML, code and Markdown depends on whether you are rendering with the Jupyter or Knitr engine. For Python and Julia scripts use the Jupyter engine. For R scripts, you can use either the Jupyter or Knitr engine.

#### Jupyter

Script rendering for Jupyter makes use of the [percent format](https://jupytext.readthedocs.io/en/latest/formats.html#the-percent-format) that is supported by several other tools including Spyder, VS Code, PyCharm, and Jupytext.

In the percent format:

*   Markdown cells are delimited by `# %% [markdown]`, and can include content as single line comments (`#`) or multi-line strings (`"""`).
*   Code cells are delimited by `# %%`.

There are also Quarto-specific additions:

*   The script must start with a markdown cell that includes a YAML header block (including the usual `---` YAML delimiters).
*   You can add code cell options in the usual way with `#|` comments.

For example, here is a Python script that includes both markdown and code cells (you can click on the numbers on the right for further details):

**script.py**
```python
# %% [markdown]
# ---
# author: Norah Jones
# ---

# %%
#| echo: false
import pandas as pd
df = pd.read_csv("palmer-penguins.csv")

# %% [markdown]
"""
