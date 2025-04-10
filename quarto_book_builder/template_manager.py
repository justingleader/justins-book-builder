"""
Enhanced template manager for the Quarto Book Builder.
"""

import os
import re
import logging
import yaml
from pathlib import Path

logger = logging.getLogger(__name__)


class TemplateManager:
    """Manages custom section templates and their application."""
    
    def __init__(self, config):
        """Initialize the template manager.
        
        Args:
            config (dict): Configuration dictionary containing custom section templates
        """
        self.config = config
        self.templates = config.get('custom_sections', {})
        self.template_dir = config.get('template_dir', 'templates')
        
        # Load external templates if specified
        self._load_external_templates()
        
    def _load_external_templates(self):
        """Load templates from external files if available."""
        if not os.path.exists(self.template_dir):
            logger.info(f"Template directory {self.template_dir} does not exist, using inline templates only")
            return
            
        logger.info(f"Loading templates from {self.template_dir}")
        
        # Look for template files
        for file in os.listdir(self.template_dir):
            if file.endswith(('.yaml', '.yml')):
                try:
                    file_path = os.path.join(self.template_dir, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        templates = yaml.safe_load(f)
                        
                    if isinstance(templates, dict):
                        # Merge with existing templates
                        for name, template in templates.items():
                            if name in self.templates:
                                logger.warning(f"Template '{name}' from {file} overrides existing template")
                            self.templates[name] = template
                            logger.info(f"Loaded template '{name}' from {file}")
                except Exception as e:
                    logger.error(f"Error loading templates from {file}: {str(e)}")
                    
        # Look for individual template files
        for section_name in list(self.templates.keys()):
            # Check for HTML template
            html_file = os.path.join(self.template_dir, f"{section_name}.html")
            if os.path.exists(html_file):
                try:
                    with open(html_file, 'r', encoding='utf-8') as f:
                        self.templates[section_name]['html'] = f.read()
                    logger.info(f"Loaded HTML template for '{section_name}' from {html_file}")
                except Exception as e:
                    logger.error(f"Error loading HTML template for '{section_name}': {str(e)}")
                    
            # Check for LaTeX template
            latex_file = os.path.join(self.template_dir, f"{section_name}.tex")
            if os.path.exists(latex_file):
                try:
                    with open(latex_file, 'r', encoding='utf-8') as f:
                        self.templates[section_name]['latex'] = f.read()
                    logger.info(f"Loaded LaTeX template for '{section_name}' from {latex_file}")
                except Exception as e:
                    logger.error(f"Error loading LaTeX template for '{section_name}': {str(e)}")
        
    def apply_template(self, section_name, content, output_format='html'):
        """Apply template to content for specified output format.
        
        Args:
            section_name (str): Name of the custom section
            content (str): Content to apply the template to
            output_format (str): Output format ('html' or 'latex')
            
        Returns:
            str: Content with template applied, or original content if no template exists
        """
        if section_name not in self.templates:
            logger.warning(f"No template found for section '{section_name}'")
            return content
            
        template = self.templates[section_name].get(output_format)
        if not template:
            logger.warning(f"No {output_format} template found for section '{section_name}'")
            return content
            
        # Extract variables from content
        variables = self._extract_variables(content, section_name)
        
        # Replace placeholders in template
        result = template
        
        # Replace content placeholder
        result = result.replace('{{ content }}', variables.get('content', content))
        
        # Replace other variables
        for key, value in variables.items():
            if key != 'content':
                result = result.replace(f"{{ {key} }}", value)
            
        return result
    
    def _extract_variables(self, content, section_name):
        """Extract variables from content.
        
        Args:
            content (str): Content to extract variables from
            section_name (str): Name of the section (for specific extraction logic)
            
        Returns:
            dict: Dictionary of variables
        """
        variables = {'content': content}
        
        # Extract author for quotes
        if section_name in ('featured-quote', 'quote'):
            # Look for author attribution
            author_match = re.search(r'\*\*—\s*([^*]+)\*\*', content)
            if author_match:
                author = author_match.group(1).strip()
                variables['author'] = author
                
                # Remove author from content
                content = content.replace(author_match.group(0), '').strip()
                variables['content'] = content
        
        # Extract title for listicles or other sections with headings
        if section_name in ('listicle', 'featured'):
            # Look for heading
            heading_match = re.search(r'^#+\s+(.+)$', content, re.MULTILINE)
            if heading_match:
                title = heading_match.group(1).strip()
                variables['title'] = title
        
        return variables
        
    def get_available_sections(self):
        """Get list of available custom section names.
        
        Returns:
            list: List of custom section names
        """
        return list(self.templates.keys())
    
    def get_template_info(self, section_name=None):
        """Get information about templates.
        
        Args:
            section_name (str, optional): Name of specific section to get info for
            
        Returns:
            dict: Template information
        """
        if section_name:
            if section_name in self.templates:
                return {
                    'name': section_name,
                    'formats': list(self.templates[section_name].keys())
                }
            return None
            
        # Return info for all templates
        result = []
        for name, template in self.templates.items():
            result.append({
                'name': name,
                'formats': list(template.keys())
            })
        return result
    
    def add_template(self, name, html_template=None, latex_template=None):
        """Add a new template.
        
        Args:
            name (str): Template name
            html_template (str, optional): HTML template
            latex_template (str, optional): LaTeX template
            
        Returns:
            bool: True if template was added
        """
        if not name:
            return False
            
        if name not in self.templates:
            self.templates[name] = {}
            
        if html_template:
            self.templates[name]['html'] = html_template
            
        if latex_template:
            self.templates[name]['latex'] = latex_template
            
        return True
    
    def save_templates(self):
        """Save templates to configuration.
        
        Returns:
            bool: True if templates were saved
        """
        self.config['custom_sections'] = self.templates
        
        # If config has a save method, use it
        if hasattr(self.config, 'save'):
            return self.config.save()
            
        return True
