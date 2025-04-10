"""
Enhanced error handling for the CLI interface.
"""

import os
import sys
import logging
import click
from pathlib import Path

from .config import ConfigManager
from .preprocessor import MarkdownPreprocessor
from .image_generator import ImageGenerator, ImageGenerationError
from .template_manager import TemplateManager
from .quarto import QuartoRenderer
from .pdf_formatter import PDFFormatter
from .epub_formatter import EPUBFormatter
from .utils import setup_logging

# Set up logging
logger = setup_logging()


@click.group()
@click.version_option(version='0.1.0')
def cli():
    """Quarto-Based CLI Book Builder.
    
    A tool for building books with Quarto, AI-generated images, and custom section templates.
    """
    pass


@cli.command()
@click.argument('project_dir', type=click.Path())
@click.option('--title', '-t', help='Book title')
@click.option('--author', '-a', help='Book author')
def init(project_dir, title, author):
    """Initialize a new book project."""
    project_dir = os.path.abspath(project_dir)
    
    try:
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
            click.echo(f"Created project directory: {project_dir}")
        
        # Create project structure
        os.makedirs(os.path.join(project_dir, 'chapters'), exist_ok=True)
        os.makedirs(os.path.join(project_dir, 'images'), exist_ok=True)
        os.makedirs(os.path.join(project_dir, 'templates'), exist_ok=True)
        
        # Create example config files
        config_path = os.path.join(project_dir, 'config.yaml')
        quarto_config_path = os.path.join(project_dir, '_quarto.yml')
        
        if not os.path.exists(config_path):
            with open(config_path, 'w') as f:
                f.write("""# Quarto Book Builder Configuration
openai_api_key: "your-api-key-here"
image_dir: "images"
build_dir: "_build"
output_dir: "_book"
max_retries: 3
retry_delay: 5
custom_sections:
  featured-quote:
    html: |
      <div class="featured-quote">
        <blockquote>{{ content }}</blockquote>
        <p class="attribution">— {{ author }}</p>
      </div>
    latex: |
      \\begin{quotation}\\noindent\\textit{{{ content }}}\\\\
      \\hfill--- {{ author }}\\end{quotation}
  listicle:
    html: |
      <div class="listicle">
        <h3>{{ title }}</h3>
        {{ content }}
      </div>
    latex: |
      \\begin{mdframed}[backgroundcolor=gray!20]\\textbf{Listicle: {{ title }}} 
      {{ content }}
      \\end{mdframed}
""")
            click.echo(f"Created configuration file: {config_path}")
        
        if not os.path.exists(quarto_config_path):
            book_title = title or "My Book"
            book_author = author or "Author Name"
            
            with open(quarto_config_path, 'w') as f:
                f.write(f"""project:
  type: book

book:
  title: "{book_title}"
  author: "{book_author}"
  date: "2025-04-06"
  chapters:
    - "chapters/01-intro.qmd"
  toc: true
  cover-image: "images/cover.png"

format:
  pdf:
    documentclass: book
    geometry: "6in,9in"
    toc: true
  epub:
    toc: true
    cover-image: "images/cover.png"
    css: "epub.css"
""")
            click.echo(f"Created Quarto configuration file: {quarto_config_path}")
        
        # Create example chapter
        chapter_path = os.path.join(project_dir, 'chapters', '01-intro.qmd')
        if not os.path.exists(chapter_path):
            with open(chapter_path, 'w') as f:
                f.write(f"""---
title: "Introduction"
---

# Introduction

Welcome to my book. This is an example chapter.

{{{{image: A digital painting of a castle on a hill at sunset, with golden skies}}}}

::: featured-quote
"The journey matters more than the destination."
**— Someone Famous**
:::
""")
            click.echo(f"Created example chapter: {chapter_path}")
        
        # Create example CSS for EPUB
        css_path = os.path.join(project_dir, 'epub.css')
        if not os.path.exists(css_path):
            epub_formatter = EPUBFormatter({'config_path': config_path})
            with open(css_path, 'w') as f:
                f.write(epub_formatter._get_default_epub_css())
            click.echo(f"Created EPUB CSS file: {css_path}")
        
        click.echo(f"Initialized book project in {project_dir}")
        click.echo("\nNext steps:")
        click.echo("1. Edit config.yaml and add your OpenAI API key")
        click.echo("2. Edit _quarto.yml to configure your book")
        click.echo("3. Edit chapters/01-intro.qmd or add more chapter files")
        click.echo("4. Run 'quarto-book-builder build' to build your book")
    
    except Exception as e:
        click.echo(f"Error initializing project: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('project_dir', type=click.Path(exists=True))
@click.option('--config', '-c', default='config.yaml', help='Configuration file')
def preprocess(project_dir, config):
    """Preprocess Markdown files without rendering."""
    project_dir = os.path.abspath(project_dir)
    config_path = os.path.join(project_dir, config)
    
    try:
        # Check if config file exists
        if not os.path.exists(config_path):
            click.echo(f"Error: Configuration file not found: {config_path}", err=True)
            sys.exit(1)
            
        # Load configuration
        config_manager = ConfigManager(config_path)
        config_data = config_manager.load()
        config_data['config_path'] = config_path
        
        # Initialize components
        image_generator = ImageGenerator(config_data)
        template_manager = TemplateManager(config_data)
        preprocessor = MarkdownPreprocessor(config_data, image_generator, template_manager)
        
        # Process all Markdown files
        processed_files = preprocessor.process_project()
        
        # Copy static files
        copied_files = preprocessor.copy_static_files()
        
        click.echo(f"Preprocessed {len(processed_files)} Markdown files")
        click.echo(f"Copied {copied_files} static files")
        click.echo("Preprocessing complete")
        
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        logger.error(f"Preprocessing failed: {str(e)}", exc_info=True)
        sys.exit(1)


@cli.command()
@click.argument('project_dir', type=click.Path(exists=True))
@click.option('--config', '-c', default='config.yaml', help='Configuration file')
@click.option('--format', '-f', default=None, help='Output format (pdf, epub, or both)')
@click.option('--force', is_flag=True, help='Force regeneration of all images')
def build(project_dir, config, format, force):
    """Build the book project."""
    project_dir = os.path.abspath(project_dir)
    config_path = os.path.join(project_dir, config)
    
    try:
        # Check if config file exists
        if not os.path.exists(config_path):
            click.echo(f"Error: Configuration file not found: {config_path}", err=True)
            sys.exit(1)
            
        # Load configuration
        config_manager = ConfigManager(config_path)
        config_data = config_manager.load()
        config_data['config_path'] = config_path
        
        # Initialize components
        image_generator = ImageGenerator(config_data)
        template_manager = TemplateManager(config_data)
        preprocessor = MarkdownPreprocessor(config_data, image_generator, template_manager)
        quarto_renderer = QuartoRenderer(config_data)
        pdf_formatter = PDFFormatter(config_data)
        epub_formatter = EPUBFormatter(config_data)
        
        # Check if Quarto is installed
        installed, version = quarto_renderer.check_quarto_installation()
        if not installed:
            click.echo("Error: Quarto is required but not found. Please install Quarto: https://quarto.org/docs/get-started/", err=True)
            sys.exit(1)
        click.echo(f"Using Quarto version: {version}")
        
        # Process all Markdown files
        click.echo("Preprocessing Markdown files...")
        processed_files = preprocessor.process_project()
        click.echo(f"Preprocessed {len(processed_files)} Markdown files")
        
        # Copy static files
        copied_files = preprocessor.copy_static_files()
        click.echo(f"Copied {copied_files} static files")
        
        # Configure output formats
        formats = []
        if format:
            formats = format.split(',')
        
        # Configure PDF output if needed
        if not formats or 'pdf' in formats:
            click.echo("Configuring PDF output...")
            pdf_formatter.configure_pdf_output()
            pdf_formatter.create_latex_template()
            pdf_formatter.add_latex_preamble()
        
        # Configure EPUB output if needed
        if not formats or 'epub' in formats:
            click.echo("Configuring EPUB output...")
            epub_formatter.configure_epub_output()
            epub_formatter.create_epub_css()
            epub_formatter.ensure_kindle_compatibility()
        
        # Render with Quarto
        click.echo("Rendering with Quarto...")
        build_dir = os.path.join(project_dir, config_data.get('build_dir', '_build'))
        try:
            quarto_renderer.render(build_dir, formats)
        except Exception as e:
            click.echo(f"Error during Quarto rendering: {str(e)}", err=True)
            click.echo("The preprocessing was completed successfully. You can try running Quarto manually:")
            click.echo(f"  cd {build_dir} && quarto render")
            sys.exit(1)
        
        # Get output files
        output_files = quarto_renderer.get_output_files()
        
        # Report results
        click.echo("\nBuild complete!")
        if output_files['pdf']:
            click.echo(f"PDF output: {', '.join(output_files['pdf'])}")
        if output_files['epub']:
            click.echo(f"EPUB output: {', '.join(output_files['epub'])}")
        if output_files['html']:
            click.echo(f"HTML output: {', '.join(output_files['html'])}")
        
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        logger.error(f"Build failed: {str(e)}", exc_info=True)
        sys.exit(1)


@cli.command()
@click.argument('project_dir', type=click.Path(exists=True))
@click.option('--config', '-c', default='config.yaml', help='Configuration file')
@click.option('--format', '-f', default='html', help='Format to preview (html, pdf, epub)')
def preview(project_dir, config, format):
    """Preview the book."""
    project_dir = os.path.abspath(project_dir)
    config_path = os.path.join(project_dir, config)
    
    try:
        # Check if config file exists
        if not os.path.exists(config_path):
            click.echo(f"Error: Configuration file not found: {config_path}", err=True)
            sys.exit(1)
            
        # Load configuration
        config_manager = ConfigManager(config_path)
        config_data = config_manager.load()
        config_data['config_path'] = config_path
        
        # Initialize Quarto renderer
        quarto_renderer = QuartoRenderer(config_data)
        
        # Check if Quarto is installed
        installed, version = quarto_renderer.check_quarto_installation()
        if not installed:
            click.echo("Error: Quarto is required but not found. Please install Quarto: https://quarto.org/docs/get-started/", err=True)
            sys.exit(1)
        
        # Preview book
        if quarto_renderer.preview(format):
            if format == 'html':
                click.echo("Started Quarto preview server. Press Ctrl+C to stop.")
                # Keep process running for HTML preview
                try:
                    import time
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    click.echo("Preview stopped.")
            else:
                click.echo(f"Opened {format.upper()} file for preview.")
        else:
            click.echo(f"Failed to preview {format.upper()} output. Make sure you have built the book first.", err=True)
            sys.exit(1)
        
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        logger.error(f"Preview failed: {str(e)}", exc_info=True)
        sys.exit(1)


@cli.command()
@click.argument('project_dir', type=click.Path(exists=True))
def clean(project_dir):
    """Clean generated files."""
    project_dir = os.path.abspath(project_dir)
    
    try:
        # Load configuration to get build and output directories
        config_path = os.path.join(project_dir, 'config.yaml')
        if os.path.exists(config_path):
            config_manager = ConfigManager(config_path)
            config_data = config_manager.load()
            build_dir = os.path.join(project_dir, config_data.get('build_dir', '_build'))
            output_dir = os.path.join(project_dir, config_data.get('output_dir', '_book'))
        else:
            build_dir = os.path.join(project_dir, '_build')
            output_dir = os.path.join(project_dir, '_book')
        
        # Remove build directory
        if os.path.exists(build_dir):
            import shutil
            shutil.rmtree(build_dir)
            click.echo(f"Removed {build_dir}")
        
        # Remove output directory
        if os.path.exists(output_dir):
            import shutil
            shutil.rmtree(output_dir)
            click.echo(f"Removed {output_dir}")
        
        click.echo("Clean complete")
        
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        logger.error(f"Clean failed: {str(e)}", exc_info=True)
        sys.exit(1)


@cli.command()
@click.argument('project_dir', type=click.Path(exists=True))
@click.option('--config', '-c', default='config.yaml', help='Configuration file')
def validate(project_dir, config):
    """Validate the project configuration and structure."""
    project_dir = os.path.abspath(project_dir)
    config_path = os.path.join(project_dir, config)
    
    try:
        # Check if config file exists
        if not os.path.exists(config_path):
            click.echo(f"Error: Configuration file not found: {config_path}", err=True)
            sys.exit(1)
            
        click.echo(f"Validating project: {project_dir}")
        
        # Check configuration
        click.echo("Checking configuration...")
        config_manager = ConfigManager(config_path)
        config_data = config_manager.load()
        
        # Check for required directories
        chapters_dir = os.path.join(project_dir, 'chapters')
        if not os.path.exists(chapters_dir):
            click.echo("Warning: 'chapters' directory not found")
        else:
            chapter_files = [f for f in os.listdir(chapters_dir) if f.endswith(('.md', '.qmd'))]
            click.echo(f"Found {len(chapter_files)} chapter files")
        
        # Check for Quarto config
        quarto_config_path = os.path.join(project_dir, '_quarto.yml')
        if not os.path.exists(quarto_config_path):
            click.echo("Warning: '_quarto.yml' file not found")
        else:
            click.echo("Quarto configuration file found")
        
        # Check for OpenAI API key
        api_key = config_data.get('openai_api_key')
        if not api_key:
            click.echo("Warning: OpenAI API key not found in configuration")
        elif api_key == "your-api-key-here":
            click.echo("Warning: Default OpenAI API key found, please update with your actual key")
        else:
            click.echo("OpenAI API key found")
        
        # Check Quarto installation
        quarto_renderer = QuartoRenderer(config_data)
        installed, version = quarto_renderer.check_quarto_installation()
        if installed:
            click.echo(f"Quarto is installed: {version}")
        else:
            click.echo("Warning: Quarto is not installed")
        
        click.echo("Validation complete")
        
    except Exception as e:
        click.echo(f"Error during validation: {str(e)}", err=True)
        logger.error(f"Validation failed: {str(e)}", exc_info=True)
        sys.exit(1)


@cli.command()
@click.argument('markdown_files', nargs=-1, type=click.Path(exists=True, readable=True))
@click.option('--config-file', '-c', type=click.Path(exists=True, readable=True), required=True, help='Configuration file path')
@click.option('--output-dir', '-o', type=click.Path(), help='Output directory')
@click.option('--format', '-f', type=click.Choice(['pdf', 'epub', 'html', 'all']), default='all', help='Output format')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
def build_from_markdown(markdown_files, config_file, output_dir=None, format='all', verbose=False):
    """Build a book directly from markdown files, using metadata from frontmatter."""
    # Set log level
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        
    logger.info(f"Building book from markdown files with metadata from frontmatter")
    
    if not markdown_files:
        logger.error("No markdown files provided")
        return 1
        
    try:
        # Load configuration
        config_manager = ConfigManager(config_file)
        config = config_manager.load_config()
        
        # Override configuration with command-line options
        if output_dir:
            config['output_dir'] = output_dir
            
        # Set up working directory
        project_dir = os.path.dirname(os.path.abspath(config_file))
        os.chdir(project_dir)
        
        # Initialize components
        image_generator = ImageGenerator(config)
        template_manager = TemplateManager(config)
        preprocessor = MarkdownPreprocessor(config, image_generator, template_manager)
        
        # Create a temporary _quarto.yml if needed
        quarto_config_path = os.path.join(project_dir, '_quarto.yml')
        if not os.path.exists(quarto_config_path):
            # Find the index file if it exists
            index_file = None
            for file in markdown_files:
                if os.path.basename(file) in ('index.md', 'index.qmd'):
                    index_file = file
                    break
                    
            # Create basic config
            quarto_config = {
                'project': {'type': 'book'},
                'book': {
                    'chapters': [os.path.relpath(f, project_dir) for f in markdown_files]
                },
                'format': {
                    'pdf': {
                        'documentclass': 'book',
                        'filters': ['filters/openai-image.lua']
                    },
                    'epub': {
                        'filters': ['filters/openai-image.lua']
                    },
                    'html': {
                        'filters': ['filters/openai-image.lua']
                    }
                }
            }
            
            # Write config
            with open(quarto_config_path, 'w') as f:
                import yaml
                yaml.dump(quarto_config, f, default_flow_style=False)
                
            logger.info(f"Created temporary Quarto config: {quarto_config_path}")
        
        # Process each markdown file
        processed_files = []
        for file in markdown_files:
            rel_path = os.path.relpath(file, project_dir)
            output_path = os.path.join(preprocessor.build_dir, rel_path)
            
            if preprocessor.process_file(file, output_path):
                processed_files.append(output_path)
                
        logger.info(f"Processed {len(processed_files)} files")
        
        # Generate quarto config with metadata from markdown frontmatter
        preprocessor.generate_quarto_config()
        
        # Copy static files (images, etc.)
        copied_files = preprocessor.copy_static_files()
        logger.info(f"Copied {copied_files} static files")
        
        # Render the book
        quarto = QuartoRenderer(config)
        
        # Check Quarto installation
        installed, version = quarto.check_quarto_installation()
        if not installed:
            logger.error("Quarto is not installed. Please install Quarto: https://quarto.org/docs/get-started/")
            return 1
            
        # Determine formats to render
        formats = []
        if format == 'all':
            formats = ['pdf', 'epub', 'html']
        else:
            formats = [format]
            
        # Render in specified formats
        for fmt in formats:
            logger.info(f"Rendering book in {fmt} format...")
            try:
                quarto.render(preprocessor.build_dir, [fmt])
                logger.info(f"Successfully rendered {fmt} format")
            except Exception as e:
                logger.error(f"Failed to render {fmt} format: {e}")
                
        # List output files
        output_files = quarto.get_output_files()
        logger.info("Output files:")
        for fmt, files in output_files.items():
            for f in files:
                logger.info(f"  {fmt}: {f}")
                
        logger.info("Book build completed successfully")
        
    except Exception as e:
        logger.error(f"Error building book: {e}", exc_info=True)
        return 1
        
    return 0


if __name__ == '__main__':
    cli()
