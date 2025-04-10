"""
Quarto Book Builder - Module Documentation

This module provides a CLI tool for building books with Quarto and AI-generated images.
"""

__version__ = "0.1.0"

# Import main modules for easier access
from .cli import cli
from .config import ConfigManager
from .preprocessor import MarkdownPreprocessor
from .image_generator import ImageGenerator
from .template_manager import TemplateManager
from .quarto import QuartoRenderer
from .pdf_formatter import PDFFormatter
from .epub_formatter import EPUBFormatter
from .utils import setup_logging

# Set up logging
logger = setup_logging()

# Define the main entry point
def main():
    """Main entry point for the CLI."""
    cli()
