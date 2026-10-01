import os
from PIL import Image

dirs_to_optimize = [
    '01-recreacion', '02-pistas', '03-mantenimiento', 
    '04-primera-piedra', '05-formacion', '06-planta', 
    'Fotos Proyectos', 'CERTIFICACIONES'
]

base_dir = r"C:\Dynastron_Code\VGI"

total_saved = 0
processed = 0

MAX_DIMENSION = 1200

for d in dirs_to_optimize:
    folder_path = os.path.join(base_dir, d)
    if not os.path.exists(folder_path):
        continue
        
    for file in os.listdir(folder_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            filepath = os.path.join(folder_path, file)
            original_size = os.path.getsize(filepath)
            
            # Skip files that are already very small (< 200KB)
            if original_size < 200 * 1024:
                continue
                
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
                        
                        # Save back in same format
                        if file.lower().endswith('.png'):
                            resized_img.save(filepath, optimize=True)
                        else:
                            # For JPEGs, we can also compress
                            if resized_img.mode in ("RGBA", "P"):
                                resized_img = resized_img.convert("RGB")
                            resized_img.save(filepath, optimize=True, quality=80)
                            
                        new_size = os.path.getsize(filepath)
                        total_saved += (original_size - new_size)
                        processed += 1
                        print(f"Optimized: {file} - Saved {(original_size - new_size) / 1024 / 1024:.2f} MB")
            except Exception as e:
                print(f"Failed to process {file}: {e}")

print(f"\nOptimization complete! Processed {processed} images.")
print(f"Total space saved: {total_saved / 1024 / 1024:.2f} MB")
