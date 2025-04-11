--[[
Quarto Templates Framework Components
Version: 1.0.0
Date: 2025-04-10

This module implements custom components for the Quarto Templates Framework.
It handles format-specific rendering for various components.
]]--

-- Load the logger
local scriptPath = PANDOC_SCRIPT_FILE:match("(.+)/[^/]+$") or "."
package.path = package.path .. ";" .. scriptPath .. "/?.lua"
local Logger = require("logger")
local logger = Logger

-- Component handlers
local Components = {}

-- Detect the current output format
function Components.detectFormat()
  local format = nil
  
  if quarto.doc.isFormat("pdf") then
    format = "pdf"
  elseif quarto.doc.isFormat("html") then
    format = "html"
  elseif quarto.doc.isFormat("epub") then
    format = "epub"
  else
    format = "unknown"
  end
  
  logger:debug("components", "Detected output format: " .. format)
  return format
end

-- Handle stats block component
function Components.statsBlock(div)
  logger:info("components", "Processing stats block: " .. (div.identifier or "unnamed"))
  
  -- Get the format being rendered
  local format = Components.detectFormat()
  
  -- Extract block title
  local title = div.attributes.title or "Statistics"
  
  if format == "pdf" then
    -- LaTeX implementation
    logger:debug("components", "Using LaTeX implementation for stats block")
    
    -- Start building LaTeX environment
    local latex = '\\begin{statsblock}{' .. title .. '}\n'
    
    -- Process content
    for _, item in ipairs(div.content) do
      latex = latex .. pandoc.write(pandoc.Pandoc({item}), "latex") .. "\n"
    end
    
    latex = latex .. '\\end{statsblock}'
    
    logger:debug("components", "Generated LaTeX: " .. latex:sub(1, 50) .. "...")
    return pandoc.RawBlock("latex", latex)
    
  elseif format == "html" or format == "epub" then
    -- HTML implementation
    logger:debug("components", "Using HTML implementation for stats block")
    
    -- Create HTML structure
    local html = '<div class="stats-block">\n'
    html = html .. '<h3 class="stats-block-title">' .. title .. '</h3>\n'
    html = html .. '<div class="stats-block-content">\n'
    
    -- Process content
    for _, item in ipairs(div.content) do
      html = html .. pandoc.write(pandoc.Pandoc({item}), "html") .. "\n"
    end
    
    html = html .. '</div>\n</div>'
    
    logger:debug("components", "Generated HTML: " .. html:sub(1, 50) .. "...")
    return pandoc.RawBlock("html", html)
  else
    -- Fallback for other formats
    logger:warning("components", "Unknown format: " .. format .. ". Using default implementation.")
    return div
  end
end

-- Initialize component system
function Components.initialize(meta)
  -- Configure logger
  logger:configure(meta)
  
  -- Log initialization
  logger:info("components", "Initializing component system")
  logger:debug("components", "Logger status: " .. logger:status())
  
  -- Return metadata unchanged
  return meta
end

-- Handle success story callout
function Components.successStory(div)
  logger:info("components", "Processing success story: " .. (div.identifier or "unnamed"))
  
  -- Get the format being rendered
  local format = Components.detectFormat()
  
  -- Find the header and content
  local header = nil
  local content = {}
  
  for i, item in ipairs(div.content) do
    if i == 1 and item.t == "Header" then
      header = item
    else
      table.insert(content, item)
    end
  end
  
  -- Default title if no header found
  local title = "Success Story"
  if header and header.content then
    title = pandoc.write(pandoc.Pandoc(header.content), "plain")
  end
  
  if format == "pdf" then
    -- LaTeX implementation
    logger:debug("components", "Using LaTeX implementation for success story")
    
    -- Start building LaTeX environment
    local latex = '\\begin{successstory}{' .. title .. '}\n'
    
    -- Process content
    for _, item in ipairs(content) do
      latex = latex .. pandoc.write(pandoc.Pandoc({item}), "latex") .. "\n"
    end
    
    latex = latex .. '\\end{successstory}'
    
    logger:debug("components", "Generated LaTeX: " .. latex:sub(1, 50) .. "...")
    return pandoc.RawBlock("latex", latex)
    
  elseif format == "html" or format == "epub" then
    -- HTML implementation
    logger:debug("components", "Using HTML implementation for success story")
    
    -- Create HTML structure
    local html = '<div class="callout-success">\n'
    html = html .. '<h3 class="callout-header">' .. title .. '</h3>\n'
    html = html .. '<div class="callout-content">\n'
    
    -- Process content
    for _, item in ipairs(content) do
      html = html .. pandoc.write(pandoc.Pandoc({item}), "html") .. "\n"
    end
    
    html = html .. '</div>\n</div>'
    
    logger:debug("components", "Generated HTML: " .. html:sub(1, 50) .. "...")
    return pandoc.RawBlock("html", html)
  else
    -- Fallback for other formats
    logger:warning("components", "Unknown format: " .. format .. ". Using default implementation.")
    return div
  end
