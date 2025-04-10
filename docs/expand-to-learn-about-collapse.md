## Expand To Learn About Collapse
This is an example of a 'folded' caution callout that can be expanded by the user. You can use `collapse="true"` to collapse it by default or `collapse="false"` to make a collapsible callout that is expanded by default.
:::
```

Note that above callout titles are defined by using a heading at the top of the callout. If you prefer, you can also specify the title using the `title` attribute. For example:

```markdown
::: {.callout-tip title="Tip with Title"}
This is a callout with a title.
:::
```

### Customizing Appearance

#### Collapse

You can create ‘folded’ callouts that can be expanded by the user by settings the `collapse` attribute on the callout. If you set `collapse=true`, the callout will be expandable, but will be collapsed by default. If you set `collapse=false`, the callout will be expandable, but will be expanded by default.

#### Appearance

Callouts have 3 different looks you can use.

*   `default`: The default appearance with colored header and an icon.
*   `simple`: A lighter weight appearance that doesn’t include a colored header background.
*   `minimal`: A minimal treatment that applies borders to the callout, but doesn’t include a header background color or icon.

You can set the callout appearance either globally in the document (or project yaml):

```yaml
callout-appearance: simple
```

or by setting the `appearance` attribute on the callout. For example

```markdown
::: {.callout-note appearance="simple"}
