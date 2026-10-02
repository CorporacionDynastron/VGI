import os

files = {
    "index.html": r"C:\Dynastron_Code\VGI\index.html",
    "nosotros.html": r"C:\Dynastron_Code\VGI\nosotros.html"
}

replacements = {
    "Estudio de ingeniería civil en Ica, Perú:": "Estudio de ingeniería civil:",
    "Proyecto Recreacional Pisco": "Proyecto Recreacional",
    "RECREACIONAL PISCO": "RECREACIONAL",
    "Pavimentación en Cañete": "Pavimentación de Vías",
    "PAVIMENTACIÓN EN CAÑETE": "PAVIMENTACIÓN",
    "Infraestructura Vial Lima": "Infraestructura Vial",
    "VIAL LIMA": "VIAL",
    "Mantenimiento Estructural Pisco": "Mantenimiento Estructural",
    "ESTRUCTURAL PISCO": "ESTRUCTURAL",
    
    # Noticias Dates
    '"noticia-date">Pisco, Ica<': '"noticia-date">Desarrollo de Obras<',
    '"noticia-date">Cañete, Lima<': '"noticia-date">Infraestructura Vial<',
    
    # Noticias Texts
    "en San Andrés, Pisco. Nuestro": ". Nuestro",
    "en Cañete, Lima. Ejecución": ". Ejecución",
    "en la provincia de Pisco. Nuestro": ". Nuestro",
    
    # Meta Tags
    "<span>ICA</span>": "<span>PROYECTO</span>",
    "<span>ICA. PERÚ</span>": "<span>EJECUCIÓN</span>",
    
    # About / Footer
    "se encuentra en Ica, Perú. Ejecutamos": "centraliza y ejecuta",
    "Av. Principal 482, Ica, Perú": "Sede Principal de Operaciones",
}

for name, path in files.items():
    if not os.path.exists(path): continue
    
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    for old, new in replacements.items():
        html = html.replace(old, new)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Applied replacements to {name}")
