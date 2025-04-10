-- stack-pdf-optimize.lua
-- PDF optimization for Stack Intelligence templates
-- Part of Phase 4: Cross-Format Optimization

-- Helper function to check if an element has a specific class
local function has_class(el, class)
  if el.attr and el.attr.classes then
    for _, cls in ipairs(el.attr.classes) do
      if cls == class then
        return true
      end
    end
  end
  return false
end

-- Function to optimize tables for PDF output
function Table(el)
  -- Add longtable environment for tables that span multiple pages
  if #el.rows > 15 then
    el.attributes["longtable"] = "true"
  end
  
  -- Handle wide tables
  if #el.headers > 5 then
    el.attributes["table-width"] = "100%"
    el.attributes["fontsize"] = "small"
  end
  
  return el
end

-- Function to optimize images for PDF output
function Image(el)
  -- Handle image sizing for PDF
  if not el.attributes.width and not el.attributes.height then
    -- Default width if none specified
    el.attributes.width = "80%"
  end
  
  -- Ensure high-resolution for print
  if el.attributes.dpi then
    -- If DPI is specified, ensure it's high enough for print
    local dpi = tonumber(el.attributes.dpi)
    if dpi and dpi < 300 then
      el.attributes.dpi = "300"
    end
  else
    -- Default to 300 DPI for print
    el.attributes.dpi = "300"
  end
  
  return el
end

-- Function to handle code blocks in PDF
function CodeBlock(el)
  -- Add line numbers for longer code blocks
  if #el.text:gmatch("(\n)") > 10 then
    table.insert(el.classes, "numberLines")
  end
  
  -- For very long lines, enable line breaking
  if el.text:find("[^\n][^\n][^\n][^\n][^\n][^\n][^\n][^\n][^\n][^\n][^\n][^\n][^\n][^\n][^\n][^\n][^\n][^\n][^\n][^\n]") then
    table.insert(el.classes, "breaklines")
  end
  
  return el
end

-- Function to add PDF-specific formatting to certain elements
function Div(el)
  -- Case study handling
  if has_class(el, "case-study") then
    -- Ensure case studies don't break across pages in PDF
    el.attributes["breakable"] = "false"
    return el
  end
  
  -- Featured quote handling
  if has_class(el, "featured-quote") then
    -- Ensure quotes don't break across pages
    el.attributes["breakable"] = "false"
    return el
  end
  
  -- Executive summary handling
  if has_class(el, "executive-summary") then
    -- Add special PDF styling
    return el
  end
  
  return el
end

-- Handle list items in PDF
function BulletList(el)
  -- Add bullet customization for PDF
  return el
end

function OrderedList(el)
  -- Add numbering customization for PDF
  return el
end

-- Process the entire document
function Pandoc(doc)
  -- First check if we're targeting PDF/LaTeX
  if not FORMAT:match('latex') and not FORMAT:match('pdf') then
    return doc
  end
  
  -- Add PDF-specific metadata if needed
  local meta = doc.meta
  
  -- Set default PDF options if not already set
  if not meta.colorlinks then
    meta.colorlinks = true
  end
  
  if not meta.linkcolor then
    meta.linkcolor = "primaryblue"
  end
  
  if not meta.urlcolor then
    meta.urlcolor = "primaryblue"
  end
  
  -- Add header/footer information if not present
  if not meta.pagestyle then
    meta.pagestyle = "fancy"
  end
  
  doc.meta = meta
  
  return doc
end

return {
  {Table = Table},
  {Image = Image},
  {CodeBlock = CodeBlock},
  {Div = Div},
  {BulletList = BulletList},
  {OrderedList = OrderedList},
  {Pandoc = Pandoc}
}