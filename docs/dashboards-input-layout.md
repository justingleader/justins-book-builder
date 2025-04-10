## Dashboards: Input Layout

Source: [Dashboard Input Layout – Quarto](https://quarto.org/docs/dashboards/inputs.html)

### Overview

There are several ways to layout inputs within interactive dashboards:

*   [Sidebars](#sidebars) provide a collapsible vertical panel for inputs.
*   [Toolbars](#toolbars) provide a horizontal panel for inputs.
*   [Card Inputs](#card-inputs) provide a panel for card-specific inputs.

These techniques all create regions for inputs with a special background color to distinguish them from ordinary content. You can also locate inputs anywhere else you wish within a dashboard (i.e. in a standard card).

### Sidebars

Sidebars are a great place to group inputs for dashboards. To include a sidebar, add the `.sidebar` class to a level 2 heading. For example:

````markdown
---
title: "Sidebar"
format: dashboard
server: shiny
---

