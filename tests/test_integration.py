"""
Integration tests for the Quarto Book Builder.
"""

import os
import pytest
import tempfile
import shutil
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from quarto_book_builder.cli import cli


@pytest.fixture
def temp_project_dir():
    """Create a temporary project directory for testing."""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


@pytest.fixture
def runner():
    """Create a CLI runner for testing."""
    return CliRunner()


@patch('quarto_book_builder.image_generator.ImageGenerator.generate_image')
@patch('quarto_book_builder.quarto.QuartoRenderer.check_quarto_installation')
@patch('quarto_book_builder.quarto.QuartoRenderer.render')
def test_full_workflow(mock_render, mock_check_quarto, mock_generate_image, runner, temp_project_dir):
    """Test the full workflow from init to build."""
    # Mock Quarto installation check
    mock_check_quarto.return_value = (True, "Quarto CLI version 1.3.450")
    
    # Mock image generation
    mock_generate_image.return_value = os.path.join(temp_project_dir, "images", "img_12345678.png")
    
    # Mock render to avoid actual Quarto execution
    mock_render.return_value = True
    
    # Step 1: Initialize project
    init_result = runner.invoke(cli, ['init', temp_project_dir])
    assert init_result.exit_code == 0
    assert 'Initialized book project' in init_result.output
    
    # Verify project structure
    assert os.path.exists(os.path.join(temp_project_dir, 'config.yaml'))
    assert os.path.exists(os.path.join(temp_project_dir, '_quarto.yml'))
    assert os.path.exists(os.path.join(temp_project_dir, 'chapters', '01-intro.qmd'))
    
    # Step 2: Update config with mock API key
    config_path = os.path.join(temp_project_dir, 'config.yaml')
    with open(config_path, 'r') as f:
        config_content = f.read()
    
    config_content = config_content.replace('openai_api_key: "your-api-key-here"', 
                                           'openai_api_key: "test-api-key-1234"')
    
    with open(config_path, 'w') as f:
        f.write(config_content)
    
    # Step 3: Preprocess files
    with patch('os.makedirs'):  # Mock directory creation
        preprocess_result = runner.invoke(cli, ['preprocess', temp_project_dir])
        assert preprocess_result.exit_code == 0
        assert 'Preprocessing complete' in preprocess_result.output
    
    # Step 4: Build book
    with patch('os.makedirs'):  # Mock directory creation
        with patch('quarto_book_builder.quarto.QuartoRenderer.get_output_files', 
                  return_value={
                      'pdf': [os.path.join(temp_project_dir, '_book', 'book.pdf')],
                      'epub': [os.path.join(temp_project_dir, '_book', 'book.epub')],
                      'html': [],
                      'other': []
                  }):
            build_result = runner.invoke(cli, ['build', temp_project_dir])
            assert build_result.exit_code == 0
            assert 'Build complete' in build_result.output
            assert 'PDF output:' in build_result.output
            assert 'EPUB output:' in build_result.output
    
    # Step 5: Clean project
    with patch('shutil.rmtree'):  # Mock directory removal
        clean_result = runner.invoke(cli, ['clean', temp_project_dir])
        assert clean_result.exit_code == 0
        assert 'Clean complete' in clean_result.output


@patch('quarto_book_builder.image_generator.ImageGenerator.generate_image')
def test_image_generation_integration(mock_generate_image, runner, temp_project_dir):
    """Test image generation integration."""
    # Initialize project
    runner.invoke(cli, ['init', temp_project_dir])
    
    # Create test chapter with image tag
    chapter_dir = os.path.join(temp_project_dir, 'chapters')
    os.makedirs(chapter_dir, exist_ok=True)
    
    with open(os.path.join(chapter_dir, 'test_images.md'), 'w') as f:
        f.write("""# Test Chapter
        
This is a test chapter with an image.

{{image: A beautiful mountain landscape with snow-capped peaks}}

And another image:

{{image: A futuristic city with flying cars}}
""")
    
    # Mock image generation
    def mock_generate_side_effect(prompt):
        # Create a unique filename based on prompt
        import hashlib
        prompt_hash = hashlib.sha1(prompt.encode()).hexdigest()[:8]
        filename = f"img_{prompt_hash}.png"
        
        # Create images directory if it doesn't exist
        images_dir = os.path.join(temp_project_dir, 'images')
        os.makedirs(images_dir, exist_ok=True)
        
        # Create empty image file
        image_path = os.path.join(images_dir, filename)
        with open(image_path, 'w') as f:
            f.write("mock image content")
            
        return image_path
    
    mock_generate_image.side_effect = mock_generate_side_effect
    
    # Update config with mock API key
    config_path = os.path.join(temp_project_dir, 'config.yaml')
    with open(config_path, 'r') as f:
        config_content = f.read()
    
    config_content = config_content.replace('openai_api_key: "your-api-key-here"', 
                                           'openai_api_key: "test-api-key-1234"')
    
    with open(config_path, 'w') as f:
        f.write(config_content)
    
    # Preprocess files
    with patch('os.makedirs', side_effect=lambda path, exist_ok: os.makedirs(path, exist_ok=True)):
        preprocess_result = runner.invoke(cli, ['preprocess', temp_project_dir])
        assert preprocess_result.exit_code == 0
    
    # Verify images were "generated"
    assert len(mock_generate_image.call_args_list) == 2
    assert mock_generate_image.call_args_list[0][0][0] == "A beautiful mountain landscape with snow-capped peaks"
    assert mock_generate_image.call_args_list[1][0][0] == "A futuristic city with flying cars"
    
    # Verify image files exist
    images_dir = os.path.join(temp_project_dir, 'images')
    assert len(os.listdir(images_dir)) == 2


