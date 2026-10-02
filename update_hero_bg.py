import os

filepath = r"C:\Dynastron_Code\VGI\planos.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

old_css = ".hero-planos { background: var(--navy-deep); color: white; padding: 180px 0 80px; text-align: center; }"
new_css = ".hero-planos { background: linear-gradient(to bottom, rgba(3,10,20,0.6), rgba(6,19,37,0.95)), url('./Fotos%20Proyectos/PROYECTO%20ALBORADA%20-%20CASA%20DE%20CAMPO.png') center/cover no-repeat; color: white; padding: 180px 0 80px; text-align: center; position: relative; }"

if old_css in html:
    html = html.replace(old_css, new_css)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully updated hero-planos background.")
else:
    print("Could not find the exact old_css string.")
