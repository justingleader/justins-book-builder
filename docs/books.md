## Books

Source: [Creating a Book – Quarto](https://quarto.org/docs/books/index.html)

### Overview

Quarto Books are combinations of multiple documents (chapters) into a single manuscript. Books can be created in a variety of formats:

*   HTML
*   PDF
*   MS Word
*   EPUB
*   AsciiDoc

HTML books are actually just a special type of [Quarto Website](https://quarto.org/docs/websites/) and consequently support all of the same features as websites including full-text search. The most important difference is that HTML books use chapter numbers and therefore support [Cross References](https://quarto.org/docs/authoring/cross-references.html) between different chapters.

Here are some examples of books created with Quarto:

| Book                      | Source                                                              |
| :------------------------ | :------------------------------------------------------------------ |
| R for Data Science        | [Code](https://github.com/hadley/r4ds/)                             |
| Python for Data Analysis  | [Code](https://github.com/wesm/pydata-book/)                        |
| Visualization Curriculum | [Code](https://github.com/datavizs23/datavizs23.github.io)          |

Quarto books can be published to a wide variety of destinations including GitHub Pages, Netlify, RStudio Connect, or any other static hosting service or intranet web server. See the documentation on [Publishing Websites](https://quarto.org/docs/websites/publishing/) for additional details.

### Quick Start

Follow the Quick Start for your tool of choice to get a simple book up and running. After covering the basics, read on to learn about more advanced book features.

*   **VS Code:**
    1.  Execute the `Quarto: Create Project` command from the command-palette.
    2.  Select `Book Project`.
    3.  Select a parent directory and name the project directory.
    4.  VS Code opens the new project. Click the `Preview` button (👁️) to preview. Preview updates automatically on render.
*   **RStudio:**
    1.  Use the `New Project` command and select `Quarto Book`.
    2.  Provide a directory name and other options.
    3.  Click the `Render` button to preview. Preview updates automatically on render.
*   **Terminal:**
    1.  Use `quarto create project book mybook`.
    2.  Use `quarto preview mybook` to render and preview. Preview updates automatically on save.

### Workflow

#### Config File

A Quarto project file (`_quarto.yml`) is contained within the book project directory. This file contains the initial configuration for your book. For example:

```yaml
# _quarto.yml
project:
  type: book

book:
  title: "mybook"
  author: "Jane Doe"
  date: "8/18/2021"
  chapters:
    - index.qmd
    - intro.qmd
    - summary.qmd
    - references.qmd

bibliography: references.bib

format:
  html:
    theme: cosmo
  pdf:
    documentclass: scrreprt
  epub:
    cover-image: cover.png
```

See the [Project Basics](https://quarto.org/docs/projects/quarto-projects.html) article to learn more about working with projects, including how to add custom pre and post render scripts to your book.

#### Book Preview

If you are using VS Code or RStudio, the `Preview` button (VS Code), or `Render` button (RStudio), automatically renders and runs `quarto preview` in an embedded window. You can also do the same thing from the Terminal if need be:

```bash
# preview the book in the current directory
quarto preview
```

Note that when you preview a book (either using VS Code / RStudio integrated tools or from the terminal) changes to configuration files (e.g. `_quarto.yml`) as well as book resources (e.g. theme or CSS files) will cause an automatic refresh of the preview.

You can customize the behavior of the preview server (port, whether it opens a browser, etc.) using command line options or the `_quarto.yml` config file. See `quarto preview help` or the [project file reference](https://quarto.org/docs/reference/projects/options.html#preview) for additional details.

**Important:** As you preview your book, chapters will be rendered and updated. However, if you make changes to global options (e.g. `_quarto.yml` or included files) you need to fully re-render your book to have all of the changes reflected. Consequently, you should always fully `quarto render` your site before deploying it, even if you have already previewed changes to some pages with the preview server.

For AsciiDoc Books we recommend using the HTML format to preview your book, read more in [AsciiDoc Books](#asciidoc-books).

#### Publishing

When you are ready to publish the book, use the `render` command to render all output formats:

```bash
quarto render
```

If you pass no arguments to `quarto render`, all formats will be rendered. You can also render individual formats via the `--to` argument:

```bash
quarto render            # render all formats
quarto render --to pdf   # render PDF format only
```

The output of your book will be written to the `_book` sub-directory of your book project:

```
mybook/
  _book/
    index.html     # and other book files
    mybook.pdf
    mybook.epub
```

See the documentation on [Publishing Websites](https://quarto.org/docs/websites/publishing/) for details on how to publish books to GitHub Pages, Netlify, and other services. Note that in that documentation the `output-dir` may be referred to as `_site`: for publishing books you should use `_book` rather than `_site`.

#### AsciiDoc Books

For AsciiDoc books, we recommend that while you are working on your book, you preview your content using Quarto’s built in HTML format, which allows an iterative workflow using the preview capabilities of Quarto. Once you’re ready to produce AsciiDoc, you can use the AsciiDoctor tools to compile your book to PDF or HTML output to preview the content in its final rendered form.

##### Previewing PDF with Asciidoctor-pdf

Creating a PDF preview with the AsciiDoc toolchain is a useful way to verify that the AsciiDoc output of your book can be rendered properly. To do this, follow these instructions:

1.  First, install Asciidoctor PDF by following the instructions here: <https://docs.asciidoctor.org/pdf-converter/latest/install/>
2.  From the terminal in the root of your project, use the following command to compile your AsciiDoc book to a PDF:

    ```bash
    asciidoctor-pdf _book/book-asciidoc/<title>.adoc
    ```

The PDF will be placed at `_book/book-asciidoc/<title>.pdf`.

##### Previewing HTML with Asciidoctor

Creating an HTML preview with the AsciiDoc toolchain is a useful way to verify that the AsciiDoc output of your book can be rendered properly. To do this, follow these instructions:

1.  First, install Asciidoctor by following the instructions here: <https://docs.asciidoctor.org/asciidoctor/latest/install/>
2.  From the terminal in the root of your project, use the following command to compile your AsciiDoc book to HTML:

    ```bash
    asciidoctor _book/book-asciidoc/<title>.adoc
    ```

A single HTML file (with the entire contents of the book) will be placed at `_book/book-asciidoc/<title>.html`. The HTML file will contain references to files and images in the `_book/book-asciidoc/` folder, so the HTML will not display these properly if it is moved without also moving those folders.

### Learning More

Once you’ve got the basic book template up and running check out these articles for various ways to enhance your book:

*   [Book Structure](https://quarto.org/docs/books/book-structure.html) delves into different ways to structure a book (numbered and unnumbered chapters/sections, creating multiple parts, adding appendices, etc.)
*   [Book Crossrefs](https://quarto.org/docs/books/book-crossrefs.html) explains how to create cross references to sections, figures, tables, equations and more within books.
*   [Book Output](https://quarto.org/docs/books/book-output.html) covers customizing the style and appearance of your book in the various output formats as well as how to provide navigation and other tools for readers.
*   [Book Options](https://quarto.org/docs/reference/projects/books.html) provides a comprehensive reference to all of the available book options.
*   [Code Execution](https://quarto.org/docs/projects/code-execution.html) provides tips for optimizing the rendering of books with large numbers of documents or expensive computations.
*   [Publishing Websites](https://quarto.org/docs/websites/publishing/) enumerates the various options for publishing your book as a website including GitHub Pages, Netlify, and RStudio Connect.

