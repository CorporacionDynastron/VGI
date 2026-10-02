import re
with open(r"C:\Dynastron_Code\VGI\planos.html", 'r', encoding='utf-8') as f:
    html = f.read()

# Find the hero section
match = re.search(r'<section class="hero[^>]*>.*?</section>', html, re.DOTALL | re.IGNORECASE)
if match:
    print(match.group(0))
else:
    match = re.search(r'<!-- HERO.*?-->(.*?)<!--', html, re.DOTALL | re.IGNORECASE)
    if match:
        print(match.group(0))
