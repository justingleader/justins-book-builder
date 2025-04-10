## Heading

Some text below
```

**Output:**
```
Pandoc
  Meta
    { unMeta = fromList [] }
  [ Header
      2
      ( "heading" , [] , [] )
      [ Str "Heading" ]
  , Para
      [ Str "Some"
      , Space
      , Str "text"
      , Space
      , Str "below"
      ]
  ]
```

Here we add a simple filter to the document that wraps all headers in `pandoc.Emph` (italics). You can see that the `Emph` AST element now wraps the heading text in the `native` output:

**document.qmd**
```yaml
---
format: native
filters: [filter.lua]
---

