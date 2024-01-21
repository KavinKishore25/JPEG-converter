import sys
import os
from PIL import Image

image_folder = sys.argv[1]
save_folder = sys.argv[2]

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{save_folder}{clean_name}.png", "png")
