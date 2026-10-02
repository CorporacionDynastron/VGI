import os
import re

html_files = [f for f in os.listdir("C:\\Dynastron_Code\\VGI") if f.endswith(".html")]

for html_file in html_files:
    filepath = os.path.join("C:\\Dynastron_Code\\VGI", html_file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if "Parque Naciones Unidas" in html or "Naciones Unidas" in html:
        print(f"Found 'Parque Naciones Unidas' in {html_file}")
    
    # Also search case-insensitive for Pisco, Ica just in case
    if re.search(r'pisco,\s*ica', html, re.IGNORECASE):
        print(f"Found 'pisco, ica' in {html_file}")
