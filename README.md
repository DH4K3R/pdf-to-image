# PDF-Image Converter 🖼️📄

Una librería Python profesional para convertir archivos PDF a Imágenes (PNG, JPG, etc.) e Imágenes a PDF. **Compatible con Windows y Linux**.

## Características ✨

✅ Convertir PDF completo a múltiples imágenes  
✅ Convertir página específica de PDF a imagen  
✅ Convertir imágenes a PDF  
✅ Convertir múltiples imágenes a un solo PDF  
✅ Soporte para formatos: PNG, JPG, BMP, TIFF  
✅ Interfaz CLI (Línea de Comandos)  
✅ API Python simple y potente  
✅ **Compatible con Windows y Linux**  
✅ Instalación automática de dependencias  
✅ Acceso directo en escritorio (Windows)  

## Requisitos Previos 📋

- **Python 3.7+**
- **Git** (para clonar el repositorio)

Las demás dependencias se instalan automáticamente.

## Instalación Rápida ⚡

### 🪟 Windows (PowerShell)

```powershell
# 1. Clona el repositorio
git clone https://github.com/DH4K3R/pdf-to-image.git
cd pdf-image-converter

# 2. Ejecuta el script de instalación automática
.\install.ps1

# 3. ¡Listo! Se creará un acceso directo en el escritorio
# Verifica con:
pdf-converter --help
```

### 🐧 Linux (Bash)

```bash
# 1. Clona el repositorio
git clone https://github.com/DH4K3R/pdf-to-image.git
cd pdf-image-converter

# 2. Ejecuta el script de instalación automática
chmod +x install.sh
./install.sh

# 3. ¡Listo! Verifica con:
pdf-converter --help
```

### 📦 Instalación manual (ambas plataformas)

```bash
# Instala desde PyPI (cuando esté publicado)
pip install pdf-image-converter

# O desde el código fuente
pip install -e .
```

## Uso Rápido

### API Python

```python
from pdf_image_converter import PDFConverter, ImageConverter

# Convertir PDF a Imágenes
pdf_converter = PDFConverter("documento.pdf")
pdf_converter.to_images("carpeta_salida")

# Convertir una página específica
pdf_converter.page_to_image(page_number=1, output_path="pagina1.png")

# Convertir Imágenes a PDF
image_converter = ImageConverter()
image_converter.images_to_pdf(
    ["imagen1.png", "imagen2.jpg"],
    "documento.pdf"
)

# Convertir una imagen a PDF
image_converter.image_to_pdf("imagen.png", "documento.pdf")
```

### Línea de Comandos

```powershell
# PDF a Imágenes
pdf-converter pdf-to-images documento.pdf --output carpeta_salida --format png

# Imagen a PDF
pdf-converter images-to-pdf --input carpeta_con_imagenes --output documento.pdf

# Imagen única a PDF
pdf-converter image-to-pdf imagen.png documento.pdf
```

## Ejemplos Detallados

### Ejemplo 1: Convertir PDF completo

```python
from pdf_image_converter import PDFConverter

pdf = PDFConverter("mi_documento.pdf")
pdf.to_images("salida", format="png", dpi=300)
```

### Ejemplo 2: Convertir páginas específicas

```python
from pdf_image_converter import PDFConverter

pdf = PDFConverter("documento.pdf")

# Solo páginas 1-5
pdf.to_images("salida", pages=[1, 2, 3, 4, 5])

# Página 1 con DPI alto para mejor calidad
pdf.page_to_image(page_number=1, output_path="pagina1_hd.png", dpi=600)
```

### Ejemplo 3: Crear PDF desde múltiples imágenes

```python
from pdf_image_converter import ImageConverter

converter = ImageConverter()
converter.images_to_pdf(
    ["img1.png", "img2.jpg", "img3.png"],
    "documento_final.pdf",
    size=(210, 297)  # Tamaño A4 en mm
)
```

## Estructura del Proyecto

```
pdf-image-converter/
├── pdf_image_converter/
│   ├── __init__.py
│   ├── pdf_converter.py       # Lógica de PDF a Imagen
│   ├── image_converter.py     # Lógica de Imagen a PDF
│   ├── cli.py                 # Interfaz línea de comandos
│   └── utils.py               # Funciones auxiliares
├── tests/
│   ├── test_pdf_converter.py
│   ├── test_image_converter.py
│   └── test_integration.py
├── examples/
│   ├── pdf_to_images.py
│   ├── images_to_pdf.py
│   └── batch_processing.py
├── install.ps1                # Script instalación PowerShell
├── setup.py
├── requirements.txt
├── README.md
└── LICENSE
```

## API Completa

### PDFConverter

```python
class PDFConverter:
    def __init__(self, pdf_path)
    def to_images(self, output_dir, format='png', dpi=150, pages=None)
    def page_to_image(self, page_number, output_path, dpi=150, format='png')
    def get_page_count()
```

### ImageConverter

```python
class ImageConverter:
    def images_to_pdf(self, image_paths, output_path, size=None)
    def image_to_pdf(self, image_path, output_path, size=None)
```

## Requisitos del Sistema

| Componente | Requisito |
|-----------|-----------|
| Python | 3.7 o superior |
| Poppler | Recomendado para mejor rendimiento |
| RAM | Mínimo 2GB |
| Almacenamiento | Depende del tamaño de los PDF/imágenes |

## Troubleshooting

### Error: "pdfrw" no encontrado

```powershell
pip install --upgrade pdf2image PyPDF2
```

### Error: Poppler no encontrado

```powershell
pip install poppler-windows
```

### PDF muy grande

Usa parámetros de DPI más bajo:

```python
pdf.to_images("salida", dpi=150)  # Reducir DPI
```

## Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

MIT License - Ver archivo LICENSE para detalles.

## Autor

Tu Nombre - [tu.email@example.com](mailto:tu.email@example.com)

## Soporte

Para reportar problemas o solicitar features:
- Issues: https://github.com/yourusername/pdf-image-converter/issues
- Email: tu.email@example.com

---

⭐ Si te fue útil, considera dar una estrella en GitHub
