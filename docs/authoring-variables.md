## Authoring Variables

Source: [Variables – Quarto](https://quarto.org/docs/authoring/variables.html)

### Overview

There are a number of ways to include dynamic variables within documents rendered by Quarto. This is useful for externalizing content that varies depending on context, or as an alternative to repeating a value in multiple places (e.g. a version number).

For example, the following prints the `title` from document metadata:

```markdown
{{< meta title >}}
```

The `{{< meta >}}` syntax used here is an example of a [shortcode](https://quarto.org/docs/authoring/shortcodes.html). Quarto supports the following shortcodes for dynamic variables:

| Shortcode | Description                             |
| :-------- | :-------------------------------------- |
| `var`     | Value from `_variables.yml` file        |
| `meta`    | Value from document metadata            |
| `env`     | Value of System environment variable    |

### var

If you are using a Quarto project, the `var` shortcode enables you to insert content from a project-level `_variables.yml` file. Create this file alongside your `_quarto.yml` project file, and then include references to those variables within any document in your project.

Variables can be either simple values or markdown content. To define variables, create a `_variables.yml` file in the root directory of your project. For example:

```yaml
# _variables.yml
version: 1.2

email:
  info: info@example.com
  support: support@example.com

engine:
  jupyter: "[Jupyter](https://jupyter.org)"
  knitr: "[Knitr](https://yihui.name/knitr)"
```

Note that the `engine` variable values include markdown for hyperlinks. Any markdown provided needs to be well-formed, and cannot change the structure of the content around it (e.g. by closing a div opened before the variable inclusion).

To include the value of a variable, use the `{{< var >}}` shortcode, for example:

```markdown
Version {{< var version >}} is a minor upgrade.

Please contact us at {{< var email.info >}}.

Quarto includes {{< var engine.jupyter >}} and
{{< var engine.knitr >}} computation engines.
```

### meta

The `meta` shortcode allows you to insert content from Pandoc metadata (e.g. YAML at the top of the document and/or in `_quarto.yml`).

For example, the following shortcode inserts the value of the `title` field from YAML metadata:

```markdown
{{< meta title >}}
```

You can dereference sub-keys using the dot (`.`) delimiter. For example:

```markdown
{{< meta labels.description >}}
```

You can also index into an array with the dot (`.`) delimiter. For example, to extract the first in the array of authors:

```markdown
{{< meta author.1 >}}
```

To reference a field that contains a dot (`.`), escape the dot with a double backslash (`\\`). For example, to get `field.with.dots`:

```markdown
{{< meta field\\.with\\.dots >}}
```

### env

The `env` shortcode enables you to read values from environment variables. For example:

```markdown
Version {{< env PRODUCT_VERSION >}} is a minor upgrade.
```

You can provide a fallback value if the environment variable isn’t set by providing a second argument:

```markdown
Version {{< env PRODUCT_VERSION "*.*" >}} is a minor upgrade.
```

You can read more about setting environment variables in Quarto projects in [Environment Variables](https://quarto.org/docs/projects/environment-variables.html).

### Escaping

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

