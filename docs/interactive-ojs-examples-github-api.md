## Interactive: OJS Examples GitHub API

Source: [GitHub API – Quarto](https://quarto.org/docs/interactive/ojs/examples/github.html)

Demonstration of using the [GitHub API](https://docs.github.com/en/rest).

````markdown
```{ojs}
viewof repo = Inputs.radio(
  ["pandas-dev/pandas", "tidyverse/ggplot2",],
  { label: "Repo:", value: "pandas-dev/pandas"}
)
```
````

````markdown
```{ojs}
import { chart } with { commits as data } from "@d3/d3-bubble-chart"
chart
```
````

````markdown
```{ojs}
//| output: none
d3 = require('d3')
contributors = await d3.json("https://api.github.com/repos/" + repo + "/stats/contributors")

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

````markdown
```{ojs}
Inputs.table(commits, { sort: "value", reverse: true })
```
````

