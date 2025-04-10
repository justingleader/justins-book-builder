"""
Enhanced utils module with improved logging and error handling.
"""

import os
import sys
import logging
from pathlib import Path


def setup_logging(log_file=None, log_level=logging.INFO):
    """Set up logging configuration.
    
    Args:
        log_file (str, optional): Path to log file
        log_level (int, optional): Logging level
        
    Returns:
        logging.Logger: Configured logger
    """
    # Create logger
    logger = logging.getLogger('quarto_book_builder')
    logger.setLevel(log_level)
    
    # Remove existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    
    # Add console handler to logger
    logger.addHandler(console_handler)
    
    # Add file handler if specified
    if log_file:
        # Create log directory if it doesn't exist
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
            
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    # Configure root logger
    root_logger = logging.getLogger()
    if not root_logger.handlers:
        root_handler = logging.StreamHandler()
        root_handler.setLevel(logging.WARNING)
        root_handler.setFormatter(formatter)
        root_logger.addHandler(root_handler)
    
    return logger


def safe_mkdir(directory):
    """Safely create a directory if it doesn't exist.
    
    Args:
        directory (str): Directory path to create
        
    Returns:
        bool: True if directory exists or was created
    """
    try:
        os.makedirs(directory, exist_ok=True)
        return True
    except Exception as e:
        logging.error(f"Failed to create directory {directory}: {str(e)}")
        return False


def get_file_extension(file_path):
    """Get the extension of a file.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        str: File extension without the dot
    """
    return os.path.splitext(file_path)[1][1:].lower()


def is_markdown_file(file_path):
    """Check if a file is a Markdown file.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        bool: True if the file is a Markdown file
    """
    return get_file_extension(file_path) in ('md', 'qmd', 'markdown')


def is_image_file(file_path):
    """Check if a file is an image file.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        bool: True if the file is an image file
    """
    return get_file_extension(file_path) in ('png', 'jpg', 'jpeg', 'gif', 'svg')


def sanitize_filename(filename):
    """Sanitize a filename to be safe for all operating systems.
    
    Args:
        filename (str): Filename to sanitize
        
    Returns:
        str: Sanitized filename
    """
    # Replace invalid characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Ensure filename is not too long
    if len(filename) > 255:
        base, ext = os.path.splitext(filename)
        filename = base[:255-len(ext)] + ext
    
    return filename


def check_quarto_installation():
    """Check if Quarto is installed.
    
    Returns:
        tuple: (is_installed, version_string)
    """
    try:
        import subprocess
        result = subprocess.run(
            ['quarto', '--version'], 
            check=True, 
            capture_output=True, 
            text=True
        )
        version = result.stdout.strip()
        return True, version
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False, None
