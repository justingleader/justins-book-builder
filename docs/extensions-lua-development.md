## Extensions: Lua Development

Source: [Lua Development – Quarto](https://quarto.org/docs/extensions/lua.html)

### Overview

The programming language used to create [filters](https://quarto.org/docs/extensions/filters.html) and [shortcodes](https://quarto.org/docs/extensions/shortcodes.html) is Lua, a lightweight, high-level scripting language. [Lua](https://www.lua.org/) is the extension language for Pandoc (which includes an embedded Lua interpreter). This means that Quarto extensions have no additional runtime dependencies or requirements.

This article will start by providing an orientation to learning Lua for those new to the language. Then, we’ll provide some tips for productive Lua development.

See the [Lua API Reference](https://quarto.org/docs/extensions/lua-api.html) for additional details on the APIs available for developing extensions.

### Learning Lua

Lua is a scripting language similar to Python, R, Julia, and JavaScript. If you are familiar with one or more of those languages you won’t have trouble picking up Lua.

Here is a recommended approach for learning Lua for use with Quarto:

1.  Read [Learn Lua in 15 Minutes](https://learnxinyminutes.com/docs/lua/) for a quick overview of the language and its syntax.
2.  Check out the first two sections of the [Pandoc Lua Filters](https://pandoc.org/lua-filters.html) documentation then skip ahead to the [Filter Examples](https://pandoc.org/lua-filters.html#examples) section to make things a bit more concrete.
3.  Once you have the basic idea of Lua and filters, get a more complete picture by skimming the full [Pandoc Lua Filters](https://pandoc.org/lua-filters.html) documentation. You won’t understand everything, but it’s a good orientation to all of the moving parts.
4.  Finally, check out the source code of the extensions published in the [Quarto Extensions](https://github.com/quarto-ext) GitHub organization (these are extensions maintained by the Quarto core team). Once you are able to read and understand that code you are ready to start developing your own extensions!

Some additional learning resources you might find useful include:

*   [Lua Quick Reference](https://github.com/rjpcomputing/luaquickref): PDF with a compact summary of the language and base library.
*   [Programming in Lua](https://www.lua.org/pil/contents.html): book by Roberto Ierusalimschy, the chief architect of the language.
*   [Lua Reference Manual](https://www.lua.org/manual/5.3/): complete definition of the language and base library.

### Development Tools

#### Quarto Preview

Quarto preview, `quarto preview`, is aware of Lua source files within extensions, and will automatically reload the preview whenever a Lua source file changes.

This makes it very easy to incrementally develop and debug Lua code (especially when combined with the [`native` format](#native-format) a described below). Live reloading for Lua files will work no matter what source code editor you are using (VS Code, RStudio, Neovim, etc.).

#### VS Code

While you can use any text editor along with `quarto preview` for developing Lua extensions, we strongly recommend that you consider using VS Code, as it provides a number of additional tools including:

*   Code completion and type checking.
*   Diagnostics for various common problems with code.
*   The ability to add types to your own functions.

Code completion covers the Lua base library as well as the Pandoc and Quarto Lua APIs, and also provides documentation on hover:

![VS Code Lua Completion](https://quarto.org/docs/extensions/images/lua-completion.png)

Diagnostics check for many common errors including failing to check for `nil`, undefined global values, shadowing of local variables, unused functions, etc.

![VS Code Lua Diagnostics](https://quarto.org/docs/extensions/images/lua-diagnostics.png)

##### Installation

To get started with using VS Code for Lua extension development, install the following software:

1.  Install the latest version (v1.2 or greater) of [Quarto](https://quarto.org/docs/download/)
2.  Install the latest version (v1.40.0 or greater) of the [Quarto VS Code Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto).
3.  For Lua code intelligence, install the [Lua LSP VS Code Extension](https://marketplace.visualstudio.com/items?itemName=sumneko.lua).

Once you’ve installed these components you should see the features described above appear automatically in your Quarto workspaces that include Lua code.

There are many options available for configuring Lua completion and diagnostics. It’s also possible to provide type information for your own functions. See the section on [Lua in VS Code](#lua-in-vs-code) below for details.

#### Diagnostic Logging

Use the functions in the `quarto.log` module to add diagnostic logging to your extension. You can use both temporary logging calls to debug a particular problem as well as add logging calls that are always present but only activated when the `--trace` flag is passed to `quarto render` or `quarto preview`.

The `quarto.log` module is based on the [pandoc-lua-logging](https://github.com/pandoc-ext/pandoc-lua-logging) project from [@wlupton](https://github.com/wlupton). You’ll recognize the functions described below from that module (e.g. `logging.output()`, `logging.warning()`, etc). For documentation on using all of the logging functions see the project [README](https://github.com/pandoc-ext/pandoc-lua-logging) file.

##### quarto.log.output

To log any object (including Pandoc AST elements), you the `quarto.log.output()` function. For example, here we log the `Div` passed to us in our filter callback function as well as some diagnostic text:

**filter.lua**
```lua
function Header(el)
  quarto.log.output("=== Handling Header ===")
  quarto.log.output(el)
end
```

This is log output you’d see in the terminal when the filter is executed:

```
=== Handling Header ===
Header {
  attr: Attr {
    attributes: AttributeList {}
    classes: List {}
    identifier: "section-one"
  }
  content: Inlines {
    [1] Str "Section"
    [2] Space
    [3] Str "One"
  }
  level: 2
}
```

##### quarto.log.warning

Use the `quarto.log.warning()` function to output warnings that can be suppressed with the `--quiet` flag:

**filter.lua**
```lua
function RawBlock(el)
  if el.format == "html" then
    quarto.log.warning("Raw HTML not supported")
    return pandoc.Null()
  end
end
```

For example, the warning above will not appear for this call to `quarto render`:

```bash
quarto render document.qmd --quiet
```

##### quarto.log.debug

Use the `quarto.log.debug()` function to write output whenever the `--trace` flag is present:

**filter.lua**
```lua
function Header(el)
  quarto.log.debug("Header: " .. el.identifier)
end
```

For example, the debug message will appear for this call to `quarto preview`:

```bash
quarto preview document.qmd --trace
```

You can keep these calls in your filter since they won’t produce output unless `--trace` is specified.

#### Native Format {#native-format}

A great tool for understanding the behavior of a Lua filter or shortcode in more depth is to target the `native` format (as opposed to `html`, `pdf`, etc.). The `native` format will show you the raw contents of the Pandoc AST. For example, here’s a simple markdown document alongside it’s `native` output:

**document.qmd**
```yaml
---
format: native
---

