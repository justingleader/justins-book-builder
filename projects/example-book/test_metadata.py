#!/usr/bin/env python3
"""
Test script to verify the extraction of metadata from markdown files.
"""

import os
import sys
import logging
import yaml
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from quarto_book_builder.preprocessor import MarkdownPreprocessor
    from quarto_book_builder.config import ConfigManager
except ImportError as e:
    logger.error(f"Failed to import required module: {e}")
    sys.exit(1)

def extract_frontmatter(file_path):
    """Extract and print frontmatter from a markdown file."""
    logger.info(f"Extracting frontmatter from: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Use a simple regex to extract YAML frontmatter
        yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if yaml_match:
            # Extract front matter
            front_matter = yaml_match.group(1)
            content_without_frontmatter = content[yaml_match.end():]
            
            try:
                # Parse YAML
                metadata = yaml.safe_load(front_matter)
                if not isinstance(metadata, dict):
                    metadata = {}
                    
                if metadata:
                    logger.info(f"Extracted metadata: {metadata}")
                    print(f"\nFile: {os.path.basename(file_path)}")
                    print("Metadata:")
                    for key, value in metadata.items():
                        print(f"  {key}: {value}")
                    print("")
                    return metadata
            except Exception as e:
                logger.warning(f"Failed to parse YAML front matter: {str(e)}")
        
        logger.info(f"No metadata found in {file_path}")
        print(f"\nNo metadata found in {os.path.basename(file_path)}\n")
        return {}
    
    except Exception as e:
        logger.error(f"Error extracting frontmatter: {e}")
        return None

def main():
    """Main function to test metadata extraction."""
    logger.info("Starting metadata extraction test")
    
    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Files to test
    test_files = [
        os.path.join(script_dir, "index.qmd"),
        os.path.join(script_dir, "chapters", "01-intro.qmd"),
        os.path.join(script_dir, "chapters", "02-ai-images.qmd")
    ]
    
    # Extract metadata from each file
    all_metadata = {}
    for file in test_files:
        if os.path.exists(file):
            metadata = extract_frontmatter(file)
            if metadata:
                all_metadata[file] = metadata
        else:
            logger.warning(f"File not found: {file}")
    
    # Check if we found index metadata
    index_file = os.path.join(script_dir, "index.qmd")
    if index_file in all_metadata:
        index_metadata = all_metadata[index_file]
        print("\nBook Metadata (from index):")
        if 'title' in index_metadata:
            print(f"  Title: {index_metadata['title']}")
        if 'author' in index_metadata:
            print(f"  Author: {index_metadata['author']}")
        if 'date' in index_metadata:
            print(f"  Date: {index_metadata['date']}")
    
    # Generate a temporary _quarto.yml to demonstrate
    quarto_config = {
        'project': {'type': 'book'},
        'book': {}
    }
    
    # Add metadata from index file if available
    if index_file in all_metadata:
        index_metadata = all_metadata[index_file]
        if 'title' in index_metadata:
            quarto_config['book']['title'] = index_metadata['title']
        if 'author' in index_metadata:
            quarto_config['book']['author'] = index_metadata['author']
        if 'date' in index_metadata:
            quarto_config['book']['date'] = index_metadata['date']
    
    # Add chapters
    chapters = []
    for file in test_files:
        if os.path.exists(file):
            rel_path = os.path.relpath(file, script_dir)
            chapters.append(rel_path)
    
    quarto_config['book']['chapters'] = chapters
    
    # Display the generated config
    print("\nGenerated Quarto Config:")
    print(yaml.dump(quarto_config, default_flow_style=False))
    
    # Save the config to a file for testing
    test_config_path = os.path.join(script_dir, "test_quarto.yml")
    with open(test_config_path, 'w') as f:
        yaml.dump(quarto_config, f, default_flow_style=False)
    print(f"\nConfig saved to: {test_config_path}")
    
    logger.info("Metadata extraction test completed")

if __name__ == "__main__":
    main() 