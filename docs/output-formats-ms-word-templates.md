## Output Formats: MS Word Templates

Source: [Word Templates – Quarto](https://quarto.org/docs/output-formats/ms-word-templates.html)

### Using Templates

If you want to customize the appearance of MS Word output, Pandoc supports a special type of template called a *reference document*. Here’s an example of specifying a custom reference document for `docx`:

```yaml
format:
  docx:
    reference-doc: custom-reference-doc.docx
```

Reference documents include sample text that uses all of the output styles used by Pandoc.

To use a reference doc template, just copy it to your document’s directory and reference it as shown above.

### Creating Templates

To create a new reference doc based on the Pandoc default, execute the following command:

```bash
quarto pandoc -o custom-reference-doc.docx \
   --print-default-data-file reference.docx
```

Then, open `custom-reference-doc.docx` in MS Word and modify styles as you wish:

![Modifying Styles in Word](https://quarto.org/docs/output-formats/images/word-styles.png)

You can open the Styles pane from the HOME tab in the MS Word toolbar.

When you move the cursor to a specific element in the document, an item in the styles list will be highlighted. If you want to modify the style of any type of element, you can click the drop-down menu on the highlighted item, and you will see a dialog box like this:

![Word Style Dialog](https://quarto.org/docs/output-formats/images/word-modify-style.png)

After you finish modifying the styles, you can save the document and use it as the template for future Word documents.

### Applying Custom Styles

Pandoc provides default styles for elements like paragraphs or code blocks and default formatting for inline elements like bold. Custom styles can be defined using divs for blocks and spans for text, so a specific style is used instead of the default.

Set the `custom-style` attribute with the name of the style defined in the default or user-provided reference document.

For example, this applies a text style called `Emphasis` to the `Get out` text instead of the default style for text:

```markdown
[Get out]{custom-style="Emphasis"}, he said.
```

This will apply the paragraph style called `Poetry` to the content inside the Div (`:::`):

```markdown
Dickinson starts the poem simply:

::: {custom-style="Poetry"}
| A Bird came down the Walk---
| He did not know I saw---
:::
```

If the `reference.docx` file does not already contain the styles, they will be added to the output file with standard text as their base style. If the styles are already defined, their definitions will not be modified.

A possible workflow could be:

1.  Create a document setting `custom-style` for all the styles you need,
2.  Render this document so that the styles are created in the output document,
3.  Save this document as a reference document for future rendering

This ensures that the names of the styles used in `custom-style` exactly match the names of the styles defined in the reference document.

Overall, this mechanism allows for great customization by allowing authors to define new styles in the reference document. For advanced users, this could be coupled with [filters](https://quarto.org/docs/extensions/filters.html) to apply a `custom-style` attribute to a filtered set of elements in the document.

