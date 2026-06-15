#!/usr/bin/env python3
"""Script para post-instalación y configuración"""

import os
import sys
import platform
from pathlib import Path


def print_section(title):
    """Imprime un encabezado"""
    print(f"\n{'='*50}")
    print(f"  {title}")
    print(f"{'='*50}\n")


def main():
    """Función principal"""
    print_section("PDF-Image Converter - Post-Instalación")
    
    system = platform.system()
    print(f"Sistema detectado: {system}")
    print(f"Python: {platform.python_version()}")
    
    # Crear directorio de datos
    if system == "Windows":
        data_dir = Path(os.getenv('USERPROFILE')) / ".pdf-image-converter"
    else:
        data_dir = Path.home() / ".pdf-image-converter"
    
    data_dir.mkdir(exist_ok=True)
    print(f"\n✅ Directorio de datos: {data_dir}")
    
    # Crear subdirectorios
    (data_dir / "uploads").mkdir(exist_ok=True)
    (data_dir / "outputs").mkdir(exist_ok=True)
    print(f"✅ Subdirectorios creados")
    
    # Verificar instalación
    print_section("Verificación de Instalación")
    
    try:
        from pdf_image_converter import PDFConverter, ImageConverter
        print("✅ Módulo pdf_image_converter importado correctamente")
    except ImportError as e:
        print(f"❌ Error al importar: {e}")
        return 1
    
    try:
        import pdf2image
        print("✅ pdf2image instalado")
    except ImportError:
        print("⚠️ pdf2image no encontrado")
    
    try:
        import PIL
        print("✅ Pillow instalado")
    except ImportError:
        print("⚠️ Pillow no encontrado")
    
    # Instrucciones finales
    print_section("¡Instalación Completada!")
    
    print(f"Plataforma: {system}")
    print(f"\nComandos disponibles:")
    print(f"  pdf-converter --help")
    print(f"  pdf-converter pdf-to-images documento.pdf --output salida")
    print(f"  pdf-converter images-to-pdf --input carpeta --output documento.pdf")
    
    if system == "Windows":
        print(f"\n💡 También puedes hacer doble clic en:")
        print(f"   'PDF-Image Converter' en tu escritorio")
    
    print(f"\n📚 Documentación:")
    print(f"  - README.md: Guía general")
    print(f"  - INSTALL.md: Instalación detallada")
    print(f"  - QUICK_START.md: Inicio rápido")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
