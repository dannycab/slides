# Project Documentation

## Overview
This repository contains tools for managing and generating slide decks for presentations. The two main scripts, `build.py` and `generate_index.py`, automate the process of converting Markdown files into various formats and creating an index for easy navigation.

---

## `build.py`

### Purpose
The `build.py` script is used to convert Markdown files into HTML, PDF, and image formats using Marp. It supports light and dark themes and can open the output folder for convenience.

### Usage
```bash
python build.py <markdown-file> [--html|--pdf|--all|--open|--png|--jpg]
```

### Arguments
- `<markdown-file>`: Path to the Markdown file to convert. If the file does not have a `.md` extension, it will be appended automatically.
- `--html`: Convert the Markdown file to HTML format.
- `--pdf`: Convert the Markdown file to PDF format.
- `--all`: Convert the Markdown file to all supported formats (HTML, PDF, and images).
- `--open`: Open the folder containing the Markdown file.
- `--png`: Convert the first slide of the Markdown file to a PNG image.
- `--jpg`: Convert the first slide of the Markdown file to a JPG image.

### Features
- Converts Markdown files to HTML, PDF, and image formats.
- Supports light and dark themes.
- Opens the output folder for quick access.

### Example
```bash
python build.py slides.md --all
```
This command converts `slides.md` to HTML, PDF, and image formats using both light and dark themes.

---

## `generate_index.py`

### Purpose
The `generate_index.py` script scans the `content/` directory for slide decks and generates an `index.html` file that serves as a table of contents for all available presentations.

### Usage
```bash
python generate_index.py
```

### Features
- Scans the `content/` directory for `info.yml` files.
- Extracts metadata about each slide deck, including:
  - Title
  - Date
  - Links to HTML and PDF versions (light and dark themes).
  - Thumbnail image (if available).
- Generates an `index.html` file using a Jinja2 template.

### Example
```bash
python generate_index.py
```
This command generates an `index.html` file in the root directory, listing all available slide decks.

---

## Dependencies

### Required Tools
- **Marp**: For converting Markdown files to HTML, PDF, and images.
- **Python Packages**:
  - `jinja2`: For rendering HTML templates.
  - `pyyaml`: For parsing YAML metadata.

### Installation
Install the required Python packages using pip:
```bash
pip install jinja2 pyyaml
```

Ensure Marp is installed and available in your system's PATH. Follow the [Marp installation guide](https://marp.app/) for setup instructions.

---

## Directory Structure
- `content/`: Contains slide decks and their metadata.
- `assets/`: Contains CSS files and templates for styling and layout.
- `index.html`: Generated table of contents for all slide decks.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.