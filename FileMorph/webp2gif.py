import os
import glob
import sys
from PIL import Image
import time

def main():
    print("=== WEBP to GIF Converter ===")

    # Ask for input directory
    input_dir = input("Enter the full path of the directory to scan for .webp files: ").strip()
    if not os.path.isdir(input_dir):
        print("Error: Input directory does not exist.")
        return

    # Ask for output directory
    output_dir = input("Enter the full path of the directory to save the .gif files: ").strip()
    if not os.path.isdir(output_dir):
        print("Error: Output directory does not exist.")
        return

    # Find all .webp files
    webp_files = glob.glob(os.path.join(input_dir, "*.webp"))
    file_count = len(webp_files)

    if file_count == 0:
        print("No .webp files found in the specified directory.")
        return

    print(f"\n{file_count} files are being converted...")

    # Simple loading animation
    for i in range(3):
        print("Converting" + "." * (i + 1))
        time.sleep(0.5)

    converted_count = 0
    for file in webp_files:
        try:
            img = Image.open(file).convert("RGBA")
            base_name = os.path.splitext(os.path.basename(file))[0]
            output_path = os.path.join(output_dir, base_name + ".gif")
            img.save(output_path, "GIF")
            converted_count += 1
        except Exception as e:
            print(f"Failed to convert {file}: {e}")

    print(f"\n{converted_count} files have been converted.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
