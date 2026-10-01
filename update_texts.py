import os
import re

# 1. FIX OBRAS.HTML
obras_file = r"C:\Dynastron_Code\VGI\obras.html"
with open(obras_file, 'r', encoding='utf-8') as f:
    obras_html = f.read()

obras_html = obras_html.replace('Planta de Tratamientos', 'Planta de Tratamiento')
obras_html = obras_html.replace('PLANTA DE TRATAMIENTOS', 'PLANTA DE TRATAMIENTO')

with open(obras_file, 'w', encoding='utf-8') as f:
    f.write(obras_html)


# 2. FIX INDEX.HTML
index_file = r"C:\Dynastron_Code\VGI\index.html"
with open(index_file, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Make the Capacitaciones card point to capacitaciones.html
index_html = index_html.replace("onclick=\"openHojaModal('modal-cursos')\"", "onclick=\"window.location.href='capacitaciones.html'\" style=\"cursor:pointer;\"")

# Add "Ver más" button to OBRAS
obras_list = """<li>Mantenimiento de infraestructura</li>
            </ul>"""
obras_btn = """<li>Mantenimiento de infraestructura</li>
            </ul>
            <button style="margin-top:25px; width:100%; padding:12px; background:transparent; border:1px solid var(--navy); color:var(--navy); font-family:var(--mono); font-weight:bold; font-size:12px; letter-spacing:0.1em; text-transform:uppercase; border-radius:4px; cursor:pointer; transition:all 0.3s;" onmouseover="this.style.background='var(--navy)'; this.style.color='#fff';" onmouseout="this.style.background='transparent'; this.style.color='var(--navy)';">Ver Obras Completas</button>"""
index_html = index_html.replace(obras_list, obras_btn)

# Add "Ver más" button to CAPACITACIONES
cap_list = """<li>Gestión y costos de obra</li>
            </ul>"""
cap_btn = """<li>Gestión y costos de obra</li>
            </ul>
            <button style="margin-top:25px; width:100%; padding:12px; background:transparent; border:1px solid var(--navy); color:var(--navy); font-family:var(--mono); font-weight:bold; font-size:12px; letter-spacing:0.1em; text-transform:uppercase; border-radius:4px; cursor:pointer; transition:all 0.3s;" onmouseover="this.style.background='var(--navy)'; this.style.color='#fff';" onmouseout="this.style.background='transparent'; this.style.color='var(--navy)';">Ver Módulos</button>"""
index_html = index_html.replace(cap_list, cap_btn)

# Also update the footer link if it says modal-cursos (it probably says capacitaciones section, which is fine)
# But wait, there was a menu link. 

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Updates completed.")
