-- stack-validation.lua
-- Validation system for Stack Intelligence templates
-- Part of Phase 3 implementation

-- Define required template sections for different document types
local document_templates = {
  ["executive_brief"] = {
    required_sections = {"executive_summary", "introduction", "key_findings", "recommendations"},
    recommended_sections = {"case_study", "methodology", "about_stack_intelligence"},
    max_length = 25,
    validate_function = function(doc)
      -- Executive Brief specific validation
      return true, ""
    end
  },
  
  ["whitepaper"] = {
    required_sections = {"executive_summary", "introduction", "background", "analysis", "conclusion"},
    recommended_sections = {"methodology", "references", "about_author", "about_stack_intelligence"},
    max_length = 50,
    validate_function = function(doc)
      -- Whitepaper specific validation
      return true, ""
    end
  },
  
  ["case_study"] = {
    required_sections = {"challenge", "solution", "results", "customer_quote"},
    recommended_sections = {"company_background", "implementation_details", "about_stack_intelligence"},
    max_length = 15,
    validate_function = function(doc)
      -- Case study specific validation
      return true, ""
    end
  },
  
  ["ebook"] = {
    required_sections = {"introduction", "chapters", "conclusion"},
    recommended_sections = {"foreword", "about_author", "references", "resources"},
    chapter_min = 3,
    chapter_max = 12,
    validate_function = function(doc)
      -- Ebook specific validation
      local chapters = 0
      -- Count chapters implementation would go here
      if chapters < 3 then
        return false, "Ebooks should have at least 3 chapters"
      end
      if chapters > 12 then
        return false, "Ebooks should have no more than 12 chapters for readability"
      end
      return true, ""
    end
  }
}

-- Functions for document validation
local function check_required_sections(metadata, template_type)
  local missing = {}
  local template = document_templates[template_type]
  
  if not template then
    return false, "Unknown template type: " .. template_type
  end
  
  -- Check for required sections
  for _, section in ipairs(template.required_sections) do
    if not metadata[section] then
      table.insert(missing, section)
    end
  end
  
  if #missing > 0 then
    return false, "Missing required sections: " .. table.concat(missing, ", ")
  end
  
  return true, ""
end

local function check_document_length(doc, template_type)
  local template = document_templates[template_type]
  if not template then
    return false, "Unknown template type: " .. template_type
  end
  
  -- Count approximate page length based on words
  local text = pandoc.utils.stringify(doc)
  local words = 0
  for _ in text:gmatch("%S+") do
    words = words + 1
  end
  
  -- Approximate pages (300 words per page is a rough estimate)
  local pages = math.ceil(words / 300)
  
  if template.max_length and pages > template.max_length then
    return false, "Document exceeds maximum recommended length of " .. template.max_length .. " pages (currently ~" .. pages .. " pages)"
  end
  
  return true, ""
end

local function validate_document(doc)
  local metadata = doc.meta
  local template_type = metadata.template_type and pandoc.utils.stringify(metadata.template_type) or nil
  
  if not template_type then
    -- Skip validation if no template_type is specified
    return nil
  end
  
  -- Check if we know how to validate this template type
  if not document_templates[template_type] then
    print("Warning: Unknown template type: " .. template_type)
    return nil
  end
  
  local errors = {}
  local warnings = {}
  
  -- Check required sections
  local sections_ok, sections_msg = check_required_sections(metadata, template_type)
  if not sections_ok then
    table.insert(errors, sections_msg)
  end
  
  -- Check document length
  local length_ok, length_msg = check_document_length(doc, template_type)
  if not length_ok then
    table.insert(warnings, length_msg)
  end
  
  -- Run template-specific validation
  local template = document_templates[template_type]
  local specific_ok, specific_msg = template.validate_function(doc)
  if not specific_ok then
    table.insert(errors, specific_msg)
  end
  
  -- Report any issues
  if #errors > 0 then
    io.stderr:write("Validation Errors for " .. template_type .. ":\n")
    for _, err in ipairs(errors) do
      io.stderr:write("  - " .. err .. "\n")
    end
  end
  
  if #warnings > 0 then
    io.stderr:write("Validation Warnings for " .. template_type .. ":\n")
    for _, warn in ipairs(warnings) do
      io.stderr:write("  - " .. warn .. "\n")
    end
  end
  
  -- Return success only if no errors (warnings are acceptable)
  return #errors == 0
end

-- Hook into the document processing
function Pandoc(doc)
  -- Run validation
  local validation_result = validate_document(doc)
  
  -- Return the document unchanged (validation just produces warnings)
  return doc
end

return {
  {Pandoc = Pandoc}
}