import os
import re

html_file = r"C:\Dynastron_Code\VGI\obras.html"
base_dir = r"C:\Dynastron_Code\VGI"

dirs = {
    "Infraestructura deportiva y recreativa": "01. RECREACION- NACIONES UNIDAS,  SAN ANDRES, PISCO",
    "Pistas y veredas": "02. PISTAS Y VEREDAS- CAÑETE. LIMA",
    "Mantenimiento de infraestructura": "03. MANTENIMIENTO- PISCO"
}

html_content = """<section class="galeria-section">
    <div class="wrap">
        <style>
            .category-section { margin-bottom: 80px; }
            .category-title { font-family: var(--display); font-size: 32px; color: var(--navy); margin-bottom: 40px; border-bottom: 2px solid var(--gold); padding-bottom: 15px; text-transform: uppercase; }
            .empty-msg { color: var(--steel); font-style: italic; font-size: 15px; }
        </style>
"""

for title, d in dirs.items():
    html_content += f'''
        <div class="category-section">
            <h3 class="category-title">{title}</h3>
            <div class="grid-container">
'''
    folder_path = os.path.join(base_dir, d.replace("Ñ", ""))
    # Handle encoding weirdness if necessary, let's just list dirs first to see exact names if python fails.
    # Actually, we can just use glob or os.listdir on exact matches if we can find them.
    
    # Try to find the folder that starts with the number
    num_prefix = d.split('.')[0]
    actual_folder = None
    for item in os.listdir(base_dir):
        if os.path.isdir(os.path.join(base_dir, item)) and item.startswith(num_prefix + "."):
            actual_folder = item
            break
            
    if actual_folder:
        folder_path = os.path.join(base_dir, actual_folder)
        images = [img for img in os.listdir(folder_path) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
        for img in images:
            # We want to display max 6 images per category to not overload, or all? Let's do max 8.
            img_path = f"./{actual_folder}/{img}"
            # URL encode the path for src
            import urllib.parse
            img_url = urllib.parse.quote(img_path)
            html_content += f'''
                <div class="gallery-item" onclick="openLightbox('{img_url}', '{title}')">
                    <img src="{img_url}" loading="lazy" alt="{title}">
                    <div class="item-overlay">
                        <span class="item-cat">Ejecución Civil</span>
                        <h4 class="item-title">{title}</h4>
                    </div>
                </div>
'''
    html_content += '''
            </div>
        </div>
'''

# Add Planta de tratamientos and Saneamiento (AI Placeholders)
html_content += '''
        <div class="category-section">
            <h3 class="category-title">Planta de Tratamientos</h3>
            <div class="grid-container">
                <div class="gallery-item" onclick="openLightbox('https://images.unsplash.com/photo-1505027492977-1037f14c46fa?q=80&w=800&auto=format&fit=crop', 'Planta de Tratamientos')">
                    <img src="https://images.unsplash.com/photo-1505027492977-1037f14c46fa?q=80&w=800&auto=format&fit=crop" loading="lazy" alt="Planta de Tratamientos">
                    <div class="item-overlay">
                        <span class="item-cat">Tratamiento de Aguas</span>
                        <h4 class="item-title">Planta de Tratamientos</h4>
                    </div>
                </div>
                <div class="gallery-item" onclick="openLightbox('https://images.unsplash.com/photo-1518623380242-d992d3c15b1d?q=80&w=800&auto=format&fit=crop', 'Planta de Tratamientos')">
                    <img src="https://images.unsplash.com/photo-1518623380242-d992d3c15b1d?q=80&w=800&auto=format&fit=crop" loading="lazy" alt="Planta de Tratamientos">
                    <div class="item-overlay">
                        <span class="item-cat">Tratamiento de Aguas</span>
                        <h4 class="item-title">Operaciones de Planta</h4>
                    </div>
                </div>
            </div>
        </div>

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
# Also remove the gallery-filter since we group by section now
html = re.sub(r'<div class="gallery-filter">.*?</div>', '', html, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated obras.html layout")
