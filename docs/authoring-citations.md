## Authoring Citations

Source: [Citations – Quarto](https://quarto.org/docs/authoring/citations.html)

### Overview

Quarto will use Pandoc to automatically generate citations and a bibliography in a number of styles. To use this capability, you will need:

1.  A quarto document formatted with citations (see [Citation Markdown](#citation-syntax)).
2.  A bibliographic data source, for example a BibLaTeX (`.bib`) or BibTeX (`.bibtex`) file.
3.  Optionally, a [CSL](https://citationstyles.org/) file which specifies the formatting to use when generating the citations and bibliography (when not using `natbib` or `biblatex` to generate the bibliography).

**Note:** When using `format: typst`, by default citation processing is handled by Typst, not Pandoc. See the [Typst](#typst-citations) section below for more details.

### Bibliography Files

Quarto supports bibliography files in a wide variety of formats including BibLaTeX and CSL. Add a bibliography to your document using the `bibliography` YAML metadata field. For example:

```yaml
---
title: "My Document"
bibliography: references.bib
---
```

**Tip:** You can provide more than one bibliography file if you would like by setting the `bibliography` field’s value to a YAML array.

See the [Pandoc Citations](https://pandoc.org/MANUAL.html#citations) documentation for additional information on bibliography formats.

### Citation Syntax

Quarto uses the standard Pandoc markdown representation for citations (e.g. `[@citation]`) — citations go inside square brackets and are separated by semicolons. Each citation must have a key, composed of ‘@’ + the citation identifier from the database, and may optionally have a prefix, a locator, and a suffix. The citation key must begin with a letter, digit, or `_`, and may contain alphanumerics, `_`, and internal punctuation characters (`:.#$%&-+?<>~/`). Here are some examples:

| Markdown Format                                                               | Output (default)                                            | Output(`csl: diabetologia.csl`) |
| :---------------------------------------------------------------------------- | :---------------------------------------------------------- | :-------------------------------- |
| `Blah Blah [see @knuth1984, pp. 33-35;`<br>`also @wickham2015, chap. 1]`      | Blah Blah (see Knuth 1984, 33–35; also Wickham 2015, chap. 1) | Blah Blah see \[1\], pp. 33-35; also \[1\], chap. 1 |
| `Blah Blah [@knuth1984, pp. 33-35,`<br>`38-39 and passim]`                     | Blah Blah (Knuth 1984, 33–35, 38–39 and passim)             | Blah Blah \[1\], pp. 33-35, 38-39 and passim |
| `Blah Blah [@wickham2015; @knuth1984].`                                        | Blah Blah (Wickham 2015; Knuth 1984).                       | Blah Blah \[1, 2\].                |
| `Wickham says blah [-@wickham2015]`                                           | Wickham says blah (2015)                                    | Wickham says blah \[1\]            |

You can also write in-text citations, as follows:

| Markdown Format               | Output (author-date format) | Output (numerical format) |
| :---------------------------- | :-------------------------- | :------------------------ |
| `@knuth1984 says blah.`       | Knuth (1984) says blah.     | \[1\] says blah.          |
| `@knuth1984 [p. 33] says blah.`| Knuth (1984, 33) says blah. | \[1\] \[p. 33\] says blah. |

See the [Pandoc Citations](https://pandoc.org/MANUAL.html#citations) documentation for additional information on citation syntax.

### Citation Style

Quarto uses Pandoc to format citations and bibliographies. By default, Pandoc will use the *Chicago Manual of Style* author-date format, but you can specify a custom formatting using CSL ([Citation Style Language](https://citationstyles.org/)). To provide a custom citation stylesheet, provide a path to a CSL file using the `csl` metadata field in your document, for example:

```yaml
---
title: "My Document"
bibliography: references.bib
csl: nature.csl
---
```

You can find CSL files or learn more about using styles at the [CSL Project](https://citationstyles.org/). You can browse the list of more than 8,500 Creative Commons CSL definitions in the CSL Project’s [central repository](https://github.com/citation-style-language/styles) or Zotero’s [style repository](https://www.zotero.org/styles).

`CSL` styling is only available when the `cite-method` is `citeproc` (which it is by default). If you are using another `cite-method`, you can control the formatting of the references using the mechanism provided by that method.

### Bibliography Generation

By default, Pandoc will automatically generate a list of works cited and place it in the document if the style calls for it. It will be placed in a div with the id `refs` if one exists:

```markdown
### References

::: {#refs}
:::
```

If no such div is found, the works cited list will be placed at the end of the document.

**Tip:** You can suppress generation of a bibliography by including `suppress-bibliography: true` option in your document metadata

Here’s an example of a generated bibliography:

> Knuth, Donald E. 1984. “Literate Programming.” *The Computer Journal* 27 (2): 97–111.
>
> Wickham, Hadley. 2015. *R Packages*. 1st ed. O’Reilly Media, Inc.

#### Including Uncited Items

If you want to include items in the bibliography without actually citing them in the body text, you can define a dummy `nocite` metadata field and put the citations there:

```yaml
---
nocite: |
  @item1, @item2
---
@item3
```

In this example, the document will contain a citation for `item3` only, but the bibliography will contain entries for `item1`, `item2`, and `item3`.

It is possible to create a bibliography with all the citations, whether or not they appear in the document, by using a wildcard:

```yaml
---
nocite: |
  @*
---
```

### LaTeX: using BibLaTeX or natbib

When creating PDFs, you can choose to use either the default Pandoc [citation handling](https://pandoc.org/MANUAL.html#citations) based on citeproc, or alternatively use `natbib` or `BibLaTeX`. This can be controlled using the `cite-method` option. For example:

```yaml
format:
  pdf:
    cite-method: biblatex
```

The default is to use `citeproc` (Pandoc’s built in citation processor).

See the main article on using [Citations](https://quarto.org/docs/authoring/citations.html) with Quarto for additional details on citation syntax, available bibliography formats, etc.

#### Options

When using natbib or biblatex you can specify the following additional options to affect how bibliographies are rendered:

| Option             | Description           |
| :----------------- | :-------------------- |
| `biblatexoptions`  | List of options for biblatex |
| `natbiboptions`    | List of options for natbib |
| `biblio-title`     | Title for bibliography |
| `biblio-style`     | Style for bibliography |

### Typst {#typst-citations}

Typst comes with its [own citation processing system for bibliographies](https://typst.app/docs/reference/bibliography/) and using `format: typst` defaults to it. To specify a bibliography style using Typst’s system, use the `bibliographystyle` option. Provide a string from [Typst’s list of built-in styles](https://typst.app/docs/reference/bibliography/bibliography/#parameters-style), e.g.:

```yaml
bibliography: refs.bib
bibliographystyle: apa
```

Or alternatively, provide a path to a local CSL file:

```yaml
bibliography: refs.bib
bibliographystyle: my-csl-style.csl
```

If you prefer to use Pandoc’s citation processing, set `citeproc: true` explicitly in YAML header:

```yaml
citeproc: true
bibliography: refs.bib
csl: https://www.zotero.org/styles/apa-with-abstract
```

To provide a citation style file to Pandoc’s citation processing system use the `csl` option, as described in [Citation Style](#citation-style).

