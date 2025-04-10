## Polar Axis

For a demonstration of a line plot on a polar axis, see @fig-polar.
```

Try changing the heading and re-rendering—the preview will update with the new heading text.

#### Code Cells

Code cells contain executable code to be run during render, with the output (and optionally the code) included in the rendered document.

````markdown
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
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()
```
````

You are likely familiar with the Matplotlib code given here. However, there are some less familiar components at the top of the code cell: `label` and `fig-cap` options. Cell options are written in YAML using a specially prefixed comment (`#|`).

In this example, the cell options are used to make the figure cross-reference-able. Try changing the `fig-cap` and/or the code then re-rendering to see the updated preview.

There are a wide variety of [cell options](https://quarto.org/docs/reference/cells/cells-jupyter.html) that you can apply to tailor your output. We’ll delve into these options in the next tutorial.

**Note:** One particularly useful cell option for figures is `fig-alt`, which enables you to add alternative text to images for users with visual impairments. See Amy Cesal’s article on [Writing Alt Text for Data Visualization](https://medium.com/nightingale/writing-alt-text-for-data-visualization-2a218ef43f81) to learn more.

### Next Up

You now know the basics of creating and authoring Quarto documents. The following tutorials explore Quarto in more depth:

*   [Tutorial: Computations](https://quarto.org/docs/get-started/computations/) — Learn how to tailor the behavior and output of executable code blocks.
*   [Tutorial: Authoring](https://quarto.org/docs/get-started/authoring/) — Learn more about output formats and technical writing features like citations, crossrefs, and advanced layout.

See the article on [Using Neovim with Quarto](https://quarto.org/docs/tools/neovim.html) to learn more about installing, using, and customizing Neovim for Quarto.

#### Footnotes

[^8]: In [this video](https://www.youtube.com/watch?v=nZMZ-kA8iEg)
[^9]: if you are using the kickstarter configuration – otherwise `ctrl-s` puts your terminal in a waiting mode until you press `ctrl+q`, which can be confusing

