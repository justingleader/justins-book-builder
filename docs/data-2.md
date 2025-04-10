## Data

```{ojs}
Inputs.table(filtered)
```

:::

```{ojs}
//| output: false
data = FileAttachment("palmer-penguins.csv").csv({ typed: true })

filtered = data.filter(function(penguin) {
  return bill_length_min < penguin.bill_length_mm &&
         islands.includes(penguin.island);
})
```
````

