import tempfile
from pathlib import Path
from pdf_image_converter.image_converter import ImageConverter
from pdf_image_converter.pdf_converter import PDFConverter
from PIL import Image


def test_integration_image_to_pdf_and_pdf_to_images():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        image_path = tmpdir_path / "test.png"
        Image.new("RGB", (10, 10), color="white").save(image_path)

        pdf_path = tmpdir_path / "output.pdf"
        converter = ImageConverter()
        converter.image_to_pdf(str(image_path), str(pdf_path))

        pdf_converter = PDFConverter(str(pdf_path))
        result = pdf_converter.to_images(str(tmpdir_path / "images"), fmt="png")
        assert len(result) >= 1
        assert Path(result[0]).exists()
