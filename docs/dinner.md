## Dinner
- Eat spaghetti
- Drink wine
```

To develop your plugin, render/preview `example.qmd`, and then make changes to `shuffler.js` and `shuffler.css` (the preview will automatically refresh when you change these files).

### Installation and Use

If your extension source code it located within a GitHub repository, then it can be added by referencing the GitHub organization and repository name. For example, you can install the `attribution` extension with the following:

```bash
quarto add quarto-ext/attribution
```

Note that it is possible to bundle and distribute extensions as simple gzip archives (as opposed to using a GitHub repository as described above). See the article on [Distributing Extensions](https://quarto.org/docs/extensions/distributing.html) for additional details.

Once an extension has been added, you can use the Reveal plugin by adding it to the `reveal-plugins` key. For example:

```yaml
---
title: "My Presentation"
format: revealjs
revealjs-plugins:
  - attribution
---
```

### Plugin Packaging

Note that the plugins listed above were not initially developed for use with Quarto. Rather, they were developed intially as native Revealjs plugins and then packaged as Quarto extensions.

For example, you can find the original implementation of the attribution plugin here: <https://github.com/rschmehl/reveal-plugins/tree/main/attribution>. The plugin is implemented with a JavaScript file and a CSS file. To make the plugin available as a Quarto extension, we package these files along with an `_extension.yml` config file that registers the plugin. Here are the files in the Quarto extension:

```
LICENSE
README.md
example.qmd
_extensions/
  attribution/
    _extension.yml
    attribution.js
    attribution.css
```

Note that the `LICENSE` and `README.md` are standard documentation files and the `example.qmd` is used for development and documentation of the extension. None of those files are actually installed by end users (rather only the contents of the `_extensions` directory is installed).

You can see the full source code of the Quarto version here: <https://github.com/quarto-ext/attribution> (we’ll also walk through the code in detail below).

### Plugin Development

You can develop either entirely new Revealjs plugins from scratch or you can package existing Revealjs extensions as described above.

Here is a list of existing 3rd party plugins for Revealjs that you might consider packaging as Quarto extensions: <https://github.com/hakimel/reveal.js/wiki/Plugins,-Tools-and-Hardware>.

If you want to develop new plugins, check out the Quarto Reveal extensions listed above as well as the code of other 3rd party Reveal Plugins. The following documentation on the Revealjs website provides additional important technical details:

*   [API Methods](https://revealjs.com/api/)
*   [Reveal Events](https://revealjs.com/events/)
*   [Plugin Configuration](https://revealjs.com/creating-plugins/#plugin-options)

Some Revealjs plugins make available various user options. If you are developing a plugin from scratch, you should use a distinct key for your plugin’s configuration. Users can use this key alongside other `revealjs` options. For example the `pointer` extension can be configured as follows:

```yaml
---
title: "Example Presentation"
format:
  revealjs:
    pointer:
      pointerSize: 18
      color: '#32cd32'
revealjs-plugins:
  - pointer
---
```

The extension accesses options using the `deck.getConfig()` function:

```javascript
return {
  id: "pointer",
  init: (deck) => {
    const config = deck.getConfig();
    const options = config.pointer || {};
    // etc
  }
}
```

Note that when packaging an existing Revealjs plugin, you can override its default configuration using the `config` key within your `_extension.yml` file. For example, these are the overrides provided by the `pointer` extension:

```yaml
title: Pointer
author: Charles Teague
contributes:
  revealjs-plugins:
    - name: RevealPointer
      script:
        - pointer.js
      stylesheet:
        - pointer.css
      config:
        pointer:
          key: "q"
          color: "red"
          pointerSize: 16
          alwaysVisible: false
```

### Example: Attribution

Here we’ll walk through the complete source code for the `attribution` extension. This extension enables you to display attribution text sideways along the right edge of Revealjs slides.

Here are source files used to develop the extension:

```
LICENSE
README.md
example.qmd
_extensions/
  attribution/
    _extension.yml
    attribution.js
    attribution.css
```

The `example.qmd` and documentation files are used for development of the extension only (it is not installed by end users). The other files provide extension registration (`_extension.yml`) and the actual implementation of the Revealjs plugin (`attribution.js` and `attribution.css`).

The `example.qmd` is a simple one-slide presentation that includes an image along with a div with class `.attribution`:

**example.qmd**
```yaml
---
title: "Attribution Extension"
format: revealjs
revealjs-plugins:
  - attribution
---

