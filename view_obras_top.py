import os

html_file = r"C:\Dynastron_Code\VGI\obras.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Just print the first 100 lines
print("\n".join(html.split("\n")[:100]))
