#!/usr/bin/env python3
"""
Build script for Quarto Book using metadata from Markdown files.
This script processes all markdown files, extracts metadata, and renders the book.
"""

import os
import sys
import yaml
import subprocess
import logging
from pathlib import Path

# Add parent directory to the path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

try:
    # Import the necessary components
    from quarto_book_builder.config import ConfigManager
    from quarto_book_builder.image_generator import ImageGenerator
    from quarto_book_builder.preprocessor import MarkdownPreprocessor
    from quarto_book_builder.template_manager import TemplateManager
    from quarto_book_builder.quarto import QuartoRenderer
except ImportError as e:
    logger.error(f"Failed to import required module: {e}")
    sys.exit(1)

def main():
    """Main function to build the book."""
    logger.info("Starting book build process...")
    
    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.yaml")
    
    try:
        # Load configuration
        logger.info(f"Loading configuration from {config_path}")
        config_manager = ConfigManager(config_path)
        config = config_manager.load()
        
        # Set up working directory
        os.chdir(script_dir)
        
        # Initialize components
        logger.info("Initializing components...")
        image_generator = ImageGenerator(config)
        template_manager = TemplateManager(config)
        preprocessor = MarkdownPreprocessor(config, image_generator, template_manager)
        
        # Process markdown files
        logger.info("Processing markdown files...")
        processed_files = preprocessor.process_project()
        logger.info(f"Processed {len(processed_files)} files")
        
        # Copy static files (images, etc.)
        copied_files = preprocessor.copy_static_files()
        logger.info(f"Copied {copied_files} static files")
        
        # Render the book
        logger.info("Rendering book with Quarto...")
        quarto = QuartoRenderer(config)
        
        # Check Quarto installation
        installed, version = quarto.check_quarto_installation()
        if not installed:
            logger.error("Quarto is not installed. Please install Quarto: https://quarto.org/docs/get-started/")
            return
        logger.info(f"Using Quarto version: {version}")
        
        # Render in all formats
        formats = ["pdf", "epub", "html"]
        for fmt in formats:
            logger.info(f"Rendering book in {fmt} format...")
            try:
                quarto.render(preprocessor.build_dir, [fmt])
                logger.info(f"Successfully rendered {fmt} format")
            except Exception as e:
                logger.error(f"Failed to render {fmt} format: {e}")
        
        # List output files
        output_files = quarto.get_output_files()
        logger.info("Output files:")
        for fmt, files in output_files.items():
            for f in files:
                logger.info(f"  {fmt}: {f}")
        
        logger.info("Book build completed successfully")
        
    except Exception as e:
        logger.error(f"Error building book: {e}", exc_info=True)
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 