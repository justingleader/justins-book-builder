## Authoring Figures

Source: [Figures – Quarto](https://quarto.org/docs/authoring/figures.html)

### Overview

Quarto includes a number of features aimed at making it easier to work with figures and subfigures, as well as for laying out panels that contain multiple figures, tables, or other content.

### Figure Basics

In Pandoc markdown, a figure is created whenever a captioned image appears by-itself in a paragraph. For example:

```markdown
![Elephant](elephant.png)
```

This results in the following treatment for various output types:

*   **HTML:** ![HTML Figure](https://quarto.org/docs/authoring/images/figure-html.png)
*   **PDF:** ![PDF Figure](https://quarto.org/docs/authoring/images/figure-pdf.png)
*   **Word:** ![Word Figure](https://quarto.org/docs/authoring/images/figure-word.png)

Note that for LaTeX / PDF output figures are automatically numbered (you can arrange for figures to be numbered in other formats using [Cross References](https://quarto.org/docs/authoring/cross-references.html)).

### Figure Sizing

By default figures are displayed using their actual size (subject to the width constraints imposed by the page they are rendered within). You can change the display size by adding the `width` and `height` attributes to the figure. For example:

```markdown
![Elephant](elephant.png){width=300}
```

Note that if only `width` is specified then `height` is calculated automatically. If you need to modify the default behaviour just add an explicit `height` attribute.

The default units for `width` and `height` are pixels. You can also specify sizes using a percentage or a conventional measurement like inches or millimetres. For example:

```markdown
![Elephant](elephant.png){width=80%}
```

```markdown
![Elephant](elephant.png){width=4in}
```

### Linked Figures

When rendering with Quarto, you can enclose a figure within a link and it will still be treated within output as a captioned figure. For example:

```markdown
[![Elephant](elephant.png)](https://en.wikipedia.org/wiki/Elephant)
```

### Figure Alignment

Figures are center aligned by default. Add the `fig-align` attribute to the image to use a different alignment. For example:

```markdown
![Elephant](elephant.png){fig-align="left"}
```

Note that figure captions are left aligned to accommodate longer caption text (which looks odd when center aligned).

### Alt Text

You can add alternative text to a figure by adding the `fig-alt` attribute to the image. For example, the following Markdown…

```markdown
![](elephant.png){fig-alt="A drawing of an elephant."}
```

… will create the following HTML with the corresponding alt tag:

```html
<img src="elephant.png" alt="A drawing of an elephant.">
```

Note that the figure caption, title, and alt text can all be different. For example, the following code…

```markdown
![Elephant](elephant.png "Title: An elephant"){fig-alt="A drawing of an elephant."}
```

…produces this HTML:

```html
<img src="elephant.png" title="Title: An elephant" alt="A drawing of an elephant.">
```

To render the caption instead as alt text you can append a backslash to the line as detailed in [the Pandoc documentation](https://pandoc.org/MANUAL.html#images):

```markdown
![A drawing of an elephant.](elephant.png)\
```

### Multiformat Figures

You can write markdown that provides a distinct image file format depending on the target output format. To do this simply leave-off the extension, for example:

```markdown
![](elephant)
```

By default this will look for `elephant.png`, however if you are rendering to PDF it will look for `elephant.pdf`. You can customize this behavior using the `default-image-extension` option. For example:

```yaml
format:
  html:
    default-image-extension: svg
  pdf:
    default-image-extension: tex
```

### Lightbox Figures

In HTML output formats you can add lightbox styling and behavior to images to allow a reader to click to see a larger version of the image. For example, the following image has lightbox treatment (click on the image to see lightbox in action):

![An elephant](https://quarto.org/docs/authoring/elephant.png){#fig-lightbox width="20%"}

Lightbox treatment can be added by adding the class `.lightbox` to an image:

```markdown
![An elephant](elephant.png){.lightbox}
```

For further details and other ways to enable and disable lightbox treatment see [Lightbox Figures](https://quarto.org/docs/output-formats/html-lightbox-figures.html).

### Applying Multiple Parameters

To combine the above methods, separate arguments by a space, for example:

```markdown
![](elephant.png){fig-alt="A drawing of an elephant." fig-align="left" width=20%}
```

### Cross References

You can cross-reference figures by adding an ID with the `fig-` prefix to them, and then referencing the figure using the `@` prefix. For example:

```markdown
![An Elephant](elephant.png)
{#fig-elephant}

This is illustrated well by @fig-elephant.
```

For figures produced by executable code cells, include a `label` with a `fig-` prefix to make them cross-referenceable. For example:

````markdown
For a demonstration of a line plot, see @fig-line-plot.

```{python}
#| label: fig-line-plot
#| fig-cap: "A line plot "
import matplotlib.pyplot as plt
plt.plot([1,23,2,4])
plt.show()
```
````

**Label Prefix:** In order for a figure to be cross-referenceable, its label must start with the `fig-` prefix.

See the article on [Cross References](https://quarto.org/docs/authoring/cross-references.html) for additional details.

### Subfigures

If you have several figures that appear as a group, you can create a figure div to enclose them. For example:

```markdown
::: {#fig-elephants layout-ncol=2}
![Surus](surus.png)
{#fig-surus}

![Hanno](hanno.png)
{#fig-hanno}

Famous Elephants
:::
```

Again, the last paragraph provides the main caption, and the individual figures carry the sub-captions. Here is what this looks like when rendered as HTML:

![Subfigures Example](https://quarto.org/docs/authoring/images/subfigure-example.png)

Note that the empty lines between the figures (and between the last figure and the caption) are required (it’s what indicates that these images belong to their own paragraphs rather than being multiple images within the same paragraph).

Note also that we also used a `layout-ncol` attribute to specify a two-column layout. The next section delves more into customizing figure layouts.

### Figure Panels

Above we demonstrate laying out two side-by-side figures with subcaptions and a main caption. You may or may not want the caption / sub-caption treatment, and you might also want to use multiple rows of figures. All of these variations are possible.

To layout two figures with their own standalone captions (and no main caption), just eliminate the `#fig` identifiers and main caption at the bottom:

```markdown
::: {layout-ncol=2}
![Surus](surus.png)

![Hanno](hanno.png)
:::
```

You can also eliminate the captions entirely:

```markdown
::: {layout-ncol=2}
![](surus.png)

![](hanno.png)
:::
```

#### Multiple Rows

If you have more than 2 images, you might want to lay them out across multiple rows. You can do this using the `layout-nrow` attribute. For example:

```markdown
::: {layout-nrow=2}
![Surus](surus.png)

![Hanno](hanno.png)

![Abdul Abbas](abdul-abbas.png)

![Lin Wang](lin-wang.png)
:::
```

More complex figure arrangements (e.g. rows with varying column layouts) are possible. See the [Custom Layouts](#custom-layouts) section below for more details.

### Figure Divs

You can treat any markdown content you want as a figure by enclosing it in Pandoc div block with an identifier prefaced with `#fig-`. For example, here we create a figure that includes an embedded iframe:

```markdown
::: {#fig-elephant-video}
<iframe width="560" height="315" src="https://www.youtube.com/embed/SNggmeilXDQ"></iframe>

Elephant Video
:::
```

Note that the last paragraph in the div block is used as the figure caption.

### LaTeX Figures

This section describes some figure handling options that are specific to LaTeX output.

One very important thing to note is that using the `fig-env` and `fig-pos` options described below will trigger the creation of a LaTeX floating environment (most often `\begin{figure}`). Depending upon where this LaTeX is generated (e.g., within another `\begin{figure}`), this could produce invalid LaTeX. To be on the safe side, these attributes should typically only be used for images at the very top level of your document.

#### Environments

There are a number of LaTeX packages that provide custom figure environments. For example, in two-column formats, the `figure*` environment spans both columns of the document. You can explicitly pass the figure environment to use as the `fig-env` attribute of the image or the fenced div:

```markdown
![Elephant](surus.jpg)
{#fig-elephant fig-env="figure*"}
```

```markdown
::: {#fig-elephant-2 fig-env="figure*"}
![](surus.jpg)
Another elephant.
:::
```

#### Figure Position

The default LaTeX `figure` is a floating environment, so the specific location it appears in your document will depend on its size and the nature of the other content around it. You can exercise some control over this behavior using the `fig-pos` option. The `fig-pos` option provides a placement specifier for the `figure` environment. For example, the `ht` in this LaTeX snippet is the `fig-pos`:

```latex
\begin{figure}[ht]
\end{figure}
```

You can specify `fig-pos` either at the document level, as an executable code block option, or within markdown. Here we do all three:

```yaml
---
title: "My Document"
format:
  pdf:
    fig-pos: 'h'
---
```

````markdown
```{python}
#| fig-pos: 't'
```
````

```markdown
![](figure.png){fig-pos='b'}
```

See [this article](https://www.overleaf.com/learn/latex/Positioning_of_Figures) for additional details on LaTeX figure positioning.

#### Figures and Code Blocks

If your figure was generated by an executable code block and the code was included in the output (`echo: true`), then `fig-pos` will be set to `H` by default (to try to keep it alongside the code that generated it). In all other cases, default LaTeX handing of figure position is used unless you specify an explicit `fig-pos`.

#### Short Captions

You can provide a short caption that is used in the “List of Figures” using the `fig-scap` option. You can specify `fig-scap` as an executable code block option or as an attribute on an image:

````markdown
```{python}
#| fig-cap: "Long caption"
#| fig-scap: "Short caption"
```
````

```markdown
![Long Caption](figure.png){fig-scap='Short caption'}
```

#### PGF/TikZ Graphics

If you are creating LaTeX output, Quarto will automatically emit the correct LaTeX for markdown images that reference `.tex` files containg [PGF/TikZ](https://en.wikipedia.org/wiki/PGF/TikZ) vector graphics. For example, the following markdown images:

```markdown
![](image1.tex)

![](image2.tex){width=80%}
```

Will be written to LaTeX as:

```latex
\input{image1.tex}

\resizebox{0.8\linewidth}{!}{
\input{image2.tex}}
```

As shown above, `width` and `height` percentages are automatically converted to `\linewidth` scaled. Alternatively you can specify custom LaTeX for the `width` and `height` arguments of `\resizebox`.

### Caption Locations

By default, figure captions are positioned below figures. In HTML and PDF formats, you can modify this behavior using the `fig-cap-location` option. For example:

```yaml
---
fig-cap-location: top
---
```

Note that this option is specified at the top level so that it can be shared by both PDF and HTML formats. If you are only targeting a single format you can place it alongside other `format` specific options.

Valid values for the caption location include:

| Value    | Description                      |
| :------- | :------------------------------- |
| `top`    | Position the caption above the figure. |
| `bottom` | Position the caption below the figure. |
| `margin` | Position the caption in the margin.  |

See the article on [Article Layout](https://quarto.org/docs/authoring/article-layout.html#margin-captions) for additional details on placing captions in the margin.

### Custom Layouts {#custom-layouts}

The examples above used the `layout-ncol` or `layout-nrow` attributes to create straightforward layouts where all columns are of equal sizes. The `layout` attribute enables the creation of much more complex layouts.

For example, this defines a layout with two equally sized figures in the first row, then another image that spans the entire second row:

```markdown
::: {layout="[ [1,1], [1] ]"}
![Surus](surus.png)

![Hanno](hanno.png)

![Lin Wang](lin-wang.png)
:::
```

The `layout` attribute is a 2-dimensional array where the first dimension defines rows and the second columns. In this case `"layout="[[1,1], [1]]"` translates to: create two rows, the first of which has two columns of equal size and the second of which has a single column.

Note that the numbers in a row are arbitrary and don’t need to add up to a particular total. You can therefore use whatever scheme is most natural. For example, here we define columns that occupy varying percentage widths of the row:

```markdown
::: {layout="[ [70,30], [100] ]"}
![Surus](surus.png)

![Hanno](hanno.png)

![Lin Wang](lin-wang.png)
:::
```

You can also use negative values to create space between elements. For example:

```markdown
::: {layout="[ [40,-20,40], [100] ]"}
![Surus](surus.png)

![Hanno](hanno.png)

![Lin Wang](lin-wang.png)
:::
```

#### Vertical Alignment

If you have a layout with a row of images of differing heights, you can control their vertical alignment using the `layout-valign` attribute. A simple example:

```markdown
::: {layout="[15,-2,10]" layout-valign="bottom"}
![Surus](surus.png)

![Lin Wang](lin-wang.png)
:::
```

Note that vertical alignment isn’t limited to images, you can also vertically align any other elements that are included in a panel.

### Computations

Figures produced by executable code blocks are automatically included in your document. To set the ID, caption and link, use the chunk options `label`, `fig-cap` and `fig-link` respectively. Other attributes, e.g. `fig-align` and `fig-alt`, can be set using the chunk option of the same name.

You can control the default size for computational figures using the `fig-width` and `fig-height` options in the document header.

Read more about these options in [Execution Options: Figure Options](https://quarto.org/docs/computations/execution-options.html#figure-options).

#### Layout

Note that figure layout attributes also work for figures produced by executable code blocks. Here are examples for both Jupyter and Knitr:

**Jupyter:**

````markdown
```{python}
#| layout-ncol: 2
#| fig-cap:
#|   - "Line Plot 1"
#|   - "Line Plot 2"

import matplotlib.pyplot as plt
plt.plot([1,23,2,4])
plt.show()

plt.plot([8,65,23,90])
plt.show()
```
````

**Knitr:**

````markdown
```{r}
#| layout-ncol: 2
#| fig-cap:
#|   - "Speed and Stopping Distances of Cars"
#|   - "Vapor Pressure of Mercury as a Function of Temperature"

plot(cars)
plot(pressure)
```
````

Note that in these examples we also use the `fig-cap` option to apply a caption to each of the generated figures.

#### Subcaptions

You can create subcaptions for computational output by combining the `fig-cap` and `fig-subcap` options. When applying captions to computational output you can optionally include a `label` with a `fig-` prefix—if you do this then the figure will be numbered and [cross-referenceable](https://quarto.org/docs/authoring/cross-references.html).

**Jupyter:**

````markdown
```{python}
#| label: fig-charts
#| fig-cap: "Charts"
#| fig-subcap:
#|   - "First"
#|   - "Second"
#| layout-ncol: 2

import matplotlib.pyplot as plt
plt.plot([1,23,2,4])
plt.show()

plt.plot([8,65,23,90])
plt.show()
```
````

**Knitr:**

````markdown
```{r}
#| label: fig-charts
#| fig-cap: "Charts"
#| fig-subcap:
#|   - "Cars"
#|   - "Pressure"
#| layout-ncol: 2

plot(cars)
plot(pressure)
```
````

#### Custom Layout

The `layout` works the same way for figures produced by Knitr or Jupyter. For example, here’s an Rmd code chunk that produces 3 plots and defines a custom layout for them:

````markdown
```{r}
#| layout: [[45,-10, 45], [100]]
plot(cars)
plot(pressure)
plot(mtcars)
```
````

### Block Layout

While the examples above illustrate laying out figures, it’s important to note that layout attributes can be used to layout any sort of block content. For example, here we layout 2 lists side-by-side:

```markdown
::: {layout-ncol=2}
### List One
- Item A
- Item B
- Item C

### List Two
- Item X
- Item Y
- Item Z
:::
```

Note that headings are automatically combined with the block that follows them, so this markdown has a total of 2 columns to lay out. Here’s an example of a paragraph next to a bullet list (without headings):

```markdown
::: {layout-ncol=2}
- Item X
- Item Y
- Item Z

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur gravida eu erat et fring. Morbi congue augue vel eros ullamcorper, eget convallis tortor sagittis. Fusce sodales viverra mauris a fringilla. Donec feugiat, justo eu blandit placerat, enim dui volutpat turpis, eu dictum lectus urna eu urna. Mauris sed massa ornare, interdum ipsum a, semper massa.
:::
```

For more complicated content use divs (`:::`) to divide your content into blocks for the layout. For example, here’s how you could lay out a code cell along with some text, next to a figure:

````markdown
:::: {layout="[ 40, 60 ]"}
::: {#first-column}
```r
# Some code
```

Some text that should be laid out below the code
:::

::: {#second-column}
![](elephant.png)
:::
::::
````

The id attributes (`#first-column` and `#second-column`) are optional, but aid readability.

