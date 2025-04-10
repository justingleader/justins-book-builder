## Authoring Includes

Source: [Includes – Quarto](https://quarto.org/docs/authoring/includes.html)

### Overview

Includes are a convenient way to re-use content across documents. Includes work for plain markdown content as well as for `.qmd` files with executable code cells (note however that the cells must all use the same engine – i.e. knitr or jupyter, but not both).

To include a file, add the `{{< include >}}` shortcode at the location in your document where you want it included.

```markdown
{{< include _content.qmd >}}
```

**Important:** Include shortcodes are equivalent to copying and pasting the text from the included file into the main file. This means that relative references (links, images, other includes, etc.) inside the included file resolve based on the directory of the main file not the included file. Use absolute (to the project root) paths for links, images, or other includes, in included files to ensure they resolve correctly, *e.g.*, `[A Figure Reused](/path/to/image.png)` or `{{< include /path/to/_file.qmd >}}`.

It also means that if the included file has a metadata block, that block will take effect in all included files. In most cases, having metadata blocks in an included file will cause unexpected behavior.

**Important:** Include shortcodes need to appear by themselves in a line, and they need to be surrounded by empty lines. This means that you cannot use an include shortcode inside markdown syntax (such as an item in a bulleted list).

### Content

A concrete example would be if you have several articles about a topic that share a common introduction. Here, we have an article titled “Revealjs Presentations” that wants to include some basic information on presentations not specific to Revealjs (we do that by including `_basics.qmd`). We also have some demo code stored as scripts that we want to include as non-executed examples (we do that by including `_demo.R` and `_demo.py` inside source code blocks):

````markdown
---
title: "Revealjs Presentations"
---

