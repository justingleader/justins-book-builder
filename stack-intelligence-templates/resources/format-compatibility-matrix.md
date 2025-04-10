# Stack Intelligence Format Compatibility Matrix

This document provides a detailed overview of how different template features render across output formats.

## Core Features

| Feature | PDF (stack-pdf) | HTML (stack-html) | EPUB (stack-epub) | Notes |
|---------|----------------|-------------------|-------------------|-------|
| **Typography** | ✅ Complete | ✅ Complete | ✅ Complete | Web formats use fallback fonts if Helvetica Neue is unavailable |
| **Color Scheme** | ✅ Complete | ✅ Complete | ✅ Complete | PDF uses CMYK equivalents for print compatibility |
| **Cover Page** | ✅ Complete | ✅ Complete | ✅ Complete | EPUB uses simplified cover layout |
| **Executive Summary** | ✅ Complete | ✅ Complete | ✅ Complete | Styling adapts to format requirements |
| **Table of Contents** | ✅ Complete | ✅ Complete | ✅ Complete | HTML provides interactive TOC |
| **Chapter Headers** | ✅ Complete | ✅ Complete | ✅ Complete | | 
| **Back Cover** | ✅ Complete | ⚠️ Basic | ⚠️ Basic | Full back cover in PDF only |

## Content Blocks

| Content Block | PDF (stack-pdf) | HTML (stack-html) | EPUB (stack-epub) | Notes |
|---------------|----------------|-------------------|-------------------|-------|
| **Featured Quotes** | ✅ Complete | ✅ Complete | ✅ Complete | |
| **Case Studies** | ✅ Complete | ✅ Complete | ✅ Basic | EPUB uses simplified layout |
| **Listicles** | ✅ Complete | ✅ Complete | ✅ Complete | |
| **Action Plans** | ✅ Complete | ✅ Complete | ✅ Complete | |
| **Stats Highlights** | ✅ Complete | ✅ Complete | ✅ Complete | |
| **Quick Tips** | ✅ Complete | ✅ Complete | ✅ Complete | |
| **Tables** | ✅ Complete | ✅ Complete | ⚠️ Basic | Complex tables simplified in EPUB |
| **Figures/Images** | ✅ Complete | ✅ Complete | ✅ Complete | Resolution adapts to format |
| **Code Blocks** | ✅ Complete | ✅ Complete | ⚠️ Basic | Line numbering only in PDF/HTML |

## Advanced Features

| Feature | PDF (stack-pdf) | HTML (stack-html) | EPUB (stack-epub) | Notes |
|---------|----------------|-------------------|-------------------|-------|
| **Cross-references** | ✅ Complete | ✅ Complete | ✅ Complete | All formats support internal links |
| **Citations** | ✅ Complete | ✅ Complete | ✅ Complete | |
| **Footnotes** | ✅ Complete | ✅ Complete | ⚠️ Basic | EPUB uses endnotes instead of footnotes |
| **Page Numbers** | ✅ Complete | ❌ N/A | ❌ N/A | Web formats don't use fixed pagination |
| **Headers/Footers** | ✅ Complete | ❌ N/A | ❌ N/A | Web formats don't use page headers/footers |
| **Responsive Design** | ❌ N/A | ✅ Complete | ✅ Complete | PDF has fixed layout |
| **Accessibility** | ⚠️ Basic | ✅ Complete | ✅ Complete | HTML has most advanced accessibility features |
| **Print Optimization** | ✅ Complete | ⚠️ Basic | ❌ N/A | PDF is fully print-optimized |
| **File Size** | ⚠️ Larger | ✅ Optimized | ✅ Optimized | PDF includes embedded fonts and high-res graphics |

## Content Recommendations by Format

### PDF (stack-pdf)
- Ideal for formal reports, executive briefs, and print distribution
- Best for documents where layout precision is critical
- Supports complex layouts, tables, and graphics
- Preferred for documents that will be referenced by page number

### HTML (stack-html)
- Ideal for interactive content, web publishing, and screen reading
- Best for documents that will be accessed on multiple devices
- Supports responsive design and interactive elements
- Good for SEO and web discoverability

### EPUB (stack-epub)
- Ideal for long-form content like e-books and detailed guides
- Best for reading on e-readers, tablets, and mobile devices
- Supports reflowable text for different screen sizes
- Good for offline reading and distribution via e-book platforms

## Cross-Format Publishing Best Practices

1. **Design for the lowest common denominator**
   - Keep layouts simple enough to work in all formats
   - Avoid features that only work in one format

2. **Test in all target formats**
   - Always preview your document in each format
   - Address format-specific issues before publishing

3. **Use appropriate media for each format**
   - High-resolution images for PDF
   - Web-optimized images for HTML
   - Smaller file size images for EPUB

4. **Leverage format-specific enhancements**
   - Add print marks and bleed for PDF when needed
   - Use responsive design features in HTML
   - Optimize navigation for EPUB