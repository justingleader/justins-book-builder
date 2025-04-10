#!/usr/bin/env python3
"""
Process input files and move them to draft working directory, then delete the input files.
"""

import os
import shutil
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def process_input_files(project_name):
    """Process input files and move them to draft working directory.
    
    Args:
        project_name (str): Name of the project directory under projects/
    """
    # Construct paths
    project_dir = Path('projects') / project_name
    input_dir = project_dir / 'input'
    draft_dir = project_dir / 'draft-1' / 'working'
    
    # Ensure directories exist
    if not input_dir.exists():
        logger.error(f"Input directory not found: {input_dir}")
        return False
        
    if not draft_dir.exists():
        logger.info(f"Creating draft directory: {draft_dir}")
        draft_dir.mkdir(parents=True, exist_ok=True)
    
    # Process each file in input directory
    processed_files = []
    for file_path in input_dir.glob('*'):
        if file_path.is_file() and file_path.suffix in ('.md', '.qmd'):
            try:
                # Copy file to draft directory
                dest_path = draft_dir / file_path.name
                shutil.copy2(file_path, dest_path)
                processed_files.append(file_path)
                logger.info(f"Processed: {file_path.name}")
            except Exception as e:
                logger.error(f"Error processing {file_path.name}: {str(e)}")
                return False
    
    # Delete processed files
    for file_path in processed_files:
        try:
            file_path.unlink()
            logger.info(f"Deleted: {file_path.name}")
        except Exception as e:
            logger.error(f"Error deleting {file_path.name}: {str(e)}")
            return False
    
    logger.info(f"Successfully processed and deleted {len(processed_files)} files")
    return True

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python process_input.py <project_name>")
        sys.exit(1)
        
    project_name = sys.argv[1]
    if process_input_files(project_name):
        sys.exit(0)
    else:
        sys.exit(1) 