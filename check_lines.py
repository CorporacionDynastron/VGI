html_file = r"C:\Dynastron_Code\VGI\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
print("Line 1384:", lines[1383].strip())
print("Line 1540:", lines[1539].strip())
