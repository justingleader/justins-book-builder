# Quarto Book Builder Templates

This directory contains global templates that can be used across all book projects in the Quarto Book Builder system.

## Available Templates

### Default Templates (default_templates.yaml)

These templates provide common content blocks that can be used in any Quarto book project:

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

### Stack Intelligence Templates

A comprehensive template system for creating professional business documents with Stack Intelligence branding. These templates support multiple output formats (PDF, HTML, EPUB) and include:

- Customized layout and styling
- Professional typography
- Branded colors and visual elements
- Cross-format compatibility
- Shortcodes for common content blocks
- Validation for template usage

See the [Stack Intelligence Templates README](stack-intelligence-templates/README.md) for more details.

## Using Global Templates

Global templates are automatically available to all projects without needing to redefine them in each project's `config.yaml`. Project-specific templates in a project's `config.yaml` will override global templates with the same name.

## Creating New Global Templates

To create a new global template:

1. Add your template definition to `default_templates.yaml` or create a new YAML file in this directory
2. Add corresponding CSS styles to `common/assets/styles.scss` if needed
3. The template will automatically be available to all projects