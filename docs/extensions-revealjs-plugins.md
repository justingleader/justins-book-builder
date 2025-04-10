## Extensions: Revealjs Plugins

Source: [Revealjs Plugins – Quarto](https://quarto.org/docs/extensions/revealjs.html)

### Overview

Revealjs plugins enable you to extend the capabilities of HTML presentations created with [Revealjs](https://revealjs.com/). The Reveal Plugin API is very rich, and many of the built-in capabilities of Quarto Revealjs presentations are implemented as plugins, including [Menu](https://quarto.org/docs/presentations/revealjs.html#navigation-menu), [Chalkboard](https://quarto.org/docs/presentations/revealjs.html#chalkboard), and [PDF Export](https://quarto.org/docs/presentations/revealjs.html#print-to-pdf).

Here are some examples of Revealjs plugins packaged as Quarto extensions:

| Extension | Description                                                                 |
| :-------- | :-------------------------------------------------------------------------- |
| [Pointer](https://github.com/quarto-ext/pointer)   | Adds support for switching the cursor to a ‘pointer’ style element while presenting. |
| [Attribution](https://github.com/quarto-ext/attribution) | Display attribution text along the right edge of slides.                    |

### Quick Start

Here we’ll describe how to create a simple Revealjs plugin extension. We’ll use the `quarto create` command to do this. If you are using VS Code or RStudio you should execute `quarto create` within their respective integrated Terminal panes.

To get started, execute `quarto create extension revealjs-plugin` within the parent directory where you’d like the plugin extension to be created:

```bash
$ quarto create extension revealjs-plugin
? Extension Name › shuffler
```

As shown above, you’ll be prompted for an extension name. Type `shuffler` and press Enter—the Revealjs plugin extension is then created:

```
Creating extension at /Users/jjallaire/quarto/dev/shuffler:
- Created README.md
- Created _extensions/shuffler/_extension.yml
- Created _extensions/shuffler/shuffler.css
- Created _extensions/shuffler/shuffler.js
- Created .gitignore
- Created example.qmd
```

If you are running within VS Code or RStudio a new window will open with the extension project.

Here’s what the contents of the files in `_extensions/shuffler/` look like:

**_extensions/shuffler/_extension.yml**
```yaml
title: Shuffler
author: J.J. Allaire
version: 1.0.0
quarto-required: ">=1.2.222"
contributes:
  revealjs-plugins:
    - name: RevealShuffler
      script:
        - shuffler.js
      stylesheet:
        - shuffler.css
```

**_extensions/shuffler/shuffler.js**
```javascript
window.RevealShuffler = function () {
  return {
    id: "RevealShuffler",
    init: function (deck) {
      // TODO: Implement your plugin functionality
      // Learn more at https://revealjs.com/creating-plugins/

      // This example shuffles the deck when the 'T' key is pressed
      deck.addKeyBinding({ keyCode: 84, key: "T" }, () => {
        deck.shuffle();
      });
    },
  };
};
```

There is also a `shuffler.css` file for providing any styles required by your plugin.

Finally, the `example.qmd` file includes code that exercises the extension. For example:

**example.qmd**
```yaml
---
title: "Shuffler Example"
format:
  revealjs: default
revealjs-plugins:
  - shuffler
---

