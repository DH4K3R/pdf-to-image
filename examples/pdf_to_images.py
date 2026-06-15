from pdf_image_converter import PDFConverter

pdf = PDFConverter("documento.pdf")
images = pdf.to_images("salida", fmt="png", dpi=200)
print(f"Convertidas {len(images)} imágenes")
