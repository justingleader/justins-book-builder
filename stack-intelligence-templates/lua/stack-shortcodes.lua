-- stack-shortcodes.lua
-- Enhanced shortcode system for Stack Intelligence templates
-- Phase 3 implementation with improved user experience

-- Utility function to format content based on output format
local function format_by_output(latex_code, html_code, other_format_content)
  if FORMAT:match 'latex' then
    return pandoc.RawBlock('latex', latex_code)
  elseif FORMAT:match 'html' then
    return pandoc.RawBlock('html', html_code)
  else
    -- Default fallback for other formats
    return other_format_content
  end
end

-- Featured Quote shortcode with validation
function Featured_Quote(args, kwargs, blocks)
  -- Validate input
  if #blocks < 1 then
    io.stderr:write("Warning: Featured quote requires at least the quote text\n")
    return pandoc.Para(pandoc.Str("[ERROR: Featured quote requires content]"))
  end
  
  local quote = pandoc.utils.stringify(blocks[1])
  local author = ""
  
  if #blocks > 1 then
    author = pandoc.utils.stringify(blocks[2])
  end
  
  -- Process any additional attributes
  local color = kwargs['color'] or "primaryorange"
  local font_size = kwargs['size'] or "normal"
  
  -- Prepare format-specific content
  local latex_code = '\\begin{featuredquote}\n' ..
                    quote .. '\n' ..
                    '\\vspace{0.5em}\\noindent\\textbf{— ' .. author .. '}\n' ..
                    '\\end{featuredquote}'
  
  local html_code = '<div class="featured-quote ' .. font_size .. '">\n' ..
                   '<blockquote>' .. quote .. '</blockquote>\n' ..
                   '<p class="attribution">— ' .. author .. '</p>\n' ..
                   '</div>'
  
  local other_content = {
    pandoc.Para {
      pandoc.Emph(pandoc.Str('"' .. quote .. '"')),
    },
    pandoc.Para {
      pandoc.Str("— " .. author)
    }
  }
  
  -- Return appropriate format
  if FORMAT:match 'latex' or FORMAT:match 'html' then
    return format_by_output(latex_code, html_code, other_content)
  else
    return other_content
  end
end

