## Manuscripts: Components (Using Manuscripts)

Source: [Using Manuscripts – Quarto](https://quarto.org/docs/manuscripts/components.html)

### Overview

Manuscripts are a type of Quarto project that allow you to write scholarly articles where computational notebooks are both the source of the article, and part of the published record.

If you are new to Quarto manuscripts, start with the [Manuscript Tutorial](https://quarto.org/docs/manuscripts/authoring/).

On this page, you can learn how to:

*   [Create a manuscript project](#creating-a-manuscript-project)
*   [Control the manuscript output](#manuscript-options) with options in `_quarto.yml`
*   [Add a journal template](#add-a-journal-template)

### Creating a Manuscript Project

To identify a project as a manuscript specify `type: manuscript` in your `_quarto.yml` configuration file:

**_quarto.yml**
```yaml
project:
  type: manuscript
```

Then, author your article content in either a Jupyter Notebook called `index.ipynb` or a Quarto document called `index.qmd`.

You can control many manuscript options with the `manuscript` key in your configuration file. For instance, you can specify a file other than `index.*` for your article source using the `article` key, e.g.:

**_quarto.yml**
```yaml
manuscript:
  article: earthquakes.qmd
```

If you would rather start with some template content, you can create a new manuscript project from the command line with:

```bash
quarto create project manuscript
```

### Including Notebooks

Any notebook files (`.qmd` or `.ipynb`) that are included in your project directory will become part of your manuscript. These notebooks will be rendered to an HTML notebook view, and will be linked from your manuscript webpage under “Notebooks”.

#### Notebook Links

The text for link under “Notebooks” will be the notebook `title` as set in its YAML metadata, or if that isn’t set, the first markdown heading in the notebook. If neither exist, the link text will be the notebook file name.

You can also set the text using `notebooks`. Use `notebook` to specify the path to the notebook, and `title` to set the link text:

**_quarto.yml**
```yaml
manuscript:
  notebooks:
    - notebook: notebooks/data-screening.ipynb
      title: Data Processing
```

#### External Notebooks

To provide links to notebooks that are hosted elsewhere, add the `url` option:

**_quarto.yml**
```yaml
manuscript:
  notebooks:
    - notebook: index.ipynb
      title: Binder Jupyter Lab Demo
      url: http://mybinder.org/v2/gh/binder-examples/jupyterlab/master?urlpath=lab/tree/index.ipynb
```

If you want Quarto to produce an HTML notebook view from your notebook source, but you would like to provide a specific version for download, add the `download-url` option:

**_quarto.yml**
```yaml
manuscript:
  notebooks:
    - notebook: notebooks/data-screening.ipynb
      title: Data Processing
      download-url: notebooks/data-screening-raw.ipynb
```

### Code Links

Use `code-links` to add links that will appear on your manuscript webpage under the heading “Code Links”. For example, the following adds a link to a Python script:

**_quarto.yml**
```yaml
manuscript:
  code-links:
    - text: Data Import Code
      icon: file-code
      href: data-import.py
```

You can provide the following options for items in `code-links`:

| Option   | Description                                                     |
| :------- | :-------------------------------------------------------------- |
| `text`   | The text to be displayed for the link.                          |
| `href`   | The URL for the link.                                           |
| `icon`   | The [bootstrap icon](https://icons.getbootstrap.com/) for the link. |
| `rel`    | The rel used in the `a` tag for this link.                      |
| `target` | The target used in the `a` tag for this link.                   |

#### GitHub and Binder Links

There are also two special values you can pass as items to `code-links`:

*   **`repo`**: Add a link to “GitHub Repo” under “Code Links” that points at the GitHub repository of your manuscript:
    **_quarto.yml**
    ```yaml
    manuscript:
      code-links: repo
    ```
    Quarto infers the URL for the link from the Git settings of your manuscript project. For `code-links: repo` to work, your manuscript project should be a Git repository, and have GitHub as the remote `origin`.
*   **`binder`**: Add a link to “Launch Binder” under “Code Links” if your manuscript is configured to [Use Binder](#using-binder):
    **_quarto.yml**
    ```yaml
    manuscript:
      code-links: binder
    ```

### Including Other Resources

Quarto will attempt to include resources needed to render your notebooks to HTML on the manuscript website. However, you can also explicitly include resources using `resources`. For example, to include a data file you’ve put in `data/earthquakes.csv` you would specify:

**_quarto.yml**
```yaml
manuscript:
  resources:
    - data/earthquakes.csv
```

This ensures readers can access your data at: `{manuscript-url}/data/earthquakes.csv`.

### MECA Bundle

One of the formats a manuscript project can produce is a Manuscript Exchange Common Approach (MECA) bundle. This bundle is a standardized way to transport your manuscript and its resources, including computational notebooks.

A MECA bundle is produced if the `jats` format is listed as an output format for your article:

**_quarto.yml**
```yaml
format:
  html: default
  jats: default
```

Or, you can explicitly set `meca-bundle` to `true` in the `manuscript` options:

**_quarto.yml**
```yaml
manuscript:
  meca-bundle: true
```

By default the MECA bundle is named after your article file, e.g. `index-meca.zip`, but you can also use `meca-bundle` to provide a file name:

**_quarto.yml**
```yaml
manuscript:
  meca-bundle: "bundle.zip"
```

### Manuscript URL

Links to your notebooks in non-HTML formats are constructed using the URL of your manuscript website. If your manuscript is published to GitHub Pages, Quarto will detect and set the URL for you. However, if you publish to a different host, or the automatic detection isn’t working, you can set the URL explicitly with `manuscript-url`:

**_quarto.yml**
```yaml
manuscript:
  manuscript-url: www.posit.co
```

### Using Binder {#using-binder}

[Binder](https://mybinder.org/) allows you to provide readers with a link that restores your computing environment so they can interact with your manuscript notebooks in a cloud computing environment.

Quarto can help you configure your manuscript to use Binder. Read more at [Using Binder](https://quarto.org/docs/projects/binder.html).

### Customizing Pages

The article page and notebook views on your manuscript site are HTML pages, and can be customized using options for the `html` format. A full list of options is available at [HTML Options](https://quarto.org/docs/reference/formats/html.html).

#### Theme

For example, you can change the visual styling of your page with the `theme` option by providing an existing theme name:

**_quarto.yml**
```yaml
format:
  html:
    theme: solar
```

You can read more at [HTML Theming](https://quarto.org/docs/output-formats/html-themes.html).

#### Commenting

Quarto also integrates with three tools to allow commenting on your manuscript site. To enable commenting, use the `comments` option to the `html` format. For example, to enable [Hypothes.is](https://web.hypothes.is/) comments, you just need to add `hypothesis: true`:

**_quarto.yml**
```yaml
format:
  html:
    comments:
      hypothesis: true
```

The other two tools available are [Utterances](https://utteranc.es/) and [Giscus](https://giscus.app/). You can read about setting them up at [HTML Basics: Commenting](https://quarto.org/docs/output-formats/html-basics.html#commenting).

### Add a Journal Template

You can find a list of available journal formats on the [Quarto Extensions: Journal Articles](https://quarto.org/docs/extensions/listing-journals.html) page. To use a journal format, e.g. the `acs` format, you’ll need to complete two steps:

1.  Install the appropriate journal format. You’ll most likely be installing in an existing project, so you’ll use the `quarto install extension` command, e.g.:
    ```bash
    quarto install extension quarto-journals/acs
    ```
    The extension identifier, `quarto-journals/acs`, is the GitHub user and repository for the extension. You’ll generally find this, and the exact installation command in the extension’s documentation.
2.  Add the `format` to your configuration file:
    **_quarto.yml**
    ```yaml
    format:
      html: default
      docx: default
      jats: default
      acs-pdf: default # Added format
    ```
    The format will be the extension’s name (`acs`), followed by an existing Quarto format (`-pdf`).

