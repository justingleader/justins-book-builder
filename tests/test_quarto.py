"""
Unit tests for the Quarto renderer module.
"""

import os
import pytest
from unittest.mock import patch, MagicMock
from quarto_book_builder.quarto import QuartoRenderer


@pytest.fixture
def mock_config():
    """Create a mock configuration for testing."""
    return {
        'config_path': '/home/user/project/config.yaml',
        'build_dir': '_build',
        'output_dir': '_book'
    }


@pytest.fixture
def quarto_renderer(mock_config):
    """Create a Quarto renderer instance with mock configuration."""
    return QuartoRenderer(mock_config)


def test_init(mock_config):
    """Test initialization of QuartoRenderer."""
    renderer = QuartoRenderer(mock_config)
    
    assert renderer.project_dir == '/home/user/project'
    assert renderer.build_dir == '/home/user/project/_build'
    assert renderer.output_dir == '/home/user/project/_book'


@patch('subprocess.run')
def test_check_quarto_installation_success(mock_run, quarto_renderer):
    """Test checking Quarto installation when it's installed."""
    # Mock successful Quarto version check
    mock_process = MagicMock()
    mock_process.stdout = "Quarto CLI version 1.3.450"
    mock_run.return_value = mock_process
    
    installed, version = quarto_renderer.check_quarto_installation()
    
    assert installed is True
    assert version == "Quarto CLI version 1.3.450"
    mock_run.assert_called_once_with(
        ['quarto', '--version'], 
        check=True, 
        capture_output=True, 
        text=True
    )


@patch('subprocess.run')
def test_check_quarto_installation_failure(mock_run, quarto_renderer):
    """Test checking Quarto installation when it's not installed."""
    # Mock Quarto command not found
    mock_run.side_effect = FileNotFoundError("No such file or directory: 'quarto'")
    
    installed, version = quarto_renderer.check_quarto_installation()
    
    assert installed is False
    assert version is None


@patch('subprocess.run')
@patch('os.path.exists')
def test_render_success(mock_exists, mock_run, quarto_renderer):
    """Test successful rendering with Quarto."""
    # Mock Quarto config exists
    mock_exists.return_value = True
    
    # Mock successful Quarto render
    mock_process = MagicMock()
    mock_process.stdout = "Output created: _book/book.pdf"
    mock_process.stderr = ""
    mock_run.return_value = mock_process
    
    # Mock check_quarto_installation
    with patch.object(quarto_renderer, 'check_quarto_installation', return_value=(True, "Quarto CLI version 1.3.450")):
        # Mock copy_output_files
        with patch.object(quarto_renderer, '_copy_output_files'):
            result = quarto_renderer.render()
            
            assert result is True
            mock_run.assert_called_once_with(
                ['quarto', 'render', '/home/user/project/_build'], 
                check=True, 
                capture_output=True, 
                text=True
            )


@patch('subprocess.run')
@patch('os.path.exists')
def test_render_with_formats(mock_exists, mock_run, quarto_renderer):
    """Test rendering with specific formats."""
    # Mock Quarto config exists
    mock_exists.return_value = True
    
    # Mock successful Quarto render
    mock_process = MagicMock()
    mock_process.stdout = "Output created: _book/book.pdf, _book/book.epub"
    mock_process.stderr = ""
    mock_run.return_value = mock_process
    
    # Mock check_quarto_installation
    with patch.object(quarto_renderer, 'check_quarto_installation', return_value=(True, "Quarto CLI version 1.3.450")):
        # Mock copy_output_files
        with patch.object(quarto_renderer, '_copy_output_files'):
            result = quarto_renderer.render(formats=['pdf', 'epub'])
            
            assert result is True
            mock_run.assert_called_once_with(
                ['quarto', 'render', '/home/user/project/_build', '--to', 'pdf,epub'], 
                check=True, 
                capture_output=True, 
                text=True
            )


@patch('subprocess.run')
def test_render_quarto_not_installed(mock_run, quarto_renderer):
    """Test rendering when Quarto is not installed."""
    # Mock check_quarto_installation
    with patch.object(quarto_renderer, 'check_quarto_installation', return_value=(False, None)):
        with pytest.raises(RuntimeError, match="Quarto is required but not found"):
            quarto_renderer.render()
            
            # Verify quarto command was not called
            mock_run.assert_not_called()


