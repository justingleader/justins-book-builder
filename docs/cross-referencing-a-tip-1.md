## Cross-Referencing a Tip
Add an ID starting with `#tip-` to reference a tip.
:::

See @tip-example...
```

This renders as follows:

> **Tip 1: Cross-Referencing a Tip**
>
> Add an ID starting with `#tip-` to reference a tip.
>
> See Tip 1…

The prefixes for each type of callout are:

Table 1: Prefixes for callout cross-references

| Callout Type | Prefix |
| :----------- | :----- |
| note         | #nte-  |
| tip          | #tip-  |
| warning      | #wrn-  |
| important    | #imp-  |
| caution      | #cau-  |

### Theorems and Proofs

Theorems are commonly used in articles and books in mathematics. To include a reference-able theorem, create a div with a `#thm-` label (or one of other theorem-type labels described below). You also need to specify a theorem name either via the first heading in the block. You can include any content you like within the div. For example:

```markdown
::: {#thm-line}
