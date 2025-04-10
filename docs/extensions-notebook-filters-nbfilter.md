## Extensions: Notebook Filters (Nbfilter)

Source: [Notebook Filters – Quarto](https://quarto.org/docs/advanced/notebook-filters.html)

### Overview

If you are rendering existing Jupyter notebooks that were not created with Quarto in mind, you may wish to do some pre-processing on the notebook prior to its conversion to markdown. This can be accomplished by specifying one or more `ipynb-filters`. These filters are passed the [JSON representation](https://nbformat.readthedocs.io/en/latest/format_description.html) of the notebook on `stdin` and should write a transformed JSON representation to `stdout`.

**Note:** The purpose of notebook filters is to adapt existing `.ipynb` files for use with Quarto. Consequently, notebook filters are only run when the original input is an `.ipynb` file (they are not run for `.qmd` files).

### Example

For example, this notebook filter uses the `nbformat` package to read a notebook, prepend a comment to the source of each code cell, and then write it back to `stdout`:

```python
import sys
import nbformat

# read notebook from stdin
nb = nbformat.reads(sys.stdin.read(), as_version = 4)

# prepend a comment to the source of each cell
for index, cell in enumerate(nb.cells):
  if cell.cell_type == 'code':
     cell.source = "# comment\n" + cell.source

# write notebook to stdout
nbformat.write(nb, sys.stdout)
```

You can arrange for this filter to be run using the `ipynb-filters` option (specified at either the document or project level):

```yaml
---
ipynb-filters:
  - filter.py
---
```

Note that the current working directory for the filter will be set to the location of the input notebook.

