## FAQ for R Markdown Users

Source: [FAQ for R Markdown Users – Quarto](https://quarto.org/docs/faq/rmarkdown.html)

Answers to R Markdown users’ most frequently asked questions about Quarto.

### What can I use Quarto for?

Quarto® is an open-source scientific and technical publishing system built on Pandoc. You can weave together narrative text and code to produce elegantly formatted output as documents, web pages, blog posts, books and more.

### Quarto sounds similar to R Markdown. What is the difference and why create a new project?

At its core, Quarto works the same way as R Markdown:

> Write plain text (with markdown) + code -> Render -> Output (HTML, PDF, Word, etc.)

The goal of Quarto is to make the process of creating and collaborating on scientific and technical documents dramatically better. Quarto combines the functionality of R Markdown, bookdown, distill, xaringian, etc into a single consistent system with “batteries included” that reflects everything we’ve learned from R Markdown over the past 10 years.

The number of languages and runtimes used for scientific discourse is very broad (and the Jupyter ecosystem in particular is extraordinarily popular). Quarto is at its core multi-language and multi-engine (supporting Knitr, Jupyter, and Observable today and potentially other engines tomorrow).

On the other hand, R Markdown is fundamentally tied to R which severely limits the number of practitioners it can benefit. Quarto is Posit’s attempt to bring R Markdown to everyone! Unlike R Markdown, Quarto doesn’t have a dependency or requirement for R. Quarto was developed to be multilingual, beginning with R, Python, Javascript, and Julia, with the idea that it will work even for languages that don’t yet exist.

While it is a “new” system, it should also be noted that it is highly compatible with existing content: you can render most R Markdown documents and Jupyter notebooks unmodified with Quarto. The concept is to make a major, long term investment in reproducible research, while keeping it compatible with existing formats and adaptable to the various environments users work in.

### Is R Markdown going away? Will my R Markdown documents continue to work?

R Markdown is not going away! R Markdown is used extensively and continues to work well. It will continue to be actively supported. We’re not leaving R Markdown, we’re expanding our scope. Over the years there have been many feature requests, and rather than implementing them all in R Markdown, for certain features we may refer you to Quarto. Everything that is currently in R Markdown will continue to work and be supported. There are no plans for deprecation.

Read more about this in Yihui Xie’s blog post [With Quarto Coming, is R Markdown Going Away? No.](https://yihui.org/en/2022/04/quarto-r-markdown/)

### Should I switch from R Markdown to Quarto?

If you like using R Markdown, there’s no need to switch! R Markdown will continue to be supported and work as it always has been. You’re welcome to try Quarto if you like, but there’s no need to switch. Some new features may only exist in Quarto, so if you want to use those, then that’s where you would give those a try.

We should emphasize that switching is not imperative. While we don’t plan on major feature initiatives in R Markdown and related packages, we are going to continue to maintain them (smaller improvements and bug fixes) for a long time to come. Furthermore, since Rmd files can in most cases be rendered without modification by Quarto, you can continue using R Markdown and the switching cost will still be minimal whenever you decide to do it.

### I use X (bookdown, blogdown, etc.). What is the Quarto equivalent?

Here are the Quarto equivalents for various packages and features of the R Markdown ecosystem (in some cases Quarto equivalents are not yet available but will be later this year):

| Feature                | R Markdown                                | Quarto                                                                       |
| :--------------------- | :---------------------------------------- | :--------------------------------------------------------------------------- |
| Basic Formats          | `html_document`, `pdf_document`, `word_document` | `html`, `pdf`, `docx`                                                        |
| Beamer                 | `beamer_presentation`                     | `beamer`                                                                     |
| PowerPoint             | `powerpoint_presentation`                 | `pptx`                                                                       |
| HTML Slides            | `xaringan`, `ioslides`, `revealjs`          | `revealjs`                                                                   |
| Advanced Layout        | `tufte`, `distill`                          | [Quarto Article Layout](https://quarto.org/docs/authoring/article-layout.html) |
| Cross References       | `html_document2`, `pdf_document2`, `word_document2` | [Quarto Crossrefs](https://quarto.org/docs/authoring/cross-references.html)  |
| Websites & Blogs       | `blogdown`, `distill`                     | [Quarto Websites](https://quarto.org/docs/websites/), [Quarto Blogs](https://quarto.org/docs/websites/website-blog.html) |
| Books                  | `bookdown`                                | [Quarto Books](https://quarto.org/docs/books/)                                 |
| Interactivity          | `Shiny Documents`                         | [Quarto Interactive Documents](https://quarto.org/docs/interactive/)           |
| Journal Articles       | `rticles`                                 | [Quarto Journal Articles](https://quarto.org/docs/journals/)                 |
| Paged HTML             | `pagedown`                                | Planned                                                                      |
| Dashboards             | `flexdashboard`                           | [Quarto Dashboards](https://quarto.org/docs/dashboards/)                     |
| Interactive Tutorials | `learnr`                                  | [Quarto Live Extension](https://github.com/quarto-ext/quarto-live)           |

### Can you create custom formats for Quarto like you can for R Markdown?

Quarto offers an [Extension](https://quarto.org/docs/extensions/) mechanism to add features to a format using [Shortcodes](https://quarto.org/docs/extensions/shortcodes.html) or [Filters](https://quarto.org/docs/extensions/filters.html) but also create [custom formats](https://quarto.org/docs/extensions/formats.html). A major difference with custom output format in R Markdown is that Quarto Extension does not use R but Lua, for example if you need to add some logic behind custom metadata fields. See [Developing with Lua](https://quarto.org/docs/extensions/lua.html) to get started if you need use it your extension. Some of the features from R Markdown custom formats like customizing knitting behavior can also now be done in YAML with [execution options](https://quarto.org/docs/computations/execution-options.html).

As example of custom formats for Quarto, [Journal Articles](https://quarto.org/docs/journals/) for Quarto are port of some custom output format inside the [`rticles`](https://pkgs.rstudio.com/rticles/) R package. Extensions lives in [Quarto Journals](https://github.com/quarto-journals) Github organization, and you can find information on how to [customize templates](https://quarto.org/docs/journals/templates.html) and [manage Authors](https://quarto.org/docs/journals/authors.html) for you format.

If you are an advanced developer of R Markdown custom format, the Extension mechanism may still have limitation (like pre and post processor). The Extension feature in Quarto will be improved over time - do not hesitate to share with us your use case or wished in our [Discussion Board](https://github.com/quarto-dev/quarto-cli/discussions).

### When would be a good time to start new projects in Quarto rather than R Markdown?

Quarto v1.0 was [announced at rstudio::conf(2022)](https://posit.co/blog/announcing-quarto-a-new-scientific-and-technical-publishing-system/). This is the first stable release which is already an excellent foundation for starting new projects with Quarto or migrating existing R Markdown projects (*if you are so inclined*). If you start using Quarto, please do stay updated with [latest release and changes](https://quarto.org/docs/download/) as development is very active.

### Does the RStudio IDE support Quarto?

Yes! You need to use RStudio v2022.07 or a later version, which includes support for [editing and preview of Quarto documents](https://quarto.org/docs/tools/rstudio.html).

You can download the latest release of RStudio from <https://posit.co/download/rstudio-desktop/>.

### Does Posit Connect support Quarto?

Yes! You can publish Quarto content to Posit Connect v2021.08.0 or later. Quarto has to be enabled as documented in the Posit Connect [admin guide](https://docs.posit.co/connect/admin/getting-started/#quarto). Connect’s user [documentation](https://docs.posit.co/connect/user/quarto/) refers to [Quarto.org docs](https://quarto.org/docs/publishing/rstudio-connect.html) on how to publish from the RStudio IDE. To publish Python-based Quarto content, you can use the [`rsconnect-python` CLI](https://docs.posit.co/connect/user/publishing/#publishing-quarto-python) from various locations, including VSCode, JupyterLab or the terminal.

