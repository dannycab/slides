#!/bin/bash
# Change working directory path by replacing the % s placeholder
# $1 is the path to the folder containing old files
# $2 is the prefix of the old files (e.g., 'old')
# $3 is the new prefix for the files

folder_path="$1"
old_prefix="$2"
new_prefix="$3"

echo "Starting file renaming process..."
echo "Looking in: $folder_path"

for file in "${folder_path}/${old_prefix}"* ; do
    # Check if the file starts with old prefix and is a regular file
    if [ -f "${file}" ]; then
        base_name=$(basename "${file}")
        new_file="${folder_path}/${new_prefix}${base_name#${old_prefix}}"
        echo "Renaming: ${file} to ${new_file}"
        mv "${file}" "${new_file}"
    fi
done

echo "File renaming completed successfully!"