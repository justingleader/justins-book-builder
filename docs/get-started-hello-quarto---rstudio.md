## Get Started: Hello, Quarto - RStudio

Source: [Tutorial: Hello, Quarto – Quarto](https://quarto.org/docs/get-started/hello/rstudio.html) (Content largely duplicated from Tools: RStudio IDE section, tailored for beginners)

### Overview

Quarto is a multi-language, [next-generation](https://quarto.org/docs/faq/rmarkdown.html) version of R Markdown from Posit and includes dozens of new features and capabilities while at the same being able to render most existing Rmd files without modification.

In this tutorial, we’ll show you how to use RStudio with Quarto. You’ll edit code and markdown in RStudio just as you would with any computational document (e.g., R Markdown) and preview the rendered document in the Viewer tab as you work.

The following is a Quarto document with the extension `.qmd` (on the left), along with its rendered version as HTML (on the right). You could also choose to render it into other formats like PDF, MS Word, etc.

![Quarto Document in RStudio](https://quarto.org/docs/get-started/images/rstudio-hello.png)

This is the basic model for Quarto publishing—take a source document and render it to a variety of output formats.

If you would like a video introduction to Quarto before you dive into the tutorial, watch the [Get Started with Quarto](https://www.youtube.com/watch?v=yvi4lNcWEzE) where you can see a preview of authoring a Quarto document with executable code chunks, rendering to multiple formats, including revealjs presentations, creating a website, and publishing on QuartoPub.

If you would like to follow along with this tutorial in your own environment, follow the steps outlined below.

1.  Download and install the latest release of RStudio:
    [Download RStudio](https://posit.co/download/rstudio-desktop/)
2.  Be sure that you have installed the `tidyverse` and `palmerpenguins` packages:
    ```r
    install.packages("tidyverse")
    install.packages("palmerpenguins")
    ```
3.  Download the Quarto document (`.qmd`) below, open it in RStudio, and click on Render.
    [Download hello.qmd](https://quarto.org/docs/get-started/hello/rstudio/hello.qmd)

### Rendering

Use the `Render` button in the RStudio IDE to render the file and preview the output with a single click or keyboard shortcut (<kbd>⇧</kbd>+<kbd>⌘</kbd>+<kbd>K</kbd>).

![RStudio Render Button](https://quarto.org/docs/get-started/images/rstudio-render-button.png)

If you prefer to automatically render whenever you save, you can check the Render on Save option on the editor toolbar. The preview will update whenever you re-render the document. Side-by-side preview works for both HTML and PDF outputs.

Note that documents can also be rendered from the R console via the `quarto` R package:

```r
# install.packages("quarto") # if needed
quarto::quarto_render("hello.qmd")
```

When rendering, Quarto generates a new file that contains selected text, code, and results from the .qmd file. The new file can be an [HTML](https://quarto.org/docs/output-formats/html-basics.html), [PDF](https://quarto.org/docs/output-formats/pdf-basics.html), [MS Word](https://quarto.org/docs/output-formats/ms-word.html) document, [presentation](https://quarto.org/docs/presentations/), [website](https://quarto.org/docs/websites/), [book](https://quarto.org/docs/books/), [interactive document](https://quarto.org/docs/interactive/), or [other format](https://quarto.org/docs/output-formats/all-formats.html).

### Authoring

In the image below, we can see the same document in the two modes of the RStudio editor: visual (on the left) and source (on the right). RStudio’s [visual editor](https://quarto.org/docs/tools/visual-editor.html) offers a [WYSIWYM](https://en.wikipedia.org/wiki/WYSIWYM) authoring experience for markdown. For formatting (e.g., bolding text), you can use the toolbar, a keyboard shortcut (<kbd>⌘</kbd>+<kbd>B</kbd>), or the markdown construct (`**bold**`). The plain text source code underlying the document is written for you, and you can view/edit it at any point by switching to source mode for editing. You can toggle back and forth between these two modes by clicking on `Source` and `Visual` in the editor toolbar (or using the keyboard shortcut <kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>F4</kbd>).

![RStudio Visual and Source Editor Modes](https://quarto.org/docs/get-started/images/rstudio-visual-source.png)

Next, let’s turn our attention to the contents of our Quarto document. The file contains three types of content: a YAML header, code chunks, and markdown text.

#### YAML header

An (optional) YAML header demarcated by three dashes (`---`) on either end.

```yaml
---
title: "Hello, Quarto"
format: html
editor: visual
---
```

When rendered, the `title`, `"Hello, Quarto"`, will appear at the top of the rendered document with a larger font size than the rest of the document. The other two YAML fields denote that the output should be in `html` format and the document should open in the `visual` editor by default.

The basic syntax of YAML uses key-value pairs in the format `key: value`. Other YAML fields commonly found in headers of documents include metadata like `author`, `subtitle`, `date` as well as customization options like `theme`, `fontcolor`, `fig-width`, etc. You can find out about all available YAML fields for HTML documents [here](https://quarto.org/docs/reference/formats/html.html). The available YAML fields vary based on document format, e.g., see [here](https://quarto.org/docs/reference/formats/pdf.html) for YAML fields for PDF documents and [here](https://quarto.org/docs/reference/formats/docx.html) for MS Word.

#### Code chunks

R code chunks identified with `{r}` with (optional) chunk options, in YAML style, identified by `#|` at the beginning of the line.

````markdown
```{r}
#| label: load-packages
#| include: false

library(tidyverse)
library(palmerpenguins)
```
````

In this case, the `label` of the code chunk is `load-packages`, and we set `include` to `false` to indicate that we don’t want the chunk itself or any of its outputs in the rendered documents.

In addition to rendering the complete document to view the results of code chunks, you can also run each code chunk interactively in the RStudio editor by clicking the `Run` icon (►) or keyboard shortcut (<kbd>⇧</kbd>+<kbd>⌘</kbd>+<kbd>⏎</kbd>). RStudio executes the code and displays the results either inline within your file or in the Console, depending on your preference.

#### Markdown text

Text with formatting, including section headings, hyperlinks, an embedded image, and an inline code chunk.

```markdown
