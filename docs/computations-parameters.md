## Computations: Parameters

Source: [Parameters – Quarto](https://quarto.org/docs/computations/parameters.html)

### Overview

You may have a set of parameters that are used to create different variations of a document. For example:

*   Showing results for a specific geographic location.
*   Running a report that covers a specific time period.
*   Running a single analysis multiple times for different assumptions.

This article describes how to define and use computational parameters with Quarto.

### Definition

Adding parameter definitions to a document works differently depending on whether you are using the [Jupyter](https://quarto.org/docs/computations/python.html) or [Knitr](https://quarto.org/docs/computations/r.html) engine.

#### Jupyter

For Jupyter, Quarto uses the same syntax for defining parameters as [Papermill](https://papermill.readthedocs.io/en/latest/usage-parameterize.html). To parameterize a document, designate a cell with the tag `parameters` and provide appropriate default values:

````markdown
```{python}
#| tags: [parameters]

alpha = 0.1
ratio = 0.1
```
````

The parameters are available in the top level environment:

````markdown
```{python}
alpha
```
````

When the document is executed with a set of new parameters a cell is injected which overrides these defaults as appropriate.

#### Knitr

For Knitr, the standard Knitr `params` YAML option is used to define parameters. For example:

```yaml
---
params:
  alpha: 0.1
  ratio: 0.1
---
```

The parameters are available in the `params` list:

````markdown
```{r}
params$alpha
```
````

### Rendering

To render using different parameters you can pass them on the command line using the `-P` flag (this works for both `.ipynb` or `.qmd` files):

```bash
quarto render document.ipynb -P alpha:0.2 -P ratio:0.3
```

Alternatively you can create a YAML file that defines the parameter values you want to render with, then call quarto render with the `--execute-params` flag:

```bash
quarto render document.qmd --execute-params params.yml
```

