-- stack-epub.lua
-- Optimizations for EPUB output format
-- Part of Phase 4: Cross-Format Optimization

-- Function to add CSS classes to divs for EPUB styling
function Div(el)
  -- Process divs with classes that match our custom blocks
  if el.classes:includes("case-study") then
    -- Ensure proper structure for EPUB compatibility
    return el
  end
  
  if el.classes:includes("executive-summary") then
    -- Ensure executive summary structure works in EPUB
    return el
  end
  
  -- Return unchanged for other divs
  return el
end

-- Function to process images for EPUB compatibility
function Image(el)
  -- Ensure images have alt text
  if el.attributes.alt == nil or el.attributes.alt == "" then
    el.attributes.alt = "Figure: " .. (el.caption or "Image")
  end
  
  -- Ensure proper dimensions
  if not el.attributes.width then
    el.attributes.width = "100%"
  end
  
  return el
end

-- Function to process code blocks for better EPUB display
function CodeBlock(el)
  -- Add EPUB-friendly classes to code blocks
  if not el.classes:includes("epub-codeblock") then
    el.classes:insert("epub-codeblock")
  end
  
  return el
end

-- Function to process tables for EPUB compatibility
function Table(el)
  -- Check table complexity and apply appropriate EPUB-friendly styling
  local num_cols = #el.headers
  local num_rows = #el.rows
  
  -- For large tables, add special handling
  if num_cols > 4 or num_rows > 10 then
    -- Add a class to indicate this is a large table
    -- This can be styled appropriately in CSS
    el.attributes["class"] = "large-table epub-table"
  else
    el.attributes["class"] = "epub-table"
  end
  
  return el
end

-- Function to enhance links for EPUB
function Link(el)
  -- Ensure links have titles for better accessibility
  if not el.attributes.title then
    el.attributes.title = el.content[1].text or "Link"
  end
  
  return el
end

-- Function to process the entire document for EPUB optimization
function Pandoc(doc)
  -- Get metadata
  local meta = doc.meta
  
  -- Add EPUB-specific metadata if not present
  if not meta.epub_title_page then
    meta.epub_title_page = true
  end
  
  if not meta.epub_chapter_level then
    meta.epub_chapter_level = 1
  end
  
  doc.meta = meta
  
  return doc
end

return {
  {Div = Div},
  {Image = Image},
  {CodeBlock = CodeBlock},
  {Table = Table},
  {Link = Link},
  {Pandoc = Pandoc}
}