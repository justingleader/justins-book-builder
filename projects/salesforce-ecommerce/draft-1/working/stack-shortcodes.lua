-- stack-shortcodes.lua
-- Simplified shortcode system for Stack Intelligence templates

-- Featured Quote shortcode
function Featured_Quote(args, kwargs, blocks)
  local quote = pandoc.utils.stringify(blocks[1])
  local author = ""
  
  if #blocks > 1 then
    author = pandoc.utils.stringify(blocks[2])
  end
  
  -- Format for PDF output with better styling
  local latex_code = '\\begin{tcolorbox}[enhanced, colback=white, colframe=white, ' ..
                    'boxrule=0pt, leftrule=3pt, left=10pt, right=5pt, top=5pt, ' ..
                    'bottom=5pt, borderline west={3pt}{0pt}{primaryorange}, ' ..
                    'arc=0pt, boxsep=5pt]\n' ..
                    '\\textit{\\large ``' .. quote .. '\'\'}' ..
                    '\\vspace{0.5em}\\begin{flushright}\\textbf{--- ' .. author .. '}\\end{flushright}' .. 
                    '\\end{tcolorbox}'
  
  return pandoc.RawBlock('latex', latex_code)
end

-- Case Study shortcode
function Case_Study(args, kwargs, blocks)
  -- Extract attributes
  local company = kwargs['company'] or "Company Name"
  local segment = kwargs['segment'] or "Industry Segment"
  local revenue = kwargs['revenue'] or "Annual Revenue"
  local challenge = kwargs['challenge'] or "Business Challenge"
  local outcome = kwargs['outcome'] or "Strategic Outcome"
  
  -- Process content
  local content = ""
  for _, block in ipairs(blocks) do
    content = content .. pandoc.utils.stringify(block) .. "\n\n"
  end
  
  -- Format for PDF output with improved design
  local latex_code = '\\begin{tcolorbox}[enhanced, title={\\Large Case Study: ' .. company .. '}, ' ..
                   'colback=white, colframe=primaryblue, ' .. 
                   'fonttitle=\\bfseries\\color{white}, ' ..
                   'coltitle=white, colbacktitle=primaryblue, ' ..
                   'arc=0pt, boxrule=1pt, leftrule=5pt, ' .. 
                   'breakable, width=\\textwidth]\n' ..
                   '\\begin{tabular}{@{}ll@{}}\n' ..
                   '\\textbf{Industry Segment:} & ' .. segment .. ' \\\\\n' ..
                   '\\textbf{Annual Revenue:} & ' .. revenue .. ' \\\\\n' ..
                   '\\textbf{Business Challenge:} & ' .. challenge .. ' \\\\\n' ..
                   '\\textbf{Strategic Outcome:} & ' .. outcome .. ' \\\\\n' ..
                   '\\end{tabular}\n\\vspace{1em}\n\n' ..
                   content .. 
                   '\\end{tcolorbox}'
  
  return pandoc.RawBlock('latex', latex_code)
end

-- Listicle shortcode
function Listicle(args, kwargs, blocks)
  local title = kwargs['title'] or "Key Points"
  local style = kwargs['style'] or ""
  
  -- Process content
  local content = ""
  for _, block in ipairs(blocks) do
    content = content .. pandoc.utils.stringify(block) .. "\n"
  end
  
  -- Format for PDF output with improved styling
  local latex_code = '\\begin{tcolorbox}[enhanced, ' ..
                   'title={\\bfseries ' .. title .. '}, ' ..
                   'colback=gray!5, colframe=primaryblue!80!gray, ' ..
                   'coltitle=white, colbacktitle=primaryblue, ' ..
                   'fonttitle=\\bfseries\\color{white}, ' ..
                   'arc=0pt, boxrule=1pt, ' ..
                   'breakable, width=\\textwidth]\n' ..
                   content .. 
                   '\\end{tcolorbox}'
  
  return pandoc.RawBlock('latex', latex_code)
end

-- Stats Highlight shortcode
function Stats_Highlight(args, kwargs, blocks)
  local title = kwargs['title'] or "Key Statistics"
  
  -- Process content
  local content = ""
  for _, block in ipairs(blocks) do
    content = content .. pandoc.utils.stringify(block) .. "\n"
  end
  
  -- Format for PDF output with improved styling
  local latex_code = '\\begin{tcolorbox}[enhanced, ' ..
                   'title={\\bfseries ' .. title .. '}, ' ..
                   'colback=secondaryblue!5, colframe=secondaryblue!50!white, ' ..
                   'coltitle=white, colbacktitle=secondaryblue, ' ..
                   'fonttitle=\\bfseries\\color{white}, ' ..
                   'arc=0pt, boxrule=1pt, ' ..
                   'breakable, width=\\textwidth]\n' ..
                   content .. 
                   '\\end{tcolorbox}'
  
  return pandoc.RawBlock('latex', latex_code)
end

