import os

target_vgi = r"C:\Dynastron_Code\VGI"
html_files = ["index.html", "nosotros.html", "obras.html", "planos.html", "capacitaciones.html"]

responsive_css = """
    <style id="global-responsive-fixes">
    /* GLOBAL RESPONSIVE FIXES */
    @media (max-width: 980px) {
        .wrap { padding-left: 20px; padding-right: 20px; }
    }
    @media (max-width: 768px) {
        .hero-obras, .hero-section, .hero { padding: 100px 0 50px !important; }
        .hero-obras h1, .hero-section h1, .hero h1 { font-size: clamp(28px, 8vw, 40px) !important; }
        .grid-container, .obras-grid, .features-grid, .valores-grid, .stat-grid, .contact-grid, .footer-grid { 
            grid-template-columns: 1fr !important; gap: 24px !important; 
        }
        .hoja-body { flex-direction: column !important; }
        .hoja-image, .hoja-content { width: 100% !important; max-width: 100% !important; }
        section { padding: 50px 0 !important; }
        .modal-content { flex-direction: column !important; }
        .modal-left { width: 100% !important; position: relative !important; height: 300px !important; }
        .modal-right { width: 100% !important; padding: 20px !important; overflow-y: visible !important; }
        .modal-body { height: 90vh !important; overflow-y: auto !important; }
        .category-title { font-size: 24px !important; }
    }
    </style>
</head>
"""

for filename in html_files:
    filepath = os.path.join(target_vgi, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove old block if exists to avoid duplicates
    if '<style id="global-responsive-fixes">' in html:
        import re
        html = re.sub(r'<style id="global-responsive-fixes">.*?</style>\s*</head>', '</head>', html, flags=re.DOTALL)
    
    html = html.replace("</head>", responsive_css)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Injected responsive CSS into {filename}")

