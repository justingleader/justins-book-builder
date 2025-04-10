import re
import os

def slugify(text):
    """Convert header text to a safe filename."""
    text = text.lower()
    text = re.sub(r'\s+', '-', text)  # Replace spaces with hyphens
    text = re.sub(r'[^a-z0-9\-]', '', text)  # Remove non-alphanumeric characters except hyphens
    text = re.sub(r'^-+|-+$', '', text)  # Remove leading/trailing hyphens
    return text if text else "untitled"

def split_markdown_by_h2(input_file, output_dir):
    """Splits a markdown file into multiple files based on H2 headers."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    current_file = None
    current_content = []
    file_counter = 0

    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                if line.startswith('## '):
                    # Close the previous file if open
                    if current_file:
                        current_file.writelines(current_content)
                        current_file.close()
                        print(f"Finished writing: {current_filename}")

                    # Start a new file
                    header_text = line[3:].strip()
                    slug = slugify(header_text)
                    # Handle potential duplicate filenames
                    potential_filename = os.path.join(output_dir, f"{slug}.md")
                    count = 1
                    current_filename = potential_filename
                    while os.path.exists(current_filename):
                        current_filename = os.path.join(output_dir, f"{slug}-{count}.md")
                        count += 1

                    print(f"Starting new file for header '{header_text}': {current_filename}")
                    current_file = open(current_filename, 'w', encoding='utf-8')
                    current_content = [line] # Start with the header line
                    file_counter += 1
                elif current_file:
                    # Append line to the current file's content
                    current_content.append(line)
                else:
                    # Content before the first H2 header (optional: could save to an intro file)
                    # For now, we'll ignore content before the first H2 unless needed
                    pass

            # Write the last file
            if current_file:
                current_file.writelines(current_content)
                current_file.close()
                print(f"Finished writing: {current_filename}")

        if file_counter == 0:
             print(f"Warning: No H2 headers found in {input_file}. No files were created.")
        else:
             print(f"Successfully split into {file_counter} files.")

    except FileNotFoundError:
        print(f"Error: Input file not found at {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
        if current_file and not current_file.closed:
            current_file.close() # Ensure file is closed on error

if __name__ == "__main__":
    input_markdown = "docs/draft/quarto-docs-full.md"
    output_directory = "docs"
    print(f"Splitting {input_markdown} into files in {output_directory} based on H2 headers...")
    split_markdown_by_h2(input_markdown, output_directory)
    print("Splitting process completed.") 