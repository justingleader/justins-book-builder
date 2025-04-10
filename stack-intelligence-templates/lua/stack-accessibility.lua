-- stack-accessibility.lua
-- Accessibility enhancements for Stack Intelligence templates
-- Part of Phase 4: Cross-Format Optimization

-- Function to add alt text to images if missing
function Image(el)
  -- Check if image has alt text
  if not el.attributes.alt or el.attributes.alt == "" then
    -- Generate alt text from caption or title
    if el.caption and pandoc.utils.stringify(el.caption) ~= "" then
      el.attributes.alt = pandoc.utils.stringify(el.caption)
    elseif el.title and el.title ~= "" then
      el.attributes.alt = el.title
    else
      -- Use filename as last resort
      local filename = el.src:match("([^/]+)$") or "image"
      el.attributes.alt = "Image: " .. filename
    end
  end
  
  return el
end

-- Function to enhance table accessibility
function Table(el)
  -- Ensure tables have appropriate attributes for screen readers
  if FORMAT:match 'html' then
    el.attributes["role"] = "table"
    
    -- Add caption if available but not explicitly set
    if el.caption and not el.attributes["aria-label"] then
      el.attributes["aria-label"] = pandoc.utils.stringify(el.caption)
    end
  end
  
  return el
end

-- Function to enhance link accessibility
function Link(el)
  -- Ensure links have title attributes for better accessibility hints
  if FORMAT:match 'html' and not el.attributes.title and el.content then
    el.attributes.title = pandoc.utils.stringify(el.content)
  end
  
  -- Add visual indication for external links in HTML
  if FORMAT:match 'html' and el.target:match('^https?://') then
    -- Add class for external links that can be styled in CSS
    if not el.attributes.class then
      el.attributes.class = "external-link"
    else
      el.attributes.class = el.attributes.class .. " external-link"
    end
    
    -- Add aria attribute for screen readers
    el.attributes["aria-label"] = pandoc.utils.stringify(el.content) .. " (external link)"
  end
  
  return el
end

-- Function to enhance code block accessibility
function CodeBlock(el)
  -- Add appropriate ARIA roles for screen readers in HTML
  if FORMAT:match 'html' then
    el.attributes["role"] = "code"
    
    -- Add language information for screen readers if available
    if el.classes and #el.classes > 0 then
      local lang = el.classes[1]
      if lang ~= "sourceCode" then
        el.attributes["aria-label"] = "Code block in " .. lang
      else
        el.attributes["aria-label"] = "Code block"
      end
    end
  end
  
  return el
end

-- Function to enhance div elements for accessibility
function Div(el)
  -- Add appropriate ARIA roles for different block types
  if FORMAT:match 'html' then
    if el.classes:includes("featured-quote") then
      el.attributes["role"] = "blockquote"
    elseif el.classes:includes("case-study") then
      el.attributes["role"] = "region"
      if not el.attributes["aria-label"] then
        el.attributes["aria-label"] = "Case Study"
      end
    elseif el.classes:includes("listicle") then
      el.attributes["role"] = "list"
    elseif el.classes:includes("callout") or 
           el.classes:includes("action-plan") or 
           el.classes:includes("stats-highlight") or 
           el.classes:includes("quick-tips") then
      el.attributes["role"] = "note"
    end
  end
  
  return el
end

-- Function to add accessibility information to the entire document
function Pandoc(doc)
  -- Only apply to HTML output
  if not FORMAT:match 'html' then
    return doc
  end
  
  -- Get metadata
  local meta = doc.meta
  
  -- Add language metadata if not present
  if not meta.lang then
    meta.lang = "en"
  end
  
  -- Add other accessibility metadata
  if not meta["aria-describedby"] and meta.abstract then
    meta["aria-describedby"] = "abstract"
  end
  
  doc.meta = meta
  
  return doc
end

return {
  {Image = Image},
  {Table = Table},
  {Link = Link},
  {CodeBlock = CodeBlock},
  {Div = Div},
  {Pandoc = Pandoc}
}