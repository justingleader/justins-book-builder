# Quarto Book Builder: Markdown Formatting Guide

This guide covers the proper formatting of markdown for the Quarto Book Builder system.

## Basic Structure

### Chapter Frontmatter
```markdown
---
title: "Chapter Title"
author: "Author Name"
description: "Brief chapter description"
date: "2025-04-07"
---
```

### Headings
```markdown
# Chapter Title (H1)
## Section Title (H2)
### Subsection Title (H3)
```

## Special Features

### AI Image Generation

#### Code Block Syntax
```markdown
```{.openai-image}
prompt: "A serene mountain landscape at sunset with a lake reflecting the orange sky"
size: "1024x1024"  # Optional
quality: "standard"  # Optional
style: "vivid"  # Optional
```
```

#### Inline Syntax
```markdown
{{image: A digital painting of a castle on a hill at sunset, with golden skies}}
```

### Custom Templates

#### Featured Quote
```markdown
::: featured-quote
"This is the quote text."
**— Author Name**
:::
```

#### Callout
```markdown
::: callout
title: Note Title
type: info  # Options: info, warning, danger, success

Callout content goes here.
:::
```

#### Figure
```markdown
::: figure
src: path/to/image.png
caption: Figure caption
description: Optional longer description
credit: Image credit information
:::
```

#### Code Block with Caption
```markdown
::: code-block
title: Example Code
language: python

def hello_world():
    print("Hello, world!")
:::
```

#### Listicle
```markdown
::: listicle
title: Top 3 Points

1. First important point
2. Second important point 
3. Third important point
:::
```

## Configuration Files

The build process uses two main configuration files:

### config.yaml
Contains OpenAI API keys, image directories, and custom template definitions.

### _quarto.yml
Defines the book structure, chapters, and output formats.

## Common Issues

- Ensure proper indentation in template blocks
- Check image paths for PDF vs HTML/EPUB formats
- Verify template names match those defined in config.yaml

## Global Templates

The system supports global templates that can be used across all book projects. These templates are stored in the `common/templates/` directory and are automatically loaded into any project.

### Using Global Templates

1. Global templates are defined in YAML files in the `common/templates/` directory, such as `common/templates/default_templates.yaml`.
2. These templates are automatically available to all projects without needing to redefine them in each project's `config.yaml`.
3. Project-specific templates in a project's `config.yaml` will override global templates with the same name.

### Available Global Templates

The system includes the following global templates:

- `featured-quote`: For highlighting important quotes
- `callout`: For information, warning, danger, and success callouts
- `figure`: For images with captions
- `code-block`: For code snippets with titles
- `listicle`: For numbered or bulleted lists with a title
- `expert-quote`: For quotes from industry experts
- `comparison-table`: For comparing different options
- `definition-callout`: For defining technical terms
- `callout-success-story`: For customer success stories
- `figure-stats`: For highlighting key metrics
- `code-block-checklist`: For implementation checklists

### Creating New Global Templates

To create a new global template:

1. Add your template definition to `common/templates/default_templates.yaml` or create a new YAML file in the `common/templates/` directory.
2. Add corresponding CSS styles to `common/assets/styles.scss` if needed.
3. The template will automatically be available to all projects.

## Release Notes

### v1.0.0 (April 10, 2025) - Template Framework Update

#### Major Changes
- Implemented a comprehensive template framework that separates core functionality from brand assets
- Created brand-aware templates with support for multiple output formats (PDF, HTML, EPUB)
- Added custom callout environments to create professionally styled documents
- Fixed PDF rendering issues for e-commerce book

#### Template System Enhancements
- Implemented a robust logging system for debugging template rendering
- Created a brand loading system that separates branding from core templates
- Added component handlers for various content blocks (quotes, callouts, stats blocks)
- Built custom LaTeX environments for professional PDF styling
- Added header and footer customization with brand colors
- Improved typography with proper font selection based on brand guidelines

#### New Components
- Featured Quote: Styled pull quotes with attribution
- Executive Guide: Professional callout boxes for key executive summaries
- Success Story: Callout boxes for customer testimonials
- Stats Block: Visually distinct blocks for statistics and metrics

