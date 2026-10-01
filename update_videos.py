import os

html_file = r"C:\Dynastron_Code\VGI\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace VIDEO 8 with VIDEO 5 (2MB instead of 11MB)
html = html.replace("VIDEO%208.mp4", "VIDEO%205.mp4")
# Replace VIDEO 7 with VIDEO 2 (1.7MB instead of 1.5MB but let's just make it VIDEO 2)
html = html.replace("VIDEO%207.mp4", "VIDEO%202.mp4")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated video selection to lighter/better videos")
