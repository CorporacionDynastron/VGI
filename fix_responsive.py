import os
import re

filepath = r"C:\Dynastron_Code\VGI\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace broken Unsplash images
html = html.replace('https://images.unsplash.com/photo-1503387762-592deb58ef4e?q=80&w=600&auto=format&fit=crop', './Fotos%20Proyectos/PROYECTO%20ALBORADA%20-%20CASA%20DE%20CAMPO.png')
html = html.replace('https://images.unsplash.com/photo-1541888081622-19e34e5db8d3?q=80&w=600&auto=format&fit=crop', './02.%20PISTAS%20Y%20VEREDAS-%20CA%C3%91ETE.%20LIMA/IMAGEN%201.png')
html = html.replace('https://images.unsplash.com/photo-1581092334651-ddf26d9a09d0?q=80&w=600&auto=format&fit=crop', './03.%20MANTENIMIENTO-%20PISCO/IMAGEN%202.png')

# 2. Fix Mobile Menu CSS
old_mobile_css = """@media (max-width:980px){
    nav.links,.nav-actions .nav-cta.ghost{ display:none; }
    nav.links.is-open{
      display:flex; flex-direction:column; position:fixed; top:0; right:0; bottom:0; width:76%;
      background:var(--navy-deep); padding:100px 34px; gap:26px; z-index:250; box-shadow:-10px 0 30px rgba(0,0,0,.5);
    }"""

new_mobile_css = """@media (max-width:980px){
    nav.links,.nav-actions .nav-cta.ghost{ display:none; }
    nav.links.is-open{
      display:flex; flex-direction:column; position:fixed; inset:0; width:100%; height:100vh;
      background:rgba(6,19,37,0.95); backdrop-filter:blur(8px); padding:120px 34px; gap:36px; z-index:250;
      align-items:center; text-align:center;
    }
    nav.links.is-open a {
      font-size: 22px;
      font-weight: 500;
      color: #fff;
      border: none;
    }
    nav.links.is-open a:hover {
      color: var(--gold);
    }"""

html = html.replace(old_mobile_css, new_mobile_css)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html")
