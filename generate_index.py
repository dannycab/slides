import os
import glob
import yaml
from jinja2 import Template

def load_info_files(directory):
    info_files = glob.glob(os.path.join(directory, "content/**/info.yml"), recursive=True)
    decks = []
    for info_file in info_files:
        with open(info_file, "r") as file:
            deck_info = yaml.safe_load(file)
            deck_dir = os.path.dirname(info_file)
            markdown_file = os.path.join(deck_dir, "slides.md")
            if os.path.exists(markdown_file):
                base_name = os.path.splitext(os.path.basename(markdown_file))[0]
                output_light_html = os.path.join(deck_dir, f"{base_name}-light.html")
                output_dark_html = os.path.join(deck_dir, f"{base_name}-dark.html")
                output_light_pdf = os.path.join(deck_dir, f"{base_name}-light.pdf")
                output_dark_pdf = os.path.join(deck_dir, f"{base_name}-dark.pdf")
                title_image = os.path.join(deck_dir, "slides.png")
                if os.path.exists(title_image):
                    deck_info["title_image"] = os.path.relpath(title_image, directory)
                deck_info.update({
                    "html_light": os.path.relpath(output_light_html, directory),
                    "html_dark": os.path.relpath(output_dark_html, directory),
                    "pdf_light": os.path.relpath(output_light_pdf, directory),
                    "pdf_dark": os.path.relpath(output_dark_pdf, directory)
                })
                decks.append(deck_info)
    # Sort decks by date
    decks.sort(key=lambda x: x.get('date', ''), reverse=True)
    return decks

def generate_html(decks, output_file):
    template_path = os.path.abspath("./assets/index.html")
    with open(template_path, "r") as file:
        template = Template(file.read())
    html_content = template.render(decks=decks)
    with open(output_file, "w") as file:
        file.write(html_content)

def main():
    slides_directory = "/Users/caballero/repos/slides"
    output_file = os.path.join(slides_directory, "index.html")
    print("Loading info files...")
    decks = load_info_files(slides_directory)
    print(f"Found {len(decks)} decks.")
    print("Generating HTML...")
    generate_html(decks, output_file)
    print(f"Table of contents generated at {output_file}")

if __name__ == "__main__":
    main()