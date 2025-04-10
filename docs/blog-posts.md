## Blog Posts

### 2023-03-17-jupyter-cell-embedding Penguins-preview

Source: [Palmer Penguins – Quarto](https://quarto.org/docs/blog/posts/2023-03-17-jupyter-cell-embedding/penguins.html)

(This appears to be a rendered output example using the Palmer Penguins dataset, included within the blog post section.)

### 2024-07-02-beautiful-tables-in-typst

Source: [Beautiful Tables in Typst – Quarto](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/)

Quarto now allows HTML Tables with CSS styling to be output in Typst.

It does this by translating CSS properties into Typst properties. You can read about the feature

*   [in the Guide](https://quarto.org/docs/authoring/tables.html#html-tables)
*   [technical details in the Advanced Docs](https://quarto.org/docs/reference/formats/typst-css.html)

Let’s look at 6 HTML tables using a variety of CSS properties also supported by Typst in Quarto.

You can click on the links below the examples to see the full documents, with source code.

1.  **Confusion Matrix (Pandas / Python)**
    This example uses a dashed border to draw attention to two cells.
    *   **Typst:** ![Typst Confusion Matrix Table](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/images/pandas-confusion-matrix-typst.png)
    *   **HTML:** ![HTML Confusion Matrix Table](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/images/pandas-confusion-matrix-html.png)
    [Source](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/examples/pandas-confusion-matrix.html)

2.  **Cars heatmap (gt / R)**
    This example uses cell background colors to encode ranges of values.
    *   **Typst:** ![Typst Cars Heatmap Table](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/images/gt-cars-typst.png)
    *   **HTML:** ![HTML Cars Heatmap Table](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/images/gt-cars-html.png)
    [Source](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/examples/gt-cars.html)

3.  **Oceania (Great Tables / Python)**
    Borders can show the structure of grouped rows.
    *   **Typst:** ![Typst Oceania Table](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/images/great-tables-oceania-typst.png)
    *   **HTML:** ![HTML Oceania Table](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/images/great-tables-oceania-html.png)
    [Source](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/examples/great-tables-oceania.html)

4.  **Islands (gt / R)**
    Font sizes and minimal borders make this table stand out.
    *   **Typst:** ![Typst Islands Table](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/images/gt-islands-typst.png)
    *   **HTML:** ![HTML Islands Table](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/images/gt-islands-html.png)
    [Source](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/examples/gt-islands.html)

5.  **Solar Zenith (Great Tables / Python)**
    Another cool heatmap.
    *   **Typst:** ![Typst Solar Zenith Table](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/images/great-tables-solar-zenith-typst.png)
    *   **HTML:** ![HTML Solar Zenith Table](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/images/great-tables-solar-zenith-html.png)
    [Source](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/examples/great-tables-solar-zenith.html)

6.  **Acting on Data (Pandas / Python)**
    Applying colors and transparency based on data.
    *   **Typst:** ![Typst Acting on Data Table](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/images/pandas-acting-on-data-typst.png)
    *   **HTML:** ![HTML Acting on Data Table](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/images/pandas-acting-on-data-html.png)
    [Source](https://quarto.org/docs/blog/posts/2024-07-02-beautiful-tables-in-typst/examples/pandas-acting-on-data.html)

We can’t wait to see what you do with this new feature!

### 2024-07-02-beautiful-tables-in-typst Examples

(These sections contain the rendered HTML output for the examples linked in the blog post above. They primarily showcase tables and do not add substantially new conceptual documentation beyond what's covered in the Typst CSS and Tables sections.)

*   **Great-tables-oceania.html**: Rendered HTML of the Oceania table example using Great Tables (Python).
*   **Great-tables-solar-zenith.html**: Rendered HTML of the Solar Zenith heatmap example using Great Tables (Python).
*   **Gt-cars.html**: Rendered HTML of the cars heatmap example using gt (R).
*   **Gt-islands.html**: Rendered HTML of the islands table example using gt (R).
*   **Pandas-acting-on-data.html**: Rendered HTML of the styled table example using Pandas (Python).
*   **Pandas-confusion-matrix.html**: Rendered HTML of the confusion matrix example using Pandas (Python).