-- Case Study shortcode with validation and more flexible structure
function Case_Study(args, kwargs, blocks)
  -- Validate required inputs
  local company = kwargs['company'] or ""
  if company == "" then
    io.stderr:write("Warning: Case study requires 'company' attribute\n")
    return pandoc.Para(pandoc.Str("[ERROR: Case study requires company name]"))
  end
  
  -- Process other attributes with defaults
  local segment = kwargs['segment'] or "Industry Segment"
  local revenue = kwargs['revenue'] or "Annual Revenue"
  local challenge = kwargs['challenge'] or "Business Challenge"
  local outcome = kwargs['outcome'] or "Strategic Outcome"
  local highlight = kwargs['highlight'] or ""
  
  -- Process content
  local content_blocks = {}
  local quote_text = ""
  local quote_author = ""
  
  -- Extract quote if present
  for i = #blocks, 1, -1 do
    local block = blocks[i]
    if block.t == "BlockQuote" then
      -- Found a blockquote, extract it as the case study quote
      local quote_content = pandoc.utils.blocks_to_inlines(block.content)
      quote_text = pandoc.utils.stringify(quote_content)
      
      -- Try to find author after the quote (assuming format: "> Quote text\n> \n> — Author")
      local lines = pandoc.utils.split_string(quote_text, "\n")
      for j, line in ipairs(lines) do
        if line:match("^%s*[—%-]%s*(.+)") then
          quote_author = line:match("^%s*[—%-]%s*(.+)")
          -- Remove author line from quote text
          table.remove(lines, j)
          quote_text = table.concat(lines, "\n")
          break
        end
      end
      
      -- Remove the blockquote from blocks to process the rest as content
      table.remove(blocks, i)
      break
    end
  end
  
  -- Convert remaining blocks to string content
  local content = ""
  for _, block in ipairs(blocks) do
    content = content .. pandoc.utils.stringify(block) .. "\n\n"
  end
  
  -- Prepare formats
  local latex_code = '\\begin{case-study}{' .. company .. '}{' .. 
                     segment .. '}{' .. revenue .. '}{' .. 
                     challenge .. '}{' .. outcome .. '}\n' ..
                     '\\begin{description}\n' ..
                     '  \\item[Industry Segment:] ' .. segment .. '\n' ..
                     '  \\item[Annual Revenue:] ' .. revenue .. '\n' ..
                     '  \\item[Business Challenge:] ' .. challenge .. '\n' ..
                     '  \\item[Strategic Outcome:] ' .. outcome .. '\n' ..
                     '\\end{description}\n\n' ..
                     content .. '\n\n' ..
                     (quote_text ~= "" and 
                      '\\begin{quote}\n\\itshape "' .. quote_text .. '"\n' ..
                      '\\begin{flushright}\n— ' .. quote_author .. '\n\\end{flushright}\n\\end{quote}\n' 
                      or '') ..
                     '\\end{case-study}'
  
  local html_code = '<div class="case-study">\n' ..
                   '<h3 class="case-study-title">Industry Success Story: ' .. company .. '</h3>\n' ..
                   '<dl class="case-study-meta">\n' ..
                   '<dt>Industry Segment:</dt><dd>' .. segment .. '</dd>\n' ..
                   '<dt>Annual Revenue:</dt><dd>' .. revenue .. '</dd>\n' ..
                   '<dt>Business Challenge:</dt><dd>' .. challenge .. '</dd>\n' ..
                   '<dt>Strategic Outcome:</dt><dd>' .. outcome .. '</dd>\n' ..
                   '</dl>\n' ..
                   '<div class="case-study-content">\n' ..
                   content .. '\n' ..
                   (quote_text ~= "" and 
                    '<blockquote>\n<p>"' .. quote_text .. '"</p>\n' ..
                    '<p class="attribution">— ' .. quote_author .. '</p>\n</blockquote>\n'
                    or '') ..
                   '</div>\n</div>'
  
  -- Default content for other formats
  local other_content = {
    pandoc.Header(3, "Industry Success Story: " .. company),
    pandoc.BulletList({
      {pandoc.Plain(pandoc.Strong("Industry Segment: ") .. pandoc.Str(segment))},
      {pandoc.Plain(pandoc.Strong("Annual Revenue: ") .. pandoc.Str(revenue))},
      {pandoc.Plain(pandoc.Strong("Business Challenge: ") .. pandoc.Str(challenge))},
      {pandoc.Plain(pandoc.Strong("Strategic Outcome: ") .. pandoc.Str(outcome))}
    }),
    pandoc.Para(pandoc.Str(content))
  }
  
  if quote_text ~= "" then
    table.insert(other_content, pandoc.BlockQuote(
      {pandoc.Para(pandoc.Emph(pandoc.Str('"' .. quote_text .. '"'))),
       pandoc.Para(pandoc.Str("— " .. quote_author))}
    ))
  end
  
  -- Return appropriate format
  if FORMAT:match 'latex' or FORMAT:match 'html' then
    return format_by_output(latex_code, html_code, other_content)
  else
    return other_content
  end
end

-- Listicle shortcode with validation
function Listicle(args, kwargs, blocks)
  -- Validate input
  if #blocks < 1 then
    io.stderr:write("Warning: Listicle requires content\n")
    return pandoc.Para(pandoc.Str("[ERROR: Listicle requires content]"))
  end
  
  local title = kwargs['title'] or "Key Points"
  local style = kwargs['style'] or "" -- Optional style: numbered, bulleted, etc.
  
  -- Process blocks
  local content = ""
  for _, block in ipairs(blocks) do
    content = content .. pandoc.utils.stringify(block) .. "\n"
  end
  
  -- Format output by type
  local latex_code = '\\begin{listicle}{' .. title .. '}\n' ..
                    content .. '\n' ..
                    '\\end{listicle}'
  
  local html_code = '<div class="listicle ' .. style .. '">\n' ..
                   '<h3>' .. title .. '</h3>\n' ..
                   content .. '\n' ..
                   '</div>'
  
  local other_content = {
    pandoc.Header(3, title),
    pandoc.Para(pandoc.Str(content))
  }
  
  -- Return appropriate format
  if FORMAT:match 'latex' or FORMAT:match 'html' then
    return format_by_output(latex_code, html_code, other_content)
  else
    return other_content
  end
