# Guía de Instalación desde PowerShell y Bash

## 🪟 Windows (PowerShell)

### Requisitos previos

- **Python 3.7+** - Descarga desde https://www.python.org/downloads/
- **Git** - Descarga desde https://git-scm.com/

### Instalación paso a paso

```powershell
# 1. Clona el repositorio
git clone https://github.com/yourusername/pdf-image-converter.git
cd pdf-image-converter

# 2. Si necesitas ejecución de scripts, ejecuta como administrador:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 3. Ejecuta el script de instalación automática
.\install.ps1

# La instalación automáticamente:
# ✅ Verifica Python y pip
# ✅ Actualiza pip
# ✅ Instala todas las dependencias necesarias
# ✅ Instala la librería pdf-image-converter
# ✅ Crea un acceso directo en el escritorio
```

### Verificación de instalación

```powershell
# Debería mostrar la ayuda
pdf-converter --help

# Prueba rápida
pdf-converter pdf-info documento.pdf
```

---

## 🐧 Linux (Ubuntu, Debian, Fedora, CentOS)

### Requisitos previos

- **Python 3.7+**
- **Git**

En la mayoría de distribuciones ya están preinstalados. Si no:

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-pip git

# Fedora
sudo dnf install python3-pip git

# CentOS
sudo yum install python3-pip git
```

### Instalación paso a paso

```bash
# 1. Clona el repositorio
git clone https://github.com/yourusername/pdf-image-converter.git
cd pdf-image-converter

# 2. Dale permisos de ejecución al script
chmod +x install.sh

# 3. Ejecuta el script de instalación automática
./install.sh

# La instalación automáticamente:
# ✅ Instala Poppler (según tu distribución)
# ✅ Verifica Python y pip
# ✅ Actualiza pip
# ✅ Instala todas las dependencias necesarias
# ✅ Instala la librería pdf-image-converter
# ✅ Crea un launcher en ~/.local/bin/
```

### Verificación de instalación

```bash
# Debería mostrar la ayuda
pdf-converter --help

# Prueba rápida
pdf-converter pdf-info documento.pdf
```

---

## 📦 Instalación Manual (ambas plataformas)

```bash
# 1. Clona el repositorio
git clone https://github.com/yourusername/pdf-image-converter.git
cd pdf-image-converter

# 2. (Solo Linux) Instala Poppler
# Ubuntu/Debian:
sudo apt-get install poppler-utils

# Fedora:
sudo dnf install poppler-utils

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Instala la librería
pip install -e .

# 5. Verifica
pdf-converter --help
```

---

## 🔧 Instalación con dependencias de desarrollo

Para contribuir al proyecto:

```powershell
# Windows
.\install.ps1 -Dev

# Linux
./install.sh  # El script detecta git y configura automáticamente
```

Esto instala además:
- pytest (para tests)
- black (para formateo de código)
- flake8 (para análisis de código)
- mypy (para type checking)

---

## ⚠️ Solucionar Problemas

### Error: "Python no encontrado" o "pip no encontrado"

**Windows:**
```powershell
# Verifica que Python está en PATH
python --version
pip --version

# Si no funciona, reinstala Python y marca "Add Python to PATH" durante la instalación
```

**Linux:**
```bash
# Verifica
python3 --version
pip3 --version

# Si no funciona, instala:
sudo apt-get install python3-pip  # Ubuntu/Debian
sudo dnf install python3-pip       # Fedora
```

### Error: PowerShell execution policy (Windows)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\install.ps1
```

### Error: "Poppler no encontrado" o no puede convertir PDFs

**Windows:**
```powershell
pip install poppler-windows
```

**Linux - Ubuntu/Debian:**
```bash
sudo apt-get install poppler-utils
```

**Linux - Fedora/RHEL/CentOS:**
```bash
sudo dnf install poppler-utils
```

**Linux - Arch:**
```bash
sudo pacman -S poppler
```

### Error: "ModuleNotFoundError"

```bash
# Actualiza todas las dependencias
pip install --upgrade pdf2image Pillow PyPDF2

# O reinstala desde requirements.txt
pip install -r requirements.txt
```

### Error: Permiso denegado en Linux

```bash
# Asegúrate de que tienes permisos en el directorio
chmod -R u+w .

# Y en el script de instalación
chmod +x install.sh
./install.sh
```

---

## 🚀 Uso después de la instalación

### Windows (PowerShell)

```powershell
# Desde el escritorio: Haz doble clic en "PDF-Image Converter"

# O desde PowerShell:
pdf-converter --help
pdf-converter pdf-to-images documento.pdf --output salida
pdf-converter images-to-pdf --input carpeta --output documento.pdf
```

### Linux (Terminal)

```bash
# Desde terminal:
pdf-converter --help
pdf-converter pdf-to-images documento.pdf --output salida
pdf-converter images-to-pdf --input carpeta --output documento.pdf

# O usa el launcher:
./pdf-converter.sh
```

---

## 📝 Variables de entorno útiles

Puedes configurar:

```bash
# Directorio de datos personalizado
export PDF_CONVERTER_DATA_DIR=/ruta/personalizada

# Nivel de verbosidad
export PDF_CONVERTER_VERBOSE=1
```

---

## 🔄 Actualizar la librería

```bash
# Desde el repositorio clonado
pip install --upgrade -e .

# O desde PyPI
pip install --upgrade pdf-image-converter
```

---

## ❌ Desinstalar

```bash
# Windows y Linux
pip uninstall pdf-image-converter

# Si quieres limpiar también los datos
# Windows: Elimina %USERPROFILE%\.pdf-image-converter
# Linux: Elimina ~/.pdf-image-converter
```

---

## 📞 ¿Problemas?

- **Issues**: https://github.com/yourusername/pdf-image-converter/issues
- **Email**: tu.email@example.com
- **Documentación**: Ver README.md y QUICK_START.md

