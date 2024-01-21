# JPEG-converter
Description:

This Python script utilizes the PIL (Python Imaging Library) module to convert a batch of images from one format to another. The script takes two command-line arguments: the path to the folder containing the original images (image_folder) and the path to the folder where the converted images will be saved (save_folder).

The script checks if the specified save folder exists and creates it if not. It then iterates through the files in the image folder, opens each image using PIL, extracts the filename without its extension, and saves the image in PNG format with the same base name to the specified save folder.

**Usage:
python script.py <image_folder_path> <save_folder_path>**

Dependencies:

* Python 3
* PIL (Python Imaging Library)


**Example:**
**python script.py input_images/ output_images/**

This script is useful for bulk image format conversion and ensures that the output images are saved in PNG format while preserving their original filenames.
