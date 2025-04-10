## Extensions: Creating Custom Formats

Source: [Custom Formats – Quarto](https://quarto.org/docs/extensions/formats.html)

### Overview

Quarto format extensions enable you to add new formats to the built-in formats (e.g. `html`, `pdf`, `docx`) already available. Custom formats can provide default document options, style-sheets, header, footer, or logo elements, and even bundle other extensions like [filters](https://quarto.org/docs/extensions/filters.html) and [shortcodes](https://quarto.org/docs/extensions/shortcodes.html). They are a great way to provide a common baseline for authoring documents or presentations within an organization, for a particular type of project or analysis, or for a specific publication.

You can specify a custom format beneath the `format` key just like a built-in format. For example:

```yaml
---
title: "My Document"
format:
  acm-pdf:
    toc: true
---
```

Custom formats all derive from one of the base formats, and include that base format as a suffix. Formats can also provide multiple variations that derive from distinct base formats. For example:

```yaml
---
title: "My Document"
toc: true
format:
  acm-pdf: default
  acm-html: default
---
```

Note that we moved the `toc` option to the top level since it is shared between both of the formats.

Custom formats can also be used with the `--to` argument to `quarto render`. For example:

```bash
quarto render document.qmd --to acm-html
```

Note that if you are specifically interested in using or creating custom formats for journals and manuscripts, you may want to proceed instead to the documentation on [Journal Articles](https://quarto.org/docs/journals/).

### Quick Start

Here we’ll describe how to create a simple HTML-based format extension. We’ll use the `quarto create` command to do this. If you are using VS Code or RStudio you should execute `quarto create` within their respective integrated Terminal panes.

To get started, execute `quarto create extension format:html` within the parent directory where you’d like the format to be created:

```bash
$ quarto create extension format:html
? Extension Name › lexdoc
```

As shown above, you’ll be prompted for an extension name. Type `lexdoc` (a document format for a fictional company named LexCrop) and press Enter—the custom format extension is then created:

```
Creating extension at /Users/jjallaire/quarto/dev/lexdoc:
- Created README.md
- Created _extensions/lexdoc/custom.scss
- Created _extensions/lexdoc/_extension.yml
- Created template.qmd
```

If you are running within VS Code or RStudio a new window will open with the extension project.

Note that this example creates a format that is derivative of the Quarto base `html` format. You can similarly create formats that are derivative of `pdf`, `docx`, and `revealjs` as follows:

```bash
quarto create extension format:pdf
quarto create extension format:docx
quarto create extension format:revealjs
```

Here’s what the contents of the files in `_extensions/lexdoc/` look like:

**_extensions/lexdoc/_extension.yml**
```yaml
title: Lexdoc
author: J.J. Allaire
version: 1.0.0
quarto-required: ">=1.2.222"
contributes:
  formats:
    html:
      toc: true
      theme: [yeti, custom.scss]
```

The custom HTML format defined here is very simple. It takes the base `html` format, turns on the table of contents by default, and sets the theme as `yeti` along with a `custom.scss` file for additional customizations:

**_extensions/lexdoc/custom.scss**
```scss
/*-- scss:defaults --*/
/* TODO: Customize appearance with SCSS variables */
/* See [HTML theme](https://quarto.org/docs/output-formats/html-themes.html#theme-options) */

/*-- scss:rules --*/
/* TODO: Provide custom CSS rules */
```

Finally, the `template.qmd` provides a base example article for users of the format:

**template.qmd**
```yaml
---
title: "Lexdoc Example"
format:
  lexdoc-html: default
author: J.J. Allaire
date: last-modified
---

