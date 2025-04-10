"""
PDF output formatting for the Quarto Book Builder.
"""

import os
import logging
import yaml
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)


class PDFFormatter:
    """Handles PDF-specific formatting and configuration."""
    
    def __init__(self, config):
        """Initialize the PDF formatter.
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.project_dir = os.path.dirname(os.path.abspath(config.get('config_path', '.')))
        self.build_dir = os.path.join(self.project_dir, config.get('build_dir', '_build'))
        
        # PDF-specific settings
        self.pdf_settings = config.get('pdf', {})
        if not self.pdf_settings:
            self.pdf_settings = {
                'documentclass': 'book',
                'geometry': '6in,9in',
                'toc': True,
                'toc-depth': 3,
                'number-sections': True,
                'colorlinks': True
            }
        
    def configure_pdf_output(self):
        """Configure PDF output settings in Quarto configuration.
        
        Returns:
            bool: True if configuration was successful
        """
        logger.info("Configuring PDF output settings")
        
        # Path to Quarto configuration file
        quarto_config_path = os.path.join(self.build_dir, '_quarto.yml')
        
        try:
            # Load existing Quarto configuration
            if os.path.exists(quarto_config_path):
                with open(quarto_config_path, 'r', encoding='utf-8') as f:
                    quarto_config = yaml.safe_load(f)
            else:
                # Create new configuration if it doesn't exist
                quarto_config = {
                    'project': {'type': 'book'},
                    'book': {},
                    'format': {}
                }
            
            # Ensure format section exists
            if 'format' not in quarto_config:
                quarto_config['format'] = {}
                
            # Update PDF format settings
            quarto_config['format']['pdf'] = self.pdf_settings
            
            # Write updated configuration
            with open(quarto_config_path, 'w', encoding='utf-8') as f:
                yaml.dump(quarto_config, f, default_flow_style=False)
                
            logger.info(f"Updated PDF configuration in {quarto_config_path}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to configure PDF output: {str(e)}")
            return False
            
    def create_latex_template(self):
        """Create or update LaTeX template for PDF output.
        
        Returns:
            bool: True if template creation was successful
        """
        # Check if custom LaTeX template is specified
        latex_template = self.pdf_settings.get('template')
        if not latex_template:
            logger.info("No custom LaTeX template specified, using Quarto defaults")
            return True
            
        # Path to template file
        template_path = os.path.join(self.project_dir, latex_template)
        
        # If template doesn't exist, create a default one
        if not os.path.exists(template_path):
            logger.info(f"Creating default LaTeX template at {template_path}")
            
            # Create template directory if needed
            os.makedirs(os.path.dirname(template_path), exist_ok=True)
            
            # Write default template
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(self._get_default_latex_template())
                
        # Copy template to build directory
        build_template_path = os.path.join(self.build_dir, os.path.basename(template_path))
        shutil.copy2(template_path, build_template_path)
        logger.info(f"Copied LaTeX template to {build_template_path}")
        
        return True
        
    def _get_default_latex_template(self):
        """Get default LaTeX template content.
        
        Returns:
            str: Default LaTeX template
        """
        return r"""% Default LaTeX template for Quarto Book Builder
% This template extends Quarto's default template with custom styling

% !TEX program = xelatex
\documentclass[$if(fontsize)$$fontsize$,$endif$$if(papersize)$$papersize$,$endif$$for(classoption)$$classoption$$sep$,$endfor$]{$documentclass$}
\usepackage{amsmath,amssymb}
\usepackage{lmodern}
\usepackage{iftex}
\usepackage{fontspec}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{caption}
\usepackage{mdframed}

% Define custom environments for our special sections
\newenvironment{featured-quote}{%
  \begin{mdframed}[linewidth=1pt, linecolor=gray, backgroundcolor=gray!10]
  \begin{quotation}\itshape
}{%
  \end{quotation}
  \end{mdframed}
}

\newenvironment{listicle}{%
  \begin{mdframed}[linewidth=1pt, linecolor=gray, backgroundcolor=gray!5]
}{%
  \end{mdframed}
}

% Title formatting
\usepackage{titlesec}
\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries}{\chaptertitlename\ \thechapter}{20pt}{\Huge}
\titleformat{\section}
  {\normalfont\Large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}
  {\normalfont\large\bfseries}{\thesubsection}{1em}{}

% Page layout
\usepackage{geometry}
\geometry{$if(geometry)$$geometry$$else$letterpaper$endif$}

% Header and footer
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

