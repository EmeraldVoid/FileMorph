import os
from PIL import Image
from tqdm import tqdm

def get_directory(prompt):
    while True:
        path = input(prompt).strip('"')
        if os.path.isdir(path):
            return path
        print("Invalid directory. Please try again.")

def convert_png_to_ico(src_dir, dest_dir):
    png_files = [f for f in os.listdir(src_dir) if f.lower().endswith('.png')]
    total = len(png_files)

    if total == 0:
        print("No .png files found in the selected directory.")
        return

    print(f"\n{total} file(s) are being converted...\n")

    for file in tqdm(png_files, desc="Converting", unit="file"):
        png_path = os.path.join(src_dir, file)
        ico_path = os.path.join(dest_dir, os.path.splitext(file)[0] + ".ico")

        try:
            with Image.open(png_path) as img:
                img.save(ico_path, format='ICO')
        except Exception as e:
            print(f"Failed to convert {file}: {e}")

    print(f"\n{total} file(s) have been converted and saved to: {dest_dir}\n")

def main():
    while True:
        print("\n--- PNG to ICO Converter ---\n")
        source_dir = get_directory("Enter the source directory containing .png files: ")
        output_dir = get_directory("Enter the destination directory to save .ico files: ")

        convert_png_to_ico(source_dir, output_dir)

        again = input("Would you like to convert more? (Yes/Y to continue): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
