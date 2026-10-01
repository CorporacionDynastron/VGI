import os

html_file = r"C:\Dynastron_Code\VGI\capacitaciones.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Add the muted attribute to all video tags in capacitaciones.html
html = html.replace('controls style="width:100%;', 'controls muted style="width:100%;')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Added muted attribute to videos.")
