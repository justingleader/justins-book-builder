## Heading 2
```
:::
```

For the Jupyter engine, you can also create raw markdown output using the functions in `IPython.display`. For example:

````markdown
```{python}
#| echo: false
radius = 10
from IPython.display import Markdown
Markdown(f"The _radius_ of the circle is **{radius}**.")
```
````

### Knitr Options

If you are using the Knitr cell execution engine, you can specify default document-level [Knitr chunk options](https://yihui.org/knitr/options/#chunk_options) in YAML. For example:

```yaml
---
title: "My Document"
format: html
knitr:
  opts_chunk:
    collapse: true
    comment: "#>"
  R.options:
    knitr.graphics.auto_pdf: true
---
```

You can additionally specify global Knitr options using [`opts_knit`](https://yihui.org/knitr/options/#global_options).

The `R.options` chunk option is a convenient way to define R options that are set temporarily via `options()` before the code chunk execution, and immediately restored afterwards.

In the example above, we establish default Knitr chunk options for a single document. You can also add shared `knitr` options to a project-wide `_quarto.yml` file or a project-directory scoped `_metadata.yml` file.

### Jupyter Options

#### Expression Printing

When multiple expressions are present in a code cell, by default, only the last top-level expression is captured in the rendered output. For example, consider the code cell:

````markdown
```{python}
"first"
"last"
```
````

When rendered to HTML the output generated is:

```
'last'
```

This behavior corresponds to the `last_expr` setting for [Jupyter shell interactivity](https://ipython.readthedocs.io/en/stable/config/options/terminal.html#configtrait-InteractiveShell.ast_node_interactivity).

You can control this behavior with the `ipynb-shell-interactivity` option. For example, to capture all top-level expressions set it to `all`:

```yaml
---
title: All expressions
format: html
ipynb-shell-interactivity: all
---
```

Now the above code cell results in the output:

```
'first'
'last'
```

**All Expressions are Printed in Dashboards:** For [dashboards](https://quarto.org/docs/dashboards/) the default setting of `ipynb-shell-interactivity` is `all`.

### Intermediates

On the way from markdown input to final output, there are some intermediate files that are created and automatically deleted at the end of rendering. You can use the following options to keep these intermediate files:

| Option      | Description                                                                |
| :---------- | :------------------------------------------------------------------------- |
| `keep-md`   | Keep the markdown file generated by executing code.                        |
| `keep-ipynb`| Keep the notebook file generated from executing code (applicable only to markdown input files) |

For example, here we specify that we want to keep the jupyter intermediate file after rendering:

```yaml
---
title: "My Document"
execute:
  keep-ipynb: true
jupyter: python3
---
```

### Fenced Echo

If you are writing a tutorial or documentation on using Quarto code blocks, you’ll likely want to include the fenced code delimiter (e.g. `````{python}`````) in your code output to emphasize that executable code requires that delimiter. You can do this using the `echo: fenced` option. For example, the following code block:

````markdown
```{python}
#| echo: fenced
1 + 1
```
````

Will be rendered as:

````markdown
```{python}
1 + 1
```
````

```
2
```

This is especially useful when you want to demonstrate the use of cell options. For example, here we demonstrate the use of the `output` and `code-overflow` options:

````markdown
```{python}
#| echo: fenced
#| output: false
#| code-overflow: wrap
1 + 1
```
````

This code block appears in the rendered document as:

````markdown
```{python}
#| output: false
#| code-overflow: wrap
1 + 1
```
````

Note that all YAML options will be included in the fenced code output *except for* `echo: fenced` (as that might be confusing to readers).

This behavior can also be specified at the document level if you want all of your executable code blocks to include the fenced delimiter and YAML options:

```yaml
---
title: "My Document"
format: html
execute:
  echo: fenced
---
```

### Unexecuted Blocks

Often you’ll want to include a fenced code block purely as documentation (not executable). You can do this by using two curly braces around the language (e.g. `python`, `r`, etc.) rather than one. For example:

````markdown
```{{python}}
1 + 1
```
````

Will be output into the document as:

````markdown
```{python}
1 + 1
```
````

If you want to show an example with multiple code blocks and other markdown, just enclose the entire example in 4 backticks (e.g. ````) and use the two curly brace syntax for code blocks within. For example:

````markdown
````
---
title: "My document"
---

Some markdown content.

```{{python}}
1 + 1
```

Some additional markdown content.
````
````

### Engine Binding

Earlier we said that the engine used for computations was determined automatically. You may want to customize this—for example you may want to use the Jupyter `R kernel` rather than Knitr, or you may want to use Knitr with Python code (via `reticulate`).

Here are the basic rules for automatic binding:

| Extension | Engine Binding                                                                                                                                                                                                                          |
| :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.qmd`    | Use Knitr engine if an `{r}` code block is discovered within the file<br>Use Jupyter engine if *any other* executable code block (e.g. `{python}`, `{julia}`, `{bash}`, etc.) is discovered within the file. The kernel used is determined based on the language of the first executable code block discovered.<br>Use no engine if no executable code blocks are discovered. |
| `.ipynb`  | Jupyter engine                                                                                                                                                                                                                          |
| `.Rmd`    | Knitr engine                                                                                                                                                                                                                            |
| `.md`     | No engine (note that if an `md` document does contain executable code blocks then an error will occur)                                                                                                                                    |

**Using python and r together:** If your quarto document includes both `{python}` and `{r}` code blocks, then quarto will automatically use Knitr engine and `reticulate` R package to execute the python content.

For `.qmd` files in particular, you can override the engine used via the `engine` option. For example:

```yaml
engine: jupyter
```

```yaml
engine: knitr
```

You can also specify that no execution engine should be used via `engine: markdown`.

The presence of the `knitr` or `jupyter` option will also override the default engine:

```yaml
knitr: true
```

```yaml
jupyter: python3
```

Variations with additional engine-specific options also work to override the default engine:

```yaml
knitr:
  opts_knit:
    verbose: true
```

```yaml
jupyter:
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
```

### Shell Commands

Using shell commands (from Bash, Zsh, etc.) within Quarto computational documents differs by engine. If you are using the Jupyter engine you can use [Jupyter shell magics](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-system). For example:

```yaml
---
title: "Using Bash"
engine: jupyter
---
```

````markdown
```{python}
!echo "foo"
```
````

Note that `!` preceding `echo` is what enables a Python cell to be able to execute a shell command.

If you are using the Knitr engine you can use `````{bash}````` cells, for example:

```yaml
---
title: "Using Bash"
engine: knitr
---
```

````markdown
```{bash}
echo "foo"
```
````

Note that the Knitr engine also supports `````{python}````` cells, enabling the combination of R, Python, and Bash in the same document.

