# Quarto Book Builder Common Resources

This directory contains shared resources that can be used across all book projects in the Quarto Book Builder system.

## Directory Structure

```
common/
├── assets/                # Shared CSS, images, and other assets
│   └── stack-intelligence/  # Stack Intelligence specific assets
├── filters/               # Reusable Quarto Lua filters
│   ├── openai-image.lua     # Image generation filter
│   └── stack-shortcodes.lua # Shortcodes implementation
└── templates/             # Global templates available to all projects
    ├── default_templates.yaml  # Default content blocks
    └── stack-intelligence-templates/  # Stack Intelligence template system
```

## Using Common Resources

### Filters

To use a filter in your Quarto project, reference it in your `_quarto.yml` file with a relative path:

```yaml
filters:
  - ../../../common/filters/openai-image.lua
```

See the [filters README](filters/README.md) for details on available filters.

### Templates

Global templates are automatically available to all projects without needing to redefine them in each project's `config.yaml`. Project-specific templates in a project's `config.yaml` will override global templates with the same name.

See the [templates README](templates/README.md) for details on available templates.

### Assets

To use shared assets in your Quarto project, reference them with a relative path:

```css
@import "../../../common/assets/stack-intelligence/stack-intel.css";
```

or in HTML:

```html
<link rel="stylesheet" href="../../../common/assets/stack-intelligence/stack-intel.css">
```

## Adding New Resources

When adding new resources:

1. Place them in the appropriate directory
2. Document their usage in the corresponding README file
3. Use relative paths to reference them from book projects