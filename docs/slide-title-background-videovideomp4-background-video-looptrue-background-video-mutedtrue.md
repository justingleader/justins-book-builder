## Slide Title {background-video="video.mp4" background-video-loop="true" background-video-muted="true"}
```

This slides's background video will play in a loop with audio muted.

### Cross-References

To add a cross-reference to a video, use the [cross-reference div syntax](https://quarto.org/docs/authoring/cross-references-divs.html) and treat it like a figure. For example,

```markdown
::: {#fig-cern}
{{< video https://www.youtube.com/embed/wo9vZccmqwc >}}

The video "CERN: The Journey of Discovery"
:::

In @fig-cern...
```

Which renders as:

> [Video: CERN: The Journey of Discovery](https://www.youtube.com/embed/wo9vZccmqwc)
>
> Figure 7: The video "CERN: The Journey of Discovery"
>
> In Figure 7...

If you would rather give videos a label and counter distinct from figures, consider defining [Custom Cross-Reference Types](https://quarto.org/docs/authoring/cross-references-custom.html).

