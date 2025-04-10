## Output Formats: PDF Engines

Source: [PDF Engines – Quarto](https://quarto.org/docs/output-formats/pdf-engine.html)

### Overview

Pandoc supports the use of a wide range of TeX distributions and PDF compilation engines including pdflatex, xelatex, lualatex, tectonic, and latexmk.

While you can employ whatever toolchain you like for LaTeX compilation, we strongly recommend the use of [TinyTeX](https://yihui.org/tinytex/), which is a distribution of [TeX Live](https://www.tug.org/texlive/) that provides a reasonably sized initial download (~100 MB) that includes the 200 or so most commonly used TeX packages for Pandoc documents.

We also recommend the use of Quarto’s built in PDF compilation engine, which among other things performs automatic installation of any missing TeX packages.

### Installing TeX

To install TinyTeX, use the following command:

```bash
quarto install tinytex
```

TinyTeX is not installed to the system `PATH` so will not affect other applications that use TeX. If you want to use TinyTeX with other applications, add the `--update-path` flag when installing (this will add TinyTex to the system path):

```bash
quarto install tinytex --update-path
```

If you already have another installation of TeX that you prefer to use with Quarto, add the `latex-tinytex: false` in your project or document front matter to prevent Quarto from using its internal version.

If you prefer TeX Live, you can find instructions for installing it here: <https://tug.org/texlive/>.

Note that Quarto’s automatic installation of missing TeX packages will work for TinyTeX and TeX Live, but not for other TeX distributions (as it relies on TeX Live’s `tlmgr` command).

### Managing TeX

In addition to installing TinyTeX, you may also update or remove the installation of TinyTex. To see the currently installed version of TinyTex, use the command:

```bash
quarto list tools
```

which will provide a list of available tools, the installed versions, and the latest available version:

```
[✓] Inspecting tools
Tool         Status            Installed     Latest
chromium     Not installed     ---           869685
tinytex      Up to date        v2022.10      v2022.10
```

To update to the latest version, use the command:

```bash
quarto update tinytex
```

which will download and install the latest version of TinyTex (following the same behavior as described for installing TinyTex above).

To remove TinyTex altogether, use the command:

```bash
quarto uninstall tinytex
```

**Tip:** Each year in April, TeXlive updates their remote package repository to the new year’s version of TeX. When this happens, previous year installations of TeX will not be able to download and install packages from the remote repository. When this happens, you may see an error like:

> Your TexLive version is not updated enough to connect to the remote repository and download packages. Please update your installation of TexLive or TinyTex.

When this happens, you can use `quarto update tinytex` to download and install an updated version of tinytex.

### Quarto PDF Engine

Quarto’s built-in PDF compilation engine handles running LaTeX multiple times to resolve index and bibliography entries, and also performs automatic LaTeX package installation. This section describes customizing the built-in engine (see the [Alternate PDF Engines](#alternate-pdf-engines) section below for docs on using other engines).

#### PDF Compilation

The following options are available for customizing PDF compilation:

| Option                | Description                                        |
| :-------------------- | :------------------------------------------------- |
| `latex-min-runs`      | Number (minimum number of compilation passes)      |
| `latex-max-runs`      | Number (maximum number of compilation passes)      |
| `latex-clean`         | Boolean (clean intermediates after compilation, defaults to `true`) |
| `latex-output-dir`    | String (output directory for intermediates and PDF)|
| `latex-makeindex`     | String (program to use for `makeindex`)            |
| `latex-makeindex-opts`| Array (options for `makeindex` program)            |

#### Package Installation

The following options are available for customizing automatic package installation:

| Option             | Description                                          |
| :----------------- | :--------------------------------------------------- |
| `latex-auto-install` | Boolean (enable/disable automatic package installation) |
| `latex-tlmgr-opts` | Array (options for `tlmgr`)                           |

### Alternate PDF Engines

You can use the `pdf-engine` and `pdf-engine-opts` to control the PDF engine that Quarto uses to compile the LaTeX output into a PDF. For example:

```yaml
title: "My Document"
pdf-engine: lualatex
pdf-engine-opts:
  - '--no-shell-escape'
  - '--halt-on-error'
```

The above example will use the `lualatex` PDF engine with some specific options, rather than the default `xelatex`.

#### Latexmk

Quarto includes a built-in Latexmk engine, which will run the `pdf-engine` more than once to generate your PDF (for example, if you are using cross references or a bibliography). In addition, this engine will detect and attempt to install missing packages, fonts, or commands if TeX Live is available.

You can disable Quarto’s built-in Latexmk engine by setting the `latex-auto-mk` option to `false`. For example:

```yaml
title: "My Document"
latex-auto-mk: false
```

Engine options can still be set using `pdf-engine-opts`. For example:

```yaml
latex-auto-mk: false
pdf-engine: latexmk
pdf-engine-opts:
  - '-auxdir=custom-aux'
  - '-emulate-aux-dir'
```

The above example will use `latexmk` as a PDF engine and set some options to modify the directory name for auxiliary files.

