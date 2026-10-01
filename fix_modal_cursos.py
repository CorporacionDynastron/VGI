import os
import re

html_file = r"C:\Dynastron_Code\VGI\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace hoja-body thumb
html = html.replace(
    '<div style="height:180px; margin:-36px -28px 25px -28px; overflow:hidden;"><img src="./03-mantenimiento/IMAGEN%202.png"',
    '<div style="height:180px; margin:-36px -28px 25px -28px; overflow:hidden;"><img src="./05-formacion/IMAGEN%201.jpeg"'
)

# Find modal-cursos left image
html = html.replace(
    '<img src="./03-mantenimiento/IMAGEN%202.png" style="width:100%; height:100%; object-fit:cover; position:absolute; inset:0; opacity:0.8;">',
    '<img src="./05-formacion/IMAGEN%202.jpeg" style="width:100%; height:100%; object-fit:cover; position:absolute; inset:0; opacity:0.8;">'
)

# Find the end of the p tag in modal-cursos and append the gallery
match = re.search(r'mantenga est.*?ndares de alta calidad\.\s*</p>', html, flags=re.DOTALL | re.IGNORECASE)
if match:
    # check if we already added it
    if 'VIDEO%208' not in html:
        gallery_html = """
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:20px;">
                  <div style="position:relative; aspect-ratio:16/9; background:#000; overflow:hidden; border-radius:8px;">
                      <video src="./05-formacion/VIDEO%208.mp4" controls style="width:100%; height:100%; object-fit:cover;"></video>
                  </div>
                  <div style="position:relative; aspect-ratio:16/9; background:#000; overflow:hidden; border-radius:8px;">
                      <video src="./05-formacion/VIDEO%207.mp4" controls style="width:100%; height:100%; object-fit:cover;"></video>
                  </div>
                  <div style="position:relative; aspect-ratio:16/9; background:#000; overflow:hidden; border-radius:8px;">
                      <img src="./05-formacion/IMAGEN%203.jpeg" style="width:100%; height:100%; object-fit:cover;">
                  </div>
                  <div style="position:relative; aspect-ratio:16/9; background:#000; overflow:hidden; border-radius:8px;">
                      <img src="./05-formacion/IMAGEN%205.jpeg" style="width:100%; height:100%; object-fit:cover;">
                  </div>
              </div>
        """
        html = html[:match.end()] + gallery_html + html[match.end():]
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print("Updated modal-cursos with videos and photos")
    else:
        print("Gallery already added")
else:
    print("Could not find the paragraph in modal-cursos to inject gallery")

