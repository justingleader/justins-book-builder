## Interactive: OJS Data Sources

Source: [Data Sources – Quarto](https://quarto.org/docs/interactive/ojs/data-sources.html)

### Overview

There are a wide variety of way to make data available to OJS:

*   Read CSV, JSON, SQLite, and more using the [FileAttachments](#file-attachments) API.
*   Use the `ojs_define()` function to make data processed in Python or R available to `{ojs}` cells ([Python and R](#python-and-r)).
*   Make calls to [Web APIs](#web-apis) for online services and data stores.

We’ll explore all of these techniques below.

### File Attachments

Use the `FileAttachment` function from the standard library to read data from a file. For example, here we read and plot a CSV of NOAA’s Monthly [CO2 concentration data](https://gml.noaa.gov/ccgg/trends/data.html) from Mauna Loa:

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

Note that we specified the `typed: true` option to the `csv()` function. When this option is specified [`d3.autoType`](https://github.com/d3/d3-dsv#autoType) is used to automatically detect numbers, dates, etc. and convert them to the correct JavaScript types. This is highly recommend when you know that your data is compatible with automatic type detection.

Here are the methods available for structured data formats:

| Method    | Description                          |
| :-------- | :----------------------------------- |
| `csv`     | Comma separated values               |
| `tsv`     | Tab separated values                 |
| `json`    | JSON (JavaScript objects)            |
| `sqlite`  | SQLite database client               |
| `arrow`   | Apache Arrow IPC file (uncompressed) |

There are also methods to get the raw data as a `blob`, `text`, `image`, or `stream`.

Note that if you are using the `arrow()` method the Apache Arrow IPC file (Feather V2 file) should be written uncompressed. For example:

````markdown
```{r}
arrow::write_feather(
  mtcars, "data.arrow", compression = "uncompressed"
)
```

```{ojs}
data = FileAttachment("data.arrow").arrow()
```
````

### Python and R

The data you want to use with OJS might not always be available in raw form. Often you’ll need to read and preprocess the raw data using Python or R. You can perform this preprocessing during document render (in an `{r}` or `{python}` code cell) and then make it available to `{ojs}` cells via the `ojs_define()` function.

Here’s an example. We’ll read the same data into R, do some grouping and summarization, then make it available to OJS using `ojs_define`:

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

Note that we could have done the same thing using Python (the `ojs_define` function is available in any document that uses R or Python).

Now we plot the data using [Observable Plot](https://github.com/observablehq/plot):

````markdown
```{ojs}
yearlyChart = Plot.plot({
  marks: [
    Plot.line(transpose(co2data), {x: "year", y: "max"}, { stroke: "black" } )
  ]}
)
```
````

See the [NOAA C02](https://quarto.org/docs/interactive/ojs/examples/noaa-co2.html) example for the full source code.

#### Transpose

You’ll note one additional twist in the OJS code above: we call the `transpose` function on our `co2data` before plotting it. The `transpose` function is built in to Quarto’s OJS engine, and will convert column-oriented datasets (like the ones used in Python and R) into the row-oriented datasets used by many JavaScript plotting libraries (including `Plot`).

For example, the following JSON data emitted from R or Python:

```json
{
  "year": [1958, 1959, 1960],
  "max": [317.51, 318.29, 320.04]
}
```

Is converted to the following via the call to `transpose`:

```json
[
  {"year": 1959, "max": 317.51},
  {"year": 1960, "max": 318.29},
  {"year": 1960, "max": 320.04}
]
```

Check the documentation for whatever plotting library you are using from OJS to see whether a call to `transpose` is required.

### Web APIs

You can use the `d3.json()` function to read JSON data from web services and data sources. Here we query the GitHub API for data on contributions to the Python pandas package:

````markdown
```{ojs}
d3 = require('d3')
contributors = await d3.json("https://api.github.com/repos/pandas-dev/pandas/stats/contributors")

commits = contributors.map(contributor => {
  const author = contributor.author;
  return {
    name: author.login,
    title: author.login,
    group: author.type,
    value: contributor.total
  }
})
```
````

View the data sorted by number of commits:

````markdown
```{ojs}
Inputs.table(commits, { sort: "value", reverse: true})
```
````

See the [GitHub API](https://quarto.org/docs/interactive/ojs/examples/github.html) example for the full source code.

