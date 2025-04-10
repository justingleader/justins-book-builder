## Authoring Contents (`{{< contents >}}` Shortcode)

Source: [contents: Rearrange content in your documents – Quarto](https://quarto.org/docs/authoring/contents.html)

### Overview

Sometimes it’s useful to define content in your document in an order that is different from the order in which you want the document to be presented. Although you can develop [Lua filters](https://quarto.org/docs/extensions/filters.html) that solve this kind of problem, Quarto 1.6 and later offers a simpler solution that works in many use cases: the `{{< contents >}}` shortcode.

Here’s a minimal example of how it can be used:

````markdown
