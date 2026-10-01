import os
import shutil

# 1. Move Piscinas to Fotos Proyectos
src_piscinas = r"C:\Dynastron_Code\VGI\FOTOS DE PROYECTOS 02\PROYECTO PISCINA CAMERUM BEACH"
dst_piscinas = r"C:\Dynastron_Code\VGI\Fotos Proyectos\PROYECTO PISCINA CAMERUM BEACH"
if not os.path.exists(dst_piscinas):
    shutil.copytree(src_piscinas, dst_piscinas)
    print(f"Copied Piscinas to {dst_piscinas}")

# 2. Move Charlas to 05-formacion
src_charlas = r"C:\Dynastron_Code\VGI\FOTOS DE PROYECTOS 02\CHARLAS DE SEGURIDAD Y SALUD EN EL TRABAJO"
dst_charlas = r"C:\Dynastron_Code\VGI\05-formacion\charlas"

if not os.path.exists(dst_charlas):
    os.makedirs(dst_charlas)
    
    # Copy all images from subfolders to dst_charlas with unique names
    img_count = 1
    for root, dirs, files in os.walk(src_charlas):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_charlas, f"charla_{img_count:02d}.png")
                shutil.copy2(src_file, dst_file)
                img_count += 1
    print(f"Copied {img_count-1} Charlas images to {dst_charlas}")

