## {.toolbar}

```{python}
```
````

### Card Inputs

In some cases you may want to connect inputs more directly to a single output. You can do this using either a card toolbar or card sidebar.

#### Card Toolbars

To add a toolbar to a card, define it immediately above or below the cell that generates the output. You can do this by either adding the `content: card-toolbar` option to a cell or by creating a div with the `.card-toolbar` class. For example:

````markdown
```{python}
#| content: card-toolbar
```

```{python}
#| title: Penguin Bills
```
````

Note that the `title` attribute is optional for cells with toolbars (if there is no `title` then the inputs will be left rather than right aligned).

#### Card Sidebars

To add a sidebar to a card, define it immediately to the left or the right of the cell that generates the output. You can do this either by adding the `content: card-sidebar` option to a cell or by creating a div with the `.card-sidebars` class. For example:

````markdown
```{python}
#| content: card-sidebar
```

```{python}
#| title: Penguin Bills
```
````

