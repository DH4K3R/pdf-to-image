@echo off
REM Launcher para PDF-Image Converter en Windows
REM Este archivo permite ejecutar la aplicación desde línea de comandos

setlocal enabledelayedexpansion

if "%1"=="" (
    pdf-converter --help
) else (
    pdf-converter %*
)

endlocal
