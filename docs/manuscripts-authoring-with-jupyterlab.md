## Manuscripts: Authoring with JupyterLab

Source: [Authoring Manuscripts – Quarto](https://quarto.org/docs/manuscripts/authoring/jupyterlab.html) (Content largely duplicated from Get Started: Hello, Quarto - Jupyter section, tailored for manuscripts)

### Overview

On this page, we’ll show you how to author an academic manuscript with Quarto in Jupyter Lab. You’ll learn how to:

*   Preview your manuscript using Jupyter Lab.
*   Add scholarly front matter to describe your article.
*   Add figures, tables, cross references, and citations with Quarto-specific markdown.
*   Include output from computations using inline code or embedded from external notebooks.

The commands and syntax you’ll learn will apply to any tool you might use to edit notebooks, not just Jupyter Lab. And, although we’ll use Python code examples, Qu
```markdown
Quarto works with any kernel, so you could use R or Julia instead.

#### Is this tutorial for me?

We will assume you:

*   are comfortable using Jupyter Lab to open and edit files,
*   have a GitHub account, and are comfortable cloning a repo to your computer,
*   are comfortable navigating your file system, and executing commands in a Terminal.

#### Setup

To follow along, you’ll need to install the Jupyter Lab Quarto extension and clone the template repository.

##### Install Quarto First

If you haven’t already, make sure you’ve installed the latest release version of Quarto, as described in the [Manuscript Overview](#manuscripts-overview).

##### Install the Jupyter Lab Quarto Extension

Installation depends on which version of JupyterLab you have:

*   **JupyterLab 4:**
    *   **In the JupyterLab UI:** Search for ‘Quarto’ in the Extension Manager and install the `jupyterlab-quarto` extension. You’ll be prompted to refresh the page when complete.
    *   **Using `pip`:**
        *   Mac/Linux: `python3 -m pip install jupyterlab-quarto`
        *   Windows: `py -m pip install jupyterlab-quarto`
*   **JupyterLab 3:**
    *   **Using `pip` (preferred):**
        *   Mac/Linux: `python3 -m pip install jupyterlab-quarto==0.1.45`
        *   Windows: `py -m pip install jupyterlab-quarto==0.1.45`
    *   **In the JupyterLab UI:** Search for ‘Quarto’ in the Extension Manager and install the `@quarto/jupyterlab-quarto` extension. Rebuild JupyterLab when prompted.

##### Clone the Template Repository

To follow this tutorial you’ll need your own copy of the [template repository](https://github.com/quarto-journals/manuscript-template), including all of its branches.

1.  Head to [GitHub to create a new repository from the template](https://github.com/quarto-journals/manuscript-template/generate).
2.  Provide a **Repository Name** and make sure you check **Include all branches**. Then **Create repository from template**.
3.  Once your repository is created, clone it to your local computer.
    ```bash
    # Replace <username> and <repo-name> with your details
    git clone git@github.com:<username>/<repo-name>.git
    ```
4.  Navigate inside the directory, and start Jupyter Lab:
    ```bash
    cd <repo-name> # Use the directory name you chose
    python3 -m jupyter lab # or py -m jupyter lab on Windows
    ```

#### Project Files

At its simplest, a Quarto manuscript project has two files:

1.  A notebook file where you write your article: `index.ipynb`. This file contains:
    *   document metadata, including article front matter (authors, affiliations, etc.) and Quarto options,
    *   the article body, written using special Quarto markdown syntax that allows you to add things like cross references and citations, and
    *   optionally, code, where you control if, or how, the code and its output appear in the article.
2.  A configuration file `_quarto.yml` that identifies the project as a Quarto manuscript and controls how your manuscript is put together.

This particular manuscript project includes some other files and folders, you’ll learn about these files as you work through this tutorial.

#### Workflow

The basic workflow for writing a manuscript in Quarto is to make changes to your article content in `index.ipynb`, preview the changes with Quarto, and repeat. Let’s try it out.

1.  Open a new Terminal in Jupyter Lab and run:
    ```bash
    quarto preview
    ```
2.  You’ll see output from Quarto on the Terminal, and a browser window will open with a live preview. Position Jupyter Lab and the live preview side by side.
3.  Open `index.ipynb` in Jupyter Lab.
4.  The first cell (starting with “La Palma Earthquakes”) is a Markdown cell. Enter Edit mode and find the line: `title: La Palma Earthquakes`.
5.  Change the line to: `title: La Palma Earthquake Mechanisms`.
6.  Save the notebook. The preview will update automatically.

**Tip:** If you close the preview accidentally, use the URL from the Terminal output (e.g. `http://localhost:3806/`) to navigate back. Stop the preview with <kbd>Ctrl</kbd> + <kbd>C</kbd> in the Terminal. Restart with `quarto preview`.

#### Notebook Structure

The file `index.ipynb` is a Jupyter Notebook. Quarto-specific features include:

1.  **YAML Header:** The first cell is a Raw cell containing YAML metadata (title, author, format options, etc.), enclosed in `---`. The Quarto Jupyter Lab Extension renders a preview of this.
2.  **Markdown Cells:** Use Quarto-flavored markdown for text, headings, figures, tables, citations, cross-references, etc.
3.  **Code Cells:** Can have Quarto options specified in `#|` comments at the top to control execution and output appearance.

The rest of this page walks through the cells in `index.ipynb`, explaining Quarto features for scholarly articles.

#### Front Matter

The YAML header sets document metadata using `key: value` pairs. For manuscripts, this includes scholarly front matter.

(Expandable section showing the full YAML header from the example `index.ipynb` - includes `title`, `author` details like ORCID, email, roles, affiliations, `keywords`, `abstract`, `plain-language-summary`, `key-points`, `date`, `bibliography`, `citation`, `number-sections`).

See [Scholarly Front Matter](https://quarto.org/docs/authoring/front-matter.html) for more details.

#### Markdown

Use standard markdown for text and headings (`## Introduction`). See [Markdown Basics](https://quarto.org/docs/authoring/markdown-basics.html).

#### Computations

(Includes Python examples, notes need for `matplotlib`, `numpy`).

Executable code appears in code cells. By default, the code itself is hidden in the rendered article, but output (figures, tables) appears. The code is included in the linked "Article Notebook" on the manuscript website.

Example code cell:
````markdown
```{python}
import matplotlib.pyplot as plt
import numpy as np
eruptions = [1492, 1585, 1646, 1677, 1712, 1949, 1971, 2021]
```
````

Use `#|` comments for Quarto options. Example `echo: true` shows code in the article:
````markdown
```{python}
#| echo: true
import matplotlib.pyplot as plt
# ... rest of code
```
````
See [Jupyter Code Cell Options](https://quarto.org/docs/reference/cells/cells-jupyter.html).

Example figure cell with options:
````markdown
```{python}
#| label: fig-timeline
#| fig-cap: Timeline of recent earthquakes on La Palma
#| fig-alt: An event plot of the years of the last 8 eruptions on La Palma.
plt.figure(figsize=(6, 1))
# ... plotting code ...
plt.show()
```
````
Use `label` with `fig-` prefix for cross-references. `fig-cap` sets the caption, `fig-alt` sets alt text.

See [Tables from Computations](https://quarto.org/docs/authoring/tables.html#computations) for table generation.

Use `output: false` to hide specific output (useful for intermediate values):
````markdown
```{python}
#| output: false
avg_years_between_eruptions = np.mean(np.diff(eruptions[:-1]))
avg_years_between_eruptions # This output won't appear in the article
```
````

Use `include: false` to hide both code and output from article and notebook view:
````markdown
```{python}
#| include: false
# ... code ...
```
````
Use [Inline Code](https://quarto.org/docs/computations/inline-code.html) for computations within text.

See [Embedding Notebooks](#embedding-notebooks) for including output from external notebooks.

**When is code executed?** By default, Quarto doesn't execute `.ipynb` notebooks during render. Run cells and save before rendering, or use `--execute` flag or `execute: true` YAML option.

#### Citations

Specify a bibliography file (e.g., `references.bib`) in YAML:
```yaml
bibliography: references.bib
```

Cite using `@key` syntax (e.g., `@marrero2019`). Enclose in brackets for parenthetical citations (`[@marrero2019]`). See [Citations](https://quarto.org/docs/authoring/citations.html).

#### Cross References

Use `@label` to reference figures (`@fig-timeline`), tables (`@tbl-history`), equations (`@eq-poisson`), or sections (`@sec-data-methods`). Requires a label with the correct prefix (`fig-`, `tbl-`, `eq-`, `sec-`) on the target element. Sections also require `number-sections: true` in YAML. Add labels to headings like `## Data & Methods {#sec-data-methods}`. See [Cross References](https://quarto.org/docs/authoring/cross-references.html).

#### Equations

Use `$` for inline math (`$x$`) and `$$` for display math. Add labels for cross-referencing:
```markdown
$$ p(x) = \frac{e^{-\lambda} \lambda^{x}}{x !} $$ {#eq-poisson}
```
See [Equations](https://quarto.org/docs/authoring/markdown-basics.html#equations).

#### Tables

Use pipe table syntax. Add captions and labels below the table:
```markdown
| Name                 | Year   |
| -------------------- | ------ |
| Current              | 2021   |
| ...                  | ...    |
: Recent historic eruptions on La Palma {#tbl-history}
```
See [Tables](https://quarto.org/docs/authoring/tables.html).

#### Static Figures

Include images using standard markdown syntax. Add captions and labels:
```markdown
![Map of La Palma](images/la-palma-map.png){#fig-map}
```
Add `fig-alt` for accessibility:
```markdown
![Map of La Palma](images/la-palma-map.png){#fig-map fig-alt="A map of the Canary Islands..."}
```
See [Figures](https://quarto.org/docs/authoring/figures.html).

#### External Embeds {#embedding-notebooks}

Embed output from another notebook (e.g., `notebooks/data-screening.ipynb`) using the `embed` shortcode with the path and cell label:
```markdown
{{< embed notebooks/data-screening.ipynb#fig-spatial-plot >}}
```
The source notebook cell needs a corresponding label:
````markdown
```{python}
#| label: fig-spatial-plot
#| fig-cap: "Locations of earthquakes..."
#| fig-alt: "A scatterplot..."
# ... plotting code ...
plt.show()
```
````
Options like `fig-cap` from the source notebook are used. See [Embedding Notebooks](https://quarto.org/docs/authoring/notebook-embed.html).

### Up Next

Proceed to [Publishing](https://quarto.org/docs/manuscripts/publishing.html) to learn how to publish your manuscript website.

