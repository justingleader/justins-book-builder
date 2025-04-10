-- stack-blocks.lua
-- Content block processing for Stack Intelligence templates

-- Process divs with custom classes
function Div(el)
  -- Process divs with classes that match our custom blocks
  if el.classes:includes("case-study") then
    -- Extract metadata from attributes
    local company = el.attributes["company"] or "Company Name"
    local segment = el.attributes["segment"] or "Industry Segment"
    local revenue = el.attributes["revenue"] or "Annual Revenue"
    local challenge = el.attributes["challenge"] or "Business Challenge"
    local outcome = el.attributes["outcome"] or "Strategic Outcome"
    
    -- Format based on output
    if FORMAT:match 'latex' then
      -- Create LaTeX environment for case study
      local latex_begin = "\\begin{case-study}{" .. company .. "}{" .. 
                         segment .. "}{" .. revenue .. "}{" .. 
                         challenge .. "}{" .. outcome .. "}"
      local latex_end = "\\end{case-study}"
      
      -- Add LaTeX tags around original content
      table.insert(el.content, 1, pandoc.RawBlock("latex", latex_begin))
      table.insert(el.content, pandoc.RawBlock("latex", latex_end))
      return el
    elseif FORMAT:match 'html' then
      -- Create HTML structure for case study
      local html_begin = "<div class=\"case-study\">" ..
                        "<h3 class=\"case-study-title\">Industry Success Story: " .. company .. "</h3>" ..
                        "<dl class=\"case-study-meta\">" ..
                        "<dt>Industry Segment:</dt><dd>" .. segment .. "</dd>" ..
                        "<dt>Annual Revenue:</dt><dd>" .. revenue .. "</dd>" ..
                        "<dt>Business Challenge:</dt><dd>" .. challenge .. "</dd>" ..
                        "<dt>Strategic Outcome:</dt><dd>" .. outcome .. "</dd>" ..
                        "</dl>" ..
                        "<div class=\"case-study-content\">"
      local html_end = "</div></div>"
      
      -- Add HTML tags around original content
      table.insert(el.content, 1, pandoc.RawBlock("html", html_begin))
      table.insert(el.content, pandoc.RawBlock("html", html_end))
      return el
    end
  elseif el.classes:includes("featured-quote") then
    -- Featured quote processing
    local quote = ""
    local author = el.attributes["author"] or ""
    
    -- Extract quote text from content
    for _, block in ipairs(el.content) do
      if block.t == "Para" or block.t == "Plain" then
        quote = pandoc.utils.stringify(block)
        break
      end
    end
    
    -- Format based on output
    if FORMAT:match 'latex' then
      return pandoc.RawBlock("latex",
        "\\begin{featuredquote}\n" ..
        quote .. "\n" ..
        "\\vspace{0.5em}\\noindent\\textbf{— " .. author .. "}\n" ..
        "\\end{featuredquote}"
      )
    elseif FORMAT:match 'html' then
      return pandoc.RawBlock("html",
        "<div class=\"featured-quote\">" ..
        "<blockquote>" .. quote .. "</blockquote>" ..
        "<p class=\"attribution\">— " .. author .. "</p>" ..
        "</div>"
      )
    end
  elseif el.classes:includes("listicle") then
    -- Listicle processing
    local title = el.attributes["title"] or "Key Points"
    
    -- Format based on output
    if FORMAT:match 'latex' then
      -- Create LaTeX environment for listicle
      local latex_begin = "\\begin{listicle}{" .. title .. "}"
      local latex_end = "\\end{listicle}"
      
      -- Add LaTeX tags around original content
      table.insert(el.content, 1, pandoc.RawBlock("latex", latex_begin))
      table.insert(el.content, pandoc.RawBlock("latex", latex_end))
      return el
    elseif FORMAT:match 'html' then
      -- Create HTML structure for listicle
      local html_begin = "<div class=\"listicle\">" ..
                        "<h3>" .. title .. "</h3>"
      local html_end = "</div>"
      
      -- Add HTML tags around original content
      table.insert(el.content, 1, pandoc.RawBlock("html", html_begin))
      table.insert(el.content, pandoc.RawBlock("html", html_end))
      return el
    end
  elseif el.classes:includes("chapter-header") then
    -- Chapter header processing
    if FORMAT:match 'latex' then
      return pandoc.RawBlock("latex", "\\textcolor{primaryblue}{\\rule{\\textwidth}{2pt}}")
    elseif FORMAT:match 'html' then
      return pandoc.RawBlock("html", "<div class=\"chapter-header\"></div>")
    end
  end
  
  return el
end

-- Convert callout divs to appropriate format
function convert_callout(el)
  if el.classes:includes("callout") then
    local callout_type = "note"
    for _, class in ipairs(el.classes) do
      if class:match("^callout%-") then
        callout_type = class:gsub("^callout%-", "")
        break
      end
    end
    
    local title = el.attributes.title or ""
    
    if FORMAT:match 'latex' then
      local env_name = "callout" .. callout_type
      local latex_begin = "\\begin{" .. env_name .. "}{" .. title .. "}"
      local latex_end = "\\end{" .. env_name .. "}"
      
      table.insert(el.content, 1, pandoc.RawBlock("latex", latex_begin))
      table.insert(el.content, pandoc.RawBlock("latex", latex_end))
    elseif FORMAT:match 'html' then
      local html_begin = "<div class=\"callout callout-" .. callout_type .. "\">"
      if title ~= "" then
        html_begin = html_begin .. "<div class=\"callout-title\">" .. title .. "</div>"
      end
      local html_end = "</div>"
      
      table.insert(el.content, 1, pandoc.RawBlock("html", html_begin))
      table.insert(el.content, pandoc.RawBlock("html", html_end))
    end
  end
  
  return el
end

return {
  {Div = Div},
  {Div = convert_callout}
}