% Hyperref settings
\hypersetup{
  colorlinks=true,
  linkcolor=$if(linkcolor)$$linkcolor$$else$blue$endif$,
  filecolor=$if(filecolor)$$filecolor$$else$magenta$endif$,
  citecolor=$if(citecolor)$$citecolor$$else$green$endif$,
  urlcolor=$if(urlcolor)$$urlcolor$$else$blue$endif$,
  pdfauthor={$author-meta$},
  pdftitle={$title-meta$}
}

% Include any custom LaTeX commands
$for(header-includes)$
$header-includes$
$endfor$

\begin{document}

% Title page
\begin{titlepage}
  \centering
  \vspace*{2cm}
  {\Huge\bfseries $title$\par}
  \vspace{1.5cm}
  {\Large $author$\par}
  \vspace{1cm}
  {\large $date$\par}
  \vfill
\end{titlepage}

% Table of contents
$if(toc)$
\tableofcontents
\newpage
$endif$

% Document content
$body$

\end{document}
"""
        
    def add_latex_preamble(self):
        """Add LaTeX preamble for custom environments.
        
        Returns:
            bool: True if preamble addition was successful
        """
        # Check if include-in-header is specified
        include_in_header = self.pdf_settings.get('include-in-header')
        if include_in_header:
            logger.info(f"Using specified include-in-header: {include_in_header}")
            return True
            
        # Create a default preamble file
        preamble_path = os.path.join(self.project_dir, 'latex-preamble.tex')
        build_preamble_path = os.path.join(self.build_dir, 'latex-preamble.tex')
        
        try:
            # Write default preamble if it doesn't exist
            if not os.path.exists(preamble_path):
                with open(preamble_path, 'w', encoding='utf-8') as f:
                    f.write(self._get_default_latex_preamble())
                logger.info(f"Created default LaTeX preamble at {preamble_path}")
                
            # Copy to build directory
            shutil.copy2(preamble_path, build_preamble_path)
            
            # Update Quarto configuration to include preamble
            quarto_config_path = os.path.join(self.build_dir, '_quarto.yml')
            
            if os.path.exists(quarto_config_path):
                with open(quarto_config_path, 'r', encoding='utf-8') as f:
                    quarto_config = yaml.safe_load(f)
                    
                # Update PDF format settings
                if 'format' not in quarto_config:
                    quarto_config['format'] = {}
                if 'pdf' not in quarto_config['format']:
                    quarto_config['format']['pdf'] = {}
                    
                quarto_config['format']['pdf']['include-in-header'] = 'latex-preamble.tex'
                
                # Write updated configuration
                with open(quarto_config_path, 'w', encoding='utf-8') as f:
                    yaml.dump(quarto_config, f, default_flow_style=False)
                    
                logger.info(f"Updated Quarto configuration to include LaTeX preamble")
                return True
                
        except Exception as e:
            logger.error(f"Failed to add LaTeX preamble: {str(e)}")
            
        return False
        
    def _get_default_latex_preamble(self):
        """Get default LaTeX preamble content.
        
        Returns:
            str: Default LaTeX preamble
        """
        return r"""% Default LaTeX preamble for Quarto Book Builder
% This file defines custom environments for special sections

% Required packages
\usepackage{mdframed}
\usepackage{xcolor}

% Define custom environments for special sections
\newenvironment{featured-quote}{%
  \begin{mdframed}[linewidth=1pt, linecolor=gray, backgroundcolor=gray!10]
  \begin{quotation}\itshape
}{%
  \end{quotation}
  \end{mdframed}
}

\newenvironment{listicle}{%
  \begin{mdframed}[linewidth=1pt, linecolor=gray, backgroundcolor=gray!5]
}{%
  \end{mdframed}
}

% Add more custom environments as needed
"""
        
    def configure_pdf_metadata(self, title=None, author=None, date=None):
        """Configure PDF metadata.
        
        Args:
            title (str, optional): Book title
            author (str, optional): Book author
            date (str, optional): Book date
            
        Returns:
            bool: True if configuration was successful
        """
        quarto_config_path = os.path.join(self.build_dir, '_quarto.yml')
        
        try:
            # Load existing Quarto configuration
            if os.path.exists(quarto_config_path):
                with open(quarto_config_path, 'r', encoding='utf-8') as f:
                    quarto_config = yaml.safe_load(f)
            else:
                return False
                
            # Ensure book section exists
            if 'book' not in quarto_config:
                quarto_config['book'] = {}
                
            # Update metadata if provided
            if title:
                quarto_config['book']['title'] = title
            if author:
                quarto_config['book']['author'] = author
            if date:
                quarto_config['book']['date'] = date
                
            # Write updated configuration
            with open(quarto_config_path, 'w', encoding='utf-8') as f:
                yaml.dump(quarto_config, f, default_flow_style=False)
                
            logger.info(f"Updated PDF metadata in {quarto_config_path}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to configure PDF metadata: {str(e)}")
            return False
