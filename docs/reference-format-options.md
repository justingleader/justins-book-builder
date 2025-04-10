## Reference: Format Options

(This combines the content from multiple specific format reference pages into a general structure. I will include the options listed across the various formats provided in the source, noting where options are format-specific if mentioned in the source.)

### Overview

This section details the various YAML options available for configuring Quarto output formats. Many options are common across formats, while others are specific to certain formats like HTML, PDF, or presentations.

### Title & Author Metadata

These options define basic document metadata.

| Option        | Description                                                           | Formats      |
| :------------ | :-------------------------------------------------------------------- | :----------- |
| `title`       | Document title                                                        | All          |
| `subtitle`    | Identifies the subtitle of the document.                              | Most         |
| `date`        | Document date                                                         | All          |
| `date-modified`| Document date modified                                                | html         |
| `author`      | Author or authors of the document                                     | All          |
| `institute`   | Author affiliations for the presentation.                             | beamer, pptx |
| `affiliation` | The list of organizations with which contributors are affiliated.       | jats         |
| `abstract`    | Summary of document                                                   | Most         |
| `abstract-title`| Title used to label document abstract                               | html, epub   |
| `thanks`      | The contents of an acknowledgments footnote after the document title.   | pdf, beamer  |
| `order`       | Order for document when included in a website automatic sidebar menu. | All          |
| `copyright`   | Licensing and copyright information.                                | jats, html   |
| `license`     | The license for this document, if any.                                | html, jats   |
| `doi`         | Displays the document Digital Object Identifier in the header.        | html         |
| `keywords`    | List of keywords to be included in the document metadata.             | Most         |
| `subject`     | The document subject                                                  | docx, odt    |
| `description` | The document description.                                             | docx, odt    |
| `category`    | The document category.                                                | docx, odt    |

### General Format Options

These options control broader aspects of rendering and format behavior.

| Option            | Description                                                                                                                          | Formats      |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------- | :----------- |
| `brand`           | Branding information to use for this document. If a string, the path to a brand file. If false, don’t use branding. If object, inline definition. | All          |
| `quarto-required` | A semver version range describing the supported quarto versions for this document or project (e.g., `>= 1.2.0`).                         | All          |
| `template`        | Use the specified file as a custom template for the generated document.                                                              | Most         |
| `template-partials`| Include the specified files as partials accessible to the template for the generated content.                                          | Most         |
| `from`            | Format to read from. Extensions can be individually enabled or disabled by appending `+EXTENSION` or `-EXTENSION`.                      | All          |
| `output-file`     | Output file to write to.                                                                                                             | All          |
| `output-ext`      | Extension to use for generated output file.                                                                                            | All          |
| `filters`         | Specify executables or Lua scripts to be used as a filter transforming the pandoc AST.                                                 | All          |
| `shortcodes`      | Specify Lua scripts that implement shortcode handlers.                                                                                 | All          |
| `metadata-files`  | Read metadata from the supplied YAML (or JSON) files.                                                                                  | All          |
| `resource-path`   | List of paths to search for images and other resources.                                                                                | All          |
| `default-image-extension`| Specify a default extension to use when image paths/URLs have no extension.                                                      | markdown, latex |
| `abbreviations`   | Specifies a custom abbreviations file.                                                                                               | All          |
| `dpi`             | Specify the default dpi (dots per inch) value for pixel conversions. Default is 96.                                                  | All          |

### Table of Contents (TOC)

Options for controlling the table of contents.

