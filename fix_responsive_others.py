import os
import re

target_vgi = r"C:\Dynastron_Code\VGI"
html_files = ["nosotros.html", "obras.html", "planos.html"]

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

for filename in html_files:
    filepath = os.path.join(target_vgi, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace(old_mobile_css, new_mobile_css)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {filename}")
