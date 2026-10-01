import os
import re

html_file = r"C:\Dynastron_Code\VGI\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any modal broken images with working AI/Unsplash or local placeholders just in case
# Let's search for "modal-capacitacion" in index.html to see its img
match = re.search(r'id="modal-capacitacion".*?<img src="([^"]+)"', html, flags=re.DOTALL)
if match:
    print("Found modal-capacitacion img:", match.group(1))
else:
    print("No img found in modal-capacitacion")
