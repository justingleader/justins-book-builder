"""
Unit tests for the CLI interface.
"""

import os
import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from quarto_book_builder.cli import cli


@pytest.fixture
def runner():
    """Create a CLI runner for testing."""
    return CliRunner()


def test_cli_version(runner):
    """Test CLI version command."""
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0
    assert '0.1.0' in result.output


@patch('os.makedirs')
@patch('builtins.open', new_callable=MagicMock)
def test_init_command(mock_open, mock_makedirs, runner):
    """Test init command."""
    # Mock file existence check
    with patch('os.path.exists', return_value=False):
        result = runner.invoke(cli, ['init', '/test/project', '--title', 'Test Book', '--author', 'Test Author'])
        
        assert result.exit_code == 0
        assert 'Created project directory' in result.output
        assert 'Initialized book project' in result.output
        
        # Verify directories were created
        mock_makedirs.assert_any_call('/test/project')
        mock_makedirs.assert_any_call('/test/project/chapters', exist_ok=True)
        mock_makedirs.assert_any_call('/test/project/images', exist_ok=True)
        mock_makedirs.assert_any_call('/test/project/templates', exist_ok=True)
        
        # Verify files were created
        mock_open.assert_any_call('/test/project/config.yaml', 'w')
        mock_open.assert_any_call('/test/project/_quarto.yml', 'w')
        mock_open.assert_any_call('/test/project/chapters/01-intro.qmd', 'w')
        mock_open.assert_any_call('/test/project/epub.css', 'w')


@patch('quarto_book_builder.cli.ConfigManager')
@patch('quarto_book_builder.cli.ImageGenerator')
@patch('quarto_book_builder.cli.TemplateManager')
@patch('quarto_book_builder.cli.MarkdownPreprocessor')
def test_preprocess_command(mock_preprocessor, mock_template_manager, mock_image_generator, mock_config_manager, runner):
    """Test preprocess command."""
    # Mock configuration
    mock_config = MagicMock()
    mock_config_manager.return_value.load.return_value = {}
    
    # Mock preprocessor
    mock_preprocessor_instance = MagicMock()
    mock_preprocessor_instance.process_project.return_value = ['file1.md', 'file2.md']
    mock_preprocessor_instance.copy_static_files.return_value = 5
    mock_preprocessor.return_value = mock_preprocessor_instance
    
    # Run command
    with patch('os.path.exists', return_value=True):
        with patch('os.path.abspath', return_value='/test/project'):
            result = runner.invoke(cli, ['preprocess', '/test/project'])
            
            assert result.exit_code == 0
            assert 'Preprocessed 2 Markdown files' in result.output
            assert 'Copied 5 static files' in result.output
            
            # Verify components were initialized
            mock_config_manager.assert_called_once()
            mock_image_generator.assert_called_once()
            mock_template_manager.assert_called_once()
            mock_preprocessor.assert_called_once()
            
            # Verify preprocessing was done
            mock_preprocessor_instance.process_project.assert_called_once()
            mock_preprocessor_instance.copy_static_files.assert_called_once()