end

-- Figure shortcode with extended options
function Figure(args, kwargs, blocks)
  -- Validate required input
  local src = kwargs['src']
  if not src then
    io.stderr:write("Warning: Figure requires 'src' attribute\n")
    return pandoc.Para(pandoc.Str("[ERROR: Figure requires src attribute]"))
  end
  
  local caption = kwargs['caption'] or ""
  local description = kwargs['description'] or ""
  local credit = kwargs['credit'] or ""
  local width = kwargs['width'] or "80%"
  
  -- Format for output types
  local latex_code = '\\begin{si-figure}{' .. src .. '}{' .. 
                    caption .. '}{' .. description .. '}{' .. credit .. '}\n' ..
                    '\\end{si-figure}'
  
  local html_code = '<figure class="si-figure">\n' ..
                   '<img src="' .. src .. '" alt="' .. description .. 
                   '" style="max-width: ' .. width .. ';">\n' ..
                   (caption ~= "" and 
                   '<figcaption>' .. caption .. 
                   (credit ~= "" and 
                   ' <span class="credit">Credit: ' .. credit .. '</span>' or '') ..
                   '</figcaption>\n' or '') ..
                   (description ~= "" and 
                   '<p class="description"><em>' .. description .. '</em></p>\n' or '') ..
                   '</figure>'
  
  local other_content = {
    pandoc.Para(pandoc.Image(caption, src))
  }
  
  if description ~= "" or credit ~= "" then
    table.insert(other_content, pandoc.Para(
      pandoc.Emph(pandoc.Str(description .. 
      (credit ~= "" and " (Credit: " .. credit .. ")" or "")))
    ))
  end
  
  -- Return appropriate format
  if FORMAT:match 'latex' or FORMAT:match 'html' then
    return format_by_output(latex_code, html_code, other_content)
  else
    return other_content
  end
end

-- Table shortcode with extended options
function Enhanced_Table(args, kwargs, blocks)
  local title = kwargs['title'] or ""
  local content = ""
  
  -- Extract content from blocks
  for _, block in ipairs(blocks) do
    if block.t == "Table" then
      -- Found a table, use it as is
      return block
    else
      -- Otherwise concatenate content as string
      content = content .. pandoc.utils.stringify(block) .. "\n"
    end
  end
  
  -- If we reach here, we didn't find a proper table, just return the blocks
  return blocks
end

-- CodeBlock shortcode with extended options
function Code_Block(args, kwargs, blocks)
  -- Validate required input
  if #blocks < 1 then
    io.stderr:write("Warning: Code Block requires content\n")
    return pandoc.Para(pandoc.Str("[ERROR: Code Block requires content]"))
  end
  
  local title = kwargs['title'] or "Code"
  local language = kwargs['language'] or ""
  
  -- Extract code content
  local code_text = pandoc.utils.stringify(blocks[1])
  
  -- Format output
  local latex_code = '\\begin{si-code}[language=' .. language .. ']{' .. title .. '}\n' ..
                    code_text .. '\n' ..
                    '\\end{si-code}'
  
  local html_code = '<div class="code-with-title">\n' ..
                   '<div class="code-title">' .. title .. '</div>\n' ..
                   '<pre><code class="language-' .. language .. '">' ..
                   pandoc.utils.escapeHTML(code_text) ..
                   '</code></pre>\n' ..
                   '</div>'
  
  local other_content = {
    pandoc.Header(4, title),
    pandoc.CodeBlock(code_text, {class = language})
  }
  
  -- Return appropriate format
  if FORMAT:match 'latex' or FORMAT:match 'html' then
    return format_by_output(latex_code, html_code, other_content)
  else
    return other_content
  end