| Option       | Description                                                                          | Formats      |
| :----------- | :----------------------------------------------------------------------------------- | :----------- |
| `toc`        | Include an automatically generated table of contents.                                | Most         |
| `toc-depth`  | Specify the number of section levels to include in the TOC. Default is 3.          | Most         |
| `toc-title`  | The title used for the table of contents.                                            | html, pdf, docx, odt, epub, beamer |
| `toc-location`| Location for TOC in HTML: `body`, `left`, `right` (default), `left-body`, `right-body`. | html         |
| `toc-expand` | How much of the HTML TOC to show initially (`true`, `false`, or depth level). Default 1. | html         |
| `toc-indent` | Indentation for each level in Typst TOC. Default `1.5em`.                            | typst        |
| `lof`        | Print a list of figures in the document.                                             | pdf, beamer  |
| `lot`        | Print a list of tables in the document.                                              | pdf, beamer  |
| `lol-title`  | The title used for the list of listings in books.                                    | pdf (book)   |

### Numbering and Headings

Options for section numbering and heading levels.

| Option                 | Description                                                                                               | Formats      |
| :--------------------- | :-------------------------------------------------------------------------------------------------------- | :----------- |
| `number-sections`      | Number section headings. Sections with class `.unnumbered` are never numbered.                             | Most         |
| `number-depth`         | Deepest level of heading to add numbers to (default is all).                                              | Most         |
| `number-offset`        | Offset for section headings (e.g., `5` to start at 6, `[1,4]` for 1.5). Implies `number-sections`.      | Most         |
| `shift-heading-level-by`| Shift heading levels by a positive or negative integer.                                                   | Most         |
| `top-level-division`   | Treat top-level headings as `section`, `chapter`, or `part`. Affects LaTeX and ConTeXt hierarchy.         | latex, context, tei, docbook |
| `section-numbering`    | Schema for numbering sections in Typst (e.g., `1.A.a`).                                                     | typst        |
| `markdown-headings`    | Specify ATX (`#`) or Setext (`===`) headings for level 1/2 in Markdown output.                             | markdown, ipynb, gfm, commonmark |

### Layout Options

Options controlling page layout, margins, and grids.

| Option         | Description                                                                                                 | Formats               |
| :------------- | :---------------------------------------------------------------------------------------------------------- | :-------------------- |
| `page-layout`  | HTML page layout: `article` (default), `full`, or `custom`.                                                 | html                  |
| `grid`         | Properties of the grid system used for layout (sidebar, body, margin, gutter widths).                       | html, dashboard       |
| `cap-location` | Default location for figure and table captions (`top`, `bottom`, `margin`).                                 | html, pdf, beamer     |
| `fig-cap-location`| Location for figure captions (`top`, `bottom`, `margin`).                                                   | html, pdf, beamer     |
| `tbl-cap-location`| Location for table captions (`top`, `bottom`, `margin`).                                                    | html, pdf, beamer     |
| `max-width`    | Max CSS width for HTML body content.                                                                        | html                  |
| `margin-left`, `margin-right`, `margin-top`, `margin-bottom` | Page margins. Usage varies by format (CSS for HTML, geometry for LaTeX, layout for ConTeXt). | html, pdf, context |
| `geometry`     | Options for the LaTeX `geometry` package (e.g., `top=30mm`).                                                | pdf, beamer           |
| `papersize`    | Paper size for PDF/Typst (e.g., `a4`, `letter`).                                                            | pdf, beamer, typst    |
| `documentclass`| LaTeX document class (e.g., `scrartcl`, `book`).                                                            | pdf, beamer           |
| `classoption`  | Options for the LaTeX document class or `fleqn` for HTML KaTeX.                                             | pdf, html, beamer     |
| `pagestyle`    | LaTeX `\pagestyle{}`.                                                                                       | pdf, beamer           |
| `indent`       | Use document class settings for indentation (LaTeX) or paragraph indent (groff ms).                         | pdf, ms, beamer       |
| `block-headings`| Make LaTeX `\paragraph` and `\subparagraph` free-standing.                                                  | pdf, beamer           |
| `layout`       | Margin and text layout options for ConTeXt.                                                                 | context               |
| `whitespace`   | Spacing between paragraphs in ConTeXt (`none`, `small`).                                                    | context               |
| `indenting`    | Paragraph indentation options for ConTeXt.                                                                  | context               |
| `page-width`   | Target body page width for docx/odt (used for layout div calculations). Default `6.5in`.                      | docx, odt             |
| `columns`      | Number of columns for body text in Typst.                                                                   | typst                 |

