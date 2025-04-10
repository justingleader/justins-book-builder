# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build/Test Commands
- Build book: `python example-book/build_book.py`
- Test image generation: `python example-book/test_image_generation.py`
- Test metadata extraction: `python example-book/test_metadata.py`
- Render specific format: `quarto render example-book --to <format>` (formats: pdf, epub, html)

## Code Style Guidelines
- **Imports**: Group standard library, then third-party, then local imports with a blank line between groups
- **Formatting**: Use 4-space indentation; keep line length under 100 characters
- **Types**: Use docstrings; consider type hints for function parameters
- **Error Handling**: Use try/except blocks with specific exceptions and proper logging
- **Logging**: Use the built-in logging module with appropriate levels (INFO, ERROR, etc.)
- **File Structure**: Follow modular design with clear separation of concerns
- **Config**: Use YAML for configuration and load via ConfigManager
- **Environment Variables**: Use for sensitive data (e.g., API keys)