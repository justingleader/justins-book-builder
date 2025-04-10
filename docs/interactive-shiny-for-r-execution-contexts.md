## Interactive: Shiny for R Execution Contexts

Source: [Execution Contexts – Quarto](https://quarto.org/docs/interactive/shiny-r/execution.html)

### Overview

Shiny interactive documents can contain both code that executes at render time as well as code that executes on the server in response to user actions and changes in input values. A solid understanding of these execution contexts is important both to have the right mental model during development as well as to optimize the performance of your document.

### Render & Server Contexts

To break this down more clearly, let’s revisit the “Hello, Shiny” document we started with in the introduction to interactive documents:

````markdown
---
title: "Old Faithful"
format: html
server: shiny
---

```{r}
sliderInput("bins", "Number of bins:", min = 1, max = 50, value = 30)
plotOutput("distPlot")
```

```{r}
#| context: server
output$distPlot <- renderPlot({
  x    <- faithful[, 2]  # Old Faithful Geyser data
  bins <- seq(min(x), max(x), length.out = input$bins + 1)
  hist(x, breaks = bins, col = 'darkgray', border = 'white')
})
```
````

Here is how execution breaks down for this document:

*   The first code chunk that contains the calls to `sliderInput()` and `plotOutput()` will execute when you render the document (e.g. `quarto render old-faithful.qmd`).
*   The second code chunk with the `context: server` option will *not* execute at render time, but rather will execute only when the document is served.

It’s critical to understand that the two chunks are run in completely separate R sessions. That means that you cannot access variables created in the first chunk within the second, and vice-versa. The is analogous to the `ui.R` and `server.R` scripts that compose most normal Shiny applications.

Of course, it’s quite useful to be able to re-use code between contexts, and we’ll cover some ways to do this in the [Sharing Code](#sharing-code) section below.

In order to make the code of interactive documents straightforward to understand and work with, we strongly recommend that your server contexts (there can be more than one) be located *at the bottom* of the document. This makes the separate execution environments more clear in the flow of the document source code.

### server.R

There is one other option if you prefer to have a stronger separation. You can restrict your `.qmd` file to *only* code that will execute at render time, and then split out the server code into a separate `server.R` file.

Re-writing our example in this fashion would look like this:

**old-faithful.qmd**
```yaml
---
title: "Old Faithful"
format: html
server: shiny
---
```

````markdown
```{r}
sliderInput("bins", "Number of bins:", min = 1, max = 50, value = 30)
plotOutput("distPlot")
```
````

**server.R**
```r
function(input, output, session) {
  output$distPlot <- renderPlot({
    x    <- faithful[, 2]  # Old Faithful Geyser data
    bins <- seq(min(x), max(x), length.out = input$bins + 1)
    hist(x, breaks = bins, col = 'darkgray', border = 'white')
  })
}
```

This is perhaps a bit less convenient but does align better with the traditional `ui.R` / `server.R` separation that exists in traditional Shiny applications.

### Sharing Code

Sharing code between rendering contexts works a bit differently depending on if your code is in a single `.qmd` file or if it uses `server.R`. We’ll cover both scenarios below.

#### Single File

##### context: setup

To have code execute in both rendering and serving contexts, create a code chunk with `context: setup`. For example:

````markdown
```{r}
#| context: setup
#| include: false

# load libraries
library(dplyr)

# load data
dataset <- import_data("data.csv")
dataset <- sample_n(dataset, 1000)
```
````

This code will execute at both render time as well as when the server is created for each new user session. Note that we also specify `include: false` to make sure that code, warnings, and output from the chunk are not included in the rendered document.

##### context: data

The loading and manipulation of data often dominates the startup time of Shiny applications. Since interactive documents are executed in two phases (the initial render and then the serving of the document to users) we can perform the expensive data manipulations during rendering and then simply load the data when starting up the application.

You can define prerendered data by adding the `context: data` option to an R code chunk. The chunk will be executed during render and any R objects it creates will be saved to an .RData file, which will then be loaded during Shiny server startup. For example, we could take the setup chunk illustrated above and factor out the data loading into its own chunk:

````markdown
```{r}
#| context: data
#| include: false

dataset <- import_data("data.csv")
dataset <- sample_n(dataset, 1000)
```
````

Note that R objects created within a `context: data` chunk are available to both the UI rendering and server contexts.

##### Knitr cache

You can further improve the performance of data rendering by adding the `cache: true` option to the data chunk. This will cause the code chunk to be re-executed only when required. For example:

````markdown
```{r}
#| context: data
#| include: false
#| cache: true
#| cache.extra: !expr file.info("data.csv")$mtime

dataset <- import_data("data.csv")
dataset <- sample_n(dataset, 1000)
```
````

In this example the cache will be invalidated if either the R code in the chunk changes or the modification time of the “data.csv” file changes (this is accomplished using the `cache.extra` option).

You can also invalidate an existing cache by removing the `_cache` directory alongside with your interactive document.

##### context: server-start

There is one additional execution context that enables you to share code and data across multiple user sessions. Chunks with `context: server-start` execute once when the Shiny document is first run and are *not* re-executed for each new user of the document. Using `context: server-start` is appropriate for several scenarios including:

*   Establishing shared connections to remote servers (e.g. databases, Spark contexts, etc.).
*   Creating reactive values intended to be shared across sessions (e.g. with `reactivePoll` or `reactiveFileReader`).

For example:

````markdown
```{r}
#| context: server-start
library(DBI)
db <- dbConnect(...)
```
````

#### Multiple Files

If your interactive document uses a `.qmd` file to define the user-interface and a `server.R` file for the server, you can put shared code in a file named `global.R`. Functions and variables defined within `global.R` will be available both during render as well as during execution of the server.

In this scenario your interactive document consists of 3 source files:

| File       | Description                                                                                       |
| :--------- | :------------------------------------------------------------------------------------------------ |
| `doc.qmd`  | Markdown content as well as Shiny inputs and outputs (e.g. `sliderInput()`, `plotOutput()`, etc.) |
| `server.R` | Main server function with reactive expressions, assignments to outputs, etc.                      |
| `global.R` | Code shared between `doc.qmd` and `server.R`.                                                     |

