## Authoring Conditional Content

Source: [Conditional Content – Quarto](https://quarto.org/docs/authoring/conditional.html)

In some cases you may want to create content that only displays for a given output format (or only displays when *not* rendering to a format). You can accomplish this by creating divs, spans and code blocks with the `.content-visible` and `.content-hidden` classes.

### .content-visible

To make content visible only for a given format, you can create a div (`:::`) with the `.content-visible` class. For example, here we mark content as only visible in HTML:

```markdown
::: {.content-visible when-format="html"}
Will only appear in HTML.
:::
```

You can also set conditions on non-executable code blocks:

````markdown
```{.python .content-visible when-format="html"}
# code shown only in HTML
2 + 2
```
````

To apply a condition only to a part of a paragraph, use a span (`[]{}`):

```markdown
Some text [in HTML.]{.content-visible when-format="html"} [in PDF.]{.content-visible when-format="pdf"}
```

You can also mark content as visible for all formats *except* a specified format. For example:

```markdown
::: {.content-visible unless-format="pdf"}
Will not appear in PDF.
:::
```

Then `when-format` and `unless-format` attributes match the current Pandoc output format with some additional intelligence to alias related formats (e.g. html, html4, and html5). Details are provided below in [Format Matching](#format-matching).

`when-format` and `unless-format` can also be combined to create more complex conditions:

```markdown
::: {.content-visible when-format="html" unless-format="revealjs"}
Will only appear in HTML and not in Reveal.js, but actually it appears.
:::

::: {.content-visible when-format="revealjs"}
Will only appear in Reveal.js and not in HTML or other formats.
:::
```

### .content-hidden

To prevent content from being displayed when rendering to a given format, use the `.content-hidden` class. For example, here we mark content as hidden in HTML:

```markdown
::: {.content-hidden when-format="html"}
Will not appear in HTML.
:::
```

You can also mark content as hidden for all formats *except* a specified format. For example:

```markdown
::: {.content-hidden unless-format="pdf"}
Will only appear in PDF.
:::
```

### Format Matching

The `when-format` and `unless-format` clauses do some aliasing of related formats to make it more straightforward to target content. The following aliases are implemented:

| Alias     | Formats                                                   |
| :-------- | :-------------------------------------------------------- |
| `latex`   | `latex`, `pdf`                                            |
| `pdf`     | `latex`, `pdf`                                            |
| `epub`    | `epub*`                                                   |
| `html`    | `html*`, `epub*`, `revealjs`                              |
| `html:js` | `html*`, `revealjs`                                       |
| `markdown`| `markdown*`, `commonmark*`, `gfm`, `markua`               |

Note that the `html:js` alias indicates that the target format is capable of executing JavaScript (this maps to all HTML formats save for ePub).

### Matching against metadata

It’s possible to match against boolean metadata values. Use the attributes `unless-meta` and `when-meta`, and use periods `.` to separate metadata keys. For example:

```markdown
::: {.content-hidden unless-meta="path.to.metadata"}
This content will be hidden unless there exists a metadata entry like such:

```yaml
path:
  to:
    metadata: true
```
:::
```

This feature is often useful alongside [project profiles](https://quarto.org/docs/projects/profiles.html). Different profiles can set different metadata values, and so can control the metadata used in conditional content.

