--[[
Quarto Templates Framework Brand Loader
Version: 1.0.0
Date: 2025-04-10

This module handles loading and applying brand configurations to Quarto documents.
It processes brand.yml files and injects brand properties into document metadata.
]]--

-- Load the logger
local scriptPath = PANDOC_SCRIPT_FILE:match("(.+)/[^/]+$") or "."
package.path = package.path .. ";" .. scriptPath .. "/?.lua"
local Logger = require("logger")
local logger = Logger

-- Initialize yaml parser if available
local yaml = nil
pcall(function() yaml = require("yaml") end)

local BrandLoader = {}

-- Load brand configuration from path
function BrandLoader.loadBrand(brandName)
  -- Skip if no brand name provided
  if not brandName or brandName == "" then
    logger:debug("brand-loader", "No brand name provided, skipping brand loading")
    return nil
  end

  logger:info("brand-loader", "Loading brand: " .. brandName)
  
  -- Default paths
  local brandPath = "branding/" .. brandName .. "/"
  local configPath = brandPath .. "brand.yml"
  
  -- Check if configuration exists
  local configFile = io.open(configPath, "r")
  if not configFile then
    logger:error("brand-loader", "Brand configuration not found: " .. configPath)
    return nil
  end
  
  -- Read configuration
  local configContent = configFile:read("*all")
  configFile:close()
  
  logger:debug("brand-loader", "Read configuration file: " .. configPath)
  
  -- Parse YAML if YAML module is available
  local brandConfig = nil
  if yaml then
    brandConfig = yaml.parse(configContent)
    if not brandConfig then
      logger:error("brand-loader", "Failed to parse brand configuration")
      return nil
    end
  else
    -- Basic parsing if YAML module not available
    logger:warning("brand-loader", "YAML parser not available, using basic parsing")
    brandConfig = BrandLoader.basicYamlParse(configContent)
  end
  
  logger:debug("brand-loader", "Brand configuration parsed successfully")
  
  -- Add paths to configuration
  brandConfig.paths = {
    base = brandPath,
    assets = brandPath .. "assets/"
  }
  
  -- Check and validate required fields
  if not brandConfig.name then
    brandConfig.name = brandName
    logger:warning("brand-loader", "Brand name not specified in config, using folder name: " .. brandName)
  end
  
  if not brandConfig.colors then
    logger:warning("brand-loader", "No colors defined in brand configuration")
    brandConfig.colors = {}
  end
  
  return brandConfig
end

-- Apply brand to metadata
function BrandLoader.applyBrand(meta)
  -- Initialize logging if needed
  logger:configure(meta)
  
  -- Log logger status
  logger:debug("brand-loader", "Logger status: " .. logger:status())
  
  -- Get brand name from metadata
  local brandName = meta.brand and pandoc.utils.stringify(meta.brand) or "default"
  
  -- Except for default brand, try to load brand configuration
  if brandName ~= "default" then
    logger:info("brand-loader", "Applying brand: " .. brandName)
    
    -- Load brand configuration
    local brand = BrandLoader.loadBrand(brandName)
    if not brand then
      logger:warning("brand-loader", "Using default branding")
      return meta
    end
    
    -- Set brand variables in metadata
    meta.brand_name = brand.name
    meta.brand_version = brand.version
    meta.brand_colors = brand.colors
    meta.brand_fonts = brand.fonts
    meta.brand_logos = brand.logos
    meta.brand_paths = brand.paths
    
    -- Log successful brand application
    logger:info("brand-loader", "Brand '" .. brandName .. "' applied successfully")
  else
    logger:info("brand-loader", "Using default branding")
  end
  
  return meta
end

-- Basic YAML parser for when yaml module is not available
function BrandLoader.basicYamlParse(content)
  local result = {}
  local currentSection = result
  local sectionStack = {}
  
  for line in content:gmatch("[^\r\n]+") do
    -- Skip comments and empty lines
    if not line:match("^%s*#") and line:match("%S") then
      -- Check indentation level
      local indent = line:match("^(%s*)")
      local indentLevel = #indent / 2
      
      -- Adjust section stack based on indentation
      while #sectionStack > indentLevel do
        table.remove(sectionStack)
        currentSection = sectionStack[#sectionStack] or result
      end
      
      -- Parse the line
      local key, value = line:match("^%s*([%w_-]+):%s*(.*)$")
      if key then
        -- Handle different value types
        if value == "" then
          -- Section header
          if not currentSection[key] then
            currentSection[key] = {}
          end
          table.insert(sectionStack, currentSection)
          currentSection = currentSection[key]
        elseif value:match("^\"(.*)\"$") or value:match("^'(.*)'$") then
          -- Quoted string
          currentSection[key] = value:match("^[\"'](.*)[\"\']$")
        elseif value:match("^%d+$") then
          -- Integer
          currentSection[key] = tonumber(value)
        elseif value:match("^%d+%.%d+$") then
          -- Float
          currentSection[key] = tonumber(value)
        elseif value:match("^true$") or value:match("^false$") then
          -- Boolean
          currentSection[key] = (value == "true")
        else
          -- Regular string
          currentSection[key] = value
        end
      end
    end
  end
  
  return result
end

-- Return functions for the Pandoc filter
return {
  {
    Meta = function(meta)
      return BrandLoader.applyBrand(meta)
    end
  }
}