## Computations: Julia

Source: [Using Julia – Quarto](https://quarto.org/docs/computations/julia.html)

### Overview

Quarto supports executable Julia code blocks within markdown. This allows you to create fully reproducible documents and reports—the Julia code required to produce your output is part of the document itself, and is automatically re-run whenever the document is rendered.

Quarto has two available engines for executing Julia code. The older one is using the [`IJulia`](https://github.com/JuliaLang/IJulia.jl) Jupyter kernel and depends on Python to run. The newer engine is using the [`QuartoNotebookRunner.jl`](https://github.com/quarto-dev/QuartoNotebookRunner.jl) package to render notebooks and does not have any additional dependencies beyond a Julia installation.

### Using the `jupyter` engine

Below we’ll describe how to [install](#installation-jupyter) IJulia and related requirements but first we’ll cover the basics of creating and rendering documents with Julia code blocks.

#### Code Blocks

Code blocks that use braces around the language name (e.g. `````{julia}`````) are executable, and will be run by Quarto during render. Here is a simple example:

````markdown
---
title: "Plots Demo"
author: "Norah Jones"
date: "5/22/2021"
format:
  html:
    code-fold: true
jupyter: julia-1.8
---

### Parametric Plots

Plot function pair (x(u), y(u)).
See @fig-parametric for an example.

```{julia}
#| label: fig-parametric
#| fig-cap: "Parametric Plots"

using Plots
plot(sin, x->sin(2x), 0, 2π,
     leg=false,
     fill=(0,:lavender))
```
````

You’ll note that there are some special comments at the top of the code block. These are cell level options that make the figure [cross-referenceable](https://quarto.org/docs/authoring/cross-references.html).

This document would result in the following rendered output:

![Rendered Julia Plot](https://quarto.org/docs/computations/images/julia-plots-output.png)

You can produce a wide variety of output types from executable code blocks, including plots, tabular output from data frames, and plain text output (e.g. printing the results of statistical summaries).

There are many options which control the behavior of code execution and output, you can read more about them in the article on [Execution Options](https://quarto.org/docs/computations/execution-options.html).

In addition to code blocks which interrupt the flow of markdown, you can also include code inline. Read more about inline code in the [Inline Code](https://quarto.org/docs/computations/inline-code.html) article.

#### Multiple Outputs

By default Julia cells will automatically print the value of their last statement (as with the example above where the call to `plot()` resulted in plot output). If you want to display multiple plots (or other types of output) from a single cell you should call the `display()` function explicitly. For example, here we output two plots side-by-side with sub-captions:

````markdown
```{julia}
#| label: fig-plots
#| fig-cap: "Multiple Plots"
#| fig-subcap:
#|   - "Plot 1"
#|   - "Plot 2"
#| layout-ncol: 2

using Plots
display(plot(sin, x -> sin(2x), 0, 2))
display(plot(x -> sin(4x), y -> sin(5y), 0, 2))
```
````

#### Rendering

Quarto will automatically run computations in any markdown document that contains executable code blocks. For example, the example shown above might be rendered to various formats with:

```bash
quarto render document.qmd # all formats
quarto render document.qmd --to pdf
quarto render document.qmd --to docx
```

The `render` command will render all formats listed in the document YAML. If no formats are specified, then it will render to HTML. You can also provide the `--to` argument to target a specific format.

Quarto can also render any Jupyter notebook (.ipynb):

```bash
quarto render document.ipynb
```

Note that the target file (in this case `document.qmd`) should always be the very first command line argument.

Note that when rendering an .ipynb Quarto will not execute the cells within the notebook by default (the presumption being that you already executed them while editing the notebook). If you want to execute the cells you can pass the `--execute` flag to render:

```bash
quarto render notebook.ipynb --execute
```

#### Installation {#installation-jupyter}

In order to render documents with embedded Julia code you’ll need to install the following components:

*   IJulia
*   Revise.jl
*   Optionally, Jupyter Cache

We’ll cover each of these in turn below.

##### IJulia

[IJulia](https://github.com/JuliaLang/IJulia.jl) is a Julia-language execution kernel for Jupyter. You can install IJulia from within the Julia REPL as follows:

```julia
using Pkg
Pkg.add("IJulia")
using IJulia
notebook()
```

The first time you run `notebook()`, it will prompt you for whether it should install Jupyter. Hit enter to have it use the `Conda.jl` package to install a minimal Python+Jupyter distribution (via [Miniconda](https://docs.conda.io/en/latest/miniconda.html)) that is private to Julia (not in your `PATH`). On Linux, it defaults to looking for `jupyter` in your `PATH` first, and only asks to installs the Conda Jupyter if that fails.

If you choose not to use Conda.jl to install Python and Jupyter you will need to make sure that you have another installation of it on your system (see the section on [Installing Jupyter](#installing-jupyter) if you need help with this).

##### Revise.jl

In addition to IJulia, you’ll want to install [Revise.jl](https://timholy.github.io/Revise.jl/stable/) and configure it for use with IJulia. Revise.jl is a library that helps you keep your Julia sessions running longer, reducing the need to restart when you make changes to code.

Quarto maintains a persistent [kernel daemon](#kernel-daemon) for each document to mitigate Jupyter start up time during iterative work. Revise.jl will make this persistent process robust in the face of package updates, git branch checkouts, etc. Install Revise.jl with:

```julia
using Pkg
Pkg.add("Revise")
```

To configure Revise to launch automatically within IJulia, create a `.julia/config/startup_ijulia.jl` file with the contents:

```julia
try
  @eval using Revise
catch e
  @warn "Revise init" exception=(e, catch_backtrace())
end
```

You can learn more about Revise.jl at <https://timholy.github.io/Revise.jl/stable>.

##### Jupyter Cache

[Jupyter Cache](https://jupyter-cache.readthedocs.io/en/latest/) enables you to cache all of the cell outputs for a notebook. If any of the cells in the notebook change then all of the cells will be re-executed.

If you are using the integrated version of Jupyter installed by `IJulia.notebook()`, then you will need to add `jupyter-cache` to the Python environment managed by IJulia. You can do that as follows:

```julia
using Conda
Conda.add("jupyter-cache")
```

Alternatively, if you are using Jupyter from within any other version of Python not managed by IJulia, see the instructions below on [Installing Jupyter](#installing-jupyter) for details on installing `jupyter cache`.

#### Workflow

You can author Quarto documents that include Julia code using any text or notebook editor. No matter what editing tool you use, you’ll always run `quarto preview` first to setup a live preview of changes in your document. Live preview is available for both HTML and PDF output. For example:

```bash
# preview as html
quarto preview document.qmd

# preview as pdf
quarto preview document.qmd --to pdf

# preview a jupyter notebook
quarto preview document.ipynb
```

Note that when rendering an `.ipynb` Quarto **will not** execute the cells within the notebook by default (the presumption being that you have already executed them while editing the notebook). If you want to execute the cells you can pass the `--execute` flag to render:

```bash
quarto render notebook.ipynb --execute
```

You can also specify this behavior within the notebook’s YAML front matter:

```yaml
---
title: "My Notebook"
execute:
  enabled: true
---
```

#### Embed Notebooks

In addition to including executable Julia code chunks in a Quarto document, you can also embed cells from an external Jupyter Notebook (`.ipynb`). See [Embedding Jupyter Notebook Cells](https://quarto.org/docs/authoring/notebook-embed.html) for more details.

#### VS Code

The [Quarto Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) for VS Code provides a variety of tools for working with `.qmd` files in VS Code. The extension integrates directly with the [Julia Extension](https://marketplace.visualstudio.com/items?itemName=julialang.language-julia) to provide the following Julia-specific capabilities:

*   Code completion
*   Cell execution
*   Contextual help

You can install the VS Code extension by searching for ‘quarto’ in the extensions panel or from the [extension marketplace](https://marketplace.visualstudio.com/items?itemName=quarto.quarto).

You can also use the VS Code notebook editor to create Julia notebooks that you will render with Quarto. The next section discusses using notebooks with Quarto in the context of Jupyter Lab, but the same concepts apply to VS Code.

#### Jupyter Lab

We could convert the simple `document.qmd` we used as an example above to a Jupyter notebook using the `quarto convert` command. For example:

```bash
quarto convert document.qmd
```

If we open this notebook in Jupyter Lab and execute the cells, here is what we see:

![Jupyter Lab with Julia Notebook](https://quarto.org/docs/computations/images/julia-jupyterlab.png)

Note that there are three different types of cell here:

1.  The YAML document options at the top are in a `Raw` cell.
2.  The heading and explanation are in a `Markdown` cell.
3.  The Julia code and its output are in a `Code` cell.

When working in a Jupyter notebook, you can use `quarto preview` to provide a live preview of your rendered document:

```bash
quarto preview document.ipynb
```

The preview will be updated every time you save the notebook in Jupyter Lab.

#### Caching

[Jupyter Cache](https://jupyter-cache.readthedocs.io/en/latest/) enables you to cache all of the cell outputs for a notebook. If any of the cells in the notebook change then all of the cells will be re-executed.

To use Jupyter Cache you’ll want to first install the `jupyter-cache` package:

| Platform   | Command                                     |
| :--------- | :------------------------------------------ |
| Mac/Linux  | `python3 -m pip install jupyter-cache`      |
| Windows    | `py -m pip install jupyter-cache`           |
| Conda      | `conda install jupyter-cache`               |

To enable the cache for a document, add the `cache` option. For example:

```yaml
---
title: "My Document"
format: html
execute:
  cache: true
---
```

You can also specify caching at the project level. For example, within a project file:

```yaml
project:
  type: website
format:
  html:
    theme: united
execute:
  cache: true
```

Note that changes within a document that aren’t within code cells (e.g. markdown narrative) do not invalidate the document cache. This makes caching a very convenient option when you are working exclusively on the prose part of a document.

Jupyter Cache include a `jcache` command line utility that you can use to analyze and manage the notebook cache. See the [Jupyter Cache](https://jupyter-cache.readthedocs.io/en/latest/) documentation for additional details.

##### Rendering

You can use `quarto render` command line options to control caching behavior without changing the document’s code. Use options to force the use of caching on all chunks, disable the use of caching on all chunks (even if it’s specified in options), or to force a refresh of the cache even if it has not been invalidated:

```bash
# use a cache (even if not enabled in options)
quarto render example.qmd --cache

# don't use a cache (even if enabled in options)
quarto render example.qmd --no-cache

# use a cache and force a refresh
quarto render example.qmd --cache-refresh
```

##### Alternatives

If you are using caching to mitigate long render-times, there are some alternatives you should consider alongside caching.

**Disabling Execution:** If you are working exclusively with prose / markdown, you may want to disable execution entirely. Do this by specifying the `enabled: false` execute option For example:

```yaml
---
title: "My Document"
format: html
execute:
  enabled: false
---
```

Note that if you are authoring using Jupyter `.ipynb` notebooks (as opposed to plain-text `.qmd` files) then this is already the default behavior: no execution occurs when you call `quarto render` (rather, execution occurs as you work within the notebook).

**Freezing Execution:** If you are working within a project and your main concern is the cumulative impact of rendering many documents at once, consider using the `freeze` option.

You can use the `freeze` option to denote that computational documents should never be re-rendered during a global project render, or alternatively only be re-rendered when their source file changes:

```yaml
execute:
  freeze: true   # never re-render during project render
```

```yaml
execute:
  freeze: auto   # re-render only when source changes
```

Note that `freeze` controls whether execution occurs during global project renders. If you do an incremental render of either a single document or a project sub-directory then code is always executed. For example:

```bash
# render single document (always executes code)
quarto render document.qmd

# render project subdirectory (always executes code)
quarto render articles
```

Learn more about using `freeze` with projects in the article on [managing project execution](https://quarto.org/docs/projects/code-execution.html#freeze).

#### Kernel Selection

You’ll note in our first example that we specified the use of the `julia-1.7` kernel explicitly in our document options (shortened for brevity):

```yaml
---
title: "StatsPlots Demo"
jupyter: julia-1.7
---
```

If no `jupyter` kernel is explicitly specified, then Quarto will attempt to automatically discover a kernel on the system that supports Julia.

You can discover the available Jupyter kernels on your system using the `quarto check` command:

```bash
quarto check jupyter
```

#### Kernel Daemon {#kernel-daemon}

To mitigate the start-up time for the Jupyter kernel Quarto keeps a daemon with a running Jupyter kernel alive for each document. This enables subsequent renders to proceed immediately without having to wait for kernel start-up.

The purpose of the daemon is to make render more responsive during interactive sessions. Accordingly, no daemon is created when documents are rendered without an active tty or when they are part of a batch rendering (e.g. in a [Quarto Project](https://quarto.org/docs/projects/quarto-projects.html)).

Note that Quarto does not use a daemon by default on Windows (as some Windows systems will not allow the socket connection required by the daemon).

You can customize this behavior using the `daemon` execution option. Set it to `false` to prevent the use of a daemon, or set it to a value (in seconds) to determine the period after which the daemon will timeout (the default is 300 seconds). For example:

```yaml
execute:
  daemon: false
```

```yaml
execute:
  daemon: 60
```

Note that if you want to use a daemon on Windows you need to enable it explicitly:

```yaml
execute:
  daemon: true
```

##### Command Line

You can also control use of the Jupyter daemon using the following command line options:

```bash
# use a daemon w/ default timeout (300 sec)
quarto render document.qmd --execute-daemon

# use a daemon w/ an explicit timeout
quarto render document.qmd --execute-daemon 60

# prevent use of a daemon
quarto render document.qmd --no-execute-daemon
```

You can also force an existing daemon to restart using the `--execute-daemon-restart` command line flag:

```bash
quarto render document.qmd --execute-daemon-restart
```

This might be useful if you suspect that the re-use of notebook sessions is causing an error.

Finally, you can print extended debugging information about daemon usage (startup, shutdown, connections, etc.) using the `--execute-debug` flag:

```bash
quarto render document.qmd --execute-debug
```

#### Installing Jupyter

You can rely on the minimal version of Python and Jupyter that is installed automatically by `IJulia`, or you can choose to install Python and Jupyter separately. If you need to install another version of Jupyter this section describes how.

If you don’t yet have Python 3 on your system, we recommend you install a version using the standard installer from <https://www.python.org/downloads/>.

If you are in a fresh Python 3 environment, installing the `jupyter` package will provide everything required to execute Jupyter kernels with Quarto:

| Pkg. Manager | Command                                 |
| :----------- | :-------------------------------------- |
| Pip (Mac/Linux) | `python3 -m pip install jupyter`      |
| Pip (Windows)   | `py -m pip install jupyter`           |
| Conda         | `conda install jupyter`                 |

You can verify that Quarto is configured correctly for Jupyter with:

```bash
quarto check jupyter
```

Quarto will select a version of Python using the [Python Launcher](https://docs.python.org/3/using/windows.html#python-launcher-for-windows) on Windows or system `PATH` on MacOS and Linux. You can override the version of Python used by Quarto by setting the `QUARTO_PYTHON` environment variable.

If you are using a virtual environment with your environment or project, see more at [Virtual Environments](https://quarto.org/docs/projects/virtual-environments.html).

##### Jupyter Cache

[Jupyter Cache](https://jupyter-cache.readthedocs.io/en/latest/) enables you to cache all of the cell outputs for a notebook. If any of the cells in the notebook change then all of the cells will be re-executed.

To use Jupyter Cache you’ll want to first install the `jupyter-cache` package:

| Platform   | Command                                     |
| :--------- | :------------------------------------------ |
| Mac/Linux  | `python3 -m pip install jupyter-cache`      |
| Windows    | `py -m pip install jupyter-cache`           |
| Conda      | `conda install jupyter-cache`               |

To enable the cache for a document, add the `cache` option. For example:

```yaml
---
title: "My Document"
format: html
execute:
  cache: true
---
```

### Using the `julia` engine

#### Installation

The `julia` engine uses the [`QuartoNotebookRunner.jl`](https://github.com/quarto-dev/QuartoNotebookRunner.jl) package to render notebooks. When you first attempt to render a notebook with the `julia` engine, Quarto will automatically install this package into a private environment that is owned by Quarto. This means you don’t have to install anything in your global Julia environment for Quarto to work and Quarto will not interfere with any other Julia environments on your system. Quarto will use the `julia` binary on your PATH by default, but you can override this using the `QUARTO_JULIA` environment variable.

##### Using custom versions of `QuartoNotebookRunner`

In special circumstances, you may not want to use the specific `QuartoNotebookRunner` version that Quarto installs for you. For example, you might be developing `QuartoNotebookRunner` itself, or you need to use a fork or an unreleased version with a bugfix. In this case, set the [environment variable](https://quarto.org/docs/projects/environment-variables.html) `QUARTO_JULIA_PROJECT` to a directory of a julia environment that has `QuartoNotebookRunner` installed.

As an example, you could install the main branch of `QuartoNotebookRunner` into the directory `/some/dir` by executing `]activate /some/dir` in a julia REPL followed by `]add QuartoNotebookRunner#main`. As long as there is no server currently running, running a command like `QUARTO_JULIA_PROJECT=/some/dir quarto render some_notebook.qmd` in your terminal will ensure the server process is started using the custom `QuartoNotebookRunner`. You can also set `quarto`’s `--execute-debug` flag and check the output to verify that the custom environment is being used.

#### Rendering notebooks

To use the `julia` engine, you have to specify it in your frontmatter:

````markdown
---
title: "A julia engine notebook"
engine: julia
---

```{julia}
1 + 2
```
````

Rendering a notebook will start a persistent server process if it hasn’t already started. This server process first loads QuartoNotebookRunner from Quarto’s private environment. QuartoNotebookRunner then spins up a separate Julia worker process for each notebook you want to render.

#### Notebook environments

By default, QuartoNotebookRunner will use the `--project=@.` flag when starting a worker. This makes Julia search for an environment (a `Project.toml` or `JuliaProject.toml` file) starting in the directory where the quarto notebook is stored and walking up the directory tree from there.

For example, for a file `/some/dir/notebook.qmd` it will look at `/some/dir/[Julia]Project.toml`, `/some/[Julia]Project.toml` and so on. You could use this behavior to let all notebooks in a quarto project share the same Julia environment, by placing it at the project’s top-level directory.

If no environment has previously been set up in any of these directories, the worker process will start with an empty environment. This means that only Julia’s standard library packages will be available for use in the notebook.

**Note:** Creating a separate environment for each notebook or each set of closely related notebooks is considered best practice. If too many different notebooks share the same environment (for example the main shared environment that Julia usually loads by default), you’re likely to break some of them unintentionally whenever you make a change to the environment.

You can create a Julia environment in multiple ways, for more information have a look at the [official documentation](https://docs.julialang.org/en/v1/stdlib/Pkg/#Working-with-Environments). One simple option for adding packages to the default environment of a new quarto notebook is to add some `Pkg` installation commands to the notebook and run it once. Afterwards, those commands can be deleted and a `Project.toml` and `Manifest.toml` file representing the environment should be present in the notebook’s directory.

````markdown
---
engine: julia
---

```{julia}
using Pkg
Pkg.add("DataFrames")
```
````

Another option is to start `julia` in a terminal which loads the REPL, and to press `]` to switch to the `Pkg` REPL mode. In this mode, you can first activate the desired environment by running `activate /some/dir` and then, for example, install the `DataFrames` package with the command `add DataFrames`.

If you do not want to use the notebook’s directory as the environment, you may specify a different directory via the `--project` flag in the `exeflags` frontmatter setting:

```yaml
---
engine: julia
julia:
  exeflags: ["--project=/some/other/dir"]
---
```

#### Worker process reuse

An idle worker process will be kept alive for 5 minutes by default, this can be changed by passing the desired number of seconds to the `daemon` key:

```yaml
---
title: "A julia notebook with ten minutes timeout"
engine: julia
execute:
  daemon: 600
---
```

Each re-render of a notebook will reuse the worker process with all dependencies already loaded, which reduces latency. As far as technically possible, QuartoNotebookRunner.jl will release resources from previous runs to the garbage collector. In each run, the code is evaluated into a fresh module so you cannot run into conflicts with variables defined in previous runs. Note, however, that certain state changes like modifications to package runtime settings or the removal or addition of function methods will persist across runs. If necessary, you can use the `--execute-daemon-restart` flag to force a restart of a notebook’s worker process.

You can also disable the daemon which will use a new process for each render (with higher latency due to package reloads):

```yaml
execute:
  daemon: false
```

The server process itself will time out after five minutes if no more worker processes exist.

#### Engine options

Engine options can be passed under the `julia` top-level key:

```yaml
---
title: "A julia engine notebook"
engine: julia
julia:
  key: value
---
```

The currently available options are:

*   `exeflags`: An array of strings which are appended to the `julia` command that starts the worker process. For example, a notebook is run with `--project=@.` by default (the environment in the directory where the notebook is stored) but this could be overridden by setting `exeflags: ["--project=/some/directory/"]`.
*   `env`: An array of strings where each string specifies one environment variable that is passed to the worker process. For example, `env: ["SOMEVAR=SOMEVALUE"]`.

#### Limitations

Currently, the `engine: julia` option must be specified in each `.qmd` file. Setting the engine project-wide via `_quarto.yml` **is not yet supported**.

```

```markdown
