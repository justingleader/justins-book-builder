## Air Quality

@fig-airquality further explores the impact of temperature on ozone level.

```{r}
#| label: fig-airquality
#| fig-cap: "Temperature and ozone level."
#| warning: false

library(ggplot2)
ggplot(airquality, aes(Temp, Ozone)) +
  geom_point() +
  geom_smooth(method = "loess")
```
````

You’ll note that there are some special comments at the top of the code block. These are cell level options that make the figure [cross-referenceable](https://quarto.org/docs/authoring/cross-references.html).

This document results in the following rendered output:

![Rendered R Plot](https://quarto.org/docs/computations/images/r-ggplot2-output.png)

You can produce a wide variety of output types from executable code blocks, including plots, tabular output from data frames, and plain text output (e.g. printing the results of statistical summaries).

There are many options which control the behavior of code execution and output, you can read more about them in the article on [Execution Options](https://quarto.org/docs/computations/execution-options.html).

In addition to code blocks which interrupt the flow of markdown, you can also include code inline. Read more about inline code in the [Inline Code](https://quarto.org/docs/computations/inline-code.html) article.

### Rendering

When a Quarto document is rendered, R code blocks are automatically executed. You can render Quarto documents in a variety of ways:

*   Using the `Render` button in RStudio:
    ![RStudio Render Button](https://quarto.org/docs/computations/images/r-render-button.png)
    The `Render` button will render the first format listed in the document YAML. If no format is specified, then it will render to HTML.
*   From the system shell using the `quarto render` command:
    ```bash
    quarto render document.qmd # all formats
    quarto render document.qmd --to pdf
    quarto render document.qmd --to docx
    ```
    Note that the target file (in this case `document.qmd`) should always be the very first command line argument.
    The `render` command will render all formats listed in the document YAML. If no formats are specified, then it will render to HTML. You can also provide the `--to` argument to target a specific format.
*   From the R console using the `quarto` R package:
    ```r
    # install.packages("quarto") # if needed
    library(quarto)
    quarto_render("document.qmd") # all formats
    quarto_render("document.qmd", output_format = "pdf")
    ```
    The function `quarto_render()` is a wrapper around `quarto render` and by default, will render all formats listed in the document YAML.
    Note that the Quarto R package is a convenience for command line rendering from R, and is not required for using Quarto with R.

### Installation

To use Quarto with R, you should install the `rmarkdown` R package:

```r
install.packages("rmarkdown")
```

Installation of the `rmarkdown` package will also install the `knitr` package so you will have everything required to render documents containing R code.

Quarto will select a version of R by looking on the system `PATH`. In addition, on Windows when R is not found on the `PATH`, the registry will be scanned for the current R version. You can override the version of R used by Quarto by setting the `QUARTO_R` environment variable to the directory where the R binary `RScript` is.

### RStudio

RStudio v2022.07 and later includes support for editing and preview of Quarto documents (the documentation below assumes you are using this build or a later version).

If you are using Quarto within RStudio it is **strongly** recommended that you use the [latest release](https://posit.co/download/rstudio-desktop/) of RStudio.

You can download RStudio from <https://posit.co/download/rstudio-desktop/>.

#### Creating Documents

Use the `File : New File : Quarto Document…` command to create new Quarto documents:

![RStudio New Document Dialog](https://quarto.org/docs/tools/images/rstudio-new-document.png)

#### Render and Preview

Use the `Render` button to preview documents as you edit them:

![RStudio Render Button](https://quarto.org/docs/computations/images/r-render-button.png)

If you prefer to automatically render whenever you save you can check the `Render on Save` option on the editor toolbar.

The preview will appear alongside the editor:

![RStudio Preview](https://quarto.org/docs/tools/images/rstudio-preview.png)

The preview will update whenever you re-render the document. Side-by-side preview works for both HTML and PDF output.

#### Projects

If you want to create a new project for a Quarto document or set of documents, use the `File : New Project…` command, specify `New Directory`, then choose `Quarto Project`:

![RStudio New Project Dialog](https://quarto.org/docs/tools/images/rstudio-new-project.png)

You can use this UI to create both vanilla projects as well as [websites](https://quarto.org/docs/websites/) and [books](https://quarto.org/docs/books/). Options are also provided for creating a `git` repository and initializing an `renv` environment for the project.

### VS Code

The [Quarto Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) for VS Code provides a variety of tools for working with `.qmd` files in VS Code. The extension integrates directly with the [R Extension](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r) to provide the following R-specific capabilities:

*   Code completion
*   Cell execution
*   Contextual help

You can install the VS Code extension by searching for ‘quarto’ in the extensions panel or from the [extension marketplace](https://marketplace.visualstudio.com/items?itemName=quarto.quarto).

The VS Code extension includes a `Quarto: Preview` command that can be accessed via the Command Palette, the keyboard shortcut <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>K</kbd>, or a `Preview` button (👁️) in the editor. After rendering, a preview is displayed in a pane within VS Code alongside your document.

You can read more about using VS Code in [Tools: VS Code](https://quarto.org/docs/tools/vscode.html).

### Emacs

The [`quarto-mode`](https://github.com/quarto-dev/quarto-emacs) MELPA package is an Emacs mode for editing Quarto documents. Install `quarto-mode` as follows:

```emacs-lisp
M-x package-refresh-contents
M-x package-install quarto-mode
```

If you have [`ESS`](https://ess.r-project.org/), `quarto-mode` will make use of it for executing R code.

Use `M-x quarto-preview` to start a `quarto preview` server that watches quarto content for changes and automatically refreshes it. If the current buffer has an associated file that exists in a quarto project, the command will preview the entire project. Otherwise, it will preview the specific file.

### Chunk Options {#chunk-options-r}

One important difference between R Markdown documents and Quarto documents is that in Quarto chunk options are typically included in special comments at the top of code chunks rather than within the line that begins the chunk. For example:

````markdown
```{r}
#| echo: false
#| fig-cap: "Air Quality"

library(ggplot2)
ggplot(airquality, aes(Temp, Ozone)) +
  geom_point() +
  geom_smooth(method = "loess", se = FALSE)
```
````

Quarto uses this approach to both better accommodate longer options like `fig-cap`, `fig-subcap`, and `fig-alt` as well as to make it straightforward to edit chunk options within more structured editors that don’t have an easy way to edit chunk metadata (e.g. most traditional notebook UIs).

**Note:** Note that if you prefer it is still possible to include chunk options on the first line (e.g. ``` ``{r, echo = FALSE}`` ```). That said, we recommend using the comment-based syntax to make documents more portable and consistent across execution engines.

Chunk options included this way use YAML syntax rather than R syntax for consistency with options provided in YAML front matter. You can still however use R code for option values by prefacing them with `!expr`. For example:

```yaml
#| fig-cap: !expr 'paste("Air", "Quality")'
```

**Caution:** the `!expr` syntax is an example of a YAML “tag” literal, and it can be unintuitive. `!expr` needs to be followed by a *single YAML “flow scalar”*: see the [YAML spec](https://yaml.org/spec/1.2.2/#733-flow-scalar-styles) for details on how double-quoted, single-quoted, and unquoted strings work.

### Chunk Labels

You can set a label for a code chunk with the `label` option:

````markdown
```{r}
#| label: convert
airquality$TempC <- (5/9) * (airquality$Temp - 32)
```
````

Unless you want to specify a cross-reference avoid using the [reserved cross-reference prefixes](https://quarto.org/docs/authoring/cross-references.html#reserved-prefixes) for chunk labels.

### Output Formats {#output-formats-r}

Another difference between R Markdown and Quarto is related to output formats. Quarto includes many more built in output formats (and many more options for customizing each format). Quarto also has native features for special project types like [Websites](https://quarto.org/docs/websites/), [Books](https://quarto.org/docs/books/), and [Blogs](https://quarto.org/docs/websites/website-blog.html) (rather than relying on external packages).

To use a format in Quarto you use the `format` key rather than the `output` key as you did in R Markdown. Here’s a comparison of equivalent format specifications:

**R Markdown:**
```yaml
title: "My Document"
output:
  html_document:
    toc: true
    number_sections: true
    css: styles.css
```

**Quarto:**
```yaml
title: "My Document"
format:
  html:
    toc: true
    number-sections: true
    css: styles.css
```

One source of the difference in syntax is that Quarto is more closely aligned with [Pandoc](https://pandoc.org/) format names and options (thus the use of `-` as a word separator rather than `_`).

See the listing of all [supported formats](https://quarto.org/docs/output-formats/all-formats.html) along with their user guides and reference pages for more details.

See the articles on creating [Websites](https://quarto.org/docs/websites/), [Books](https://quarto.org/docs/books/), and [Blogs](https://quarto.org/docs/websites/website-blog.html) for additional details on more advanced output formats.

### Data Frames

You can control how data frames are printed by default using the `df-print` document option. Available options include:

| Option    | Description                                                                                              |
| :-------- | :------------------------------------------------------------------------------------------------------- |
| `default` | Use the default S3 method for the data frame.                                                            |
| `kable`   | Markdown table using the [`knitr::kable()`](https://rdrr.io/cran/knitr/man/kable.html) function.             |
| `tibble`  | Plain text table using the [`tibble`](https://tibble.tidyverse.org/) package.                                |
| `paged`   | HTML table with paging for row and column overflow (implemented using [`rmarkdown::paged_table()`](https://pkgs.rstudio.com/rmarkdown/reference/paged_table.html)) |

For example, here we specify that we want `paged` printing for data frames:

```yaml
---
title: "Document"
format:
  html:
    df-print: paged
---
```

### Knitr Options {#knitr-options-r}

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

### Caching

The [Knitr Cache](https://yihui.org/knitr/options/#cache) operates at the level of individual cells rather than the entire document. While this can be very convenient, it also introduced some special requirements around managing the dependencies between cells.

You can enable the Knitr cache at the document or project level using standard YAML options:

```yaml
---
title: "My Document"
format: html
execute:
  cache: true
---
```

You can also enable caching on a per-cell basis (in this you would *not* set the document level option):

````markdown
```{r}
#| cache: true
summary(cars)
```
````

There are a variety of other cell-level options that affect Knitr caching behavior. You can learn about them in the Knitr [cell options](https://quarto.org/docs/reference/cells/cells-knitr.html#cache) reference. Another excellent resource is Yihui Xie’s article on [cache invalidation](https://yihui.org/knitr/demo/cache/).

#### Rendering

You can use `quarto render` command line options to control caching behavior without changing the document’s code. Use options to force the use of caching on all chunks, disable the use of caching on all chunks (even if it’s specified in options), or to force a refresh of the cache even if it has not been invalidated:

```bash
# use a cache (even if not enabled in options)
quarto render example.qmd --cache

# don't use a cache (even if enabled in options)
quarto render example.qmd --no-cache

# use a cache and force a refresh
quarto render example.qmd --cache-refresh
```

#### Alternatives

If you are using caching to mitigate long render-times, there are some alternatives you should consider alongside caching.

**Disabling Execution:** If you are working exclusively with prose / markdown, you may want to disable execution entirely. Do this by specifying the `enabled: false` execute option For example:

```yaml
---
title: "My Document"
format: html
execute:
  enabled: false
---
```

Note that if you are authoring using Jupyter `.ipynb` notebooks (as opposed to plain-text `.qmd` files) then this is already the default behavior: no execution occurs when you call `quarto render` (rather, execution occurs as you work within the notebook).

**Freezing Execution:** If you are working within a project and your main concern is the cumulative impact of rendering many documents at once, consider using the `freeze` option.

You can use the `freeze` option to denote that computational documents should never be re-rendered during a global project render, or alternatively only be re-rendered when their source file changes:

```yaml
execute:
  freeze: true   # never re-render during project render
```

```yaml
execute:
  freeze: auto   # re-render only when source changes
```

Note that `freeze` controls whether execution occurs during global project renders. If you do an incremental render of either a single document or a project sub-directory then code is always executed. For example:

```bash
# render single document (always executes code)
quarto render document.qmd

# render project subdirectory (always executes code)
quarto render articles
```

Learn more about using `freeze` with projects in the article on [managing project execution](https://quarto.org/docs/projects/code-execution.html#freeze).

