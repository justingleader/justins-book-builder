-- stack-code.lua
-- Enhanced code block processing for Stack Intelligence templates

function CodeBlock(el)
  -- Process only code blocks with title attribute
  if el.attr and el.attr.attributes and el.attr.attributes.title then
    local title = el.attr.attributes.title
    local language = ""
    
    -- Get language if specified in classes
    for _, class in ipairs(el.attr.classes) do
      if class ~= "code-block" then
        language = class
        break
      end
    end
    
    -- Format differently based on output format
    if FORMAT:match 'latex' then
      return pandoc.RawBlock('latex', 
        "\\begin{si-code}[language=" .. language .. "]{" .. title .. "}\n" ..
        el.text ..
        "\n\\end{si-code}")
    elseif FORMAT:match 'html' then
      return pandoc.RawBlock('html',
        "<div class=\"code-with-title\">\n" ..
        "  <div class=\"code-title\">" .. title .. "</div>\n" ..
        "  <pre><code class=\"language-" .. language .. "\">" .. 
        pandoc.utils.escapeHTML(el.text) .. 
        "</code></pre>\n" ..
        "</div>")
    end
  end
  
  -- Also process fenced divs with code-block class
  if el.attr and el.attr.classes and pandoc.List.includes(el.attr.classes, "code-block") then
    local title = el.attr.attributes.title or "Code"
    local language = el.attr.attributes.language or ""
    
    -- Format differently based on output format
    if FORMAT:match 'latex' then
      return pandoc.RawBlock('latex', 
        "\\begin{si-code}[language=" .. language .. "]{" .. title .. "}\n" ..
        el.text ..
        "\n\\end{si-code}")
    elseif FORMAT:match 'html' then
      return pandoc.RawBlock('html',
        "<div class=\"code-with-title\">\n" ..
        "  <div class=\"code-title\">" .. title .. "</div>\n" ..
        "  <pre><code class=\"language-" .. language .. "\">" .. 
        pandoc.utils.escapeHTML(el.text) .. 
        "</code></pre>\n" ..
        "</div>")
    end
  end
  
  return el
end

function Div(el)
  -- Process divs with code-block class
  if el.classes:includes("code-block") then
    local title = el.attributes.title or "Code"
    local language = el.attributes.language or ""
    local code_text = ""
    
    -- Extract code from the div content
    for _, block in ipairs(el.content) do
      if block.t == "CodeBlock" then
        code_text = block.text
        break
      end
    end
    
    -- If no code block found, try to extract from Plain or Para blocks
    if code_text == "" then
      for _, block in ipairs(el.content) do
        if block.t == "Para" or block.t == "Plain" then
          code_text = pandoc.utils.stringify(block)
          break
        end
      end
    end
    
    -- Format differently based on output format
    if FORMAT:match 'latex' then
      return pandoc.RawBlock('latex', 
        "\\begin{si-code}[language=" .. language .. "]{" .. title .. "}\n" ..
        code_text ..
        "\n\\end{si-code}")
    elseif FORMAT:match 'html' then
      return pandoc.RawBlock('html',
        "<div class=\"code-with-title\">\n" ..
        "  <div class=\"code-title\">" .. title .. "</div>\n" ..
        "  <pre><code class=\"language-" .. language .. "\">" .. 
        pandoc.utils.escapeHTML(code_text) .. 
        "</code></pre>\n" ..
        "</div>")
    end
  end
  
  return el
end

return {
  {CodeBlock = CodeBlock},
  {Div = Div}
}