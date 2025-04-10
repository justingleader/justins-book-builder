"""
EPUB output formatting for the Quarto Book Builder.
"""

import os
import logging
import yaml
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)


class EPUBFormatter:
    """Handles EPUB-specific formatting and configuration."""
    
    def __init__(self, config):
        """Initialize the EPUB formatter.
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.project_dir = os.path.dirname(os.path.abspath(config.get('config_path', '.')))
        self.build_dir = os.path.join(self.project_dir, config.get('build_dir', '_build'))
        
        # EPUB-specific settings
        self.epub_settings = config.get('epub', {})
        if not self.epub_settings:
            self.epub_settings = {
                'toc': True,
                'toc-depth': 3,
                'number-sections': True,
                'css': 'epub.css'
            }
        
    def configure_epub_output(self):
        """Configure EPUB output settings in Quarto configuration.
        
        Returns:
            bool: True if configuration was successful
        """
        logger.info("Configuring EPUB output settings")
        
        # Path to Quarto configuration file
        quarto_config_path = os.path.join(self.build_dir, '_quarto.yml')
        
        try:
            # Load existing Quarto configuration
            if os.path.exists(quarto_config_path):
                with open(quarto_config_path, 'r', encoding='utf-8') as f:
                    quarto_config = yaml.safe_load(f)
            else:
                # Create new configuration if it doesn't exist
                quarto_config = {
                    'project': {'type': 'book'},
                    'book': {},
                    'format': {}
                }
            
            # Ensure format section exists
            if 'format' not in quarto_config:
                quarto_config['format'] = {}
                
            # Update EPUB format settings
            quarto_config['format']['epub'] = self.epub_settings
            
            # Write updated configuration
            with open(quarto_config_path, 'w', encoding='utf-8') as f:
                yaml.dump(quarto_config, f, default_flow_style=False)
                
            logger.info(f"Updated EPUB configuration in {quarto_config_path}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to configure EPUB output: {str(e)}")
            return False
            
    def create_epub_css(self):
        """Create or update CSS for EPUB output.
        
        Returns:
            bool: True if CSS creation was successful
        """
        # Check if custom CSS is specified
        css_file = self.epub_settings.get('css')
        if not css_file:
            logger.info("No custom CSS specified, using Quarto defaults")
            return True
            
        # Path to CSS file
        css_path = os.path.join(self.project_dir, css_file)
        
        # If CSS doesn't exist, create a default one
        if not os.path.exists(css_path):
            logger.info(f"Creating default EPUB CSS at {css_path}")
            
            # Create directory if needed
            os.makedirs(os.path.dirname(css_path), exist_ok=True)
            
            # Write default CSS
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(self._get_default_epub_css())
                
        # Copy CSS to build directory
        build_css_path = os.path.join(self.build_dir, os.path.basename(css_path))
        shutil.copy2(css_path, build_css_path)
        logger.info(f"Copied EPUB CSS to {build_css_path}")
        
        return True
        
    def _get_default_epub_css(self):
        """Get default EPUB CSS content.
        
        Returns:
            str: Default EPUB CSS
        """
        return """/* Default CSS for EPUB output */

/* General styling */
body {
  font-family: serif;
  line-height: 1.5;
  margin: 0;
  padding: 0;
  max-width: 100%;
}

h1, h2, h3, h4, h5, h6 {
  font-family: sans-serif;
  margin-top: 1.5em;
  margin-bottom: 0.5em;
}

h1 {
  font-size: 2em;
  border-bottom: 1px solid #eee;
  padding-bottom: 0.3em;
}

h2 {
  font-size: 1.5em;
}

h3 {
  font-size: 1.3em;
}

p {
  margin-top: 0.5em;
  margin-bottom: 0.5em;
}

/* Images */
img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 1em auto;
}

/* Code blocks */
pre {
  background-color: #f8f8f8;
  border: 1px solid #ddd;
  padding: 0.5em;
  overflow-x: auto;
  font-size: 0.9em;
  line-height: 1.4;
}

code {
  font-family: monospace;
  background-color: #f8f8f8;
  padding: 0.1em 0.3em;
  border-radius: 3px;
  font-size: 0.9em;
}

/* Tables */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 1em 0;
}

th, td {
  border: 1px solid #ddd;
  padding: 0.5em;
}

th {
  background-color: #f8f8f8;
  font-weight: bold;
}

/* Blockquotes */
blockquote {
  border-left: 4px solid #ddd;
  padding-left: 1em;
  margin-left: 0;
  color: #666;
}

