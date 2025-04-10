## Dashboards: Layout

Source: [Dashboard Layout – Quarto](https://quarto.org/docs/dashboards/layout.html)

Dashboards are compositions of components used to provide navigation and present data. Below we’ll describe the components that are used to structure the navigation and layout of dashboards.

### Navigation

All dashboards include a top-level navigation bar that provide a title and (optionally) a logo and author. Dashboards with [multiple pages](#pages) also contain a link to each page on the navigation bar:

![Dashboard Navigation Bar](https://quarto.org/docs/dashboards/images/navbar-basic.png)

The `title` and `author` are specified as they are with normal documents. You can also include a `logo` and one or more `nav-buttons`:

```yaml
---
title: "Palmer Penguins"
author: "Cobblepot Analytics"
format:
  dashboard:
    logo: images/penguins.png
    nav-buttons: [linkedin, twitter, github]
---
```

The following special aliases are recognized for navigation buttons: `linkedin`, `facebook`, `reddit`, `twitter`, and `github`. You can also create custom buttons as described in [Nav Items](https://quarto.org/docs/reference/projects/websites.html#nav-items). For example:

```yaml
format:
  dashboard:
    nav-buttons:
      - reddit
      - icon: gitlab
        href: https://gitlab.com/
```

### Layout

Within a page, dashboard components are laid out using alternating sets of rows and columns. Rows and columns are in turn defined by markdown headings and computational cells. For example, here’s a simple layout with two rows, where the second row is split into two columns:

````markdown
---
title: "Palmer Penguins"
author: "Cobblepot Analytics"
format: dashboard
---

