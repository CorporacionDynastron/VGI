import os
import re
import urllib.parse
import shutil

base_dir = r"C:\Dynastron_Code\VGI"
html_file = os.path.join(base_dir, "obras.html")

# 1. Setup the saneamiento folder and copy generated images
saneamiento_dir = os.path.join(base_dir, "07-saneamiento")
if not os.path.exists(saneamiento_dir):
    os.makedirs(saneamiento_dir)

# Define paths to artifacts
art_dir = r"C:\Users\Lando\.gemini\antigravity\brain\9a29f7e9-350b-489c-ac3b-6acb708754b4"
img1 = os.path.join(art_dir, "saneamiento_1_1790887781030.jpg")
img2 = os.path.join(art_dir, "saneamiento_2_1790887807761.jpg")
img3 = os.path.join(art_dir, "saneamiento_3_1790887863496.jpg")

# Copy if they exist (they should)
if os.path.exists(img1): shutil.copy2(img1, os.path.join(saneamiento_dir, "saneamiento_1.jpg"))
if os.path.exists(img2): shutil.copy2(img2, os.path.join(saneamiento_dir, "saneamiento_2.jpg"))
if os.path.exists(img3): shutil.copy2(img3, os.path.join(saneamiento_dir, "saneamiento_3.jpg"))


# 2. Rewrite the HTML
dirs = {
    "Infraestructura deportiva y recreativa": "01-recreacion",
    "Pistas y veredas": "02-pistas",
    "Mantenimiento de infraestructura": "03-mantenimiento",
    "Planta de Tratamiento": "06-planta",
    "Saneamiento": "07-saneamiento"
}

html_content = '''<section class="galeria-section">
    <div class="wrap">
        <style>
            .category-section { margin-bottom: 80px; }
            .category-title { font-family: var(--display); font-size: 32px; color: var(--navy); margin-bottom: 40px; border-bottom: 2px solid var(--gold); padding-bottom: 15px; text-transform: uppercase; }
            .empty-msg { color: var(--steel); font-style: italic; font-size: 15px; }
        </style>
'''

for title, folder_name in dirs.items():
    html_content += f'''
        <div class="category-section">
            <h3 class="category-title">{title}</h3>
            <div class="grid-container">
'''
    folder_path = os.path.join(base_dir, folder_name)
    if os.path.exists(folder_path):
        images = [img for img in os.listdir(folder_path) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        for img in images:
            safe_img = urllib.parse.quote(img)
            img_url = f"./{folder_name}/{safe_img}"
            html_content += f'''
                <div class="gallery-item" onclick="openLightbox('{img_url}', '{title}')">
                    <img src="{img_url}" loading="lazy" alt="{title}">
                    <div class="item-overlay">
                        <span class="item-cat">Ejecución Civil</span>
                        <h4 class="item-title">{title}</h4>
                    </div>
                </div>
'''
    else:
        html_content += f'<p class="empty-msg">No hay imágenes disponibles para {title}</p>'

    html_content += '''
            </div>
        </div>
'''

html_content += '''
    </div>
</section>'''

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the entire gallery section
html = re.sub(r'<section class="galeria-section">.*?</section>', html_content, html, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated obras.html and fully fixed the structure with Saneamiento.")
