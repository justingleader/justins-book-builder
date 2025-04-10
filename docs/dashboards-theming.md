## Dashboards: Theming

Source: [Dashboard Theming – Quarto](https://quarto.org/docs/dashboards/theming.html)

### Overview

Quarto Dashboards use same Bootstrap 5 based theming system as regular HTML documents (so themes you have built for HTML websites can also be used with dashboards). Use the `theme` option to choose a theme:

```yaml
theme: cosmo
```

Quarto includes 25 themes from the [Bootswatch](https://bootswatch.com/) project (for example, the website uses the `cosmo` theme). Available themes include:

*   `default`, `cerulean`, `cosmo`, `cyborg`, `darkly`, `flatly`, `journal`, `litera`, `lumen`, `lux`, `materia`, `minty`, `morph`, `pulse`, `quartz`, `sandstone`, `simplex`, `sketchy`, `slate`, `solar`, `spacelab`, `superhero`, `united`, `vapor`, `yeti`, `zephyr`

Use of any of these themes via the `theme` option. For example:

```yaml
format:
  dashboard:
    theme: united
```

In the following sections we’ll describe how you can customize these themes or create your own new themes.

### Theme Options

You can do extensive customization of themes using [Sass](https://sass-lang.com/). Bootstrap defines over 1,400 Sass variables that control fonts, colors, padding, borders, and much more. You can see all of the variables here:

<https://github.com/twbs/bootstrap/blob/main/scss/_variables.scss>

Sass theme files can define both *variables* that globally set things like colors and fonts, as well as *rules* that define more fine grained behavior. To customize an existing Bootstrap theme with your own set of variables and/or rules, just provide the base theme and then your custom theme file(s):

```yaml
theme:
  - cosmo
  - custom.scss
```

Your `custom.scss` file might look something like this:

```scss
/*-- scss:defaults --*/
$h2-font-size:          1.6rem !default;
$headings-font-weight:  500 !default;

/*-- scss:rules --*/
h1, h2, h3, h4, h5, h6 {
  text-shadow: -1px -1px 0 rgba(0, 0, 0, .3);
}
```

Note that the variables section is denoted by the `/*-- scss:defaults --*/` comment and the rules section (where normal CSS rules go) is denoted by the `/*-- scss:rules --*/` comment.

### Custom Themes

You can naturally also create an entirely custom theme and provide only that (in this case you will inherit from the default Bootstrap theme):

```yaml
theme: custom.scss
```

For example, here are the theme files for the 25 built-in Bootswatch themes:

<https://github.com/quarto-dev/quarto-cli/tree/main/src/resources/formats/html/bootstrap/themes>

You can read more about the custom theming design [here](https://quarto.org/docs/output-formats/html-themes-more.html).

### Sass Variables

The following Sass Variables can be specified within SCSS files (note that these variables should always be prefixed with a `$` and are specified within theme files rather than within YAML options):

#### Colors

| Variable        | Notes                                                                                            |
| :-------------- | :----------------------------------------------------------------------------------------------- |
| `$body-bg`      | The page background color.                                                                       |
| `$body-color`   | The page text color.                                                                             |
| `$link-color`   | The link color.                                                                                  |
| `$input-bg`     | The background color for HTML inputs.                                                            |
| `$popover-bg`   | The background color for popovers (for example, when a citation preview is shown).               |

#### Fonts

| Variable                 | Notes                                       |
| :----------------------- | :------------------------------------------ |
| `$font-family-sans-serif`| The sans-serif font family for the page.      |
| `$font-family-monospace` | The monospace font family for the page.       |
| `$font-size-root`        | The base font size for the page.            |
| `$toc-font-size`         | The font size for the page TOC.             |
| `$h1-font-size` to `$h5-font-size` | Font sizes for the specified headings. |

#### Code Blocks

| Variable                         | Notes                                                                                                                                                 |
| :------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$code-block-border-left`        | By default, Quarto does not display a left border on code blocks. Set this variable to a truthy value or a CSS color to enable the left border.        |
| `$code-block-border-left-style`  | The style of the left border displayed on code blocks. Defaults to `solid`.                                                                           |
| `$code-block-border-left-size`   | The thickness of the left border displayed on code blocks. Defaults to `3px`;                                                                           |
| `$code-block-padding-left`       | The amount of padding applied between the code and the border. Defaults to `0.6em`.                                                                   |
| `$code-block-bg`                 | By default, Quarto sets a background on code blocks by adding transparency to the theme’s `progress-bg` color. Set this variable to truthy value or a CSS color. |
| `$code-block-bg-padding`         | The padding applied to the code block. Defaults to `0.4em`.                                                                                           |
| `$code-block-bg-alpha`           | The amount to alter the transparency fo the `progress-bg` color. This is not used if an explicit background color is set. Defaults to `-0.35`.            |

#### Code Annotation

You can customize the colors used to highlight lines when [code annotation](https://quarto.org/docs/authoring/code-annotation.html) is used:

| Variable                           | Notes                                                       |
| :--------------------------------- | :---------------------------------------------------------- |
| `$code-annotation-higlight-color`  | The color used as a border on highlighted lines.            |
| `$code-annotation-higlight-bg`     | The color used for the background of highlighted lines.     |

#### Code Copy

You can also customize the colors of the button which appears for `code-copy: true` with the following variables:

| Variable                       | Notes                                                              |
| :----------------------------- | :----------------------------------------------------------------- |
| `$btn-code-copy-color`         | The color used for the copy button at the top right of code blocks.|
| `$btn-code-copy-color-active`  | The hover color used for the copy button at the top right of code blocks. |

#### Inline Code

| Variable     | Notes                                                                                             |
| :----------- | :------------------------------------------------------------------------------------------------ |
| `$code-bg`   | The background color of inline code. Defaults to a mix between the `body-bg` and `body-color`.    |
| `$code-color`| The text color of inline code. Defaults to a generated contrasting color against the `code-bg`.     |

#### Table of Contents

| Variable               | Notes                                                               |
| :--------------------- | :------------------------------------------------------------------ |
| `$toc-color`           | The color for table of contents text.                               |
| `$toc-font-size`       | The font-size for table of contents text.                           |
| `$toc-active-border`   | The left border color for the currently active table of contents item. |
| `$toc-inactive-border` | The left border colors for inactive table of contents items.        |

#### Layout

| Variable              | Notes                                                                                    |
| :-------------------- | :--------------------------------------------------------------------------------------- |
| `$content-padding-top`| Padding that should appear before the main content area (including the sidebar, content, and TOC. |

#### Navigation

| Variable        | Notes                                                                                                                                                           |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$navbar-bg`    | The background color of the navbar. Defaults to the theme’s `$primary` color.                                                                                   |
| `$navbar-fg`    | The color of foreground elements (text and navigation) on the navbar. If not specified, a contrasting color is automatically computed.                          |
| `$navbar-hl`    | The highlight color for links in the navbar. If not specified, the `$link-color` is used or a contrasting color is automatically computed.                      |
| `$sidebar-bg`   | The background color for a sidebar. Defaults to `$light` except when a navbar is present or when the style is `floating`. In that case it defaults to the `$body-bg` color. |
| `$sidebar-fg`   | The color of foreground elements (text and navigation) on the sidebar. If not specified, a contrasting color is automatically computed.                         |
| `$sidebar-hl`   | The highlight color for links in the sidebar. If not specified, the `$link-color` is used.                                                                        |
| `$footer-bg`    | The background color for the footer. Defaults to the `$body-bg` color.                                                                                          |
| `$footer-fg`    | The color of foreground elements (text and navigation) on the footer. If not specified, a contrasting color is automatically computed.                          |

#### Callouts

| Variable                   | Notes                                                                                                       |
| :------------------------- | :---------------------------------------------------------------------------------------------------------- |
| `$callout-border-width`    | The left border width of callouts. Defaults to `5px`.                                                       |
| `$callout-border-scale`    | The border color of callouts computed by shifting the callout color by this amount. Defaults to `0%`.        |
| `$callout-icon-scale`      | The color of the callout icon computed by shifting the callout color by this amount. Defaults to `10%`.       |
| `$callout-margin-top`      | The amount of top margin on the callout. Defaults to `1.25rem`.                                               |
| `$callout-margin-bottom`   | The amount of bottom margin on the callout. Defaults to `1.25rem`.                                             |
| `$callout-color-<type>`    | The colors for the various types of callouts. Defaults: note: `$blue`, tip: `$green`, caution: `$orange`, warning: `$yellow`, important: `$red` |

#### Value Boxes {#value-boxes}

Use the `$valuebox-bg-<type>` variables to override the background color of value boxes that are set with `color: <type>`.

| Variable              | Type              |
| :-------------------- | :---------------- |
| `$valuebox-bg-primary`  | `color: primary`  |
| `$valuebox-bg-secondary`| `color: secondary`|
| `$valuebox-bg-success`  | `color: success`  |
| `$valuebox-bg-info`     | `color: info`     |
| `$valuebox-bg-warning`  | `color: warning`  |
| `$valuebox-bg-danger`   | `color: danger`   |
| `$valuebox-bg-light`    | `color: light`    |
| `$valuebox-bg-dark`     | `color: dark`     |

#### Bootstrap Variables

In addition to the above Sass variables, Bootstrap itself supports hundreds of additional variables. You can [learn more about Bootstrap’s use of Sass variables](https://getbootstrap.com/docs/5.1/customize/sass/) or review the [raw variables and their default values](https://github.com/twbs/bootstrap/blob/main/scss/_variables.scss).

