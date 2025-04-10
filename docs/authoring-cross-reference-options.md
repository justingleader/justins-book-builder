## Authoring Cross-Reference Options

Source: [Cross-Reference Options – Quarto](https://quarto.org/docs/authoring/cross-reference-options.html)

### Overview

There are a wide variety of options available for customizing caption labels and references. These options are all specified within the `crossref` key of document metadata.

On this page we highlight some of the most useful, but you can find all available `crossref` options on the [Cross-Reference Options](https://quarto.org/docs/reference/metadata/crossref.html) reference page.

Note that since LaTeX does its own formatting and layout of figures and tables, not all of these options will apply when rendering to PDF. Specifically, delimiter options like `title-delim` and numbering options like `labels` don’t work for PDF output. Additionally, formatting directives are not applied (e.g. italicizing the figure title) for LaTeX titles.

### Titles

You can specify the title prefix used for captions using `*-title` options. You can also specify the delimiter used between the prefix and the caption using the `title-delim` option. For example:

```yaml
---
title: "My Document"
crossref:
  fig-title: Fig      # (default is "Figure")
  tbl-title: Tbl      # (default is "Table")
  title-delim: "—"    # (default is ":")
---
```

### References

You can specify the prefix used for inline reference type using `*-prefix` options. You can also specify whether references should be hyper-linked using the `ref-hyperlink` option. For example:

```yaml
---
title: "My Document"
crossref:
  fig-prefix: figure    # (default is "Figure")
  tbl-prefix: table     # (default is "Table")
  ref-hyperlink: false  # (default is true)
---
```

### Numbering

There are a variety of numbering schemes available for cross-references, including:

*   `arabic` (1, 2, 3)
*   `roman` (I, II, III, IV)
*   `roman i` (i, ii, iii, iv)
*   `alpha x` (start from letter ‘x’)
*   `alpha X` (start from letter ‘X’)

You can specify the numbering scheme used for all types (other than sub-references) using the `labels` option. For sub-references (e.g. subfigures), you can specify the number scheme using the `subref-labels` option. For example:

```yaml
---
title: "My Document"
crossref:
  labels: alpha a         # (default is arabic)
  subref-labels: roman i  # (default is alpha a)
---
```

If you would like, you can specify the number scheme for a specific type using the `*-labels` options. For example:

```yaml
---
title: "My Document"
crossref:
  fig-labels: alpha a     # (default is arabic)
  tbl-labels: alpha a     # (default is arabic)
  subref-labels: roman i  # (default is alpha a)
---
```

If both `labels` and a type specific label option is provided, the type specific option will override the `labels` option.

### Chapter Numbering

You can use the `crossref: chapters` option to indicate that top-level headings (H1) in your document correspond to chapters, and that cross-references should be sub-numbered by chapter. For example:

```yaml
---
title: "My Document"
author: "Jane Doe"
number-sections: true
crossref:
  chapters: true
---

# Introduction

![Elephant](elephant.png)
{#fig-elephant}

See @fig-elephant for an illustration.
```

