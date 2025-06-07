# Write a program to clear the clutter inside a folder on your computer. 
# You should use os module to rename all the png images from 1.png all the
# way till n.png where n is the number of png files in that folder.
# Do the same for other file formats.
# For example:
# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png

import os

def clear_clutter_and_rename(folder_path):
    # Get all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    

    # Dictionary to hold files by extension
    files_by_ext = {}

    # Group files by their extension
    for file in files:
        _, ext = os.path.splitext(file)
        ext = ext.lower()
        if ext:
            files_by_ext.setdefault(ext, []).append(file)

    # Now rename files in each extension group
    for ext, files in files_by_ext.items():
        files.sort()  # sort files alphabetically for consistent renaming
        for i, file in enumerate(files, start=1):
            new_name = f"{i}{ext}"
            src = os.path.join(folder_path, file)
            dst = os.path.join(folder_path, new_name)
            os.rename(src, dst)
            print(f"Renamed: {file} --> {new_name}")

# Replace this path with the folder you want to clean
folder_path = r"C:\Documents\codes\.vscode\example_clear_clutter"  # <-- Change this to your actual folder
clear_clutter_and_rename(folder_path)

