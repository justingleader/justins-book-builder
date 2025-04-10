## Books: Book Crossrefs

Source: [Book Crossrefs – Quarto](https://quarto.org/docs/books/book-crossrefs.html)

### Overview

One important difference between creating a website and a book is that in addition to their web output, books can also be rendered as a single continuous document (e.g a PDF or MS Word document). Books also may or may not be read digitally (which means that internal hyperlinks may or may not be available).

To create books that are consumable in all of these mediums, special care should be taken when creating links to other chapters or sections within chapters (note though that if your book targets *only* HTML output you can feel free to use conventional hyperlinks).

Quarto cross references provide automatic numbering and reference creation for figures, tables, equations, sections, listings, theorems, and proofs. In books, cross references work the same way except they can reach across chapters.

If you aren’t already familiar with using crossrefs you may want to read the documentation on [cross references](https://quarto.org/docs/authoring/cross-references.html) before reading on about how they work with books.

### Creating References

To reference a figure, table, or other cross-referenceable entity, use the `@` syntax (similar to citations) along with the ID / label of the entity you are referencing: For example:

```markdown
See @fig-penginus-by-island for a breakdown by island.
```

References made this way will be automatically resolved across chapters (including the requisite chapter number in the reference).

To make a chapter or section reference-able, you add a `#sec` prefix to its main heading. For example:

```markdown
# Introduction {#sec-introduction}
```

**Label Prefix:** In order for a chapter to be cross-referenceable, its label must start with the `sec-` prefix.

To refer to a section, include a cross-reference to it using an `@` identifier as we did above in the figure example:

```markdown
See @sec-introduction for additional discussion.
```

Which, for example, will render as:

> See Chapter 1 for additional discussion.

The appropriate prefix, “Chapter” or “Section”, will be added to the reference based on the level of the heading. To suppress the prefix, use bracket syntax and prepend `-` before `@`. For example, `[-@sec-introduction]` will produce just “1” without the “Chapter” prefix.

To provide a custom prefix, e.g. “Chapter” for a section heading, spell out the prefix in the bracket syntax. For example:

```markdown
See [Chapter @sec-visualization] for more details on visualizing model diagnostics.
```

Which might render as:

> See Chapter 1.2 for more details on visualizing model diagnostics.

### Section Numbers

By default, all headings in your document create a numbered section. You customize numbering depth using the `number-depth` option. For example, to only number sections immediately below the chapter level, use this:

```yaml
number-depth: 2
```

Note that `toc-depth` is independent of `number-depth` (i.e. you can have unnumbered entries in the TOC if they are masked out from numbering by `number-depth`).

### Chapter Numbering

In books, figures, tables and other cross-reference targets automatically include a chapter number. For example, the following markdown located in Chapter 3 of your book:

```markdown
As illustrated in @fig-geo-comparison, the western states have a much higher incidence of forest fires.
```

Might be rendered as:

> As illustrated in fig. 3.2, the western states have a much higher incidence of forest fires.

Note that while books do support unnumbered chapters, you naturally cannot create cross-references to content in chapters without numbers.

### Hyperlinks

If you are creating an HTML-only book (or a PDF / MS Word book that you don’t expect will be printed) then you can feel free to use normal hyperlinks rather than section cross-references.

To create a hyperlink within a book, provide the source file as the link target. You can also add hash identifiers (`#`) to the source file if you want to link to a particular section in the document. For example:

```markdown
[about](about.qmd)

[about](about.qmd#section)
```

Using the source file as the link target ensures that links will be resolved correctly both for HTML output and for formats that produce a single file (e.g. PDF or MS Word).

Note that if you are targeting printed output for your book you should use explicit cross references to other chapters and sections rather than simple links as shown above. This is because In printed output links aren’t navigable so you need to provide readers with numbered references (e.g. “sec. 5.3”) rather than hyperlinks.

