## Data

```{ojs}
Inputs.table(filtered)
```

:::
````

See the [Layout](https://quarto.org/docs/interactive/ojs/examples/layout.html) example for the full source code.

Learn more in the article on [Layout](https://quarto.org/docs/interactive/layout.html) for interactive documents.

### Cell Figures

OJS cells can also be rendered as numbered, [cross-referenceable](https://quarto.org/docs/authoring/cross-references.html) figures. To do this, add the `label` and `fig-cap` options to the cell. For example:

````markdown
```{ojs}
//| echo: fenced
//| label: fig-penguin-body-mass
//| fig-cap: "Penguin body mass by sex and species"

Plot.rectY(filtered,
  Plot.binX({y: "count"}, {x: "body_mass_g", fill: "species", thresholds: 20}))
  .plot({
    facet: {
      data: filtered,
      x: "sex",
      y: "species",
      marginRight: 80
    },
    marks: [
      Plot.frame(),
    ]
  }
)
```
````

Result:

> ```ojs
> Plot.rectY(filtered,
>   Plot.binX({y: "count"}, {x: "body_mass_g", fill: "species", thresholds: 20}))
>   .plot({
>     facet: {
>       data: filtered,
>       x: "sex",
>       y: "species",
>       marginRight: 80
>     },
>     marks: [
>       Plot.frame(),
>     ]
>   }
> )
> ```
>
> ![Figure 1: Penguin body mass by sex and species](https://quarto.org/docs/interactive/ojs/ojs-cells_files/figure-html/fig-penguin-body-mass-output-1.png){#fig-penguin-body-mass}

See Figure 1 for further illustration.

To reference the figure use its label in a markdown [cross reference](https://quarto.org/docs/authoring/cross-references.html):

```markdown
See @fig-penguin-body-mass for further illustration.
```

