#!/usr/bin/env python3
"""
Test script for OpenAI image generation.
This script tests the image generation functionality directly, 
bypassing the Quarto rendering process.
"""

import os
import sys
import logging
import yaml

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='image_generator_test.log',
    filemode='w'
)

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from quarto_book_builder.image_generator import ImageGenerator
    logging.info("Successfully imported ImageGenerator")
except Exception as e:
    logging.error(f"Error importing ImageGenerator: {str(e)}")
    sys.exit(1)

def main():
    """Main test function"""
    logging.info("Starting image generator test")
    
    # Get the current working directory and script directory
    cwd = os.getcwd()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    logging.info(f"Current working directory: {cwd}")
    logging.info(f"Script directory: {script_dir}")
    
    try:
        # Look for config in script directory first (test-book), then in working directory
        config_paths = [
            os.path.join(script_dir, 'config.yaml'),     # test-book/config.yaml
            os.path.join(cwd, 'test-book', 'config.yaml'),  # cwd/test-book/config.yaml
            os.path.join(cwd, 'config.yaml'),            # cwd/config.yaml
        ]
        
        config = None
        for config_path in config_paths:
            logging.info(f"Trying config path: {config_path}")
            if os.path.exists(config_path):
                logging.info(f"Found config at: {config_path}")
                with open(config_path, 'r') as f:
                    config = yaml.safe_load(f)
                break
        
        if not config:
            logging.error("Could not find config.yaml in any location")
            print("ERROR: Could not find config.yaml")
            return
        
        logging.info(f"Config loaded successfully: {config.keys()}")
        
        # Check if we have the required keys
        if 'openai_api_key' not in config:
            logging.error("OpenAI API key not found in config")
            print("ERROR: OpenAI API key not found in config")
            return
        
        # Initialize the image generator with absolute paths
        # Make image_dir an absolute path
        if 'image_dir' in config and not os.path.isabs(config['image_dir']):
            config['image_dir'] = os.path.join(script_dir, config['image_dir'])
            logging.info(f"Using absolute image directory: {config['image_dir']}")
        
        logging.info("Initializing ImageGenerator")
        image_generator = ImageGenerator(config)
        
        # Generate a test image
        prompt = "A serene mountain landscape at sunset with a lake reflecting the orange sky, digital art style"
        logging.info(f"Generating image with prompt: {prompt}")
        
        image_path = image_generator.generate_image(prompt)
        logging.info(f"Image generated: {image_path}")
        
        # Verify the image exists
        if os.path.exists(image_path):
            logging.info(f"Image file exists at {image_path}")
            print(f"SUCCESS: Image generated and saved to {image_path}")
            
            # Get absolute path of the image
            abs_image_path = os.path.abspath(image_path)
            logging.info(f"Absolute image path: {abs_image_path}")
            
            # Get path relative to script dir (for Quarto PDF)
            rel_to_script = os.path.relpath(image_path, script_dir)
            logging.info(f"Path relative to script dir: {rel_to_script}")
        else:
            logging.error(f"Image file does not exist at {image_path}")
            print(f"ERROR: Image file not found at {image_path}")
        
        # Also check image directory
        image_dir = config.get('image_dir', os.path.join(script_dir, 'images'))
        logging.info(f"Checking image directory: {image_dir}")
        if os.path.exists(image_dir):
            files = os.listdir(image_dir)
            logging.info(f"Files in image directory: {files}")
        else:
            logging.error(f"Image directory does not exist: {image_dir}")
        
    except Exception as e:
        logging.exception("Error during image generation test")
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    main() 