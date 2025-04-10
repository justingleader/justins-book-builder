## Extensions: Starter Templates

Source: [Starter Templates – Quarto](https://quarto.org/docs/extensions/starter-templates.html)

### Overview

Starter templates provide a straightforward way for users to get started with new Quarto projects by providing example content and options. You might use starter templates to:

*   Create a working initial document for [Journal Articles](https://quarto.org/docs/journals/) or [Custom Formats](https://quarto.org/docs/extensions/formats.html).
*   Provide the initial content for a custom [Project Type](https://quarto.org/docs/extensions/project-types.html).
*   Scaffold a standard form of data analysis project used by your organization.

Starter templates are essentially just GitHub repositories that are copied to a new directory on the user’s system. As we’ll describe below in [Extensions & Templates](#extensions--templates), often times the repository for a custom format is also used as a starter template.

### Creating a Template

To create a starter template, just create a GitHub repository that includes the files you want copied into projects created with the template. All of the files in the repository are copied except for:

*   Hidden files (any file or directory name that starts with `.` (e.g. `.gitignore`).
*   Common GitHub repository files like `README.md` and `LICENSE`.

If you’d like, you can also include a `.quartoignore` file in the root of your repository listing other files or directories you’d like to exclude. Each line of the file should be a glob describing file(s) to ignore (using syntax like a `.gitignore` file).

#### template.qmd

There is one special file you’ll typically want to include in templates that target creation of documents (as opposed to projects): `template.qmd`. There are two reasons to include a `template.qmd`:

1.  It provides an easy way to test that your template is working as expected.
2.  When the template is copied into the target directory, the `template.qmd` will automatically be renamed to match the name that the user provided for the directory.

If you are creating a template that targets creation of a website or book, a `template.qmd` is generally not necessary (as the `index.qmd` file already serves this purpose).

### Using a Template

Once you’ve created the template repository and pushed it to GitHub, it can be instantiated with the following command:

```bash
quarto use template cooltools/cool-project
```

This command copies the contents of the GitHub repository at `https://github.com/cooltools/cool-project` to the local system (excluding selected files as discussed above).

If the command is run in an empty directory, the user will be prompted whether they’d like to use the existing directory or create a new directory. If the command is run in a directory which contains other files or directories, they’ll be prompted for the name of a directory to create.

### Extensions & Templates {#extensions--templates}

When creating [Journal Articles](https://quarto.org/docs/journals/), [Custom Formats](https://quarto.org/docs/extensions/formats.html), or [Project Type](https://quarto.org/docs/extensions/project-types.html) extensions, we recommend that you additionally provide a starter template to make it easy for users to get started.

This is generally as easy as adding a `template.qmd` file to your extension that demonstrates its use. With this configuration, users can either begin using your extension via the template or by a conventional `quarto install` of the extension.

For example, consider the [ACM](https://github.com/quarto-journals/acm) Journal Article extension. The extension repository supports *either* getting started with a template:

```bash
quarto use template quarto-journals/acm
```

Alternatively, you can add the format (without the template) into an existing project or directory:

```bash
quarto add quarto-journals/acm
```

