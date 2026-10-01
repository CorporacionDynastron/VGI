import re

html_file = r"C:\Dynastron_Code\VGI\obras.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the Saneamiento section specifically
saneamiento_section = re.search(r'id="saneamiento".*?(?:<section|$)', html, flags=re.DOTALL | re.IGNORECASE)
if saneamiento_section:
    print("Found saneamiento section:")
    images = re.findall(r'<img.*?src="(.*?)"', saneamiento_section.group(0))
    for img in images:
        print(f"Image: {img}")
else:
    print("No saneamiento section found.")
