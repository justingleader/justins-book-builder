## Authoring Callouts

Source: [Callout Blocks – Quarto](https://quarto.org/docs/authoring/callouts.html)

### Callout Blocks

Callouts are an excellent way to draw extra attention to certain concepts, or to more clearly indicate that certain content is supplemental or applicable to only some scenarios.

### Callout Types

There are five different types of callouts available.

*   note
*   warning
*   important
*   tip
*   caution

The color and icon will be different depending upon the type that you select. Here are what the various types look like in HTML output:

::: {.callout-note}
Note that there are five types of callouts, including: `note`, `tip`, `warning`, `caution`, and `important`.
:::

::: {.callout-warning}
Callouts provide a simple way to attract attention, for example, to this warning.
:::

::: {.callout-important}
This is Important

Danger, callouts will really improve your writing.
:::

::: {.callout-tip title="Tip With Title"}
This is an example of a callout with a title.
:::

::: {.callout-caution collapse="true" title="Expand To Learn About Collapse"}
This is an example of a ‘collapsed’ caution callout that can be expanded by the user. You can use `collapse="true"` to collapse it by default or `collapse="false"` to make a collapsible callout that is expanded by default.

*This feature is not available for Revealjs presentations yet (See Issue [1328](https://github.com/quarto-dev/quarto-cli/issues/1328))*
:::

### Markdown Syntax

Create callouts in markdown using the following syntax (note that the first markdown heading used within the callout is used as the callout heading):

```markdown
::: {.callout-note}
Note that there are five types of callouts, including:
`note`, `warning`, `important`, `tip`, and `caution`.
:::

::: {.callout-tip}
