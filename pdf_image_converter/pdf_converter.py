import os
from pathlib import Path
from typing import List, Optional
from pdf2image import convert_from_path


class PDFConverter:
    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"El archivo PDF no existe: {self.pdf_path}")

    def to_images(
        self,
        output_dir: str,
        fmt: str = "png",
        dpi: int = 150,
        pages: Optional[List[int]] = None,
    ) -> List[str]:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        convert_from_path_args = {
            "dpi": dpi,
            "fmt": fmt,
            "output_folder": str(output_dir),
            "paths_only": True,
        }

        if pages is not None:
            convert_from_path_args["first_page"] = min(pages)
            convert_from_path_args["last_page"] = max(pages)

        images = convert_from_path(str(self.pdf_path), **convert_from_path_args)
        return [str(Path(image).resolve()) for image in images]

    def page_to_image(
        self,
        page_number: int,
        output_path: str,
        dpi: int = 150,
        fmt: str = "png",
    ) -> str:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        images = convert_from_path(
            str(self.pdf_path),
            dpi=dpi,
            fmt=fmt,
            first_page=page_number,
            last_page=page_number,
            output_folder=str(output_path.parent),
            paths_only=True,
        )

        if not images:
            raise RuntimeError(f"No se pudo convertir la página {page_number}")

        result_path = Path(images[0])
        if result_path != output_path:
            result_path.rename(output_path)

        return str(output_path.resolve())

    def get_page_count(self) -> int:
        from PyPDF2 import PdfReader

        reader = PdfReader(str(self.pdf_path))
        return len(reader.pages)
