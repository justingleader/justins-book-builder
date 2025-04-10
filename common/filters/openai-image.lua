-- OpenAI Image Generation Filter for Quarto
local config = nil

-- Debugging function to write logs to a file
local function log(message)
    local log_file = io.open("openai-filter.log", "a")
    if log_file then
        log_file:write(os.date("%Y-%m-%d %H:%M:%S") .. " - " .. tostring(message) .. "\n")
        log_file:close()
    end
end

-- Get current script directory
local script_path = PANDOC_SCRIPT_FILE or ""
local script_dir = script_path:match("(.*/)")
log("Script path: " .. tostring(script_path))
log("Script directory: " .. tostring(script_dir or "nil"))

-- Log the current working directory
local cwd = io.popen("pwd"):read("*a"):gsub("\n", "")
log("Working directory: " .. cwd)

local function read_config()
    log("Reading config file...")
    
    -- Try multiple possible config locations
    local config_paths = {
        "config.yaml",
        "../config.yaml",
        "./config.yaml",
        script_dir and (script_dir .. "../config.yaml") or nil,
        script_dir and (script_dir .. "config.yaml") or nil,
        cwd .. "/config.yaml",
        cwd .. "/test-book/config.yaml"
    }
    
    -- Filter out nil paths
    local valid_paths = {}
    for _, path in ipairs(config_paths) do
        if path then
            table.insert(valid_paths, path)
        end
    end
    
    local config_file = nil
    local used_path = nil
    
    for _, path in ipairs(valid_paths) do
        log("Trying config path: " .. path)
        config_file = io.open(path, "r")
        if config_file then
            used_path = path
            log("Successfully opened config at: " .. path)
            break
        end
    end
    
    if not config_file then
        local error_msg = "Error: Could not open config.yaml in any location"
        log(error_msg)
        error(error_msg)
    end
    
    local content = config_file:read("*all")
    config_file:close()
    
    -- Simple YAML parsing (basic implementation)
    local config = {}
    for line in content:gmatch("[^\r\n]+") do
        local key, value = line:match("^%s*([^:]+):%s*(.+)")
        if key and value then
            -- Remove quotes if present
            value = value:gsub('^"(.*)"$', '%1')
            config[key:gsub("%s+", "")] = value
        end
    end
    
    -- Add the config path directory to use for relative paths
    config.config_dir = used_path:match("(.*/)")
    if not config.config_dir then
        config.config_dir = "./"
    end
    
    log("Config loaded from: " .. used_path)
    log("Config directory: " .. config.config_dir)
    
    return config
end

-- Create a more robust path function
local function resolve_path(base_dir, path)
    if path:sub(1,1) == "/" then
        -- Absolute path
        return path
    else
        -- Relative path
        return base_dir .. path
    end
end

function Meta(meta)
    log("Meta function called")
    -- Read configuration
    config = read_config()
    meta.openai_config = config
    return meta
end

function CodeBlock(block)
    log("CodeBlock function called")
    if block.classes[1] == "openai-image" then
        log("Processing openai-image block")
        
        -- Make sure we have config
        if not config then
            log("Config not loaded yet, loading now")
            config = read_config()
        end
        
        -- Parse the code block content
        local params = {}
        for line in block.text:gmatch("[^\r\n]+") do
            local key, value = line:match("^%s*([^:]+):%s*(.+)")
            if key and value then
                -- Remove quotes if present
                value = value:gsub('^"(.*)"$', '%1')
                params[key:gsub("%s+", "")] = value
            end
        end
        log("Parsed params for image: " .. (params.prompt or "unknown"))
        
        -- Fix image_dir path to be absolute
        local image_dir = config.image_dir or "images"
        if not image_dir:sub(1,1) == "/" then
            -- Make image_dir absolute using config directory as base
            image_dir = resolve_path(config.config_dir, image_dir)
        end
        log("Using image directory: " .. image_dir)
        
        -- Create a Python script to generate the image
        local python_script = string.format([[
import sys
import os
import traceback

try:
    # Add parent directory to Python path
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(parent_dir)
    
    from quarto_book_builder.image_generator import ImageGenerator
    
    # Log Python environment for debugging
    with open("openai-python.log", "a") as log:
        log.write("\n--- New image generation attempt ---\n")
        log.write(f"Python version: {sys.version}\n")
        log.write(f"Working directory: {os.getcwd()}\n")
        log.write(f"Script location: {__file__}\n")
        log.write(f"Parent directory: {parent_dir}\n")
    
    # Create properly resolved config
    config = {
        'openai_api_key': '%s',
        'image_dir': '%s',
        'max_retries': 3
    }

    # Log config
    with open("openai-python.log", "a") as log:
        log.write(f"Config: {config}\n")
        log.write(f"Image directory exists: {os.path.exists(config['image_dir'])}\n")
        
    # Create generator and generate image
    generator = ImageGenerator(config)
    prompt = %s
    
    with open("openai-python.log", "a") as log:
        log.write(f"Generating image with prompt: {prompt}\n")
        
    image_path = generator.generate_image(prompt)
    
    # Log results
    with open("openai-python.log", "a") as log:
        log.write(f"Image generated at: {image_path}\n")
        log.write(f"Image exists: {os.path.exists(image_path)}\n")
        log.write(f"Absolute image path: {os.path.abspath(image_path)}\n")
        
    print(image_path)
except Exception as e:
    with open("openai-python.log", "a") as log:
        log.write(f"Error: {str(e)}\n")
        log.write(traceback.format_exc())
    print("ERROR: " + str(e))
]], 
            config.openai_api_key,
            image_dir,
            string.format("%q", params.prompt)  -- Use proper string quoting in Python
        )
        
        -- Write the Python script to a temporary file
        local temp_script = os.tmpname()
        log("Temporary script file: " .. temp_script)
        local f = io.open(temp_script, "w")
        f:write(python_script)
        f:close()
        
        log("Executing Python script...")
        -- Execute the Python script
        local handle = io.popen("python3 " .. temp_script .. " 2>&1")
        local result = handle:read("*a")
        local _, _, code = handle:close()
        log("Python script exit code: " .. tostring(code or "unknown"))
        os.remove(temp_script)
        
        log("Python script result: " .. result)
        
        -- Check for error
        if result:match("^ERROR:") then
            log("Error detected in Python execution")
            return pandoc.Para({
                pandoc.Str("Error generating image: " .. result:match("^ERROR:%s*(.*)"))
            })
        end
        
        -- Get the image path from the result
        local image_path = result:match("^%s*(.-)%s*$")
        log("Image path from Python: " .. image_path)
        
        -- Get the format we're rendering to
        local format = pandoc.format or "html"
        log("Current format: " .. format)
        
        -- Create paths for different output formats
        local rel_path = image_path
        
        -- For PDF, we need relative path with special handling
        if format:match("latex") or format:match("pdf") then
            -- For LaTeX/PDF we need relative path from the document
            -- Extract filename from path
            local filename = image_path:match("([^/\\]+)$")
            
            -- Use filename with images directory
            if filename then
                rel_path = "../images/" .. filename
                log("Using PDF relative path: " .. rel_path)
            else
                log("Failed to extract filename from path, using absolute path")
                rel_path = image_path
            end
        else
            -- For other formats like HTML/EPUB, use absolute path
            rel_path = image_path
            log("Using absolute path for format " .. format .. ": " .. rel_path)
        end
        
        -- Create image block with caption
        local caption = params.prompt or ""
        local image_block = pandoc.Para({
            pandoc.Image({pandoc.Str(caption)}, rel_path, caption)
        })
        
        return image_block
    end
    return block
end 