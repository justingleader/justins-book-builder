## Data

```{ojs}
Inputs.table(filtered)
```

:::
````

Read and filter the data based on the user’s inputs:

````markdown
```{ojs}
//| output: false
data = FileAttachment("palmer-penguins.csv").csv({typed: true})

filtered = data.filter(function(penguin) {
  return bill_length_min < penguin.bill_length_mm &&
         islands.includes(penguin.island);
})
```
````

### `width` and `layoutWidth`: fine-grained layout tracking

Like ObservableHQ, `ojs` cells support the reactive `width` which tracks the `clientWidth` of the main HTML element.

````markdown
```{ojs}
width
```
````

In addition, if you need the widths of specific parts of the layout, use the CSS class `ojs-track-layout` in a div. Quarto’s OJS runtime tracks all such divs in `layoutWidth`. In this example, the tabset above has id `penguins-tabset`, and you can see its `clientWidth` reactively below. If this webpage is sufficiently wide, the sidebar will take up some of the space and the width of the resulting tabset will be smaller:

````markdown
```{ojs}
layoutWidth['penguins-tabset']
```
````

