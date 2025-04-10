"""
Unit tests for the PDF formatter module.
"""

import os
import pytest
from unittest.mock import patch, mock_open, MagicMock
from quarto_book_builder.pdf_formatter import PDFFormatter


@pytest.fixture
def mock_config():
    """Create a mock configuration for testing."""
    return {
        'config_path': '/home/user/project/config.yaml',
        'build_dir': '_build',
        'pdf': {
            'documentclass': 'book',
            'geometry': '6in,9in',
            'toc': True,
            'toc-depth': 3,
            'number-sections': True,
            'colorlinks': True
        }
    }


@pytest.fixture
def pdf_formatter(mock_config):
    """Create a PDF formatter instance with mock configuration."""
    return PDFFormatter(mock_config)


def test_init(mock_config):
    """Test initialization of PDFFormatter."""
    formatter = PDFFormatter(mock_config)
    
    assert formatter.project_dir == '/home/user/project'
    assert formatter.build_dir == '/home/user/project/_build'
    assert formatter.pdf_settings == mock_config['pdf']


def test_init_default_pdf_settings():
    """Test initialization with default PDF settings."""
    config = {
        'config_path': '/home/user/project/config.yaml',
        'build_dir': '_build'
    }
    formatter = PDFFormatter(config)
    
    assert formatter.pdf_settings['documentclass'] == 'book'
    assert formatter.pdf_settings['geometry'] == '6in,9in'
    assert formatter.pdf_settings['toc'] is True


@patch('os.path.exists')
@patch('yaml.safe_load')
@patch('yaml.dump')
def test_configure_pdf_output_existing_config(mock_dump, mock_load, mock_exists, pdf_formatter):
    """Test configuring PDF output with existing Quarto configuration."""
    # Mock file exists
    mock_exists.return_value = True
    
    # Mock loading existing config
    mock_load.return_value = {
        'project': {'type': 'book'},
        'book': {'title': 'Test Book'},
        'format': {'html': {}}
    }
    
    # Call the method
    result = pdf_formatter.configure_pdf_output()
    
    # Verify result
    assert result is True
    
    # Verify config was updated
    mock_dump.assert_called_once()
    args, kwargs = mock_dump.call_args
    updated_config = args[0]
    assert updated_config['format']['pdf'] == pdf_formatter.pdf_settings


@patch('os.path.exists')
@patch('yaml.dump')
def test_configure_pdf_output_new_config(mock_dump, mock_exists, pdf_formatter):
    """Test configuring PDF output with new Quarto configuration."""
    # Mock file doesn't exist
    mock_exists.return_value = False
    
    # Call the method
    result = pdf_formatter.configure_pdf_output()
    
    # Verify result
    assert result is True
    
    # Verify new config was created
    mock_dump.assert_called_once()
    args, kwargs = mock_dump.call_args
    new_config = args[0]
    assert new_config['project']['type'] == 'book'
    assert new_config['format']['pdf'] == pdf_formatter.pdf_settings


@patch('os.path.exists')
@patch('os.makedirs')
def test_create_latex_template_no_custom_template(mock_makedirs, mock_exists, pdf_formatter):
    """Test creating LaTeX template when no custom template is specified."""
    # Remove template from settings
    pdf_formatter.pdf_settings.pop('template', None)
    
    # Call the method
    result = pdf_formatter.create_latex_template()
    
    # Verify result
    assert result is True
    
    # Verify no files were created
    mock_makedirs.assert_not_called()


@patch('os.path.exists')
@patch('os.makedirs')
@patch('shutil.copy2')
def test_create_latex_template_with_existing_template(mock_copy, mock_makedirs, mock_exists, pdf_formatter):
    """Test creating LaTeX template with existing template file."""
    # Add template to settings
    pdf_formatter.pdf_settings['template'] = 'templates/custom.tex'
    
    # Mock template exists
    mock_exists.return_value = True
    
    # Call the method
    result = pdf_formatter.create_latex_template()
    
    # Verify result
    assert result is True
    
    # Verify template was copied
    mock_copy.assert_called_once_with(
        '/home/user/project/templates/custom.tex',
        '/home/user/project/_build/custom.tex'
    )
    
    # Verify no directories were created
    mock_makedirs.assert_not_called()


@patch('os.path.exists')
@patch('os.makedirs')
@patch('builtins.open', new_callable=mock_open)
@patch('shutil.copy2')
def test_create_latex_template_create_new_template(mock_copy, mock_open, mock_makedirs, mock_exists, pdf_formatter):
    """Test creating a new LaTeX template when it doesn't exist."""
    # Add template to settings
    pdf_formatter.pdf_settings['template'] = 'templates/custom.tex'
    
    # Mock template doesn't exist
    def exists_side_effect(path):
        return 'project/_build' in path  # Only build dir exists
    mock_exists.side_effect = exists_side_effect
    
    # Call the method
    result = pdf_formatter.create_latex_template()
    
    # Verify result
    assert result is True
    
    # Verify directory was created
    mock_makedirs.assert_called_once_with('/home/user/project/templates', exist_ok=True)
    
    # Verify template was written
    mock_open.assert_called_with('/home/user/project/templates/custom.tex', 'w', encoding='utf-8')
    
    # Verify template was copied
    mock_copy.assert_called_once()


@patch('os.path.exists')
@patch('shutil.copy2')
@patch('yaml.safe_load')
@patch('yaml.dump')
def test_add_latex_preamble(mock_dump, mock_load, mock_copy, mock_exists, pdf_formatter):
    """Test adding LaTeX preamble."""
    # Mock files exist
    def exists_side_effect(path):
        return True
    mock_exists.side_effect = exists_side_effect
    
    # Mock loading existing config
    mock_load.return_value = {
        'project': {'type': 'book'},
        'book': {'title': 'Test Book'},
        'format': {'pdf': {}}
    }
    
    # Call the method
    result = pdf_formatter.add_latex_preamble()
    
    # Verify result
    assert result is True
    
    # Verify preamble was copied
    mock_copy.assert_called_once()
    
    # Verify config was updated
    mock_dump.assert_called_once()
    args, kwargs = mock_dump.call_args
    updated_config = args[0]
    assert updated_config['format']['pdf']['include-in-header'] == 'latex-preamble.tex'


@patch('os.path.exists')
@patch('yaml.safe_load')
@patch('yaml.dump')
def test_configure_pdf_metadata(mock_dump, mock_load, mock_exists, pdf_formatter):
    """Test configuring PDF metadata."""
    # Mock file exists
    mock_exists.return_value = True
    
    # Mock loading existing config
    mock_load.return_value = {
        'project': {'type': 'book'},
        'book': {'title': 'Old Title'},
        'format': {'pdf': {}}
    }
    
    # Call the method
    result = pdf_formatter.configure_pdf_metadata(
        title='New Title',
        author='Test Author',
        date='2025-04-06'
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
