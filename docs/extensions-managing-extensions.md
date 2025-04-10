## Extensions: Managing Extensions

Source: [Managing Extensions – Quarto](https://quarto.org/docs/extensions/managing.html)

### Installation

If you want to use an extension within a document or project you need to add it to a project or directory. Rather than installing into a global library, Quarto extensions are stored locally, directly alongside the document or project they are used within. For example, if you have a project in a directory named `myblog`, you could add some extensions for use with that the project as follows:

```bash
cd myblog
quarto add quarto-ext/fontawesome
quarto add quarto-ext/video
```

This will result in an `_extensions` folder being created at the root of your project, and the `fontawesome` and `video` extensions being placed within it.

Note that a project isn’t strictly required for using extensions—if you add extensions in a directory that isn’t a project then any document located directly alongside the `_extensions` folder can use the extensions.

**Extension Trust:** Quarto extensions may execute code when documents are rendered. Therefore, if you do not trust the author of an extension, we recommend that you do not install or use the extension.

### Version Control

If you are using version control you should check the `_extensions` directory in to your repo along with your other code. Extensions used by a document or project are treated as source code to ensure very long term reproducibility—your project doesn’t need to rely on the availability of an external package manager (or the maintenance of older extension versions) to successfully render now and far into the future.

### Repositories

The extensions in the example above were prefixed with `quarto-ext` because they were distributed from the `quarto-ext` GitHub organization. Extensions can be similarly distributed from *any* GitHub organization. So for example the following might also be valid command to add extensions to a project:

```bash
quarto add cooltools/lightbox
quarto add bigstateu/fancytweet
```

While it’s convenient to distribute extensions using GitHub, you can also bundle them into a `.zip` or `.tar.gz` archive and distribute them using a URL or a local file. See the article on [Distributing Extensions](https://quarto.org/docs/extensions/distributing.html) for additional details.

### Updating

You can list and update configured extensions for a given project with the following commands:

```bash
quarto list extensions
quarto update quarto-ext/fontawesome
```

Note that when updating an extension you’ll be prompted to confirm the update based on the version you have and the version you are attempting to update to.

### Removing

Use this command to remove an extension from a project:

```bash
quarto remove quarto-ext/fontawesome
```

If you run the `quarto remove extension` command with no `extension-id`, you will be presented with a list of extensions that are present and you may select which extensions to remove.

