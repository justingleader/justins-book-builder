## HTML Tables Example {#sec-html-tables}

```{=html}
<table>
  <caption><span data-qmd="As described in [Section -@sec-html-tables], Quarto are great."></span></caption>
  <thead>
    <tr>
      <th><span data-qmd="_Header 1_"></span></th>
      <th><span data-qmd="_Header 2_"></span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span data-qmd="{{< video https://www.youtube.com/embed/wo9vZccmqwc >}}"></span></td>
      <td>Regular output</td>
    </tr>
  </tbody>
</table>
```
````

Which renders as follows:

### HTML Tables Example {#sec-html-tables}

As described in Section 9, Quarto are great.

| *Header 1*                                         | *Header 2*     |
| :------------------------------------------------- | :------------- |
| [Video: What is CERN?](https://www.youtube.com/embed/wo9vZccmqwc) | Regular output |

#### Colspans and Rowspans

Tables containing cells spanning multiple rows or columns are supported across output formats.

***except in PDF margins***

However, using markdown, it is tricky to draw grid tables with spans, and there is no way to express spans in pipe tables.

If you are comfortable with HTML, or use a package that generates HTML, the table cell HTML attributes `colspan` and `rowspan` are a better option.

````markdown
```{=html}
<table>
<tr> <td colspan="2">I span two columns</td><td>C1</td> </tr>
<tr> <td rowspan="2">I span two rows</td><td>B2</td><td>C2</td> </tr>
<tr>                                  <td>B3</td><td>C3</td> </tr>
</table>
```
````

Result:

|                   |                  |    |
| :---------------- | :--------------- | :- |
| I span two columns|                  | C1 |
| I span two rows   | B2               | C2 |
|                   | B3               | C3 |

#### Individual cell alignment

Markdown supports specification of alignment by column, but does not allow setting the alignment of individual cells. The CSS properties `text-align` and `vertical-align` are only available through Raw HTML. (These are not currently supported by PDF/Latex or Pptx output formats, and Docx only supports `text-align`.)

````markdown
```{=html}
<table>
<tr>
<td><img src="https://placehold.co/600x400/png"/></td>
<td style="vertical-align: top">vertical-align: top</td>
<td style="vertical-align: middle">vertical-align: middle</td>
<td style="vertical-align: bottom">vertical-align: bottom</td>
</tr>
<tr> <td style="text-align: left">text-align: left</td> </tr>
<tr> <td style="text-align: center">text-align: center</td> </tr>
<tr> <td style="text-align: right">text-align: right</td> </tr>
</table>
```
````

Result:

| ![600x400 Placeholder](https://placehold.co/600x400/png) |                  |                      |                    |
| :------------------------------------------------------ | :--------------- | :------------------- | :----------------- |
|                                                         | vertical-align: top | vertical-align: middle | vertical-align: bottom |
| text-align: left                                        |                  |                      |                    |
| text-align: center                                      |                  |                      |                    |
| text-align: right                                       |                  |                      |                    |

### Disabling Quarto Table Processing

It’s possible that Quarto’s processing of HTML tables may interfere with the HTML produced computationally with table packages in R and Python (or other supported languages).

When you disable Quarto’s HTML table processing, tables are not translated to Markdown, will not be rendered to other output formats, and can not use Quarto Markdown features, like cross-references, shortcodes, etc. The tables also won’t be visible to Lua filters that act on `Table` nodes.

You can disable Quarto’s HTML table processing at a document level or project level with the option `html-table-processing`:

```yaml
---
format:
  html:
    html-table-processing: none
---
```

This option is also available as a code cell option for Knitr and Jupyter, e.g.

````markdown
```{r}
#| html-table-processing: none
# R Code that generates an HTML table
```
````

To disable Quarto’s HTML table processing for parts of a document use a div with the attribute `html-table-processing="none"`:

```markdown
::: {html-table-processing="none"}
Content with HTML tables you don't want processed.
:::
```

**Library authors:** If you are the author of a library that emits HTML tables you might like to disable Quarto’s processing of HTML tables by adding the attribute `data-quarto-disable-processing="true"` to the `<table>` element. For example:

```html
<table data-quarto-disable-processing="true">
  ...
</table>
```

Additionally, you can add the comment `<!--| quarto-html-table-processing: none -->` to the HTML raw block, and Quarto will not attempt to process it.

