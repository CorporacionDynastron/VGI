import re
with open(r"C:\Dynastron_Code\VGI\planos.html", 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'\.hero-planos\s*\{[^}]*\}', html)
if match:
    print(match.group(0))
