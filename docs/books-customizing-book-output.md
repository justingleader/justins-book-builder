## Books: Customizing Book Output

Source: [Customizing Book Output – Quarto](https://quarto.org/docs/books/book-output.html)

This article covers customizing the output of book projects, including how to tailor the styles and appearance of books in each supported output format.

### Format Options

If you want to specify rendering options (including format-specific options), you do it within the `_quarto.yml` project file rather than within the individual markdown documents. This is because when rendering a book all of the chapters are combined together into a single document (with a single set of format options).

Here’s an example configuration:

```yaml
highlight-style: pygments

format:
  html:
    theme: cosmo
    code-copy: true
  pdf: default

bibliography: references.bib
csl: citestyle.csl
```

Note that in the above configuration the `highlight-style` option applies to all formats whereas the `html` options apply to only HTML output. The bibliography related options naturally also apply to all formats.

### Reader Tools

#### Website Tools

HTML books are at their core [Quarto Websites](https://quarto.org/docs/websites/) with some special navigational behavior built in. This means that all of the features described for enhancing websites are also available for books, including:

*   [Navbars](https://quarto.org/docs/websites/website-navigation.html#top-navigation)
*   [Social Metadata](https://quarto.org/docs/websites/website-tools.html#social-metadata)
*   [Full Text Search](https://quarto.org/docs/websites/website-search.html)
*   [Google Analytics](https://quarto.org/docs/websites/website-tools.html#google-analytics)
*   [Headers and Footers](https://quarto.org/docs/websites/website-tools.html#headers-footers)
*   [Dark Mode](https://quarto.org/docs/output-formats/html-themes.html#dark-mode)

One important thing to note about using website tools is that while these tools are added to websites within the `website` key, in a book you should include the same options in the `book` key. For example, in a website you would include a favicon and twitter card as follows:

```yaml
website:
  favicon: logo.png
  twitter-card: true
  site-url: https://example.com
```

In a book you’d use the `book` key instead:

```yaml
book:
  favicon: logo.png
  twitter-card: true
  site-url: https://example.com
```

#### Sidebar Tools

Books automatically include a navigational sidebar that can optionally include tools for searching book contents, sharing links to the book, etc. Here is an example `_quarto.yml` file that enables these options:

```yaml
book:
  title: "Hands-On Programming with R"
  author: "Garrett Grolemund"
  search: true
  repo-url: https://github.com/jjallaire/hopr/
  repo-actions: [edit]
  downloads: [pdf, epub]
  sharing: [twitter, facebook]

comments:
  hypothesis: true
```

Note the various tools that now appear:

![Sidebar Tools Example](https://quarto.org/docs/books/images/sidebar-tools.png)

*   The search box enables full text search of the entire book
*   The buttons immediately below the book title in the sidebar provide a link to the GitHub repo for the book, downloads for PDF and ePub versions of the book, and links for sharing the book on Twitter and Facebook.
*   Immediately below the table of contents on the right there is an “Edit this page” link that takes the reader to the edit interface on GitHub for the current chapter. Note that in this example we specify `repo-actions: [edit]`. You can optionally also add `issue` and `source` actions (e.g. `repo-actions: [edit, issue, source]`). There are additional options available (`repo-subdir` and `repo-branch`) for [customizing repository links](https://quarto.org/docs/websites/website-navigation.html#github-links).
*   The [Hypothesis](https://web.hypothes.is/) commenting bar appears on the far right of the page. Note that `commenting` is a feature available for all Quarto HTML output so appears in its own YAML key.

#### Sidebar Options

Note that books utilize the standard sidebar component from [Quarto Websites](https://quarto.org/docs/websites/). This means that you can use any of the available [sidebar options](https://quarto.org/docs/reference/projects/websites.html#sidebar) within your `book` configuration. For example, here we specify a docked sidebar with a light background:

```yaml
book:
  title: "Hands-On Programming with R"
  author: "Garrett Grolemund"
  sidebar:
    style: docked
    background: light
```

### Cover Images

You can provide a cover image for EPUB and/or HTML formats using the `cover-image` option. For example:

```yaml
book:
  cover-image: cover.png
```

You can also do this on a per-format basis (if for example you want to provide a higher resolution image for EPUB and a lower resolution image for HTML to reduce download time). For example:

```yaml
format:
  html:
    cover-image: cover.png
  epub:
    cover-image: cover-highres.png
```

You can specify HTML alt-text for book cover images using the `cover-image-alt` option:

```yaml
book:
  cover-image: cover.png
  cover-image-alt: |
    Alternative text describing the book cover
```

### Output Path

By default, book output is written to the `_book` directory of your project. You can change this via the `output-dir` project option. For example:

```yaml
project:
  type: book
  output-dir: docs
```

Single file outputs like PDF, EPUB, etc. are also written to the `output-dir`. Their file name is derived from the book `title`. You can change this via the `output-file` option:

```yaml
book:
  title: "My Book"
  output-file: "my-book"
```

Note that the `output-file` should *not* have a file extension (that will be provided automatically as appropriate for each format).

### LaTeX Output

In some cases you’ll want to do customization of the LaTeX output before creating the final printed manuscript (e.g. to affect how text flows between pages or within and around figures). The best way to approach this is to develop your book all the way to completion, then render to the `latex` format

```bash
quarto render --to latex
```

The complete LaTeX source code of your book will be output into the `_book/book-latex` directory.

At this point you should probably make a copy or git branch of the `_book` directory to perform your final LaTeX modifications within (since the modifications you make to LaTeX will not be preserved in your markdown source, and will therefore be overwritten the next time you render).

### HTML Styles

HTML output can be customized either by adding (or enhancing) a custom theme, or by providing an ordinary CSS file. Use the `theme` option to specify a theme:

```yaml
format:
  html:
    theme: cosmo
```

To further customize a theme add a custom theme file:

```yaml
format:
  html:
    theme: [cosmo, theme.scss]
```

You can learn more about creating theme files in the documentation on [HTML Themes](https://quarto.org/docs/output-formats/html-themes.html).

You can also just use plain CSS. For example:

```yaml
format:
  html:
    css: styles.css
```

### EPUB Styles

You can also use CSS to customize EPUB output:

```yaml
format:
  epub:
    css: epub-styles.css
    epub-cover-image: epub-cover.png
```

Note that we also specify a cover image. To learn more about other EPUB options, see the Pandoc [documentation on EPUBs](https://pandoc.org/MANUAL.html#epub-metadata).

### PDF Styles

You can include additional LaTeX directives in the preamble of your book using the `include-in-header` option. You can also add `documentclass` and other options (see the Pandoc documentation on [LaTeX options](https://pandoc.org/MANUAL.html#variables-for-latex) for additional details). For example:

```yaml
format:
  pdf:
    documentclass: scrbook
    include-in-header: preamble.tex
    fontfamily: libertinus
```

Quarto uses the [KOMA Script](https://www.ctan.org/pkg/koma-script) `scrreprt` document class by default for PDF books. KOMA-Script classes are drop-in replacements for the standard classes with an emphasis on typography and versatility.

You can switch to KOMA `scrbook` as demonstrated above, or to the standard LaTeX `book` and `report` classes. You can find a summary of the differences between `book` and `report` here: <https://tex.stackexchange.com/questions/36988>

### MS Word Styles

You can customize MS Word output by creating a new [reference doc](https://quarto.org/docs/output-formats/ms-word-templates.html#creating-templates), and then applying it to your book as follows:

```yaml
format:
  docx:
    reference-doc: custom-reference.docx
```

Learn more about creating and customizing a reference document in the documentation on [Word templates](https://quarto.org/docs/output-formats/ms-word-templates.html).

