-- stack-figures.lua
-- Enhanced figure processing for Stack Intelligence templates

-- Helper function to get the image path with the correct extension
function get_image_path(src)
  if FORMAT:match "latex" then
    -- For latex, prioritize PDF versions if available
    return src:gsub("%.png$", ".pdf"):gsub("%.jpg$", ".pdf"):gsub("%.jpeg$", ".pdf")
  else
    return src
  end
end

-- Process figures with custom attributes
function Image(el)
  -- Only process figures with specific attributes
  if el.attributes.caption or el.attributes.description or el.attributes.credit then
    local src = get_image_path(el.src)
    local caption = el.attributes.caption or ""
    local description = el.attributes.description or ""
    local credit = el.attributes.credit or ""
    
    -- For LaTeX output
    if FORMAT:match 'latex' then
      -- Create a figure environment with the custom styling
      local latex = [[
\begin{si-figure}{]] .. src .. [[}{]] .. caption .. [[}{]] .. description .. [[}{]] .. credit .. [[}
\end{si-figure}
]]
      return pandoc.RawInline('latex', latex)
    
    -- For HTML output
    elseif FORMAT:match 'html' then
      -- Create an HTML figure with the custom styling
      local html = [[
<figure class="si-figure">
  <img src="]] .. src .. [[" alt="]] .. description .. [[">
  <figcaption>]] .. caption .. 
        (credit ~= "" and [[ <span class="credit">Credit: ]] .. credit .. [[</span>]] or "") .. 
        [[</figcaption>]] ..
        (description ~= "" and [[<p class="description"><em>]] .. description .. [[</em></p>]] or "") .. 
        [[
</figure>
]]
      return pandoc.RawInline('html', html)
    end
  end
  
  -- Return unmodified for other formats or if missing required attributes
  return el
end

-- Process fenced divs with figure class
function Div(el)
  if el.classes:includes("figure") then
    local src = el.attributes.src or ""
    local caption = el.attributes.caption or ""
    local description = el.attributes.description or ""
    local credit = el.attributes.credit or ""
    
    src = get_image_path(src)
    
    -- For LaTeX output
    if FORMAT:match 'latex' then
      return pandoc.RawBlock('latex', [[
\begin{si-figure}{]] .. src .. [[}{]] .. caption .. [[}{]] .. description .. [[}{]] .. credit .. [[}
\end{si-figure}
]])
    
    -- For HTML output
    elseif FORMAT:match 'html' then
      return pandoc.RawBlock('html', [[
<figure class="si-figure">
  <img src="]] .. src .. [[" alt="]] .. description .. [[">
  <figcaption>]] .. caption .. 
        (credit ~= "" and [[ <span class="credit">Credit: ]] .. credit .. [[</span>]] or "") .. 
        [[</figcaption>]] ..
        (description ~= "" and [[<p class="description"><em>]] .. description .. [[</em></p>]] or "") .. 
        [[
</figure>
]])
    end
  end
  
  return el
end

return {
  {Image = Image},
  {Div = Div}
}