import re

html_file = r"C:\Dynastron_Code\VGI\obras.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

titles = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', html, flags=re.IGNORECASE)
for i, title in enumerate(titles):
    print(f"Title {i}: {title.strip()}")
