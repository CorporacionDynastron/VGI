import os
import re
import urllib.parse

html_file = r"C:\Dynastron_Code\VGI\obras.html"
base_dir = r"C:\Dynastron_Code\VGI"

dirs = {
    "Infraestructura deportiva y recreativa": "01-recreacion",
    "Pistas y veredas": "02-pistas",
    "Mantenimiento de infraestructura": "03-mantenimiento",
    "Planta de Tratamientos": "06-planta-tratamiento"
}

html_content = """<section class="galeria-section">
    <div class="wrap">
        <style>
            .category-section { margin-bottom: 80px; }
            .category-title { font-family: var(--display); font-size: 32px; color: var(--navy); margin-bottom: 40px; border-bottom: 2px solid var(--gold); padding-bottom: 15px; text-transform: uppercase; }
            .empty-msg { color: var(--steel); font-style: italic; font-size: 15px; }
        </style>
"""

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
            # properly URL encode just the filename, not the path separators
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

# Add Saneamiento (AI Placeholders)
html_content += '''
        <div class="category-section">
            <h3 class="category-title">Saneamiento</h3>
            <div class="grid-container">
                <div class="gallery-item" onclick="openLightbox('https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=800&auto=format&fit=crop', 'Saneamiento')">
                    <img src="https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=800&auto=format&fit=crop" loading="lazy" alt="Saneamiento">
                    <div class="item-overlay">
                        <span class="item-cat">Redes y Tuberías</span>
                        <h4 class="item-title">Saneamiento</h4>
                    </div>
                </div>
            </div>
        </div>
'''

html_content += """
    </div>
</section>"""

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<section class="galeria-section">.*?</section>', html_content, html, flags=re.DOTALL)
html = re.sub(r'<div class="gallery-filter">.*?</div>', '', html, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated obras.html layout with clean paths")
