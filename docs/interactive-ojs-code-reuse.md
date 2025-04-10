## Interactive: OJS Code Reuse

Source: [Code Reuse – Quarto](https://quarto.org/docs/interactive/ojs/code-reuse.html)

As you build larger Quarto projects (like [websites](https://quarto.org/docs/websites/) and [books](https://quarto.org/docs/books/)) that incorporate OJS, you’ll likely want to re-use code, data, and output across different pages.

### Modules

JavaScript modules are directly supported in Quarto’s OJS blocks. For example, if we have the following source file `square.js`:

```javascript
export function square(x) {
  return x * x;
}
```

Then you can import and use the `square()` function as follows:

````markdown
```{ojs}
import { square } from "./square.js";
square(5)
```
````

### Data

You may be using Python or R to pre-process data that is then provided to OJS via the `ojs_define()` function (this is described in more depth in the [Data Sources](https://quarto.org/docs/interactive/ojs/data-sources.html) article). If you want to share data prepared in this fashion you can import it directly from another `.qmd`.

For example, here we import the `co2data` that we read and pre-processed with dplyr in `data-sources.qmd`:

````markdown
```{ojs}
import { co2data } from "./data-sources.qmd";
Inputs.table(transpose(co2data))
```
````

### Output

You can import any reactive value from another `.qmd` file. Here, we’re reusing a chart directly from `data-sources.qmd`:

````markdown
```{ojs}
import { yearlyChart } from "./data-sources.qmd";
yearlyChart
```
````

