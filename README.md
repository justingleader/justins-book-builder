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

## Directory Structure

The workspace is organized to manage multiple book projects and shared resources:

```
/
├── common/                 # Shared resources across all projects
│   ├── filters/            # Reusable Quarto Lua filters
│   └── assets/             # Shared images, CSS, etc.
├── docs/                   # General documentation (like this README)
├── logs/                   # Log files from build processes or scripts
├── projects/               # Contains individual book projects
│   └── [your-book-name]/   # Directory for a specific book
│       ├── input/            # Raw source materials (e.g., .md chapters, images)
│       ├── draft-1/          # Folder for the first draft iteration
│       │   ├── working/      # Active Quarto project files (.qmd, _quarto.yml)
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
└── test_app.py             # Test application script
```

**Workflow:**

1.  Place raw manuscript files (e.g., `.md` chapters, original images) into `projects/[your-book-name]/input/`.
2.  For a new draft (e.g., `draft-1`), create the `draft-1/working` and `draft-1/output` subdirectories.
3.  Copy or adapt files from `input/` into `draft-1/working/`. Set up the `_quarto.yml` file within `draft-1/working/`.
4.  Work on the book within the `draft-1/working/` directory.
5.  Render the book using Quarto, directing the output (if possible) or moving it to `draft-1/output/`.
6.  For subsequent drafts, repeat steps 2-5 (e.g., for `draft-2`).
7.  Shared filters or assets (like CSS themes) should be placed in the `common/` directory and referenced using relative paths from the `_quarto.yml` file in a draft's `working` directory (e.g., `../../common/filters/myfilter.lua`).
