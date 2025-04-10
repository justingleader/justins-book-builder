"""
Unit tests for the template manager module.
"""

import os
import pytest
from unittest.mock import patch, mock_open
from quarto_book_builder.template_manager import TemplateManager


@pytest.fixture
def mock_config():
    """Create a mock configuration for testing."""
    return {
        'template_dir': '/tmp/test_templates',
        'custom_sections': {
            'featured-quote': {
                'html': '<div class="featured-quote"><blockquote>{{ content }}</blockquote><p class="attribution">— {{ author }}</p></div>',
                'latex': '\\begin{quotation}\\noindent\\textit{{{ content }}}\\\\\\hfill--- {{ author }}\\end{quotation}'
            },
            'listicle': {
                'html': '<div class="listicle"><h3>{{ title }}</h3>{{ content }}</div>',
                'latex': '\\begin{mdframed}[backgroundcolor=gray!20]\\textbf{Listicle: {{ title }}} {{ content }}\\end{mdframed}'
            }
        }
    }


@pytest.fixture
def template_manager(mock_config):
    """Create a template manager instance with mock configuration."""
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = False  # No external templates
        return TemplateManager(mock_config)


def test_init(mock_config):
    """Test initialization of TemplateManager."""
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = False  # No external templates
        manager = TemplateManager(mock_config)
        
        assert manager.template_dir == '/tmp/test_templates'
        assert 'featured-quote' in manager.templates
        assert 'listicle' in manager.templates


def test_apply_template_html(template_manager):
    """Test applying HTML template."""
    content = "This is a quote"
    result = template_manager.apply_template('featured-quote', content, 'html')
    
    assert '<div class="featured-quote">' in result
    assert '<blockquote>This is a quote</blockquote>' in result
    assert '<p class="attribution">— </p>' in result  # No author


def test_apply_template_latex(template_manager):
    """Test applying LaTeX template."""
    content = "This is a quote"
    result = template_manager.apply_template('featured-quote', content, 'latex')
    
    assert '\\begin{quotation}' in result
    assert '\\noindent\\textit{This is a quote}' in result
    assert '\\hfill--- ' in result  # No author


def test_apply_template_with_author(template_manager):
    """Test applying template with author extraction."""
    content = "This is a quote\n\n**— Albert Einstein**"
    result = template_manager.apply_template('featured-quote', content, 'html')
    
    assert '<div class="featured-quote">' in result
    assert '<blockquote>This is a quote</blockquote>' in result
    assert '<p class="attribution">— Albert Einstein</p>' in result


def test_apply_template_with_title(template_manager):
    """Test applying template with title extraction."""
    content = "## Top Tips\n\n- Tip 1\n- Tip 2"
    result = template_manager.apply_template('listicle', content, 'html')
    
    assert '<div class="listicle">' in result
    assert '<h3>Top Tips</h3>' in result
    assert '- Tip 1\n- Tip 2' in result


def test_apply_template_unknown_section(template_manager):
    """Test applying template for unknown section."""
    content = "Some content"
    result = template_manager.apply_template('unknown-section', content, 'html')
    
    # Should return original content
    assert result == content


def test_apply_template_unknown_format(template_manager):
    """Test applying template for unknown format."""
    content = "Some content"
    result = template_manager.apply_template('featured-quote', content, 'unknown')
    
    # Should return original content
    assert result == content


def test_get_available_sections(template_manager):
    """Test getting available sections."""
    sections = template_manager.get_available_sections()
    
    assert 'featured-quote' in sections
    assert 'listicle' in sections
    assert len(sections) == 2


def test_get_template_info(template_manager):
    """Test getting template info."""
    # Get info for all templates
    info = template_manager.get_template_info()
    
    assert len(info) == 2
    assert any(item['name'] == 'featured-quote' for item in info)
    assert any(item['name'] == 'listicle' for item in info)
    
    # Get info for specific template
    quote_info = template_manager.get_template_info('featured-quote')
    
    assert quote_info['name'] == 'featured-quote'
    assert 'html' in quote_info['formats']
    assert 'latex' in quote_info['formats']
    
    # Get info for unknown template
    unknown_info = template_manager.get_template_info('unknown')
    
    assert unknown_info is None


def test_add_template(template_manager):
    """Test adding a new template."""
    # Add new template
    result = template_manager.add_template(
        'note',
        html_template='<div class="note">{{ content }}</div>',
        latex_template='\\begin{note}{{ content }}\\end{note}'
    )
    
    assert result is True
    assert 'note' in template_manager.templates
    assert template_manager.templates['note']['html'] == '<div class="note">{{ content }}</div>'
    assert template_manager.templates['note']['latex'] == '\\begin{note}{{ content }}\\end{note}'


@patch('os.path.exists')
@patch('os.listdir')
def test_load_external_templates_yaml(mock_listdir, mock_exists, mock_config):
    """Test loading templates from external YAML files."""
    # Mock directory exists
    mock_exists.return_value = True
    
    # Mock directory contents
    mock_listdir.return_value = ['templates.yaml']
    
    # Mock file open
    yaml_content = """
    note:
      html: '<div class="note">{{ content }}</div>'
      latex: '\\begin{note}{{ content }}\\end{note}'
    """
    
    with patch('builtins.open', mock_open(read_data=yaml_content)):
        manager = TemplateManager(mock_config)
        
        # Verify template was loaded
        assert 'note' in manager.templates
        assert manager.templates['note']['html'] == '<div class="note">{{ content }}</div>'
        assert manager.templates['note']['latex'] == '\\begin{note}{{ content }}\\end{note}'


@patch('os.path.exists')
def test_load_external_templates_individual(mock_exists, mock_config):
    """Test loading templates from individual files."""
    # Mock file existence checks
    def exists_side_effect(path):
        if path == '/tmp/test_templates':
            return True
        if path == '/tmp/test_templates/featured-quote.html':
            return True
        if path == '/tmp/test_templates/featured-quote.tex':
            return True
        return False
        
    mock_exists.side_effect = exists_side_effect
    
    # Mock directory listing
    with patch('os.listdir', return_value=[]):
        # Mock file open
        html_content = '<div class="custom-quote">{{ content }} - {{ author }}</div>'
        tex_content = '\\begin{customquote}{{ content }} - {{ author }}\\end{customquote}'
        
        # Need to handle multiple file opens with different content
        mock_file = mock_open()
        mock_file.side_effect = [
            mock_open(read_data=html_content).return_value,
            mock_open(read_data=tex_content).return_value
        ]
        
        with patch('builtins.open', mock_file):
            manager = TemplateManager(mock_config)
            
            # Verify template was updated
            assert manager.templates['featured-quote']['html'] == html_content
            assert manager.templates['featured-quote']['latex'] == tex_content
