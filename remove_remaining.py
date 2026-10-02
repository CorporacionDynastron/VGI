import os

html_file = r"C:\Dynastron_Code\VGI\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    "en San Andrés, Pisco. Ejecución": ". Ejecución",
    "público en Cañete. Trabajos": "público. Trabajos"
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Replaced remaining locations")
