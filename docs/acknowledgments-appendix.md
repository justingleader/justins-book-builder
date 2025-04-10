## Acknowledgments {.appendix}

I am grateful for the insightful comments offered by the anonymous peer reviewers at Books & Texts. The generosity and expertise of one and all have improved this study in innumerable ways and saved me from many errors; those that inevitably remain are entirely my own responsibility.
```

Any sections marked with the `.appendix` class will be included at the front of the appendix in the order in which they appear in the document. A more complete example appendix including attribution and the above custom appendix section looks like:

![Appendix with Attribution and Custom Section](https://quarto.org/docs/authoring/images/appendix-with-attrib.png)

### License

If you include a license in the front matter or citation information for your document, a ‘Reuse’ section will automatically be added to the appendix. Read more about specifying a license in [Front Matter](https://quarto.org/docs/authoring/front-matter.html#license).

Here is an example of a complete appendix including all the fields with an Attribution-ShareAlike Creative Commons license.

![Complete Appendix Example](https://quarto.org/docs/authoring/images/appendix-complete.png)

### Appendix Style

You can control how Quarto process the appendix of your document using the `appendix-style` option. There are three options available:

*   `default`: The default appendix treatment create a smaller font face and gathers the various sections into stylized groups at the end of the document.
*   `plain`: The plain treatment will do all the appendix processing (gathering and organizing the sections at the end of the document, creating sections like ‘Reuse’), but will not apply the default appendix styling.
*   `none`: `none` disables appendix processing altogether. Content will not be processed or organized and information like ‘Citation’ and ‘Reuse’ will not be included in the document.

