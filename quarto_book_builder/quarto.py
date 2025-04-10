"""
Enhanced Quarto integration for the Quarto Book Builder.
"""

import os
import subprocess
import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)


class QuartoRenderer:
    """Interfaces with Quarto for rendering."""
    
    def __init__(self, config):
        """Initialize the Quarto renderer.
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.project_dir = os.path.dirname(os.path.abspath(config.get('config_path', '.')))
        self.build_dir = os.path.join(self.project_dir, config.get('build_dir', '_build'))
        self.output_dir = os.path.join(self.project_dir, config.get('output_dir', '_book'))
        
    def check_quarto_installation(self):
        """Check if Quarto is installed.
        
        Returns:
            tuple: (is_installed, version_string)
            
        Raises:
            RuntimeError: If Quarto command fails
        """
        try:
            result = subprocess.run(
                ['quarto', '--version'], 
                check=True, 
                capture_output=True, 
                text=True
            )
            version = result.stdout.strip()
            logger.info(f"Quarto version: {version}")
            return True, version
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            logger.error(f"Quarto check failed: {str(e)}")
            return False, None
        
    def render(self, project_dir=None, formats=None):
        """Render the book using Quarto.
        
        Args:
            project_dir (str, optional): Path to the project directory
            formats (list, optional): List of output formats to render
            
        Returns:
            bool: True if rendering was successful
            
        Raises:
            subprocess.CalledProcessError: If Quarto command fails
            RuntimeError: If Quarto is not installed
        """
        # Use provided project_dir or default to build_dir
        if project_dir is None:
            project_dir = self.build_dir
            
        logger.info(f"Rendering project in {project_dir}")
        
        # Check if Quarto is installed
        installed, version = self.check_quarto_installation()
        if not installed:
            raise RuntimeError("Quarto is required but not found. Please install Quarto: https://quarto.org/docs/get-started/")
        
        # Ensure _quarto.yml exists in the project directory
        quarto_config_path = os.path.join(project_dir, '_quarto.yml')
        if not os.path.exists(quarto_config_path):
            # Copy from original project directory if available
            original_config = os.path.join(self.project_dir, '_quarto.yml')
            if os.path.exists(original_config):
                shutil.copy2(original_config, quarto_config_path)
                logger.info(f"Copied Quarto config from {original_config} to {quarto_config_path}")
            else:
                raise FileNotFoundError(f"Quarto configuration file not found: {quarto_config_path}")
        
        # Build command
        cmd = ['quarto', 'render', project_dir]
        
        if formats:
            cmd.extend(['--to', ','.join(formats)])
            
        logger.info(f"Running command: {' '.join(cmd)}")
        
        try:
            # Run Quarto command
            result = subprocess.run(
                cmd, 
                check=True, 
                capture_output=True, 
                text=True
            )
            
            logger.info(f"Quarto render output: {result.stdout}")
            
            if result.stderr:
                logger.warning(f"Quarto render warnings: {result.stderr}")
            
            # Copy output files to project directory if needed
            self._copy_output_files(project_dir)
                
            return True
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Quarto render failed: {e.stderr}")
            raise
            
    def _copy_output_files(self, project_dir):
        """Copy output files from _book directory to project output directory.
        
        Args:
            project_dir (str): Path to the project directory
        """
        # Quarto typically outputs to _book directory within the project
        quarto_output_dir = os.path.join(project_dir, '_book')
        
        if os.path.exists(quarto_output_dir) and os.path.isdir(quarto_output_dir):
            # Create output directory if it doesn't exist
            os.makedirs(self.output_dir, exist_ok=True)
            
            # Copy all files from Quarto output to our output directory
            for item in os.listdir(quarto_output_dir):
                src = os.path.join(quarto_output_dir, item)
                dst = os.path.join(self.output_dir, item)
                
                if os.path.isfile(src):
                    shutil.copy2(src, dst)
                    logger.info(f"Copied {src} to {dst}")
                elif os.path.isdir(src):
                    if os.path.exists(dst):
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst)
                    logger.info(f"Copied directory {src} to {dst}")
    
    def get_output_files(self):
        """Get list of output files.
        
        Returns:
            dict: Dictionary of output files by format
        """
        result = {
            'pdf': [],
            'epub': [],
            'html': [],
            'other': []
        }
        
        if not os.path.exists(self.output_dir):
            return result
            
        for file in os.listdir(self.output_dir):
            file_path = os.path.join(self.output_dir, file)
            if not os.path.isfile(file_path):
                continue
                
            if file.endswith('.pdf'):
                result['pdf'].append(file_path)
            elif file.endswith('.epub'):
                result['epub'].append(file_path)
            elif file.endswith('.html'):
                result['html'].append(file_path)
            else:
                result['other'].append(file_path)
                
        return result
        
    def preview(self, format='html'):
        """Preview the book using Quarto.
        
        Args:
            format (str): Format to preview ('html', 'pdf', 'epub')
            
        Returns:
            bool: True if preview was successful
        """
        if format not in ('html', 'pdf', 'epub'):
            logger.error(f"Unsupported preview format: {format}")
            return False
            
        # Check if output file exists
        output_files = self.get_output_files()
        if not output_files[format]:
            logger.error(f"No {format} output files found")
            return False
            
        # For HTML, use Quarto preview
        if format == 'html':
            try:
                cmd = ['quarto', 'preview', self.project_dir]
                logger.info(f"Running command: {' '.join(cmd)}")
                
                # Run in background
                subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                
                logger.info(f"Started Quarto preview server")
                return True
                
            except Exception as e:
                logger.error(f"Quarto preview failed: {str(e)}")
                return False
                
        # For PDF and EPUB, try to open with system default
        try:
            file_path = output_files[format][0]
            
            if os.name == 'nt':  # Windows
                os.startfile(file_path)
            elif os.name == 'posix':  # Linux, macOS
                if format == 'pdf':
                    subprocess.Popen(['xdg-open', file_path])
                elif format == 'epub':
                    subprocess.Popen(['xdg-open', file_path])
                    
            logger.info(f"Opened {file_path} for preview")
            return True
            
        except Exception as e:
            logger.error(f"Failed to open {format} file: {str(e)}")
            return False
