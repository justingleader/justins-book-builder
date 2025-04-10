## Polar Axis

For a demonstration of a line plot on a polar axis, see @fig-polar.

```{python}
#| label: fig-polar
#| fig-cap: "A line plot on a polar axis"

import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
fig, ax = plt.subplots(
  subplot_kw = {'projection': 'polar'}
)
ax.plot(theta, r);
ax.set_rticks([0.5, 1, 1.5, 2]);
ax.grid(True);

plt.show()
```

To render and preview, execute the `QuartoPreview` command by pressing `:` to enter command mode and typing the command (there is autocompletion if you press the `tab` key). In the kickstarter configuration, there are more shortcuts starting with `space q` (spacebar followed by q, in normal mode).

**How it Works:** When you render a `.qmd` file with Quarto, the executable code blocks are processed by Jupyter, and the resulting combination of code, markdown, and output is converted to plain markdown. Then, this markdown is processed by [Pandoc](https://pandoc.org), which creates the finished format.

### Authoring

Let’s try making a small change and then re-rendering:

1.  Change the line of code that defines `theta` as follows:
    ```python
    theta = 4 * np.pi * r
    ```
2.  Save the file using either `:w` in normal mode or `ctrl-s`[^9]

The document is rendered, and the browser preview is updated. This is the basic workflow for authoring with Quarto.

### Running Cells

You don’t need to fully render documents in order to iterate on code cells. With the provided configuration we can open a terminal of our choosing using the leader key (`<space>`) followed by `c` (for code) and then `p` (for python) or `i` (for ipython).

If you wait a little in between the key presses a small window pops up at the bottom of your screen to tell you about existing keybindings:

![Neovim Keybinding Helper](https://quarto.org/docs/get-started/images/neovim-whichkey.png)

We can navigate between the code and the terminal using `ctrl` plus vim direction keys and enter commands into the python REPL by going into insert mode in this terminal buffer.

To send code to the python REPL from quarto we navigate to one of our code blocks and press `<space><cr>` (space bar followed by Enter). The plugin responsible for sending code to various places, [`vim-slime`](https://github.com/jpalardy/vim-slime) will prompt us with the question which terminal to send the code to, pre filled with the latest terminal we created.

If you want to use `ctrl+Enter` to send code just like in RStudio, you are going to have to tell your terminal emulator to send the correct key codes. For example, in the `kitty` terminal the configuration looks as follows:

```
map ctrl+shift+enter no_op
map shift+enter send_text all \x1b[13;2u
map ctrl+enter send_text all \x1b[13;5u
```

This is what the kickstarter configuration has been tested with.

There are few different types of content in `hello.qmd`, let’s work a bit with each type.

#### YAML Options

At the top of the file there is a YAML block with document level options.

```yaml
---
title: "Quarto Basics"
format:
  html:
    code-fold: true
jupyter: python3
---
```

Try changing the `code-fold` option to `false`:

```yaml
format:
  html:
    code-fold: false
```

Then re-render the document by saving it. You’ll notice that the code is now shown above the plot, where previously it was hidden with a `Code` button that could be used to show it.

#### Markdown

Narrative content is written using markdown. Here we specify a heading and a cross-reference to the figure created in the code cell below.

```markdown
