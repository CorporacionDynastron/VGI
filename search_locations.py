import os
import re

html_files = [f for f in os.listdir("C:\\Dynastron_Code\\VGI") if f.endswith(".html")]
locations = ["pisco", "ica", "lima", "cañete", "canete", "chincha", "ayacucho", "arequipa", "huancayo"]

for html_file in html_files:
    filepath = os.path.join("C:\\Dynastron_Code\\VGI", html_file)
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        line_lower = line.lower()
        found = []
        for loc in locations:
            # We want to match whole words preferably, but simple 'in' is fine for a quick check
            if re.search(r'\b' + loc + r'\b', line_lower):
                found.append(loc)
        
        if found:
            print(f"{html_file}:{i+1} -> Found: {', '.join(found)}\n  Line: {line.strip()[:100]}...")