### Code Block Options

Options related to the display and execution of code blocks.

| Option                  | Description                                                                                                            | Formats               |
| :---------------------- | :--------------------------------------------------------------------------------------------------------------------- | :-------------------- |
| `code-fold`             | Collapse code blocks in HTML (`true`, `false`, `show`).                                                                  | html, epub            |
| `code-summary`          | Summary text for collapsed code blocks.                                                                                | html, epub            |
| `code-overflow`         | How to handle code overflow (`scroll` or `wrap`).                                                                        | html, epub            |
| `code-line-numbers`     | Include line numbers (`true` or `false`). Supports highlighting ranges/steps for revealjs.                                | html, pdf, beamer, docx, odt, typst, revealjs |
| `code-copy`             | Enable code copy icon for HTML (`true`, `false`, `hover`).                                                               | html, epub            |
| `code-link`             | Enable hyperlinking of functions to documentation (knitr only).                                                          | html                  |
| `code-annotations`      | Style for code annotations (`below`, `hover`, `select`, `none`, `false`).                                                 | All                   |
| `code-block-border-left`| Apply left border to code blocks (HTML/PDF/Beamer - specify `true` or color).                                             | html, pdf, beamer     |
| `code-block-bg`         | Apply background color to code blocks (HTML/PDF/Beamer - specify `true` or color).                                        | html, pdf, beamer     |
| `highlight-style`       | Syntax highlighting theme (e.g., `github`, `arrow`, `pygments`, or path to `.theme` file).                               | html, pdf, beamer, docx |
| `syntax-definitions`    | KDE language syntax definition files (XML).                                                                            | html, pdf, beamer, docx |
| `listings`              | Use LaTeX `listings` package for code blocks.                                                                          | pdf, beamer           |
| `indented-code-classes` | Specify CSS classes for indented code blocks.                                                                          | html, pdf, beamer     |
| `filename`              | Code block filename attribute (used by some formats like HTML, PDF).                                                   | Most                  |

### Execution Options

These options control how computational code cells are executed. They are typically nested under the `execute` key.

| Option       | Description                                                                                                      | Formats |
| :----------- | :--------------------------------------------------------------------------------------------------------------- | :------ |
| `eval`       | Evaluate code cells (`true`, `false`, or line numbers for knitr).                                                | All     |
| `echo`       | Include source code in output (`true`, `false`, `fenced`, or line numbers for knitr). Default depends on format.    | All     |
| `output`     | Include execution results (`true`, `false`, `asis`).                                                             | All     |
| `warning`    | Include warnings (`true` or `false`).                                                                            | All     |
| `error`      | Include errors (`true` or `false`). If `true`, errors don't halt rendering.                                      | All     |
| `include`    | Catch-all for preventing any cell output (`true` or `false`).                                                    | All     |
| `cache`      | Cache computation results (`true`, `false`, `refresh`). Uses knitr cache or Jupyter Cache.                         | All     |
| `freeze`     | Control re-computation during project render (`true`, `false`, `auto`).                                          | All     |
| `debug`      | Enable Jupyter debugging output (`true` or `false`).                                                             | Jupyter |
| `daemon`     | Use a persistent Jupyter kernel daemon (`true`, `false`, or timeout in seconds). Default depends on OS.          | Jupyter |
| `execute-dir`| Working directory for computations (`file` or `project`).                                                        | Project |
| `keep-md`    | Keep the intermediate markdown file generated after execution.                                                   | All     |
| `keep-ipynb` | Keep the intermediate Jupyter notebook file generated (from `.qmd`).                                             | All     |
| `ipynb-filters`| Filters to pre-process `.ipynb` files before rendering.                                                          | All     |
| `ipynb-shell-interactivity`| Jupyter cell expression printing behavior (`all`, `last_expr`, `none`).                              | Jupyter |
| `plotly-connected`| Use online Plotly library (`true`) or embed offline (`false`).                                               | All     |

