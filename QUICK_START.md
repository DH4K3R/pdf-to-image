# INICIO RÁPIDO 🚀

## ✅ Librería lista para instalar desde PowerShell y Bash

### 📋 Estructura creada:

```
pdf-image-converter/
├── 📁 pdf_image_converter/          # Código principal
│   ├── __init__.py
│   ├── pdf_converter.py             # PDF → Imágenes
│   ├── image_converter.py           # Imágenes → PDF
│   ├── cli.py                       # Interfaz línea de comandos
│   ├── icon.svg                     # Icono de la aplicación
│   └── utils.py
├── 📁 examples/                     # Ejemplos de uso
├── 📁 tests/                        # Tests unitarios
├── setup.py                         # Configuración (cross-platform)
├── install.ps1                      # ⚙️ Instalador automático Windows
├── install.sh                       # ⚙️ Instalador automático Linux
├── pdf-converter.bat                # 🪟 Launcher Windows
├── pdf-converter.sh                 # 🐧 Launcher Linux
├── requirements.txt                 # Dependencias
├── requirements-dev.txt             # Dependencias desarrollo
├── README.md                        # Documentación
├── INSTALL.md                       # Guía instalación detallada
├── MANIFEST.in                      # Archivos a incluir
├── LICENSE                          # MIT License
└── .gitignore
```

## 🪟 Instalación Windows (PowerShell)

```powershell
# 1. Clona el repositorio
git clone https://github.com/yourusername/pdf-image-converter.git
cd pdf-image-converter

# 2. Ejecuta la instalación automática
.\install.ps1

# ¡Listo! Se creará un acceso directo en el escritorio
```

**El script automáticamente:**
- ✅ Verifica Python y pip
- ✅ Actualiza pip
- ✅ Instala todas las dependencias
- ✅ Instala poppler-windows (para convertir PDFs)
- ✅ Instala la librería
- ✅ Crea acceso directo en el escritorio

## 🐧 Instalación Linux (Bash)

```bash
# 1. Clona el repositorio
git clone https://github.com/yourusername/pdf-image-converter.git
cd pdf-image-converter

# 2. Dale permisos de ejecución
chmod +x install.sh

# 3. Ejecuta la instalación automática
./install.sh

# ¡Listo! Se configurará automáticamente
```

**El script automáticamente:**
- ✅ Detecta tu distribución Linux
- ✅ Instala poppler (Ubuntu/Debian/Fedora/CentOS/Arch)
- ✅ Verifica Python y pip
- ✅ Actualiza pip
- ✅ Instala todas las dependencias
- ✅ Instala la librería
- ✅ Crea launcher en ~/.local/bin/

## 💡 Usos principales

### 🪟 Windows (PowerShell)

```powershell
# Opción 1: Haz doble clic en "PDF-Image Converter" en el escritorio

# Opción 2: Desde PowerShell
pdf-converter --help
pdf-converter pdf-to-images documento.pdf --output carpeta_salida --dpi 300
pdf-converter images-to-pdf --input carpeta_imagenes --output documento.pdf
```

### 🐧 Linux (Terminal)

```bash
# Desde terminal
pdf-converter --help
pdf-converter pdf-to-images documento.pdf --output carpeta_salida --dpi 300
pdf-converter images-to-pdf --input carpeta_imagenes --output documento.pdf

# O usa el launcher
./pdf-converter.sh
```

### 🐍 Desde Python (ambas plataformas)

```python
from pdf_image_converter import PDFConverter, ImageConverter

# PDF a Imágenes
pdf = PDFConverter("documento.pdf")
archivos = pdf.to_images("salida", dpi=300)
print(f"Convertidas {len(archivos)} imágenes")

# Imágenes a PDF
converter = ImageConverter()
converter.images_to_pdf(["img1.png", "img2.jpg"], "documento.pdf")
```

## 📦 Características

✅ Convertir PDF completo a múltiples imágenes  
✅ Convertir página específica de PDF  
✅ Convertir imágenes a PDF  
✅ Soporte PNG, JPG, BMP, TIFF  
✅ CLI completa  
✅ API Python profesional  
✅ **Compatible Windows + Linux**  
✅ **Instalación automática de todas las dependencias**  
✅ **Acceso directo / Launcher incluido**  
✅ Documentación completa  
✅ Tests unitarios  

## 🔧 Requisitos mínimos

| Requisito | Windows | Linux |
|-----------|---------|-------|
| Python | 3.7+ | 3.7+ |
| Git | Recomendado | Recomendado |
| Permisos | Usuario normal | Usuario normal |
| Admin | No (excepto execution policy) | No |

## 📚 Documentación

| Archivo | Propósito |
|---------|-----------|
| README.md | Guía principal y características |
| INSTALL.md | Guía detallada para ambas plataformas |
| examples/usage_examples.py | Ejemplos de código |
| tests/test_converters.py | Tests unitarios |

## 🌐 Subir a GitHub

```bash
git init
git add .
git commit -m "Initial commit: PDF-Image Converter Library"
git branch -M main
git remote add origin https://github.com/yourusername/pdf-image-converter.git
git push -u origin main
```

## 🎁 Bonificaciones incluidas

- 🎨 Icono profesional (SVG)
- 📜 Scripts launcher para Windows y Linux
- 🔄 Instalación automática de todas las dependencias
- 📋 Guía de instalación multi-plataforma
- 🧪 Tests unitarios listos para usar
- 📖 Documentación en español
- 📦 Estructura lista para publicar en PyPI

## ⚠️ Si tienes problemas

Ver **INSTALL.md** para troubleshooting detallado y soluciones para:
- Errores de PowerShell
- Python no encontrado
- Poppler no encontrado
- Problemas de permisos en Linux
- Y más...

---

¡Librería **completamente lista para usar**! 🎉

Compatible con **Windows y Linux** con instalación **100% automática**.
