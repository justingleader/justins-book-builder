## Interactive: OJS Examples NOAA CO2

Source: [NOAA CO2 – Quarto](https://quarto.org/docs/interactive/ojs/examples/noaa-co2.html)

Read and plot a CSV of NOAA’s Monthly [CO2 concentration data](https://gml.noaa.gov/ccgg/trends/data.html) from Mauna Loa:

````markdown
```{ojs}
data = {
  const co2data = await FileAttachment("co2_mm.csv").csv({ typed: true });
  return co2data.map(d => {
    d["decimal date"] = Number(d["decimal date"]);
    d.average = Number(d.average);
    return d;
  });
}

Plot.plot({
  marks: [
    Plot.line(data, { x: "decimal date", y: "average"}, { stroke: "black" } )
  ]
})
```
````

Read the same data into R, do some grouping and summarization, then make it available using `ojs_define`:

````markdown
```{r}
#| output: false
library(readr)
library(dplyr)

co2 = read_csv("co2_mm.csv")  %>%
  group_by(year) %>%
  summarize(max = max(average))
ojs_define(co2data = co2)
```
````

Now plot the summarized data:

````markdown
```{ojs}
Plot.plot({
  marks: [
    Plot.line(transpose(co2data), {x: "year", y: "max"}, { stroke: "black" } )
  ]}
)
```
````

