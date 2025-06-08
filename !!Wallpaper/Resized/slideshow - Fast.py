import os
import time
import ctypes
from pathlib import Path

# Path to your wallpaper folder
WALLPAPER_DIR = r"C:\Users\Kids\Downloads\!!Wallpaper\Resized"

# Time between wallpaper changes (in seconds)
SLIDE_INTERVAL = 1  # Change to 300 for 5 minutes, etc.

# Get list of .png files
wallpapers = [str(p) for p in Path(WALLPAPER_DIR).glob("*.png")]

# Sort wallpapers by numeric filename
def extract_number(file_path):
    try:
        return int(Path(file_path).stem)
    except ValueError:
        return float('inf')  # Send non-numeric names to the end

wallpapers.sort(key=extract_number)

def set_wallpaper(image_path):
    # Use Windows API to set wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

if not wallpapers:
    print("No PNG wallpapers found.")
else:
    print(f"Found {len(wallpapers)} wallpapers. Starting slideshow...")
    while True:
        for wallpaper in wallpapers:
            print(f"Setting wallpaper: {wallpaper}")
            set_wallpaper(wallpaper)
            time.sleep(SLIDE_INTERVAL)
