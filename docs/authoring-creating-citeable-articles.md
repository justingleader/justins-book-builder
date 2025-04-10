## Authoring Creating Citeable Articles

Source: [Creating Citeable Articles – Quarto](https://quarto.org/docs/authoring/create-citeable-articles.html)

### Creating Citeable Articles

You can make it easier for others to cite your work by providing additional metadata with the YAML front-matter of your article. Citations can be provided for both articles published to the web or for articles published in journals (with or without a DOI).

### Web Articles

To provide a citation for an article published to the web, include author and date metadata as well as a citation url. For example:

```yaml
---
title: "Summarizing Output for Reproducible Documents"
description: |
  A summary of the best practices for summarizing output of reproducible scientific documents.
date: 5/4/2018
author:
  - name: Norah Jones
    url: https://example.com/norahjones
    affiliation: Spacely Sprockets
    affiliation-url: https://example.com/spacelysprockets
citation:
  url: https://example.com/summarizing-output
bibliography: biblio.bib
---
```

Name particles can be further defined in the `name` key following the [Citation Style Language (CSL) specification for naming particles](https://docs.citationstyles.org/en/stable/specification.html#name-variables). If you omit the citation url, Quarto will attempt to generate a citation url by using the `site-url` and the current page’s location. If you’d like to allow Quarto to generate the citation url, you can omit the citation url and simply enable citation output on the page. For example:

```yaml
---
title: "Summarizing Output for Reproducible Documents"
description: |
  A summary of the best practices for summarizing output of reproducible scientific documents.
date: 5/4/2018
author:
  - name: Norah Jones
    url: https://example.com/norahjones
    affiliation: Spacely Sprockets
    affiliation-url: https://example.com/spacelysprokets
citation: true
bibliography: biblio.bib
---
```

When this metadata is available, a citation appendix is automatically added to the article. The citation appendix will present both a copy-able `bibtex` representation of the document and a formatted representation of the citation (based upon the document’s CSL file, if specified). For example:

![Citation Appendix Example](https://quarto.org/docs/authoring/images/citeable-appendix.png)

By default both the `bibtex` and formatted representations are displayed. You can use the `appendix-cite-as` option to control this behavior:

*   `appendix-cite-as: false`: Do not include any citations in the appendix.
*   `appendix-cite-as: bibtex`: Show only the BibTeX version of the citation.
*   `appendix-cite-as: display`: Show only the display version of the citation.

### Journal Articles

If your article is published within a Journal, you can add the following the additional fields to generate the appropriate citation entry:

```yaml
---
title: "Summarizing Output for Reproducible Documents"
description: |
  A summary of the best practices for summarizing output of reproducible scientific documents.
date: 5/4/2018
author:
  - name: Norah Jones
    url: https://example.com/norahjones
    affiliation: Spacely Sprockets
    affiliation-url: https://example.com/spacelysprokets
citation:
  type: article-journal
  container-title: "Journal of Data Science Software"
  doi: "10.23915/reprodocs.00010"
  url: https://example.com/summarizing-output
bibliography: biblio.bib
---
```

This is how the citation is presented in the appendix:

![Journal Citation Appendix Example](https://quarto.org/docs/authoring/images/journal-appendix.png)

### Other Types of Documents

The BibTeX and formatted attribution displayed in the document will be generated based upon the complete citation information that is present in the `citation` key, which is based upon the [Citation Style Language (CSL) specification for items](https://docs.citationstyles.org/en/stable/specification.html#appendix-iv-variables). You can learn more about the available options in the [Citation Metadata Reference](https://quarto.org/docs/reference/metadata/citation.html).

### Google Scholar

Quarto documents can include metadata compatible with the format indexed by [Google Scholar](https://scholar.google.com/). This makes it easy for indexing engines (Google Scholar or otherwise) to extract not only a citation for your article but also information on other sources which you cited. To enable this use the `google-scholar` option:

```yaml
title: "Summarizing Output for Reproducible Documents"
description: |
  A summary of the best practices for summarizing output of reproducible scientific documents.
date: 5/4/2018
author:
  - name: Norah Jones
    url: https://example.com/norahjones
    affiliation: Spacely Sprockets
    affiliation-url: https://example.com/spacelysprokets
citation:
  type: article-journal
  container-title: "Journal of Data Science Software"
  doi: "10.23915/reprodocs.00010"
  url: https://example.com/summarizing-output
bibliography: biblio.bib
google-scholar: true
```

For example, here is the Google Scholar metadata automatically included for a document created with the above metadata:

```html
<meta name="citation_title" content="Summarizing Output for Reproducible Documents">
<meta name="citation_author" content="Norah Jones">
<meta name="citation_online_date" content="2018-05-04">
<meta name="citation_fulltext_html_url" content="https://example.com/summarizing-output">
<meta name="citation_publication_date" content="2018-05-04">
<meta name="citation_journal_title" content="Journal of Data Science Software">
<meta name="citation_reference" content="citation_title=Donald knuth;,citation_fulltext_html_url=http://dx.doi.org/10.7551/mitpress/5485.003.0041;,citation_publication_date=1989;,citation_journal_title=undefined;">
```

In the addition to the citation metadata from this document described above, Quarto will automatically generate a `citatation_reference` entry for each of the entries included in the document’s bibliography.

### Citation Fields

Quarto’s approach to emitting scholarly metadata is to take the standard CSL fields and make them into the corresponding Google Scholar / Zotero / Highwire metadata tags as appropriate. The following fields, when specified under the `citation` key of the document metadata, will generate scholarly meta tags in the rendered HTML document as described. These fields comprise the required Google Scholar fields as well as additional, optional fields that may also be included.

| Document Yaml         | Metadata Tag                 | Notes                                                                                                                                                                                           |
| :-------------------- | :--------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`               | `citation_title`             | Document `title` will be used if not provided.                                                                                                                                                |
| `author`              | `citation_author`            | One or more authors[^4]. Document `author` will be used if not provided as a citation subkey.                                                                                                |
| `editor`              | `citation_editor`            | One or more editors[^5].                                                                                                                                                                      |
| `abstract`            | `citation_abstract`          | Document `abstract` will be used if not provided.                                                                                                                                             |
| `keyword`[^6]         | `citation_keywords`          | Document `keywords` will be used if not provided.                                                                                                                                             |
| `issued`              | `citation_publication_date`  | Document `date` will be used if not provided. <br> In addition, the issued date will be used to populate the following fields:<br>`citation_cover_date`<br>`citation_year`                      |
| `available-date`      | `citation_online_date`       | Document `date` will be used if not provided.                                                                                                                                                 |
| `url`                 | `citation_fulltext_html_url` | `url` will be synthesized for current document if a `site-url` has been specified.                                                                                                                |
| `pdf-url`             | `citation_pdf_url`           |                                                                                                                                                                                                 |
| `language`            | `citation_language`          | Document `lang` will be used if not provided.                                                                                                                                                 |
| `type`                | `<none>`                     | A valid CSL type. See [https://docs.citationstyles.org/en/stable/specification.html#appendix-iii-types](https://docs.citationstyles.org/en/stable/specification.html#appendix-iii-types).       |
| `doi`                 | `citation_doi`               | Document `doi` will be used if not provided.                                                                                                                                                  |
| `isbn`                | `citation_isbn`              |                                                                                                                                                                                                 |
| `issn`                | `citation_issn`              |                                                                                                                                                                                                 |
| `eissn`               | `citation_eissn`             |                                                                                                                                                                                                 |
| `pmid`                | `citation_pmid`              |                                                                                                                                                                                                 |
| `issue`               | `citation_issue`             |                                                                                                                                                                                                 |
| `volume`              | `citation_volume`            |                                                                                                                                                                                                 |
| `page`                | `citation_firstpage`, `citation_lastpage` | Will be split on `-` to create appropriate page metadata.                                                                                                                           |
| `page-first`          | `citation_firstpage`         |                                                                                                                                                                                                 |
| `page-last`           | `citation_lastpage`          |                                                                                                                                                                                                 |
| `abstract-url`        | `citation_abstract_html_url` |                                                                                                                                                                                                 |
| `container-title`     | `citation_journal_title`     | For specific types, other meta tags will be produced:<br>`type: paper-conference` -> `citation_conference_title`<br>`type: book` -> `citation_book_title`<br>`type: chapter` -> `citation_inbook_title` |
| `number`              | `citation_technical_report_number` | `citation_technical_report_number` will be created if the type is report.                                                                                                                     |
| `publisher`           | `citation_publisher`         | For specific types, other meta tags will be produced:<br>`type: paper-conference` -> `citation_conference`<br>`type: thesis` -> `citation_dissertation_institution`<br>`type:report` -> `citation_technical_report_institution` |
| `container-title-short`| `citation_journal_abbrev`    |                                                                                                                                                                                                 |
| `collection-title`    | `citation_series_title`      |                                                                                                                                                                                                 |

For example, citation data for a published conference paper defined as such in the document front matter:

```yaml
title: A Published Conference Paper
author:
  - name: Norah Jones
    affiliation: School of Hard Knocks
    orcid: 0000-0001-8715-9476
citation:
  type: paper-conference
  container-title: "Proceedings of the annual conference of the Society for Research"
  publisher: "Society for Research"
  issued: 2020/09/23
  volume: 2
  doi: "10.23915/reprodocs.00010"
  url: https://example.com/summarizing-output
  page-first: 46
  page-last: 53
editor:
  - Don Draper
  - Nick Fury
google-scholar: true
```

provides HTML metadata like:

```html
<meta name="citation_title" content="A Published Conference Paper">
<meta name="citation_author" content="Norah Jones">
<meta name="citation_editor" content="Nick Cage">
<meta name="citation_editor" content="Don Draper">
<meta name="citation_publication_date" content="2020-09-23">
<meta name="citation_cover_date" content="2020-09-23">
<meta name="citation_year" content="2020">
<meta name="citation_fulltext_html_url" content="https://example.com/summarizing-output">
<meta name="citation_doi" content="10.23915/reprodocs.00010">
<meta name="citation_volume" content="2">
<meta name="citation_language" content="en">
<meta name="citation_conference_title" content="Proceedings of the annual conference of the Society for Research">
<meta name="citation_conference" content="Society for Research">
```

#### Footnotes

[^4]: Specify one or more authors using one of the following:<br>`author: Norah Jones`<br>or multiple values like:<br>`author:`<br>`  - Norah Jones`<br>`  - Nick Fury`<br>The list of authors provded under the citation key will be used instead of the document authors when generating the html metadata.
[^5]: Specify one or more editors using one of the following:<br>`editors: Norah Jones`<br>or multiple values like:<br>`editors:`<br>`  - Norah Jones`<br>`  - Nick Fury`
[^6]: Note that the `keyword` citation field is a comma separated string of keywords (consistent with CSL).

