import re
with open(r"C:\Dynastron_Code\VGI\index.html", 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.finditer(r'.{0,30}Pisco, Ica.{0,30}', html, re.IGNORECASE | re.DOTALL)
for m in matches:
    print("Found Pisco, Ica:", repr(m.group(0)))

matches2 = re.finditer(r'.{0,30}Cañete, Lima.{0,30}', html, re.IGNORECASE | re.DOTALL)
for m in matches2:
    print("Found Cañete, Lima:", repr(m.group(0)))
