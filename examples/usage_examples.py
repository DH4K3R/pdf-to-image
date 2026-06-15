from pdf_image_converter import PDFConverter, ImageConverter

# Convertir PDF a imágenes
pdf = PDFConverter("documento.pdf")
imagenes = pdf.to_images("salida", fmt="png", dpi=200)
print(f"Convertidas {len(imagenes)} imágenes")

# Convertir una sola imagen a PDF
converter = ImageConverter()
output_pdf = converter.image_to_pdf("imagen.png", "documento.pdf")
print(f"PDF generado: {output_pdf}")
