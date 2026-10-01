import os

html_file = r"C:\Dynastron_Code\VGI\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace 01
html = html.replace('01.%20RECREACION-%20NACIONES%20UNIDAS%2C%20%20SAN%20ANDRES%2C%20PISCO', '01-recreacion')
# Replace 02 (with and without %C3%91 which is Ñ)
html = html.replace('02.%20PISTAS%20Y%20VEREDAS-%20CA%C3%91ETE.%20LIMA', '02-pistas')
html = html.replace('02.%20PISTAS%20Y%20VEREDAS-%20CAETE.%20LIMA', '02-pistas')
# Replace 03
html = html.replace('03.%20MANTENIMIENTO-%20PISCO', '03-mantenimiento')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed paths in index.html")
