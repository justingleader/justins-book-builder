## Manuscripts (Overview)

Source: [Quarto Manuscripts – Quarto](https://quarto.org/docs/manuscripts/)

### Overview

Quarto manuscript projects provide a framework for writing and publishing scholarly articles. A Quarto manuscript lets you:

*   Use one or more notebooks or `.qmd` documents as the source of content and computations, and then publish these computations alongside the manuscript, allowing readers to dive into your code.
*   Produce manuscripts in multiple formats (including LaTeX or MS Word formats required by journals), and give readers easy access to all of the formats through a manuscript website.

The output of a Quarto manuscript is a website ([live example](https://quarto-journals.github.io/manuscript-template/)). The article itself appears as the content of the website, and can include all the elements common to scholarly writing like figures, tables, equations, cross references and citations. The website also makes available other formats (e.g. PDF, Docx) as well as links to all of the computations used to create the article.

![Manuscript Website Example](https://quarto.org/docs/manuscripts/images/manuscript-website.png)

#### Article Content

#### Navigation

On the right, you’ll see navigation: a table of contents for the article itself followed by links to `Other Formats`, `Notebooks` and `Other Links`.

#### Other Formats

These links allow a reader to download alternative formats of your article. In this example, there is an MS Word version that may be useful for a reviewer to provide feedback and a PDF version that uses the American Geophysical Union’s (AGU) template. Additionally, there is a MECA archive, a zip file that is designed to capture your article and its supporting documents into a single file suitable for sending to a publisher.

#### Notebooks

These are links to notebooks included in the manuscript. The “Article Notebook” is the notebook version of the article itself. In this example, “Data Screening” is a notebook from which a single cell is embedded in the article. Any other notebooks that are included in the project, even if they are not directly used in the article will also appear here.

When a reader visits any of these notebook links, they are served an HTML version of the notebook, allowing them to view the code and output without leaving their browser. In addition, a link to download the source code of the notebook is also provided.

![Notebook View in Manuscript Website](https://quarto.org/docs/manuscripts/images/manuscript-notebook-view.png)
*HTML view of the Data Screening notebook*

#### Other Links

Links that leave the manuscript webpage, for example to take a reader to the manuscript’s GitHub Repo.

### Get Started

#### Install Quarto

Manuscripts are a feature in the 1.4 release of Quarto. Before you get started, make sure you install the [latest release](https://quarto.org/docs/download/) version of Quarto.

#### Choose Your Tool

You can author Quarto manuscripts in any tool or notebook editor. The tutorials below walk you through authoring Quarto manuscripts with a few common tools.

Choose your tool to start learning:

*   [Jupyter](https://quarto.org/docs/manuscripts/authoring/jupyterlab.html)
*   [VS Code](https://quarto.org/docs/manuscripts/authoring/vscode.html)
*   [RStudio](https://quarto.org/docs/manuscripts/authoring/rstudio.html)

