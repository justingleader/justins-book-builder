## Extensions: Distributing Extensions

Source: [Distributing Extensions – Quarto](https://quarto.org/docs/extensions/distributing.html)

### Overview

Quarto extensions are directories that contain an `_extensions` sub-directory with one or more extensions. The files above the `_extensions` directory are not installed, so typically contain README and LICENSE files, examples, test cases, etc.

There are two distinct ways to distribute extensions to end users:

1.  Publish your extension in a public GitHub repository.
2.  Bundle your extension into a `.zip` or `.tar.gz` archive.

Each method has benefits and drawbacks that will be explored below. First we’ll cover the basic file structure and contents of an extension.

### Extension Contents

Quarto Extensions are directories that contain an `_extensions` folder that contains one or more extension contributions. While the most common case is the distribution of a single extension, it is possible to create a single extension directory that includes multiple shortcodes, multiple filters, or a combination of both.

Here is the contents of an extension named `my-filter`:

```
README.md
LICENSE
example.qmd
_extensions/
  my-filter/
    _extension.yml
    my-filter.lua
```

Note that the only thing strictly required is the `_extensions` directory (anything above that is for your own purposes and is ignored during installation). Even so, it’s good practice to include a `README.md` and `LICENSE` file, and the `example.qmd` will be useful for developing your extension.

#### _extension.yml

Each extension is defined by its `_extension.yml` file which contains the metadata about the extension as well as the what items it contributes when used. For example, here is the `_extension.yml` for a filter extension:

```yaml
title: My Filter
author: Cooltools
version: 1.0.0
quarto-required: ">=1.2.0"
contributes:
  filters:
    - my-filter.lua
```

Here are all of the fields that can be specified in the `_extension.yml` file:

| Field            | Description                                                                                                                                                            |
| :--------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`          | The extension’s name                                                                                                                                                   |
| `author`         | The author of the extension                                                                                                                                            |
| `version`        | A semantic version number this release. When installing, updating, or releasing an extension, this version number will be used to present a summary of actions to the user. |
| `quarto-required`| A semantic version number indicating the minimum quarto version required to run this extension.                                                                          |
| `contributes`    | The items that this extension will contribute to the render. These are allowed subkeys: `shortcodes`, `filters`, `formats`                                                 |

**Note:** The `version` field is checked for conformity to [semantic versioning](https://semver.org/). For example, valid `version` values would be: `1.0.0`, `2.3.4-alpha`, `1.2.3-beta+build567`, `3.0.0-alpha.2`, `4.2.1+build.987`. Invalid `version` values would be: `1.2` (missing patch version), `1.2.3.4` (extra version segment), `1.2.3-beta.5+build` (missing build metadata identifier).

### GitHub Distribution

Distributing extensions on GitHub has a number of benefits, including compact syntax (e.g. `quarto add org-name/extension`), the use of organizations as a “namespace” for managing name conflicts, and the ability to target specific releases or tags.

For example, the extensions in the `quarto-ext` GitHub organization can be added to a project with these commands:

```bash
quarto add quarto-ext/lightbox
quarto add quarto-ext/fontawesome
```

By default, extensions are added from the `HEAD` of the `main` branch of the repository. You can also target tags and/or branches in your repository by including an `@` after the repository name. For example:

```bash
quarto add quarto-ext/lightbox@v1.2
quarto add quarto-ext/lightbox@bugfix-22
```

Extensions added from GitHub have another special property: the GitHub organization can be used as a namespace qualifier to disambiguate extensions that have the same name. For example, if you have two different `lightbox` extensions in your project, you explicitly specify the `quarto-ext` one as follows:

```yaml
---
filters:
  - quarto-ext/lightbox
---
```

You can also add an extension from a subdirectory of a GitHub repository. For example, here we install two different extensions from the `cooltools/icons` repository:

```bash
quarto add cooltools/icons/fontawesome
quarto add cooltools/icons/iconify
```

### Archive Distribution

Distributing extensions as a `.zip` or `.tar.gz` archive has the benefit of not requiring public distribution. These extensions can also be added directly from non-GitHub version control services using the archive URLs normally provided for repositories.

Note that unlike GitHub hosted extensions, extensions installed from archives do not have an organizational namespace (they all share a single namespace).

#### Git Repositories

To add an extension to a project from a GitLab repository you could do this:

```bash
quarto add https://gitlab.com/cooltools/shorty/-/archive/main/shorty-main.zip
```

You’ll note that the above URL references the `main` branch. You can similarly target any other branch, tag, or release. For example, to add an extension using the `v1.0` tag:

```bash
quarto add https://gitlab.com/cooltools/shorty/-/archive/v1.0/shorty-main.zip
```

If you are using BitBucket, Azure DevOps, or another Git hosting provider, consult the appropriate service documentation to learn how to form archive URLs for repositories.

#### Archive Files

The above examples demonstrate adding an extension from a Git repository, you can also add an extension from an archive published to an ordinary web host. For example:

```bash
quarto add https://cooltools.org/quarto/shorty.zip
```

Or alternatively from a local archive file or even ordinary uncompressed directory:

```bash
quarto add ~/Downloads/shorty.zip
quarto add /share/quarto/extensions/shorty
```

