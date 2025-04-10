## Get Started: Hello, Quarto - Text Editor

Source: [Tutorial: Hello, Quarto – Quarto](https://quarto.org/docs/get-started/hello/text-editor.html) (Content largely duplicated from Tools: Text Editors section, tailored for beginners)

### Overview

In this tutorial we’ll show you how to use your favorite text editor with Quarto. You’ll edit plain text `.qmd` files and preview the rendered document in a web browser as you work.

Below is an overview of how this will look.

![Text Editor and Quarto Preview](https://quarto.org/docs/get-started/images/text-editor-preview.png)

The document on the left is *rendered* into the HTML version you see on the right. This is the basic model for Quarto publishing—take a source document (in this case a notebook) and render it to a variety of [output formats](https://quarto.org/docs/output-formats/all-formats.html), including HTML, PDF, MS Word, etc.

The tutorials will make use of the `matplotlib` and `plotly` Python packages—the commands you can use to install them are given in the table below.

| Platform   | Commands                                                     |
| :--------- | :----------------------------------------------------------- |
| Mac/Linux  | `python3 -m pip install jupyter matplotlib plotly`           |
| Windows    | `py -m pip install jupyter matplotlib plotly`                |

**Note:** Note that while this tutorial uses Python, using Julia (via the [`IJulia`](https://github.com/JuliaLang/IJulia.jl) kernel) is also well supported. See the article on [Using Julia](https://quarto.org/docs/computations/julia.html) for additional details.

### Editor Modes

If you are using VS Code, you should install the [Quarto Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) for VS Code before proceeding. The extension provides syntax highlighting for markdown and embedded languages, completion for embedded languages (e.g. Python, R, Julia, LaTeX, etc.), commands and key-bindings for running cells and selected line(s), and much more.

There are also Quarto syntax highlighting modes available for several other editors:

| Editor         | Extension                                                   |
| :------------- | :---------------------------------------------------------- |
| Emacs          | <https://github.com/quarto-dev/quarto-emacs>                |
| Vim / Neovim   | <https://github.com/quarto-dev/quarto-vim>                  |
| Neovim         | <https://github.com/quarto-dev/quarto-nvim>                 |
| Sublime Text   | <https://github.com/quarto-dev/quarto-sublime>              |

### Rendering

We’ll start out by rendering a simple example (`hello.qmd`) to a couple of formats. If you want to follow along step-by-step in your own environment, create a new file named `hello.qmd` and copy the following content into it.

```yaml
---
title: "Quarto Basics"
format:
  html:
    code-fold: true
jupyter: python3
---

