## Get Started: Hello, Quarto - VS Code

Source: [Tutorial: Hello, Quarto – Quarto](https://quarto.org/docs/get-started/hello/vscode.html) (Content largely duplicated from Tools: VS Code section, tailored for beginners)

### Overview

In this tutorial we’ll show you how to use Quarto with VS Code. Before getting started, you should install the [Quarto VS Code Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto), which includes many tools that enhance working with Quarto, including:

*   Integrated render and preview for Quarto documents.
*   Syntax highlighting for markdown and embedded languages
*   Completion and diagnostics for YAML options
*   Completion for embedded languages (e.g. Python, R, Julia, etc.)
*   Commands and key-bindings for running cells and selected lines.

You can install the Quarto extension from within the `Extensions` tab in VS Code, from the [Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=quarto.quarto), the [Open VSX Registry](https://open-vsx.org/extension/quarto/quarto) or directly from a [VISX extension file](https://github.com/quarto-dev/quarto/releases).

**Note:** This tutorial focuses on editing plain text Quarto `.qmd` files in VS Code. Depending on your preferences and the task at hand there are two other editing modes available for Quarto documents: the [Visual Editor](https://quarto.org/docs/tools/vscode-visual-editor.html) and the [Notebook Editor](https://quarto.org/docs/tools/vscode-notebook-editor.html). For the purposes of learning we recommend you work through this tutorial using the VS Code text editor, then after you’ve mastered the basics explore using the other editing modes.

### Basic Workflow

Quarto `.qmd` files contain a combination of markdown and executable code cells. Here’s what it might look like in VS Code to edit and preview a `.qmd` file:

![VS Code and Quarto Preview](https://quarto.org/docs/get-started/images/vscode-hello.png)

The document on the left is *rendered* into the HTML version you see on the right. This is the basic model for Quarto publishing—take a source document and render it to a variety of [output formats](https://quarto.org/docs/output-formats/all-formats.html), including HTML, PDF, MS Word, etc.

The tutorials will make use of the `matplotlib` and `plotly` Python packages—the commands you can use to install them are given in the table below.

| Platform   | Commands                                                     |
| :--------- | :----------------------------------------------------------- |
| Mac/Linux  | `python3 -m pip install jupyter matplotlib plotly`           |
| Windows    | `py -m pip install jupyter matplotlib plotly`                |

**Note:** Note that while this tutorial uses Python, using Julia (via the [`IJulia`](https://github.com/JuliaLang/IJulia.jl) kernel) is also well supported. See the article on [Using Julia](https://quarto.org/docs/computations/julia.html) for additional details.

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

