import re
with open(r"C:\Dynastron_Code\VGI\index.html", 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.finditer(r'Pisco,\s*Ica', html, re.IGNORECASE)
count = 0
for m in matches:
    print("Found Pisco, Ica:", m.group(0))
    count += 1
print(f"Total matches: {count}")

matches2 = re.finditer(r'Cañete,\s*Lima', html, re.IGNORECASE)
count2 = 0
for m in matches2:
    print("Found Cañete, Lima:", m.group(0))
    count2 += 1
print(f"Total matches2: {count2}")
