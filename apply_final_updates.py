import os
import re
from PIL import Image

# --- 1. OPTIMIZE NEW IMAGES ---
def optimize_folder(folder_path):
    MAX_DIMENSION = 1200
    if not os.path.exists(folder_path): return
    for file in os.listdir(folder_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(folder_path, file)
            original_size = os.path.getsize(filepath)
            if original_size < 200 * 1024: continue
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

print("Optimizing Piscinas...")
optimize_folder(r"C:\Dynastron_Code\VGI\Fotos Proyectos\PROYECTO PISCINA CAMERUM BEACH")
print("Optimizing Charlas...")
optimize_folder(r"C:\Dynastron_Code\VGI\05-formacion\charlas")

# --- 2. UPDATE PLANOS.HTML ---
planos_file = r"C:\Dynastron_Code\VGI\planos.html"
with open(planos_file, 'r', encoding='utf-8') as f:
    planos_html = f.read()

piscinas_html = """
<div class="project-card">
    <div class="project-header" onclick="this.parentElement.classList.toggle('active')">
        <h4 class="project-title">Proyecto Piscina Camerum Beach</h4>
        <span class="project-icon">▼</span>
    </div>
    <div class="project-content">
        <div class="grid-container">
            <div class="gallery-item" onclick="openLightbox('./Fotos Proyectos/PROYECTO PISCINA CAMERUM BEACH/IMAGEN 01.png', 'Piscina Camerum Beach - 1')">
                <img src="./Fotos Proyectos/PROYECTO PISCINA CAMERUM BEACH/IMAGEN 01.png" loading="lazy" alt="Piscina 1">
            </div>
            <div class="gallery-item" onclick="openLightbox('./Fotos Proyectos/PROYECTO PISCINA CAMERUM BEACH/IMAGEN 02.png', 'Piscina Camerum Beach - 2')">
                <img src="./Fotos Proyectos/PROYECTO PISCINA CAMERUM BEACH/IMAGEN 02.png" loading="lazy" alt="Piscina 2">
            </div>
            <div class="gallery-item" onclick="openLightbox('./Fotos Proyectos/PROYECTO PISCINA CAMERUM BEACH/IMAGEN 03.png', 'Piscina Camerum Beach - 3')">
                <img src="./Fotos Proyectos/PROYECTO PISCINA CAMERUM BEACH/IMAGEN 03.png" loading="lazy" alt="Piscina 3">
            </div>
        </div>
    </div>
</div>
"""
planos_html = re.sub(r'<p class="empty-msg">.*?</p>', piscinas_html, planos_html)
with open(planos_file, 'w', encoding='utf-8') as f:
    f.write(planos_html)


# --- 3. UPDATE CAPACITACIONES.HTML ---
cap_file = r"C:\Dynastron_Code\VGI\capacitaciones.html"
with open(cap_file, 'r', encoding='utf-8') as f:
    cap_html = f.read()

# Add charla 1-13 to the grid
charlas_imgs = ""
for i in range(1, 14):
    charlas_imgs += f'<div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05);"><img src="./05-formacion/charlas/charla_{i:02d}.png" style="width:100%; height:100%; object-fit:cover;"></div>\n'

cap_html = cap_html.replace('<!-- MORE_IMAGES_PLACEHOLDER -->', '') # Just in case
cap_html = cap_html.replace('</div>\n        </div>\n    </div>\n</section>', f'{charlas_imgs}            </div>\n        </div>\n    </div>\n</section>')

with open(cap_file, 'w', encoding='utf-8') as f:
    f.write(cap_html)


# --- 4. UPDATE OBRAS.HTML (Saneamiento) ---
obras_file = r"C:\Dynastron_Code\VGI\obras.html"
with open(obras_file, 'r', encoding='utf-8') as f:
    obras_html = f.read()

saneamiento_old = r"""<div class="grid-container">\s*<div class="gallery-item".*?</div>\s*</div>"""
saneamiento_new = """<div class="grid-container">
    <div class="gallery-item" onclick="openLightbox('https://images.unsplash.com/photo-1541888062837-1422ab72a9e2?auto=format&fit=crop&q=80&w=800', 'Saneamiento 1')">
        <img src="https://images.unsplash.com/photo-1541888062837-1422ab72a9e2?auto=format&fit=crop&q=80&w=800" loading="lazy" alt="Saneamiento 1">
        <div class="item-overlay"><span class="item-cat">Redes y Tuberías</span><h4 class="item-title">Instalación</h4></div>
    </div>
    <div class="gallery-item" onclick="openLightbox('https://images.unsplash.com/photo-1504307651254-35680f356fce?auto=format&fit=crop&q=80&w=800', 'Saneamiento 2')">
        <img src="https://images.unsplash.com/photo-1504307651254-35680f356fce?auto=format&fit=crop&q=80&w=800" loading="lazy" alt="Saneamiento 2">
        <div class="item-overlay"><span class="item-cat">Redes y Tuberías</span><h4 class="item-title">Mantenimiento</h4></div>
    </div>
    <div class="gallery-item" onclick="openLightbox('https://images.unsplash.com/photo-1621905252507-b35492cc74b4?auto=format&fit=crop&q=80&w=800', 'Saneamiento 3')">
        <img src="https://images.unsplash.com/photo-1621905252507-b35492cc74b4?auto=format&fit=crop&q=80&w=800" loading="lazy" alt="Saneamiento 3">
        <div class="item-overlay"><span class="item-cat">Redes y Tuberías</span><h4 class="item-title">Infraestructura</h4></div>
    </div>
</div>"""

obras_html = re.sub(saneamiento_old, saneamiento_new, obras_html, flags=re.DOTALL)

with open(obras_file, 'w', encoding='utf-8') as f:
    f.write(obras_html)

print("All HTML files updated successfully.")