/* Custom section styles */
.featured-quote {
  background-color: #f8f8f8;
  border-left: 4px solid #666;
  padding: 1em;
  margin: 1em 0;
}

.featured-quote blockquote {
  border-left: none;
  padding-left: 0;
  font-style: italic;
}

.featured-quote .attribution {
  text-align: right;
  font-weight: bold;
  margin-top: 0.5em;
}

.listicle {
  background-color: #f9f9f9;
  border: 1px solid #eee;
  padding: 1em;
  margin: 1em 0;
}

.listicle h3 {
  margin-top: 0;
  color: #333;
}

/* Table of contents */
nav.toc ol {
  padding-left: 1.5em;
}

nav.toc li {
  margin-bottom: 0.5em;
}
"""
        
    def configure_epub_metadata(self, title=None, author=None, date=None, cover_image=None):
        """Configure EPUB metadata.
        
        Args:
            title (str, optional): Book title
            author (str, optional): Book author
            date (str, optional): Book date
            cover_image (str, optional): Path to cover image
            
        Returns:
            bool: True if configuration was successful
        """
        quarto_config_path = os.path.join(self.build_dir, '_quarto.yml')
        
        try:
            # Load existing Quarto configuration
            if os.path.exists(quarto_config_path):
                with open(quarto_config_path, 'r', encoding='utf-8') as f:
                    quarto_config = yaml.safe_load(f)
            else:
                return False
                
            # Ensure book section exists
            if 'book' not in quarto_config:
                quarto_config['book'] = {}
                
            # Update metadata if provided
            if title:
                quarto_config['book']['title'] = title
            if author:
                quarto_config['book']['author'] = author
            if date:
                quarto_config['book']['date'] = date
                
            # Update cover image if provided
            if cover_image:
                quarto_config['book']['cover-image'] = cover_image
                
                # Also set in EPUB format section
                if 'format' not in quarto_config:
                    quarto_config['format'] = {}
                if 'epub' not in quarto_config['format']:
                    quarto_config['format']['epub'] = {}
                    
                quarto_config['format']['epub']['cover-image'] = cover_image
                
            # Write updated configuration
            with open(quarto_config_path, 'w', encoding='utf-8') as f:
                yaml.dump(quarto_config, f, default_flow_style=False)
                
            logger.info(f"Updated EPUB metadata in {quarto_config_path}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to configure EPUB metadata: {str(e)}")
            return False
            
    def validate_epub(self, epub_path):
        """Validate EPUB file using epubcheck if available.
        
        Args:
            epub_path (str): Path to EPUB file
            
        Returns:
            bool: True if validation was successful or skipped
        """
        if not os.path.exists(epub_path):
            logger.error(f"EPUB file not found: {epub_path}")
            return False
            
        # Check if epubcheck is available
        try:
            result = subprocess.run(['which', 'epubcheck'], capture_output=True, text=True)
            epubcheck_path = result.stdout.strip()
            
            if not epubcheck_path:
                logger.warning("epubcheck not found, skipping validation")
                return True
                
            # Run epubcheck
            logger.info(f"Validating EPUB file: {epub_path}")
            result = subprocess.run(
                ['epubcheck', epub_path],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                logger.info("EPUB validation successful")
                return True
            else:
                logger.error(f"EPUB validation failed: {result.stderr}")
                return False
                
        except Exception as e:
            logger.warning(f"Failed to run epubcheck: {str(e)}")
            return True  # Skip validation on error
            
    def ensure_kindle_compatibility(self):
        """Ensure EPUB is compatible with Kindle (KDP).
        
        Returns:
            bool: True if configuration was successful
        """
        # KDP requires EPUB 3 format
        quarto_config_path = os.path.join(self.build_dir, '_quarto.yml')
        
        try:
            # Load existing Quarto configuration
            if os.path.exists(quarto_config_path):
                with open(quarto_config_path, 'r', encoding='utf-8') as f:
                    quarto_config = yaml.safe_load(f)
            else:
                return False
                
            # Ensure format section exists
            if 'format' not in quarto_config:
                quarto_config['format'] = {}
            if 'epub' not in quarto_config['format']:
                quarto_config['format']['epub'] = {}
                
            # Set EPUB version to 3.0
            quarto_config['format']['epub']['epub-version'] = '3.0'
            
            # Write updated configuration
            with open(quarto_config_path, 'w', encoding='utf-8') as f:
                yaml.dump(quarto_config, f, default_flow_style=False)
                
            logger.info(f"Updated EPUB configuration for Kindle compatibility")
            return True
            
        except Exception as e:
            logger.error(f"Failed to configure EPUB for Kindle compatibility: {str(e)}")
            return False
