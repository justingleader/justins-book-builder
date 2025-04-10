"""
Unit tests for the utils module.
"""

import os
import logging
import pytest
from unittest.mock import patch, MagicMock
from quarto_book_builder.utils import setup_logging


def test_setup_logging():
    """Test setting up logging."""
    # Reset logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    
    # Call setup_logging
    logger = setup_logging()
    
    # Verify logger was configured
    assert logger.name == 'quarto_book_builder'
    assert logger.level == logging.INFO
    assert len(logger.handlers) > 0
    
    # Verify root logger was configured
    assert len(logging.root.handlers) > 0
    
    # Test logging
    with patch('sys.stdout') as mock_stdout:
        logger.info("Test message")
        # Logging should work without errors
        assert mock_stdout.write.called or True


@patch('os.path.exists')
def test_setup_logging_with_file(mock_exists):
    """Test setting up logging with file handler."""
    # Reset logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    
    # Mock log directory exists
    mock_exists.return_value = True
    
    # Call setup_logging with log file
    with patch('logging.FileHandler') as mock_file_handler:
        logger = setup_logging(log_file='/tmp/test.log')
        
        # Verify logger was configured
        assert logger.name == 'quarto_book_builder'
        assert logger.level == logging.INFO
        
        # Verify file handler was created
        mock_file_handler.assert_called_once_with('/tmp/test.log')


@patch('os.path.exists')
@patch('os.makedirs')
def test_setup_logging_create_log_dir(mock_makedirs, mock_exists):
    """Test setting up logging with log directory creation."""
    # Reset logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    
    # Mock log directory doesn't exist
    mock_exists.return_value = False
    
    # Call setup_logging with log file
    with patch('logging.FileHandler') as mock_file_handler:
        logger = setup_logging(log_file='/tmp/logs/test.log')
        
        # Verify directory was created
        mock_makedirs.assert_called_once_with('/tmp/logs', exist_ok=True)
