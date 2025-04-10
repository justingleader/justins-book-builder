## Get Started: Hello, Quarto - Neovim

Source: [Tutorial: Hello, Quarto – Quarto](https://quarto.org/docs/get-started/hello/neovim.html) (Content largely duplicated from Tools: Neovim section, tailored for beginners)

### Overview

In this tutorial we’ll show you how to use Quarto with Neovim. While we cover the basics here, you will also want to review the article on [Using Neovim with Quarto](https://quarto.org/docs/tools/neovim.html) to learn more about installing, using, and customizing Neovim for Quarto.

If you already have Neovim configured to your liking, you may only want to add the [`quarto-nvim`](https://github.com/quarto-dev/quarto-nvim) plugin and only refer to this guide for inspiration and seeing the possibilities. But if you are entirely new to Neovim or want to simply try out a configuration already set up for data science with Quarto, you should head over to this [kickstarter configuration](https://github.com/jmbuhr/quarto-nvim-kickstarter). This is also what we will be using for this tutorial.

**Note:** Neovim is a highly customizable editor. So much so that Neovim core member TJ Devries has recently coined the term Personal Development Environments (PDE)[^8] to separate the concept from Integrated Development Environments (IDEs) such as VS Code and RStudio. Out of the box neovim is fairly minimal. To work efficiently and get all the nice features, you have to configure it. You have to make it your own. If this approach sounds enticing to you, read on. Welcome to the rabbit hole. 🐰

You can also watch [this video](https://www.youtube.com/watch?v=p2XdHq8L7qM) for a quick guide to getting started with the kickstarter configuration alongside this write-up.

The Quarto Neovim plugin aims to not reinvent the wheel. Existing plugins in the Neovim ecosystem are leveraged to provide the full experience. Some of the features provided by `quarto-nvim` and enhanced by plugins found in the kickstarter configuration are:

*   Preview for Quarto documents.
*   Syntax highlighting for markdown and embedded languages
*   Completion for embedded languages (e.g. Python, R, Julia, etc.)
*   Commands and key-bindings for running cells and selected lines.
*   Completion for bibliography references, file paths, LaTeX math symbols, emoji.
*   Optional spellchecking and completion.
*   Code snippets.
*   Export of code chunks into standalone scripts.

See the article on [Using Neovim with Quarto](https://quarto.org/docs/tools/neovim.html) for all of the details.

### Basic Workflow

Quarto `.qmd` files contain a combination of markdown and executable code cells. Here’s what it might look like in Neovim to edit and preview a `.qmd` file:

![Neovim and Quarto Preview](https://quarto.org/docs/get-started/images/neovim-preview.gif)

The `.qmd` file you see on the left is *rendered* into the HTML document you see on the right side. This is the basic model for Quarto publishing—take a source document and render it to a variety of [output formats](https://quarto.org/docs/output-formats/all-formats.html), including HTML, PDF, MS Word, etc.

The tutorials will make use of the `matplotlib` and `plotly` Python packages—the commands you can use to install them are given in the table below.

| Platform   | Commands                                                     |
| :--------- | :----------------------------------------------------------- |
| Mac/Linux  | `python3 -m pip install jupyter matplotlib plotly`           |
| Windows    | `py -m pip install jupyter matplotlib plotly`                |

**Note:** Note that while this tutorial uses Python, using Julia (via the [`IJulia`](https://github.com/JuliaLang/IJulia.jl) kernel) or using R (via the [`knitr`](https://yihui.org/knitr/) package), are also well supported. See the articles on [Using Julia](https://quarto.org/docs/computations/julia.html) and [Using R](https://quarto.org/docs/computations/r.html) for additional details.

### Render and Preview

We’ll start out by rendering a simple example (`hello.qmd`) to a couple of formats. If you want to follow along step-by-step in your own environment, create a new file named `hello.qmd` and copy the following content into it.

```yaml
---
title: "Quarto Basics"
format:
  html:
    code-fold: true
jupyter: python3
---