@patch('quarto_book_builder.template_manager.TemplateManager.apply_template')
def test_custom_section_integration(mock_apply_template, runner, temp_project_dir):
    """Test custom section template integration."""
    # Initialize project
    runner.invoke(cli, ['init', temp_project_dir])
    
    # Create test chapter with custom section
    chapter_dir = os.path.join(temp_project_dir, 'chapters')
    os.makedirs(chapter_dir, exist_ok=True)
    
    with open(os.path.join(chapter_dir, 'test_sections.md'), 'w') as f:
        f.write("""# Test Chapter
        
This is a test chapter with a custom section.

::: featured-quote
"The best way to predict the future is to invent it."
**— Alan Kay**
:::

And another section:

::: listicle
## Top 3 Programming Languages

1. Python
2. JavaScript
3. Rust
:::
""")
    
    # Mock template application
    def mock_apply_template_side_effect(section_name, content, output_format):
        if section_name == 'featured-quote':
            if output_format == 'html':
                return f'<div class="featured-quote"><blockquote>{content}</blockquote><p class="attribution">— Alan Kay</p></div>'
            else:
                return f'\\begin{{quotation}}\\noindent\\textit{{{content}}}\\\\\\hfill--- Alan Kay\\end{{quotation}}'
        elif section_name == 'listicle':
            if output_format == 'html':
                return f'<div class="listicle"><h3>Top 3 Programming Languages</h3>{content}</div>'
            else:
                return f'\\begin{{mdframed}}[backgroundcolor=gray!20]\\textbf{{Listicle: Top 3 Programming Languages}} {content}\\end{{mdframed}}'
        return content
    
    mock_apply_template.side_effect = mock_apply_template_side_effect
    
    # Update config with mock API key
    config_path = os.path.join(temp_project_dir, 'config.yaml')
    with open(config_path, 'r') as f:
        config_content = f.read()
    
    config_content = config_content.replace('openai_api_key: "your-api-key-here"', 
                                           'openai_api_key: "test-api-key-1234"')
    
    with open(config_path, 'w') as f:
        f.write(config_content)
    
    # Preprocess files
    with patch('os.makedirs', side_effect=lambda path, exist_ok: os.makedirs(path, exist_ok=True)):
        with patch('quarto_book_builder.image_generator.ImageGenerator.generate_image', return_value="mock_image.png"):
            preprocess_result = runner.invoke(cli, ['preprocess', temp_project_dir])
            assert preprocess_result.exit_code == 0
    
    # Verify templates were applied
    assert len(mock_apply_template.call_args_list) == 4  # 2 sections x 2 formats (html, latex)
    
    # Check first call (featured-quote, html)
    assert mock_apply_template.call_args_list[0][0][0] == 'featured-quote'
    assert '"The best way to predict the future is to invent it."' in mock_apply_template.call_args_list[0][0][1]
    assert mock_apply_template.call_args_list[0][0][2] == 'html'
    
    # Check second call (featured-quote, latex)
    assert mock_apply_template.call_args_list[1][0][0] == 'featured-quote'
    assert '"The best way to predict the future is to invent it."' in mock_apply_template.call_args_list[1][0][1]
    assert mock_apply_template.call_args_list[1][0][2] == 'latex'
