## Interactive: Shiny for R Running Documents

Source: [Running Documents – Quarto](https://quarto.org/docs/interactive/shiny-r/running.html)

### Overview

There are a number of ways to run Shiny interactive documents:

*   Use `Run Document` within the RStudio IDE.
*   Use the `quarto serve` command line interface.
*   Deploy them to a server for use by a wider audience.

We’ll cover all of these scenario in depth here. Note that in order to run interactive Shiny documents you will to install the very latest version of the `rmarkdown` package (v2.10) which you can install as follows:

```r
install.packages("rmarkdown")
```

### RStudio IDE

While you are developing an interactive document it will likely be most convenient to run within RStudio.

Note that you need RStudio v2022.07 or a later version in order to run Quarto interactive documents. You can download the latest release at <https://posit.co/download/rstudio-desktop/>.

Click the `Run Document` button while editing a Shiny interactive document to render and view the document within the IDE:

![RStudio Run Document Button](https://quarto.org/docs/interactive/shiny-r/images/rstudio-run-document.png)

When you make changes, just click `Run Document` again to see them reflected in the document preview.

Two options you may want to consider enabling are `Run on Save` and `Preview in Viewer Pane` (by default previews occur in an external window). You can access these options on the editor toolbar:

![RStudio Preview Options](https://quarto.org/docs/interactive/shiny-r/images/rstudio-preview-options.png)

### Command Line

You can also run Shiny interactive documents from the command line via `quarto serve`. For example:

```bash
quarto serve document.qmd
```

There are a number of options to the `serve` command to control the port and host of the document server as well as whether a browser is automatically opened for the running document. You can learn more about these options with `quarto serve help`.

If you are within an R session you can also use the `quarto` R package to run a document:

```r
library(quarto)
quarto_serve("document.qmd")
```

### Deployment

#### ShinyApps

You can publish Shiny interactive documents to the [ShinyApps](https://www.shinyapps.io/) hosted service. To do this you should ensure that you have:

1.  An account on ShinyApps (use the [signup form](https://www.shinyapps.io/admin/#/signup) to create an account).
2.  The very latest versions of the `rsconnect` and `quarto` R packages. You can install them as follows:
    ```r
    install.packages("rsconnect")
    install.packages("quarto")
    ```

You can then deploy your interactive document using the `quarto_publish_app()` function of the `quarto` package. You can do this as follows (working from the directory that contains your document):

```r
library(quarto)
quarto_publish_app(server = "shinyapps.io")
```

If you are using RStudio you can also use the `Publish` button <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAB+SURBVDhPY1i1atV/AMRADNwGKsZmYGBCUiqCZncYzGBoAm4gAVKtjHGLAa0gmAEYAAb9Y8xCbGSA5kgxH2MsALP3ASwzUHJlA9YBVhMAzJyyGQMwAgJGZrPPDgAV6ZmAZhBGDFsOcgaSAgAVkCfgXg8qBkbGDEzAgAACEGAAgFeyLqClXZEwAAAAAElFTkSuQmCC" alt="Publish" width="16"> available when working with an interactive document:

![RStudio Publish Button](https://quarto.org/docs/interactive/shiny-r/images/rstudio-publish.png)

Note that you should always `Run Document` locally prior to publishing your document (as this will create the `.html` file that is served on ShinyApps.

#### Hugging Face

HuggingFace Spaces provides an SDK for deploying Shiny for R applications. Learn more about using HuggingFace with Shiny for R here: <https://huggingface.co/docs/hub/spaces-sdks-docker-shiny#shiny-for-r>.

#### Posit Connect

[Posit Connect](https://posit.co/products/enterprise/connect/) is a server product from Posit for secure sharing of applications, reports, and plots. You can publish Shiny interactive documents to Posit Connect in much the same way as described above for [ShinyApps](#shinyapps).

First, make sure you very latest development versions of the `rsconnect` and `quarto` R packages. You can install them as follows:

```r
install.packages("rsconnect")
install.packages("quarto")
```

Next, deploy your interactive document using the `quarto_publish_app()` function of the `quarto` package, providing the domain name or IP address of your Posit Connect installation via the `server` parameter. You can do this as follows (working from the directory that contains your document):

```r
library(quarto)
quarto_publish_app(server = "rsc.example.com")
```

If you are using RStudio you can also use the `Publish` button <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAB+SURBVDhPY1i1atV/AMRADNwGKsZmYGBCUiqCZncYzGBoAm4gAVKtjHGLAa0gmAEYAAb9Y8xCbGSA5kgxH2MsALP3ASwzUHJlA9YBVhMAzJyyGQMwAgJGZrPPDgAV6ZmAZhBGDFsOcgaSAgAVkCfgXg8qBkbGDEzAgAACEGAAgFeyLqClXZEwAAAAAElFTkSuQmCC" alt="Publish" width="16"> as described above in the ShinyApps documentation:

![RStudio Publish Button](https://quarto.org/docs/interactive/shiny-r/images/rstudio-publish.png)

As with ShinyApps, you should always `Run Document` locally prior to publishing your document (as this will create the `.html` file that is served by Posit Connect).

