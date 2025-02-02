import os
import sys

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.startswith("slides"):
            new_filename = "slide" + filename[len("slides"):]
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} to {new_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python rename_files.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    rename_files_in_directory(directory)

if __name__ == "__main__":
    main()