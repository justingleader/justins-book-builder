## Authoring Shortcodes

Source: [Shortcodes – Quarto](https://quarto.org/docs/authoring/shortcodes.html)

### Overview

Shortcodes are special markdown directives that generate various types of content. Quarto shortcodes are similar in form and function to [Hugo shortcodes](https://gohugo.io/content-management/shortcodes/) and [WordPress shortcodes](https://wordpress.org/support/article/shortcode/).

For example, the following shortcode prints the `title` from document metadata:

```markdown
{{< meta title >}}
```

### Built-in Shortcodes

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

If you want to dive in to creating your own shortcode, check out the article on [Creating Shortcodes](https://quarto.org/docs/extensions/shortcodes.html).

