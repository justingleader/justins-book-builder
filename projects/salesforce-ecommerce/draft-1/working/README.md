# Quarto Templates Framework

A flexible Quarto template system with branding support, consistent components across formats, and comprehensive logging.

## Status

This project is currently in active development. See [PROGRESS.md](PROGRESS.md) for current status.

## Features

- **Cross-format Support**: Consistent components for PDF, HTML, and EPUB outputs
- **Brand System**: Easily switch between different brand styles without changing templates
- **Component Library**: Reusable, styled components like stats blocks and callouts
- **Comprehensive Logging**: Detailed logging system for troubleshooting

## Directory Structure

```
quarto-templates/
├── _extensions/
│   └── templates/          # Core extension
│       ├── _extension.yml  # Extension configuration
│       ├── templates/      # Format templates
│       ├── partials/       # Template partials
│       ├── resources/      # CSS and JS resources
│       ├── lua/            # Lua filters
│       └── examples/       # Example documents
│
├── branding/               # Brand assets
│   ├── stack-intelligence/ # One brand
│   └── other-brand/        # Another brand
│
└── docs/                   # Documentation
```

## Installation

Coming soon.

## Usage

```yaml
---
title: "My Document"
format: templates-pdf     # Or templates-html, templates-epub
brand: stack-intelligence # Brand name (folder in branding/)
log-level: INFO          # DEBUG, INFO, WARNING, ERROR
log-file: "_logs/render.log"
---
```

## Component Examples

### Stats Block
```markdown
::: {.stats-block title="Key Performance Metrics"}
- **80%** increase in conversion rate
- **45%** reduction in bounce rate
- **2.5x** improvement in customer retention
:::
```

### Success Story
```markdown
::: {.callout-success}
## Success Story: Company Name

**Company:** Acme Corp  
**Industry:** Manufacturing  
**Challenge:** Legacy systems causing delays  
**Solution:** Implemented AI-driven workflow  
**Results:**  
- 35% increase in productivity
- $2.4M annual cost savings
- 98% customer satisfaction rating
:::
```

## License

Copyright © 2025 Stack Intelligence. All rights reserved.

## Contact

For more information, contact info@stackintelligence.com