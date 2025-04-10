## Authoring Tables

Source: [Tables – Quarto](https://quarto.org/docs/authoring/tables.html)

### Overview

Quarto includes a number of features aimed at making it easy to to author and customize markdown table output, including:

*   Specifying column alignment and widths.
*   Providing captions, subcaptions, and cross-references.
*   Generating tables dynamically from executable code cells.

This article covers using these features in-depth.

### Markdown Tables

The most commonly used markdown table is known as a pipe table. Pipe tables support specifying per column alignment as well as captions. For example:

```markdown
| Default | Left  | Right | Center |
|---------|:------|------:|:------:|
| 12      | 12    |    12 |   12   |
| 123     | 123   |   123 |  123   |
| 1       | 1     |     1 |   1    |
: Demonstration of pipe table syntax
```

Result:

Demonstration of pipe table syntax

| Default | Left  | Right | Center |
| :------ | :---- | ----: | :----: |
| 12      | 12    |    12 |   12   |
| 123     | 123   |   123 |  123   |
| 1       | 1     |     1 |   1    |

The beginning and ending pipe characters are optional, but pipes are required between all columns. The colons indicate column alignment as shown. The header cannot be omitted, however you can simulate a headerless table by including a header with blank cells.

Since the pipes indicate column boundaries, columns need not be vertically aligned, as they are in the above example. So, this is a perfectly legal (though ugly) pipe table:

```markdown
fruit| price
-----|-----:
apple|2.05
pear|1.37
orange|3.09
```

The cells of pipe tables cannot contain block elements like paragraphs and lists, and cannot span multiple lines. If a pipe table contains a row whose markdown content is wider than the column width (see [`columns`](https://quarto.org/docs/reference/formats/html.html#columns) option), then the table will take up the full text width and the cell contents will wrap, with the relative cell widths determined by the number of dashes in the line separating the table header from the table body.

For example `---|-` would make the first column 3/4 and the second column 1/4 of the full text width. On the other hand, if no lines are wider than column width, then cell contents will not be wrapped, and the cells will be sized to their contents.

#### Using Bootstrap classes

Bootstrap table classes given as attributes next to a table caption are inserted into the `<table>` element. The classes permitted are those that apply expressly to the entire table, and these are: `"primary"`, `"secondary"`, `"success"`, `"danger"`, `"warning"`, `"info"`, `"light"`, `"dark"`, `"striped"`, `"hover"`, `"active"`, `"bordered"`, `"borderless"`, `"sm"`, `"responsive"`, `"responsive-sm"`, `"responsive-md"`, `"responsive-lg"`, `"responsive-xl"`, `"responsive-xxl"`. For example, the following Markdown table will be rendered with row stripes and the rows will also be highlighted on hover:

```markdown
| fruit  | price  |
|--------|--------|
| apple  | 2.05   |
| pear   | 1.37   |
| orange | 3.09   |
: Fruit prices {.striped .hover}
```

Result:

Fruit prices

| fruit  | price |
| :----- | ----: |
| apple  |  2.05 |
| pear   |  1.37 |
| orange |  3.09 |

#### Authoring

For simple tables with only a few cells it’s straightforward to create them directly in markdown. As tables get larger, it makes sense to use an authoring tool. Some table authoring tools to consider include:

*   [TablesGenerator](https://www.tablesgenerator.com/markdown_tables): Online tool for generating markdown tables
*   [Emacs TableMode](https://table.sourceforge.net/): Text based table creation and editing capabilities for Emacs.
*   [Quarto Visual Editor](https://quarto.org/docs/tools/visual-editor.html): Visual editor for `.qmd` files with table editing support.

### Column Widths

Above we describe a means of specifying column widths using the relative number of dashes in each column header (*e.g.*, `---|-` to get a 75% / 25% split for a two-column table).

You can also explicitly specify columns widths using the `tbl-colwidths` attribute or document-level option. For an individual markdown table, add the attribute after the caption. For example:

```markdown
| fruit  | price  |
|--------|--------|
| apple  | 2.05   |
| pear   | 1.37   |
| orange | 3.09   |
: Fruit prices {tbl-colwidths="[75,25]"}
```

Result:

Fruit prices

| fruit  | price |
| :----- | ----: |
| apple  |  2.05 |
| pear   |  1.37 |
| orange |  3.09 |

If your table doesn’t have a caption, then you can still specify only `tbl-colwidths`:

```markdown
| fruit  | price  |
|--------|--------|
| apple  | 2.05   |
| pear   | 1.37   |
| orange | 3.09   |
: {tbl-colwidths="[75,25]"}
```

Result:

| fruit  | price |
| :----- | ----: |
| apple  |  2.05 |
| pear   |  1.37 |
| orange |  3.09 |

Column widths can also be specified at the document level (*e.g.*, to have uniform widths across a set of tables):

```yaml
---
title: "My Document"
format: html
tbl-colwidths: [75, 25]
---
```

### Cross References

For tables produced by executable code cells, include a label with a `tbl-` prefix to make them cross-referenceable. For example:

````markdown
```{python}
#| label: tbl-planets
#| tbl-cap: Astronomical object

from IPython.display import Markdown
from tabulate import tabulate
table = [["Sun","696,000",1.989e30],
         ["Earth","6,371",5.972e24],
         ["Moon","1,737",7.34e22],
         ["Mars","3,390",6.39e23]]
Markdown(tabulate(
  table,
  headers=["Astronomical object","R (km)", "mass (kg)"]
))
```
````

Result:

Table 1: Astronomical object

| Astronomical object   | R (km)   |   mass (kg) |
| :-------------------- | :------- | ----------: |
| Sun                   | 696,000  | 1.989e+30   |
| Earth                 | 6,371    | 5.972e+24   |
| Moon                  | 1,737    | 7.34e+22    |
| Mars                  | 3,390    | 6.39e+23    |

**Label Prefix:** In order for a table to be cross-referenceable, its label must start with the `tbl-` prefix.

For markdown tables, add a caption below the table, then include a `#tbl-` label in braces at the end of the caption. For example:

```markdown
| Col1 | Col2 | Col3 |
|------|------|------|
| A    | B    | C    |
| E    | F    | G    |
| A    | G    | G    |
: My Caption {#tbl-letters}

See @tbl-letters.
```

Which looks like this when rendered to HTML:

![Cross Reference Table Example](https://quarto.org/docs/authoring/images/cross-reference-table.png)

See the article on [Cross References](https://quarto.org/docs/authoring/cross-references.html) for additional details.

### Subtables

You may want to create a composition of several sub-tables. To do this, create a div with a main identifier, then apply sub-identifiers (and optional caption text) to the contained tables. For example:

```markdown
::: {#tbl-panel layout-ncol=2}

| Col1 | Col2 | Col3 |
|------|------|------|
| A    | B    | C    |
| E    | F    | G    |
| A    | G    | G    |
: First Table {#tbl-first}

| Col1 | Col2 | Col3 |
|------|------|------|
| A    | B    | C    |
| E    | F    | G    |
| A    | G    | G    |
: Second Table {#tbl-second}

Main Caption
:::

See @tbl-panel for details, especially @tbl-second.
```

Which looks like this when rendered to HTML:

![Subtable Example](https://quarto.org/docs/authoring/images/cross-reference-subtable.png)

Note that the “Main Caption” for the table is provided as the last block within the containing div.

### Caption Location

By default, table captions are positioned above tables. You can modify this behavior using the `tbl-cap-location` option. For example:

```yaml
---
tbl-cap-location: bottom
---
```

Note that this option is specified at the top level so that it can be shared by both PDF and HTML formats. If you are only targeting a single format you can place it alongside other `format` specific options.

Valid values for the caption location include:

| Value    | Description                       |
| :------- | :-------------------------------- |
| `top`    | Position the caption above the table. |
| `bottom` | Position the caption below the table. |
| `margin` | Position the caption in the margin.   |

See the article on [Article Layout](https://quarto.org/docs/authoring/article-layout.html#margin-captions) for additional details on placing captions in the margin.

### Computations

All of the options described above work for tables produced by executable code cells. For example, here we use the Python `tabulate` package along with the `Markdown()` function from the IPython `display` module to print a markdown table:

````markdown
```{python}
#| label: tbl-planet-measures
#| tbl-cap: Astronomical object

from IPython.display import Markdown
from tabulate import tabulate
table = [["Sun","696,000",1.989e30],
         ["Earth","6,371",5.972e24],
         ["Moon","1,737",7.34e22],
         ["Mars","3,390",6.39e23]]
Markdown(tabulate(
  table,
  headers=["Astronomical object","R (km)", "mass (kg)"]
))
```
````

Result:

Table 2: Astronomical object

| Astronomical object   | R (km)   |   mass (kg) |
| :-------------------- | :------- | ----------: |
| Sun                   | 696,000  | 1.989e+30   |
| Earth                 | 6,371    | 5.972e+24   |
| Moon                  | 1,737    | 7.34e+22    |
| Mars                  | 3,390    | 6.39e+23    |

Here we apply the `tbl-cap` and `tbl-colwidths` options to a code cell that uses the knitr `kable()` function to write a markdown table:

````markdown
```{r}
#| label: tbl-cars
#| tbl-cap: "Cars"
#| tbl-colwidths: [60,40]

kable(head(cars))
```
````

If your code cell produces multiple tables, you can also specify subcaptions and layout using cell options:

**Python**
````markdown
```{python}
#| label: tbl-example
#| tbl-cap: "Example"
#| tbl-subcap:
#|   - "MPG"
#|   - "Taxis"
#| layout-ncol: 2

import seaborn as sns
from IPython.display import Markdown, display

mpg = sns.load_dataset("mpg").head(10)
taxis = sns.load_dataset("taxis").head(10)

display(Markdown(mpg.to_markdown(index = False)))
display(Markdown(taxis.to_markdown(index = False)))
```
````

Note that we use the `display()` function imported from `IPython` so that we can render multiple outputs from a single cell (by default cells only output their last expression).

**R**
````markdown
```{r}
#| label: tbl-example
#| tbl-cap: "Example"
#| tbl-subcap:
#|   - "Cars"
#|   - "Pressure"
#| layout-ncol: 2

library(knitr)
kable(head(cars))
kable(head(pressure))
```
````

#### Computational Table Styling

Quarto adds additional styling to tables generated by computations. By default, such tables are styled to be smaller and have striped rows. If you want to disable this treatment, add `plain` to the classes of the code cell:

````markdown
```{r}
#| classes: plain
tibble::tribble(
  ~fruit,   ~price,
  "apple",  2.05,
  "pear",   1.37,
  "orange", 3.09
) |>
  gt::gt()
```
````

### Grid Tables

Grid tables are a more advanced type of markdown tables that allow arbitrary block elements (multiple paragraphs, code blocks, lists, etc.). For example:

```markdown
+-----------+-----------+--------------------+
| Fruit     | Price     | Advantages         |
+===========+===========+====================+
| Bananas   | $1.34     | - built-in wrapper |
|           |           | - bright color     |
+-----------+-----------+--------------------+
| Oranges   | $2.10     | - cures scurvy     |
|           |           | - tasty            |
+-----------+-----------+--------------------+
: Sample grid table.
```

Which looks like this when rendered to HTML:

Sample grid table.

| Fruit   | Price | Advantages         |
| :------ | :---- | :----------------- |
| Bananas | $1.34 | - built-in wrapper<br>- bright color |
| Oranges | $2.10 | - cures scurvy<br>- tasty |

The row of `=`s separates the header from the table body, and can be omitted for a headerless table. The cells of grid tables may contain arbitrary block elements (multiple paragraphs, code blocks, lists, etc.)

Alignments can be specified as with pipe tables, by putting colons at the boundaries of the separator line after the header:

```markdown
+---------+--------+------------------+
| Right   | Left   | Centered         |
+========:+:=======+:================:+
| Bananas | $1.34  | built-in wrapper |
+---------+--------+------------------+
```

Which looks like this when rendered to HTML:

| Right   | Left  | Centered         |
| :------ | :---- | :--------------- |
| Bananas | $1.34 | built-in wrapper |

For headerless tables, the colons go on the top line instead:

```markdown
+----------:+:----------+:--------:+
| Right     | Left      | Centered |
+-----------+-----------+----------+
```

Which looks like this when rendered to HTML:

| Right | Left | Centered |
| :---- | :--- | :------- |
| Right | Left | Centered |

Note that grid tables are quite awkward to write with a plain text editor (because unlike pipe tables, the column indicators must align). Here are some tools that can assist with creating grid tables:

*   Emacs’ `table-mode` (`M-x table-insert`)
*   Quarto [Visual Editor](https://quarto.org/docs/tools/visual-editor.html)
*   Tables Generator’s [Plain Text mode](https://www.tablesgenerator.com/text_tables) with `Use reStructuredText syntax` enabled

### HTML Tables

Quarto can process HTML tables in `html` `RawBlock` nodes (*i.e.*, `{=html}`) and convert them to Markdown tables, regardless of the output format (intentionally including non-HTML formats). As a result, you can use HTML table syntax in your documents and it will be converted to Markdown syntax for all formats. Additionally, libraries that emit computational tables in HTML format can work in other output formats.

For example, consider the following raw HTML block:

````markdown
```{=html}
<table>
  <caption>As described in the section above, Quarto tables are great.</caption>
  <thead>
    <tr>
      <th>Header 1</th>
      <th>Header 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
    <td><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/African_Bush_Elephant.jpg/220px-African_Bush_Elephant.jpg" alt="African Bush Elephant" /></td>
      <td>Regular output</td>
    </tr>
  </tbody>
</table>
```
````

When rendered, this results in the following output for HTML and PDF formats:

**HTML Output:**

As described in the section above, Quarto tables are great.

| Header 1                                                                                                                             | Header 2       |
| :----------------------------------------------------------------------------------------------------------------------------------- | :------------- |
| ![African Bush Elephant](https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/African_Bush_Elephant.jpg/220px-African_Bush_Elephant.jpg) | Regular output |

**PDF Output:**

![PDF Table Example](https://quarto.org/docs/authoring/images/pdf-table-example.png)

In addition, Quarto supports the specification of embedded Markdown content in tables. This is done by providing a data attribute `qmd` or `qmd-base64` in an embedded `span` or `div` node. These nodes can appear anywhere that such content is allowed: table headers, footers, cells, captions, *etc.*

For example, the following table includes a cross reference, markdown formatting and a shortcode:

````markdown
