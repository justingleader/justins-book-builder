## Polar Axis

For a demonstration of a line plot on a polar axis, see @fig-polar.
```

Try changing the heading and saving the notebook—the preview will update with the new heading text.

#### Code Cells

You are likely already familiar with code cells, like the one shown below.

![Code Cell](https://quarto.org/docs/get-started/images/jupyterlab-code-cell.png)

```python
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

But there are some new components at the top of the code cell: `label` and `fig-cap` options. Cell options are written in YAML using a specially prefixed comment (`#|`).

In this example, the cell options are used to make the figure cross-reference-able. Try changing the `fig-cap` and/or the code, running the cell, and then saving the notebook to see the updated preview.

There are a wide variety of [cell options](https://quarto.org/docs/reference/cells/cells-jupyter.html) that you can apply to tailor your output. We’ll delve into these options in the next tutorial.

**Note:** One particularly useful cell option for figures is `fig-alt`, which enables you to add alternative text to images for users with visual impairments. See Amy Cesal’s article on [Writing Alt Text for Data Visualization](https://medium.com/nightingale/writing-alt-text-for-data-visualization-2a218ef43f81) to learn more.

### Next Up

You now know the basics of creating and authoring Quarto documents. The following tutorials explore Quarto in more depth:

*   [Tutorial: Computations](https://quarto.org/docs/get-started/computations/) — Learn how to tailor the behavior and output of executable code blocks.
*   [Tutorial: Authoring](https://quarto.org/docs/get-started/authoring/) — Learn more about output formats and technical writing features like citations, crossrefs, and advanced layout.

Additionally, you may want to install the [Quarto JupyterLab Extension](https://quarto.org/docs/tools/jupyter-lab-extension.html) which provides additional tools for working with Quarto in JupyterLab.

