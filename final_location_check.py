import os
import re

html_files = [f for f in os.listdir("C:\\Dynastron_Code\\VGI") if f.endswith(".html")]

for html_file in html_files:
    filepath = os.path.join("C:\\Dynastron_Code\\VGI", html_file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check for specific words, excluding Aceros Arequipa
    matches = re.finditer(r'\b(pisco|ica|cañete|lima)\b', html, re.IGNORECASE)
    for m in matches:
        start = max(0, m.start() - 30)
        end = min(len(html), m.end() + 30)
        print(f"Found in {html_file}: {html[start:end]}")
