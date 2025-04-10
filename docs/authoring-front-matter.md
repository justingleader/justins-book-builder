## Authoring Front Matter

Source: [Front Matter – Quarto](https://quarto.org/docs/authoring/front-matter.html)

### Overview

Scholarly articles require much more detail in their front matter than simply a title and an author. Quarto provides a rich set of YAML metadata keys to describe these details. On this page, you’ll learn how to specify authors and their affiliations, article summaries like an abstract and keywords, and how to include information on copyright, licensing and funding.

This YAML header includes examples of all the top level keys discussed on this page:

```yaml
# document.qmd
---
title: "Toward a Unified Theory of High-Energy Metaphysics: Silly String Theory"
date: 2008-02-29
author:
  - name: Josiah Carberry
    id: jc
    orcid: 0000-0002-1825-0097
    email: josiah@psychoceramics.org
    affiliation:
      - name: Brown University
        city: Providence
        state: RI
        url: www.brown.edu
abstract: >
  The characteristic theme of the works of Stone is
  the bridge between culture and society. ...
keywords:
  - Metaphysics
  - String Theory
license: "CC BY"
copyright:
  holder: Josiah Carberry
  year: 2008
citation:
  container-title: Journal of Psychoceramics
  volume: 1
  issue: 1
  doi: 10.5555/12345678
funding: "The author received no specific funding for this work."
---
```

The documents produced by the above metadata for the HTML and JATS formats are shown below.

*   **JATS:** ![JATS Front Matter Example](https://quarto.org/docs/authoring/images/jats-front-matter.png)
*   **HTML:** ![HTML Front Matter Example](https://quarto.org/docs/authoring/images/html-front-matter.png)

Not all of the metadata keys are used in every format. However, the tags described on this page will generally be supported in [journal article formats](https://quarto.org/docs/journals/formats.html). Currently the JATS format makes use of the broadest set of metadata tags, so if you want to check how things render we recommend previewing with `format: jats`.

### Authors & Affiliations

The simplest way to describe an author is with a string directly to the `author` key:

```yaml
---
author: Norah Jones
---
```

However, the `author` key has a number of sub-keys that provide the additional detail required for scholarly articles. For instance, you can add an author’s affiliation by using the `affiliation` key. In the simplest form, an author along with their affiliation can be described by passing a string to each of `name` and `affiliation`:

```yaml
---
author:
  name: Norah Jones
  affiliation: Carnegie Mellon University
---
```

You can read about the other keys you can provide to `author` and `affiliation` in the corresponding [Author](#author) and [Affiliation](#affiliation) sections below.

Both `author` and `affiliation` can take multiple elements to describe multiple authors, or authors with multiple affiliations. As an example, here is the YAML to describe a document with two authors, the first of which has two affiliations:

```yaml
---
author:
  - name: Norah Jones
    affiliation:
      - Carnegie Mellon University
      - University of Chicago
  - name: Josiah Carberry
    affiliation: Brown University
---
```

Notice that each element of `author` and `affiliation` is prefaced by a `-` and indented appropriately. You can read more about shortcuts to avoid repetition when authors share affiliations in the [Multiple Authors](#multiple-authors) section below.

**Singular or Plural?** Both of these keys can be specified using a singular (`author` and `affiliation`) or plural (`authors` and `affiliations`) form.

#### Author

Beyond `name` and `affiliation`, `author` can also take any of the following:

| Available keys to `author` | Type      | Description                                                                                                   |
| :------------------------- | :-------- | :------------------------------------------------------------------------------------------------------------ |
| `email`, `phone`, `fax`, `url` | string    | Contact details for the author. Converted to hyperlinks in many formats.                                          |
| `degrees`                  | string(s) | Academic titles or professional certifications displayed following a personal name.                           |
| `orcid`                    | string    | Author’s Open Researcher and Contributor ID ([ORCID](https://orcid.org/)), in the form `0000-0000-0000-0000`. Creates a link to the author’s ORCID in many formats. |
| `note`, `acknowledgements` | string    | Notes to attach to an author, such as contribution details; Author’s acknowledgements.                          |
| `roles`                    | string(s) | Author’s roles. Read more in [Author Roles](#author-roles) below.                                               |
| `corresponding`, `equal-contributor`, `deceased` | `true`/`false` | Set this author as: the corresponding author; as having contributed equally with all other contributors; and/or deceased. |
| `id`                       | string    | An identifier to be used to refer to this author in other fields. See an example in [Funding](#funding).       |

An `affiliations-url` key can also be provided to `author`, and will be propagated to the `url` key of `affiliation`.

As an example, a more complete description of an author might look like:

```yaml
---
author:
  - name: Josiah Carberry
    orcid: 0000-0002-1825-0097
    url: https://en.wikipedia.org/wiki/Josiah_S._Carberry
    email: josiah@psychoceramics.org
    corresponding: true
---
```

##### Name Components

Quarto will automatically parse the `name` key into its components. However, if this parsing is incorrect you can specify the components, `given`, `family`, `dropping-particle`, and `non-dropping-particle` directly, for example:

```yaml
---
author:
  - name:
      given: Charles
      family: Gaulle
      non-dropping-particle: de
  - name:
      given: Ludwig
      family: Beethoven
      dropping-particle: van
---
```

##### Degrees

You may specify degrees or academic titles using the `degrees` field of authors:

```yaml
author:
  - name: Josiah Carberry
    degrees:
      - B.S.
      - PhD
```

##### Author Roles

Use `roles` to describe an author’s contributions to the work. You can use free form text as a string:

```yaml
author:
  - name: Josiah Carberry
    roles: "Conceived and designed the study, analysed the results and wrote the manuscript."
```

Or alternatively, make use of the [Contributor Roles Taxonomy (CRediT)](https://credit.niso.org/). To use CRediT roles provide one of the [14 contributor](#credit-contributor-roles) roles, e.g.:

```yaml
author:
  - name: Josiah Carberry
    roles: conceptualization
```

Or, an array of roles:

```yaml
author:
  - name: Josiah Carberry
    roles: [investigation, data curation]
```

Or specify the role along with a degree of contribution:

```yaml
author:
  - name: Josiah Carberry
    roles:
      - investigation: lead
      - data curation: supporting
```

**Expand to see the 14 Contributor Roles** {#credit-contributor-roles}

| CRediT contributor values available in `roles` | Alias    |
| :------------------------------------------- | :------- |
| `conceptualization`                          |          |
| `data curation`                              |          |
| `formal analysis`                            | analysis |
| `funding acquisition`                        | funding  |
| `investigation`                              |          |
| `methodology`                                |          |
| `project administration`                     |          |
| `resources`                                  |          |
| `software`                                   |          |
| `supervision`                                |          |
| `validation`                                 |          |
| `visualization`                              |          |
| `writing – review & editing`                 | editing  |
| `writing – original draft`                   | writing  |

#### Affiliation

Like `author`, you can provide a string is directly to `affiliation`, as in:

```yaml
---
author:
  name: Norah Jones
  affiliation: Carnegie Mellon University
---
```

Alternatively, you can provide the name explicitly to the `name` key, like:

```yaml
---
author:
  name: Norah Jones
  affiliation:
    name: Carnegie Mellon University
---
```

In addition to `name`, `affiliation` can take any of the following:

| Available keys to `affiliation` | Type    | Description                                                                                                                                                                                                                                                      |
| :------------------------------ | :------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `department`                    | String  |                                                                                                                                                                                                                                                                  |
| `group`                         | String  | Team or research group within the affiliation                                                                                                                                                                                                                    |
| `address`, `city`, `region` or `state`, `country`, `postal-code` | String  | Affiliation’s location. Provide one of `region` or `state`, and any combination of the other keys.                                                                                                                                |
| `url`                           | String  | Affiliation’s website. Converted to a link in many formats.                                                                                                                                                                                                      |
| `isni`, `ringgold`, `ror`       | Numeric, Numeric, String | Affiliation IDs: 16 digit [International Standard Name Identifier (ISNI)](https://isni.org/); 4-6 digit [Ringgold ID](https://www.ringgold.com/); [Research Organization Registry (ROR) ID](https://ror.org/), starting with `https://ror.org/`, followed by a 9 digit alphanumeric identifier. |

For example, a more complete `affiliation` for an author might look like:

```yaml
---
author:
  name: Josiah Carberry
  orcid: 0000-0002-1825-0097
  url: https://en.wikipedia.org/wiki/Josiah_S._Carberry
  email: josiah@psychoceramics.org
  corresponding: true
  affiliation:
    - name: Brown University
      department: Psychoceramics
      city: Providence
      state: RI
      country: US
      url: www.brown.edu
      ringgold: 6752
      isni: 0000000419369094
---
```

#### Multiple Authors

When there are multiple authors of a document, it is common that they share affiliations. To avoid repeating an affiliation’s details, you can describe an affiliation once, assign it an id, and then refer to the id in other fields.

One approach is to assign an `id` to each affiliation where they are described within an author. For example, here we assign the author’s affiliations the ids `cmu` and `chicago`:

```yaml
---
author:
  - name: Norah Jones
    affiliation:
      - id: cmu
        name: Carnegie Mellon University
      - id: chicago
        name: University of Chicago
---
```

Then, when adding additional authors, you can refer to affiliations using `ref:`:

```yaml
---
author:
  - name: Norah Jones
    affiliation:
      - id: cmu
        name: Carnegie Mellon University
      - id: chicago
        name: University of Chicago
  - name: John Hamm
    affiliation:
      - ref: cmu
---
```

An alternative approach is to define affiliations at the top level, as opposed to within an `author`:

```yaml
---
author:
  - name: Norah Jones
    affiliation:
      - ref: cmu
      - ref: chicago
  - name: John Hamm
    affiliation:
      - ref: cmu
affiliations:
  - id: cmu
    name: Carnegie Mellon University
  - id: chicago
    name: University of Chicago
---
```

This approach may be more convenient in cases where you also want to refer to affiliations in fields other than `author`, e.g. `funding`.

### Abstract

You can add an abstract with the `abstract` key. Since abstracts are generally longer than a line, and may contain markdown, you’ll need to provide it using YAML’s literal block style. That is, place a `|` on the same line as `abstract:` and indent your raw abstract text by two spaces.

For example:

```yaml
---
abstract: |
  This article evaluates novel approaches to do
  some really important things.
---
```

### Keywords

Keywords can be added with `keywords`:

```yaml
---
keywords:
  - open-source
  - scientific publishing
  - reproducible research
---
```

### Copyright

You can specify copyright in two ways. Either directly as a string to `copyright`:

```yaml
---
copyright: "Copyright Acme, Inc. 2021. All Rights Reserved"
---
```

Which is equivalent to providing the same string to the `statement` sub-key:

```yaml
---
copyright:
  statement: "Copyright Acme, Inc. 2021. All Rights Reserved"
---
```

Or, alternatively, by specifying a `holder` and `year`:

```yaml
---
copyright:
  holder: Acme, Inc
  year: 2021
---
```

When specifying `year` you can also use a range (`year: 2021 - 2023`) or an array (`year: [2021, 2022, 2023]`).

### License

To specify a license, you can pass a string directly to `license`:

```yaml
---
license: "This work is dedicated to the Public Domain"
---
```

This is equivalent to specifying the `text` sub-key directly:

```yaml
---
license:
  text: "This work is dedicated to the Public Domain"
---
```

You can add additional details by providing the `type` and `url` sub-keys:

```yaml
---
license:
  text: >
    Permission is granted to copy, distribute and/or
    modify this document under the terms of the GNU Free
    Documentation License, Version 1.3 or any later version
    published by the Free Software Foundation; with no
    Invariant Sections, no Front-Cover Texts, and no
    Back-Cover Texts. A copy of the license is included in
    the section entitled "GNU Free Documentation License"
  type: open-access
  url: https://www.gnu.org/licenses/fdl-1.3-standalone.html
---
```

If you are choosing a Creative Commons license you may simply pass an abbreviation:

```yaml
---
license: "CC BY"
---
```

The available abbreviations are covered in the [Creative Commons](#creative-commons) section below.

#### Creative Commons

The [Creative Commons](https://creativecommons.org/) copyright licenses and tools forge a balance inside the traditional “all rights reserved” setting that copyright law creates. These tools give everyone from individual creators to large companies and institutions a simple, standardized way to grant copyright permissions to their creative work.

Here are some of the common forms of Creative Commons content license:

| License      | Name                               | Description                                                                                                                                                                                                                                                                                                       |
| :----------- | :--------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CC BY`      | Attribution                        | This license lets others distribute, remix, tweak, and build upon your work, even commercially, as long as they credit you for the original creation. This is the most accommodating of licenses offered.                                                                                                      |
| `CC BY-SA`   | Attribution-ShareAlike             | This license lets others remix, tweak, and build upon your work even for commercial purposes, as long as they credit you and license their new creations under the identical terms. This license is often compared to “copyleft” free and open source software licenses. All new works based on yours will carry the same license, so any derivatives will also allow commercial use. |
| `CC BY-ND`   | Attribution-NoDerivs               | This license allows for redistribution, commercial and non-commercial, as long as it is passed along unchanged and in whole, with credit to you.                                                                                                                                                                 |
| `CC BY-NC`   | Attribution-NonCommercial          | This license lets others remix, tweak, and build upon your work non-commercially, and although their new works must also acknowledge you and be non-commercial, they don’t have to license their derivative works on the same terms.                                                                             |
| `CC BY-NC-SA`| Attribution-NonCommercial-ShareAlike | This license lets others remix, adapt, and build upon your work non-commercially, as long as they credit you and license their new creations under the identical terms. |
| `CC BY-NC-ND`| Attribution-NonCommercial-NoDerivs | This license is the most restrictive of the six main licenses, only allowing others to download your works and share them with others as long as they credit you, but they can’t change them in any way or use them commercially.                                                                              |
| `CC0`        | CC0 (aka CC Zero) is a public dedication tool, which enables creators to give up their copyright and put their works into the worldwide public domain. CC0 enables reusers to distribute, remix, adapt, and build upon the material in any medium or format, with no conditions. |

If you specify a Creative Commons license for your content, Quarto will automatically include the relevant link to the appropriate license.

### Citation

The `citation` key allows you to specify additional metadata that is used to create a citation for the document. You can read more about this in [Creating Citeable Articles](https://quarto.org/docs/authoring/create-citeable-articles.html).

### Funding

The `funding` key can directly take a string:

```yaml
---
funding: "The author(s) received no specific funding for this work."
---
```

This is equivalent to providing the `statement` sub-key directly:

```yaml
---
funding:
  statement: "The author(s) received no specific funding for this work."
---
```

The `funding` key can also take the sub-keys `source`, `recipient` and `investigator`. Both `recipient` and `investigator` can take a string, or a reference to an author or affiliation using `ref:`. For example, this front matter adds funding where the investigator is specified using an author id:

```yaml
---
author:
  - name: Norah Jones
    id: nj
funding:
  - source: "NIH (Grant #: 1-R01-MH99999-01A1)"
    investigator:
      - ref: nj
---
```

