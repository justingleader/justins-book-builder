# Stack Intelligence Templates for Quarto

This Quarto extension provides professional templates and tools for creating business documents that follow Stack Intelligence brand guidelines. The templates support multiple output formats including PDF, HTML, and DOCX.

## Installation

```bash
quarto add stack-intelligence/templates
```

## Usage

### Step 1: Create a new document using the template

```bash
quarto use template stack-intelligence/templates/starter
```

### Step 2: Edit your document using the built-in shortcodes

```markdown
{{{< featured-quote >}}
This is an impactful quote that captures the essence of your message.

Author Name, Position at Company
{{{< /featured-quote >}}
```

### Step 3: Render your document

```bash
quarto render document.qmd
```

## Features

- Professional templates for executive briefs, whitepapers, case studies, and e-books
- Responsive design for both print and digital formats
- Built-in shortcodes for common content blocks
- Automatic validation of document structure
- Stack Intelligence brand compliance
- Cross-format compatibility

## Documentation

### Template Types

The extension supports the following document types:

- **Executive Brief**: Concise documents (10-25 pages) for senior leadership
- **Whitepaper**: In-depth exploration of a topic (20-50 pages)
- **Case Study**: Real-world implementation examples (5-15 pages)
- **E-Book**: Comprehensive, visually engaging content (3-12 chapters)

Specify the template type in your YAML frontmatter:

```yaml
---
title: "Document Title"
author: "Author Name"
date: today
template_type: "executive_brief" # Options: executive_brief, whitepaper, case_study, ebook
---
```

### Available Shortcodes

- `featured-quote`: Highlight impactful quotes
- `case-study`: Showcase real-world examples
- `listicle`: Present key points in a structured format
- `figure`: Display images with captions and credits
- `enhanced-table`: Format tables with titles and styling
- `code-block`: Display code snippets with syntax highlighting
- `action-plan`: Present executive action plans
- `stats-highlight`: Emphasize key statistics
- `quick-tips`: Provide implementation best practices

See the [Snippet Library Guide](resources/snippet-library-guide.md) for detailed usage examples.

### Validation System

The templates include a validation system that checks your document structure against best practices for each document type. See the [Template Validation Guide](resources/template-validation-guide.md) for details.

### Resources

- [Template Structure Guide](resources/documents/template-structure.md)
- [Document Checklist](resources/documents/template-checklist.md)
- [Snippet Library](resources/snippets/)

## License

© 2023 Stack Intelligence. All rights reserved.

## Support

For questions or support, contact: support@stackintelligence.com