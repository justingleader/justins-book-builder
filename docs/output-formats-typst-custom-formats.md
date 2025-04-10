## Output Formats: Typst Custom Formats

Source: [Custom Typst Formats – Quarto](https://quarto.org/docs/output-formats/typst-custom.html)

### Overview

When you author a Typst document in Quarto, you’ll be using a Quarto format that is in turn based on a Typst template. The default template provides a basic article layout, but Typst provides an easy way to [define your own templates](https://typst.app/docs/tutorial/making-a-template/) to produce highly customized documents.

Typst templates can be packaged as custom formats for Quarto to allow them to be easily used and shared. On this page, learn about some custom Typst formats available from the Quarto team, as well as how to create your own.

### Custom Formats

You can create highly customized output with Typst by defining a new format based on a custom Typst template. The Typst team has created several useful [templates](https://typst.app/docs/packages/templates/), a few which have been adapted for use with Quarto as custom formats. These formats include:

| Format     | Usage                                                        |
| :--------- | :----------------------------------------------------------- |
| Poster     | `quarto use template quarto-ext/typst-templates/poster`      |
| IEEE       | `quarto use template quarto-ext/typst-templates/ieee`        |
| AMS        | `quarto use template quarto-ext/typst-templates/ams`         |
| Letter     | `quarto use template quarto-ext/typst-templates/letter`      |
| Fiction    | `quarto use template quarto-ext/typst-templates/fiction`     |
| Dept News  | `quarto use template quarto-ext/typst-templates/dept-news`   |

The source code for these formats is available at <https://github.com/quarto-ext/typst-templates>.

### Create a Format

To create a new custom Typst format (or package an existing Typst template for use with Quarto) use the `quarto create` command to get started:

```bash
quarto create extension format
```

Then, choose `typst` as the base format and provide a name for the extension (e.g. `letter`). A sample Typst format extension will be created based on the code used in the default template that ships with Quarto. It will include the following files which you can edit to implement your custom format:

| File                  | Description                                                                                                                               |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| `_extension.yml`      | Basic extension metadata (name, author, description, etc.) and format definition.                                                          |
| `README.md`           | Documentation on how to install and use the format.                                                                                       |
| `template.qmd`        | A starter document that demonstrates the basics of the format.                                                                            |
| `typst-template.typ`  | The core Typst template function (documentation on creating Typst templates can be found here: <https://typst.app/docs/tutorial/making-a-template/>). |
| `typst-show.typ`      | File that calls the template’s function (mapping Pandoc metadata to function arguments).                                                    |

Additional resources you might find useful when creating custom formats include:

*   The official Typst tutorial on [Making a Template](https://typst.app/docs/tutorial/making-a-template/)
*   List of third party templates from the [Awesome Quarto](https://github.com/mcanouil/awesome-quarto#typst-templates) repo.

### Advanced Customization

**Note:** This section covers advanced customization of Typst format output and can be safely ignored unless you have found the method of defining custom Typst formats described above too limited.

Above we describe a method of creating a Typst format based on specifying two [template partials](https://quarto.org/docs/journals/templates.html#template-partials) (`typst-template.typ` and `typst-show.typ`). These partials customize components of the default Typst Pandoc template, but leave some of the core scaffolding including definitions required by Pandoc for its Typst output as well as handling of bibliographies and footnotes (this means that your own custom Typst formats do not need to explicitly handle them).

If you would like to fully override the Pandoc template used for rendering Typst, use the `template` option in your custom format (rather than `template-partials`) and provide an alternate implementation of the default template. For example, your `_extensions.yml` might look like this:

**_extensions.yml**
```yaml
title: Typst Custom Format
author: Jane Smith
version: "0.2.0"
quarto-required: ">=1.4.11"

contributes:
  formats:
    typst:
      template: template.typ
      template-partials:
        - typst-template.typ
        - typst-show.typ
```

Use the [source code](https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/formats/typst/pandoc/template.typ) of the default template as a starting point for your `template.typ`. Note that you can call all of the template partials provided by Quarto (e.g. `biblio.typ()` or `notes.typ()`) from within your custom template implementation.

The [AMS](https://github.com/quarto-ext/typst-templates/tree/main/_extensions/ams) format provides an example of redefining the main template (in that case, it is to prevent automatic bibliography processing by Quarto in deference to the built-in handling of the Typst AMS template).

