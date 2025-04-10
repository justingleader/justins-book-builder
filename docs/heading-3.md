## Heading

Some text below
```

**filter.lua**
```lua
function Header(el)
  el.content = {pandoc.Emph(el.content)}
  return el
end
```

**Output:**
```
Pandoc
  Meta
    { unMeta = fromList [] }
  [ Header
      2
      ( “heading” , [] , [] )
      [ Emph [ Str “Heading” ]
      ]
  , Para
      [ Str “Some”
      , Space
      , Str “text”
      , Space
      , Str “below”
      ]
  ]
```

#### Lua in VS Code {#lua-in-vs-code}

##### Type Hints

While Quarto provides type information for the Pandoc and Quarto Lua APIs, this doesn’t cover functions that you write within your own extensions. You can however add type information using [Annotations](https://github.com/LuaLS/lua-language-server/wiki/Annotations). For example, here we indicate that a function takes a `string` and a `pandoc.List()` and returns either a `pandoc.List()` or `nil`:

```lua
---@param text string
---@param blocks pandoc.List
---@return pandoc.List|nil
function check_for_text(text, blocks)
  -- implementation
end
```

With these type declarations, any attempt to call the function without the correct types will result in a diagnostic message. Further, if a caller fails to check for `nil` before using the return value a diagnostic will also occur.

You can learn more about all of the available type annotations in the [Annotations Reference](https://github.com/LuaLS/lua-language-server/wiki/Annotations) for the Lua Language Server.

##### Settings

The [Lua Language Server](https://marketplace.visualstudio.com/items?itemName=sumneko.lua) extension includes a wide variety of options to customize its behavior (e.g. what diagnostics to show, which completions to offer, etc.).

All of the available options are documented in the [Settings Reference](https://github.com/LuaLS/lua-language-server/wiki/Settings) for the Lua Language Server.

Quarto provides a default configuration file (`.luarc.json`) within the root of any workspace that includes Quarto Lua extensions. This file is necessary because it provides a reference to the Lua type definitions for Pandoc and Quarto within your currently installed version of Quarto. Without it, the Lua extension wouldn’t know anything about Quarto and would report errors for “unknown” Pandoc modules.

If, for example, Quarto is installed at `/opt/quarto/`, the default contents of the configuration file will be:

**.luarc.json**
```json
{
  "Generator": [
    "Quarto"
  ],
  "Lua.runtime.version": "Lua 5.3",
  "Lua.workspace.checkThirdParty": false,
  "Lua.workspace.library": [
    "/opt/quarto/share/lua-types"
  ],
  "Lua.runtime.plugin": "/opt/quarto/share/lua-plugin/plugin.lua",
  "Lua.completion.showWord": "Disable",
  "Lua.completion.keywordSnippet": "Both",
  "Lua.diagnostics.disable": [
    "lowercase-global",
    "trailing-space"
  ]
}
```

The `.luarc.json` file will also be automatically added to `.gitignore` since it points to the absolute path of Quarto on the local system.

You can change any of the settings within this file save for the `Lua.workspace.library` and `Lua.runtime.plugin` (these are automatically maintained by the Quarto extension based on where Quarto is installed). See the [Settings Reference](https://github.com/LuaLS/lua-language-server/wiki/Settings) for all available settings.

If you prefer to manage this file manually, simply remove the `Generator` key and Quarto will no longer update the `Lua.workspace.library` and `Lua.runtime.plugin` settings automatically.

You can also globally disable the automatic creation of `.luarc.json` using the `Quarto > Lua: Provide Types` VS Code setting.

