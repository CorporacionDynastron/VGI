import os
from PIL import Image

def optimize_folder(folder_path):
    MAX_DIMENSION = 1200
    if not os.path.exists(folder_path): return
    for file in os.listdir(folder_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(folder_path, file)
            original_size = os.path.getsize(filepath)
            if original_size < 100 * 1024: continue
            try:
                with Image.open(filepath) as img:
                    width, height = img.size
                    if width > MAX_DIMENSION or height > MAX_DIMENSION:
                        if width > height:
                            new_width = MAX_DIMENSION
                            new_height = int((MAX_DIMENSION / width) * height)
                        else:
                            new_height = MAX_DIMENSION
                            new_width = int((MAX_DIMENSION / height) * width)
                        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                        if file.lower().endswith('.png'):
                            resized_img.save(filepath, optimize=True)
                        else:
                            if resized_img.mode in ("RGBA", "P"):
                                resized_img = resized_img.convert("RGB")
                            resized_img.save(filepath, optimize=True, quality=80)
                        print(f"Optimized {file}")
            except Exception as e:
                print(f"Error optimizing {file}: {e}")

optimize_folder(r"C:\Dynastron_Code\VGI\07-saneamiento")