### Figure Options

Options controlling the output of figures.

| Option         | Description                                                                                              | Formats            |
| :------------- | :------------------------------------------------------------------------------------------------------- | :----------------- |
| `fig-width`    | Default width for generated figures (inches). Cell-level only for knitr.                                 | All                |
| `fig-height`   | Default height for generated figures (inches). Cell-level only for knitr.                                | All                |
| `fig-format`   | Default format for generated figures (`retina`, `png`, `jpeg`, `svg`, `pdf`).                              | All                |
| `fig-dpi`      | Default DPI for generated figures. Cell-level only for knitr.                                           | All                |
| `fig-asp`      | Aspect ratio (height/width) for generated figures (knitr only).                                          | Knitr Engine       |
| `fig-align`    | Figure horizontal alignment (`default`, `left`, `right`, `center`).                                        | html, pdf, docx, odt |
| `fig-alt`      | Alternative text for HTML images.                                                                        | html               |
| `fig-link`     | Hyperlink target for the figure.                                                                         | html               |
| `fig-env`      | LaTeX environment for figure output (e.g., `figure*`).                                                    | pdf, beamer        |
| `fig-pos`      | LaTeX figure position (`h`, `t`, `b`, `p`, `H`, `!`, or `false`). Default `H` for computational figs.      | pdf, beamer        |
| `fig-scap`     | Short caption for LaTeX List of Figures.                                                                 | pdf, beamer        |
| `fig-responsive`| Make images responsive in HTML.                                                                          | html, epub         |
| `out-width`    | Output width for knitr figures (e.g., `50%`, `3in`).                                                      | Knitr Engine       |
| `out-height`   | Output height for knitr figures.                                                                         | Knitr Engine       |
| `fig-keep`     | Which plots to keep in knitr (`high`, `none`, `all`, `first`, `last`, numeric vector).                    | Knitr Engine       |
| `fig-show`     | How to show knitr plots (`asis`, `hold`, `animate`, `hide`).                                             | Knitr Engine       |
| `out-extra`    | Additional raw LaTeX or HTML options for figures.                                                        | Knitr Engine       |
| `external`     | Externalize tikz graphics (pre-compile to PDF) (knitr only).                                             | Knitr Engine       |
| `sanitize`     | Sanitize tikz graphics (escape special LaTeX characters) (knitr only).                                   | Knitr Engine       |
| `interval`     | Time interval (seconds) between animation frames (knitr only).                                           | Knitr Engine       |
| `aniopts`      | Extra options for LaTeX `animate` package (knitr only).                                                   | Knitr Engine       |
| `animation-hook`| Hook function for HTML animations (`ffmpeg` or `gifski`) (knitr only).                                  | Knitr Engine       |
| `lightbox`     | Enable lightbox for figures in HTML.                                                                     | html               |

### Table Options

Options controlling the output of tables.

| Option                | Description                                                                                             | Formats               |
| :-------------------- | :------------------------------------------------------------------------------------------------------ | :-------------------- |
| `tbl-colwidths`       | Explicit column widths for markdown tables (`auto`, `true`, `false`, or array like `[40, 60]`).            | Most                  |
| `df-print`            | Method for printing knitr data frames (`default`, `kable`, `tibble`, `paged`).                            | Knitr Engine          |
| `list-tables`         | Use RST list tables.                                                                                    | rst                   |
| `html-table-processing`| Disable Quarto's HTML table processing (`none`).                                                        | html, pdf, docx, etc. |
| `css-property-processing`| Control translation of CSS properties to Typst properties (`translate` (default), `none`).             | typst                 |
| `html-pre-tag-processing`| Control processing of HTML `<pre>` tags for Typst (`parse` via div attribute, `none`).                 | typst                 |

