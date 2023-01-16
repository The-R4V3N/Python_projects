"""
*
 * @file classify-files.py
 * @author Oliver Joisten (https://oliver-joisten.se/)
 * @brief 
 * @version 0.1
 * @date 2023-01-07
 * 
 * @copyright Copyright (c) 2023
 * 
"""

import os
import time

# Directory to be monitored
directory = r"C:\Users\username\Downloads"

# Dictionary of file categories and their extensions
categories = {
    "Images": ["jpeg", "jpg", "png", "svg", "gif", "psd", "bmp", "tif", "tiff"],
    "Documents": ["txt", "doc", "docx", "ppt", "pptx"],
    "PDFs": ["pdf"],
    "Datasets": ["csv", "xlsx", "json"],
    "Videos": ["mp4"],
    "Installation": ["exe"],
    "Zip": ["zip"],
}

for category in [
    "Images",
    "Documents",
    "PDFs",
    "Datasets",
    "Videos",
    "Installation",
    "Zip",
]:
    os.makedirs(os.path.join(directory, category), exist_ok=True)

# Function to classify a file


def classify_file(filename):
    # Find the file extension
    extension = filename.split(".")[-1]

    # Iterate over the categories
    for category, extensions in categories.items():
        # If the extension matches one of the extensions in the category, move the file
        if extension in extensions:
            # Construct the file paths
            source_path = os.path.join(directory, filename)
            dest_path = os.path.join(directory, category, filename)

            # Move the file
            os.rename(source_path, dest_path)
            print(f"Moved {filename} to {category}")
            break


# Classify all existing files in the directory
for filename in os.listdir(directory):
    classify_file(filename)

# Initial list of files in the directory
initial_files = os.listdir(directory)

while True:
    # List of files in the directory after a short sleep
    # runs every hour, time is in seconds. 60 minutes * 60 seconds = 3600 seconds
    time.sleep(3600)

    current_files = os.listdir(directory)

    # Find the new files
    new_files = list(set(current_files) - set(initial_files))

    # Classify the new files
    for filename in new_files:
        classify_file(filename)

    # Update the initial list of files
    initial_files = current_files
