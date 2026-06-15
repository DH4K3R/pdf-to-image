import tempfile
from pathlib import Path
from pdf_image_converter.image_converter import ImageConverter
from PIL import Image


def test_image_to_pdf_missing_file():
    converter = ImageConverter()
    try:
        converter.image_to_pdf("noexiste.png", "out.pdf")
        assert False, "Debería lanzar FileNotFoundError"
    except FileNotFoundError:
        assert True


def test_images_to_pdf_empty_list():
    converter = ImageConverter()
    try:
        converter.images_to_pdf([], "out.pdf")
        assert False, "Debería lanzar ValueError"
    except ValueError:
        assert True


def test_image_to_pdf_success():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "test.png"
        Image.new("RGB", (10, 10), color="white").save(path)
        output = Path(tmpdir) / "out.pdf"
        converter = ImageConverter()
        result = converter.image_to_pdf(str(path), str(output))
        assert Path(result).exists()
