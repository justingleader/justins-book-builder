"""
Enhanced configuration handling for the Quarto Book Builder.
"""

import os
import yaml
import logging
from .utils import setup_logging

logger = logging.getLogger(__name__)


class ConfigManager:
    """Handles loading and validating the user's configuration from YAML files."""
    
    DEFAULT_CONFIG = {
        'image_dir': 'images',
        'image_size': '1024x1024',
        'image_format': 'png',
        'build_dir': '_build',
        'output_dir': '_book',
        'custom_sections': {}
    }
    
    def __init__(self, config_path):
        """Initialize the configuration manager.
        
        Args:
            config_path (str): Path to the configuration file
        """
        self.config_path = config_path
        self.config = None
        self.quarto_config = None
        
    def load(self):
        """Load configuration from YAML file.
        
        Returns:
            dict: The loaded configuration
        
        Raises:
            FileNotFoundError: If the configuration file does not exist
            yaml.YAMLError: If the configuration file is not valid YAML
        """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        
        with open(self.config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        # Apply default values
        self._apply_defaults()
        
        # Validate configuration
        self.validate()
        
        # Load Quarto configuration if available
        self._load_quarto_config()
        
        return self.config
    
    def _apply_defaults(self):
        """Apply default values to configuration."""
        if self.config is None:
            self.config = {}
            
        # Apply default values for missing keys
        for key, value in self.DEFAULT_CONFIG.items():
            if key not in self.config:
                self.config[key] = value
                
    def _load_quarto_config(self):
        """Load Quarto configuration if available."""
        # Determine project directory from config file path
        project_dir = os.path.dirname(os.path.abspath(self.config_path))
        quarto_config_path = os.path.join(project_dir, '_quarto.yml')
        
        if os.path.exists(quarto_config_path):
            try:
                with open(quarto_config_path, 'r') as f:
                    self.quarto_config = yaml.safe_load(f)
                logger.info(f"Loaded Quarto configuration from {quarto_config_path}")
            except Exception as e:
                logger.warning(f"Failed to load Quarto configuration: {str(e)}")
        else:
            logger.warning(f"Quarto configuration not found at {quarto_config_path}")
        
    def validate(self):
        """Validate configuration.
        
        Raises:
            ValueError: If required configuration is missing or invalid
        """
        if not self.config:
            raise ValueError("Configuration is empty")
        
        # Check for OpenAI API key
        if 'openai_api_key' not in self.config:
            raise ValueError("OpenAI API key is required in configuration")
        
        # Validate image directory
        image_dir = self.config.get('image_dir')
        if not image_dir:
            raise ValueError("Image directory must be specified")
        
        # Validate custom section templates if present
        if 'custom_sections' in self.config:
            for section_name, section_config in self.config['custom_sections'].items():
                if not isinstance(section_config, dict):
                    raise ValueError(f"Custom section '{section_name}' must be a dictionary")
                
                # At least one format (html or latex) should be defined
                if 'html' not in section_config and 'latex' not in section_config:
                    raise ValueError(f"Custom section '{section_name}' must define at least one format (html or latex)")
        
        return True
    
    def get_book_metadata(self):
        """Get book metadata from Quarto configuration.
        
        Returns:
            dict: Book metadata (title, author, date)
        """
        metadata = {
            'title': 'Untitled Book',
            'author': 'Unknown Author',
            'date': ''
        }
        
        if self.quarto_config and 'book' in self.quarto_config:
            book_config = self.quarto_config['book']
            if 'title' in book_config:
                metadata['title'] = book_config['title']
            if 'author' in book_config:
                metadata['author'] = book_config['author']
            if 'date' in book_config:
                metadata['date'] = book_config['date']
                
        return metadata
    
    def get_chapter_files(self):
        """Get list of chapter files from Quarto configuration.
        
        Returns:
            list: List of chapter file paths
        """
        if self.quarto_config and 'book' in self.quarto_config and 'chapters' in self.quarto_config['book']:
            return self.quarto_config['book']['chapters']
        return []
    
    def get_output_formats(self):
        """Get list of output formats from Quarto configuration.
        
        Returns:
            list: List of output formats
        """
        formats = []
        if self.quarto_config and 'format' in self.quarto_config:
            formats = list(self.quarto_config['format'].keys())
        return formats
    
    def save(self):
        """Save configuration to file.
        
        Returns:
            bool: True if save was successful
        """
        try:
            with open(self.config_path, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False)
            logger.info(f"Configuration saved to {self.config_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to save configuration: {str(e)}")
            return False
    
    def update(self, key, value):
        """Update configuration value.
        
        Args:
            key (str): Configuration key
            value: Configuration value
            
        Returns:
            bool: True if update was successful
        """
        if self.config is None:
            self.load()
            
        self.config[key] = value
        return self.save()
