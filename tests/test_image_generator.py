"""
Unit tests for the image generator module.
"""

import os
import pytest
from unittest.mock import patch, MagicMock
from quarto_book_builder.image_generator import ImageGenerator


@pytest.fixture
def mock_config():
    """Create a mock configuration for testing."""
    return {
        'openai_api_key': 'test_api_key',
        'image_dir': '/tmp/test_images',
        'image_size': '1024x1024',
        'image_format': 'png'
    }


@pytest.fixture
def image_generator(mock_config):
    """Create an image generator instance with mock configuration."""
    with patch('os.makedirs'):  # Mock directory creation
        return ImageGenerator(mock_config)


def test_init(mock_config):
    """Test initialization of ImageGenerator."""
    with patch('os.makedirs') as mock_makedirs:
        generator = ImageGenerator(mock_config)
        
        assert generator.api_key == 'test_api_key'
        assert generator.image_dir == '/tmp/test_images'
        assert generator.image_size == '1024x1024'
        assert generator.image_format == 'png'
        mock_makedirs.assert_called_once_with('/tmp/test_images', exist_ok=True)


def test_get_filename_from_prompt(image_generator):
    """Test generating filename from prompt."""
    filename = image_generator._get_filename_from_prompt("A castle on a hill")
    
    assert filename.startswith("img_")
    assert filename.endswith(".png")
    assert len(filename) == 12  # "img_" + 8 chars + ".png"
    
    # Same prompt should generate same filename
    filename2 = image_generator._get_filename_from_prompt("A castle on a hill")
    assert filename == filename2
    
    # Different prompt should generate different filename
    filename3 = image_generator._get_filename_from_prompt("A forest at sunset")
    assert filename != filename3


@patch('requests.get')
@patch('openai.OpenAI')
def test_generate_image(mock_openai, mock_requests, image_generator):
    """Test generating an image."""
    # Mock OpenAI client
    mock_client = MagicMock()
    mock_openai.return_value = mock_client
    
    # Mock response from OpenAI API
    mock_response = MagicMock()
    mock_response.data = [MagicMock(url="https://example.com/image.png")]
    mock_client.images.generate.return_value = mock_response
    
    # Mock requests response
    mock_requests_response = MagicMock()
    mock_requests.return_value = mock_requests_response
    
    # Mock file operations
    with patch('builtins.open', create=True) as mock_open:
        # Call the method
        result = image_generator.generate_image("A castle on a hill")
        
        # Verify OpenAI API was called correctly
        mock_client.images.generate.assert_called_once_with(
            model="dall-e-3",
            prompt="A castle on a hill",
            n=1,
            size="1024x1024",
            quality="standard",
            response_format="url"
        )
        
        # Verify image was downloaded
        mock_requests.assert_called_once_with(
            "https://example.com/image.png", 
            stream=True,
            timeout=30
        )
        
        # Verify file was written
        mock_open.assert_called()
        
        # Verify result is the filepath
        assert result.endswith(".png")
        assert "/tmp/test_images/img_" in result


@patch('os.path.exists')
def test_generate_image_cached(mock_exists, image_generator):
    """Test that cached images are not regenerated."""
    # Mock that the file exists
    mock_exists.return_value = True
    
    # Add entry to cache
    prompt = "A castle on a hill"
    prompt_hash = prompt_hash = "12345678"  # Simplified for test
    filename = f"img_{prompt_hash}.png"
    image_generator.cache[prompt_hash] = filename
    
    # Mock the hash function to return our test hash
    with patch('hashlib.sha1') as mock_hash:
        mock_hash_instance = MagicMock()
        mock_hash_instance.hexdigest.return_value = prompt_hash + "extra"  # Return longer string that will be sliced
        mock_hash.return_value = mock_hash_instance
        
        # Call the method
        with patch('openai.OpenAI') as mock_openai:  # This shouldn't be called
            result = image_generator.generate_image(prompt)
            
            # Verify OpenAI API was not called
            mock_openai.assert_not_called()
            
            # Verify result is the cached filepath
            assert result == os.path.join('/tmp/test_images', filename)


def test_clear_cache(image_generator):
    """Test clearing the image cache."""
    # Add some entries to cache
    image_generator.cache = {'hash1': 'file1.png', 'hash2': 'file2.png'}
    
    # Mock save_cache
    with patch.object(image_generator, '_save_cache') as mock_save:
        image_generator.clear_cache()
        
        # Verify cache was cleared
        assert image_generator.cache == {}
        mock_save.assert_called_once()


@patch('os.path.exists')
@patch('os.listdir')
def test_list_generated_images(mock_listdir, mock_exists, image_generator):
    """Test listing generated images."""
    # Mock directory exists
    mock_exists.return_value = True
    
    # Mock directory contents
    mock_listdir.return_value = [
        'img_12345678.png',
        'img_abcdef12.png',
        'other_file.txt',
        'not_an_image.png'
    ]
    
    # Call the method
    result = image_generator.list_generated_images()
    
    # Verify result contains only the generated images
    assert len(result) == 2
    assert '/tmp/test_images/img_12345678.png' in result
    assert '/tmp/test_images/img_abcdef12.png' in result
    assert '/tmp/test_images/other_file.txt' not in result
    assert '/tmp/test_images/not_an_image.png' not in result
