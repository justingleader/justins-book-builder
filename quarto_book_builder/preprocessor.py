"""
Enhanced Markdown preprocessor for the Quarto Book Builder.
"""

import os
import re
import logging
import yaml
from pathlib import Path

logger = logging.getLogger(__name__)


class MarkdownPreprocessor:
    """Processes Markdown files to handle special tags."""
    
    # Regex patterns for special tags
    IMAGE_TAG_PATTERN = r'\{\{image:\s*([^}]+)\}\}'
    SECTION_START_PATTERN = r':::\s*([a-zA-Z0-9_-]+)\s*\n'
    SECTION_END_PATTERN = r'\n\s*:::\s*\n'
    YAML_FRONTMATTER_PATTERN = r'^---\n(.*?)\n---'
    
    def __init__(self, config, image_generator, template_manager):
        """Initialize the Markdown preprocessor.
        
        Args:
            config (dict): Configuration dictionary
            image_generator (ImageGenerator): Image generator instance
            template_manager (TemplateManager): Template manager instance
        """
        self.config = config
        self.image_generator = image_generator
        self.template_manager = template_manager
        self.project_dir = os.path.dirname(os.path.abspath(config.get('config_path', '.')))
        self.build_dir = os.path.join(self.project_dir, config.get('build_dir', '_build'))
        self.image_dir = os.path.join(self.project_dir, config.get('image_dir', 'images'))
        
        # Ensure directories exist
        os.makedirs(self.build_dir, exist_ok=True)
        os.makedirs(self.image_dir, exist_ok=True)
        
        # Store document metadata from files
        self.document_metadata = {}
        
    def process_project(self):
        """Process all Markdown files in the project.
        
        Returns:
            list: List of processed file paths
        """
        processed_files = []
        
        # Process all Markdown files
        for root, _, files in os.walk(self.project_dir):
            for file in files:
                if file.endswith(('.md', '.qmd')):
                    input_path = os.path.join(root, file)
                    
                    # Skip files in build directory
                    if self.build_dir in input_path:
                        continue
                        
                    # Create relative path for output
                    rel_path = os.path.relpath(input_path, self.project_dir)
                    output_path = os.path.join(self.build_dir, rel_path)
                    
                    # Process file
                    if self.process_file(input_path, output_path):
                        processed_files.append(output_path)
        
        # Create a _quarto.yml file with extracted metadata
        self.generate_quarto_config()
                    
        return processed_files
        
    def process_file(self, input_path, output_path):
        """Process a single Markdown file.
        
        Args:
            input_path (str): Path to the input Markdown file
            output_path (str): Path to write the processed output
            
        Returns:
            bool: True if processing was successful
        """
        logger.info(f"Processing file: {input_path}")
        
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract metadata from frontmatter
            metadata, content_without_frontmatter = self.extract_metadata(content)
            if metadata:
                # Store metadata with the file path as key
                self.document_metadata[input_path] = metadata
                logger.info(f"Extracted metadata: {metadata}")
                
                # For index files or specified main files, use metadata for book properties
                if os.path.basename(input_path) == 'index.md' or os.path.basename(input_path) == 'index.qmd':
                    logger.info(f"Using metadata from index file for book properties")
                    
            # Process image tags
            processed_content, image_count = self.process_image_tags(content)
            logger.info(f"Processed {image_count} image tags")
            
            # Process custom section tags
            processed_content, section_count = self.process_section_tags(processed_content)
            logger.info(f"Processed {section_count} custom section tags")
            
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Write processed content
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(processed_content)
                
            logger.info(f"Processed file written to: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error processing file {input_path}: {str(e)}")
            return False
            
    def process_image_tags(self, content):
        """Find and replace image tags with Markdown image syntax.
        
        Args:
            content (str): Markdown content
            
        Returns:
            tuple: (processed_content, image_count)
        """
        image_count = 0
        
        def replace_image_tag(match):
            nonlocal image_count
            prompt = match.group(1).strip()
            logger.info(f"Found image prompt: {prompt}")
            
            try:
                # Generate image
                image_path = self.image_generator.generate_image(prompt)
                
                # Create relative path for Markdown
                rel_path = os.path.join(self.config.get('image_dir', 'images'), 
                                       os.path.basename(image_path))
                
                # Increment counter
                image_count += 1
                
                # Return Markdown image syntax
                return f"![{prompt}]({rel_path})"
                
            except Exception as e:
                logger.error(f"Error generating image for prompt '{prompt}': {str(e)}")
                return f"**[Image failed to generate: {prompt}]**"
        
        # Replace all image tags
        processed_content = re.sub(self.IMAGE_TAG_PATTERN, replace_image_tag, content)
        
        return processed_content, image_count
        
    def process_section_tags(self, content):
        """Find and replace custom section tags with templates.
        
        Args:
            content (str): Markdown content
            
        Returns:
            tuple: (processed_content, section_count)
        """
        section_count = 0
        
        # Find all section blocks
        current_pos = 0
        result = []
        
        while True:
            # Find start of section
            start_match = re.search(self.SECTION_START_PATTERN, content[current_pos:])
            if not start_match:
                # No more sections, add remaining content
                result.append(content[current_pos:])
                break
                
            # Add content before section
            result.append(content[current_pos:current_pos + start_match.start()])
            
            # Get section name
            section_name = start_match.group(1).strip()
            logger.info(f"Found section: {section_name}")
            
            # Find end of section
            section_start_pos = current_pos + start_match.end()
            end_match = re.search(self.SECTION_END_PATTERN, content[section_start_pos:])
            
            if not end_match:
                # No end marker found, treat rest of content as section
                section_content = content[section_start_pos:]
                current_pos = len(content)
            else:
                # Extract section content
                section_content = content[section_start_pos:section_start_pos + end_match.start()]
                current_pos = section_start_pos + end_match.end()
            
            # Apply template for HTML
            html_content = self.template_manager.apply_template(section_name, section_content, 'html')
            
            # Apply template for LaTeX
            latex_content = self.template_manager.apply_template(section_name, section_content, 'latex')
            
            # Add HTML comment for HTML output
            result.append(f"<!--begin-{section_name}-->\n{html_content}\n<!--end-{section_name}-->\n")
            
            # Add LaTeX raw block for PDF output
            result.append(f"```{{=latex}}\n{latex_content}\n```\n")
            
            # Increment counter
            section_count += 1
        
        return ''.join(result), section_count
    
    def extract_metadata(self, content):
        """Extract YAML metadata from Markdown content.
        
        Args:
            content (str): Markdown content
            
        Returns:
            tuple: (metadata_dict, content_without_metadata)
        """
        # Check for YAML front matter using regex to handle multiline
        yaml_match = re.match(self.YAML_FRONTMATTER_PATTERN, content, re.DOTALL)
        if yaml_match:
            # Extract front matter
            front_matter = yaml_match.group(1)
            content_without_frontmatter = content[yaml_match.end():]
            
            try:
                # Parse YAML
                metadata = yaml.safe_load(front_matter)
                if not isinstance(metadata, dict):
                    metadata = {}
                    
                # Return metadata and content without front matter
                return metadata, content_without_frontmatter
            except Exception as e:
                logger.warning(f"Failed to parse YAML front matter: {str(e)}")
        
        # No metadata or parsing failed
        return {}, content
    
    def generate_quarto_config(self):
        """Generate a Quarto configuration file with extracted metadata.
        
        This creates a _quarto.yml file in the build directory with title and author
        from the markdown files' frontmatter.
        """
        try:
            # Start with the base config
            quarto_config = {}
            
            # Copy existing quarto config if available
            original_config_path = os.path.join(self.project_dir, '_quarto.yml')
            if os.path.exists(original_config_path):
                with open(original_config_path, 'r') as f:
                    quarto_config = yaml.safe_load(f) or {}
            
            # Ensure book section exists
            if 'book' not in quarto_config:
                quarto_config['book'] = {}
                
            # Look for index files to extract title and author
            for filepath, metadata in self.document_metadata.items():
                if os.path.basename(filepath) in ('index.md', 'index.qmd'):
                    # Apply metadata from index file if available
                    if 'title' in metadata and 'title' not in quarto_config['book']:
                        quarto_config['book']['title'] = metadata['title']
                    if 'author' in metadata and 'author' not in quarto_config['book']:
                        quarto_config['book']['author'] = metadata['author']
                    if 'date' in metadata and 'date' not in quarto_config['book']:
                        quarto_config['book']['date'] = metadata['date']
                    break
            
            # Write the updated config
            build_config_path = os.path.join(self.build_dir, '_quarto.yml')
            with open(build_config_path, 'w') as f:
                yaml.dump(quarto_config, f, default_flow_style=False)
                
            logger.info(f"Generated Quarto config at {build_config_path}")
            
        except Exception as e:
            logger.error(f"Error generating Quarto config: {str(e)}")
    
    def copy_static_files(self):
        """Copy static files (images, etc.) to build directory.
        
        Returns:
            int: Number of files copied
        """
        count = 0
        
        # Copy images
        if os.path.exists(self.image_dir):
            build_image_dir = os.path.join(self.build_dir, os.path.basename(self.image_dir))
            os.makedirs(build_image_dir, exist_ok=True)
            
            for file in os.listdir(self.image_dir):
                src = os.path.join(self.image_dir, file)
                dst = os.path.join(build_image_dir, file)
                
                if os.path.isfile(src):
                    import shutil
                    shutil.copy2(src, dst)
                    count += 1
        
        return count
