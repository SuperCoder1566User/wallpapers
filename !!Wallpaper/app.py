import os
from PIL import Image

# Constants
TARGET_WIDTH = 1920
TARGET_HEIGHT = 1080
TARGET_SIZE = (TARGET_WIDTH, TARGET_HEIGHT)
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

def is_image_file(filename):
    return filename.lower().endswith(VALID_EXTENSIONS)

def crop_center_resize(image, size):
    img_ratio = image.width / image.height
    target_ratio = size[0] / size[1]

    if img_ratio > target_ratio:
        new_width = int(image.height * target_ratio)
        offset = (image.width - new_width) // 2
        cropped = image.crop((offset, 0, offset + new_width, image.height))
    else:
        new_height = int(image.width / target_ratio)
        offset = (image.height - new_height) // 2
        cropped = image.crop((0, offset, image.width, offset + new_height))

    return cropped.resize(size, Image.LANCZOS)

def main():
    # Get user input
    try:
        start_index = int(input("Start index (e.g. 6): "))
        end_index = int(input("End index (e.g. 15): "))
        image_limit = int(input("How many images should be processed?: "))
    except ValueError:
        print("❌ Please enter valid integer values.")
        return

    if end_index < start_index:
        print("❌ End index must be greater than or equal to start index.")
        return

    # Step 1: Find image files
    all_files = [f for f in os.listdir() if os.path.isfile(f) and is_image_file(f)]
    files = all_files[:image_limit]

    if len(files) < (end_index - start_index + 1):
        print("⚠️ Warning: You don't have enough images to fill the entire index range.")
        print(f"Will process {len(files)} images, and names will start from index {start_index}.")
    
    # Step 2: Crop and save
    for i, filename in enumerate(files, start=start_index):
        with Image.open(filename) as img:
            cropped = crop_center_resize(img, TARGET_SIZE)
            new_filename = f"{i}.png"
            cropped.save(new_filename, "PNG")
            print(f"✅ Saved: {new_filename}")

    # Step 3: Delete originals
    for f in files:
        os.remove(f)
        print(f"🗑️ Deleted original: {f}")

if __name__ == "__main__":
    main()
