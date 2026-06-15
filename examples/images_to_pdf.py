from pdf_image_converter import ImageConverter

converter = ImageConverter()
output = converter.images_to_pdf(["imagen1.png", "imagen2.jpg"], "documento.pdf")
print(f"PDF generado: {output}")
