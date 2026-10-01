import os

obras_file = r"C:\Dynastron_Code\VGI\obras.html"
with open(obras_file, 'r', encoding='utf-8') as f:
    obras = f.read()

header = obras.split('<section class="hero-obras">')[0]
footer = '<footer class="footer">' + obras.split('<footer class="footer">')[1]

# Modify the title in the header slightly for capacitaciones
header = header.replace("<title>Galería de Obras | VADGOD INGS</title>", "<title>Formación Técnica | VADGOD INGS</title>")

cap_content = """
<!-- HERO CAPACITACIONES -->
<section class="hero-obras" style="background: var(--navy-deep); color: white; padding: 180px 0 80px; text-align: center;">
    <div class="wrap">
        <span class="eyebrow" style="font-family: var(--mono); font-size: 11px; letter-spacing: .15em; color: var(--gold); text-transform: uppercase; margin-bottom: 20px; display: block;">INSTITUTO VADGOD</span>
        <h1 style="font-family: var(--display); font-size: clamp(36px, 5vw, 60px); line-height: 1.1; margin-bottom: 24px; text-transform: uppercase;">Formación Técnica</h1>
        <p style="color: rgba(255,255,255,0.7); max-width: 600px; margin: 0 auto; line-height: 1.6;">
            Compartimos nuestra experiencia directamente desde el campo. Dictamos programas de formación especializados para ingenieros civiles, arquitectos, maestros de obra y operarios, asegurando que el mercado mantenga estándares de alta calidad.
        </p>
    </div>
</section>

<!-- CONTENIDO DE CAPACITACIONES -->
<section style="background:var(--paper); padding:80px 0;">
    <div class="wrap">
        <div style="margin-bottom:80px;">
            <h2 style="font-family:var(--display); font-size:28px; color:var(--navy); margin-bottom:40px; text-transform:uppercase; text-align:center;">Videos Destacados</h2>
            
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:40px;">
                <!-- Video 1 -->
                <div style="background:#fff; border-radius:12px; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.05);">
                    <div style="position:relative; aspect-ratio:16/9; background:#000;">
                        <video src="./05-formacion/VIDEO 2.mp4" controls style="width:100%; height:100%; object-fit:cover;"></video>
                    </div>
                    <div style="padding:30px;">
                        <h4 style="font-family:var(--display); font-size:18px; font-weight:700; color:var(--navy); margin-bottom:12px; text-transform:uppercase;">Sustentación de Mejora de Suelos</h4>
                        <p style="font-size:15px; color:var(--steel); line-height:1.7;">
                            Exposición académica detallando el método de estabilización y mejoramiento del suelo utilizando cemento en un 3%. Análisis práctico con demostración en maqueta a escala.
                        </p>
                    </div>
                </div>

                <!-- Video 2 -->
                <div style="background:#fff; border-radius:12px; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.05);">
                    <div style="position:relative; aspect-ratio:16/9; background:#000;">
                        <video src="./05-formacion/VIDEO 5.mp4" controls style="width:100%; height:100%; object-fit:cover;"></video>
                    </div>
                    <div style="padding:30px;">
                        <h4 style="font-family:var(--display); font-size:18px; font-weight:700; color:var(--navy); margin-bottom:12px; text-transform:uppercase;">Taller de Cimentaciones en Maqueta</h4>
                        <p style="font-size:15px; color:var(--steel); line-height:1.7;">
                            Revisión detallada de un modelo físico (maqueta) que ilustra procesos constructivos, zapatas, cimientos y disposición de acero de refuerzo para una comprensión práctica y directa.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <div>
            <h2 style="font-family:var(--display); font-size:28px; color:var(--navy); margin-bottom:40px; text-transform:uppercase; text-align:center;">Galería de Formación</h2>
            <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:20px;">
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05);"><img src="./05-formacion/IMAGEN 1.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05);"><img src="./05-formacion/IMAGEN 2.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05);"><img src="./05-formacion/IMAGEN 3.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05);"><img src="./05-formacion/IMAGEN 4.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05);"><img src="./05-formacion/IMAGEN 5.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05);"><img src="./05-formacion/IMAGEN 6.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05);"><img src="./05-formacion/IMAGEN 7.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
                <div style="aspect-ratio:4/3; border-radius:8px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.05);"><img src="./05-formacion/IMAGEN 8.jpeg" style="width:100%; height:100%; object-fit:cover;"></div>
            </div>
        </div>
    </div>
</section>
"""

full_html = header + cap_content + footer

with open(r"C:\Dynastron_Code\VGI\capacitaciones.html", 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Regenerated capacitaciones.html cleanly!")
