## Authoring Title Blocks

Source: [Title Blocks – Quarto](https://quarto.org/docs/authoring/title-blocks.html)

### Overview

HTML pages rendered with Quarto include a formatted title block at the start of the article. The title block contains the title, subtitle, authors, date, doi, and abstract.

A simple example title block looks like:

![Simple Title Block Example](https://quarto.org/docs/authoring/images/title-block-simple.png)

The title block will automatically layout elements from the front matter of the document. If you’d like, you can control the behavior using `title-block-style`.

There are three options available:

*   `default`: The default title-block treatment create a smaller font face and gathers the various title elements into stylized groups in the title block of the document.
*   `plain`: The plain treatment will do all the title element processing (gathering and organizing the elements), but will not apply the default title block styling.
*   `none`: `none` disables title block processing altogether. Content will not be processed or organized and the title block will be emitted verbatim from Pandoc.

### Title Banners

In addition, if you’d like a more prominent title block, you can use `title-block-banner` to create a banner style title block. A banner style title block will position the title, subtitle, description, and categories in a banner above the article. For example:

```yaml
---
title-block-banner: true
---
```

will render a title block like:

![Title Banner Example](https://quarto.org/docs/authoring/images/title-block-banner.png)

#### Custom Backgrounds

In this case, the color of the banner is automatically determined based upon the theme. However, you can control the banner background by providing either a CSS color (e.g. `"#FFDDFF"`, or `red`) or the path to an image which will be used the background. For example, to use a banner image, you might write:

```yaml
---
title-block-banner: images/banner.jpeg
---
```

which would render a banner title block like:

![Title Banner with Image Background](https://quarto.org/docs/authoring/images/title-block-banner-image.png)

When you provide an explicit background color or image, Quarto assumes that the color of the background will contrast with the body background color and automatically uses the body background color as the text color over the banner.

#### Foreground Color

You can specify the color the for the text of the banner as well, using `title-block-banner-color` and providing a CSS color (e.g. `"#FFDDFF"`, or `red`).

### Date

Quarto includes the document’s `date` in the title block. In addition to writing a standard date, you may also use a few special keywords which will generate a date for you. `today` will provide the current date with the current time set to 0, `now` will provide the current date and time, and `last-modified` will provide the file modification date and time of the document itself.

#### Formatting

When your title block is output using the `default` or `plain` styles, Quarto will automatically format the date based upon the document locale (`lang`). You can control formatting by specifying a `date-format` in the document front matter. For example:

```yaml
---
title: Summarizing Output for Reproducible Documents
date: 2018-05-04
date-format: short
---
```

For more about date formats, see the Quarto [date format reference](https://quarto.org/docs/reference/dates.html).

### Metadata Labels

The labels for the metadata included in the title block have default values that are properly localized, but you may want to provide your own labels for metadata. You can use the following to customize the labels:

| Option              | Label         | Styles               |
| :------------------ | :------------ | :------------------- |
| `author-title`      | Authors       | `plain`, `default`   |
| `affiliation-title` | Affiliations  | `plain`, `default`   |
| `abstract-title`    | Abstract      | `plain`, `default`, `none` |
| `description-title` | Description   | `plain`, `default`   |
| `published-title`   | Date Published| `plain`, `default`   |
| `doi-title`         | DOI           | `plain`, `default`   |

### Custom Title Pages

To learn more about providing a complete custom title block, see the [documentation on template partials](https://quarto.org/docs/journals/templates.html).

