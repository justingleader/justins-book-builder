# Cross-Format Optimization Guide

This guide explains how to effectively use the Stack Intelligence template system across multiple output formats (PDF, HTML, and EPUB).

## Format-Specific Features

### PDF Output

PDF output is optimized for both digital viewing and printing using the `stack-pdf` format.

```yaml
format:
  stack-pdf: default
```

Key PDF features:
- Professional print-ready layout
- High-resolution image handling (300 DPI)
- Precise typography control
- Proper page breaks around content blocks
- Table of contents with page numbers
- Page headers and footers

### HTML Output

HTML output is responsive and web-optimized using the `stack-html` format.

```yaml
format:
  stack-html: default
```

Key HTML features:
- Responsive design that adapts to different screen sizes
- Optimized for both desktop and mobile viewing
- Accessibility enhancements for screen readers
- Interactive elements when appropriate
- Fixed navigation with table of contents

### EPUB Output

EPUB output is optimized for e-readers and mobile devices using the `stack-epub` format.

```yaml
format:
  stack-epub: default
```

Key EPUB features:
- Reflowable text to accommodate different screen sizes
- Lightweight, optimized for e-readers
- Embedded fonts and styling
- Proper chapter navigation
- Compatible with major e-reader platforms

## Multi-Format Publishing

To create a document that can be rendered in multiple formats, specify all desired formats in your YAML frontmatter:

```yaml
---
title: "Document Title"
author: "Author Name"
date: "2023-12-01"
format:
  stack-pdf: default
  stack-html: default
  stack-epub: default
---
```

## Format-Specific Customizations

Each format can be customized individually:

```yaml
---
title: "Document Title"
author: "Author Name"
date: "2023-12-01"
format:
  stack-pdf:
    lot: true              # List of tables
    lof: true              # List of figures
    fontsize: 11pt
  stack-html:
    toc-depth: 4
    theme: flatly
  stack-epub:
    css: "custom-epub.css"
---
```

## Optimizing Images

For cross-format compatibility, consider these image guidelines:

1. **Use vector formats (SVG)** when possible for diagrams and illustrations
2. **Provide high-resolution raster images** (300 DPI) for photographs
3. **Use appropriate width attributes** in your markup:

```markdown
{{{< figure src="images/diagram.svg" width="80%" 
   caption="Architecture Diagram" >}}
```

4. **Avoid fixed pixel dimensions** in favor of percentage-based widths

## Handling Complex Tables

For tables that need to work across formats:

1. **Keep tables simple** when possible (4-5 columns maximum)
2. **Use the enhanced-table shortcode** for complex tables:

```markdown
{{{< enhanced-table title="Quarterly Results" >}}
| Quarter | Revenue | Growth |
|---------|---------|--------|
| Q1      | $1.2M   | 5%     |
| Q2      | $1.4M   | 16%    |
{{{< /enhanced-table >}}
```

3. **Consider breaking complex tables** into multiple simpler tables

## Accessibility Considerations

The template system includes built-in accessibility enhancements:

1. **Proper heading structure** - Use sequential heading levels (h1, h2, h3, etc.)
2. **Image alt text** - Always provide descriptive alt text for images
3. **Semantic HTML** - The system adds appropriate ARIA roles and attributes
4. **Color contrast** - Stack Intelligence colors meet WCAG AA standards
5. **Scalable text** - Text remains readable when scaled up

## Performance Optimization

For faster rendering and better user experience:

1. **Optimize images** - Compress images before including them
2. **Use appropriate formats** - SVG for vector graphics, WebP or JPEG for photos
3. **Break long documents** into chapters or sections
4. **Limit use of complex elements** in extremely long documents

## Testing Cross-Format Output

Always test your document in all target formats:

```bash
quarto render document.qmd --to stack-pdf
quarto render document.qmd --to stack-html
quarto render document.qmd --to stack-epub
```

Or render all formats at once:

```bash
quarto render document.qmd
```

## Troubleshooting Common Issues

### PDF Rendering Issues

- **Problem**: Tables or figures break across pages awkwardly
  **Solution**: Use the `{breakable=false}` attribute in LaTeX blocks

- **Problem**: Long code blocks overflow page margins
  **Solution**: Set `{breaklines=true}` in LaTeX code block

### HTML Rendering Issues

- **Problem**: Content overflows on mobile screens
  **Solution**: Avoid fixed-width elements, use percentage-based widths

- **Problem**: Navigation sidebar takes too much space on small screens
  **Solution**: The responsive design automatically converts the sidebar to a collapsible menu

### EPUB Rendering Issues

- **Problem**: Complex layouts don't render properly on e-readers
  **Solution**: Simplify layouts for EPUB, use standard formatting

- **Problem**: Custom fonts don't appear on some e-readers
  **Solution**: The template uses fallback fonts that are widely supported