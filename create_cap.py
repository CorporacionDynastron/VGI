import os
import re

index_file = r"C:\Dynastron_Code\VGI\index.html"
with open(index_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header
head_match = re.search(r'(.*?<!-- ==========================================================================.*?(?:HERO|SOBRE NOSOTROS))', html, flags=re.DOTALL)
header = head_match.group(1) if head_match else ""
# Remove the <style> parts that are only for index? No, keep it simple.

# Extract footer
footer_match = re.search(r'(<!-- ==========================================================================.*?FOOTER.*)', html, flags=re.DOTALL)
footer = footer_match.group(1) if footer_match else ""

# Generate the content for Capacitaciones
cap_content = """
<!-- HERO CAPACITACIONES -->
<section class="hero" style="min-height: 40vh; padding-top:120px; padding-bottom:50px;">
    <div class="wrap">
        <span class="hero-tag" data-aos="fade-up">INSTITUTO VADGOD</span>
        <h1 class="hero-title" data-aos="fade-up" data-aos-delay="100">Formación<br>Técnica.</h1>
        <p class="hero-desc" data-aos="fade-up" data-aos-delay="200" style="max-width:800px;">
            Compartimos nuestra experiencia directamente desde el campo. Dictamos programas de formación especializados para ingenieros civiles, arquitectos, maestros de obra y operarios, asegurando que el mercado mantenga estándares de alta calidad.
        </p>
    </div>
</section>

<!-- CONTENIDO DE CAPACITACIONES -->
<section style="background:var(--paper); padding:60px 0;">
    <div class="wrap">
        <div style="margin-bottom:60px;">
            <h2 style="font-family:var(--display); font-size:32px; color:var(--navy); margin-bottom:20px; text-transform:uppercase;">Videos Destacados</h2>
            
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:40px;">
                <!-- Video 1 -->
                <div style="background:#fff; border-radius:12px; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.05);">
                    <div style="position:relative; aspect-ratio:16/9; background:#000;">
                        <video src="./05-formacion/VIDEO 2.mp4" controls style="width:100%; height:100%; object-fit:cover;"></video>
                    </div>
                    <div style="padding:25px;">
                        <h4 style="font-family:var(--display); font-size:20px; color:var(--navy); margin-bottom:10px;">Sustentación de Mejora de Suelos</h4>
                        <p style="font-size:14px; color:var(--steel); line-height:1.6;">
                            Exposición académica detallando el método de estabilización y mejoramiento del suelo utilizando cemento en un 3%. Análisis práctico con demostración en maqueta a escala.
                        </p>
                    </div>
                </div>

                <!-- Video 2 -->
                <div style="background:#fff; border-radius:12px; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.05);">
                    <div style="position:relative; aspect-ratio:16/9; background:#000;">
                        <video src="./05-formacion/VIDEO 5.mp4" controls style="width:100%; height:100%; object-fit:cover;"></video>
                    </div>
                    <div style="padding:25px;">
                        <h4 style="font-family:var(--display); font-size:20px; color:var(--navy); margin-bottom:10px;">Taller de Cimentaciones en Maqueta</h4>
                        <p style="font-size:14px; color:var(--steel); line-height:1.6;">
                            Revisión detallada de un modelo físico (maqueta) que ilustra procesos constructivos, zapatas, cimientos y disposición de acero de refuerzo para una comprensión práctica y directa.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <div>
            <h2 style="font-family:var(--display); font-size:32px; color:var(--navy); margin-bottom:20px; text-transform:uppercase;">Galería de Formación</h2>
            <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(250px, 1fr)); gap:15px;">
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden;"><img src="./05-formacion/IMAGEN 1.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden;"><img src="./05-formacion/IMAGEN 2.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden;"><img src="./05-formacion/IMAGEN 3.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden;"><img src="./05-formacion/IMAGEN 4.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden;"><img src="./05-formacion/IMAGEN 5.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden;"><img src="./05-formacion/IMAGEN 6.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden;"><img src="./05-formacion/IMAGEN 7.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden;"><img src="./05-formacion/IMAGEN 8.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
            </div>
        </div>
    </div>
</section>
"""

full_html = header + cap_content + footer

with open(r"C:\Dynastron_Code\VGI\capacitaciones.html", 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Created capacitaciones.html")
