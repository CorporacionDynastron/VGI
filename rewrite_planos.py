import os
import re

html_file = r"C:\Dynastron_Code\VGI\planos.html"

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Define the new grouped HTML structure
new_gallery_html = """<section class="galeria-section">
    <div class="wrap">
        <style>
            .category-section { margin-bottom: 80px; }
            .category-title { font-family: var(--display); font-size: 32px; color: var(--navy); margin-bottom: 40px; border-bottom: 2px solid var(--gold); padding-bottom: 15px; text-transform: uppercase; }
            .project-group { margin-bottom: 50px; }
            .project-title { font-family: var(--body); font-size: 22px; color: var(--steel); margin-bottom: 25px; display: flex; align-items: center; gap: 15px; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; }
            .project-title::before { content: ""; display: block; width: 30px; height: 2px; background: var(--gold); }
            .empty-msg { color: var(--steel); font-style: italic; font-size: 15px; }
        </style>

        <!-- VIVIENDAS UNIFAMILIARES -->
        <div class="category-section">
            <h3 class="category-title">Viviendas Unifamiliares</h3>
            
            <div class="project-group">
                <h4 class="project-title">Proyecto Amalfi</h4>
                <div class="grid-container">
                    <!-- Amalfi -->
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20AMALFI-%20UNIFAMILIAR.png', 'PROYECTO AMALFI - FACHADA')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20AMALFI-%20UNIFAMILIAR.png" loading="lazy" alt="PROYECTO AMALFI - FACHADA"></div>
                        <div class="info"><h4>FACHADA</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20AMALFI-%20INTERIOR%201.png', 'PROYECTO AMALFI - INTERIOR 1')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20AMALFI-%20INTERIOR%201.png" loading="lazy" alt="PROYECTO AMALFI - INTERIOR 1"></div>
                        <div class="info"><h4>INTERIOR 1</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20AMALFI-%20INTERIOR%202.png', 'PROYECTO AMALFI - INTERIOR 2')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20AMALFI-%20INTERIOR%202.png" loading="lazy" alt="PROYECTO AMALFI - INTERIOR 2"></div>
                        <div class="info"><h4>INTERIOR 2</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20AMALFI-%20INTERIOR%203.png', 'PROYECTO AMALFI - INTERIOR 3')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20AMALFI-%20INTERIOR%203.png" loading="lazy" alt="PROYECTO AMALFI - INTERIOR 3"></div>
                        <div class="info"><h4>INTERIOR 3</h4></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- VIVIENDAS MULTIFAMILIARES -->
        <div class="category-section">
            <h3 class="category-title">Viviendas Multifamiliares</h3>
            
            <div class="project-group">
                <h4 class="project-title">Proyecto Lituania</h4>
                <div class="grid-container">
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20LITUANIA-MULTIFAMILIAR.png', 'PROYECTO LITUANIA - FACHADA')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20LITUANIA-MULTIFAMILIAR.png" loading="lazy" alt="PROYECTO LITUANIA - FACHADA"></div>
                        <div class="info"><h4>FACHADA</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20LITUANIA-IINTERIOR%201.png', 'PROYECTO LITUANIA - INTERIOR 1')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20LITUANIA-IINTERIOR%201.png" loading="lazy" alt="PROYECTO LITUANIA - INTERIOR 1"></div>
                        <div class="info"><h4>INTERIOR 1</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20LITUANIA-IINTERIOR%202.png', 'PROYECTO LITUANIA - INTERIOR 2')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20LITUANIA-IINTERIOR%202.png" loading="lazy" alt="PROYECTO LITUANIA - INTERIOR 2"></div>
                        <div class="info"><h4>INTERIOR 2</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20LITUANIA%20-%20INTERIOR%203.png', 'PROYECTO LITUANIA - INTERIOR 3')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20LITUANIA%20-%20INTERIOR%203.png" loading="lazy" alt="PROYECTO LITUANIA - INTERIOR 3"></div>
                        <div class="info"><h4>INTERIOR 3</h4></div>
                    </div>
                </div>
            </div>

            <div class="project-group">
                <h4 class="project-title">Proyecto Manhattan</h4>
                <div class="grid-container">
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20MANHATAN-%20MULTIFAMILIAR.png', 'PROYECTO MANHATAN - FACHADA')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20MANHATAN-%20MULTIFAMILIAR.png" loading="lazy" alt="PROYECTO MANHATAN - FACHADA"></div>
                        <div class="info"><h4>FACHADA</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20MANHATAN%20-%20INTERIOR%201.png', 'PROYECTO MANHATAN - INTERIOR 1')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20MANHATAN%20-%20INTERIOR%201.png" loading="lazy" alt="PROYECTO MANHATAN - INTERIOR 1"></div>
                        <div class="info"><h4>INTERIOR 1</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20MANHATAN%20-%20INTERIOR%202.png', 'PROYECTO MANHATAN - INTERIOR 2')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20MANHATAN%20-%20INTERIOR%202.png" loading="lazy" alt="PROYECTO MANHATAN - INTERIOR 2"></div>
                        <div class="info"><h4>INTERIOR 2</h4></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- CASAS DE CAMPO -->
        <div class="category-section">
            <h3 class="category-title">Casas de Campo</h3>
            
            <div class="project-group">
                <h4 class="project-title">Proyecto Alborada</h4>
                <div class="grid-container">
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20ALBORADA%20-%20CASA%20DE%20CAMPO.png', 'PROYECTO ALBORADA - FACHADA')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20ALBORADA%20-%20CASA%20DE%20CAMPO.png" loading="lazy" alt="PROYECTO ALBORADA - FACHADA"></div>
                        <div class="info"><h4>FACHADA</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20ALBORADA%20-%20INTERIOR%201.png', 'PROYECTO ALBORADA - INTERIOR 1')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20ALBORADA%20-%20INTERIOR%201.png" loading="lazy" alt="PROYECTO ALBORADA - INTERIOR 1"></div>
                        <div class="info"><h4>INTERIOR 1</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20ALBORADA%20-%20INTERIOR%202.png', 'PROYECTO ALBORADA - INTERIOR 2')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20ALBORADA%20-%20INTERIOR%202.png" loading="lazy" alt="PROYECTO ALBORADA - INTERIOR 2"></div>
                        <div class="info"><h4>INTERIOR 2</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20ALBORADA%20-%20INTERIOR%203.png', 'PROYECTO ALBORADA - INTERIOR 3')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20ALBORADA%20-%20INTERIOR%203.png" loading="lazy" alt="PROYECTO ALBORADA - INTERIOR 3"></div>
                        <div class="info"><h4>INTERIOR 3</h4></div>
                    </div>
                </div>
            </div>

            <div class="project-group">
                <h4 class="project-title">Proyecto Olivo</h4>
                <div class="grid-container">
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20OLIVO%20-%20CASA%20DE%20CAMPO.png', 'PROYECTO OLIVO - FACHADA')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20OLIVO%20-%20CASA%20DE%20CAMPO.png" loading="lazy" alt="PROYECTO OLIVO - FACHADA"></div>
                        <div class="info"><h4>FACHADA</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20OLIVO%20-%20INTERIOR%201.png', 'PROYECTO OLIVO - INTERIOR 1')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20OLIVO%20-%20INTERIOR%201.png" loading="lazy" alt="PROYECTO OLIVO - INTERIOR 1"></div>
                        <div class="info"><h4>INTERIOR 1</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20OLIVO%20-%20INTERIOR%202.png', 'PROYECTO OLIVO - INTERIOR 2')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20OLIVO%20-%20INTERIOR%202.png" loading="lazy" alt="PROYECTO OLIVO - INTERIOR 2"></div>
                        <div class="info"><h4>INTERIOR 2</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20OLIVO%20-%20INTERIOR%203.png', 'PROYECTO OLIVO - INTERIOR 3')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20OLIVO%20-%20INTERIOR%203.png" loading="lazy" alt="PROYECTO OLIVO - INTERIOR 3"></div>
                        <div class="info"><h4>INTERIOR 3</h4></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- CASAS DE PLAYA -->
        <div class="category-section">
            <h3 class="category-title">Casas de Playa</h3>
            
            <div class="project-group">
                <h4 class="project-title">Proyecto Brisa</h4>
                <div class="grid-container">
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20BRISA%20-CASA%20DE%20PLAYA.png', 'PROYECTO BRISA - FACHADA')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20BRISA%20-CASA%20DE%20PLAYA.png" loading="lazy" alt="PROYECTO BRISA - FACHADA"></div>
                        <div class="info"><h4>FACHADA</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20BRISA%20-interior%201.png', 'PROYECTO BRISA - INTERIOR 1')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20BRISA%20-interior%201.png" loading="lazy" alt="PROYECTO BRISA - INTERIOR 1"></div>
                        <div class="info"><h4>INTERIOR 1</h4></div>
                    </div>
                </div>
            </div>

            <div class="project-group">
                <h4 class="project-title">Proyecto Coral</h4>
                <div class="grid-container">
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20CORAL%20-%20CASA%20DE%20PLAYA.png', 'PROYECTO CORAL - FACHADA')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20CORAL%20-%20CASA%20DE%20PLAYA.png" loading="lazy" alt="PROYECTO CORAL - FACHADA"></div>
                        <div class="info"><h4>FACHADA</h4></div>
                    </div>
                    <div class="gallery-card" onclick="openLightbox('./Fotos%20Proyectos/PROYECTO%20CORAL%20-%20interior%201.png', 'PROYECTO CORAL - INTERIOR 1')">
                        <div class="img-wrap"><img src="./Fotos%20Proyectos/PROYECTO%20CORAL%20-%20interior%201.png" loading="lazy" alt="PROYECTO CORAL - INTERIOR 1"></div>
                        <div class="info"><h4>INTERIOR 1</h4></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- PISCINAS -->
        <div class="category-section">
            <h3 class="category-title">Piscinas</h3>
            <p class="empty-msg">Nuevos proyectos de piscinas en ejecución. Pronto publicaremos los resultados.</p>
        </div>

    </div>
</section>"""

# Replace the existing section
html = re.sub(r'<section class="galeria-section">.*?</section>', new_gallery_html, html, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated planos.html layout")
