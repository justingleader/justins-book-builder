## Interactive: Shiny for R External Resources

Source: [External Resources – Quarto](https://quarto.org/docs/interactive/shiny-r/resources.html)

### Overview

There are two types of external resource file that might be referenced from within a Shiny interactive document:

1.  Files referenced from R code (e.g. R scripts, datasets, configuration files, etc.); and
2.  Static assets referenced from the web document (e.g. CSS style-sheets, images, etc.)

Below we’ll describe how each of these resource types are handled within interactive documents.

### Code Resources

For files referenced from R code, you can reference anything located within the directory of (or sub-directories of) the main `.qmd` file. This is no different than with any other `.qmd` file or even R script.

Similarly, files created by executing R code (e.g. figures generated from code chunks) are automatically located in the document `_files` directory alongside the HTML output file. No special handling is required for these files.

### Asset Resources

Many interactive documents will consist of only the generated HTML and figures located in the `_files` directory. However, in some cases you may want to add static images, CSS files, or other assets to your document.

In these cases, you need to be sure to locate the files within one of the following specially named sub-directories to ensure they can be located by the Shiny server:

| Directory | Description                                   |
| :-------- | :-------------------------------------------- |
| `images/` | Image files (e.g. PNG, JPEG, etc.)            |
| `css/`    | CSS stylesheets                               |
| `js/`     | JavaScript scripts                            |
| `www/`    | Any other files (e.g. downloadable datasets) |

The reason that all files within the directory of the main `.qmd` can’t be referenced from within the web document is that many of these files are application source code and data, which may not be something you want to be downloadable by end users. By restricting the files which can be referenced to the above directories you can control which files are downloadable and which are not.

