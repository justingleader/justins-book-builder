## Computations: R

Source: [Using R – Quarto](https://quarto.org/docs/computations/r.html)

### Overview

Quarto is a multi-language, [next generation](https://quarto.org/docs/faq/rmarkdown.html) version of R Markdown from Posit and includes dozens of new features and capabilities while at the same being able to render most existing Rmd files without modification.

Like R Markdown, Quarto uses [`Knitr`](https://yihui.org/knitr/) to execute R code, and is therefore able to render most existing Rmd files without modification.

We’ll start by covering the basics of Quarto, then delve into the differences between Quarto and R Markdown in the sections on [Chunk Options](#chunk-options-r) and [Output Formats](#output-formats-r) below.

### Code Blocks

Code blocks that use braces around the language name (e.g. `````{r}`````) are executable, and will be run by Quarto during render. Here is a simple example:

````markdown
---
title: "ggplot2 demo"
author: "Norah Jones"
date: "5/22/2021"
format:
  html:
    code-fold: true
---

