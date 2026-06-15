#!/bin/bash
# Launcher para PDF-Image Converter en Linux
# Ejecuta: chmod +x pdf-converter.sh && ./pdf-converter.sh

if [ $# -eq 0 ]; then
    pdf-converter --help
else
    pdf-converter "$@"
fi
