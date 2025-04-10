## Extensions: Creating Filters

Source: [Creating Filters – Quarto](https://quarto.org/docs/extensions/filters.html)

### Overview

If the base features of Pandoc and Quarto don’t do exactly what you need, you can very likely create a [Pandoc Filter](https://pandoc.org/filters.html) that bridges the gap.

Pandoc consists of a set of readers and writers. When converting a document from one format to another, text is parsed by a reader into pandoc’s intermediate representation of the document—an “abstract syntax tree” or AST—which is then converted by the writer into the target format. The pandoc AST format is defined in the module [`Text.Pandoc.Definition`](https://hackage.haskell.org/package/pandoc-types/docs/Text-Pandoc-Definition.html) in the pandoc-types package.

A “filter” is a program that modifies the AST, between the reader and the writer.

```
INPUT --reader--> AST --filter--> AST --writer--> OUTPUT
```

Pandoc’s built-in citation processing is implemented as a filter, as are many of Quarto’s internal extensions (e.g. cross-references, figure layout, etc.).

You can write Pandoc filters using Lua (via Pandoc’s built-in Lua interpreter) or using any other language using a JSON representation of the Pandoc AST piped to/from an external process. We strongly recommend using Lua Filters, which have the following advantages:

*   No external dependencies
*   High performance (no serialization or process execution overhead)
*   Access to the [Pandoc](https://pandoc.org/lua-filters.html) and [Quarto](https://quarto.org/docs/extensions/lua-api.html) libraries of Lua helper functions.

### Activating Filters

If you’ve developed a filter and want to use it within a document you need to add it to the list of `filters` for the document. For example, here we arrange for the `spellcheck` filter to run:

```yaml
---
filters:
  - spellcheck.lua
---
```

By default, user filters are run before Quarto’s built-in filters. For some filters you’ll want to modify this behavior. For example, here we arrange to run `spellcheck` before Quarto’s filters and `fontawesome` after:

```yaml
filters:
  - spellcheck.lua
  - quarto
  - fontawesome
```

You’ll notice that one of the extensions (`spellcheck.lua`) has a file extension and the other (`fontawesome`) does not. This difference stems from how the extensions are distributed: an extension distributed as a plain Lua file uses `.lua` whereas a filter distributed as a [Quarto Extension](https://quarto.org/docs/extensions/) does not. The next section explores how to create filters as extensions.

### Filter Extensions

#### Quick Start

Here we’ll describe how to create a simple filter extension. We’ll use the `quarto create` command to do this. If you are using VS Code or RStudio you should execute `quarto create` within their respective integrated Terminal panes.

To get started, execute `quarto create extension filter` within the parent directory where you’d like the filter extension to be created:

```bash
$ quarto create extension filter
? Extension Name › fancy-header
```

As shown above, you’ll be prompted for an extension name. Type `fancy-header` and press Enter—the filter extension is then created:

```
Creating extension at /Users/jjallaire/quarto/dev/fancy-header:
- Created README.md
- Created _extensions/fancy-header/_extension.yml
- Created _extensions/fancy-header/fancy-header.lua
- Created .gitignore
- Created example.qmd
```

If you are running within VS Code or RStudio a new window will open with the extension project.

Here’s what the contents of the files in `_extensions/fancy-header/` look like:

**_extensions/fancy-header/_extension.yml**
```yaml
title: Fancy-header
author: J.J. Allaire
version: 1.0.0
quarto-required: ">=99.9.0"
contributes:
  filters:
    - fancy-header.lua
```

**_extensions/fancy-header/fancy-header.lua**
```lua
-- Reformat all heading text
function Header(el)
  el.content = pandoc.Emph(el.content)
  return el
end
```

Finally, the `example.qmd` file includes code that exercises the extension. For example:

**example.qmd**
```yaml
---
title: "Fancy-header Example"
filters:
  - fancy-header
---

