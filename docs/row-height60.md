## Row {height=60%}

```{python}
#| title: GDP and Life Expectancy
px.scatter(
  df, x="gdpPercap", y="lifeExp",
  animation_frame="year", animation_group="country",
  size="pop", color="continent", hover_name="country",
  facet_col="continent", log_x=True, size_max=45,
  range_x=[100,100000], range_y=[25,90]
)
```

