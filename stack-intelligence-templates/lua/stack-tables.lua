-- stack-tables.lua
-- Enhanced table processing for Stack Intelligence templates

function enhance_html_table(el)
  -- Add custom class to table
  table.insert(el.classes, "si-table")
  
  -- Process header row if present
  if el.head and el.head.rows and #el.head.rows > 0 then
    for i, row in ipairs(el.head.rows) do
      for j, cell in ipairs(row.cells) do
        -- Add header styling class to cell
        if not cell.attr then
          cell.attr = pandoc.Attr()
        end
        table.insert(cell.attr.classes, "si-header")
      end
    end
  else
    -- If there's no header but there are rows, use the first row as header
    if el.bodies and #el.bodies > 0 and el.bodies[1].rows and #el.bodies[1].rows > 0 then
      -- Create a new header
      el.head = {
        attr = pandoc.Attr(),
        rows = { el.bodies[1].rows[1] }
      }
      
      -- Add styling to the header cells
      for j, cell in ipairs(el.head.rows[1].cells) do
        if not cell.attr then
          cell.attr = pandoc.Attr()
        end
        table.insert(cell.attr.classes, "si-header")
      end
      
      -- Remove the first row from body
      table.remove(el.bodies[1].rows, 1)
    end
  end
  
  -- Add alternating row classes for better readability
  if el.bodies then
    for i, body in ipairs(el.bodies) do
      if body.rows then
        for j, row in ipairs(body.rows) do
          if not row.attr then
            row.attr = pandoc.Attr()
          end
          
          if j % 2 == 0 then
            table.insert(row.attr.classes, "even-row")
          else
            table.insert(row.attr.classes, "odd-row")
          end
        end
      end
    end
  end
  
  return el
end

function enhance_latex_table(el)
  -- Get caption if it exists
  local caption = ""
  if el.caption and el.caption.long then
    caption = pandoc.utils.stringify(el.caption.long)
  end
  
  -- Get the table contents as string (can't easily manipulate within Lua)
  local content = pandoc.utils.stringify(el)
  
  -- Create a custom LaTeX table environment
  -- This is a simplified approach; a more comprehensive one would parse the table structure
  local latex = [[
\begin{si-table}{]] .. caption .. [[}{tbl:]] .. pandoc.sha1(content) .. [[}
]] .. content .. [[
\end{si-table}
]]

  return pandoc.RawBlock("latex", latex)
end

function Table(el)
  -- For HTML output
  if FORMAT:match 'html' then
    return enhance_html_table(el)
  -- For LaTeX output (this is tricky with raw pandoc tables)
  elseif FORMAT:match 'latex' then
    -- The simple approach just adds a class, the LaTeX template handles styling
    table.insert(el.classes, "si-table")
    -- A more complex approach would be to convert to a raw LaTeX table
    -- return enhance_latex_table(el)
  end
  
  return el
end

return {
  {Table = Table}
}