end

-- Executive action plan shortcode
function Action_Plan(args, kwargs, blocks)
  local title = kwargs['title'] or "Executive Action Plan"
  local content = ""
  
  -- Process blocks
  for _, block in ipairs(blocks) do
    content = content .. pandoc.utils.stringify(block) .. "\n"
  end
  
  -- Format output
  local latex_code = '\\begin{calloutimportant}{' .. title .. '}\n' ..
                    content .. '\n' ..
                    '\\end{calloutimportant}'
  
  local html_code = '<div class="callout callout-important">\n' ..
                   '<div class="callout-title">' .. title .. '</div>\n' ..
                   content .. '\n' ..
                   '</div>'
  
  local other_content = {
    pandoc.Header(4, title),
    pandoc.Para(pandoc.Str(content))
  }
  
  -- Return appropriate format
  if FORMAT:match 'latex' or FORMAT:match 'html' then
    return format_by_output(latex_code, html_code, other_content)
  else
    return other_content
  end
end

-- Stats highlight shortcode
function Stats_Highlight(args, kwargs, blocks)
  local title = kwargs['title'] or "Key Statistics"
  local content = ""
  
  -- Process blocks
  for _, block in ipairs(blocks) do
    content = content .. pandoc.utils.stringify(block) .. "\n"
  end
  
  -- Format output
  local latex_code = '\\begin{calloutnote}{' .. title .. '}\n' ..
                    content .. '\n' ..
                    '\\end{calloutnote}'
  
  local html_code = '<div class="callout callout-note">\n' ..
                   '<div class="callout-title">' .. title .. '</div>\n' ..
                   content .. '\n' ..
                   '</div>'
  
  local other_content = {
    pandoc.Header(4, title),
    pandoc.Para(pandoc.Str(content))
  }
  
  -- Return appropriate format
  if FORMAT:match 'latex' or FORMAT:match 'html' then
    return format_by_output(latex_code, html_code, other_content)
  else
    return other_content
  end
end

-- Quick tips shortcode
function Quick_Tips(args, kwargs, blocks)
  local title = kwargs['title'] or "Quick Tips"
  local content = ""
  
  -- Process blocks
  for _, block in ipairs(blocks) do
    content = content .. pandoc.utils.stringify(block) .. "\n"
  end
  
  -- Format output
  local latex_code = '\\begin{callouttip}{' .. title .. '}\n' ..
                    content .. '\n' ..
                    '\\end{callouttip}'
  
  local html_code = '<div class="callout callout-tip">\n' ..
                   '<div class="callout-title">' .. title .. '</div>\n' ..
                   content .. '\n' ..
                   '</div>'
  
  local other_content = {
    pandoc.Header(4, title),
    pandoc.Para(pandoc.Str(content))
  }
  
  -- Return appropriate format
  if FORMAT:match 'latex' or FORMAT:match 'html' then
    return format_by_output(latex_code, html_code, other_content)
  else
    return other_content
  end
end

-- Register all shortcodes
function Pandoc(doc)
  -- Register shortcodes with improved naming
  pandoc.utils.register_shortcode('featured-quote', Featured_Quote)
  pandoc.utils.register_shortcode('case-study', Case_Study)
  pandoc.utils.register_shortcode('listicle', Listicle)
  pandoc.utils.register_shortcode('figure', Figure)
  pandoc.utils.register_shortcode('enhanced-table', Enhanced_Table)
  pandoc.utils.register_shortcode('code-block', Code_Block)
  pandoc.utils.register_shortcode('action-plan', Action_Plan)
  pandoc.utils.register_shortcode('stats-highlight', Stats_Highlight)
  pandoc.utils.register_shortcode('quick-tips', Quick_Tips)
  
  return doc
end

return {
  {Pandoc = Pandoc}
}