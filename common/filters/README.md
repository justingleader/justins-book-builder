# Quarto Book Builder Filters

This directory contains Lua filters that can be used across all book projects in the Quarto Book Builder system.

## Available Filters

### openai-image.lua

A filter for generating images using the OpenAI DALL-E API. This filter allows you to:

- Generate images directly within your Quarto documents
- Specify the prompt, size, quality, and style for image generation
- Use inline or block syntax for image generation

Usage in Quarto documents:

```markdown
```{.openai-image}
prompt: "A serene mountain landscape at sunset with a lake reflecting the orange sky"
size: "1024x1024"  # Optional
quality: "standard"  # Optional
style: "vivid"  # Optional
```
```

See the main README for more details on using this filter.

### stack-shortcodes.lua

A filter that provides shortcodes for use with the Stack Intelligence templates. This filter includes:

- Featured Quote shortcode for highlighting important quotes
- Case Study shortcode for showcasing real-world examples
- Listicle shortcode for creating structured lists
- Stats Highlight shortcode for emphasizing key statistics
- Action Plan shortcode for executive action plans
- Quick Tips shortcode for implementation advice

Usage in Quarto documents:

```markdown
{{{< featured-quote color="primaryorange" size="normal" >}}
This is an impactful quote that captures the essence of your message.

Author Name, Position at Company
{{{< /featured-quote >}}
```

See the Stack Intelligence Template documentation for more details on available shortcodes and their options.

## Adding New Filters

To add a new filter:

1. Add the Lua filter file to this directory
2. Document its usage in this README
3. Reference the filter in your `_quarto.yml` file with a relative path:

```yaml
filters:
  - ../../../common/filters/your-filter.lua
```