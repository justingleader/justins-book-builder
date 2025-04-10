## Pay Attention
Using callouts is an effective way to highlight content that your reader give special consideration or attention.
:::

### Format Support

The following formats render callouts as illustrated above:

*   HTML
*   PDF
*   MS Word
*   EPUB
*   Revealjs (without collapse option)

Note that callout rendering for HTML is not available when you disable the standard HTML theme (e.g. if you specify the `theme: none` option). Also, some features are specific to document using Bootstrap, like collapsible callouts, and won’t work in other documents.

When the target format doesn’t support callouts, they are rendered as a simple blockquote with the title in bold.

### Cross-References

To cross-reference a callout, add an ID attribute that starts with the appropriate callout prefix (see [Table 1](#tbl-callout-prefixes)). You can then reference the callout using the usual `@` syntax. For example, here we add the ID `#tip-example` to the callout, and then refer back to it:

```markdown
::: {#tip-example .callout-tip}
