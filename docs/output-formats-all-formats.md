## Output Formats: All Formats

Source: [All Formats – Quarto](https://quarto.org/docs/output-formats/all-formats.html)

### Overview

Pandoc supports a huge array of output formats, all of which can be used with Quarto. To use any Pandoc format just use the `format` option or the `--to` command line option.

For example, here’s some YAML that specifies the use of the `html` format as well as a couple of format options:

```yaml
---
title: "My Document"
format:
  html:
    toc: true
    code-fold: true
---
```

Alternatively you can specify the use of a format on the command line:

```bash
quarto render document.qmd --to html
```

See below for a list of all output formats by type along with links to their reference documentation.

### Documents

*   [HTML](https://quarto.org/docs/reference/formats/html.html): HTML is a markup language used for structuring and presenting content on the web.
*   [PDF](https://quarto.org/docs/reference/formats/pdf.html): PDF is a file format for creating print-ready paged documents.
*   [MS Word](https://quarto.org/docs/reference/formats/docx.html): MS Word is the word processor included with Microsoft Office.
*   [OpenDocument](https://quarto.org/docs/reference/formats/odt.html): ODT is an open standard file format for word processing documents.
*   [ePub](https://quarto.org/docs/reference/formats/epub.html): ePub is an e-book file format that is supported by many e-readers.

### Presentations

*   [Revealjs](https://quarto.org/docs/reference/formats/presentations/revealjs.html): Revealjs is an open source HTML presentation framework.
*   [PowerPoint](https://quarto.org/docs/reference/formats/presentations/pptx.html): PowerPoint is the presentation editing software included with Microsoft Office.
*   [Beamer](https://quarto.org/docs/reference/formats/presentations/beamer.html): Beamer is a LaTeX class for producing presentations and slides.

### Markdown

*   [GitHub](https://quarto.org/docs/reference/formats/markdown/gfm.html): GitHub Flavored Markdown (GFM) is the dialect of Markdown that is currently supported for user content on GitHub.
*   [CommonMark](https://quarto.org/docs/reference/formats/markdown/commonmark.html): CommonMark is a strongly defined, highly compatible specification of Markdown.
*   [Hugo](https://quarto.org/docs/output-formats/hugo.html): Hugo is an open-source static website generator. (*User guide link provided*)
*   [Docusaurus](https://quarto.org/docs/output-formats/docusaurus.html): Docusaurus is an open-source markdown documentation system. (*User guide link provided*)
*   [Markua](https://quarto.org/docs/reference/formats/markdown/markua.html): Markua is a markdown variant used by Leanpub.

### Wikis

*   [MediaWiki](https://quarto.org/docs/reference/formats/wiki/mediawiki.html): MediaWiki is the native document format of Wikipedia.
*   [DokuWiki](https://quarto.org/docs/reference/formats/wiki/dokuwiki.html): DokuWiki is a simple to use and highly versatile open source wiki software that doesn’t require a database.
*   [ZimWiki](https://quarto.org/docs/reference/formats/wiki/zimwiki.html): Zim is a graphical text editor used to maintain a collection of wiki pages.
*   [Jira Wiki](https://quarto.org/docs/reference/formats/wiki/jira.html): Jira Wiki is the native document format for the Jira issue tracking and project management system from Atlassian.
*   [XWiki](https://quarto.org/docs/reference/formats/wiki/xwiki.html): XWiki is an open-source enterprise wiki system.

### More Formats

*   [JATS](https://quarto.org/docs/reference/formats/jats.html): JATS (Journal Article Tag Suite) is an XML format for marking up and exchanging journal content.
*   [Jupyter](https://quarto.org/docs/reference/formats/ipynb.html): Jupyter Notebooks combine software code, computational output, explanatory text and multimedia resources in a single document.
*   [ConTeXt](https://quarto.org/docs/reference/formats/context.html): ConTeXt is a system for typesetting documents based on TEX and METAPOST.
*   [RTF](https://quarto.org/docs/reference/formats/rtf.html): The Rich Text Format (RTF) is a file format for cross-platform document interchange.
*   [reST](https://quarto.org/docs/reference/formats/rst.html): reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system.
*   [AsciiDoc](https://quarto.org/docs/reference/formats/asciidoc.html): AsciiDoc is a text document format for writing documentation, articles, and books, ebooks, slideshows, web pages, man pages and blogs.
*   [Org-Mode](https://quarto.org/docs/reference/formats/org.html): Org-Mode is an Emacs major mode for keeping notes, authoring documents, creating computational notebooks, and more.
*   [Muse](https://quarto.org/docs/reference/formats/muse.html): Emacs Muse is an authoring and publishing environment for Emacs.
*   [GNU Texinfo](https://quarto.org/docs/reference/formats/texinfo.html): Texinfo is the official documentation format of the GNU project.
*   [Groff Man Page](https://quarto.org/docs/reference/formats/man.html): The Groff (GNU troff) man page document formats consists of plain text mixed with formatting commands that produce ASCII/UTF8 for display at the terminal.
*   [Groff Manuscript](https://quarto.org/docs/reference/formats/ms.html): The Groff (GNU troff) manuscript format consists of plain text mixed with formatting commands that produces PostScript, PDF, or HTML.
*   [Haddock markup](https://quarto.org/docs/reference/formats/haddock.html): Haddock is a tool for automatically generating documentation from annotated Haskell source code.
*   [OPML](https://quarto.org/docs/reference/formats/opml.html): OPML (Outline Processor Markup Language) is an XML format for outlines.
*   [Textile](https://quarto.org/docs/reference/formats/textile.html): Textile is a simple text markup language that makes it easy to structure content for blogs, wikis, and documentation.
*   [DocBook](https://quarto.org/docs/reference/formats/docbook.html): DocBook is an XML schema particularly well suited to books and papers about computer hardware and software.
*   [InDesign](https://quarto.org/docs/reference/formats/icml.html): ICML is an XML representation of an Adobe InDesign document.
*   [TEI Simple](https://quarto.org/docs/reference/formats/tei.html): TEI Simple aims to define a new *highly-constrained* and *prescriptive* subset of the Text Encoding Initiative (TEI) Guidelines suited to the representation of early modern and modern books.
*   [FictionBook](https://quarto.org/docs/reference/formats/fb2.html): FictionBook is an open XML-based e-book format.

