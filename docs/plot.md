## Plot

```{ojs}
Plot.rectY(data,
  Plot.stackY(
    Plot.binX(
      {y: "count"},
      {x: "body_mass_g", fill: "species", thresholds: 20})
    )
  )
  .plot({
    facet: {
      data,
      x: "sex"
    },
    marks: [Plot.frame()]
  })
```

