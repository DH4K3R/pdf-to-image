#!/bin/bash
# Script de Instalación para pdf-image-converter
# Uso: bash install.sh
# Plataformas soportadas: Linux (Ubuntu, Debian, Fedora, CentOS)

set -e

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;36m'
NC='\033[0m' # No Color

# Funciones
print_section() {
    echo ""
    echo -e "${BLUE}========================================"
    echo -e "$1"
    echo -e "========================================${NC}"
    echo ""
}

print_step() {
    echo -e "${YELLOW}[$1/$2] $3${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Detectar distribución Linux
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        echo "$ID"
    else
        echo "unknown"
    fi
}

# Instalar Poppler según la distribución
install_poppler() {
    DISTRO=$(detect_distro)
    
    case $DISTRO in
        ubuntu|debian)
            print_step "1" "6" "Instalando Poppler (Ubuntu/Debian)..."
            sudo apt-get update -qq
            sudo apt-get install -y poppler-utils > /dev/null 2>&1
            ;;
        fedora|rhel|centos)
            print_step "1" "6" "Instalando Poppler (Fedora/RHEL/CentOS)..."
            sudo dnf install -y poppler-utils > /dev/null 2>&1
            ;;
        arch)
            print_step "1" "6" "Instalando Poppler (Arch)..."
            sudo pacman -S --noconfirm poppler > /dev/null 2>&1
            ;;
        *)
            print_error "Distribución no reconocida. Instala 'poppler-utils' manualmente"
            return 1
            ;;
    esac
    print_success "Poppler instalado"
}

print_section "PDF-Image Converter - Instalación Automática"
echo -e "${BLUE}Plataforma: Linux${NC}"
echo ""

TOTAL_STEPS=6

# Paso 1: Verificar Python
print_step "1" "$TOTAL_STEPS" "Verificando Python..."
if ! command -v python3 &> /dev/null; then
    print_error "Python3 no está instalado"
    echo "Instala Python3 con: sudo apt install python3-pip"
    exit 1
fi
PYTHON_VERSION=$(python3 --version)
print_success "Python encontrado: $PYTHON_VERSION"

# Paso 2: Instalar Poppler
install_poppler || exit 1

# Paso 3: Actualizar pip
print_step "3" "$TOTAL_STEPS" "Actualizando pip..."
python3 -m pip install --upgrade pip --quiet 2>/dev/null || true
print_success "pip actualizado"

# Paso 4: Instalar dependencias
print_step "4" "$TOTAL_STEPS" "Instalando dependencias..."
pip3 install -q -r requirements.txt
if [ $? -ne 0 ]; then
    print_error "Falló la instalación de dependencias"
    exit 1
fi
print_success "Dependencias instaladas"

# Paso 5: Instalar la librería
print_step "5" "$TOTAL_STEPS" "Instalando pdf-image-converter..."
pip3 install -q -e .
if [ $? -ne 0 ]; then
    print_error "Falló la instalación de pdf-image-converter"
    exit 1
fi
print_success "pdf-image-converter instalado"

# Paso 6: Crear directorio de datos
print_step "6" "$TOTAL_STEPS" "Configurando directorios..."
mkdir -p "$HOME/.pdf-image-converter"
print_success "Directorio de datos creado: $HOME/.pdf-image-converter"

# Crear launcher
LAUNCHER_DIR="$HOME/.local/bin"
mkdir -p "$LAUNCHER_DIR"
cat > "$LAUNCHER_DIR/pdf-converter-gui" << 'LAUNCHER_EOF'
#!/bin/bash
# Launcher gráfico para PDF-Image Converter
python3 -m pdf_image_converter.cli "$@"
LAUNCHER_EOF
chmod +x "$LAUNCHER_DIR/pdf-converter-gui"

print_section "Instalación Completada" "Green"
echo -e "${BLUE}Verifica la instalación con:${NC}"
echo -e "  ${YELLOW}pdf-converter --help${NC}"
echo ""
echo -e "${BLUE}Próximos pasos:${NC}"
echo -e "  1. Ejecuta: ${YELLOW}pdf-converter --help${NC}"
echo -e "  2. Ver ejemplos: ${YELLOW}cat examples/usage_examples.py${NC}"
echo -e "  3. O desde Python: ${YELLOW}python3 -c \"from pdf_image_converter import PDFConverter\"${NC}"
echo ""
echo -e "${BLUE}Comandos útiles:${NC}"
echo -e "  ${YELLOW}pdf-converter pdf-to-images documento.pdf --output salida${NC}"
echo -e "  ${YELLOW}pdf-converter images-to-pdf --input carpeta --output documento.pdf${NC}"
echo ""
