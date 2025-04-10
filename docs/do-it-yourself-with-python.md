## Do it yourself with Python

```python
{{< include _demo.py >}}
```

Copy the Python code above and run it.
````

Note that we use an underscore (`_`) prefix for the included files. You should always use an underscore prefix with included files so that they are automatically ignored (i.e. not treated as standalone files) by a `quarto render` of a project.

### Computations

You can also include files with computational cells. For example, here we include a `.qmd` that does some data preprocessing that we want shared across multiple documents:

```markdown
---
title: "My Document"
---

{{< include _data.qmd >}}

Use the data...
```

where the content would be

**_data.qmd**

````markdown
Load the `sp500` from [`great_tables`](https://posit-dev.github.io/great-tables/)

```{python}
import great_tables as gt
from great_tables.data import sp500

sp500.head()
```
````

A couple of important things to remember when using computational includes:

*   All computations still share a single engine (e.g. knitr or jupyter)
*   Computational includes work only in `.qmd` files (they don’t work in `.ipynb` notebook files)

Note that you can’t use the `include` shortcode within a computational code block itself - as the example above shows, the executable code block needs to be inside the included document.

