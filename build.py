import os
import sys
from subprocess import run, CalledProcessError

def convert_to_html(markdown_file, css_file, output_file):
    """
    Converts a Markdown file to HTML using Marp with the specified CSS theme.

    Args:
        markdown_file (str): Path to the Markdown file.
        css_file (str): Path to the CSS file.
        output_file (str): Path to the output HTML file.
    """
    command = ["marp", "--html", "--allow-local-files", "--theme", css_file, markdown_file, "-o", output_file]
    print(f"Running command: {' '.join(command)}")
    try:
        result = run(command, capture_output=True, text=True, check=True)
        print(f"Successfully created {output_file}")
    except CalledProcessError as e:
        print(f"Error creating {output_file}: {e.stderr}")

def convert_to_pdf(markdown_file, theme_file, output_file):
    """
    Converts a Markdown file to PDF using Marp with the specified theme.

    Args:
        markdown_file (str): Path to the Markdown file.
        theme_file (str): Path to the theme file (CSS or SCSS).
        output_file (str): Path to the output PDF file.
    """
    command = ["marp", "--pdf", "--theme", theme_file, markdown_file, "-o", output_file]
    print(f"Running command: {' '.join(command)}")
    try:
        result = run(command, capture_output=True, text=True, check=True)
        print(f"Successfully created {output_file}")
    except CalledProcessError as e:
        print(f"Error creating {output_file}: {e.stderr}")

def convert_to_image(markdown_file, css_file, output_file, image_format):
    """
    Converts the first slide of a Markdown file to an image using Marp with the specified CSS theme.

    Args:
        markdown_file (str): Path to the Markdown file.
        css_file (str): Path to the CSS file.
        output_file (str): Path to the output image file.
        image_format (str): The format of the output image (png or jpg).
    """
    command = ["marp", f"--{image_format}", "--allow-local-files", "--theme", css_file, markdown_file, "-o", output_file]
    print(f"Running command: {' '.join(command)}")
    try:
        result = run(command, capture_output=True, text=True, check=True)
        print(f"Successfully created {output_file}")
    except CalledProcessError as e:
        print(f"Error creating {output_file}: {e.stderr}")

def open_folder(folder_path):
    """
    Opens the specified folder using the default file manager on macOS.

    Args:
        folder_path (str): Path to the folder to open.
    """
    command = ["open", folder_path]
    print(f"Opening folder: {folder_path}")
    try:
        result = run(command, capture_output=True, text=True, check=True)
        print(f"Successfully opened {folder_path}")
    except CalledProcessError as e:
        print(f"Error opening {folder_path}: {e.stderr}")

def main():
    """
    Main function to handle input arguments and initiate the conversion process.
    """
    if len(sys.argv) < 2:
        print("Usage: python build.py <markdown-file> [--html|--pdf|--all|--open|--png|--jpg]")
        sys.exit(1)

    markdown_file = sys.argv[1]
    if not markdown_file.endswith(".md"):
        markdown_file += ".md"

    if len(sys.argv) > 2 and sys.argv[2] == "--open":
        folder_path = os.path.dirname(markdown_file)
        open_folder(folder_path)
        sys.exit(0)

    if not os.path.exists(markdown_file):
        print(f"Error: Markdown file '{markdown_file}' does not exist.")
        sys.exit(1)

    base_name = os.path.splitext(os.path.basename(markdown_file))[0]
    light_theme = "rose-pine-dawn"
    dark_theme = "rose-pine-moon"
    gaia_theme = "gaia.scss"
    css_light = os.path.abspath(f"./assets/css/{light_theme}.css")
    css_dark = os.path.abspath(f"./assets/css/{dark_theme}.css")
    css_gaia = os.path.abspath(f"./assets/css/{gaia_theme}")

    if not os.path.exists(css_light):
        print(f"Error: CSS file '{css_light}' does not exist.")
        sys.exit(1)

    if not os.path.exists(css_dark):
        print(f"Error: CSS file '{css_dark}' does not exist.")
        sys.exit(1)

    if not os.path.exists(css_gaia):
        print(f"Error: Theme file '{css_gaia}' does not exist.")
        sys.exit(1)

    # Create directories for HTML, PDF, and image outputs
    output_dir = os.path.dirname(markdown_file)
    os.makedirs(output_dir, exist_ok=True)

    output_light_pdf = os.path.join(output_dir, f"{base_name}-light.pdf")
    output_dark_pdf = os.path.join(output_dir, f"{base_name}-dark.pdf")
    output_gaia_pdf = os.path.join(output_dir, f"{base_name}-gaia.pdf")

    # Determine the conversion mode
    mode = "--pdf"
    if len(sys.argv) > 2:
        mode = sys.argv[2]

    output_light_html = os.path.join(output_dir, f"{base_name}-light.html")
    output_dark_html = os.path.join(output_dir, f"{base_name}-dark.html")
    output_light_png = os.path.join(output_dir, f"{base_name}-light.png")
    output_dark_png = os.path.join(output_dir, f"{base_name}-dark.png")
    output_light_jpg = os.path.join(output_dir, f"{base_name}-light.jpg")
    output_dark_jpg = os.path.join(output_dir, f"{base_name}-dark.jpg")
    output_png = os.path.join(output_dir, f"{base_name}.png")
    output_jpg = os.path.join(output_dir, f"{base_name}.jpg")

    if mode == "--html" or mode == "--all":
        print(f"Converting '{markdown_file}' to HTML with light theme...")
        convert_to_html(markdown_file, css_light, output_light_html)

        print(f"Converting '{markdown_file}' to HTML with dark theme...")
        convert_to_html(markdown_file, css_dark, output_dark_html)

    if mode == "--pdf" or mode == "--all":
        print(f"Converting '{markdown_file}' to PDF with light theme...")
        convert_to_pdf(markdown_file, css_light, output_light_pdf)

        print(f"Converting '{markdown_file}' to PDF with dark theme...")
        convert_to_pdf(markdown_file, css_dark, output_dark_pdf)

        print(f"Converting '{markdown_file}' to PDF with Gaia theme...")
        convert_to_pdf(markdown_file, css_gaia, output_gaia_pdf)

    if mode == "--png" or mode == "--all":
        print(f"Converting '{markdown_file}' to PNG with light theme...")
        convert_to_image(markdown_file, css_light, output_png, "png")

    if mode == "--jpg" or mode == "--all":
        print(f"Converting '{markdown_file}' to JPG with light theme...")
        convert_to_image(markdown_file, css_light, output_jpg, "jpg")

if __name__ == "__main__":
    main()