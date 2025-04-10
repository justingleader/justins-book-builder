"""
Enhanced error handling for the image generator module.
"""

import os
import hashlib
import requests
import logging
import time
from pathlib import Path
from openai import OpenAI, OpenAIError, APIError, RateLimitError

logger = logging.getLogger(__name__)


class ImageGenerationError(Exception):
    """Exception raised for errors in the image generation process."""
    pass


class ImageGenerator:
    """Handles interaction with OpenAI API for image generation with improved error handling."""
    
    def __init__(self, config):
        """Initialize the image generator.
        
        Args:
            config (dict): Configuration dictionary containing OpenAI API key
        """
        self.config = config
        self.api_key = config.get('openai_api_key')
        
        if not self.api_key:
            logger.warning("OpenAI API key is missing. Image generation will be disabled.")
            self.client = None
        else:
            self.client = OpenAI(api_key=self.api_key)
            
        self.image_dir = config.get('image_dir', 'images')
        self.image_size = config.get('image_size', '1024x1024')
        self.image_format = config.get('image_format', 'png')
        self.max_retries = config.get('max_retries', 3)
        self.retry_delay = config.get('retry_delay', 5)
        self.cache = {}  # Cache of prompt to filename mappings
        
        # Create image directory if it doesn't exist
        os.makedirs(self.image_dir, exist_ok=True)
        
        # Load cache from disk if available
        self._load_cache()
        
    def _load_cache(self):
        """Load cache of previously generated images."""
        cache_path = os.path.join(self.image_dir, '.image_cache.txt')
        if os.path.exists(cache_path):
            try:
                with open(cache_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if '|' in line:
                            prompt_hash, filename = line.strip().split('|', 1)
                            self.cache[prompt_hash] = filename
                logger.info(f"Loaded {len(self.cache)} entries from image cache")
            except Exception as e:
                logger.warning(f"Failed to load image cache: {str(e)}")
        
    def _save_cache(self):
        """Save cache of generated images to disk."""
        cache_path = os.path.join(self.image_dir, '.image_cache.txt')
        try:
            with open(cache_path, 'w', encoding='utf-8') as f:
                for prompt_hash, filename in self.cache.items():
                    f.write(f"{prompt_hash}|{filename}\n")
            logger.info(f"Saved {len(self.cache)} entries to image cache")
        except Exception as e:
            logger.warning(f"Failed to save image cache: {str(e)}")
        
    def generate_image(self, prompt, force_regenerate=False):
        """Generate image from prompt and return file path with improved error handling.
        
        Args:
            prompt (str): Text prompt for image generation
            force_regenerate (bool): Whether to force regeneration even if cached
            
        Returns:
            str: Path to the generated image file
            
        Raises:
            ImageGenerationError: If image generation fails after retries
        """
        # Check if API key is available
        if not self.client:
            logger.warning("Skipping image generation: No OpenAI API key provided")
            return self._create_placeholder_image(prompt)
            
        # Generate a unique filename based on prompt
        prompt_hash = hashlib.sha1(prompt.encode()).hexdigest()[:8]
        filename = f"img_{prompt_hash}.{self.image_format}"
        filepath = os.path.join(self.image_dir, filename)
        
        # Check if image already exists (caching)
        if not force_regenerate and prompt_hash in self.cache and os.path.exists(filepath):
            logger.info(f"Image for prompt '{prompt}' already exists at {filepath}")
            return filepath
            
        logger.info(f"Generating image for prompt: {prompt}")
        
        # Implement retry logic
        for attempt in range(1, self.max_retries + 1):
            try:
                # Call OpenAI API
                response = self.client.images.generate(
                    model="dall-e-3",  # Using the latest model as of March 2025
                    prompt=prompt,
                    n=1,
                    size=self.image_size,
                    quality="standard",
                    response_format="url"
                )
                
                # Get image URL from response
                image_url = response.data[0].url
                
                # Download and save image
                self._download_image(image_url, filepath)
                
                # Update cache
                self.cache[prompt_hash] = filename
                self._save_cache()
                
                logger.info(f"Image generated and saved to {filepath}")
                return filepath
                
            except RateLimitError as e:
                logger.warning(f"Rate limit exceeded (attempt {attempt}/{self.max_retries}): {str(e)}")
                if attempt < self.max_retries:
                    wait_time = self.retry_delay * (2 ** (attempt - 1))  # Exponential backoff
                    logger.info(f"Waiting {wait_time} seconds before retrying...")
                    time.sleep(wait_time)
                else:
                    logger.error("Max retries exceeded for rate limit error")
                    return self._create_placeholder_image(prompt, "Rate limit exceeded")
                    
            except APIError as e:
                logger.warning(f"API error (attempt {attempt}/{self.max_retries}): {str(e)}")
                if attempt < self.max_retries and (500 <= getattr(e, 'status_code', 0) < 600):
                    # Only retry on server errors (5xx)
                    wait_time = self.retry_delay * attempt
                    logger.info(f"Waiting {wait_time} seconds before retrying...")
                    time.sleep(wait_time)
                else:
                    logger.error("API error, not retrying")
                    return self._create_placeholder_image(prompt, f"API error: {str(e)}")
                    
            except OpenAIError as e:
                logger.error(f"OpenAI error: {str(e)}")
                return self._create_placeholder_image(prompt, f"OpenAI error: {str(e)}")
                
            except Exception as e:
                logger.error(f"Unexpected error generating image: {str(e)}")
                return self._create_placeholder_image(prompt, f"Error: {str(e)}")
        
        # If we get here, all retries failed
        logger.error("All image generation attempts failed")
        return self._create_placeholder_image(prompt, "All generation attempts failed")
        
    def _create_placeholder_image(self, prompt, error_message=None):
        """Create a placeholder image when generation fails.
        
        Args:
            prompt (str): Original prompt
            error_message (str, optional): Error message to include
            
        Returns:
            str: Path to the placeholder image
        """
        # Generate a unique filename based on prompt
        prompt_hash = hashlib.sha1(prompt.encode()).hexdigest()[:8]
        filename = f"placeholder_{prompt_hash}.{self.image_format}"
        filepath = os.path.join(self.image_dir, filename)
        
        try:
            # Create a simple text file as placeholder
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"Placeholder for image: {prompt}\n")
                if error_message:
                    f.write(f"Error: {error_message}\n")
                    
            logger.info(f"Created placeholder image at {filepath}")
            return filepath
            
        except Exception as e:
            logger.error(f"Failed to create placeholder image: {str(e)}")
            return os.path.join(self.image_dir, "error.txt")
        
    def _download_image(self, url, filepath):
        """Download image from URL and save to filepath with improved error handling.
        
        Args:
            url (str): URL of the image
            filepath (str): Path to save the image
            
        Raises:
            Exception: If download fails after retries
        """
        for attempt in range(1, self.max_retries + 1):
            try:
                response = requests.get(url, stream=True, timeout=30)
                response.raise_for_status()
                
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        
                logger.info(f"Downloaded image to {filepath}")
                return
                    
            except requests.exceptions.RequestException as e:
                logger.warning(f"Download error (attempt {attempt}/{self.max_retries}): {str(e)}")
                if attempt < self.max_retries:
                    wait_time = self.retry_delay * attempt
                    logger.info(f"Waiting {wait_time} seconds before retrying download...")
                    time.sleep(wait_time)
                else:
                    logger.error("Max retries exceeded for download")
                    raise Exception(f"Failed to download image after {self.max_retries} attempts: {str(e)}")
            
    def list_generated_images(self):
        """List all generated images.
        
        Returns:
            list: List of image file paths
        """
        images = []
        if os.path.exists(self.image_dir):
            for file in os.listdir(self.image_dir):
                if (file.startswith('img_') or file.startswith('placeholder_')) and file.endswith(f'.{self.image_format}'):
                    images.append(os.path.join(self.image_dir, file))
        return images
        
    def clear_cache(self):
        """Clear the image cache (but don't delete files)."""
        self.cache = {}
        self._save_cache()
        logger.info("Image cache cleared")
        
    def get_prompt_for_image(self, image_path):
        """Try to find the original prompt for an image.
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            str: Original prompt or None if not found
        """
        filename = os.path.basename(image_path)
        
        # Extract hash from filename
        if (filename.startswith('img_') or filename.startswith('placeholder_')) and '.' in filename:
            img_hash = filename.split('_')[1].split('.')[0]
            
            # Search cache in reverse
            for prompt_hash, cached_filename in self.cache.items():
                if cached_filename == filename or prompt_hash == img_hash:
                    return prompt_hash
                    
        return None
