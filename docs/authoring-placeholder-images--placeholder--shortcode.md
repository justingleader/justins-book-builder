## Authoring Placeholder Images (`{{< placeholder >}}` Shortcode)

Source: [Adding Placeholder Images to Your Documents – Quarto](https://quarto.org/docs/authoring/placeholder.html)

### Adding Placeholder Images to Your Documents

#### Overview

The `{{< placeholder >}}` shortcode generates a placeholder image, which is incredibly useful when you’re designing your document or website layout but the final images aren’t ready yet. It helps maintain the design integrity without interrupting the development flow. Placeholder images can have configurable sizes and will be generated in either PNG or SVG format.

#### Example

Here’s an example of a placeholder image:

![Default Placeholder Image](https://quarto.org/docs/authoring/placeholder_files/figure-html/cell-2-output-1.png){fig-alt="A 100x100 pixel placeholder image."}

By default, the `placeholder` shortcode creates 100x100 pixel images in the PNG format. You can customize the size and format of the image by providing parameters to the shortcode.

#### Usage

The `placeholder` shortcode can take additional arguments controling the size and format of the image:

```markdown
{{< placeholder 400 200 format=svg >}}
```

![Custom Placeholder Image](https://quarto.org/docs/authoring/placeholder_files/figure-html/cell-3-output-1.png){fig-alt="A 400x200 pixel SVG placeholder image."}

This will create a scalable vector graphic (SVG) placeholder image with dimensions of 400x200 pixels.

It also takes an optional `format` keyword argument.

*   `{{< placeholder >}}`: Create a 100x100 pixel PNG placeholder image.
*   `{{< placeholder width >}}`: Create a `width`x`width` pixel PNG placeholder image.
*   `{{< placeholder width height >}}`: Create a `width`x`height` pixel PNG placeholder image.
*   `{{< placeholder format="svg" >}}`: Create a 100x100 SVG placeholder image.
*   `{{< placeholder width format="svg" >}}`: Create a `width`x`width` SVG placeholder image.
*   `{{< placeholder width height format="svg" >}}`: Create a `width`x`height` SVG placeholder image.

