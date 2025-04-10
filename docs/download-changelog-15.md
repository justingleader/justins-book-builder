## Download: Changelog 1.5

Source: [1.5 Release Notes – Quarto](https://quarto.org/docs/download/changelog/1.5.html)

(Summarizes new features and bug fixes for Quarto version 1.5. Includes backports from v1.6 and patch release fixes.)

*   **v1.6 Backports & Patch Fixes:** Addresses issues with callouts in revealjs, Chrome arguments for remote rendering, `quarto inspect` with `!expr`, include resolution, float captions, error status reporting, dashboard titles, page navigation HTML, iTables in dashboards, website search performance, LaTeX citations, multi-column code folding, latex crossref underscores, IDE code cell detection, docusaurus preview, lightbox margin captions, manuscript embeds, empty LaTeX floats, `fig-align=right` in LaTeX, macOS installer messages, Connect publishing bundles, noncentered LaTeX subfigures, select controls in dashboard toolbars, duplicate headings in ipynb, navbar alignment, margin footnotes breaking hover-citations, breadcrumb markdown, R code cell LaTeX dependencies in books, dashboard Plotly on Windows, unix launcher paths, code cell layout rendering, `tbl-colwidths` regression, escaped inline code, `fig-alt` regression, `fig-subcap: true` crashes, `column-margin` spans, parsed HTML tables in various formats, R 4.1 compatibility, revealjs PDF export, unlabeled tables with `tbl-cap-location`.
*   **v1.5 Changes:**
    *   **HTML:** TOC expansion fixes, custom license URLs, body classes, margin layout fixes, `polyfill.io` replaced, code copy in modals, checkbox margins, callout rendering, table/header/body text appearance tuning.
    *   **PDF:** `rsvg-convert` control, captionless subfloats, locale hyphenation, table environments with custom floats, bibliography handling, listing crossref fixes.
    *   **RevealJS:** Whitespace stripping, special character handling in filenames, theme path fixes, code block header background.
    *   **Docusaurus/GFM:** Backtick escaping, MathJax preview for GFM, float rendering in GFM.
    *   **PowerPoint:** HTML table processing fixes.
    *   **Interactive Documents:** `code-link` ignored with Shiny+Knitr.
    *   **Websites:** Logo options for sidebars, title overwriting fixes, breadcrumb control, social metadata improvements, footer layout, announcement bar.
    *   **Books:** Footer URL fixes, bibliography URL fixes, download icon fixes.
    *   **OJS/Typst:** Error message improvements, Typst CSS translation, subfloat counters, callout fixes, data URI resolution, internationalization, custom formats updates, Typst 0.11.0 upgrade.
    *   **Jupyter:** Temp file naming, widget state escaping, kernel discovery with venv, mixed-case extensions, stream merging improvements, traceback in errors, image dimension fixes, notebook title fixes.
    *   **Listings:** Output directory exclusion, filtering improvements, localized filter text, `image: false` respect, duplicate author handling, YAML file listing fixes, image placeholder fixes, category feed support, lazy loading option.
    *   **Manuscripts:** Notebook ordering, theorem rendering.
    *   **Extensions:** Resource copying fixes, installation from branches with slashes, metadata extension type.
    *   **Shortcodes:** `embed` with Knitr+HTML dependencies, `placeholder` shortcode, key-value argument fixes, `embed` SVG retrieval, shortcode resolution in attributes.
    *   **Lightbox:** Description attribute usage.
    *   **Filters:** HTML raw block table extraction improvements, float type robustness, labeled table fixes with `eval: false`.
    *   **Other:** `classes: plain` for computational tables, preview template reloading, macOS architecture detection, Lua `LUA_CPATH` fix, lowercase filenames in `quarto create`, `quarto check` improvements, `quarto run` fixes, Deno V8 memory adjustment, TinyTeX mirror setting, `format: native` fixes, tabset configuration schema.
    *   **Languages:** Serbian-Latin, Slovak, Greek, Norwegian, Lithuanian, Traditional Chinese (Taiwan) translations added/updated.

