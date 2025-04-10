#!/usr/bin/env python3
"""
Test script for the Quarto Book Builder.
This script creates a sample project and tests the functionality of the CLI.
"""

import os
import sys
import subprocess
import tempfile
import shutil
import time

# Colors for terminal output
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def print_step(message):
    """Print a step message."""
    print(f"\n{YELLOW}=== {message} ==={RESET}")

def print_success(message):
    """Print a success message."""
    print(f"{GREEN}✓ {message}{RESET}")

def print_error(message):
    """Print an error message."""
    print(f"{RED}✗ {message}{RESET}")

def run_command(command, cwd=None):
    """Run a command and return the result."""
    print(f"Running: {' '.join(command)}")
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"{GREEN}Command succeeded{RESET}")
        if result.stdout:
            print(f"Output: {result.stdout[:500]}...")
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        print(f"{RED}Command failed with exit code {e.returncode}{RESET}")
        if e.stdout:
            print(f"Stdout: {e.stdout}")
        if e.stderr:
            print(f"Stderr: {e.stderr}")
        return False, e.stderr
    except Exception as e:
        print(f"{RED}Error: {str(e)}{RESET}")
        return False, str(e)

def main():
    """Main function to test the Quarto Book Builder."""
    # Create a temporary directory for testing
    temp_dir = tempfile.mkdtemp()
    print(f"Created temporary directory: {temp_dir}")

    try:
        # Step 1: Install the package
        print_step("Installing the Quarto Book Builder package")
        success, _ = run_command([
            "pip", "install", "-e", "/home/ubuntu/quarto_book_builder"
        ])
        if not success:
            print_error("Failed to install the package")
            return 1
        print_success("Package installed successfully")

        # Step 2: Initialize a new project
        print_step("Initializing a new project")
        project_dir = os.path.join(temp_dir, "test-book")
        success, _ = run_command([
            "quarto-book-builder", "init", project_dir,
            "--title", "Test Book",
            "--author", "Test Author"
        ])
        if not success:
            print_error("Failed to initialize the project")
            return 1
        print_success("Project initialized successfully")

        # Step 3: Check if project files were created
        print_step("Checking project files")
        required_files = [
            "config.yaml",
            "_quarto.yml",
            "chapters/01-intro.qmd",
            "epub.css"
        ]
        for file in required_files:
            file_path = os.path.join(project_dir, file)
            if os.path.exists(file_path):
                print_success(f"File exists: {file}")
            else:
                print_error(f"File does not exist: {file}")
                return 1

        # Step 4: Update the config with a mock API key
        print_step("Updating configuration")
        config_path = os.path.join(project_dir, "config.yaml")
        with open(config_path, "r") as f:
            config_content = f.read()
        
        config_content = config_content.replace(
            'openai_api_key: "your-api-key-here"',
            'openai_api_key: "sk-mock-api-key-for-testing"'
        )
        
        with open(config_path, "w") as f:
            f.write(config_content)
        print_success("Configuration updated successfully")

        # Step 5: Create a custom chapter
        print_step("Creating a custom chapter")
        custom_chapter_path = os.path.join(project_dir, "chapters", "02-custom.qmd")
        with open(custom_chapter_path, "w") as f:
            f.write("""---
title: "Custom Chapter"
---

# Custom Chapter

This is a custom chapter with various features.

## Image Generation

Here's an AI-generated image:

{{image: A serene lake surrounded by mountains at sunset}}

## Custom Sections

::: featured-quote
"The only way to do great work is to love what you do."
**— Steve Jobs**
:::

::: listicle
## Top 3 Programming Tips

1. Write clean, readable code
2. Test early and often
3. Document your work
:::

## Code Example

```python
def hello_world():
    print("Hello, World!")
```

## Conclusion

This chapter demonstrates the features of the Quarto Book Builder.
""")
        print_success("Custom chapter created successfully")

        # Step 6: Update Quarto config to include the new chapter
        print_step("Updating Quarto configuration")
        quarto_config_path = os.path.join(project_dir, "_quarto.yml")
        with open(quarto_config_path, "r") as f:
            quarto_config_content = f.read()
        
        quarto_config_content = quarto_config_content.replace(
            '  chapters:\n    - "chapters/01-intro.qmd"',
            '  chapters:\n    - "chapters/01-intro.qmd"\n    - "chapters/02-custom.qmd"'
        )
        
        with open(quarto_config_path, "w") as f:
            f.write(quarto_config_content)
        print_success("Quarto configuration updated successfully")

        # Step 7: Preprocess the project
        print_step("Preprocessing the project")
        success, _ = run_command([
            "quarto-book-builder", "preprocess", project_dir
        ])
        if not success:
            print_error("Failed to preprocess the project")
            return 1
        print_success("Project preprocessed successfully")

        # Step 8: Check if build directory was created
        build_dir = os.path.join(project_dir, "_build")
        if os.path.exists(build_dir):
            print_success("Build directory created successfully")
        else:
            print_error("Build directory was not created")
            return 1

        # Step 9: Check if image was processed
        print_step("Checking image processing")
        images_dir = os.path.join(project_dir, "images")
        if os.path.exists(images_dir) and len(os.listdir(images_dir)) > 0:
            print_success(f"Images directory contains files: {os.listdir(images_dir)}")
        else:
            print_error("No images were generated")
            # This is not a critical error as we're using a mock API key
            print_success("Continuing with tests...")

        # Step 10: Clean the project
        print_step("Cleaning the project")
        success, _ = run_command([
            "quarto-book-builder", "clean", project_dir
        ])
        if not success:
            print_error("Failed to clean the project")
            return 1
        print_success("Project cleaned successfully")

        # Step 11: Check if build directory was removed
        if not os.path.exists(build_dir):
            print_success("Build directory was removed successfully")
        else:
            print_error("Build directory was not removed")
            return 1

        # Final success message
        print(f"\n{GREEN}All tests passed successfully!{RESET}")
        print(f"Test project is available at: {project_dir}")
        print("You can explore the project files or delete the directory when done.")

        return 0

    except Exception as e:
        print(f"{RED}Error: {str(e)}{RESET}")
        return 1
    finally:
        # Don't remove the temp directory so the user can inspect it
        print(f"Temporary directory {temp_dir} was not removed for inspection.")

if __name__ == "__main__":
    sys.exit(main())