end

-- Handle tip callout
function Components.tipCallout(div)
  logger:info("components", "Processing tip callout: " .. (div.identifier or "unnamed"))
  
  -- Get the format being rendered
  local format = Components.detectFormat()
  
  -- Find the header and content
  local header = nil
  local content = {}
  
  for i, item in ipairs(div.content) do
    if i == 1 and item.t == "Header" then
      header = item
    else
      table.insert(content, item)
    end
  end
  
  -- Default title if no header found
  local title = "Tip"
  if header and header.content then
    title = pandoc.write(pandoc.Pandoc(header.content), "plain")
  end
  
  if format == "pdf" then
    -- LaTeX implementation
    logger:debug("components", "Using LaTeX implementation for tip callout")
    
    -- Start building LaTeX environment
    local latex = '\\begin{tipcallout}{' .. title .. '}\n'
    
    -- Process content
    for _, item in ipairs(content) do
      latex = latex .. pandoc.write(pandoc.Pandoc({item}), "latex") .. "\n"
    end
    
    latex = latex .. '\\end{tipcallout}'
    
    logger:debug("components", "Generated LaTeX: " .. latex:sub(1, 50) .. "...")
    return pandoc.RawBlock("latex", latex)
    
  elseif format == "html" or format == "epub" then
    -- HTML implementation
    logger:debug("components", "Using HTML implementation for tip callout")
    
    -- Create HTML structure
    local html = '<div class="callout-tip">\n'
    html = html .. '<h3 class="callout-header">' .. title .. '</h3>\n'
    html = html .. '<div class="callout-content">\n'
    
    -- Process content
    for _, item in ipairs(content) do
      html = html .. pandoc.write(pandoc.Pandoc({item}), "html") .. "\n"
    end
    
    html = html .. '</div>\n</div>'
    
    logger:debug("components", "Generated HTML: " .. html:sub(1, 50) .. "...")
    return pandoc.RawBlock("html", html)
  else
    -- Fallback for other formats
    logger:warning("components", "Unknown format: " .. format .. ". Using default implementation.")
    return div
  end
end

-- Handle note callout
function Components.noteCallout(div)
  logger:info("components", "Processing note callout: " .. (div.identifier or "unnamed"))
  
  -- Get the format being rendered
  local format = Components.detectFormat()
  
  -- Find the header and content
  local header = nil
  local content = {}
  
  for i, item in ipairs(div.content) do
    if i == 1 and item.t == "Header" then
      header = item
    else
      table.insert(content, item)
    end
  end
  
  -- Default title if no header found
  local title = "Note"
  if header and header.content then
    title = pandoc.write(pandoc.Pandoc(header.content), "plain")
  end
  
  if format == "pdf" then
    -- LaTeX implementation
    logger:debug("components", "Using LaTeX implementation for note callout")
    
    -- Start building LaTeX environment
    local latex = '\\begin{notecallout}{' .. title .. '}\n'
    
    -- Process content
    for _, item in ipairs(content) do
      latex = latex .. pandoc.write(pandoc.Pandoc({item}), "latex") .. "\n"
    end
    
    latex = latex .. '\\end{notecallout}'
    
    logger:debug("components", "Generated LaTeX: " .. latex:sub(1, 50) .. "...")
    return pandoc.RawBlock("latex", latex)
    
  elseif format == "html" or format == "epub" then
    -- HTML implementation
    logger:debug("components", "Using HTML implementation for note callout")
    
    -- Create HTML structure
    local html = '<div class="callout-note">\n'
    html = html .. '<h3 class="callout-header">' .. title .. '</h3>\n'
    html = html .. '<div class="callout-content">\n'
    
    -- Process content
    for _, item in ipairs(content) do
      html = html .. pandoc.write(pandoc.Pandoc({item}), "html") .. "\n"
    end
    
    html = html .. '</div>\n</div>'
    
    logger:debug("components", "Generated HTML: " .. html:sub(1, 50) .. "...")
    return pandoc.RawBlock("html", html)
  else
    -- Fallback for other formats
    logger:warning("components", "Unknown format: " .. format .. ". Using default implementation.")
    return div
  end
end