@patch('quarto_book_builder.cli.ConfigManager')
@patch('quarto_book_builder.cli.ImageGenerator')
@patch('quarto_book_builder.cli.TemplateManager')
@patch('quarto_book_builder.cli.MarkdownPreprocessor')
@patch('quarto_book_builder.cli.QuartoRenderer')
@patch('quarto_book_builder.cli.PDFFormatter')
@patch('quarto_book_builder.cli.EPUBFormatter')
def test_build_command(mock_epub_formatter, mock_pdf_formatter, mock_quarto_renderer, 
                      mock_preprocessor, mock_template_manager, mock_image_generator, 
                      mock_config_manager, runner):
    """Test build command."""
    # Mock configuration
    mock_config = MagicMock()
    mock_config_manager.return_value.load.return_value = {}
    
    # Mock Quarto renderer
    mock_quarto_instance = MagicMock()
    mock_quarto_instance.check_quarto_installation.return_value = (True, "Quarto CLI version 1.3.450")
    mock_quarto_instance.get_output_files.return_value = {
        'pdf': ['/test/project/_book/book.pdf'],
        'epub': ['/test/project/_book/book.epub'],
        'html': [],
        'other': []
    }
    mock_quarto_renderer.return_value = mock_quarto_instance
    
    # Mock preprocessor
    mock_preprocessor_instance = MagicMock()
    mock_preprocessor_instance.process_project.return_value = ['file1.md', 'file2.md']
    mock_preprocessor_instance.copy_static_files.return_value = 5
    mock_preprocessor.return_value = mock_preprocessor_instance
    
    # Mock formatters
    mock_pdf_instance = MagicMock()
    mock_pdf_formatter.return_value = mock_pdf_instance
    mock_epub_instance = MagicMock()
    mock_epub_formatter.return_value = mock_epub_instance
    
    # Run command
    with patch('os.path.exists', return_value=True):
        with patch('os.path.abspath', return_value='/test/project'):
            with patch('os.path.join', return_value='/test/project/_build'):
                result = runner.invoke(cli, ['build', '/test/project', '--format', 'pdf,epub'])
                
                assert result.exit_code == 0
                assert 'Using Quarto version: Quarto CLI version 1.3.450' in result.output
                assert 'Preprocessed 2 Markdown files' in result.output
                assert 'Configuring PDF output' in result.output
                assert 'Configuring EPUB output' in result.output
                assert 'Rendering with Quarto' in result.output
                assert 'Build complete' in result.output
                assert 'PDF output:' in result.output
                assert 'EPUB output:' in result.output
                
                # Verify components were initialized
                mock_config_manager.assert_called_once()
                mock_image_generator.assert_called_once()
                mock_template_manager.assert_called_once()
                mock_preprocessor.assert_called_once()
                mock_quarto_renderer.assert_called_once()
                mock_pdf_formatter.assert_called_once()
                mock_epub_formatter.assert_called_once()
                
                # Verify Quarto was checked
                mock_quarto_instance.check_quarto_installation.assert_called_once()
                
                # Verify preprocessing was done
                mock_preprocessor_instance.process_project.assert_called_once()
                mock_preprocessor_instance.copy_static_files.assert_called_once()
                
                # Verify formatters were configured
                mock_pdf_instance.configure_pdf_output.assert_called_once()
                mock_pdf_instance.create_latex_template.assert_called_once()
                mock_pdf_instance.add_latex_preamble.assert_called_once()
                mock_epub_instance.configure_epub_output.assert_called_once()
                mock_epub_instance.create_epub_css.assert_called_once()
                mock_epub_instance.ensure_kindle_compatibility.assert_called_once()
                
                # Verify rendering was done
                mock_quarto_instance.render.assert_called_once()
                mock_quarto_instance.get_output_files.assert_called_once()


@patch('quarto_book_builder.cli.ConfigManager')
@patch('quarto_book_builder.cli.QuartoRenderer')
def test_preview_command(mock_quarto_renderer, mock_config_manager, runner):
    """Test preview command."""
    # Mock configuration
    mock_config = MagicMock()
    mock_config_manager.return_value.load.return_value = {}
    
    # Mock Quarto renderer
    mock_quarto_instance = MagicMock()
    mock_quarto_instance.preview.return_value = True
    mock_quarto_renderer.return_value = mock_quarto_instance
    
    # Run command for PDF preview
    with patch('os.path.exists', return_value=True):
        with patch('os.path.abspath', return_value='/test/project'):
            result = runner.invoke(cli, ['preview', '/test/project', '--format', 'pdf'])
            
            assert result.exit_code == 0
            assert 'Opened PDF file for preview' in result.output
            
            # Verify components were initialized
            mock_config_manager.assert_called_once()
            mock_quarto_renderer.assert_called_once()
            
            # Verify preview was called
            mock_quarto_instance.preview.assert_called_once_with('pdf')


@patch('shutil.rmtree')
@patch('quarto_book_builder.cli.ConfigManager')
def test_clean_command(mock_config_manager, mock_rmtree, runner):
    """Test clean command."""
    # Mock configuration
    mock_config = MagicMock()
    mock_config_manager.return_value.load.return_value = {
        'build_dir': '_build',
        'output_dir': '_book'
    }
    
    # Run command
    with patch('os.path.exists', return_value=True):
        with patch('os.path.abspath', return_value='/test/project'):
            result = runner.invoke(cli, ['clean', '/test/project'])
            
            assert result.exit_code == 0
            assert 'Removed /test/project/_build' in result.output
            assert 'Removed /test/project/_book' in result.output
            assert 'Clean complete' in result.output
            
            # Verify directories were removed
            mock_rmtree.assert_any_call('/test/project/_build')
            mock_rmtree.assert_any_call('/test/project/_book')
