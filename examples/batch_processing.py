from pdf_image_converter import ImageConverter
from pathlib import Path

input_dir = Path("imagenes")
output_pdf = Path("salida.pdf")
image_files = sorted(str(path) for path in input_dir.glob("*.png"))

converter = ImageConverter()
converter.images_to_pdf(image_files, str(output_pdf))
print(f"PDF generado: {output_pdf}")
