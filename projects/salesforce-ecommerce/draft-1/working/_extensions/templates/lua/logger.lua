--[[
Quarto Templates Framework Logging System
Version: 1.0.0
Date: 2025-04-10

This module provides a centralized logging system for the Quarto Templates Framework.
It supports different log levels, file or console output, and contextual logging by component.
]]--

Logger = {}
Logger.levels = {DEBUG = 10, INFO = 20, WARNING = 30, ERROR = 40}
Logger.level = Logger.levels.INFO  -- Default level
Logger.logfile = nil               -- Default to console
Logger.enabled = true              -- Logging can be disabled entirely

-- Set the minimum log level to record
function Logger:setLevel(level)
  if type(level) == "string" then
    level = string.upper(level)
    if self.levels[level] then
      self.level = self.levels[level]
    else
      print("WARNING: Invalid log level '" .. level .. "'. Using INFO level.")
      self.level = self.levels.INFO
    end
  elseif type(level) == "number" then
    self.level = level
  else
    print("WARNING: Invalid log level type. Using INFO level.")
    self.level = self.levels.INFO
  end
  return self
end

-- Set the output logfile (nil for console output)
function Logger:setLogFile(filename)
  if filename then
    -- Test if we can open the file for writing
    local file = io.open(filename, "a")
    if file then
      file:write("--- Logging initialized at " .. os.date("%Y-%m-%d %H:%M:%S") .. " ---\n")
      file:close()
      self.logfile = filename
      self:info("logger", "Logging to file: " .. filename)
    else
      print("WARNING: Cannot write to log file '" .. filename .. "'. Using console output.")
      self.logfile = nil
    end
  else
    self.logfile = nil
  end
  return self
end

-- Enable or disable logging
function Logger:setEnabled(enabled)
  self.enabled = enabled
  return self
end

-- Internal logging function
function Logger:log(level, component, message)
  if not self.enabled or level < self.level then return end
  
  local timestamp = os.date("%Y-%m-%d %H:%M:%S")
  local levelName = "UNKNOWN"
  for name, val in pairs(self.levels) do
    if val == level then levelName = name end
  end
  
  local logMessage = string.format("[%s] [%s] [%s]: %s", 
                                  timestamp, levelName, component, message)
  
  if self.logfile then
    local file = io.open(self.logfile, "a")
    if file then
      file:write(logMessage .. "\n")
      file:close()
    else
      -- Fallback to console if file can't be opened
      print(logMessage)
    end
  else
    print(logMessage)
  end
end

-- Log a DEBUG message
function Logger:debug(component, message)
  self:log(self.levels.DEBUG, component, message)
  return self
end

-- Log an INFO message
function Logger:info(component, message)
  self:log(self.levels.INFO, component, message)
  return self
end

-- Log a WARNING message
function Logger:warning(component, message)
  self:log(self.levels.WARNING, component, message)
  return self
end

-- Log an ERROR message
function Logger:error(component, message)
  self:log(self.levels.ERROR, component, message)
  return self
end

-- Set defaults from metadata if provided
function Logger:configure(meta)
  if meta then
    -- Set log level from metadata
    if meta["log-level"] then
      self:setLevel(meta["log-level"])
    end
    
    -- Set log file from metadata
    if meta["log-file"] then
      self:setLogFile(meta["log-file"])
    end
    
    -- Set enabled state from metadata
    if meta["log-enabled"] ~= nil then
      self:setEnabled(meta["log-enabled"])
    end
  end
  
  return self
end

-- Get a string representation of the current configuration
function Logger:status()
  local levelName = "UNKNOWN"
  for name, val in pairs(self.levels) do
    if val == self.level then levelName = name end
  end
  
  local output = self.logfile or "console"
  local status = string.format("Logger configured with level=%s, output=%s, enabled=%s", 
                              levelName, output, tostring(self.enabled))
  
  return status
end

return Logger