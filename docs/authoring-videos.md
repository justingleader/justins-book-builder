## Authoring Videos

Source: [Videos – Quarto](https://quarto.org/docs/authoring/videos.html)

### Overview

You can embed videos in documents using the `{{< video >}}` shortcode. For example, here we embed a YouTube video:

```markdown
{{< video https://www.youtube.com/embed/wo9vZccmqwc >}}
```

Videos can refer to video files (e.g. `.mp4`) or can be links to videos published on YouTube, Vimeo, or Brightcove.

Here are some additional examples that demonstrate using various video sources and options:

```markdown
{{< video local-video.mp4 >}}

{{< video https://www.youtube.com/embed/wo9vZccmqwc >}}

{{< video https://vimeo.com/548291297 >}}

{{< video https://youtu.be/wo9vZccmqwc width="400" height="300" >}}

{{< video https://www.youtube.com/embed/wo9vZccmqwc
    title="What is the CERN?"
    start="116"
    aspect-ratio="21x9"
>}}
```

In HTML formats the video will be embedded within the document. For other formats, a simple link to the video will be rendered.

Next, we’ll cover the various options available for video embedding. For additional details on using videos within Revealjs presentations (including how to create slides with full-screen video backgrounds), see the [Revealjs](#revealjs) section below.

### Video URL

The video URL can specify either a path to a video file (e.g. a `.mp4`) alongside the document, a remote URL to a video file, or a URL to a video service (YouTube, Vimeo, or Brightcove).

These are valid URLs for video files:

```markdown
{{< video local-video.mp4 >}}

{{< video https://videos.example.com/video.mp4 >}}
```

For video services, a variety of URL forms are supported. For example, the following video service URLs are all valid:

```markdown
{{< video https://youtu.be/wo9vZccmqwc >}}
{{< video https://www.youtube.com/watch?v=wo9vZccmqwc >}}
{{< video https://www.youtube.com/embed/wo9vZccmqwc >}}

{{< video https://vimeo.com/548291297 >}}

{{< video https://players.brightcove.net/1460825906/default_default/index.html?videoId=5988531335001 >}}
```

Note that YouTube videos support both the URL that is available in the address bar when watching a video as well as the standard URLs used for linking and embedding. Brightcove videos are embedded using the standard [iframe embed code](https://studio.support.brightcove.com/publish/publishing-videos-iframe-embed-code.html).

### Options

#### Aspect Ratio

Videos are automatically rendered responsively using the full width of the document’s main text column. The `aspect-ratio` specifies how the height should vary with changes in width. For example:

```markdown
{{< video https://youtu.be/wo9vZccmqwc aspect-ratio="4x3" >}}
```

Available `aspect ratios` include `1x1`, `4x3`, `16x9` (the default), and `21x9`.

#### Width and Height

You can disable responsive sizing by providing explicit `width` and `height` attributes. For example:

```markdown
{{< video https://youtu.be/wo9vZccmqwc width="250" height="175" >}}
```

This will produce a video that renders at the specified dimensions and is not responsive. Note that when no `height` or `width` are specified, videos will size responsively given the space available to them.

#### Start Time

For YouTube videos, you can specify a `start` option to indicate how many seconds into the video you want to start playing:

```markdown
{{< video https://youtu.be/wo9vZccmqwc start="10" >}}
```

#### Frame Title

The `title` option adds a `title` attribute to the video `<iframe>`:

```markdown
{{< video https://www.youtube.com/embed/wo9vZccmqwc
    title='What is the CERN?'
>}}
```

### Revealjs

You can include videos within [Revealjs](https://quarto.org/docs/presentations/revealjs.html) presentations in one of two ways:

1.  A video that appears within the contents of a slide.
2.  A video that occupies the entire background of a slide.

#### Slide Content

Here’s a video on a slide without a title:

```markdown
---
{{< video https://youtu.be/wo9vZccmqwc width="100%" height="100%" >}}
```

Note that we set the `width` and `height` explicitly to 100% so that the video fills the slide.

Here’s a video on a slide with a title.

```markdown
