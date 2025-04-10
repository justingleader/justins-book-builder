## Authoring Language

Source: [Document Language – Quarto](https://quarto.org/docs/authoring/language.html)

### Overview

Document language plays a role in Pandoc’s processing of most formats, and controls hyphenation in PDF output when using LaTeX (through `babel` and `polyglossia`) or ConTeXt.

Additonally, Quarto, Pandoc, and LaTeX will sometimes generate textual output that requires localization. For example, “Figure” or “List of Figures” for cross references, callout captions like “Note” or “Warning”, or the “Code” caption for folded code chunks.

### `lang` Option

The `lang` document option identifies the main language of the document using IETF language tags (following the [BCP 47](https://tools.ietf.org/html/bcp47) standard), such as `en` or `en-GB`. The [Language subtag lookup](https://r12a.github.io/app-subtags/) tool can look up or verify these tags.

For example, this document specifies the use of French:

```yaml
---
title: "My Document"
lang: fr
---
```

This will result in the use of French translations as well as the application of other language specific rules to document processing. The following languages currently have full translations available:

*   English (`en`, used by default)
*   Chinese (`zh`)
*   Spanish (`es`)
*   French (`fr`)
*   Japanese (`ja`)
*   German (`de`)
*   Portuguese (`pt`)
*   Russian (`ru`)
*   Czech (`cs`)
*   Finnish (`fi`)
*   Dutch (`nl`)
*   Italian (`it`)
*   Polish (`pl`)
*   Korean (`ko`)

### Alternate Language

If you aren’t happy with the default language used for a given part of a document you can provide alternate language via the `language` key (this can be used at a document or project level). For example, to override the values for the “Author” and “Published” captions used within title blocks you could do this:

```yaml
---
title: "My Document"
author: "Norah Jones"
date: 5/22/2022
language:
  title-block-author-single: "Writer"
  title-block-published: "Updated"
---
```

As described below, you can also provide these translations in a standalone YAML file and reference it as follows:

```yaml
---
title: "My Document"
author: "Norah Jones"
date: 5/22/2022
language: custom.yml
---
```

You can discover all of the `language` values that can be customized by referencing this file: [https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/language/_language.yml](https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/language/_language.yml).

### Per-Language Alternates

Alternate values can be restricted to a particular target language using subkeys of the `language` key. This way, distinct values can be defined for each language. For example, you can override the English and French versions of the “Published” caption:

```yaml
---
title: "My Document"
author: "Norah Jones"
date: 5/22/2022
lang: fr
language:
  en:
    title-block-published: "Updated"
  fr:
    title-block-published: "Mis à jour"
---
```

In this case the French “Mis à jour” will be used since `lang` is set to `fr`.

These language-specific alternate values can also be provided in a standalone YAML file. For example, the following file could be used by setting `language: custom-language.yml` in the metadata:

**custom-language.yml**
```yaml
en:
  title-block-published: "Updated"
fr:
  title-block-published: "Mis à jour"
```

### Custom Translations

You can create and use a custom translation for a new language not supported by Quarto as follows:

1.  Make a copy of the default `_language.yml` file ([https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/language/_language.yml](https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/language/_language.yml)).
2.  Provide translations from the default English values.
3.  Specify the custom translation file using the `language` option. For example:

```yaml
---
language: custom.yml
---
```

The `language` option can be specified at a project or document level. Additionally, if you include a `_language.yml` file in the root of your project alongside your `_quarto.yml` config file it will be automatically used.

If you create a language translation file please consider contributing it so others can benefit from it. See the documentation on [contributing language translations](https://github.com/quarto-dev/quarto-cli/blob/main/CONTRIBUTING.md#language-translations) for additional details.

