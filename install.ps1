# Script de Instalación para pdf-image-converter
# Uso: .\install.ps1
# Plataformas soportadas: Windows

param(
    [switch]$Silent = $false,
    [switch]$Dev = $false
)

function Write-Section {
    param([string]$Message, [string]$Color = "Cyan")
    Write-Host ""
    Write-Host "========================================" -ForegroundColor $Color
    Write-Host $Message -ForegroundColor $Color
    Write-Host "========================================" -ForegroundColor $Color
    Write-Host ""
}

function Write-Step {
    param([string]$Message, [int]$StepNumber, [int]$TotalSteps)
    Write-Host "[$StepNumber/$TotalSteps] $Message" -ForegroundColor Yellow
}

function Write-Success {
    param([string]$Message)
    Write-Host "✅ $Message" -ForegroundColor Green
}

function Write-Error-Custom {
    param([string]$Message)
    Write-Host "❌ $Message" -ForegroundColor Red
}

Write-Section "PDF-Image Converter - Instalación Automática" "Cyan"
Write-Host "Plataforma: Windows PowerShell" -ForegroundColor Magenta
Write-Host ""

$totalSteps = if ($Dev) { 8 } else { 7 }

# Paso 1: Verificar Python
Write-Step "Verificando Python..." 1 $totalSteps
$pythonCheck = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error-Custom "Python no está instalado o no está en PATH"
    Write-Host "Descarga desde: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}
Write-Success "Python encontrado: $pythonCheck"

# Paso 2: Verificar pip
Write-Step "Verificando pip..." 2 $totalSteps
$pipCheck = pip --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error-Custom "pip no está instalado"
    exit 1
}
Write-Success "pip encontrado: $pipCheck"

# Paso 3: Actualizar pip
Write-Step "Actualizando pip..." 3 $totalSteps
python -m pip install --upgrade pip --quiet
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  Advertencia: No se pudo actualizar pip" -ForegroundColor Yellow
} else {
    Write-Success "pip actualizado"
}

# Paso 4: Instalar dependencias principales
Write-Step "Instalando dependencias..." 4 $totalSteps
pip install -q -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Error-Custom "Falló la instalación de dependencias"
    exit 1
}
Write-Success "Dependencias instaladas"

# Paso 5: Instalar dependencias de desarrollo (opcional)
if ($Dev) {
    Write-Step "Instalando dependencias de desarrollo..." 5 $totalSteps
    pip install -q -r requirements-dev.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "⚠️  Advertencia: No se pudieron instalar dependencias de desarrollo" -ForegroundColor Yellow
    } else {
        Write-Success "Dependencias de desarrollo instaladas"
    }
    $stepOffset = 1
} else {
    $stepOffset = 0
}

# Paso 6: Instalar la librería
Write-Step "Instalando pdf-image-converter..." (5 + $stepOffset) $totalSteps
pip install -q -e .
if ($LASTEXITCODE -ne 0) {
    Write-Error-Custom "Falló la instalación de pdf-image-converter"
    exit 1
}
Write-Success "pdf-image-converter instalado"

# Paso 7: Crear directorio de datos
Write-Step "Configurando directorios..." (6 + $stepOffset) $totalSteps
$dataDir = "$env:USERPROFILE\.pdf-image-converter"
New-Item -ItemType Directory -Path $dataDir -Force | Out-Null
Write-Success "Directorio de datos creado: $dataDir"

# Paso 8: Crear acceso directo (solo si no es modo silencioso)
Write-Step "Creando acceso directo..." (7 + $stepOffset) $totalSteps
$desktopPath = [System.IO.Path]::Combine([System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::Desktop), "PDF-Image Converter.lnk")
$shellLink = New-Object -ComObject WScript.Shell
$link = $shellLink.CreateShortcut($desktopPath)
$link.TargetPath = "cmd.exe"
$link.Arguments = "/k pdf-converter --help"
$link.WorkingDirectory = $env:USERPROFILE
$link.Description = "PDF-Image Converter - Convierte PDF a Imágenes e Imágenes a PDF"
$link.IconLocation = "C:\Windows\System32\notepad.exe"
$link.Save()
Write-Success "Acceso directo creado en el escritorio"

# Paso final: Verificación
Write-Section "Instalación Completada" "Green"
Write-Host "Verifica la instalación con:" -ForegroundColor Cyan
Write-Host "  pdf-converter --help" -ForegroundColor White
Write-Host ""
Write-Host "Próximos pasos:" -ForegroundColor Cyan
Write-Host "  1. Abre 'PDF-Image Converter' desde el escritorio" -ForegroundColor White
Write-Host "  2. O ejecuta en PowerShell: pdf-converter --help" -ForegroundColor White
Write-Host "  3. Ver ejemplos: examples\usage_examples.py" -ForegroundColor White
Write-Host ""
Write-Host "Comandos útiles:" -ForegroundColor Cyan
Write-Host "  pdf-converter pdf-to-images documento.pdf --output salida" -ForegroundColor White
Write-Host "  pdf-converter images-to-pdf --input carpeta --output documento.pdf" -ForegroundColor White
Write-Host ""
