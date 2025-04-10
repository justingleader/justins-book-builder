## Slide Title {background-color='{{< brand color primary >}}'}
```

**Limitation:** You can’t currently access `typography`, `meta`, or `defaults` values using the `brand` shortcode.

##### In SCSS

The colors defined in `palette` are set as SCSS variables of the form `brand-COLOR_NAME`. For example, if `_brand.yml` defines `blue`:

```yaml
# _brand.yml
color:
  palette:
    blue: "#ddeaf1"
```

Then the variable `$brand-blue` is will be set to `#ddeaf1` in the `defaults` layer of [Quarto’s SCSS layering system](https://quarto.org/docs/output-formats/html-themes-more.html#bootstrap-bootswatch-layering). You can add a custom SCSS file, `styles.scss`, in the usual way:

```yaml
# _quarto.yml
format:
  html:
    theme: [styles.scss]
```

Then `styles.scss` can use these brand variables to make style tweaks. For example, you might want all `h1` elements to be `blue`:

```scss
/* styles.scss */
/*-- scss:rules --*/
h1 {
  color: $brand-blue;
}
```

When you specify SCSS files without an explicit `brand` element, it is equivalent to listing them after `brand`. For instance, the above `theme` is equivalent to:

```yaml
# _quarto.yml
format:
  html:
    theme: [brand, styles.scss]
```

The order of elements in `theme` controls their priority. For example, you could layer brand and your custom SCSS on top of a built-in theme:

```yaml
# _quarto.yml
format:
  html:
    theme: [cosmo, brand, styles.scss]
```

You can learn more about layering themes in [More About Quarto Themes](https://quarto.org/docs/output-formats/html-themes-more.html).

##### Typst

In Typst documents, brand colors are set in a `dictionary` called `brand-color`. You can access them directory in raw Typst blocks using the syntax `brand-color.COLOR_NAME`. For example, you could make a rectangle filled with your `primary` brand color:

```markdown
# document.qmd
```{=typst}
#rect(fill: brand-color.primary)
```
```

##### Lua API

Filters and shortcodes can access brand values using the `brand` Lua module.

```lua
local brand = require('modules/brand/brand')
local primary = brand.get_color('primary')
```

#### Migrating to `_brand.yml`: use the `brand` string in `theme`

**Note:** The following information is only necessary if you are migrating projects created with Quarto 1.5 and earlier to use `_brand.yml`.

Migrating existing projects to Quarto 1.6’s `_brand.yml` support is a straightforward process. The usual way to create themes in Quarto 1.5 and earlier is to use one of the predefined bootswatch themes. This is often combined with an additional user-defined `.scss` file. In Quarto 1.5, a `_quarto.yml` file usually has an entry like the following:

```yaml
# Quarto 1.5 syntax
theme:
  - cosmo        # a predefined bootswatch theme
  - tweaks.scss  # a user-defined customization
```

When using this syntax with Quarto 1.6’s `_brand.yml` support, keep in mind that `_brand.yml` always takes *lowest* priority in styles. In other words, the configuration above is equivalent to the following:

```yaml
# Quarto 1.6 syntax
theme:
  - brand        # theming derived from `_brand.yml`
  - cosmo        # a predefined bootswatch theme
  - tweaks.scss  # a user-defined customization
```

As a result, values set by `brand` here are potentially overriden by the `cosmo` theme or by `tweaks.scss`. This is sometimes useful, but often you will want to make `brand` *more* important than the theme. For these situations, use the following:

```yaml
# Quarto 1.6 syntax
theme:
  - cosmo        # a predefined bootswatch theme
  - brand        # theming derived from `_brand.yml`
  - tweaks.scss  # a user-defined customization
```

Learn more about how Quarto generates styles in [More About Quarto Themes](https://quarto.org/docs/output-formats/html-themes-more.html).

