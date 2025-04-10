"""
Unit tests for the EPUB formatter module.
"""

import os
import pytest
from unittest.mock import patch, mock_open, MagicMock
from quarto_book_builder.epub_formatter import EPUBFormatter


@pytest.fixture
def mock_config():
    """Create a mock configuration for testing."""
    return {
        'config_path': '/home/user/project/config.yaml',
        'build_dir': '_build',
        'epub': {
            'toc': True,
            'toc-depth': 3,
            'number-sections': True,
            'css': 'epub.css'
        }
    }


@pytest.fixture
def epub_formatter(mock_config):
    """Create an EPUB formatter instance with mock configuration."""
    return EPUBFormatter(mock_config)


def test_init(mock_config):
    """Test initialization of EPUBFormatter."""
    formatter = EPUBFormatter(mock_config)
    
    assert formatter.project_dir == '/home/user/project'
    assert formatter.build_dir == '/home/user/project/_build'
    assert formatter.epub_settings == mock_config['epub']


def test_init_default_epub_settings():
    """Test initialization with default EPUB settings."""
    config = {
        'config_path': '/home/user/project/config.yaml',
        'build_dir': '_build'
    }
    formatter = EPUBFormatter(config)
    
    assert formatter.epub_settings['toc'] is True
    assert formatter.epub_settings['toc-depth'] == 3
    assert formatter.epub_settings['css'] == 'epub.css'


@patch('os.path.exists')
@patch('yaml.safe_load')
@patch('yaml.dump')
def test_configure_epub_output_existing_config(mock_dump, mock_load, mock_exists, epub_formatter):
    """Test configuring EPUB output with existing Quarto configuration."""
    # Mock file exists
    mock_exists.return_value = True
    
    # Mock loading existing config
    mock_load.return_value = {
        'project': {'type': 'book'},
        'book': {'title': 'Test Book'},
        'format': {'html': {}}
    }
    
    # Call the method
    result = epub_formatter.configure_epub_output()
    
    # Verify result
    assert result is True
    
    # Verify config was updated
    mock_dump.assert_called_once()
    args, kwargs = mock_dump.call_args
    updated_config = args[0]
    assert updated_config['format']['epub'] == epub_formatter.epub_settings


@patch('os.path.exists')
@patch('yaml.dump')
def test_configure_epub_output_new_config(mock_dump, mock_exists, epub_formatter):
    """Test configuring EPUB output with new Quarto configuration."""
    # Mock file doesn't exist
    mock_exists.return_value = False
    
    # Call the method
    result = epub_formatter.configure_epub_output()
    
    # Verify result
    assert result is True
    
    # Verify new config was created
    mock_dump.assert_called_once()
    args, kwargs = mock_dump.call_args
    new_config = args[0]
    assert new_config['project']['type'] == 'book'
    assert new_config['format']['epub'] == epub_formatter.epub_settings


@patch('os.path.exists')
@patch('os.makedirs')
def test_create_epub_css_no_custom_css(mock_makedirs, mock_exists, epub_formatter):
    """Test creating EPUB CSS when no custom CSS is specified."""
    # Remove CSS from settings
    epub_formatter.epub_settings.pop('css', None)
    
    # Call the method
    result = epub_formatter.create_epub_css()
    
    # Verify result
    assert result is True
    
    # Verify no files were created
    mock_makedirs.assert_not_called()


@patch('os.path.exists')
@patch('os.makedirs')
@patch('shutil.copy2')
def test_create_epub_css_with_existing_css(mock_copy, mock_makedirs, mock_exists, epub_formatter):
    """Test creating EPUB CSS with existing CSS file."""
    # Mock CSS exists
    mock_exists.return_value = True
    
    # Call the method
    result = epub_formatter.create_epub_css()
    
    # Verify result
    assert result is True
    
    # Verify CSS was copied
    mock_copy.assert_called_once_with(
        '/home/user/project/epub.css',
        '/home/user/project/_build/epub.css'
    )
    
    # Verify no directories were created
    mock_makedirs.assert_not_called()


@patch('os.path.exists')
@patch('os.makedirs')
@patch('builtins.open', new_callable=mock_open)
@patch('shutil.copy2')
def test_create_epub_css_create_new_css(mock_copy, mock_open, mock_makedirs, mock_exists, epub_formatter):
    """Test creating a new EPUB CSS when it doesn't exist."""
    # Mock CSS doesn't exist
    def exists_side_effect(path):
        return 'project/_build' in path  # Only build dir exists
    mock_exists.side_effect = exists_side_effect
    
    # Call the method
    result = epub_formatter.create_epub_css()
    
    # Verify result
    assert result is True
    
    # Verify directory was created
    mock_makedirs.assert_called_once_with('/home/user/project', exist_ok=True)
    
    # Verify CSS was written
    mock_open.assert_called_with('/home/user/project/epub.css', 'w', encoding='utf-8')
    
    # Verify CSS was copied
    mock_copy.assert_called_once()


@patch('os.path.exists')
@patch('yaml.safe_load')
@patch('yaml.dump')
def test_configure_epub_metadata(mock_dump, mock_load, mock_exists, epub_formatter):
    """Test configuring EPUB metadata."""
    # Mock file exists
    mock_exists.return_value = True
    
    # Mock loading existing config
    mock_load.return_value = {
        'project': {'type': 'book'},
        'book': {'title': 'Old Title'},
        'format': {'epub': {}}
    }
    
    # Call the method
    result = epub_formatter.configure_epub_metadata(
        title='New Title',
        author='Test Author',
        date='2025-04-06',
        cover_image='images/cover.png'
    )
    
    # Verify result
    assert result is True
    
    # Verify config was updated
    mock_dump.assert_called_once()
    args, kwargs = mock_dump.call_args
    updated_config = args[0]
    assert updated_config['book']['title'] == 'New Title'
    assert updated_config['book']['author'] == 'Test Author'
    assert updated_config['book']['date'] == '2025-04-06'
    assert updated_config['book']['cover-image'] == 'images/cover.png'
    assert updated_config['format']['epub']['cover-image'] == 'images/cover.png'


@patch('os.path.exists')
@patch('yaml.safe_load')
@patch('yaml.dump')
def test_ensure_kindle_compatibility(mock_dump, mock_load, mock_exists, epub_formatter):
    """Test ensuring Kindle compatibility."""
    # Mock file exists
    mock_exists.return_value = True
    
    # Mock loading existing config
    mock_load.return_value = {
        'project': {'type': 'book'},
        'book': {'title': 'Test Book'},
        'format': {'epub': {}}
    }
    
    # Call the method
    result = epub_formatter.ensure_kindle_compatibility()
    
    # Verify result
    assert result is True
    
    # Verify config was updated
    mock_dump.assert_called_once()
    args, kwargs = mock_dump.call_args
    updated_config = args[0]
    assert updated_config['format']['epub']['epub-version'] == '3.0'
