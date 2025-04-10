# Cover Images for Stack Intelligence Templates

This directory should contain cover images for different output formats:

- `stack-cover.png` - Default cover image for EPUB and other formats
- `stack-cover-highres.png` - High-resolution cover for print (300 DPI)

## Cover Image Requirements

### EPUB Covers
- Dimensions: 1600 x 2400 pixels (2:3 aspect ratio)
- Format: PNG or JPG
- File: `stack-cover.png`

### Print Covers
- Dimensions: 3000 x 4500 pixels (2:3 aspect ratio)
- Resolution: 300 DPI
- Format: PNG or JPG
- File: `stack-cover-highres.png`

### Web Covers
- Dimensions: 1200 x 1800 pixels (2:3 aspect ratio)
- Format: PNG or JPG
- File: `stack-cover-web.png`

## Template Cover Design

The default Stack Intelligence cover design includes:
- Stack Intelligence logo at the top
- Title centered in Primary Blue
- Subtitle below in Secondary Blue
- Author name(s) at the bottom
- Optional background pattern or image

## Customizing Cover Images

To use a custom cover image, specify it in your YAML frontmatter:

```yaml
---
title: "Document Title"
author: "Author Name"
format:
  stack-pdf:
    cover-image: "my-custom-cover.png"
  stack-epub:
    epub-cover-image: "my-custom-cover.png"
---
```