-- Handle featured quote
function Components.featuredQuote(div)
  logger:info("components", "Processing featured quote: " .. (div.identifier or "unnamed"))
  
  -- Get the format being rendered
  local format = Components.detectFormat()
  
  -- Extract content
  local content = {}
  local attribution = div.attributes.attribution or ""
  
  -- Get content
  content = div.content
  
  if format == "pdf" then
    -- LaTeX implementation
    logger:debug("components", "Using LaTeX implementation for featured quote")
    
    -- Start building LaTeX environment
    local latex = '\\begin{featuredquote}[Featured Quote]\n'
    
    -- Process content
    for _, item in ipairs(content) do
      latex = latex .. pandoc.write(pandoc.Pandoc({item}), "latex") .. "\n"
    end
    
    -- Add attribution if present
    if attribution ~= "" then
      latex = latex .. '\\par\\vspace{0.5em}\\hfill--- ' .. attribution .. '\n'
    end
    
    latex = latex .. '\\end{featuredquote}'
    
    logger:debug("components", "Generated LaTeX: " .. latex:sub(1, 50) .. "...")
    return pandoc.RawBlock("latex", latex)
    
  elseif format == "html" or format == "epub" then
    -- HTML implementation
    logger:debug("components", "Using HTML implementation for featured quote")
    
    -- Create HTML structure
    local html = '<div class="featured-quote">\n'
    html = html .. '<div class="quote-icon">💡</div>\n'
    html = html .. '<div class="quote-content">\n'
    
    -- Process content
    for _, item in ipairs(content) do
      html = html .. pandoc.write(pandoc.Pandoc({item}), "html") .. "\n"
    end
    
    -- Add attribution if present
    if attribution ~= "" then
      html = html .. '<div class="quote-attribution">— ' .. attribution .. '</div>\n'
    end
    
    html = html .. '</div>\n</div>'
    
    logger:debug("components", "Generated HTML: " .. html:sub(1, 50) .. "...")
    return pandoc.RawBlock("html", html)
  else
    -- Fallback for other formats
    logger:warning("components", "Unknown format: " .. format .. ". Using default implementation.")
    return div
  end
end

-- Handle executive guide
function Components.executiveGuide(div)
  logger:info("components", "Processing executive guide: " .. (div.identifier or "unnamed"))
  
  -- Get the format being rendered
  local format = Components.detectFormat()
  
  -- Extract content
  local content = div.content
  
  if format == "pdf" then
    -- LaTeX implementation
    logger:debug("components", "Using LaTeX implementation for executive guide")
    
    -- Start building LaTeX environment
    local latex = '\\begin{executiveguide}[STACK INTELLIGENCE EXECUTIVE GUIDE]\n'
    
    -- Process content
    for _, item in ipairs(content) do
      latex = latex .. pandoc.write(pandoc.Pandoc({item}), "latex") .. "\n"
    end
    
    latex = latex .. '\\end{executiveguide}'
    
    logger:debug("components", "Generated LaTeX: " .. latex:sub(1, 50) .. "...")
    return pandoc.RawBlock("latex", latex)
    
  elseif format == "html" or format == "epub" then
    -- HTML implementation
    logger:debug("components", "Using HTML implementation for executive guide")
    
    -- Create HTML structure
    local html = '<div class="executive-guide">\n'
    html = html .. '<div class="guide-header">⚠️ STACK INTELLIGENCE EXECUTIVE GUIDE</div>\n'
    html = html .. '<div class="guide-content">\n'
    
    -- Process content
    for _, item in ipairs(content) do
      html = html .. pandoc.write(pandoc.Pandoc({item}), "html") .. "\n"
    end
    
    html = html .. '</div>\n</div>'
    
    logger:debug("components", "Generated HTML: " .. html:sub(1, 50) .. "...")
    return pandoc.RawBlock("html", html)
  else
    -- Fallback for other formats
    logger:warning("components", "Unknown format: " .. format .. ". Using default implementation.")
    return div
  end
end

-- Return filter functions
return {
  {
    Meta = Components.initialize
  },
  {
    Div = function(div)
      -- Handle different component types
      if div.classes:includes("stats-block") then
        return Components.statsBlock(div)
      elseif div.classes:includes("callout-success") then
        return Components.successStory(div)
      elseif div.classes:includes("callout-tip") then
        return Components.tipCallout(div)
      elseif div.classes:includes("callout-note") then
        return Components.noteCallout(div)
      elseif div.classes:includes("featured-quote") then
        return Components.featuredQuote(div)
      elseif div.classes:includes("executive-guide") then
        return Components.executiveGuide(div)
      end
      -- Return div unchanged if not handled
      return div
    end
  }
}