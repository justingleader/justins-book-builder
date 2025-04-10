## Line
The equation of any straight line, called a linear equation, can be written as:
$$ y = mx + b $$
:::

See @thm-line.
```

For LaTeX output, the `amsthm` package is used for typesetting theorems. For other formats an appropriate treatment is used (the above is an example of HTML output).

There are a number of theorem variations supported, each with their own label prefix:

| Label Prefix | Printed Name | LaTeX Environment |
| :----------- | :----------- | :---------------- |
| `#thm-`      | Theorem      | theorem           |
| `#lem-`      | Lemma        | lemma             |
| `#cor-`      | Corollary    | corollary         |
| `#prp-`      | Proposition  | proposition       |
| `#cnj-`      | Conjecture   | conjecture        |
| `#def-`      | Definition   | definition        |
| `#exm-`      | Example      | example           |
| `#exr-`      | Exercise     | exercise          |
| `#sol-`      | Solution     | solution          |
| `#rem-`      | Remark       | remark            |

The `proof` environment receives similar typesetting as theorems, however it is not numbered (and therefore cannot be cross-referenced). To create a proof add the `.proof` class to a div:

```markdown
::: {.proof}
By induction.
:::
```

As with theorems you can optionally include a heading as the first element of the div (or a `name` attribute) to give the environment a caption for typesetting (this typically appears in parentheses after the environment title).

For LaTeX output the `amsthm` package is used to typeset these environments. For other formats a similar treatment is used, but you can further customizing this using CSS.

### Equations

Provide an `#eq-` label immediately after an equation to make it referenceable. For example:

```markdown
Black-Scholes (@eq-black-scholes) is a mathematical model that seeks to explain the behavior of financial derivatives, most commonly options:

$$ \frac{\partial \mathrm C}{ \partial \mathrm t } + \frac{1}{2}\sigma^{2} \mathrm S^{2} \frac{\partial^{2} \mathrm C}{\partial \mathrm S^2} + \mathrm r \mathrm S \frac{\partial \mathrm C}{\partial \mathrm S}\ =   \mathrm r \mathrm C $$ {#eq-black-scholes}
```

Result:

> Black-Scholes (Equation 1) is a mathematical model that seeks to explain the behavior of financial derivatives, most commonly options:
> \[ \frac{\partial \mathrm C}{ \partial \mathrm t } + \frac{1}{2}\sigma^{2} \mathrm S^{2} \frac{\partial^{2} \mathrm C}{\partial \mathrm S^2} + \mathrm r \mathrm S \frac{\partial \mathrm C}{\partial \mathrm S}\ =   \mathrm r \mathrm C \tag{1}\]

Note that the equation number is included (via `\qquad`) in the right margin of the equation.

### Sections

To reference a section, add a `#sec-` identifier to any heading. For example:

```markdown
