import os
import re

html_file = r"C:\Dynastron_Code\VGI\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Change modal trigger to page link
html = html.replace('onclick="openHojaModal(\'modal-obras\')"', 'onclick="window.location.href=\'obras.html\'" style="cursor:pointer;"')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html to point to obras.html")
