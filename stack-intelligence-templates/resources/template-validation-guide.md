# Stack Intelligence Template Validation Guide

The Stack Intelligence templates include a robust validation system to help ensure your documents follow the recommended structure and best practices for different document types.

## Using Template Validation

### Step 1: Specify Your Template Type

In your document's YAML frontmatter, include the `template_type` field:

```yaml
---
title: "Market Analysis: Cloud Computing in Financial Services"
author: "Jane Smith"
date: "2023-07-15"
template_type: "whitepaper"
---
```

### Step 2: Run Quarto Render

When you render your document, the validation system will automatically check your content against the requirements for your chosen template type.

## Supported Template Types

### Executive Brief

```yaml
template_type: "executive_brief"
```

**Required Sections:**
- Executive Summary
- Introduction
- Key Findings
- Recommendations

**Recommended Sections:**
- Case Study
- Methodology
- About Stack Intelligence

**Length Guidelines:** Maximum 25 pages (approximately 7,500 words)

### Whitepaper

```yaml
template_type: "whitepaper"
```

**Required Sections:**
- Executive Summary
- Introduction
- Background
- Analysis
- Conclusion

**Recommended Sections:**
- Methodology
- References
- About Author
- About Stack Intelligence

**Length Guidelines:** Maximum 50 pages (approximately 15,000 words)

### Case Study

```yaml
template_type: "case_study"
```

**Required Sections:**
- Challenge
- Solution
- Results
- Customer Quote

**Recommended Sections:**
- Company Background
- Implementation Details
- About Stack Intelligence

**Length Guidelines:** Maximum 15 pages (approximately 4,500 words)

### E-Book

```yaml
template_type: "ebook"
```

**Required Sections:**
- Introduction
- At least 3 chapters
- Conclusion

**Recommended Sections:**
- Foreword
- About Author
- References
- Resources

**Chapter Guidelines:** Minimum 3 chapters, maximum 12 chapters

## How Validation Works

During document rendering, the validation system checks for:

1. **Required Sections:** Missing required sections generate errors
2. **Document Length:** Documents exceeding recommended length generate warnings
3. **Template-Specific Rules:** Each template type has specific validation rules

## Responding to Validation Messages

### Validation Errors

Errors indicate that your document is missing essential components required by the template. You should address these issues to ensure your document follows the established structure.

Example error message:
```
Validation Errors for executive_brief:
  - Missing required sections: executive_summary, recommendations
```

### Validation Warnings

Warnings indicate recommended improvements but won't prevent your document from rendering. Consider addressing these to enhance document quality.

Example warning message:
```
Validation Warnings for whitepaper:
  - Document exceeds maximum recommended length of 50 pages (currently ~62 pages)
```

## Troubleshooting

If validation isn't working as expected:

1. Double-check that `template_type` is spelled correctly in your YAML frontmatter
2. Ensure your document sections have the proper headings/markers
3. Update to the latest version of the Stack Intelligence templates

## Custom Validation Rules

For projects requiring custom validation rules beyond the default templates, please contact the Stack Intelligence design team.