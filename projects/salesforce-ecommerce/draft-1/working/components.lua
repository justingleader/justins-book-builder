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
      end
      -- Add more component handlers here
      
      -- Return div unchanged if not handled
      return div
    end
  }
}