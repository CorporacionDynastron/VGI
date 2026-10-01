import os
import re

target_vgi = r"C:\Dynastron_Code\VGI"
html_files = ["index.html", "nosotros.html", "obras.html", "planos.html"]

old_font = r'--mono:\s*"JetBrains Mono", monospace;'
new_font = r"--mono: 'Inter', 'Roboto', sans-serif;"

for filename in html_files:
    filepath = os.path.join(target_vgi, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = re.sub(old_font, new_font, html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated font in {filename}")
