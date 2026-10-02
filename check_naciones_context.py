import re
with open(r"C:\Dynastron_Code\VGI\index.html", 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.finditer(r'.{0,100}Parque Naciones Unidas.{0,100}', html, re.IGNORECASE | re.DOTALL)
for m in matches:
    print("Found context:\n", repr(m.group(0)))
