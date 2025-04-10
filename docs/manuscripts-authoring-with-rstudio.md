## Manuscripts: Authoring with RStudio

Source: [Authoring Manuscripts – Quarto](https://quarto.org/docs/manuscripts/authoring/rstudio.html) (Content largely duplicated from Get Started: Hello, Quarto - RStudio section, tailored for manuscripts)

### Overview

On this page, we’ll show you how to author an academic manuscript with Quarto in RStudio. You’ll learn how to:

*   Preview your manuscript using RStudio.
*   Add scholarly front matter to describe your article.
*   Add figures, tables, cross references, and citations with Quarto-specific markdown.
*   Include output from computations using inline code or embedded from external notebooks.

The syntax you’ll learn will apply regardless of the tool you are using to edit notebooks. And although we’ll use R code examples, you could use Python or Julia instead.

**What’s a notebook?** We use "notebook" interchangeably for Quarto documents (`.qmd`) and Jupyter Notebooks (`.ipynb`). Both combine code and narrative. When publishing manuscripts, Quarto `.qmd` files are often converted to `.ipynb` to include outputs alongside code.

#### Is this tutorial for me?

We will assume you:

*   are comfortable using RStudio to open and edit files,
*   have a GitHub account, and are comfortable cloning a repo to your computer,
*   are comfortable navigating your file system, and executing commands in a Terminal.

#### Setup

To follow along, you’ll need to clone the template repository.

##### Install Quarto First

If you haven’t already, make sure you’ve installed the latest release version of Quarto, as described in the [Manuscript Overview](#manuscripts-overview).

##### Clone the Template Repository

To follow this tutorial you’ll need your own copy of the [template repository](https://github.com/quarto-journals/manuscript-template), including all of its branches.

1.  Head to [GitHub to create a new repository from the template](https://github.com/quarto-journals/manuscript-template/generate).
2.  Provide a **Repository Name** and make sure you check **Include all branches**. Then **Create repository from template**.
3.  Once your repository is created, clone it to your local computer. Use RStudio: `File` > `New Project` > `From Version Control` > `Git`, paste the repo URL.

#### Project Files

(Content identical to JupyterLab section: describes `index.qmd` and `_quarto.yml` as core files.)

#### Workflow

The basic workflow is: edit `index.qmd`, preview changes, repeat.

1.  Open `index.qmd`.
2.  Render and preview using the `Render` button (or <kbd>⇧</kbd>+<kbd>⌘</kbd>+<kbd>K</kbd>). Preview appears in the Viewer pane.
3.  Find the line: `title: La Palma Earthquakes`.
4.  Change it to: `title: La Palma Earthquake Mechanisms`.
5.  Save, re-render, and see the preview update.

##### Visual Editor

RStudio's [visual editor](https://quarto.org/docs/tools/visual-editor.html) provides WYSIWYM editing. Toggle between Source and Visual modes (<kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>F4</kbd>). Visual mode simplifies adding citations, tables, etc.

#### Notebook Structure

Quarto `.qmd` files contain:

1.  **YAML Header:** Document metadata and options, enclosed in `---`.
2.  **Code Chunks:** Executable code (e.g., ````{r}`). Options use `#|` comments.
3.  **Markdown:** Narrative text using Quarto-flavored markdown.

#### Front Matter

(Content identical to JupyterLab section, explaining YAML key-value pairs for scholarly metadata).

#### Markdown

(Content identical to JupyterLab section, explaining basic markdown and linking to Markdown Basics).

#### Computations

(Includes R examples, notes need for `tidyverse` package).

Executable code appears in code chunks. Code is hidden by default in the article but included in the "Article Notebook" view.

Example hidden code chunk:
````markdown
```{r}
eruptions <- c(1492, 1585, 1646, 1677, 1712, 1949, 1971, 2021)
n_eruptions <- length(eruptions)
```
````

Use `#|` for Quarto options. Example `echo: true` shows code:
````markdown
```{r}
#| echo: true
# ... R code ...
```
````
See [Knitr Code Cell Options](https://quarto.org/docs/reference/cells/cells-knitr.html).

Example figure chunk:
````markdown
```{r}
#| label: fig-timeline
#| fig-cap: Timeline of recent earthquakes on La Palma
#| fig-alt: An event plot of the years of the last 8 eruptions on La Palma.
#| fig-height: 1.5
#| fig-width: 6
par(mar = c(3, 1, 1, 1) + 0.1)
plot(eruptions, rep(0, n_eruptions), pch = "|", axes = FALSE)
axis(1)
box()
```
````
Use `label` with `fig-` prefix for cross-references. `fig-cap` sets the caption, `fig-alt` sets alt text.

See [Tables from Computations](https://quarto.org/docs/authoring/tables.html#computations).

Use `output: false` to hide specific output:
````markdown
```{r}
#| output: false
avg_years_between_eruptions <- mean(diff(eruptions[-n_eruptions]))
avg_years_between_eruptions # Output hidden in article
```
````
Use `include: false` to hide code and output entirely.

Use inline R code `` `{r} expr` ``:
```markdown
...every `{r} round(avg_years_between_eruptions, 1)` years...
```
Renders as: "...every 79.8 years..."
See [Inline Code](https://quarto.org/docs/computations/inline-code.html).

See [Embedding Notebooks](#embedding-notebooks-1) for including external notebook output.

**When is code executed?** By default, Quarto executes `.qmd` code during render. This template uses `freeze`, saving outputs in `_freeze/`. Code is only re-run if the source changes. Commit `_freeze/` changes.

#### Citations

(Content largely identical to JupyterLab section, explaining `bibliography` YAML key, `.bib` files, `@key` syntax, bracket variations, and using RStudio's Visual Editor `Insert -> Citation` tool.)

#### Cross References

(Content largely identical to JupyterLab section, explaining `@label` syntax, required prefixes `fig-`, `tbl-`, `eq-`, `sec-`, `number-sections: true` for sections, and using RStudio's Visual Editor `Insert -> Cross Reference` tool.)

#### Equations

(Content identical to JupyterLab section, explaining `$` and `$$` syntax for LaTeX math and adding labels like `{#eq-poisson}`.)

#### Tables

(Content largely identical to JupyterLab section, explaining pipe table syntax, captions with `{#tbl-label}`. Mentions RStudio's Visual Editor table tools.)

#### Static Figures

(Content largely identical to JupyterLab section, explaining `![Caption](path){#fig-label fig-alt="text"}` syntax.)

#### External Embeds {#embedding-notebooks-1}

Embed output from other `.qmd` files (or `.ipynb`).
Use the `embed` shortcode:
```markdown
{{< embed notebooks/explore-earthquakes.qmd#fig-spatial-plot >}}
```
Requires a chunk label in the source notebook:
````markdown
```{r}
#| label: fig-spatial-plot
#| fig-cap: "Locations of earthquakes..."
#| fig-alt: "A scatterplot..."
# ... plotting code ...
```
````
Options like `fig-cap` propagate. Changing the source notebook triggers re-render. You might need `install.packages("tidyverse")` for the example.

### Up Next

Proceed to [Publishing](https://quarto.org/docs/manuscripts/publishing.html) to learn how to publish your manuscript website.