#### Known Issues
- HTML output requires additional stylesheet refinements
- EPUB format still needs template testing and optimization
- Custom image handling needs improvement for multi-format compatibility

## Directory Structure

The workspace is organized to manage multiple book projects and shared resources:

```
/
├── common/                 # Shared resources across all projects
│   ├── filters/            # Reusable Quarto Lua filters
│   ├── templates/          # Global templates available to all projects
│   └── assets/             # Shared images, CSS, etc.
├── docs/                   # Split documentation files (generated by split_docs.py)
│   └── draft/              # Raw, large documentation files (e.g., source before splitting)
├── logs/                   # Log files from build processes or scripts
├── projects/               # Contains individual book projects
│   └── [your-book-name]/   # Directory for a specific book
│       ├── input/            # Raw source materials (e.g., .md chapters, images)
│       ├── draft-1/          # Folder for the first draft iteration
│       │   ├── working/      # Active Quarto project files (.qmd, _quarto.yml)
│       │   │   └── _extensions/  # Quarto extension with templates and filters
│       │   └── output/       # Rendered output for this draft (PDF, HTML)
│       ├── draft-2/          # Folder for the second draft iteration
│       │   ├── working/
│       │   └── output/
│       └── ...               # Additional drafts
├── quarto_book_builder/    # Source code for the builder tool
├── tests/                  # Tests for the builder tool
├── temp/                   # Temporary files (e.g., downloads)
├── .venv/                  # Python virtual environment
├── _build/                 # Quarto build output directory (often project-specific)
├── .gitignore              # Specifies intentionally untracked files
├── README.md               # This file
├── requirements.txt        # Python package requirements
├── setup.py                # Python package setup script
├── split_docs.py           # Script to split large markdown files by H2 headers
└── test_app.py             # Test application script
```

**Brand Assets Directory Structure:**

The `brand-assets/` directory contains all brand-related resources and guidelines:

```
brand-assets/
├── images/                 # Brand visual assets
│   ├── logos/             # Company logos in various formats
│   ├── color-swatches/    # Brand color palette visual references
│   └── photography/       # Brand photography guidelines and examples
├── json/                  # Machine-readable brand specifications
│   ├── color_palette.json     # Color definitions and usage
│   ├── typography.json        # Font specifications
│   ├── layout_spacing.json    # Layout and spacing rules
│   ├── logo_usage.json       # Logo usage guidelines
│   └── imagery_photography.json # Photography style guide
├── markdown/              # Human-readable brand guidelines
│   ├── stack_intelligence_style_guide.md  # Main style guide
│   ├── color_palette_specifications.md    # Color usage details
│   ├── typography_guidelines.md           # Typography rules
│   ├── layout_spacing_principles.md       # Layout guidelines
│   ├── logo_guidelines.md                 # Logo usage rules
│   └── imagery_photography_guidelines.md  # Photography guidelines
└── templates/            # Brand-compliant document templates
    ├── b2b_executive_ebook_template.md    # Executive ebook template
    └── salesforce_ae_ebook_template.md    # Sales ebook template
```

**Notes on `docs/` Directory:**

*   The `docs/draft/` subdirectory is used to store original, large documentation files (like `quarto-docs-full.md`).
*   The `split_docs.py` script reads files from `docs/draft/`, splits them based on Level 2 Markdown headers (`##`), and writes the resulting smaller files directly into the main `docs/` directory.

**Workflow:**

1.  Place raw manuscript files (e.g., `.md` chapters, images) into `projects/[your-book-name]/input/`.
2.  Run the input processor to move files to draft and delete input files:
   ```bash
   python process_input.py [your-book-name]
   ```
   This will:
   - Copy files from `input/` to `draft-1/working/`
   - Delete the files from `input/` after successful processing
3.  For a new draft (e.g., `draft-1`), create the `draft-1/working/` and `draft-1/output/` subdirectories if they don't exist.
4.  Set up the `