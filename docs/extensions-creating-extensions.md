## Extensions: Creating Extensions

Source: [Creating Extensions – Quarto](https://quarto.org/docs/extensions/creating.html)

### Overview

Quarto Extensions are a powerful way to modify or extend the behavior of Quarto, and can be created and distributed by anyone. There are several types of extensions available:

| Extension         | Description                                                                                                                                                   |
| :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Shortcodes](https://quarto.org/docs/extensions/shortcodes.html)        | Special markdown directives that generate various types of content. For example, you could create shortcodes to embed tweets or videos in a document.        |
| [Filters](https://quarto.org/docs/extensions/filters.html)           | A flexible and powerful tool for introducing new global behaviors and/or new markdown rendering behaviors. For example, you could create filters to implement output folding, an image carousel, or just about anything you can imagine! |
| [Journal Articles](https://quarto.org/docs/journals/)  | Enable authoring of professional Journal articles using markdown, and produce both LaTeX (PDF) and HTML versions of the articles.                               |
| [Custom Formats](https://quarto.org/docs/extensions/formats.html)    | Create new output formats by bundling together document options, templates, style sheets, and other content.                                                     |
| [Revealjs Plugins](https://quarto.org/docs/extensions/revealjs.html)  | Extend the capabilities of HTML presentations created with Revealjs.                                                                                         |
| [Project Types](https://quarto.org/docs/extensions/project-types.html)   | Create new project project types that bundle together standard content and options, or make it easy to create a website for a custom HTML format.          |
| [Starter Templates](https://quarto.org/docs/extensions/starter-templates.html) | Help users get started with new projects by providing a template and example content. Starter templates aren’t strictly extensions (i.e. they aren’t installed in the `_extensions` directory) but they are often used with custom formats and project types. |
| [Metadata](https://quarto.org/docs/extensions/metadata.html)          | Provide YAML configuration that can be merged into existing Quarto projects.                                                                                   |

### Development

Each type of extension has its own development requirements: in some cases an extension can be created with YAML metadata alone, however in many cases you’ll end up doing some custom scripting using Lua.

These articles provide in-depth documentation on learning and using Lua for extension development:

*   [Lua Development](https://quarto.org/docs/extensions/lua.html) helps you get started with Lua (the language used to create extensions)
*   [Lua API Documentation](https://quarto.org/docs/extensions/lua-api.html) provides documentation on the Pandoc and Quarto Lua APIs used for creating extensions.

### Distribution

There are two distinct ways to distribute extensions to end users:

1.  Publish your extension in a public GitHub repository.
2.  Bundle your extension into a `.zip` or `.tar.gz` archive.

[Distributing Extensions](https://quarto.org/docs/extensions/distributing.html) goes into more depth on how to package and distribute extensions, both on GitHub and using plain gzip archives.

### Examples

The documentation linked to above provides simple motivating examples for each type of extension. Once you understand these, check out the following for more sophisticated examples of each type of extension:

*   The [Quarto Extensions](https://github.com/quarto-ext) GitHub organization provides a set of extensions developed by the core Quarto team. Many of these extensions implement frequently requested features, and all of them provide sound examples of how to implement extensions.
*   The [Quarto Journals](https://github.com/quarto-journals) GitHub organization contains a set of Journal Article formats developed by the core Quarto team or contributed by third parties.
*   Finally, most [published extensions](https://quarto.org/docs/extensions/) are hosted on GitHub and therefore have source code available that you can learn from.

