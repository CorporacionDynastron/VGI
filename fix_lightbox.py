import os
import re

target_vgi = r"C:\Dynastron_Code\VGI"
html_files = ["obras.html", "planos.html"]

for filename in html_files:
    filepath = os.path.join(target_vgi, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix lightbox absolute paths: onclick="openLightbox('/...')" -> onclick="openLightbox('./...')"
    html = re.sub(r'openLightbox\(\'\/([^/][^\']*)\'', r"openLightbox('./\1'", html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Fixed lightbox paths in {filename}")

print("Lightbox paths converted to relative.")