-- Action Plan shortcode
function Action_Plan(args, kwargs, blocks)
  local title = kwargs['title'] or "Action Plan"
  
  -- Process content
  local content = ""
  for _, block in ipairs(blocks) do
    content = content .. pandoc.utils.stringify(block) .. "\n"
  end
  
  -- Format for PDF output with improved styling
  local latex_code = '\\begin{tcolorbox}[enhanced, ' ..
                   'title={\\bfseries ' .. title .. '}, ' ..
                   'colback=primaryorange!5, colframe=primaryorange!80!white, ' ..
                   'coltitle=white, colbacktitle=primaryorange, ' ..
                   'fonttitle=\\bfseries\\color{white}, ' ..
                   'arc=0pt, boxrule=1pt, ' ..
                   'breakable, width=\\textwidth]\n' ..
                   content .. 
                   '\\end{tcolorbox}'
  
  return pandoc.RawBlock('latex', latex_code)
end

-- Quick Tips shortcode
function Quick_Tips(args, kwargs, blocks)
  local title = kwargs['title'] or "Quick Tips"
  
  -- Process content
  local content = ""
  for _, block in ipairs(blocks) do
    content = content .. pandoc.utils.stringify(block) .. "\n"
  end
  
  -- Format for PDF output with improved styling
  local latex_code = '\\begin{tcolorbox}[enhanced, ' ..
                   'title={\\bfseries ' .. title .. '}, ' ..
                   'colback=green!5, colframe=green!80!black, ' ..
                   'coltitle=white, colbacktitle=green!70!black, ' ..
                   'fonttitle=\\bfseries\\color{white}, ' ..
                   'arc=0pt, boxrule=1pt, ' ..
                   'breakable, width=\\textwidth]\n' ..
                   content .. 
                   '\\end{tcolorbox}'
  
  return pandoc.RawBlock('latex', latex_code)
end

-- Process raw blocks to handle shortcodes manually
function RawBlock(el)
  if el.format ~= "html" then
    return nil
  end
  
  -- Match for featured-quote shortcode
  if el.text:match("{{{< featured%-quote") then
    local content = el.text:match("{{{< featured%-quote.->(.-){{{< /featured%-quote >}}")
    if content then
      local blocks = {}
      for line in content:gmatch("[^\r\n]+") do
        table.insert(blocks, line)
      end
      if #blocks >= 2 then
        return Featured_Quote({}, {}, blocks)
      end
    end
  end
  
  -- Match for case-study shortcode
  if el.text:match("{{{< case%-study") then
    local attrs = {}
    local company = el.text:match('company="([^"]+)"')
    if company then attrs['company'] = company end
    
    local segment = el.text:match('segment="([^"]+)"')
    if segment then attrs['segment'] = segment end
    
    local revenue = el.text:match('revenue="([^"]+)"')
    if revenue then attrs['revenue'] = revenue end
    
    local challenge = el.text:match('challenge="([^"]+)"')
    if challenge then attrs['challenge'] = challenge end
    
    local outcome = el.text:match('outcome="([^"]+)"')
    if outcome then attrs['outcome'] = outcome end
    
    local content = el.text:match("{{{< case%-study.->(.-){{{< /case%-study >}}")
    if content then
      local blocks = {}
      for line in content:gmatch("[^\r\n]+") do
        table.insert(blocks, line)
      end
      return Case_Study({}, attrs, blocks)
    end
  end
  
  -- Match for listicle shortcode
  if el.text:match("{{{< listicle") then
    local attrs = {}
    local title = el.text:match('title="([^"]+)"')
    if title then attrs['title'] = title end
    
    local content = el.text:match("{{{< listicle.->(.-){{{< /listicle >}}")
    if content then
      local blocks = {}
      for line in content:gmatch("[^\r\n]+") do
        table.insert(blocks, line)
      end
      return Listicle({}, attrs, blocks)
    end
  end
  
  -- Match for stats-highlight shortcode
  if el.text:match("{{{< stats%-highlight") then
    local attrs = {}
    local title = el.text:match('title="([^"]+)"')
    if title then attrs['title'] = title end
    
    local content = el.text:match("{{{< stats%-highlight.->(.-){{{< /stats%-highlight >}}")
    if content then
      local blocks = {}
      for line in content:gmatch("[^\r\n]+") do
        table.insert(blocks, line)
      end
      return Stats_Highlight({}, attrs, blocks)
    end
  end
  
  -- Match for action-plan shortcode
  if el.text:match("{{{< action%-plan") then
    local attrs = {}
    local title = el.text:match('title="([^"]+)"')
    if title then attrs['title'] = title end
    
    local content = el.text:match("{{{< action%-plan.->(.-){{{< /action%-plan >}}")
    if content then
      local blocks = {}
      for line in content:gmatch("[^\r\n]+") do
        table.insert(blocks, line)
      end
      return Action_Plan({}, attrs, blocks)
    end
  end
  
  -- Match for quick-tips shortcode
  if el.text:match("{{{< quick%-tips") then
    local attrs = {}
    local title = el.text:match('title="([^"]+)"')
    if title then attrs['title'] = title end
    
    local content = el.text:match("{{{< quick%-tips.->(.-){{{< /quick%-tips >}}")
    if content then
      local blocks = {}
      for line in content:gmatch("[^\r\n]+") do
        table.insert(blocks, line)
      end
      return Quick_Tips({}, attrs, blocks)
    end
  end
  
  return nil
end

-- Process document
function Pandoc(doc)
  return doc
end

return {
  {Pandoc = Pandoc},
  {RawBlock = RawBlock}
}