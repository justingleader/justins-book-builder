## Extensions: Metadata Extensions

Source: [Metadata Extensions – Quarto](https://quarto.org/docs/extensions/metadata.html)

Metadata extensions are Quarto extensions that provide metadata (YAML objects) that can be merged to existing Quarto configurations in a reusable manner.

**Important:** Currently, metadata extensions only merge project-level metadata. This limitation will be lifted in the future.

### Quick Start

Here we’ll describe how to create a simple metadata extension. We’ll use the `quarto create` command to do this. If you are using VS Code or RStudio you should execute `quarto create` within their respective integrated Terminal panes.

To get started, execute `quarto create extension metadata` within the parent directory where you’d like the filter extension to be created:

```bash
$ quarto create extension metadata
? Extension Name › my-prerender-scripts
```

As shown above, you’ll be prompted for an extension name. Type `my-prerender-scripts` and press Enter—the filter extension is then created:

```
? Extension Name › my-prerender-scripts
Creating extension at /Users/cscheid/Desktop/my-prerender-scripts:
- Created README.md
- Created _extensions/my-prerender-scripts/_extension.yml
- Created .gitignore
? Open With
❯ vscode
  rstudio
  (don't open)
```

If you are running within VS Code or RStudio a new window will open with the extension project.

### Contents of Metadata Extensions

Here’s what the contents of the files in `_extensions/my-prerender-scripts/` look like:

**_extensions/my-prerender-scripts/_extension.yml**
```yaml
title: My-prerender-scripts
author: Carlos Scheidegger
version: 1.0.0
quarto-required: ">=99.9.0"
contributes:
  metadata:
    project:
      # your per-project metadata goes here
```

### How Metadata Extensions Work

Under the `project` key, any YAML you add will be automatically merged to *any* project using this extension. This behaves differently from custom project extensions. Quarto projects using metadata extensions do not need to change their project types for the metadata to be merged.

**Note:** As noted above, metadata extensions only merge project-level metadata in the `project` key. This limitation will be lifted in the future.