### References and Citations

Options for managing bibliographies, citations, footnotes, and cross-references.

| Option                 | Description                                                                                                          | Formats            |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------- | :----------------- |
| `bibliography`         | Document bibliography file(s) (BibTeX, CSL JSON, etc.).                                                                | All                |
| `csl`                  | Citation Style Language file (`.csl`) for formatting.                                                                | All                |
| `citeproc`             | Turn on built-in citation processing.                                                                                | All                |
| `cite-method`          | Citation processing method for PDF (`citeproc`, `natbib`, `biblatex`).                                               | pdf, beamer        |
| `biblatexoptions`      | List of options for BibLaTeX.                                                                                        | pdf, beamer        |
| `natbiboptions`        | List of options for natbib.                                                                                          | pdf, beamer        |
| `biblio-style`         | Bibliography style for natbib/biblatex (e.g., `dinat`).                                                              | pdf, beamer        |
| `biblio-title`         | Bibliography title for natbib/biblatex.                                                                              | pdf, beamer        |
| `biblio-config`        | Output bib config for natbib/biblatex even if `citeproc` is used.                                                    | pdf, beamer        |
| `bibliographystyle`   | Bibliography style for Typst's built-in system (e.g., `apa`, path to `.csl`).                                          | typst              |
| `citation-abbreviations`| JSON file with journal abbreviations for `form="short"`.                                                             | All                |
| `link-citations`       | Hyperlink citations to bibliography entries (author-date/numerical styles). Defaults `false`.                           | Most (not Word)    |
| `link-bibliography`    | Hyperlink DOIs, URLs, etc., in bibliography. Defaults `true`.                                                        | pdf, beamer        |
| `notes-after-punctuation`| Place footnote/citation markers after punctuation (note styles). Default `true`.                                   | Most               |
| `links-as-notes`       | Print links as footnotes (LaTeX/Beamer only).                                                                        | pdf, beamer        |
| `reference-location`   | Location for footnotes/references (`block`, `section`, `document`, `margin`).                                        | html, pdf, commonmark, muse |
| `citations-hover`      | Enable hover popup for citations in HTML.                                                                            | html               |
| `footnotes-hover`      | Enable hover popup for footnotes in HTML.                                                                            | html               |
| `crossrefs-hover`      | Enable hover popup for cross-references in HTML.                                                                     | html               |
| `crossref`             | Configuration for cross-reference labels and prefixes. See [Cross Reference Options](https://quarto.org/docs/reference/metadata/crossref.html). | All                |
| `citation`             | Citation metadata for the document itself (CSL YAML). See [Citation Metadata](https://quarto.org/docs/reference/metadata/citation.html).   | All                |

### Language and Directionality

Options for document language and text direction.

| Option     | Description                                                                              | Formats |
| :--------- | :--------------------------------------------------------------------------------------- | :------ |
| `lang`     | Main document language (IETF tag, e.g., `en`, `fr-CA`). Affects hyphenation, localization. | All     |
| `language` | YAML file containing custom language translations.                                       | All     |
| `dir`      | Base script direction (`rtl` or `ltr`). Affects HTML, LaTeX (xelatex), ConTeXt.          | All     |

### Includes and Resources

Options for including external content and resources.

| Option              | Description                                                                                             | Formats               |
| :------------------ | :------------------------------------------------------------------------------------------------------ | :-------------------- |
| `include-in-header` | Include content at the end of the header (e.g., CSS/JS in HTML, LaTeX preamble).                         | html, pdf, context, beamer, etc. |
| `include-before-body`| Include content at the beginning of the body.                                                           | html, pdf, context, etc. |
| `include-after-body` | Include content at the end of the body.                                                                 | html, pdf, context, etc. |
| `resources`         | Path (or glob) to additional files to publish with the document.                                        | html, epub            |
| `embed-resources`   | Create a self-contained HTML file with embedded resources (`data:` URIs).                               | html, revealjs        |
| `self-contained-math`| Embed math libraries (MathJax/KaTeX) in self-contained HTML.                                           | html, revealjs        |
| `extract-media`     | Extract linked media to a directory and update references.                                              | All                   |
| `format-resources`  | List of file paths to copy into the input directory during render (e.g., `.bst` for LaTeX).             | pdf, custom formats   |
| `includesource`     | Include all source documents as file attachments in ConTeXt PDF.                                        | context               |
| `font-paths`        | Additional paths to search for fonts in Typst.                                                          | typst                 |
| `header`            | Header text for man pages.                                                                              | man                   |
| `footer`            | Footer text for man pages.                                                                              | man                   |
| `headertext`        | Running header text for ConTeXt (up to 4 placements).                                                   | context               |
| `footertext`        | Running footer text for ConTeXt (up to 4 placements).                                                   | context               |

### Metadata Options

Options controlling document metadata fields in the output.

| Option             | Description                                                    | Formats         |
| :----------------- | :------------------------------------------------------------- | :-------------- |
| `title-meta`       | Sets the title metadata (e.g., in PDF properties).             | pdf, beamer     |
| `author-meta`      | Sets the author metadata.                                      | pdf, beamer     |
| `date-meta`        | Sets the date metadata.                                        | pdf, html       |
| `pagetitle`        | Sets the `<title>` metadata for HTML documents.                  | html            |
| `title-prefix`     | Prefix for HTML `<title>`.                                     | html            |
| `description-meta` | Sets the description metadata.                                 | html            |
| `google-scholar`   | Generate Google Scholar compatible metadata tags.              | html            |
| `open-graph`       | Generate Open Graph metadata (boolean or object with options). | html (website)  |
| `twitter-card`     | Generate Twitter Card metadata (boolean or object with options).| html (website)  |
| `epub-metadata`    | XML file with EPUB Dublin Core metadata overrides.             | epub            |

### Rendering Control

Options affecting the overall rendering process.

| Option                     | Description                                                                                                                                | Formats     |
| :------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| `reference-doc`            | Use specified file as a style reference for docx, pptx, odt.                                                                               | docx, pptx, odt |
| `keep-typ`                 | Keep the intermediate `.typ` file used during Typst rendering.                                                                             | typst       |
| `latex-auto-mk`            | Use Quarto's built-in PDF rendering wrapper (auto installs packages).                                                                      | pdf, beamer |
| `latex-auto-install`       | Enable/disable automatic LaTeX package installation.                                                                                       | pdf, beamer |
| `latex-min-runs`, `latex-max-runs` | Min/max LaTeX compilation passes.                                                                                                    | pdf, beamer |
| `latex-clean`              | Clean intermediate LaTeX files after compilation (default `true`).                                                                           | pdf, beamer |
| `latex-makeindex`          | Program for `makeindex`.                                                                                                                   | pdf, beamer |
| `latex-makeindex-opts`     | Command line options for `makeindex`.                                                                                                      | pdf, beamer |
| `latex-tlmgr-opts`         | Command line options for `tlmgr`.                                                                                                          | pdf, beamer |
| `latex-output-dir`         | Output directory for LaTeX intermediates and PDF.                                                                                            | pdf, beamer |
| `latex-tinytex`            | Set to `false` to prevent using an installed TinyTeX.                                                                                      | pdf, beamer |
| `latex-input-paths`        | Array of paths for LaTeX input search.                                                                                                     | pdf, beamer |
| `use-rsvg-convert`         | If `true`, attempt to use `rsvg-convert` for SVG to PDF conversion.                                                                        | pdf, beamer |
| `pdfa`                     | Generate PDF/A conforming output (specify type like `1b:2005` or `true`). Requires ICC profiles.                                           | context     |
| `pdfaiccprofile`           | ICC profile for PDF/A output.                                                                                                              | context     |
| `pdfaintent`               | Output intent for PDF/A colors.                                                                                                            | context     |
| `ipynb-output`             | Control which cell output formats are rendered in `.ipynb` output (`all`, `none`, `best` (default)).                                        | ipynb       |

### Text Output Options

Options controlling the formatting of plain text based output formats.

| Option          | Description                                                                                                  | Formats         |
| :-------------- | :----------------------------------------------------------------------------------------------------------- | :-------------- |
| `wrap`          | Text wrapping strategy (`auto`, `none`, `preserve`). Default `auto`.                                           | Text-based    |
| `columns`       | Line length (characters) for wrapping and plain text table calculations. Default 72. Number of cols for Typst. | Text-based, typst |
| `tab-stop`      | Number of spaces per tab (default 4).                                                                        | Text-based    |
| `preserve-tabs` | Preserve tabs in code blocks instead of converting to spaces.                                                | Text-based    |
| `eol`           | Line ending style (`crlf`, `lf`, `native`).                                                                  | Text-based    |
| `strip-comments`| Strip HTML comments from source.                                                                               | html, markdown, textile |
| `ascii`         | Use only ASCII characters in output (uses entities or escapes).                                              | html, xml, markdown, text-based |

### Presentation Specific Options

These options apply specifically to presentation formats like Revealjs, Beamer, and PowerPoint.

| Option            | Description                                                                                              | Format         |
| :---------------- | :------------------------------------------------------------------------------------------------------- | :------------- |
| `incremental`     | Make lists display incrementally by default.                                                             | revealjs, pptx, beamer |
| `slide-level`     | Heading level that creates new slides (0-6). Default varies.                                             | revealjs, pptx, beamer |
| `aspectratio`     | Slide aspect ratio (e.g., `169` for 16:9).                                                               | beamer         |
| `navigation`      | Beamer navigation symbols (`empty`, `frame`, `vertical`, `horizontal`).                                  | beamer         |
| `section-titles`  | Enable title pages for new sections in Beamer (default `true`).                                          | beamer         |
| `theme`, `colortheme`, `fonttheme`, `innertheme`, `outertheme`, `themeoptions` | Beamer themes and options.                 | beamer         |
| `revealjs-url`    | Directory containing reveal.js files.                                                                    | revealjs       |
| `width`, `height`, `margin`, `min-scale`, `max-scale` | Revealjs presentation size and scaling options.                      | revealjs       |
| `controls`, `progress`, `history`, `center`, `touch`, `keyboard`, `mouse-wheel`, `slide-number`, etc. | Revealjs navigation and display controls. See [Revealjs Options](https://quarto.org/docs/reference/formats/presentations/revealjs.html). | revealjs       |
| `transition`, `background-transition`, `transition-speed` | Revealjs slide transition effects and speed.                       | revealjs       |
| `auto-slide`, `loop`, `auto-slide-stoppable`, `auto-slide-method` | Revealjs auto-sliding options.                           | revealjs       |
| `fragments`, `auto-animate`, `parallax-background-image`, etc. | Revealjs advanced features. See [Revealjs Options](https://quarto.org/docs/reference/formats/presentations/revealjs.html). | revealjs       |
| `chalkboard`, `menu`, `multiplex`, `notes`, `pointer` | Revealjs built-in and extension plugin configurations.                 | revealjs       |

### Wiki Specific Options

| Option   | Description                       | Format   |
| :------- | :-------------------------------- | :------- |
| `section`| Section number for man pages.     | man      |
| `header` | Header for man pages.             | man      |
| `footer` | Footer for man pages.             | man      |

### Deprecated/Legacy Options

(This section would list options from previous versions that are no longer recommended or have been replaced, if any were present in the source data.)

*None explicitly listed in the provided source data.*

---
```
