## Extensions: Creating Shortcodes

Source: [Creating Shortcodes – Quarto](https://quarto.org/docs/extensions/shortcodes.html)

This article describes how to create your own shortcodes.

### Overview

Shortcodes are special markdown directives that generate various types of content. Quarto shortcodes are similar in form and function to [Hugo shortcodes](https://gohugo.io/content-management/shortcodes/) and [WordPress shortcodes](https://wordpress.org/support/article/shortcode/).

For example, the following shortcode prints the `title` from document metadata:

```markdown
{{< meta title >}}
```

#### Built-in Shortcodes

Quarto supports several shortcodes natively:

| Shortcode     | Description                                 |
| :------------ | :------------------------------------------ |
| `var`         | Print value from `_variables.yml` file    |
| `meta`        | Print value from document metadata          |
| `env`         | Print system environment variable           |
| `pagebreak`   | Insert a native page-break                  |
| `kbd`         | Describe keyboard shortcuts                 |
| `video`       | Embed a video in a document                 |
| `include`     | Include contents of another qmd             |
| `embed`       | Embed cells from a Jupyter Notebook         |
| `placeholder` | Add placeholder images to your document     |
| `lipsum`      | Add placeholder text to your document       |
| `contents`    | Rearrange content in your document          |

### Quick Start

Here we’ll describe how to create a simple shortcode extension. We’ll use the `quarto create` command to do this. If you are using VS Code or RStudio, you should execute `quarto create` within their respective integrated terminal panes.

To get started, execute `quarto create extension shortcode` within the parent directory where you’d like the shortcode extension to be created:

```bash
$ quarto create extension shortcode
? Extension Name › shorty
```

As shown above, you’ll be prompted for an extension name. Type `shorty` and press Enter—the shortcode extension is then created:

```
Creating extension at /Users/jjallaire/extensions/shorty/shorty:
- Created README.md
- Created _extensions/shorty/shorty.lua
- Created _extensions/shorty/_extension.yml
- Created .gitignore
- Created example.qmd
```

If you are running within VS Code or RStudio, a new window will open with the extension project.

Here’s what the contents of the files in `_extensions/shorty/` look like:

**_extensions/shorty/_extension.yml**
```yaml
title: Shorty
author: J.J. Allaire
version: 1.0.0
quarto-required: ">=1.2.222"
contributes:
  shortcodes:
    - shorty.lua
```

**_extensions/shorty/shorty.lua**
```lua
return {
  ['shorty'] = function (args, kwargs, meta)
    return pandoc.Str("Hello from Shorty!")
  end
}
```

Finally, the `example.qmd` file includes code that exercises the extension. For example:

**example.qmd**
```yaml
---
title: "Shorty Example"
---

{{< shorty >}}
```

To develop your shortcode, render/preview `example.qmd`, and then make changes to `shorty.lua` (the preview will automatically refresh when you change `shorty.lua`).

### Development

Shortcodes are created using Lua. If you aren’t familar with Lua (or with Pandoc filters), here are some resources to help you along:

*   [Lua Development](https://quarto.org/docs/extensions/lua.html) (Lua is the language used to create shortcodes).
*   [Lua API Reference](https://quarto.org/docs/extensions/lua-api.html), which describes the Lua extension API for Quarto.

Shortcodes are implemented as Lua functions that take one or more arguments and return a Pandoc AST node (or list of nodes).

Here’s the implementation of the `env` shortcode that is built in to Quarto:

**env.lua**
```lua
function env(args)
  local var = pandoc.utils.stringify(args[1])
  local value = os.getenv(var)
  if value ~= nil then
    return pandoc.Str(value)
  else
    return pandoc.Null()
  end
end
```

Note that arguments to shortcodes are provided in `args` (a 1-dimensional array), and that each argument is a list of Pandoc inlines (i.e. markdown AST parsed from the text).

We use the `pandoc.utils.stringify()` function to convert the inlines to an ordinary string, and then the `os.getenv()` function to get its value.

You would use this shortcode as follows:

```markdown
{{< env HOME >}}
```

### Distribution

If your extension source code is located within a GitHub repository, then it can be installed by referencing the GitHub organization and repository name. For example:

```bash
# install the current HEAD of the extension
quarto add cooltools/shorty

# install a branch or tagged release of the extension
quarto add cooltools/shorty@v1.2
quarto add cooltools/shorty@bugfix-22
```

Note that it is possible to bundle and distribute extensions as simple gzip archives (as opposed to using a GitHub repository as described above). See the article on [Distributing Extensions](https://quarto.org/docs/extensions/distributing.html) for additional details.

### Examples

You might find it instructive to examine the source code of these shortcode extensions authored by the Quarto team:

| Extension    | Description                                                                          |
| :----------- | :----------------------------------------------------------------------------------- |
| [fancy-text](https://github.com/quarto-ext/fancy-text) | Output nicely formatted versions of fancy strings such as LaTeX and BibTeX in multiple formats. |
| [fontawesome](https://github.com/quarto-ext/fontawesome)| Use Font Awesome icons in HTML and PDF documents.                                      |
| [video](https://github.com/quarto-ext/video)        | Embed videos in HTML documents and Revealjs presentations.                           |

Some additional annotated examples are provided below.

#### Raw Output

Shortcodes can tailor their output to the format being rendered to. This is often useful when you want to conditionally generate rich HTML output but still have the same document render properly to PDF or MS Word.

The `pagebreak` shortcode generates “native” pagebreaks in a variety of formats. Here’s the implementation of `pagebreak`:

**pagebreak.lua**
```lua
function pagebreak()
  local raw = {
    epub = '<p style="page-break-after: always;"> </p>',
    html = '<div style="page-break-after: always;"></div>',
    latex = '\\newpage{}',
    ooxml = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>',
    odt = '<text:p text:style-name="Pagebreak"/>',
    context = '\\page'
  }
  if quarto.doc.isFormat('docx') then
    return pandoc.RawBlock('openxml', raw.ooxml)
  elseif quarto.doc.isFormat('pdf') then
    return pandoc.RawBlock('tex', raw.latex)
  elseif quarto.doc.isFormat('odt') then
    return pandoc.RawBlock('opendocument', raw.odt)
  elseif quarto.doc.isFormat('epub') then
    return pandoc.RawBlock('html', raw.epub)
  elseif quarto.doc.isFormat('html') then
    return pandoc.RawBlock('html', raw.html)
  elseif quarto.doc.isFormat('context') then
    return pandoc.RawBlock('context', raw.context)
  else
    -- fall back to insert a form feed character
    return pandoc.Para{pandoc.Str '\f'}
  end
end
```

We use the `pandoc.RawBlock()` function to output the appropriate raw content for the target format. Note that raw blocks are passed straight through to the output file and are not processed as markdown.

You’d use this shortcode as follows:

```markdown
{{< pagebreak >}}
```

#### Named Arguments

The examples above use either a single argument (`env`) or no arguments at all (`pagebreak`). Here we demonstrate named argument handling by implementing a `git-rev` shortcode that prints the current git revision, providing a `short` option to determine whether a short or long SHA1 value is displayed:

**git.lua**
```lua
-- run git and read its output
function git(command)
  local p = io.popen("git " .. command)
  local output = p:read('*all')
  p:close()
  return output
end

-- return a table containing shortcode definitions
-- defining shortcodes this way allows us to create helper
-- functions that are not themselves considered shortcodes
return {
  ["git-rev"] = function (args, kwargs)
    -- command line args
    local cmdArgs = ""
    local short = pandoc.utils.stringify(kwargs["short"])
    if short == "true" then
      cmdArgs = cmdArgs .. "--short "
    end

    -- run the command
    local cmd = "rev-parse " .. cmdArgs .. "HEAD"
    local rev = git(cmd)

    -- return as string
    return pandoc.Str(rev)
  end
}
```

There are some new things demonstrated here:

1.  Rather than defining our shortcode functions globally, we return a table with the shortcode definitions. This allows us to define helper functions that are not themselves registered as shortcodes. It also enables us to define a shortcode with a dash (`-`) in its name.
2.  There is a new argument to our shortcode handler: `kwargs`. This holds any named arguments to the shortcode. As with `args`, values in `kwargs` will always be a list of Pandoc inlines (allowing you to accept markdown as an argument). Since `short` is a simple boolean value we need to call `pandoc.utils.stringify()` to treat it as a string and then compare it to `"true"`.

We’d use this shortcode as follows:

```markdown
---
title: "My Document"
---

{{< git-rev >}}

{{< git-rev short=true >}}
```

#### Metadata Options

In some cases you may want to provide options that affect how your shortcode behaves. There is a third argument to shortcode handlers (`meta`) that provides access to document and/or project level metadata.

Let’s implement a different version of the `git-rev` shortcode that emits the revision as a link to GitHub rather than plain text. To do this, we make use of `github.owner` and `github.repo` metadata values:

**git.lua**
```lua
function git(command)
  local p = io.popen("git " .. command)
  local output = p:read('*all')
  p:close()
  return output
end

return {
  ["git-rev"] = function (args, kwargs, meta)
    -- run the command
    local rev = git("rev-parse HEAD")

    -- target repo
    local owner = pandoc.utils.stringify(meta["github.owner"])
    local repo = pandoc.utils.stringify(meta["github.repo"])
    local url = "https://github.com/" .. owner .. "/" .. repo .. "/" .. rev

    -- return as link
    return pandoc.Link(pandoc.Str(rev), url)
  end
}
```

As with `args` and `kwargs`, `meta` values are always provided as a list of Pandoc inlines, so often need to be converted to string using `pandoc.utils.stringify()`.

To use this shortcode in a document, we provide the GitHub info as document options, then include the shortcode where we want the link to be:

```yaml
---
title: "My Document"
github:
  owner: quarto-dev
  repo: quarto-cli
---

{{< git-rev >}}
```

The shortcode registration and GitHub metadata could just as well been provided in a project-level `_quarto.yml` file or a directory-level `_metadata.yml` file.

#### Raw Arguments

In Quarto >= 1.3, you can also access the raw stream of inlines passed to a shortcode by adding a `raw_args` parameter. For example:

```lua
function shorty(args, kwargs, meta, raw_args)
  -- ...
end
```

#### Context Awareness

In Quarto >= 1.5, you can access the context in which the shortcode was invoked as the fifth parameter of the function call. `context` is a string that will be one of `block`, `inline`, or `text`:

*   if `context` is `block`, then the shortcode exists in a block by itself
*   if `context` is `inline`, then the shortcode exists as one of many inline nodes
*   if `context` is `text`, then the shortcode exists inside a text field of a Pandoc node. These can be:
    *   the content of `CodeBlock` or `Code` elements
    *   the content of `RawBlock` or `RawInline` elements
    *   the content of attributes of Pandoc elements like `Div`, `Span`, etc.
    *   the URL of a `Link` element
    *   the source of an `Image` element

```lua
function shorty(args, kwargs, meta, raw_args, context)
  -- ...
end
```

#### Escaping

If you are writing documentation about using variable shortcodes (for example, this article!) you might need to prevent them from being processed. You can do this in two ways:

1.  Escape the shortcode reference with extra braces like this:

    ```markdown
    {{{< var version >}}}
    ```

2.  Add a `shortcodes=false` attribute to any code block you want to prevent processing of shortcodes within:

    ````markdown
    ```{shortcodes=false}
    {{< var version >}}
    ```
    ````

