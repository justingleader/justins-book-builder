## Output Formats: HTML Theming

Source: [HTML Theming – Quarto](https://quarto.org/docs/output-formats/html-themes.html)

### Overview

HTML documents rendered with Quarto use Bootstrap 5 by default. This can be disabled or customized via the `theme` option:

```yaml
theme: default   # bootstrap 5 default
theme: cosmo     # cosmo bootswatch theme
theme: pandoc    # pandoc default html treatment
theme: none      # no theme css added to document
```

Quarto includes 25 themes from the [Bootswatch](https://bootswatch.com/) project (for example, this website uses the `cosmo` theme). Available themes include:

*   `default`, `cerulean`, `cosmo`, `cyborg`, `darkly`, `flatly`, `journal`, `litera`, `lumen`, `lux`, `materia`, `minty`, `morph`, `pulse`, `quartz`, `sandstone`, `simplex`, `sketchy`, `slate`, `solar`, `spacelab`, `superhero`, `united`, `vapor`, `yeti`, `zephyr`

Use of any of these themes via the `theme` option. For example:

```yaml
format:
  html:
    theme: united
```

You can also customize these themes or create your own new themes. Learn how to do this below in [Theme Options](#theme-options).

### Basic Options

If you are using a Bootstrap theme or the Pandoc theme, there are a set of options you can provide in document metadata to customize its appearance. These include:

| Option          | Description                                                                         |
| :-------------- | :---------------------------------------------------------------------------------- |
| `max-width`     | The maximum width occupied by page content. Defaults to 1400px for bootstrap themes and 36em for the pandoc theme. |
| `mainfont`      | Sets the `font-family` property for the document.                                   |
| `fontsize`      | Sets the base CSS `font-size` for the document.                                     |
| `fontcolor`     | Sets the default text `color` for the document.                                     |
| `linkcolor`     | Sets the default text `color` for hyperlinks.                                       |
| `monofont`      | Sets the `font-family` property for `<code>` elements.                              |
| `monobackgroundcolor` | Sets the `background-color` property for `<code>` elements.                   |
| `linestretch`   | Sets the CSS `line-height` property (affects distance between lines of text, defaults to 1.5). |
| `backgroundcolor` | Sets the `background-color` for the document.                                     |
| `margin-left`, `margin-right`, `margin-top`, `margin-bottom` | Sets the CSS `margin` properties for the document body.                     |

For example. here we set the font-size a bit larger and specify that we want a bit more space between lines of text:

```yaml
title: "My Document"
format:
  html:
    theme: cosmo
    fontsize: 1.1em
    linestretch: 1.7
```

### Theme Options {#theme-options}

You can do extensive customization of themes using [Sass](https://sass-lang.com/). Bootstrap defines over 1,400 Sass variables that control fonts, colors, padding, borders, and much more. You can see all of the variables here: <https://github.com/twbs/bootstrap/blob/main/scss/_variables.scss>

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

### Dark Mode

In addition to providing a single theme for your html output, you may also provide a light and dark theme. For example:

```yaml
theme:
  light: flatly
  dark: darkly
```

Setting the above themes in your `_quarto.yml` results in both a dark and light version of your output being available. For example:

*   **Flatly Themed Output:** ![Flatly Theme Example](https://quarto.org/docs/output-formats/images/theme-flatly.png)
*   **Darkly Themed Output:** ![Darkly Theme Example](https://quarto.org/docs/output-formats/images/theme-darkly.png)

When providing both a dark and light mode for your html output, Quarto will automatically create a toggle to allow your reader to select the desired dark or light appearance. The toggle will automatically appear in the top right corner of your html output. When possible, the toggle will use browser local storage to maintain the user’s preference across sessions.

The first appearance (light or dark) elements in the theme to determine the default appearance for your html output. For example, since the `light` option appears first in the above example, a reader will see the light appearance by default.

Quarto will automatically select the appropriate light or dark version of the text highlighter that you have specified when possible. For more information, see [Code Highlighting](https://quarto.org/docs/output-formats/html-code.html#highlighting).

#### Customizing Themes

As when providing a single theme, you may provide a custom theme for dark and light mode, or a list of `scss` files to customize the light and dark appearance. This website, for example uses the following to use a light `cosmo` theme and then customizes the `cosmo` theme with additional Sass variables when in dark mode:

```yaml
theme:
  light: cosmo
  dark: [cosmo, theme-dark.scss]
```

The contents of `theme-dark.scss` which is customizing the cosmo document appearance is:

```scss
/*-- scss:defaults --*/

// Base document colors
$body-bg: #181818;
$body-color: white;
$link-color: #75AADB;

// Code blocks
$code-block-bg-alpha: -.8;
```

For more information about available Sass variables, see [HTML Customization Using Sass Variables](#sass-variables).

### Sass Variables {#sass-variables}

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

#### Value Boxes

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

