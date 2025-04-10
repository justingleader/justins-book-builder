# Salesforce Commerce and Revenue Cloud E-Book

This Quarto project contains the content for the "2x your Lifetime Customer Value with Salesforce Commerce and Revenue Cloud" e-book.

## Current Implementation

The e-book uses the Stack Intelligence templates for styling and formatting. The implementation includes:

- Professional cover page with Stack Intelligence branding
- Custom content blocks with Stack Intelligence styling:
  - Featured quotes with orange accents
  - Case studies with structured metadata
  - Listicles with enhanced formatting
  - Statistics highlights for key metrics
  - Action plans with distinctive styling
  - Quick tips sections for implementation advice
- Custom typography using Helvetica Neue
- Professional layout with headers, footers, and proper spacing

## Files and Structure

- `_quarto.yml` - Configuration file for the Quarto project
- `index.md` - Cover page and book frontmatter
- `00a_Introduction.md` - Introduction chapter
- `01.md` through `12.md` - Main chapters of the book
- `_book/` - Generated output files
- `stack-shortcodes.lua` - Local implementation of the Stack Intelligence shortcodes

## Building the Book

To render the book to PDF:

```bash
quarto render --to pdf
```

Output will be generated in the `_book` directory.

## Relationship to Global Templates

This project uses a localized version of the Stack Intelligence templates. The global templates are available in:

- `/common/templates/stack-intelligence-templates/` - Full template system
- `/common/filters/` - Global Lua filters

This localization enables the project to work independently while maintaining the Stack Intelligence brand identity.

## Shortcodes

The book uses the following shortcodes for custom content blocks:

```markdown
{{{< featured-quote color="primaryorange" size="normal" >}}
Quote text goes here.

Author Name, Position at Company
{{{< /featured-quote >}}

{{{< case-study company="Company Name" segment="Industry" revenue="$XXM" challenge="Challenge" outcome="Outcome" >}}
Case study content goes here.

> "Optional quote from company representative."
> 
> — Name, Position
{{{< /case-study >}}

{{{< listicle title="Title" style="numbered" >}}
1. First item
2. Second item
3. Third item
{{{< /listicle >}}

{{{< stats-highlight title="Statistics Title" >}}
- **Statistic 1**: Value and context
- **Statistic 2**: Value and context
{{{< /stats-highlight >}}

{{{< action-plan title="Action Plan Title" >}}
1. **First step**: Details
2. **Second step**: Details
{{{< /action-plan >}}

{{{< quick-tips title="Tips Title" >}}
- First tip
- Second tip
{{{< /quick-tips >}}
```