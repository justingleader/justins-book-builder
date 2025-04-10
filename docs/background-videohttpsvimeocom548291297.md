## {background-video="https://vimeo.com/548291297"}
```

Note that when using `background-video` for video files (as distinct from services like YouTube) you can specify a number of other attributes, including:

| Attribute                | Default   | Description                                                                                                                               |
| :----------------------- | :-------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| `background-video`       |           | A single video source, or a comma separated list of video sources.                                                                        |
| `background-video-loop`  | `false`   | Flags if the video should play repeatedly.                                                                                                |
| `background-video-muted` | `false`   | Flags if the audio should be muted.                                                                                                       |
| `background-size`        | `cover`   | Use `cover` for full screen and some cropping or `contain` for letterboxing.                                                              |
| `background-opacity`     | `1`       | Opacity of the background video on a 0-1 scale. 0 is transparent and 1 is fully opaque.                                                   |

For example:

```markdown
