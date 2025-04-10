## Output Formats: Typst

Source: [Typst Basics – Quarto](https://quarto.org/docs/output-formats/typst.html)

### Overview

[Typst](https://typst.app/) is a new open-source markup-based typesetting system that is designed to be as powerful as LaTeX while being much easier to learn and use. Typst creates beautiful PDF output with blazing fast render times.

Use the `typst` format to create a PDF document via Typst. For example:

**hello-typst.qmd**
```yaml
---
title: "Hello Typst!"
format:
  typst:
    toc: true
    section-numbering: 1.1.a
    columns: 2
---
```

Rendering or previewing this document will invoke the Typst CLI to create `hello-typst.pdf`, a PDF file, from your markdown source file. Quarto includes the Typst CLI so no separate installation of Typst is required.

The above example highlights a few of the options available for Typst output. This document covers these and other options in detail. See the Typst [format reference](https://quarto.org/docs/reference/formats/typst.html) for a complete list of all available options.

One of the highlights of Typst is the ease of creating highly customized templates. For example, here are some Typst templates that you can use in Quarto as custom formats:

*   [IEEE](https://github.com/quarto-ext/typst-templates/tree/main/_extensions/ieee)
*   [Poster](https://github.com/quarto-ext/typst-templates/tree/main/_extensions/poster)
*   [Letter](https://github.com/quarto-ext/typst-templates/tree/main/_extensions/letter)
*   [Dept News](https://github.com/quarto-ext/typst-templates/tree/main/_extensions/dept-news)

Learn more about how to use them, and how to create your own in [Custom Formats](https://quarto.org/docs/output-formats/typst-custom.html).

### Known Limitations

Since Typst is under active development, there are still some limitations to Quarto’s Typst support:

*   The default size of images may not reflect the behavior you are used to in other output formats. This is a problem that Typst, pandoc and Quarto are actively working to fix. In the meantime, you can manually [specify image widths](https://quarto.org/docs/authoring/figures.html#figure-sizing).
*   Advanced page layout (e.g. using the `.column` classes as explained in [Article Layout](https://quarto.org/docs/authoring/article-layout.html)) is not implemented.
*   Various other small things might not yet be implemented. Please [let us know](https://github.com/quarto-dev/quarto-cli/issues/new/choose) if you see things that could use improvement!

### Page Layout

You can control the size of the page (`papersize`), the page margins (`margin`), and the number of columns used for page content (`columns`). For example, the following YAML modifies all three options:

```yaml
---
title: Page Layout
format:
  typst:
    papersize: a5
    margin:
      x: 1cm
      y: 1cm
    columns: 2
---
```

The resulting layout is shown below alongside an example of the default layout:

*   **Customized Layout:** ![Custom Typst Layout](https://quarto.org/docs/output-formats/images/typst-custom-layout.png)
*   **Default Layout:** ![Default Typst Layout](https://quarto.org/docs/output-formats/images/typst-default-layout.png)

You can read more about these page layout options in the sections below.

#### Paper Size

The `papersize` option expects a string matching one of Typst’s supported [paper sizes](https://typst.app/docs/reference/layout/page/#parameters-paper). The default template is equivalent to:

```yaml
papersize: us-letter
```

#### Margins

The `margin` option expects one or more of the suboptions: `x`, `y`, `top`, `bottom`, `left` and `right`. The default template uses margins equivalent to:

```yaml
margin:
  x: 1.25in
  y: 1.25in
```

This sets the margins in the horizontal direction (`x`), i.e. `left` and `right`, as well as the margins in the vertical direction (`y`), i.e. `top` and `bottom` to 1.25 inches.

The values for the margins are specified using Typst’s [`length`](https://typst.app/docs/reference/layout/length/), (e.g. `5cm`) or [`relative length`](https://typst.app/docs/reference/layout/relative-length/) (e.g. `10%`) types. You can specify a single margin:

```yaml
margin:
  left: 1cm
```

Then, any unspecified margins will inherit from the default margins.

#### Columns

The `columns` option expects a number - the number of columns your body content should have. The default template sets `columns` to `1`.

### Table of Contents

Use the `toc` option to include an automatically generated table of contents in the output document. Use the `toc-depth` option to specify the number of section levels to include in the table of contents. The default is 3 (which means that level-1, 2, and 3 headings will be listed in the contents). For example:

```yaml
toc: true
toc-depth: 2
```

You can customize the title used for the table of contents using the `toc-title` option:

```yaml
toc-title: Contents
```

If you want to exclude a heading from the table of contents, add both the `.unnumbered` and `.unlisted` classes to it:

```markdown
### More Options {.unnumbered .unlisted}
```

The `toc-indent` option controls how far entries are indented in the displayed table of contents. The default is equivalent to:

```yaml
toc-indent: 1.5em
```

### Section Numbering

Use the `number-sections` option to number section headings in the output document. For example:

```yaml
number-sections: true
```

Use the `number-depth` option to specify the deepest level of heading to add numbers to (by default all headings are numbered). For example:

```yaml
number-depth: 3
```

To exclude an individual heading from numbering, add the `.unnumbered` class to it:

```markdown
### More Options {.unnumbered}
```

You can also customize the display of the section numbers with the `section-numbering` YAML option. This option expects a string that describes the numbering schema. For example, the following schema describes numbering sections with numerals, subsection with uppercase letters, and subsubsections with lower case letters, using `.` as a separator:

```yaml
---
section-numbering: 1.A.a
---
```

You can read more about specifying the numbering schema in the [Typst documentation for numbering](https://typst.app/docs/reference/model/numbering/).

### Code Annotation

You can add annotations to lines of code in code blocks and executable code cells. See [Code Annotation](https://quarto.org/docs/authoring/code-annotation.html) for full details.

### Bibliography

Typst comes with its [own citation processing system for bibliographies](https://typst.app/docs/reference/bibliography/) and using `format: typst` defaults to it. To specify a bibliography style using Typst’s system, use the `bibliographystyle` option. Provide a string from [Typst’s list of built-in styles](https://typst.app/docs/reference/bibliography/bibliography/#parameters-style), e.g.:

```yaml
bibliography: refs.bib
bibliographystyle: apa
```

Or alternatively, provide a path to a local CSL file:

```yaml
bibliography: refs.bib
bibliographystyle: my-csl-style.csl
```

If you prefer to use Pandoc’s citation processing, set `citeproc: true` explicitly in YAML header:

```yaml
citeproc: true
bibliography: refs.bib
csl: https://www.zotero.org/styles/apa-with-abstract
```

To provide a citation style file to Pandoc’s citation processing system use the `csl` option, as described in [Citation Style](https://quarto.org/docs/authoring/citations.html#citation-style).

### Typst Blocks

If you want to change the appearance of blocks using native Typst `#block()` calls, you can add the `.block` class to a Div and provide whatever arguments are appropriate. For example:

```markdown
::: {.block fill="luma(230)" inset="8pt" radius="4pt"}
This is a block with gray background and slightly rounded corners.
:::
```

This gets compiled to

```typst
#block(fill:luma(230), inset:8pt, radius:4pt,
[This is a block with gray background and slightly rounded corners.])
```

### Raw Typst

If you want to use raw `typst` markup, use a raw `typst` block. For example:

````markdown
```{=typst}
#set par(justify: true)

== Background
In the case of glaciers, fluid dynamics principles can be used to understand how the movement and behavior of the ice is influenced by factors such as temperature, pressure, and the presence of other fluids (such as water).
```
````

To learn more about `typst` markup, see the tutorial here: <https://typst.app/docs/tutorial/>.

### Typst CSS

To allow similar styling between HTML and Typst, Quarto will translate CSS properties into Typst properties.

You can use CSS properties directly in your Quarto markup, and they will get translated to appropriate Typst elements and properties.

For example, text-related properties `color`, `opacity`, and `background-color` can be applied to spans:

```markdown
Here is a [span with a green background]{style="background-color:green"}.
```

`font-family` and `font-size` can be applied to a div or table:

```markdown
:::{style="font-family: helvetica"}
This div is rendered in Helvetica.
:::
```

See [the Advanced documentation](https://quarto.org/docs/reference/formats/typst-css.html) for supported elements and properties, and how to add more using Lua filters.

You are most likely to encounter Typst CSS when using libraries that produce HTML tables. The translation of the CSS means your table in Typst should look similar to how it looks in HTML without any intervention on your part.

For example, here is a temperature heatmap using `gt` in R, and `pandas` in Python.

**R - gt:**

````markdown
```{r}
library(gt)
temps <- data.frame(
  year = c(1920:1924),
  Jan = c(40.6, 44.2, 37.5, 41.8, 39.3),
  Jun = c(58.5, 58.7, 57.8, 52.7, 57.7)
)
temps |>
  gt() |>
  data_color(
    columns = c(-year),
    fn = scales::col_numeric(
      colorspace::diverge_hcl(n = 9,
        palette = "Green-Orange"),
      domain = c(35, 62))
  )
```
````

**Python - Pandas:**

````markdown
```{python}
import pandas as pd
import numpy as np

temps = pd.DataFrame({
  'year': [*range(1920, 1925)],
  'Jan': [40.6, 44.2, 37.5, 41.8, 39.3],
  'Jun': [58.5, 58.7, 57.8, 52.7, 57.7]
}).set_index('year')

def make_pretty(styler):
  styler.background_gradient(axis=None,
    vmin=31, vmax=66, cmap="RdYlGn_r")
  return styler

temps.style.pipe(make_pretty)
```
````

Note that [named Typst colors](https://typst.app/docs/reference/visualize/color/#named-colors) will be preferred over [named CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color). If you want exactly the same color in your HTML and Typst output, specify the color using `rgb()` or hexadecimal `#rrggbb` syntax.

Typst does not support opacity as a filter, so opacity is simulated using the alpha channel of the color.

### Typst File (`.typ`)

The rendering process produces a native Typst file (`.typ)` which is then compiled to PDF using the Typst CLI. This intermediate file is then automatically removed. If you want to preserve the `.typ` file, use the `keep-typ` option. For example:

```yaml
---
title: "My Document"
format:
  typst:
    keep-typ: true
---
```

You can compile a `.typ` file to PDF directly using the `quarto typst compile` command in a terminal. For example:

```bash
quarto typst compile article.typ
```

The `quarto typst` command uses the version of Typst built in to Quarto and supports all Typst CLI actions and flags. For example, to determine the version of Typst embedded in Quarto:

```bash
quarto typst --version
```

### Fonts Support

The main font used for the document can be specified with the `mainfont` YAML option. Typst will search by default in installed system fonts. You can set additional paths to search using `font-paths`. For example:

```yaml
---
title: "My Document"
format:
  typst:
    mainfont: "Agbalumo"
    font-paths: myfonts
---
```

This will search for a `*.ttf` or `*.otf` file matching the font name in the `./myfonts/` directory, in addition to searching in installed system fonts.

The `TYPST_FONT_PATHS` environment variable is also taken into account for compatibility with Typst configuration, but setting `font-paths` will take precedence over any path set in the `TYPST_FONT_PATHS` environment variable.

Set the base size of the font used in the document with `fontsize`. The size used in the default template is equivalent to:

```yaml
---
fontsize: 11pt
---
```

### Computation Figure Format

Typst has great support for SVG graphics, so `format: typst` defaults to `fig-format: svg`. This configuration means executable code cells that produce images will produce `.svg` output.

If you prefer to include raster graphics, set `fig-format` to another value, like for example:

```yaml
format:
  typst:
    fig-format: png
```

See other figure options on the [Typst reference page](https://quarto.org/docs/reference/formats/typst.html#figures).

### Includes

If you want to include additional content in your document from another file, you can use the `include-in-*` options:

| Option              | Description                                                                        |
| :------------------ | :--------------------------------------------------------------------------------- |
| `include-in-header` | Include contents of `file`, verbatim, at the end of the header.                    |
| `include-before-body`| Include contents of `file`, verbatim, at the beginning of the document body.       |
| `include-after-body` | Include contents of `file`, verbatim, at the end of the document body.             |

You can specify a single file or multiple files for each of these options directly, or use the `file:` subkey. To include raw content in the YAML header, use the `text` subkey. When using `text:`, add the `|` character after `text:` to indicate that the value is a multi-line string. If you omit `file:` or `text:`, Quarto assumes you are providing a file.

For example:

```yaml
format:
  typst:
    include-before-body:
      - text: |
          #show heading: set text(navy)
```

