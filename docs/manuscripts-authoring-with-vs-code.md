## Manuscripts: Authoring with VS Code

Source: [Authoring Manuscripts – Quarto](https://quarto.org/docs/manuscripts/authoring/vscode.html) (Content largely duplicated from Get Started: Hello, Quarto - VS Code section, tailored for manuscripts)

### Overview

On this page, we’ll show you how to author an academic manuscript with Quarto in VS Code. You’ll learn how to:

*   Preview your manuscript using VS Code.
*   Add scholarly front matter to describe your article.
*   Add figures, tables, cross references, and citations with Quarto-specific markdown.
*   Include output from computations using inline code or embedded from external notebooks.

The syntax you’ll learn will apply regardless of the tool you are using to edit notebooks. And although we’ll use Python code examples, you could use R or Julia instead.

**Do you mostly use `.ipynb`?** As a VS Code user, we recommend writing your article in a `.qmd` file. However, if you primarily work with `.ipynb` files, the Jupyter Lab tutorial might be more relevant. Install the [Quarto extension for Jupyter Lab](https://quarto.org/docs/tools/jupyter-lab-extension.html), then follow the Jupyter Lab tutorial starting from [Clone the Template Repository](https://quarto.org/docs/manuscripts/authoring/jupyterlab.html#clone-the-template-repository). You might also read about using [Quarto with VS Code’s Notebook Editor](https://quarto.org/docs/tools/vscode-notebook-editor.html).

#### Is this tutorial for me?

We will assume you:

*   are comfortable using VS Code to open and edit files,
*   have a GitHub account, and are comfortable cloning a repo to your computer,
*   are comfortable navigating your file system, and executing commands in a Terminal.

#### Setup

To follow along, you’ll need to install the VS Code Quarto extension, install some Python packages, and clone the template repository.

##### Install Quarto First

If you haven’t already, make sure you’ve installed the latest release version of Quarto, as described in the [Manuscript Overview](#manuscripts-overview).

##### Install the Quarto VS Code Extension

Install the Quarto extension from the [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) or the [Open VSX Registry](https://open-vsx.org/extension/quarto/quarto).

##### Install Python Packages

The template manuscript includes Python code. Install `jupyter`, `pandas`, and `matplotlib`:

```bash
# On Mac/Linux
python3 -m pip install jupyter matplotlib pandas
# On Windows
# py -m pip install jupyter matplotlib pandas
```
Alternatively, use `requirements.txt` from the cloned repo.

##### Clone the Template Repository

To follow this tutorial you’ll need your own copy of the [template repository](https://github.com/quarto-journals/manuscript-template), including all of its branches.

1.  Head to [GitHub to create a new repository from the template](https://github.com/quarto-journals/manuscript-template/generate).
2.  Provide a **Repository Name** and make sure you check **Include all branches**. Then **Create repository from template**.
3.  Once your repository is created, clone it to your local computer.
    ```bash
    # Replace <username> and <repo-name> with your details
    git clone git@github.com:<username>/<repo-name>.git
    ```
4.  Open the cloned directory in VS Code.

#### Project Files

(Content identical to JupyterLab section: describes `index.qmd` and `_quarto.yml` as core files.)

#### Workflow

The basic workflow is: edit `index.qmd`, preview changes, repeat.

1.  Open `index.qmd`.
2.  Preview using the `Preview` button (👁️) or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>K</kbd> (<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>K</kbd> on Mac). The preview appears in a pane.
3.  Find the line: `title: La Palma Earthquakes`.
4.  Change it to: `title: La Palma Earthquake Mechanisms`.
5.  Save, hit Preview again, and see the preview update.

##### Visual Editor

VS Code's [visual editor](https://quarto.org/docs/tools/vscode-visual-editor.html) provides WYSIWYM editing. Toggle between Source and Visual modes using the Editor menu or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F4</kbd> (<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>F4</kbd> on Mac).

#### Notebook Structure

Quarto `.qmd` files contain:

1.  **YAML Header:** Document metadata and options, enclosed in `---`.
2.  **Code Chunks:** Executable code (e.g., ````{python}`). Options use `#|` comments.
3.  **Markdown:** Narrative text using Quarto-flavored markdown.

#### Front Matter

(Content identical to JupyterLab section, explaining YAML key-value pairs for scholarly metadata).

#### Markdown

(Content identical to JupyterLab section, explaining basic markdown and linking to Markdown Basics).

#### Computations

(Content identical to JupyterLab section, explaining code visibility, `#|` options, `label`, `fig-cap`, `fig-alt`, `output: false`, `include: false`, inline code ` ``{python} expr`` `, embedding, and freeze.)

#### Citations

(Content identical to JupyterLab section, explaining `bibliography` YAML key, `.bib` files, `@key` syntax, bracket variations, and using VS Code's Visual Editor `Insert -> Citation` tool.)

#### Cross References

(Content identical to JupyterLab section, explaining `@label` syntax, required prefixes `fig-`, `tbl-`, `eq-`, `sec-`, `number-sections: true` for sections, and using VS Code's Visual Editor `Insert -> Cross Reference` tool.)

#### Equations

(Content identical to JupyterLab section, explaining `$` and `$$` syntax for LaTeX math and adding labels like `{#eq-poisson}`.)

#### Tables

(Content largely identical to JupyterLab section, explaining pipe table syntax, captions with `{#tbl-label}`. Mentions VS Code's Visual Editor table tools.)

#### Static Figures

(Content largely identical to JupyterLab section, explaining `![Caption](path){#fig-label fig-alt="text"}` syntax.)

#### External Embeds {#embedding-notebooks-2}

(Content identical to RStudio section, explaining embedding `.qmd` or `.ipynb` output using `{{< embed >}}` shortcode.)

### Up Next

Proceed to [Publishing](https://quarto.org/docs/manuscripts/publishing.html) to learn how to publish your manuscript website.

