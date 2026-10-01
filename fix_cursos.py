import os

html_file = r"C:\Dynastron_Code\VGI\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace unsplash in modal-cursos with local
html = html.replace('https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?q=80&w=800&auto=format&fit=crop', './03.%20MANTENIMIENTO-%20PISCO/IMAGEN%202.png')

# Wait, there's another image for Cursos on the card itself:
html = html.replace('https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?q=80&w=600&auto=format&fit=crop', './03.%20MANTENIMIENTO-%20PISCO/IMAGEN%202.png')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated capacitaciones images to local placeholders")
