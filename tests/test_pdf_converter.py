import tempfile
from pathlib import Path
from pdf_image_converter.pdf_converter import PDFConverter


def test_pdf_converter_init_file_not_found():
    try:
        PDFConverter("noexiste.pdf")
        assert False, "Debería lanzar FileNotFoundError"
    except FileNotFoundError:
        assert True


def test_pdf_converter_to_images_invalid_path():
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = Path(tmpdir) / "dummy.pdf"
        pdf_path.write_text("%PDF-1.4\n%...\n")
        converter = PDFConverter(str(pdf_path))
        try:
            converter.to_images(str(Path(tmpdir) / "salida"))
        except Exception as e:
            assert "No se pudo" in str(e) or isinstance(e, RuntimeError)
