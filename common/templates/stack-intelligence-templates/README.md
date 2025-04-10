# Stack Intelligence Templates for Quarto

This directory contains the Stack Intelligence template system for Quarto, organized according to the Quarto Book Builder project structure. These templates provide professional styling for business documents across multiple output formats.

## Directory Structure

```
stack-intelligence-templates/
├── PREVIEW.md             # Progress tracking document
├── README.md              # This file
├── _extension.yml         # Quarto extension configuration
├── covers/                # Cover page images and assets
├── epub/                  # EPUB-specific styling and configuration
├── lua/                   # Lua filters for content processing
│   ├── stack-accessibility.lua
│   ├── stack-blocks.lua
│   ├── stack-code.lua
│   ├── stack-epub.lua
│   ├── stack-figures.lua
│   ├── stack-pdf-optimize.lua
│   ├── stack-shortcodes.lua
│   ├── stack-tables.lua
│   └── stack-validation.lua
├── partials/              # LaTeX template partials
│   ├── back-cover.tex
│   ├── callouts.tex
│   ├── case-study.tex
│   ├── chapter-header.tex
│   ├── code-block.tex
│   ├── cover.tex
│   ├── executive-summary.tex
│   ├── figure.tex
│   └── table.tex
├── resources/             # Documentation and examples
│   ├── cross-format-guide.md
│   ├── documents/
│   │   ├── template-checklist.md
│   │   └── template-structure.md
│   ├── examples/
│   │   ├── cross-format-test.qmd
│   │   ├── sample-chapter.qmd
│   │   ├── sample-executive-summary.qmd
│   │   └── shortcode-reference.qmd
│   ├── format-compatibility-matrix.md
│   ├── snippet-library-guide.md
│   ├── snippets/
│   │   ├── action-plan.qmd
│   │   ├── case-study.qmd
│   │   ├── code-block.qmd
│   │   ├── executive-summary.qmd
│   │   ├── featured-quote.qmd
│   │   ├── figure.qmd
│   │   ├── listicle.qmd
│   │   ├── quick-tips.qmd
│   │   ├── stats-highlight.qmd
│   │   └── template-starter.qmd
│   └── template-validation-guide.md
├── styles/                # CSS styling for HTML output
│   ├── stack-intel.css
│   ├── stack-intel.scss
│   └── stack-responsive.css
└── templates/             # Main template files
    └── stack-book.tex
```

## Related Files

The templates rely on Lua filters in the common filters directory:

```
common/filters/
├── openai-image.lua       # Image generation filter
└── stack-shortcodes.lua   # Shortcodes implementation
```

## Usage

To use these templates in a Quarto book project, add the following to your `_quarto.yml` file:

```yaml
format:
  pdf:
    include-in-header: 
      - text: |
          \usepackage{xcolor}
          \usepackage{tcolorbox}
          \usepackage{fontspec}
          \usepackage{fancyhdr}
          \tcbuselibrary{skins,breakable}
          
          % Stack Intelligence colors
          \definecolor{primaryblue}{HTML}{2a368e}
          \definecolor{primaryorange}{HTML}{EB7527}
          \definecolor{secondaryblue}{HTML}{7EA0C6}
          \definecolor{secondarytext}{HTML}{666666}
          
          % Use system fonts
          \setmainfont{Helvetica Neue}
          
          % Header and footer styling
          \pagestyle{fancy}
          \fancyhf{}
          \fancyhead[LE,RO]{\thepage}
          \fancyhead[RE,LO]{\slshape\nouppercase{\leftmark}}
          \fancyfoot[C]{\textcopyright\ 2023 Stack Intelligence}
          \renewcommand{\headrulewidth}{0.4pt}
          \renewcommand{\footrulewidth}{0pt}
    documentclass: scrreprt
    papersize: letter
    fontsize: 11pt
    toc: true
    toc-title: "CONTENTS"
    number-sections: true
    colorlinks: true
    linkcolor: primaryblue
    geometry:
      - margin=1in
    fig-width: 6
    fig-height: 4
    highlight-style: github
    filters:
      - ../../../common/filters/stack-shortcodes.lua
```

## Available Shortcodes

The following shortcodes are available for use in your documents:

- `featured-quote`: For highlighting important quotes
- `case-study`: For showcasing real-world examples
- `listicle`: For creating structured lists
- `figure`: For images with captions and credits
- `enhanced-table`: For formatted tables
- `code-block`: For code snippets with titles
- `action-plan`: For executive action plans
- `stats-highlight`: For emphasizing key statistics
- `quick-tips`: For implementation advice

See the `resources/snippet-library-guide.md` file for detailed usage examples.

## Document Types

The template system supports the following document types:

- **Executive Brief**: Concise documents (10-25 pages) for senior leadership
- **Whitepaper**: In-depth exploration of a topic (20-50 pages)
- **Case Study**: Real-world implementation examples (5-15 pages)
- **E-Book**: Comprehensive, visually engaging content (3-12 chapters)

Specify the document type in your YAML frontmatter using the `template_type` field.

## Cross-Format Support

These templates provide consistent styling across multiple output formats:

- **PDF**: High-quality print-ready output
- **HTML**: Responsive web output
- **EPUB**: E-reader friendly format

See `resources/cross-format-guide.md` for details on optimizing for each format.