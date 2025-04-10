## Heading

This filter adds formatting to heading text.
```

Note that the value provided to `filters` in `example.qmd` should be the name of the extension (`fancy-header`), not the filename of the filter (`fancy-header.lua`). This allows you to bundle more than one filter in your extension:

**_extensions/fancy-header/_extension.yml**
```yaml
contributes:
  filters:
    - fancy-header.lua
    - make-fancier.lua
```

All of filters in your extension will be applied when a user uses your extension in their document.

To develop your filter, render/preview `example.qmd`, and then make changes to `fancy-header.lua` (the preview will automatically refresh when you change `fancy-header.lua`).

#### Development

To learn more about developing filter extensions:

*   If necessary, brush up on [Lua Development](https://quarto.org/docs/extensions/lua.html) (Lua is the language used to create filters).
*   Review the Pandoc documentation on [Writing Lua Filters](https://pandoc.org/lua-filters.html).
*   Read the [Lua API Reference](https://quarto.org/docs/extensions/lua-api.html), which describes the Lua extension API for Quarto.
*   If you want to write a JSON filter, see the documentation on [Writing JSON filters](https://pandoc.org/filters.html#json-filters).
*   To create a new filter extension, use the `quarto create extension filter` command as described above.

#### Distribution

If your extension source code is located within a GitHub repository, then it can be added to a project by referencing the GitHub organization and repository name. For example:

```bash
# target the current HEAD of the extension
quarto add cooltools/output-folding

# target a branch or tagged release of the extension
quarto add cooltools/output-folding@v1.2
quarto add cooltools/output-folding@bugfix-22
```

Note that it is possible to bundle and distribute extensions as simple gzip archives (as opposed to using a GitHub repository as described above). See the article on [Distributing Extensions](https://quarto.org/docs/extensions/distributing.html) for additional details.

#### Examples

You might also find it instructive to examine the source code of these filter extensions authored by the Quarto team:

| Extension name      | Description                                             |
| :------------------ | :------------------------------------------------------ |
| [latex-environment](https://github.com/quarto-ext/latex-environment) | Quarto extension to output custom LaTeX environments.   |
| [lightbox](https://github.com/quarto-ext/lightbox)          | Create lightbox treatments for images in your HTML documents. |