@patch('os.path.exists')
@patch('os.path.isdir')
@patch('os.listdir')
@patch('os.makedirs')
@patch('shutil.copy2')
@patch('shutil.copytree')
@patch('shutil.rmtree')
def test_copy_output_files(mock_rmtree, mock_copytree, mock_copy2, mock_makedirs, 
                          mock_listdir, mock_isdir, mock_exists, quarto_renderer):
    """Test copying output files from Quarto _book directory."""
    # Mock directory exists
    mock_exists.return_value = True
    
    # Mock directory listing
    mock_listdir.return_value = ['book.pdf', 'book.epub', 'images']
    
    # Mock file/directory checks
    def is_dir_side_effect(path):
        return 'images' in path
        
    mock_isdir.side_effect = is_dir_side_effect
    
    # Call the method
    quarto_renderer._copy_output_files('/home/user/project/_build')
    
    # Verify output directory was created
    mock_makedirs.assert_called_once_with('/home/user/project/_book', exist_ok=True)
    
    # Verify files were copied
    mock_copy2.assert_any_call(
        '/home/user/project/_build/_book/book.pdf', 
        '/home/user/project/_book/book.pdf'
    )
    mock_copy2.assert_any_call(
        '/home/user/project/_build/_book/book.epub', 
        '/home/user/project/_book/book.epub'
    )
    
    # Verify directory was copied
    mock_copytree.assert_called_once_with(
        '/home/user/project/_build/_book/images', 
        '/home/user/project/_book/images'
    )


@patch('os.path.exists')
@patch('os.listdir')
@patch('os.path.isfile')
def test_get_output_files(mock_isfile, mock_listdir, mock_exists, quarto_renderer):
    """Test getting list of output files."""
    # Mock directory exists
    mock_exists.return_value = True
    
    # Mock directory listing
    mock_listdir.return_value = ['book.pdf', 'book.epub', 'index.html', 'data.json', 'images']
    
    # Mock file check
    def is_file_side_effect(path):
        return 'images' not in path
        
    mock_isfile.side_effect = is_file_side_effect
    
    # Call the method
    result = quarto_renderer.get_output_files()
    
    # Verify result
    assert '/home/user/project/_book/book.pdf' in result['pdf']
    assert '/home/user/project/_book/book.epub' in result['epub']
    assert '/home/user/project/_book/index.html' in result['html']
    assert '/home/user/project/_book/data.json' in result['other']
    assert len(result['pdf']) == 1
    assert len(result['epub']) == 1
    assert len(result['html']) == 1
    assert len(result['other']) == 1


@patch('subprocess.Popen')
@patch('os.path.exists')
def test_preview_html(mock_exists, mock_popen, quarto_renderer):
    """Test previewing HTML output."""
    # Mock get_output_files
    with patch.object(quarto_renderer, 'get_output_files', return_value={
        'html': ['/home/user/project/_book/index.html'],
        'pdf': [],
        'epub': [],
        'other': []
    }):
        result = quarto_renderer.preview('html')
        
        assert result is True
        mock_popen.assert_called_once_with(
            ['quarto', 'preview', '/home/user/project'],
            stdout=pytest.ANY,
            stderr=pytest.ANY
        )


@patch('subprocess.Popen')
@patch('os.name', 'posix')  # Mock Linux/macOS
def test_preview_pdf(mock_popen, quarto_renderer):
    """Test previewing PDF output on Linux/macOS."""
    # Mock get_output_files
    with patch.object(quarto_renderer, 'get_output_files', return_value={
        'html': [],
        'pdf': ['/home/user/project/_book/book.pdf'],
        'epub': [],
        'other': []
    }):
        result = quarto_renderer.preview('pdf')
        
        assert result is True
        mock_popen.assert_called_once_with(
            ['xdg-open', '/home/user/project/_book/book.pdf']
        )


def test_preview_no_files(quarto_renderer):
    """Test previewing when no output files exist."""
    # Mock get_output_files
    with patch.object(quarto_renderer, 'get_output_files', return_value={
        'html': [],
        'pdf': [],
        'epub': [],
        'other': []
    }):
        result = quarto_renderer.preview('pdf')
        
        assert result is False
