## Advanced Jupyter Kernel Execution

Source: [Jupyter Kernel Execution – Quarto](https://quarto.org/docs/computations/jupyter-kernels.html)

### Jupyter Kernel Execution

Quarto executes Jupyter notebooks using `nbclient` together with a few additional options to support some of Quarto’s features. Quarto has built-in support for these features in the `python` and `julia` Jupyter kernels.

In addition, starting in Quarto 1.5, any Jupyter kernel can configure itself to support the features described below.

### Setup and cleanup cells

In order for Quarto notebooks and documents to communicate global options with a Jupyter Kernel, Quarto uses special `setup` and `cleanup` cells.

In `python` and `julia` kernels, the setup and cleanup cells are defined by the following files:

Julia:
*   [setup](https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/jupyter/kernels/julia/setup.jl)
*   [cleanup](https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/jupyter/kernels/julia/cleanup.jl)

Python:
*   [setup](https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/jupyter/kernels/python/setup.py)
*   [cleanup](https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/jupyter/kernels/python/cleanup.py)

### Adding support to a Jupyter kernel

If a Jupyter kernel wants to execute in awareness of Quarto’s context, it should signal its support by adding the following files to the kernelspec directory:

*   `quarto_setup_cell`: the source code for a setup cell to be executed by nbclient at the beginning of execution of any Quarto notebook or document. Quarto will create a Jupyter notebook cell with the contents of this file as the `source` field.
*   `quarto_cleanup_cell`: analogously to above, the source code for a cleanup cell.

**Tip:** In order to make the implementation of these features easier for writers of custom kernels, we have made available a fork of Jupyter’s `echo_kernel`. This example kernel is meant to showcase the basics of a custom kernel implementation, and our fork adds the setup cell functionality. See the [source for more](https://github.com/quarto-dev/echo_kernel).

### Quarto document options

Jupyter kernels can have access to a number of Quarto options that can affect cell execution.

Currently, the supported options are:

*   `format`: the format that will be used to produce the document
*   `params`: the parameters that will be used in a [parameterized execution](https://quarto.org/docs/computations/parameters.html)
*   `allow_errors`: if `true`, then the kernel is asked to not stop execution if a cell produces an error
*   `fig_width`: the requested figure width in inches
*   `fig_height`: the requested figure height in inches
*   `fig_format`: the requested format for figure output (`png`, `jpg`, etc)
*   `fig_dpi`: the requested resolution for images in dots per inch
*   `cache`: if `true`, then Jupyter cache will be used

Quarto uses [Jupyter Comms](https://jupyter-notebook.readthedocs.io/en/stable/comms.html) to provide its options to a kernel during execution. Specifically, Quarto will open a comm with target name `quarto_kernel_setup`, and its initialization message content will contain these options under the `options` key.

**Tip:** In order to make the implementation of these features easier for writers of custom kernels, we have made available a fork of Jupyter’s `echo_kernel`. This example kernel is meant to showcase the basics of a custom kernel implementation, and our fork adds the setup cell functionality. See the [source for more](https://github.com/quarto-dev/echo_kernel).

### Daemonization

Quarto offers built-in support for `julia` and `python` kernels by default, see the docs for more ([Julia](https://quarto.org/docs/computations/julia.html#kernel-daemon), [Python](https://quarto.org/docs/computations/python.html#kernel-daemon)).

### Adding support to a Jupyter kernel

Arbitrary Jupyter kernels can indicate support for daemons. To do so, provide a `quarto_setup_cell` file in the kernelspec directory so that setup cells can be executed, and ensure that the execution of the setup cell returns an output result with metadata indicating support for running as a daemon. The supported metadata options are:

*   `daemonize`: if a kernel returns `true` when executing Quarto’s setup cell, then Quarto will maintain a persistent kernel. The daemon options are the same as in the [documentation above](https://quarto.org/docs/computations/julia.html#kernel-daemon).
*   `restart_kernel`: if a kernel returns `true`, then Quarto will forcibly restart the kernel. This allows kernels to detect that their configuration has been changed such that it cannot support continued execution in the same process.

**Tip:** In order to make the implementation of these features easier for writers of custom kernels, we have made available a fork of Jupyter’s `echo_kernel`. This example kernel is meant to showcase the basics of a custom kernel implementation, and our fork adds the setup cell functionality. See the [source for more](https://github.com/quarto-dev/echo_kernel).

