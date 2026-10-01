import os
import re

html_file = r"C:\Dynastron_Code\VGI\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's find the whole testimonios section which contains client-marks
match = re.search(r'<div class="client-marks">.*?</div>\s*</div>\s*</section>', html, flags=re.DOTALL)
if match:
    old_html = match.group(0)
    
    new_html = """
        <div style="margin-top:40px;">
            <h5 style="font-family:var(--display); font-size:16px; color:var(--navy); margin-bottom:15px; text-transform:uppercase; font-weight:700;">Patrocinadores y Marcas Aliadas</h5>
            <div class="client-marks" style="margin-bottom:30px;">
                <div class="client-mark" title="Aceros Arequipa">
                    <img src="./storage/aliados/qdxDX4Is7LXzQiO4274OO4ZoyyoEmvIbcTBmcR0r.webp" alt="ACEROS AREQUIPA">
                </div>
                <div class="client-mark" title="Cemento Sol">
                    <img src="./storage/aliados/gRpn81FV7bMEmfIBQREgyGnJyFfxRsTxRJr7eRUB.jpg" alt="CEMENTO SOL">
                </div>
                <div class="client-mark" title="Sika">
                    <img src="./storage/aliados/fHSSJMGyFg8BCa1DhN270wRvgyEnR5UFqVPMzaWk.webp" alt="SIKA">
                </div>
                <div class="client-mark" title="Ladrillos Gonzaga">
                    <img src="./storage/aliados/qPS6pte7yVCcqvtVWwukart42a2wPySC8w1mW9Vk.png" alt="Ladrillos Gonzaga">
                </div>
            </div>

            <h5 style="font-family:var(--display); font-size:16px; color:var(--navy); margin-bottom:15px; text-transform:uppercase; font-weight:700;">Certificaciones de Calidad</h5>
            <div class="client-marks">
                <div class="client-mark" title="Colegio de Ingenieros del Perú">
                    <img src="./storage/aliados/IUbbSY3xCcy6hNE5Xz17vDL5Z2Oj8CLN9fkKMD5r.png" alt="CIP">
                </div>
                <div class="client-mark" title="ISO 37001">
                    <img src="./CERTIFICACIONES/ISO 37001.jpg" alt="ISO 37001">
                </div>
                <!-- Future ISOs can go here -->
            </div>
        </div>
      </div>
    </div>
  </section>"""
    html = html.replace(old_html, new_html.strip())
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated client-marks splitting.")
else:
    print("Could not find client-marks section.")
